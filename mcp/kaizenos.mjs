import { randomUUID } from "node:crypto";

import kaizenOsContract from "../contracts/kaizenos-agent-tools.json" with { type: "json" };
import { bearerToken, isLikelyJwt, isPersonalAgentKey, oauthChallenge } from "./oauth.mjs";

const DEFAULT_KAIZENOS_MCP_URL = "https://zovuwpfbsmnzgfkgxxpp.supabase.co/functions/v1/agent-mcp";
const DEFAULT_PROTOCOL_VERSION = "2025-06-18";
const DEFAULT_TIMEOUT_MS = 15_000;

// This is the intentionally narrow public-plugin slice of the canonical
// KaizenOS contract. Finance, outbound messaging, Outlook sync, quote-send,
// and discovery-email actions remain outside this adapter.
const KAIZENOS_TOOL_NAMES = [
  "kai_search_context",
  "kai_get_record_context",
  "kai_get_priorities",
  "kai_create_merchant",
  "kai_update_merchant",
  "kai_create_partner",
  "kai_update_partner",
  "kai_create_contact",
  "kai_update_contact",
  "kai_create_deal",
  "kai_update_deal",
  "kai_move_deal_stage",
  "kai_create_project",
  "kai_activate_deal_engagement",
  "kai_update_project",
  "kai_move_project_status",
  "kai_create_task",
  "kai_update_task",
  "kai_create_project_milestone",
  "kai_update_project_milestone",
  "kai_delete_project_milestone",
  "kai_log_activity",
  "kai_attach_source",
  "kai_link_document",
  "kai_create_client_request",
  "kai_list_client_update_drafts",
  "kai_draft_client_update",
];

const canonicalByName = new Map(kaizenOsContract.map((tool) => [tool.name, tool]));

for (const name of KAIZENOS_TOOL_NAMES) {
  if (!canonicalByName.has(name)) {
    throw new Error(`KaizenOS contract is missing the required named tool: ${name}`);
  }
}

export const KAIZENOS_TOOL_DEFINITIONS = Object.freeze(
  KAIZENOS_TOOL_NAMES.map((name) => Object.freeze({ ...canonicalByName.get(name) })),
);

const writeToolNames = new Set(
  KAIZENOS_TOOL_DEFINITIONS.filter((tool) => tool.destructive === true).map((tool) => tool.name),
);

export const KAIZENOS_READ_TOOL_NAMES = Object.freeze(
  KAIZENOS_TOOL_DEFINITIONS.filter((tool) => !writeToolNames.has(tool.name)).map((tool) => tool.name),
);

export const KAIZENOS_WRITE_TOOL_NAMES = Object.freeze([...writeToolNames]);

function runtimeEnv(name) {
  const netlifyValue = globalThis.Netlify?.env?.get?.(name);
  if (typeof netlifyValue === "string" && netlifyValue.trim()) return netlifyValue.trim();
  if (typeof process !== "undefined" && typeof process.env?.[name] === "string" && process.env[name].trim()) {
    return process.env[name].trim();
  }
  return undefined;
}

function booleanOption(value, fallback = false) {
  if (typeof value === "boolean") return value;
  if (typeof value !== "string") return fallback;
  return ["1", "true", "yes", "on"].includes(value.trim().toLowerCase());
}

function tokenFromValue(value) {
  if (typeof value !== "string") return null;
  const trimmed = value.trim();
  if (!trimmed) return null;
  return /^bearer\s+/i.test(trimmed) ? trimmed.slice(7).trim() : trimmed;
}

function tokenFromAuthorizationHeader(value) {
  return bearerToken(value);
}

function constantTimeEqual(left, right) {
  if (typeof left !== "string" || typeof right !== "string" || left.length !== right.length) return false;
  let difference = 0;
  for (let index = 0; index < left.length; index += 1) {
    difference |= left.charCodeAt(index) ^ right.charCodeAt(index);
  }
  return difference === 0;
}

function safeEndpoint(value) {
  const endpoint = new URL(value);
  const local = endpoint.hostname === "localhost" || endpoint.hostname === "127.0.0.1";
  if (endpoint.protocol !== "https:" && !local) {
    throw new Error("KAIZENOS_MCP_URL must use HTTPS outside local development.");
  }
  endpoint.username = "";
  endpoint.password = "";
  endpoint.hash = "";
  return endpoint.toString();
}

