# Asset Pack 1 — Blueprint Diagnostic Pack

> The Blueprint is one producer of the Engagement Baseline: the source-of-truth package consumed by Sales/SOW, migration, launch QA, and Ops Care. Direct implementation can use an Implementation Scoping Brief instead. If the Baseline is weak, every later stage reverts to custom work. Build it well, once.

---

## Purpose

Turn discovery into a paid diagnostic that defines, in writing and with evidence, the things a partner needs before quoting an implementation:

- The real scope of the migration and the operational build around it
- The data caps and overage exposure
- The recommended migration lane (API-first default; Matrixify or Admin CSV as named fallback)
- Launch readiness and the gaps that must close before go-live
- Whether the account is a fit for Ops Care, and at what tier
- The approved [Engagement Baseline](templates/engagement-baseline.md) that downstream packs execute against

The Blueprint is a paid engagement ([BLUEPRINT_FEE]), not a free scoping call. It is the right path when the merchant has a capable internal team, wants advisory support, or needs diagnostic depth before committing. Direct full implementation can proceed after a scoping call when KaizenCommerce will own delivery and the scope is clear enough to protect pricing. A referral may skip the paid Blueprint deliverable, but it must still produce an approved Engagement Baseline through the [Shopify Referral Scope Brief](templates/shopify-referral-scope-brief.md).

---

## Buyer / user

| Role | Who | Responsibility |
|------|-----|----------------|
| Buyer | Owner or COO of the merchant | Authorizes the Blueprint, owns the resulting report, makes the proceed decision |
| Internal lead | CEO | Runs discovery, qualifies fit, owns the relationship and the final report narrative |
| Technical assessor | CTO | Owns system inventory, data readiness, migration lane recommendation, risk scoring |
| Not involved | Silent partner | — |

The Blueprint is sold to the economic buyer, not the IT manager. If the only available contact is an IT manager with no budget authority, flag it as a qualification risk before booking the diagnostic.

---

## Required inputs

Before the Blueprint engagement starts, these must exist:

- A signed Blueprint order or agreement and the [BLUEPRINT_FEE] fee arrangement (the fee credits against a later implementation)
- A completed [merchant-intake](templates/merchant-intake.md) form, or a booked discovery call to complete it live
- Access commitment from the merchant: a named internal owner who can answer operational questions and grant read access to current systems
- Current POS contract renewal / termination date, even if approximate
- Seasonal blackout windows, fiscal-close constraints, lease/opening events, or other dates when launch disruption is unacceptable
- A target window for the diagnostic (1–2 weeks)

If intake is less than ~70% complete and no discovery call is booked, do not start the audit. Incomplete inputs produce a weak Blueprint.

---

## Buyer-facing frame

The Blueprint is not "paid discovery" and it is not only a Risk Map, Cutover Plan, and number. It is
the merchant's diagnostic source of truth for implementation: current systems, location workflows,
catalog and data readiness, integration ownership, migration lane, launch constraints, scope
boundaries, retainer fit, and the implementation sequence.

Three decision artifacts make that broader diagnostic easy for the owner-operator to act on:

1. **Risk Map** — what can break, what it would affect, and how severe it is.
2. **Cutover Plan** — the recommended go-live route in buyer language: readiness validation, pilot location, launch decision checkpoint, rollout groups, and post-launch stabilization.
3. **The Number** — the implementation investment range, credit treatment, and overage exposure tied to evidence.

The diagnostic-only guarantee applies to the promised Blueprint package: the report, baseline, and
decision artifacts. If KaizenCommerce does not deliver those promised diagnostic artifacts, the
Blueprint fee is refundable. The guarantee does not apply to
implementation outcomes, ROI, third-party approvals, or timeline promises.

---

## Deliverables

What the merchant receives:

1. **Blueprint Report** — the primary deliverable (outline below). Branded, client-owned, written in the KaizenCommerce voice. Rendered client-facing reports must be 15-20 pages minimum; do not ship a compressed report unless the partners explicitly approve that exception.
2. **Risk Map** — a scored register of what could go wrong, by severity, owner, and handling path.
3. **Cutover Plan** — a practical first-pass launch plan written for the merchant: readiness validation, pilot location, launch decision checkpoint, rollout groups, and post-launch stabilization. Internally, map it to [The Kaizen Cutover Methodology](../reference/kaizen-cutover-methodology.md).
4. **The Number** — implementation tier, operational build, retainer fit, Blueprint credit, data caps, and overage exposure tied to evidence.
5. **Migration lane recommendation** — API-first, Matrixify, or Admin CSV, with the reasoning and any documentation-verification flags.
6. **Retainer fit assessment** — whether Ops Care fits, at which tier, and the named operational-continuity risks it would cover.

