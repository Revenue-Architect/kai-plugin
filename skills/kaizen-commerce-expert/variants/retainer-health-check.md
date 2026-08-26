# Retainer And Health Check Variant

Use this variant after go-live, after a completed engagement, or when the operator wants to convert
operational findings into a retainer, health check, case study, or upsell.

## Required Context

- Engagement completed or current operating state
- Go-live date and support window
- Baseline metrics and post-launch outcomes
- Remaining pain points or adoption gaps
- Staff readiness and owner capacity
- Systems in scope and unresolved risks
- Client appetite for ongoing support

## Default Skill Chain

1. `reference/kaizen-retainer-architecture.md` for the recurring-revenue model: service-module
   catalog, the three retainer products, attach-by-default discipline, and anti-selection rules
2. `skills/kaizen-ops-health-report.md` when a live Shopify store is connected — pull real store
   data and compute health signals as the recurring deliverable
3. `skills/kaizen-report.md` for health check, retainer pitch, case study, or upsell template
4. `skills/kaizen-report-exec.md` to render the populated report, retainer deck, or QBR
5. `skills/kaizen-finance.md` if retainer economics or agency margin matters
6. `reference/kaizen-operational-readiness.md` for support tier logic and maturity-based positioning
7. `reference/kaizen-pricing.md` for the three retainer products and the pass-through integration model
8. `skills/kaizen-check.md` before client-facing output

## Retainer Model — Which Product To Attach

This variant pitches retainers, not a single retainer. Choose the product(s) by what the engagement
left behind, and stack them when more than one applies:

- **Managed Integration Retainer** — any client with a built POS ↔ ERP ↔ accounting integration.
  Price middleware at cost (transparent line item) plus a priced management layer; never bundle
  platform cost into a thin markup.
- **AnyDB Operations Retainer** — any client running a delivered AnyDB operational system.
- **Ops Care Retainer** — any live multi-location operation, assembled from the service-module
  catalog (Flow upkeep, data hygiene, ops reporting, seasonal reconfig, incremental builds,
  priority support, training refreshes, new-channel rollouts), with the monthly Operations Health
  Report as the backbone deliverable.

The monthly Operations Health Report re-diagnoses the client and surfaces the next fix and next
build, so the retainer feeds the implementation funnel. Track **implementation → retainer attach %**
as a core business metric. Full model in `reference/kaizen-retainer-architecture.md`.

## Output Shape

- Current state after launch
- What improved
- What still needs ownership
- Support risk if Kaizen steps away
- Retainer recommendation and tier logic
- Scope boundaries and included hours
- Next 30/60/90 day focus
- Kill conditions: when retainer is not justified or should be deferred

## Common Risks

- Pitching retainer as generic support instead of specific operational continuity
- Forgetting to separate warranty/hypercare from paid ongoing support
- Overstating outcomes without baseline data
- Ignoring client internal ownership capacity
- Turning a health check into a sales deck too early

## When Not To Use

- The client is still pre-proposal. Use `skills/kaizen-propose.md`.
- The request is a post-discovery or post-Blueprint follow-up. Use `skills/kaizen-followup.md`.
- The task is pure financial planning with no client deliverable. Use `skills/kaizen-finance.md`.

## Variant Depth Additions

### Anti-Selection Rules

- Do not pitch expansion to Red accounts. Stabilize first.
- Do not pitch retainer as generic support. Tie it to specific operational continuity risk.
- Do not claim outcomes without baseline and post-launch evidence.

### Known Failure Modes

- Warranty/hypercare confused with paid ongoing support.
- Account health based on sentiment instead of evidence.
- Case study claims exceed what metrics prove.
- Client internal ownership capacity ignored.

### Default Evidence Gates

- Baseline and post-launch outcomes.
- Open risks and owner capacity.
- Support window and warranty boundary.
- Account health band and expansion readiness.

### Operating Hooks

- Account Health / Expansion Hook for health band and expansion readiness.
- Evidence Gate Hook for QBR, case study, ROI, savings, or outcome claims.
- Task / Follow-Up Hook for client-owned next steps and renewal/retainer decisions.

### Output Shape By Mode

- Quick Read: health band, expansion readiness, next action.
- Operator Analysis: stabilize/expand/closeout recommendation, risks, owner gaps.
- Client Deliverable: QBR, health check, retainer pitch, case study, or testimonial draft.
- Execution Artifact: account-health report, QBR structure, champion kit, follow-up tasks.

### Source-Of-Truth And AnyDB Boundary

Shopify and AnyDB operational data should support health claims where available. AnyDB may become
the ongoing operating layer for exception queues, ownership, reporting, and continuous improvement
when post-go-live gaps require structured follow-through.
