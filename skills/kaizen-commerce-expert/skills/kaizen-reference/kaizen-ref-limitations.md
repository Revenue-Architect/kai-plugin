---
name: kaizen-ref-limitations
description: "Deep retail reference for limitations questions routed by Kai."
metadata_version: 1
layer: retail-reference
upstream: ["kaizen-retail-expert-v2"]
downstream: []
adjacent: []
canon: []
owns: ["limitations domain reference"]
does_not_own: ["final implementation recommendation without routed skill context"]
---

### 3H. Known Limitations & Workarounds

---

#### Known Limitations

##### Inventory Limitations

| Limitation | Details | Workaround |
|-----------|---------|------------|
| No batch/lot tracking | Cannot track inventory by batch number or lot with expiry dates | Third-party apps (Katana, SKULabs) or custom metafield-based solution |
| No serialized inventory | Cannot track individual units by serial number | Metafields + custom app; or SKULabs, Finale Inventory |
| No demand forecasting | No built-in inventory forecasting or replenishment suggestions | Inventory Planner, Flieber, or ERP integration |
| No complex UoM | Cannot natively sell in multiple units of measure (box, pallet, each) | Custom development or app (e.g., Bold Custom Pricing) |
| No warehouse task management | No pick/pack/stage workflows for warehouse operations | ShipHero, ShipBob, Deposco, or custom WMS. **AnyDB can manage task queues.** |
| No custom inventory states | Limited to 5 states (available, committed, incoming, reserved, unavailable) | Use `unavailable` sub-reasons or custom app tracking |
| REST variant limit | REST API limited to 100 variants per product | Use GraphQL API (supports 2,048 variants) |
| No negative inventory alerts | System allows overselling; no proactive alerts for negative stock | Shopify Flow automation + notification, or third-party monitoring |
| No advanced GIS routing | Order routing doesn't optimize by geography with precision | Third-party OMS (Fluent Commerce, Manhattan) |
| No robust purchase orders (native) | Native PO functionality is basic and still maturing; advanced PO management not yet fully built into core | Third-party PO apps or ERP. **AnyDB can track PO lifecycle.** |
| No consignment inventory | Cannot track consigned stock separately from owned inventory | Metafield-based tracking + custom reporting |

##### POS-Specific Limitations

| Limitation | Details | Workaround |
|-----------|---------|------------|
| No restaurant features | No kitchen display, table management, tip pooling, menu management | Not a workaround. Recommend Square/Toast/Lightspeed Restaurant |
| Limited offline capability | Cash sales work offline; card authorization requires connectivity | Accept cash offline; queue card transactions for when online |
| No layaway | Cannot natively hold items with partial payment over time | Draft orders with partial payment; or third-party app |
| No appointment scheduling | No built-in booking/appointment system | BookThatApp, Sesami, Appointedd, or custom |
| No gift registry | No native gift registry at POS | Third-party apps (Gift Reggie, Wishlist Plus) |
| No commission tracking | Cannot natively calculate staff commissions | Commissionly, Rewardify, or custom tracking |
| No advanced barcode generation | Basic barcode support; no custom label design in POS | Retail Barcode Labels app, or label printer integration |
| POS Extensions != Online Checkout Extensions | Different extension systems; cannot reuse online checkout extensions in POS | Build separate POS UI Extensions |
| Customer-facing display requires separate app | Not built into core POS app; requires the Customer View app (Shopify recommended, app ID 2838) running on a second screen | Install Customer View app; pair via same WiFi network |
| B2B features not in POS | B2B catalog, company accounts, payment terms NOT available at POS | Draft orders with manual B2B pricing |
| No automatic reorder points | No trigger to auto-create POs when stock hits threshold | Shopify Flow + custom automation, or Inventory Planner/Flieber |
| Limited POS reporting (Lite) | POS Lite has minimal reporting | Upgrade to POS Pro for full retail reports |
| No employee scheduling | No shift scheduling or time-off management | Deputy, Homebase, When I Work |
| No integrated CCTV/security | No loss prevention integration | Third-party LP solutions |

##### Integration Limitations

