# Kaizen Sales OS

Use this reference when the request is about KaizenCommerce's sales operating system, sales stages,
CRM/source-of-truth discipline, AE referrals, proposal readiness, follow-up cadence, or sales
methodology (four-phase engagement model, Doctor Diagnosis discovery, objection handling, revenue
sequence, conversion benchmarks). This is a
control layer, not a new execution pack. It calls existing Kai skills instead of duplicating them.

## Operating Model

Sales OS governs the path from signal to signed work:

```
Signal -> Qualified Conversation -> Discovery / Scoping -> Blueprint/Advisory or Scoped Implementation Proposal ->
Close / Nurture -> Handoff -> Retainer / Expansion
```

Existing skills remain the engines:

| Stage | Primary engine | Source/gate |
|---|---|---|
| Signal and account research | `skills/kaizen-research.md` | Public evidence, private notes, Exa when web research is needed |
| Outreach and AE nurture | `skills/kaizen-outreach.md`, `skills/kaizen-email-exec.md` | Real trigger, no generic pitch, no fabricated ROI |
| Call prep and discovery summary | `skills/kaizen-qualify.md` | Fit, pain, authority, timing, budget signals |
| Diagnostic source of truth | `skills/kaizen-diagnose.md` | Blueprint findings when advisory/diagnostic is the lane |
| POS wedge source of truth | `delivery-os/README.md` + Pack 1 | Scoped discovery, Blueprint, referral brief, or approved Engagement Baseline |
| Mixed Commerce source of truth | `delivery-os/templates/mixed-commerce-baseline-brief.md` | Architect Mode 2 Integration Map + Engagement Baseline + Mixed extension |
| Proposal and SOW | `skills/kaizen-propose.md`, `skills/kaizen-invoice-exec.md`, `skills/kaizen-scope.md` | Approved source artifact, pricing reference, exclusions |
| Follow-up and next steps | `skills/kaizen-followup.md`, `skills/kaizen-email-exec.md` | Adds new information; no empty check-ins |
| Forecast and channel health | `skills/kaizen-pipeline.md` | Stage, owner, next action, AE touchpoint freshness |
| Post-close account health | `skills/kaizen-report.md`, `skills/kaizen-ops-health-report.md` | Retainer fit, QBR, expansion only when account health allows |

## Channel Priority

Rank pipeline sources by trust and conversion leverage:

1. **Shopify AE / SE referral** — highest trust, fastest context transfer, best for urgent POS
   migration risk.
2. **Partner / ISV referral** — high trust when the partner already sees operational pain.
3. **Buying group / co-op cluster referral** — strongest when one owner-operator proof point can
   create warm introductions across similar independent merchants.
4. **Peer intro / customer referral** — high trust, slower volume.
5. **Targeted outbound** — support channel only; use real trigger and owner-operator pain.
6. **Cold generic outbound** — lowest priority; do not let it dominate qualified pipeline.

Pipeline health concern: if more than half of qualified opportunities are cold-sourced for two
consecutive months, treat it as a GTM problem, not a rep-effort problem.

## Source Of Truth

Use KaizenOS MCP as the default CRM and project-management source. It owns current merchants,
contacts, deals, projects, tasks, priorities, activity, evidence sources, and relationship
intelligence. Start with `kai_get_priorities` for ranked work, `kai_search_context` for lookup,
and `kai_get_record_context` for bounded record context.

The legacy AnyDB Kaizen OS database is archive/reference only for CRM/project-management work. Do
not treat AnyDB documentation/search MCP tools, AnyDB record tools, or old AnyDB exports as current
CRM state unless the operator explicitly asks for legacy audit or migration recovery.

For client-specific commands, recall Kai memory before synthesis and draft memory updates only when
client state changed. Do not write authoritative memory without explicit approval.

## Stage Gates

### 1. Signal Gate

Pass when there is a real reason to engage: Shopify AE / SE referral, partner referral, buying
group / co-op cluster signal, POS pain, expansion, messy
inventory, integration friction, back-office workflow failure, DTC/B2B operating complexity, or a
specific partner/channel trigger.

Fail when the account is generic, off-ICP, low-complexity theme work, or price-shopping without a
clear operational problem.

### 2. Discovery Gate

