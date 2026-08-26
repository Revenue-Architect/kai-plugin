# Asset Pack 3 — Launch QA Pack

Internal operating pack for go-live. Makes launch repeatable and **evidence-based across every location**. QA proves readiness; it does not assume it. This is an internal operating document, not client marketing.

> **Source of truth:** the approved Engagement Baseline from Pack 1 sets launch constraints and scope; Pack 2 hands off a validated migration under Parallel Validation. Pack 3 confirms each location can actually operate.

> **Partner judgment owns QA signoff.** A location goes live when the evidence says so, or on a documented, partner-approved exception — never on optimism.

> **No invented platform behavior.** Do not assert POS behavior, gift-card behavior, store-credit behavior, or POS permission behavior from memory. Tag uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

> **Parallel Validation holds through launch.** Legacy POS stays live until Shopify is proven at each location. No "zero downtime" / "no lost data" claims.

> **Use The Kaizen Cutover.** Launch QA follows the named cutover methodology:
> Shadow → Pilot Store → Verdict Gate → Waves → Hypercare. See
> [`reference/kaizen-cutover-methodology.md`](../reference/kaizen-cutover-methodology.md).

---

## Purpose

Run a per-location readiness gauntlet that proves staff can complete core workflows, inventory is accurate enough to launch, payments and hardware work, transactions behave, reporting is usable, integrations are monitored or intentionally disabled, and every known issue has an owner and severity. The output is a signed, named launch signoff per location and a managed hypercare window.

## Buyer / user

| Role | Owns |
|------|------|
| CTO | Technical validation, test execution, integration decisions, severity calls |
| CEO | Client-facing signoff, go-live command center, hypercare coordination |
| Merchant owner | Staff availability, location access, reporting confirmation, signoff authority |

## Required inputs

- Pack 2 cutover accepted (validated migration, reconciliation passed)
- Configured Shopify store, locations, and staff permissions
- Hardware installed per location
- Launch window confirmed against Engagement Baseline constraints
- Named merchant signoff authority per location

## Deliverables

| # | Deliverable | Template |
|---|-------------|----------|
| 1 | Store + per-location readiness | [launch-qa-checklist](templates/launch-qa-checklist.md) |
| 2 | Workflow + transaction test results | [launch-test-pack](templates/launch-test-pack.md) |
| 3 | Go-live command center + hypercare log | [launch-ops-log](templates/launch-ops-log.md) |
| 4 | Signed launch signoff per location | [launch-signoff-form](templates/launch-signoff-form.md) |

---

## The Kaizen Cutover phase map

This pack owns the launch-readiness and support portions of the methodology.

| Cutover phase | Pack 3 responsibility |
|---|---|
| Shadow | Confirm store, staff, payment, hardware, reporting, and workflow readiness before live selling moves. |
| Pilot Store | Prove one representative location can operate the new path with named staff and real hardware. |
| Verdict Gate | Decide whether remaining locations wave, hold, or rework based on signed evidence. |
| Waves | Run per-location readiness, command center, signoff, and issue capture for each launch group. |
| Hypercare | Monitor issues by owner and severity, then route unresolved work to warranty, Ops Care, or change order. |

---

## Section 1 — Store readiness checklist

Run once at the store level before any location goes live. Owner: CTO.

- [ ] Store settings, taxes, and currencies configured
- [ ] Sales channels configured or intentionally deferred (documented)
- [ ] Payment processor live and configured `[FLAG: verify current Shopify docs before client commitment]` where regional behavior matters
- [ ] Migrated data accepted from Pack 2 (reconciliation passed)
- [ ] Staff roles defined at the store level
- [ ] Reporting baseline available

## Section 2 — Per-location readiness checklist

Run once **per location**. A location does not go live until it passes or has a documented partner-approved exception. Owner: CTO validates, CEO signs. Template: [launch-qa-checklist](templates/launch-qa-checklist.md).

- [ ] Location created and active
- [ ] Inventory accurate enough to launch (threshold: `[NEED: launch inventory-accuracy threshold]`)
- [ ] Hardware installed and paired
- [ ] Staff assigned with correct permissions
- [ ] Workflow tests passed (Section 5)
- [ ] Transaction matrices passed (Sections 6–7)
- [ ] Reporting validated (Section 9)
- [ ] Integrations monitored or intentionally disabled (Section 10)
- [ ] Known issues logged with owner + severity; no Critical open

## Section 3 — Hardware / payment validation

Per location. Owner: CTO. Do not assert device or processor behavior from memory.

- [ ] Terminals / readers paired and tested on real hardware
- [ ] Receipt printer working
- [ ] Cash drawer / barcode scanner functioning (if in scope)
- [ ] A real test sale completed end-to-end on the hardware
- [ ] Payment processor live for the location's region `[FLAG: verify current Shopify docs before client commitment]`
- [ ] Refund to original tender tested `[FLAG: verify current Shopify docs before client commitment]`

## Section 4 — Staff permissions validation

Per location. Confirm against the configured roles, not from memory of POS permission behavior. Owner: CTO.

- [ ] Each role can perform its intended actions
- [ ] Restricted actions are blocked for non-managers
- [ ] Manager override works as configured
- [ ] Permission behavior verified in the actual POS, not assumed `[FLAG: verify current Shopify docs before client commitment]`

## Section 5 — POS workflow test scripts

Staffed tests proving people can do the job. Owner: CTO observes, staff execute. Template: [launch-test-pack](templates/launch-test-pack.md) (Part A).

Core scripts (each: steps → expected result → pass/fail → notes):

- Ring a standard sale
- Apply a discount
- Process a return
- Process an exchange
- Look up a product / customer
- Handle a split or alternate tender
- Manager override action

