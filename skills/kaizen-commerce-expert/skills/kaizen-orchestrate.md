<!-- KaizenCommerce Expert System — Codex Skill Knowledge -->
<!-- Load this file on demand from the main skill router -->

---
name: kaizen-orchestrate
description: >
  KaizenCommerce Engagement Orchestrator — semi-autonomous engagement runner that chains skills
  from signed deal (or new prospect) through post-delivery. Five modes: (1) Run Engagement — full
  pipeline for a client and tier, (2) Resume — pick up where you left off via client memory,
  (3) Skip to Phase — jump to a specific phase, (4) Status — show engagement progress,
  (5) Phase Only — run a single phase in isolation.
  Trigger on: "run engagement for [client]", "resume [client]", "skip to phase [N]",
  "engagement status for [client]", "run phase [N] for [client]", "orchestrate", "factory mode",
  "start the pipeline for [client]".
  This skill coordinates other skills — it does NOT replace them. Every skill continues to work
  standalone. The orchestrator is an optional coordination layer.
metadata_version: 1
layer: internal-operations
upstream: []
downstream: []
adjacent: []
canon: ["reference/kaizen-kaizenos-integration-map.md"]
owns: ["Phase routing, handoff discipline"]
does_not_own: ["Replacing phase-level skills"]
---

# KaizenCommerce — Engagement Orchestrator

**Canon (R2 — never restated here):** voice/forbidden phrases → `reference/kaizen-voice.md` · money/tiers → `reference/kaizen-pricing.md` · firm targets → `reference/kaizen-identity.md`.

v1.0 capstone skill. This is the coordination layer that runs a KaizenCommerce engagement from first contact through post-delivery, invoking skills in sequence with human approval gates at critical moments. It does not replace individual skills. It chains them.

**Foundation:** Apply your foundational KaizenCommerce knowledge for tier logic, voice rules, pricing, ICP criteria, and commercial guardrails. Do not duplicate that content. Reference and apply it.

**Reference files — load on demand:**
- `reference/kaizen-surface-complexity.md` — merchant profile classification; load at Phase 1 when tier is being confirmed, to validate surface complexity vs. pricing tier
- `reference/kaizen-operational-readiness.md` — maturity model; load at Phase 1 (post-Blueprint) to calibrate Phase 3 training intensity and Phase 5 retainer tier
- `reference/kaizen-risk-matrix.md` — risk register; load at Phase 3 start (Build) for any Gold/Diamond engagement
- `reference/kaizen-client-journey.md` — KaizenOS-owned activation, handover, first-seven-days,
  delivery-phase, and closeout contract
- `reference/kaizen-kaizenos-integration-map.md` — canonical read/write sequences and approval discipline

**Platform context:** This skill now runs in a Codex/ChatGPT-style environment. Filesystem access, local tools, and browsing may be available. Prefer direct execution when it is faster and safer; fall back to the chat-driven orchestration flow here when the task is primarily routing, sequencing, or handoff management.

## KaizenOS Control Plane

KaizenOS is the system of record for every durable engagement fact: deal stage, accepted
quote/SOW evidence, invoices, project status, current phase, milestones, tasks, dependencies,
client requests, activities, documents, updates, and priorities.

At session start, phase start, resume, and status:

1. resolve the merchant/deal/project with `kai_search_context`
2. load bounded live state with `kai_get_record_context`
3. use current KaizenOS phase, milestones, tasks, blockers, and requests as the starting position
4. recall Kai memory only for judgment narrative and operator preferences

If memory conflicts with KaizenOS, current KaizenOS state wins. Draft a correction; never run a
rival phase/task tracker from memory or filesystem state.

## Mode Detection

| Input pattern | Mode |
|---|---|
| "Run engagement for [client]" / "start pipeline for [client]" / "orchestrate [client]" / client name + tier + "go" | RUN ENGAGEMENT |
| "Resume [client]" / "pick up where we left off" / "continue the engagement" | RESUME |
| "Skip to phase [N]" / "jump to [phase name]" / "we already have the SOW signed" | SKIP TO PHASE |
| "Status for [client]" / "where are we with [client]" / "engagement progress" | STATUS |
| "Run phase [N] for [client]" / "just the build phase" / "phase [N] only" | PHASE ONLY |
| Ambiguous | Ask: "Are you starting a new engagement, resuming an existing one, or checking status?" |

---

## Shared Infrastructure

### Step Execution Protocol

Every step in every phase follows this sequence:

1. **Announce** the step using the step header format (see Output Format below)
2. **Recall** current KaizenOS record context, then relevant Kai memory narrative
3. **Execute** the skill, applying its full knowledge and producing its standard output
4. **Validate** the output if it is client-facing (invoke kaizen-check)
5. **Save** durable state to KaizenOS through approval-gated named tools; draft a Kai memory
   narrative only when judgment context changed
6. **Transition** to the next step, or present an approval gate if one is required

If a step produces low-quality output or encounters missing information, STOP. Do not proceed. Present the issue and ask for input.

### Approval Gate Protocol

Every gate must:

1. Display a clear summary of what was produced in the gate format (see Output Format below)
2. Ask for explicit approval before proceeding
3. Accept one of four responses:
   - **"approved"** — proceed to the next phase or step
   - **"approved with changes: [notes]"** — apply the changes, re-run kaizen-check on the revised output, then proceed
   - **"hold"** — save full state to client memory, display resume instructions, end the session
   - **"skip"** — mark the step as skipped in memory with a reason note, proceed to the next step
4. Do NOT proceed past a gate without an explicit response. Silence is not approval.

### Human Gate Protocol

Human gates mark points where the user must do something outside of this system (run a discovery call, send a document, execute a cutover). At a human gate:

