# Kaizen Proposal Proof Bank

Use this reference when building proposals, SOW direction, executive summaries, win themes,
retainer pitches, QBRs, or case-study-ready claims.

This is a proof-pattern library, not a claims library. Do not state a proof point as fact unless
the current merchant evidence, approved Kaizen artifact, or source-backed example supports it.

## Proof Rule

Every important proposal claim should be supported by one of:

- discovery evidence from the merchant
- Blueprint finding
- migration/QA method
- operational artifact Kaizen will produce
- current Shopify/AnyDB/Flow source-backed capability
- approved case evidence
- labeled assumption or estimate

If none exists, weaken the claim or remove it.

## Provenance & Capture Schema

Every bank entry carries a provenance tag. The first `[REAL]` entries landed 2026-06-10 via the
retroactive seeding session (Real Evidence Entries below). Win-theme and pricing-rationale
patterns further down remain `[SYN]` structure unless a `[REAL]` instance is attached to them.

- `[REAL:TAG-YYYY]` — observed in a real Kaizen engagement (e.g. `[REAL:JAZ-2026]`). Required
  fields: **source engagement** (anonymized) · **date observed** · **vertical/merchant type** ·
  **confidence level** · **proposal-safe: yes/no**. Optional: size band, system stack,
  applies-when, kill conditions, metric provenance.
- `[SYN]` — synthetic pattern. Usable for internal reasoning and structure; never presented as a
  client result. Synthetic entries retire as real equivalents land.

**Hard gate (poison control):** evidence may appear in client-facing proposal language only if
`proposal-safe: yes`. Everything else is internal-reasoning only — no exceptions, regardless of
how good the number looks.

**Write path:** entries enter via `Close Client` (or sales-stage capture in `Post Call Update`).
Kai drafts the entry; the operator approves before it lands. Anonymized by default. `Kai Doctor`
reports the synthetic-to-real ratio per bank quarterly.

## Real Evidence Entries ([REAL] — seeded 2026-06-10, approval-gated)

All entries below are `proposal-safe: no` (internal reasoning only) unless and until upgraded
deliberately, per entry, after outcomes are verified. Dollar figures here are NEVER client-facing.

### [REAL:JAZ-2026] Blueprint Entry Beats Implementation Pitch With Capable In-House Teams
- source: fitness-brand apparel ecommerce (JAZ) · date observed: 2026-06-01 · vertical: apparel
  ecom, franchise B2B · confidence: high · **proposal-safe: no** (candidate for yes after the
  Blueprint is delivered — structural fact only, never commercial figures)
- observed: merchant with a strong internal team (tech lead + two senior devs, already
  prototyping) explicitly wanted "an extra pair of eyes," not agency delivery. Fixed-fee 7-day
  Blueprint + month-to-month implementation advisory (fee credited 100% against implementation
  on pivot) won over a full implementation pitch. Proposal accepted same week.
- applies when: technically capable in-house team + tight deadline + architecture risk →
  advisory wedge, not delivery pitch. Kill: team wants delivery ownership transferred.
- metric provenance: internal KT briefing message 2026-06-01 (option acceptance + terms).

### [REAL:JAZ-2026] Tag-Based Entitlements Over Native B2B For Franchise Storefronts
- source: JAZ · date observed: 2026-05-21 · vertical: apparel ecom, franchise B2B · confidence:
  high · **proposal-safe: no**
- observed: four segments on one storefront (US franchisees 45% of sales / 20% off · Japan
  franchisees 45% / 20% · employees 2% / 30% · DTC 8%). Native Shopify B2B evaluated by the
  merchant and rejected; visibility gating (Locksmith) + tiered pricing (Wholesale Gorilla)
  driven by login tags assigned from an in-house franchise app.
- applies when: segments must shop the consumer storefront with automatic entitlements. Kill:
  tag-sync source not production-ready at launch — entitlements silently fail open or closed.
- metric provenance: partner brief PDF 2026-05-14 (segment shares, discounts).

### [REAL:SGP-2026] Square→Shopify Matrixify Lane With Source-ID Idempotency
- source: food producer, Square→Shopify POS migration (SGP) · date observed: 2026-04-03/05
  (artifact dates) · vertical: food producer retail+ecom · confidence: high · **proposal-safe:
  no** — candidate for yes after go-live reconciliation verdict
- observed: original Square product/customer exports transformed to Matrixify CSVs carrying
  `custom.square_id` metafields as the source-ID key; >10,500 customers split into bounded
  ~1,500-row transfer packages; catalog shipped as a revised Matrixify workbook.
