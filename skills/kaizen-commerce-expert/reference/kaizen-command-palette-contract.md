# Kaizen Command Palette

Load this file when the operator uses a short workflow command such as `New Deal`, `Sync Client`,
`Prep Call`, `Post Call Update`, `Build Blueprint`, `Use Delivery OS`, `Start Delivery`, `Onboard Client`, `Migration Package`, `Migration QA`,
`Delegate to Antigravity`, `Resume Client`, `Kai Status`, `Kai Doctor`, `Start My Day`, `End My Day`,
`Weekly Review`, `Evidence Research`, `Kai Priorities`, `Review Workspace`, `Close Client`,
`Vendor Freshness Check`, `Update Kai Vendor Knowledge`, `Check Shopify Freshness`, or
`Check AnyDB Freshness`.

This is Kai's operator command layer. It turns short commands into complete, evidence-first
workflows while keeping `SKILL.md` lean.

## Progressive Disclosure References

Use this file as the canonical command index. When the command category is clear and deeper
workflow guidance is needed, load only the matching category reference:

| Category | Commands | Reference |
|---|---|---|
| Daily, status, priorities | `Kai Status`, `Kai Doctor`, `Start My Day`, `End My Day`, `Weekly Review`, `Kai Priorities` | `reference/kaizen-command-palette.md` (Category: Daily, Status, And Priorities) |
| Pipeline and client intake | `New Deal`, `Sync Client`, `Prep Call`, `Post Call Update`, `Build Blueprint`, `Build Proposal`, `Start Delivery`, `Onboard Client`, `Resume Client` | `reference/kaizen-command-palette.md` (Category: Pipeline And Client Intake) |
| POS Delivery OS wedge | `Use Delivery OS`, `Run Pack 1`, `Use Pack 5`, `Audit against Pack 5`, `Build Engagement Baseline`, `Implementation Scoping Brief`, `Shopify Referral Scope Brief` | `delivery-os/README.md` |
| Execution, QA, closeout | `Migration Package`, `Migration QA`, `Evidence Research`, `Review Workspace`, `Close Client` | `reference/kaizen-command-palette.md` (Category: Execution, QA, And Closeout) |
| Vendor freshness and hooks | `Vendor Freshness Check`, `Update Kai Vendor Knowledge`, `Check Shopify Freshness`, `Check AnyDB Freshness`, operating hooks | `reference/kaizen-command-palette.md` (Category: Vendor Freshness And Operating Hooks) |

Do not load every category reference for a single command. Load the command index first, then the
one category reference that matches the workflow.

## Command Rules

- Treat exact command phrases as execution requests, not brainstorming prompts.
- Treat close natural-language equivalents as the same execution requests. Normalize the user's
  phrase to the nearest canonical command, then run that workflow.
- Do not force the operator to remember exact command names. If the intent is clear from phrasing like
  "begin my day", "catch me up", "what should I work on next", "wrap my day", "help me prep for my
  call", or "process these notes", execute the matching command.
- Ask a clarification only when two command intents are genuinely plausible, when a required
  merchant/client name is missing for client-specific work, or when the next action is destructive
  or externally visible.
- Create or recall client memory before client-specific work.
- Load `reference/kaizen-memory-hook-protocol.md` for client-specific commands and known-client
  natural-language aliases. Auto-recall known client memory first, then continue the command.
- After meaningful client work, draft a memory update proposal when client state changed. Never
  apply the update without explicit approval.
- For commands that need private deal context, gather evidence before synthesis.
- Keep authoritative decisions, pricing, migration lane selection, final QA, and client-facing
  synthesis in Kai.
- Antigravity CLI may receive bounded grunt-work tasks only after Kai writes a task contract.
- When delegated execution is explicitly requested, try `agy` first, then Grok Build CLI (`grok`) if
  Antigravity is unavailable, unusable, or quota-blocked; never claim either CLI ran without output.
- Antigravity CLI must not access production credentials, write authoritative memory, choose migration
  lanes, or produce final client-facing recommendations without Kai review.
