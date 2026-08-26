# Kaizen Blueprint Finding Bank

Use this reference to turn discovery notes into sharper Blueprint findings. These are synthetic
finding patterns, not client artifacts. Replace or extend them with real Kaizen findings when real
Blueprints, transcripts, and outcomes are available.

**Provenance:** findings are `[SYN]` patterns unless marked otherwise; the 2026-06-10 seeding
session landed the first `[REAL]` finding and `[REAL]` instances (below). Tagging scheme,
required fields for `[REAL]` entries, and the proposal-safe hard gate live in
`reference/kaizen-proposal-proof-bank.md` (Provenance & Capture Schema) — one authority for
both banks. New real findings enter via `Close Client`, approval-gated, anonymized by default.

## Finding Format

Each Blueprint finding should answer:

- finding: what is happening
- evidence signals: what supports it
- likely root cause: why it happens
- business implication: what it costs or risks
- recommendation path: discovery, Blueprint, migration, AnyDB, Flow, training, reporting, or hold
- kill condition: what would change the recommendation
- next evidence question: the smallest input that improves confidence

## Finding: Inventory Cannot Be Trusted Across Locations

Evidence signals:

- staff manually call stores before promising stock
- ecommerce availability causes cancellations or customer service issues
- inventory is manually corrected at a regular cadence
- store-level counts do not match central reporting

Likely root cause:

- inventory write paths are not controlled by one source of truth
- receiving, returns, transfers, or damages are not recorded consistently
- location mappings or staff workflows differ by store

Business implication:

- lost sales from cancelled orders
- staff time spent verifying stock
- customer trust erosion
- buying and replenishment decisions based on weak data

Recommendation path:

- require source-of-truth mapping before migration scope is final
- validate inventory per SKU per location
- include staff workflow and permissions in cutover readiness
- consider AnyDB only for exception queue or receiving workflow, not as inventory master by default

Kill condition:

- if a sample export proves location-level inventory is accurate and staff follow one workflow, downgrade this from core finding to watch item

Next evidence question:

- "Show three recent inventory mismatches and how each was corrected."

## Finding: Manual Reporting Is Masking Process Gaps

Evidence signals:

- leadership waits for spreadsheets to know performance
- reports require manual exports from multiple systems
- only one person understands the report logic
- report numbers are disputed by operations or finance

Likely root cause:

- system ownership and reconciliation rules are unclear
- reports are compensating for weak workflow state
- operational events are not captured at the point of work

Business implication:

- slow decisions
- finance or ops time spent rebuilding truth
- weak visibility into margin, inventory, staffing, or expansion readiness

Recommendation path:

- map source systems and decision use cases before dashboard work
- define report owner, cadence, and reconciliation rule
- consider AnyDB when the missing input is workflow state, owner, approval, or exception status

Kill condition:

- if reports come from one trusted source with low manual manipulation, focus on report design rather than workflow architecture

Next evidence question:

- "What decisions are delayed until this report is finished?"

## Finding: Catalog Data Debt Threatens Migration Quality

Evidence signals:

- duplicate SKUs or handles
- missing option values
- inconsistent variant naming
- product records lack ecommerce-ready fields
- high manual cleanup expected before import

Likely root cause:

- legacy product creation rules were inconsistent
- POS data was not designed for ecommerce merchandising
- variant and SKU conventions changed over time

Business implication:

- migration errors
- staff search friction
- product visibility problems online or in POS
- timeline risk from unplanned cleanup

Recommendation path:

- require sample catalog audit before timeline confidence
- separate cleanup, import, and merchandising scope
- make catalog validation a pre-import gate

Kill condition:

- if representative sample validation clears SKU, handle, variant, price, tax, and image checks, reduce migration risk rating

Next evidence question:

- "Can we review a current product export plus 20 representative products across top categories?"

Real instances (`proposal-safe: no`, internal reasoning only):

