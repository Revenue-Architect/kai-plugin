# Post Baseline Proposal Variant

Use this variant when a Blueprint has been completed, or when the POS Delivery OS has an approved
Engagement Baseline from a partner-approved Shopify Referral Scope Brief, and the next step is a
paid implementation proposal, SOW, or client-facing scope recommendation.

## Required Context

- Blueprint findings and recommended architecture, or approved Engagement Baseline for a POS
  Delivery OS referral path
- Source artifact: Blueprint Diagnostic or Shopify Referral Scope Brief
- Client name, current stack, location count, and service type
- Confirmed pain points and quantified impacts
- Recommended tier and why
- Data volumes and caps
- Timeline constraints and staff readiness
- Apps, integrations, hardware, training, and support assumptions

## Default Skill Chain

1. `skills/kaizen-diagnose.md` as the default source of findings, or
   `delivery-os/templates/engagement-baseline.md` when a POS Delivery OS referral path is approved
2. `skills/kaizen-propose.md` for proposal and SOW
3. `reference/kaizen-pricing.md` for tier logic, caps, overage, and Blueprint credit
4. `reference/kaizen-operational-readiness.md` when maturity affects retainer or support
5. `skills/kaizen-check.md` Full Review or Decision Review before sending

## Output Shape

- Situation mirrors the Blueprint findings or approved Engagement Baseline
- Recommendation names tier, phase, and reason
- Scope table with client-specific why
- App stack with ownership and app-cost exclusion
- Business case grounded in client facts or labeled estimates
- Risk register with mitigations
- Commercial table: gross, Blueprint credit if charged, net
- Kill conditions that change tier, scope, timeline, or price

## Common Risks

- Repeating the Blueprint/Baseline instead of converting findings into scope
- Showing a Blueprint credit when no Blueprint fee was charged
- Letting AnyDB Phase 2 slip into committed Phase 1 scope
- Recommending Diamond without cap, risk, or integration evidence
- Using business-case numbers not provided by the client

## When Not To Use

- No Blueprint has been completed and no approved Engagement Baseline exists. Sell the Blueprint
  first, or route a Shopify-referred POS wedge through the Referral Scope Brief.
- The user asks for only a short follow-up email. Use `skills/kaizen-followup.md` or `skills/kaizen-email-exec.md`.
- The request is for an invoice or formal SOW document artifact. Use `skills/kaizen-invoice-exec.md`.

## Variant Depth Additions

### Anti-Selection Rules

- Do not write a proposal that does not trace back to Blueprint findings or an approved POS
  Delivery OS Engagement Baseline.
- Do not include implementation pricing without approved commercial inputs.
- Do not let Phase 2 AnyDB, ERP, app cleanup, or custom work slide into committed Phase 1 scope
  without explicit scope language.

### Known Failure Modes

- Proposal repeats diagnosis instead of converting it into scope.
- Gross fee, Blueprint credit, net investment, and payment schedule do not reconcile.
- Win themes appear in the executive summary but disappear from scope and risk sections.
- Risk register names generic risks instead of merchant-specific proof.

### Default Evidence Gates

- Blueprint findings and source evidence available, or approved POS Delivery OS Engagement Baseline
  with source artifact named.
- Pricing loaded from `reference/kaizen-pricing.md`.
- Win Theme Matrix completed before drafting.
- SOW references, section numbering, exclusions, and assumptions checked together.

### Operating Hooks

- Evidence Gate Hook for proof, business case, ROI, and risk claims.
- Task / Follow-Up Hook for missing approvals, pricing inputs, and client dependencies.
- Account Health / Expansion Hook only if this is a post-go-live expansion proposal.

### Output Shape By Mode

- Quick Read: proposal readiness, missing input, next action.
- Operator Analysis: scope recommendation, commercial risk, proof gaps, kill conditions.
- Client Deliverable: proposal/SOW-ready narrative with pricing and exclusions.
- Execution Artifact: proposal draft, SOW sections, pricing table, risk register, checklist.

### Source-Of-Truth And AnyDB Boundary

The source artifact is the commercial source of truth for why the work exists. Valid sources are a
Blueprint, Implementation Scoping Brief, approved Referral Scope Brief, or Engagement Baseline.
Shopify owns commerce execution where scoped. AnyDB is included when the source artifact proves
workflow state, approvals, exceptions, portals, or reporting need an operating layer.
