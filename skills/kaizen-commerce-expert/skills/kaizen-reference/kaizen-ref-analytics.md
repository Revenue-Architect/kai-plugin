---
name: kaizen-ref-analytics
description: "Deep retail reference for analytics questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["analytics domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3E. Analytics & KPIs

---

#### Retail Analytics & KPIs

##### Tier 1: Must-Know Retail KPIs

**Sales Performance:**

| KPI | Formula | Industry Benchmark | Shopify Report |
|-----|---------|-------------------|----------------|
| Gross Sales | Total revenue before returns/discounts | Varies | Analytics > Reports > Sales |
| Net Sales | Gross Sales - Returns - Discounts | Varies | Analytics > Reports > Sales |
| Average Transaction Value (ATV) | Net Sales / Number of Transactions | $50-150 (general retail) | Analytics > Reports > Retail sales |
| Units Per Transaction (UPT) | Total Units Sold / Number of Transactions | 2.0-3.5 (apparel) | Custom (ShopifyQL) |
| Conversion Rate | Transactions / Foot Traffic | 20-40% (in-store); 2-4% (online) | Online: Analytics; In-store: needs RetailNext |
| Sales Per Square Foot | Net Sales / Selling Floor Area | $300-500 (specialty retail) | Not native |
| Comp Store Sales | (This Year - Last Year) / Last Year x 100 | 2-5% growth (healthy) | Custom (ShopifyQL) |

**Inventory Performance:**

| KPI | Formula | Industry Benchmark | Shopify Report |
|-----|---------|-------------------|----------------|
| Inventory Turnover | COGS / Average Inventory Value | 4-6x/year (general); 6-12x (grocery) | Partial: need COGS tracking |
| Days of Inventory (DOI) | 365 / Inventory Turnover | 60-90 days | Inventory reports |
| Sell-Through Rate | Units Sold / (Units Sold + Ending Inventory) x 100 | 60-80% (end of season) | Partial |
| GMROI | Gross Margin / Average Inventory Cost | 2.0-3.5x (healthy) | Not native: requires COGS |
| Stock-to-Sales Ratio | Beginning Inventory / Monthly Net Sales | 2.0-4.0 (apparel) | Custom (ShopifyQL) |
| Shrinkage Rate | (Book - Physical) / Book x 100 | 1.4-1.6% (NRF average) | Via Quick Counts |
| ABC Classification | A: Top 80%; B: Next 15%; C: Bottom 5% | Varies | Analytics > Reports |
| Stockout Rate | SKU-Location-Days OOS / Total x 100 | < 2% | Not native |
| Fill Rate | Orders Shipped Complete / Total x 100 | > 95% | Custom |

**Customer Metrics:**

| KPI | Formula | Benchmark | Shopify Report |
|-----|---------|-----------|----------------|
| Customer Lifetime Value (CLV) | Avg Order Value x Purchase Frequency x Lifespan | Varies | Customer cohort analysis |
| Repeat Purchase Rate | Customers 2+ orders / Total x 100 | 25-40% (DTC); 40-60% (retail) | Returning customer rate |
| Customer Acquisition Cost (CAC) | Marketing Spend / New Customers | Varies by channel | Custom |
| Customer Retention Rate | (End - New) / Start x 100 | 60-80% (retail) | Customer cohort |
| Net Promoter Score (NPS) | % Promoters - % Detractors | 50+ (excellent retail) | Not native -- survey tools (Delighted, AskNicely, Medallia) |

**Profitability:**

| KPI | Formula | Benchmark | Shopify Report |
|-----|---------|-----------|----------------|
| Gross Margin % | (Revenue - COGS) / Revenue x 100 | 40-60% (apparel); 25-35% (electronics) | Partial |
| EBITDA Margin | EBITDA / Revenue x 100 | 5-15% (retail) | Not in Shopify -- accounting system |
| Markdown % | Total Markdowns / Gross Sales x 100 | 15-30% (fashion); 5-10% (basics) | Not native |
| Return Rate | Units Returned / Units Sold x 100 | 8-10% (in-store); 15-30% (online) | Analytics > Returns |

##### Tier 2: Operational KPIs

**Fulfillment Performance:**

| KPI | Formula | Target | Shopify Report |
|-----|---------|--------|----------------|
| Order Cycle Time | Time from order to delivered | 2-5 days | Partial -- order timestamps |
| Pick Accuracy | Correct Picks / Total x 100 | > 99.5% | Not native -- WMS |
| Pack Rate | Orders Packed per Hour | 15-30 (manual) | Not native -- WMS |
| Ship Time | Time from order to label created | < 24 hours | Fulfillment timestamp delta |
| On-Time Delivery | Orders Delivered by Promised Date / Total Orders | > 95% | Not native -- carrier data |
| BOPIS Readiness Time | Time from order to "Ready" | < 2 hours | Fulfillment status timestamps |

**Store Operations:**

