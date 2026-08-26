# Kai Skill Graph

Use this reference when auditing how Kai skills connect, deciding which adjacent skill to pair, or
answering "what is upstream/downstream of this?" This is the compact graph plus the visual
pipeline map and the delegation lanes. For installed-skill pairings (external, `ce-*`, `ckm:*`),
`reference/kaizen-cross-skill-pairing-architecture.md` is the single authority.

Validated against the local Kai source/runtime on 2026-06-05.

## Graph Rules

- Kai remains the orchestrator and final signer for commercial, scope, migration, architecture, and
  client-facing recommendations.
- A skill's upstream input is context it consumes. Downstream is the next likely handoff. Adjacent
  skills are optional pairings, not automatic loads.
- Skills under `skills/` are self-contained (v2); the full-contracts bundle is dissolved. Deep platform/lane execution detail lives in `variants/`.
  The full contract remains authoritative when producing a deliverable.
- Adjacent workflow skills support Kai. They are source-managed in this repo under `skills/` and
  installed into the Codex runtime by `scripts/install.sh`. They do not override Kaizen pricing,
  Shopify/AnyDB source rules, migration lane decisions, or final QA.

## Core Pipeline Graph

| Skill | Layer | Upstream | Downstream | Adjacent | Owns | Does not own | Full contract |
|---|---|---|---|---|---|---|---|
| `kaizen-research` | Sales intake | New Deal, public/private evidence | `kaizen-qualify`, `kaizen-outreach`, `kaizen-memory` | `customer-research`, `competitor-profiling`, Exa | Merchant intel, stack signals, public proof | Pricing, scope, final recommendation | Inline |
| `kaizen-outreach` | Sales intake | Research signal, ICP trigger | `kaizen-email-exec`, `kaizen-qualify` | `cold-email`, `sales-enablement`, `stop-slop` | Signal-based outbound angle | Proposal, ROI, implementation promise | `skills/kaizen-outreach.md` |
| `kaizen-email-exec` | Sales execution | Outreach strategy, follow-up context | `kaizen-qualify`, `kaizen-followup` | `cold-email`, `email-sequence`, `copy-editing` | Send-ready email copy | Deal strategy, pricing authority | `skills/kaizen-email-exec.md` |
| `kaizen-qualify` | Discovery | Research, call context, AE context | `kaizen-diagnose`, Delivery OS Pack 1 | `operations-manager`, `customer-research`, `revops` | Fit, pain, authority, discovery summary | Full scope, full price, final architecture | `skills/kaizen-qualify.md` |
| `kaizen-diagnose` | Blueprint | Discovery, exports, system inventory | `kaizen-propose`, Delivery OS Engagement Baseline | `operations-manager`, `kaizen-retail-architecture`, `kaizen-anydb-schema` | Findings, Risk Map, Cutover Plan, Blueprint report | SOW/legal terms, unverified ROI | `skills/kaizen-diagnose.md` |
| `kaizen-propose` | Proposal | Scoped evidence: Blueprint, Implementation Scoping Brief, Shopify Referral Scope Brief, or approved Engagement Baseline | `kaizen-invoice-exec`, `kaizen-onboard`, `kaizen-scope` | `pricing-strategy`, `sales-enablement`, `kaizen-check` | Proposal structure, scope narrative, cutover framing, retainer attach | Invented pricing, legal/payment terms | `skills/kaizen-propose.md` |
| `kaizen-invoice-exec` | Commercial execution | Accepted proposal, SOW inputs | `kaizen-onboard`, finance/task handoff | `kaizen-scope`, `kaizen-finance` | SOW/invoice/change-order documents | Pricing invention, legal review replacement | `skills/kaizen-invoice-exec.md` |
| `kaizen-onboard` | Delivery activation + kickoff | KaizenOS deal/project, accepted SOW, approved scope source, first-payment evidence, access needs | `kaizen-hardware`, `kaizen-shopify-config`, `kaizen-architect` | `operations-manager`, `revops` | KaizenOS-derived handover, secure intake/requests, kickoff, first-seven-days plan | Architecture, migration QA | `reference/kaizen-client-journey.md` |
| `kaizen-hardware` | Delivery prep | Onboarding, location inventory, role list | `kaizen-shopify-config`, `kaizen-test-exec`, `kaizen-training` | `operations-manager`, `kaizen-retail-architecture` | Hardware/network plan | Final POS architecture, payment behavior claims | `skills/kaizen-hardware.md` |
| `kaizen-shopify-config` | Delivery prep | Hardware plan, store/location requirements | `kaizen-test-exec`, `kaizen-training`, `kaizen-migrate` | `kaizen-shopify-flow`, Shopify Dev MCP | Shopify setup plan/config checklist | Migration lane, final go-live verdict | `skills/kaizen-shopify-config.md` |
| `kaizen-architect` | Architecture | Blueprint, scope, workflow notes | `kaizen-dataprep`, `kaizen-anydb-build`, Mixed Commerce Baseline | `operations-manager`, `kaizen-anydb-schema`, `kaizen-retail-architecture` | Source-of-truth, build-vs-buy, integration map, SOPs | Pricing, sales close, final migration QA | `skills/kaizen-architect.md` |
| `kaizen-dataprep` | Migration prep | Architecture, source export, target contract | `kaizen-api-migration-exec`, `kaizen-matrixify-exec`, `kaizen-migrate` | `kaizen-shopify-migration`, `ce-debug` | Field mapping, cleanup, data readiness | Final lane choice, go-live approval | `skills/kaizen-dataprep.md` |
| `kaizen-api-migration-exec` | Execution | Dataprep, lane decision, API contract | `kaizen-validate`, `kaizen-reconcile`, `kaizen-migrate` | `ce-code-review`, `ce-debug`, Shopify Dev MCP | API payload/package execution artifacts | Final client verdict, source-of-truth decision | Inline |
| `kaizen-matrixify-exec` | Execution | Dataprep, explicit Matrixify lane | `kaizen-validate`, `kaizen-reconcile`, `kaizen-migrate` | `kaizen-shopify-migration`, `kaizen-migration-qa` | Matrixify CSV package | API lane override, final go-live verdict | `skills/kaizen-matrixify-exec.md` |
| `kaizen-square-migration` | Platform execution | Square export, selected lane | `kaizen-dataprep`, `kaizen-matrixify-exec`, `kaizen-validate` | `kaizen-shopify-migration`, Matrixify docs | Square-specific migration transformation | Generic platform pricing, final QA signoff | `skills/kaizen-square-migration.md` |
| `kaizen-migrate` | Migration runbook | Proposal/SOW, architecture, dataprep | `kaizen-test-exec`, `kaizen-validate`, `kaizen-reconcile` | `kaizen-shopify-migration`, `kaizen-migration-qa`, `ce-debug` | Runbook, The Kaizen Cutover, rollback, lane documentation | Unverified API behavior, client-ready QA verdict alone | `skills/kaizen-migrate.md` |
| `kaizen-test-exec` | QA execution | Migration runbook, hardware/config plan | `kaizen-validate`, `kaizen-training` | `kaizen-migration-qa`, `ce-test-browser` | Test scripts, transaction/hardware validation | Reconciliation authority, launch signoff alone | `skills/kaizen-test-exec.md` |
| `kaizen-validate` | QA | Test evidence, import logs, API responses | `kaizen-reconcile`, `kaizen-check`, launch decision | `kaizen-migration-qa`, Shopify Dev MCP | Error triage, validation verdict | Business scope, remediation pricing | Inline |
| `kaizen-reconcile` | QA | Source and target exports, validation evidence | `kaizen-training`, `kaizen-report`, launch decision | `kaizen-migration-qa`, `operations-manager` | Record-level reconciliation | Commercial acceptance, client comms alone | Inline |
| `kaizen-training` | Launch readiness | Config, hardware, test scripts, roles | Launch, `kaizen-report`, Ops Care | `operations-manager`, `sales-enablement` | Role-based training plan and readiness | Store configuration, launch QA signoff alone | `skills/kaizen-training.md` |
| `kaizen-anydb-dataload` | AnyDB execution | Architecture, source data, schema | `kaizen-anydb-build`, `kaizen-anydb-audit` | `kaizen-anydb-schema` | Load/seed data into AnyDB | Workflow design, source-of-truth decision | Inline |
| `kaizen-anydb-build` | AnyDB execution | Architect spec, workflow registry, data model | `kaizen-anydb-audit`, `kaizen-flow-build`, Ops Care | `operations-manager`, `kaizen-anydb-schema`, `ckm:ui-styling` | Schema config, formulas, automation rules | Shopify source-of-truth decision, pricing | `skills/kaizen-anydb-build.md` |
| `kaizen-anydb-audit` | AnyDB QA | Built AnyDB system, approved spec | `kaizen-report`, Ops Care | `kaizen-anydb-schema`, `kaizen-check` | Build/spec QA and remediation list | New architecture scope | Inline |
| `kaizen-flow` | Automation planning | Architecture, workflow need | `kaizen-flow-build`, `kaizen-check` | `kaizen-shopify-flow`, Shopify Dev MCP | Flow-vs-AnyDB decision and workflow design | Build-ready current Shopify claims without docs | `skills/kaizen-flow.md` |
| `kaizen-flow-build` | Automation execution | Approved Flow design | `kaizen-test-exec`, `kaizen-check` | `kaizen-shopify-flow`, Shopify Dev MCP | Buildable Flow workflow specs | Final automation architecture | Inline |
| `kaizen-report` | Post-go-live | Launch result, account state, proof | `kaizen-report-exec`, `kaizen-publish`, retainer | `operations-manager`, `churn-prevention` | Health narrative, account status, retainer framing | Fabricated outcomes, unsourced proof | Inline |
| `kaizen-ops-health-report` | Recurring | Live store health pull, retainer context | QBR, `kaizen-report`, expansion gate | `operations-manager`, `churn-prevention` | Monthly Operations Health Report | Expansion when account is red | Inline |
| `kaizen-report-exec` | Asset execution | Report brief, health data, case-study inputs | `kaizen-publish`, AE assets | `sales-enablement`, `ckm:design-system` | Health check, case study, retainer pitch assets | New proof claims | `skills/kaizen-report-exec.md` |
| `kaizen-publish` | Distribution | Case study, post, deck, report | `kaizen-content-calendar`, AE proof | `social-content`, `ckm:brand`, `ckm:design-system` | Public/partner-facing packaging | Source facts, pricing, technical claims | Inline |
| `kaizen-content-calendar` | Distribution | Published proof, themes, campaign goals | Social/content execution | `content-strategy`, `social-content`, `stop-slop` | Content calendar and repurposing plan | Client claims without permission | Inline |
| `kaizen-render` | Asset execution | Approved content and template | PDF/deck/document handoff | `ckm:design-system`, `ce-proof` | Styled PDF/Google Doc output | Content strategy, scope | Inline |
| `kaizen-generate` | File generation | Mapping/spec/sample need | `kaizen-validate`, implementation handoff | `ce-work`, `ce-code-review` | Sample data, CSVs, scripts, configs | Strategy, final QA | `skills/kaizen-generate.md` |
| `kaizen-check` | Quality layer | Any deliverable needing review | Final send, remediation loop | `ce-proof`, `copy-editing` | Scope, pricing, evidence, voice, QA review | Producing original client artifact alone | `skills/kaizen-check.md` |
| `kaizen-scope` | Scope governance | Proposal/SOW, change signal, overage | Change order, proposal/SOW update | `pricing-strategy`, `kaizen-invoice-exec` | Exclusions, assumptions, change triggers | New pricing without approval | Inline |
| `kaizen-orchestrate` | Engagement control | Multi-phase client work, resume request | Current phase skill, task/memory updates | `revops`, `operations-manager` | Phase routing, handoff discipline | Replacing phase-level skills | `skills/kaizen-orchestrate.md` |
| `kaizen-memory` | Intelligence | Client facts, approved memory updates | All client-specific skills | Memory hook protocol | Client profile recall/update mechanics | Unapproved authoritative memory | Inline |
| `kaizen-proactive` | Intelligence | Recent output, open tasks | Suggested next action | `revops`, `kaizen-check` | Next-step suggestion | Marking inferred tasks accepted | Inline |
| `kaizen-pipeline` | Internal operating | Deal list, AnyDB/CRM/project source | Priorities, forecasts, follow-ups | `revops`, `sales-enablement` | Pipeline review and forecast | Client relationship truth without source | Inline |
| `kaizen-finance` | Internal operating | Engagement economics, pipeline data | Pricing review, P&L, margin decision | `pricing-strategy`, `revops` | Financial model and P&L | Canonical pricing changes alone | `skills/kaizen-finance.md` |
| `kaizen-firm-economics` | Firm-building | Utilization, capacity, margin question | Hiring/pricing/bench decision | `pricing-strategy`, `operations-manager` | Capacity and margin analysis | Client delivery scope | Inline |
| `kaizen-productize` | Firm-building | Repeated work pattern, offer idea | Delivery OS, sales assets, SOW boundaries | `pricing-strategy`, `sales-enablement`, `operations-manager` | Productized offer design | Final technical scope/pricing alone | Inline |
| `kaizen-partner-ecosystem` | Firm-building | Partner/channel question | AE enablement, co-sell plan | `sales-enablement`, `referral-program`, `co-marketing` | Partner strategy | Client proof without permission | Inline |
| `kaizen-retail-expert-v2` | Retail reference | POS/retail/domain question | Domain-specific reference route | `kaizen-retail-architecture` | Retail domain triage | Final implementation plan alone | Inline |
| `kaizen-catalog-review` | Retail QA | Product/catalog export | Dataprep, migrate, publish | `kaizen-retail-research`, `seo-audit` | Catalog/import readiness | Migration lane signoff | `skills/kaizen-catalog-review.md` |

