# KaizenCommerce Firm Strategy Reference

Reference file for the kaizen-commerce-expert skill. Load this when Kai is answering internal
firm-building questions: utilization, hiring, bench risk, productized offers, reusable IP,
value pricing, partner ecosystem, co-sell, or agency operating model decisions.

This is an internal strategy layer. It supports KaizenCommerce business decisions and should not
override client-facing commercial guardrails, pricing rules, evidence gates, or the two-lane
discipline.

---

## Work-Type Model

The model below is a structural default, not a statement of KaizenCommerce actual margins or
staffing mix. Use real hours, rates, and delivery history before making a recommendation.

| Type | What it means | KaizenCommerce mapping | Economic profile |
|---|---|---|---|
| Brains | Novel, high-expertise, custom judgment | Diamond and enterprise custom integration development, net-new AnyDB architecture, unusual source-of-truth decisions | Highest price potential, lowest staffing depth, partner-heavy |
| Grey Hair | Experienced execution of a known-hard problem | Silver and Gold POS migrations, standard AnyDB builds, DTC or B2B operating architecture after a Blueprint | Moderate reuse, judgment-driven, trainable with senior oversight |
| Procedure | Systematized, repeatable work | Blueprint diagnostic, templated AnyDB modules, API migration mapping kits, Matrixify mapping kits when that lane is selected, Flow workflow libraries, store configuration checklists | Highest repeatability, best candidate for templates, junior delivery, or fixed-scope packages |

KaizenCommerce starts structurally Brains-heavy because partner expertise is the product. The path
to more durable revenue is to move recurring work down the stack: turn repeated migrations,
AnyDB modules, Flow patterns, QA checks, and report formats into Procedure while reserving partner
time for Brains work, sales, QA, and final strategy.

## Utilization Defaults

These are operating defaults for analysis, not confirmed targets.

| Role | Structural target band | Reason |
|---|---:|---|
| Partners in a 3-partner shop | 35-55% billable | Partners must also sell, scope, manage, QA, build partner channels, and protect client strategy. |
| First delivery hire | 60-75% billable | Delivery staff need enough paid work to justify fixed cost, with some non-billable time for training, QA, and process building. |
| Senior delivery lead after the first hire | 50-65% billable | A lead carries delivery, training, standards, estimates, and project oversight. |
| Specialist contractor | 50-70% billable while active | Contractors should absorb bounded work without creating permanent bench risk. |

The bench problem has two sides. Idle staff burn cash. No delivery bench forces partners to turn
away work or leave sales to do repeatable delivery. The default first-hire trigger is two
consecutive months where Procedure or Grey Hair work is being turned away, delayed, or forcing
partners off sales. Do not hire from a single busy spike.

## Value Pricing Principle

Price against the value of the client outcome, not the hours KaizenCommerce spends delivering it.
When the outcome changes the client's economics, quantify that outcome in the client's own
numbers and label any estimate before using it.

The two-lane model already supports value pricing: the scoping call or diagnostic clarifies the problem, validates
scope, and prevents the implementation from being sold as a commodity bid.

## Partner Posture

KaizenCommerce should treat ecosystem growth as a warm-introduction system, not a logo-collecting
exercise. The best partners send multi-location, operationally complex merchants that match the
ICP and need trusted implementation judgment. Shopify, app vendors, ERPs, 3PLs, agencies, and
consultants can all extend reach when they complement the core offer and do not pull the firm
toward low-complexity work.

## Firm-Building Routing

| User need | Load |
|---|---|
| Utilization, capacity, bench, first hire, margin, value pricing, profit per person | `../skills/kaizen-firm-economics.md` |
| Productizing a service, creating reusable IP, packaging an accelerator, tightening sales posture | `../skills/kaizen-productize.md` |
| Shopify partner motion, ISV co-sell, nearbound accounts, referral ecosystem, alliance selection | `../skills/kaizen-partner-ecosystem.md` |
| Preventive SOW boundaries, exclusions, data caps, approval gates before an engagement starts | `../skills/kaizen-scope.md` plus proposal or invoice skill as needed |

## Guardrails

- NEVER present structural defaults as KaizenCommerce actuals.
- ALWAYS ask for or label real inputs before calculating hiring, pricing, margin, or capacity.
- NEVER let firm-building advice weaken the two-lane commercial model, ICP boundaries, pricing source
  of truth, or delivery quality standard.
- For current Shopify Partner Program specifics, verify live sources before advising on tiers,
  benefits, application requirements, incentives, or directory rules.
