# Kaizen Routing Index

Load this file when selecting which Kai skill, reference, scenario variant, or example should drive
the current task. Search it with exact user words first, then fall back to the trigger
disambiguation rules.

## Route Decision Block

When routing is non-trivial, decide with this compact block before loading deep context:

```yaml
mode: Quick Read | Operator Analysis | Client Deliverable | Execution Artifact
primary_skill: skills/<file>.md | none
supporting_refs: []
scenario_variant: variants/<file>.md | none
examples: []
mcp_required: Shopify Dev MCP | Exa MCP | AnyDB MCP | Matrixify MCP | none
delegation_allowed: local_only | subagents_if_explicit | antigravity_if_explicit
```

## Skill Routing

When the user describes what they need, read the relevant skill file from the `skills/` directory
and follow its complete instructions before generating output.

| User says | Read this skill file |
|---|---|
| "New Deal", "New Deal: [merchant]", "Sync Client", "Prep Call", "Post Call Update", "Build Blueprint", "Build Proposal", "Use Delivery OS", "Run Pack 1", "Use Pack 5", "Shopify Referral Scope Brief", "Start Delivery", "Onboard Client", "Migration Package", "Migration QA", "Delegate to Antigravity", "Resume Client", "Kai Status", "Kai Doctor", "Start My Day", "End My Day", "Weekly Review", "Evidence Research", "Kai Priorities", "Review Workspace", "Close Client" | `reference/kaizen-command-palette.md` |
| "Start My Day", "End My Day", "Weekly Review", "Kai Status", "Kai Doctor", "Kai Priorities", "begin my day", "wrap my day", "what should I work on" | `reference/kaizen-command-palette.md` (Category: Daily, Status, And Priorities) |
| "New Deal", "Sync Client", "Prep Call", "Post Call Update", "Build Blueprint", "Build Proposal", "Use Delivery OS", "Run Pack 1", "Use Pack 5", "Shopify Referral Scope Brief", "Start Delivery", "Onboard Client", "Resume Client", "catch me up on", "process these notes" | `reference/kaizen-command-palette.md` (Category: Pipeline And Client Intake) |
| "Migration Package", "Migration QA", "Evidence Research", "Review Workspace", "Log Win", "Close Client", "go-live verdict", "closeout" | `reference/kaizen-command-palette.md` (Category: Execution, QA, And Closeout) |
| "Vendor Freshness Check", "Update Kai Vendor Knowledge", "Check Shopify Freshness", "Check AnyDB Freshness", "update Shopify changelog", "AnyDB releases" | `reference/kaizen-command-palette.md` + `reference/kaizen-vendor-freshness-protocol.md` |
| "Vendor Freshness Check", "Update Kai Vendor Knowledge", "Check Shopify Freshness", "Check AnyDB Freshness", "freshness gate", "operating hook" | `reference/kaizen-command-palette.md` (Category: Vendor Freshness And Operating Hooks) |
| "current Shopify", "current AnyDB", "verify platform behavior", "evidence gate", "proof before sending", "follow-up tasks", "next steps from notes", "account health", "expansion signal", "churn risk", "QBR" | `reference/kaizen-operating-hook-protocols.md` + relevant primary skill |
| "write a cold email", "outreach to [prospect]", "follow up with", "LinkedIn DM" | `skills/kaizen-outreach.md` |
| "prep me for a call", "discovery questions", "I have a call with..." | `skills/kaizen-qualify.md` |
| "write the Blueprint report", "findings report", "diagnostic" | `skills/kaizen-diagnose.md` |
| "write a proposal", "generate proposal" | `skills/kaizen-propose.md` + `reference/kaizen-pdf-template-system.md` + `assets/templates/kaizen-proposal-template.pdf` |
| "create SOW", "generate SOW", "Statement of Work" | `skills/kaizen-propose.md` or `skills/kaizen-invoice-exec.md` + `reference/kaizen-pdf-template-system.md` + `assets/templates/kaizen-sow-template.html` |
| "tight SOW", "SOW governance", "prevent scope creep", "write exclusions", "what is not included", "scope boundaries" | `skills/kaizen-scope.md` + `skills/kaizen-propose.md` or `skills/kaizen-invoice-exec.md` as needed |
| "Use Delivery OS", "Delivery OS", "POS wedge", "multi-location POS transformation", "run the POS wedge", "run Delivery OS for" | `delivery-os/README.md` |
| "Run Pack 1", "Blueprint Diagnostic Pack", "Engagement Baseline", "build the Engagement Baseline", "approved Baseline" | `delivery-os/01-blueprint-diagnostic-pack.md` + `delivery-os/templates/engagement-baseline.md` |
| "Shopify Referral Scope Brief", "Referral Scope Brief", "Shopify Referral Baseline", "AE referred this merchant", "Shopify referral exception" | `delivery-os/templates/shopify-referral-scope-brief.md` + `delivery-os/templates/engagement-baseline.md` |
| "Mixed Commerce Systems Baseline Brief", "Mixed Commerce Baseline", "multi-surface baseline", "cross-surface source of truth" | `delivery-os/templates/mixed-commerce-baseline-brief.md` + `delivery-os/templates/engagement-baseline-mixed-extension.md` |
| "Use Pack 5", "Sales / SOW Pack", "audit against Pack 5", "Pack 5 proposal", "Pack 5 SOW" | `delivery-os/05-sales-sow-pack.md` + `delivery-os/templates/sow-boundaries.md` |
| "Shopify SE referral one-pager", "SE one-pager", "AE referral one-pager", "partner referral one-pager" | `delivery-os/templates/se-referral-one-pager.md` + `delivery-os/05-sales-sow-pack.md` |
| "start delivery", "kick off", "onboard", "project kickoff", "start the engagement", "first seven days" | `reference/kaizen-client-journey.md` + `skills/kaizen-onboard.md` |
| "Shopify DTC", "DTC commerce", "online store architecture", "storefront architecture", "customer accounts", "checkout architecture", "Shopify B2B", "wholesale portal", "B2B catalogs", "price lists", "payment terms", "company locations" | `reference/kaizen-shopify-commerce-systems.md` + route by output type to `skills/kaizen-qualify.md`, `skills/kaizen-diagnose.md`, `skills/kaizen-propose.md`, or `skills/kaizen-architect.md` |
| "AnyDB spec", "architecture doc", "integration mapping", "build SOPs" | `skills/kaizen-architect.md` + `reference/kaizen-anydb-patterns.md` |
| "AnyDB formula syntax", "what field type should this be", "AnyDB cell type", "formula", "AnyDB cell format", "attach vs reference", "how do I write this rollup", "rollup" | `reference/kaizen-anydb-patterns.md` |
| "build a Flow", "Shopify Flow workflow", "automate this in Flow" | `skills/kaizen-flow.md` |
| "clean this export", "prep for API import", "prep for Matrixify", "audit this CSV", "map these columns", "make this migration-ready" | `skills/kaizen-dataprep.md` |
| "review the products", "catalog review", "is this ready for import", "retail readiness check", "catalog audit" | `skills/kaizen-catalog-review.md` |
| "Square migration", "Square to Shopify", "Square export", "Square to Matrixify", "transform Square CSV" | `skills/kaizen-square-migration.md` |
| "migration runbook", "cutover plan", "field mapping", "migration lane", "Matrixify", "Kaizen Cutover", "Shadow Pilot Store Verdict Gate Waves Hypercare" | `skills/kaizen-migrate.md` + `reference/kaizen-cutover-methodology.md` |
| "check the Dry Run", "API job logs", "GraphQL response", "retry file", "import errors", "what failed", "parse the import results" | `skills/kaizen-validate.md` |
| "reconcile the data", "compare legacy to Shopify", "post-cutover check" | `skills/kaizen-reconcile.md` |
| "load data into AnyDB", "seed the system", "populate AnyDB" | `skills/kaizen-anydb-dataload.md` |
| "audit the AnyDB build", "does build match spec", "QA the ops system" | `skills/kaizen-anydb-audit.md` |
| "training plan", "staff training", "quick reference guide", "training schedule" | `skills/kaizen-training.md` |
| "hardware plan", "hardware spec", "network assessment", "device setup" | `skills/kaizen-hardware.md` |
| "change order", "scope change", "over the cap", "out of scope", "overage" | `skills/kaizen-scope.md` |
| "health check", "retainer pitch", "case study", "testimonial", "upsell" | `skills/kaizen-report.md` |
| "LinkedIn carousel", "pitch deck", "presentation", "PPTX", "slide deck", "clean up the voice" | `skills/kaizen-publish.md`; for PPTX/deck requests also load `assets/templates/kaizen-pitch-deck-template.pptx`, `reference/kaizen-pptx-design-system.md`, `examples/kaizen-pitch-deck-example.pptx`, and `examples/kaizen-pitch-deck-example.md` |
| "Blueprint Advisory", "Silver tier document", "blueprint PDF", "render the blueprint" | `skills/kaizen-render.md` + `reference/kaizen-pdf-template-system.md` + `assets/templates/kaizen-proposal-template.pdf` + `examples/kaizen-blueprint-advisory-example.pdf` + `examples/kaizen-blueprint-advisory-example.md` |
| "pipeline review", "deal scoring", "ARR forecast", "weekly dashboard" | `skills/kaizen-pipeline.md` |
| "Sales OS", "sales operating system", "sales stages", "proposal readiness", "AE referral lane", "CRM source of truth", "sales handoff" | `reference/kaizen-sales-os.md` |
| "utilization", "should I hire", "do we have capacity", "bench", "profit per engineer", "margin on this engagement", "leverage ratio", "blended rate", "value pricing", "are we pricing right", "firm economics", "can we afford to", "rate card", "billable target" | `skills/kaizen-firm-economics.md` |
| "productize", "package this offer", "turn this into a repeatable service", "make this a fixed-scope offer", "build an accelerator", "reusable asset", "stop doing this custom", "standardize this delivery", "should this be a product", "decouple revenue from hours", "sales posture", "stop competing on price", "we keep getting out-bid" | `skills/kaizen-productize.md` |
| "partner strategy", "co-sell", "Shopify partner", "become a Plus partner", "nearbound", "ISV alliance", "referral partner", "overlap accounts", "channel strategy", "who should we partner with", "app partnerships", "ecosystem growth" | `skills/kaizen-partner-ecosystem.md` |
| "research this merchant", "who is [company]", "what's their tech stack" | `skills/kaizen-research.md` |
| "save client context", "update client profile", "what do we know about [client]", "catch me up on [client]", "process these notes", "save this to [client] memory" | `reference/kaizen-memory-hook-protocol.md` + `skills/kaizen-memory.md` |
| "validate this deliverable", "check the proposal", "QA before sending" | `skills/kaizen-check.md` |
| "run competence evals", "test Kai quality", "quality regression", "judgment eval", "output quality eval", "run Kai evals" | Dev-layer activity — suites live in the source repo's dev-only maintenance layer, run from a dev checkout (never shipped). Deliverable scoring rubrics: `reference/kaizen-judgment-rubrics.md` |
| "render as PDF", "styled document", "generate Google Doc" | `skills/kaizen-render.md` |
| "generate import file", "create CSV", "AnyDB build config", "sample data" | `skills/kaizen-generate.md` |
| "content calendar", "what should I post", "repurpose this for LinkedIn" | `skills/kaizen-content-calendar.md` |
| "engagement P&L", "monthly financials", "pricing analysis", "revenue forecast" | `skills/kaizen-finance.md` |
| "API migration", "API-to-API migration", "batch ETL", "payload prep", "Admin API import", "build the migration package", "produce the migration files", "migration package" | `skills/kaizen-api-migration-exec.md` |
| "build the Matrixify import", "generate Matrixify files", "produce Matrixify CSVs", "transform this export into Matrixify format" | `skills/kaizen-matrixify-exec.md` |
| "build the AnyDB system", "generate schema config", "seed data for AnyDB" | `skills/kaizen-anydb-build.md` |
| "build the Flow workflows", "create the automations", "automation package" | `skills/kaizen-flow-build.md` |
| "write the follow-up", "detailed recap", "post-discovery email", "post-Blueprint summary", "post-proposal follow-up", "kickoff recap" | `skills/kaizen-followup.md` |
| "draft the emails", "write the cold sequence", "follow-up email" | `skills/kaizen-email-exec.md` |
| "generate SOW", "create invoice", "change order document" | `skills/kaizen-invoice-exec.md` |
| "configure Shopify", "location setup", "staff permissions", "Smart Grid" | `skills/kaizen-shopify-config.md` |
| "test scripts", "Dry Run config", "transaction testing", "hardware validation" | `skills/kaizen-test-exec.md` |
| "generate the health check", "build the case study", "retainer pitch deck" | `skills/kaizen-report-exec.md` |
| "ops health report", "operations health report", "monthly health report", "run the health report", "live store health check", "check [client]'s store health", "store health pull" | `skills/kaizen-ops-health-report.md` (live Shopify MCP pull) + `reference/kaizen-mcp-protocols.md` |
| "set up a retainer", "what retainer", "managed integration retainer", "AnyDB retainer", "Ops Care retainer", "recurring revenue", "attach a retainer", "retainer products", "retainer attach" | `reference/kaizen-retainer-architecture.md` + `reference/kaizen-pricing.md` |
| "run the engagement", "run Silver for [client]", "orchestrate", "resume [client]" | `skills/kaizen-orchestrate.md` |
| "skill graph", "upstream downstream", "upstream and downstream skills", "adjacent skills", "workflow skills", "which skills connect", "operations-manager with Kai" | `reference/kaizen-skill-graph.md` |
| "cross-skill pairing", "skill pairing architecture", "all my skills", "pair my skills with Kai", "CKM with Kai", "CE with Kai", "elevate KaizenCommerce with my skills" | `reference/kaizen-cross-skill-pairing-architecture.md` |
| Any POS, retail, inventory, warehouse, merchandising, fulfillment question | `skills/kaizen-retail-expert-v2.md` (routes to `skills/kaizen-reference/` by domain) |
| General KaizenCommerce question (pricing, positioning, strategy) | Load the matching `reference/` file (see Reference Files table below) |
| "source of truth", "build vs buy", "what should Shopify own", "native vs third-party", "which systems to keep" | `skills/kaizen-architect.md` router + `skills/kaizen-architect.md` Mode 2 + `reference/kaizen-build-vs-buy.md` + `reference/kaizen-surface-complexity.md` |
| "operational maturity", "is this team ready for Shopify", "how much support will they need", "post-launch ownership" | `reference/kaizen-operational-readiness.md` + `skills/kaizen-diagnose.md` |
| "enterprise migration", "multi-surface merchant", "20+ locations", "ERP integration", "which ERP connector" | `skills/kaizen-architect.md` router + `skills/kaizen-architect.md` Mode 2 + `reference/kaizen-surface-complexity.md` + `reference/kaizen-erp-patterns.md` |
| "Lightspeed migration", "Heartland migration", "Clover migration", "Revel migration", "Teamwork migration", "BigCommerce migration", "WooCommerce migration" | `reference/kaizen-platform-migrations.md` + `skills/kaizen-dataprep.md` |
| "risk register", "what can go wrong", "cutover risks", "ERP risks" | `reference/kaizen-risk-matrix.md` |
| "how mature is this merchant", "classify the merchant", "what profile is this" | `reference/kaizen-surface-complexity.md` + `reference/kaizen-operational-readiness.md` |

