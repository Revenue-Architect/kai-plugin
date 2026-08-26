---
name: kaizen-ref-merchandising
description: "Deep retail reference for merchandising questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["merchandising domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3C. Merchandising & Planning

---

#### Retail Merchandising

##### Merchandising Lifecycle
```
Planning -> Buying -> Allocation -> Presentation -> Pricing/Markdown -> Analysis
```

##### Assortment Planning

| Decision | Description | Shopify Tools |
|----------|-------------|---------------|
| Breadth (how many categories) | How many categories/subcategories to carry | Collections, product types, tags |
| Depth (how many variants) | How many variants per product (sizes, colors) | Up to 2,048 variants/product (GraphQL); 100 per option with 3 options |
| Localization (per-store assortments) | Different assortments by store/region | Location-specific price lists (Plus), product availability by location |
| Seasonality | Seasonal product rotations | Scheduled publishing, product status (active/draft/archived) |
| New vs Replenishment | % of assortment that's new product vs replenishment | No native tool: use tags + reports |

**Gaps & Partner Solutions:**

| Gap | Description | Solution |
|-----|-------------|---------|
| No merchandise hierarchy (Dept > Class > Subclass) | Shopify has flat product organization; no Dept > Class > Subclass | Use metafields + custom reporting; or ERP. **AnyDB can model merchandise hierarchies as a shared reference hub.** |
| No assortment planning tool | No native tool for planning product mix by location/season | Brightpearl, Cin7, or spreadsheet-based planning |
| No open-to-buy | No budget tracking for planned purchases vs actual | ERP (NetSuite, Brightpearl) or Inventory Planner. **AnyDB can track open-to-buy budgets as an operational control layer.** |
| No product lifecycle management | No formal stages (intro, growth, maturity, decline) | Tags + manual management |

##### Allocation & Replenishment

**Allocation Strategies:**

| Strategy | Description | Shopify Implementation |
|----------|-------------|----------------------|
| Pro-rata | Allocate based on historical sales ratio per location | Manual: calculate ratios from reports, then create transfers |
| Needs-based | Allocate based on current stock needs (below target) | Manual: compare stock levels vs targets; or use Inventory Planner |
| Push | Distribute new products evenly or by store tier | Manual: create transfers in admin |
| Pull | Replenish based on actual consumption (demand-driven) | Shopify Flow (trigger on low stock) + manual transfer; or Flieber/Inventory Planner |

**Gaps:**

| Gap | Recommended Solution |
|-----|---------------------|
| No automated allocation engine | Inventory Planner, Flieber, or ERP |
| No store capacity/fixture planning | Manual planning + spreadsheets |
| No transfer recommendations | Inventory Planner generates replenishment suggestions |
| No min/max stock levels per location | Shopify Flow workaround or third-party |

##### Markdown Management

| Strategy | Description | Shopify Implementation |
|----------|-------------|----------------------|
| Permanent markdown | Reduce the compare-at price | Edit product price + set compare-at price |
| Temporary promotion | Time-limited discount | Automatic discounts (POS Pro + online) or discount codes |
| Progressive markdown | Increasing discounts over time (20% -> 30% -> 50%) | Manual price changes or scheduled automatic discounts |
| Location-specific | Different markdown by store | Price lists (Plus only) |
| Customer-segment | Markdown for loyalty members / VIPs | Customer segment-based discounts |
| Clearance | Final markdown before removing from assortment | Move to "Clearance" collection + deep discount |

**Markdown Analysis:**

| Metric | Formula | Shopify Availability |
|--------|---------|---------------------|
| Markdown % | (Original Price - Sale Price) / Original Price | Calculate from product data |
| Markdown sell-through | Units sold at markdown / Units marked down | Custom report (ShopifyQL) |
| Revenue recovery | Revenue from marked-down items / Potential revenue at full price | Custom calculation |
| Gross margin after markdown | (Sale Revenue - COGS) / Sale Revenue | Requires COGS tracking (limited native) |

