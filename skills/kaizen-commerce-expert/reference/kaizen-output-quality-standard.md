# Kaizen Output Quality Standard

Use this reference when Kai is producing or reviewing important work, especially diagnosis,
proposal, architecture, migration, QA, outreach, or account reporting.

This file defines what "good" means. It is not another process checklist. It is the taste layer
for Kai's work.

## Source Streams

Current source priority:

1. **agency-agents synthesis:** sales strategy, workflow architecture, reality checking,
   proposal quality, account strategy, pipeline quality, behavioral training, and system-boundary
   contracts.
2. **management-consulting decision-quality patterns:** assumptions discipline, evidence
   separation, falsifiability, anti-selection rules, gotchas, decision gates, and "what would make
   this wrong?" reasoning.
3. **Kaizen artifacts when available:** real Kaizen proposals, Blueprints, call notes,
   migration plans, QA findings, client outcomes, emails, and QBRs. Do not invent examples in this
   category. Use only provided artifacts or reviewed source material.

## Universal Standard

Excellent Kai output is:

- specific to the merchant, stack, workflow, and decision in front of the team
- grounded in evidence, with assumptions and estimates separated
- operational enough for the next person to act without re-discovery
- commercially disciplined: two-lane, scope-aware, pricing-safe, and source-backed
- falsifiable: it names what would change the recommendation
- concise enough to use, but not thin where judgment matters
- direct in Kaizen voice, without filler, generic adjectives, or vague reassurance

Weak Kai output is:

- generic enough that the merchant name could be swapped without changing the content
- framework-heavy but evidence-light
- confident without data, source, owner, or operational detail
- missing the next action
- focused on features instead of root cause, risk, and business consequence
- safe-sounding but not actually testable

Failing Kai output is:

- inventing facts, ROI, timelines, pricing, source behavior, or platform constraints
- hiding assumptions inside client-facing deliverables
- approving go-live, automation, migration, or scope without evidence
- recommending implementation before discovery proves the problem
- treating Matrixify as the default lane instead of a selected lane
- exposing internal sales-framework jargon in client-facing output unless the operator asks
- producing a client-facing artifact that cannot survive a line-by-line evidence review

## Skill-Specific Quality Criteria

### kaizen-diagnose

Excellent:

- separates confirmed facts, inferred causes, assumptions, and missing evidence
- identifies root cause, not only symptoms
- answers the six discovery questions or marks them missing
- ties each recommendation to operational impact and cost of inaction
- preserves the merchant's language without parroting unverified claims

Weak:

- repeats call notes as a summary with no diagnosis
- lists generic Shopify benefits instead of operational failure patterns
- recommends Blueprint, migration, or AnyDB without saying why now
- misses who owns the pain and who must approve change

Fail:

- pitches implementation before discovery is complete
- invents costs, urgency, stakeholder alignment, or data quality
- treats a vague pain point as enough to scope work

### kaizen-propose

Excellent:

- opens with a clear commercial argument specific to the merchant
- uses 3 to 5 win themes tied to discovery evidence
- makes scope boundaries, exclusions, responsibilities, and dependencies explicit
- places pricing after value, risk, and scope clarity
- makes the buyer feel the proposal could not be reused for another merchant

Weak:

- reads like a template with the merchant name inserted
- lists features instead of a solution journey
- has a risk register that does not change the buying decision
- uses proof language without proof

Fail:

- invents ROI, case evidence, pricing, payment terms, or legal terms
- buries exclusions or client responsibilities
- changes proposal section numbering without updating SOW references and checks

### kaizen-architect

Excellent:

- defines source of truth for every critical entity
- maps workflows before tables
- uses the 4-view workflow registry for multi-workflow builds
- defines boundary handoff contracts with failure, timeout, owner, and recovery behavior
- explains what the merchant, Kaizen PM, AnyDB, and Shopify each see at key states

Weak:

- starts with tables before workflows and states
- treats AnyDB as a passive data copy
- omits owner, fallback, or exception handling
- overuses automation without proving the human process

Fail:

- calls AnyDB a database in client-facing output
- makes AnyDB the source of truth for Shopify-owned entities without explicit justification
- designs formulas, syncs, or automations without current source validation where required

### kaizen-migrate

Excellent:

- names the migration lane and why it fits
- includes field mappings, count gates, validation gates, rollback triggers, and cleanup ledgers
- keeps legacy live until Shopify is proven
- treats API-first as default and Matrixify as selected when evidence supports it
- makes go/no-go criteria concrete enough for a technical lead to enforce

Weak:

- creates a plausible timeline without data volume or export quality
- mentions rollback without naming resources and destroy methods
- treats import success as go-live readiness
- skips training, hardware, permissions, or reconciliation dependencies

Fail:

- allows production writes without approval and evidence gates
- ignores unresolved Matrixify/API errors
- omits Created Resource Ledger or ABORT_CLEANUP when resources are created

### kaizen-validate

Excellent:

- returns PASS, PASS WITH NOTES, FAIL, or NOT READY with evidence
- names exact tested files, counts, checks, records, screenshots, or logs
- separates blocking issues from watch items
- gives the next retest path

Weak:

- says "looks good" without count math
- only checks top-line success messages
- fails to connect errors to remediation owners

Fail:

- passes missing evidence
- ignores unresolved row-level, API, Matrixify, Shopify, AnyDB, or hardware failures
- hides a go-live blocker inside notes

### kaizen-reconcile

Excellent:

- reconciles at the most useful key: SKU, variant, location, customer, order, gift card, or custom ID
- explains expected differences before calling discrepancies
- produces a discrepancy table with owner, severity, and fix path
- connects reconciliation status to go-live, hypercare, or client communication

Weak:

- compares only aggregate counts
- does not explain duplicate, skipped, excluded, or intentionally transformed records
- gives fixes without source file or system owner

Fail:

- treats unreconciled financial, inventory, gift card, or order data as acceptable
- passes reconciliation without a retained evidence trail

### kaizen-outreach

Excellent:

- starts from a real signal, not flattery
- reframes a status quo cost the merchant plausibly feels
- teaches a new operating lens before presenting Kaizen
- has one clear, low-friction next step
- avoids generic "checking in" or volume-first outreach

Weak:

- sounds like a marketing sequence that could go to anyone
- mentions Shopify without a merchant-specific reason
- asks for a meeting before earning attention

Fail:

- invents facts about the merchant
- uses pressure, fake urgency, fake personalization, or unverifiable claims
- exposes internal sales frameworks in the email

### kaizen-report

Excellent:

- separates project health, account health, and expansion logic
- uses confirmed before/after metrics or labels gaps clearly
- classifies Green, Yellow, or Red before expansion
- gives a mutual action plan with owners and dates
- supports QBR, retainer, case study, and testimonial decisions with evidence

Weak:

- recaps activity instead of value, risk, and next actions
- recommends retainer without proving post-go-live need
- mixes support issues and expansion opportunities without account health logic

Fail:

- pitches expansion to a Red account
- invents post-go-live outcomes or testimonial claims
- publishes a status report with Yellow/Red risk and no recovery plan

## Review Pass

Before finalizing high-stakes output, ask:

1. Would this still make sense if the merchant name were removed? If yes, it is too generic.
2. What evidence supports the strongest claim?
3. What assumption, if wrong, would change the answer?
4. What is the first action after this output?
5. Who owns that action?
6. What would make this output unsafe to send, build, or approve?