**Routing behavior:** When the user's message matches a trigger pattern above, read the matching
skill file from the `skills/` directory and follow its complete instructions before generating
output. For general background questions that don't match a specific skill, load the relevant
file from `reference/` instead of answering from memory.

## Reference Files — load on demand

The reference files below carry the deep background that used to live inline in this brain.
Load a reference file when the current task needs that body of knowledge — not by default.

| When you need... | Read this |
|---|---|
| Company identity, partners, service pillars, ICP, growth targets | `reference/kaizen-identity.md` |
| Full tier deliverables, retainer scope, overage language | `reference/kaizen-pricing.md` |
| Recurring-revenue model: service-module catalog, the three retainer products (Managed Integration, AnyDB Operations, Ops Care), pass-through integration economics, land-and-expand map, attach metrics, anti-selection | `reference/kaizen-retainer-architecture.md` |
| Sales methodology, Doctor Diagnosis, objection handling, revenue sequence | `reference/kaizen-sales-os.md` |
| Sales operating layer: stages, gates, AnyDB CRM/project source, AE referrals, proposal readiness, follow-up cadence | `reference/kaizen-sales-os.md` |
| Productized client journey: activation conditions, KaizenOS-derived handover, first seven days, delivery phases, and closeout | `reference/kaizen-client-journey.md` |
| Named POS cutover method, Shadow / Pilot Store / Verdict Gate / Waves / Hypercare, controlled launch promise | `reference/kaizen-cutover-methodology.md` |
| POS Delivery OS wedge: Engagement Baseline, Shopify Referral Scope Brief, Pack 1, Pack 5, pack QA | `delivery-os/README.md` |
| Data freshness defaults, source-of-truth heuristics | `reference/kaizen-data-freshness.md` |
| Vendor changelog freshness, generated Shopify/AnyDB index, stale-platform fail gates | `reference/kaizen-vendor-freshness-protocol.md` + `reference-content/` |
| Curated platform changes that move a Kaizen recommendation: Scripts shutdown, feature previews (physical inventory/bins, market-driven shipping, inventory transfers), POS UI extension breaking changes, B2B and admin changes | `reference/kaizen-platform-change-radar.md` |
| Context load budgets, load profiles, and oversized-skill load contracts | `reference/kaizen-context-load-profiles.md` |
| Pricing usage, pricing drift detection, and source-of-truth pricing boundaries | `reference/kaizen-pricing.md`, `reference/kaizen-pricing-usage-standard.md` |
| Firm-building strategy: utilization, bench, first hire, productized offers, reusable IP, value pricing, partner ecosystem, co-sell | `reference/kaizen-firm-strategy.md` |
| Runtime portability for Codex, chat-only, and external-agent execution | `reference/kaizen-runtime-portability.md` |
| Shopify DTC/B2B commerce systems, AnyDB-first commerce lens, non-POS fit rules | `reference/kaizen-shopify-commerce-systems.md` |
| Brand tokens, colors, document footer, DS v2 light/dark mode, typography, component specs, token audit allowlist | `reference/kaizen-ds-v2.html` + `reference/kaizen-design-system.md` + `reference/kaizen-design-tokens.json` |
| Full pipeline architecture diagram, skill category map | `reference/kaizen-skill-graph.md` |
| Compact skill graph with upstream, downstream, adjacent skills, ownership boundaries, and workflow pairings | `reference/kaizen-skill-graph.md` |
| Full catalog of documented skill-pair combinations | `reference/kaizen-composition.md` |
| Cross-skill pairing architecture across installed Codex skills, CKM, CE, operations, marketing, CRO, and support utilities | `reference/kaizen-cross-skill-pairing-architecture.md` |
| Antigravity CLI delegation recommendations, task contract, review flow, token economics | `reference/kaizen-antigravity-delegation.md` |
| Merchant profile classification (Simple Retail / Growing Multi-Location / Complex Multi-Surface), source-of-truth decisions by domain | `reference/kaizen-surface-complexity.md` |
| 4-verdict decision framework for every system: NATIVE / THIRD-PARTY / CUSTOM BUILD / RETAIN & INTEGRATE | `reference/kaizen-build-vs-buy.md` |
| Operational maturity scoring (Emerging/Established/Advanced), SI dependency, retainer tier positioning | `reference/kaizen-operational-readiness.md` |
| Signal inference chains — auto-resolve ERP/accounting/loyalty/WMS from confirmed platform signals | `reference/kaizen-signal-inference.md` |
| Unified risk matrix (standard, POS, ERP conditional, B2B conditional, operational readiness) | `reference/kaizen-risk-matrix.md` |
| Platform-specific migration data model notes (Lightspeed, Heartland, Clover, Revel, Teamwork, BigCommerce, WooCommerce, Shopify→Shopify) | `reference/kaizen-platform-migrations.md` |
| ERP connector patterns, source-of-truth matrix, data flow specs, Last 10% edge cases (NetSuite, QuickBooks, SAP B1, D365 BC, SAP S/4HANA, Sage) | `reference/kaizen-erp-patterns.md` |
| AnyDB cell types, formula syntax, cell formats, connection rules, canonical formulas, validation rules | `reference/kaizen-anydb-patterns.md` |
| Scenario-level output contracts for common Kai recommendations | `reference/kaizen-scenario-output-contracts.md` |
| Recommendation confidence levels, evidence registers, and kill-condition patterns | `reference/kaizen-recommendation-confidence.md` |
| Kai regression/eval suites, move maps, audit synthesis | Dev-only maintenance layer in the source repo — never shipped, never loaded at runtime |
| V3 context threat model and mitigation map | `reference/kaizen-context-threat-model.md` |
| Shared Kaizen specialist subagent registry | `reference/kaizen-specialist-registry.md` |
| Unified MCP source-of-truth protocols | `reference/kaizen-mcp-protocols.md` |
| Full voice and stop-slop rules | `reference/kaizen-voice.md` |
| Operating rules, pricing snapshot, precedence, gotchas, and recovery | `reference/kaizen-operating-rules.md` |
| Antigravity vs subagent vs local execution decision map | `reference/kaizen-skill-graph.md` |
| KaizenOS record ownership, command-to-tool sequences, agent write discipline | `reference/kaizen-kaizenos-integration-map.md` |
| Canadian sales tax (GST/HST/QST/PST), Quebec Bill 96 / French-language obligations, Interac/POS payment behavior, CAD payouts | `reference/kaizen-canada-retail-compliance.md` |
| Persistent client memory, memory scripts, Antigravity/Kai `memory_delta.json`, auto-recall, and approval-gated memory updates | `reference/kaizen-memory-architecture.md`, `reference/kaizen-memory-hook-protocol.md` |
| Soft hooks for vendor freshness, evidence gates, proposed follow-up tasks, and account health/expansion checks | `reference/kaizen-operating-hook-protocols.md` |
| Operator command workflows such as New Deal, Kai Doctor, Start My Day, Evidence Research, Kai Priorities, Review Workspace, Close Client, task ledger, and next command suggestions | `reference/kaizen-command-palette.md` (category sections inline; full contract in `reference/kaizen-command-palette-contract.md`) |

