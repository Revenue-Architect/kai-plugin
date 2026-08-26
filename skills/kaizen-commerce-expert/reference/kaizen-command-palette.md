# Kaizen Command Palette

Load this file when the operator uses a short workflow command such as `New Deal`, `Sync Client`,
`Prep Call`, `Post Call Update`, `Build Blueprint`, `Build Proposal`, `Use Delivery OS`,
`Run Pack 1`, `Use Pack 5`, `Implementation Scoping Brief`, `Shopify Referral Scope Brief`, `SE Referral One-Pager`,
`Migration Package`, `Migration QA`, `Log Win`,
`Delegate to Antigravity`, `Resume Client`, `Kai Status`, `Kai Doctor`, `Start My Day`, `End My Day`,
`Weekly Review`, `Evidence Research`, `Kai Priorities`, `Review Workspace`, `Close Client`,
`Vendor Freshness Check`, `Update Kai Vendor Knowledge`, `Check Shopify Freshness`, or
`Check AnyDB Freshness`.

This is the operator command index plus per-category contracts. The complete command contract
(alias map, run-folder expectations, task-ledger outputs, edge cases) lives in
`reference/kaizen-command-palette-contract.md`; load it only when a category section is not enough.

## Progressive Disclosure References

| Category | Commands | Reference |
|---|---|---|
| Daily, status, priorities | `Kai Status`, `Kai Doctor`, `Start My Day`, `End My Day`, `Weekly Review`, `Kai Priorities` | this file, Category: Daily, Status, And Priorities |
| Pipeline and client intake | `New Deal`, `Sync Client`, `Prep Call`, `Post Call Update`, `Build Blueprint`, `Build Proposal`, `Start Delivery`, `Onboard Client`, `Resume Client` | this file, Category: Pipeline And Client Intake |
| POS Delivery OS wedge | `Use Delivery OS`, `Run Pack 1`, `Use Pack 5`, `Audit against Pack 5`, `Build Engagement Baseline`, `Implementation Scoping Brief`, `Shopify Referral Scope Brief`, `SE Referral One-Pager` | `delivery-os/README.md` |
| Execution, QA, closeout | `Migration Package`, `Migration QA`, `Evidence Research`, `Review Workspace`, `Close Client` | this file, Category: Execution, QA, And Closeout |
| Vendor freshness and hooks | `Vendor Freshness Check`, `Update Kai Vendor Knowledge`, `Check Shopify Freshness`, `Check AnyDB Freshness`, operating hooks | this file, Category: Vendor Freshness And Operating Hooks |
| Full command contract | All commands, aliases, task outputs, connector contracts | `reference/kaizen-command-palette-contract.md` |

Command categories live in this file (sections below). Escalate to the full contract only when a
category section is not enough.

## Command Rules

- Treat exact command phrases and close natural-language aliases as execution requests.
- Create or recall client memory before client-specific work.
- Load `reference/kaizen-memory-hook-protocol.md` for the Memory Hook Protocol and client-memory update gates.
- Load `reference/kaizen-operating-hook-protocols.md` for Operating Hook Protocols, vendor freshness, evidence gates, task extraction, account health, or expansion judgment.
- Use `scripts/kaizen-workflow.py` when a run folder or task ledger entry is useful.
- Use `scripts/kaizen-tasks.py` for task ledger operations.
- In the installed skill runtime, these scripts are wrappers that forward to the durable
  `kaizen-skills` source checkout. Prefer running from the source repo root; set
  `KAIZEN_SKILLS_ROOT` or `KAI_SOURCE_ROOT` if the checkout is not at the default path.
- For private deal context, gather available evidence before synthesis. Source current CRM/project state from KaizenOS MCP first, then enrich with Outlook Email, Outlook Calendar, Microsoft Teams, Microsoft SharePoint, client memory, task ledger, and public/Exa research when needed.
- Load `reference/kaizen-kaizenos-integration-map.md` for per-command KaizenOS tool sequences,
  the record-ownership boundary, and write discipline.
- Client-update drafting (weekly project updates) goes through KaizenOS:
  `kai_list_client_update_drafts` to find the draft, `kai_draft_client_update` to write content in
  Kaizen voice. Approval and sending stay in the app.
