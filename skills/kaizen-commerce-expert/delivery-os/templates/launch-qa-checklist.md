# Template — Launch QA Checklist (per location)

Run once **per location**. A location does not go live until it passes or has a documented partner-approved exception. Owner: CTO validates · CEO signs. Governed by [Pack 3 — Launch QA](../03-launch-qa-pack.md).

> Parallel Validation holds: legacy POS stays live until this location is proven. Verify POS / payment / gift-card behavior in the actual system — do not assume. Tag uncertainty `[FLAG: verify current Shopify docs before client commitment]`.

**Location:** ______  **Date:** ______  **Validator (CTO):** ______  **Signoff authority (named):** ______  **Inventory threshold:** `[NEED: launch inventory-accuracy threshold]`

## Store-level (confirm once before first location)
- [ ] Store settings, taxes, currencies configured
- [ ] Channels configured or deferred (documented)
- [ ] Migrated data accepted from Pack 2
- [ ] Reporting baseline available

## Location readiness
- [ ] Location created and active
- [ ] Inventory accurate enough to launch (meets threshold)
- [ ] Hardware installed and paired
- [ ] Staff assigned with correct permissions

## Hardware / payment
- [ ] Terminals / readers paired and tested
- [ ] Receipt printer working
- [ ] Real test sale completed on hardware
- [ ] Processor live for region `[FLAG: verify current Shopify docs before client commitment]`

## Staff permissions
- [ ] Each role performs intended actions
- [ ] Restricted actions blocked for non-managers
- [ ] Manager override works as configured (verified in POS)

## Transactions
- [ ] Sale · discount · return · exchange · partial refund pass ([launch-test-pack](launch-test-pack.md))
- [ ] Gift card / store credit pass or limitation documented `[FLAG: verify current Shopify docs before client commitment]`

## Workflows
- [ ] Core POS workflow scripts pass — staff can complete ([launch-test-pack](launch-test-pack.md))

## Inventory & reporting
- [ ] On-hand by location within threshold; high-value SKUs spot-checked
- [ ] Core reports populate and match merchant expectations

## Integrations
- [ ] Every integration monitored or intentionally disabled (documented)

## Known issues (owner + severity)
| Issue | Severity (Critical/Important/Watch) | Owner | Status |
|-------|-------------------------------------|-------|--------|
| | | | |

**Gate:** no Critical open · all passed or partner-approved exception documented · [launch-signoff-form](launch-signoff-form.md) signed by the named authority.

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
