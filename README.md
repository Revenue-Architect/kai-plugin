# Kaizen Commerce

`@Kaizen Commerce` is a Codex/ChatGPT plugin built from the verified Kaizen
Commerce runtime. It packages Kai's commerce expert router, companion Kaizen
skills, a Kaizen Knowledge MCP server, a bounded KaizenOS CRM/project
operations adapter, and the V3 Kaizen Workbench UI for Shopify POS, retail
operations, migrations, solution engineering, and delivery work.

## MCP boundary

The MCP layer combines packaged knowledge and deterministic analysis/draft
helpers with named KaizenOS tools. The KaizenOS adapter forwards only the
canonical CRM and project-management slice of the KaizenOS Agent MCP. It does
not expose Shopify, AnyDB, finance, Outlook sync, quote-send, or discovery-email
actions.

Live KaizenOS access requires a caller-authenticated OAuth-linked KaizenOS
account or a personal `kai_...` bearer key. Anonymous hosted requests can still
use the packaged advisory tools, but cannot read live records or commit writes.
OAuth identity is resolved to the signed-in KaizenOS profile: admin/member
profiles can use the bounded write scope, while viewer profiles remain
read-only. Committed writes require the canonical preview/approval/idempotency
sequence.

The plugin keeps Kai's existing source-of-truth rules, evidence separation,
scope protection, and two-lane commercial model. It is packaged from the
compiled Codex runtime so development-only maintenance material is not shipped.

## V3 interactive boundary

V3 uses a decoupled data/render pattern. The data and draft tools return
reusable `structuredContent`; `render_kaizen_workbench` attaches the versioned
MCP Apps resource `ui://kaizen-commerce/workbench-v3.html` only after the model
has a result worth reviewing. The widget can call the read-only data tools from
inside the mounted view, preserve a local snapshot, share view context with
Kai, and request a next evidence-gated step.

The Workbench includes Deal Snapshot, Architecture Map, Migration Risk, Scope
Builder, Blueprint, Proposal, and SOW views. It has no external domains, no
connector credentials, and no write or send actions of its own. Pricing,
client-ready documents, and third-party system changes remain outside this
release. Live KaizenOS records are accessed only through the named server tools.

## Recommended ChatGPT distribution

The full Kaizen Commerce canon is intentionally included in this package. The
portable core is the bundled skills; the MCP server and Workbench are an
optional hosted enhancement. This lets the same plugin work in ordinary
ChatGPT chats while still exposing structured analysis, search/fetch, and the
Workbench when the ChatGPT app connection is enabled.

Because this account does not have a ChatGPT Business workspace, coworker
sharing uses the public universal Plugin Directory rather than private
workspace publishing. That makes the package discoverable to anyone who finds
or searches for it. Do not add client records, credentials, secrets, or private
merchant documents to this distribution.

An approved public listing is the route for coworker use without a Business
workspace. The listing can be used from supported ChatGPT surfaces, but mobile
availability and write behavior are controlled by the current ChatGPT product
rollout and the app's approval status; do not treat the local Developer Mode
connection as proof of mobile support.

### Personal Developer Mode setup

For local testing, install dependencies and run the HTTP server:

```bash
npm install
npm test
HOST=127.0.0.1 PORT=8787 npm run start
```

Connect the endpoint through a Secure MCP Tunnel or another HTTPS tunnel while
developing. The URL supplied to ChatGPT must end in `/mcp`.

In ChatGPT, enable **Settings → Security and login → Developer mode**, open
the Plugins page, select **+**, and add the HTTPS MCP endpoint. Refresh the
connection after tool or UI metadata changes, then start a new chat.

If ChatGPT gives the connection a technical ID beginning with
`plugin_asdk_app`, wire that ID into the local plugin package with:

```bash
npm run configure:chatgpt -- plugin_asdk_app_<id>
npm run check:chatgpt
```

This creates `.app.json` and adds the compatibility `apps` mapping to the
plugin manifest. It is intentionally generated after ChatGPT creates the
account-specific connection instead of storing an invented ID in source.

For local KaizenOS reads and writes, start the stdio server with the token in
your shell environment:

```bash
KAIZENOS_MCP_BEARER_TOKEN=<personal-key-or-private-token> npm run start:stdio
```

Keep the value in a local secret manager or shell session. Do not place it in
`.env`, the plugin package, prompts, widget state, or logs. The server accepts
personal `kai_...` keys directly and preserves KaizenOS attribution. It also
supports a private shared token for local compatibility.

ChatGPT web and mobile need an authenticated MCP connection before they can use
live KaizenOS tools. The current Developer Mode connection is no-auth, so it
exposes the advisory surface while correctly returning an
authentication-required result for live CRM/project calls. Do not put one
personal key into an anonymous public endpoint.

### Public coworker distribution

For coworker access, deploy the Netlify Function behind a stable public HTTPS
origin. Netlify is configured in `netlify.toml`; the MCP endpoint is `/mcp` and
the health endpoint is `/healthz`.

After authenticating Netlify, link or create the site and deploy:

```bash
npx netlify login
npx netlify status
npx netlify link
npx netlify deploy --prod
```

