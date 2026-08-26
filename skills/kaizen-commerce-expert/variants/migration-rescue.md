# Migration Rescue Variant

Use this variant when a migration is failing, blocked, over scope, returning import errors, or
producing reconciliation mismatches.

## Required Context

- Source platform and destination Shopify store state
- What already ran: export, clean, dry run, live import, cutover, validation
- Import tool and job IDs if available
- Error files, failed rows, rejected fields, or reconciliation report
- Expected vs actual counts
- Cutover status and whether stores are live
- Client-facing commitments already made

## Default Skill Chain

1. `skills/kaizen-validate.md` for Dry Run or import error triage
2. `skills/kaizen-reconcile.md` for expected-vs-actual mismatch
3. `skills/kaizen-dataprep.md` for data repair
4. `skills/kaizen-migrate.md` for revised runbook or rollback path
5. `skills/kaizen-scope.md` if data volume, timeline, or effort exceeds scope
6. `skills/kaizen-check.md` before any client-facing update

## Output Shape

- Current status: blocked, degraded, recoverable, or production-risk
- Root-cause hypothesis
- Evidence needed to confirm
- Immediate containment
- Fix path with owner and sequence
- Scope or change-order implication
- Client communication stance
- Kill conditions: when to pause imports, roll back, or re-scope

## Common Risks

- Continuing live imports before the failed pattern is isolated
- Treating every failed row as independent instead of finding field-level root cause
- Hiding scope growth when source data quality is worse than expected
- Sending client updates before counts and impacts are reconciled
- Fixing files without preserving an audit trail

## When Not To Use

- The task is a normal pre-migration field map. Use `skills/kaizen-dataprep.md`.
- The task is to generate final import files. Use `skills/kaizen-matrixify-exec.md`.
- The issue is only a client communication draft. Use `skills/kaizen-followup.md` with rescue facts.

## Variant Depth Additions

### Anti-Selection Rules

- Do not keep importing until the failure pattern is isolated.
- Do not send a reassuring client update before counts, failed rows, and production impact are
  understood.
- Do not fix files without preserving original exports, transformed files, logs, and retry sets.

### Known Failure Modes

- Row-level errors treated as unrelated when a mapping rule is wrong.
- Failed records repaired but not re-reconciled.
- Scope growth hidden inside "cleanup."
- Rollback plan exists in prose but lacks created-resource ledger.

### Default Evidence Gates

- Failed-row sample and root-cause hypothesis.
- Expected vs actual counts.
- Import logs, retry files, transformed files, and source exports preserved.
- Go/no-go or pause decision with owner.

### Operating Hooks

- Evidence Gate Hook for every rescue verdict.
- Vendor Freshness Auto-Gate for Shopify API, Matrixify, and AnyDB behavior.
- Task / Follow-Up Hook for remediation owners, client asks, and retest actions.

### Output Shape By Mode

- Quick Read: current status, immediate stop/continue call, next evidence needed.
- Operator Analysis: root cause, containment, fix path, scope implication, client stance.
- Client Deliverable: plain-language status, impact, next action, and ownership.
- Execution Artifact: repair plan, retry package, reconciliation checklist, cleanup ledger.

### Source-Of-Truth And AnyDB Boundary

Do not let rescue work change system ownership silently. Shopify remains target commerce truth
after successful import. Legacy remains reference truth until reconciliation passes. AnyDB is used
only for approved workflow state, exception tracking, or remediation coordination.
