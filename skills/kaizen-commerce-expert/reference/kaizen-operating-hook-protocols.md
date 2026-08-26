# Kai Operating Hook Protocols

Use this reference for safe automatic checks Kai should run before or after common KaizenCommerce
work. These are soft hooks: they load context, check gates, and draft proposals. They do not send
messages, approve work, mutate authoritative memory, mark tasks done, or make client-visible
claims without review.

## Hook Model

Kai may automate four safe actions:

- auto-load the relevant protocol
- auto-check the relevant source, gate, ledger, or run folder
- auto-draft a proposed update, task, verdict, or account-health note
- auto-block final output with `NOT READY`, `DEFER`, or a plain-language caveat when required
  evidence is missing

Kai must not automate these actions without explicit approval:

- authoritative memory writes
- accepted task creation from inferred follow-ups
- task completion
- proposal/SOW pricing approval
- go-live approval
- vendor-current technical claims when the source has not been checked
- client-facing expansion, QBR, case study, or ROI claims without evidence

## 1. Vendor Freshness Auto-Gate

Trigger this hook when the work mentions or depends on:

- Shopify Admin GraphQL, API versions, mutations, scopes, bulk operations, staged uploads, POS UI,
  Shopify Flow, Shopify Functions, Liquid, Hydrogen, Polaris, Markets, taxes, payments, B2B,
  checkout, customer accounts, or Shopify plan/rollout behavior
- AnyDB formulas, cell types, references, rollups, workflows, imports, permissions, releases,
  roadmap claims, or Shopify sync behavior
- Matrixify columns, supported entities, dry runs, import limits, error handling, or export shape
- integration automation where vendor behavior affects safety

Required behavior:

1. Load `reference/kaizen-vendor-freshness-protocol.md`.
2. Check the local `reference-content/` index for relevant recent changes or `[NEEDS-MERGE]`
   items.
3. If the claim is version-sensitive, plan-sensitive, rollout-sensitive, API-schema-sensitive, or
   build-ready, validate against Shopify Dev MCP, AnyDB docs/MCP, Matrixify docs, or canonical
   vendor URLs before finalizing.
4. If live validation is not possible in the current run, mark the point as `needs live
   verification` or `NOT READY` rather than presenting it as current truth.

Output requirement when freshness materially changes the answer:

```text
Freshness hook:
- Local index checked: yes/no
- Live source checked: source or none
- Verdict: current / current with caveat / needs live verification / NOT READY
- Impact: one sentence
```

## 3. Evidence Gate Hook

Trigger this hook when the work includes:

- migration QA, reconciliation, go-live readiness, import/export review, or rollback decisions
- delivery validation, audits, automation readiness, Shopify Flow or AnyDB build sign-off
- proposal proof, case study claims, QBR/account-health claims, ROI, savings, or performance claims
- any client-visible recommendation that depends on source-backed proof

Required behavior:

1. Load `reference/kaizen-evidence-and-gates.md`.
2. Start from `NOT READY` until files, sources, counts, commands, screenshots/logs, assumptions,
   and fail gates are accounted for.
3. Use `PASS`, `PASS WITH NOTES`, `FAIL`, or `NOT READY` exactly for internal verdicts.
4. Apply automatic fail gates before polish. A single blocking fail gate prevents `PASS`.
5. Preserve file-based handoffs under the run folder when the work is substantial.

Output requirement when a verdict is needed:

```markdown
## Evidence Manifest

**Verdict:** PASS / PASS WITH NOTES / FAIL / NOT READY
**Files read:** ...
**Sources checked:** ...
**Commands run:** ...
**Automatic fail gates checked:** ...
**Next action:** ...
```

## 5. Task / Follow-Up Hook

Trigger this hook when the work includes:

- call notes, transcripts, meeting prep, post-call updates, follow-up drafts, or next steps
- commitments, blockers, owners, due dates, waiting-on items, or promised client/partner actions
- `Start My Day`, `End My Day`, `Weekly Review`, `Kai Status`, `Kai Priorities`, `Review
  Workspace`, `Close Client`, or natural-language equivalents

Required behavior:

1. Extract proposed follow-ups as structured tasks with owner, due date, source, client, priority,
   and confidence when available.
2. Mark inferred tasks as proposals. Do not create accepted task ledger entries unless the user
   explicitly asks for the task or a command script intentionally creates command-run tasks.
3. When a run folder exists, write proposals to `kai/proposed_tasks.json`.
4. In chat, show a compact Proposed Tasks section and ask for approval when inferred tasks should
   enter the ledger.
5. Do not mark tasks complete unless the intended handoff, send, validation, or approval actually
   happened.

Proposed task file shape:

```json
{
  "approval_status": "PROPOSED_NOT_APPROVED",
  "source": "Post Call Update",
  "client": "Merchant Name",
  "tasks": [
    {
      "title": "Send follow-up email",
      "owner": "the operator",
      "due": "TBD",
      "priority": "P3",
      "source_reference": "call notes or run file",
      "confidence": "medium",
      "userAccepted": false
    }
  ]
}
```

## 7. Account Health / Expansion Hook

Trigger this hook when the work includes:

- post-go-live reporting, QBRs, account health, retainers, support, expansion, upsell, churn risk,
  renewals, referrals, testimonials, case studies, or client closeout
- signs of poor adoption, unresolved support issues, stalled stakeholders, missing outcomes,
  invoice friction, or declining responsiveness

Required behavior:

1. Classify health as Green, Yellow, or Red using the account-health guidance in
   `skills/kaizen-report.md`, `skills/kaizen-report-exec.md`, and `skills/kaizen-finance.md`.
2. Expansion requires all four parts: signal, context, timing, and stakeholder alignment.
3. Yellow accounts require stabilization before expansion. Red accounts use save/stabilize logic,
   not upsell logic.
4. QBRs must include outcomes, open risks, next operating improvements, and source-backed evidence.
5. Case study, testimonial, ROI, or expansion claims must pass the Evidence Gate Hook.

Output requirement when health or expansion is relevant:

```text
Account health hook:
- Health: Green / Yellow / Red / Unknown
- Evidence: source-backed signals
- Expansion readiness: ready / stabilize first / not appropriate
- Next action: one operational next step
```

## Combined Hook Order

When multiple hooks apply, run them in this order:

1. Memory Hook Protocol for known-client recall.
2. Vendor Freshness Auto-Gate for platform-current claims.
3. Evidence Gate Hook for proof, readiness, and verdicts.
4. Task / Follow-Up Hook for inferred actions and commitments.
5. Account Health / Expansion Hook for post-go-live, QBR, and closeout work.

Do not let one hook hide another. For example, a QBR may need memory recall, source freshness,
evidence gates, proposed follow-up tasks, and account-health classification in the same output.