- Use `scripts/kaizen-workflow.py` when a run folder or task ledger entry is useful.
- Use `scripts/kaizen-tasks.py` for task ledger operations.
- In the installed skill runtime, these scripts are wrappers that forward to the durable
  `kaizen-skills` source checkout. Prefer running from the source repo root; set
  `KAIZEN_SKILLS_ROOT` or `KAI_SOURCE_ROOT` if the checkout is not at the default path.
- For vendor freshness commands, load `reference/kaizen-vendor-freshness-protocol.md` and inspect
  `reference-content/` before giving a freshness verdict.
- Load `reference/kaizen-operating-hook-protocols.md` when a command touches vendor-current
  platform behavior, proof/readiness verdicts, follow-up/task extraction, or account-health and
  expansion judgment.

## Command Table

| Command | Trigger examples | Primary action |
|---|---|---|
| `New Deal: [Merchant Name]` | `New Deal: Acme Retail`, `new deal Acme Retail`, `new lead from Acme`, `new opportunity: Acme` | Initialize client memory, create a run folder, gather Outlook/Teams/SharePoint/Exa evidence, create task ledger entries, and produce a first Kai opportunity review. |
| `Sync Client: [Merchant Name]` | `sync client Acme`, `refresh Acme context`, `catch me up on Acme`, `what changed with Acme` | Recall client memory, gather new private/public evidence, update context deltas, and identify new tasks or blockers. |
| `Prep Call: [Merchant Name]` | `prep call Acme`, `prep me for Acme discovery`, `help me get ready for my Acme call`, `I have a call with Acme` | Build a call brief from memory, recent evidence, open tasks, known gaps, and discovery strategy. |
| `Post Call Update: [Merchant Name]` | `post call update Acme`, `process these Acme notes`, `turn this call into next steps`, `capture follow-ups from this call` | Convert call notes into reviewed memory updates, tasks, decisions, next actions, and follow-up draft if needed. |
| `Build Blueprint: [Merchant Name]` | `build blueprint Acme`, `diagnose Acme`, `turn this into a Blueprint`, `what is the operating diagnosis for Acme` | Route to `kaizen-diagnose.md` after memory recall and evidence check. |
| `Build Proposal: [Merchant Name]` | `build proposal Acme`, `generate SOW Acme`, `draft the Acme proposal`, `turn this scope into a proposal` | Route to `kaizen-propose.md` and pricing rules after memory recall and scoped-evidence check. |
| `Start Delivery: [Merchant Name]` | `start delivery Acme`, `onboard Acme`, `kick off Acme`, `set up the Acme project` | Load `reference/kaizen-client-journey.md`, resolve the KaizenOS deal/project, verify activation conditions, use `kai_activate_deal_engagement` for accepted commercial activation, and preview only missing direct/manual project-plan writes before approval. |
| `Use Delivery OS: [Merchant Name]` | `use delivery os Acme`, `run the POS wedge for Acme`, `run Delivery OS for this multi-location POS deal` | Load `delivery-os/README.md`. Confirm the opportunity fits the multi-location Shopify POS transformation wedge, then select the needed pack. |
| `Run Pack 1: [Merchant Name]` | `run Pack 1 for Acme`, `run the Blueprint Diagnostic Pack`, `build the Engagement Baseline` | Load `delivery-os/01-blueprint-diagnostic-pack.md` and produce or audit the Engagement Baseline path. |
| `Use Pack 5: [Merchant Name]` | `use Pack 5 for this proposal`, `shape this SOW with Pack 5`, `audit this proposal against Pack 5` | Load `delivery-os/05-sales-sow-pack.md`; require scoped evidence or route back to Pack 1. |
| `Implementation Scoping Brief: [Merchant Name]` | `implementation scoping brief Acme`, `scoping brief Acme`, `full implementation scoping Acme` | Load `delivery-os/templates/implementation-scoping-brief.md` and `delivery-os/templates/engagement-baseline.md`; use for direct full implementation after a qualified scoping call. |
| `Shopify Referral Scope Brief: [Merchant Name]` | `Shopify referral brief Acme`, `AE referred this merchant`, `skip Blueprint for a Shopify referral` | Load `delivery-os/templates/shopify-referral-scope-brief.md` and `delivery-os/templates/engagement-baseline.md`; treat the exception as partner-approved only when stated. |
| `Migration Package: [Merchant Name]` | `migration package Acme`, `plan the Acme migration`, `build the migration runbook`, `package this migration` | Route to API-first migration planning or execution. Name the migration lane. |
| `Migration QA: [Merchant Name]` | `migration QA Acme`, `review API migration logs Acme`, `is this migration safe for go-live`, `check these import logs` | Route to validation/reconciliation and inspect API logs, retry files, exports, and Matrixify results only when applicable. |
| `Delegate to Antigravity: [bounded task]` | `delegate to Antigravity: normalize source CSV headers`, `use Antigravity CLI: normalize source CSV headers` | Write a bounded Antigravity task contract and required `manifest.json` output. |
| `Resume Client: [Merchant Name]` | `resume Acme`, `where are we with Acme`, `where did we leave off with Acme` | Recall memory, open tasks, recent events, decisions, blockers, and recommended next command. |
| `Kai Status` | `Kai status`, `status of active clients`, `where are we`, `catch me up`, `what's active` | Show memory root status, active clients, open tasks, and stale/review-needed items. |
| `Kai Doctor` | `Kai Doctor`, `run Kai preflight`, `check Kai setup`, `is Kai healthy` | Run preflight diagnostics for memory root, scripts, source/runtime drift, stale clients, pending runs, and open tasks. |
| `Start My Day` | `start my day`, `begin my day`, `just starting off my day`, `morning briefing`, `morning check-in`, `what should I look at today` | Create a concise daily operator briefing from Outlook Calendar, Outlook Email, Teams, SharePoint, tasks, memory, and pending runs. |
| `End My Day` | `end my day`, `wrap up`, `wrap my day`, `done for today`, `close out today`, `what did I miss today` | Review completed meetings, new evidence, follow-ups, tasks, pending memory deltas, and tomorrow/next-week preview. |
| `Weekly Review` | `weekly review`, `review the week`, `how did the week go`, `plan next week`, `weekly wrap` | Summarize the week across clients, tasks, runs, decisions, stale context, next-week risk, and connector evidence. |
| `Evidence Research: [topic]` | `evidence research: Shopify POS returns`, `facts only on Acme`, `research this without recommendations`, `source-backed facts on this` | Gather facts, patterns, anomalies, and sources only. No recommendations, pricing, scope, or final strategy. |
| `Kai Priorities` | `Kai priorities`, `what should I focus on`, `what should I do next`, `what matters most right now`, `rank my priorities` | Rank active work from KaizenOS MCP priorities and relationship signals first, then enrich the top records with Outlook Email, Microsoft Teams, Microsoft SharePoint, and filesystem memory/task context. |
| `Review Workspace` | `review workspace`, `OODA review`, `what can we improve`, `things feel messy`, `audit the workspace` | Surface unfinished work, then identify repeatable system improvements for skills, scripts, memory, references, and validation. |
| `Close Client: [Merchant Name]` | `close client Acme`, `archive Acme safely`, `finish Acme closeout`, `we are done with Acme` | Prepare a safe closeout plan, final summary, task review, archive plan, and post-close opportunities. |
| `Vendor Freshness Check` | `vendor freshness check`, `is Kai's Shopify knowledge fresh`, `check platform freshness`, `is this platform info stale` | Inspect the generated vendor freshness manifest, needs-merge log, and relevant Shopify/AnyDB sections; report currentness, stale areas, and live-validation needs. |
| `Update Kai Vendor Knowledge` | `update Kai vendor knowledge`, `update Shopify changelog`, `refresh AnyDB releases`, `refresh platform knowledge` | Run or instruct `python3 skills/kaizen-commerce-expert/scripts/update_vendor_knowledge.py`, then summarize new entries, auto-curated updates, and items needing review. |
| `Check Shopify Freshness` | `check Shopify freshness`, `is this Shopify API info current`, `verify current Shopify behavior` | Review Shopify developer and merchant changelog indexes, then require Shopify Dev MCP or canonical Shopify URLs for final technical claims. |
| `Check AnyDB Freshness` | `check AnyDB freshness`, `AnyDB releases`, `is this AnyDB behavior current`, `verify current AnyDB behavior` | Review AnyDB release, roadmap, and generated section notes; require AnyDB docs/MCP validation before build-ready guidance. |

