# Template — Engagement Baseline

Minimum source-of-truth package consumed by Packs 2-5. The Engagement Baseline is produced by the paid Blueprint Diagnostic, the Implementation Scoping Brief, the approved Shopify Referral Scope Brief, or — for multi-surface merchants — the [Mixed Commerce Systems Baseline Brief](mixed-commerce-baseline-brief.md). Governed by [Pack 1 — Blueprint Diagnostic](../01-blueprint-diagnostic-pack.md).

> **Mixed Commerce engagements:** this base template is POS-shaped (one POS, one migration entity list, one launch). For two or more active commerce surfaces, also complete the append-only [Engagement Baseline — Mixed extension](engagement-baseline-mixed-extension.md) for surface inventory, cross-surface source-of-truth, per-surface lanes, launch sequence, and cross-surface risk. Downstream packs read the base plus the extension as one Baseline.

> Downstream packs need evidence, not a label. A merchant may skip the paid Blueprint deliverable only when a scoping brief or referral brief still captures entity scope, cap, lane, risk, launch, and source-of-truth decisions.

**Client:** ______  **Source artifact:** Blueprint / Implementation Scoping Brief / Shopify Referral Scope Brief  **Source date:** ______  **CEO sign-off:** ______  **CTO sign-off:** ______

## Provenance tags

| Tag | Meaning | Downstream treatment |
|-----|---------|----------------------|
| `[BLUEPRINT-CONFIRMED]` | Confirmed through the paid Blueprint, source-system evidence, export, or approved report | Standard gates apply |
| `[DISCOVERY-INFERRED]` | Inferred from AE context or discovery calls, not yet verified against source systems | May support a protected SOW if visible; must be validated before Dry Run/cutover when migration-affecting |
| `[OPEN]` | Unknown or undecided | Blocks the relevant gate until resolved or partner-accepted as a named assumption |

Use client-facing labels only when needed: Confirmed, Inferred, Open. Do not expose internal tags in polished client copy unless the artifact is explicitly internal.

## 1. Scope baseline

| Field | Value | Provenance | Owner | Notes |
|-------|-------|------------|-------|-------|
| Locations | | | | |
| Current POS | | | | |
| Shopify status | | | | |
| Recommended tier | | | | |
| Data cap | | | | |
| Overage exposure | Yes / No / Unknown | | | |
| Launch constraints | | | | |
| Named merchant owner | | | | |

## 2. Migration baseline

| Entity | In scope? | Volume | Lane | Provenance | Verification status | Notes |
|--------|-----------|--------|------|------------|---------------------|-------|
| Products | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Variants | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Collections | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Customers | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Orders | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Inventory | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Locations | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | |
| Metafields/metaobjects | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | `[FLAG: verify current Shopify docs before client commitment]` where behavior is uncertain |
| Gift cards / store credit | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | `[FLAG: verify current Shopify docs before client commitment]` |
| Staff / POS permissions | Yes / No / TBD | | API / Matrixify / CSV / TBD | | | `[FLAG: verify current Shopify docs before client commitment]` |

## 3. Source-of-truth decisions

| Domain | Current owner | Target owner | Conflict? | Provenance | Decision / next action |
|--------|---------------|--------------|-----------|------------|------------------------|
| Catalog | | | Yes / No | | |
| Inventory | | | Yes / No | | |
| Customers | | | Yes / No | | |
| Orders / financials | | | Yes / No | | |
| Reporting | | | Yes / No | | |

## 4. Operational risk register

| Risk | Severity (Critical/Important/Watch) | Provenance | Mitigation | Owner | Gate affected |
|------|--------------------------------------|------------|------------|-------|---------------|
| | | | | | Pre-SOW / Pre-Dry Run / Pre-cutover / Launch |

## 5. Retainer fit

| Signal | Retainer module / product | Named operational-continuity risk | Provenance | Include? |
|--------|---------------------------|-----------------------------------|------------|----------|
| | | | | Yes / No / Defer |

## 6. Assumption and flag ledger

| ID | Item | Tag | Affects | Owner | Required before | Resolution |
|----|------|-----|---------|-------|-----------------|------------|
| A-001 | | `[DISCOVERY-INFERRED]` / `[OPEN]` | SOW / migration / launch / retainer | | | |

## Baseline gates

### Pre-SOW gate
- [ ] Source artifact is named: Blueprint, Implementation Scoping Brief, or Shopify Referral Scope Brief
- [ ] Tier, migration lane, data cap, entity scope, launch constraints, and retainer fit are present
- [ ] All assumptions and `[FLAG]` items are visible in the assumption ledger
- [ ] Any `[OPEN]` item that affects price, cap, exclusion, or feasibility has a named owner and SOW treatment
- [ ] CTO signs the provisional migration lane and data cap before the SOW is sent
- [ ] If source artifact is Implementation Scoping Brief, scoping-call evidence covers delivery ownership, locations, stack, data/integration exposure, timeline, and open assumptions
- [ ] If source artifact is Shopify Referral Scope Brief, the referral context is partner-approved

### Pre-Dry Run / pre-cutover validation gate
- [ ] No migration-critical `[OPEN]` item remains unresolved
- [ ] No migration-critical `[DISCOVERY-INFERRED]` item remains unvalidated against source-system access, exports, or Shopify configuration
- [ ] Material deltas from the baseline have been routed to Pack 5 as change-order or SOW amendment decisions
- [ ] Current-doc verification flags that affect client commitments are resolved or excluded

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
