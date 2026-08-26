# Asset Pack 2 — API-First Migration Package

Internal operating pack for the migration stage of the wedge. Turns an Engagement-Baseline-approved migration into a repeatable plan-and-execute system where **API-first is the default lane** and Matrixify or Shopify Admin CSV are *named, evidence-justified fallback lanes* — never the silent default. This is an internal operating document, not client marketing.

> **Source of truth:** the approved Engagement Baseline from Pack 1. The Baseline may be produced by a paid Blueprint, an Implementation Scoping Brief, or an approved Shopify Referral Scope Brief. Entity scope, data cap, risk register, source-of-truth decisions, launch constraints, and the indicative lane all come from it. This pack validates and executes against the Baseline; it does not redefine scope.

> **Partner judgment owns the final call** on migration lane, source-of-truth architecture, reconciliation tolerance, and cutover go/no-go. This pack recommends from evidence; the CTO signs off.

> **No invented platform behavior.** Do not assert Shopify API fields, scopes, constraints, POS behavior, gift-card behavior, store-credit behavior, metaobject behavior, or POS permission behavior from memory. Anything that needs confirmation is tagged `[FLAG: verify current Shopify docs before client commitment]`.

> **No "zero downtime" or "no lost data" claims.** Use the canonical Parallel Validation language: the legacy POS stays live until Shopify is proven, Dry Run precedes live cutover, and data is validated before cutover.

> **Use The Kaizen Cutover.** Migration planning follows the named cutover methodology:
> Shadow → Pilot Store → Verdict Gate → Waves → Hypercare. See
> [`reference/kaizen-cutover-methodology.md`](../reference/kaizen-cutover-methodology.md).

---

## Purpose

Plan and execute the data migration with a documented lane, a field-level map, a Dry Run before live, a reconciliation pass, a scoped cutover, and a recovery plan if cutover fails. Every step has an owner, a gate, and an escalation path so the CTO is not improvising under cutover pressure.

## Buyer / user

| Role | Owns |
|------|------|
| CTO | Lane decision, entity/field mapping, Dry Run, reconciliation sign-off, cutover go/no-go, rollback execution |
| CEO | Client communication, scope/change-order interface, cutover-window scheduling |
| Merchant owner | Source-system access, data validation, sign-off on Dry Run results and reconciliation |

## Required inputs

- Approved [engagement-baseline](templates/engagement-baseline.md), with source artifact named (Blueprint or Shopify Referral Scope Brief), indicative migration lane, named entity scope, data cap, risk register, and launch constraints
- Completed [system-inventory](templates/system-inventory.md) from Pack 1/referral intake with lane signals and data volumes
- Signed SOW with explicit data cap (Pack 5)
- Source-system access (credentials and/or export capability) confirmed
- A reconciliation tolerance decision from the partner — `[NEED: reconciliation tolerance]` until approved

## Deliverables

| # | Deliverable | Template |
|---|-------------|----------|
| 1 | Documented migration lane + reasoning | this pack (§1) |
| 2 | Entity & field map | [migration-entity-map](templates/migration-entity-map.md) |
| 3 | Data-quality assessment | this pack (§5) |
| 4 | Migration runbook | [migration-runbook](templates/migration-runbook.md) |
| 5 | Dry Run plan + results | [dry-run-results](templates/dry-run-results.md) |
| 6 | Reconciliation results | [reconciliation-checklist](templates/reconciliation-checklist.md) |
| 7 | Cutover & rollback plan | [cutover-plan](templates/cutover-plan.md) |
| 8 | Exception log | [exception-log](templates/exception-log.md) |

---

## The Kaizen Cutover phase map

This pack owns Shadow, Pilot Store, Verdict Gate, and the migration portions of Waves. Pack 3 owns
per-location launch QA and Hypercare handoff.