## Natural-Language Alias Map

Use this map when the operator asks naturally instead of using a command name.

| User phrase pattern | Canonical command |
|---|---|
| "begin my day", "starting off my day", "morning check-in", "what should I look at today" | `Start My Day` |
| "done for today", "wrap my day", "close out today", "what did I miss today" | `End My Day` |
| "where are we", "catch me up", "what's active", "current status" | `Kai Status` |
| "what should I do next", "what matters most", "rank my priorities" | `Kai Priorities` |
| "things feel messy", "audit the workspace", "what can we improve" | `Review Workspace` |
| "help me get ready for my call with [merchant]", "I have a call with [merchant]" | `Prep Call: [Merchant Name]` |
| "process these notes", "turn this call into next steps", "capture follow-ups" | `Post Call Update: [Merchant Name]` when a merchant is known, otherwise ask for the merchant/client name |
| "new lead from [merchant]", "new opportunity: [merchant]" | `New Deal: [Merchant Name]` |
| "start delivery for [merchant]", "onboard [merchant]", "kick off [merchant]", "set up the [merchant] project" | `Start Delivery: [Merchant Name]` |
| "use Delivery OS for [merchant]", "run the POS wedge for [merchant]", "this is a Shopify POS transformation" | `Use Delivery OS: [Merchant Name]` |
| "build the Engagement Baseline", "Shopify referral scope brief", "AE referred this merchant" | `Run Pack 1: [Merchant Name]` or `Shopify Referral Scope Brief: [Merchant Name]`; choose the referral command only when Shopify referral context is explicit |
| "where did we leave off with [merchant]", "catch me up on [merchant]" | `Resume Client: [Merchant Name]` or `Sync Client: [Merchant Name]`; choose `Sync Client` when the user asks to refresh evidence |

