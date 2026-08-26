# Template — Mixed Commerce Systems Baseline Brief

Producer of the [Engagement Baseline](engagement-baseline.md) for **Mixed Commerce Systems** engagements — merchants who run two or more active commerce surfaces (DTC storefront, Shopify POS, B2B/wholesale, marketplace, ERP-backed operations) where source-of-truth and launch sequencing cross surface boundaries. Governed by [Pack 1 — Blueprint Diagnostic](../01-blueprint-diagnostic-pack.md). Engine: [`kaizen-architect`](../../skills/kaizen-architect.md) router + [full Mode 2 contract](skills/kaizen-architect.md#mode-2-integration-mapping) (Integration Map).

> The POS Blueprint and the Shopify Referral Scope Brief are POS-shaped: one POS, one migration entity list, one launch. Mixed Commerce is a multi-surface problem — the load-bearing decisions are the cross-surface source-of-truth map, the AnyDB operating-layer role, and the launch sequence. This brief captures those, then produces the standard Engagement Baseline plus the [Mixed extension](engagement-baseline-mixed-extension.md).

**Client:** ______  **Source artifact:** Blueprint (Mixed) / Shopify Referral (Mixed)  **Source date:** ______  **CEO sign-off:** ______  **CTO sign-off:** ______

---

## How this brief is produced

This is not a from-scratch diagnostic. It runs the architect engine and records the decisions:

1. **Run `kaizen-architect` Mode 2 (Integration Map)** against the merchant's stack. Mode 2 produces the surface-complexity classification, the Systems-in-Scope table with build-vs-buy verdicts, the cross-surface source-of-truth matrix, the integration map, the refresh protocol, and the AnyDB role decision. That is the engine output.
2. **Record the engine output into this brief** (Sections 2–5), tagging provenance.
3. **Add the two Mixed-only commercial decisions the architect does not own:** the implementation **sequence** (Section 6) and the cross-surface **risk gates** (Section 7).
4. **Produce the Engagement Baseline + Mixed extension** (Section 9), CTO-signed before any SOW.

Do not duplicate source-of-truth logic here. The architect Mode 2 reference chain ([`kaizen-surface-complexity.md`](../../reference/kaizen-surface-complexity.md), [`kaizen-build-vs-buy.md`](../../reference/kaizen-build-vs-buy.md), [`kaizen-data-freshness.md`](../../reference/kaizen-data-freshness.md), [`kaizen-signal-inference.md`](../../reference/kaizen-signal-inference.md), [`kaizen-erp-patterns.md`](../../reference/kaizen-erp-patterns.md)) owns it. This brief consumes the verdict.

Provenance tags follow [`kaizen-recommendation-confidence.md`](../../reference/kaizen-recommendation-confidence.md): `[BLUEPRINT-CONFIRMED]`, `[DISCOVERY-INFERRED]`, `[OPEN]`.

---

## 1. Lane confirmation gate (anti-misclassification)

Mixed Commerce is the most over-claimed lane. Confirm it before producing a multi-surface baseline. A merchant is Mixed **only** when both hold:

- [ ] **Two or more active commerce surfaces** are genuinely in scope (not "a storefront we might add later")
- [ ] At least one **cross-surface dependency** exists: shared inventory across channels, one customer who buys both DTC and B2B, price that must stay consistent across a storefront and a price list, or a launch where one surface cannot go live until another is resolved

If only one surface is real, **stop and route out** — do not over-build:

| Reality | Route to |
|---------|----------|
| One POS, multi-location migration | POS [Blueprint Diagnostic](../01-blueprint-diagnostic-pack.md) (standard producer) |
| DTC storefront only | DTC path → [`variants/shopify-dtc-commerce.md`](../../variants/shopify-dtc-commerce.md), Baseline via Blueprint |
| B2B/wholesale only | B2B path → [`variants/shopify-b2b-commerce.md`](../../variants/shopify-b2b-commerce.md), Baseline via Blueprint |
| AnyDB operations only | [`variants/anydb-operations-build.md`](../../variants/anydb-operations-build.md) |

State the confirmed surfaces and the cross-surface dependency in one line before continuing. If the cross-surface dependency is `[OPEN]`, that is a discovery gap, not a green light.

---

## 2. Commerce surface inventory

One row per active or in-scope surface. Source: architect Mode 2 Step 1 (System Inventory).

| Surface | In scope? | Status | Platform / system | Role in the business | Volume | Provenance |
|---------|-----------|--------|-------------------|----------------------|--------|------------|
| DTC storefront | Yes / No / TBD | None / Live / In-progress / Legacy | | | | |
| Shopify POS (retail) | Yes / No / TBD | None / Live / In-progress / Legacy | | | | |
| B2B / wholesale | Yes / No / TBD | None / Live / In-progress / Legacy | | | | |
| Marketplace(s) | Yes / No / TBD | None / Live / In-progress / Legacy | | | | |
| ERP / accounting backbone | Yes / No / TBD | — | | | | |
| WMS / 3PL / fulfillment | Yes / No / TBD | — | | | | |
| Custom / other surface | Yes / No / TBD | — | | | | |

**Surface-complexity classification** (architect Mode 2 Step 1b): Simple Retail / Growing Multi-Location / Complex Multi-Surface → ______. Every source-of-truth decision below must be consistent with this classification.

---

## 3. Cross-surface source-of-truth map

The core of a Mixed engagement. One owner per entity per surface, or an explicit split with a conflict rule. Source: architect Mode 2 Step 2 (Source-of-Truth Assignment). Never let two surfaces appear to own the same write path without a stated rule.

| Entity | Owner (system of truth) | Surfaces that read it | Split / lifecycle ownership | Conflict? | Provenance | Decision / next action |
|--------|-------------------------|-----------------------|-----------------------------|-----------|------------|------------------------|
| Product / catalog | | | | Yes / No | | |
| Price (retail) | | | | Yes / No | | |
| Price (B2B price lists) | | | | Yes / No | | |
| Inventory / availability | | | | Yes / No | | |
| Customer (DTC) | | | | Yes / No | | |
| Company / B2B account | | | | Yes / No | | |
| Order capture | | | | Yes / No | | |
| Payment / AR / deposits | | | | Yes / No | | |
| Fulfillment state | | | | Yes / No | | |
| Content / merchandising | | | | Yes / No | | |
| Reporting | | | | Yes / No | | |

**Build-vs-buy verdict per system** (architect Mode 2): NATIVE / THIRD-PARTY / CUSTOM BUILD / RETAIN & INTEGRATE — carried from the Systems-in-Scope table. No system in scope without a verdict.

---

## 4. AnyDB operating-layer role

Apply the AnyDB-first rule from [`kaizen-shopify-commerce-systems.md`](../../reference/kaizen-shopify-commerce-systems.md): for Mixed engagements, evaluate AnyDB as the operating-control layer **before** defaulting to native-only or app-only. Name one role or "not needed" with a reason — do not leave it implicit.

| Question | Answer | Provenance |
|----------|--------|------------|
| Is AnyDB in scope? | Yes / No | |
| Role (if yes) | Operational control layer / Exception queue / Approval workflow layer / Shared reference hub / Supplemental reporting workspace | |
| What records live in AnyDB | | |
| Which surfaces write into it | | |
| Which users act in it | | |
| What writes back out, under what control | | |
| If "not needed," why native/app-only is acceptable here | | |

AnyDB must have a specific job — workflow state, approvals, exception management, portal/account onboarding, cross-surface reconciliation, or role-based reporting. A passive copy of Shopify or ERP data is a redesign signal, not an AnyDB role.

---

## 5. Per-surface scope and migration lane

Each surface carries its own scope and migration lane. A DTC storefront migration, a POS migration, and a B2B build are three different lanes inside one engagement. API-first is the default lane; Matrixify and Admin CSV are named fallbacks.

| Surface | In scope this engagement? | Build vs migrate | Migration lane | Data cap | Key entities | Provenance | Flags |
|---------|---------------------------|------------------|----------------|----------|--------------|------------|-------|
| DTC storefront | Yes / No / TBD | Build / Migrate / Both | API / Matrixify / CSV / N-A | | | | |
| Shopify POS | Yes / No / TBD | Build / Migrate / Both | API / Matrixify / CSV / N-A | | | | `[FLAG: gift card / store credit — verify current Shopify docs]` where in scope |
| B2B / wholesale | Yes / No / TBD | Build / Migrate / Both | API / Matrixify / CSV / N-A | | | | `[FLAG: B2B companies / catalogs / price lists — verify current Shopify docs]` where in scope |
| Marketplace | Yes / No / TBD | Build / Migrate / Both | API / Matrixify / CSV / N-A | | | | |

Each in-scope lane is provisional until the CTO signs it. Migration-affecting `[DISCOVERY-INFERRED]` or `[OPEN]` items go to the Pack 2 validation gate per surface.

---

## 6. Implementation sequence (Mixed-specific)

The architect engine maps the systems; it does not decide go-live order. This is the Mixed-only commercial decision — record it explicitly, because sequencing wrong corrupts data across surfaces.

| Decision | Value | Provenance | Rationale |
|----------|-------|------------|-----------|
| Launch order | e.g. ERP/SoT resolution → POS → DTC → B2B | | |
| Parallel vs phased | Parallel / Phased / Mixed | | |
| Hard dependencies | e.g. inventory SoT must be authoritative before any sales channel goes live | | |
| Surfaces deferred to a later phase | | | |
| Sequencing risk if reordered | | | |

**Default discipline:** the surface that owns a shared entity (inventory, price, customer/company) is resolved and authoritative **before** the surfaces that consume it go live. Do not launch a second sales channel against an inventory source that is not yet the agreed system of truth.

---

## 7. Cross-surface risk gates

Risks that exist only because surfaces interact. Score with Pack 1's Likelihood × Impact model (Critical 6–9 / Important 3–4 / Watch 1–2).

| Cross-surface risk | Surfaces involved | Severity | Provenance | Mitigation | Owner | Gate affected |
|--------------------|-------------------|----------|------------|------------|-------|---------------|
| Double-sell of shared stock across channels | POS + DTC + marketplace | | | | | Pre-cutover / Launch |
| Price drift across storefront and B2B price lists | DTC + B2B | | | | | Pre-SOW / Pre-launch |
| Customer identity collision (same buyer DTC + B2B) | DTC + B2B | | | | | Pre-Dry Run |
| Inventory promise mismatch (availability vs reality) | All sales surfaces | | | | | Pre-cutover |
| Order/financial double-count across surfaces in reporting | All + ERP/accounting | | | | | Pre-launch |
| Fulfillment routing ambiguity across channels | Sales surfaces + WMS/3PL | | | | | Pre-launch |

Add merchant-specific cross-surface risks surfaced in discovery. Single-surface risks belong in the standard Pack 1 risk register, not here.

---

## 8. Commercial path

| Item | Rule |
|------|------|
| Commercial lane | **Mixed Commerce Systems Implementation** — requires an approved price. Do not use POS location tiers (Silver/Gold/Diamond) as a shortcut unless POS migration is the lead scope. Pull pricing from [`reference/kaizen-pricing.md`](../../reference/kaizen-pricing.md) or mark `[NEED: approved commerce systems price]`. |
| Commercial lane | Blueprint/advisory, scoped full implementation, or Shopify Referral may produce the Baseline, but none can skip this brief's surface inventory, cross-surface SoT, lanes, sequence, and risk gates. |
| Blueprint credit | Shown only if a Blueprint fee was actually charged. |
| Retainer fit | Mixed engagements usually carry more integration surface area; assess Ops Care fit per surface, tied to named cross-surface continuity risks. |

---

## 9. Required output

- [ ] Completed [Engagement Baseline](engagement-baseline.md) (shared scope, risk, retainer, assumption ledger)
- [ ] Completed [Engagement Baseline — Mixed extension](engagement-baseline-mixed-extension.md) (surface inventory, cross-surface SoT, per-surface lanes, sequence, cross-surface risks)
- [ ] Architect Mode 2 Integration Map attached or referenced as the SoT/integration source artifact
- [ ] CTO signed the cross-surface source-of-truth map, every in-scope per-surface lane, and the launch sequence before any client SOW
- [ ] Pack 2 validation gate lists every migration-affecting inferred/open item, **per surface**

---

## Client responsibilities

- Name an internal owner with authority across all in-scope surfaces, not one per silo with no decision power
- Grant read access to each surface's admin and the back-office systems (ERP/accounting/WMS) feeding them
- Confirm which surface is authoritative for shared entities today, even where it is messy
- Supply representative exports per surface when requested
- Make the proceed / sequence decision after the baseline is delivered

---

## Exclusions

This brief is a diagnostic-and-architecture producer. It does **not** include:

- Any migration, build, or configuration on any surface
- Any AnyDB build or schema implementation (that is `kaizen-anydb-build` after an approved spec)
- The full AnyDB technical spec (that is `kaizen-architect` Mode 1)
- Guaranteed implementation pricing beyond indicative ranges (final price in the proposal/SOW, Pack 5)
- Launch-date commitments (the sequence is indicative until the SOW)

---

## QA gate

The Mixed baseline does not ship until all pass. Fix in place and re-verify the whole list.

- [ ] Lane confirmation gate passed: ≥2 active surfaces and a named cross-surface dependency; otherwise routed out
- [ ] Surface inventory complete; surface-complexity classification stated
- [ ] Cross-surface source-of-truth map assigns one owner (or explicit split + conflict rule) for every entity; no shared write path is unowned
- [ ] Every system in scope has a build-vs-buy verdict
- [ ] AnyDB role is named explicitly, or "not needed" is justified against the AnyDB-first rule
- [ ] Each in-scope surface has its own lane; API-first default honored; fallbacks named
- [ ] Implementation sequence is stated with hard dependencies and sequencing risk
- [ ] Cross-surface risk gates scored; Critical items called out
- [ ] Commercial lane is Mixed Commerce Systems (approved price), not a POS-tier shortcut
- [ ] Confirmed / inferred / open are visibly separated; no assumption presented as fact
- [ ] Any Shopify behavior needing current-docs verification is flagged, not asserted (B2B catalogs/price lists, gift card/store credit, metaobjects, POS permissions)
- [ ] No invented data, no fabricated ROI
- [ ] Engagement Baseline + Mixed extension produced and CTO-signed

For a Shopify Referral (Mixed) exception, replace the client-facing Blueprint report gate with the referral exception approval, but keep both baseline gates. No downstream pack starts without a signed Baseline.

---

## Escalation triggers

Stop and bring in partner judgment when:

- No internal owner has authority across surfaces (silo owners with no cross-surface decision power)
- A shared entity (inventory, price, customer/company) has no agreed system of truth and the merchant cannot decide
- Two surfaces must both own the same write path and no conflict rule is acceptable to the merchant
- The launch sequence forces a sales channel live against an unresolved inventory or price source of truth
- A Critical (6–9) cross-surface risk has no viable mitigation
- ERP or marketplace behavior the architecture depends on cannot be verified
- The merchant insists on a fixed multi-surface quote before the source-of-truth map exists

---

## Reusable templates / references

- [engagement-baseline.md](engagement-baseline.md) — shared source-of-truth package (Packs 2–5)
- [engagement-baseline-mixed-extension.md](engagement-baseline-mixed-extension.md) — multi-surface extension
- [`kaizen-architect.md`](../../skills/kaizen-architect.md) router + [full Mode 2 contract](skills/kaizen-architect.md#mode-2-integration-mapping) — the integration-map engine
- [`kaizen-shopify-commerce-systems.md`](../../reference/kaizen-shopify-commerce-systems.md) — Mixed lane definition, AnyDB-first rule, output contract
- [`kaizen-surface-complexity.md`](../../reference/kaizen-surface-complexity.md), [`kaizen-build-vs-buy.md`](../../reference/kaizen-build-vs-buy.md) — classification + verdict frameworks
- Risk scoring model — Pack 1 (Likelihood × Impact)

---

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
