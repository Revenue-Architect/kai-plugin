# Template — Migration Runbook

Ordered execution record for one engagement. Owner: CTO. Governed by [Pack 2 — API-First Migration](../02-api-first-migration-package.md) §6.

**Client:** ______  **Cutover window:** ______  **Reconciliation tolerance:** `[NEED: reconciliation tolerance]` until partner-approved

## Phase gates

| Phase | Owner | Gate to pass before proceeding | Status |
|-------|-------|--------------------------------|--------|
| Prep | CTO | Access confirmed · entity map + field maps final · scope frozen · data-quality checklist passed | |
| Build | CTO | Each entity loader tested on sample with idempotency key | |
| Dry Run | CTO | Full load into test/dev target; results captured | |
| Validate | CTO | Reconciliation within approved tolerance | |
| Fix | CTO | Exception log cleared of Criticals; affected entities re-run | |
| Cutover | CTO + merchant | Cutover plan approved; Parallel Validation in place | |
| Confirm | CTO + merchant | Post-cutover reconciliation passed; sign-off obtained | |

## Load order (confirm per build)

locations → products → variants → inventory · customers → orders · collections after products · metafields/metaobjects after parent records.
`[FLAG: verify current Shopify docs before client commitment]` where exact ordering behavior affects a commitment.

## Execution log

| Step | Entity | Lane | Start | End | Source count | Loaded count | Errors | Notes |
|------|--------|------|-------|-----|--------------|--------------|--------|-------|
| | | | | | | | | |

**Parallel Validation reminder:** legacy POS stays live and authoritative until Shopify is proven. Data is validated before cutover is called done.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
