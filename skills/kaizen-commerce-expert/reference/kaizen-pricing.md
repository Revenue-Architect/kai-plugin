# KaizenCommerce Tier Logic, Pricing & Commercial Guardrails

Reference file for the kaizen-commerce-expert skill. Loaded on demand by `kaizen-propose`, `kaizen-scope`, `kaizen-finance`, `kaizen-invoice-exec`, `kaizen-qualify`, `kaizen-diagnose`, and any other skill that produces commercial output. SKILL.md keeps a compact summary; full deliverables detail and overage language live here.

---

## Tier Logic & Pricing

### POS Migration Tiers

| Tier | Locations | Price (USD) | Timeline | Data Cap |
|---|---|---|---|---|
| Blueprint | Any | $2,000 | 1–2 weeks | N/A — diagnostic |
| Silver | 1–5 | From $7,500 | 4–7 weeks | 50K products/customers |
| Gold | 6–10 | From $10,000 | 5–10 weeks | 150K products/customers |
| Diamond | 11+ / Enterprise | From $30,000 | TBD | Unlimited |

### AnyDB Operations Build

| Tier | Price Range (USD) | Scope |
|---|---|---|
| Blueprint | $2,000 | Back-office ops audit, workflow gap analysis, architecture recs |
| Standard Build | $7,500–$12,000 | Single workflow domain, 3–6 automations, basic Shopify integration |
| Advanced Build | $12,000–$20,000 | Multiple domains, complex schema, 6+ automations, deep integration, portal |

### Shopify Commerce Systems

Use for DTC Commerce, B2B Commerce, or Mixed Commerce Systems where POS migration is not the lead
scope.

| Commercial path | Pricing rule | Scope |
|---|---|---|
| Blueprint | $2,000 | Diagnose storefront, checkout, customer-account, B2B, catalog, pricing, app-stack, ERP/accounting, fulfillment, and AnyDB operating-layer needs |
| DTC Commerce Implementation | Requires approved price | Online-store, app-stack, customer-account, checkout, content/data continuity, fulfillment, returns, SEO, subscriptions, analytics, or post-launch operating model |
| B2B Commerce Implementation | Requires approved price | Companies, company locations, catalogs, price lists, quantity rules, payment terms, approval/review workflows, ERP/accounting, and AnyDB operating layer. Confirm the merchant's plan before scoping: deposits, partial payments, per-company catalog assignment, and more than 3 active catalogs are Plus-only |
| Mixed Commerce Systems | Requires approved price | Any combination of POS, DTC, B2B, ERP/accounting, fulfillment, AnyDB, and migration scope |

Do not use POS location tiers as a shortcut for DTC/B2B pricing unless POS migration is explicitly
in scope. If implementation pricing is missing, use `[NEED: approved commerce systems price]` or
recommend the Blueprint/advisory path or a scoped implementation call before pricing.

#### B2B Scope Drivers

B2B is now a KaizenCommerce specialization, so scope it on its own drivers rather than translating
from POS location count. These are the variables that move effort. Use them to build the estimate and
to defend it.

| Driver | Low effort | High effort |
|---|---|---|
| Buying accounts | Under 50, clean data | Hundreds, duplicated, no external IDs |
| Pricing tiers | 1–3, fits the native catalog budget | More than 3, or per-company pricing |
| Catalog assignment | Markets-based, plan-native | Per-company on Plus, or operating-layer driven |
| Ordering model | Buyer self-serve only | Rep-assisted plus buyer self-serve plus quoting |
| Approval workflow | None | Buyer-side chains, credit holds, exception queues |
| Payment | Net terms only | Deposits, partial payments, per-fulfillment requests (all Plus) |
| Customer accounts | Already on new accounts | Legacy account migration in scope |
| Historical orders | Reference-only or none | Full import with reconciliation |
| ERP/accounting | One-way, one system | Two-way sync, price authoring conflict, AR reconciliation |
| Tax | Single jurisdiction | Multi-jurisdiction with exemption certificate lifecycle |

