# Asset Pack 5 — Sales / SOW Pack

Internal operating pack for the wedge: **multi-location Shopify POS transformation with scoping, Blueprint/advisory, full implementation, API-first migration, launch QA, and Ops Care.** This pack lets KaizenCommerce qualify, sell, scope, protect, and hand off the wedge without partner improvisation. It is an internal operating document, not a landing page, brochure, or sales deck.

> **Pricing is referenced, not duplicated.** Every dollar figure, tier deliverable, retainer price, and overage clause is canonical in [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md). Load it for any commercial artifact. This pack names tiers and shows the *shape* of the economics; it does not restate price tables. Pricing-usage rules: [`reference/kaizen-pricing-usage-standard.md`](../reference/kaizen-pricing-usage-standard.md).

> **Client-facing snippets in this pack are marked `[DRAFT — partner/legal review before client use]`.** Do not paste them into a client document without partner sign-off, and never invent payment, warranty, or legal terms.

---

## Purpose

Turn scoped evidence into a sold, scoped, and protected engagement. Pack 5 governs the commercial layer: how the wedge is explained internally, how a prospect is qualified, how the two commercial lanes are chosen, how Shopify Referral context is controlled, how the proposal and SOW are assembled from source-of-truth outputs, and how the retainer is attached by default.

Every proposal and SOW **derives from scoped evidence**: an approved Engagement Baseline, Blueprint Diagnostic, Implementation Scoping Brief, or partner-approved Shopify Referral Scope Brief. The source must cover tier/path, migration lane, data cap, risk register, recommendation matrix, and retainer fit.

## Buyer / user

| Role | Owns | In this pack |
|------|------|--------------|
| CEO | Sales, qualification, scoping, proposal narrative, SOW assembly, retainer attach | Primary owner of every section |
| CTO | Migration lane confirmation, technical exclusions, data-cap feasibility, doc-verification flags | Reviews proposal/SOW technical scope before send |
| Merchant owner (client) | Economic decision, data accuracy, SOW signature, access | Receives proposal, SOW, retainer offer |

## Required inputs

An approved [engagement-baseline](templates/engagement-baseline.md) (Pack 1) supplying:

- Recommended tier (Silver / Gold / Diamond, or a Commerce Systems path)
- Named migration lane (API-first default; Matrixify / Admin CSV only as fallback)
- Data cap and overage exposure
- Scored Risk Map
- Launch plan for POS migration using buyer-facing rollout language; internal cutover-method
  evidence stays in Pack 2/3 execution artifacts
- Implementation recommendation matrix (tier + operational workflow build + retainer fit, net investment shown)
- Retainer fit assessment with named operational-continuity risks
- Source artifact: Blueprint Diagnostic, Implementation Scoping Brief, or Shopify Referral Scope Brief
- Assumption/flag ledger using `[BLUEPRINT-CONFIRMED]`, `[DISCOVERY-INFERRED]`, and `[OPEN]`

If any input is missing, the proposal is not ready. Mark the gap `[NEED: <input> from Engagement Baseline]` and route back to Pack 1.

## Deliverables

| # | Deliverable | Audience | Source |
|---|-------------|----------|--------|
| 1 | Internal wedge one-pager | Internal | This pack |
| 2 | Qualification question bank | Internal | This pack |
| 3 | Two-lane objection handling | Internal | This pack + [`reference/kaizen-sales-os.md`](../reference/kaizen-sales-os.md) |
| 4 | Proposal | Client | Engagement Baseline recommendation matrix + [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md) |
| 5 | SOW with inclusion / exclusion / responsibility / cap blocks | Client | [`templates/sow-boundaries.md`](templates/sow-boundaries.md) |
| 6 | Change-order trigger list | Internal + Client | This pack |
| 7 | Retainer attach offer | Client | [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md) |
| 8 | Shopify SE referral brief | Partner / AE | [`templates/se-referral-one-pager.md`](templates/se-referral-one-pager.md) |

---

## Section 1 — Internal wedge one-pager

Internal reference. The shared mental model every partner uses when talking about the wedge.

