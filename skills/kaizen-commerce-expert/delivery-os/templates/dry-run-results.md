# Template — Dry Run Results

Evidence that the live cutover will behave. Dry Run always precedes live. Owner: CTO. Governed by [Pack 2 — API-First Migration](../02-api-first-migration-package.md) §7.

**Client:** ______  **Target:** Shopify test/dev (NOT live)  **Date:** ______  **Tolerance:** `[NEED: reconciliation tolerance]`

## Per-entity result

| Entity | Lane | Source count | Loaded count | Errors | Spot-checks passed | Pass/Fail |
|--------|------|--------------|--------------|--------|--------------------|-----------|
| | | | | | | |

## Errors (→ exception log)

| ID | Entity | Error | Severity (Critical/Important/Watch) | Owner | Status |
|----|--------|-------|-------------------------------------|-------|--------|
| | | | | | |

## Verdict

- [ ] All entities within approved tolerance
- [ ] No Critical error open
- [ ] Spot-checks passed per entity

**Dry Run result:** PASS / FAIL. A FAIL blocks cutover until exceptions are resolved and the affected entities are re-run.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
