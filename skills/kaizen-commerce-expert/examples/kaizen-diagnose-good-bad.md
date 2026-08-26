# Kaizen Diagnose Good/Bad Examples

These are synthetic examples for Kai quality training. They are not Kaizen client artifacts.

## Example 1: Weak Notes To Blueprint Direction

Input:

```text
Merchant has 3 stores. Old POS. Inventory is bad. Reporting is manual. Owner wants Shopify.
```

Weak output:

```text
The merchant should move to Shopify POS because it will improve inventory, reporting, and store
operations. We recommend a migration project with training and reporting setup.
```

Why it fails:

- repeats the notes without diagnosis
- does not identify root cause
- invents readiness for implementation
- does not separate confirmed facts from assumptions
- does not ask for the next evidence that changes scope

Strong output:

```text
Recommendation confidence: Low to Medium.

Confirmed:
- 3 stores
- current POS is old
- inventory accuracy is a known pain
- reporting is manual
- owner is interested in Shopify

Diagnosis:
The operating issue is not simply "old POS." The likely problem is that inventory and reporting are
not trusted enough to run multi-store decisions. Before recommending a migration scope, Kai needs to
know whether inventory drift comes from receiving, returns, transfers, ecommerce sync, staff
adjustments, or weak product data.

Business implication:
If inventory remains unreliable, Shopify POS alone will not fix the operating behavior. The
merchant may migrate bad workflows into a better platform and still have stockouts, manual checks,
and weak replenishment decisions.

Next evidence needed:
1. current POS name and export quality
2. product and inventory counts by location
3. how receiving, returns, and transfers are handled today
4. whether ecommerce is in scope
5. whether the owner, ops lead, or store managers feel the pain most

Next action:
Run Blueprint discovery focused on inventory source of truth, location mapping, data quality, and
staff workflows before quoting implementation.
```

Why it works:

- treats weak notes as weak evidence
- avoids premature implementation scope
- names likely root-cause branches
- makes the next discovery action specific

## Example 2: Discovery Notes With Real Pain

Input:

```text
4 locations. Lightspeed POS. Shopify ecommerce. Staff say online inventory is wrong every week.
Manager exports reports every Friday and spends 5 hours reconciling. Owner wants to open 2 more
locations next year. Gift cards are active. No ERP.
```

Weak output:

```text
This is a strong Shopify POS opportunity. They should migrate to Shopify POS and consolidate
inventory and reporting. We should propose Gold.
```

Why it fails:

- jumps to tier before data volume and gift card risk are known
- misses expansion pressure
- misses weekly reconciliation cost
- does not flag gift cards as a gate

Strong output:

```text
Core finding:
The merchant is running omnichannel retail without a trusted inventory and reporting layer. The
weekly 5-hour reconciliation task is evidence that the current stack cannot produce decision-ready
truth without manual repair.

Root cause hypothesis:
Lightspeed POS and Shopify ecommerce likely do not share inventory state cleanly enough across four
locations. The exact root cause could be sync timing, location mapping, receiving/returns process,
or catalog mismatch. Gift cards add financial liability risk and must be validated separately.

Implication:
Opening two more locations would multiply the current reconciliation burden and increase the risk
of online stock promises that stores cannot fulfill.

Recommendation:
Proceed to Blueprint with migration-readiness focus. Do not quote final implementation until product
count, customer count, gift card export quality, inventory by location, and ecommerce requirements
are reviewed.

Kill conditions:
- If gift card balances cannot be exported or reconciled, scope/timeline changes.
- If Shopify ecommerce product data conflicts with Lightspeed product data, catalog cleanup becomes
an explicit workstream.
- If staff workflows are causing inventory drift, training and permissions are part of the fix.
```

Why it works:

- turns facts into diagnosis
- preserves uncertainty
- ties risk to expansion
- names gates before proposal
