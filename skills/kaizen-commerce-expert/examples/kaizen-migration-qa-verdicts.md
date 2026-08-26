# Kaizen Migration QA Verdict Examples

These are synthetic examples for Kai quality training. They are not Kaizen client artifacts.

## Verdict: PASS

Input:

```text
Products source count: 12,480
Transformed rows: 18,920 variant rows
API attempted products: 12,480
API success: 12,480
API failures: 0
Inventory by location source count: 38,200
Inventory target count: 38,200
Spot checks: 25/25 passed
Rollback ledger: complete
```

Good verdict:

```text
Verdict: PASS

Evidence reviewed:
- source product export
- transformed product payload
- API job log
- inventory reconciliation extract
- 25 product/variant/location spot checks
- Created Resource Ledger

Reason:
Product counts reconcile from source through API success. Inventory by location reconciles exactly.
No failed rows, dead-letter records, or unresolved warnings remain. Spot checks passed.

Remaining notes:
- keep rollback ledger retained through hypercare
- run post-go-live inventory reconciliation after first trading day

Next action:
Proceed to the next go-live checklist gate.
```

Why it works:

- verdict is explicit
- evidence is named
- notes are not blockers
- next action is clear

## Verdict: PASS WITH NOTES

Input:

```text
Customers source count: 8,200
Imported: 8,198
Excluded: 2 records with no email or phone
Warnings: 46 duplicate phone warnings, all mapped to existing customer records
Rejected rows: 0
```

Good verdict:

```text
Verdict: PASS WITH NOTES

Evidence reviewed:
- customer source export
- customer transform log
- import result export
- duplicate phone warning group

Reason:
The two-record variance is explained and documented as exclusion. No rejected rows remain. Duplicate
phone warnings are non-blocking because customer merge policy uses email as primary key and phone as
secondary reference.

Watch item:
Customer service should know that phone-only customer lookup may be weaker for the 46 warning group.

Next action:
Retain exclusion log and proceed. No re-import required.
```

Why it works:

- does not fail explained variance
- distinguishes warning from blocker
- preserves operational note

## Verdict: FAIL

Input:

```text
Matrixify Dry Run product import.
18% rows failed.
Errors: duplicate handles, missing option values, invalid image URLs.
Client asks if we can proceed and fix after.
```

Good verdict:

```text
Verdict: FAIL

Blocking issues:
1. Duplicate handles can create or overwrite the wrong products.
2. Missing option values can break variant structure.
3. Invalid image URLs indicate source media will not publish as expected.

Do not proceed to live import.

Required fix path:
1. Stop additional imports.
2. Preserve original file, transformed file, Dry Run result, and error export.
3. Group failures by root cause.
4. Fix handle generation and option mapping first.
5. Decide whether images are in scope for launch or post-launch.
6. Re-run Dry Run on corrected file.

Next action:
Run targeted data prep repair on failed product rows and return with the new Dry Run export.
```

Why it works:

- refuses unsafe live import
- names why each failure matters
- gives sequence

## Verdict: NOT READY

Input:

```text
API job says success. No source count, no transformed count, no reconciliation extract.
```

Good verdict:

```text
Verdict: NOT READY

Reason:
The API job success message is not enough evidence for sign-off. Kai cannot verify whether all
source records were attempted, transformed correctly, created/updated correctly, or reconciled in
Shopify.

Missing evidence:
- source entity count
- transformed payload count
- attempted/succeeded/failed API count
- dead-letter or retry queue status
- Shopify post-load count
- spot-check or reconciliation extract

Next action:
Collect the missing evidence and rerun migration QA. Do not treat this as PASS until counts and
reconciliation exist.
```

Why it works:

- does not convert confidence into evidence
- names exact missing proof
