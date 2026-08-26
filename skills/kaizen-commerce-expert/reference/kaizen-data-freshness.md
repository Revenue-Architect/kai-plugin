# KaizenCommerce Data Freshness Protocols

Reference file for the kaizen-commerce-expert skill. Loaded on demand by `kaizen-architect`, `kaizen-flow`, `kaizen-migrate`, `kaizen-anydb-build`, and `kaizen-reconcile` when designing integration architecture or specifying source-of-truth boundaries.

---

## Data Freshness Protocols

When designing integration architecture, apply these defaults:

| Entity | Default Update Type | Freshness Target | Validation | Repair Path |
|---|---|---|---|---|
| Orders | Event-driven | Immediate / near real-time | Record arrival + status checks | Retry, requeue, manual review |
| Payments & Refunds | Event-driven + reconciliation | Immediate + daily tie-out | Financial status comparison | Retry, reconcile, escalate |
| Inventory | Event-driven + reconciliation | Near real-time | Quantity + location comparison | Retry, queue exceptions, daily balance |
| Shipments | Event-driven | Near real-time | Tracking + status comparison | Retry, carrier-status review |
| Products & Variants | Scheduled or event-driven | Hourly to daily | Changed record comparison | Reprocess changed records |
| Price/Cost data | Scheduled | Hourly to daily | Changed field audit | Re-run batch or manual correction |
| Customers | Event-driven + dedupe | Near real-time | Identity + key match review | Merge review, exception handling |
| Payouts/Accounting | Scheduled + reconciliation | Daily / end-of-day | Tie-out + completeness | Re-export, reconcile, finance review |
| Vendor/PO reference | Scheduled | Daily to weekly | Count + change review | Re-run batch |

### Source-of-Truth Heuristics
1. Origin of the business event
2. System already used for operational reconciliation
3. System with cleanest keys and lowest manual overwrite risk
4. System downstream teams trust for audit/finance
5. If no single source stable, declare split ownership explicitly
