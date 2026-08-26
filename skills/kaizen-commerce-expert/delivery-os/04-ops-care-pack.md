# Asset Pack 4 — Ops Care Pack

Internal operating pack for the post-launch stage. Converts operational entropy after go-live into recurring revenue and managed account health. **Ops Care is not generic support** — every module ties to a named operational-continuity risk. This is an internal operating document, not client marketing.

> **Source of truth:** the approved Engagement Baseline from Pack 1 named the operational-continuity risks and the retainer fit; Pack 3 handed off open items and hypercare context. Pack 4 runs the recurring partnership against those risks.

> **Backbone deliverable:** the monthly Operations Health Report. It is the recurring proof of value and the upsell instrument.

> **Pricing is referenced, not duplicated.** Retainer products and modules are governed by [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md); dollar values are canonical in [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md). This pack names tiers and modules; it does not restate price tables.

> **No invented platform behavior.** Do not assert Shopify Flow, POS, or integration behavior from memory. Tag uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

---

## Purpose

Keep the live multi-location operation running and surface the next improvement before it becomes a problem. Ops Care monitors integrations, maintains data hygiene and Flow automations, tracks operational issues, runs quarterly reviews, classifies account health, and manages expansion — but only on stable accounts. Stabilize before you expand.

## Buyer / user

| Role | Owns |
|------|------|
| CEO | Account health, QBR, retainer relationship, expansion decisions |
| CTO | Integration health, Flow maintenance, data hygiene, technical issue resolution |
| Merchant owner | Operational input, QBR participation, authorizing incremental builds |

## Required inputs

- Completed launch with signed signoff per location (Pack 3)
- Retainer fit assessment from the Engagement Baseline (Pack 1), with named risks
- Signed retainer (product + tier per [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md))
- Baseline account-health classification
- Hypercare handoff items (Pack 3)

## Deliverables

| # | Deliverable | Template |
|---|-------------|----------|
| 1 | Monthly Operations Health Report — backbone; includes integration health, data hygiene, Flow maintenance module checks + account-health classification | [monthly-ops-health-report](templates/monthly-ops-health-report.md) |
| 2 | POS operations issue log | [pos-operations-issue-log](templates/pos-operations-issue-log.md) |
| 3 | Quarterly business review | [qbr-template](templates/qbr-template.md) |
| 4 | Expansion opportunity log | [expansion-opportunity-log](templates/expansion-opportunity-log.md) |

---

## Section 1 — Monthly Operations Health Report workflow

The backbone deliverable. Owner: CEO assembles · CTO supplies technical status. Template: [monthly-ops-health-report](templates/monthly-ops-health-report.md).

| Step | Owner | Action |
|------|-------|--------|
| 1 | CTO | Pull integration health, data hygiene, Flow status, POS issues |
| 2 | CEO | Classify account health (green/yellow/red) from the evidence |
| 3 | CEO | Write the operator-language summary: what changed, what needs attention |
| 4 | CTO | Tie each module status to its named operational-continuity risk |
| 5 | CEO | Track retainer hours against the tier cap |
| 6 | CEO | Surface the next implementation opportunity **only if health ≥ yellow** |
| 7 | Both | Run the QA gate, deliver |

Every module in the report maps to a risk. A status with no named risk behind it is generic support, which Ops Care is not.

## Section 2 — Integration health checklist

Covers the named risk: *a POS ↔ ERP ↔ accounting sync failing without anyone noticing.* Owner: CTO. Worked in the [monthly-ops-health-report](templates/monthly-ops-health-report.md) (Integration health module detail).

- [ ] Each integration's last successful sync confirmed
- [ ] Error/exception queue reviewed and cleared or escalated
- [ ] Volume/throughput within expected range
- [ ] Source-of-truth ownership still correct per [`reference/kaizen-data-freshness.md`](../reference/kaizen-data-freshness.md)
- [ ] Any middleware (Patchworks/Versori/etc.) status confirmed `[FLAG: verify current Shopify docs before client commitment]` where platform behavior is uncertain
- [ ] Disabled integrations still intentionally disabled (not silently re-enabled)

## Section 3 — Data hygiene checklist

Covers the named risk: *duplicate/dirty records degrading inventory and customer accuracy.* Owner: CTO. Worked in the [monthly-ops-health-report](templates/monthly-ops-health-report.md) (Data hygiene module detail).

- [ ] Duplicate customers/products scanned; merge candidates flagged
- [ ] Inventory accuracy spot-checked against operational reality
- [ ] Orphaned/incomplete records identified
- [ ] Key-field integrity holds (SKUs, identifiers)
- [ ] Drift since last month noted with cause

## Section 4 — Shopify Flow maintenance checklist

Covers the named risk: *automations silently breaking after a Shopify or app change.* Owner: CTO. Worked in the [monthly-ops-health-report](templates/monthly-ops-health-report.md) (Flow maintenance module detail).

- [ ] Each live Flow's run history reviewed for failures
- [ ] Flows referencing changed apps/fields validated `[FLAG: verify current Shopify docs before client commitment]`
- [ ] New/changed business rules captured as Flow change requests
- [ ] Disabled/retired Flows documented
- [ ] Flow changes composed via kaizen-flow-build where a build is needed

## Section 5 — POS operations issue log

Covers the named risk: *a location-level operational issue with no fast path to resolution.* Owner: CTO resolves · CEO tracks. Template: [pos-operations-issue-log](templates/pos-operations-issue-log.md).