## Memory Hook Protocol

For client-specific commands, Kai should behave as if memory recall is part of the command even
when the operator does not say "memory."

Use `reference/kaizen-memory-hook-protocol.md` with:

- `Prep Call`
- `Post Call Update`
- `Build Blueprint`
- `Build Proposal`
- `Start Delivery`
- `Onboard Client`
- `Use Delivery OS`
- `Run Pack 1`
- `Use Pack 5`
- `Shopify Referral Scope Brief`
- `Migration QA`
- `Resume Client`
- `Sync Client`
- `Close Client`
- natural-language equivalents such as "catch me up on Acme", "help me prep for my Acme call",
  "process these notes", and "save this to Acme memory"

Read behavior:

- If exactly one known client matches, run `./scripts/kaizen-memory-recall.py "[Client Name]"`
  before producing the command output.
- If no known client matches, ask before creating memory unless the command is `New Deal`.
- If multiple clients match, ask one short clarification question.

Write behavior:

- Draft a proposed memory update after client decisions, confirmed stack changes, call notes,
  proposal/SOW status, pricing approvals, migration lane decisions, QA verdicts, delivery updates,
  go-live updates, QBR/account-health changes, or post-go-live metrics.
- Do not draft memory updates for casual brainstorming, generic Shopify/AnyDB advice, unsent
  draft emails, unsupported assumptions, raw exports, secrets, credentials, tokens, or API keys.
- Surface the proposal in chat. When a run folder exists, also write `kai/context-delta.md` and
  `kai/memory_delta.json`.
- Apply only after explicit approval such as "apply the memory update for Acme" or "save this to
  Acme memory."

## Operating Hook Protocols

Use `reference/kaizen-operating-hook-protocols.md` for safe automatic checks that should run
around command workflows. These hooks make Kai more automatic without allowing silent writes,
silent approvals, or unverified platform claims.

### Vendor Freshness Auto-Gate

Trigger when the command or output depends on current Shopify, AnyDB, Matrixify, Flow, API,
plan/rollout, or integration behavior.