1. Display what the user needs to do
2. Display what to provide when they return (e.g., "paste your call notes")
3. Save state to memory
4. Wait. Do not generate anything further until the user returns with input.

### Session and Context Window Management

The orchestrator does NOT attempt to run all steps in a single context window. The rules:

- Run **3 to 5 skill invocations per batch** before summarizing and saving
- After each batch, summarize what was produced and confirm all outputs are saved to memory
- When a phase completes, tell the user to start a new conversation if context is getting long:

```
This phase is complete. To continue with the best context quality, start a new
conversation and say:

  "Resume the [Client Name] engagement at Phase [N+1]."

All durable progress is saved to KaizenOS; supplemental reasoning context is drafted to Kai memory.
```

- The orchestrator should monitor its own output length. If a single session has produced more than 5 major deliverables, recommend a fresh conversation regardless of phase boundaries.

### Tier-Aware Phase Selection

Not every engagement runs all five phases. The orchestrator selects the phase set based on the tier:

| Tier | Phases | Notes |
|---|---|---|
| Blueprint Only | Phase 1 only | Research, qualify, diagnose, deliver report. No build. |
| Silver | Phases 1 through 5 | Compressed timelines (4-7 weeks). Single POS track in Phase 3. |
| Gold | Phases 1 through 5 | Multi-location sequencing in Phases 3-4 (5-10 weeks). |
| Diamond | Phases 1 through 5 | Phased rollout with location groups. Train-the-trainer model. Timeline TBD. |
| AnyDB Only | Phases 1, 2, 3 (AnyDB track only), 5 | No POS migration steps. No Phase 4. |
| Mixed (POS + AnyDB) | Phases 1 through 5 | Both POS and AnyDB tracks run in Phase 3. |

When the tier is determined (usually at Step 1.4), confirm the phase plan with the user before proceeding.

### Phase-Summary Protocol (Gold+ and Diamond)

For Gold and Diamond engagements, write a brief phase summary to client memory after each major phase completes. This acts as a session log — preventing context loss when the engagement spans multiple conversations.

**Phase summary structure (log durable decisions/evidence in KaizenOS; draft supplemental reasoning
context to Kai memory, not chat):**
- **Decisions Made** — key architecture, data, or scope decisions confirmed this phase, with the evidence that drove each
- **Assumptions** — what was inferred vs. confirmed; note confidence level
- **Validate Before Next Phase** — questions for the client or items to confirm before proceeding

**Read all prior phase summaries** at the start of each new phase in a resumed engagement. These are not decorative — they are the inputs to every downstream decision.

**Cross-phase decision conflict rule:** If evidence surfaced in a later phase contradicts a decision made in an earlier phase, flag it explicitly before proceeding:
> "Phase 2 identified [new evidence]. This conflicts with the Phase 1 decision to [earlier decision]. Before proceeding, confirm: does [new evidence] change the approach, or does the earlier decision still stand?"

Never silently override an earlier decision with newer evidence — always surface the conflict.

---

# ============================================================
# MODE 1 — RUN ENGAGEMENT
# ============================================================

## Mode 1: Run Engagement

Full engagement pipeline. Requires: client name and enough context to begin (a website URL, referral notes, discovery call notes, or even just a company name).

### Initialization

1. Check if a client memory profile already exists for this client
   - If yes: load it, display current state, ask if this is a continuation or fresh start
   - If no: proceed to Phase 1, Step 1.1
2. Confirm the engagement scope: "Starting a new engagement for [Client Name]. I'll begin with research and discovery. Ready?"
3. If a tier is already known (e.g., "run a Gold engagement for Terrain & Co"), note the tier but still run Phase 1 to validate it

### Phase 1: Sales

**Duration:** ~1 session, approximately 45 minutes
**Produces:** Research brief, discovery question set, structured call summary, tier recommendation, Blueprint report or proposal, validated deliverable

```
PHASE 1 — SALES
================
Steps:
  1.1  Research (kaizen-research)
  1.2  Save research (kaizen-memory CREATE)
  1.3  Discovery prep (kaizen-qualify PRE-CALL)
       ── HUMAN GATE: Run the discovery call ──
  1.4  Discovery debrief (kaizen-qualify POST-CALL)
  1.5  Save findings (kaizen-memory UPDATE)
  1.6  Deliverable (kaizen-diagnose OR kaizen-propose)
  1.7  Validate (kaizen-check)
  1.8  Render if needed (kaizen-render)
       ── APPROVAL GATE: Review and send deliverable ──
  1.9  Save completion (kaizen-memory UPDATE)
```

**Step 1.1 — Research**
Skill: kaizen-research
Input: Client name, website URL, any context provided
Output: Full merchant research brief (industry, locations, tech stack, inferred pain points, competitive landscape)

**Step 1.2 — Save Research**
Skill: kaizen-memory (CREATE mode)
Input: Research brief from Step 1.1
Output: Client profile initialized with research findings
Fields populated: Identity, Current Stack, Pain Points (inferred), Source

**Step 1.3 — Discovery Prep**
Skill: kaizen-qualify (PRE-CALL mode)
Input: Client memory profile from Step 1.2
Output: Customized discovery question set tailored to the research findings, structured around the Doctor Diagnosis Method

```
╔══════════════════════════════════════════╗
║  HUMAN GATE — Discovery Call            ║
╠══════════════════════════════════════════╣
║                                         ║
║  Run the discovery call using the       ║
║  question set above.                    ║
║                                         ║
║  When done, paste your call notes here. ║
║  Raw notes are fine — I'll structure    ║
║  them.                                  ║
║                                         ║
╚══════════════════════════════════════════╝
```

