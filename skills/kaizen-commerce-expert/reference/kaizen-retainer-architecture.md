# Kaizen Retainer Architecture — Recurring Revenue Model

Load this file when scoping, pricing, pitching, or running any retainer; when deciding what
ongoing work to attach after an implementation; or when answering recurring-revenue strategy
questions. Dollar values are canonical in `reference/kaizen-pricing.md` — this file owns the
*model*, not the price table.

## The Recurring-Revenue Thesis

A retainer is not a product. It is ownership of the recurring entropy of a live commerce
operation. A multi-location Shopify operation is never "done": automations break when business
rules change, integrations drift, catalog and inventory accuracy degrade every month, new
locations and channels open, and staff turn over. That entropy is the annuity.

This reframes the earlier mistake of thinking "AnyDB build = the only retainer." AnyDB is one
recurring surface. The recurring pain is much larger than AnyDB, and every implementation Kaizen
ships leaves behind a managed surface that justifies ongoing revenue.

Two disciplines make recurring revenue compound:

1. **Attach by default.** Every implementation proposal carries the matching retainer offer in the
   same document — the build, and the partnership that keeps it alive. Not a later upsell.
2. **The monthly report re-diagnoses.** The recurring Operations Health Report surfaces the next
   fix and the next build, so the retainer feeds the implementation funnel instead of replacing it.

## Service Module Catalog

Retainers are assembled from these recurring service modules. A retainer product is a named bundle
of modules at a price band, not a new thing to invent each time.

| Module | What recurs | What Kaizen does | Typical trigger |
|---|---|---|---|
| **Shopify Flow maintenance & expansion** | Automations break when business rules, apps, or Shopify behavior change | Monitor, repair, and extend Flows; add new automations as rules evolve | Any client with live Flows |
| **Integration health** | POS ↔ ERP ↔ accounting syncs drift and fail | Monitor middleware, catch and repair sync errors, manage the vendor relationship | Any client with a built integration |
| **Data hygiene** | Catalog and inventory accuracy degrade with daily operations | Recurring audits of inventory accuracy, catalog completeness, duplicate/orphan records | Any multi-location or high-SKU client |
| **Operations reporting** | The business always needs current numbers | Monthly Operations Health Report (auto-generated via Shopify MCP) + quarterly business review | Every retainer — this is the backbone deliverable |
| **Incremental builds** | The backlog is never empty | A recurring block of small build/config work each cycle | Any client with an evolving operation |
| **Seasonal reconfiguration** | Peaks, promos, and new-location rollouts repeat | Peak readiness, promo/discount setup, new-location POS rollout | Retail clients with seasonal cycles |
| **Priority support / SLA** | Break-fix demand is continuous | Guaranteed response window, escalation path, break-fix within the included block | Any client who cannot afford downtime |
| **Training refreshes** | Retail staff churn; POS training is never finished | Refresh training as staff turn over; quick-reference updates | Multi-location retail with staff turnover |
| **New channel rollouts** | Growth adds B2B, wholesale, Markets, subscriptions | Stand up and configure the new channel on the existing stack | Any client expanding channels |

A retainer is not a help desk. Each module ties to a specific operational-continuity risk. If a
module cannot be tied to a named risk for this client, do not include it.

## The Three Retainer Products

All three can be held simultaneously by one client (e.g., Managed Integration + Ops Care). Pick the
product by what the implementation left behind.

### 1. Managed Integration Retainer

The stickiest product. A broken POS↔ERP↔accounting integration is business-critical, so clients are
reluctant to cancel. Triggered by any integration build (Patchworks, Versori, or similar
middleware).

**Pricing model — never bundle cost into a thin markup.** Separate the three components:

1. **Middleware subscription** — passed through *at cost* as a transparent client line item. Do not
   mark it up. Transparency is the position: the client pays the platform what the platform costs,
   and pays Kaizen for managing it.
2. **Management layer** — Kaizen's actual recurring revenue: monitoring integration health,
   catching and repairing sync errors, managing the vendor relationship, monthly reporting.
3. **Break-fix / change requests** — work above a defined monthly threshold is billed at the
   standard rate under an SLA tier.

