# Template — B2B Launch Test Pack

Everything tested before a B2B go-live: buyer self-serve, rep-assisted ordering, pricing resolution,
terms, approval, and the ERP/accounting handoff. Run with real accounts on the merchant's actual plan.
Owner: CTO observes · merchant reps and a pilot buyer execute. Peer of `launch-test-pack.md`.

> Verify behavior in the actual store on the merchant's actual plan. Catalog assignment, deposits,
> partial payments, and contextual checkout are plan-gated. Do not assert them from memory. Tag
> uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

**Merchant:** ______  **Plan:** ______  **Date:** ______  **Accounts tested:** ______

---

## Part A — Plan gate (do this first)

Confirm before testing anything below. A failure here invalidates the rest of the pack.

| # | Check | Expected | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Merchant plan confirmed in admin | Matches the plan the SOW was scoped against | | |
| 2 | Active catalog count | ≤3 on Basic/Grow/Advanced; unlimited on Plus | | |
| 3 | Catalog assignment method | Markets below Plus; direct company/location on Plus | | |
| 4 | Deposits in scope? | Plus only. If scoped below Plus, stop and escalate | | |
| 5 | Partial payments in scope? | Plus only | | |
| 6 | Contextual checkout/storefront in scope? | Advanced or Plus only | | |
| 7 | Customer accounts | New customer accounts active, not legacy | | |

---

## Part B — Buyer self-serve workflow scripts

| # | Workflow | Steps | Expected result | Pass/Fail | Notes |
|---|---|---|---|---|---|
| 1 | Buyer login | | Lands in correct company context | | |
| 2 | Location selection (multi-location buyer) | | Correct catalog and pricing load | | |
| 3 | Browse assigned catalog | | Only published products visible | | |
| 4 | Price resolution | | Correct price list applied | | |
| 5 | Volume price break | | Break applies at the right quantity | | |
| 6 | Quantity rules | | Min, max, increment all enforced | | |
| 7 | Quick order list / bulk entry | | | | |
| 8 | Reorder from history | | | | |
| 9 | Checkout on terms | | Correct payment terms template applied | | |
| 10 | PO number capture | | Buyer PO reference persists to the order | | |

A workflow a real buyer cannot complete unaided is a readiness gap, not a footnote.

---

## Part C — Rep-assisted workflow scripts

| # | Workflow | Expected result | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Rep creates draft order for a company contact | | | |
| 2 | Rep applies correct account pricing | | | |
| 3 | Buyer receives, reviews, approves | | | |
| 4 | Buyer pays from the draft order invoice | | | |
| 5 | Rep permission scoping | Rep sees only assigned accounts | | |
| 6 | Merchant review requirement (if configured) | Order held for review before release | | |

---

## Part D — Pricing resolution matrix

Run every combination the merchant actually sells into. Multiple pricing catalogs resolve to the
**lowest** price; a product must be published in at least one applicable publication to be visible.

| Account | Location | Product | Expected price | Actual | Pass/Fail |
|---|---|---|---|---|---|
| | | | | | |

Include at least one deliberately overlapping case if the merchant has more than one catalog.

---

## Part E — Terms, payment, and AR

| # | Check | Expected | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Correct terms template per company location | | | |
| 2 | Payment reminder fires | | | |
| 3 | Vaulted card charge | | | |
| 4 | ACH (US merchants) | | | |
| 5 | **Manual payment capture on fulfillment** | Automatic capture is NOT supported on B2B. Confirm the merchant's team knows they capture manually | | |
| 6 | Credit hold / over-limit behavior | Matches the agreed operating rule | | |
| 7 | Invoice reaches accounting/ERP with correct terms | | | |

Item 5 is the most commonly missed operational fact in a B2B launch. Confirm a named person owns
manual capture before go-live.

---

## Part F — ERP / accounting handoff

| # | Check | Expected | Pass/Fail | Notes |
|---|---|---|---|---|
| 1 | Order releases to ERP on the agreed trigger | | | |
| 2 | Company maps to the correct ERP account code | | | |
| 3 | Failure path when release fails | Someone is alerted, order is not silently stuck | | |
| 4 | Price disagreement between Shopify and ERP | Detected, not silently accepted | | |
| 5 | Tax / exemption certificate applied correctly | | | |

---

## Part G — Sign-off

| Item | Owner | Date | Signature |
|---|---|---|---|
| Buyer workflows pass | | | |
| Rep workflows pass | | | |
| Pricing matrix pass | | | |
| Terms and AR pass | | | |
| ERP handoff pass | | | |
| Named launch authority accepts | | | |

No blocking failure may remain open at sign-off. Record every non-blocking issue in the launch ops log
with an owner and a date.
