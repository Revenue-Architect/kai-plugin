# Template — Engagement Baseline, Mixed Commerce Extension

**Append-only extension. Use *with* [engagement-baseline.md](engagement-baseline.md), not instead of it.** The base Engagement Baseline owns the shared fields (scope, risk register, retainer fit, assumption ledger, baseline gates). This extension adds only the structures a multi-surface engagement needs and the base — which is POS-shaped — does not carry. Produced by the [Mixed Commerce Systems Baseline Brief](mixed-commerce-baseline-brief.md). Governed by [Pack 1 — Blueprint Diagnostic](../01-blueprint-diagnostic-pack.md).

> Do not fork the base baseline. Fill the base for everything shared; fill this for everything cross-surface. Downstream packs read both as one Baseline.

**Client:** ______  **Attached to base Baseline dated:** ______  **CTO sign-off (SoT map + lanes + sequence):** ______

Provenance tags as in the base baseline: `[BLUEPRINT-CONFIRMED]`, `[DISCOVERY-INFERRED]`, `[OPEN]`.

## M1. Surface inventory

| Surface | In scope? | Status | Platform / system | Volume | Provenance |
|---------|-----------|--------|-------------------|--------|------------|
| DTC storefront | Yes / No / TBD | None / Live / In-progress / Legacy | | | |
| Shopify POS | Yes / No / TBD | None / Live / In-progress / Legacy | | | |
| B2B / wholesale | Yes / No / TBD | None / Live / In-progress / Legacy | | | |
| Marketplace(s) | Yes / No / TBD | None / Live / In-progress / Legacy | | | |
| ERP / accounting | Yes / No / TBD | — | | | |
| WMS / 3PL | Yes / No / TBD | — | | | |

**Surface-complexity classification:** Simple Retail / Growing Multi-Location / Complex Multi-Surface → ______

## M2. Cross-surface source-of-truth map

Extends Section 3 of the base baseline (5-row SoT) to the full multi-surface entity set. One owner per entity, or an explicit split with a conflict rule.

| Entity | Owner (system of truth) | Surfaces that read it | Split / lifecycle ownership | Conflict rule | Provenance |
|--------|-------------------------|-----------------------|-----------------------------|---------------|------------|
| Product / catalog | | | | | |
| Price (retail) | | | | | |
| Price (B2B price lists) | | | | | |
| Inventory / availability | | | | | |
| Customer (DTC) | | | | | |
| Company / B2B account | | | | | |
| Order capture | | | | | |
| Payment / AR / deposits | | | | | |
| Fulfillment state | | | | | |
| Content / merchandising | | | | | |
| Reporting | | | | | |

## M3. Per-surface migration / build lane

Extends Section 2 of the base baseline. Each surface carries its own lane and cap.

| Surface | In scope? | Build / migrate | Lane (API / Matrixify / CSV) | Data cap | Provenance | Verification status | Flags |
|---------|-----------|-----------------|------------------------------|----------|------------|---------------------|-------|
| DTC storefront | Yes / No / TBD | | | | | | |
| Shopify POS | Yes / No / TBD | | | | | | `[FLAG: gift card / store credit]` |
| B2B / wholesale | Yes / No / TBD | | | | | | `[FLAG: companies / catalogs / price lists]` |
| Marketplace | Yes / No / TBD | | | | | | |

## M4. Implementation sequence

| Field | Value | Provenance |
|-------|-------|------------|
| Launch order | | |
| Parallel vs phased | Parallel / Phased / Mixed | |
| Hard dependencies | | |
| Deferred surfaces | | |
| Sequencing risk if reordered | | |

## M5. Cross-surface risk register

Cross-surface risks only. Single-surface risks stay in Section 4 of the base baseline.

| Cross-surface risk | Surfaces | Severity (Critical/Important/Watch) | Provenance | Mitigation | Owner | Gate affected |
|--------------------|----------|--------------------------------------|------------|------------|-------|---------------|
| | | | | | | Pre-SOW / Pre-Dry Run / Pre-cutover / Launch |

## M6. AnyDB operating-layer role

| Question | Answer | Provenance |
|----------|--------|------------|
| In scope? | Yes / No | |
| Role | Operational control / Exception queue / Approval / Reference hub / Reporting / Not needed | |
| Records / writers / readers | | |
| Writes back out under what control | | |

## Mixed extension gates

### Pre-SOW gate (in addition to the base baseline Pre-SOW gate)
- [ ] Every cross-surface shared entity (inventory, price, customer/company) has one named owner or an explicit split + conflict rule
- [ ] Every in-scope surface has its own lane and cap
- [ ] Implementation sequence is stated with hard dependencies
- [ ] CTO signed the cross-surface SoT map, per-surface lanes, and sequence
- [ ] Commercial lane is Mixed Commerce Systems (approved price), not a POS-tier shortcut

### Pre-Dry Run / pre-cutover gate (per surface)
- [ ] No migration-critical `[OPEN]` or unvalidated `[DISCOVERY-INFERRED]` item remains on any surface going live in this phase
- [ ] No sales surface goes live against a shared entity whose source of truth is not yet authoritative
- [ ] Current-doc verification flags affecting client commitments are resolved or excluded, per surface

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