**Plan-gated scope rule.** Before pricing any B2B engagement, confirm the merchant's plan. If the
requested scope includes deposits, partial payments, per-fulfillment payment requests, per-company
catalog assignment, or more than 3 active catalogs, and the merchant is not on Plus, the estimate
must name the path (Plus upgrade, public app, operating-layer build, or scope reduction) and price
it. Never let a Plus-only capability enter a non-Plus SOW as though it were configuration.

**Legacy customer accounts rule.** A merchant on legacy customer accounts is buying an account
migration alongside the B2B build. Price it as its own line, not as setup.

### Retainer Architecture

Three retainer products, assembled from the service-module catalog in
`reference/kaizen-retainer-architecture.md`. One client may hold more than one at once. Attach the
matching product by default to every implementation — see "Retainer Attach Discipline" below.

**1. Managed Integration Retainer** — for any client with a built POS ↔ ERP ↔ accounting
integration (Patchworks, Versori, or similar). Price the three components separately; never bundle
platform cost into a thin markup:

| Component | Treatment | Amount (USD/mo) |
|---|---|---|
| Middleware subscription | Pass through **at cost**, transparent client line item | Vendor's actual cost (no markup) |
| Management layer | Kaizen recurring revenue: monitoring, error repair, vendor management, monthly reporting | $500–$800 |
| Break-fix / change requests | Billed at standard rate above the included threshold | Standard hourly above ~2 hrs/mo |

Typical client total: **~$800–$1,300/mo** (middleware at cost + management layer). Kaizen margin
lives in the management layer, not in a platform markup.

**2. AnyDB Operations Retainer** — ongoing management of a delivered AnyDB operational system:
schema/formula upkeep, automation maintenance, exception-queue management, new workflow domains,
monthly reporting.

| Tier | Price (USD/mo) | Scope |
|---|---|---|
| Tier 1 | $500–$750 | Monitoring, formula/automation upkeep, minor schema adjustments, up to ~4 hrs/month |
| Tier 2 | $750–$1,500 | Active ops support, schema iterations, new workflow domains, up to ~10 hrs/month, quarterly review |

**3. Ops Care Retainer** — the general retainer for any live multi-location operation, assembled
from the module catalog (Flow upkeep, data hygiene, ops reporting, seasonal reconfig, incremental
builds, priority support, training refreshes, new-channel rollouts):

| Tier | Price (USD/mo) | Scope |
|---|---|---|
| Tier 1 | $500–$750 | Monitoring, monthly Operations Health Report, data-hygiene checks, minor adjustments, priority support, up to ~4 hrs/month |
| Tier 2 | $750–$1,500 | Everything in Tier 1 + active Flow upkeep, schema/config iterations, seasonal reconfiguration, incremental-build block, quarterly business review, up to ~10 hrs/month |

The monthly Operations Health Report is the backbone deliverable for Ops Care and the upsell
instrument across all three products — auto-generated against the client's live store via
`skills/kaizen-ops-health-report.md`.

### Retainer Attach Discipline

Every implementation proposal carries the matching retainer offer in the same document — the build,
and the partnership that keeps it alive. This is a default, not a later upsell.

| Implementation left behind... | Attach |
|---|---|
| A POS ↔ ERP ↔ accounting integration | Managed Integration Retainer |
| An AnyDB operational system | AnyDB Operations Retainer |
| A live multi-location operation | Ops Care Retainer (tier by operational maturity) |

Track **implementation → retainer attach %** as a core business metric. Position the tier by the
merchant's operational maturity (`reference/kaizen-operational-readiness.md`), not by default to the
largest tier.

### Tier Deliverables Detail

**Blueprint:** Full systems audit, ops gap analysis, tech stack assessment, migration roadmap, actionable report client owns.

**Silver:** Up to 50K products/customers migration, gift card migration, virtual hardware config, 15-day staff training, POS setup audit + implementation, discovery call, data sanitization & mapping.

**Gold:** Everything in Silver + multi-location config, historical order migration, 150K data limit, custom reporting dashboards, priority scheduling, 30-day premium support.

**Diamond:** Everything in Gold + unlimited data, advanced loyalty routing, custom integration dev, white-glove enterprise support, dedicated migration specialist, enterprise SLA.

