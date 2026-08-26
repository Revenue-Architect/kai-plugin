import { createServer as createHttpServer } from "node:http";
import { createHash, randomUUID } from "node:crypto";
import { readFile, readdir, stat } from "node:fs/promises";
import { basename, dirname, extname, join, relative, sep } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

import { createKaizenOsClient, KAIZENOS_TOOL_DEFINITIONS } from "./kaizenos.mjs";
import { KAIZEN_OAUTH_SCOPES } from "./oauth.mjs";

const SERVER_NAME = "kaizen-knowledge";
const SERVER_VERSION = "0.4.0";
const PORT = Number.parseInt(process.env.PORT ?? "8787", 10);
const HOST = process.env.HOST ?? "127.0.0.1";
const MAX_JSON_BODY_BYTES = Number.parseInt(process.env.MAX_JSON_BODY_BYTES ?? "2000000", 10);
const UI_DOMAIN = process.env.UI_DOMAIN?.trim();
const moduleRoot = dirname(dirname(fileURLToPath(import.meta.url)));
// Netlify bundles this module into /var/task/netlify/functions. Static files
// declared with functions.included_files are copied relative to /var/task, so
// move one level up when the bundled module root is the Netlify directory.
const pluginRoot = moduleRoot.endsWith(`${sep}netlify`) ? dirname(moduleRoot) : moduleRoot;
const skillsRoot = join(pluginRoot, "skills");
const sourceRepo = "https://github.com/Kaizen-Commerce/kaizen-skills";
const supportedTextExtensions = new Set([
  ".css",
  ".html",
  ".js",
  ".json",
  ".md",
  ".mjs",
  ".py",
  ".txt",
  ".ts",
  ".yaml",
  ".yml",
]);
const maxIndexedBytes = 1_000_000;
const maxFetchBytes = 1_000_000;
const WORKBENCH_URI = "ui://kaizen-commerce/workbench-v3.html";
const WORKBENCH_MIME_TYPE = "text/html;profile=mcp-app";
const workbenchViewTitles = {
  deal_snapshot: "Deal Snapshot",
  architecture_map: "Architecture Map",
  migration_risk: "Migration Risk",
  scope_builder: "Scope Builder",
  blueprint: "Blueprint Diagnostic",
  proposal: "Proposal Draft",
  sow: "SOW Draft",
};

let knowledgeIndexPromise;
let workbenchHtmlPromise;
let workbenchStateVersion = 0;

async function getWorkbenchHtml() {
  workbenchHtmlPromise ??= readFile(join(pluginRoot, "mcp", "workbench.html"), "utf8");
  return workbenchHtmlPromise;
}

function toPosixPath(value) {
  return value.split(sep).join("/");
}

function canonicalUrl(skillName, relativePath) {
  const sourcePath = ["skills", skillName, ...relativePath.split("/")]
    .map((segment) => encodeURIComponent(segment))
    .join("/");
  return `${sourceRepo}/blob/main/${sourcePath}`;
}

function resourceId(skillName, relativePath) {
  return `kaizen://skills/${skillName}/${relativePath}`;
}

function parseFrontmatter(text) {
  const match = text.match(/^---\s*\n([\s\S]*?)\n---\s*(?:\n|$)/);
  if (!match) return {};
  const values = {};
  for (const line of match[1].split("\n")) {
    const separator = line.indexOf(":");
    if (separator < 1) continue;
    const key = line.slice(0, separator).trim();
    const value = line.slice(separator + 1).trim().replace(/^['"]|['"]$/g, "");
    if (key && value) values[key] = value;
  }
  return values;
}

function titleFor(relativePath, text, frontmatter = {}) {
  if (frontmatter.name) return frontmatter.name;
  const heading = text.match(/^#\s+(.+)$/m)?.[1]?.trim();
  if (heading) return heading.replace(/\s+#*$/, "");
  return basename(relativePath, extname(relativePath));
}

async function collectTextFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    if (entry.name.startsWith(".")) continue;
    const path = join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await collectTextFiles(path)));
      continue;
    }
    if (!supportedTextExtensions.has(extname(entry.name).toLowerCase())) continue;
    const fileStats = await stat(path);
    if (fileStats.size > maxIndexedBytes) continue;
    files.push(path);
  }
  return files;
}

async function buildKnowledgeIndex() {
  const entries = [];
  const skillDirs = (await readdir(skillsRoot, { withFileTypes: true }))
    .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
    .sort((a, b) => a.name.localeCompare(b.name));

  for (const skillDir of skillDirs) {
    const skillName = skillDir.name;
    const skillRoot = join(skillsRoot, skillName);
    const files = await collectTextFiles(skillRoot);
    for (const filePath of files) {
      const relativePath = toPosixPath(relative(skillRoot, filePath));
      const text = await readFile(filePath, "utf8");
      const frontmatter = parseFrontmatter(text);
      const id = resourceId(skillName, relativePath);
      entries.push({
        id,
        skill: skillName,
        path: relativePath,
        title: titleFor(relativePath, text, frontmatter),
        description: frontmatter.description ?? "",
        text,
        url: canonicalUrl(skillName, relativePath),
        digest: `sha256:${createHash("sha256").update(text, "utf8").digest("hex")}`,
      });
    }
  }

  const byId = new Map(entries.map((entry) => [entry.id, entry]));
  const byUrl = new Map(entries.map((entry) => [entry.url, entry]));
  return { entries, byId, byUrl };
}