## Delivery OS Overlay

| Producer or pack | Upstream | Downstream | Adjacent | Owns | Does not own |
|---|---|---|---|---|---|
| Blueprint Diagnostic Pack | Discovery, system inventory, merchant intake | Engagement Baseline, Packs 2-5 | `kaizen-diagnose`, `operations-manager` | Baseline evidence, Risk Map, Cutover Plan, lane recommendation | Skipping evidence because a Blueprint was not sold |
| Implementation Scoping Brief | Qualified scoping call, merchant delivery-ownership need | Engagement Baseline, Pack 5 | `kaizen-qualify`, `kaizen-sales-os.md` | Direct full-implementation evidence, assumptions, open gaps, pricing-source guardrails | Treating confidence as scope proof |
| Shopify Referral Scope Brief | Shopify AE context, partner approval | Engagement Baseline, Pack 5 | `kaizen-qualify`, `kaizen-sales-os.md` | Fast exception path with evidence gates | Treating AE context as proof |
| Mixed Commerce Systems Baseline Brief | `kaizen-architect` router + `skills/kaizen-architect.md` Mode 2 Integration Map | Engagement Baseline + Mixed extension | `operations-manager`, `kaizen-anydb-schema` | Multi-surface source-of-truth and launch-sequence capture | Selling every complex Shopify account as Delivery OS |
| Pack 2 API-First Migration | Approved Engagement Baseline | Dry Run, reconciliation, cutover | `kaizen-migrate`, `kaizen-shopify-migration` | Migration execution package, Shadow / Pilot Store / Verdict Gate evidence | Redefining scope |
| Pack 3 Launch QA | Pack 2 validation, baseline constraints | Go-live signoff, hypercare | `kaizen-test-exec`, `kaizen-training` | Per-location launch readiness, Waves / Hypercare evidence | Migration data remediation |
| Pack 4 Ops Care | Launch handoff, open risks | Monthly health report, QBR | `kaizen-report`, `operations-manager`, `churn-prevention` | Recurring operating health | Expansion on red accounts |
| Pack 5 Sales / SOW | Approved Engagement Baseline | Proposal/SOW, onboarding, SE referral one-pager | `kaizen-propose`, `kaizen-scope`, `sales-enablement` | Commercial scope protection and partner-safe referral assets | Pricing not in canonical source |

