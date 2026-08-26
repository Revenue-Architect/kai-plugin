# Kaizen AnyDB Architecture Examples

These are synthetic examples for Kai quality training. They are not Kaizen client artifacts.

## Example 1: Weak AnyDB Recommendation

Input:

```text
Client wants to manage vendor purchase orders and receiving. Shopify POS is used in stores.
```

Weak output:

```text
Create an AnyDB database for vendors, purchase orders, and receiving. Add automations for approvals
and vendor emails.
```

Why it fails:

- calls AnyDB a database
- starts with tables before workflow
- assumes automation readiness
- does not define Shopify boundary
- no statuses, owners, views, or failure handling

Strong output:

```text
AnyDB fit: likely yes, if Shopify and existing apps do not already own PO workflow.

Workflow:
1. Buyer drafts PO.
2. Manager approves if threshold is exceeded.
3. PO is sent to vendor.
4. Receiving team logs partial or complete receipt.
5. Exceptions are reviewed before Shopify inventory changes.

Source-of-truth boundary:
- Shopify remains product and inventory execution layer.
- AnyDB owns vendor, PO, approval, receiving, and exception workflow.

Core Types:
- Vendors
- Purchase Orders
- PO Line Items
- Receiving Logs
- Approval Requests
- Exceptions

Key statuses:
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

Automation verdict:
PARTIAL AUTOMATION ONLY until approval thresholds, vendor email owner, and inventory write-back path
are confirmed.

Next evidence needed:
- current PO spreadsheet
- approval thresholds
- receiving process
- whether Shopify inventory should be adjusted manually, by API, or not at all from this workflow
```

Why it works:

- workflow first
- source-of-truth boundary clear
- automation governed
- next evidence named

## Example 2: Special Orders State Model

Input:

```text
Jewelry retailer takes special orders in store. Staff write notes in POS and text vendors manually.
Owner wants visibility into what is stuck.
```

Good output:

```text
AnyDB role:
Operational control layer for special order status, vendor follow-up, and customer commitment.
Shopify remains the order/customer commerce record.

State model:

| State | Entered by | Exited by | Merchant sees | Kaizen/ops sees |
|---|---|---|---|---|
| Requested | staff creates special order | manager confirms feasibility | POS note or order tag exists | new record in special order queue |
| Confirmed | manager approves | PO/vendor request sent | customer commitment is recorded | owner, due date, vendor assigned |
| Ordered | vendor request sent | vendor acknowledges | staff can answer status | vendor follow-up date visible |
| In transit | vendor confirms shipment | item received | staff sees expected date | exception if ETA slips |
| Ready for pickup | item received | customer picks up | pickup status clear | open commitment ready to close |
| Exception | ETA missed or vendor issue | owner resolves | staff sees escalation state | manager queue shows blocker |

Handoff contract:
HANDOFF: Shopify order/tag -> AnyDB special order record
PAYLOAD: order ID, customer, item, requested date, staff owner, notes
SUCCESS RESPONSE: AnyDB record ID, status, owner
FAILURE RESPONSE: error, missing field, retryable flag
TIMEOUT: same business day -> treated as failure
ON FAILURE: assign manager review task
```

Why it works:

- shows states
- clarifies what each party sees
- defines handoff failure behavior