Each entry: ID, location, issue, severity, owner, status, resolution. Recurring issues feed the health classification and may surface an incremental-build opportunity (stable accounts only).

## Section 6 — QBR workflow

Quarterly business review. Owner: CEO leads · CTO on technical. Template: [qbr-template](templates/qbr-template.md).

| Step | Action |
|------|--------|
| 1 | Review the quarter's health trend (3 monthly reports) |
| 2 | Review issues resolved, risks retired, risks emerging |
| 3 | Review retainer-hour usage vs tier |
| 4 | Present expansion opportunities **only if account health ≥ yellow** |
| 5 | Confirm or re-tier the retainer by operational maturity |

If the account is red, the QBR is a stabilization plan, not an expansion pitch.

## Section 7 — Retainer tier fit matrix

Match the retainer product and tier to the operation. Reference, do not duplicate, pricing: model in [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md), dollar values in [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md). Position by operational maturity ([`reference/kaizen-operational-readiness.md`](../reference/kaizen-operational-readiness.md)), not by default to the largest tier.

| What the engagement left behind | Retainer product | Tier signal |
|---------------------------------|------------------|-------------|
| A live multi-location operation | Ops Care Retainer | Tier by operational maturity / support volume |
| A POS ↔ ERP ↔ accounting integration | Managed Integration Retainer | By integration complexity (middleware at cost + management layer) |
| A delivered AnyDB system | AnyDB Operations Retainer | By schema/automation maintenance load |

A single client may hold more than one product. Pricing and tier ranges are canonical in the reference — never invent them.

## Section 8 — Account health model (green / yellow / red)

Owner: CEO classifies from evidence each month. The rubric below is the reference; the per-month classification is recorded in the [monthly-ops-health-report](templates/monthly-ops-health-report.md) (Account health classification).

| Health | Signals | Action posture |
|--------|---------|----------------|
| 🟢 Green | Integrations healthy, data clean, Flows stable, issues low/resolved | Maintain; surface the next improvement |
| 🟡 Yellow | One module degraded or recurring issues; trend watchable | Address the degradation; cautious on expansion |
| 🔴 Red | Integration failing, data drift, unresolved Criticals, operational disruption | **Stabilize first. Do not pitch expansion or incremental builds.** |

Classification is evidence-based, not a feeling. The model drives whether expansion is even on the table.

## Section 9 — Expansion opportunity log

Surfaced opportunities, gated on health. Owner: CEO. Template: [expansion-opportunity-log](templates/expansion-opportunity-log.md).

Each entry: opportunity, the named operational need behind it, account health at time of surfacing, and a gate flag. **Do not pitch expansion or incremental builds to a red-health account.** A logged opportunity on a red account waits until the account is stabilized to ≥ yellow.

## Section 10 — Retainer hour / cap tracking

Owner: CEO. Track hours used against the tier's monthly cap (cap defined in [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md)).

| Month | Tier cap (hrs) | Hours used | Over cap? | Action |
|-------|----------------|------------|-----------|--------|
| | | | | Change order / re-tier if recurring |

Recurring overage is a re-tier or change-order conversation, not silent absorption.

---

## QA gate

The monthly report and Ops Care output do not go out until all pass. Fix in place, then re-verify.

- [ ] Monthly Operations Health Report produced (backbone deliverable)
- [ ] Every module status ties to a **named operational-continuity risk** — no generic support
- [ ] Account health classified from evidence (green/yellow/red)
- [ ] Expansion/incremental builds **not** pitched on a red-health account
- [ ] Retainer hours tracked against the tier cap
- [ ] Retainer pricing referenced from canonical sources, not duplicated or invented
- [ ] No Shopify Flow/POS/integration behavior asserted from memory; uncertainties tagged `[FLAG: verify current Shopify docs before client commitment]`
- [ ] No fabricated ROI; only the merchant's own numbers or clearly-labeled conservative estimates
- [ ] Client-facing snippets tagged `[DRAFT — partner/legal review before client use]`

Retainer tiering, expansion timing, and stabilization calls remain partner judgment.

---

## Escalation triggers

Bring in partner judgment when:

- Account health drops to red
- An integration is failing and affecting operations
- Retainer hours are repeatedly over the tier cap
- Data hygiene is degrading month over month
- A Flow is silently failing after a platform/app change `[FLAG: verify current Shopify docs before client commitment]`
- The merchant requests out-of-scope build work (route to Pack 5 / kaizen-scope)
- An expansion opportunity is being considered on an unstable account

---

## Reusable templates / checklists

- [monthly-ops-health-report](templates/monthly-ops-health-report.md) (backbone — integration health, data hygiene, Flow maintenance, account-health classification) · [pos-operations-issue-log](templates/pos-operations-issue-log.md) · [qbr-template](templates/qbr-template.md) · [expansion-opportunity-log](templates/expansion-opportunity-log.md)

**Reference depth:** [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md) · [`reference/kaizen-operational-readiness.md`](../reference/kaizen-operational-readiness.md) · [`reference/kaizen-data-freshness.md`](../reference/kaizen-data-freshness.md) · [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md)

*Composes with kaizen-report-exec, kaizen-flow-build, kaizen-finance, kaizen-scope. Receives from Pack 3 (Launch QA). Surfaces opportunities back to Pack 5 (Sales/SOW).*

---
*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
