---
name: kaizen-ref-partners
description: "Deep retail reference for partners questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["partners domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3F. Technology Partners

---

#### Technology Partners

**IMPORTANT:** Partner pricing and features change frequently. Always verify current pricing via web search before quoting.

##### Partner Recommendation Decision Tree

```
Merchant Complexity Assessment:

  SKU count < 500
  Locations < 5                     -> TIER 1: Shopify Native + Apps
  No warehouse / 3PL
  No ERP

  SKU count 500-10,000
  Locations 5-20                    -> TIER 2: Mid-Market IMS/WMS
  Simple warehouse ops
  Basic ERP or accounting

  SKU count 10,000+
  Locations 20+                     -> TIER 3: Enterprise ERP/WMS
  Complex warehouse (zones, waves)
  ERP with full financials
```

**KaizenCommerce note:** For merchants in the "operational gap" between Shopify native and a full ERP/WMS, AnyDB is KaizenCommerce's preferred solution. It fills the back-office operations layer (vendor PO management, exception tracking, approval workflows, custom reporting) without the cost or complexity of enterprise software.

##### Tier 1: Shopify-Native Apps

Best for: SMBs, DTC brands opening retail, simple multi-location.

**Inventory Management Apps:**

| App | Best For | Key Features | POS Integration | Pricing (verify) |
|-----|----------|-------------|-----------------|-------------------|
| **Stocky** (sunsetting) | Legacy users | POs, stock takes, transfers | Deep (built-in) | Free with POS Pro |
| Quick Counts | Stock counting | Barcode scan, discrepancy view | Native POS extension | Free with POS Pro |
| Inventory Planner | Demand forecasting | Forecasting, PO automation, supplier mgmt | Reads Shopify inventory | From ~$249/mo |
| Prediko | AI forecasting for DTC | AI demand forecasting, PO management, raw materials | Reads Shopify inventory | From ~$59/mo |
| Flieber | Multi-channel planning | Demand planning, replenishment, Amazon + Shopify | Reads Shopify inventory | From ~$350/mo |
| Stocktake Online | Cycle counting (blind counts, scheduled) | Blind counts, scheduled counts, multi-user | Writes to Shopify inventory | From ~$39/mo |
| Katana | Manufacturing + inventory, BOM | BOM, production planning, batch tracking | Syncs with Shopify | From ~$179/mo |
| Sumtracker | Multi-channel sync | Real-time sync Shopify + Amazon + eBay | Syncs with Shopify | From ~$49/mo |

**Fulfillment & Shipping Apps:**

| App | Best For | Key Features | Pricing (verify) |
|-----|----------|-------------|-------------------|
| ShipStation | Multi-carrier shipping | Rate comparison, label printing, automation rules | From ~$9.99/mo |
| Shopify Shipping | Simple shipping | Built-in label purchasing, carrier rates | Included |
| Easyship | International shipping | Duty/tax calc, 250+ couriers | Free tier available |

**Loyalty & Clienteling Apps (POS-Compatible):**

| App | Best For | Key Features | POS Integration |
|-----|----------|-------------|-----------------|
| Smile.io | Points & rewards | Points, VIP tiers, referrals | Full POS integration |
| Marsello | Loyalty + marketing | Combined loyalty and email | Deep POS integration |
| Endear | Clienteling CRM | Customer outreach, style profiles | Works alongside POS |
| Rise.ai | Store credit / gift cards | Advanced gift card + credit management | POS redemption |

##### Tier 2: Mid-Market IMS / WMS

Best for: Growing brands, 500-10,000 SKUs, multi-location with warehouse ops.

**IMS:**