| Cutover phase | Pack 2 responsibility |
|---|---|
| Shadow | Build and validate the target data path while the legacy POS remains live. |
| Pilot Store | Prepare entity maps, Dry Run results, and reconciliation evidence for one representative location. |
| Verdict Gate | Present pass/hold/rework evidence: unresolved defects, variance decisions, open source-of-truth conflicts, and rollback path. |
| Waves | Provide repeatable runbooks and exception handling for each launch group. |
| Hypercare | Hand open migration exceptions to Pack 3 / Ops Care with owner and severity. |

---

## Section 1 — Migration lane decision tree

API-first is the default. A fallback lane is chosen only when a documented condition forces it, and the CTO signs off on the change. Record the decision and reasoning in the entity map. The lane may differ per entity (e.g. API for products, a fallback for one awkward legacy export).

```
START: every entity defaults to API-first
   │
   ├─ Is there reliable programmatic access to BOTH the source data and the
   │  Shopify Admin API for this entity, at the required volume?
   │        │
   │        ├─ YES ──► Does the entity have a current, documented Shopify API
   │        │          path for every field in scope?
   │        │              ├─ YES ──► API-FIRST (default). Proceed.
   │        │              └─ UNSURE ► [FLAG: verify current Shopify docs before
   │        │                          client commitment] then decide.
   │        │
   │        └─ NO ───► Why not? (no source API, throttling beyond window,
   │                   no field-level access, one-off legacy dump only)
   │                        │
   │                        ├─ Structured bulk export exists & entity is well
   │                        │  supported by Matrixify ──► MATRIXIFY (fallback)
   │                        │
   │                        └─ Small volume / simple entity / no better path
   │                           ──► SHOPIFY ADMIN CSV (fallback)
   │
   └─ Record: chosen lane + reason + any [FLAG] + CTO sign-off
```

### API-first default conditions (use API when all hold)

- Programmatic read access to the source entity at the required volume
- A current, documented Shopify Admin API write path for every in-scope field
- Volume and rate limits fit the cutover window with margin
- Field-level control is needed (transforms, idempotency keys, partial re-runs)

### Matrixify fallback conditions (choose Matrixify when)

- No usable source API, but a clean structured bulk export exists
- The entity is well-supported by Matrixify's documented import format
- Volume is large enough that spreadsheet-style bulk handling is more reliable than scripted API calls for this entity
- API path for the entity is uncertain — confirm against current Matrixify and Shopify docs `[FLAG: verify current Shopify docs before client commitment]`

### Shopify Admin CSV fallback conditions (choose Admin CSV when)

- Small or simple entity where native CSV import is sufficient
- No API access and the entity maps cleanly to Shopify's native CSV columns
- A one-time load where scripting or Matrixify is unjustified overhead

**Rule:** the lane is recommended from evidence in the entity map, but **final lane is CTO/partner sign-off.** Document why a fallback was chosen over API.

---

## Section 2 — Source-system access requirements

Confirm before any mapping. Missing access is an escalation trigger, not a problem to discover at cutover.

| Requirement | Owner | Status gate |
|-------------|-------|-------------|
| Source read access (API creds or export capability) per entity | Merchant owner → CTO | Confirmed before mapping |
| Shopify store admin access at the required permission level | Merchant owner → CTO | Confirmed before Dry Run |
| Representative sample export per entity | Merchant owner | Received before field mapping |
| Source-of-truth decision where the Engagement Baseline flagged a conflict | Partner + merchant | Decided before reconciliation design |
| Confirmation of history depth, gift-card, and store-credit scope | Merchant owner | Confirmed before Dry Run |

Do not assert what Shopify API scopes or permission levels are required from memory — confirm against current documentation and tag `[FLAG: verify current Shopify docs before client commitment]` where the exact scope matters to a commitment.

---

## Section 2A — Baseline validation gate

Before Dry Run, validate every migration-affecting Baseline field against source-system access, representative exports, or Shopify configuration. This is mandatory for Shopify Referral deals and still useful for Blueprint deals.

