# Migration Execution Variant — API-First Lane

Load when the lane decision selects `api_to_api` (the KaizenCommerce default) and the runbook
moves to execution configuration. This variant owns the execution mechanics; the lane DECISION
stays in `skills/kaizen-migrate.md`.

## Execution Architecture

- **Per-entity pipelines**, run in dependency order: metafield definitions → products →
  publication → customers → inventory (R4 after products+locations) → gift cards → historical
  orders LAST (R5 is the least reversible).
- **Idempotency keys:** every source record carries `migration.source_id` (metafield/tag/note
  attribute). Re-runs upsert or skip — never blind-create. Recipes R1/R7 are upsert-native;
  R3/R5/R6 are not — those pipelines check-before-create against the ledger.
- **Batching:** bulk lane (R2: staged JSONL + bulkOperationRunMutation) for volume entities; one
  bulk op runs at a time per shop — serialize, poll, archive every JSONL + result file as the
  audit ledger. Small/risky entities (gift cards) run as throttled individual calls with
  per-record logging instead.
- **Throttling/retry:** respect cost-based rate limits with exponential backoff; a retry queue
  file per pipeline (failed row + error + attempt count); three failures → human review, never
  infinite retry. Recipe-specific caps (R5 dev-store 5/min; R1 variant daily cap past 50K) go in
  the runbook timeline math.
- **Environments:** full dry run on a development store first — same scripts, same data, R8
  reconciliation must pass there before the production run is scheduled.

## Required Inputs
Custom app with exactly the scopes the recipe set needs (least privilege; offline token for R5) ·
export files frozen + hashed in Phase 1 · entity dependency map · cutover freeze window.

## Validation Protocol
After each pipeline: R8 counts vs Phase-1 baseline for that entity, spot-check sample, and the
entity's financial tie-out where applicable (R6 to the cent). No pipeline starts while the
previous entity's reconciliation is red.

## Rollback Notes
The JSONL/result archives ARE the created-resource ledger. Rollback is per-entity, newest-first
(orders → gift cards deactivate → inventory snapshot restore → customers → products). Rollback
scripts are written and dry-run-tested BEFORE the production run, not improvised during an
incident.

## Variant Depth Additions
This lane's deliverables: pipeline scripts (Antigravity/scripts may draft; Kai owns review),
retry-queue convention, ledger archive layout, and the dependency-ordered run schedule with
recipe rate caps applied.

## Anti-Selection Rules
Source APIs unavailable/locked (no export API, plan-gated) → Matrixify or CSV lane wins, don't
force API symmetry. One-shot tiny imports (<500 simple records) → `shopify_admin_csv` is honest.

## Known Failure Modes
Blind-create reruns after partial failure (duplicates); orders imported before customers
(identity stitching lost); bulk ops run in parallel (they queue/fail); dry-run skipped "because
the data is clean".

## Default Evidence Gates
Dry-run R8 reconciliation green on dev store · scopes audit (no over-provisioned app) · recipe
recheck dates valid (`reference/kaizen-api-recipe-bank.md` bank status) · rollback scripts
tested · dual sign-off before production run.

## Operating Hooks
Vendor freshness: any recipe past its recheck date re-validates via Shopify Dev MCP before
execution. Flywheel: pipeline incidents and their fixes feed this variant at Close Client.

## Output Shape By Mode
Runbook Phase 3-5 expansion: per-pipeline config blocks (entity, recipe, batch size, throttle,
retry policy, ledger path, reconciliation query) + the run schedule. Execution scripts delivered
as artifacts, never inlined in client documents.

## Source-Of-Truth
Lane decision: `skills/kaizen-migrate.md` · recipes + classes + recheck:
`reference/kaizen-api-recipe-bank.md` · MCP rules: `reference/kaizen-mcp-protocols.md` ·
QA verdicts: `delivery-os/templates/migration-qa-evidence-pack.md`
