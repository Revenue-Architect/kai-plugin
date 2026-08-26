# KaizenCommerce Cross-Skill Pairing Architecture

Use this reference when the operator asks how the installed Codex skills should pair with Kai, how to
elevate KaizenCommerce output with other skills, or how to choose an optimal multi-skill workflow.
This file is an operating architecture, not a trigger to activate every skill. Load only the
specific pairings needed for the current task.

Snapshot scope: first-class adjacent workflow skills source-managed under this repo's `skills/`
directory and installed to `~/.codex/skills` by `scripts/install.sh`, plus the Kaizen specialist
skills that live beside Kai at runtime. System skills under `.system`, plugin-cache skills, and
duplicate `.agents` examples are support context only unless the operator explicitly asks about them.

## Control Rules

Kai remains the orchestrator. External skills can improve strategy framing, process rigor, brand,
design, growth distribution, code execution, QA, or asset production. They do not override Kai's
commerce judgment.

Kai owns:
- final client-facing synthesis
- commercial positioning, scope, pricing, and two-lane commercial decisions
- Shopify vs AnyDB vs app vs ERP source-of-truth decisions
- migration lane decisions and final QA verdicts
- source-backed current-platform claims

External skills support:
- deeper research or process lenses
- writing cleanup and channel-specific formatting
- brand, design, UI, and visual asset production
- engineering workflow, repo hygiene, testing, and PR execution
- marketing distribution, CRO, SEO, and growth systems

Never use a pairing as an excuse to skip Kai's source rules. Current Shopify technical behavior
still uses Shopify Dev MCP. Broader KaizenCommerce web research still uses Exa MCP by default.
AnyDB syntax or platform behavior must pass the AnyDB freshness/source gate when current behavior
matters.

## Tier Definitions

| Tier | Meaning | Default behavior |
|---|---|---|
| Core Pairing | Materially improves KaizenCommerce sales, delivery, QA, architecture, content, or client outcomes | Use when the workflow matches |
| Situational Pairing | Useful for a specific output or channel, but not part of the default Kai path | Use only when requested or clearly relevant |
| Support Utility | Helps repo/runtime/process work, but should not shape client recommendations | Keep behind implementation or maintenance tasks |
| Low/No Fit | Installed skill exists, but has little direct KaizenCommerce leverage | Mention only when asked |

## Highest-Leverage Workflow Stacks

### 1. Shopify AE Enablement

Use when creating AE-facing positioning, referral criteria, partner one-pagers, LinkedIn posts, or
deal-qualification language.

Order:
1. Kai: define the referral-fit thesis, commercial guardrails, and Shopify/AnyDB boundary.
2. `product-marketing-context`: sharpen segment, pain, proof, and differentiation.
3. `sales-enablement`: convert the thesis into AE talk tracks, battlecards, one-pagers, or objection handling.
4. `social-content` and `stop-slop`: turn into LinkedIn-ready posts without engagement bait.
5. `ckm:brand` and `ckm:design-system`: align wording and visuals to KaizenCommerce.
6. `ckm:banner-design` or `ckm:design`: create optional social/partner assets.

Kai must keep AE content from becoming generic "Shopify agency" language. The angle is retail
operating confidence: cutover, data, uptime, staff training, inventory, reporting, and the ops
layer around Shopify.

### 2. Blueprint and Operational Diagnostic Upgrade

Use when producing or improving Blueprint reports, merchant diagnostics, operational readiness
reviews, or pre-proposal findings.

Order:
1. Kai `kaizen-research` and `kaizen-qualify`: collect merchant facts and discovery context.
2. `operations-manager`: add maturity model, process map, KPI owner/data-source discipline, DMAIC/PDCA lens, and capacity constraints.
3. Kai `kaizen-diagnose`: write findings, implications, risk, and Blueprint framing.
4. `kaizen-retail-architecture` or `kaizen-anydb-schema`: review source-of-truth or AnyDB architecture when needed.
5. Kai `kaizen-check`: validate scope, numbers, voice, evidence, and commercial safety.
6. Kai `kaizen-render` plus `ckm:design-system`: create a polished PDF or deck.

The operations lens strengthens the diagnosis, but Kai owns the recommendation and must avoid
inventing ROI, benchmarks, or savings.

### 3. AnyDB Portal and Operations System Design

Use when designing vendor portals, PO workflows, approval queues, inventory exception workflows,
B2B portals, or KaizenCommerce OS screens.

