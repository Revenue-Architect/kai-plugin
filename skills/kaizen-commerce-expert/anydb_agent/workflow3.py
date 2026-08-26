#!/usr/bin/env python3
"""
Workflow 3: deal_brief.json → AnyDB (Merchant + Contact + Deal).

Reads a deal_brief.json produced by `kaizen_discovery_parser.py` (Workflow 2)
and creates matching records in AnyDB via the typed AnyDBClient. Because
LangExtract doesn't always fill every field, CLI flags let you supply what
the parser missed (or override what it got wrong).

Flow:
    1. Load and dedupe the brief
    2. Build a Merchant model (CLI overrides > brief values > None)
    3. Dry-run? Print the three payloads and exit.
    4. Create Merchant → read adoid
    5. Create Contact (if we have a name) with company=RefValue(merchant_id)
    6. Create Deal with merchant_account + primary_contact refs

Usage:
    export ANYDB_DEFAULT_API_KEY=...

    # Dry run — print what would be sent, no writes
    python3.11 workflow3.py --input deal_brief.json --dry-run \\
        --merchant-name "Quai du Vin"

    # Real run
    python3.11 workflow3.py --input deal_brief.json \\
        --merchant-name "Quai du Vin" \\
        --contact-name "Marcus Chen" \\
        --contact-email marcus@quaiduvin.com \\
        --contact-title "COO"
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Optional

from agent import AnyDBClient
from models import (
    Contact,
    ContactRole,
    Deal,
    DealPackageTier,
    DealSalesStage,
    DealType,
    Merchant,
    MerchantClientStatus,
    MerchantIndustry,
    MerchantLegacyPOS,
    RefValue,
)


# ---------- brief parsing ----------


def load_brief(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return json.load(f)


def _dedupe(items: list[Any] | None) -> list[Any]:
    """Multi-pass LangExtract often duplicates list values. Strip blanks + dupes."""
    if not items:
        return []
    seen: list[Any] = []
    for x in items:
        if x in (None, "", [], {}):
            continue
        if x not in seen:
            seen.append(x)
    return seen


def _first(items: list[Any] | None) -> Optional[Any]:
    cleaned = _dedupe(items)
    return cleaned[0] if cleaned else None


def _map_legacy_pos(raw: Optional[str]) -> Optional[MerchantLegacyPOS]:
    """Fuzzy-map free-form POS names to the Merchant enum."""
    if not raw:
        return None
    s = raw.lower()
    if "lightspeed" in s:
        return MerchantLegacyPOS.LIGHTSPEED
    if "square" in s:
        return MerchantLegacyPOS.SQUARE
    if "heartland" in s:
        return MerchantLegacyPOS.HEARTLAND
    if "shopify" in s:
        return MerchantLegacyPOS.SHOPIFY_UPGRADE
    if "vend" in s:
        return MerchantLegacyPOS.VEND
    return MerchantLegacyPOS.OTHER  # NetSuite POS, Revel, Clover, etc.


def _map_tier(raw: Optional[str]) -> Optional[DealPackageTier]:
    if not raw:
        return None
    s = raw.lower()
    if "silver" in s:
        return DealPackageTier.SILVER
    if "gold" in s:
        return DealPackageTier.GOLD
    if "diamond" in s:
        return DealPackageTier.DIAMOND
    return DealPackageTier.CUSTOM


def _map_industry(raw: Optional[str]) -> Optional[MerchantIndustry]:
    if not raw:
        return None
    s = raw.lower()
    for keyword, tag in [
        ("fashion", MerchantIndustry.FASHION),
        ("apparel", MerchantIndustry.FASHION),
        ("food", MerchantIndustry.FOOD_BEVERAGE),
        ("beverage", MerchantIndustry.FOOD_BEVERAGE),
        ("wine", MerchantIndustry.FOOD_BEVERAGE),
        ("restaurant", MerchantIndustry.FOOD_BEVERAGE),
        ("home", MerchantIndustry.HOME_GOODS),
        ("health", MerchantIndustry.HEALTH_BEAUTY),
        ("beauty", MerchantIndustry.HEALTH_BEAUTY),
        ("sport", MerchantIndustry.SPORTING_GOODS),
        ("retail", MerchantIndustry.RETAIL),
    ]:
        if keyword in s:
            return tag
    return MerchantIndustry.OTHER


def _build_notes(brief: dict[str, Any]) -> Optional[str]:
    """Roll the free-text intel from the brief into a single Notes block."""
    parts: list[str] = []
    pain = brief.get("pain") or {}
    for label, key in [
        ("Data fragmentation", "data_fragmentation"),
        ("Timeline driver", "timeline_driver"),
        ("Primary pain", "primary"),
        ("Secondary pain", "secondary"),
        ("Prior migration", "prior_migration"),
    ]:
        v = pain.get(key)
        if v:
            parts.append(f"<p><strong>{label}:</strong> {v}</p>")

    stack = brief.get("stack") or {}
    integrations = _dedupe(stack.get("integrations"))
    if integrations:
        parts.append(
            "<p><strong>Integrations:</strong> " + "; ".join(integrations) + "</p>"
        )

    flags = brief.get("scope_flags") or []
    if flags:
        bullets = "".join(
            f"<li>{f.get('flag', '')}: {f.get('note', '')}</li>" for f in flags
        )
        parts.append(f"<p><strong>Scope flags:</strong></p><ul>{bullets}</ul>")

    new_locs = (brief.get("merchant") or {}).get("new_locations_planned")
    if new_locs:
        parts.append(f"<p><strong>New locations planned:</strong> {new_locs}</p>")

    return "\n".join(parts) if parts else None


# ---------- model construction ----------


def build_merchant(brief: dict[str, Any], args: argparse.Namespace) -> Merchant:
    m = brief.get("merchant") or {}
    stack = brief.get("stack") or {}

    name = args.merchant_name or m.get("name")
    if not name:
        sys.exit(
            "ERROR: merchant.name is null in the brief and no --merchant-name supplied.\n"
            "       Run with --merchant-name 'Company Name' to override."
        )

    return Merchant(
        company_name=name,
        legacy_pos=_map_legacy_pos(args.legacy_pos or _first(stack.get("current_pos"))),
        notes=_build_notes(brief),
        client_status=MerchantClientStatus.PROSPECT,
        industry=_map_industry(args.industry or m.get("vertical")),
        website=args.website or m.get("website"),
        num_locations=m.get("location_count"),
    )


def build_contact(
    brief: dict[str, Any],
    args: argparse.Namespace,
    merchant_adoid: str,
) -> Optional[Contact]:
    m = brief.get("merchant") or {}
    name = args.contact_name or m.get("decision_maker")
    if not name:
        return None  # no contact info — skip

    return Contact(
        full_name=name,
        email=args.contact_email,
        phone=args.contact_phone,
        job_title=args.contact_title,
        linkedin=args.contact_linkedin,
        role=ContactRole.DECISION_MAKER,
        primary_contact=True,
        company=RefValue(adoid=merchant_adoid),
    )


def build_deal(
    brief: dict[str, Any],
    args: argparse.Namespace,
    merchant_adoid: str,
    contact_adoid: Optional[str],
    merchant_name: str,
) -> tuple[str, Deal]:
    pricing = brief.get("pricing") or {}
    deal_name = args.deal_name or f"{merchant_name} — POS Migration"

    deal = Deal(
        deal_name=deal_name,
        sales_stage=DealSalesStage.DISCOVERY,
        deal_type=DealType.NEW_CLIENT,
        package_tier=_map_tier(args.tier or pricing.get("tier")),
        blueprint_booked=bool(pricing.get("blueprint_fee")),
        deal_value=float(pricing["implementation_fee"])
        if pricing.get("implementation_fee") is not None
        else None,
        merchant_account=RefValue(adoid=merchant_adoid),
        primary_contact=RefValue(adoid=contact_adoid) if contact_adoid else None,
    )
    return deal_name, deal


# ---------- driver ----------


def _print_payload(label: str, record: Any) -> None:
    print(f"\n--- {label} ---")
    print(json.dumps(record.model_dump(exclude_none=True), indent=2, ensure_ascii=False))
    print("content dict:")
    print(json.dumps(record.to_content_payload(), indent=2, ensure_ascii=False))


async def run(args: argparse.Namespace) -> int:
    brief = load_brief(Path(args.input))
    print(f"Loaded brief from {args.input}")
    print(f"  generated_date: {brief.get('generated_date')}")

    # ---- Merchant (always) ----
    merchant = build_merchant(brief, args)
    merchant_name = merchant.company_name or ""
    print(f"\nMerchant: {merchant_name}")

    if args.dry_run:
        _print_payload("MERCHANT (dry-run)", merchant)
        # Build the rest using placeholder IDs so the user sees the full shape
        placeholder_mid = "<new-merchant-adoid>"
        contact = build_contact(brief, args, placeholder_mid)
        if contact:
            _print_payload("CONTACT (dry-run)", contact)
        placeholder_cid = "<new-contact-adoid>" if contact else None
        _, deal = build_deal(brief, args, placeholder_mid, placeholder_cid, merchant_name)
        _print_payload("DEAL (dry-run)", deal)
        print("\n[dry-run] no records written.")
        return 0

    async with AnyDBClient() as db:
        # ---- 1. Merchant ----
        res = await db.create(merchant, templatename="Merchants", name=merchant_name)
        merchant_adoid = _extract_adoid(res)
        if not merchant_adoid:
            print("ERROR: create_record returned no adoid for Merchant:", res)
            return 1
        print(f"  ✓ Merchant created: {merchant_adoid}")

        # ---- 2. Contact (optional) ----
        contact = build_contact(brief, args, merchant_adoid)
        contact_adoid: Optional[str] = None
        if contact:
            cres = await db.create(
                contact,
                templatename="Contacts",
                name=contact.full_name or "Unnamed Contact",
                attach=merchant_adoid,
            )
            contact_adoid = _extract_adoid(cres)
            if contact_adoid:
                print(f"  ✓ Contact created: {contact_adoid} ({contact.full_name})")
            else:
                print("  ! Contact create returned no adoid:", cres)
        else:
            print("  - no contact info in brief; skipping Contact")

        # ---- 3. Deal ----
        deal_name, deal = build_deal(
            brief, args, merchant_adoid, contact_adoid, merchant_name
        )
        dres = await db.create(deal, templatename="Deals", name=deal_name)
        deal_adoid = _extract_adoid(dres)
        if deal_adoid:
            print(f"  ✓ Deal created: {deal_adoid} ({deal_name})")
        else:
            print("  ! Deal create returned no adoid:", dres)

    print("\nDone.")
    return 0


def _extract_adoid(res: Any) -> Optional[str]:
    if not isinstance(res, dict):
        return None
    if res.get("adoid"):
        return res["adoid"]
    meta = res.get("meta") or {}
    if meta.get("adoid"):
        return meta["adoid"]
    # Some MCP responses wrap the new record under different keys
    for key in ("record", "item", "created"):
        inner = res.get(key)
        if isinstance(inner, dict):
            if inner.get("adoid"):
                return inner["adoid"]
            im = inner.get("meta") or {}
            if im.get("adoid"):
                return im["adoid"]
    return None


# ---------- CLI ----------


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Create Merchant + Contact + Deal in AnyDB from a deal_brief.json",
    )
    p.add_argument("--input", "-i", required=True, help="Path to deal_brief.json")
    p.add_argument("--dry-run", action="store_true", help="Print payloads, don't write")

    # Merchant overrides
    p.add_argument("--merchant-name", help="Override merchant.name (required if null in brief)")
    p.add_argument("--legacy-pos", help="Override current POS (e.g. 'Lightspeed')")
    p.add_argument("--industry", help="Override merchant.vertical")
    p.add_argument("--website", help="Override merchant.website")

    # Contact overrides / supplements
    p.add_argument("--contact-name", help="Full name of primary contact")
    p.add_argument("--contact-email", help="Primary contact email")
    p.add_argument("--contact-phone", help="Primary contact phone")
    p.add_argument("--contact-title", help="Primary contact job title")
    p.add_argument("--contact-linkedin", help="Primary contact LinkedIn URL")

    # Deal overrides
    p.add_argument("--deal-name", help="Override auto-generated deal name")
    p.add_argument("--tier", help="Override pricing.tier (Silver / Gold / Diamond / Custom)")

    return p.parse_args()


def main() -> int:
    return asyncio.run(run(parse_args()))


if __name__ == "__main__":
    sys.exit(main())