What KaizenCommerce keeps internally:

- Approved [engagement-baseline](templates/engagement-baseline.md)
- Completed [system-inventory](templates/system-inventory.md)
- Completed [merchant-intake](templates/merchant-intake.md)
- The risk scoring worksheet
- Notes feeding the migration entity map (handed to Pack 2 if the deal proceeds)
- For approved Shopify referrals: completed [shopify-referral-scope-brief](templates/shopify-referral-scope-brief.md)

---

## Engagement Baseline producers

Downstream packs consume the **Engagement Baseline**, not the existence of a paid report. The Blueprint is the strongest diagnostic producer, but direct implementation uses an Implementation Scoping Brief when the merchant wants KaizenCommerce to own delivery and the scoping call gives enough evidence. The Shopify Referral Scope Brief is the approved partner-referral producer when the merchant comes through Shopify.

| Producer | When used | Output | Commercial treatment |
|----------|-----------|--------|----------------------|
| Blueprint Diagnostic | Advisory lane, capable internal team, unclear risk, or merchant wants a paid audit and launch plan | Blueprint Report + Engagement Baseline | Blueprint credit can be shown if the fee was charged |
| Implementation Scoping Brief | Direct full-implementation lane after a qualified scoping call | Internal Scoping Brief + Engagement Baseline | No Blueprint credit unless a Blueprint fee was actually charged |
| Shopify Referral Scope Brief | Partner-approved Shopify referral | Internal Referral Scope Brief + Engagement Baseline | No Blueprint credit unless a Blueprint fee was actually charged |
| [Mixed Commerce Systems Baseline Brief](templates/mixed-commerce-baseline-brief.md) | Two or more active commerce surfaces (DTC + POS + B2B + ERP/marketplace) with cross-surface source-of-truth or sequencing dependencies | Architect Mode 2 Integration Map + Engagement Baseline + [Mixed extension](templates/engagement-baseline-mixed-extension.md) | Mixed Commerce Systems Implementation — approved price, no POS-tier shortcut |