- For KaizenOS MCP reads, prefer `kai_get_priorities` for priority queues, `kai_search_context` for record lookup, and `kai_get_record_context` for bounded merchant/contact/deal/project/task context.
- For KaizenOS MCP writes, prefer named tools over generic actions, use `dryRun=true` when checking shape or risk, and include `idempotencyKey` on retries.
- Keep authoritative decisions, pricing, migration lane selection, final QA, and client-facing synthesis in Kai.
- Delegate to Antigravity only through a bounded task contract.

## Command Table

| Command | Trigger examples | Primary action |
|---|---|---|
| `New Deal: [Merchant Name]` | `New Deal: Acme Retail`, `new deal Acme Retail`, `new lead from Acme` | Search KaizenOS first to avoid duplicates, then initialize/create the deal context, gather Outlook Email, Microsoft Teams, Microsoft SharePoint, and public evidence, create task ledger entries, and produce a first Kai opportunity review. |
| `Sync Client: [Merchant Name]` | `sync client Acme`, `refresh Acme context`, `catch me up on Acme` | Resolve the KaizenOS merchant/deal/project, fetch record context, gather new evidence, identify deltas, and propose reviewed KaizenOS/memory/task updates. |
| `Prep Call: [Merchant Name]` | `prep call Acme`, `I have a call with Acme` | Build a call brief from KaizenOS record context, memory, evidence, open tasks, known gaps, and discovery strategy. |
| `Post Call Update: [Merchant Name]` | `post call update Acme`, `process these Acme notes` | Convert call notes into reviewed KaizenOS activity/tasks/decisions, memory updates, next actions, and a follow-up draft when useful. |
| `Build Blueprint: [Merchant Name]` | `build blueprint Acme`, `diagnose Acme` | Route to `skills/kaizen-diagnose.md` after memory recall and evidence check. |
| `Build Proposal: [Merchant Name]` | `build proposal Acme`, `generate SOW Acme` | Route to `skills/kaizen-propose.md` and pricing rules after source-artifact status check. |
| `Start Delivery: [Merchant Name]` | `start delivery Acme`, `onboard Acme`, `kick off Acme`, `set up the Acme project` | Load `reference/kaizen-client-journey.md` and `skills/kaizen-onboard.md`; resolve the KaizenOS deal/project, verify activation conditions, use `kai_activate_deal_engagement` for accepted commercial activation, and preview only the exact missing named writes for direct/manual paths. |
| `Use Delivery OS: [Merchant Name]` | `use delivery os Acme`, `run the POS wedge for Acme` | Load `delivery-os/README.md`, confirm fit, then select the needed pack. |
| `Run Pack 1: [Merchant Name]` | `run Pack 1 for Acme`, `build the Engagement Baseline` | Load `delivery-os/01-blueprint-diagnostic-pack.md` and produce or audit the Engagement Baseline path. |
| `Use Pack 5: [Merchant Name]` | `use Pack 5 for this proposal`, `shape this SOW with Pack 5` | Load `delivery-os/05-sales-sow-pack.md`; require an approved Engagement Baseline or route back to Pack 1. |
| `Implementation Scoping Brief: [Merchant Name]` | `implementation scoping brief Acme`, `scoping brief Acme`, `full implementation scoping Acme` | Load `delivery-os/templates/implementation-scoping-brief.md` and `delivery-os/templates/engagement-baseline.md`; use when the merchant wants KaizenCommerce to own delivery after a qualified scoping call. |
| `Shopify Referral Scope Brief: [Merchant Name]` | `Shopify referral brief Acme`, `AE referred this merchant` | Load `delivery-os/templates/shopify-referral-scope-brief.md` and `delivery-os/templates/engagement-baseline.md`; treat the exception as partner-approved only when stated. |
| `SE Referral One-Pager` | `SE one-pager`, `AE referral one-pager`, `partner referral one-pager` | Load `delivery-os/templates/se-referral-one-pager.md`; keep claims partner-safe and do not add unsupported conversion metrics. |
| `Migration Package: [Merchant Name]` | `migration package Acme`, `build the migration runbook` | Route to API-first migration planning or execution and name the migration lane. |
| `Migration QA: [Merchant Name]` | `migration QA Acme`, `is this migration safe for go-live` | Route to validation/reconciliation and inspect logs, retry files, exports, and Matrixify results only when applicable. |
| `Delegate to Antigravity: [bounded task]` | `delegate to Antigravity: normalize source CSV headers`, `use Antigravity CLI: normalize source CSV headers` | Write a bounded Antigravity task contract and required `manifest.json` output. |
| `Resume Client: [Merchant Name]` | `resume Acme`, `where did we leave off with Acme` | Recall memory, tasks, recent events, decisions, blockers, and recommended next command. |
| `Kai Status` | `Kai status`, `where are we` | Show memory root status, active clients, open tasks, and stale/review-needed items. |
| `Kai Doctor` | `Kai Doctor`, `run Kai preflight` | Run preflight diagnostics for memory root, scripts, source/runtime drift, stale clients, pending runs, and open tasks. |
| `Start My Day` | `start my day`, `morning briefing` | Create a daily operator briefing from Outlook Calendar, Outlook Email, Microsoft Teams, Microsoft SharePoint, tasks, memory, and pending runs. |
| `End My Day` | `end my day`, `wrap my day` | Review completed meetings, new evidence, follow-ups, tasks, pending memory deltas, and upcoming risks. |
| `Weekly Review` | `weekly review`, `plan next week` | Summarize the week across clients, tasks, runs, decisions, stale context, next-week risk, and connector evidence. |
| `Evidence Research: [topic]` | `evidence research: Shopify POS returns`, `facts only on Acme` | Gather Facts, patterns, Anomalies, sources, and open questions only. No recommendations, pricing, scope, or final strategy. |
| `Kai Priorities` | `Kai priorities`, `what should I focus on` | Rank active work from KaizenOS MCP priorities and relationship signals first, then enrich with Outlook Email, Microsoft Teams, Microsoft SharePoint, and filesystem memory/task context. |
| `Review Workspace` | `review workspace`, `OODA review` | Surface unfinished work and identify repeatable system improvements. |
| `Close Client: [Merchant Name]` | `close client Acme`, `archive Acme safely` | Prepare closeout plan, final summary, task review, archive plan, and post-close opportunities. |
| `Log Win: [Merchant Name]` | `log win Acme`, `case study draft Acme`, `bank the Acme result` | Pull engagement actuals from the KaizenOS record (timeline, entity counts, reconciliation results), then draft approval-gated proof-bank and finding-bank entries per the Provenance & Capture Schema. |
| `Vendor Freshness Check` | `vendor freshness check`, `is Kai's Shopify knowledge fresh` | Inspect the vendor freshness manifest and report currentness, stale areas, and live-validation needs. |
| `Update Kai Vendor Knowledge` | `update Kai vendor knowledge`, `update Shopify changelog` | Run or instruct the vendor-knowledge updater, then summarize new entries and review-needed items. |
| `Check Shopify Freshness` | `check Shopify freshness`, `verify current Shopify behavior` | Review Shopify indexes, then require Shopify Dev MCP or canonical Shopify URLs for final technical claims. |
| `Check AnyDB Freshness` | `check AnyDB freshness`, `verify current AnyDB behavior` | Review AnyDB release notes and require AnyDB docs/MCP validation before build-ready guidance. |

