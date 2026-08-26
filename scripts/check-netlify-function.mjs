import { join } from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = join(fileURLToPath(new URL("..", import.meta.url)));
const { default: handler } = await import(join(pluginRoot, "netlify/functions/kaizen-mcp.mjs"));

function fail(message) {
  throw new Error(message);
}

async function call(body) {
  const response = await handler(new Request("https://example.net/mcp", {
    method: "POST",
    headers: { "content-type": "application/json", accept: "application/json, text/event-stream" },
    body: JSON.stringify(body),
  }));
  const text = await response.text();
  if (!response.ok) fail(`Netlify MCP function returned ${response.status}.`);
  const dataLine = text.split(/\r?\n/).find((line) => line.startsWith("data: "));
  if (!dataLine) fail("Netlify MCP function did not return an SSE data event.");
  return { response, payload: JSON.parse(dataLine.slice(6)) };
}

const health = await handler(new Request("https://example.net/healthz"));
if (health.status !== 200) fail(`Netlify health check returned ${health.status}.`);
if (health.headers.get("access-control-allow-origin") !== "*") fail("Netlify health response is missing CORS headers.");
if (!health.headers.get("access-control-expose-headers")?.includes("WWW-Authenticate")) {
  fail("Netlify CORS does not expose WWW-Authenticate.");
}

const resourceMetadata = await handler(new Request("https://example.net/.well-known/oauth-protected-resource"));
if (resourceMetadata.status !== 200) fail(`OAuth protected-resource metadata returned ${resourceMetadata.status}.`);
const metadata = JSON.parse(await resourceMetadata.text());
if (metadata.resource !== "https://example.net/mcp") fail("OAuth metadata does not use the request's MCP resource URL in local checks.");
if (!Array.isArray(metadata.authorization_servers) || !metadata.authorization_servers.length) fail("OAuth metadata has no authorization server.");

await call({
  jsonrpc: "2.0",
  id: 1,
  method: "initialize",
  params: { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "netlify-check", version: "1.0" } },
});

const listed = await call({ jsonrpc: "2.0", id: 2, method: "tools/list", params: {} });
const tools = listed.payload.result?.tools ?? [];
const toolNames = tools.map((tool) => tool.name);
for (const expected of [
  "search",
  "fetch",
  "render_kaizen_workbench",
  "kai_search_context",
  "kai_create_merchant",
  "kai_create_project",
  "kai_activate_deal_engagement",
  "kai_create_task",
  "kai_update_project_milestone",
]) {
  if (!toolNames.includes(expected)) fail(`Netlify MCP function is missing ${expected}.`);
}
const merchantTool = tools.find((tool) => tool.name === "kai_create_merchant");
if (merchantTool?.annotations?.readOnlyHint !== false || merchantTool?.annotations?.destructiveHint !== true) {
  fail("Netlify MCP CRM write metadata is not marked destructive.");
}
if (merchantTool?.securitySchemes?.[0]?.type !== "oauth2") {
  fail("Netlify MCP CRM write metadata is missing root-level OAuth security schemes.");
}

const searched = await call({
  jsonrpc: "2.0",
  id: 3,
  method: "tools/call",
  params: { name: "search", arguments: { query: "Shopify POS" } },
});
if (searched.payload.result?.isError) fail("Netlify MCP search returned an error.");
const searchText = searched.payload.result?.content?.find((item) => item.type === "text")?.text;
const searchPayload = searchText ? JSON.parse(searchText) : null;
if (!searchPayload?.results?.length) fail("Netlify MCP search returned no results.");

const blockedWrite = await call({
  jsonrpc: "2.0",
  id: 4,
  method: "tools/call",
  params: { name: "kai_create_merchant", arguments: { input: { name: "Netlify auth check" }, dryRun: true } },
});
if (blockedWrite.payload.result?.isError !== true) fail("Anonymous Netlify KaizenOS write did not fail closed.");
const blockedText = blockedWrite.payload.result?.content?.find((item) => item.type === "text")?.text ?? "";
if (!/authentication is required/i.test(blockedText)) fail("Anonymous KaizenOS failure did not explain the authentication requirement.");

console.log("Netlify function check passed: health, CORS, initialize, tools/list, search, write metadata, and anonymous write gate.");
