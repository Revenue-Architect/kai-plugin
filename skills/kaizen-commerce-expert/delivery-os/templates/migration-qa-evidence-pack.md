# Migration QA Evidence Pack — Per-Entity Reconciliation → Verdict

Fill one entity block per migrated entity, then the verdict page. This document is the evidence
behind the go/no-go decision; an unfilled block means the entity is NOT verified. Default verdict
is **NOT READY** until evidence clears every gate. Produced during Phase 5 of the runbook
(`skills/kaizen-migrate.md`); rendered for client sign-off via kaizen-render when required.

## Entity Reconciliation Block (copy per entity)

```
ENTITY: [Products / Variants / Customers / Inventory by location / Gift cards /
         Historical orders / Custom data]
Lane used:            [api_to_api / matrixify_csv / shopify_admin_csv]
Source baseline:      [count]  captured [date]  from [export file + hash]
Target count:         [count]  via [R8 query / Matrixify results file]  at [timestamp]
Count parity:         [MATCH / DELTA: n]  Delta explanation: [required if any delta]

SPOT-CHECK SAMPLE     size [n — minimum 20 or 5%, whichever larger; selection: stratified,
                       not first-rows]
  Fields compared:    [list]
  Result:             [n/n pass]  Failures: [each one listed + disposition]

FINANCIAL TIE-OUT     [required for gift cards, store credit, order totals; n/a otherwise]
  Legacy sum:         [amount + currency]  (source: [file/report])
  Shopify sum:        [amount + currency]  (source: [query/report])
  Delta:              [must be 0.00 for liabilities — to the cent]
  ⚠ Net-zero is not pass: verify no offsetting per-record errors in the spot-check.

SERIAL/UNIT-LEVEL     [required for serialized inventory; n/a otherwise]
  Method:             [serial list diff]   Unmatched serials: [list or none]

Open [VERIFY] items:  [none / list — any open item blocks READY]
Entity verdict:       [READY / READY WITH NOTES / NOT READY] + one-line reason
```

## Verdict Document (one page, after all entity blocks)

```
MIGRATION QA VERDICT — [Client] — [Legacy] → Shopify POS
Date / Prepared by / Runbook version

| Entity | Count parity | Spot-check | Tie-out | Verdict |
|---|---|---|---|---|
| ...one row per entity block above... |

Overall verdict: [READY / READY WITH NOTES / NOT READY]
  - READY: every entity READY; zero open [VERIFY]; tie-outs at 0.00.
  - READY WITH NOTES: only non-blocking notes (cosmetic deltas, documented + accepted by client
    in writing). List each note.
  - NOT READY: any entity NOT READY, any open [VERIFY], any unexplained delta. List blockers +
    owner + retest plan.

Sign-off (both required before cutover proceeds):
  KaizenCommerce verification: [name, date]
  Client named contact acceptance: [name, date]
```

## Rules

- Evidence references files and queries, never memory ("counts matched" without the artifact is
  not evidence).
- Baselines come from Phase 1 frozen exports; if the source moved (live trading), re-freeze and
  re-baseline — never reconcile against a stale baseline.
- This pack feeds the Evidence Gate Hook: case-study or proposal claims about this migration
  cite this document per the proof bank's Provenance & Capture Schema.