| Limitation | Details | Workaround |
|-----------|---------|------------|
| No native ERP connector | No built-in SAP, NetSuite, Oracle integration | Middleware (Celigo, MuleSoft, Pipe17) or custom integration |
| Shipping labels not via API | Cannot purchase shipping labels programmatically | Must use Shopify admin UI; or integrate with ShipStation, EasyPost |
| No POS-specific webhooks | POS transactions use same order webhooks as online | Filter by `source_name` field in order webhook payload |
| Limited POS UI Extension access | Extensions can't modify core POS UI (only render in defined targets) | Work within available extension targets; request new targets |
| No real-time inventory push | Inventory changes notify via webhooks (slight delay) | Poll API for critical integrations; or use webhook + verify pattern |

##### Plan-Gated Limitations

| Feature | POS Lite (Free) | POS Pro ($89/mo) | Plus |
|---------|-----------------|-------------------|------|
| Exchanges | No | Yes | Yes |
| Returns | Original location only | Any location (cross-location) | Any location |
| Smart grid (full) | Limited | Full | Full |
| Automatic discounts at POS | No | Yes | Yes |
| Advanced inventory (transfers, POs) | No | Yes | Yes |
| Staff roles (granular) | Basic | Full (24+ permissions) | Full |
| Manager approval workflow | No | Yes | Yes |
| Required customer data capture | No | Yes (set fields as required) | Yes |
| BOPIS, ship-from-store | No | Yes | Yes |
| Daily sale summaries | No | Yes | Yes |
| Advanced reports | No | Yes | Yes |
| In-store analytics | No | Yes | Yes |
| Liquid receipt customization | No (header/footer only) | Yes (full Liquid templates) | Yes |
| POS Pro locations included | 0 | N/A | 20 free (all free w/ Shopify Payments) |
| Unlimited registers | 1 | Unlimited | Unlimited |

##### Regional / Market Limitations

| Limitation | Details |
|-----------|---------|
| POS Go availability | Only available in select markets (US, Canada, UK, Ireland, Australia -- verify) |
| Tap to Pay | Not available in all countries; expanding (verify per market) |
| Hardware shipping | Shopify hardware only ships to supported countries |
| Shopify Payments requirement | Card readers and Tap to Pay require Shopify Payments; not available in all countries |
| Tax calculation | Automated tax may not cover all jurisdictions; verify for specific country |
| Receipt language | Receipts may not support all languages natively |

##### Commonly Requested Missing Features

**High-Frequency Requests:**
1. **Serialized inventory tracking** -- by unit serial number
2. **Advanced purchase order management** -- with vendor portals
3. **Employee scheduling** -- shift management integrated with POS
4. **Customer-facing display** -- second screen showing transaction (available via Customer View app)
5. **Integrated loyalty at POS** -- native points/rewards (requires app today)
6. **Kitchen display system** -- for food service (not Shopify's market)
7. **Advanced barcode label design** -- custom label templates
8. **Layaway / payment plans** -- partial payment with item hold
9. **Integrated accounting** -- direct QuickBooks/Xero sync from POS
10. **Multi-currency at POS** -- accept multiple currencies in-store

**Medium-Frequency Requests:**
- Consignment management
- Rental/reservation system
- Repair/service ticket tracking
- Advanced age verification
- Weight-based selling (deli, bulk goods)
- Matrix/grid inventory view at POS
- Inter-store communication
- Advanced loss prevention reporting

##### How to Handle Limitations in Sales Conversations

**Framework: Acknowledge, Contextualize, Solve**

1. Acknowledge: "You're right, Shopify doesn't natively support [feature] today."
2. Contextualize: Explain why it's designed this way, or what's available instead.
3. Solve: App Store solution, custom development option, or AnyDB operational layer.

**Example:**
> **Merchant:** "We need serialized inventory tracking."
>
> **Response:** "Shopify doesn't have native serial number tracking at the inventory item level today. However, there are proven approaches:
> 1. **App Store:** SKULabs and Finale Inventory both support serialized tracking with Shopify integration
> 2. **Custom approach:** Use product metafields to store serial numbers, with a custom POS extension for scanning/recording serials at point of sale
> 3. **ERP integration:** If you're using an ERP with serialization (like NetSuite), maintain serials there and sync inventory totals to Shopify
>
> The right approach depends on your volume and complexity. Would you like me to dig into any of these?"

##### Gap -> Product Feedback Pipeline

When a limitation surfaces in a merchant conversation:
1. Check if it's already on roadmap (Vault, INTERNAL-ONLY)
2. If genuine gap -> suggest `/product-feedback` to draft Salesforce product feedback
3. Link feedback to specific merchant opportunity for prioritization signal
4. Note: never promise roadmap items to merchants

---

