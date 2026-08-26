# KaizenCommerce Client Journey

Load this reference when starting delivery, onboarding a signed client, resuming an engagement,
planning the first seven days, moving a project phase, or closing a project.

## Operating Principle

Productize the journey, not the merchant. Every engagement follows the same control system:
activation conditions, a source-backed handover, a visible first week, persisted milestones,
acceptance gates, reviewed client updates, controlled launch, and evidence-backed closeout.
Scope, architecture, data, and rollout depth remain client-specific.

## System Boundary

- **KaizenOS owns live state:** deal, accepted quote/SOW evidence, first-payment evidence, project,
  phase, milestones, tasks, dependencies, client requests, activities, documents, approvals,
  updates, invoices, and priorities.
- **Kai owns judgment and artifacts:** handover synthesis, onboarding package, access-request
  wording, kickoff agenda, workflow map, risk interpretation, readiness verdicts, client-update
  drafting, and closeout synthesis.
- **Kai memory is narrative only.** It may preserve operator preferences and reasoning context,
  but it never becomes a rival project tracker. On conflict, current KaizenOS state wins.

Do not create a second project board or onboarding database in Notion, ClickUp, Asana, a local
task ledger, or a form tool. A form or communication tool may collect information, but its status
and canonical links must return to KaizenOS.

## Canonical Journey

| Stage | KaizenOS state | Kai responsibility | Exit gate |
|---|---|---|---|
| 0. Discovery / scope | Deal + source artifact | Qualify, diagnose, select advisory or implementation lane | Scope source named and approved |
| 1. Contracting | Proposal/SOW evidence + invoice | Validate scope, terms, acceptance criteria, and payment schedule | SOW accepted; first payment confirmed for implementation |
| 2. Sales-to-delivery handover | Source deal linked to project | Build the internal handover brief from KaizenOS; do not re-key known facts | Owners, outcomes, exclusions, assumptions, risks, dates, and open access are explicit |
| 3. Activation / first seven days | Project + Project Initiation tasks + client requests | Welcome, intake, kickoff, recap, workflow confirmation, visible progress | Kickoff complete; blockers assigned; first real progress shown |
| 4. Architecture / build | Phase milestones + tasks + decisions | Produce architecture and build artifacts; protect scope | Approved design and acceptance evidence |
| 5. Migration / readiness tracks | Data Migration, Build, Training tasks | Run migration, hardware, permissions, and training as named parallel tracks | Dry Run/reconciliation and readiness checks pass |
| 6. QA / UAT | QA tasks + client approvals | Internal QA first, then merchant UAT with representative operators | Named launch authority signs off; no blocking failure remains |
| 7. Launch / hypercare | Launch and Hypercare milestones + issue tasks | Controlled cutover, daily risk review when warranted, client updates | Stabilization criteria pass; operating owner accepts handoff |
| 8. Closeout / compounding | Closeout milestone + evidence links | Handoff package, retro, proof capture, retainer/clean-close decision | Open work assigned; evidence and reusable lessons captured |

KaizenOS macro phases remain:
`Discovery → Architecture → Build → Data Migration → QA → Training → Launch → Hypercare → Closeout`.
The Kaizen cutover method (`Shadow → Pilot Store → Verdict Gate → Waves → Hypercare`) is a
launch runbook inside those phases, not a competing project-phase taxonomy.

## Activation Conditions

An implementation project may be created in `Scoping` so the record and invoice can exist, but
delivery work and kickoff do not start until all applicable activation conditions are confirmed:

- accepted SOW is linked
- scope source is approved
- first implementation payment is confirmed
- merchant and primary contact are linked
- KaizenCommerce project owner and merchant decision owner are named
- kickoff date and target window are recorded
- material exclusions, assumptions, client responsibilities, and launch constraints are visible

If one is missing, create or update the corresponding KaizenOS task/request and keep the gate
`NOT READY`. Do not work around the gap in Kai memory.

## Sales-To-Delivery Handover

Use `delivery-os/templates/sales-to-delivery-handover.md`. Populate it from the source deal,
accepted quote/SOW, source artifact, notes, documents, and invoice state in KaizenOS.

