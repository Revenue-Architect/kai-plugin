# Template — Monthly Operations Health Report

The backbone Ops Care deliverable and the upsell instrument. Owner: CEO assembles · CTO supplies technical status. Governed by [Pack 4 — Ops Care](../04-ops-care-pack.md) §1–4 & §8.

> Every module status ties to a named operational-continuity risk. No generic support. Reference retainer pricing, never invent it. Tag platform-behavior uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

**Client:** ______  **Month:** ______  **Retainer product + tier:** ______  **Account health:** 🟢 / 🟡 / 🔴

## Health summary
Operator-language read on the month. Lead with what changed and what needs attention. No boilerplate, no fabricated ROI.

## Module status (each tied to a named risk)
| Module | Named risk it covers | Status | Notes |
|--------|----------------------|--------|-------|
| Integration health | POS ↔ ERP ↔ accounting sync failing unnoticed | 🟢/🟡/🔴 | |
| Data hygiene | Dupes/drift degrading inventory + customer accuracy | 🟢/🟡/🔴 | |
| Flow maintenance | Automations silently breaking after a change | 🟢/🟡/🔴 | `[FLAG]` if uncertain |
| POS operations | Location issue with no fast resolution path | 🟢/🟡/🔴 | see [pos-operations-issue-log](pos-operations-issue-log.md) |

---

### Module detail — work the checks behind each status

**Integration health** (Owner: CTO · apply [`reference/kaizen-data-freshness.md`](../../reference/kaizen-data-freshness.md))

| Integration | Last successful sync | Error queue cleared? | Throughput normal? | Source of truth still correct? | Status |
|-------------|----------------------|----------------------|--------------------|--------------------------------|--------|
| | | | | | 🟢/🟡/🔴 |

- [ ] Disabled integrations still intentionally disabled (not silently re-enabled)
- [ ] Middleware (Patchworks/Versori/etc.) status confirmed `[FLAG: verify current Shopify docs before client commitment]` where uncertain
- [ ] Any failure escalated per Pack 4 escalation triggers

**Data hygiene** (Owner: CTO)

- [ ] Duplicate customers scanned; merge candidates flagged
- [ ] Duplicate/conflicting products scanned
- [ ] Inventory accuracy spot-checked against operational reality
- [ ] Orphaned / incomplete records identified
- [ ] Key-field integrity holds (SKUs, identifiers)
- [ ] Drift since last month noted with cause

| Finding | Count | Severity | Owner | Action |
|---------|-------|----------|-------|--------|
| | | | | |

_Merges and bulk corrections are operational changes — log them and confirm before applying. Report actuals, no fabricated "records cleaned" metrics._

**Flow maintenance** (Owner: CTO · builds compose via kaizen-flow-build)

| Flow | Purpose / risk it covers | Run history reviewed? | Failures? | References changed app/field? | Status |
|------|--------------------------|------------------------|-----------|-------------------------------|--------|
| | | | | `[FLAG]` if yes | 🟢/🟡/🔴 |

- [ ] Each live Flow's run history reviewed for failures
- [ ] Flows referencing changed apps/fields validated `[FLAG: verify current Shopify docs before client commitment]`
- [ ] New/changed business rules captured as Flow change requests
- [ ] Disabled/retired Flows documented

---

## Account health classification (evidence → 🟢 / 🟡 / 🔴)
Rubric lives in [Pack 4 §8](../04-ops-care-pack.md). Classify from evidence, not a feeling. A single red dimension affecting operations sets the account red until resolved.

| Dimension | Status | Evidence |
|-----------|--------|----------|
| Integration health | 🟢/🟡/🔴 | |
| Data hygiene | 🟢/🟡/🔴 | |
| Flow maintenance | 🟢/🟡/🔴 | |
| POS operations | 🟢/🟡/🔴 | |

## Issues this month
| ID | Location | Issue | Severity | Owner | Status |
|----|----------|-------|----------|-------|--------|
| | | | | | |

## Retainer hours
Used ____ / ____ (tier cap, per [`reference/kaizen-retainer-architecture.md`](../../reference/kaizen-retainer-architecture.md)). Over cap? Yes/No → re-tier or change order if recurring.

## Next implementation opportunity
Surface one **only if health ≥ 🟡**. If 🔴, this section is a stabilization plan, not an expansion pitch. Log to [expansion-opportunity-log](expansion-opportunity-log.md).

`[DRAFT — partner/legal review before client use]` for any client-facing version.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