| Baseline tag | Treatment in Pack 2 |
|--------------|---------------------|
| `[BLUEPRINT-CONFIRMED]` | Sample-check and proceed through normal gates |
| `[DISCOVERY-INFERRED]` | Confirm against source exports/admin evidence before Dry Run if it affects entity scope, lane, cap, mapping, source-of-truth, gift cards/store credit, permissions, or history depth |
| `[OPEN]` | Blocks Dry Run when migration-affecting; may proceed only if explicitly excluded from scope or partner-accepted as a non-migration assumption |

Material deltas from the Baseline route back to Pack 5 before work proceeds: cap overage, entity added/removed, lane change, integration added, source-of-truth conflict, or unverified Shopify behavior that changes scope.

---

## Section 3 — Entity map workflow

Build the entity map from the Engagement Baseline and system-inventory. One row per entity, with lane, volume, key field, dependencies, provenance, and flags. Owner: CTO. Template: [migration-entity-map](templates/migration-entity-map.md).

1. List every in-scope entity from the Engagement Baseline (products, variants, collections, customers, orders, inventory, locations, metafields, metaobjects, and — if applicable — gift cards/store credit, discounts/promotions, staff/POS permissions).
2. For each, record source location, target, lane, volume, key field, and load-order dependency (e.g. products before inventory; customers before orders).
3. Mark any entity whose Shopify behavior is uncertain with `[FLAG: verify current Shopify docs before client commitment]`.
4. CTO signs off the lane per entity.

Entity coverage to assess every time: **products, variants, collections, customers, orders, inventory, locations, metafields, metaobjects, gift cards/store credit (if applicable), discounts/promotions (if applicable), staff/POS permissions (where applicable).** For gift cards, store credit, metaobjects, and POS permissions, do not assume migratability or behavior — verify and flag.

---

## Section 4 — Field mapping workflow

For each entity, map source field → Shopify target field, with transform, default, and validation rule. Owner: CTO. Template: [migration-entity-map](templates/migration-entity-map.md) (Part B — field map).

1. Pull the entity's in-scope fields from the sample export.
2. Map each to a Shopify target field. Where no current documented target is known, mark `[FLAG: verify current Shopify docs before client commitment]` rather than guessing a field name.
3. Define the transform (format, units, encoding), default value, and a validation rule per field.
4. Define the idempotency/match key so a partial re-run does not duplicate records.
5. Flag fields with no clean target as open decisions — do not silently drop data.

---

## Section 5 — Data-quality checklist

Run against sample exports before Dry Run. Findings feed the exception log and may trigger a change order if cleanup is out of scope.

- [ ] Every entity has a stable unique key; duplicates identified and a merge rule decided
- [ ] Required fields populated; missing-value handling defined per field
- [ ] Encoding/format consistent (dates, currency, units, character encoding)
- [ ] Referential integrity holds (orders reference real customers; variants reference real products)
- [ ] Volume per entity matches the SOW cap; overage exposure flagged to Pack 5 if near/over
- [ ] Gift card / store credit balances and status captured `[FLAG: verify current Shopify docs before client commitment]`
- [ ] Source-of-truth conflicts resolved or escalated
- [ ] Records out of scope explicitly excluded (not silently dropped)
- [ ] Cleanup the merchant must perform is listed and assigned

---

## Section 6 — Migration runbook

The ordered execution sequence. Owner: CTO. Template: [migration-runbook](templates/migration-runbook.md).

| Phase | Step | Gate before proceeding |
|-------|------|------------------------|
| Prep | Confirm access, finalize entity map + field maps, freeze scope | Data-quality checklist passed |
| Build | Implement load per entity in dependency order, with idempotency keys | Each loader tested on sample |
| Dry Run | Full load into a Shopify test/dev target; capture results | Dry Run plan executed (§7) |
| Validate | Reconcile Dry Run output vs source | Reconciliation within `[NEED: reconciliation tolerance]` |
| Fix | Resolve exceptions; re-run affected entities | Exception log cleared of Criticals |
| Cutover | Execute live load on the agreed window under Parallel Validation | Cutover plan approved (§8) |
| Confirm | Post-cutover reconciliation; legacy stays live until proven | Sign-off obtained |

