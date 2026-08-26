# Template — SOW Boundaries

Reusable scope-protection template for the POS transformation wedge. Assemble from the approved Engagement Baseline (Pack 1) and the tier deliverables in [`reference/kaizen-pricing.md`](../../reference/kaizen-pricing.md). Governed by [Pack 5 — Sales / SOW](../05-sales-sow-pack.md).

> Every block below is a **client-facing draft. `[DRAFT — partner/legal review before client use]`.** Do not send without partner sign-off. Never invent pricing, payment, warranty, or legal terms — pull from canonical pricing or mark `[NEED: approved price]`.

> Derive every line from an approved Engagement Baseline. If the Baseline did not scope it, it does not belong here.

**Client:** ______  **Tier:** Silver / Gold / Diamond / Commerce Systems  **Migration lane:** API-first / Matrixify / Admin CSV  **Data cap:** ______ products/customers  **Source artifact:** Blueprint / Implementation Scoping Brief / Shopify Referral Scope Brief  **Source date:** ______

Owners: CEO assembles · CTO confirms technical lines · merchant owner signs.

---

## Inclusion block
`[DRAFT — partner/legal review before client use]`

This engagement includes, for the **[tier]** scope:

- Discovery and source-of-truth findings carried into delivery
- Migration of in-scope entities via the **[named lane]**, up to the stated data cap
- In-scope entities (from Engagement Baseline entity scope): products, variants, collections, customers, orders, inventory, locations, metafields/metaobjects
- Gift card / store credit migration *(only where the Engagement Baseline/Pack 2 confirmed feasibility — else flag)*
- Multi-location configuration and per-location launch QA
- Staff permissions configuration and the tier's training allotment
- Dry Run before live cutover; The Kaizen Cutover phase plan; legacy POS stays live until proven
- Reconciliation and launch signoff
- Retainer offer attached per the Retainer block

_Each line must trace to an Engagement Baseline finding or the tier deliverable list._

## Exclusion block
`[DRAFT — partner/legal review before client use]`

Not included unless added by change order:

- Data beyond the stated cap
- Source-system cleanup the merchant does not authorize or perform
- Net-new catalog creation, enrichment, or photography (vs migration of existing)
- Migration lane change caused by source access the merchant cannot provide
- Integrations the merchant declines to enable; apps outside the named list
- Custom development beyond the named operational workflow build scope
- Historical order migration beyond the tier's included depth
- Hardware procurement outside the agreed device list
- Any Shopify behavior flagged for current-documentation verification, until verified by the CTO
- Training beyond the tier's included allotment

## Client responsibility block
`[DRAFT — partner/legal review before client use]`

- Named internal owner with authority and availability through the engagement
- Read/admin access to current POS, Shopify admin, and back-office systems
- Representative data exports and sample files on request
- Timely validation of Dry Run and reconciliation, and launch signoff
- Confirming history-depth and gift-card/store-credit requirements before migration
- Staff availability for per-location workflow testing at go-live
- Source-of-truth decisions where the Engagement Baseline flagged a conflict
- Authorizing any change order before out-of-scope work proceeds

## Data cap language
Canonical clause: [`reference/kaizen-pricing.md`](../../reference/kaizen-pricing.md) (Standard Overage Language).
`[DRAFT — partner/legal review before client use]`
> This engagement includes migration of up to **[included limit]** products/customers. If the final export exceeds that threshold, we will issue a change order covering additional mapping, QA, and import workload, which may affect both project fee and delivery timeline.

_The cap is a number, not "reasonable volume." If the Engagement Baseline shows the merchant near or over cap, name the overage exposure in the proposal up front. Never promise fixed scope without a cap._

## Change-order triggers
- Final export exceeds the data cap
- Scope added beyond the inclusion block
- Migration lane forced to change due to source access
- Net-new catalog / enrichment requested
- Additional integration or app brought into scope
- History depth beyond tier inclusion
- Operational workflow scope expands beyond the named build
- Out-of-scope request mid-engagement (pause → document → authorize)
- A flagged Shopify behavior proves to require unscoped work after verification

_No out-of-scope work proceeds on goodwill. Document, size, authorize. Composes with `kaizen-scope`._

## Retainer attach language
Attach by default. Tie every module to a named operational-continuity risk; never pitch as generic support. **Do not pitch expansion/incremental builds to a red-health account — stabilize first.** Catalog: [`reference/kaizen-retainer-architecture.md`](../../reference/kaizen-retainer-architecture.md).

| Implementation leaves behind | Attach |
|------------------------------|--------|
| A live multi-location operation | Ops Care Retainer (tier by operational maturity) |
| A POS ↔ ERP ↔ accounting integration | Managed Integration Retainer |
| A delivered operational workflow system | AnyDB Operations Retainer |

`[DRAFT — partner/legal review before client use]`
> After go-live, we keep the operation running: a monthly Operations Health Report, plus [named modules tied to the risks the Engagement Baseline surfaced]. The report tracks the operation and surfaces the next improvement before it becomes a problem.

---

**Commercial guardrails:** choose Blueprint/advisory or scoped full implementation explicitly · cap explicit · Blueprint credit shown only when a Blueprint fee was charged · no fabricated ROI · no fixed scope without a cap · pricing referenced from `kaizen-pricing.md`, never invented.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
