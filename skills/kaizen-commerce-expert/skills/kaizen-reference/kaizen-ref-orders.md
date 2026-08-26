---
name: kaizen-ref-orders
description: "Deep retail reference for orders questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["orders domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3D. Order Management & Fulfillment

---

#### Order Management

##### What Is an OMS?

An Order Management System (OMS) is the central nervous system connecting customer orders to inventory and fulfillment. It answers: "Where should this order be fulfilled from, and how?"

```
Order Capture -> Routing -> Fulfillment -> Shipping -> Returns
```

##### Distributed Order Management (DOM)

DOM is the intelligence layer that routes orders across multiple fulfillment nodes. Key decisions:

| Decision | Factors |
|----------|---------|
| Where to fulfill | Inventory availability, proximity, shipping cost, fulfillment capacity |
| How to fulfill | Ship, BOPIS, local delivery, ship-from-store |
| When to split | Split across locations vs hold for consolidated shipment |
| Backorder handling | Wait for stock vs partial ship + backorder |
| Cancellation/modification | Order changes before fulfillment starts |

##### Shopify's Native Order Management

| Capability | Description | How It Works |
|-----------|-------------|-------------|
| Multi-channel order capture | Orders from online, POS, B2B, draft orders, external channels | All orders flow into unified order list |
| Automatic order routing | Routes orders to optimal fulfillment location | Based on inventory availability + proximity rules |
| Fulfillment orders | Per-location fulfillment assignments | One fulfillment order per inventory location |
| Split fulfillment | Orders split across multiple locations | Automatic when items are at different locations |
| Fulfillment holds | Hold orders before routing to fulfillment | Useful for fraud review, address verification |
| Order editing | Add/remove items, change shipping after order placed | Admin + API support |
| BOPIS fulfillment | In-store pickup with pick & pack verification | POS Pro; barcode scanning (2026+) |
| Ship-from-store | Route online orders to store for fulfillment | POS Pro; order routing auto-selects store |
| Local delivery | Delivery zones by postal code or radius | Admin configuration |
| Returns & exchanges | Process returns with refund/restock/exchange | POS + admin; cross-channel returns supported |
| Draft orders | Manual order creation (phone orders, custom quotes) | Admin + POS |
| Shipping labels | Purchase and print labels from admin | Via Shopify Shipping or third-party carrier apps |

##### Shopify Order Lifecycle

```
Order Created (any channel)
        |
Fulfillment Orders Created (per location)
        |
   +----+----+----+
   v         v         v
Warehouse  Store 1   3PL
Fulfillment Fulfillment Fulfillment
   |         |         |
   v         v         v
Shipped   Shipped/   Shipped
          Pickup
   |         |         |
   +---------+---------+
             v
      Order Fulfilled
```

##### Fulfillment Orders API

```graphql
# Query fulfillment orders for an order
query FulfillmentOrders($orderId: ID!) {
  order(id: $orderId) {
    fulfillmentOrders(first: 10) {
      edges {
        node {
          id
          status
          assignedLocation { name }
          lineItems(first: 50) {
            edges {
              node {
                id
                totalQuantity
                remainingQuantity
              }
            }
          }
        }
      }
    }
  }
}

# Submit fulfillment request to a fulfillment service
mutation SubmitFulfillment($id: ID!) {
  fulfillmentOrderSubmitFulfillmentRequest(id: $id) {
    originalFulfillmentOrder { id status }
    userErrors { field message }
  }
}

# Create fulfillment (mark as shipped)
mutation CreateFulfillment($fulfillment: FulfillmentV2Input!) {
  fulfillmentCreateV2(fulfillment: $fulfillment) {
    fulfillment {
      id
      status
      trackingInfo { number url company }
    }
    userErrors { field message }
  }
}
```

##### Order Routing Limitations (Native)