The Mixed producer is governed by this pack but driven by [`kaizen-architect`](../skills/kaizen-architect.md) router + [full Mode 2 contract](skills/kaizen-architect.md#mode-2-integration-mapping) (Integration Map) as its engine: the architect maps surfaces, build-vs-buy verdicts, and cross-surface source of truth; the brief adds the launch sequence and cross-surface risk gates the architect does not own. The single-POS Blueprint dimensions below still apply to the POS surface of a Mixed engagement.

Baseline fields use provenance tags from [`reference/kaizen-recommendation-confidence.md`](../reference/kaizen-recommendation-confidence.md):

| Tag | Meaning | Gate treatment |
|-----|---------|----------------|
| `[BLUEPRINT-CONFIRMED]` | Confirmed through Blueprint/source-system evidence | Standard gates apply |
| `[DISCOVERY-INFERRED]` | Inferred from Shopify AE context or discovery calls | May support a protected SOW if visible; must be validated before Dry Run/cutover when migration-affecting |
| `[OPEN]` | Unknown or undecided | Blocks the relevant gate until resolved or explicitly partner-accepted as an assumption |

**Load-bearing rule:** Skipping the paid Blueprint deliverable never skips diagnostic evidence. Scoping-call notes and AE context are useful directionally, but they are not proof of data quality, gift-card/store-credit feasibility, POS permissions, integration ownership, or source-system reality until captured in an approved Baseline.

---

## Internal workflow

| Step | Owner | Action | Output |
|------|-------|--------|--------|
| 1. Intake | CEO | Send merchant-intake; book discovery call if needed | Completed intake form |
| 2. Discovery call | CEO | Run the Doctor Diagnosis framework. Quantify pain in the client's own words before any solution talk | Pain quantified, scope signals captured |
| 3. System inventory | CTO | Walk the current POS, ecommerce, and back-office stack. Capture systems, versions, integrations, data volumes | Completed system-inventory |
| 4. Location & workflow audit | CTO + CEO | Map each location's workflows, hardware, staff roles, and exceptions | Location/workflow audit section |
| 5. Data readiness assessment | CTO | Assess export integrity, key quality, dedup needs, history depth | Data readiness checklist + cap estimate |
| 6. Risk scoring | CTO | Score operational risks (model below) | Operational risk register |
| 7. Lane recommendation | CTO | Choose migration lane against the decision tree (see Pack 2). Flag anything needing current Shopify docs | Named lane + flags |
| 8. Recommendation matrix | CEO + CTO | Map findings to tier + operational workflow build + retainer fit. Compute net investment | Implementation recommendation matrix |
| 9. Report assembly | CEO | Write the Blueprint Report. Apply voice filter | Draft report |
| 10. QA gate | CEO + CTO | Run the QA gate (below). Fix in place, re-verify | Approved report |
| 11. Delivery | CEO | Present the report. Position the proceed decision. Hand off to Pack 5 (Sales/SOW) | Delivered report + next step |

---

## Discovery: Doctor Diagnosis method

The discovery call is where pain gets quantified. Sequence:

1. **Anchor authority (0–5 min).** Lead with the ex-Shopify (Logistics) credential. Name specific system failure modes so the merchant knows you have seen this before.
2. **Peel the onion (5–15 min).** Quantify the pain. Hours per week on reconciliation? Cost of stockouts? How often do they oversell? What does a bad count cost at month-end?
3. **Expose the native gap (15–20 min).** Show where Shopify's native capability ends and operational chaos begins - the point where an operational workflow layer, Special Orders workflow, robust inventory management, customizable Purchase Order flows, or store-team workflow may be justified.
4. **Pivot to Blueprint (20–30 min).** "Before we talk implementation, let's do a proper diagnostic." The Blueprint is the next step, not a quote.

**Core rule:** never present a solution until the client has verbalized the cost of their problem in their own words.

---

## What the Blueprint must cover

Every Blueprint audits these dimensions. Risk Map, Cutover Plan, and The Number are the executive
decision artifacts; they do not replace the underlying diagnostic work. Anything not assessed is a
gap that resurfaces as scope creep later.

| Dimension | What to capture | Why it matters |
|-----------|-----------------|----------------|
| Number of locations | Count, type (retail / warehouse / pop-up), geographic spread | Drives tier (Silver 1–5, Gold 6–10, Diamond 11+) and launch complexity |
| Current POS | System, version, contract renewal / termination date, custom modifications | Drives migration lane, urgency, and edge-case risk |
| Shopify store status | None / live / in-progress; theme; plan level | Determines build-from-zero vs migrate-into-existing |
| Product / catalog complexity | SKU count, variant depth, bundles, kits, custom attributes | Drives entity-mapping effort and data cap |
| Inventory workflows | Counting cadence, transfers, bin/shelf/condition tracking, receiving | Primary operational workflow trigger signal |
| Customer / order history needs | How much history must migrate, loyalty ties, B2B accounts | Drives data volume and order-migration scope (Gold+) |
| Staff roles & permissions | Roles per location, permission granularity, manager overrides | Drives POS permission config and training plan |
| Hardware / payment setup | Terminals, readers, receipt printers, payment processor, regional availability | Drives hardware spec and launch QA |
| Gift cards / store credit | Volume, current system, outstanding liability | Migration edge case; flag for verification |
| Loyalty / subscriptions / apps | Programs, app dependencies, data portability | Integration risk and post-launch app reconfiguration |
| ERP / accounting / WMS / 3PL | Systems, integration method, source-of-truth ownership | Integration architecture and data-freshness defaults |
| Reporting needs | Reports they rely on today, who consumes them, cadence | Determines custom reporting and operational dashboard needs |
| Launch constraints | Seasonal blackouts, lease events, fiscal close, staffing, payment freezes | Drives launch timing, pilot-location choice, and rollout sequencing |
| Internal owner readiness | Is there a named internal owner with time and authority? | Single biggest predictor of a clean engagement |

---

## Operational risk scoring model

Score each identified risk on two axes, then rank. This produces the risk register in the report and feeds the lane and tier recommendations.

**Likelihood** (1–3): 1 = unlikely, 2 = possible, 3 = likely given what we observed.
**Impact** (1–3): 1 = inconvenient, 2 = disrupts a location or workflow, 3 = blocks launch or risks data loss / financial error.

**Risk score = Likelihood × Impact** (range 1–9).

| Score | Severity | Design token | Handling |
|-------|----------|-------------|----------|
| 6–9 | Critical | Core Red (`#a8201a`) | Must be resolved or mitigated before implementation can be quoted with confidence. Name it in the report. |
| 3–4 | Important | Red Tint Important (`#C05048`) | Plan a mitigation; may affect tier, cap, or timeline. |
| 1–2 | Watch | — | Note it; monitor during delivery. |

Common risk categories to score every time: data export integrity, duplicate/dirty keys, gift card / store credit portability, history depth vs cap, integration source-of-truth conflicts, hardware/payment regional gaps, staff readiness, seasonal/launch-window collision, single-threaded stakeholder, no internal owner.

Never invent a risk score to justify a tier. Score from what the inventory and discovery actually surfaced.

---

## Blueprint Report outline

The report is the deliverable the client owns. It should render to **15-20 pages minimum** with
enough diagnostic depth to be useful after the sales conversation. If it is under 15 pages, the
current-state evidence, workflow maps, migration assessment, risk rationale, recommendation matrix,
or roadmap is too thin. Expand those sections with evidence, not filler. Structure:

1. **Cover** — merchant name, "Blueprint Diagnostic - KaizenCommerce's paid pre-implementation audit and launch plan," date, confidential. Brand cover uses core Black or Deep Navy.
2. **Executive summary** — the three to five findings that matter most, in plain operator language. Lead with the cost of the current state, not the agency.
3. **Current state** — system inventory summary, location/workflow map, data profile. Confirmed facts only.
4. **The native gap** — where Shopify's native capability ends and where the merchant's operations currently break. Use core Red for the before/problem state and Deep Navy for the after/process state.
5. **Migration assessment** — recommended lane (API-first / Matrixify / Admin CSV), entity scope, data cap, and any items flagged for current-documentation verification.
6. **Risk Map** — scored table, Critical first, with owner, mitigation, and whether it blocks cutover.
7. **Cutover Plan** — readiness validation, pilot location, launch decision checkpoint, rollout groups, and post-launch stabilization, with open assumptions clearly marked.
8. **Recommendation matrix** — tier, operational workflow build (if any), retainer fit, with reasoning.
9. **The Number / Investment** — gross fee → Blueprint credit ([BLUEPRINT_FEE]) → net total. Data cap stated explicitly. Overage language included where data is near or over cap.
10. **Roadmap** — the phased path (diagnostic/advisory → architecture → implementation → activation) with indicative timeline.
11. **Footer on every page** — `KaizenCommerce | kaizencommerce.ca | Confidential | Page X`.

Separate confirmed facts, assumptions, and open questions visibly. An assumption presented as fact is a failure of the QA gate.

---

## Implementation recommendation matrix

The matrix maps findings to a recommendation. Fill it from the audit, never from a target deal size.

| Decision | Options | Drivers from the Blueprint |
|----------|---------|----------------------------|
| POS tier | Silver (1–5 loc, ≤50K), Gold (6–10 loc, ≤150K), Diamond (11+ / enterprise, unlimited) | Location count, data volume, history depth, support level needed |
| Operational workflow build | None / Standard ($7.5K–$12K) / Advanced ($12K–$20K) | Inventory complexity beyond native, vendor PO lifecycle, B2B portal, cross-system reconciliation load |
| Retainer | None now / Tier 1 ($500–$750/mo) / Tier 2 ($750–$1,500/mo) | Integration count, data hygiene exposure, Flow maintenance, ongoing build appetite |
| Data cap | Stated number | Product + customer + order volume from inventory |
| Overage exposure | Yes / No + change-order language | Whether final export is likely to exceed the cap |

**Net investment is always shown:** gross fee → Blueprint credit → net total. Recommend an operational workflow build only where Shopify Analytics, Admin, or a standard app does not already cover the need natively; map the technical platform internally.

---

## Retainer fit assessment

Assess whether Ops Care fits, and tie every recommended module to a named operational-continuity risk. Do not pitch a retainer as generic support.

| Signal observed in Blueprint | Suggests | Module it covers |
|------------------------------|----------|------------------|
| Multiple live integrations (ERP / WMS / 3PL / accounting) | Tier 1+ | Integration monitoring |
| Recurring data hygiene problems (dupes, drift) | Tier 1+ | Data hygiene |
| Shopify Flow automations in the build | Tier 1+ | Flow maintenance |
| Seasonal reconfiguration needs | Tier 2 | Seasonal reconfiguration |
| Appetite for incremental builds post-launch | Tier 2 | Incremental builds |
| Reporting that needs ongoing tuning | Tier 1+ | Operations reporting |

If the account looks unstable (red health predicted at launch), the Blueprint should recommend stabilization first, not expansion.

---

## Client responsibilities

- Provide a named internal owner with authority and availability for the diagnostic window
- Grant read access to current POS, ecommerce admin, and relevant back-office systems
- Supply representative data exports or sample files when requested
- Answer operational questions honestly, including known problem areas
- Make the proceed / no-proceed decision after delivery

---

## Exclusions

The Blueprint is a diagnostic. It explicitly does **not** include:

- Any data migration, transformation, or import work
- Any Shopify store configuration or build
- Any operational workflow build or schema implementation
- Any hardware procurement or setup
- Any staff training delivery
- Guaranteed pricing for implementation beyond the indicative tier ranges (final pricing follows in the proposal/SOW)
- Implementation timeline commitments (the roadmap is indicative)

Implementation scope is defined in the proposal and SOW (Pack 5), not the Blueprint.

---

## QA gate

The Blueprint does not ship until all of these pass. If one fails, fix in place and re-verify the whole list — a fix that breaks another item is not a fix.

- [ ] Every required dimension (locations through internal owner) is assessed or explicitly marked "not applicable" with reason
- [ ] POS contract renewal / termination date is captured or marked "not discussed - confirm"
- [ ] Seasonal blackout and launch-constraint windows are captured or marked "not discussed - confirm"
- [ ] Engagement Baseline is complete, source artifact named, and provenance tags applied
- [ ] Migration lane is named, with reasoning, and any Shopify behavior needing current-docs verification is flagged
- [ ] Risk Map is scored using Likelihood × Impact; Critical items are called out with owner and handling path
- [ ] Report defines Blueprint Diagnostic on first mention as KaizenCommerce's paid pre-implementation audit and launch plan
- [ ] Cutover Plan uses buyer-facing rollout language and maps internally to Shadow, Pilot Store, Verdict Gate, Waves, and Hypercare, or states why a phase is not applicable
- [ ] Recommendation matrix shows tier, operational workflow build, retainer fit — each justified by a finding, not a target deal size
- [ ] Data cap is stated explicitly; overage language is present if data is near or over cap
- [ ] Net investment is shown (gross → Blueprint credit → net)
- [ ] Rendered report is 15-20 pages minimum, or a partner-approved compressed-report exception is documented
- [ ] Confirmed facts, assumptions, and open questions are visibly separated; no assumption is presented as fact
- [ ] No invented data and no fabricated ROI; any estimate is labeled conservative and sourced
- [ ] Voice filter applied: no em-dash drama, no hollow openers, no forbidden phrases, no filler affirmations
- [ ] Footer present on every page

For Shopify Referral exceptions, replace the client-facing Blueprint report gate with the Referral Scope Brief gate, but keep the Engagement Baseline gate. No downstream pack starts without a signed Baseline.

Final scope, pricing, and the migration-lane decision remain partner judgment. The QA gate verifies the Blueprint is complete and honest, not that it has pre-committed the partner.

---

## Escalation triggers

Stop and bring in partner judgment (or pause the engagement) when:

- No named internal owner exists, or the only contact lacks budget authority
- Data export integrity cannot be confirmed (corrupt, inaccessible, or no clean key)
- Gift card / store credit liability is material and portability is unverified
- A Critical (6–9) risk has no viable mitigation
- The merchant insists on a fixed implementation quote before the diagnostic is complete
- Discovery reveals the merchant is below ICP (single location, sub-$2M, wants cheap/fast without data integrity)
- Any Shopify technical assumption the recommendation depends on cannot be verified against current documentation

---

## Reusable templates / checklists

- [merchant-intake.md](templates/merchant-intake.md) — discovery intake + merchant profile
- [system-inventory.md](templates/system-inventory.md) — current POS / ecommerce / back-office inventory
- [engagement-baseline.md](templates/engagement-baseline.md) — minimum source-of-truth package for Packs 2–5
- [shopify-referral-scope-brief.md](templates/shopify-referral-scope-brief.md) — approved Shopify referral exception path
- [mixed-commerce-baseline-brief.md](templates/mixed-commerce-baseline-brief.md) — multi-surface (DTC + POS + B2B + ERP/marketplace) Baseline producer, architect-Mode-2 driven
- [engagement-baseline-mixed-extension.md](templates/engagement-baseline-mixed-extension.md) — append-only multi-surface extension to the Engagement Baseline
- Risk scoring model — embedded above (Likelihood × Impact)
- Blueprint Report outline — embedded above
- Implementation recommendation matrix — embedded above
- Retainer fit assessment — embedded above

---

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
