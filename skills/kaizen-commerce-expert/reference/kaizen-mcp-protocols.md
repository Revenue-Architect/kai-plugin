# Kaizen MCP Protocols

Load this file when a task depends on live KaizenOS records, live documentation, current technical
behavior, or MCP source-of-truth boundaries.

## Vendor Freshness Layer

Use `reference/kaizen-vendor-freshness-protocol.md` with this file when a task depends on current
Shopify, AnyDB, Matrixify, or integration behavior. The generated `reference-content/` index helps
Kai notice recent changelog and release items, but it does not replace canonical source
validation.

Freshness rule:
- Use the local vendor index for navigation and recent-change awareness.
- Use Shopify Dev MCP, AnyDB docs/MCP, Matrixify docs, or canonical public URLs for final truth.
- If a relevant generated item is marked `[NEEDS-MERGE]`, do not treat the affected
  recommendation as final until the source is reviewed live.

## Shopify Dev MCP Protocol

Use Shopify Dev MCP as the source of truth whenever generating, validating, or explaining current
Shopify technical behavior:

- Admin GraphQL queries or mutations
- Bulk operations, staged uploads, `orderCreate`, inventory, products, customers, locations,
  metafields, metaobjects, gift cards, API scopes, or version-sensitive Admin API behavior
- Shopify CLI workflows or store execution commands
- POS UI, Liquid, Hydrogen, Functions, Polaris, or Shopify component/theme code

Required workflow:
1. Call `learn_shopify_api` for the correct Shopify API surface.
2. Use `search_docs_chunks` for docs-backed behavior.
3. Use `validate_graphql_codeblocks` for any generated Shopify GraphQL.
4. Use Shopify theme/component validators when generating theme, POS UI, Polaris, Hydrogen, or
   extension code.
5. Do not guess schema fields, mutation inputs, scopes, or current platform constraints from memory.

Keep Exa MCP as the default for broader KaizenCommerce web research. Use Shopify Dev MCP for
Shopify developer/API truth.

## KaizenOS MCP Protocol

KaizenOS MCP is the default source of truth for KaizenCommerce CRM, project-management, priorities,
relationship context, and agent-safe record writes. Per-command tool sequences and the
record-ownership boundary live in `reference/kaizen-kaizenos-integration-map.md`. It has officially replaced the legacy AnyDB
Kaizen OS CRM/project-management database.

Use KaizenOS MCP first for:

- active deals, merchants, contacts, projects, tasks, invoices, evidence sources, and activity
- `Kai Priorities`, `Kai Status`, `Start My Day`, `End My Day`, `Weekly Review`, and `Resume Client`
- pipeline review, deal scoring, call prep, post-call updates, account-health reads, and handoffs
- relationship intelligence such as merchant warm paths, contact cadence, referral source, and
  relationship-risk signals

Preferred read workflow:

1. `kai_get_priorities` for ranked work, notification/digest queue, and relationship signals.
2. `kai_search_context` to resolve a merchant, contact, deal, project, task, invoice, or evidence
   source by name.
3. `kai_get_record_context` (or `kai_agent_action` with action `get_record_context` when the named
   wrapper is unavailable) for the bounded record context pack before synthesis.
4. Enrich only after the KaizenOS record read: Outlook Email, Calendar, Teams, SharePoint,
   filesystem memory, and Exa can challenge or add evidence, but they do not outrank current
   KaizenOS record state.

Preferred write workflow:

- Use named tools such as `kai_create_deal`, `kai_update_deal`, `kai_create_project`,
  `kai_update_project`, `kai_create_task`, `kai_update_task`,
  `kai_create_project_milestone`, `kai_update_project_milestone`,
  `kai_delete_project_milestone`, `kai_log_activity`, `kai_attach_source`, and
  `kai_create_client_request`.
- Use `dryRun=true` before write actions when validating shape, scope, or idempotency.
- Provide an `idempotencyKey` for retries or workflow automation.
- Do not write raw database rows when a named KaizenOS tool exists.
- Do not write finance actions unless the task explicitly requires finance and the available key
  has finance scope.

### Canonical Commercial Activation

For an accepted quote/SOW engagement, use `kai_activate_deal_engagement` as the canonical
Deal → Project activation path. It previews and atomically commits the linked project, persisted
milestones and tasks, deposit draft, and remaining phase billing. A committed call must echo the
previewed `expectedQuoteId`, `expectedQuoteContentRevision`, `expectedAcceptanceId` when present,
`expectedCommercialFingerprint`, and `expectedScheduleIds`; if any commercial pin changes, stop and
preview again. Do not imitate this flow with separate project, milestone, task, or billing writes.

Individual project and plan tools remain valid for direct/manual projects and reviewed post-activation
changes. A direct project exception is finance-audited evidence, not quote or SOW acceptance.