The compact pricing snapshot lives in `reference/kaizen-operating-rules.md`. Load the full
`reference/kaizen-pricing.md` only when producing a proposal, change order, invoice, or
engagement P&L.

## Scenario Variants — load on demand

Use a variant when the request matches a repeatable agency scenario and Kai needs the default
skill chain, output shape, risks, and anti-selection rules. Do not load variants for simple
Quick Read answers.

| Scenario | Read this |
|---|---|
| POS migration from Lightspeed, Square, Clover, Heartland, Revel, Teamwork, or similar | `variants/pos-migration.md` |
| WooCommerce, BigCommerce, Magento, custom ecommerce, or Shopify-to-Shopify migration | `variants/ecommerce-to-shopify.md` |
| Shopify DTC, online-store architecture, checkout/customer-account architecture, app-stack cleanup, or DTC operating model | `variants/shopify-dtc-commerce.md` |
| Shopify B2B, wholesale, dealer portal, company-specific pricing, catalogs, payment terms, or account-order workflow | `variants/shopify-b2b-commerce.md` (depth: `skills/kaizen-reference/kaizen-ref-b2b.md`) |
| B2B plan capability, catalog limits, deposits, partial payments, company/location modeling, B2B migration entities, or native-versus-operating-layer boundary | `skills/kaizen-reference/kaizen-ref-b2b.md` |
| AnyDB operations workflow, approval layer, vendor portal, or back-office build | `variants/anydb-operations-build.md` |
| ERP, accounting, WMS, 3PL, or connector-heavy retail architecture | `variants/erp-connected-retail.md` |
| Failed, blocked, over-scope, or mismatched migration | `variants/migration-rescue.md` |
| Square source migration execution detail | `variants/migration-square.md` |
| Lightspeed R-Series or X-Series source migration execution detail | `variants/migration-lightspeed.md` |
| Magento 2 / Adobe Commerce source migration execution detail | `variants/migration-magento2.md` |
| WooCommerce source migration execution detail | `variants/migration-woocommerce.md` |
| API lane execution config, pipelines, idempotency, retry queues | `variants/migration-lane-api-first.md` |
| Matrixify lane execution config, sheets, import modes, dry runs | `variants/migration-lane-matrixify.md` |
| API recipe, mutation reference, scopes, verified Shopify operations | `reference/kaizen-api-recipe-bank.md` |
| Migration QA evidence, reconciliation verdict, count parity sign-off | `delivery-os/templates/migration-qa-evidence-pack.md` |
| Fitness franchise, studio brand, membership + retail mix | `variants/vertical-fitness-franchise.md` |
| Jewelry retailer, serialized inventory, repairs, custom orders | `variants/vertical-jewelry-multilocation.md` |
| Food producer, specialty food, lot tracking, wholesale + retail mix | `variants/vertical-food-producer.md` |
| Kitchen, home goods, furniture, special orders, dropship, delivery | `variants/vertical-kitchen-home.md` |
| "en français", "in French", francophone merchant, French outreach or summary | `variants/fr-ca-mode.md` + `reference/kaizen-fr-ca-glossary.md` |
| Competing agency, enterprise SI, "they have a cheaper quote", DIY comparison, competitive positioning | `reference/kaizen-competitive-positioning.md` |
| Proposal or SOW direction after a completed Blueprint or approved POS Delivery OS Engagement Baseline | `variants/post-blueprint-proposal.md` |
| Post-launch health check, retainer, case study, or upsell | `variants/retainer-health-check.md` |