Before a proposal, confirm:

- economic buyer or path to buyer
- current stack and location/channel footprint
- business pain in the merchant's own language
- timeline pressure or reason to act now
- current POS renewal / termination date for POS migration opportunities
- seasonal blackout or off-limits launch windows for POS migration opportunities
- data/integration exposure
- decision process and next action
- owner / COO access or a clear path to the economic buyer

If fewer than these are known, continue discovery, book a scoping call, or sell the Blueprint. Do not force proposal work.

### 3. Source-Artifact Gate

KaizenCommerce has two commercial lanes:

1. **Blueprint Diagnostic + Advisory** — use when the merchant has a capable internal team,
   scope/risk is unclear, or the strongest next step is a paid audit and launch plan.
2. **Scoped full implementation** — use when the merchant wants KaizenCommerce to own delivery and
   a scoping call has established the stack, location count, migration entities, data/integration
   exposure, timeline pressure, decision process, and open assumptions.

In client-facing or partner-facing language, define Blueprint on first mention as
KaizenCommerce's paid pre-implementation audit and launch plan. Do not force Blueprint when the
merchant is clearly buying delivery and the scoping call gives enough evidence for a protected
implementation proposal.

For the POS Delivery OS wedge, an implementation proposal, SOW, migration plan, launch QA plan, or
Ops Care attach requires a named source artifact: scoped discovery notes, Blueprint Diagnostic,
partner-approved Shopify Referral Scope Brief, or approved Engagement Baseline. AE context is
directional; source-system evidence and partner signoff make it usable.

For Mixed Commerce Systems, use the Mixed Commerce Systems Baseline Brief only when two or more
active commerce surfaces and a cross-surface dependency are confirmed. For DTC-only, B2B-only, and
AnyDB-only paths, do not apply the POS Engagement Baseline rule globally until those lanes have
their own approved Baseline producers. Use the relevant variant, architecture skill, and pricing
guardrails instead.

### 4. Proposal Readiness Gate

A proposal is ready only when it has:

- source artifact named
- tier/path and rationale
- scoped deliverables
- explicit exclusions
- data caps and overage/change-order language
- client responsibilities
- migration lane where migration is in scope
- launch plan where POS migration is in scope
- pricing from `reference/kaizen-pricing.md` or `[NEED: approved price]`
- retainer attach decision tied to named operational risk, not generic support

### 5. Close / Handoff Gate

After acceptance, hand off:

- accepted proposal/SOW
- source artifact
- open assumptions and client responsibilities
- migration lane and data cap
- named owners
- next command: onboarding, invoice/SOW package, migration package, or Delivery OS pack

## Shopify AE Referral Lane

Use when a Shopify AE or partner sends a merchant.

1. Preserve the relationship context and speed.
2. Do not treat AE context as proof of source data, integrations, permissions, or gift-card/store-credit feasibility.
3. Route the opportunity into one of two lanes:
   - advisory: strong merchant technical team wants to self-implement with KaizenCommerce guiding
     launch architecture, workflow translation, QA readiness, and rollout.
   - full implementation: merchant needs Shopify POS delivery, operational coverage,
     existing-stack integrations, and workflow builds such as Special Orders workflow, robust
     inventory management, customizable Purchase Order flows, or store-team workflow.
4. If the opportunity fits the POS wedge and needs a fast partner-referred scope, run
   `delivery-os/templates/shopify-referral-scope-brief.md`; otherwise use the normal scoping call
   or Blueprint/advisory path.
5. Produce scoped evidence before client SOW, migration package, launch QA, or Ops Care attach.
6. Show no Blueprint credit unless a Blueprint fee was actually charged.

## Follow-Up Cadence

- After first call: send a specific recap and next step within 24 hours.
- After Blueprint/Baseline: summarize the decision path, open assumptions, and proposal timing.
- After proposal: add clarification or proof; do not restate the whole proposal.
- After silence: add a new signal, operational insight, or concrete timing reason. Never send an empty "checking in."
- After close: move to onboarding/SOW/invoice handoff, not more sales language.

## Sales Methodology