- applies when: Square sources at >10K records on the Matrixify lane — batch bounded, keep
  source-ID metafields so re-runs repair instead of duplicate.
- metric provenance: delivery artifact tree (original + transformed file sets, batch file names).

### [REAL:SGP-2026] Shopify AE Referral Co-Sell Converts To Closed Won
- source: SGP · date observed: 2026-03→06 (deal lifecycle) · vertical: food producer ·
  confidence: high · **proposal-safe: no** (internal commercial data)
- observed: AE-referral sourced deal ran the partner co-sell motion to SOW Accepted and Stage
  Closed Won at Silver tier; delivery project in progress the same quarter.
- applies when: outreach E2 proof that the AE lane produces closed business — internal
  reasoning and partner-lane prioritization only.
- metric provenance: KaizenOS deal/project record (stage, tier, source, motion).

### [REAL:KIW-2026] Price To The Buyer's Alternative, Not A Flat Card
- source: nonprofit ecommerce prospect (KIW) · date observed: 2026-05-27→06-06 · vertical:
  nonprofit ecom · confidence: medium-high · **proposal-safe: no** (internal judgment)
- observed: post-discovery complexity review concluded the deal did not warrant the top
  package; small mission-driven org priced deliberately lower, while an agency-inevitable buyer
  (JAZ) was priced at full value the same fortnight.
- applies when: calibrating willingness-to-pay — anchor on the buyer's realistic alternative
  (in-house / no-agency vs agency-inevitable). Kill: discounting a buyer who was always going
  to hire an agency anyway.
- metric provenance: internal deal-review messages 2026-05-23→06-06.

### [REAL:KZ-2026] Small-SKU POS Pilot As The Wedge Into An ERP-Run Big-Ticket Retailer
- source: kitchen/bath remodeling retailer, 5 Bay Area showrooms (KZ) · date observed:
  2026-04-02 · vertical: kitchen/home, special-order big-ticket · confidence: high ·
  **proposal-safe: no**
- observed: ~$75M-revenue retailer running entirely on NetSuite (sales orders, inventory,
  customers) entered via a narrow Phase 1 — Shopify POS for ~100 small accessory SKUs with
  barcode checkout, one pilot location before all five, fast go-live target — with a Phase 2
  customer portal + in-store pickup behind it. Buying committee shape: comprehensive pricing
  quote (licenses, hardware, connector app tiers) → workflow demo → internal review by
  inventory/accounting/purchasing → owner final approval.
- applies when: ERP-centric big-ticket retailers — don't pitch the whole business; find the
  small-SKU operational wedge and phase the rest. Kill: pilot scope creeps into special-order
  workflows before the POS basics prove out.
- metric provenance: internal merchant-overview message 2026-04-02 (revenue, locations, phase
  goals, decision criteria).

### [REAL:KZ-2026] Integration-Partner Boundary: Migration Is Ours, Connector Is Theirs
- source: KZ · date observed: 2026-04-08 · vertical: kitchen/home · confidence: high ·
  **proposal-safe: no**
- observed: scope split stated plainly — Kaizen does the data migration; a named iPaaS partner
  (Versori) handles the NetSuite integration; Kaizen sets it up properly and verifies. Clean
  ownership lines in the proposal prevent integration scope from silently becoming Kaizen's
  delivery risk.
- applies when: ERP-connected retail with a connector vendor in play — name who owns each leg
  and who verifies, in writing. Kill: "set up and verify" drifting into ongoing integration
  maintenance without a retainer.
- metric provenance: internal scope message 2026-04-08.

### [REAL:KZ-2026] Proposals Speak TO The Merchant — And Legacy Proposals Are Liabilities
- source: KZ · date observed: 2026-04-06→08 · vertical: kitchen/home · confidence: high ·
  **proposal-safe: no** (internal craft lesson)
- observed: a proposal draft was rejected internally for reading "like full AI," discussing the
  merchant in the third person; corrected to direct address ("you are unable to wait for…").
  Separately, a stale prior-year proposal for the same merchant was flagged as usable "against
  us" in negotiation — old commercial documents are live liabilities at re-engagement.
- applies when: every proposal pass — voice check includes person-of-address, not just
  forbidden phrases; re-engagements start by auditing what the merchant already holds.