The handover is a derived brief, not another form the salesperson must complete. Only ask for a
fact when it is absent from the source records. Link the completed brief to the project.

## Days 0–7 Contract

### Day 0

- send a personal welcome and a short "what happens in the next seven days" note
- create or confirm the KaizenOS project in `Scoping`
- seed the Project Initiation task pack and persisted milestones
- send the compact activation intake and secure access requests
- confirm the agreed communication channel and canonical document workspace

### Days 1–2

- read the accepted SOW, scope source, deal notes, and handover brief
- prepare the kickoff around known risks and missing decisions
- resolve access through collaborator invitations, vendor grants, or an approved secret manager
- never collect passwords, API tokens, or credentials in a form, chat, task, or KaizenOS note

### Days 2–3

- run kickoff
- confirm outcomes, success measures, owners, milestone dates, communication cadence,
  escalation path, and recovery expectations
- test access while the responsible client owner is present when practical
- send the written recap and workflow map within one business day
- turn every open item into a KaizenOS task, approval, or client request with owner and due date

### By Day 3 After Kickoff

Show real progress: a scoped configuration walkthrough, data finding, workflow map, prototype,
or other project artifact. A generic status message does not qualify.

### By Day 7

- publish the reviewed client update from KaizenOS: done, next, risks, decisions, waiting on client
- confirm the next milestone and acceptance evidence
- escalate unresolved access, ownership, or scope blockers instead of hiding them

Daily client check-ins are risk-based, not automatic. Use them during launch/hypercare or when a
named risk warrants the cadence. Normal active delivery uses the cadence agreed at kickoff plus
the weekly KaizenOS update.

## Client Intake Standard

Use `delivery-os/templates/client-activation-intake.md` as the default post-SOW activation intake.
It is short and asks only for missing activation facts. The separate KaizenOS Discovery Questionnaire
is the pre-activation discovery path: it supports durable server-side drafts, evidence attachments,
Review Queue review, and an immutable Discovery Brief. The long question bank in `kaizen-onboard`
is internal; select only questions not already answered by discovery, the Blueprint, or SOW.

Include one optional, low-pressure referral seed at the end of Day 0 intake. It is never required,
scored, chased, or used as an activation condition. Do not collect a third party's contact details
without consent; let the client offer an introduction or choose to revisit later. The deliberate
referral follow-up still belongs after value is visible—normally at health review, handoff,
testimonial, or QBR. Gifts and personal touches are optional relationship choices, not workflow
gates.

## KaizenOS Write Pattern

1. Resolve the deal/project with `kai_search_context` and `kai_get_record_context`.
2. If accepted commercial provenance exists and a project does not exist, use the app's canonical
   `kai_activate_deal_engagement` preview/commit path; it preserves the accepted quote and atomically
   seeds the linked project, delivery plan, deposit draft, and remaining phase billing without re-keying.
   Use individual project writes only for direct/manual projects or reviewed follow-up changes.
3. Preview any new agent write with `dryRun=true` and show the proposed fields.
4. After approval, commit the activation tool with its exact commercial pins, or use the named
   individual write for a direct/manual path, always with stable idempotency keys.
5. Draft client updates with `kai_draft_client_update`; approval and sending stay in KaizenOS.
6. Re-read the project, billing, and phase records after writes and report the canonical phase, next milestone, blockers,
   waiting-on-client items, and next action.

Never bulk-create a second copy of tasks or milestones. Read first and add only what is missing.

## Closeout And Compounding

Closeout requires:

- architecture and runbooks linked
- training recordings/materials linked
- permissions/ownership matrix linked
- known limitations and open issues assigned
- escalation and ongoing operating owner confirmed
- actual dates, reconciliation evidence, and acceptance evidence recorded
- internal retro completed
- reusable process improvement and proof-bank drafts prepared with provenance
- retainer, warranty, support, or clean-close path explicit

Only evidence-backed lessons enter Kai's reusable banks. Client-specific state stays in KaizenOS.