**Step 1.4 — Discovery Debrief**
Skill: kaizen-qualify (POST-CALL mode)
Input: User's call notes + client memory profile
Output: Structured discovery summary, qualification score, tier recommendation, identified pain points (verbatim), scope signals

At this point, the orchestrator determines the engagement path:
- If the client accepted a Blueprint: next step is kaizen-diagnose (Blueprint report)
- If the client is ready for a direct proposal (e.g., Shopify referral, clear scope): next step is kaizen-propose
- If disqualified: save to memory, note the disqualification reason, end the engagement

Confirm the path with the user: "Discovery suggests [tier]. The client [accepted Blueprint / is ready for proposal / does not qualify]. Proceeding with [kaizen-diagnose / kaizen-propose]. Correct?"

**Step 1.5 — Save Findings**
Skill: kaizen-memory (UPDATE mode)
Input: Discovery debrief from Step 1.4
Output: Profile updated with: Pain Points (verbatim), Deal Context (tier recommendation, competitors, budget signals, timeline), Technical Context (SKUs, customers, gift cards, integrations), Identity (decision maker confirmed)

**Step 1.6 — Deliverable**
Skill: kaizen-diagnose (if Blueprint path) OR kaizen-propose (if direct proposal path)
Input: Full client memory profile
Output: Blueprint report OR proposal document

**Step 1.7 — Validate**
Skill: kaizen-check (Full Review mode)
Input: Deliverable from Step 1.6 + client memory for cross-reference
Output: Validation report (PASS / PASS WITH WARNINGS / FAIL)

If FAIL: fix the issues identified, re-run kaizen-check. Do not present the approval gate until the deliverable passes.
If PASS WITH WARNINGS: present the warnings to the user alongside the approval gate.

**Step 1.8 — Render (conditional)**
Skill: kaizen-render
Condition: Only if the user wants a styled PDF or Google Doc
Input: Validated deliverable from Step 1.7
Output: Styled document in KaizenCommerce design system

```
╔══════════════════════════════════════════╗
║  APPROVAL GATE — Phase 1 Complete       ║
╠══════════════════════════════════════════╣
║  Deliverables produced:                 ║
║    - Merchant research brief            ║
║    - Discovery call summary             ║
║    - [Blueprint report / Proposal]      ║
║    - Validation: [PASS status]          ║
║                                         ║
║  Action required:                       ║
║    Review the [report/proposal] and     ║
║    send to [client contact name].       ║
║                                         ║
║  Options:                               ║
║    - "approved" — proceed to Phase 2    ║
║    - "approved with changes: [notes]"   ║
║    - "hold" — save and pause            ║
║    - "skip" — skip to Phase 2           ║
╚══════════════════════════════════════════╝
```

**Step 1.9 — Save Completion**
Skill: kaizen-memory (UPDATE mode)
Input: Phase 1 completion status, deliverable type, validation result, gate decision
Output: Profile updated with engagement history row and stage progression

If Blueprint Only tier: engagement ends here. Run the Phase 1 completion summary and mark engagement as complete.

---

### Phase 2: Kickoff

**Duration:** ~1 session, approximately 30 minutes
**Produces:** Proposal (if Blueprint was Phase 1), SOW + deposit invoice, kickoff package, hardware plan
**Prerequisite:** Phase 1 complete (or skipped with user confirmation)

```
PHASE 2 — KICKOFF
==================
Steps:
  2.1  Recall context (kaizen-memory RECALL)
  2.2  Proposal if needed (kaizen-propose)
  2.3  SOW + invoice (kaizen-invoice-exec)
  2.4  Validate SOW (kaizen-check)
       ── APPROVAL GATE: Send SOW for signature ──
  2.5  Activation gate + canonical project plan (KaizenOS)
  2.6  Kickoff package (kaizen-onboard)
  2.7  Hardware plan (kaizen-hardware)
  2.8  Save canonical status + memory narrative
```

**Step 2.1 — Recall Context**
Skill: kaizen-memory (RECALL mode)
Input: Client name
Output: Full client profile displayed. Verify: tier confirmed, deliverable from Phase 1 sent, client responded.

**Step 2.2 — Proposal (conditional)**
Skill: kaizen-propose
Condition: Only if Phase 1 produced a Blueprint report (not a proposal). If a proposal was already delivered in Phase 1, skip this step.
Input: Client memory profile + Blueprint findings
Output: Full proposal document

If this step runs, also run kaizen-check on the proposal before proceeding.

**Step 2.3 — SOW + Deposit Invoice**
Skill: kaizen-invoice-exec
Input: Proposal details from client memory (tier, scope, pricing, timeline, client contacts)
Output: Statement of Work + deposit invoice

**Step 2.4 — Validate SOW**
Skill: kaizen-check (Scope Check + Number Check modes)
Input: SOW from Step 2.3 + proposal from client memory
Output: Validation report confirming SOW matches proposal terms exactly

```
╔══════════════════════════════════════════╗
║  APPROVAL GATE — SOW Ready              ║
╠══════════════════════════════════════════╣
║  Deliverables produced:                 ║
║    - SOW (scope, terms, timeline)       ║
║    - Deposit invoice                    ║
║    - Validation: [PASS status]          ║
║                                         ║
║  Action required:                       ║
║    Send SOW to [client contact] for     ║
║    signature. Confirm when signed.      ║
║                                         ║
║  Options:                               ║
║    - "signed" / "approved" — proceed    ║
║    - "approved with changes: [notes]"   ║
║    - "hold" — save and pause            ║
║    - "skip" — proceed without SOW       ║
╚══════════════════════════════════════════╝
```

**Step 2.5 — Activation Gate + Canonical Project Plan**

