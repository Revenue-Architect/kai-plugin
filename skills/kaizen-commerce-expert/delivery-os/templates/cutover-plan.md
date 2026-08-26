# Template — The Kaizen Cutover & Rollback Plan

The phase plan for Shadow, Pilot Store, Verdict Gate, Waves, and Hypercare, plus the recovery plan
if the migration cannot proceed. Owner: CTO executes · CEO manages client comms · merchant owner
validates. Governed by [Pack 2 — API-First Migration](../02-api-first-migration-package.md) §8 &
§10 and [`reference/kaizen-cutover-methodology.md`](../../reference/kaizen-cutover-methodology.md).

> **Controlled cutover:** the legacy POS stays live and authoritative until Shopify is proven. Do
> not decommission legacy on cutover day. Data is validated before cutover is called done. This is
> not a risk-free launch promise.

**Client:** ______  **Cutover window:** ______  **Go/no-go owner:** CTO  **Merchant validator:** ______

## Pre-cutover gate (all must pass)
- [ ] Dry Run passed against approved tolerance
- [ ] Exception log cleared of Criticals
- [ ] Source + Shopify access confirmed
- [ ] Rollback section below ready and owner assigned
- [ ] Cutover window confirmed inside any Engagement Baseline launch constraint (season / lease / fiscal close)
- [ ] Reconciliation tolerance partner-approved `[NEED: reconciliation tolerance]`

## Execution sequence
| Step | Entity | Owner | Validate before next step | Done |
|------|--------|-------|---------------------------|------|
| 1 | (runbook order) | CTO | counts + spot-checks | |

## Cutover phase plan

| Phase | Scope | Owner | Exit evidence | Status |
|---|---|---|---|---|
| Shadow | Target data path configured while legacy remains authoritative | CTO | Dry Run passed, entity map confirmed, Criticals cleared | |
| Pilot Store | Representative location proves staff workflow and data path | CTO + merchant validator | Pilot verdict signed or hold reason documented | |
| Verdict Gate | Partner decision to wave, hold, or rework | CTO + CEO | Open defects classified, rollback path confirmed, partner signoff | |
| Waves | Remaining launch groups executed with runbook and issue log | CEO + CTO | Per-wave signoff and reconciliation check | |
| Hypercare | Post-launch issue monitoring and handoff | CEO | Warranty / Ops Care / change-order route documented | |

## Acceptance
- [ ] Post-cutover reconciliation passed
- [ ] Spot-checks passed per entity
- [ ] Merchant validator confirms
- [ ] Cutover declared accepted (legacy remains live until go-live signoff in Pack 3)

If acceptance fails → invoke the Rollback section below. Hand off to [Pack 3 — Launch QA](../03-launch-qa-pack.md).

---

## Rollback (operational recovery — not a platform guarantee)

Rollback does **not** mean Shopify automatically reverts writes. It is an operational decision to keep running on legacy. Owner: CTO calls it · CEO notifies locations.

> The strongest rollback is a Dry Run that prevents needing one. Where reversing a specific Shopify write is in question, tag `[FLAG: verify current Shopify docs before client commitment]`.

**Decision point:** invoke when post-cutover reconciliation fails the approved tolerance, or a Critical exception surfaces that cannot be resolved inside the window.

**What rollback IS:**

- Legacy POS is still live and authoritative (Parallel Validation) — operations continue on legacy
- Cutover is declared not-accepted; the new system does not become the source of truth
- Recovery actions: halt the load · isolate failed entities · correct · re-run on the next window
- Interim plan for the merchant while on legacy

**What rollback is NOT:**

- Not Shopify auto-undoing writes
- Not instant total reversal of all migrated data
- Not a substitute for a passing Dry Run

**Recovery checklist:**

- [ ] Load halted, failed entities isolated
- [ ] Root cause logged in [exception-log](exception-log.md)
- [ ] Merchant + locations notified; interim legacy process confirmed
- [ ] Correction made and re-tested on sample
- [ ] Next cutover window agreed

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
