import { createLocalJWKSet, createRemoteJWKSet, jwtVerify } from "jose";

const DEFAULT_AUTH_SERVER = "https://zovuwpfbsmnzgfkgxxpp.supabase.co/auth/v1";
const DEFAULT_ISSUER = DEFAULT_AUTH_SERVER;
const DEFAULT_JWKS_URI = `${DEFAULT_AUTH_SERVER}/.well-known/jwks.json`;
const DEFAULT_AUDIENCE = "authenticated";
const DEFAULT_SCOPES = Object.freeze(["openid", "email", "profile", "offline_access"]);
const DEFAULT_RESOURCE_DOCUMENTATION = "https://github.com/Kaizen-Commerce/kaizen-commerce";

const remoteJwks = new Map();

export const KAIZEN_OAUTH_SCOPES = DEFAULT_SCOPES;

function runtimeEnv(name) {
  const netlifyValue = globalThis.Netlify?.env?.get?.(name);
  if (typeof netlifyValue === "string" && netlifyValue.trim()) return netlifyValue.trim();
  if (typeof process !== "undefined" && typeof process.env?.[name] === "string" && process.env[name].trim()) {
    return process.env[name].trim();
  }
  return undefined;
}

function normalizeUrl(value, name, { allowHttpLocal = false } = {}) {
  const url = new URL(value);
  const isLocal = url.hostname === "localhost" || url.hostname === "127.0.0.1";
  if (url.protocol !== "https:" && !(allowHttpLocal && isLocal)) {
    throw new Error(`${name} must use HTTPS outside local development.`);
  }
  url.username = "";
  url.password = "";
  url.hash = "";
  return url.toString().replace(/\/$/u, "");
}

function scopeList(value) {
  if (Array.isArray(value)) return [...new Set(value.map(String).map((scope) => scope.trim()).filter(Boolean))];
  if (typeof value === "string" && value.trim()) {
    return [...new Set(value.trim().split(/[\s,]+/u).map((scope) => scope.trim()).filter(Boolean))];
  }
  return [...DEFAULT_SCOPES];
}

function quoteHeaderValue(value) {
  return String(value).replaceAll("\\", "\\\\").replaceAll('"', '\\"');
}

export function bearerToken(authorizationHeader) {
  if (typeof authorizationHeader !== "string") return null;
  const match = authorizationHeader.trim().match(/^Bearer\s+(.+)$/iu);
  return match?.[1]?.trim() || null;
}

export function isPersonalAgentKey(value) {
  return typeof value === "string" && /^kai_[a-f0-9]{64}$/iu.test(value);
}

export function isLikelyJwt(value) {
  if (typeof value !== "string") return false;
  const parts = value.split(".");
  return parts.length === 3 && parts.every((part) => /^[A-Za-z0-9_-]+$/u.test(part));
}

export function oauthSettings(options = {}) {
  const resource = normalizeUrl(
    options.resource ?? runtimeEnv("MCP_RESOURCE_URL") ?? `${options.origin ?? "https://kai-commerce-agent.netlify.app"}/mcp`,
    "MCP_RESOURCE_URL",
    { allowHttpLocal: true },
  );
  const resourceOrigin = new URL(resource).origin;
  const metadataUrl = normalizeUrl(
    options.resourceMetadataUrl ??
      runtimeEnv("MCP_OAUTH_RESOURCE_METADATA_URL") ??
      `${resourceOrigin}/.well-known/oauth-protected-resource`,
    "MCP_OAUTH_RESOURCE_METADATA_URL",
    { allowHttpLocal: true },
  );
  const authorizationServer = normalizeUrl(
    options.authorizationServer ?? runtimeEnv("KAIZEN_OAUTH_AUTH_SERVER") ?? DEFAULT_AUTH_SERVER,
    "KAIZEN_OAUTH_AUTH_SERVER",
  );
  const issuer = normalizeUrl(
    options.issuer ?? runtimeEnv("KAIZEN_OAUTH_ISSUER") ?? authorizationServer,
    "KAIZEN_OAUTH_ISSUER",
  );
  const jwksUri = normalizeUrl(
    options.jwksUri ?? runtimeEnv("KAIZEN_OAUTH_JWKS_URI") ?? `${issuer}/.well-known/jwks.json`,
    "KAIZEN_OAUTH_JWKS_URI",
  );
  return Object.freeze({
    resource,
    metadataUrl,
    authorizationServer,
    issuer,
    jwksUri,
    audience: options.audience ?? runtimeEnv("KAIZEN_OAUTH_AUDIENCE") ?? DEFAULT_AUDIENCE,
    scopes: scopeList(options.scopes ?? runtimeEnv("KAIZEN_OAUTH_SCOPES")),
    resourceDocumentation:
      options.resourceDocumentation ??
      runtimeEnv("MCP_RESOURCE_DOCUMENTATION") ??
      DEFAULT_RESOURCE_DOCUMENTATION,
  });
}