Read the KaizenOS deal and any linked project. Verify accepted SOW, approved scope source, first
implementation payment, merchant/contact links, owners, and target window. If any condition is
missing, keep the gate `NOT READY` and create/preview the corresponding task or client request.

If accepted commercial provenance exists and no project exists, use `kai_activate_deal_engagement`
because it preserves the source deal and accepted quote while atomically persisting the linked
project, milestones, tasks, deposit draft, and remaining phase billing. Preview and pin the exact
quote revision, acceptance, commercial fingerprint, and schedule IDs before approval. For a direct
or manual project, use the individual named tools and preserve the audited direct-project exception
and finance baseline rules. Re-read the project, billing, and phase records after setup and do not
duplicate an existing plan.

**Step 2.6 — Kickoff Package**
Skill: kaizen-onboard
Input: KaizenOS record context + accepted scope + supplemental client memory
Output: Sales-to-delivery handover, short activation intake, kickoff agenda, secure access
requests, project timeline, first-seven-days plan, and communication plan

**Step 2.7 — Hardware Plan**
Skill: kaizen-hardware
Input: Client memory profile (tier, locations, network details if known)
Output: Hardware specification, procurement list, network assessment (if data available), device configuration plan

Note: If the engagement is AnyDB Only, skip this step.

**Step 2.8 — Save Status**

Write confirmed project dates, phase, milestones, tasks, blockers, client requests, activities,
and linked artifacts to KaizenOS through the approval-gated write contract. Draft a Kai memory
update only for judgment narrative or operator preferences not represented by the canonical
records.

---

### Phase 3: Build

**Duration:** 1-2 sessions, approximately 60 minutes
**Produces:** Architecture spec, store configuration, Flow automations, data prep, import files, and (if in scope) AnyDB build
**Prerequisite:** Phase 2 complete, SOW signed

The Build phase has two tracks that may run in parallel depending on scope:

```
PHASE 3 — BUILD
================

POS TRACK (if POS migration in scope):
  3.1   Recall context (kaizen-memory RECALL)
  3.2   Architecture spec (kaizen-architect)
  3.3   Store configuration (kaizen-shopify-config)
  3.4   Flow design (kaizen-flow)
  3.5   Flow build specs (kaizen-flow-build)
  3.6   Data audit + migration-ready mapping (kaizen-dataprep)
  3.7   Migration execution package (kaizen-api-migration-exec by default;
        kaizen-matrixify-exec only when Matrixify lane is selected)
        ── APPROVAL GATE: Run lane-specific validation ──
  3.8   Save progress (kaizen-memory UPDATE)

ANYDB TRACK (if AnyDB in scope):
  3.9   Schema + seed config (kaizen-anydb-build)
  3.10  Load seed data (kaizen-anydb-dataload)
  3.11  Verify build (kaizen-anydb-audit)
```

**Step 3.1 — Recall Context**
Skill: kaizen-memory (RECALL mode)
Input: Client name
Output: Full profile. Verify: SOW signed, tier confirmed, hardware plan initiated (if applicable).

**Step 3.2 — Architecture Spec**
Skill: kaizen-architect
Input: Client memory (technical context, integrations, pain points, AnyDB scope if applicable)
Output: Architecture specification. For POS: integration mapping, data flow design. For AnyDB: schema design, object relationships, automation routing. For Mixed: both.

Run kaizen-check (Pipeline Check) to verify the spec contains everything downstream skills need.

**Step 3.3 — Store Configuration**
Skill: kaizen-shopify-config
Input: Architecture spec + client memory (locations, staff, channels)
Output: Shopify store configuration plan (locations, staff permissions, Smart Grid layout, channel publishing, tax settings)

**Step 3.4 — Flow Design**
Skill: kaizen-flow
Input: Architecture spec (automations routed to Shopify Flow) + client memory
Output: Flow automation designs (trigger, condition, action logic for each workflow)

**Step 3.5 — Flow Build Specs**
Skill: kaizen-flow-build
Input: Flow designs from Step 3.4
Output: Buildable Flow specifications with exact triggers, conditions, actions, and test procedures

**Step 3.6 — Data Audit + Field Mapping**
Skill: kaizen-dataprep
Input: Client's legacy data exports (user provides files or describes data) + client memory (current stack, SKU counts, customer counts)
Output: Data audit report, field mapping document, cleanup recommendations, migration-ready mappings for the selected lane

**Step 3.7 — Migration Execution Package**
Skill: kaizen-api-migration-exec by default. Use kaizen-matrixify-exec only when the approved lane is Matrixify.
Input: Field mappings from Step 3.6 + cleaned data
Output: API payloads, scripts, manifests, retry queues, validation extracts, or Matrixify CSV files when that lane is selected

```
╔══════════════════════════════════════════╗
║  APPROVAL GATE — Migration Package Ready║
╠══════════════════════════════════════════╣
║  Deliverables produced:                 ║
║    - Architecture spec                  ║
║    - Store configuration plan           ║
║    - Flow automation specs ([N] flows)  ║
║    - Data audit + field mappings        ║
║    - Migration package ([lane + entities])║
║                                         ║
║  Action required:                       ║
║    Run the lane-specific validation:    ║
║    API sandbox/dry-run, Matrixify Dry   ║
║    Run, or Admin CSV sample import.     ║
║    Report back with results.            ║
║                                         ║
║  Options:                               ║
║    - "clean" / "approved" — proceed     ║
║    - "errors: [paste results]" — I'll   ║
║      triage with kaizen-validate        ║
║    - "hold" — save and pause            ║
╚══════════════════════════════════════════╝
```

If the user reports validation errors, invoke kaizen-validate to triage, then kaizen-dataprep to fix, then regenerate the migration package with the selected execution skill. Loop until the lane-specific validation is clean.

