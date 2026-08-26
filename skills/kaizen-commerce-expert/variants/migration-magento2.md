# Migration Execution Variant — Magento 2 Source

Load when the source is Magento 2 / Adobe Commerce. This is an ecommerce-platform migration
(usually with `variants/ecommerce-to-shopify.md` co-loaded) — POS is rarely the lead entity;
catalog complexity and URL equity are.

## Entity Inventory

| Entity | Source | Watch |
|---|---|---|
| Catalog (simple/configurable/bundle/grouped/virtual) | REST/GraphQL API, admin export | product-type mapping is the project |
| Customers + addresses | API/export | password hashes do NOT migrate — account reactivation flow required |
| Customer groups / tier prices | API | maps to Shopify B2B price lists or tags+discounts — architecture decision |
| Orders | API | importable history per recipe R5 constraints |
| Categories | API | tree → collections strategy |
| CMS pages/blocks | API | content migration is its own workstream — scope explicitly |
| URL rewrites | rewrite table export | THE SEO asset — 301 map source |
| Attributes/EAV | attribute sets | metafield definitions plan |

## Data Traps

- **Product type mapping:** configurable→product+variants (clean); bundle/grouped have NO native
  Shopify equivalent — per-case decision (components as standalone + manual merchandising, a
  bundle app, or fixed-kit SKUs) `[VERIFY merchant's actual bundle semantics]`.
- **EAV attribute sprawl:** years of attributes, many dead. Audit usage counts in Phase 1;
  migrate only attributes with storefront or operational function — the rest is data hoarding.
- **Customer passwords:** unmigratable. Plan the account-invite flow and its CX messaging as a
  runbook line item, not a surprise.
- **Tier/group pricing:** if wholesale is real, this is a B2B architecture decision
  (`variants/shopify-b2b-commerce.md`), not a field map.
- **URL equity:** rewrite-table export → 301 map → validated pre-go-live crawl (propose §8
  Technical SEO scope). Magento URL structures are deep; missing this bleeds organic traffic.
- **Layered config:** store views / websites multiply everything — confirm which store views are
  actually live before scoping by raw counts.

## Field Mapping (anchors)

| Magento 2 | Shopify | Note |
|---|---|---|
| entity_id / sku | metafield `migration.source_id` / variant sku | sku is the natural key — verify uniqueness |
| configurable attributes | options 1-3 | >3 attributes needs a flattening decision |
| special_price + dates | price (+ scheduled change decision) | scheduling differs `[VERIFY need]` |
| meta_title/meta_description | SEO fields | |
| url_key + rewrites | handle + 301 map | |

## Validation Queries
Recipe bank R8 counts per store view in scope; category↔collection spot-check; 301 map sampled
against live crawl; order totals sampled against Magento order grid sums.

## Rollback Notes
Magento stays live until cutover sign-off (DNS-level rollback is real here — document TTLs).
Shopify-side ledger per R2; never bulk-delete during a live traffic window.

## Variant Depth Additions
Phase 2 (mapping) and the SEO workstream dominate; budget EAV audit time explicitly. Bundles and
B2B pricing are the two scope-explosion risks — both get kill-condition language in §9.

## Anti-Selection Rules
Magento 1 / OpenMage → same shape but worse exports; flag the difference, don't assume M2 docs
apply `[VERIFY everything]`. Adobe Commerce Cloud B2B suites with punchout/ERP → architecture
engagement first, not a migration runbook.

## Known Failure Modes
Bundle semantics discovered at import; dead attributes migrated wholesale; 301 map built from
current URLs only (missing legacy rewrite chains); store-view double counting.

## Default Evidence Gates
Live store-view inventory confirmed; bundle/grouped product decision signed before Phase 3;
pre-go-live crawl with zero unmapped indexed URLs.

## Operating Hooks
Vendor freshness: Shopify B2B capabilities move fast — verify current state via Shopify Dev MCP
when tier pricing is in scope. Flywheel: Magento findings to this variant at Close Client.

## Output Shape By Mode
9-phase runbook + SEO supplement; lane `api_to_api` for catalog/customers, R5 constraints govern
order history; CMS content as an explicit separate workstream.

## Source-Of-Truth
Lane + contract: `skills/kaizen-migrate.md` · recipes: `reference/kaizen-api-recipe-bank.md` ·
ecom patterns: `variants/ecommerce-to-shopify.md` · B2B: `variants/shopify-b2b-commerce.md` ·
QA verdicts: `delivery-os/templates/migration-qa-evidence-pack.md`