Order:
1. Kai `kaizen-architect`: decide what Shopify owns, what AnyDB owns, and what must remain in an ERP or app.
2. `operations-manager`: map the process, handoffs, SLAs, KPIs, and control plan.
3. `kaizen-anydb-schema`: refine Types, Cells, formulas, Attach vs Reference, and schema QA.
4. `kaizen-shopify-flow`: verify which automations belong in Flow rather than AnyDB.
5. `ckm:ui-styling`, `ce-frontend-design`, or `ui-ux-pro-max`: turn the workflow into usable screens, dashboards, and responsive layouts.
6. Kai `kaizen-check`: validate the build spec before implementation.

Do not let UI skills redesign the data model. UI skills expose whether the workflow is usable;
Kai and AnyDB specialists own the operating architecture.

### 4. Migration Delivery and QA

Use for Shopify migration strategy, API-first execution packages, Matrixify fallback, dry runs,
logs, reconciliation, and go-live verdicts.

Order:
1. Kai: choose the migration lane and define the source-of-truth contract.
2. `kaizen-shopify-migration`: map entities, cutover, staged execution, and fallback.
3. `kaizen-migration-qa`: triage evidence, API logs, import results, and reconciliation variances.
4. `ce-debug`, `ce-code-review`, `ce-test-browser`, or `ce-work`: support scripts, tests, and local engineering work when files or code are involved.
5. Kai: sign off on final QA verdict, client communication, and remediation plan.

External engineering skills can improve implementation quality. They cannot choose the final lane
or declare the migration ready without Kai's evidence gate.

### 5. Post-Go-Live Proof and Retainer Growth

Use after go-live for health checks, retainer pitches, QBRs, case studies, testimonial requests,
expansion signals, and churn prevention.

Order:
1. Kai `kaizen-report`: capture what shipped, what changed, what still needs ownership, and what deserves proof.
2. `operations-manager`: map before/after KPIs, control plans, SLA gaps, utilization, and process maturity.
3. `churn-prevention`: classify account risk, retention drivers, and adoption gaps.
4. `referral-program`, `co-marketing`, or `community-marketing`: turn successful clients into proof, partner motion, and referral loops.
5. `kaizen-publish`, `ckm:brand`, `ckm:design-system`, and `ckm:banner-design`: create case-study, social, PDF, and AE proof assets.

Proof must stay sourced. If baseline metrics are estimates, label them.

### 6. KaizenCommerce Website, Tools, and Frontend Experiences

Use for KaizenSite, free tools, landing pages, calculators, dashboards, client portals, or internal
ops tooling.

Order:
1. Kai: define audience, promise, source-of-truth, and commercial role.
2. `site-architecture`, `page-cro`, `product-marketing-context`, or `customer-research`: shape information architecture and conversion path.
3. `ce-frontend-design`, `ckm:ui-styling`, and `ui-ux-pro-max`: design/build the interface.
4. `analytics-tracking`, `ab-test-setup`, and `ce-test-browser`: instrument and verify.
5. `seo-audit`, `ai-seo`, `schema-markup`, or `programmatic-seo`: improve discoverability when the page is public.

Do not build landing-page gloss when the user asked for an actual tool or operational interface.

## Exhaustive Skill Matrix