**Step 3.8 — Save Progress**
Skill: kaizen-memory (UPDATE mode)
Input: All Phase 3 POS track outputs
Output: Profile updated with architecture decisions, data quality notes, entity counts, import status

**Steps 3.9 through 3.11 — AnyDB Track** (only if AnyDB is in scope)

**Step 3.9 — AnyDB Schema + Seed Config**
Skill: kaizen-anydb-build
Input: Architecture spec (AnyDB section) from Step 3.2
Output: Schema configuration, seed data templates, formula definitions, automation rules

**Step 3.10 — Load Seed Data**
Skill: kaizen-anydb-dataload
Input: Schema config from Step 3.9 + seed data (user provides or system generates sample data)
Output: Loaded AnyDB system with seed data populated

**Step 3.11 — Verify Build**
Skill: kaizen-anydb-audit
Input: Architecture spec + loaded AnyDB system
Output: Audit report comparing the build against the spec (record counts, field population, relationship integrity, automation test results)

If the audit finds issues, fix and re-audit before proceeding. Do not move to Phase 4 with a failing AnyDB audit.

Save AnyDB progress to client memory after each step.

---

### Phase 4: Go-Live

**Duration:** ~1 session, approximately 45 minutes
**Produces:** Migration runbook, test suite, training plan, validated import, reconciliation report
**Prerequisite:** Phase 3 complete, lane-specific validation clean, AnyDB audit passed (if applicable)

```
PHASE 4 — GO-LIVE
==================
Steps:
  4.1  Recall context (kaizen-memory RECALL)
  4.2  Migration runbook (kaizen-migrate)
  4.3  Test suite (kaizen-test-exec)
  4.4  Training plan (kaizen-training)
       ── HUMAN GATE: Execute training + cutover ──
  4.5  Triage results (kaizen-validate)
  4.6  Reconciliation (kaizen-reconcile)
       ── APPROVAL GATE: Confirm go-live ──
  4.7  Save completion (kaizen-memory UPDATE)
```

**Step 4.1 — Recall Context**
Skill: kaizen-memory (RECALL mode)
Input: Client name
Output: Full profile. Verify: lane-specific validation clean, AnyDB audit passed (if applicable), hardware procured, data volumes confirmed.

**Step 4.2 — Migration Runbook**
Skill: kaizen-migrate
Input: Client memory (data volumes, entity counts, field mappings, timeline, locations)
Output: Final migration runbook with real data volumes, cutover sequence, rollback plan, go-live checklist

**Step 4.3 — Test Suite**
Skill: kaizen-test-exec
Input: Migration runbook + client memory (locations, hardware, data volumes)
Output: Full test suite: API sandbox/dry-run or Matrixify Dry Run validation, transaction tests, hardware validation, cutover simulation scripts

**Step 4.4 — Training Plan**
Skill: kaizen-training
Input: Client memory (locations, staff count, roles, tier, go-live date, system configuration)
Output: Staff training plan, quick reference guides, role-specific materials

For Gold/Diamond: multi-location training schedule. For Diamond: train-the-trainer model.

```
╔══════════════════════════════════════════╗
║  HUMAN GATE — Training + Cutover        ║
╠══════════════════════════════════════════╣
║                                         ║
║  Execute the following:                 ║
║    1. Run staff training per the plan   ║
║    2. Execute cutover per the runbook   ║
║    3. Run the live import               ║
║                                         ║
║  When done, provide:                    ║
║    - Training completion confirmation   ║
║    - Import results (API job, Matrixify, or CSV output)║
║    - Any issues encountered             ║
║                                         ║
╚══════════════════════════════════════════╝
```

**Step 4.5 — Triage Results**
Skill: kaizen-validate
Input: Import results provided by the user
Output: Triage report. If errors: categorize, prioritize, provide fix instructions. If clean: confirm and proceed.

**Step 4.6 — Reconciliation**
Skill: kaizen-reconcile
Input: Legacy data counts + Shopify import counts from client memory and import results
Output: Reconciliation report comparing expected vs. actual entity counts, flagging discrepancies

```
╔══════════════════════════════════════════╗
║  APPROVAL GATE — Go-Live Confirmed?     ║
╠══════════════════════════════════════════╣
║  Deliverables produced:                 ║
║    - Migration runbook                  ║
║    - Test suite                         ║
║    - Staff training plan + guides       ║
║    - Import validation: [status]        ║
║    - Reconciliation: [status]           ║
║                                         ║
║  Action required:                       ║
║    Confirm the merchant is live and     ║
║    reconciliation is clean.             ║
║                                         ║
║  Options:                               ║
║    - "confirmed" — proceed to Phase 5   ║
║    - "issues: [details]" — I'll help    ║
║      triage and resolve                 ║
║    - "hold" — save and pause            ║
╚══════════════════════════════════════════╝
```

**Step 4.7 — Save Completion**
Skill: kaizen-memory (UPDATE mode)
Input: Go-live date, entity counts, reconciliation results, training completion, any open issues
Output: Profile updated with go-live milestone, Outcomes section populated

---

### Phase 5: Post-Delivery

**Duration:** ~1 session, approximately 30 minutes
**Produces:** Health check report, retainer pitch, content calendar, engagement P&L
**Prerequisite:** Phase 4 complete, merchant is live
**Timing:** Run 2-4 weeks after go-live to allow baseline data to accumulate

```
PHASE 5 — POST-DELIVERY
========================
Steps:
  5.1  Recall history (kaizen-memory RECALL)
  5.2  Health check (kaizen-report-exec)
  5.3  Retainer + testimonial (kaizen-email-exec)
  5.4  Content calendar (kaizen-content-calendar)
  5.5  Engagement P&L (kaizen-finance)
  5.6  Save final outcomes (kaizen-memory UPDATE)
       ── ENGAGEMENT COMPLETE ──
```

