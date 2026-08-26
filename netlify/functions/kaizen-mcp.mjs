import { WebStandardStreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/webStandardStreamableHttp.js";

import { createKaizenServer } from "../../mcp/server.mjs";
import {
  bearerToken,
  isLikelyJwt,
  isPersonalAgentKey,
  oauthChallenge,
  oauthSettings,
  protectedResourceMetadata,
  verifyOAuthAccessToken,
} from "../../mcp/oauth.mjs";

const netlifyEnv = globalThis.Netlify?.env;
const MAX_BODY_BYTES = Number.parseInt(netlifyEnv?.get("MAX_JSON_BODY_BYTES") ?? process.env.MAX_JSON_BODY_BYTES ?? "2000000", 10);
const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Authorization, Content-Type, MCP-Session-Id, Last-Event-ID, MCP-Protocol-Version",
  "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
  "Access-Control-Expose-Headers": "MCP-Session-Id, MCP-Protocol-Version, WWW-Authenticate",
  "X-Content-Type-Options": "nosniff",
};

function withCors(response) {
  const headers = new Headers(response.headers);
  for (const [name, value] of Object.entries(corsHeaders)) headers.set(name, value);
  return new Response(response.body, { status: response.status, statusText: response.statusText, headers });
}

function jsonResponse(body, status = 200, extraHeaders = {}) {
  return withCors(new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store", ...extraHeaders },
  }));
}

function runtimeEnv(name) {
  const netlifyValue = netlifyEnv?.get?.(name);
  if (typeof netlifyValue === "string" && netlifyValue.trim()) return netlifyValue.trim();
  if (typeof process !== "undefined" && typeof process.env?.[name] === "string" && process.env[name].trim()) {
    return process.env[name].trim();
  }
  return undefined;
}

function tokenFromValue(value) {
  if (typeof value !== "string") return null;
  const trimmed = value.trim();
  if (!trimmed) return null;
  return /^bearer\s+/iu.test(trimmed) ? trimmed.slice(7).trim() : trimmed;
}

function constantTimeEqual(left, right) {
  if (typeof left !== "string" || typeof right !== "string" || left.length !== right.length) return false;
  let difference = 0;
  for (let index = 0; index < left.length; index += 1) difference |= left.charCodeAt(index) ^ right.charCodeAt(index);
  return difference === 0;
}

function requestOAuthSettings(request) {
  const origin = new URL(request.url).origin;
  return oauthSettings({
    origin,
    resource: runtimeEnv("MCP_RESOURCE_URL") ?? `${origin}/mcp`,
  });
}

async function validateCaller(request) {
  const token = bearerToken(request.headers.get("authorization"));
  if (!token) return { kind: "missing", settings: requestOAuthSettings(request) };
  if (isPersonalAgentKey(token)) return { kind: "compat", settings: requestOAuthSettings(request) };

  const shared = tokenFromValue(runtimeEnv("KAIZENOS_MCP_BEARER_TOKEN") ?? runtimeEnv("MCP_SERVER_BEARER_TOKEN"));
  if (shared && constantTimeEqual(token, shared)) {
    return { kind: "compat", settings: requestOAuthSettings(request) };
  }

  if (!isLikelyJwt(token)) return { kind: "invalid", settings: requestOAuthSettings(request) };
  const settings = requestOAuthSettings(request);
  const verification = await verifyOAuthAccessToken(token, settings);
  return verification.ok
    ? { kind: "oauth", settings, verification }
    : { kind: "invalid", settings, error: verification.error };
}

function unauthorizedResponse(settings, description = "The KaizenOS sign-in has expired or is invalid.") {
  return jsonResponse(
    { error: "Unauthorized" },
    401,
    {
      "WWW-Authenticate": oauthChallenge({
        metadataUrl: settings.metadataUrl,
        error: "invalid_token",
        description,
      }),
    },
  );
}

export default async function handler(request) {
  if (request.method === "OPTIONS") return withCors(new Response(null, { status: 204 }));

  const url = new URL(request.url);
  if (url.pathname === "/.well-known/oauth-protected-resource") {
    if (request.method !== "GET") return jsonResponse({ error: "Method not allowed" }, 405);
    const settings = requestOAuthSettings(request);
    return jsonResponse(protectedResourceMetadata(settings), 200, {
      "Cache-Control": "public, max-age=300",
    });
  }

  if (url.pathname === "/healthz") {
    const oauth = requestOAuthSettings(request);
    return jsonResponse({
      status: "ok",
      server: "kaizen-knowledge",
      version: "0.4.0",
      runtime: "netlify-function",
      kaizenOs: "caller-authenticated CRM and project operations",
      oauth: {
        resource: oauth.resource,
        issuer: oauth.issuer,
        jwksUri: oauth.jwksUri,
        scopes: oauth.scopes,
      },
    });
  }

  if (url.pathname !== "/mcp") return jsonResponse({ error: "Not found" }, 404);

  const declaredLength = Number.parseInt(request.headers.get("content-length") ?? "0", 10);
  if (declaredLength > MAX_BODY_BYTES) {
    return jsonResponse({ error: `Request body exceeds ${MAX_BODY_BYTES} bytes.` }, 413);
  }

  const caller = await validateCaller(request);
  if (caller.kind === "invalid") return unauthorizedResponse(caller.settings);

  const server = createKaizenServer({
    hostedRequest: true,
    kaizenOsAuthorization: request.headers.get("authorization") ?? undefined,
    oauthResourceMetadataUrl: caller.settings.metadataUrl,
  });
  const transport = new WebStandardStreamableHTTPServerTransport({
    sessionIdGenerator: undefined,
  });

  try {
    await server.connect(transport);
    return withCors(await transport.handleRequest(request));
  } catch (error) {
    console.error("Netlify MCP request failed:", error);
    return jsonResponse({ jsonrpc: "2.0", error: { code: -32603, message: "Internal MCP server error" }, id: null }, 500);
  }
}

export const config = {
  path: ["/mcp", "/healthz", "/.well-known/oauth-protected-resource"],
};