Behavior:

- check `reference-content/` for recent Shopify/AnyDB changes and `[NEEDS-MERGE]` items
- validate with Shopify Dev MCP, AnyDB docs/MCP, Matrixify docs, or canonical vendor URLs when the
  claim is build-ready, version-sensitive, plan-sensitive, rollout-sensitive, or client-facing
- block with `NOT READY`, `DEFER`, or a visible caveat when the current source has not been checked

### Evidence Gate Hook

Trigger for QA, migration readiness, reconciliation, go-live, automation approval, proposal proof,
QBR claims, case study claims, ROI, savings, or client-facing outcome claims.

Behavior:

- load `reference/kaizen-evidence-and-gates.md`
- default critical delivery work to `NOT READY` until sources, files, counts, commands, screenshots
  or logs, assumptions, and automatic fail gates are accounted for
- produce an Evidence Manifest for substantial work

### Task / Follow-Up Hook

Trigger for notes, transcripts, post-call updates, follow-up drafts, commitments, blockers, due
dates, owners, `Start My Day`, `End My Day`, `Weekly Review`, `Kai Status`, `Kai Priorities`,
`Review Workspace`, and `Close Client`.

Behavior:

- extract proposed tasks with owner, due date, source, client, priority, and confidence when known
- keep inferred tasks as proposals with `userAccepted: false`
- when a run folder exists, write `kai/proposed_tasks.json`
- never mark a task complete unless the send, handoff, validation, or approval actually happened

### Account Health / Expansion Hook

Trigger for post-go-live reports, QBRs, retainers, expansion, upsell, support risk, churn risk,
referrals, testimonials, case studies, and client closeout.

Behavior:

- classify Green, Yellow, Red, or Unknown when enough evidence exists
- require signal, context, timing, and stakeholder alignment before expansion language
- use stabilize-first logic for Yellow and save/stabilize logic for Red
- run the Evidence Gate Hook for claims about ROI, savings, performance, adoption, or case-study
  outcomes

## Operator Pattern Additions

Apply these add-ons to the named commands without changing their existing script usage or evidence
requirements.

### Kai Status

Add a `State of Play` brief:

- active clients, active runs, open tasks, stale memory, and source/runtime drift
- last meaningful movement by client or agency system
- blocked items that need the operator, client, partner, or evidence input
- one-priority focus for the next work block

Add a `Decision Log` summary when decisions changed since the last status:

- decision made
- source evidence or approving person
- affected files, client memory, proposal, migration plan, or automation
- cascading update check required

### Start My Day

Add a morning `State of Play`:

- what matters today
- where evidence is stale
- which meetings need prep
- which client/prospect has the highest consequence if ignored
- one-priority focus before opening secondary work

Add a `Document Dependency Map` when a meeting, proposal, migration, or QA item depends on files:

- source document
- dependent output
- owner
- freshness risk
- next update needed

### End My Day

Add a daily `Decision Log` and `Cascading Update Check`:

- decisions made today
- where each decision must be reflected: memory, task ledger, proposal, SOW, migration plan,
  AnyDB spec, Flow spec, report, or follow-up email
- evidence files or connector sources that justify the update
- tomorrow's one-priority focus

Do not mark a task closed just because a draft was produced. Completion requires the intended
handoff, send, validation, or approval to be done.

### Weekly Review

Add a weekly `State of Play`:

- client pipeline movement
- stalled items
- risk concentration by client, scope, data, stakeholder, or evidence gap
- account health movement where post-go-live clients exist
- one-priority focus for the coming week

Add a `Positioning-for-Impact Check`:

- where Kaizen has a clear operational consequence to teach
- where messaging is still generic
- which proposal, follow-up, or QBR should be tightened around business impact

### Kai Priorities

Add one-priority focus discipline:

- pick the single highest-consequence next action
- explain why it beats the next two alternatives
- name the evidence that makes it urgent
- name the command that should execute it

Scores are advisory. If a score conflicts with a client deadline, cash impact, trust risk, or
approved commitment, explain the override instead of hiding it.

### Review Workspace