**What it is.** A retailer moving to Shopify POS, run as an operational launch, not a data import.
KaizenCommerce has two commercial lanes: Blueprint Diagnostic + Advisory, KaizenCommerce's paid
pre-implementation audit and launch plan for capable internal teams, and full implementation for
merchants that need Shopify POS delivery, operational coverage, existing-stack integrations, and
workflow builds around store operations.

**Who it's for.** ICP: $2M–$20M top-line, 2–20+ retail locations, on legacy POS
(Lightspeed, Square, Heartland, Teamwork, custom), already on or evaluating Shopify, owner/COO
accessible, prior tech investment. Pain signal: POS and back-office do not talk: overselling,
manual counts, spreadsheet ops, Special Orders workflow, robust inventory management,
customizable Purchase Order flows, or store-team workflow issues.

**Why us.** CTO is ex-Shopify (Logistics division, pre-divestiture). Direct knowledge of how
Shopify infrastructure makes decisions. We validate data and store workflows before launch, test
with a representative store before broader rollout, keep the legacy POS available until Shopify is
proven, and avoid a planned store-closing cutover.

**How it's sold.** Start with a scoping conversation, then choose the lane. Define Blueprint in
client or partner language as KaizenCommerce's paid pre-implementation audit and launch plan.
Use Blueprint Diagnostic + Advisory when the merchant has a capable internal team or unclear risk.
Use full implementation when the merchant wants KaizenCommerce to own delivery and the scoping call
establishes the scope. Operational workflow build and retainer are recommended from scoped
evidence, never quoted cold.

**What it is not.** Not a "Shopify POS setup." Not a single-location or sub-$2M engagement. Not a fixed price before diagnosis. Not a dev shop taking arbitrary build tickets.

**The revenue shape.** Blueprint/advisory or approved Shopify Referral Baseline → self-implementation
guidance or full Shopify POS implementation → operational workflow layer where justified → retainer
attached by default. Sequence economics live in [`reference/kaizen-sales-os.md`](../reference/kaizen-sales-os.md)
and [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md).

**One-line positioning (internal):** "We help retailers launch Shopify POS without making store
teams the first real test. Capable internal teams use us for the paid audit and launch plan;
merchants that need delivery use us for full implementation, existing-stack integrations, and the
operational workflow layer around store operations."

---

## Section 2 — Qualification question bank

Run before booking Blueprint/advisory or accepting a full implementation path. Goal: confirm ICP fit and surface the economic buyer. Score each block; a hard fail in Fit or Authority disqualifies or pauses. Owner: CEO.

### Block A — Fit (must pass)

| # | Question | Disqualifier |
|---|----------|--------------|
| A1 | How many retail locations do you operate, and what types? | Single location / sub-complexity |
| A2 | What POS are you on today, and how long? | Already on Shopify POS and happy (no migration) |
| A3 | Roughly what's your annual top-line? | Below ~$2M |
| A4 | Are you on Shopify for ecommerce, or evaluating it? | No Shopify intent at all |

### Block B — Pain (qualifies depth)

