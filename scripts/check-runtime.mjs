import { spawn } from "node:child_process";
import { setTimeout as delay } from "node:timers/promises";
import { fileURLToPath } from "node:url";
import { join } from "node:path";

const pluginRoot = join(fileURLToPath(new URL("..", import.meta.url)));
const port = Number.parseInt(process.env.KAIZEN_TEST_PORT ?? "8797", 10);
const baseUrl = `http://127.0.0.1:${port}`;
const server = spawn(process.execPath, [join(pluginRoot, "mcp", "server.mjs"), "--http"], {
  cwd: pluginRoot,
  env: { ...process.env, HOST: "127.0.0.1", PORT: String(port), MCP_TRANSPORT: "http" },
  stdio: ["ignore", "pipe", "pipe"],
});

function fail(message) {
  throw new Error(message);
}

async function waitForHealth() {
  for (let attempt = 0; attempt < 50; attempt += 1) {
    try {
      const response = await fetch(`${baseUrl}/healthz`);
      if (response.ok) return;
    } catch {
      // The server may still be starting.
    }
    await delay(100);
  }
  fail("MCP server did not become healthy in time.");
}

async function readRpcResponse(response) {
  const text = await response.text();
  if (response.headers.get("content-type")?.includes("text/event-stream")) {
    const dataLine = text.split(/\r?\n/).find((line) => line.startsWith("data: "));
    if (!dataLine) fail("MCP stream response did not contain a data event.");
    return JSON.parse(dataLine.slice(6));
  }
  return JSON.parse(text);
}

async function rpc(body, sessionId) {
  const headers = { "Content-Type": "application/json", Accept: "application/json, text/event-stream" };
  if (sessionId) headers["MCP-Session-Id"] = sessionId;
  const response = await fetch(`${baseUrl}/mcp`, { method: "POST", headers, body: JSON.stringify(body) });
  const payload = await readRpcResponse(response);
  if (!response.ok) fail(`MCP request failed with ${response.status}: ${JSON.stringify(payload)}`);
  return { payload, sessionId: response.headers.get("mcp-session-id") ?? sessionId };
}

try {
  await waitForHealth();
  const options = await fetch(`${baseUrl}/mcp`, { method: "OPTIONS" });
  if (options.status !== 204) fail(`MCP OPTIONS returned ${options.status}, expected 204.`);
  if (!options.headers.get("access-control-expose-headers")?.toLowerCase().includes("mcp-session-id")) {
    fail("MCP OPTIONS does not expose MCP-Session-Id.");
  }

  const oversized = await fetch(`${baseUrl}/mcp`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ oversized: "x".repeat(2_000_100) }),
  });
  if (oversized.status !== 413) fail(`Oversized MCP body returned ${oversized.status}, expected 413.`);

  const initialized = await rpc({
    jsonrpc: "2.0",
    id: 1,
    method: "initialize",
    params: {
      protocolVersion: "2025-06-18",
      capabilities: {},
      clientInfo: { name: "kaizen-runtime-check", version: "0.3.0" },
    },
  });
  if (!initialized.sessionId) fail("MCP initialize did not return a session id.");

  const listed = await rpc({ jsonrpc: "2.0", id: 2, method: "tools/list", params: {} }, initialized.sessionId);
  const toolNames = listed.payload.result?.tools?.map((tool) => tool.name) ?? [];
  for (const expected of [
    "search",
    "fetch",
    "analyze_opportunity",
    "render_kaizen_workbench",
    "kai_search_context",
    "kai_create_merchant",
    "kai_create_project",
    "kai_activate_deal_engagement",
    "kai_create_task",
    "kai_update_project_milestone",
  ]) {
    if (!toolNames.includes(expected)) fail(`MCP tools/list is missing ${expected}.`);
  }

  const resources = await rpc({ jsonrpc: "2.0", id: 3, method: "resources/list", params: {} }, initialized.sessionId);
  const resourceUris = resources.payload.result?.resources?.map((resource) => resource.uri) ?? [];
  if (!resourceUris.includes("ui://kaizen-commerce/workbench-v3.html")) fail("Workbench resource is missing.");

  const rendered = await rpc({
    jsonrpc: "2.0",
    id: 4,
    method: "tools/call",
    params: { name: "render_kaizen_workbench", arguments: { view: "deal_snapshot", payload: { merchant: "Runtime check" } } },
  }, initialized.sessionId);
  if (rendered.payload.result?.structuredContent?.readOnly !== true) fail("Workbench result is not marked read-only.");

  const blockedWrite = await rpc({
    jsonrpc: "2.0",
    id: 5,
    method: "tools/call",
    params: { name: "kai_create_merchant", arguments: { input: { name: "Runtime auth check" }, dryRun: true } },
  }, initialized.sessionId);
  if (blockedWrite.payload.result?.isError !== true) fail("Anonymous KaizenOS write did not fail closed.");

  await fetch(`${baseUrl}/mcp`, { method: "DELETE", headers: { "MCP-Session-Id": initialized.sessionId } });
  console.log("MCP runtime check passed: health, initialize, tools/list, resources/list, render tool, anonymous write gate, and session close.");
} finally {
  server.kill("SIGTERM");
}