## Adjacent Workflow Pairings

Pairings with external, `ce-*`, and `ckm:*` skills are owned by
`reference/kaizen-cross-skill-pairing-architecture.md` (tier definitions, workflow stacks,
exhaustive matrix, routing heuristics, anti-patterns). Do not restate that matrix here; this
file owns Kai-internal topology only.

## Maintenance Contract

When adding a new Kai skill, update:

1. `reference/kaizen-routing-index.md`
2. this file (graph, visual pipeline, delegation lanes)
3. `reference/kaizen-cross-skill-pairing-architecture.md` only if an external pairing changes
4. validation tests when a new route becomes load-bearing

## Visual Pipeline Map

Documentation, not runtime context: load when onboarding a collaborator or debugging a routing
decision. Day-to-day skill execution does not need this section.

This brain is the foundation for a connected system of 46 skills + reference files covering the
full agency lifecycle. The system has five layers: pipeline (sequential handoffs), intelligence
(cross-cutting context), execution (hands-on file/document generation), support (reference +
recurring), and firm-building (internal operating strategy).

```
SALES CYCLE                     DELIVERY CYCLE                          POST-DELIVERY
─────────────────               ──────────────────────────────          ─────────────────
kaizen-research                 kaizen-onboard                          kaizen-report-exec
  (Merchant intel)                (Kickoff & access)                      (Auto-generate reports
  ↓                               ↓                                       with real data)
kaizen-outreach                 kaizen-hardware                           ↓
  ↓                               (Hardware & network)                  kaizen-publish
kaizen-email-exec                 ↓                                       (LinkedIn, PPTX, voice)
  (Send-ready emails)           kaizen-shopify-config                     ↓
  ↓                               (Store configuration)                kaizen-content-calendar
kaizen-qualify                    ↓                                       (Repurpose outcomes)
  (Discovery PRE/POST)         kaizen-architect
  ↓                               (AnyDB + Integration + SOP)
kaizen-diagnose                   ↓
  (Blueprint report)            ┌───────────────┬───────────────┐
  ↓                             │  POS TRACK    │  ANYDB TRACK  │
kaizen-propose                  │               │               │
  (Proposal + SOW)              │ dataprep      │ anydb-dataload│
  ↓                             │   ↓           │   ↓           │
kaizen-invoice-exec             │ api-migration │ anydb-build   │
  (SOW, invoices, agreements)   │   (API first) │   (schema+seed│
                                │ matrixify-exec│    +formulas) │
                                │   (fallback)  │               │
                                │   ↓           │               │
                                │ migrate       │   ↓           │
                                │   ↓           │ anydb-audit   │
                                │ test-exec     │               │
                                │   (Dry Run +  │               │
                                │    test scripts)              │
                                │   ↓           │               │
                                │ validate      │               │
                                │   ↓           │               │
                                │ reconcile     │               │
                                └───────┬───────┴───────┬───────┘
                                        ↓               ↓
                                    kaizen-training
                                      ↓
                                    flow-build
                                      (Importable Flow workflows)

INTELLIGENCE LAYER (cross-cutting — supports all stages)
─────────────────────────────────────────────────────────
kaizen-memory       Client context that persists across the entire pipeline
kaizen-check        Validates deliverables before they reach the client
kaizen-proactive    Suggests the logical next step after every skill output

FIRM-BUILDING LAYER (cross-cutting, internal operating strategy)
────────────────────────────────────────────────────────────────
kaizen-firm-economics    Utilization, bench risk, first hire, margin, value pricing
kaizen-productize        Productized offers, reusable IP, accelerators, sales posture
kaizen-partner-ecosystem Shopify partner motion, ISV co-sell, nearbound account strategy

EXECUTION LAYER (hands-on — produces actual files/documents/configs)
────────────────────────────────────────────────────────────────────
kaizen-api-migration-exec API-first migration packages, payloads, scripts, retry queues, manifests
kaizen-matrixify-exec   Matrixify CSV packages when that lane is explicitly selected
kaizen-anydb-build      Schema configs, seed data, formulas, automation rules for AnyDB
kaizen-flow-build       Buildable Flow workflow specs with exact triggers/actions
kaizen-email-exec       Fully personalized, send-ready emails (no placeholders)
kaizen-invoice-exec     SOWs, invoices, change orders, engagement agreements
kaizen-shopify-config   Store configuration: locations, staff, Smart Grid, channels
kaizen-test-exec        Executable test scripts: API dry-run, Matrixify Dry Run, transactions, hardware, cutover
kaizen-report-exec      Health checks, case studies, retainer pitches with real data
kaizen-generate         Lightweight file generation (sample data, migration scripts)
kaizen-render           Styled PDF/Google Doc output using KaizenCommerce design system

SUPPORT / RECURRING / REFERENCE
───────────────────────────────
kaizen-pipeline         Weekly CRM review, deal scoring, ARR tracking
kaizen-finance          Engagement P&L, monthly review, pricing analysis, forecasts
kaizen-flow             Shopify Flow design (planning — flow-build is execution)
kaizen-scope            Mid-project change orders, overages, scope adjustments
kaizen-retail-expert-v2 POS, inventory, fulfillment domain reference (routes to kaizen-reference/)
```