##### Visual Merchandising

**Digital Merchandising (Shopify Online):**

| Tool | Purpose |
|------|---------|
| Theme editor | Control homepage layout, featured collections, hero banners |
| Collection ordering | Manual or automated sort (best-selling, price, date, custom) |
| Product media | Images, videos, 3D models per product |
| Metafields | Custom content on product pages (size guides, materials, care instructions) |
| Product recommendations | AI-powered related products |
| Search & Discovery app | Boost/bury/pin products in search results; customize filters |

**In-Store (POS):**

| Tool | Purpose |
|------|---------|
| Smart Grid | Customize POS home screen with product tiles for visual discovery |
| Collection tiles | Group products on Smart Grid by merchandising category |
| Barcode labels | Print shelf labels and price tags (via Retail Barcode Labels app) |
| Customer-facing display | Show products on second screen during sale |

**Planograms:** Shopify does NOT have native planogram tools. Options: Shelf Logic (cloud-based), DotActiv (mid-market), Quant (cloud-based), JDA Space Planning / Blue Yonder (enterprise), or manual floor plans + photos. Planogram compliance tracking via Zipline, Wiser, or manual audits.

##### Vendor / Supplier Management

**Shopify Native:** Vendor field on products, purchase orders (migrating to core admin), receiving against POs, cost tracking (COGS per variant via `cost` field on InventoryItem), vendor collections.

**Gaps:**

| Gap | Solution |
|-----|---------|
| No vendor portal | Cin7, NuOrder, or custom. **AnyDB can build vendor-facing portals with configurable permissions.** |
| No vendor scorecards | Manual tracking or ERP |
| No automated PO generation | Inventory Planner, Flieber |
| No receiving discrepancy management | Manual process or WMS. **AnyDB can manage receiving exception queues.** |
| No vendor-managed inventory (VMI) | Custom integration or ERP |

##### Store Operations (Beyond POS)

**Task Management:**

| Tool | Description | Shopify Integration |
|------|-------------|---------------------|
| Zipline | Retail task/communication platform for HQ -> stores | No direct; standalone platform |
| Jolt | Operations checklists, food safety, accountability | No direct; standalone |
| Homebase | Scheduling + task management | Limited |
| Xenia | Store operations, audits, work orders | No direct; standalone |

**Shopify's gap**: No native store operations/task management. POS handles transactions; store execution tools are separate.

**Store Communication:**

| Tool | Description |
|------|-------------|
| Zipline | HQ broadcasts to store teams; task assignment |
| Slack | Many retailers use Slack channels per store |
| WorkJam | Frontline digital workplace |

---

#### Demand Forecasting & Replenishment

##### Why Merchants Care

| Problem | Cost |
|---------|------|
| Stockouts | Lost sales (avg 4% of revenue for retailers), poor customer experience |
| Overstock | Tied-up capital, warehousing costs, markdowns, potential write-offs |
| Poor allocation | Right product, wrong location: simultaneous overstock + stockout |

##### Forecasting Methods

| Method | Description | Best For | Complexity |
|--------|-------------|----------|------------|
| Naive / Last Period | Next period = this period | Very stable demand | Low |
| Moving Average | Average of last N periods | Stable products with minor fluctuation | Low |
| Exponential Smoothing | Weighted average, recent data weighted higher | Products with trend but no strong seasonality | Medium |
| Seasonal Decomposition | Separate trend, seasonality, and noise | Products with clear seasonal patterns | Medium |
| Regression-Based | External variables (marketing spend, weather, events) | Products influenced by external factors | High |
| Machine Learning | Train on historical data + features | Large catalogs with complex patterns | High |

