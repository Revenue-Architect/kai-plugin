# Kai Automation Governance

Use this reference when Kai recommends, designs, builds, audits, or validates AnyDB automations,
Shopify Flow workflows, API integrations, sync jobs, or operational automations.

## Verdicts

Choose exactly one governance verdict:

| Verdict | Meaning |
|---|---|
| `APPROVE` | High recurring value, controlled risk, clear owner, tested recovery path. |
| `APPROVE AS PILOT` | Plausible value, but limited rollout or measured trial required. |
| `PARTIAL AUTOMATION ONLY` | Automate safe segments and keep human checkpoints for high-risk steps. |
| `DEFER` | Process is not mature, value is unclear, or dependencies need stabilization. |
| `REJECT` | Weak economics or unacceptable operational, compliance, or customer risk. |

## Required Evaluation

Every automation recommendation must name:

- Business goal and current manual flow.
- Time savings or risk reduction expected.
- Data criticality: customer, order, inventory, finance, payment, staff, or compliance data.
- Source of truth for every field the automation reads or writes.
- Owner and escalation path.
- Trigger, validation, action, result verification, logging, and status writeback.
- Failure modes: wrong data, duplicate event, missing event, timeout, rate limit, auth failure, partial write.
- Fallback or manual recovery path.
- Test evidence required before production.

## Implementation Standard

Production-grade automations should include:

1. Trigger.
2. Input validation.
3. Data normalization.
4. Business logic.
5. External action.
6. Result validation.
7. Logging or audit trail.
8. Error branch.
9. Fallback or manual recovery.
10. Completion or status writeback.

## Naming And Versioning

Use explicit names for maintained workflows:

```text
[ENV]-[SYSTEM]-[PROCESS]-[ACTION]-v[MAJOR.MINOR]
```

Examples:

- `PROD-Shopify-LowStock-NotifyOps-v1.0`
- `TEST-AnyDB-POApproval-CreateShopifyTag-v0.4`

Avoid names such as `final`, `new test`, `copy`, or `fix2`.

## Test Baseline

Before production recommendation, require:

- Happy path test.
- Invalid input test.
- Duplicate event test.
- External dependency failure test.
- Timeout or retry test where relevant.
- Fallback or manual recovery test.
- Scale sanity check for realistic volume.

## Re-Audit Triggers

Re-audit an automation when:

- Shopify, AnyDB, Matrixify, or connected API behavior changes.
- Schema, formula, field name, or event payload changes.
- Error rate rises or repeated manual fixes appear.
- Volume increases materially.
- Compliance or ownership changes.
- Client adds a location, channel, ERP, WMS, 3PL, loyalty, or accounting integration.

## Client-Facing Rule

Do not describe an automation as final or safe because it is technically possible. State the
governance verdict, constraints, required tests, owner, and fallback in operational language.