### Discovery Intake and Immutable Evidence

Use `kai_send_intake_request` for the private Discovery Questionnaire. It accepts a required
`merchantId`, optional `dealId`, frozen modules, `sentToEmail`, `expiresAt`, and `sendEmail`; email
requires a valid recipient. Committed calls require a top-level `idempotencyKey`, return the raw
secret only once, and must never place the token or URL in logs, summaries, or general activity
metadata. Use `kai_get_intake_answers` to read submitted answers. Drafts, progress, attachments,
and the immutable Discovery Brief are handled by the app; applying answers remains a human Review
Queue action. Do not confuse this workflow with the shorter post-SOW activation intake.

### Finance, Margin, and Invoice Boundaries

- Use `kai_set_project_margin_baseline` only for finance-reviewed historical or direct-project
  exceptions. Evidence documents and a mandatory reason are required; accepted quote baselines are
  immutable, and the action never creates acceptance, SOW acceptance, invoices, billing schedules,
  or project phases.
- Use `kai_invoice_status` for invoice facts, `kai_create_expense` / `kai_update_expense` for
  finance-gated expenses, and `kai_bill_expenses_to_invoice` for reviewed rebilling. Use
  `kai_queue_invoice_reminder` only through the approval-gated workflow.
- The app owns canonical billing terms and phase triggers. Treat `QA` and `Launch` as the canonical
  phase values and inherit the accepted schedule rather than hardcoding 50/25/25.

### Rendered KaizenOS Views

The connected plugin may expose UI-only render tools that are not part of the vendored agent action
contract. When those tools are available, use the exact named renderer for the requested view and do
not claim a view opened from a prose response alone. They are a presentation surface, not a substitute
for the read/write contract above.

Do not use AnyDB docs/search MCP, legacy AnyDB database IDs, or local AnyDB exports as current CRM
or project-management truth. Use them only for AnyDB platform behavior, AnyDB client workflow
systems, or explicit legacy-data/audit work.

## Exa MCP Protocol

Use Exa MCP for KaizenCommerce web research that is not Shopify developer/API truth:

- merchant research
- platform comparisons
- public tech stack checks
- partner/app research
- competitive research
- current web evidence for client-facing strategy

When Exa output is used for a client-facing or strategic recommendation, preserve source URLs,
dates when visible, exact merchant names, and evidence boundaries. Do not convert weak public
signals into confirmed facts.

## AnyDB MCP Protocol

Use AnyDB docs or MCP access when generating or validating current AnyDB behavior:

- AnyDB Type or Cell design
- formula syntax
- Attach vs Reference decisions
- rollups, references, formulas, and validation constraints
- data-load or audit behavior that depends on AnyDB semantics

Separate the AnyDB tool surfaces from KaizenOS:

- `mcp__anydb_com.*` and `mcp__kaizen_anydb_docs.*` are docs/search surfaces only. Do not treat
  them as Kaizen OS record access.
- Database record access requires tools such as `list_teams`, `list_databases_for_team`,
  `list_records`, `get_record`, `search_records`, `create_record`, and `update_record`, or the
  local `anydb_agent` wrapper when `ANYDB_DEFAULT_API_KEY` and `ANYDB_DEFAULT_USER_EMAIL` are
  available.

Legacy AnyDB Kaizen OS IDs (archive/reference only, not current CRM/project-management truth):

- team ID: `69a206b4a3eaf1244c2a1831`
- database ID: `6a04b2e1bf8f55f1cb0b73ea`
- default URL: `https://app.anydb.com/69a206b4a3eaf1244c2a1831/6a04b2e1bf8f55f1cb0b73ea`

If record-level database tools are unavailable, load `reference/kaizen-anydb-patterns.md` and
clearly separate confirmed local guidance from anything that would need live AnyDB validation. For
CRM or project-management lookups, use KaizenOS MCP instead.

## Matrixify MCP Protocol

Matrixify remains a supported migration lane, not the default migration answer.

Use Matrixify docs or MCP access when:

- the operator explicitly asks for Matrixify
- an existing client project is already Matrixify-scoped
- Kai selected `matrixify_csv` as the lower-risk lane for a specific entity
- a Dry Run result, Matrixify error, or Matrixify column behavior needs interpretation

Do not use Matrixify docs to justify generic migration strategy when the selected lane is
`api_to_api`, `shopify_admin_csv`, or `hybrid` without a Matrixify component.

## MCP Server Fallback

Some skills reference MCP servers for live documentation lookup (e.g., `anydb-com` for AnyDB docs, `matrixify-app` for Matrixify docs). If an MCP server is unavailable or not connected, use the relevant skill file as the primary reference and web search as a fallback. Never tell the user you cannot answer because an MCP server is missing.