Before asking ChatGPT to connect, enable the Supabase OAuth 2.1 server for the
KaizenOS project, set its authorization/consent path to
`/oauth/consent`, and deploy the KaizenOS frontend containing
`src/pages/OAuthConsent.tsx`. The frontend is the consent screen that lets a
user inspect the requesting app, approve or deny access, and return to ChatGPT.
Keep the issuer, JWKS, audience, and exact `/mcp` resource values aligned with
the Netlify environment in `netlify.toml`.

For a local Netlify Function test, use:

```bash
npm run netlify:dev
```

The container build remains available for a non-Netlify production host:

```bash
docker build -t kaizen-commerce .
docker run --rm -p 8787:8787 \
  -e HOST=0.0.0.0 \
  -e PORT=8787 \
  -e UI_DOMAIN=https://your-plugin.example.com \
  kaizen-commerce
```

Then submit the plugin from the OpenAI Platform app submission flow, scan the
live MCP endpoint, provide the required listing/legal information and test
prompts, and publish it after approval. The checked-in
`chatgpt-app-submission.json` is the prepared testing packet. Coworkers can
then install it individually from the universal directory on their own
ChatGPT accounts. A Business workspace is not required for that public
distribution model, but public approval and surface availability are still
required.

The public release is advisory for anonymous users. Its KaizenOS tool
definitions are present, but live CRM/project reads and writes require caller
authentication. The plugin does not connect to Shopify or AnyDB, and it does
not send external messages or approve/sign commercial documents.

## Example prompts

```text
@Kaizen Commerce prep me for this merchant's Shopify POS discovery call:
12 stores, Lightspeed Retail, NetSuite ERP, Shopify ecommerce, and complex
special orders.
```

```text
@Kaizen Commerce assess the migration risks and propose the right delivery lane.
```

```text
@Kaizen Commerce turn these confirmed discovery facts into a scope-first SOW.
```

## Packaged skills

- `kaizen-commerce-expert` — Kai router and full Kaizen Commerce operating system
- `kaizen-anydb-schema` — AnyDB schema and workflow design
- `kaizen-frontend-audit` — frontend quality and implementation audit
- `kaizen-migration-qa` — migration verification and reconciliation
- `kaizen-retail-architecture` — retail systems architecture
- `kaizen-retail-research` — retail and commerce research
- `kaizen-shopify-flow` — Shopify Flow design
- `kaizen-shopify-migration` — Shopify migration planning
- `kaizen-subagent-orchestrator` — bounded delegation patterns

## MCP tools

- `search` and `fetch` — standard read-only knowledge retrieval
- `analyze_opportunity` — merchant complexity, risks, missing inputs, and lane
- `build_solution_architecture` — source-of-truth and integration workstreams
- `assess_migration` — migration risks and QA gates
- `generate_blueprint` — draft Blueprint structure from supplied facts
- `generate_proposal` — draft proposal structure without inventing pricing
- `generate_sow` — draft SOW structure without sending or approving contracts
- `render_kaizen_workbench` — render the versioned read-only Workbench UI from a prior result
- `kai_search_context`, `kai_get_record_context`, `kai_get_priorities` — authenticated KaizenOS context reads
- `kai_create_*`, `kai_update_*`, and `kai_move_*` CRM tools — merchants, partners, contacts, deals, and stages
- `kai_create_project`, `kai_activate_deal_engagement`, `kai_update_project`, `kai_move_project_status` — project lifecycle operations
- `kai_create_task`, `kai_update_task`, and milestone tools — delivery-plan operations
- `kai_log_activity`, `kai_attach_source`, `kai_link_document`, and `kai_create_client_request` — audited project/CRM evidence and request writes
- `kai_list_client_update_drafts`, `kai_draft_client_update` — reviewable client-update drafts

KaizenOS write tools accept the canonical `input`, `dryRun`, and
`idempotencyKey` envelope. The adapter blocks committed writes without an
idempotency key and blocks hosted shared-token commits unless
`KAIZENOS_ALLOW_SERVER_WRITES=true` is explicitly enabled for a private
deployment. The model must still obtain explicit operator approval between the
preview and commit calls.

## Workbench UI

The resource is served by the same MCP server and uses the MCP Apps bridge
(`ui/initialize`, `tools/call`, `ui/notifications/tool-result`, `ui/message`,
and `ui/update-model-context`). ChatGPT-only `window.openai` helpers are
feature-detected for display mode, widget state, follow-up messaging, and tool
calls when the host exposes them.

## Run the MCP server

```bash
npm install
npm run check
npm run start:stdio
```

For ChatGPT Developer Mode or MCP Inspector, run the Streamable HTTP endpoint:

```bash
npm run start
# MCP endpoint: http://127.0.0.1:8787/mcp
```

The public ChatGPT path requires a stable HTTPS deployment or a development
tunnel. The local Codex plugin uses the stdio configuration in `.mcp.json`.
Custom UI rendering requires an MCP Apps-compatible host; the local stdio
smoke check validates the resource and bridge contract but does not replace
visual QA in ChatGPT Developer Mode.