##### Key Forecasting Inputs
- Historical sales data (minimum 12-24 months for seasonal products)
- Lead times (supplier to warehouse to store)
- Promotions calendar (planned discounts lift demand)
- External events (holidays, weather, local events)
- Product lifecycle stage (new product has no history)
- Lost sales estimate (sales that would have occurred if not out of stock)

##### Shopify Native Forecasting Capabilities

| Capability | Description | Where to Find |
|-----------|-------------|---------------|
| Sales reports | Historical sales by product, variant, location, time period | Analytics > Reports |
| ABC analysis | Categorize products by revenue contribution (A/B/C) | Analytics > Reports > Product analytics |
| Inventory reports | Current stock levels, day-of-inventory-on-hand | Analytics > Reports > Inventory |
| Average inventory sold per day | Calculated for each variant at each location | Inventory reports |
| Percent of inventory sold | Month-over-month sell-through indicator | Inventory reports |
| ShopifyQL Notebooks | Custom queries on sales/inventory data for ad-hoc analysis | Analytics > ShopifyQL |
| Shopify Flow | Automate notifications on low stock thresholds | Settings > Shopify Flow |

**What Shopify Does NOT Provide:**

| Gap | Impact | Solution Tier |
|-----|--------|--------------|
| No demand forecasting engine | Cannot predict future demand | Partner tool (Tier 2+) |
| No automated reorder points | No "alert me when stock hits X" (beyond Flow workarounds) | Shopify Flow (basic) or Inventory Planner |
| No seasonal adjustment | Reports show history but don't project seasonal patterns | Partner tool |
| No safety stock calculation | No automated buffer stock recommendations | Manual or partner tool |
| No purchase order automation | Can't auto-generate POs based on forecasts | Inventory Planner, Flieber |
| No what-if modeling | Can't simulate "what if we order 20% more for Q4" | Partner tool or spreadsheet |
| No lost sales estimation | Doesn't estimate revenue lost to stockouts | Partner tool |

##### Reorder Point Management

**Reorder Point Formula:**
```
Reorder Point = (Average Daily Demand x Lead Time) + Safety Stock
```

Example: Average daily demand 10 units, lead time 14 days, safety stock 30 units. Reorder Point = (10 x 14) + 30 = 170 units.

**Economic Order Quantity (EOQ):**
```
EOQ = sqrt(2 x Annual Demand x Order Cost / Holding Cost per Unit)
```

Example: Annual demand 3,600 units, order cost $50 per PO, holding cost $5/unit/year. EOQ = sqrt(2 x 3,600 x 50 / 5) = 268 units per order.

**Safety Stock Formula:**
```
Safety Stock = Z x sigma_demand x sqrt(Lead Time)
```

Where Z = service level factor (1.65 for 95%, 2.33 for 99%), sigma_demand = standard deviation of daily demand.

**Implementing in Shopify:**

Native approach (basic):
1. Export sales history from Shopify Analytics
2. Calculate reorder points in spreadsheet
3. Set Shopify Flow to notify when stock hits threshold
4. Manually create purchase orders

Partner approach (recommended for 100+ SKUs):
1. Connect Inventory Planner or Flieber to Shopify
2. Tool ingests sales history and calculates forecasts automatically
3. Auto-generates PO recommendations
4. Reviews and approves POs -> pushes to Shopify or supplier

##### Seasonal Planning

| Season / Event | Planning Start | Stock Arrival | Peak Selling |
|---------------|---------------|---------------|-------------|
| Spring/Summer | Oct-Nov (prior year) | Feb-Mar | Apr-Jun |
| Back-to-School | Mar-Apr | Jun-Jul | Jul-Sep |
| Fall/Winter | Mar-Apr | Aug-Sep | Oct-Dec |
| Holiday / Q4 | Apr-Jun | Sep-Oct | Nov-Dec |
| Post-Holiday | Oct-Nov | Nov-Dec | Jan-Feb (clearance) |