| Limitation | Impact | Solution |
|-----------|--------|---------|
| No cost optimization | Can't minimize total fulfillment cost across network | External OMS (Fluent, Manhattan) |
| No capacity constraints | Can't limit orders per location per day | External OMS or custom logic |
| No labor-aware routing | Doesn't consider store fulfillment capacity | External OMS |
| Limited split logic | Will split aggressively; can't set "prefer consolidated" rules | External OMS for advanced |
| No backorder management | If no location has stock, order sits unfulfilled | Manual handling or external OMS |
| No promised delivery date | Can't commit "deliver by X" and route accordingly | External OMS |
| No dynamic re-routing | Can't auto re-route if fulfillment fails at a location | Manual reassignment or custom app |

##### Returns Management

**Shopify Native Returns:**

| Capability | Details |
|-----------|---------|
| Return request | Customer requests return via online account or staff initiates in admin/POS |
| Return reasons | Configurable return reason codes |
| Return rules | Set return windows, final-sale items, restocking fees |
| Refund methods | Original payment, store credit (gift card), exchange (POS Pro) |
| Restocking | Automatic or manual restock at return location |
| Return shipping | Generate return labels (Shopify Shipping) |
| Cross-channel | Buy online, return in store (and vice versa) |

**Reverse Logistics Gaps:**

| Gap | Impact | Solution |
|-----|--------|---------|
| No returns grading | Can't grade returned items (A/B/C condition) | Custom app or RMA platform (Loop, Returnly) |
| No automated return routing | Can't route returns to optimal location | Manual or external OMS |
| No refurbishment workflow | Can't track repair/refurb process | Custom development or ERP |
| No disposition management | Can't auto-decide: restock, discount, liquidate, dispose | Custom logic or returns platform |
| No return analytics | Limited native reporting on return patterns | ShopifyQL or Loop/Narvar |

**Returns Management Partners:**

| Platform | Best For | Key Features |
|----------|----------|-------------|
| Loop Returns | Shopify-native, exchanges | Automated returns portal, exchanges, store credit incentives, analytics |
| Narvar | Enterprise returns experience | Branded tracking, returns management, proactive communication |
| AfterShip Returns | Multi-channel returns | Return portal, auto-approval rules, return label generation |
| Happy Returns | In-person returns (Return Bars) | Drop-off network, box-free returns, aggregated shipping |

##### When Does a Merchant Need an External OMS?

**Shopify Native Is Sufficient When:** Single warehouse + retail stores (< 20 locations), simple routing rules, no promised delivery dates, standard return/exchange workflows, no 3PL orchestration beyond SFN/ShipBob.

**External OMS Recommended When:** Complex routing (cost optimization, capacity constraints), promised delivery dates, 1,000+ orders/day, multiple fulfillment partners (3+), advanced returns (grading, disposition), marketplace fulfillment (drop-ship vendor management), pre-order/backorder management.

**OMS Partners:**

| Platform | Tier | Best For | Shopify Integration |
|----------|------|----------|---------------------|
| Shopify native | Built-in | Most merchants | Native |
| Pipe17 | Mid-market | Multi-system order routing | Shopify connector + middleware |
| Fabric OMS | Mid-enterprise | Growing omnichannel brands | API integration |
| Fluent Commerce | Enterprise | Complex DOM, global operations | API + middleware |
| Manhattan Active OM | Enterprise | Large-scale retail, advanced DOM | API + middleware (MuleSoft) |
| Kibo Commerce | Enterprise | Unified commerce | API integration |
| IBM Sterling OMS | Enterprise | Complex B2B + B2C | Heavy integration |

##### Order Management Webhooks

| Webhook | Fires When | Common Use |
|---------|-----------|------------|
| `orders/create` | New order placed | Push to ERP/WMS/OMS |
| `orders/updated` | Order modified | Sync changes to external systems |
| `orders/cancelled` | Order cancelled | Cancel in WMS, release inventory |
| `orders/fulfilled` | Order shipped | Update customer, sync tracking |
| `fulfillment_events/create` | Tracking update | Real-time status to customer |
| `refunds/create` | Refund processed | Sync refund to ERP/accounting |

Note: POS transactions trigger the same `orders/create` webhook. Filter by `source_name` field: `"pos"` for POS, `"web"` for online, `"shopify_draft_order"` for draft orders.

---

