---
name: kaizen-ref-discovery
description: "Deep retail reference for discovery questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["discovery domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3K. Discovery Questions

---

All discovery questions consolidated from domain references. Use these during merchant qualification and needs assessment.

#### Forecasting & Replenishment Discovery

1. How do you currently forecast demand? (gut feel, spreadsheets, software)
2. What's your average supplier lead time? Longest lead time?
3. Have you experienced significant stockouts in the last year? Estimated lost revenue?
4. Do you carry seasonal inventory? How far ahead do you plan?
5. Do you have safety stock policies? How were they set?
6. How do you currently create purchase orders? Manual or automated?
7. Do you sell on multiple channels (Shopify + Amazon + wholesale)? Need aggregated forecasting?
8. How many SKUs do you actively manage? How many suppliers?
9. Do you manufacture or source internationally? (longer lead times = more forecasting importance)
10. What's your biggest inventory challenge today? (stockouts, overstock, cash flow, markdown losses)

#### Warehouse Operations Discovery

1. How many orders per day do you ship from your warehouse?
2. What picking method do you use today? (single order, batch, wave, zone)
3. Do you use bin/shelf locations in your warehouse?
4. How many warehouse staff? Any productivity tracking?
5. Do you need FIFO, FEFO, or lot/batch tracking?
6. Do you currently use a WMS? Which one?
7. Is your warehouse self-operated or outsourced to a 3PL?
8. What shipping carriers do you use? How do you select carrier per order?
9. Do you have any barcode scanning infrastructure?
10. Do you print pick lists or use mobile-directed picking?
11. Does your warehouse also fulfill B2B/wholesale orders?
12. Do you need your warehouse to support returns processing?
13. Are there compliance requirements (temperature tracking, hazmat, serial numbers)?
14. Do you plan to add more warehouses or fulfillment centers?
15. Do retail stores also function as fulfillment points?

#### Order Management Discovery

**Current State:**
1. How many orders per day across all channels?
2. How many fulfillment locations (warehouses, stores, 3PLs)?
3. Do you promise delivery dates to customers? How do you manage that today?
4. What's your current order routing logic? Manual or automated?

**Fulfillment Complexity:**
5. Do you split orders across locations, or prefer consolidated shipment?
6. Do stores fulfill online orders? What percentage?
7. Do you use any 3PLs? How many?
8. Do you have drop-ship vendors?
9. How do you handle backorders or pre-orders?

**Returns:**
10. What's your return rate? (Industry avg: 8-10% in-store, 15-30% online)
11. Do you accept cross-channel returns (buy online, return in store)?
12. Do you need to grade returned items before restocking?
13. Do you offer exchanges? Even exchanges only or with price difference?

**Integration:**
14. Do orders need to flow to an ERP for financials/invoicing?
15. Do you need real-time order status visible across all systems?
16. Any marketplace channels (Amazon, Walmart) that need unified fulfillment?

#### Merchandising Discovery

**Assortment & Planning:**
1. How do you decide what products to carry and where? Is it centralized or per-store?
2. Do you have different assortments by store (localized merchandising)?
3. Do you do seasonal planning? How far in advance?
4. How do you track open-to-buy budgets?

**Allocation:**
5. How do you decide how much inventory goes to each store vs warehouse?
6. Do you auto-replenish stores from a central warehouse? What triggers it?
7. Do stores request transfers, or is it centrally managed?

**Markdown:**
8. What's your markdown cadence? (Weekly, monthly, seasonal?)
9. Do you use different markdown strategies by location or customer segment?
10. How do you measure markdown effectiveness?

**Visual Merchandising:**
11. Do you use planograms? Who creates them?
12. How do you communicate merchandising standards to stores?
13. Do you audit visual merchandising compliance?

**Vendors:**
14. How many vendors/suppliers do you work with?
15. Do vendors need portal access for order/stock visibility?
16. Do you do any vendor-managed inventory (VMI)?

#### Analytics & Reporting Discovery

1. What KPIs does your leadership team review weekly? Monthly?
2. Do you currently track inventory turnover or GMROI?
3. Do you measure in-store conversion rate (foot traffic -> transaction)?
4. What reporting tools do you use today? (Excel, BI tool, ERP reports)
5. Do you need cross-location comparative reporting?
6. Do you track staff sales performance? Is commission a factor?
7. Do you need to report to investors/board? What format?
8. How do you measure your omnichannel effectiveness today?

#### General POS & Retail Discovery

1. How many retail locations do you have today? Plans to expand?
2. How many registers/devices per location?
3. Do you currently use a POS system? Which one? What do you like/dislike?
4. What payment methods do your customers expect? (cards, mobile wallets, cash, custom)
5. Do you need omnichannel fulfillment? (BOPIS, ship-from-store, local delivery)
6. How do you handle returns today? Cross-channel?
7. Do you have an existing ecommerce store? On what platform?
8. Do you use an ERP, IMS, or WMS today? Which one?
9. What's your biggest operational pain point in retail right now?
10. Are you evaluating other POS systems? Which ones?

---

