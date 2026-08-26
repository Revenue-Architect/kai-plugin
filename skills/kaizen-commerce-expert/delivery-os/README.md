# KaizenCommerce Delivery OS

Internal operating system for one productized wedge: **multi-location Shopify POS transformation** — scoping, Blueprint/advisory, full implementation, API-first migration, launch QA, and Ops Care.

This is an internal delivery system, not a public package. It exists to reduce partner delivery time, make scoping consistent, raise quality, and create a clear path from scoped discovery, paid Blueprint/advisory, or approved Shopify Referral Baseline → implementation → recurring Ops Care. It is not a fixed-scope commodity offer. Partner judgment stays responsible for final scope, pricing, architecture, source-of-truth decisions, migration lane, and QA signoff.

POS rollout language uses [The Kaizen Cutover Methodology](../reference/kaizen-cutover-methodology.md):
Shadow → Pilot Store → Verdict Gate → Waves → Hypercare. The method is a controlled cutover
discipline, not a risk-free launch promise.

---

## Productization status

**Productize, but not fully sellable yet.** The wedge is teachable (with SOPs and templates), valuable (failed POS transformation disrupts inventory, staff workflows, payments, reporting, and customer experience across every location), and repeatable (multi-location migrations share recurring patterns). What is missing before KaizenCommerce promotes a fixed-scope or repeatable package is the internal asset library this folder builds. See `DECISIONS-BEFORE-SELLABLE.md` for the open commercial and technical decisions.

---

## The five asset packs

| # | Pack | Purpose | Primary partner |
|---|------|---------|-----------------|
| 1 | [Blueprint Diagnostic](01-blueprint-diagnostic-pack.md) | Turn discovery into a paid diagnostic across systems, workflows, data readiness, migration lane, launch readiness, retainer fit, and the executive artifacts: Risk Map, Cutover Plan, and The Number | CEO (discovery), CTO (technical assessment) |
| 2 | [API-First Migration](02-api-first-migration-package.md) | Repeatable migration planning and execution. API-first is the default lane; Matrixify and Admin CSV are supported fallbacks | CTO |
| 3 | [Launch QA](03-launch-qa-pack.md) | Make go-live repeatable and evidence-based across all locations | CTO + CEO |
| 4 | [Ops Care](04-ops-care-pack.md) | Convert post-launch operational entropy into recurring revenue and account health management | CEO (account), CTO (technical) |
| 5 | [Sales / SOW](05-sales-sow-pack.md) | Make the wedge easy to explain, qualify, scope, and protect commercially | CEO |

The **Engagement Baseline** is the source of truth. It can be produced by a paid Blueprint, an Implementation Scoping Brief for merchants buying full delivery after a scoping call, or an approved Shopify Referral Scope Brief. Qualification, scope, migration lane, QA plan, proposal, and Ops Care attach all derive from the Baseline. A weak Baseline turns every later stage back into custom work, which is why Pack 1 is built deepest.

**Founder note:** Mixed Commerce is not the wedge. It is the escalation lane when a POS opportunity exposes real cross-surface system design: DTC, B2B, ERP/accounting, marketplace, fulfillment, or AnyDB source-of-truth dependencies that can change launch sequence or scope. Do not sell every complex Shopify account as Delivery OS. Use the Mixed Commerce Systems Baseline Brief only when the cross-surface dependency is confirmed and partner-approved.

---

## How the packs connect

```
Discovery ──► [1] BLUEPRINT / ADVISORY ─┐
Scoping Call ─► IMPLEMENTATION BRIEF ───┤
Shopify Referral ─► REFERRAL BRIEF ─────┤
                                         ▼
                              ENGAGEMENT BASELINE
                              defines:
                              • scope + data caps
                              • migration lane (API / Matrixify / CSV)
                              • launch readiness gaps
                              • Risk Map
                              • Cutover Plan
                              • The Number
                              • retainer fit
                                         │
        ┌────────────────────────────────┼────────────┬──────────────┐
        ▼                                ▼            ▼              ▼
   [5] SALES/SOW                   [2] MIGRATION  [3] LAUNCH QA  [4] OPS CARE
   (scope &                        (plan +        (go-live       (recurring
    protect)                        execute)       signoff)       ownership)
```

Every pack in this OS is structured the same way so a partner can pick up any stage cold:

- **Purpose** — what the pack is for
- **Buyer / user** — who runs it, who receives it
- **Required inputs** — what must exist before starting
- **Deliverables** — what the pack produces
- **Internal workflow** — step sequence with owner roles
- **Client responsibilities** — what the merchant must supply or do
- **Exclusions** — what is explicitly out of scope
- **QA gate** — the check that must pass before the pack is "done"
- **Escalation triggers** — conditions that require partner judgment or a stop
- **Reusable templates / checklists** — the artifacts that make it repeatable

---

## Templates