| # | Question | What it reveals |
|---|----------|-----------------|
| B1 | Where do POS and inventory disagree today? | Core wedge pain |
| B2 | How many hours/week go to reconciliation or manual counts? | Quantified cost (client's own number) |
| B3 | How often do you oversell, and what does it cost you? | Severity |
| B4 | Where does operational data actually live — spreadsheets, email, tools? | Operational workflow signal |
| B5 | What broke last time you changed systems? | Risk + trust posture |

### Block C — Authority & readiness (must pass)

| # | Question | Disqualifier |
|---|----------|--------------|
| C1 | Who signs off on a technology investment like this? | Decision-maker not accessible |
| C2 | Who internally would own this day-to-day during the project? | No named internal owner |
| C3 | Have you invested in retail technology before? | No budget posture |
| C4 | What's forcing the timing — lease, season, contract end? | No real driver (deprioritize) |
| C5 | When does the current POS contract renew or terminate? | Unknown renewal date on active migration opportunity |
| C6 | What seasonal, fiscal-close, staffing, or event windows are off-limits for launch? | Unknown blackout window on active migration opportunity |

### Block D — Commercial posture (informs framing, not a gate)

| # | Question | Use |
|---|----------|-----|
| D1 | How are you thinking about budget for fixing this? | Frame Blueprint as low-risk entry |
| D2 | Is this a "this quarter" problem or a "someday" problem? | Pipeline priority |

**Qualification verdict:** Pass Fit + Authority + clear delivery ownership need → book a scoping call and prepare an Implementation Scoping Brief. Pass Fit + Authority but unclear risk or strong internal team → sell Blueprint Diagnostic + Advisory. Fail Fit → decline or refer. Pass Fit, weak Pain → keep diagnosing before proposing. Authority gap → resolve before booking.

---

## Section 3 — Two-lane objection handling

Hold the line against blind quotes, not against full implementation as a lane. Full implementation can be priced after a scoping call when the merchant wants KaizenCommerce to own delivery and the scope evidence is sufficient. Blueprint Diagnostic + Advisory is the right lane for capable internal teams or unclear risk. Deeper objection scripts: [`reference/kaizen-sales-os.md`](../reference/kaizen-sales-os.md).

| Objection | Internal response strategy |
|-----------|----------------------------|
| "Just send me a quote for the migration." | Do not quote blind. If they want KaizenCommerce to own delivery, book the scoping call and price against locations, data, integrations, timeline, and assumptions. If they have a capable internal team or unclear risk, the Blueprint Diagnostic + Advisory path produces the implementation number and the merchant owns the report either way. |
| "Why pay for a diagnostic? Other agencies scope free." | Use Blueprint only when diagnostic depth is the right lane: internal team enablement, unclear risks, or a merchant that wants a written launch plan before committing. If they want KaizenCommerce to own delivery and the scoping call gives enough evidence, move to scoped implementation instead of forcing a diagnostic. |
| "We already know what we need — just do it." | If scope evidence is real, use the implementation lane. If it is only confidence without data, expose the unknowns: dirty export, gift-card liability, integration source of truth, hardware readiness, or launch constraints. Those need a scoping brief or Blueprint before SOW. |
| "How do I know you won't break our stores?" | We do not ask the stores to learn the new workflow for the first time on launch day. We validate data and workflows before launch, test with a representative store before broader rollout, keep the legacy POS available until Shopify is proven, and score the exact risks up front. |
| "The Blueprint fee feels like an extra cost." | It is not additive if the project proceeds. It credits against implementation. Show gross → Blueprint credit → net (Section 4). If KaizenCommerce fails to deliver the promised diagnostic artifacts, the Blueprint fee is refundable; the guarantee is diagnostic-only. |
| "Can you guarantee the implementation price now?" | Indicative tier range now, firm price in the proposal *after* the Engagement Baseline defines cap and lane. A firm number before diagnosis is either inflated or unprotected. |

**Rule:** never present implementation pricing before the merchant has verbalized the cost of their current problem and the scope evidence is sufficient. Reframe price against that cost; do not discount.

---

## Section 3A — Shopify Referral exception path

Use only when the merchant is referred by Shopify and a partner approves bypassing the paid Blueprint deliverable. The exception is not a cold-quote lane. It is a compressed evidence lane.

Required referral artifacts:

- [shopify-referral-scope-brief](templates/shopify-referral-scope-brief.md)
- [engagement-baseline](templates/engagement-baseline.md)
- Completed or attached merchant-intake and system-inventory
- AE context and discovery-call notes
- Assumption/flag ledger with provenance tags
- CTO sign-off on provisional lane and data cap before the client SOW is sent

Two gates apply:

| Gate | Purpose | Rule |
|------|---------|------|
| Pre-SOW Baseline Gate | Enough evidence exists to price, cap, exclude, and protect scope | `[DISCOVERY-INFERRED]` items can remain only if visible, owned, and treated as assumptions/exclusions |
| Pre-Dry Run / pre-cutover validation gate | Enough evidence exists to execute safely | No migration-critical `[DISCOVERY-INFERRED]` or `[OPEN]` item remains unresolved |

Referral economics variant: do not show a Blueprint credit unless the Blueprint fee was actually charged. If Shopify referral terms affect economics, mark them `[NEED: partner/legal review]` and do not invent payment or referral-fee terms.

---

## Section 4 — Proposal outline

The proposal is client-facing and assembled **entirely from the approved Engagement Baseline**. Owner: CEO drafts, CTO reviews technical scope. Composes with `kaizen-propose` and `kaizen-invoice-exec`.

| § | Section | Content | Source |
|---|---------|---------|--------|
| 1 | Cover | Merchant, "Implementation Proposal," date, confidential | — |
| 2 | What we found | 3–5 Baseline findings in operator language; lead with the cost of current state | Baseline summary + Risk Map |
| 3 | Recommended path | Tier + operational workflow build (if any) + migration lane, named explicitly | Baseline recommendation matrix |
| 4 | Scope | What the engagement covers, by stage | SOW inclusion block (Section 5) |
| 5 | Data cap & overage | Explicit cap + overage/change-order clause | Section 7 + [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md) |
| 6 | Migration approach | API-first lane (or named fallback) + buyer-facing launch plan; flag any doc-verify items | Baseline lane recommendation + Cutover Plan |
| 7 | Investment | Net-investment block (below) | [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md) |
| 8 | Retainer | Ops Care attach, tied to named risks | Section 9 + [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md) |
| 9 | Timeline | Indicative per-tier window, phased | [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md) |
| 10 | Next step | Signature + kickoff (Pack 1 → onboarding) | — |

### Net-investment block (required format)

For Blueprint-sourced Baselines, show the three-line shape. Pull real figures from [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md); never hardcode them here.

```
Gross implementation fee ........  [tier fee — from kaizen-pricing.md]
Less Blueprint credit ...........  −[Blueprint fee already paid]
Net investment ..................  [gross − credit]
```

`[DRAFT — partner/legal review before client use]`
> Your Blueprint fee credits in full against this implementation. The figure below is net of that credit. Final fee assumes data within the stated cap; volume above the cap is handled by change order (see Data cap).

For Shopify Referral Baselines where no Blueprint fee was charged, use the referral variant:

```
Implementation fee .............  [approved fee — from kaizen-pricing.md or partner-approved quote]
Blueprint credit ...............  N/A — no Blueprint fee charged
Net investment ..................  [implementation fee]
```

**Rules:** if pricing is not yet approved for the path (e.g. DTC/B2B Commerce Systems), use `[NEED: approved price]` rather than inventing a number. Never fabricate ROI — use only the merchant's own quantified pain (Block B) or a clearly-labeled conservative estimate.

---

## Section 5 — SOW inclusion block

Reusable client-facing draft. Assemble from the Engagement Baseline recommendation matrix and the tier deliverables in [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md). Full template: [`templates/sow-boundaries.md`](templates/sow-boundaries.md). Owner: CEO assembles, CTO confirms technical lines.

`[DRAFT — partner/legal review before client use]`

This engagement includes, for the **[tier]** scope:

- Discovery and source-of-truth findings carried into delivery
- Migration of in-scope entities via the **[named lane — API-first / Matrixify / Admin CSV]**, up to the stated **data cap**
- In-scope entities: products, variants, collections, customers, orders, inventory, locations, metafields/metaobjects as defined in the Engagement Baseline entity scope
- Gift card / store credit migration *(where the Engagement Baseline/Pack 2 confirmed feasibility — flag if unverified)*
- Multi-location configuration and per-location launch QA
- Staff permissions configuration and the tier's training allotment
- Dry Run before live cutover; buyer-facing launch plan; legacy POS stays live until proven
- Reconciliation and a launch signoff (Pack 3)
- The retainer offer attached per Section 9

Each line must trace to an Engagement Baseline finding or the tier deliverable list. Do not include a line the Baseline did not scope.

---

## Section 6 — SOW exclusion block

Reusable client-facing draft. Protects scope. Owner: CEO + CTO.

`[DRAFT — partner/legal review before client use]`

This engagement does **not** include, unless added by change order:

- Data beyond the stated cap (handled per Data cap, Section 7)
- Source-system cleanup the merchant does not authorize or perform
- Net-new catalog creation, enrichment, or photography (vs migration of existing records)
- Migration lane change after the lane is set (e.g. API-first to a fallback) where caused by source-system access the merchant cannot provide
- Integrations the merchant declines to enable, or third-party apps outside the named app list
- Custom development beyond the named operational workflow build scope
- Historical order migration beyond the tier's included depth
- Hardware procurement outside the agreed device list
- Any Shopify behavior flagged for current-documentation verification until verified by the CTO
- Training beyond the tier's included allotment

---

## Section 7 — Client responsibility block

Reusable client-facing draft. The engagement assumes these; absence becomes an escalation trigger. Owner: CEO.

`[DRAFT — partner/legal review before client use]`

The client is responsible for:

- A named internal owner with authority and availability through the engagement
- Read/admin access to current POS, Shopify admin, and relevant back-office systems
- Representative data exports and sample files on request
- Timely validation of Dry Run results and reconciliation, and launch signoff
- Confirming history-depth and gift-card/store-credit requirements before migration
- Staff availability for per-location workflow testing at go-live
- Decisions on integration source-of-truth where the Engagement Baseline flagged a conflict
- Authorizing any change order before out-of-scope work proceeds

---

## Section 8 — Data cap language

Every SOW states the cap explicitly and carries the overage clause. Canonical clause: [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md) (Standard Overage Language). Cap is set from the Engagement Baseline data profile.

`[DRAFT — partner/legal review before client use]`
> This engagement includes migration of up to **[included limit]** products/customers. If the final export exceeds that threshold, we will issue a change order covering additional mapping, QA, and import workload, which may affect both project fee and delivery timeline.

**Rules:** the cap is a number, not "reasonable volume." If the Engagement Baseline shows the merchant is near or over the cap, name the overage exposure in the proposal up front rather than discovering it mid-build. Never promise fixed scope without a cap.

---

## Section 9 — Change-order triggers

When reality diverges from the SOW, a change order fires before work proceeds. Composes with `kaizen-scope`. Owner: CEO issues, CTO sizes the technical delta.

| Trigger | Action |
|---------|--------|
| Final export exceeds the data cap | Change order: additional mapping, QA, import; may move fee and timeline |
| Scope added beyond the inclusion block | Change order sized against the original proposal |
| Migration lane forced to change due to source access | Change order if the fallback lane adds mapping/QA work |
| Net-new catalog / enrichment requested | Change order; this is creation, not migration |
| Additional integration or app brought into scope | Change order: mapping, source-of-truth, monitoring |
| History depth requested beyond tier inclusion | Change order |
| Operational workflow scope expands beyond named build | Change order or separate build SOW |
| Out-of-scope request mid-engagement | Pause, document, change order before proceeding |
| A flagged Shopify behavior proves to require unscoped work after verification | Change order, with the verification outcome attached |

**Rule:** no out-of-scope work proceeds on goodwill. Document the trigger, size it, get authorization.

---

## Section 10 — Retainer attach language

Ops Care is attached **by default** to every implementation proposal — the build and the partnership that keeps it alive, in the same document. It is not a later upsell and not generic support. Every module ties to a **named operational-continuity risk** from the Engagement Baseline. Product catalog and pricing: [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md) and [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md). Owner: CEO (account), CTO (technical modules).

### Which retainer to attach

| What the implementation leaves behind | Attach |
|---------------------------------------|--------|
| A live multi-location operation | Ops Care Retainer (tier by operational maturity) |
| A built POS ↔ ERP ↔ accounting integration | Managed Integration Retainer |
| A delivered operational workflow system | Operations Retainer (internally mapped to AnyDB Operations where applicable) |

A single client may hold more than one. Position the tier by operational maturity ([`reference/kaizen-operational-readiness.md`](../reference/kaizen-operational-readiness.md)), not by default to the largest tier.

### Tie each module to a named risk

`[DRAFT — partner/legal review before client use]`

| Ops Care module | Named operational-continuity risk it covers |
|-----------------|---------------------------------------------|
| Operations reporting (monthly health report) | Operating blind between go-live and the next problem |
| Data hygiene | Duplicate/dirty records degrading inventory and customer accuracy |
| Flow maintenance | Automations silently breaking after a Shopify or app change |
| Integration monitoring | A POS ↔ ERP ↔ accounting sync failing without anyone noticing |
| Seasonal reconfiguration | Peak-season config errors at the worst possible time |
| Incremental builds | Operational needs outgrowing the launch build |
| Staff training refreshes | Workflow drift and turnover eroding launch discipline |
| Priority support | A location-down issue with no fast path to resolution |

**Rules:** do not pitch the retainer as generic support — lead with the specific risk. **Do not pitch expansion or incremental builds to a red-health account; stabilize first.** The monthly Operations Health Report is the backbone deliverable and the upsell instrument; it surfaces the next implementation opportunity for green/yellow accounts only.

---

## Section 11 — QA gate

Pack 5 output does not go to the client until all pass. Composes with `kaizen-check`. Fix in place, then re-verify the whole list.

- [ ] Proposal/SOW derives from scoped evidence (tier, lane, cap, risks, matrix, retainer fit all present)
- [ ] Source artifact is named: Blueprint Diagnostic, Implementation Scoping Brief, Shopify Referral Scope Brief, or Engagement Baseline
- [ ] Client/partner-facing first mention defines Blueprint Diagnostic as KaizenCommerce's paid pre-implementation audit and launch plan
- [ ] Commercial lane is explicit: Blueprint/advisory or full implementation after scoped discovery
- [ ] No implementation pricing quoted before scope evidence exists
- [ ] Shopify Referral context documented and partner-approved if used
- [ ] Migration lane named explicitly; API-first is the default and any fallback is justified
- [ ] Data cap stated as a number; overage/change-order clause present
- [ ] Net investment block matches the source artifact: Blueprint credit shown only when a Blueprint fee was actually charged; figures pulled from `kaizen-pricing.md`, not hardcoded
- [ ] No invented pricing, payment, warranty, or legal terms; `[NEED: approved price]` used where pricing is unapproved
- [ ] No fabricated ROI; only the merchant's quantified pain or a clearly-labeled conservative estimate
- [ ] Retainer attached by default, each module tied to a named risk; no expansion pitched to a red account
- [ ] No Shopify technical claim that requires current-documentation verification ships unflagged
- [ ] No commodity "Shopify POS setup" language; no dev-shop positioning
- [ ] Client/partner-facing rollout language avoids internal phase labels unless the output is an execution runbook
- [ ] Kaizen voice applied: direct, operational, no hype, no filler; no forbidden phrases
- [ ] All client-facing snippets marked `[DRAFT — partner/legal review]` until partner sign-off
- [ ] Footer present

Final scope, pricing, migration lane, and SOW signoff remain partner judgment. The QA gate verifies the commercial artifact is complete, honest, and Baseline-derived — not that it has replaced partner decision-making.

---

## Section 12 — Escalation triggers

Stop and bring in partner judgment when:

- The merchant demands a fixed implementation quote before a scoping call, Blueprint, or approved Baseline
- The merchant pushes for fixed scope with no data cap
- Qualification shows sub-ICP fit (single location, sub-$2M, no decision-maker access, wants cheap/fast without data integrity)
- An ROI or savings claim is requested without supporting client data
- Required pricing is unapproved (DTC/B2B Commerce Systems path with no approved price)
- A SOW line depends on a Shopify behavior the CTO has not verified against current documentation
- The recommended retainer would be pitched to an account predicted red at launch
- The merchant cannot supply a named internal owner or system access the SOW assumes

---

## Reusable templates / checklists

- [`templates/sow-boundaries.md`](templates/sow-boundaries.md) — inclusion / exclusion / responsibility / cap / change-order / retainer blocks
- [`templates/engagement-baseline.md`](templates/engagement-baseline.md) — approved source-of-truth package
- [`templates/shopify-referral-scope-brief.md`](templates/shopify-referral-scope-brief.md) — Shopify Referral exception intake
- Qualification question bank — Section 2
- Objection handling — Section 3 (+ [`reference/kaizen-sales-os.md`](../reference/kaizen-sales-os.md))
- Proposal outline + net-investment block — Section 4
- Change-order triggers — Section 9
- Retainer attach matrix + risk map — Section 10

**Canonical sources:** pricing [`reference/kaizen-pricing.md`](../reference/kaizen-pricing.md) · pricing usage [`reference/kaizen-pricing-usage-standard.md`](../reference/kaizen-pricing-usage-standard.md) · sales [`reference/kaizen-sales-os.md`](../reference/kaizen-sales-os.md) · retainers [`reference/kaizen-retainer-architecture.md`](../reference/kaizen-retainer-architecture.md).

*Composes with kaizen-propose, kaizen-invoice-exec, kaizen-scope, kaizen-check, kaizen-finance.*

---
*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
