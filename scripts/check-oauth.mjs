import { exportJWK, generateKeyPair, SignJWT } from "jose";
import {
  oauthChallenge,
  protectedResourceMetadata,
  verifyOAuthAccessToken,
} from "../mcp/oauth.mjs";

function fail(message) {
  throw new Error(message);
}

const settings = {
  resource: "https://kai-commerce-agent.example/mcp",
  resourceMetadataUrl: "https://kai-commerce-agent.example/.well-known/oauth-protected-resource",
  authorizationServer: "https://kaizen-auth.example/auth/v1",
  issuer: "https://kaizen-auth.example/auth/v1",
  jwksUri: "https://kaizen-auth.example/auth/v1/.well-known/jwks.json",
  audience: "authenticated",
  scopes: ["openid", "email", "profile", "offline_access"],
};

const metadata = protectedResourceMetadata(settings);
if (metadata.resource !== settings.resource) fail("Protected-resource metadata has the wrong resource identifier.");
if (metadata.authorization_servers?.[0] !== settings.authorizationServer) fail("Protected-resource metadata has the wrong authorization server.");
const challenge = oauthChallenge({ metadataUrl: settings.resourceMetadataUrl });
if (!challenge.includes(`resource_metadata="${settings.resourceMetadataUrl}"`)) {
  fail("OAuth challenge is missing the protected-resource metadata URL.");
}

const { privateKey, publicKey } = await generateKeyPair("ES256");
const jwk = await exportJWK(publicKey);
jwk.alg = "ES256";
jwk.use = "sig";
jwk.kid = "kaizen-oauth-check";
const jwks = { keys: [jwk] };

async function token(overrides = {}) {
  const claims = {
    sub: "user-kaizen-check",
    client_id: "chatgpt-public-client",
    scope: "openid email profile offline_access",
    resource: settings.resource,
    ...overrides,
  };
  return new SignJWT(claims)
    .setProtectedHeader({ alg: "ES256", kid: jwk.kid })
    .setIssuer(settings.issuer)
    .setAudience(settings.audience)
    .setSubject(claims.sub)
    .setIssuedAt()
    .setExpirationTime("10m")
    .sign(privateKey);
}

const valid = await verifyOAuthAccessToken(await token(), { ...settings, jwks });
if (!valid.ok || valid.subject !== "user-kaizen-check" || valid.clientId !== "chatgpt-public-client") {
  fail("A valid OAuth access token was not accepted with its user/client identity.");
}
if (!valid.scopes.includes("openid") || !valid.scopes.includes("offline_access")) {
  fail("OAuth scopes were not parsed from a valid access token.");
}

const wrongAudience = await verifyOAuthAccessToken(
  await token(),
  { ...settings, audience: "different-resource", jwks },
);
if (wrongAudience.ok) fail("A token with the wrong audience was accepted.");

const missingClient = await verifyOAuthAccessToken(await token({ client_id: undefined }), { ...settings, jwks });
if (missingClient.ok) fail("A token without an OAuth client binding was accepted.");

const wrongResource = await verifyOAuthAccessToken(
  await token({ resource: "https://other.example/mcp" }),
  { ...settings, jwks },
);
if (wrongResource.ok) fail("A token for a different MCP resource was accepted.");

console.log("OAuth check passed: metadata, challenge, signature, issuer, audience, client binding, scope, and resource checks.");
