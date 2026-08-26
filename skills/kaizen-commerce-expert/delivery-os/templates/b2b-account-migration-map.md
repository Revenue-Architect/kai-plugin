# Template — B2B Account Migration Map

Entity-by-entity migration scope for a B2B engagement. Peer of `migration-entity-map.md`, which
covers the retail/catalog side. Use both when a merchant migrates retail and wholesale together.

Anything not named here is out of scope until it is added here with an owner and an estimate.

**Merchant:** ______  **Source system:** ______  **Target plan:** ______  **Cutover window:** ______

---

## Part A — Scope decisions (settle before estimating)

| Decision | Options | Chosen | Rationale |
|---|---|---|---|
| Historical orders | Reference-only / full import / none | | Drives effort more than any other line |
| Open AR balances | Stay in ERP / migrate | | Usually stays in ERP. Confirm, never assume |
| Draft orders and quotes in flight | Freeze / migrate / recreate | | Always noticed at go-live if skipped |
| Customer accounts | Already new / migrating from legacy | | B2B requires new customer accounts |
| Pricing authoring direction | Shopify authors / ERP authors | | Two-way price sync is a known failure point |

---

## Part B — Entity map

| Entity | Source | Count | Target | Method | Owner | Status |
|---|---|---|---|---|---|---|
| Companies | | | Company | | | |
| Company locations | | | CompanyLocation | | | |
| Company contacts | | | Customer + contact role | | | |
| Location permissions | | | Location-level permissions | | | |
| Catalogs | | | Catalog | | | |
| Publications (assortments) | | | Publication | | | |
| Price lists | | | PriceList | | | |
| Fixed prices | | | PriceList fixed prices | | | |
| Percentage adjustments | | | PriceListParent adjustment | | | |
| Quantity rules | | | Quantity rules | | | |
| Volume price breaks | | | Quantity price breaks | | | |
| Payment terms assignments | | | BuyerExperienceConfiguration | | | |
| Tax exemptions / certificates | | | TaxExemption | | | |
| Historical orders | | | Order (import) | | | |
| Open orders / backorders | | | | | | |
| Draft orders / quotes | | | DraftOrder | | | |
| ERP account code mapping | | | Metafield or external ID | | | |

---

## Part C — Catalog budget check

Non-Plus caps at **3 active catalogs across all B2B markets**, assigned via Markets. Plus allows
unlimited catalogs and direct company/location assignment.

| Question | Answer |
|---|---|
| Distinct pricing tiers in the source system | |
| Distinct product assortments | |
| Catalogs needed under the pricing-only + publication-only split | |
| Merchant's plan | |
| **Fits natively?** | Yes / No — if No, name the path: Plus upgrade, operating layer, or tier consolidation |

If the answer is No and the merchant will not upgrade, the pricing model must be consolidated or
moved into the operating layer. Decide this before build, not during.

---

## Part D — Reconciliation targets

| Entity | Source count | Target count | Variance | Explained | Sign-off |
|---|---|---|---|---|---|
| Companies | | | | | |
| Company locations | | | | | |
| Company contacts | | | | | |
| Price list entries | | | | | |
| Historical orders | | | | | |

Zero unexplained variance before go-live. An explained variance needs a written reason, not a shrug.

---

## Part E — Cutover freeze plan

| Item | Freeze starts | Owner | Recovery if late |
|---|---|---|---|
| New company/account creation in source | | | |
| Price list edits in source | | | |
| Draft orders and quotes | | | |
| Open order entry | | | |

Name who tells the sales reps the freeze has started. A B2B freeze fails when reps keep quoting.
