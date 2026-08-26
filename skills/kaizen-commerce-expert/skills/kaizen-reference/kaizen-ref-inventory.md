---
name: kaizen-ref-inventory
description: "Deep retail reference for inventory questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["inventory domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3B. Inventory & Warehouse

---

#### Inventory API Reference

##### Inventory Data Model

```
Product
  +-- ProductVariant (1:1 with InventoryItem)
        +-- InventoryItem
              +-- InventoryLevel (one per Location)
                    +-- available       <- can be purchased
                    +-- committed       <- sold, awaiting fulfillment
                    +-- incoming        <- expected from transfers/POs
                    +-- reserved        <- held for draft orders
                    +-- unavailable
                          +-- damaged
                          +-- safety_stock
                          +-- quality_control
                          +-- other
```

**Key Relationships:**
- Product to Variant: One-to-many (max 2,048 variants via GraphQL; 100 via REST)
- Variant to InventoryItem: One-to-one
- InventoryItem to InventoryLevel: One per Location where the item is stocked
- Location types: Merchant-managed (standard) or Fulfillment Service (3PL/WMS)

##### Quantity States

| State | Description | Modified By |
|-------|-------------|-------------|
| `available` | Can be purchased by customers | Sales, adjustments, transfers, returns |
| `committed` | Sold but not yet fulfilled | Order creation, fulfillment |
| `incoming` | Expected from transfer or purchase order | Transfer creation, PO receipt |
| `reserved` | Held for draft orders | Draft order creation/deletion |
| `unavailable` | Not for sale (damaged, safety stock, QC, other) | Manual adjustment |
| `on_hand` | Calculated: available + committed + unavailable | Read-only aggregate |

Quantity Calculation: `on_hand = available + committed + unavailable`

##### GraphQL Mutations

**Adjust Quantities (PREFERRED):**

Use `inventoryAdjustQuantities` for incremental changes. This is Shopify's recommended approach. It handles concurrency correctly.

```graphql
mutation AdjustQuantities($input: InventoryAdjustQuantitiesInput!) {
  inventoryAdjustQuantities(input: $input) {
    inventoryAdjustmentGroup {
      createdAt
      reason
      referenceDocumentUri
      changes {
        name
        delta
        quantityAfterChange
        item { id }
        location { id }
      }
    }
    userErrors { field message code }
  }
}
```

Variables:
```json
{
  "input": {
    "reason": "correction",
    "name": "available",
    "changes": [
      {
        "delta": 10,
        "inventoryItemId": "gid://shopify/InventoryItem/123",
        "locationId": "gid://shopify/Location/456"
      }
    ]
  }
}
```

Valid reasons: `correction`, `cycle_count_available`, `damaged`, `shrinkage`, `promotion_or_demotion`, `received`, `reservation_created`, `reservation_deleted`, `reservation_updated`, `restock`, `safety_stock`, `quality_control`, `other`

**Set Quantities (Use for Full Sync):**

Use `inventorySetQuantities` when syncing from an external IMS that provides absolute values. Less safe than adjust for incremental changes.

```graphql
mutation SetQuantities($input: InventorySetQuantitiesInput!) {
  inventorySetQuantities(input: $input) {
    inventoryAdjustmentGroup {
      createdAt
      reason
    }
    userErrors { field message code }
  }
}
```

Variables:
```json
{
  "input": {
    "reason": "correction",
    "ignoreCompareQuantity": true,
    "quantities": [
      {
        "inventoryItemId": "gid://shopify/InventoryItem/123",
        "locationId": "gid://shopify/Location/456",
        "quantity": 50,
        "name": "available"
      }
    ]
  }
}
```

`ignoreCompareQuantity`: Set `true` for blind overwrites (external system is source of truth). Set `false` + provide `compareQuantity` for optimistic concurrency.

**Activate Inventory at Location:**
```graphql
mutation ActivateInventoryItem(
  $inventoryItemId: ID!
  $locationId: ID!
  $available: Int
) {
  inventoryActivate(
    inventoryItemId: $inventoryItemId
    locationId: $locationId
    available: $available
  ) {
    inventoryLevel {
      id
      quantities(names: ["available"]) { name quantity }
      item { id }
      location { id }
    }
  }
}
```