## Good/Bad Examples — load on demand

Use examples when output taste matters, when a section feels generic, or when reviewing a
deliverable before it goes to a client. Load only the matching example.

| Output type | Read this |
|---|---|
| Blueprint executive summary | `examples/blueprint-executive-summary.md` |
| Blueprint Advisory full document (Silver tier PDF) | `assets/templates/kaizen-proposal-template.pdf` + `examples/kaizen-blueprint-advisory-example.pdf` + `examples/kaizen-blueprint-advisory-example.md` + `reference/kaizen-pdf-template-system.md` |
| SOW / Engagement Agreement | `assets/templates/kaizen-sow-template.html` + `assets/templates/kaizen-sow-template.pdf` + `reference/kaizen-pdf-template-system.md` |
| Pitch deck or PPTX presentation | `assets/templates/kaizen-pitch-deck-template.pptx` + `reference/kaizen-pptx-design-system.md` + `examples/kaizen-pitch-deck-example.pptx` + `examples/kaizen-pitch-deck-example.md` |
| Proposal Situation section | `examples/proposal-situation.md` |
| AnyDB recommendation | `examples/anydb-architecture-recommendation.md` |
| Source-of-truth decision | `examples/source-of-truth-decision.md` |
| Migration risk section | `examples/migration-risk-section.md` |
| Post-discovery follow-up email | `examples/post-discovery-followup-email.md` |
| Decision Review / adversarial recommendation check | `examples/decision-review.md` |
| Diagnose good/bad examples | `examples/kaizen-diagnose-good-bad.md` |
| Proposal good/bad examples | `examples/kaizen-proposal-good-bad.md` |
| Migration QA verdict examples | `examples/kaizen-migration-qa-verdicts.md` |
| AnyDB architecture examples | `examples/kaizen-anydb-architecture-examples.md` |
| Signal-based outreach examples | `examples/kaizen-outreach-signal-based-examples.md` |
| QBR and account-health examples | `examples/kaizen-qbr-account-health-examples.md` |

## Trigger Disambiguation

When a request could match multiple skills, use these tiebreakers in order:

1. **Pipeline position:** Where is this client in the engagement? If pre-build, route to architect. If mid-migration, route to dataprep or migrate. If post-build, route to anydb-audit or report.
2. **Output type:** What is the user expecting to receive? A spec document → architect. A transformed CSV → dataprep. A loaded AnyDB system → anydb-dataload. A verification report → anydb-audit or validate.
3. **Verb signal:** "Design" / "spec" / "map" → architect. "Clean" / "prep" / "transform" → dataprep. "Load" / "seed" / "populate" → anydb-dataload. "Check" / "verify" / "audit" → anydb-audit or validate.
4. **When still ambiguous:** Ask one question: "Are you looking for [option A] or [option B]?" — name the two most likely skills' outputs in plain language, not skill names.
5. **"Follow-up email" depth signal:** If the trigger is "follow-up email" or similar, check the depth signal. Short nudge, check-in, or touch → `kaizen-email-exec` (≤150 words). Structured recap, detailed summary, or milestone follow-up where the merchant needs to *understand something new* → `kaizen-followup` (no word cap).