### Commercial Guardrails
- **Data limits must be explicit.** State the cap clearly.
- **Overages addressed up front.** If data likely exceeds cap, add change-order language.
- **Net investment always shown.** Gross fee → Blueprint credit → net total.
- **Never invent ROI numbers.** Client-provided facts or clearly labeled conservative estimates only.
- **Two commercial lanes.** KaizenCommerce sells (1) Blueprint Diagnostic + Advisory for capable
  internal teams, uncertain scope, or merchants who want a paid audit and launch plan before
  committing, and (2) full implementation for merchants that need KaizenCommerce to own delivery
  after a scoping call establishes the scope.
- **No blind implementation quotes.** A first ask for a "ballpark," "starting at," or tier minimum
  may use the POS tier ranges only when the scoping call or provided brief establishes location
  count, current stack, migration entities, data/integration exposure, timeline pressure, and open
  assumptions. If those are missing, quote no implementation number: recommend the scoping call or
  Blueprint/advisory lane and state what must be scoped before implementation pricing is reliable.
  Required compact form when inputs are missing: `I would not quote implementation blind. The next
  step is a scoping call; if they have a capable internal team or unclear risk, the Blueprint is
  $2,000 USD and credits toward implementation.`
- **Implementation ranges are canon-only.** When scope is sufficiently known, state that the
  implementation range comes from this pricing canon, name the assumptions, include data caps and
  overage exposure, and avoid invented ROI or unsupported timelines.
- **Blueprint guarantee is diagnostic-only.** The Blueprint fee is refundable only if
  KaizenCommerce fails to deliver the promised diagnostic artifacts. Never attach the guarantee to
  implementation pricing, timeline, launch outcome, ROI, or approval by a third party.
- **DTC/B2B implementation pricing requires approval.** Do not invent commerce systems pricing
  from POS tiers unless POS migration is actually in scope.
- **AnyDB-first commerce lens.** For B2B/DTC operating workflows, evaluate AnyDB before
  recommending native-only or app-only scope.

### Implementation Payment Schedule (single authority)

For every new implementation engagement, use the standard **50% / 25% / 25%** schedule unless
the operator explicitly approves different terms or an already signed agreement controls. Calculate all
three payments from the **net implementation investment after any applicable Blueprint credit**.

| Payment | Share of net investment | Invoice trigger | Required milestone language |
|---|---:|---|---|
| Initial deposit | 50% | SOW execution | Confirms the start date and resource allocation; the delivery timeline begins after execution, deposit payment, and required access. |
| Mid-project milestone | 25% | Client accepts the named midpoint milestone in the SOW | Name the exact acceptance gate, such as validated migration/configuration or an approved UAT-ready build. Do not use a vague calendar-only trigger. |
| Final payment | 25% | Go-live confirmation or the SOW's agreed completion gate when no launch is in scope | Tie the invoice to the named completion evidence and acceptance criteria. |

- Invoice each milestone on the **net** investment, not the gross fee.
- State USD, approved payment methods, and Net 7 from each invoice date.
- Shopify platform, app, connector, and other vendor fees are billed separately.
- Do not use 50% / 50% or tier-based payment splits as the default for a new implementation.
- Blueprint/advisory-only work and change orders follow their separately approved commercial terms;
  do not automatically force the implementation schedule onto them.

### Standard Overage Language
> This engagement includes migration of up to [included limit] products/customers. If the final export exceeds that threshold, we will issue a change order covering additional mapping, QA, and import workload, which may affect both project fee and delivery timeline.

### Warranty & Hypercare Windows (single authority — skills never restate the windows)

- **Silver — 7-day bug warranty:** any defect or misconfiguration directly attributable to
  KaizenCommerce's implementation work, reported within 7 calendar days of go-live, is resolved at
  no additional cost. Firm commitment.
- **Gold and Diamond — 14-day bug warranty:** same terms, reported within 14 calendar days of
  go-live. Firm commitment.
- **Exclusions (state explicitly):** client-made changes, new feature requests, third-party app
  updates, and issues reported after the window.
- **Requirement:** warranty requires a named client contact for acceptance testing in the final
  pre-launch week.
- **After the window:** issues route to the active retainer; with no retainer in place, a change
  order is issued before work begins.
- Proposals and SOWs quote these windows from this section only. Vague language ("we'll support
  you after launch") fails QA.