export function protectedResourceMetadata(options = {}) {
  const settings = oauthSettings(options);
  return {
    resource: settings.resource,
    authorization_servers: [settings.authorizationServer],
    scopes_supported: settings.scopes,
    resource_documentation: settings.resourceDocumentation,
  };
}

export function oauthChallenge({
  metadataUrl,
  error = "invalid_token",
  description = "Sign in to KaizenOS to use this tool.",
  scope,
} = {}) {
  const metadata = metadataUrl ?? oauthSettings().metadataUrl;
  const fields = [
    `resource_metadata="${quoteHeaderValue(metadata)}"`,
    ...(scope ? [`scope="${quoteHeaderValue(scope)}"`] : []),
    `error="${quoteHeaderValue(error)}"`,
    `error_description="${quoteHeaderValue(description)}"`,
  ];
  return `Bearer ${fields.join(", ")}`;
}

function remoteKeySet(settings) {
  const existing = remoteJwks.get(settings.jwksUri);
  if (existing) return existing;
  const keySet = createRemoteJWKSet(new URL(settings.jwksUri), {
    timeoutDuration: 5_000,
    cacheMaxAge: 10 * 60 * 1_000,
  });
  remoteJwks.set(settings.jwksUri, keySet);
  return keySet;
}

function audienceValues(payload) {
  return Array.isArray(payload.aud) ? payload.aud : [payload.aud];
}

export async function verifyOAuthAccessToken(token, options = {}) {
  const settings = oauthSettings(options);
  if (!isLikelyJwt(token)) {
    return { ok: false, error: "The presented OAuth access token is not a JWT." };
  }

  try {
    const keySet = options.jwks ? createLocalJWKSet(options.jwks) : remoteKeySet(settings);
    const { payload } = await jwtVerify(token, keySet, {
      issuer: settings.issuer,
      audience: settings.audience,
      algorithms: ["ES256", "RS256"],
      clockTolerance: 5,
    });
    if (typeof payload.sub !== "string" || !payload.sub.trim()) {
      return { ok: false, error: "The OAuth token has no user subject." };
    }
    if (typeof payload.client_id !== "string" || !payload.client_id.trim()) {
      return { ok: false, error: "The OAuth token is not bound to an OAuth client." };
    }
    const audiences = audienceValues(payload);
    if (!audiences.includes(settings.audience)) {
      return { ok: false, error: "The OAuth token audience is not valid for KaizenOS." };
    }
    if (payload.resource && payload.resource !== settings.resource) {
      return { ok: false, error: "The OAuth token resource does not match Kaizen Commerce." };
    }

    return {
      ok: true,
      subject: payload.sub,
      clientId: payload.client_id,
      scopes: typeof payload.scope === "string" ? scopeList(payload.scope) : [],
      claims: payload,
      settings,
    };
  } catch (error) {
    return {
      ok: false,
      error: error instanceof Error ? error.message : "The OAuth token could not be verified.",
    };
  }
}