**Deactivate Inventory at Location:**
```graphql
mutation DeactivateInventoryItem($inventoryLevelId: ID!) {
  inventoryDeactivate(inventoryLevelId: $inventoryLevelId) {
    userErrors { field message }
  }
}
```

##### Inventory Transfers

**Create Transfer:**
```graphql
mutation CreateTransfer($input: InventoryTransferCreateInput!) {
  inventoryTransferCreate(input: $input) {
    inventoryTransfer {
      id
      status
      origin { location { id name } }
      destination { location { id name } }
      expectedArrival
      trackingInfo { number url company }
    }
    userErrors { field message }
  }
}
```

**Transfer Workflow:**
1. Create transfer: status `pending`
2. Ship transfer: status `in_transit` (inventory moves to `incoming` at destination)
3. Receive transfer: status `received` (inventory becomes `available` at destination)
4. Partial receive: partially received items become available; rest remain incoming

**Transfer Entities:**

| Entity | Purpose |
|--------|---------|
| `InventoryTransfer` | Master record -- origin, destination, status |
| `InventoryShipmentOrder` | Shipment request within a transfer |
| `InventoryShipment` | Actual shipment execution with tracking |

##### Queries

**Get Inventory Levels for a Product:**
```graphql
query GetInventoryLevels($productId: ID!) {
  product(id: $productId) {
    variants(first: 100) {
      edges {
        node {
          id
          title
          sku
          inventoryItem {
            id
            tracked
            inventoryLevels(first: 50) {
              edges {
                node {
                  id
                  quantities(names: ["available", "committed", "incoming", "reserved"]) {
                    name
                    quantity
                  }
                  location { id name }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

**Get Inventory at Specific Location:**
```graphql
query InventoryAtLocation($locationId: ID!) {
  location(id: $locationId) {
    name
    inventoryLevels(first: 250) {
      edges {
        node {
          quantities(names: ["available", "committed", "on_hand"]) {
            name
            quantity
          }
          item {
            variant { title sku product { title } }
          }
        }
      }
    }
  }
}
```

**List Locations:**
```graphql
query Locations {
  locations(first: 50) {
    edges {
      node {
        id
        name
        address { address1 city province country }
        fulfillmentService { id serviceName }
        isActive
        shipsInventory
      }
    }
  }
}
```

##### Webhooks

| Webhook Topic | Fires When |
|--------------|------------|
| `inventory_levels/connect` | Inventory item connected to location |
| `inventory_levels/disconnect` | Inventory item disconnected from location |
| `inventory_levels/update` | Inventory level quantity changes |
| `inventory_items/create` | New inventory item created |
| `inventory_items/update` | Inventory item updated |
| `inventory_items/delete` | Inventory item deleted |

**Webhook Payload (inventory_levels/update):**
```json
{
  "inventory_item_id": 123456,
  "location_id": 789012,
  "available": 45,
  "updated_at": "2025-03-19T10:30:00Z"
}
```

##### REST vs GraphQL

| Capability | REST | GraphQL |
|-----------|------|---------|
| Status | Supported (bug fixes only) | Primary, all new features |
| Max variants per product | 100 | 2,048 |
| Inventory states | `available` only | All 5 states |
| Bulk operations | Limited | Full support |
| Inventory transfers | Not available | Full CRUD |
| Rate limiting | Request-based | Cost-based (more efficient) |

Recommendation: Always use GraphQL for new integrations. REST is frozen for new features.

##### Integration Patterns

**Pattern 1: Shopify as Inventory Master** -- Shopify tracks all inventory. External systems read via API/webhooks. Best for simple retail, small catalog.

**Pattern 2: External IMS as Master** -- ERP/WMS/IMS is source of truth. Use `inventorySetQuantities` to push quantities to Shopify. Subscribe to Shopify webhooks for sales/returns.

**Pattern 3: Bidirectional Sync** -- Both systems can modify inventory. Use `inventoryAdjustQuantities` with `compareQuantity` for optimistic concurrency. Most complex; use middleware (Celigo, MuleSoft, custom).

**Pattern 4: Fulfillment Service** -- 3PL manages inventory at their locations. Use Fulfillment Service API to register locations. Enable SKU sharing for multi-location support.

##### Common Pitfalls

1. Using SET when you should ADJUST: `set` can overwrite concurrent changes; `adjust` is atomic
2. Not handling rate limits: Implement exponential backoff
3. Ignoring `userErrors`: Mutations return `userErrors` array; always check it
4. REST variant limit: REST caps at 100 variants; use GraphQL for high-variant products
5. Location activation: Must call `inventoryActivate` before setting quantities at a new location
6. Fulfillment service locations: Different workflow; fulfillment must be "requested" not directly created
7. Negative quantities: `available` can go negative (oversell); handle in your integration logic

---

#### Warehouse Management

##### Core WMS Concepts

**Warehouse Operations Lifecycle:**
```
Receiving -> Put-Away -> Storage -> Picking -> Packing -> Shipping -> Returns
```

| Operation | Description | Shopify Native? |
|-----------|-------------|-----------------|
| Receiving | Inbound goods against POs or transfers | Partial: PO receiving in admin; transfer receiving in POS + admin |
| Put-Away | Moving received goods to storage locations | No: no bin/slot direction |
| Storage | Organizing inventory in bins/shelves/zones | No: location-level only, no sub-location |
| Picking | Retrieving items for orders | Basic: BOPIS pick & pack in POS; no wave/batch/zone picking |
| Packing | Preparing items for shipment | Basic: admin fulfillment; no pack station workflow |
| Shipping | Label generation, carrier selection | Via Shopify Shipping, ShipStation, or similar apps |
| Returns | Processing returned goods back to inventory | Yes: POS returns restock; admin returns processing |

##### Picking Methods

| Method | Description | Best For | Shopify Support |
|--------|-------------|----------|-----------------|
| Discrete/Single Order | Pick one order at a time | Low volume, simple operations | Admin fulfillment screen |
| Batch Picking | Pick multiple orders simultaneously, sort later | Medium volume (50-200 orders/day) | Not native: ShipHero, SKULabs |
| Wave Picking | Group orders into waves by criteria (carrier, zone, priority) | High volume (200+ orders/day) | Not native: WMS required |
| Zone Picking | Pickers assigned to warehouse zones; orders pass through zones | Large warehouses with diverse product types | Not native: WMS required |
| Cluster Picking | Pick into multiple tote/bins simultaneously | High-SKU, multi-order efficiency | Not native: WMS required |

##### Storage Concepts

| Concept | Description | Shopify Support |
|---------|-------------|-----------------|
| Bin Locations | Named positions in a warehouse (Aisle A, Shelf 3, Bin 4) | Not native: metafields or WMS |
| Slotting | Optimizing product placement (fast movers near packing stations) | Not native: WMS |
| FIFO | First In, First Out -- ship oldest inventory first | Not native: WMS or manual discipline |
| FEFO | First Expired, First Out -- critical for perishables | Not native: WMS (requires expiry tracking) |
| LIFO | Last In, First Out -- rare in retail | Not native |
| Bulk vs Pick Locations | Separate storage for bulk reserve vs active picking area | Not native: WMS |
| Cross-Docking | Receive and ship without storage (bypass warehouse) | Not native: enterprise WMS |

##### Shopify's Native Warehouse Capabilities

| Capability | How It Works | Plan Required |
|-----------|-------------|---------------|
| Multi-location inventory | Track quantities at unlimited locations | All plans |
| Inventory transfers | Move stock between locations with tracking | POS Pro for POS; admin for all |
| Inventory states | available, committed, incoming, reserved, unavailable | All plans (GraphQL) |
| Order routing | Automatic fulfillment assignment | All plans |
| Fulfillment orders | Per-location fulfillment tracking | All plans |
| BOPIS pick & pack | Barcode-verified picking for in-store pickup orders | POS Pro |
| Ship-from-store | Fulfill online orders from retail locations | POS Pro |
| Purchase orders | Create POs, track incoming, receive stock | POS Pro |
| Stock adjustments | Adjust quantities with reason codes | All plans |
| Quick Counts | Native cycle counting in POS with barcode scanning | POS Pro |
| Webhooks | Real-time inventory change notifications | All plans |

##### What Shopify Does NOT Do (Warehouse Gaps)

| Gap | Recommended Solution |
|-----|---------------------|
| No bin/shelf locations | WMS app (PULPO, ShipHero) or metafield-based tracking. **AnyDB can serve as a lightweight bin/location tracking layer here.** |
| No pick/pack workflows | WMS (ShipHero, SKULabs, PULPO) |
| No slotting optimization | WMS with slotting module |
| No FIFO/FEFO enforcement | WMS or manual process; Katana for manufacturing |
| No labor management | WMS with labor module or Deputy/Homebase |
| No warehouse task queue | WMS. **AnyDB can manage task queues as an operational control layer.** |
| No yard management | Enterprise WMS (Manhattan, SAP EWM) |
| No cross-docking | Enterprise WMS |
| No returns grading | Custom app or WMS |
| No cartonization | ShipStation, WMS, or shipping app |

##### Warehouse Architecture Patterns with Shopify

**Pattern 1: Shopify-Only (No WMS)**
Best for: < 100 orders/day, < 1,000 SKUs, simple operations. Inventory tracked in Shopify at location level. Transfers managed in admin. Stock counts via Quick Counts.

**Pattern 2: Shopify + Lightweight WMS App**
Best for: 100-500 orders/day, growing brands. WMS manages warehouse operations (pick, pack, ship). Shopify remains source of truth for products and orders. Inventory syncs bidirectionally.

**Pattern 3: ERP-WMS + Shopify (Enterprise)**
Best for: 500+ orders/day, complex operations. ERP is master for financials, purchasing. WMS handles warehouse execution. Shopify handles commerce, POS, customer experience. Middleware orchestrates data flow.

**Pattern 4: Store-as-Warehouse (Ship-from-Store)**
Best for: Retailers using stores for online fulfillment. Shopify order routing directs orders to optimal location. Store staff use POS to pick and pack orders. Barcode-verified BOPIS pick & pack.

##### 3PL / Fulfillment Service Integration

Shopify has a specific API for 3PL/fulfillment partners: Register as Fulfillment Service (creates managed location), fulfillment requests flow Shopify to 3PL, 3PL manages their own inventory levels at their location.

**Common 3PL Partners:**

| Partner | Type | Best For |
|---------|------|----------|
| SFN (Shopify Fulfillment Network) | Shopify-owned 3PL | DTC brands wanting hands-off fulfillment |
| ShipBob | Tech-enabled 3PL | Growing DTC, distributed US fulfillment |
| Deliverr (now Flexport) | 2-day fulfillment | Fast shipping, marketplace fulfillment |
| Red Stag | Heavy/oversized | Furniture, fitness equipment, large items |
| ShipMonk | Small parcel 3PL | Subscription boxes, small-medium brands |

##### Loss Prevention & Shrinkage

**Shrinkage Types:**

| Type | % of Total (industry avg) | Shopify Tools |
|------|--------------------------|---------------|
| External theft | ~37% | POS staff permissions, cash tracking, manager approval |
| Employee theft | ~28% | POS audit trail, cash session reconciliation, permission controls |
| Administrative errors | ~25% | Cycle counts (Quick Counts), inventory adjustment history |
| Vendor fraud | ~5% | PO receiving verification, quantity mismatch alerts |
| Unknown/other | ~5% | Regular cycle counting, ABC analysis |

**Cycle Count Strategy:**
1. Full inventory count: Annual or biannual
2. ABC cycle counting: A items monthly, B items quarterly, C items annually
3. Random sampling: Count random items weekly
4. Exception-based: Count when discrepancies surface

##### WMS Qualification Matrix

| Signal | Recommendation |
|--------|---------------|
| < 50 orders/day, simple catalog | Shopify native is likely sufficient |
| 50-200 orders/day, growing | Consider lightweight WMS (ShipHero, PULPO) |
| 200+ orders/day, complex ops | WMS required (ShipHero, Deposco, or enterprise WMS) |
| Multiple warehouses + stores | WMS + Shopify integration (middleware recommended) |
| 3PL (outsourced) | Fulfillment service integration; no merchant-side WMS needed |
| Manufacturing + warehouse | Katana or Cin7 (MRP + WMS combined) |

---