| KPI | Formula | Target | Shopify Report |
|-----|---------|--------|----------------|
| Cash Variance | (Expected - Actual) / Total Cash Sales x 100 | < 0.5% | Cash tracking reports (POS Pro) |
| Labor Cost % | Total Labor / Net Sales x 100 | 10-20% | Not native -- scheduling tool |
| Sales Per Labor Hour | Net Sales / Total Hours | $80-200 | Not native -- scheduling tool |
| BOPIS Attachment Rate | Additional Purchases / BOPIS Orders | 30-50% | Custom analysis |

##### GMROI Deep Dive

```
GMROI = Gross Margin $ / Average Inventory at Cost

Where:
  Gross Margin $ = Net Sales - COGS
  Average Inventory at Cost = (Beginning + Ending) / 2
```

| GMROI | Meaning |
|-------|---------|
| < 1.0 | Losing money on inventory investment |
| 1.0 - 2.0 | Low return; consider assortment changes |
| 2.0 - 3.5 | Healthy return for most retail categories |
| 3.5 - 5.0 | Strong performer |
| > 5.0 | Exceptional (or potentially understocked) |

**GMROI by Retail Category (Benchmarks):**

| Category | Typical GMROI |
|----------|--------------|
| Grocery | 1.5 - 3.0 |
| Apparel | 2.0 - 4.0 |
| Jewelry | 1.5 - 2.5 |
| Electronics | 3.0 - 5.0 |
| Home furnishings | 2.0 - 3.0 |
| Health & beauty | 2.5 - 4.0 |
| Sporting goods | 2.0 - 3.5 |

Shopify tracks `cost` per InventoryItem (variant-level COGS), but native reports don't calculate GMROI directly. Options: export + spreadsheet, ShopifyQL, Inventory Planner, or BigQuery (Plus with data export).

##### Shopify Reporting Ecosystem

**Native Reports (Analytics > Reports):**

| Report Category | Available Reports |
|----------------|-------------------|
| Sales | Total sales, sales over time, sales by product, sales by variant, sales by traffic referrer |
| Retail | Daily sales summary, sales by staff, sales by location, sales by register |
| Inventory | Month-end inventory snapshot, ABC analysis, average inventory sold per day, percent of inventory sold |
| Customers | Customers over time, returning vs new, customer cohort analysis |
| Orders | Orders over time, fulfillment status, order value distribution |
| Finances | Gross profit, tips, payments by type, transaction fees |

**ShopifyQL Notebooks:**
Custom SQL-like queries on Shopify data. Useful for:
- Year-over-year comparisons
- Custom metric calculations (UPT, ATV by segment)
- Cross-dimensional analysis (sales by product x location x time)
- Ad-hoc investigation

##### Third-Party Analytics

| Tool | Best For | Key Feature |
|------|----------|------------|
| Polar Analytics | DTC + retail, unified dashboard | Unified dashboard, cohort analysis, marketing attribution |
| Lifetimely | Customer LTV, cohort analysis | Predictive CLV, cohort analysis, profit tracking |
| RetailNext | Foot traffic, in-store conversion, heat maps | Door sensors, heat maps, staff optimization |
| Dor | Affordable foot traffic counting | Door sensor, Shopify integration |
| Glew.io | Multi-channel analytics | Cross-channel reporting, customer segmentation |
| Triple Whale | DTC attribution, profit tracking | Marketing attribution, creative analytics |

##### How to Use KPIs in Pre-Sales Conversations

Instead of: "Shopify has inventory reports."

Say: "Shopify tracks sell-through rate, ABC classification, and inventory days-on-hand natively. For GMROI and inventory turnover analysis, we connect tools like Inventory Planner or use ShopifyQL for custom calculations."

**Common Merchant Concerns -> KPI Response:**

| Merchant Says | KPI to Reference | Shopify Answer |
|--------------|-----------------|----------------|
| "We need better inventory visibility" | DOI, stockout rate, ABC | "Shopify shows real-time quantities across all locations with 5 inventory states. ABC analysis in native reports. Days of inventory in inventory snapshot." |
| "We're overstocked and cash-strapped" | Inventory turnover, GMROI, stock-to-sales | "We can identify slow movers via sell-through reports and ABC analysis. Pair with Inventory Planner for automated reorder optimization." |
| "We need to measure store performance" | Sales/sq ft, ATV, UPT, comp store | "POS Pro reports sales by location, by staff, by product. ATV is in retail reports. For foot traffic conversion, add RetailNext or Dor." |
| "Our return rate is killing us" | Return rate, net margin impact | "Shopify tracks return rates by product and channel. Loop Returns adds pattern detection and exchange incentives to reduce refund rate." |
| "How do we know if our inventory investment is paying off?" | GMROI, inventory turnover | "GMROI is the key metric. Shopify tracks COGS at variant level. Calculate in ShopifyQL or connect Inventory Planner for automated GMROI reporting." |

---

