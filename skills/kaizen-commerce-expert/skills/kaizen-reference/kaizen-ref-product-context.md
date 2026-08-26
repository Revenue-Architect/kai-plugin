---
name: kaizen-ref-product-context
description: "Deep retail reference for product context questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["product context domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

## Product Context

### POS Plan Tiers

| Feature | POS Lite (Free) | POS Pro ($89/mo/location) |
|---------|-----------------|---------------------------|
| In-person selling | Yes | Yes |
| Staff PINs | Unlimited | Unlimited |
| Smart grid customization | Limited | Full |
| Inventory management | Basic | Advanced (transfers, POs, stock adjustments) |
| Analytics | Basic | Advanced retail reports |
| Omnichannel selling | Basic | Full (BOPIS, ship-from-store, local delivery) |
| Staff roles & permissions | Basic | Granular (24+ permissions) |
| Exchanges | No | Yes |
| Daily sale summaries | No | Yes |
| Quick Counts (cycle counting) | No | Yes |
| Cash management (register-level) | Basic | Full (reason codes, reconciliation) |

### Commerce Model Impact

- **D2C + Retail**: Full POS feature set available
- **B2B + Retail**: Limited. B2B catalog/pricing features NOT available in POS
- **Wholesale + Retail**: Separate pricing via POS discounts or B2B price lists (any paid plan; Plus for per-company assignment)
- **Franchise**: Multi-store via Shopify Plus with org-level management

### Technology Partner Decision Tree

```
< 500 SKUs, < 5 locations, no warehouse    -> Tier 1: Shopify Native + Apps
500-10K SKUs, 5-20 locations, basic WH     -> Tier 2: Mid-Market IMS/WMS
10K+ SKUs, 20+ locations, complex ops/ERP  -> Tier 3: Enterprise ERP/WMS
```

For merchants in the operational gap between Tier 1 and Tier 2 (the "spreadsheet chaos" zone), AnyDB serves as the operational control layer that sits behind Shopify POS.