| Platform | Best For | Key Features | Shopify Integration | Pricing (verify) |
|----------|----------|-------------|---------------------|-------------------|
| Cin7 Core | Multi-channel + B2B + light manufacturing | Real-time inventory, POs, BOMs, B2B portal, 700+ integrations, EDI | Native Shopify connector, real-time sync | From ~$349/mo |
| Cin7 Omni | Enterprise multi-channel | Advanced warehouse, EDI, 3PL management | Native connector | Custom pricing |
| Linnworks | High-volume multi-marketplace | 100+ marketplace integrations, automation rules, warehouse transfers | Shopify + POS sync | Custom |
| SKULabs | Warehouse + multi-carrier | Barcode picking/packing, serialized inventory, batch/lot, 30+ carriers | Real-time Shopify sync | From ~$299/mo |
| Finale Inventory | Mid-market WMS/IMS bridge | Bin locations, batch/lot, serial tracking, wave picking | Shopify connector | From ~$99/mo |
| Veeqo (Amazon-owned) | Multi-channel + shipping | Inventory sync, shipping labels, Amazon integration | Shopify connector | Free (Amazon subsidy) |

**WMS:**

| Platform | Best For | Key Features | Shopify Integration | Pricing (verify) |
|----------|----------|-------------|---------------------|-------------------|
| ShipHero | Shopify Plus brands | End-to-end WMS, smart warehouse routing, analytics | Official Plus partner; 1-click | From ~$169/mo |
| PULPO WMS | SMB warehouse | Pick/pack/ship, bin management, returns, POS inventory sync | Native Shopify app + POS | From ~$100/mo |
| Logiwa | High-volume fulfillment | Cloud WMS, wave picking, 3PL management | Shopify connector | Custom |
| ShipBob | Outsourced fulfillment (3PL) | Multi-warehouse, 2-day shipping, distributed inventory | Native app; fulfillment service | Per-order pricing |
| Deposco | Enterprise fulfillment | DOM, warehouse execution, supply chain planning | API integration | Custom |

##### Tier 3: Enterprise ERP / WMS

Best for: 10,000+ SKUs, 20+ locations, complex financials.

**ERP:**

| Platform | Best For | Key Features | Shopify Integration | Pricing (verify) |
|----------|----------|-------------|---------------------|-------------------|
| NetSuite (Oracle) | Enterprise all-in-one | Financials, inventory, WMS, demand planning, SuiteScript | Via Celigo, Pipe17, or custom SuiteScript | ~$25K-50K+ first year |
| Brightpearl (Sage) | Retail operations platform | OMS, inventory, accounting, purchasing, automation | Native Shopify connector | Custom/enterprise |
| SAP Business One | Mid-market SAP | Financials, inventory, CRM, production | Via middleware (Celigo, MuleSoft) | ~$3K-5K/user/year |
| Microsoft Dynamics 365 | Large enterprise | Finance, supply chain, commerce, BI | Via middleware or custom integration | Custom |
| Acumatica | Cloud-native mid-market | Distribution, manufacturing, project accounting | Shopify connector available | Custom |
| Odoo | Open-source / modular | Inventory, MRP, accounting, CRM -- highly customizable | Community connector + custom | From free to ~$25/user/mo |

**Enterprise WMS:**

| Platform | Best For | Key Features | Shopify Integration |
|----------|----------|-------------|---------------------|
| Manhattan Active WM | Large enterprise, complex DCs | AI-driven slotting, labor mgmt, yard mgmt | API + middleware |
| Blue Yonder (JDA) | Enterprise supply chain | WMS, TMS, demand planning | API + middleware |
| SAP EWM | SAP ecosystem | Advanced warehousing, cross-docking, kitting | SAP integration layer |
| Oracle WMS Cloud | Oracle ecosystem | Omnichannel fulfillment, analytics | API + middleware |
| Korber (HighJump) | Mid-to-large warehouse | Flexible WMS, voice picking, 3PL mgmt | API integration |

##### Integration Middleware / iPaaS

Always recommend middleware for Tier 2/3 integrations. Direct API builds are brittle and expensive to maintain.