async function getKnowledgeIndex() {
  knowledgeIndexPromise ??= buildKnowledgeIndex();
  return knowledgeIndexPromise;
}

function tokenize(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .split(/\s+/)
    .filter((token) => token.length > 1);
}

function searchEntries(entries, query) {
  const tokens = tokenize(query);
  if (!tokens.length) return [];

  return entries
    .map((entry) => {
      const title = entry.title.toLowerCase();
      const path = entry.path.toLowerCase();
      const haystack = entry.text.toLowerCase();
      let score = 0;
      for (const token of tokens) {
        if (title.includes(token)) score += 8;
        if (path.includes(token)) score += 4;
        const matches = haystack.match(new RegExp(token.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g"));
        score += Math.min(matches?.length ?? 0, 8);
      }
      return { entry, score };
    })
    .filter(({ score }) => score > 0)
    .sort((left, right) => right.score - left.score || left.entry.id.localeCompare(right.entry.id))
    .slice(0, 12)
    .map(({ entry }) => ({
      id: entry.id,
      title: entry.title,
      url: entry.url,
    }));
}

function standardContent(payload) {
  return {
    content: [{ type: "text", text: JSON.stringify(payload) }],
    structuredContent: payload,
  };
}

function textContent(text, structuredContent) {
  return {
    content: [{ type: "text", text }],
    structuredContent,
  };
}

function uniqueStrings(values = []) {
  return [...new Set(values.map((value) => String(value).trim()).filter(Boolean))];
}

function classifyOpportunity(input) {
  const systems = uniqueStrings(input.currentSystems);
  const channels = uniqueStrings(input.channels);
  const signals = [];
  const missingInputs = [];

  if (input.locationCount != null) {
    signals.push(`${input.locationCount} location(s) supplied`);
  } else {
    missingInputs.push("location count");
  }
  if (systems.length) signals.push(`systems named: ${systems.join(", ")}`);
  else missingInputs.push("current commerce and back-office stack");
  if (channels.length) signals.push(`channels named: ${channels.join(", ")}`);
  if (input.customerCount != null) signals.push(`${input.customerCount} customer records supplied`);
  if (input.skuCount != null) signals.push(`${input.skuCount} SKU count supplied`);
  if (input.b2b === true) signals.push("B2B or wholesale is in scope");
  if (input.specialOrders === true) signals.push("special orders are in scope");
  if (input.timelinePressure) signals.push(`timeline pressure: ${input.timelinePressure}`);

  const complex =
    (input.locationCount ?? 0) >= 10 ||
    systems.length >= 5 ||
    channels.length >= 4 ||
    (input.customerCount ?? 0) >= 100_000 ||
    (input.skuCount ?? 0) >= 50_000;
  const growing =
    complex ||
    (input.locationCount ?? 0) >= 3 ||
    systems.length >= 2 ||
    input.b2b === true ||
    input.specialOrders === true;
  const classification = complex
    ? "Complex Multi-Surface"
    : growing
      ? "Growing Multi-Location"
      : "Simple Retail";

  const enoughScopeEvidence =
    input.locationCount != null && systems.length > 0 && Boolean(input.notes?.trim());
  const recommendedLane = enoughScopeEvidence
    ? "Full implementation after a scoping call, with open assumptions carried into the SOW."
    : "Blueprint Diagnostic + Advisory or a paid scoping call before implementation pricing."

  if (!input.b2b && input.b2b !== false) missingInputs.push("whether B2B or wholesale is in scope");
  if (!input.specialOrders && input.specialOrders !== false) missingInputs.push("special-order workflow exposure");
  if (!input.timelinePressure) missingInputs.push("timeline pressure and target launch date");

  return {
    classification,
    complexitySignals: signals,
    recommendedLane,
    risks: [
      complex ? "Multiple systems or high data volume may put integration and migration on the critical path." : null,
      input.b2b ? "B2B company, price-list, payment, and ERP boundaries need explicit discovery." : null,
      input.specialOrders ? "Special-order state, vendor workflow, and customer communication need a named owner." : null,
      missingInputs.length ? "The missing inputs limit confidence in scope, timing, and architecture." : null,
    ].filter(Boolean),
    missingInputs: uniqueStrings(missingInputs),
    evidence: {
      confirmed: [
        "Only facts supplied in this tool call are treated as confirmed.",
        ...(input.notes?.trim() ? [input.notes.trim()] : []),
      ],
      inferred: [
        `Merchant profile classified as ${classification} from the supplied signals.`,
        "Commercial lane recommendation is a planning inference, not an approved quote.",
      ],
    },
  };
}

function buildArchitecture(input) {
  const systems = uniqueStrings(input.systems);
  const domains = uniqueStrings(input.domains?.length ? input.domains : ["catalog", "inventory", "orders", "customers", "pricing"]);
  const hasExternalMaster = systems.some((system) => /erp|wms|pim|oms|crm|netsuite|lightspeed|dynamics|sap/i.test(system));
  const sourceOfTruth = {};

  for (const domain of domains) {
    if (domain === "catalog") sourceOfTruth[domain] = hasExternalMaster ? "External catalog owner or Shopify, confirm ownership before build." : "Shopify, unless a named ERP/PIM owns catalog data.";
    else if (domain === "inventory") sourceOfTruth[domain] = hasExternalMaster ? "ERP/WMS allocation owner, with Shopify as an operational consumer where appropriate." : "Shopify locations and inventory, subject to replenishment and transfer requirements.";
    else if (domain === "orders") sourceOfTruth[domain] = input.b2b ? "Shopify for POS/DTC; ERP/OMS for wholesale or multi-surface orders." : "Shopify for POS/DTC, with accounting or ERP synchronization defined explicitly.";
    else if (domain === "customers") sourceOfTruth[domain] = systems.some((system) => /crm|cdp|hubspot|salesforce/i.test(system)) ? "CRM/CDP for enrichment and lifecycle; Shopify for commerce identity and purchase history." : "Shopify, with downstream CRM or marketing enrichment documented.";
    else if (domain === "pricing") sourceOfTruth[domain] = input.b2b || hasExternalMaster ? "ERP or Shopify B2B price-list owner, confirmed by contract-pricing discovery." : "Shopify price and discount rules.";
    else sourceOfTruth[domain] = "Ownership requires discovery before implementation.";
  }

  return {
    architectureType: input.locationCount >= 10 || systems.length >= 5 ? "Complex multi-surface commerce" : "Scope-dependent commerce system",
    sourceOfTruth,
    integrationWorkstreams: [
      "Confirm record ownership by domain before mapping fields or automations.",
      "Define one-way versus bidirectional synchronization and conflict handling.",
      "Separate migration scope from post-launch workflow and integration scope.",
      "Attach QA evidence to each critical data and operational handoff.",
    ],
    openQuestions: [
      "Which system owns each domain today?",
      "Which system is allowed to write the target record after launch?",
      "What happens when an upstream record is incomplete, duplicated, or late?",
      "Which store-team workflows must work on day one?",
    ],
    evidence: {
      confirmed: [
        ...(systems.length ? [`Systems supplied: ${systems.join(", ")}.`] : []),
        ...(domains.length ? [`Domains requested: ${domains.join(", ")}.`] : []),
      ],
      inferred: ["Source-of-truth recommendations are heuristics and require merchant confirmation."],
    },
  };
}

function assessMigration(input) {
  const entities = uniqueStrings(input.entities);
  const systems = uniqueStrings(input.currentSystems);
  const risks = [];
  const gates = [];
  const highExposure = entities.length >= 6 || (input.locationCount ?? 0) >= 10 || systems.length >= 3;

  if (entities.includes("customers")) risks.push({ area: "Customers", level: "medium", reason: "Deduplication, identity matching, consent, and historical ownership need evidence." });
  if (entities.includes("orders")) risks.push({ area: "Orders", level: "high", reason: "Historical orders, financial reporting, and fulfillment state are easy to mis-map." });
  if (entities.includes("inventory")) risks.push({ area: "Inventory", level: "high", reason: "Location mapping, available quantities, committed stock, and timing must reconcile." });
  if (entities.includes("companies") || entities.includes("price_lists")) risks.push({ area: "B2B", level: "high", reason: "Company, location, payment, and price-list relationships need a separate test pack." });
  if (input.dataQualityNotes?.trim()) risks.push({ area: "Data quality", level: "high", reason: input.dataQualityNotes.trim() });
  if (input.timelinePressure === "high") risks.push({ area: "Timeline", level: "high", reason: "Compressed cutover time reduces room for reconciliation and recovery." });
  if (!risks.length) risks.push({ area: "Discovery", level: "medium", reason: "Migration risk cannot be scored until entities, volumes, and ownership are confirmed." });

  gates.push("Freeze the migration entity map and source-of-truth decisions.");
  gates.push("Produce a representative export and run dedupe/validation checks.");
  gates.push("Complete a dry run with row counts, exceptions, and reconciliation evidence.");
  gates.push("Approve cutover, rollback, and post-cutover verification owners.");

  return {
    currentPlatform: input.currentPlatform,
    targetPlatform: input.targetPlatform ?? "Shopify",
    riskLevel: highExposure || risks.some((risk) => risk.level === "high") ? "high" : "medium",
    risks,
    gates,
    recommendedApproach: highExposure
      ? "Use an API-first migration package with a documented entity map, dry run, reconciliation, and cutover recovery path."
      : "Complete a scoped migration assessment before selecting API-first or Matrixify execution.",
    evidence: {
      confirmed: [
        `Current platform: ${input.currentPlatform}.`,
        ...(entities.length ? [`Entities supplied: ${entities.join(", ")}.`] : []),
      ],
      inferred: ["Risk level is inferred from the supplied entities, system count, location count, and stated pressure."],
    },
  };
}

function draftBlueprint(input) {
  const confirmedFacts = input.confirmedFacts.trim();
  const openQuestions = uniqueStrings(input.openQuestions);
  return {
    documentType: "Blueprint Diagnostic + Advisory",
    status: "Draft from supplied inputs",
    merchantName: input.merchantName?.trim() || "Unspecified merchant",
    sections: [
      { heading: "Executive summary", body: confirmedFacts || "[CONFIRMED] No confirmed facts supplied.", evidence: "confirmed input only" },
      { heading: "Current-state surfaces", body: "Map storefront, POS, inventory, orders, customers, B2B, integrations, and store-team workflows from confirmed discovery facts.", evidence: "structure to complete" },
      { heading: "Findings and risks", body: "Record each finding as Confirmed, Inferred, Assumed, or Estimated. Attach the evidence and the operational consequence.", evidence: "method guardrail" },
      { heading: "Decision path", body: "Recommend Blueprint/advisory or full implementation only after scope evidence, timing pressure, and open assumptions are visible.", evidence: "commercial guardrail" },
      { heading: "Launch plan", body: "Sequence data readiness, architecture, configuration, migration, QA, training, cutover, and first-seven-day support.", evidence: "delivery structure" },
    ],
    openQuestions: openQuestions.length ? openQuestions : ["Which facts still require merchant or vendor confirmation?"],
    guardrails: ["No invented pricing, ROI, capabilities, or merchant facts.", "This is a draft outline, not client-ready proof or an approved proposal."],
  };
}

function draftProposal(input) {
  const confirmedFacts = input.confirmedFacts.trim();
  const scope = uniqueStrings(input.scope);
  const assumptions = uniqueStrings(input.assumptions);
  const pricingProvided = Boolean(input.pricing?.trim());
  return {
    documentType: "Kaizen Commerce proposal draft",
    status: "Draft from supplied inputs",
    lane: input.lane,
    sections: [
      { heading: "Situation", body: confirmedFacts || "[CONFIRMED] Add the merchant's confirmed situation before sending.", evidence: "confirmed input only" },
      { heading: "Recommended path", body: input.lane === "unknown" ? "Run a scoping call or Blueprint/advisory diagnostic before committing to an implementation path." : `Proposed lane: ${input.lane}. Validate the lane against scope evidence before sending.`, evidence: "decision draft" },
      { heading: "Scope and deliverables", body: scope.length ? scope.join("; ") : "[ASSUMED] Define deliverables from the confirmed discovery record.", evidence: scope.length ? "supplied scope" : "missing input" },
      { heading: "Commercials", body: pricingProvided ? input.pricing.trim() : "[VERIFY] Pricing was not supplied. Load the pricing canon and confirm location count, stack, migration exposure, timeline pressure, and assumptions before quoting.", evidence: pricingProvided ? "supplied pricing" : "pricing intentionally absent" },
      { heading: "Assumptions and boundaries", body: assumptions.length ? assumptions.join("; ") : "[ASSUMED] Add explicit inclusions, exclusions, dependencies, and change-order triggers.", evidence: assumptions.length ? "supplied assumptions" : "missing input" },
    ],
    guardrails: ["Do not send this draft as a client deliverable until facts, pricing, scope, and proof are verified.", "Do not promise work that changes fee, timeline, or risk without scope authority."],
  };
}

function draftSow(input) {
  const inScope = uniqueStrings(input.inScope);
  const outOfScope = uniqueStrings(input.outOfScope);
  const assumptions = uniqueStrings(input.assumptions);
  const milestones = uniqueStrings(input.milestones);
  return {
    documentType: "Kaizen Commerce SOW draft",
    status: "Draft from supplied inputs",
    sections: [
      { heading: "Objective", body: input.objective?.trim() || "[CONFIRMED] Add the agreed business and operational objective." },
      { heading: "In scope", body: inScope.length ? inScope.join("; ") : "[VERIFY] No in-scope deliverables supplied." },
      { heading: "Out of scope", body: outOfScope.length ? outOfScope.join("; ") : "[VERIFY] Add explicit exclusions and change-order boundaries." },
      { heading: "Milestones", body: milestones.length ? milestones.join("; ") : "[VERIFY] Add milestone names, acceptance evidence, and owner responsibilities." },
      { heading: "Assumptions and dependencies", body: assumptions.length ? assumptions.join("; ") : "[VERIFY] Add merchant inputs, access, approvals, vendor dependencies, and data assumptions." },
    ],
    guardrails: ["This draft does not invent pricing, payment terms, dates, or acceptance criteria.", "Every scope change that affects fee, timeline, or risk requires the change-order path."],
  };
}

function registerWorkbenchResource(server) {
  server.registerResource(
    "kaizen-workbench",
    WORKBENCH_URI,
    {
      title: "Kaizen Commerce Workbench",
      description: "Versioned read-only interactive workbench for Kaizen Commerce deal, architecture, migration, and delivery drafts.",
      mimeType: WORKBENCH_MIME_TYPE,
      _meta: {
        ui: {
          prefersBorder: true,
          ...(UI_DOMAIN ? { domain: UI_DOMAIN } : {}),
          csp: {
            connectDomains: [],
            resourceDomains: [],
          },
        },
        "openai/widgetDescription": "A read-only Kaizen Commerce workbench for reviewing evidence, risks, architecture, scope, and draft delivery artifacts.",
      },
    },
    async () => ({
      contents: [
        {
          uri: WORKBENCH_URI,
          mimeType: WORKBENCH_MIME_TYPE,
          text: await getWorkbenchHtml(),
          _meta: {
            ui: {
              prefersBorder: true,
              ...(UI_DOMAIN ? { domain: UI_DOMAIN } : {}),
              csp: {
                connectDomains: [],
                resourceDomains: [],
              },
            },
            "openai/widgetDescription": "A read-only Kaizen Commerce workbench for reviewing evidence, risks, architecture, scope, and draft delivery artifacts.",
          },
        },
      ],
    }),
  );
}

function registerWorkbenchTool(server) {
  server.registerTool(
    "render_kaizen_workbench",
    {
      title: "Render Kaizen Workbench",
      description: "Use this after a data or draft tool has produced a model-checked result and the user needs an interactive Kaizen Workbench view. Choose the closest view and pass only the concise structured result; this tool renders read-only UI and performs no external action.",
      inputSchema: {
        view: z.enum(Object.keys(workbenchViewTitles)).default("deal_snapshot"),
        title: z.string().optional().describe("Optional merchant or workstream title shown in the workbench."),
        payload: z.record(z.string(), z.any()).default({}).describe("Concise structured result from a prior Kaizen tool call."),
      },
      outputSchema: {
        view: z.string(),
        title: z.string(),
        payload: z.record(z.string(), z.any()),
        stateVersion: z.number().int(),
        readOnly: z.boolean(),
      },
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        openWorldHint: false,
        idempotentHint: true,
      },
      _meta: {
        ui: { resourceUri: WORKBENCH_URI },
        "openai/outputTemplate": WORKBENCH_URI,
        "openai/toolInvocation/invoking": "Opening Kaizen Workbench",
        "openai/toolInvocation/invoked": "Kaizen Workbench ready",
      },
    },
    async ({ view, title, payload }) => {
      const resolvedView = view ?? "deal_snapshot";
      const resolvedTitle = title?.trim() || workbenchViewTitles[resolvedView] || "Kaizen Workbench";
      const stateVersion = ++workbenchStateVersion;
      const resolvedPayload = payload ?? {};
      return {
        content: [{ type: "text", text: `Rendered the read-only ${resolvedTitle} view in Kaizen Workbench.` }],
        structuredContent: {
          view: resolvedView,
          title: resolvedTitle,
          payload: resolvedPayload,
          stateVersion,
          readOnly: true,
        },
        _meta: {
          "openai/outputTemplate": WORKBENCH_URI,
          "openai/widgetDescription": "A read-only Kaizen Commerce workbench for reviewing evidence, risks, architecture, scope, and draft delivery artifacts.",
        },
      };
    },
  );
}

const kaizenOsOutputSchema = {
  ok: z.boolean(),
  status: z.number().int(),
  action: z.string(),
  dryRun: z.boolean(),
  idempotencyKey: z.string().nullable().optional(),
  data: z.any().optional(),
  error: z.string().optional(),
};

const kaizenOsSecuritySchemes = Object.freeze([
  Object.freeze({ type: "oauth2", scopes: [...KAIZEN_OAUTH_SCOPES] }),
]);

function registerKaizenOsTools(server, kaizenOsClient) {
  const securityByName = new Map();
  for (const definition of KAIZENOS_TOOL_DEFINITIONS) {
    const isWrite = definition.destructive === true;
    const safetyDescription = isWrite
      ? " Requires a signed-in KaizenOS account with the appropriate role. Preview with dryRun=true, show the exact proposed fields to the operator, wait for explicit approval, then commit the same payload with a unique idempotencyKey."
      : " Requires a signed-in KaizenOS account. Use this for live KaizenOS context; it does not change records.";

    server.registerTool(
      definition.name,
      {
        title: definition.title,
        description: `${definition.description}${safetyDescription}`,
        inputSchema: {
          input: z.record(z.string(), z.any()).default({}).describe(definition.inputDescription),
          idempotencyKey: z.string().min(1).optional().describe("Unique key for a committed write retry; omit it from the initial dry run."),
          dryRun: z.boolean().default(false).describe("When true, validate and preview without committing the KaizenOS change."),
        },
        outputSchema: kaizenOsOutputSchema,
        annotations: {
          readOnlyHint: !isWrite,
          destructiveHint: isWrite,
          idempotentHint: isWrite,
          openWorldHint: false,
        },
        // The current TypeScript SDK serializes unknown auth metadata under
        // _meta. attachToolSecuritySchemes() promotes this to the root-level
        // tools/list field required by ChatGPT while retaining the mirror for
        // older MCP hosts.
        _meta: { securitySchemes: kaizenOsSecuritySchemes },
      },
      async ({ input, idempotencyKey, dryRun }) => kaizenOsClient.call({
        definition,
        input: input ?? {},
        idempotencyKey,
        dryRun: dryRun === true,
      }),
    );
    securityByName.set(definition.name, kaizenOsSecuritySchemes);
  }
  return securityByName;
}

function attachToolSecuritySchemes(server, securityByName) {
  const handlers = server.server?._requestHandlers;
  const original = handlers?.get("tools/list");
  if (typeof original !== "function") {
    throw new Error("MCP SDK tools/list handler is unavailable; cannot publish OAuth tool metadata.");
  }
  // @modelcontextprotocol/sdk 1.30.0 stores securitySchemes in _meta but
  // ChatGPT expects the Apps SDK field at the root of each tool descriptor.
  // Wrap the SDK's own serializer so schemas and pagination remain intact.
  handlers.set("tools/list", async (request, extra) => {
    const result = await original(request, extra);
    return {
      ...result,
      tools: (result.tools ?? []).map((tool) => {
        const schemes = securityByName.get(tool.name);
        return schemes ? { ...tool, securitySchemes: schemes } : tool;
      }),
    };
  });
}

function registerTools(server) {
  server.registerTool(
    "search",
    {
      title: "Search Kaizen knowledge",
      description: "Use this when the user needs to find a Kaizen Commerce skill, reference, example, template, or operating rule. Search the packaged knowledge before making a canon-sensitive claim.",
      inputSchema: { query: z.string().min(1).describe("Plain-language search query") },
      outputSchema: {
        results: z.array(z.object({
          id: z.string(),
          title: z.string(),
          url: z.string(),
        })),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async ({ query }) => {
      const index = await getKnowledgeIndex();
      return standardContent({ results: searchEntries(index.entries, query) });
    },
  );

  server.registerTool(
    "fetch",
    {
      title: "Fetch Kaizen knowledge",
      description: "Use this after search when the user needs the full text of a specific Kaizen Commerce knowledge item. Pass the exact id returned by search.",
      inputSchema: { id: z.string().min(1).describe("Knowledge item id returned by search") },
      outputSchema: {
        id: z.string().optional(),
        title: z.string().optional(),
        text: z.string().optional(),
        url: z.string().optional(),
        metadata: z.object({
          skill: z.string().optional(),
          path: z.string().optional(),
          digest: z.string().optional(),
        }).optional(),
        error: z.string().optional(),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async ({ id }) => {
      const index = await getKnowledgeIndex();
      const entry = index.byId.get(id) ?? index.byUrl.get(id);
      if (!entry) return standardContent({ error: `Knowledge item not found: ${id}` });
      return standardContent({
        id: entry.id,
        title: entry.title,
        text: entry.text,
        url: entry.url,
        metadata: { skill: entry.skill, path: entry.path, digest: entry.digest },
      });
    },
  );

  server.registerTool(
    "analyze_opportunity",
    {
      title: "Analyze merchant opportunity",
      description: "Use this when the user provides merchant facts and wants a scope-first profile, risks, missing discovery inputs, or a Blueprint-versus-implementation lane recommendation. Treat the result as inference from supplied inputs, not live CRM data.",
      inputSchema: {
        merchantName: z.string().optional(),
        locationCount: z.number().int().min(1).optional(),
        currentSystems: z.array(z.string()).optional(),
        channels: z.array(z.string()).optional(),
        customerCount: z.number().int().min(0).optional(),
        skuCount: z.number().int().min(0).optional(),
        b2b: z.boolean().optional(),
        specialOrders: z.boolean().optional(),
        timelinePressure: z.enum(["low", "medium", "high"]).optional(),
        notes: z.string().optional(),
      },
      outputSchema: {
        classification: z.string(),
        complexitySignals: z.array(z.string()),
        recommendedLane: z.string(),
        risks: z.array(z.string()),
        missingInputs: z.array(z.string()),
        evidence: z.object({ confirmed: z.array(z.string()), inferred: z.array(z.string()) }),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async (input) => {
      const result = classifyOpportunity(input);
      return textContent(`Classified the supplied merchant facts as ${result.classification}.`, result);
    },
  );

  server.registerTool(
    "build_solution_architecture",
    {
      title: "Build solution architecture",
      description: "Use this when the user needs a first-pass Shopify, retail operations, B2B, or integration architecture from named systems and domains. It proposes ownership heuristics and open questions; it does not inspect live systems.",
      inputSchema: {
        systems: z.array(z.string()).min(1),
        domains: z.array(z.enum(["catalog", "inventory", "orders", "customers", "pricing", "fulfillment", "payments"])).optional(),
        locationCount: z.number().int().min(1).optional(),
        b2b: z.boolean().optional(),
        notes: z.string().optional(),
      },
      outputSchema: {
        architectureType: z.string(),
        sourceOfTruth: z.record(z.string(), z.string()),
        integrationWorkstreams: z.array(z.string()),
        openQuestions: z.array(z.string()),
        evidence: z.object({ confirmed: z.array(z.string()), inferred: z.array(z.string()) }),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async (input) => {
      const result = buildArchitecture(input);
      return textContent("Built a first-pass architecture from the supplied systems and domains.", result);
    },
  );

  server.registerTool(
    "assess_migration",
    {
      title: "Assess migration risk",
      description: "Use this when the user needs a migration risk assessment, entity map, QA gates, or a first-pass API-first versus spreadsheet/import recommendation. It does not connect to or modify a source or target platform.",
      inputSchema: {
        currentPlatform: z.string().min(1),
        targetPlatform: z.string().optional(),
        entities: z.array(z.enum(["products", "variants", "inventory", "customers", "orders", "locations", "companies", "price_lists", "discounts", "fulfillments"])).optional(),
        currentSystems: z.array(z.string()).optional(),
        locationCount: z.number().int().min(1).optional(),
        dataQualityNotes: z.string().optional(),
        timelinePressure: z.enum(["low", "medium", "high"]).optional(),
      },
      outputSchema: {
        currentPlatform: z.string(),
        targetPlatform: z.string(),
        riskLevel: z.enum(["medium", "high"]),
        risks: z.array(z.object({ area: z.string(), level: z.enum(["medium", "high"]), reason: z.string() })),
        gates: z.array(z.string()),
        recommendedApproach: z.string(),
        evidence: z.object({ confirmed: z.array(z.string()), inferred: z.array(z.string()) }),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async (input) => {
      const result = assessMigration(input);
      return textContent(`Migration assessment is ${result.riskLevel} risk based on the supplied inputs.`, result);
    },
  );

  server.registerTool(
    "generate_blueprint",
    {
      title: "Draft Blueprint outline",
      description: "Use this when the user wants a Blueprint Diagnostic + Advisory outline from confirmed discovery facts. Keep the output as a draft and preserve Confirmed, Inferred, Assumed, and Estimated labels.",
      inputSchema: {
        merchantName: z.string().optional(),
        confirmedFacts: z.string().min(1),
        openQuestions: z.array(z.string()).optional(),
      },
      outputSchema: {
        documentType: z.string(),
        status: z.string(),
        merchantName: z.string(),
        sections: z.array(z.object({ heading: z.string(), body: z.string(), evidence: z.string() })),
        openQuestions: z.array(z.string()),
        guardrails: z.array(z.string()),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async (input) => {
      const result = draftBlueprint(input);
      return textContent("Drafted a Blueprint outline from the supplied facts; no client-ready artifact was created.", result);
    },
  );

  server.registerTool(
    "generate_proposal",
    {
      title: "Draft proposal structure",
      description: "Use this when the user wants a proposal draft from confirmed facts, a selected commercial lane, scope, assumptions, and optionally supplied pricing. Never invent pricing or promise unsupported scope.",
      inputSchema: {
        confirmedFacts: z.string().min(1),
        lane: z.enum(["blueprint-advisory", "full-implementation", "unknown"]).default("unknown"),
        scope: z.array(z.string()).optional(),
        assumptions: z.array(z.string()).optional(),
        pricing: z.string().optional(),
      },
      outputSchema: {
        documentType: z.string(),
        status: z.string(),
        lane: z.string(),
        sections: z.array(z.object({ heading: z.string(), body: z.string(), evidence: z.string() })),
        guardrails: z.array(z.string()),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async (input) => {
      const result = draftProposal(input);
      return textContent("Drafted a proposal structure; pricing and scope still require canon and evidence checks.", result);
    },
  );

  server.registerTool(
    "generate_sow",
    {
      title: "Draft SOW structure",
      description: "Use this when the user wants a statement-of-work draft from an agreed objective, inclusions, exclusions, assumptions, and milestones. It does not create, send, or approve a contract.",
      inputSchema: {
        objective: z.string().optional(),
        inScope: z.array(z.string()).optional(),
        outOfScope: z.array(z.string()).optional(),
        assumptions: z.array(z.string()).optional(),
        milestones: z.array(z.string()).optional(),
      },
      outputSchema: {
        documentType: z.string(),
        status: z.string(),
        sections: z.array(z.object({ heading: z.string(), body: z.string() })),
        guardrails: z.array(z.string()),
      },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    },
    async (input) => {
      const result = draftSow(input);
      return textContent("Drafted an SOW structure; scope authority and commercial review are still required.", result);
    },
  );
}

export function createKaizenServer(options = {}) {
  const kaizenOsClient = options.kaizenOsClient ?? createKaizenOsClient({
    authorization: options.kaizenOsAuthorization,
    hosted: options.hostedRequest === true,
    oauthResourceMetadataUrl: options.oauthResourceMetadataUrl,
  });
  const server = new McpServer(
    { name: SERVER_NAME, version: SERVER_VERSION },
    {
      instructions:
      "Kaizen Commerce combines the packaged Kai canon with a bounded KaizenOS operator adapter. Search and fetch canon before making canon-sensitive claims. KaizenOS is the live source of truth for CRM and delivery records when a caller has linked a KaizenOS account through OAuth or supplied a private personal key. OAuth identity maps to the signed-in KaizenOS profile; member/admin profiles can write, while viewer profiles remain read-only. For every write, read the current record first, preview with dryRun=true, show the exact proposed fields, wait for explicit approval, then commit the same payload with a unique idempotencyKey. Anonymous hosted requests cannot access live records or commit writes. Never invent pricing, live records, vendor capabilities, or connector actions.",
    },
  );
  registerWorkbenchResource(server);
  registerTools(server);
  const securityByName = registerKaizenOsTools(server, kaizenOsClient);
  attachToolSecuritySchemes(server, securityByName);
  registerWorkbenchTool(server);
  return server;
}

function setCorsHeaders(response) {
  response.setHeader("Access-Control-Allow-Origin", "*");
  response.setHeader("Access-Control-Allow-Headers", "Authorization, Content-Type, MCP-Session-Id, Last-Event-ID, MCP-Protocol-Version");
  response.setHeader("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS");
  response.setHeader("Access-Control-Expose-Headers", "MCP-Session-Id, MCP-Protocol-Version, WWW-Authenticate");
  response.setHeader("X-Content-Type-Options", "nosniff");
}

function readJsonBody(request) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let totalBytes = 0;
    let settled = false;
    request.on("data", (chunk) => {
      if (settled) return;
      totalBytes += chunk.length;
      if (totalBytes > MAX_JSON_BODY_BYTES) {
        settled = true;
        request.pause();
        const error = new Error(`Request body exceeds ${MAX_JSON_BODY_BYTES} bytes.`);
        error.statusCode = 413;
        reject(error);
        return;
      }
      chunks.push(chunk);
    });
    request.on("end", () => {
      if (settled) return;
      settled = true;
      const raw = Buffer.concat(chunks).toString("utf8");
      if (!raw.trim()) return resolve(undefined);
      try {
        resolve(JSON.parse(raw));
      } catch (error) {
        reject(new Error(`Invalid JSON body: ${error.message}`));
      }
    });
    request.on("error", (error) => {
      if (settled) return;
      settled = true;
      reject(error);
    });
  });
}

function jsonError(response, status, message) {
  if (response.headersSent) return;
  response.statusCode = status;
  response.setHeader("Content-Type", "application/json");
  response.end(JSON.stringify({ jsonrpc: "2.0", error: { code: -32000, message }, id: null }));
}

async function startHttpServer() {
  const transports = new Map();
  const servers = new Map();

  const handlePost = async (request, response, body) => {
    const sessionId = request.headers["mcp-session-id"];
    let transport = sessionId ? transports.get(sessionId) : undefined;

    if (!transport && !sessionId && isInitializeRequest(body)) {
      let server;
      transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: () => randomUUID(),
        onsessioninitialized: (newSessionId) => {
          transports.set(newSessionId, transport);
          servers.set(newSessionId, server);
        },
      });
      transport.onclose = () => {
        const closedSessionId = transport.sessionId;
        if (closedSessionId) {
          transports.delete(closedSessionId);
          servers.delete(closedSessionId);
        }
        void server?.close();
      };
      server = createKaizenServer({
        hostedRequest: true,
        kaizenOsAuthorization: Array.isArray(request.headers.authorization)
          ? request.headers.authorization[0]
          : request.headers.authorization,
        oauthResourceMetadataUrl: `http://${request.headers.host ?? `${HOST}:${PORT}`}/.well-known/oauth-protected-resource`,
      });
      await server.connect(transport);
    }

    if (!transport) {
      jsonError(response, 400, "Missing or invalid MCP session. Send initialize first.");
      return;
    }
    await transport.handleRequest(request, response, body);
  };

  const httpServer = createHttpServer(async (request, response) => {
    setCorsHeaders(response);
    if (request.method === "OPTIONS") {
      response.statusCode = 204;
      response.end();
      return;
    }
    if (request.url === "/healthz") {
      response.setHeader("Content-Type", "application/json");
      response.end(JSON.stringify({ status: "ok", server: SERVER_NAME, version: SERVER_VERSION }));
      return;
    }
    if (request.url !== "/mcp") {
      response.statusCode = 404;
      response.end("Not found");
      return;
    }

    try {
      if (request.method === "POST") {
        await handlePost(request, response, await readJsonBody(request));
        return;
      }
      const sessionId = request.headers["mcp-session-id"];
      const transport = sessionId ? transports.get(sessionId) : undefined;
      if (!transport) {
        jsonError(response, 400, "Missing or invalid MCP session.");
        return;
      }
      if (request.method === "GET" || request.method === "DELETE") {
        await transport.handleRequest(request, response);
        return;
      }
      response.statusCode = 405;
      response.setHeader("Allow", "GET, POST, DELETE, OPTIONS");
      response.end("Method not allowed");
    } catch (error) {
      console.error("MCP request failed:", error);
      jsonError(response, error.statusCode ?? 500, error.statusCode === 413 ? error.message : "Internal MCP server error");
    }
  });

  httpServer.listen(PORT, HOST, () => {
    console.error(`Kaizen Knowledge MCP server listening on http://${HOST}:${PORT}/mcp`);
  });

  const shutdown = async () => {
    for (const transport of transports.values()) await transport.close();
    httpServer.close();
  };
  process.once("SIGINT", () => void shutdown());
  process.once("SIGTERM", () => void shutdown());
}

async function startStdioServer() {
  const server = createKaizenServer();
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

const isMainModule = process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url;

if (isMainModule) {
  if (process.argv.includes("--http") || process.env.MCP_TRANSPORT === "http") {
    await startHttpServer();
  } else {
    await startStdioServer();
  }
}
