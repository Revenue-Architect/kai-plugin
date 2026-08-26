# Template — Launch Test Pack (per location)

Everything tested at a location before go-live: staffed workflow scripts and the transaction matrix. Run on real hardware. Owner: CTO observes · staff execute. Governed by [Pack 3 — Launch QA](../03-launch-qa-pack.md) §5–7.

> Verify behavior in the actual POS. Do not assert POS, gift-card, store-credit, or refund-tender behavior from memory. Tag uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

**Location:** ______  **Date:** ______  **Staff tested:** ______

---

## Part A — POS workflow scripts (can staff do the job?)

| # | Workflow | Steps | Expected result | Pass/Fail | Notes |
|---|----------|-------|-----------------|-----------|-------|
| 1 | Standard sale | | | | |
| 2 | Apply discount | | | | |
| 3 | Process return | | | | |
| 4 | Process exchange | | | | |
| 5 | Product / customer lookup | | | | |
| 6 | Split / alternate tender | | | | |
| 7 | Manager override | | | | `[FLAG: verify current Shopify docs before client commitment]` if behavior uncertain |

A workflow staff cannot complete is a readiness gap, not a footnote.

---

## Part B — Order / refund / exchange matrix

| Scenario | Expected | Pass/Fail | Notes |
|----------|----------|-----------|-------|
| Standard sale | | | |
| Sale with discount | | | |
| Refund to original tender | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Exchange (even) | | | |
| Exchange (uneven) | | | |
| Partial refund | | | |

---

## Part C — Gift card / store credit (only if in scope + Baseline-confirmed)

| Scenario | Expected | Pass/Fail | Flag |
|----------|----------|-----------|------|
| Issue gift card | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Redeem gift card | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Check balance | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Issue store credit | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Redeem store credit | | | `[FLAG: verify current Shopify docs before client commitment]` |

If gift card / store credit was not migrated or is unverified, document the limitation on the location's [launch-signoff-form](launch-signoff-form.md).

**Gate:** log every failure to the location's known-issues list with severity. No Critical open at go-live.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
