# Kaizen AnyDB Use Case Library

Use this reference when deciding whether AnyDB belongs in scope or when shaping an AnyDB spec.
This file is a pattern library, not a substitute for `kaizen-anydb-patterns.md`. Load the AnyDB
patterns file before writing exact cell types, formulas, or build instructions.

## Buyer-Facing Naming

Use AnyDB as the internal implementation platform. In buyer-facing sales, proposals, and
diagnostics, name the operating workflow first. The merchant should understand the business
surface before the platform.

| AnyDB-backed use case | Buyer-facing name |
|---|---|
| Vendor Purchase Order Control | Vendor Desk |
| Special Orders And Customer Commitments | Special Order Desk |
| Repairs And Service Queue | Service Desk |
| Inventory Exception Queue | Inventory Exception Hub |
| Migration QA / launch issue tracking | Cutover Command Center |

Acceptable phrasing:

- "Vendor Desk, powered by the operating layer we configure behind Shopify"
- "Inventory Exception Hub"
- "Cutover Command Center for launch and hypercare"

Avoid leading with:

- "We will build you an AnyDB"
- "AnyDB is the platform you are buying"
- "The project is an AnyDB implementation" unless the buyer specifically asks about the technical
  platform

## Use Case Format

For each use case, define:

- when to use
- do not use when
- source-of-truth boundary
- core Types
- important statuses
- views and roles
- automations
- handoffs
- failure modes
- success metrics

## Vendor Purchase Order Control

Use when:

- vendor ordering lives in spreadsheets, email, or one person's memory
- approvals are needed before ordering
- receiving is not tied to expected inventory
- managers need visibility into open POs and delays

Do not use when:

- Shopify or an existing inventory planning app already owns POs cleanly
- the merchant only needs simple reorder reminders
- vendor process is not mature enough to model

Source-of-truth boundary:

- Shopify owns product and inventory execution.
- AnyDB owns vendor, PO, approval, receiving, exception, and follow-up workflow.

Core Types:

- Vendors
- Purchase Orders
- PO Line Items
- Receiving Logs
- Approval Requests
- Exceptions

Statuses:

- Draft
- Pending approval
- Approved
- Sent to vendor
- Partially received
- Received
- Exception
- Closed

Views:

- Buyer queue
- Manager approval queue
- Receiving queue
- Vendor follow-up queue
- Exception queue

Automations:

- notify approver when PO exceeds threshold
- create receiving tasks when expected date approaches
- flag partial receiving after due date
- escalate vendor follow-up after no response

Handoffs:

- Shopify product read -> AnyDB PO line lookup
- AnyDB receiving exception -> Shopify inventory review task
- AnyDB vendor follow-up -> email or task queue

Failure modes:

- PO line references product that no longer exists
- receiving changes stock without Shopify validation
- approval threshold has no owner
- vendor email automation fires without human review where required

Success metrics:

- every open PO has owner and status
- receiving exceptions are visible
- approval cycle time is measurable
- Shopify inventory updates remain governed by the approved source-of-truth path

## Special Orders And Customer Commitments

Use when:

- customers order items not currently available in store
- staff need to track vendor ETA, customer communication, and pickup readiness
- Shopify order state alone does not show operational commitment status

Do not use when:

- Shopify native order notes, tags, and fulfillment statuses are sufficient
- the workflow has low volume and no operational risk

Source-of-truth boundary:

- Shopify owns order and customer commerce record.
- AnyDB owns special-order operational state, vendor follow-up, and commitment queue.

Core Types:

- Special Orders
- Special Order Line Items
- Vendor Follow-Ups
- Customer Updates
- Pickup Commitments

Statuses:

- Requested
- Confirmed
- Ordered
- Vendor acknowledged
- In transit
- Ready for pickup
- Picked up
- Cancelled
- Exception

Views:

- Store staff queue
- Manager exception queue
- Vendor follow-up queue
- Customer update queue