## Evidence-Only Structure

When a command asks for evidence-only research, output: Facts, Patterns, Anomalies, Sources, Open Questions. Do not include recommendations unless the user asks for them after the evidence pass.

## Category: Daily, Status, And Priorities

### Commands

- `Kai Status`: active clients, open tasks, stale memory, pending runs, blockers, source/runtime
  drift, and one-priority focus.
- `Kai Doctor`: local health diagnostics for memory root, scripts, stale clients, pending runs,
  source/runtime drift, and open task count.
- `Start My Day`: morning operator brief from calendar, email, Teams, SharePoint, memory, tasks,
  pending runs, and highest-consequence next action.
- `End My Day`: decisions captured, follow-ups owed, tasks created/completed, memory deltas,
  evidence files touched, and next-day preview.
- `Weekly Review`: client movement, stalled items, risk concentration, account health movement,
  decisions, and next-week focus.
- `Kai Priorities`: ranked active work plus one highest-consequence next action. Source priorities
  directly from KaizenOS MCP `kai_get_priorities` first, including relationship signals; use
  filesystem memory/task signals only as secondary context, and use Outlook Email, Microsoft Teams,
  and Microsoft SharePoint to enrich or challenge the top KaizenOS-ranked items.

### Required Hooks

- Memory Hook for known clients.
- KaizenOS MCP priority source check before ranking.
- Task / Follow-Up Hook for commitments, owners, due dates, and waiting-on items.
- Evidence Gate Hook when a priority depends on proof, QA, or delivery readiness.
- Account Health / Expansion Hook when post-go-live or QBR signals appear.