- metric provenance: internal review messages 2026-04-06→08 (the operator's correction).

### [REAL:KIW-2026] Discovery-To-Artifact Inside One Business Day
- source: KIW · date observed: 2026-05-28 · vertical: nonprofit ecom · confidence: medium ·
  **proposal-safe: no**
- observed: Blueprint + summary email assembled and sent within ~24h of the discovery call,
  CC'ing named client stakeholders. Cadence evidence for the sales-os follow-up standard.
- metric provenance: internal messages 2026-05-28.

## Win Theme Pattern: Inventory Confidence Before Growth

Use when:

- merchant has multi-location inventory distrust
- online availability or pickup accuracy is weak
- staff rely on manual checks

Buyer need:

- trust stock before promising customers, adding locations, or scaling ecommerce

Kaizen differentiator:

- source-of-truth mapping, per-location reconciliation, Shopify POS configuration, training, and exception handling

Proof pattern:

- use confirmed examples of inventory mismatch, cancelled orders, manual counts, or reconciliation effort
- if no metrics exist, state the evidence gap and make validation part of Blueprint

Proposal sections:

- executive summary
- scope of work
- migration validation
- risk register
- pricing rationale

Weak wording:

- "We will improve inventory visibility."

Stronger wording:

- "The first priority is to make location inventory trustworthy enough for staff and online shoppers to act on it. That requires source-of-truth mapping, per-location validation, and staff workflows that keep Shopify accurate after go-live."

## Win Theme Pattern: Parallel Validation Reduces Cutover Risk

Use when:

- migration has multiple locations, complex data, gift cards, or operational dependency
- client fears downtime or go-live disruption

Buyer need:

- move systems without breaking selling operations

Kaizen differentiator:

- legacy remains live until Shopify is proven through validation, testing, training, and go/no-go gates

Proof pattern:

- use migration method, runbook, QA gates, created resource ledger, and rollback path
- do not claim risk-free launch; use controlled-cutover language tied to approved evidence

Weak wording:

- "We make migration seamless."

Stronger wording:

- "The cutover is controlled by evidence, not optimism. Legacy stays available while Shopify is validated through record counts, POS testing, training readiness, and a clear go/no-go checklist."

## Win Theme Pattern: Workflow Ownership Beats More Notifications

Use when:

- client wants automation but has unclear ownership
- tasks fall through email, Slack, spreadsheets, or memory
- exceptions have no queue

Buyer need:

- know who owns stuck work and what happens next

Kaizen differentiator:

- workflow state model, AnyDB queues, owner fields, escalation rules, and automation governance

Proof pattern:

- use examples of unresolved tasks, delayed approvals, vendor follow-ups, or exceptions
- show source-of-truth and handoff contracts

Weak wording:

- "We can automate your workflow."

Stronger wording:

- "Automation only helps once ownership is visible. The design first gives every exception a status, owner, and next action; then automation can safely notify, escalate, or queue work."

## Win Theme Pattern: Blueprint Protects Scope And Spend

Use when:

- prospect wants implementation quote too early
- discovery is incomplete
- data quality, integrations, or stakeholder alignment are unknown

Buyer need:

- know what they are buying before committing to implementation

Kaizen differentiator:

- Blueprint validates data, workflow, scope, risks, and commercial path before implementation

Proof pattern:

- list current unknowns and what Blueprint will resolve
- use kill conditions and decision gates

Weak wording:

- "Blueprint is our discovery phase."

Stronger wording:

- "Blueprint is the control point that prevents a vague migration from becoming an expensive surprise. It confirms the data, workflows, risks, and implementation shape before a full build is priced."

## Win Theme Pattern: Staff Readiness Is Part Of Delivery

Use when:

- POS migration affects multiple staff roles or stores
- manager fears go-live chaos
- training has not been scoped

Buyer need:

- staff who can sell, return, discount, redeem gift cards, and close the day without support panic

Kaizen differentiator:

- role-based training, micro-sprints, quick-reference cards, and readiness gates

Proof pattern:

- use role list, workflow list, go-live schedule, hardware plan, and training readiness checks

Weak wording:

- "We provide training."

Stronger wording:

- "Training is treated as go-live readiness, not documentation. Each role practices the real workflows they need on day one, and readiness gaps become targeted retraining before cutover."

## Pricing Rationale Patterns

Use only with approved pricing inputs.

Valid pricing rationale:

- scope complexity
- location count
- entity count and data quality
- integration complexity
- historical data requirements
- gift card or liability requirements
- training and go-live support requirements
- risk controls and QA burden

Invalid pricing rationale:

- invented ROI
- vague "complexity"
- competitor comparison without approved context
- unapproved discounting
- unsupported savings claims

## Proof Hygiene

Before finalizing:

1. Does every strong claim have evidence?
2. Are assumptions visible where needed?
3. Does the proposal explain why this scope, why now, and why Kai?
4. Did pricing follow value and scope clarity?
5. Can the strongest proof point survive a client asking, "Where did this come from?"