### Four-Phase Engagement Model
1. **Scoping / Blueprint Decision** — Decide the commercial lane. Capable internal team or unclear
   risk → Blueprint Diagnostic + Advisory. Merchant wants KaizenCommerce delivery and scope is
   understood → scoped full implementation proposal.
2. **Architecture** — Design the launch path, existing-stack integrations, operational workflow
   layer, data model, automation boundaries, and hardware/config needs. No build without approved
   spec.
3. **Implementation** — Shopify POS delivery, data/workflow preparation, store-team testing,
   existing tech stack integrations, pilot launch support, phased rollout, and operational
   workflow builds where needed.
4. **Activation** — Go-live, staff training, post-launch stabilization, and retainer attach where
   the engagement leaves operational-continuity risk.

### Discovery Call Framework (Doctor Diagnosis Method)
1. **Anchor Authority (0–5 min)** — Lead with ex-Shopify credential. Name specific system failures.
2. **Peel the Onion (5–15 min)** — Quantify pain. Hours on reconciliation? Cost of stockouts? Oversell frequency?
3. **Expose the Native Gap (15–20 min)** — Show where Shopify ends and operational chaos begins.
4. **Lane Decision (20–30 min)** — confirm whether they need Blueprint/advisory or want
   KaizenCommerce to scope and own full implementation.

**Core Sales Rule:** Never present solution until the client has verbalized the cost of their problem in their own words.

### Objection Handling

| Objection | Response Strategy |
|---|---|
| "I don't know this agency" | Name specific failure modes. Offer Blueprint as low-risk proof. CTO's ex-Shopify background. |
| "What if something breaks?" | Use plain rollout language. KaizenCommerce validates data and store workflows before launch, tests with a representative store before broader rollout, keeps the legacy POS available until Shopify is proven, and routes post-launch issues by owner and severity. |
| "The implementation fee feels high" | Quantify the current problem using client-provided facts or clearly labeled estimates. Don't discount — reframe. |
| "Why pay for the Blueprint?" | Define it first: the Blueprint Diagnostic is KaizenCommerce's paid pre-implementation audit and launch plan. It is best when they have an internal team or the risk surface is unclear. If they want KaizenCommerce to own delivery and the scoping call confirms enough detail, full implementation can be scoped directly. |
| "Just send a quote." | Do not quote blind. If the scoping call has enough evidence, use the pricing canon and name assumptions. If not, book the scoping call or sell Blueprint/advisory when diagnostic depth is the safer path. |
| "Can you guarantee nothing goes wrong?" | Do not promise risk-free launch. Promise controlled cutover: prove workflow and data before broader rollout, make rollback paths visible, and avoid a planned store-closing cutover. |
| "Need to think about it" | Identify real hesitation. Follow up with specific value, not pressure. |

### Revenue Sequence (Single Client)
Scoping call → either Blueprint/advisory or scoped full implementation → operational workflow layer
where justified → retainer. Use `reference/kaizen-pricing.md` for current implementation and
retainer economics.

### Operational Workflow Trigger
Two weeks post-POS go-live: "One thing we noticed during implementation is [specific observation].
We saw [specific impact]. We can build a structured workflow for that." Internally, route the build
through the AnyDB lane when durable workflow state, exceptions, approvals, reporting, or
cross-system reconciliation are required.

### Conversion Benchmarks

Use these as operating health checks, not promises:

| Metric | Healthy signal | Concern signal |
|---|---|---|
| Discovery → Lane decision | Merchant accepts either Blueprint/advisory or scoped implementation next step when pain, buyer, and timing are real | Repeated quote requests with no buyer access or scope evidence |
| Blueprint/Scoping → Implementation | 40%+ of completed diagnostics or scoped calls proceed when ICP fit is strong | Below 30% suggests weak qualification, unclear pain, or poor diagnostic-to-number handoff |
| Referral source mix | Shopify AE / partner / peer referrals are primary qualified lead sources | More than half of qualified pipeline is cold-sourced for two consecutive months |
| Owner-operator access | Economic buyer participates before proposal | IT-only or manager-only contact controls the process |

## Output Contract

When asked for Sales OS guidance, return:

- current stage
- source artifact status
- missing gates
- next best command
- risk if skipped

For client-facing sales writing, use the existing outreach, email, follow-up, or proposal skills.
This reference only decides the path and gates.
