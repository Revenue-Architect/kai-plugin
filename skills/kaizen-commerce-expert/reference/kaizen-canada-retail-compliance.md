# Canada Retail Compliance — Tax, Language, Payments

Load this file when a Canadian merchant engagement touches sales tax setup, Quebec French-language
obligations, or Canada-specific POS payment behavior. Facts below carry a source and a
verified-on date. Rates and thresholds change: for client-facing or filing-adjacent claims, treat
anything past its verified date as `[VERIFY]` and confirm against the linked source (this file is
in scope for the Vendor Freshness Auto-Gate). Kai advises on system configuration and operational
impact; filing obligations and legal interpretations go to the merchant's accountant or counsel —
say so explicitly in deliverables.

## Sales Tax Landscape (verified 2026-07-02)

| Regime | Where | Rate | Notes |
|---|---|---|---|
| GST | Federal, everywhere | 5% | Base tax in non-HST provinces |
| HST | ON | 13% | Harmonized, CRA-administered |
| HST | NB, NL, PE | 15% | — |
| HST | NS | 14% | Cut from 15% effective 2025-04-01 — check invoices/quotes that straddle the change |
| QST | QC | 9.975% | Administered by Revenu Québec, separate registration from CRA GST |
| PST | BC 7%, SK 6%, MB 7% | — | Separate provincial registrations on top of 5% GST |
| None | AB, YT, NT, NU | GST only | — |

Sources: [Canada.ca GST/HST rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html),
[PwC Canada tax summary](https://taxsummaries.pwc.com/canada/corporate/other-taxes).

- **Registration threshold:** GST/HST registration is required once worldwide taxable revenues
  exceed $30,000 CAD over four consecutive calendar quarters (or a single quarter). Below that, a
  merchant is a "small supplier" and registration is optional. Quebec QST has its own registration
  with Revenu Québec.
- **Shopify's role:** Shopify calculates and collects the configured taxes at checkout/POS by
  destination and registration, but **does not remit** to CRA or Revenu Québec. The merchant (or
  their accountant) tracks per-province collections and files. Set registrations under
  Settings → Taxes and duties → Canada; POS locations must carry the right provincial defaults.
  Source: [Shopify Canadian taxes reference](https://help.shopify.com/en/manual/taxes/canada/canada-tax-reference)
  (verified 2026-07-02).
- **Diagnostic checks:** multi-province retailers with one blanket tax rate; QST registration
  missing while selling into Quebec; tax-included vs tax-excluded pricing inconsistencies between
  POS and online; NS invoices still at 15% after 2025-04-01.

## Quebec French Language (Bill 96 / Law 14) (verified 2026-07-02)

Key obligations for retailers, in force 2025-06-01 unless noted:

- **Products:** all inscriptions on products sold in Quebec (including packaging, wrapping,
  accompanying documents, directions, warranty certificates) must be in French with no other
  language more prominent. Descriptive/generic terms inside a non-French trademark must be
  translated. Grace period: non-compliant products manufactured before 2025-06-01 may sell
  through until **2027-06-01**.
- **Storefront signage:** a recognized non-French trademark on signage visible from outside must
  be accompanied by **markedly predominant** French text.
- **E-commerce:** the rules apply to products sold into Quebec online, regardless of warehouse
  location. Contracts of adhesion (including online checkout terms) must be presented in French
  first.
- **Francisation:** businesses with 25+ employees must register with the OQLF and complete a
  francisation process.
- **Kai relevance:** catalog migrations for Quebec retailers must preserve/add French product
  content (use `variants/fr-ca-mode.md` and `reference/kaizen-fr-ca-glossary.md`); storefront and
  theme work must respect French predominance; receipts, notifications, and customer-account
  surfaces for Quebec stores should be configured in French. Flag gaps as findings in Blueprints —
  do not provide legal conclusions.

Sources: [Stikeman Elliott on Bill 96 signage/packaging](https://stikeman.com/en-ca/kh/competitor/bill-96-new-rules-for-the-use-of-trademarks-on-commercial-signage-and-product-packaging),
[McCarthy Tétrault on the 2025-06-01 requirements](https://www.mccarthy.ca/en/insights/blogs/consumer-markets-perspectives/french-language-requirements-bill-96-and-june-1-2025-common-misconceptions),
[CFIB Law 14 guide](https://www.cfib-fcei.ca/en/site/qc-law-14-bill-96).

## Canada POS Payments (verified 2026-07-02)

- **Interac debit on Shopify POS:** supported with compatible readers (tap and chip+PIN). Canada
  specifics: debit cards **tap only** (no insert for debit); PIN entry happens on the iPad/iPhone;
  Interac tap limit **$100 CAD** by card, up to **$200** via Apple Pay/Google Pay wallets —
  higher-ticket retail (jewelry, furniture) must plan for credit or wallet flows at the counter.
  Interac refunds must be in person with the card present. Source:
  [Shopify Tap & Chip supported payments](https://help.shopify.com/en/manual/sell-in-person/hardware/card-readers/tap-chip/supported-payment-types-and-availability).
- **Shopify Payments payouts (Canada):** minimum settlement 3 business days; no minimum payout
  amount; CAD payout to a Canadian CAD checking account avoids multi-currency payout fees. On
  Advanced/Plus, two bank accounts can split CAD and USD payouts — relevant for cross-border DTC
  sellers pricing in USD. Source:
  [Shopify payouts in Canada](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/canada/payouts).
- **Diagnostic checks:** debit-heavy verticals underestimating the Interac tap ceiling; refund
  workflows that assume cardless debit refunds; USD pricing with CAD-only payout setups eating
  conversion fees.

## Refresh Discipline

When citing any figure here in a client deliverable, restate its verified date. If the claim is
filing-adjacent (registration, remittance, francisation deadlines), add the accountant/counsel
referral line. Re-verify this file's facts when the vendor-freshness snapshot refresh runs, and
whenever a provincial budget cycle (spring) or Shopify Editions (winter/summer) lands.
