# Kai Evidence And Gates

Use this reference when a Kai output affects delivery readiness, QA, migration, validation,
commercial decisions, client handoff, or post-go-live reporting.

## Verdicts

| Verdict | Meaning | Use when |
|---|---|---|
| `PASS` | Evidence supports proceeding. | Required checks are complete and no blocking issue remains. |
| `PASS WITH NOTES` | Proceed, but with named watch items. | Non-blocking risks exist and have owners or follow-up timing. |
| `FAIL` | Do not proceed. | A blocking requirement, source check, or acceptance criterion failed. |
| `NOT READY` | Evidence is incomplete. | The work may be sound, but proof is missing or unverified. |

Default critical delivery verdict is `NOT READY` until the evidence clears the relevant gate.
Do not convert `NOT READY` to `PASS` based on confidence or attestation alone.

## Evidence Gate Hook

Kai should load this protocol automatically when a workflow needs proof, readiness, sign-off, or
client-visible claims. This includes migration QA, reconciliation, go-live decisions, automation
approval, proposal proof, QBR claims, case study claims, ROI, savings, and post-go-live outcomes.

Hook behavior:

- Start at `NOT READY` until the required files, sources, commands, counts, logs, assumptions, and
  fail gates are accounted for.
- Use `PASS`, `PASS WITH NOTES`, `FAIL`, or `NOT READY` exactly for internal verdicts.
- Apply automatic fail gates before polishing the answer.
- For large work, preserve a file-based handoff under the run folder instead of relying on a
  message-only summary.

The hook is allowed to block final output. It is not allowed to relax a gate because the answer
sounds plausible.

## Evidence Manifest

Use this structure when an output needs review or sign-off:

```markdown
## Evidence Manifest

**Verdict:** PASS / PASS WITH NOTES / FAIL / NOT READY
**Files read:** [paths]
**Sources checked:** [URLs, MCP docs, transcripts, exports, memory entries]
**Commands run:** [commands and status]
**Counts checked:** [source count, target count, discrepancy]
**Screenshots or logs reviewed:** [paths or N/A]
**Assumptions:** [items still unconfirmed]
**Automatic fail gates checked:** [yes/no + notes]
**Unresolved risks:** [risk, owner, next action]
**Next action:** [proceed / fix / re-run / hold / escalate]
```

## Automatic Fail Pattern

Any single automatic fail condition blocks sign-off. Examples:

- Required source-of-truth documentation was not checked.
- Expected and actual counts do not reconcile.
- A Shopify, Matrixify, AnyDB, Flow, or integration behavior is version-sensitive and unverified.
- A created resource lacks an `ABORT_CLEANUP` method.
- A critical error row, failed API job, rejected record, broken formula, or missing required field remains open.
- A client-facing commercial output has unapproved pricing, hidden assumptions, or missing exclusions.
- A training, hardware, or cutover plan lacks owner, timing, and go/no-go criteria.
- A handoff omits required downstream fields.

## File-Based Handoffs

For substantial work, prefer file-backed evidence under a run folder:

```text
runs/[date]-[client]-[task]/
  kai/
    REVIEW.md
    evidence/
    context-delta.md
  agents/
    [agent-name]/
      findings.md
      evidence.jsonl
      files_read.txt
```

Message-only summaries are acceptable for small tasks. Large QA, migration, research, and audit
work should preserve files, commands, counts, and source references.

## Retry And Recovery

- Retry only after the blocker is named and assigned.
- Do not re-run a full workflow when a targeted failed gate can be retested.
- After three failed attempts on the same gate, escalate or decompose the work.
- If rollback is required, use the resource ledger from the producing skill before making new changes.

## Voice Rule

Internal verdicts can be blunt. Client-facing deliverables should translate verdicts into plain,
specific language without exposing internal labels unless labels are useful for clarity.