### Skill Categories

**Pipeline nodes** (produce handoffs to the next stage):
research → outreach → qualify → diagnose → propose → onboard → hardware → shopify-config → architect → dataprep → migrate → validate → reconcile → training → anydb-dataload → anydb-audit → report → publish → content-calendar

**Intelligence layer** (cross-cutting, supports all stages):
memory, check, proactive

**Firm-building layer** (cross-cutting, internal operating strategy):
firm-economics, productize, partner-ecosystem

**Execution layer** (hands-on — produces actual files, documents, configs):
api-migration-exec, matrixify-exec, anydb-build, flow-build, email-exec, invoice-exec, shopify-config, test-exec, report-exec, generate, render

**Support/reference skills** (called alongside pipeline nodes):
flow, retail-expert-v2, scope, pipeline, finance

**Firm-building note:**
The firm-building layer sits alongside the engagement pipeline, not inside the sequential client
handoff path. `kaizen-firm-economics`, `kaizen-productize`, and `kaizen-partner-ecosystem` are
governed by `reference/kaizen-firm-strategy.md` and should be loaded only when the user is making
internal operating decisions about capacity, pricing mechanics, packaged offers, reusable IP, or
partner-led growth.

**Mid-engagement skills** (triggered when project reality diverges from plan, produces handoff):
scope

