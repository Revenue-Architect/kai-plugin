# Kaizen ↔ KaizenOS Integration Map

Load this file when a palette command or client workflow needs to read from or write to KaizenOS,
or when deciding which surface owns a piece of client state. Tool behavior and argument shapes are
governed by the vendored contract in `contracts/kaizenos-agent-tools.json` (repo root); CI fails
when a tool named here leaves that contract.

## The One Rule

**KaizenOS is the system of record; Kai is the judgment layer.** Any durable fact about a
merchant, contact, deal, project, task, invoice, or relationship must be readable from — or
written back to — KaizenOS via `kai_*` tools. Kai owns reasoning, drafting, diagnosis, and
architecture; it never becomes a second database. On conflict, current KaizenOS record state
wins; Kai memory narrative annotates, never overrides.

## Ownership Boundary

| Concern | Owner | Kai's interaction |
|---|---|---|
| Merchants, contacts, deals, stages | KaizenOS | `kai_search_context`, `kai_create_merchant`, `kai_create_contact`, `kai_create_deal`, `kai_update_deal`, `kai_move_deal_stage` |
| Quotes, SOWs, and commercial acceptance | KaizenOS | `kai_send_quote_for_acceptance`; read the accepted quote/acceptance before activation |
| Projects, tasks, dependencies, milestones, and billing activation | KaizenOS | `kai_activate_deal_engagement` for accepted commercial activation; `kai_create_project`, `kai_create_task`, and `kai_create_project_milestone` plus their named update tools for direct/manual or reviewed follow-up changes |
| Client approvals and file/access requests | KaizenOS | `kai_create_client_request`; never place credentials in a request, task, note, or activity |
| Discovery questionnaires and evidence | KaizenOS | `kai_send_intake_request`, `kai_get_intake_answers`; submitted answers are reviewed in the app and become an immutable Discovery Brief; never log or reconstruct the raw token |
| Activity and call notes | KaizenOS | `kai_log_activity` after every Post Call Update |
| Evidence and documents | KaizenOS (SharePoint/OneDrive links) | `kai_attach_source`, `kai_link_document` on every deliverable |
| Priorities / next best action | KaizenOS (`kai_get_priorities`) | Consume-only. Kai never maintains a rival priority queue. |
| Invoices and reminders | KaizenOS | `kai_invoice_status`; `kai_queue_invoice_reminder` (approval-gated) |
| Expenses and invoice rebilling | KaizenOS | `kai_create_expense`, `kai_update_expense`, `kai_bill_expenses_to_invoice`; finance-gated and approval-bound |
| Historical/direct margin baselines | KaizenOS | `kai_set_project_margin_baseline`; finance-only, evidence-backed, and never a substitute for quote/SOW acceptance |
| Microsoft 365 sync | KaizenOS (`kai_trigger_outlook_sync`) | Trigger and read; never scrape in parallel |
| Client updates (weekly, reviewed) | KaizenOS (cadence, approval, send path) | `kai_list_client_update_drafts` to find drafts; `kai_draft_client_update` for content only. Agents never set status, approve, or send. |
| Judgment narrative, operator preferences, cross-client patterns | Kai file memory (see `reference/kaizen-memory-architecture.md`) | Memory deltas, approval-gated |
| Pricing, voice, methodology | Kai canon | Unchanged; never mirrored into KaizenOS |

## Command → Tool Sequences

