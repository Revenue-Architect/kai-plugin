# Vertical Playbook — Jewelry Multi-Location

Use this variant for jewelry retailers with 2+ locations: fine jewelry, watches, custom work,
repairs. Loads on top of the matching scenario variant (usually pos-migration).

**Provenance:** patterns below are `[SYN]` domain knowledge until the seeding session lands
`[REAL:PJ-2026]` entries from the Paris Jewellers engagement (capture slots below).

## Required Context

- Serialized vs non-serialized mix (fine pieces vs fashion/accessories)
- Repairs and custom-order volume; how they're tracked today (the notebook test)
- Consignment and memo inventory presence (vendor-owned stock on the floor)
- Appraisal/certification document handling (GIA certs etc.)
- Insurance requirements tied to inventory records

## Default Skill Chain

1. `skills/kaizen-qualify.md` — discovery with the angles below
2. `skills/kaizen-diagnose.md` — Blueprint; repairs/custom workflows usually drive the AnyDB story
3. `skills/kaizen-architect.md` — when repairs/custom-order state needs an operating layer
4. `skills/kaizen-migrate.md` — serial integrity is the migration headline risk

## Vertical Pattern Library [SYN]

- **Serial integrity is the migration:** each serialized piece is a unit of one with its own cost,
  cert, and location. Count parity is necessary but not sufficient — serial-level reconciliation
  is the QA bar.
- **Repairs are a workflow business hiding inside a retail business:** intake → estimate →
  approval → bench → QC → notify → pickup, with customer property liability throughout. This is
  workflow state (AnyDB candidate), not a POS feature.
- **Custom orders carry deposits:** deposit liability + milestone communication; ties to the
  special-orders pattern.
- **High-value, low-velocity inventory:** stockouts aren't the pain — trust, location accuracy,
  and shrink visibility are. Lead diagnosis with "can you trust where every piece is right now?"
- **Memo/consignment stock:** vendor-owned pieces must not enter owned-inventory valuation;
  classic migration contamination trap.

## Discovery Angles

- "Walk me through a repair from drop-off to pickup — where does that live today?"
- "If a piece moves between stores for a customer viewing, who knows, and how?"
- "What happens to the cert when a serialized piece sells?"
- "How much of the floor is memo stock, and how is it flagged at the register?"

## Data Traps

- Serial numbers stored in free-text fields or SKU suffixes — mapping landmine
- Metal-price-driven cost updates (cost history vs current replacement cost)
- Deposits on custom work recorded as sales rather than liabilities
- Trade-ins and store credit conventions with no system representation
- Repair items that are *customer property*, not inventory — must never migrate as stock

## Evidence Capture Slots (seeded 2026-06-10; all `proposal-safe: no`, internal only)

`[REAL:PJ-2026]` Ecom-first, POS-later sequencing (2026-05-07 discovery, 23-location jewelry
retailer, confidence high): ScanPoint POS + WooCommerce; merchant chose ecommerce-first Shopify
migration with POS-later sequencing. Drivers: slow Woo storefront, plugin/cache maintenance
friction, limited uploads/exports, ecom inventory manually updated and disconnected from POS.
Applies when ecom pain outruns POS pain in multi-location specialty retail — sequence ecom
first and keep the POS path open in the architecture.

`[REAL:PJ-2026]` Data continuity is deal-shaping before proposal (2026-05-07/12, confidence
high): customer history, gift cards/store credit, and account continuity named by the merchant
as must-survive items before any tier discussion; ~10K products with a likely 2–3K active
launch subset, ~25K customer records needing cleanup, some product data living only in the POS.
Open gates at capture: gift-card plugin unknown, ScanPoint export sample pending, accounting
system unconfirmed.

`[REAL:PJ-2026]` Peak-season cutover window + incumbent competitor (2026-05-12, confidence
high for timeline / medium for budget signals): July ideal launch, September hard stop before
peak — jewelry trades on Q4, so the cutover window is seasonal, not arbitrary. A competitor
(built the sister brand's site) was already in the account. Budget signals exist in an internal
prep note only — `[VERIFY before any client-facing use]`.

Still pending (do not invent): repairs/custom-order workflow decision · migration trap actually
encountered (engagement has not reached delivery).

## Variant Depth Additions

- Tier discipline: location count says Silver/Gold, but serialized + repairs + consignment
  complexity is exactly the "complexity ≠ Diamond" test — scope the workstreams, don't inflate
  the tier.
- The repairs workflow is frequently the wedge that wins the deal: nobody else maps it.

## Anti-Selection Rules

- Single-location jeweler without repairs/custom volume → standard retail handling.
- Pure e-commerce jewelry brand (no stores) → `variants/shopify-dtc-commerce.md` instead.

## Known Failure Modes

- Running a count-parity-only migration QA on serialized stock.
- Letting memo stock into owned-inventory valuation.
- Promising repairs functionality as a POS feature instead of scoping the operating layer.

## Default Evidence Gates

- No proposal-safe jewelry proof exists until the session lands it; pattern language only.
- Platform capability claims (serialized inventory handling) per vendor-freshness protocol.

## Operating Hooks

- Memory: record serialization share, repairs volume, consignment presence on first discovery.
- Flywheel: capture slots above at `Close Client`; corrections to these patterns retire the
  matching `[SYN]` lines.

## Output Shape By Mode

- Quick Read: fit + the inventory-trust framing.
- Client Deliverable: Blueprint §3b leads with repairs/custom workflow map; §6 separates POS
  migration from workflow layer phases.
- Execution Artifact: migration runbook adds serial-level reconciliation to Phase 5 and a memo-
  stock exclusion rule to Phase 2.

## Source-Of-Truth

- Migration QA: `skills/kaizen-migrate.md` QA gate · Evidence:
  `reference/kaizen-proposal-proof-bank.md` schema · Retail ops patterns:
  `reference/kaizen-retail-ops-patterns.md` · Pricing: `reference/kaizen-pricing.md`