**Standalone recurring** (not tied to a single engagement):
pipeline

### Full pipeline sequence:
`outreach → qualify → diagnose → propose → onboard → architect → [POS track | AnyDB track] → report → publish`

Each skill:
1. Works standalone with full quality
2. Can receive handoff context from the previous skill
3. Pipeline nodes produce output + explicit next-step handoff for the next skill
4. References this brain for shared knowledge (tiers, voice, pricing, commercial guardrails)

When a pipeline skill instructs you to "read kaizen-brain for context," it means apply all the knowledge in this file — tier logic, voice rules, pricing, commercial guardrails, and ICP — to the task at hand.

## Delegation Lanes

Load this section when deciding between local Kai work, specialist subagents, or Antigravity CLI.

## Local Kai

Keep work local when the task involves:

- immediate blocking decisions
- final client-facing synthesis
- commercial positioning, pricing, scope, or source-of-truth verdicts
- small tasks faster to complete than to delegate
- live user collaboration where asking a worker would add friction

Kai owns final judgment. Delegation can gather evidence or prepare artifacts, but Kai signs off.

## Specialist Subagents

Use specialist subagents only when the user explicitly asks for:

- subagents
- delegation
- parallel agent work
- splitting the task across agents
- optimized Kaizen subagent workflow

Load `reference/kaizen-specialist-registry.md` before spawning. Use subagents for bounded sidecar
work that benefits from separate context: research, QA, architecture critique, migration mapping,
AnyDB schema review, Flow checks, or frontend audit.