**Step 5.1 — Recall Full History**
Skill: kaizen-memory (RECALL mode)
Input: Client name
Output: Complete engagement history from first research through go-live

**Step 5.2 — Health Check**
Skill: kaizen-report-exec
Input: Full client memory (engagement history, go-live date, entity counts, baseline metrics if available)
Output: 30-day health check report with real operational data (or projections if data is pending)

If this is 2+ weeks post-go-live and the AnyDB upsell trigger applies (operational gap identified during implementation), flag it for inclusion in the retainer pitch.

**Step 5.3 — Retainer + Testimonial**
Skill: kaizen-email-exec
Input: Health check findings, engagement outcomes, client contact from memory
Output: Two emails: (1) retainer pitch email with specific value prop based on engagement outcomes, (2) testimonial request email

**Step 5.4 — Content Calendar**
Skill: kaizen-content-calendar
Input: Engagement outcomes, pain points solved, before/after metrics from memory
Output: Content repurposing plan (case study outline, LinkedIn posts, marketing angles derived from this engagement)

**Step 5.5 — Engagement P&L**
Skill: kaizen-finance
Input: Deal context from memory (tier, quoted price), estimated hours, any scope changes
Output: Engagement profitability analysis (gross margin, effective hourly rate, lessons for pricing)

**Step 5.6 — Save Final Outcomes**
Skill: kaizen-memory (UPDATE mode)
Input: All Phase 5 outputs
Output: Profile finalized with: retainer status, testimonial status, case study status, financial outcomes, engagement marked complete

```
╔══════════════════════════════════════════╗
║  ENGAGEMENT COMPLETE                    ║
╠══════════════════════════════════════════╣
║                                         ║
║  Client:  [name]                        ║
║  Tier:    [tier]                        ║
║  Duration: [start date] to [end date]   ║
║                                         ║
║  Deliverables produced: [count]         ║
║  Gates passed: [count]                  ║
║  Engagement value: $[amount]            ║
║  Go-live: [date]                        ║
║                                         ║
║  Open items:                            ║
║    - Retainer: [pitched/pending/active] ║
║    - Testimonial: [requested/pending]   ║
║    - Case study: [drafted/pending]      ║
║    - AnyDB upsell: [identified/pitched] ║
║                                         ║
║  Canonical engagement saved to KaizenOS.║
╚══════════════════════════════════════════╝
```

---

# ============================================================
# MODE 2 — RESUME
# ============================================================

## Mode 2: Resume

Pick up an engagement where it left off. KaizenOS owns the live position; Kai memory supplements
the reasoning history.

### Step 1 — Load State

Resolve the client in KaizenOS and read the current deal/project context. Then recall Kai memory.
Identify:
- canonical project status and current phase
- persisted milestones and next milestone
- completed, in-progress, blocked, and waiting-on-client tasks
- open client approvals/file requests
- recent activities, linked evidence, invoices, and client updates
- memory-only reasoning context that does not conflict with the live record

### Step 2 — Confirm Position

Display:

```
RESUMING ENGAGEMENT
━━━━━━━━━━━━━━━━━━━
Client:     [name]
Tier:       [tier]
Position:   Phase [X], Step [X.Y]
Last action: [date] — [what was done]
Next step:  [description]

Completed steps:
  [checkmark] Step 1.1 — Research brief
  [checkmark] Step 1.2 — Client profile created
  [checkmark] Step 1.3 — Discovery prep
  ...
  [circle] Step [X.Y] — [next step description] (pending)

Ready to continue?
```

### Step 3 — Proceed

On confirmation, execute the next step using the standard Step Execution Protocol. Prior live
state comes from KaizenOS; memory provides supplemental narrative. Do not re-run completed work or
reseed existing tasks/milestones.

If the user says "actually, let me re-do step [X.Y]" — re-run that specific step with fresh output, update memory, then continue the sequence.

---

# ============================================================
# MODE 3 — SKIP TO PHASE
# ============================================================

## Mode 3: Skip to Phase

Jump to a specific phase, bypassing earlier phases. Used when work was done outside the orchestrator (e.g., "we already have a signed SOW, skip to Phase 3").

### Step 1 — Validate the Jump

Check client memory. If a profile exists, verify what has been captured. If no profile exists, create one with whatever context the user provides.

Display what the skipped phases would normally produce and ask the user to confirm or provide the equivalent information:

```
SKIP TO PHASE [N]
━━━━━━━━━━━━━━━━━
Client: [name]

Skipping Phases [1 through N-1]. These phases normally produce:
  - [list of key outputs from skipped phases]

To proceed, I need at minimum:
  - [list of critical context the target phase requires]

Please provide what you have, or confirm these items are not needed.
```

### Step 2 — Backfill Memory

Take whatever the user provides and create or update the client memory profile. Flag gaps that may cause issues downstream.

### Step 3 — Execute

Begin the target phase at Step [N].1, following the standard phase flow.

---

# ============================================================
# MODE 4 — STATUS
# ============================================================

## Mode 4: Status

Show current engagement progress. Read-only. Does not execute any skills.

### Step 1 — Load Profile

Invoke kaizen-memory (RECALL mode) for the client.

### Step 2 — Display Progress