| Skill | Tier | Best Kai pairing | Primary use | Boundary |
|---|---|---|---|---|
| `ab-test-setup` | Situational Pairing | `kaizen-content-calendar`, `kaizen-publish`, KaizenSite, CRO workflows | Test hooks, offers, landing pages, lead magnets, and AE enablement variants | Does not invent success metrics; Kai defines business goal |
| `ad-creative` | Situational Pairing | `kaizen-content-calendar`, `paid-ads`, `ckm:banner-design` | Paid ad copy and creative variants for Blueprint, POS migration, or AnyDB campaigns | Ads must follow Kai proof and pricing guardrails |
| `ai-seo` | Core Pairing | KaizenSite, `kaizen-publish`, `content-strategy` | Optimize KaizenCommerce content for AI citations and answer engines | Must not create unsupported market claims |
| `analytics-tracking` | Core Pairing | KaizenSite, CRO, paid, free-tool workflows | Define events, conversion tracking, attribution, and experiment measurement | Does not decide the commercial thesis |
| `aso-audit` | Low/No Fit | none by default | Only useful if KaizenCommerce audits or launches an app listing | Keep outside normal Kaizen workflows |
| `ckm:banner-design` | Core Pairing | `kaizen-publish`, `kaizen-content-calendar`, `kaizen-report`, AE enablement | LinkedIn banners, carousel covers, partner graphics, case-study visuals | Visual asset layer only |
| `ckm:brand` | Core Pairing | `kaizen-identity`, `kaizen-voice`, `kaizen-check`, AE enablement | Brand bible, messaging matrix, voice consistency, partner/ICP positioning | Does not change commercial rules |
| `ce-agent-native-architecture` | Situational Pairing | KaizenCommerce OS, internal agent tooling, MCP/plugin design | Agent-native architecture for Kaizen internal systems or client-facing AI workflows | Kai decides business purpose and data boundaries |
| `ce-agent-native-audit` | Situational Pairing | KaizenCommerce OS, automation governance, MCP/plugin work | Audit agentic workflows for autonomy, safety, and architecture quality | Does not approve client delivery alone |
| `ce-brainstorm` | Situational Pairing | early product/service ideation before Kai spec | Explore ambiguous ideas before Kai turns them into scope or strategy | Use before decisions, not after requirements are stable |
| `ce-clean-gone-branches` | Support Utility | repo maintenance | Clean stale branches in Kaizen repos | No client-facing role |
| `ce-code-review` | Core Pairing | migration scripts, KaizenSite, AnyDB tooling, source repo changes | Review code changes before PR or deployment | Technical review only; Kai owns domain correctness |
| `ce-commit-push-pr` | Support Utility | source repo or client repo delivery | Commit, push, and open PRs with clear descriptions | Use only when user asks to ship |
| `ce-commit` | Support Utility | source repo maintenance | Create clean commits for Kai or client code changes | No strategy role |
| `ce-compound-refresh` | Support Utility | Compound Engineering maintenance | Refresh stale CE learning and plugin context | No direct Kaizen client role |
| `ce-compound` | Support Utility | solved-problem documentation | Capture reusable engineering lessons after hard tasks | Internal learning only |
| `ce-debug` | Core Pairing | migration scripts, Shopify API jobs, frontend bugs, build failures | Root-cause debugging with evidence | Kai owns final remediation plan when commerce risk exists |
| `ce-demo-reel` | Situational Pairing | KaizenSite, case studies, tool demos | Capture visual demo reels of working apps or interfaces | Marketing/demo artifact only |
| `ce-dhh-rails-style` | Low/No Fit | Rails-only client/internal apps | Apply Rails/37signals style when the codebase is Rails | No role outside Rails work |
| `ce-doc-review` | Core Pairing | proposals, Blueprint drafts, specs, plans | Persona-based review of important plans and docs | Kai resolves findings and signs off |
| `ce-frontend-design` | Core Pairing | KaizenSite, portals, dashboards, landing pages | Build or improve high-quality web interfaces | Must respect Kai/CKM brand and existing design systems |
| `ce-gemini-imagegen` | Situational Pairing | visual assets, hero images, campaign graphics | Gemini image generation/editing for marketing assets | Do not use for factual product screenshots |
| `ce-ideate` | Situational Pairing | service offers, tools, content series | Generate and evaluate ideas before Kai scopes work | Kai chooses final direction |
| `ce-optimize` | Core Pairing | prompts, research quality, conversion, search, workflows | Run measurable optimization loops | Metrics must be explicitly defined |
| `ce-plan` | Core Pairing | implementation plans, delivery plans, repo changes | Turn scoped work into decision-complete plans | Kai owns Kaizen-specific constraints |
| `ce-polish-beta` | Situational Pairing | frontend/UI after implementation | Browser-based polish loop | Only after a page/app exists |
| `ce-product-pulse` | Situational Pairing | Kaizen apps, tools, client dashboards | Usage and product-health pulse reports | Requires configured telemetry |
| `ce-proof` | Core Pairing | QA-heavy client deliverables and code changes | Human-in-the-loop proofing before final handoff | Supplements, not replaces, Kai check |
| `ce-release-notes` | Support Utility | source repo or client app release notes | Summarize shipped changes | No commercial recommendation role |
| `ce-report-bug` | Support Utility | Compound plugin issues | File structured bug reports | No Kaizen workflow role |
| `ce-resolve-pr-feedback` | Support Utility | repo delivery | Address PR review feedback | Technical execution only |
| `ce-riffrec-feedback-analysis` | Situational Pairing | product feedback recordings | Analyze Riffrec user feedback bundles | Only when that artifact exists |
| `ce-sessions` | Core Pairing | prior Codex work, Kai history, handoffs | Search previous sessions for decisions and evidence | Treat old session data as stale until verified when needed |
| `ce-setup` | Support Utility | local dev/plugin setup | Diagnose CE environment and missing tools | No client-facing role |
| `ce-simplify-code` | Core Pairing | recently changed scripts/apps | Refine code clarity while preserving behavior | Do not refactor unrelated code |
| `ce-slack-research` | Situational Pairing | internal Slack evidence, client/team research | Search Slack-derived context when available | Observe privacy and evidence boundaries |
| `ce-strategy` | Situational Pairing | long-running product/repo strategy | Maintain strategy docs for Kaizen apps or tools | Kai owns agency strategy and client commercial decisions |
| `ce-test-browser` | Core Pairing | frontend, Shopify theme, portal, website checks | Browser verification, screenshots, and UI test evidence | Use for local/visual verification |
| `ce-test-xcode` | Low/No Fit | iOS apps only | Build/test iOS apps | Rare for KaizenCommerce |
| `ce-update` | Support Utility | CE plugin update checks | Check/update Compound Engineering tooling | No client-facing role |
| `ce-work-beta` | Support Utility | code execution | Beta autonomous work execution | Prefer standard Kai/CE workflows unless explicitly chosen |
| `ce-work` | Core Pairing | scoped implementation tasks | Execute code work efficiently | Kai provides domain constraints and final review |
| `ce-worktree` | Support Utility | isolated repo work | Create worktrees for risky or parallel implementation | Use when repo isolation matters |
| `churn-prevention` | Core Pairing | `kaizen-report`, retainer, QBR, account health | Identify churn risk, adoption gaps, retention motions | Must be grounded in actual client state |
| `co-marketing` | Situational Pairing | case studies, Shopify AE/partner motion | Partner campaigns, joint content, proof distribution | Requires approved partner/client permission |
| `cold-email` | Core Pairing | `kaizen-outreach`, `kaizen-email-exec` | Prospecting emails and follow-up sequences | Kai keeps the two-lane model and no invented claims |
| `community-marketing` | Situational Pairing | long-term audience/partner ecosystem | Community-led growth, groups, advocates | Not a default near-term sales motion |
| `competitor-alternatives` | Situational Pairing | SEO pages, sales battlecards, platform comparisons | Alternative/vs pages and competitive collateral | Claims need current source verification |
| `competitor-profiling` | Core Pairing | merchant research, market positioning, sales enablement | Competitor intelligence and battlecards | Do not overstate competitor weaknesses |
| `content-strategy` | Core Pairing | `kaizen-content-calendar`, KaizenSite | Content pillars, editorial roadmap, topic clusters | Kai owns commerce point of view |
| `copy-editing` | Core Pairing | all prose deliverables | Tighten grammar, clarity, and readability | Must preserve Kaizen voice and facts |
| `copywriting` | Core Pairing | website, landing pages, email, sales pages | Write conversion copy from Kai strategy | No unsupported ROI or guarantees |
| `customer-research` | Core Pairing | ICP, discovery, VOC, website/copy | VOC mining, persona/JTBD synthesis, interview analysis | Web research still follows Exa/source rules when Kaizen-related |
| `ckm:design-system` | Core Pairing | `kaizen-render`, `kaizen-publish`, KaizenSite | Tokens, typography, CSS variables, slide/doc consistency | Kai `kaizen-ds-v2.html`, `kaizen-design-system.md`, and `kaizen-design-tokens.json` remain source of truth |
| `ckm:design` | Situational Pairing | multi-asset campaigns and brand kits | Umbrella design orchestration for full campaign packages | Prefer narrower CKM skills for simple tasks |
| `directory-submissions` | Situational Pairing | local/partner SEO | Directory and marketplace listing strategy | Only after positioning and site pages are ready |
| `email-sequence` | Core Pairing | nurture after lead magnets, partner campaigns, webinar follow-up | Warm/lifecycle email sequences | Kai controls offer and claims |
| `form-cro` | Core Pairing | Blueprint lead forms, discovery intake, free tools | Reduce form friction and improve lead quality | Must preserve needed qualification fields |
| `free-tool-strategy` | Core Pairing | Kaizen lead-gen tools and calculators | Plan useful public tools for leads and links | Kai defines retail/operator utility |
| `image` | Situational Pairing | blog/social/website graphics | General marketing image creation and optimization | Avoid fake screenshots or fabricated client visuals |
| `kaizen-anydb-schema` | Core Pairing | `kaizen-architect`, `kaizen-anydb-build`, `kaizen-anydb-audit` | AnyDB Types, Cells, formulas, Attach vs Reference, schema QA | Thin wrapper; Kai remains orchestrator |
| `kaizen-commerce-expert` | Core Pairing | self | Main router, agency brain, commercial/technical authority | Must stay lean and source-backed |
| `kaizen-frontend-audit` | Core Pairing | storefront/PDP/cart/BOPIS/theme review | Shopify storefront UX and merchandising audit | Use as specialist when explicitly delegating or auditing |
| `kaizen-migration-qa` | Core Pairing | `kaizen-validate`, `kaizen-reconcile`, go-live verdict | Dry Run, API job, Matrixify result, reconciliation QA | Does not independently approve final client verdict |
| `kaizen-retail-architecture` | Core Pairing | `kaizen-architect`, source-of-truth decisions | POS/ERP/WMS/build-vs-buy architecture critique | Kai signs final recommendation |
| `kaizen-retail-research` | Core Pairing | `kaizen-research`, `New Deal`, platform research | Merchant research, stack detection, docs verification | Use Exa first for Kaizen web research |
| `kaizen-shopify-flow` | Core Pairing | `kaizen-flow`, `kaizen-architect`, automation boundary | Shopify Flow capability checks and workflow design | Does not force Flow when AnyDB or app layer is better |
| `kaizen-shopify-migration` | Core Pairing | `kaizen-migrate`, `kaizen-api-migration-exec`, `kaizen-square-migration` | API-first migration mapping, Matrixify fallback, cutover planning | Kai owns authoritative lane |
| `kaizen-subagent-orchestrator` | Core Pairing | explicit subagent workflows | Split bounded Kaizen work across global specialists | Only when the operator explicitly asks for subagents/delegation |
| `launch-strategy` | Situational Pairing | Kaizen offers, tools, events, campaigns | Launch sequencing for new services or assets | Kai defines offer and ICP |
| `lead-magnets` | Core Pairing | Blueprint lead gen, guides, checklists | Plan gated assets and downloadable resources | Must not dilute Blueprint as paid diagnostic entry |
| `lfg` | Support Utility | large software tasks | Full autonomous engineering pipeline | Use only on explicit hands-off code execution requests |
| `marketing-ideas` | Situational Pairing | content ideation, campaigns | Generate marketing angles and tactics | Filter through Kai ICP and proof discipline |
| `marketing-psychology` | Situational Pairing | copy, CRO, offers | Improve persuasion with behavioral principles | No manipulative or unsupported claims |
| `onboarding-cro` | Core Pairing | client portals, free tools, SaaS-like Kaizen tools | Improve post-signup activation and setup flows | Useful for productized internal/client tools |
| `operations-manager` | Core Pairing | `kaizen-diagnose`, `kaizen-architect`, `kaizen-report`, retainer | Process maps, maturity, KPIs, capacity, DMAIC, vendor scorecards | Operations lens supports Kai; it does not price or scope |
| `page-cro` | Core Pairing | KaizenSite, landing pages, service pages | Improve page conversion and clarity | Kai owns value prop and audience |
| `paid-ads` | Situational Pairing | paid acquisition strategy | Campaign strategy, channels, targeting, budgets | Requires approved spend and offer |
| `paywall-upgrade-cro` | Low/No Fit | productized tools only | In-product upgrade prompts | Rare unless Kaizen ships a freemium tool |
| `popup-cro` | Situational Pairing | website lead capture and announcements | Popups, sticky bars, overlays | Use sparingly; avoid cheapening premium agency positioning |
| `pricing-strategy` | Core Pairing | `kaizen-propose`, `kaizen-finance`, offer design | Packaging, value metrics, pricing research, monetization | Kai pricing source of truth still wins |
| `product-marketing-context` | Core Pairing | positioning, website, AE enablement, content | Single source for audience, pains, proof, messaging | Does not override Kai identity or service rules |
| `programmatic-seo` | Situational Pairing | local/location/industry pages, tool pages | SEO pages at scale | Requires source-backed templates and no thin content |
| `referral-program` | Core Pairing | Shopify AE/partner/referral motion, post-go-live | Referral incentives, partner loops, client advocacy | Must respect partner/client permission and brand fit |
| `revops` | Core Pairing | pipeline, CRM, sales process, KaizenCommerce OS | Pipeline hygiene, lifecycle stages, forecast, CRM workflows | Kai owns relationship context and strategy |
| `sales-enablement` | Core Pairing | AE kits, battlecards, proposals, objection handling | One-pagers, talk tracks, battlecards, sales assets | Kai owns factual claims and commercial guardrails |
| `schema-markup` | Core Pairing | KaizenSite, case studies, service pages | JSON-LD and rich-result eligibility | Must match visible/source-backed page content |
| `seo-audit` | Core Pairing | KaizenSite and client storefront audits | Technical/on-page SEO, indexation, CWV, metadata | Use current source data for live sites |
| `signup-flow-cro` | Situational Pairing | free tools, portals, inquiry flows | Improve account/trial/signup completion | Not default for standard contact forms |
| `site-architecture` | Core Pairing | KaizenSite, service pages, resource library | Website IA, page hierarchy, navigation, conversion paths | Kai owns message and commercial posture |
| `social-content` | Core Pairing | `kaizen-content-calendar`, `kaizen-publish` | LinkedIn/social strategy, hooks, scheduling, repurposing | Must pass Kai voice and stop-slop filter |
| `stop-slop` | Core Pairing | all Kaizen prose | Remove AI tells, filler, formulaic structures | Already part of Kai voice philosophy; use as extra pass |
| `ckm:ui-styling` | Core Pairing | AnyDB portals, dashboards, KaizenSite, storefront UI | shadcn/Tailwind UI, accessible layouts, responsive design | UI implementation only; not source-of-truth design |
| `ui-ux-pro-max` | Core Pairing | frontend audit, KaizenSite, portals, graphics | High-depth UX/design critique and polish | Pair with Kai for domain-specific screens |
| `video` | Situational Pairing | case studies, demos, social clips, explainers | Video production and AI video workflows | Use sourced visuals and approved client details |

