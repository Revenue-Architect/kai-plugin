# Kaizen QBR And Account Health Examples

These are synthetic examples for Kai quality training. They are not Kaizen client artifacts.

## Example 1: Green Account

Input:

```text
30 days after Shopify POS go-live. 4 stores live. Inventory discrepancy tickets dropped from 18 in
week 1 to 3 in week 4. Staff completed training. Owner asks about purchase order workflow.
```

Good output:

```text
Account Health: Green

Evidence:
- all 4 stores live
- discrepancy tickets declined from 18 to 3 over first month
- staff training complete
- owner is asking about next operational workflow

Interpretation:
The account is stable enough to discuss expansion, but the expansion should be tied to the next
workflow bottleneck, not a generic retainer upsell.

Expansion signal:
- Signal: owner asks about PO workflow
- Context: POS migration is stable enough that attention has moved to back-office operations
- Timing: post-go-live stabilization is complete enough for discovery
- Stakeholder alignment: owner is engaged

Recommended QBR focus:
1. value delivered during go-live
2. remaining inventory watch items
3. purchase order workflow discovery
4. mutual action plan for AnyDB Blueprint or operational scoping
```

Why it works:

- separates health from expansion
- uses evidence
- confirms all four expansion signal fields

## Example 2: Yellow Account

Input:

```text
Go-live succeeded, but managers still ask support for returns and discounts. Inventory is mostly
accurate. Sponsor has not joined the last two check-ins. Staff say training was too rushed.
```

Good output:

```text
Account Health: Yellow

Reason:
The system appears operational, but adoption and sponsor engagement are weak. Expansion should be
deferred until staff confidence and executive sponsorship stabilize.

Risks:
- managers still depend on support for common workflows
- sponsor engagement is slipping
- rushed training may create recurring support tickets

Recovery plan:
1. run targeted manager micro-sprint for returns, discounts, and closeout
2. schedule sponsor touchpoint with a concise status brief
3. track support ticket volume for two weeks

Expansion:
Deferred. Do not pitch new workflows until adoption risk is under control.
```

Why it works:

- blocks expansion despite some positive signals
- names recovery actions
- treats adoption as account health

## Example 3: Red Account

Input:

```text
Client is live but gift card balances are disputed. Owner is upset. Support tickets are increasing.
Inventory confidence is mixed. Team asks whether to pitch retainer.
```

Good output:

```text
Account Health: Red

Reason:
There is an unresolved trust issue around gift card liability and support volume is increasing.
This is a save-play account, not an expansion or retainer pitch moment.

Immediate actions:
1. reconcile gift card liability with source export, Shopify result, and finance owner
2. create issue list with severity, owner, and next update time
3. send a factual client update only after reconciliation path is clear
4. pause expansion and retainer language

Do not say:
"Now is a good time to discuss ongoing support."

Safer stance:
"The priority is to resolve the gift card discrepancy, show the reconciliation evidence, and agree
on the next update point."
```

Why it works:

- does not pitch expansion on a Red account
- names trust repair before commercial motion
- ties action to evidence
