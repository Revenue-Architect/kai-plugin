import assert from "node:assert/strict";

import {
  createKaizenOsClient,
  KAIZENOS_READ_TOOL_NAMES,
  KAIZENOS_TOOL_DEFINITIONS,
  KAIZENOS_WRITE_TOOL_NAMES,
} from "../mcp/kaizenos.mjs";

const merchantCreate = KAIZENOS_TOOL_DEFINITIONS.find((tool) => tool.name === "kai_create_merchant");
if (!merchantCreate) throw new Error("Canonical CRM create tool is missing from the adapter.");

for (const name of [
  "kai_create_merchant",
  "kai_update_contact",
  "kai_create_deal",
  "kai_activate_deal_engagement",
  "kai_create_project",
  "kai_create_task",
  "kai_update_project_milestone",
  "kai_log_activity",
]) {
  assert.ok(KAIZENOS_WRITE_TOOL_NAMES.includes(name), `${name} should be a write tool.`);
}
for (const name of ["kai_search_context", "kai_get_record_context", "kai_get_priorities", "kai_list_client_update_drafts"]) {
  assert.ok(KAIZENOS_READ_TOOL_NAMES.includes(name), `${name} should be a read tool.`);
}
for (const name of ["kai_create_expense", "kai_trigger_outlook_sync", "kai_send_intake_request", "kai_send_quote_for_acceptance"]) {
  assert.ok(!KAIZENOS_TOOL_DEFINITIONS.some((tool) => tool.name === name), `${name} must remain outside this plugin slice.`);
}

const personalKey = `kai_${"a".repeat(64)}`;
const calls = [];
const fetchImpl = async (url, options) => {
  calls.push({ url, options, body: JSON.parse(options.body) });
  const request = calls.at(-1).body;
  const dryRun = request.params.arguments.dryRun === true;
  return new Response(JSON.stringify({
    jsonrpc: "2.0",
    id: request.id,
    result: {
      content: [{ type: "text", text: "mock KaizenOS result" }],
      structuredContent: {
        ok: true,
        status: 200,
        action: "create_merchant",
        dryRun,
        idempotencyKey: request.params.arguments.idempotencyKey ?? null,
        data: { preview: dryRun },
      },
    },
  }), { status: 200, headers: { "content-type": "application/json" } });
};

const anonymous = createKaizenOsClient({ hosted: true, fetchImpl, endpoint: "https://example.test/mcp" });
const anonymousResult = await anonymous.call({ definition: merchantCreate, input: { name: "Test" }, dryRun: true });
assert.equal(anonymousResult.isError, true);
assert.match(anonymousResult.content[0].text, /authentication is required/i);
assert.equal(calls.length, 0, "Anonymous calls must not reach KaizenOS.");

const shared = createKaizenOsClient({
  hosted: true,
  serverToken: "shared-test-token",
  authorization: "Bearer shared-test-token",
  fetchImpl,
  endpoint: "https://example.test/mcp",
});
const sharedPreview = await shared.call({ definition: merchantCreate, input: { name: "Preview" }, dryRun: true });
assert.equal(sharedPreview.structuredContent.dryRun, true);
assert.equal(calls.at(-1).options.headers.authorization, "Bearer shared-test-token");
const sharedCommit = await shared.call({ definition: merchantCreate, input: { name: "Commit" }, dryRun: false, idempotencyKey: "shared-commit-1" });
assert.equal(sharedCommit.isError, true, "Shared hosted tokens must not commit by default.");
assert.match(sharedCommit.content[0].text, /private deployment/i);
assert.equal(calls.length, 1, "Blocked shared commit must not reach KaizenOS.");

const personal = createKaizenOsClient({
  hosted: true,
  authorization: `Bearer ${personalKey}`,
  fetchImpl,
  endpoint: "https://example.test/mcp",
});
const missingKey = await personal.call({ definition: merchantCreate, input: { name: "Missing key" }, dryRun: false });
assert.equal(missingKey.isError, true);
assert.equal(calls.length, 1, "A commit without an idempotency key must be blocked locally.");
const committed = await personal.call({
  definition: merchantCreate,
  input: { name: "Approved merchant" },
  dryRun: false,
  idempotencyKey: "personal-commit-1",
});
assert.equal(committed.isError, undefined);
assert.equal(committed.structuredContent.dryRun, false);
assert.equal(committed.structuredContent.idempotencyKey, "personal-commit-1");
assert.equal(calls.at(-1).options.headers.authorization, `Bearer ${personalKey}`);
assert.equal(calls.at(-1).body.params.name, "kai_create_merchant");
assert.deepEqual(calls.at(-1).body.params.arguments.input, { name: "Approved merchant" });

const local = createKaizenOsClient({
  hosted: false,
  serverToken: "local-test-token",
  fetchImpl,
  endpoint: "https://example.test/mcp",
});
const localCommit = await local.call({ definition: merchantCreate, input: { name: "Local merchant" }, idempotencyKey: "local-1" });
assert.equal(localCommit.isError, undefined);
assert.equal(calls.at(-1).options.headers.authorization, "Bearer local-test-token");

console.log(`KaizenOS adapter check passed: ${KAIZENOS_TOOL_DEFINITIONS.length} named tools, ${KAIZENOS_WRITE_TOOL_NAMES.length} writes, auth and commit gates.`);