Add a `Document Dependency Map` and `Cascading Update Check`:

- files or references changed
- downstream documents affected
- command palette, skill, memory, script, or source/runtime sync implications
- validation required before the change can be treated as durable

Review Workspace may recommend improvements, but implementation still requires either explicit
approval or a direct implementation request from the operator.

### Vendor Freshness Commands

Use these commands when Kai's local Shopify, AnyDB, Matrixify, or automation knowledge may be stale.

`Vendor Freshness Check` output:

- last vendor index update
- source status for Shopify merchant changelog, Shopify developer changelog, AnyDB releases, and
  AnyDB roadmap
- count of auto-curated items and `[NEEDS-MERGE]` items
- affected Kai domains: migration, POS, Flow, AnyDB, proposal, training, reporting, or outreach
- whether live MCP/docs validation is required before the current answer can be final

`Update Kai Vendor Knowledge` execution:

```bash
python3 skills/kaizen-commerce-expert/scripts/update_vendor_knowledge.py
```

After running it, summarize:

- new entries found
- generated files updated
- items marked `[NEEDS-MERGE]`
- any source fetch errors
- whether the runtime skill also needs source sync/install

`Check Shopify Freshness`:

- inspect `reference-content/shopify-dev/` and `reference-content/shopify-help/`
- use Shopify Dev MCP for Admin GraphQL, API versions, scopes, CLI, POS UI, Functions, Liquid,
  Hydrogen, Polaris, custom data, and extension targets
- use canonical Shopify public URLs for merchant/admin behavior, plan availability, rollout,
  taxes, payments, Markets, POS, checkout, and customer accounts

`Check AnyDB Freshness`:

- inspect `reference-content/anydb/`
- use AnyDB docs/MCP for formulas, cell types, references, rollups, imports, workflows, and
  Shopify sync before producing a build-ready artifact
- treat AnyDB roadmap items as directional unless release notes or docs confirm shipped behavior

### Close Client

Add a `Closeout Package` before archive recommendations:

- final State of Play
- open tasks and disposition
- delivered artifacts and evidence links
- Decision Log
- outstanding invoices, approvals, or unresolved commitments if known
- retained assets: case study, testimonial, referral, reactivation, support, or retainer angle
- final Document Dependency Map for client memory, proposals, SOWs, migration files, reports,
  exports, and client-visible docs

Add a `Positioning-for-Impact Check` before reactivation, case study, or testimonial language.
Claims must be evidence-backed and must not inflate outcomes beyond the source material.

## New Deal Workflow

`New Deal: [Merchant Name]` is the default intake command for a new prospect, lead, referral,
or active opportunity.

### Script Scaffold

Run from the kaizen-skills checkout (default `~/Documents/Codex/kaizen-skills`) when a local run folder is useful:

```bash
./scripts/kaizen-workflow.py new-deal "Merchant Name" --website "https://example.com"
```

The script creates:

```text
kaizen-memory/
  clients/[merchant-slug]/
  runs/[date]-[merchant-slug]-new-deal/
    TASK.md
    antigravity/
      manifest.json
      evidence/
      outputs/
    kai/
      REVIEW.md
      context-delta.md
      memory_delta.json
      evidence/
    APPROVAL.md
  tasks/active/
```

### Required Data Gathering

Kai should gather available context before drafting the opportunity review.

1. Outlook Email
   - Search for merchant name, domain, stakeholder names, proposal language, discovery notes,
     attachments, calendar-derived signals, and recent threads.
   - Save source-backed notes to `kai/evidence/outlook-email.md`.
2. Microsoft Teams
   - Search chats and messages for the merchant, contacts, blockers, technical asks, timelines,
     and follow-ups.
   - Save source-backed notes to `kai/evidence/microsoft-teams.md`.
3. Microsoft SharePoint
   - Search for transcripts, meeting notes, discovery docs, proposal drafts, data exports,
     spreadsheets, decks, and merchant folders.
   - Save source-backed notes to `kai/evidence/sharepoint.md`.
4. Exa MCP
   - Gather public merchant research: website, store count, current platform signals, Shopify
     signals, POS/ecommerce stack clues, operations footprint, and risk signals.
   - Save source-backed notes to `kai/evidence/exa-public-research.md`.