Load-order dependencies (general): locations → products → variants → inventory; customers → orders; collections after products; metafields/metaobjects after their parent records. Confirm exact dependencies per build; do not assume Shopify ordering behavior `[FLAG: verify current Shopify docs before client commitment]` where it affects a commitment.

---

## Section 7 — Dry Run plan

Dry Run always precedes live. It is the evidence that the live cutover will behave. Owner: CTO. Template: [dry-run-results](templates/dry-run-results.md).

- Load the full in-scope dataset into a Shopify test/dev target (not the live store)
- Record per entity: source count, loaded count, error count, sample spot-checks
- Capture every error in the exception log with severity
- Compare against the reconciliation checklist (§9)
- Result is pass/fail against the partner-approved tolerance `[NEED: reconciliation tolerance]`
- A failed Dry Run blocks cutover until exceptions are resolved and re-run

---

## Section 8 — Cutover plan

The live load, executed under Parallel Validation. Owner: CTO executes, CEO manages client comms, merchant owner validates. Template: [cutover-plan](templates/cutover-plan.md).

- **Parallel Validation:** the legacy POS stays live and authoritative until Shopify is proven. Do not decommission legacy on cutover day.
- Confirmed cutover window inside any Engagement Baseline launch constraint (season, lease, fiscal close)
- Pre-cutover checklist: Dry Run passed, exceptions cleared, access confirmed, rollback plan ready
- Execute live load in runbook order; validate counts and spot-checks **before** declaring cutover complete
- Data is validated before cutover is called done — not after
- Named go/no-go owner (CTO) and a named merchant validator
- Hand off to Pack 3 (Launch QA) for per-location go-live

**No "zero downtime" claim.** The guarantee is that legacy remains the source of truth until the new system is validated.

---

## Section 9 — Reconciliation checklist

Proves the migrated data matches the source within the approved tolerance. Owner: CTO. Template: [reconciliation-checklist](templates/reconciliation-checklist.md).

- [ ] Per-entity counts compared: source vs Shopify
- [ ] Financial totals tied out where applicable (orders, refunds) — apply data-freshness defaults from [`reference/kaizen-data-freshness.md`](../reference/kaizen-data-freshness.md)
- [ ] Key-field spot checks on a sampled set per entity
- [ ] Referential integrity re-checked post-load
- [ ] Inventory quantities by location compared
- [ ] Variances classified and logged; each Critical resolved before cutover sign-off
- [ ] Result recorded against the approved tolerance `[NEED: reconciliation tolerance]`

Reconciliation tolerance is a **partner decision** unless already approved. Do not assume "exact match" or invent a percentage.

---

## Section 10 — Rollback definition (carefully scoped)

Rollback is an **operational recovery plan, not a platform guarantee.** It does not mean Shopify can revert everything to a prior state. Owner: CTO. Template: [cutover-plan](templates/cutover-plan.md) (Rollback section).

What rollback **is**:

- Because of Parallel Validation, the legacy POS is still live and authoritative; if cutover fails validation, operations continue on legacy
- A documented decision point: if post-cutover reconciliation fails the approved tolerance, declare the cutover not-accepted and keep running on legacy
- A defined set of recovery actions: halt the load, isolate the failed entities, correct, and re-run on the next window
- Clear ownership and communication: who calls it, who tells the locations, what the merchant does in the interim

What rollback is **not**:

- Not a claim that Shopify will automatically undo writes
- Not a promise of instant, total reversal of all migrated data
- Not a substitute for a passing Dry Run

The strongest rollback is a Dry Run that prevents needing one. State the recovery plan in operational terms; do not imply platform-level magic. Where reversing a specific Shopify write is in question, tag `[FLAG: verify current Shopify docs before client commitment]`.

