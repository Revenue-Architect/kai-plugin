# Good vs Bad: Migration Risk Section

Use when writing risk sections for Blueprint, proposals, runbooks, or client updates.

## Bad

"There is some risk around data quality and timing. KaizenCommerce will monitor the migration
closely and communicate with the client if issues arise."

## Why It Fails

- Generic
- No trigger
- No owner
- No mitigation
- Does not say when scope or timeline changes

## Good

"Product export quality is the main migration risk. If the Lightspeed export contains duplicate
SKUs, missing variant options, or inconsistent vendor names, import prep will take longer than the
standard Silver scope assumes.

Mitigation: run a Dry Run against a cleaned sample before finalizing the live import plan. If more
than 5 percent of product rows require manual correction, pause the timeline and issue a scope
review before continuing. Owner: KaizenCommerce for data triage, client for source-system cleanup
decisions."

## Why It Works

- Names the actual failure pattern
- Defines a measurable trigger
- Assigns owner
- Connects risk to scope and timeline