A workflow staff cannot complete is a readiness gap, not a footnote.

## Section 6 — Order / refund / exchange test matrix

Per location, on real hardware. Template: [launch-test-pack](templates/launch-test-pack.md) (Part B).

| Scenario | Expected | Pass/Fail | Notes |
|----------|----------|-----------|-------|
| Standard sale | | | |
| Sale with discount | | | |
| Refund to original tender | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Exchange (even / uneven) | | | |
| Partial refund | | | |

## Section 7 — Gift card / store-credit test matrix

Only where in scope and confirmed feasible by the Engagement Baseline/Pack 2. Do not assume issuance, redemption, or balance behavior. Template: [launch-test-pack](templates/launch-test-pack.md) (Part C).

| Scenario | Expected | Pass/Fail | Flag |
|----------|----------|-----------|------|
| Issue gift card | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Redeem gift card | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Check balance | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Issue store credit | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Redeem store credit | | | `[FLAG: verify current Shopify docs before client commitment]` |

If gift card / store credit was not migrated or is unverified, mark the location's signoff with the limitation explicitly.

## Section 8 — Inventory validation checklist

Per location. Owner: CTO.

- [ ] On-hand quantities by location match the reconciled source within the launch threshold
- [ ] High-velocity / high-value SKUs spot-checked physically
- [ ] Transfers and incoming receiving handled correctly in a test
- [ ] Inventory accuracy meets `[NEED: launch inventory-accuracy threshold]`

## Section 9 — Reporting validation checklist

Owner: CTO validates, merchant confirms the reports match expectations.

- [ ] Core sales/inventory reports populate
- [ ] Numbers match what the merchant expects to see
- [ ] Reconciliation/financial views are usable for end-of-day
- [ ] Any report gap documented with owner

## Section 10 — Integration monitoring / disable decision

For every integration, a deliberate decision before go-live: monitored or intentionally disabled. No integration is left in an undefined state. Owner: CTO + merchant.

| Integration | Decision (Monitor / Disable) | Owner | Notes |
|-------------|------------------------------|-------|-------|
| | | | |

Apply data-freshness defaults from [`reference/kaizen-data-freshness.md`](../reference/kaizen-data-freshness.md). A disabled integration is documented so it is not assumed live.

## Section 11 — Go-live command center

The launch-day control surface. Owner: CEO runs it, CTO on point for technical calls. Template: [launch-ops-log](templates/launch-ops-log.md) (Part A).

- Named owners on point per location
- Real-time issue capture into the hypercare log
- Go/no-go status per location
- Escalation path live during the window

## Section 12 — Hypercare issue log

Post-launch close monitoring. Every issue: owner + severity + status. Template: [launch-ops-log](templates/launch-ops-log.md) (Part B). Hands off unresolved non-Criticals to Pack 4 (Ops Care) with context.

## Section 13 — Launch signoff form

Per location, signed by a **named** merchant authority — not "the client." Template: [launch-signoff-form](templates/launch-signoff-form.md).

`[DRAFT — partner/legal review before client use]`
> [Location] has completed launch QA. Core workflows, hardware, payments, transactions, inventory accuracy, and reporting were tested and meet the launch criteria. Known issues are listed with owner and severity; none are Critical. Legacy remains available per Parallel Validation until this location is confirmed stable.
> Signed: __________ (name, role)  Date: ______

---

## QA gate

A location does not go live until all pass. Fix in place, then re-verify.

- [ ] Store readiness passed
- [ ] This location's readiness checklist passed (or a documented partner-approved exception)
- [ ] Hardware/payment validated on real hardware
- [ ] Staff permissions verified in the actual POS, not assumed
- [ ] Workflow scripts passed — staff can complete core tasks
- [ ] Order/refund/exchange matrix passed
- [ ] Gift card/store-credit matrix passed or limitation documented; behavior verified, not assumed
- [ ] Inventory accuracy meets the launch threshold `[NEED: launch inventory-accuracy threshold]`
- [ ] Reporting validated and confirmed by the merchant
- [ ] Every integration is monitored or intentionally disabled (documented)
- [ ] **No Critical issue open at go-live**
- [ ] Launch signoff signed by a named merchant authority
- [ ] No "zero downtime" claim; Parallel Validation language used; Shopify-behavior uncertainties tagged `[FLAG]`
- [ ] Client-facing snippets tagged `[DRAFT — partner/legal review before client use]`

QA signoff remains partner judgment. The gate verifies the evidence exists; the partner decides go-live.

---

## Escalation triggers

Stop / hold go-live and bring in partner judgment when:

- Payment or hardware fails at a location
- Inventory accuracy is below the launch threshold
- Staff cannot complete a core workflow
- An integration is failing with no monitor/disable decision
- Gift card / store credit behavior is unverified and in scope
- A Critical issue is open at the planned go-live moment
- The signoff authority is unavailable or unnamed
- A location would go live on optimism rather than passed evidence

---

## Reusable templates / checklists

- [launch-qa-checklist](templates/launch-qa-checklist.md) · [launch-test-pack](templates/launch-test-pack.md) (workflow + transaction tests) · [launch-ops-log](templates/launch-ops-log.md) (command center + hypercare) · [launch-signoff-form](templates/launch-signoff-form.md)

**Reference depth:** [`reference/kaizen-evidence-and-gates.md`](../reference/kaizen-evidence-and-gates.md) · [`reference/kaizen-operational-readiness.md`](../reference/kaizen-operational-readiness.md) · [`reference/kaizen-data-freshness.md`](../reference/kaizen-data-freshness.md)

*Composes with kaizen-test-exec, kaizen-training, kaizen-shopify-config, kaizen-hardware. Receives from Pack 2, hands off to Pack 4 (Ops Care).*

---
*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
