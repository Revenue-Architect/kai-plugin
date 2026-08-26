# Template — Reconciliation Checklist

Proves migrated data matches source within the partner-approved tolerance. Run after Dry Run and again post-cutover. Owner: CTO. Governed by [Pack 2 — API-First Migration](../02-api-first-migration-package.md) §9.

**Client:** ______  **Stage:** Dry Run / Post-cutover  **Tolerance:** `[NEED: reconciliation tolerance]` (partner decision)

## Count + integrity checks

| Check | Source | Shopify | Variance | Within tolerance? |
|-------|--------|---------|----------|-------------------|
| Products count | | | | |
| Variants count | | | | |
| Customers count | | | | |
| Orders count | | | | |
| Inventory by location | | | | |
| Order financial totals | | | | |
| Refund totals | | | | |

- [ ] Key-field spot checks per entity passed
- [ ] Referential integrity re-checked post-load
- [ ] Financial tie-out applied per [`reference/kaizen-data-freshness.md`](../../reference/kaizen-data-freshness.md)
- [ ] Every variance classified and logged
- [ ] No Critical variance open at sign-off

**Reconciliation result:** PASS / FAIL against approved tolerance. Tolerance is a partner decision — do not assume exact match or invent a percentage.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