### Output Discipline

- Keep daily/status outputs short enough to act on.
- Name the one priority that beats the alternatives.
- For `Kai Priorities`, rank from KaizenOS MCP priorities first. Keep filesystem memory/task
  signals separate as secondary stale-context or pending-run evidence.
- Filter obvious placeholder/test records and state when KaizenOS MCP could not be checked.
- Before finalizing the chat recommendation, check Outlook Email, Microsoft Teams, and Microsoft
  SharePoint for the top KaizenOS-ranked clients when those connectors are available.
- Do not mark tasks done unless completion is confirmed.
- Do not create accepted inferred tasks without approval.
- If source connectors are unavailable, state what could not be checked.


## Category: Pipeline And Client Intake

### Commands

- `New Deal`: create or initialize client context, gather public/private evidence, and produce a
  first opportunity review.
- `Sync Client`: recall memory, refresh source evidence, identify changed state, blockers, and
  proposed memory/task updates.
- `Prep Call`: call brief from memory, current evidence, open risks, discovery strategy, and
  one-priority focus.
- `Post Call Update`: decisions, tasks, follow-ups, memory deltas, discovery gaps, and next command.
  **Optional sales-stage evidence capture:** if the call surfaced a reusable pattern (objection,
  win theme, vertical signal), offer one draft bank entry per the Provenance & Capture Schema in
  `reference/kaizen-proposal-proof-bank.md` — approval-gated, `proposal-safe: no` by default,
  skip silently if nothing qualifies.
- `Build Blueprint`: route to diagnosis after memory recall and evidence check.
- `Build Proposal`: route to proposal after Blueprint/pricing guardrails and win-theme checks.
- `Start Delivery` / `Onboard Client`: verify the KaizenOS activation gate, derive the
  sales-to-delivery handover from canonical records, seed or reconcile the project plan without
  duplication, and produce the first-seven-days package.
- `Use Delivery OS`: load `delivery-os/README.md`, confirm the multi-location Shopify POS wedge
  fit, then select the pack that matches the current stage.
- `Run Pack 1`: build or audit the POS Delivery OS Engagement Baseline from the Blueprint
  Diagnostic or approved Shopify Referral Scope Brief.
- `Use Pack 5`: shape or audit the proposal/SOW against the approved Engagement Baseline,
  pricing source, scope boundaries, and retainer attach rules.
- `Implementation Scoping Brief`: use for the direct full-implementation lane after scoped
  discovery confirms delivery ownership, locations, stack, data/integration exposure, timeline,
  and open assumptions.
- `Shopify Referral Scope Brief`: use only for a Shopify-referred merchant where partner judgment
  approves bypassing the paid Blueprint deliverable; AE context directs discovery but does not
  replace source-system evidence.
- `Resume Client`: recall memory, active tasks, pending runs, recent decisions, blockers, and next
  command.

### Required Hooks

- KaizenOS MCP record check before client-specific synthesis or CRM/project write.
- Memory Hook before client-specific output.
- Task / Follow-Up Hook after calls, notes, or commitments.
- Pricing Usage Standard before any dollar value appears.
- Evidence Gate Hook for claims, proposal proof, or readiness decisions.
- Vendor Freshness Auto-Gate when current Shopify, AnyDB, Matrixify, Flow, or API behavior matters.

### Output Discipline

- Do not pitch implementation before discovery proves the problem.
- For existing merchants, deals, projects, or tasks, resolve the KaizenOS record first and use its
  current stage/status/owner/next action as the source state.
- For the POS Delivery OS wedge, do not move to proposal, SOW, migration, launch QA, or Ops Care
  attach without an approved Engagement Baseline.
- Do not start implementation delivery or kickoff without an accepted SOW, approved scope source,
  and first-payment confirmation. A project may exist in `Scoping` while the activation gate is
  incomplete.
- Never collect credentials in an onboarding form, task, note, or client request. Request secure
  collaborator/vendor access and store only status, owner, and canonical links.
