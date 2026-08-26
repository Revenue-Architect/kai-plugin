# Shopify Taxes

Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.
Validate current behavior through the canonical vendor source before production guidance.

## Recent feature updates (auto-curated)

<!-- BEGIN AUTO-CURATED UPDATES -->
- [AUTO-CURATED] 2026-05-14 - [Updates to Italy's Sardinian province definitions](https://changelog.shopify.com/posts/italy-s-sardinian-province-definitions-updated)
  - Source: Shopify merchant changelog; route: Shopify Taxes; categories: Admin
  - Note: We've updated Italy's province definitions to reflect the Sardinian administrative restoration that took effect in June 2025: * Gallura Nord-Est Sardegna (OT) is now a selectable province * Carbonia-Iglesias (CI) has been renamed to Sulcis Iglesiente to match the restored province name. Merchants shipping to Sardinia may notice updated province names in checkout. Partners using the address validation or autocomplete...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-13 - [Shopify Tax has expanded to Canada](https://changelog.shopify.com/posts/shopify-tax-has-expanded-to-canada)
  - Source: Shopify merchant changelog; route: Shopify Taxes; categories: Admin
  - Note: Managing Canadian sales tax is complicated, which is why we're committed to making it better. Shopify Tax is bringing brand new features to your admin that will make it easier to collect the right amounts at the right time, and know where your business is liable. New Enhanced calculations Stay confidently compliant selling across Canada knowing that Shopify Tax is accurately calculating sales tax rates (GST, HST, PS...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
- [AUTO-CURATED] 2026-05-04 - [Apply discounts to items on the refund page](https://changelog.shopify.com/posts/apply-discounts-to-items-on-the-refund-page)
  - Source: Shopify merchant changelog; route: Shopify Taxes; categories: Admin
  - Note: What changed When issuing a refund from the refund page, you can now add, update, or remove a discount on eligible items without leaving the refund page. How it works 1. Open an order and navigate to the refund page. 2. Add, update, or remove a discount on any eligible item. 3. The page updates with the revised outstanding balance. 4. Issue the refund against the discounted amount. Why it matters Previously, applyin...
  - Freshness rule: validate canonical vendor docs/MCP before production guidance.
<!-- END AUTO-CURATED UPDATES -->

## Canonical validation rule

- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.
- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.
- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.
