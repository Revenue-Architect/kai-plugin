---
name: kaizen-signal-inference
description: Signal inference chains for auto-resolving system gaps before asking discovery questions. Load in kaizen-qualify (PRE-CALL) and kaizen-architect to skip questions already answered by known signals.
---

# Signal Inference Chains

Use these chains during discovery prep and architecture work. If a confirmed signal matches a chain, auto-resolve the inferred system — upgrade its confidence and **do not ask the user about it.**

Announce resolved inferences before presenting remaining questions so the user can correct:
> "From what you've shared: QuickBooks inferred from Square POS history — will map as accounting integration. Correct me if wrong."

---

## POS Platform → Accounting / ERP

| Confirmed Signal | Inferred System | Confidence | Action |
|-----------------|----------------|-----------|--------|
| Square POS confirmed | QuickBooks Online or Xero (likely) | INFERRED | Skip generic "what accounting?" — ask specifically: "QuickBooks or Xero for accounting?" |
| Lightspeed R-Series confirmed | QuickBooks, Xero, or Sage (80% of cases) | INFERRED | Ask targeted: "Which accounting system connects to Lightspeed?" |
| Lightspeed X-Series confirmed | More likely to have ERP (Lightspeed X attracts larger retailers) | INFERRED | Treat as Growing Multi-Location; probe ERP specifically |
| Heartland Retail confirmed | QuickBooks common; some have custom accounting | INFERRED | Ask "QuickBooks, NetSuite, or something else for accounting?" |
| Revel Systems confirmed | More likely to have ERP (Revel attracts multi-location restaurant/retail) | INFERRED | Probe ERP; also infer iPad-based hardware preference |
| Clover confirmed | QuickBooks common; smaller merchants | INFERRED | Likely Simple Retail profile; accounting = QuickBooks |
| Teamwork Commerce confirmed | Mid-to-large retailer; likely has ERP (NetSuite, D365 common) | INFERRED | Skip "do you have an ERP?" — ask "NetSuite or D365 for your ERP?" |

---

## POS Platform → Loyalty & CRM

| Confirmed Signal | Inferred System | Confidence | Action |
|-----------------|----------------|-----------|--------|
| Lightspeed with Marsello | Marsello loyalty confirmed | CONFIRMED | Skip loyalty question; flag Marsello migration as in-scope |
| Lightspeed with Mailchimp connected | Email marketing = Mailchimp | CONFIRMED | Note Klaviyo migration likely needed |
| Square with Square Loyalty | Square Loyalty confirmed; will not migrate natively | CONFIRMED | Flag loyalty gap — Shopify native or third-party (Smile.io) needed |
| Revel with third-party loyalty named | That loyalty platform | CONFIRMED | Skip loyalty question |

---

## POS Platform → Inventory Method

| Confirmed Signal | Inferred System | Confidence | Action |
|-----------------|----------------|-----------|--------|
| Single-location merchant confirmed | Simple inventory (no WMS) | CONFIRMED | Shopify native inventory is sufficient; skip WMS question |
| 5+ locations confirmed | Likely multi-location inventory complexity | INFERRED | Ask about transfer orders, stock allocation, and replenishment process |
| Lightspeed with purchase orders in use | Lightspeed PO module as inventory layer | CONFIRMED | Flag Lightspeed PO → Shopify purchase order workflow gap |
| Named WMS detected (Cin7, DEAR, Fishbowl, Brightpearl) | That WMS | CONFIRMED | Skip WMS question; RETAIN & INTEGRATE verdict; probe sync direction |

---

## ERP / Accounting Platform → Integration Complexity

| Confirmed Signal | Inferred System | Confidence | Action |
|-----------------|----------------|-----------|--------|
| QuickBooks Online confirmed | Simple accounting sync only (not ERP-level) | CONFIRMED | Recommend third-party connector (Bench, A2X, QuickBooks Connector); not on critical path |
| QuickBooks Desktop confirmed | Higher complexity — Desktop ≠ Cloud API | INFERRED | Flag: QBO connector apps don't work with Desktop; requires middleware or upgrade to QBO |
| NetSuite confirmed | Full ERP integration in scope | CONFIRMED | Load [`kaizen-erp-patterns.md`](kaizen-erp-patterns.md) for NetSuite section; add ERP integration to scope |
| Sage 50 / Sage 100 confirmed | Legacy ERP; limited API | INFERRED | Custom integration likely required; probe API availability |
| Microsoft Dynamics 365 Business Central confirmed | Mid-tier ERP; good API | CONFIRMED | Load [`kaizen-erp-patterns.md`](kaizen-erp-patterns.md) for D365 section |
| SAP Business One confirmed | SMB ERP; Service Layer API | CONFIRMED | Load [`kaizen-erp-patterns.md`](kaizen-erp-patterns.md) for SAP B1 section |
| Shopify already in use (Shopify → Shopify migration) | Integration complexity is low; focus on data shape | CONFIRMED | Load [`kaizen-platform-migrations.md`](kaizen-platform-migrations.md) Shopify-to-Shopify section |

---

## Staff & Team Signals → Operational Maturity

| Confirmed Signal | Inferred Maturity Dimension | Action |
|-----------------|---------------------------|--------|
| "Our IT person handles everything" | Low tech ops maturity (Emerging) | Flag SI dependency in scope |
| "We have an in-house dev" | Established+ tech ops | Adjust training timeline; merchant can own integrations post-launch |
| "We use Slack + project management tools internally" | Established process maturity | Standard change management assumption |
| "We've migrated platforms before" | Established+ change management | Shorten change management risk; ask what they learned |
| "We've never done anything like this" | Emerging change management | Budget extra change management support; flag in Blueprint |
| Large franchise with 20+ locations but no IT department | Critical gap: Low tech ops + high complexity | Flag in Blueprint as highest engagement risk |

---

## Channel & Scope Signals

| Confirmed Signal | Inferred | Action |
|-----------------|---------|--------|
| Merchant sells online + in-store | Shopify POS + Online Store both in scope | Skip "do you have an online store?" |
| Merchant named in product description as a gift shop / specialty food | Likely Simple Retail or Growing; vertical = gift/specialty food | Route kaizen-catalog-review to gift/specialty food vertical |
| Merchant has wholesale pricing tiers mentioned | Native B2B or price list logic in scope on any paid plan | Probe account count, distinct pricing tiers, and current plan. More than 3 tiers or per-company pricing points to Plus or an operating layer |
| Gift cards mentioned or visible on website | Gift card migration in scope | Add to migration scope; verify current Shopify handling through Shopify Dev MCP; flag gift card balance reconciliation in kaizen-reconcile |
| Multiple currencies mentioned | Shopify Markets in scope | Flag Markets setup in kaizen-shopify-config; probe tax + pricing per market |