Architect the integration through Kaizen's agency middleware account where the platform allows it.
This creates healthy switching cost and gives Kaizen multi-client platform leverage. The
integration IP — the design, the monitoring logic, the error-handling runbook — lives in Kaizen's
skill and runbooks, **not** in the middleware platform. That keeps the model vendor-agnostic: the
client stays because Kaizen runs the integration, not because one platform locks them in.

See `reference/kaizen-pricing.md` for the canonical management-layer band and client-total range.

### 2. AnyDB Operations Retainer

Once an AnyDB operational system runs approvals, exceptions, portals, or reporting, it must be
maintained and evolved. Triggered by any AnyDB build. Scope draws from: schema and formula upkeep,
automation maintenance, exception-queue management, new workflow domains as the operation grows,
and monthly operations reporting. Tiered like Ops Care. Anchor: the operational system is
mission-critical once adopted, so continuity is the value, not hours.

### 3. Ops Care Retainer

The general retainer for any live multi-location operation, assembled from the module catalog.
Tiered (canonical bands in `reference/kaizen-pricing.md`):

- **Tier 1** — monitoring, the monthly Operations Health Report, data-hygiene checks, minor
  adjustments, and priority support within a small included block.
- **Tier 2** — everything in Tier 1 plus active Flow upkeep, schema/config iterations, seasonal
  reconfiguration, an incremental-build block, and a quarterly business review, within a larger
  included block.

Position the tier by the merchant's operational maturity (see
`reference/kaizen-operational-readiness.md`): Emerging teams need Tier 2 hand-holding early;
Advanced teams that own their system need Tier 1 monitoring and an escalation path.

## Land-and-Expand Map

```
ENTRY
  Blueprint (front-door audit) — identifies the gap
        |
        v
IMPLEMENTATION (productized ladder — see kaizen-pricing.md)
  Silver / Gold / Diamond POS  •  AnyDB Build  •  DTC/B2B Commerce  •  Integration build
        |
        v
RETAINER (attach by default — one or more, stacked)
  Managed Integration  •  AnyDB Operations  •  Ops Care (Tier 1 / Tier 2)
        |
        v
EXPANSION (the monthly report manufactures the next project)
  Health Report + QBR surface the next fix and the next build
        |
        +--> client re-enters the implementation funnel at a higher ACV
```

The bottom arrow is the engine. A finished project is the start of the next conversation, not the
end of the relationship. The monthly Operations Health Report is both the retainer's backbone
deliverable and the upsell instrument: every report ends with the issues it found and the fixes
that resolve them.

## Attach Metrics

Track two ratios as first-class business metrics. They run the whole model:

- **Blueprint → implementation attach %** — does the front door convert to a build?
- **Implementation → retainer attach %** — does every build become an annuity?

A third signal worth watching: **retainer → next-build %** — does the monthly report actually
surface and convert expansion work? Record these alongside engagement history in the memory system.

## Anti-Selection — When NOT to Pitch a Retainer

- Do not pitch a retainer (or expansion) to a Red-health account. Stabilize first.
- Do not pitch a retainer as generic support. Tie every retainer to a specific operational-continuity
  risk for this client.
- Do not claim outcomes without baseline and post-launch evidence.
- Do not confuse warranty/hypercare with paid ongoing support. The warranty window is included; the
  retainer begins where the warranty ends.
- Do not ignore the client's internal ownership capacity. An Advanced team that can run its own
  system gets a lighter tier, not a forced heavy one.

## Cross-References

- `reference/kaizen-pricing.md` — canonical retainer dollar bands, pass-through structure, tiers
- `skills/kaizen-ops-health-report.md` — the automated monthly Operations Health Report (Shopify MCP)
- `skills/kaizen-report-exec.md` — health check, retainer pitch deck, QBR, case study production
- `variants/retainer-health-check.md` — the post-go-live retainer scenario and skill chain
- `reference/kaizen-operational-readiness.md` — maturity scoring for tier positioning
- `skills/kaizen-propose.md` — proposal-stage retainer attach discipline