Before using built-in subagents for delegated execution, check the external CLI order required by
the operator: `agy` first, then Grok Build CLI (`grok`) when Antigravity is unavailable, unusable,
or quota-blocked. Use built-in subagents only when both external lanes are not usable.

## Antigravity Relay

| User says | Action |
|---|---|
| "should I use Antigravity or a subagent", "recommend a delegation lane", "what saves Codex usage here" | Load `reference/kaizen-antigravity-delegation.md`, then output a delegation recommendation only |
| "delegate this to Antigravity", "use Antigravity CLI", "give me an Antigravity CLI prompt", "have Antigravity handle this" | Load `reference/kaizen-antigravity-delegation.md`, then output the required Antigravity CLI task block |
| "here's what Antigravity returned", "Antigravity is done, here's the output" | Load `reference/kaizen-antigravity-delegation.md`, then give a PASS / PASS WITH NOTES / FAIL verdict |
| "Antigravity got it wrong, fix the instructions" | Load `reference/kaizen-antigravity-delegation.md`, then output a corrective Antigravity CLI task block |
| "what would you send Antigravity for this" | Load `reference/kaizen-antigravity-delegation.md`, then draft a preview Antigravity CLI task block |
| Outdated third-party delegation wording | Route to Antigravity CLI and use Antigravity naming in the response |