- Keep sales frameworks internal unless the operator asks for methodology language.
- Do not expose MEDDPICC or other sales-framework jargon in client-facing output.
- Do not invent pricing, ROI, stakeholder authority, timelines, or source behavior.


## Category: Execution, QA, And Closeout

### Commands

- `Migration Package`: route to API-first migration planning or execution, name the migration
  lane, and preserve rollback/cleanup requirements.
- `Migration QA`: inspect logs, retry files, exports, reconciliation, Matrixify results when
  applicable, and produce a gated verdict.
- `Evidence Research`: gather facts, patterns, anomalies, and sources only. No strategy until
  synthesis is requested.
- `Review Workspace`: surface outstanding work first, then recommend reusable system improvements.
- `Log Win`: evidence flywheel on demand. Resolve the KaizenOS record (`kai_search_context` ->
  `kai_get_record_context`), pull engagement actuals (timeline, entity counts, reconciliation
  results, launch outcomes), and draft 1-3 bank entries (proof patterns ->
  `reference/kaizen-proposal-proof-bank.md`, diagnostic findings ->
  `reference/kaizen-blueprint-finding-bank.md`) using the Provenance & Capture Schema: source
  engagement (anonymized), date observed, vertical, confidence, proposal-safe yes/no. Default
  `proposal-safe: no`; drafts are approval-gated - never write to the banks without sign-off.
  Numbers come from KaizenOS records or labeled evidence, never invented.
- `Close Client`: closeout package, open-task review, final summary, retained opportunities, and
  safe archive plan. **Evidence flywheel step (required):** before archiving, draft 1-3 judgment
  bank entries from the engagement (proof patterns → `reference/kaizen-proposal-proof-bank.md`,
  diagnostic findings → `reference/kaizen-blueprint-finding-bank.md`) using the Provenance &
  Capture Schema: source engagement (anonymized), date observed, vertical, confidence,
  proposal-safe yes/no. Default `proposal-safe: no` until the operator explicitly approves. Drafts are
  approval-gated — present them in the closeout summary; never write to the banks without
  sign-off. If the engagement produced nothing bank-worthy, say so explicitly rather than
  skipping silently.

### Required Hooks

- Evidence Gate Hook for QA, go-live, reconciliation, case-study, and client-facing proof.
- Vendor Freshness Auto-Gate for platform-current claims.
- ABORT_CLEANUP / Created Resource Ledger when artifacts or resources are created.
- Task / Follow-Up Hook for blockers, remediation, archive actions, and next steps.
- Account Health / Expansion Hook for post-close opportunities.

### Output Discipline

- Default critical delivery verdict is `NOT READY` until evidence clears the gate.
- Do not continue live imports before failed patterns are isolated.
- Do not delete or archive evidence, memory, exports, or run folders automatically.
- Do not turn evidence-only work into strategy in the same pass.


## Category: Vendor Freshness And Operating Hooks

### Commands

- `Vendor Freshness Check`: inspect the generated vendor freshness manifest, changelog state,
  needs-merge items, and affected Kai domains.
- `Update Kai Vendor Knowledge`: run or instruct the vendor updater and summarize generated files,
  new entries, and review-needed items.
- `Check Shopify Freshness`: inspect Shopify developer/help indexes and validate technical claims
  with Shopify Dev MCP or canonical Shopify URLs.
- `Check AnyDB Freshness`: inspect AnyDB release notes and validate build-ready guidance with
  AnyDB docs/MCP.

### Required Hooks

- Vendor Freshness Auto-Gate for Shopify, AnyDB, Matrixify, Flow, API, plan, rollout, or
  integration behavior.
- Evidence Gate Hook when the platform claim affects QA, go-live, proposal proof, or client-facing
  recommendation.
- Runtime Portability check when local generated indexes are unavailable.

### Output Discipline

- Treat `reference-content/` as navigation, not final proof.
- Treat `_needs-merge.md` as active infrastructure, not dead content.
- Use live source validation for build-ready, version-sensitive, plan-sensitive, rollout-sensitive,
  or client-facing claims.
- If live validation cannot run, mark the point as needing verification instead of guessing.


## Full Contract

Read `reference/kaizen-command-palette-contract.md` for the full alias map, memory-hook checklist, connector-data gathering contract, run-folder expectations, task-ledger outputs, and command-specific edge cases.