- `[REAL:JAZ-2026]` (2026-06-01, apparel ecom / franchise B2B, confidence high): product truth
  split across THREE legacy sources — ERP as SKU authority, the storefront platform holding
  images/descriptions/categories, and an internal Access database augmenting exports. Migration
  mapping must reconcile all three; order-history scope wavered 2 vs 4 years (~100K orders).
- `[REAL:SGP-2026]` (2026-06-03 retro, food producer, confidence high): source-data audit
  happened after commitment — "finding out later what a mess it is." Cleanup scope discovered
  mid-delivery instead of during discovery. Reinforces: sample export walkthrough is a
  discovery-phase gate, and the merchant's cleanup duties go in the scope document.
- `[REAL:KZ-2026]` (2026-04-08, kitchen/home big-ticket retail, confidence high): the ~600 SKUs
  the merchant wanted to "migrate" did not exist in any catalog — no documented record at all
  ("can't import stuff that doesn't exist"). The extreme end of catalog debt: catalog CREATION
  is a separate, merchant-dependent workstream, never bundled silently into migration scope.

## Finding: Concurrent ERP + Commerce Cutover Is A Compound Risk `[REAL:JAZ-2026]`

Source: apparel ecom / franchise B2B engagement (JAZ) · date observed 2026-05-21→06-01 ·
confidence high · **proposal-safe: no**.

Evidence signals:

- new ERP launching at the same moment as the new commerce platform, on a fixed go-live date
- integration testing depends on the ERP being usable — a dependency outside the commerce
  project's control
- prior platform attempt abandoned mid-implementation (delayed, overly complex)
- custom middleware proposed for inventory/order sync between two systems that are BOTH new

Likely root cause:

- vendor contract or fiscal-year pressure forcing both replacements into one window
- sunk-cost recovery from the abandoned implementation compressing the new timeline

Business implication:

- a slip in either system slips both; no stable system to reconcile against during cutover
- launch-day incidents have two candidate root systems — triage time doubles

Recommendation path:

- name the dual cutover as the project's core risk in the Blueprint, not a footnote
- sequence: prove ERP usable in test before commerce integration freeze; define oversell
  prevention and daily reconciliation BEFORE launch traffic
- stage rollback positions per system — never assume a joint rollback

Kill condition:

- if the ERP go-live can be decoupled (even by weeks), downgrade to standard integration risk

Next evidence question:

- "What is the earliest date the ERP test environment is usable with production-shaped data?"

## Finding: Source Of Truth Is Entity-Specific, Not Platform-Wide

Evidence signals:

- Shopify, ERP, POS, accounting, apps, and spreadsheets each own part of the operation
- client asks whether "Shopify can be the source of truth" broadly
- updates happen in more than one system
- conflicts are resolved manually

Likely root cause:

- entity ownership has not been defined
- sync direction and cadence are unclear
- exceptions such as refunds, partial fulfillment, tax, and inventory adjustments are not designed

Business implication:

- overwritten data
- reconciliation work
- unstable reporting
- integration risk after migration

Recommendation path:

- create entity-level source-of-truth matrix
- define write paths, conflict rules, and reconciliation owner
- use Shopify as commerce execution layer where appropriate
- keep AnyDB as operational/spec layer unless justified otherwise

Kill condition:

- if one system clearly owns all relevant entities and integrations only read from it, simplify architecture

Next evidence question:

- "Which systems can create or update products, inventory, customers, orders, and payouts today?"

## Finding: Staff Readiness Is A Go-Live Risk

Evidence signals:

- training is not scheduled
- staff roles are unclear
- hardware or permissions are not configured
- legacy workflows differ materially from Shopify POS
- go-live depends on a small group of superusers

Likely root cause:

- training treated as documentation rather than operational readiness
- workflows are not role-specific
- staff have not practiced real transactions on real configuration

Business implication:

- checkout errors
- slower lines
- avoidable support tickets
- manager confidence loss during cutover

Recommendation path:

- role-based training with micro-sprints
- quick-reference cards for register use
- readiness test before go-live
- hardware, permissions, and product data configured before training

Kill condition:

- if all roles pass practical transaction tests at every location, downgrade to post-go-live support watch item

Next evidence question:

- "Who needs to process sales, returns, discounts, gift cards, cash close, and inventory adjustments on day one?"

## Finding: Automation Request Is Premature

Evidence signals:

- client asks to automate a process with many exceptions
- rule owner is unclear
- trigger data is unreliable
- no one monitors failed automation runs

Likely root cause:

- manual process is not stable enough to encode
- ownership, fallback, and logging are missing
- the desired automation may be masking a workflow-design problem

Business implication:

- hidden failures
- wrong updates to Shopify or AnyDB
- customer-visible mistakes
- support burden after launch

Recommendation path:

- classify automation as APPROVE, APPROVE AS PILOT, PARTIAL AUTOMATION ONLY, DEFER, or REJECT
- stabilize workflow manually first when needed
- automate safe preparation, tagging, or notification before final decisions

Kill condition:

- if trigger data, owner, fallback, logging, and tests are clear, automation can move from DEFER to pilot or approval

Next evidence question:

- "What happens today when this process fails, and who owns the fix?"

## Finding: Account Pricing Is Maintained By Hand `[SYN]`

Evidence signals:

- price lists live in spreadsheets, emailed to buyers or reps on request
- a named person is the only one who knows why an account gets its price
- price changes reach some accounts late, or not at all
- reps quote from memory or from a stale PDF
- disputes at invoicing about what price was agreed

Likely root cause:

- pricing was never modeled as data, so it accumulated as exceptions
- the ERP holds cost and list price but not negotiated account price
- no system enforces which account sees which price at order time

Business implication:

- margin leaks through stale or wrong prices
- invoicing disputes consume finance and sales time
- the pricing owner is a single point of failure
- the merchant cannot add accounts without adding manual work

Recommendation path:

- count distinct pricing tiers before recommending anything. This is the number that decides architecture
- check it against the plan ceiling: non-Plus allows 3 active catalogs assigned via Markets, Plus allows unlimited plus direct company assignment
- if tiers fit, this is native catalog and price list work
- if tiers exceed the ceiling, name the fork: consolidate tiers, upgrade to Plus, or move pricing governance into the operating layer
- never scope per-company pricing below Plus as though it were configuration

Kill condition:

- if the merchant actually runs 2 or 3 real tiers and the rest is noise, this is a native configuration job, not an engagement

Next evidence question:

- "Export the current price lists. How many genuinely distinct tiers are there, and who approves a new one?"

## Finding: Order Intake Is Re-Keyed Into The ERP `[SYN]`

Evidence signals:

- orders arrive by email, phone, or PDF and someone types them into the ERP
- reps enter orders on behalf of buyers who have no login
- order acknowledgements are manual
- errors surface at picking or invoicing rather than at entry
- the merchant measures order volume in hours of admin time

Likely root cause:

- no buyer-facing ordering surface exists, so humans are the integration
- the ERP was never exposed to buyers and nobody wanted to build a portal
- account-specific pricing made self-serve feel impossible

Business implication:

- order entry cost scales linearly with volume
- keying errors reach the customer as wrong shipments
- order-to-cash cycle stretches with manual handoffs
- growth is capped by admin headcount

Recommendation path:

- quantify current re-keying: orders per week times minutes per order. This is the number the proposal is built on
- map the target ordering model: buyer self-serve, rep-assisted draft orders, or both
- define the ERP release trigger and, explicitly, the failure path when release fails
- confirm the merchant knows automatic payment capture is not supported on B2B checkouts and name who captures manually

Kill condition:

- if order volume is low and stable, and the real problem is pricing rather than intake, do not lead with a portal

Next evidence question:

- "How many orders came in last week, through what channel, and how long did each take to enter?"