Antigravity CLI is a bounded local execution lane for grunt work and evidence gathering. Never
invoke it automatically. Kai may suggest Antigravity when it is the right low-risk execution or
research lane, but only outputs an Antigravity task block when the operator explicitly asks to use
Antigravity or asks for the Antigravity prompt. Keep client-facing synthesis, strategy, pricing,
source-of-truth decisions, and final QA in Kai. If the operator asks for subagents or parallel agents
without naming Antigravity, apply the external CLI fallback order above before using the global
Kaizen specialist subagent workflow.

## Antigravity vs Subagent Decision

Use Antigravity CLI when the operator explicitly wants Antigravity, asks for the `agy` lane, or the task
is bounded execution or research gathering:

- API payload preparation
- local ETL scripts
- CSV/Excel cleanup
- schema normalization
- raw source research gathering
- documentation/source collection
- test fixture generation
- log parsing
- dry-run/sandbox command execution
- migration manifest generation

Use Kaizen specialist subagents when the operator asks for subagents or parallel agents and the work
needs domain judgment inside the Kaizen skill system:

- merchant research plus architecture synthesis
- AnyDB schema design review
- migration strategy, lane evidence, or QA
- Shopify Flow checks
- storefront/POS UX audit
- independent critique before Kai ships a client-facing answer

Do not let Antigravity or subagents choose the authoritative migration lane, pricing, scope,
source-of-truth architecture, or final sign-off.
