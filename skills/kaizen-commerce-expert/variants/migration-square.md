# Migration Execution Variant — Square Source

Load when the source platform is Square (Square for Retail / Square POS). Co-loads with the
lane variant per `skills/kaizen-migrate.md` precedence. Platform claims below are stable
structural knowledge; anything marked `[VERIFY]` must be confirmed against the merchant's
actual export before the runbook is execution-ready.

## Entity Inventory (what exists in Square and where it exports from)

| Entity | Source | Export path | Watch |
|---|---|---|---|
| Items/variations | Square Catalog | Dashboard export CSV / Catalog API | variations flatten oddly in CSV; API preserves structure |
| Customers | Square Directory | Dashboard export / Customers API | profiles are thin: email OR phone often missing |
| Inventory by location | Square for Retail | Inventory API / per-location CSV | plain Square (non-Retail) has weaker location granularity `[VERIFY which product]` |
| Gift cards + balances | Square Gift Cards | **no self-serve balance export** — request from Square support or Gift Cards API `[VERIFY access]` | THE high-risk entity |
| Orders/transactions | Square Transactions | CSV export windows / Orders API | itemization quality varies by era of the account |
| Loyalty | Square Loyalty | API only `[VERIFY]` | points→Shopify needs a mapping decision, not a copy |

## Data Traps

- **Variation flattening:** Square "items with variations" export as repeated rows; SKU may live
  on the variation only. Map item→product, variation→variant explicitly; never trust row order.
- **Customer identity sparseness:** heavy duplicate risk on import (R3 dedupe gate) because
  Square allows email-less, phone-less profiles created at the register.
- **Gift card balance access:** plan the support-request lead time in the runbook timeline;
  balances change daily while legacy stays live — re-export at cutover freeze, tie out to the
  cent (recipe R6).
- **Category ≠ collection:** Square categories are flat; decide Shopify collection strategy
  (manual vs automated by tag) before mapping.
- **Tax mismatch:** Square tax tables are location-scoped settings, not data to migrate —
  rebuild in Shopify per location, verify with test transactions per location.
- **Modifiers:** Square modifiers have no clean Shopify equivalent — decide per case: variant
  explosion, line-item properties, or app `[VERIFY merchant usage first]`.

## Field Mapping (anchor rows — full map built per merchant, exact names verified per MCP protocol)

| Square | Shopify | Note |
|---|---|---|
| Item Name / Variation Name | product title / variant option | option naming decision needed |
| SKU (variation) | variant sku | blank SKUs common — generate + flag |
| Price | variant price | Square exports cents in API, dollars in CSV — normalize `[VERIFY export type]` |
| GTIN | barcode | |
| Reference ID | metafield `migration.source_id` | idempotency + audit key |

## Validation Queries

Recipe bank R8 counts + R6 gift card sum vs the Square export baseline captured in Phase 1.
Spot-check sample: 20 products across categories, 10 customers with history, every gift card
batch's running total.

## Rollback Notes

Square remains the source of truth through parallel validation until Shopify is proven.
Shopify-side created-resource ledger from the JSONL files (R2); gift cards
deactivate-not-delete; inventory pre-import snapshot per location before R4 runs.

## Variant Depth Additions
Square-specific runbook deltas concentrate in Phase 1 (export completeness — especially gift
cards) and Phase 2 (variation reconstruction). Budget a Square support-ticket lead time line item.

Real execution evidence (`proposal-safe: no`, internal): `[REAL:SGP-2026]` — Square→Shopify run
on the Matrixify lane with `custom.square_id` source-ID metafields and >10,500 customers in
bounded ~1,500-row transfer packages (full entry: proof bank). Hard lesson from the same job:
the source-data walkthrough happened AFTER commitment and the cleanup mess surfaced
mid-delivery — the Phase-1 export audit is a discovery-stage gate, not a kickoff task (finding
bank, "Catalog Data Debt" real instances).

## Anti-Selection Rules
Square for Restaurants → not our lane. Square Online (Weebly) stores migrating web only → use
`variants/ecommerce-to-shopify.md` instead, this variant covers the POS/retail entity set.

## Known Failure Modes
Trusting CSV variation rows; importing register-created duplicate customers; gift card sum
checked at export time but not re-frozen at cutover; modifiers discovered during import week.

## Default Evidence Gates
No live import without R5/R6 dry-run on a dev store; gift card tie-out to the cent; every
`[VERIFY]` in this file resolved or escalated before the runbook is marked execution-ready.

## Operating Hooks
Vendor freshness: Square export formats drift — verify against a fresh sample export every
engagement, never against a previous client's files. Flywheel: capture Square-specific surprises
to this variant at Close Client.

## Output Shape By Mode
Runbook per `skills/kaizen-migrate.md` 9-phase contract with this variant's traps merged into
Phases 1-2-5; lane decision usually `api_to_api` primary with `matrixify_csv` fallback.

## Source-Of-Truth
Lane + contract: `skills/kaizen-migrate.md` · recipes: `reference/kaizen-api-recipe-bank.md` ·
QA verdicts: `delivery-os/templates/migration-qa-evidence-pack.md` · MCP rules:
`reference/kaizen-mcp-protocols.md`