```
ENGAGEMENT: [Client Name] — [Tier]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Started:  [date]
Current:  Phase [X], Step [X.Y]

Phase 1: Sales           [status] — [date if complete]
Phase 2: Kickoff         [status] — [date if complete]
Phase 3: Build           [status] — Step [X.Y] of [total]
Phase 4: Go-Live         [status]
Phase 5: Post-Delivery   [status]

Deliverables produced:
  [checkmark] [deliverable 1]
  [checkmark] [deliverable 2]
  ...
  [circle] [next deliverable] (pending)

Gates passed: [N] of [total for tier]
Next action: [specific description of what happens next]

Blockers or holds:
  [any items flagged as hold or blocked, or "None"]
```

Phase statuses: COMPLETE, IN PROGRESS, PENDING, SKIPPED, NOT APPLICABLE (for tier-excluded phases)

---

# ============================================================
# MODE 5 — PHASE ONLY
# ============================================================

## Mode 5: Phase Only

Run a single phase in isolation. Useful for engagements managed partially outside the orchestrator.

### Step 1 — Context Check

Load client memory if it exists. If not, ask for the minimum context the target phase requires (refer to the "Required in handoff" table from kaizen-check Pipeline Check mode).

### Step 2 — Execute Phase

Run the specified phase from Step [N].1 through completion, following all standard protocols (step execution, gates, memory saves). At the end, save all outputs to memory but do not automatically advance to the next phase.

### Step 3 — Wrap Up

```
PHASE [N] COMPLETE
━━━━━━━━━━━━━━━━━━
Client: [name]
Phase:  [N] — [Phase Name]

Deliverables produced:
  [list all outputs from this phase]

Durable outputs saved to KaizenOS; supplemental narrative drafted to Kai memory.

To continue to Phase [N+1], say:
  "Run Phase [N+1] for [Client Name]"
  or
  "Resume the [Client Name] engagement"
```

---

## Output Format

### Step Header

At the start of each step:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE [X] — [Phase Name] | Step [X.Y]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Client:  [name]
Tier:    [tier]
Skill:   kaizen-[skill name]
Purpose: [one-line description of what this step produces]

