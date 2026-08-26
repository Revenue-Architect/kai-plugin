# POS Migration Variant

Use this variant when a merchant is moving from Lightspeed, Square, Clover, Heartland, Revel,
Teamwork, or another in-store POS to Shopify POS.

## Required Context

- Merchant name and retail category
- Current POS and ecommerce stack
- Location count and planned location growth
- Data volume: products, customers, orders, gift cards, loyalty, inventory by location
- Known pain: inventory accuracy, reporting, hardware, staff workflows, ecommerce sync, support burden
- Timing constraints: lease, seasonality, contract expiry, event, expansion, or launch date

## Default Skill Chain

1. `skills/kaizen-research.md` if merchant facts or current stack need confirmation
2. `skills/kaizen-qualify.md` for discovery prep or call notes
3. `skills/kaizen-diagnose.md` for Blueprint findings
4. `skills/kaizen-propose.md` for commercial path
5. `skills/kaizen-migrate.md` plus `skills/kaizen-dataprep.md` for migration plan
6. `skills/kaizen-training.md`, `skills/kaizen-hardware.md`, and `skills/kaizen-check.md` before go-live

## Output Shape

- Recommendation: migrate now, defer, run Blueprint/advisory, or run implementation scoping
- Migration scope: entities included and excluded
- Data risk: record counts, export quality, gift cards, loyalty, historical orders
- Cutover readiness: hardware, payments, staff permissions, training, support coverage
- Tier fit: Silver, Gold, Diamond, or Blueprint-only
- Kill conditions: what would change the tier, timeline, or recommendation
- Next action: one concrete step

## Common Risks

- Treating platform name as enough to estimate data complexity
- Ignoring gift card liability or loyalty continuity
- Assuming all historical orders need full operational migration
- Missing store-level inventory opening counts
- Underweighting staff training and payment setup
- Quoting implementation when discovery is too thin

## When Not To Use

- The ask is only about one Shopify POS setting or hardware question. Use `skills/kaizen-retail-expert-v2.md` or `skills/kaizen-hardware.md`.
- The merchant is already on Shopify POS and only needs optimization. Use `skills/kaizen-report.md` or `skills/kaizen-shopify-config.md`.
- The request is to produce actual import files. Use `skills/kaizen-matrixify-exec.md`.

## Variant Depth Additions

### Anti-Selection Rules

- Do not recommend implementation before scoping if data volume, gift cards, loyalty, hardware,
  payments, or staff workflows are not understood.
- Do not assume historical orders, gift cards, or loyalty are included just because the merchant
  says "migration."
- Do not choose Matrixify by habit. API-first remains the default unless Matrixify is explicitly
  selected or lower-risk for a specific entity.

### Known Failure Modes

- Missing opening inventory counts by location.
- Gift-card liability not reconciled before cutover.
- Historical orders treated as operational orders instead of read-only reference history.
- Hardware, payment terminal, staff permission, or Smart Grid setup left until go-live.

### Default Evidence Gates

- Source export inventory count vs Shopify target count.
- Product/customer/location counts and rejected-row review.
- Gift-card and loyalty inclusion/exclusion decision.
- POS transaction test evidence before go-live.

### Operating Hooks

- Vendor Freshness Auto-Gate for Shopify POS, Admin API, Matrixify, and hardware/payment behavior.
- Evidence Gate Hook for migration QA and go-live.
- Task / Follow-Up Hook for client-owned exports, hardware orders, and training actions.

### Output Shape By Mode

- Quick Read: recommendation, biggest risk, next action.
- Operator Analysis: lane, scope, risks, kill conditions, what would change the recommendation.
- Client Deliverable: plain-language migration path, assumptions, exclusions, timeline, and next step.
- Execution Artifact: runbook, mapping, validation gates, rollback ledger, and cutover checklist.

### Source-Of-Truth And AnyDB Boundary

Shopify should own active POS transactions, products, customers, inventory, payments, and locations
unless an ERP is confirmed as master. AnyDB is first considered for exception handling, approvals,
vendor operations, reconciliation, reporting, or workflow state around the migration.