function resolveCredential({ authorization, serverToken, hosted }) {
  const presented = tokenFromAuthorizationHeader(authorization);
  const configured = tokenFromValue(serverToken);

  // Personal kai_ keys are validated by the KaizenOS Agent API and preserve
  // founder attribution, revocation, and scope. Never forward an arbitrary
  // caller bearer token to the upstream service.
  if (presented && isPersonalAgentKey(presented)) {
    return { header: `Bearer ${presented}`, source: "personal" };
  }

  // Supabase Auth OAuth access tokens are verified at the hosted resource
  // boundary before this client is constructed. Forward only JWT-shaped
  // callers here; the canonical KaizenOS Agent API performs the identity,
  // role, scope, issuer, audience, and expiry checks again.
  if (presented && isLikelyJwt(presented)) {
    return { header: `Bearer ${presented}`, source: "oauth" };
  }

  // A configured shared token can be used by a private authenticated app, but
  // only when the caller presented that exact token. It is never an anonymous
  // fallback for a hosted/public endpoint.
  if (presented && configured && constantTimeEqual(presented, configured)) {
    return { header: `Bearer ${configured}`, source: "shared" };
  }

  // Local stdio is a private process, so the operator's environment token is
  // a safe compatibility path. Hosted requests must present caller auth.
  if (!hosted && configured) {
    return { header: `Bearer ${configured}`, source: "local" };
  }

  return null;
}

function redact(message) {
  return String(message)
    .replace(/kai_[a-f0-9]{64}/gi, "kai_[redacted]")
    .replace(/bearer\s+(?:kai_[a-f0-9]{64}|[A-Za-z0-9._~+/=-]{32,})/gi, "Bearer [redacted]");
}

function toolError(message, auth = {}) {
  const safeMessage = redact(message);
  const metadataUrl = auth.metadataUrl;
  return {
    isError: true,
    structuredContent: { ok: false, error: safeMessage },
    content: [{ type: "text", text: safeMessage }],
    ...(metadataUrl
      ? {
          _meta: {
            "mcp/www_authenticate": [oauthChallenge({
              metadataUrl,
              error: auth.error ?? "invalid_token",
              description: safeMessage,
              scope: auth.scope,
            })],
          },
        }
      : {}),
  };
}

function parseUpstreamPayload(raw) {
  const text = String(raw ?? "").trim();
  if (!text) throw new Error("KaizenOS MCP returned an empty response.");

  try {
    return JSON.parse(text);
  } catch {
    const dataLines = text
      .split(/\r?\n/)
      .filter((line) => line.startsWith("data:"))
      .map((line) => line.slice(5).trim())
      .filter((line) => line && line !== "[DONE]");
    for (const line of dataLines.reverse()) {
      try {
        return JSON.parse(line);
      } catch {
        // Try the next event payload without echoing upstream response data.
      }
    }
  }

  throw new Error("KaizenOS MCP returned an unreadable response.");
}

function normalizedStructuredContent({ definition, result, status, dryRun, idempotencyKey, responseOk }) {
  const source = result?.structuredContent;
  if (source && typeof source === "object" && !Array.isArray(source)) {
    return {
      ...source,
      ok: typeof source.ok === "boolean" ? source.ok : responseOk && result?.isError !== true,
      status: Number.isInteger(source.status) ? source.status : status,
      action: typeof source.action === "string" ? source.action : definition.action,
      dryRun: source.dryRun === true ? true : dryRun,
      idempotencyKey: source.idempotencyKey ?? idempotencyKey ?? null,
      data: Object.prototype.hasOwnProperty.call(source, "data") ? source.data : null,
    };
  }

  return {
    ok: responseOk && result?.isError !== true,
    status,
    action: definition.action,
    dryRun,
    idempotencyKey: idempotencyKey ?? null,
    data: null,
  };
}

function resultFromUpstream({ definition, response, payload, dryRun, idempotencyKey, oauthResourceMetadataUrl }) {
  if (payload?.error) {
    const message = typeof payload.error.message === "string" ? payload.error.message : "Unknown JSON-RPC error.";
    return toolError(
      `KaizenOS ${definition.name} failed: ${message}`,
      response.status === 401 ? { metadataUrl: oauthResourceMetadataUrl } : {},
    );
  }

  const result = payload?.result;
  if (!result || typeof result !== "object") {
    return toolError(`KaizenOS ${definition.name} returned no tool result.`);
  }

  const isError = !response.ok || result.isError === true;
  const structuredContent = normalizedStructuredContent({
    definition,
    result,
    status: response.status,
    dryRun,
    idempotencyKey,
    responseOk: response.ok,
  });
  const content = Array.isArray(result.content) && result.content.length
    ? result.content
    : [{ type: "text", text: `KaizenOS ${definition.name} completed.` }];

  return {
    ...(isError ? { isError: true } : {}),
    content,
    structuredContent,
    ...(result._meta && typeof result._meta === "object" ? { _meta: result._meta } : {}),
  };
}

function timeoutSignal(timeoutMs) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  return { signal: controller.signal, cancel: () => clearTimeout(timer) };
}

