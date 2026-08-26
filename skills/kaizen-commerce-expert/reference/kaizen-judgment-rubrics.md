# Kaizen Judgment Rubrics

Use this reference to score Kai outputs during reviews, rewrites, evals, or quality upgrades.
It is designed for practical inspection, not academic benchmarking.

Score each criterion 0 to 2:

- `0`: missing or unsafe
- `1`: present but shallow, generic, or weakly evidenced
- `2`: strong, specific, evidence-aware, and usable

Anything below 10 out of 14 needs revision. Anything below 8 should not be used externally.

## Universal Judgment Rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Context fit | Wrong mode or route | Mostly right but overbuilt or underbuilt | Matches decision, audience, and output type |
| Evidence discipline | Blends facts and guesses | Some labels but gaps remain | Clear facts, inferences, assumptions, estimates |
| Operational specificity | Generic advice | Some systems/workflows named | Concrete systems, owners, states, risks, next actions |
| Commercial discipline | Invents or overreaches | Mostly safe with minor ambiguity | two-lane, scope-safe, pricing-safe, source-backed |
| Falsifiability | No kill conditions | One weak caveat | Names what would change the recommendation |
| Actionability | No clear next step | Next step exists but vague | One clear action with owner/input/date when possible |
| Kaizen voice | Filler, generic, or evasive | Mostly direct with some slack | Direct, specific, operational, no empty adjectives |

## Diagnosis Rubric

Use for `kaizen-diagnose`, Blueprint direction, post-call synthesis, and discovery reviews.

High-quality diagnosis:

- proves the current state
- identifies the real operational gap
- names root cause and cost of inaction
- connects pain to stakeholder consequences
- knows when discovery is insufficient

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Six discovery answers | Missing | Partial | Complete or explicitly marked missing |
| Root cause | Symptom only | Plausible but weak | Specific and tied to current setup |
| Business impact | Generic | Qualitative only | Quantified or clearly evidence-bound |
| Stakeholders | Unknown | Roles mentioned | Decision and pain ownership clear |
| Recommendation readiness | Premature pitch | Conditional | Clear next step or hold reason |

Fail gates:

- implementation pitch before discovery proves the problem
- fabricated impact, timeline, urgency, or stakeholder alignment
- no distinction between confirmed and inferred findings

## Proposal Rubric

Use for `kaizen-propose`, SOW direction, executive summary rewrites, and proposal reviews.

High-quality proposal work:

- tells a merchant-specific commercial story
- proves Kaizen understands the risk of change and the risk of staying still
- makes scope boundaries easy to understand
- ties pricing to value, evidence, and delivery shape

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Merchant specificity | Generic | Some specifics | Cannot be reused for another merchant |
| Win themes | Missing | Present but weak | 3 to 5 themes tied to evidence and proof |
| Executive summary | Generic intro | Clear but thin | Situation, tension, thesis, proof, transformed state |
| Scope protection | Hidden assumptions | Some boundaries | Exclusions, dependencies, responsibilities explicit |
| Pricing discipline | Invented or premature | Mostly safe | Pricing follows approved inputs and value logic |

Fail gates:

- invented ROI, pricing, payment terms, or proof
- proposal contradicts the two-lane commercial model
- section changes break SOW, verification, or payment references

## Architecture Rubric

Use for `kaizen-architect`, AnyDB specs, integration maps, SOPs, and automation architecture.

High-quality architecture:

- starts from workflow and ownership, not tables
- defines source of truth and failure behavior
- makes state visible to people and systems
- avoids unnecessary automation

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Workflow clarity | Missing | Partial | Actor, trigger, state, output, owner clear |
| Source of truth | Blurry | Entity-level partial | Entity-level ownership and conflict rules clear |
| Handoff contracts | Missing | Some boundaries | Payload, success, failure, timeout, recovery defined |
| State visibility | Not addressed | Internal only | Merchant, Kaizen PM, AnyDB, Shopify views clear |
| Automation judgment | Automation by default | Some checks | Verdict, fallback, logging, tests, owner clear |

