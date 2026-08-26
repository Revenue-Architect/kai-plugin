# Migration Execution Variant — Matrixify Lane

Load when the lane decision selects `matrixify_csv` for some or all entities (the operator asked for
it, scope committed to it, or an entity is lower-risk through Matrixify). Execution mechanics
only — the lane DECISION stays in `skills/kaizen-migrate.md`.

## Hard Rule — column names are never guessed

Matrixify sheet/column names and import semantics come from the **matrixify-app MCP** at build
time, every time. Formats evolve; a column name remembered from a previous engagement is a
vendor-freshness violation. No MCP available → every column name in the mapping carries
`[VERIFY]` and the package is not execution-ready.

## Execution Architecture

- **Entity sheets in dependency order** (same order as the API lane): products → customers →
  inventory → gift cards `[VERIFY availability/plan gating via matrixify-app MCP]` → orders.
- **Import mode discipline:** explicit mode per sheet — new-only creation vs update vs upsert
  (`[VERIFY current mode names via MCP]`). Migrations default to upsert-by-handle/ID so re-runs
  repair instead of duplicate.
- **Dry Run first:** Matrixify's dry-run/validation pass on every sheet; the results file is a
  runbook artifact. No live import without a clean dry run + sign-off (migrate QA gate).
- **Batch sizing:** split exports into bounded files (per entity, per location where relevant) so
  a failed import has a small blast radius and a named retry file.
- **Results files are the ledger:** every import's results export (with created/updated IDs and
  errors) is archived — that is the rollback reference and the audit trail.

## Required Inputs
Matrixify subscription on the target store (temporary line item in the app stack per propose §5) ·
frozen source exports · the per-entity mapping doc with MCP-verified column names · dry-run
sign-off owner named.

## Validation Protocol
Per sheet: results-file error count zero (or triaged) → R8-style counts vs Phase-1 baseline →
spot-check sample → financial tie-outs (gift cards to the cent) before the next entity starts.

## Rollback Notes
Results files identify every created object → targeted reversal imports (Matrixify delete/update
sheets) or API cleanup. Gift cards deactivate-not-delete. Never roll back by re-importing the
original source file with delete semantics against a live store without entity-level review.

## Variant Depth Additions
This lane's deliverables: the mapping doc (source field → Matrixify column, MCP-verified), the
sheet inventory with import modes, dry-run results log, and the results-file archive layout.

## Anti-Selection Rules
Huge repeatable migrations with controllable APIs on both sides → API lane is structurally
safer (idempotency, retry queues). Entities with per-record risk needing per-record logging
(gift card liability at scale) → consider API lane for that entity even in a Matrixify project.

## Known Failure Modes
Guessed column names; "Create" mode re-runs after partial failure (duplicates); skipping dry run
on the "easy" entity; results files discarded (no ledger, no rollback); option-value drift
imported verbatim.

## Default Evidence Gates
Every column name MCP-verified or `[VERIFY]`-flagged · dry-run results archived per sheet ·
reconciliation green per entity before the next begins · dual sign-off before cutover.

## Operating Hooks
Vendor freshness: matrixify-app MCP check recorded in the runbook's Lane Decision block
(`Matrixify MCP check: complete`). Flywheel: Matrixify quirks captured here at Close Client.

## Output Shape By Mode
Runbook Phase 3-5 expansion: sheet inventory table (sheet, mode, source file, dry-run status,
results file path) + mapping doc as Supplement A.

## Source-Of-Truth
Lane decision: `skills/kaizen-migrate.md` · column truth: matrixify-app MCP per
`reference/kaizen-mcp-protocols.md` · execution stub: `skills/kaizen-matrixify-exec.md` ·
QA verdicts: `delivery-os/templates/migration-qa-evidence-pack.md`