export function createKaizenOsClient(options = {}) {
  const hosted = options.hosted === true;
  const serverToken = options.serverToken
    ?? runtimeEnv("KAIZENOS_MCP_BEARER_TOKEN")
    ?? runtimeEnv("MCP_SERVER_BEARER_TOKEN");
  const authorization = options.authorization;
  const credential = resolveCredential({ authorization, serverToken, hosted });
  const endpointValue = options.endpoint ?? runtimeEnv("KAIZENOS_MCP_URL") ?? DEFAULT_KAIZENOS_MCP_URL;
  let endpoint;
  let configurationError;
  try {
    endpoint = safeEndpoint(endpointValue);
  } catch (error) {
    configurationError = redact(error instanceof Error ? error.message : String(error));
  }

  const allowServerWrites = booleanOption(
    options.allowServerWrites ?? runtimeEnv("KAIZENOS_ALLOW_SERVER_WRITES"),
    false,
  );
  const fetchImpl = options.fetchImpl ?? globalThis.fetch;
  const configuredTimeoutMs = Number.parseInt(
    runtimeEnv("KAIZENOS_MCP_TIMEOUT_MS") ?? String(DEFAULT_TIMEOUT_MS),
    10,
  );
  const timeoutMs = Number.isInteger(options.timeoutMs) && options.timeoutMs > 0
    ? options.timeoutMs
    : configuredTimeoutMs > 0
      ? configuredTimeoutMs
      : DEFAULT_TIMEOUT_MS;
  const serverWritesAllowed = credential?.source === "personal"
    || credential?.source === "oauth"
    || credential?.source === "local"
    || (credential?.source === "shared" && allowServerWrites);
  const oauthResourceMetadataUrl = options.oauthResourceMetadataUrl
    ?? runtimeEnv("MCP_OAUTH_RESOURCE_METADATA_URL");

  return {
    configured: Boolean(endpoint && credential),
    credentialSource: credential?.source ?? null,
    endpoint: endpoint ?? null,
    async call({ definition, input = {}, dryRun = false, idempotencyKey }) {
      const committed = definition.destructive === true && dryRun !== true;
      const normalizedKey = typeof idempotencyKey === "string" && idempotencyKey.trim()
        ? idempotencyKey.trim()
        : undefined;

      if (committed && !normalizedKey) {
        return toolError(
          `${definition.name} is a write action. Preview with dryRun=true first, then commit with a unique idempotencyKey after explicit approval.`,
        );
      }
      if (configurationError) return toolError(`KaizenOS MCP configuration error: ${configurationError}`);
      if (!credential) {
        return toolError(
          "KaizenOS authentication is required for live CRM/project data. Sign in through OAuth, use a personal kai_... bearer key, or configure a private authenticated KaizenOS MCP token; no anonymous live-record access is enabled.",
          {
            metadataUrl: oauthResourceMetadataUrl,
            error: "invalid_token",
            description: "Sign in to KaizenOS to access live CRM and project records.",
          },
        );
      }
      if (committed && !serverWritesAllowed) {
        return toolError(
          "Hosted KaizenOS commits require a caller-authenticated OAuth-linked member/admin or a personal kai_... key. A shared server token may preview writes, but it cannot commit them unless KAIZENOS_ALLOW_SERVER_WRITES=true is explicitly enabled on a private deployment.",
          {
            metadataUrl: oauthResourceMetadataUrl,
            error: "insufficient_scope",
            description: "Your KaizenOS account is not authorized to commit this write.",
          },
        );
      }
      if (typeof fetchImpl !== "function") return toolError("KaizenOS MCP forwarding is unavailable in this runtime.");

      const argumentsPayload = {
        input: input && typeof input === "object" && !Array.isArray(input) ? input : {},
        dryRun: dryRun === true,
        ...(normalizedKey ? { idempotencyKey: normalizedKey } : {}),
      };
      const requestBody = {
        jsonrpc: "2.0",
        id: randomUUID(),
        method: "tools/call",
        params: { name: definition.name, arguments: argumentsPayload },
      };
      const timeout = timeoutSignal(timeoutMs);
      let response;
      try {
        response = await fetchImpl(endpoint, {
          method: "POST",
          headers: {
            accept: "application/json, text/event-stream",
            authorization: credential.header,
            "content-type": "application/json",
            "mcp-protocol-version": DEFAULT_PROTOCOL_VERSION,
          },
          body: JSON.stringify(requestBody),
          signal: timeout.signal,
        });
      } catch (error) {
        const message = error?.name === "AbortError"
          ? `KaizenOS MCP request timed out after ${timeoutMs}ms.`
          : `KaizenOS MCP could not be reached: ${error instanceof Error ? error.message : String(error)}`;
        return toolError(message);
      } finally {
        timeout.cancel();
      }

      let payload;
      try {
        payload = parseUpstreamPayload(await response.text());
      } catch (error) {
        return toolError(error instanceof Error ? error.message : String(error));
      }

      return resultFromUpstream({
        definition,
        response,
        payload,
        dryRun: dryRun === true,
        idempotencyKey: normalizedKey,
        oauthResourceMetadataUrl,
      });
    },
  };
}

export function isKaizenOsWriteTool(name) {
  return writeToolNames.has(name);
}
