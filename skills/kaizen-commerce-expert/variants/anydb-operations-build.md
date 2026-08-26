# AnyDB Operations Build Variant

Use this variant when the merchant needs an operational system around Shopify for workflow state,
approvals, exception handling, vendor collaboration, purchasing, transfers, receiving, custom
reporting, or back-office orchestration.

## Required Context

- Workflow domain: purchasing, receiving, transfers, approvals, vendor portal, wholesale, reporting, exceptions
- Current source systems and what each system owns
- Users and roles
- Objects and records involved
- Shopify data needed in or out
- Automations, approvals, notifications, and reporting needs
- Whether this is Blueprint, architecture spec, or build execution

## Default Skill Chain

1. `skills/kaizen-architect.md` router + `skills/kaizen-architect.md` Mode 1 for AnyDB spec
2. `reference/kaizen-anydb-patterns.md` before any field, formula, Lookup, Reference, or Attach design
3. `reference/kaizen-build-vs-buy.md` for the NATIVE / THIRD-PARTY / CUSTOM / RETAIN verdict
4. `skills/kaizen-anydb-build.md` for actual build package
5. `skills/kaizen-anydb-audit.md` for QA against the spec
6. `skills/kaizen-check.md` when recommendation or client-facing scope needs validation

## Output Shape

- Operational problem AnyDB is solving
- Why Shopify native, Flow, or an app is insufficient
- Source-of-truth boundary
- Type/object model
- Workflow map
- Automations and approvals
- Reporting outcomes
- Build assumptions and kill conditions
- Next action

## Common Risks

- Building AnyDB as a passive copy of Shopify data
- Creating a second order, catalog, or inventory system without a clear ownership rule
- Writing formula or cell types from memory instead of `kaizen-anydb-patterns.md`
- Skipping portal, role, and maintenance ownership
- Failing to name what happens when Shopify and AnyDB disagree

## When Not To Use

- The approved scope is explicitly native Shopify, Shopify Flow, or app-only and has no AnyDB
  operating layer. Do not reject AnyDB merely because native Shopify, Shopify native B2B, Flow, or
  a standard app can perform part of a DTC/B2B workflow.
- The request is only AnyDB formula syntax. Load `reference/kaizen-anydb-patterns.md`.
- The user asks for build files from an approved spec. Use `skills/kaizen-anydb-build.md`.

## Variant Depth Additions

### Anti-Selection Rules

- Do not build AnyDB as a passive Shopify mirror.
- Do not give AnyDB write ownership over Shopify-owned commerce records without a conflict rule.
- Do not approve a build without owner, maintenance model, fallback, logging, and QA path.

### Known Failure Modes

- Object model matches current spreadsheets but not the actual workflow.
- Formula, Reference, Attach, or Lookup design is written from memory instead of current AnyDB docs.
- Portal users and internal operators see different states with no reconciliation.
- Automations trigger from ambiguous status values.

### Default Evidence Gates

- Source-of-truth matrix.
- Type/object model with owners.
- Status lifecycle and handoff ownership.
- Automation governance verdicts and rollback path.
- AnyDB formula/cell behavior validated against current docs/MCP.

### Operating Hooks

- Vendor Freshness Auto-Gate for AnyDB releases, formulas, cell types, workflows, imports, and
  Shopify sync.
- Evidence Gate Hook for build approval and QA.
- Task / Follow-Up Hook for owner, fallback, and unresolved workflow decisions.

### Output Shape By Mode

- Quick Read: whether AnyDB fits, why, and next input.
- Operator Analysis: workflow boundary, source of truth, risks, automation verdict.
- Client Deliverable: operating problem, AnyDB role, Shopify boundary, assumptions, next step.
- Execution Artifact: schema, formulas, automations, permissions, QA checklist, cleanup ledger.

### Source-Of-Truth And AnyDB Boundary

Shopify remains commerce execution and transaction truth unless explicitly displaced by an approved
system boundary. AnyDB owns workflow state, approvals, exceptions, coordination, and reporting when
those needs exceed Shopify native/app execution.