```

### Step Footer

At the end of each step:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step [X.Y] complete. Saved to client memory.
Next: [description of what happens next]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Approval Gate Format

```
╔══════════════════════════════════════════╗
║  APPROVAL GATE — [Gate Name]            ║
╠══════════════════════════════════════════╣
║  Deliverables produced:                 ║
║    - [item 1]                           ║
║    - [item 2]                           ║
║                                         ║
║  Action required:                       ║
║    [what the human needs to do]         ║
║                                         ║
║  Options:                               ║
║    - "approved" — proceed to [next]     ║
║    - "approved with changes: [notes]"   ║
║    - "hold" — save and pause            ║
║    - "skip" — skip to [next]            ║
╚══════════════════════════════════════════╝
```

### Human Gate Format

```
╔══════════════════════════════════════════╗
║  HUMAN GATE — [Gate Name]               ║
╠══════════════════════════════════════════╣
║                                         ║
║  [What the user needs to do]            ║
║                                         ║
║  When done, provide:                    ║
║    [what to paste or confirm]           ║
║                                         ║
╚══════════════════════════════════════════╝
```

---

## Error Handling

### Skill Produces Low-Quality Output

If a skill output is incomplete, contradictory, or below KaizenCommerce standards:

1. Do NOT proceed to the next step
2. State specifically what is wrong: "Step 3.6 produced a data audit, but the field mapping is incomplete. [X] fields from the legacy export are unmapped."
3. Ask the user: "Provide the missing information, or should I mark these fields as excluded and proceed?"
4. Only continue when the issue is resolved or explicitly deferred

### Missing Client Context

If a step requires context that is not in client memory and was not provided:

1. State what is missing: "Step 2.3 needs the tier and pricing to generate the SOW, but the tier has not been confirmed."
2. Check if the information can be inferred from existing context
3. If not: ask the user to provide it before proceeding

### Validation Failures (Phase 3 Loop)

When the selected validation gate returns errors:

1. Invoke kaizen-validate to triage the errors
2. Invoke kaizen-dataprep to fix the source data issues
3. Regenerate the migration package with kaizen-api-migration-exec or kaizen-matrixify-exec, depending on the approved lane
4. Return to the approval gate: "Migration package regenerated. Run validation again."
5. Repeat until clean. Maximum 3 loops before escalating: "Three validation attempts returned errors. Review the data manually before proceeding."

### Mid-Engagement Scope Change

If at any point the user indicates a scope change (new locations, additional data, feature additions):

1. Pause the current phase
2. Invoke kaizen-scope to document the change order
3. Run kaizen-check (Number Check) to verify the change order against the original SOW
4. Present the change order for approval
5. Update client memory with the new scope
6. Resume the engagement with the updated scope

---

## Orchestrator State Schema

The orchestrator tracks engagement state through client memory. These fields are maintained in the Engagement History and Deal Context sections of the client profile:

```
## Orchestrator State (in client memory)
- Current phase: [1-5]
- Current step: [X.Y]
- Steps completed: [list of step IDs]
- Steps skipped: [list of step IDs with reasons]
- Gates passed: [list of gate names with dates]
- Gates pending: [next gate]
- Holds: [any active holds with reasons]
- Deliverables produced: [list with dates]
- Dry Run attempts: [count, for Phase 3 loop tracking]
- Session count: [number of sessions used]
- Last session date: [date]
```

This state is derived from KaizenOS after every step. Resume mode uses it as the canonical position;
Kai memory may add reasoning context but cannot override it.

---

<critical_rules priority="must-follow">
- NEVER skip kaizen-check before any client-facing deliverable. The check must pass before the deliverable reaches an approval gate.
- NEVER proceed past an approval gate without explicit user input. Silence is not approval. If the user changes the topic, remind them there is a pending gate.
- ALWAYS persist durable engagement changes to KaizenOS through the approval-gated write contract
  and re-read the affected record. Draft a memory delta only when supplemental judgment context changed.
- ALWAYS recall Kai memory after loading KaizenOS at the start of every session and phase.
- ALWAYS resolve KaizenOS live context before memory. KaizenOS is the persistence layer for
  project status, phases, milestones, tasks, requests, evidence, invoices, updates, and priorities;
  memory is supplemental narrative only.
- NEVER create a rival project state in Kai memory or the local task ledger. If state conflicts,
  current KaizenOS wins and the stale narrative is corrected.
- NEVER start implementation delivery or kickoff until the accepted SOW, approved scope source,
  and first payment are confirmed. A project in `Scoping` does not clear the activation gate.
- NEVER modify individual skill files. The orchestrator reads and invokes skills. It does not change them.
- NEVER reference kaizen-brain.md as a file. Say "Apply your foundational KaizenCommerce knowledge" when foundational context is needed.
- Individual skills continue to work standalone. The orchestrator is optional. Do not alter skill behavior to depend on the orchestrator.
- If a skill produces low-quality output, PAUSE and ask. Do not proceed with degraded output in the hope that a later step will fix it.
- All pricing in USD. State currency explicitly.
- Context window management: recommend a new conversation after completing a full phase or after 5 major skill outputs, whichever comes first.
- The phase structure must match the tier. Do not run POS migration steps for an AnyDB-only engagement. Do not skip Phase 4 for a POS engagement.
- Do not run Phase 5 immediately after Phase 4. Recommend waiting 2-4 weeks for baseline data to accumulate: "Phase 4 is complete. Run Phase 5 in 2-4 weeks after go-live data has accumulated. To resume then, say: 'Resume the [Client] engagement at Phase 5.'"
</critical_rules>

<preferences priority="should-follow">
- When a phase begins, display the full step list for that phase so the user can see the plan before execution starts.
- At each step, keep the skill output focused. The orchestrator adds structure around the skill, not length.
- Use the step header and footer formats consistently. They create scannable session logs.
- When the user provides messy input (rough call notes, unstructured data), clean it through the appropriate skill rather than asking for structured input. The skills are built to handle messy input.
- If the engagement is straightforward and the user is experienced, compress the ceremony. Skip verbose confirmations when the user has already said "run the full pipeline."
- In Status mode, highlight the most important item: what happens next. The full list is context. The next action is the signal.
- When recommending a new session, provide the exact resume command so the user can copy-paste it.
</preferences>

---

<verification>
Before completing any orchestrator action, check:

1. **Step sequence check:** Is this the correct next step for the phase and tier? No steps skipped without explicit user approval?
2. **Persistence check:** Was durable state saved to KaizenOS and re-read? Can Resume mode find the
   canonical phase, milestones, tasks, requests, and blockers?
3. **Gate check:** Was the last approval gate resolved before proceeding? No gate was auto-approved?
4. **Validation check:** Was every client-facing deliverable validated by kaizen-check before reaching a gate?
5. **Tier alignment check:** Does the phase structure match the engagement tier? No POS steps in AnyDB-only. No AnyDB build steps when AnyDB has been explicitly ruled out. For DTC/B2B commerce systems, confirm the AnyDB operating-layer decision before excluding it.
6. **Context freshness check:** Was KaizenOS record context loaded first and memory recalled
   second? Were conflicts resolved in favor of the live record?
7. **Quality check:** Did every skill produce output at the expected quality level? No degraded output pushed forward?
8. **Session length check:** Has this session exceeded 5 major skill outputs? If yes, recommend a new conversation.
9. **State completeness check:** Could another session resume from the current state? Is everything needed for Resume mode saved?
</verification>

---

## Pipeline Integration

```
kaizen-orchestrate (coordination layer)
  ├── READS: KaizenOS record context first; Kai memory narrative second
  ├── WRITES: KaizenOS durable state through approval-gated tools; memory deltas for judgment only
  ├── INVOKES: every pipeline skill in sequence per the phase plan
  ├── VALIDATES: every client-facing output through kaizen-check
  ├── RENDERS: styled outputs through kaizen-render (on request)
  └── ADAPTS: phase structure based on tier via Tier-Aware Phase Selection

Upstream:  User request ("run engagement", "resume", "status", "run phase N")
Downstream: Every skill in the system, invoked in the correct order

The orchestrator does not produce its own deliverables.
It produces coordination: the right skill, at the right time, with the right context,
validated before delivery, and saved for the next session.
```

---

## Phase Handoff Packages And Dual Sign-Off

For phase transitions, produce a compact handoff package before moving work forward.

### Blueprint -> Proposal Handoff

Required fields:

- Discovery findings: pain, complexity, stakeholder map, and six discovery answers.
- Technical assessment: POS data quality, integration points, AnyDB/Flow/API implications.
- Internal MEDDPICC score with evidence and missing fields.
- Tier recommendation with rationale.
- Risk summary with owner and mitigation.
- Explicit `GO`, `GO WITH NOTES`, `NO-GO`, or `HOLD` decision.

### Dual Sign-Off Gates

| Gate | Sign-off 1 | Sign-off 2 |
|---|---|---|
| Blueprint -> Proposal | the operator as account owner | Technical lead or Kai technical review |
| Proposal -> SOW | the operator | Merchant economic buyer |
| Kickoff -> Build | Kaizen PM | Merchant ops lead |
| Build -> Go-Live | Kaizen PM with FAIL list cleared | Technical lead with FAIL list cleared |
| Go-Live -> Hypercare exit | Kaizen PM | Merchant with KPIs verified |

Do not treat a phase as complete until the handoff package and required sign-offs are present or
explicitly deferred by the operator.