| Command | KaizenOS sequence |
|---|---|
| `Start My Day` / `Kai Priorities` / `Kai Status` | `kai_get_priorities` → enrich with Outlook Calendar/Email, Teams, SharePoint → render plan. Never recompute the ranking locally. |
| `New Deal: [Merchant]` | `kai_search_context` (dedupe) → `kai_create_merchant` if new → `kai_create_contact` if named → `kai_create_deal` (`dryRun=true` first on first-of-kind shapes) |
| `Sync Client` / `Prep Call` / `Resume Client` | `kai_search_context` → `kai_get_record_context` → memory recall → synthesis |
| `Post Call Update` | `kai_log_activity` → `kai_update_deal` / `kai_move_deal_stage` when stage changed → `kai_create_task` per follow-up → memory delta draft (approval-gated) |
| `Build Blueprint` / `Build Proposal` | record context read first → produce artifact → `kai_attach_source` or `kai_link_document` on the deal |
| `Start Delivery` / `Onboard Client` | `kai_search_context` → `kai_get_record_context` → verify accepted quote/SOW, approved scope source, first-payment evidence, merchant/contact, owners, and target window → if accepted commercial provenance exists, preview `kai_activate_deal_engagement` and pin the quote revision, acceptance, commercial fingerprint, and schedule IDs → commit only after approval → re-read project, phases, billing, and tasks |
| `Start Direct Project` | `kai_search_context` → resolve the direct project and deal relationship → verify the audited direct-project exception and finance baseline when the deal is being closed → use the existing manual/direct project path; never synthesize quote or SOW acceptance |
| `Send Discovery Questionnaire` | read merchant/deal first → preview `kai_send_intake_request` → commit only with a unique top-level idempotency key → treat `intakeUrl` as a one-time secret → use `kai_get_intake_answers` after submission and keep application of answers human-gated |
| `Migration Package` / `Migration QA` | record context read → verdict/runbook artifact → `kai_attach_source` on the project → `kai_update_task` for remediation items |
| Invoice follow-up | `kai_invoice_status` → `kai_queue_invoice_reminder` only with explicit approval |
| `End My Day` / `Weekly Review` | `kai_get_priorities` + task ledger → `kai_log_activity` for decisions worth the record → memory delta draft |
| `Close Client` | record context read → closeout artifact → `kai_attach_source` → `kai_update_project` / `kai_move_project_status` |
| `Log Win` | `kai_search_context` → `kai_get_record_context` (engagement actuals) → draft bank entries (approval-gated) → `kai_log_activity` noting the captured proof |
| Client update drafting | `kai_list_client_update_drafts` → `kai_get_record_context` for the project → draft in Kaizen voice (load `reference/kaizen-voice.md`) → `kai_draft_client_update` (content only; operator approves and sends in the app) |

## Write Discipline

- `dryRun=true` before the first write of a new shape or when validating scope/idempotency.
- Pass an `idempotencyKey` on retries and in any automated flow.
- Prefer named tools; use the generic `kai_agent_action` dispatch only when a named wrapper is
  unavailable in the connected surface.
- For `kai_activate_deal_engagement`, commit only the exact schedule and commercial pins returned by
  preview: `expectedQuoteId`, `expectedQuoteContentRevision`, `expectedAcceptanceId` when present,
  `expectedCommercialFingerprint`, and `expectedScheduleIds`.
- For `kai_send_intake_request`, `sendEmail=true` requires a valid recipient; `expiresAt` is part of
  the request contract; the raw secret is returned once and must stay out of logs, summaries, and
  general activity metadata.
- Writes are approval-gated the same way memory writes are: draft the change, show it, apply on
  approval. Never auto-send reminders or client-visible requests.
- Every client deliverable ends with `kai_attach_source` or `kai_link_document` so the KaizenOS
  evidence trail stays complete.
- Project setup is idempotent. Read existing milestones, tasks, and requests before creating
  anything; never seed a second delivery plan because a local handoff or memory file looks empty.
- After a delivery write, re-read the project and report the canonical phase, next milestone,
  blockers, waiting-on-client requests, and next action.

## Roadmap Tie-Ins (consume when the app ships them)

- **Client updates:** shipped. Use `kai_list_client_update_drafts` / `kai_draft_client_update`
  per the sequences above; there is deliberately no agent approve/send action.
- **Deal Desk quotes/SOW:** `skills/kaizen-propose.md` stays the reasoning engine and should emit
  the structured quote payload the app's builder expects, then attach the SOW via
  `kai_link_document`.
- **Project plans:** shipped. Accepted commercial activation now persists the linked project,
  milestones, tasks, deposit draft, and remaining phase billing atomically through
  `kai_activate_deal_engagement`. Kai may add or revise a template-managed plan through the
  individual tools only with approval and after checking for an existing plan.
- **Discovery intake and Brief:** shipped. Public intake drafts and evidence attachments remain
  server-side/private; the submitted Discovery Brief is immutable and is the evidence source for
  Review Queue application. It is distinct from the short client activation intake.
- **Canonical billing:** the app owns accepted payment schedules and canonical `QA` / `Launch`
  triggers. Never recreate a standard schedule from percentages or use the retired `Launch QA` name.
