# Migration Execution Variant — WooCommerce Source

Load when the source is WooCommerce. The defining reality: Woo is WordPress — data quality is a
function of the plugin stack, not the platform. Phase 1 is a plugin census before it is an
export.

## Entity Inventory

| Entity | Source | Watch |
|---|---|---|
| Products (simple/variable/grouped/external) | REST API, WP export, DB | variable→variants clean; grouped/external need decisions |
| Customers | REST API / users table | guest checkouts are orders without accounts — decide identity stitching |
| Orders | REST API | status taxonomy may be plugin-customized `[VERIFY statuses]` |
| Coupons | REST API | recreate strategy, not data migration |
| Subscriptions (WooCommerce Subscriptions) | plugin tables | CRITICAL: payment tokens are gateway-held — subscription migration is a gateway conversation, not an export `[VERIFY gateway + processor portability]` |
| Bookings/memberships/custom plugins | plugin tables | per-plugin decision; never assume exportable |
| SEO (Yoast/RankMath) | plugin meta | meta + redirects into the 301 workstream |

## Data Traps

- **Plugin-defined truth:** attributes, statuses, and even prices can live in plugin meta.
  The plugin census (active plugins touching catalog/checkout/orders) is a Phase-1 deliverable
  and the scope document.
- **Subscriptions:** tokenized payment methods belong to the gateway. Portability depends on the
  processor relationship (Stripe token export vs locked) — lead time + customer re-authorization
  fallback plan; this can be the whole project's critical path.
- **Variable product attribute sprawl:** global vs per-product attributes mix; normalize to ≤3
  options or decide a flattening strategy.
- **Guest order identity:** orders with no account → customer stitching by email decision
  (create customers vs import as guest) before R3/R5 sequencing.
- **Stock honesty:** Woo stock fields are often decorative (no enforcement culture) — treat
  counts as suspect; physical count or merchant attestation for opening counts.
- **Tax history:** imported orders carry captured amounts (R5) — never re-derive from current
  tax settings.

## Field Mapping (anchors)

| WooCommerce | Shopify | Note |
|---|---|---|
| post ID / _sku | metafield `migration.source_id` / sku | sku gaps common — generate + flag |
| variation attributes | options | normalize value map |
| _regular_price / _sale_price | compare_at_price / price | confirm semantic with merchant |
| order status (incl. custom) | financial/fulfillment status map | document the status map explicitly |
| Yoast/RankMath meta | SEO fields + 301 map | |

## Validation Queries
Recipe bank R8; order sampling vs WooCommerce reports totals for the same window; subscription
inventory (count + MRR sum) reconciled with gateway records `[VERIFY both sides]`.

## Rollback Notes
WP site stays live until DNS cutover; document TTLs. Shopify ledger per R2. Subscriptions:
NEVER cancel gateway-side until Shopify-side billing is confirmed live — double-billing and
no-billing are both unacceptable; the runbook needs an explicit subscription cutover gate.

## Variant Depth Additions
Subscriptions and the plugin census are the two deltas that justify this variant; both are
kill-condition candidates for §9 at proposal stage.

## Anti-Selection Rules
WooCommerce as a brochure site with a handful of products → just rebuild, no migration project.
Multisite networks → scope per-site; this variant covers one store at a time.

## Known Failure Modes
Plugin meta discovered at import; subscription tokens assumed portable; guest orders dropped
silently; decorative stock imported as truth.

## Default Evidence Gates
Plugin census complete and signed; subscription portability answer in writing from the gateway;
every `[VERIFY]` resolved before execution-ready.

## Operating Hooks
Vendor freshness: subscription/checkout capabilities on Shopify side verified current via
Shopify Dev MCP when subscriptions are in scope. Flywheel: Woo findings here at Close Client.

## Output Shape By Mode
9-phase runbook; lane `api_to_api` default; subscriptions get their own phase insert with the
gateway gate; SEO supplement per propose §8.

## Source-Of-Truth
Lane + contract: `skills/kaizen-migrate.md` · recipes: `reference/kaizen-api-recipe-bank.md` ·
ecom patterns: `variants/ecommerce-to-shopify.md` · QA verdicts:
`delivery-os/templates/migration-qa-evidence-pack.md`
