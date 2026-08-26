# The Kaizen Cutover Methodology

Source-of-truth doctrine for POS migration launch planning. Client-facing outputs may use the name
"The Kaizen Cutover." Internal outputs may call it the cutover methodology.

## Promise boundary

KaizenCommerce does not promise that a migration is risk-free. The promise is a controlled
cutover: prove the operating path before wave launch, keep rollback options visible, and prevent a
planned store-closing cutover.

Use this language:

> The goal is not a dramatic launch day. The goal is a controlled cutover where the store team has
> already seen the workflow, the data has already been reconciled, and every open risk has an
> owner.

Avoid these claims:

- "Zero downtime"
- "No disruption"
- "No lost sales"
- "Guaranteed launch date"
- "Guaranteed inventory accuracy"
- "We will never close stores"

## Phases

| Phase | Purpose | Exit gate |
|---|---|---|
| 1. Shadow | Configure the target path and compare it against current operations without disrupting selling. | Data map, permissions, hardware/payment path, gift-card/store-credit stance, and integration ownership are confirmed or flagged. |
| 2. Pilot Store | Run one representative location through the target workflow before broader rollout. | Staff can sell, receive, transfer, reconcile, and escalate issues using the new operating path. |
| 3. Verdict Gate | Decide whether to wave, hold, or rework before broader rollout. | Open defects are classified, owners are named, and payment/inventory variances are inside partner-approved tolerance. |
| 4. Waves | Launch remaining locations in controlled groups. | Each wave has a named launch owner, support window, rollback path, and daily reconciliation check. |
| 5. Hypercare | Stabilize, monitor exceptions, and move into retainer or change-order mode. | Warranty window, retainer route, unresolved defects, and owner handoff are documented. |

## Required artifacts

Each implementation using this method should produce or reference:

- Engagement Baseline from Blueprint Diagnostic or approved Shopify Referral Scope Brief
- Risk Map from Blueprint
- Cutover Plan with phase dates, owners, gates, and rollback notes
- Data/entity map for products, customers, orders, gift cards, loyalty, inventory, and locations
- Pilot Store verdict
- Wave launch checklist
- Hypercare and warranty routing

## Client-facing framing

Lead with owner-operator fear of breakage:

- "Your biggest risk is not the software switch. It is discovering workflow exceptions after the
  stores are live."
- "Inventory shrink usually shows up as a people-and-process problem before it shows up as a
  system problem."
- "The cutover plan exists so staff are not learning the workflow for the first time while a
  customer is at the counter."

## Proposal and SOW placement

Use the methodology in migration approach sections, not as a standalone product unless the scope is
specifically a cutover rescue or launch-readiness review.

Milestone billing can mirror the phases only when the SOW has already approved milestone billing.
Do not invent a payment schedule from this reference.