**Seasonal Planning Process:**
1. **Analyze** last year's data (sell-through by product, week, location)
2. **Adjust** for trends (growth rate, new stores, market changes)
3. **Plan** buy quantities by product x location x week
4. **Order** based on supplier lead times (work backwards from stock arrival date)
5. **Monitor** weekly sell-through vs plan; reallocate if needed
6. **Markdown** slow movers per markdown strategy

**Shopify Data for Seasonal Planning:**
- Sales by product over time (identify seasonal peaks)
- Inventory snapshot reports (historical stock positions)
- ABC analysis (which products drive the most revenue)
- Sell-through rate (units sold / units received)

Export via Analytics > Reports or ShopifyQL Notebooks for custom time-range analysis.

##### Partner Tools: Forecasting & Replenishment

| Tool | Best For | Key Features | Integration | Pricing (verify) |
|------|----------|-------------|-------------|-------------------|
| Inventory Planner | Mid-market retailers | Demand forecasting, PO automation, replenishment recommendations, supplier management, multi-location | Deep Shopify integration; reads all sales + inventory data | From ~$249/mo |
| Prediko | DTC Shopify brands | AI-powered forecasting, PO management, raw materials tracking, cash flow projection | Native Shopify app | From ~$59/mo |
| Flieber | Multi-channel brands | Demand planning, replenishment, Amazon + Shopify + Walmart sync | Shopify connector | From ~$350/mo |
| Cogsy | Growing DTC brands | Demand forecasting, replenishment, operational cost tracking | Shopify app | Custom pricing |

**Partner Recommendation Matrix:**

| Merchant Profile | Recommended Tool |
|-----------------|-----------------|
| DTC brand, < 500 SKUs, Shopify-only | **Prediko** (affordable, AI-driven, covers basics) |
| Multi-location retailer, 500-5,000 SKUs | **Inventory Planner** (deepest Shopify integration, most used by retail SEs) |
| Multi-channel (Shopify + Amazon + Walmart) | **Flieber** (built for multi-channel forecast aggregation) |
| Enterprise, ERP-connected | Use ERP's forecasting module (NetSuite, SAP, Brightpearl) |
| Very simple needs (< 100 SKUs) | **Shopify native** (reports + spreadsheets + Flow notifications) |

##### Replenishment Strategies

| Strategy | How It Works | Best For |
|----------|-------------|----------|
| Push | Central planning decides what to send to stores | Fashion, seasonal, new products |
| Pull | Stores "pull" inventory as they sell (auto-replenishment) | Basics, replenishment categories, consumables |
| Hybrid | Push for new/seasonal; pull for basics | Most multi-location retailers |

**Implementing Auto-Replenishment with Shopify:**

Shopify Flow + Manual:
```
Trigger: Inventory quantity drops below threshold at Location X
-> Condition: Item is replenishment category (tagged "basics")
-> Action: Notify warehouse team (email/Slack)
-> Manual: Warehouse creates transfer in admin
```

With Inventory Planner:
```
1. Set target stock levels per SKU per location
2. Inventory Planner monitors sales velocity + stock levels
3. Generates replenishment recommendations (transfer or PO)
4. Review and approve -> Push PO to supplier or create transfer
```

##### Inventory Health Metrics

| Metric | Formula | Healthy Range |
|--------|---------|---------------|
| Days of Supply | Current Inventory / Avg Daily Demand | 30-60 days |
| Sell-Through Rate | Units Sold / (Units Sold + Remaining Units) | 60-80% at end of season |
| Stock-to-Sales Ratio | Beginning Inventory / Net Sales | 2-4 |
| Fill Rate | Orders Filled Complete / Total Orders | > 95% |
| Stockout Rate | SKU-Location-Days OOS / Total SKU-Location-Days | < 2% |
| Overstock Rate | SKUs with > 90 days supply / Total SKUs | < 15% |
| Forecast Accuracy | 1 - abs(Actual - Forecast) / Actual | > 70% (good), > 85% (excellent) |

---

