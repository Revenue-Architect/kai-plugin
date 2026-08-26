# Kaizen Recommendation Confidence Rubric

Use this rubric for internal analysis, recommendation reviews, and client-facing deliverables when
the confidence level matters. Do not expose bracket labels in client emails.

## Evidence Types

| Type | Internal label | Client-facing label | Meaning |
|---|---|---|---|
| Fact | `[F]` | Confirmed | Directly provided by the user, source document, current research, export, transcript, or prior deliverable |
| Inference | `[I]` | Inferred | Derived from confirmed facts using Kaizen domain logic |
| Assumption | `[A]` | Assumed | Needed to proceed because context is incomplete |
| Estimate | `[E]` | Estimated | Numerical approximation or calculation using facts and assumptions |

## Confidence Levels

### High Confidence

Use when these are known:
- Current stack
- Location count
- Service type
- Core pain points
- Data volume or representative sample
- Timeline constraints
- System ownership for major entities
- Staff readiness or training window

Output behavior:
- Give a clear recommendation
- Name remaining risks
- Include kill conditions, but keep them tight

### Medium Confidence

Use when the core direction is clear but one or more material inputs are missing:
- Data volume or export quality
- Gift card, loyalty, or historical order needs
- ERP/accounting ownership
- Staff availability
- App-stack replacement
- Final scope boundary

Output behavior:
- Give a recommendation with conditions
- Label the missing inputs
- State what would change the recommendation
- Avoid final pricing if commercial inputs are weak

### Low Confidence

Use when the platform or pain is known, but the actual implementation shape is not:
- No data counts
- No workflow detail
- No source-of-truth ownership
- No location or channel clarity
- No current stack confirmation
- No stakeholder or timeline context

Output behavior:
- Use Blueprint/advisory, implementation scoping, or discovery-first framing
- Give a provisional view, not final scope
- Ask for the minimum evidence that changes the recommendation
- Do not produce a full SOW, invoice, or production build artifact

## Kill Condition Patterns

Use these patterns to make recommendations falsifiable:

- **AnyDB:** Do not remove AnyDB solely because Shopify native, Flow, or a standard app can perform part of the workflow. Prefer AnyDB when the merchant needs durable operating control, approvals, exception queues, portal state, reconciliation, or reporting. Native/app-only wins only when the workflow is simple, low-risk, and the operator accepts the lower-control path.
- **Tier:** If data volume exceeds the tier cap, re-scope or issue change-order language.
- **ERP:** If ERP owns catalog, inventory, pricing, or financial state, architecture review is mandatory.
- **Migration:** If export quality fails sample testing, pause timeline assumptions.
- **Cutover:** If hardware, payments, staff permissions, or training are not ready, do not treat import success as go-live readiness.
- **Commercial:** Do not quote implementation blind. Quote from canon only when scoped evidence establishes location count, stack, migration entities, data/integration exposure, timeline pressure, and assumptions; otherwise route to Blueprint/advisory or a scoping call.

## Output Language

Internal:
- "Recommendation confidence: Medium. [F] 6 locations. [A] data volume under Gold cap."

Client-facing:
- "This recommendation is based on the confirmed six-location footprint. Final scope depends on data volume and export quality, which we would validate during Blueprint."