5. Shopify Dev MCP
   - Use only when the New Deal review generates or validates current Shopify technical behavior,
     API/GraphQL, Shopify CLI, POS UI, Liquid, Hydrogen, Functions, or Polaris behavior.

### REVIEW.md Contract

Kai writes `kai/REVIEW.md` with:

- `Status`: `PASS`, `PASS WITH NOTES`, or `FAIL`
- evidence gathered by source
- current known stack
- confirmed, inferred, and unknown merchant facts
- stakeholder and timeline signals
- operational pain points
- opportunity hypothesis
- likely Kaizen entry point
- missing inputs
- open task summary
- recommended next command
- whether Antigravity CLI should receive a bounded task
- whether memory should be updated

### Memory Contract

Kai owns authoritative memory. After evidence review:

- write `kai/context-delta.md` and, when a run folder exists, `kai/memory_delta.json`
- surface a compact memory proposal in chat with the exact approval phrase
- apply reviewed durable changes with `scripts/kaizen-memory-apply-delta.py`
- run `scripts/kaizen-memory-consolidate.py` after major updates

Do not store secrets, credentials, API tokens, private customer exports, or unnecessary bulk
transcript content in memory. Store source references and concise evidence instead.

## Kai Doctor

`Kai Doctor` is the preflight command for checking whether Kai is ready for serious work.

Run from the kaizen-skills checkout (default `~/Documents/Codex/kaizen-skills`):

```bash
./scripts/kaizen-workflow.py doctor
```

The script checks:

- memory root exists and can be initialized
- active clients and run folders
- stale client memory
- pending run folders with `PENDING`, `NEEDS_REVIEW`, or `BLOCKED`
- active task count
- required workflow scripts exist and are executable
- source/runtime drift for key Kai files under `~/.codex/skills`

The report is written to:

```text
kaizen-memory/agency/kai-doctor-report.md
```

Kai should run or suggest `Kai Doctor` before:

- large proposal/SOW work
- migration execution or QA
- memory maintenance
- command palette debugging
- any session where stale client context could change the answer

## Daily Briefing Commands

### Start My Day

Use for morning planning.

```bash
./scripts/kaizen-workflow.py start-my-day
```

Kai gathers:

- Outlook Calendar: today's accepted/tentative/owned events and calls needing prep
- Outlook Email: unread or recent client/prospect threads requiring action
- Microsoft Teams: mentions, client/prospect chats, blockers, and urgent updates
- Microsoft SharePoint: transcripts, meeting notes, decks, exports, and docs modified since the last workday
- Kaizen memory: active clients, open tasks, pending runs, stale clients, and Kai Doctor warnings

Output should be a concise operator brief:

- top priorities
- meetings requiring prep
- client/prospect items needing action
- open blockers
- stale context
- recommended next Kai commands

### End My Day

Use for wrap-up.

```bash
./scripts/kaizen-workflow.py end-my-day
```

Kai gathers:

- Outlook Calendar: completed meetings and missed prep/follow-up needs
- Outlook Email: sent/received client updates, unanswered threads, and promised follow-ups
- Microsoft Teams: decisions, blockers, action items, and client/prospect mentions from today
- Microsoft SharePoint: transcripts or files created/modified today that should become evidence
- Kaizen memory: tasks created/completed today, run folders touched, context deltas needing review, tomorrow preview

Output should include:

- completed work
- decisions captured
- tasks created/completed
- follow-ups owed
- memory updates needed
- next workday preview

### Weekly Review

Use for week-level operating control.

```bash
./scripts/kaizen-workflow.py weekly-review
```

Kai gathers:

- Outlook Calendar: last seven days of client/prospect meetings and next week preview
- Outlook Email: active deal/client threads, stalled replies, and follow-up obligations
- Microsoft Teams: week-level decisions, blockers, AE/partner signals, and commitments
- Microsoft SharePoint: transcripts, proposals, exports, or decks modified this week
- Kaizen memory: active clients, open tasks, pending runs, stale clients, and major decisions logged this week