Shared, fill-in artifacts live in [`templates/`](templates/), grouped by the pack that owns them.

**Blueprint (Pack 1)**

| Template | Purpose |
|----------|---------|
| [merchant-intake.md](templates/merchant-intake.md) | Discovery intake + merchant profile |
| [system-inventory.md](templates/system-inventory.md) | Current POS / ecommerce / back-office inventory (also feeds Pack 2) |
| [engagement-baseline.md](templates/engagement-baseline.md) | Minimum source-of-truth package consumed by Packs 2–5 |
| [implementation-scoping-brief.md](templates/implementation-scoping-brief.md) | Direct full-implementation scoping artifact after a qualified scoping call |
| [shopify-referral-scope-brief.md](templates/shopify-referral-scope-brief.md) | Shopify Referral exception path that produces the Baseline |
| [mixed-commerce-baseline-brief.md](templates/mixed-commerce-baseline-brief.md) | Multi-surface (DTC + POS + B2B + ERP/marketplace) Baseline producer; engine is `kaizen-architect` router + [full Mode 2 contract](skills/kaizen-architect.md#mode-2-integration-mapping) |
| [engagement-baseline-mixed-extension.md](templates/engagement-baseline-mixed-extension.md) | Append-only multi-surface extension to the Engagement Baseline |

**Activation / handover**

| Template | Purpose |
|----------|---------|
| [sales-to-delivery-handover.md](templates/sales-to-delivery-handover.md) | Internal, KaizenOS-derived handover brief after SOW acceptance; avoids re-keying sales facts |
| [client-activation-intake.md](templates/client-activation-intake.md) | Short client-facing pre-kickoff intake and secure-access status checklist |

**API-First Migration (Pack 2)**

| Template | Purpose |
|----------|---------|
| [migration-entity-map.md](templates/migration-entity-map.md) | Entity map (Part A) + per-entity field map (Part B) |
| [migration-runbook.md](templates/migration-runbook.md) | Phase-gated execution record |
| [dry-run-results.md](templates/dry-run-results.md) | Dry Run counts, errors, pass/fail |
| [reconciliation-checklist.md](templates/reconciliation-checklist.md) | Source vs Shopify reconciliation against approved tolerance |
| [cutover-plan.md](templates/cutover-plan.md) | The Kaizen Cutover phase plan + rollback (operational recovery) |
| [exception-log.md](templates/exception-log.md) | All errors / variances / open decisions |
| [b2b-account-migration-map.md](templates/b2b-account-migration-map.md) | B2B entity map: companies, locations, contacts, catalogs, price lists, terms, historical orders, plus the catalog-budget check against the merchant's plan |

**Launch QA (Pack 3)**

| Template | Purpose |
|----------|---------|
| [launch-qa-checklist.md](templates/launch-qa-checklist.md) | Per-location readiness gauntlet |
| [launch-test-pack.md](templates/launch-test-pack.md) | Staffed workflow + transaction tests (incl. gift card/store credit) |
| [b2b-launch-test-pack.md](templates/b2b-launch-test-pack.md) | B2B go-live tests: plan gate, buyer self-serve, rep-assisted, pricing resolution matrix, terms/AR, ERP handoff |
| [launch-ops-log.md](templates/launch-ops-log.md) | Go-live command center + hypercare issue log |
| [launch-signoff-form.md](templates/launch-signoff-form.md) | Per-location signoff by a named authority |

**Ops Care (Pack 4)**

| Template | Purpose |
|----------|---------|
| [monthly-ops-health-report.md](templates/monthly-ops-health-report.md) | Backbone monthly deliverable — folds in integration health, data hygiene, Flow maintenance, and account-health classification |
| [pos-operations-issue-log.md](templates/pos-operations-issue-log.md) | Recurring operational issues |
| [qbr-template.md](templates/qbr-template.md) | Quarterly business review |
| [expansion-opportunity-log.md](templates/expansion-opportunity-log.md) | Health-gated expansion tracking |

**Sales / SOW (Pack 5)**

| Template | Purpose |
|----------|---------|
| [sow-boundaries.md](templates/sow-boundaries.md) | Inclusion/exclusion/responsibility/cap/change-order/retainer blocks |
| [se-referral-one-pager.md](templates/se-referral-one-pager.md) | Shopify SE / AE referral asset |

---

## Output standard for every asset in this OS

Operational, not fluffy. Checklists, tables, and templates over prose. Confirmed facts, assumptions, and open questions kept visibly separate. Engagement Baseline provenance tags (`[BLUEPRINT-CONFIRMED]`, `[DISCOVERY-INFERRED]`, `[OPEN]`) are used internally where source confidence matters. Owner roles named, not just tasks. QA gates included. Exclusions and escalation triggers explicit. No invented data, no fabricated ROI, no Shopify technical claims that require current-documentation verification without a flag. Partner judgment owns final scope, pricing, migration lane, and QA signoff.

---

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