Fail gates:

- AnyDB replaces Shopify source-of-truth without explicit reason
- build starts before workflow registry exists for multi-workflow systems
- automation hides errors or lacks owner/fallback

## Migration Rubric

Use for `kaizen-migrate`, `kaizen-api-migration-exec`, `kaizen-matrixify-exec`, and data prep.

High-quality migration work:

- names the lane and preserves evidence
- treats go-live as a business event, not only an import event
- keeps rollback and cleanup executable

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Lane selection | Missing | Named but weak | API/Matrixify/Admin/hybrid named with rationale |
| Mapping completeness | Vague | Main entities only | Entity, field, key, transform, owner clear |
| Validation gates | Generic | Some counts | Count, field, sample, system, and evidence gates |
| Rollback/cleanup | Missing | Conceptual | Created Resource Ledger and ABORT_CLEANUP usable |
| Go-live readiness | Import-only | Some readiness | Hardware, training, permissions, support, reconciliation included |

Fail gates:

- production execution without explicit approval
- unresolved error rows or unreconciled critical counts
- rollback path not documented before resources are created

## QA And Reconciliation Rubric

Use for `kaizen-validate`, `kaizen-reconcile`, `kaizen-check`, and migration QA wrapper work.

High-quality QA:

- defaults to NOT READY until evidence clears
- is exact about counts, records, and files
- separates blocking defects from notes

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Verdict | Missing | Vague | PASS/PASS WITH NOTES/FAIL/NOT READY |
| Evidence manifest | Missing | Partial | Sources, files, checks, timestamps, owner clear |
| Count logic | Missing | Aggregate only | Source, transformed, attempted, succeeded, failed, reconciled |
| Issue quality | Vague | Some records | Severity, key, owner, fix, retest requirement |
| Handoff | Missing | General | Exact files, next action, retry/retest path |

Fail gates:

- passing missing evidence
- treating top-line success as proof
- hiding blockers in notes

## Outreach Rubric

Use for `kaizen-outreach`, `kaizen-email-exec`, and signal-based sales writing.

High-quality outreach:

- starts from a real signal
- teaches a useful operational point
- makes a specific, low-friction ask

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Signal | Invented or absent | Generic | Specific and source-backed or clearly inferred |
| Reframe | Missing | Weak | Challenges a real status quo cost |
| Relevance | Generic | Industry-level | Merchant/workflow-specific |
| Proof/credibility | Unsupported | Vague | Concrete method, artifact, or relevant proof |
| CTA | Pushy or vague | Acceptable | Specific, easy, and aligned to signal |

Fail gates:

- fake personalization
- generic checking-in language
- invented merchant facts
- client-facing sales-framework labels

## Reporting And Account Health Rubric

Use for `kaizen-report`, `kaizen-report-exec`, and post-go-live reviews.

High-quality reporting:

- proves value delivered or names missing baselines
- separates health, expansion, support, and churn logic
- gives owners and dates

Score:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Metrics | Invented or absent | Some activity stats | Before/after or evidence-bound gaps |
| Health band | Missing | Stated without logic | Green/Yellow/Red with reasons and actions |
| Expansion judgment | Signal-only | Conditional | Signal, context, timing, stakeholder alignment |
| Risk handling | Vague | Some risks | Churn/support risks with owner and next step |
| Action plan | Missing | Generic | Mutual action plan with owner/date |

Fail gates:

- expansion pitch on Red account
- case study/testimonial claim without evidence
- Yellow/Red status without recovery plan

## Reviewer Questions

Use these during manual review:

1. Is the answer merchant-specific or template-specific?
2. What is the strongest claim, and what evidence supports it?
3. What would make the recommendation wrong?
4. Did Kai name the owner, system, file, or record where it matters?
5. Did Kai avoid invented pricing, ROI, timelines, and platform behavior?
6. Is the next action obvious enough to execute today?