## Evidence-Only Research Mode

Use `Evidence Research: [topic]` when research should not become strategy yet.

```bash
./scripts/kaizen-workflow.py evidence-research "Research topic"
./scripts/kaizen-workflow.py evidence-research "Research topic" --client "Merchant Name"
```

Required output structure:

1. Facts
   - each fact has a source, date when available, and exact value or short snippet
2. Patterns
   - observable patterns only, no recommendations
3. Anomalies
   - contradictions, missing data, suspicious values, confidence gaps
4. Sources
   - URLs, file paths, connector names, MCP/tool references

Forbidden in evidence-only mode:

- strategic recommendations
- business impact claims
- pricing
- scope decisions
- migration lane decisions
- final client-facing synthesis

Antigravity CLI may be used for this mode when Kai writes a bounded evidence task. Antigravity must return
`manifest.json` plus source-backed evidence files, not a prose-only summary.

## Kai Priorities

Use `Kai Priorities` to generate an internal operating dashboard.

```bash
./scripts/kaizen-workflow.py priorities
```

The script scores active clients using:

- KaizenOS MCP priorities, record context, and relationship signals
- active task priority and status
- pending run folders
- stale client memory
- commercial lane / source artifact status
- known tier / engagement signal

It writes:

```text
kaizen-memory/agency/kai-priorities.md
```

Kai should treat the score as a prioritization aid, not a commercial truth. Final priority still
depends on client commitments, deadlines, approved scope, cash impact, and the operator's judgment.
If KaizenOS MCP is unavailable, the command should still run and explicitly state that KaizenOS
could not be checked.

## Review Workspace

Use `Review Workspace` after focused work sessions, before large refactors, or when Kai feels
slower than it should.

```bash
./scripts/kaizen-workflow.py review-workspace
```

Workflow:

1. Complete or surface outstanding work first.
   - accepted active tasks
   - pending run folders
   - uncommitted source changes
2. Run OODA.
   - Observe: what happened this session?
   - Orient: what repeated, slowed down, or required lookup?
   - Decide: what reusable improvement is worth making?
   - Act: implement approved changes only, then validate/install/commit/push if appropriate.

Output should include:

- outstanding work summary
- systemic improvements found
- recommended implementation order
- files/scripts likely affected
- whether memory should be updated

## Close Client

Use `Close Client: [Merchant Name]` when an engagement is complete, lost, paused, or needs safe
archive review.

```bash
./scripts/kaizen-workflow.py close-client "Merchant Name"
```

Kai must review before any archive action:

- client memory profile and summary
- active tasks
- pending run folders
- unreviewed Antigravity manifests
- context deltas or approvals
- unresolved blockers
- retainer, case study, testimonial, referral, or reactivation opportunities

Safety rules:

- do not delete memory, evidence, exports, transcripts, or run folders
- do not mark tasks done unless completion is confirmed
- do not remove source references
- keep case study/testimonial claims evidence-backed

## Task Ledger

Tasks live under the memory root:

```text
kaizen-memory/
  tasks/
    schema.json
    active/
      task_[timestamp]_[slug].json
    archive/
      YYYY/
        MM/
          task_[timestamp]_[slug].json
```

Use:

```bash
./scripts/kaizen-tasks.py add --client "Merchant Name" --title "Gather Outlook evidence" --user-accepted
./scripts/kaizen-tasks.py list --client "Merchant Name"
./scripts/kaizen-tasks.py status task_20260512123000_merchant done
```

Task rules:

- explicit command-created tasks use `userAccepted: true`
- auto-detected tasks from notes, transcripts, or Antigravity manifests use `userAccepted: false`
- titles should be short, verb-first, and merchant-free
- task descriptions should preserve the source run folder, file, or transcript reference

## Next Command Suggestions

After command workflows, end with two to four relevant copyable next commands, for example:

- `Sync Client: [Merchant Name]`
- `Prep Call: [Merchant Name]`
- `Build Blueprint: [Merchant Name]`
- `Delegate to Antigravity: [bounded task]`

Do not repeat commands already completed in the same run unless they are genuinely the next step.