Automations:

- alert staff when ETA passes
- create customer update reminder
- flag missing vendor acknowledgement

Failure modes:

- customer promised date is not tied to vendor evidence
- staff update AnyDB but Shopify order note/tag remains stale
- vendor exception lacks owner

Success metrics:

- every active special order has next action and owner
- customer commitments are visible before pickup day
- exceptions are surfaced before customer escalation

## Repairs And Service Queue

Use when:

- products come back for repair, sizing, warranty, cleaning, or service
- staff need intake, status, customer updates, and pickup handoff
- service state is not visible in Shopify order history

Do not use when:

- service volume is low and a simple Shopify note is enough
- no one owns service follow-up

Source-of-truth boundary:

- Shopify owns customer and sale record.
- AnyDB owns service case state and operational follow-up.

Core Types:

- Service Cases
- Service Tasks
- Customer Updates
- Vendor/Workshop Records
- Pickup Logs

Statuses:

- Intake
- Assessment
- Awaiting approval
- In service
- Ready for pickup
- Completed
- Cancelled
- Exception

Views:

- Store intake queue
- Workshop queue
- Customer update queue
- Pickup queue

Automations:

- reminder when case has no update after threshold
- task when approval is needed
- notification when pickup-ready status is reached

Failure modes:

- customer communication happens outside the case record
- service item lacks photo or intake details
- ready-for-pickup queue is not reviewed daily

Success metrics:

- every service case has status, owner, and next update date
- overdue cases are visible
- customer pickup commitments are tracked

## Inventory Exception Queue

Use when:

- inventory mismatches recur but root causes vary
- store staff need a standard way to log discrepancies
- managers need trend visibility across locations

Do not use when:

- Shopify inventory adjustments and reports already resolve the issue
- the merchant wants AnyDB to become inventory master without architecture approval

Source-of-truth boundary:

- Shopify owns inventory execution.
- AnyDB owns exception intake, investigation, owner, and resolution workflow.

Core Types:

- Inventory Exceptions
- Products
- Locations
- Investigation Tasks
- Resolution Notes

Statuses:

- New
- In review
- Waiting on store
- Corrected in Shopify
- No change needed
- Escalated
- Closed

Views:

- Store exception intake
- Ops review queue
- Location trend view
- Product trend view

Automations:

- notify ops for high-value or repeated exceptions
- escalate stale exceptions
- generate weekly exception review task

Failure modes:

- staff use exception queue as replacement for proper Shopify adjustment workflow
- correction happens without evidence
- repeated exceptions are closed without root-cause review

Success metrics:

- exceptions have owner and resolution reason
- repeated SKU/location patterns are visible
- Shopify remains the inventory record of execution

## Migration QA Dashboard

Use when:

- migration has multiple files, jobs, retry queues, or validation reports
- QA evidence needs one operational view
- client or internal team needs clear pass/fail tracking

Do not use when:

- migration is small and file-based handoff is sufficient
- evidence can be reviewed faster in the existing run folder

Source-of-truth boundary:

- Migration files and logs remain source evidence.
- AnyDB owns QA workflow state, issue ownership, and sign-off readiness.

Core Types:

- Migration Entities
- Import Jobs
- Validation Checks
- Reconciliation Issues
- Retry Queues
- Sign-Off Gates

Statuses:

- Pending
- Running
- Failed
- Needs fix
- Retest ready
- Passed
- Signed off

Views:

- Entity readiness
- Blocking issues
- Retest queue
- Sign-off dashboard

Automations:

- assign owner when validation fails
- notify when retest is ready
- escalate critical issue before go-live gate

Failure modes:

- dashboard becomes a second source of counts instead of referencing evidence files
- issue status updates without retained proof
- sign-off gate bypasses validation evidence

Success metrics:

- every entity has latest evidence path
- blockers are owner-assigned
- sign-off depends on retained validation and reconciliation proof