---

## Section 11 — Exception log

Every error, variance, and open decision in one place. Owner: CTO. Template: [exception-log](templates/exception-log.md).

Each entry: ID, entity, description, severity (Critical / Important / Watch — see [`reference/kaizen-risk-matrix.md`](../reference/kaizen-risk-matrix.md)), owner, status, resolution. No Critical exception is open at cutover sign-off.

---

## QA gate

Migration output does not advance until all pass. Fix in place, then re-verify the whole list.

- [ ] Migration lane is named per entity, justified, and CTO-signed; API-first held as default
- [ ] Source artifact is named (Blueprint or Shopify Referral Scope Brief), and the approved Engagement Baseline is attached
- [ ] No migration-critical `[OPEN]` item remains unresolved before Dry Run
- [ ] No migration-critical `[DISCOVERY-INFERRED]` item remains unvalidated before Dry Run/cutover
- [ ] Every fallback (Matrixify / Admin CSV) has a documented condition behind it
- [ ] No Shopify API field, scope, constraint, or POS/gift-card/store-credit/metaobject/permission behavior asserted from memory; uncertain items tagged `[FLAG: verify current Shopify docs before client commitment]`
- [ ] Data-quality checklist passed; cleanup responsibilities assigned
- [ ] Dry Run executed and passed against the approved tolerance before any live cutover
- [ ] Reconciliation tolerance is partner-approved or marked `[NEED: reconciliation tolerance]`
- [ ] Reconciliation completed; no Critical variance open at sign-off
- [ ] Cutover plan uses Parallel Validation; data validated before cutover is called done
- [ ] Rollback defined as an operational recovery plan, not a platform guarantee; no "zero downtime"/"no lost data" claims
- [ ] Exception log has no open Critical at sign-off
- [ ] Any client-facing snippet tagged `[DRAFT — partner/legal review before client use]`

Final lane, tolerance, source-of-truth architecture, and cutover go/no-go remain partner judgment.

---

## Escalation triggers

Stop and bring in partner judgment when:

- Source-system access cannot be confirmed for an in-scope entity
- A Shopify Referral Baseline contains a migration-critical `[DISCOVERY-INFERRED]` or `[OPEN]` item that cannot be validated before Dry Run
- An entity's Shopify behavior is uncertain and a client commitment depends on it (`[FLAG]` unresolved)
- Data volume exceeds the SOW cap mid-migration (route to Pack 5 change order)
- A clean unique key does not exist for an entity and no merge rule is agreed
- Gift card / store credit / metaobject / POS permission migratability is unverified and in scope
- Dry Run fails and exceptions cannot be resolved within the cutover window
- Reconciliation tolerance is undecided at the point reconciliation must run
- A source-of-truth conflict has no owner decision
- Cutover validation fails and the rollback decision point is reached

---

## Reusable templates / checklists

- [migration-entity-map](templates/migration-entity-map.md) (entity + field map) · [migration-runbook](templates/migration-runbook.md) · [dry-run-results](templates/dry-run-results.md) · [reconciliation-checklist](templates/reconciliation-checklist.md) · [cutover-plan](templates/cutover-plan.md) (cutover + rollback) · [exception-log](templates/exception-log.md)

**Reference depth:** [`reference/kaizen-migration-playbooks.md`](../reference/kaizen-migration-playbooks.md) · [`reference/kaizen-platform-migrations.md`](../reference/kaizen-platform-migrations.md) · [`reference/kaizen-data-freshness.md`](../reference/kaizen-data-freshness.md) · [`reference/kaizen-risk-matrix.md`](../reference/kaizen-risk-matrix.md)

*Composes with kaizen-migrate, kaizen-dataprep, kaizen-matrixify-exec, kaizen-validate, kaizen-reconcile. Hands off to Pack 3 (Launch QA).*

---
*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
