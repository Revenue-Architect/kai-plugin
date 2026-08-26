# Kaizen Retail Operations Patterns

Use this reference when Kai is diagnosing retail problems, preparing discovery, writing Blueprint
findings, scoping migrations, designing AnyDB workflows, or building post-go-live reports.

These are reusable retail operating patterns synthesized from agency-agents judgment patterns,
management-consulting decision-quality rules, and Kaizen's current positioning. They are not
client artifacts. Replace synthetic examples with real Kaizen examples when they become available.

## How To Use

For each merchant problem:

1. Identify the visible symptom.
2. Name the likely root-cause pattern.
3. Ask what evidence would prove or disprove it.
4. Tie the implication to revenue, labor, shrink, reporting, customer experience, or expansion risk.
5. Recommend Blueprint, architecture, migration, training, or reporting only after the pattern is supported.

## Pattern: Inventory Trust Gap

Visible symptoms:

- staff do not trust inventory shown in POS or ecommerce
- online orders get cancelled because store stock is wrong
- weekly manual counts are used to "fix" the system
- managers keep side spreadsheets for high-value products

Likely root causes:

- inventory adjustments happen outside the source system
- transfers, returns, damaged goods, or receiving workflows are not recorded consistently
- location mappings are wrong or too broad
- ecommerce, POS, ERP, and warehouse systems each hold partial truth
- staff permissions or habits make the official workflow hard to follow

Evidence to request:

- location-level inventory export
- recent cancelled orders or stockout examples
- transfer and receiving process notes
- return/exchange workflow
- list of systems that can change inventory

Kai judgment:

- Do not treat this as a "Shopify migration" problem until the write paths are known.
- If multiple systems can change inventory, require entity-level source-of-truth mapping.
- If staff workarounds are driving drift, include training and permissions in the fix.

## Pattern: Multi-Location Visibility Gap

Visible symptoms:

- store staff call other locations to check stock
- ecommerce cannot expose reliable pickup availability
- managers cannot see location-level sell-through
- transfers are manual, delayed, or undocumented

Likely root causes:

- locations are modeled inconsistently across systems
- inventory, fulfillment, and reporting use different location names or IDs
- transfer status does not update inventory at the right time
- staff lack a standard exception path when stock is wrong

Evidence to request:

- Shopify or legacy location list
- transfer records
- pickup/fulfillment rules
- location-specific inventory exports
- staff escalation process for stock discrepancies

Kai judgment:

- Location mapping is a migration gate, not an admin afterthought.
- Per-location reconciliation matters more than aggregate inventory totals.
- AnyDB may help manage exceptions, transfer requests, or receiving tasks, but Shopify should remain the inventory execution layer unless explicitly designed otherwise.

## Pattern: Manual Reporting Drag

Visible symptoms:

- leadership waits for weekly/monthly spreadsheets
- finance or ops exports reports manually
- store managers cannot see the same numbers as head office
- decisions depend on one person who knows the spreadsheet

Likely root causes:

- source systems do not agree on entity ownership
- reports combine sales, payouts, inventory, labor, and purchasing without stable keys
- Shopify, accounting, and operational tools are not reconciled
- manual reporting is hiding process gaps upstream

Evidence to request:

- sample reports
- source exports used to build them
- owner and cadence for each report
- decisions made from the report
- reconciliation rules and known exceptions

Kai judgment:

- Do not promise dashboards before the underlying source-of-truth and reconciliation rules are clear.
- Reporting value is strongest when tied to decisions: buying, staffing, replenishment, markdowns, or expansion.
- AnyDB is useful when the report requires operational workflow state, not just Shopify sales data.

## Pattern: Catalog Data Debt

Visible symptoms:

- duplicate SKUs, inconsistent variants, missing images, bad product types
- product handles collide during import
- staff search products differently by store
- ecommerce merchandising is hard because POS data is messy

Likely root causes:

- products were created ad hoc over many years
- SKU and variant conventions were never enforced
- ecommerce fields were retrofitted onto POS data
- legacy system exports collapse or split variant data unexpectedly

Evidence to request:

- product export
- variant/SKU uniqueness check
- sample products across top categories
- ecommerce merchandising requirements
- legacy product creation process

Kai judgment:

- Catalog cleanup is not cosmetic when it affects POS search, ecommerce merchandising, inventory, and migration success.
- A migration plan should separate data cleanup, import mechanics, and post-import merchandising.
- If product data is weak, timeline and scope confidence drop until sample validation is done.

## Pattern: Staff Muscle-Memory Risk

Visible symptoms:

- staff resist the new POS
- managers fear go-live day errors
- training is requested late
- "the old system was faster" becomes the default complaint

Likely root causes:

- training happens too early, too late, or on demo data
- old workflows are not mapped to new workflows
- staff are taught too many tasks at once
- permissions, hardware, and quick-reference materials are missing

Evidence to request:

- role list
- top POS workflows by frequency
- legacy workflow screenshots or steps
- go-live staffing schedule
- training availability by location

Kai judgment:

- Training is a go-live gate, not a support add-on.
- Use micro-sprints and one critical action per session.
- Train on real configuration and product data, not a blank store.

## Pattern: Gift Card And Liability Risk

Visible symptoms:

- gift cards are in use but balances are hard to export
- finance wants liability preserved
- staff are unsure how old cards redeem after go-live
- gift card import path is unclear

Likely root causes:

- legacy system lacks original issue amount or clean balance export
- balances are split across online and in-store tools
- codes are not compatible with the target path
- liability reconciliation owner is not assigned

Evidence to request:

- gift card balance export
- total liability report
- sample codes
- redemption workflow
- finance sign-off requirement

Kai judgment:

- Gift cards need financial reconciliation, not only import mechanics.
- If current balance is the only available value, state the business decision explicitly.
- Do not treat go-live as ready until redemption workflow and liability check are proven.

## Pattern: Workflow Ownership Gap

Visible symptoms:

- "everyone" handles exceptions
- tasks live in Slack, email, spreadsheets, and memory
- managers cannot tell which orders, vendors, or returns are stuck
- automations trigger messages but no one owns resolution

Likely root causes:

- no single operational queue
- no status model
- no owner field or escalation rules
- automation replaced notification but not accountability

Evidence to request:

- current exception examples
- who notices the problem
- who can fix it
- where status is tracked
- what happens when no one responds

Kai judgment:

- This is often an AnyDB fit when Shopify/Flow can record events but not manage ownership.
- Design statuses, owners, and views before automations.
- Automation without accountability makes the workflow less visible, not better.

## Pattern: Automation Readiness Gap

Visible symptoms:

- client asks to automate a process that is not stable manually
- there are many exceptions
- data needed for the trigger is missing or unreliable
- nobody watches failed runs

Likely root causes:

- business rule is not mature
- source of truth is unclear
- manual exception path is not documented
- logging and failure handling are missing

Evidence to request:

- current manual process
- exception frequency
- trigger data source
- owner and fallback
- test cases and failure examples

Kai judgment:

- Use `PARTIAL AUTOMATION ONLY` when automation can prepare, tag, notify, or queue but not safely decide.
- Use `DEFER` when source data, owner, or test path is unclear.
- Use `REJECT` when automation bypasses required approval or creates source-of-truth risk.