## Routing Heuristics

When a request mentions another skill and Kai, route by output type:

| Output requested | Default stack |
|---|---|
| Thought leadership or LinkedIn | Kai + `kaizen-content-calendar` + `social-content` + `stop-slop` + optional `ckm:brand` |
| AE-facing sales asset | Kai + `sales-enablement` + `product-marketing-context` + `ckm:brand` + optional `ckm:design-system` |
| Blueprint/diagnostic | Kai + `operations-manager` + relevant retail/architecture specialist + `kaizen-check` |
| Proposal/SOW | Kai + `pricing-strategy` only as a strategy lens + `kaizen-check`; Kai pricing source wins |
| Styled PDF/deck | Kai content skill + `kaizen-render`/`kaizen-publish` + `ckm:design-system` |
| AnyDB ops system | Kai + `operations-manager` + `kaizen-anydb-schema` + `ckm:ui-styling` |
| Migration package | Kai + `kaizen-shopify-migration` + `kaizen-migration-qa` + CE engineering skills if code/files exist |
| Website or landing page | Kai + `site-architecture` + `page-cro` + `ce-frontend-design` + `ckm:ui-styling` |
| Free tool | Kai + `free-tool-strategy` + `ce-plan` + `ce-frontend-design` + tracking/CRO skills |
| Post-go-live growth | Kai + `operations-manager` + `churn-prevention` + `referral-program`/`co-marketing` + `kaizen-publish` |
| Repo or skill maintenance | Kai maintenance refs + relevant `ce-*` implementation/review skills |

## Anti-Patterns

- Do not stack many skills just because they exist. Each added skill must contribute a distinct
  lens, artifact, or validation pass.
- Do not let marketing skills invent proof, savings, ROI, client outcomes, or competitor claims.
- Do not let design skills replace Kai's DS v2 source of truth.
- Do not let operations frameworks create fake precision. If KPI data is missing, mark the gap.
- Do not let CE execution skills mutate repos unless the user requested implementation.
- Do not invoke subagents unless the operator explicitly asks for subagents, delegation, or parallel
  agent work.
- Do not route current Shopify API/schema questions to generic coding skills before Shopify Dev
  MCP verification.

## Best Default

For most KaizenCommerce work, the optimal architecture is:

1. Kai routes, frames, and owns the recommendation.
2. One domain specialist deepens the work if needed.
3. One quality layer reviews it.
4. One brand/design/growth layer packages it only when the output needs distribution or polish.

That keeps quality high without turning every answer into a context-heavy committee.