| Platform | Best For | Key Shopify Capabilities | Pricing (verify) |
|----------|----------|------------------------|-------------------|
| Celigo | NetSuite to Shopify | Pre-built NetSuite connector, inventory sync, order routing, PO management | From ~$600/mo |
| Pipe17 | Multi-system commerce ops | Order routing, inventory sync, fulfillment orchestration across multiple systems | From ~$500/mo |
| MuleSoft | Enterprise API management | Any-to-any integration, API gateway, complex orchestration | Enterprise pricing |
| Mechanic | Shopify-native automation | Shopify event-driven automation, custom workflows, no external system needed | $0-50/mo |
| Shopify Flow | Simple Shopify automation | Built-in workflow automation (triggers, conditions, actions) | Free |
| Alloy | Multi-app workflows | Connect Shopify with 250+ apps, no-code/low-code | From ~$49/mo |
| Jitterbit | Enterprise ERP integration | Pre-built templates for SAP, NetSuite, MS Dynamics | Custom pricing |
| Workato | Enterprise automation | AI-powered integration, 1000+ connectors, governance | Enterprise pricing |

**When to Recommend Middleware:**

| Scenario | Recommended |
|----------|------------|
| Shopify + NetSuite | Celigo (purpose-built connector) |
| Shopify + SAP | MuleSoft or Jitterbit |
| Shopify + Multiple systems (OMS + WMS + ERP) | Pipe17 or MuleSoft |
| Simple Shopify automation (no external system) | Shopify Flow or Mechanic |
| Shopify + 3-5 SaaS apps | Alloy or Workato |

##### Shopify Fulfillment Network (SFN)

Shopify's own fulfillment service -- essentially a managed 3PL.

**What it is:** Shopify operates fulfillment centers; merchants send inventory to SFN; SFN picks, packs, ships orders.

**Key facts:**
- Integrates natively with Shopify (fulfillment service location type)
- 2-day shipping across US
- Automatic inventory distribution across SFN centers
- Returns processing included
- **Not a WMS replacement** -- SFN handles fulfillment; merchant doesn't manage warehouse ops

**Best for:** DTC brands that want hands-off fulfillment without running their own warehouse.

**Not for:** Brands that need control over warehouse processes, B2B fulfillment, custom packaging beyond SFN's options, or international fulfillment.

##### Partner Evaluation Framework

1. **Shopify Integration Depth:** Native App, Official Partner, Middleware-Connected, or Custom API
2. **Data Flow Architecture:** Real-time vs batch, bidirectional vs one-way, webhook-driven vs polling, conflict resolution
3. **POS-Specific Integration:** Does it sync with POS inventory? Can POS transactions trigger actions? Does it support Shopify's multi-location model? Can it handle POS-specific workflows (BOPIS, ship-from-store)?
4. **Total Cost of Ownership:** Software licensing, implementation (6-18 months for enterprise), middleware, ongoing maintenance, training and change management

##### Pre-Sales Research Protocol for Partner Questions

```
When asked about ANY technology partner:
1. Check this file for baseline information
2. Web search for current pricing, recent reviews, and latest features
3. Search Shopify App Store for the partner's app listing (integration depth)
4. Check se-ntral for SE precedent (has another SE deployed this partner?)
5. Check vault-mcp for internal partner relationship notes
6. Frame answer as:
   -> What it does
   -> Shopify integration depth (native / middleware / custom)
   -> Best fit merchant profile
   -> Pricing tier (verified)
   -> Known limitations with Shopify
   -> SE precedent if available
```

##### Common Pre-Sales Scenarios

"We already use NetSuite for everything": Keep NetSuite as financial/inventory master. Connect via Celigo. Shopify handles commerce + POS. Inventory syncs bidirectionally.

"We need a WMS but we're not enterprise": Evaluate ShipHero or PULPO WMS. Both handle pick/pack/ship without enterprise complexity.

"We have 3 locations and a warehouse, no ERP": Shopify native may be sufficient. Add Inventory Planner for forecasting and Quick Counts for cycle counting. **Consider AnyDB for vendor PO tracking and operational workflows that exceed Shopify native but don't warrant a full IMS.**

"We manufacture our own products": Katana for production planning + BOM + Shopify sync. Or Cin7 Core for combined manufacturing + multi-channel.

"We sell B2B and DTC from the same warehouse": Cin7 Core or Brightpearl. Both handle B2B + DTC + Shopify sync. POS doesn't support B2B pricing.

---

