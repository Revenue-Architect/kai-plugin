---
name: kaizen-risk-matrix
description: Unified risk matrix for Kaizen engagements. Standard migration risks, POS-specific risks, ERP conditional risks, B2B conditional risks, and operational readiness risks. Load in kaizen-diagnose (Risks section), kaizen-propose (scope protection language), and kaizen-migrate (rollback planning).
---

# Risk Matrix Reference

## 1. Standard Risks (Apply to All Engagements)

| # | Risk | Impact | Likelihood | Mitigation |
|---|------|--------|------------|-----------|
| R1 | **Data migration corruption / data loss** | Critical | Medium | Run lane-specific validation 2–3 times; validate in dev store or sandbox; never migrate directly to production; reconciliation check post-live import |
| R2 | **In-flight order reconciliation failure** | High | Low–Medium | Keep open orders in legacy system through cutover; import as completed orders 30 days post-launch; never attempt to migrate active payment tokens |
| R3 | **Passwords cannot migrate** | Low | Certain | Passwords never migrate (different hashing algorithms). Plan for passwordless magic links or forced password reset. Communicate to customers pre-launch. |
| R4 | **Scope creep during migration** | Medium | High | Define MVP feature set and data scope in blueprint; explicit data caps in SOW; change-order process documented in kaizen-scope |
| R5 | **Third-party app performance impact** | Medium | High | Audit every app's JS payload; benchmark before/after each install; prefer Built for Shopify apps; cap at 10–15 apps |
| R6 | **Staff not ready at go-live** | High | Medium | Training starts in Week 2, not Week 6; quick reference guides in hands before cutover; super-user identified at each location |
| R7 | **Data quality in legacy system worse than expected** | High | Medium | Validate data sample in discovery (not just count rows — look at field completeness); flag in Blueprint; data prep adds to timeline |
| R8 | **Cutover extends beyond window** | Medium | Low–Medium | Dry-run the cutover sequence; assign roles; define abort criteria before the window opens; run kaizen-test-exec cutover simulation |

---

## 2. POS-Specific Risks (Always In Scope for Kaizen)

| # | Risk | Impact | Likelihood | Mitigation |
|---|------|--------|------------|-----------|
| P1 | **Hardware procurement lead times missed** | High | Medium | Order hardware in Week 0–1; 4–8 week lead times on Shopify POS Terminal, Hub, card readers; document expected delivery dates in hardware plan |
| P2 | **Parallel-run period creates staff confusion** | Medium | High | Designate which system is used for which transactions during parallel; clear written instructions; super-user support on the floor |
| P3 | **Controlled cutover exposure** | Critical | Low | Lane-specific validation gates are non-negotiable; kaizen-validate must PASS before live import; no skipping validation gates under time pressure |
| P4 | **Inventory count discrepancy at cutover** | High | Medium | Physical count 24–48 hours pre-cutover; reconcile against the selected migration lane output; kaizen-reconcile inventory mode before go-live |
| P5 | **Gift card balances not reconciled** | High | Low–Medium | Gift card total liability must match exactly; kaizen-reconcile gift card audit is required, not optional |
| P6 | **Smart Grid not configured for staff workflows** | Medium | Medium | Build Smart Grid layout in kaizen-shopify-config based on actual transaction types; demo during training; leave time for adjustments |
| P7 | **Network/WiFi inadequate at location** | High | Low | Network assessment in kaizen-hardware for every location; Shopify POS requires reliable WiFi; cellular backup for payment processing |
| P8 | **Multi-location inventory not reconciled per location** | High | Medium | Reconcile inventory per-SKU per-location, not just total; kaizen-reconcile inventory mode; never declare "inventory matches" on aggregate count alone |

---

## 3. ERP Conditional Risks (When ERP Integration Is In Scope)

| # | Risk | Impact | Likelihood | Mitigation |
|---|------|--------|------------|-----------|
| E1 | **ERP integration breaks in production** | Critical | Medium | Test with real transaction data; plan for the "Last 10%" edge cases (see [`kaizen-erp-patterns.md`](kaizen-erp-patterns.md)); maintain parallel systems during transition |
| E2 | **ERP credentials / sandbox access delays project** | Medium | High | Request ERP access in Week 0 onboarding; add to Data Access Checklist in kaizen-onboard |
| E3 | **Order edit flow not handled** | High | Medium | Shopify `orders/edited` webhook is separate from `orders/create`; ERP must handle post-creation updates; scope this explicitly |
| E4 | **QuickBooks Desktop (vs Online) API gap** | Medium | Medium | QBO connectors don't work with QB Desktop; if merchant has QB Desktop, custom middleware or QBO migration is required — flag in discovery |
| E5 | **Character encoding issues (SAP environments)** | Low | Medium | SAP defaults to ISO-8859-1; ensure UTF-8 conversion in any data pipeline |
| E6 | **NetSuite saved search row limit** | Low | Low–Medium | NetSuite Saved Search default row limit is 1,000; configure pagination in Celigo flows |
| E7 | **Inventory sync drift over time** | High | Medium | Use absolute `set` calls (not delta `adjust`) for inventory sync; reconcile on schedule |

---

## 4. B2B Conditional Risks (When Wholesale Is In Scope)

| # | Risk | Impact | Likelihood | Mitigation |
|---|------|--------|------------|-----------|
| B1 | **Shopify B2B native coverage gap discovered late** | High | Medium | Audit all B2B requirements in Blueprint against native capabilities; flag custom gaps before proposing scope |
| B2 | **Plan ceiling not surfaced at scoping** | High | Medium | B2B companies and price lists work on every paid plan since 2026-04-02. Plus is still required for more than 3 active catalogs, per-company catalog assignment, partial payments, deposits, and Checkout UI Extensions. Confirm the merchant's plan in discovery and state the ceiling in the proposal |
| B3 | **Price list volume (1,000+ companies)** | Medium | Low | Manual price list management won't scale; scope ERP-driven Catalogs API sync from the start |

---

## 5. Operational Readiness Risks (Severity Scales by Maturity)

See `kaizen-operational-readiness.md` for maturity scoring. These risks increase significantly in Emerging merchants.

| # | Risk | Emerging Impact | Established Impact | Advanced Impact |
|---|------|----------------|-------------------|----------------|
| OR1 | **Team not trained on Shopify at go-live** | CRITICAL — may stall operations | Moderate | Low |
| OR2 | **No internal technical champion** | High — decisions stall | Moderate | Low |
| OR3 | **No rollback / incident response plan** | Critical | Moderate | Low |
| OR4 | **Stakeholder misalignment on scope** | High | Moderate | Low |
| OR5 | **Post-launch ownership unclear** | High — merchant leans on Kaizen indefinitely | Moderate | Low |
| OR6 | **Integration monitoring absent** | High — breaks surface via customer complaints | Moderate | Low |

---

## 6. Risks That Are NOT Kaizen's Default Scope

These risks exist but are typically out-of-scope for standard Kaizen engagements. Flag them if present; don't absorb them without a change order.

- **SEO redirect management** — URL mapping and 301 redirect strategy is out of standard scope; can be added as a change order
- **Custom app development** — if build-vs-buy analysis surfaces a CUSTOM BUILD verdict, that is a separate scope line
- **ERP implementation changes** — Kaizen connects to ERP; Kaizen does not reconfigure the ERP
- **Data compliance / GDPR / RTBF** — flag if merchant is in regulated industry or EU market; outside standard scope
