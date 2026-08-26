# Kaizen Proposal Good/Bad Examples

These are synthetic examples for Kai quality training. They are not Kaizen client artifacts.

## Example 1: Generic Executive Summary

Input:

```text
Merchant: 4-store retailer on Square POS. Wants Shopify POS. 38K products, 12K customers. Manual
inventory count every Friday. No ERP. Wants go-live before September.
```

Weak output:

```text
We are pleased to present a Shopify POS implementation proposal for your business. KaizenCommerce
will provide a seamless migration from Square to Shopify, including products, customers, inventory,
training, and support.
```

Why it fails:

- generic and reusable
- uses banned filler
- ignores 38K products, 12K customers, weekly inventory count, and September pressure
- does not explain why Blueprint or migration controls matter

Strong output:

```text
Your current Square setup is forcing the team to manually rebuild inventory confidence every Friday.
That is the operational problem to solve before September: not just moving 38K products and 12K
customers into Shopify, but proving store inventory is accurate enough for staff to sell from it
without a weekly reset.

Kaizen's recommendation is a controlled Shopify POS migration with inventory validation, data
quality gates, role-based training, and a go/no-go cutover. The work should stay API-first unless
sample data proves a file-based lane is safer for a specific entity. Final implementation scope
depends on product export quality, customer merge rules, inventory by location, and gift card or
historical order requirements if those enter scope.
```

Why it works:

- merchant-specific
- ties scope to the operating pain
- avoids unsupported certainty
- protects final scope

## Example 2: Weak Pricing Rationale

Weak output:

```text
Gold is recommended because the migration is complex and Kaizen has deep experience with Shopify
POS.
```

Why it fails:

- "complex" is not evidence
- experience is not a buyer-specific value argument
- no scope boundaries
- no risk gates

Strong output:

```text
Gold is directionally appropriate if the approved scope includes products, customers, inventory by
location, staff training, and go-live support across all four stores. The rationale is the
combination of data volume, location-level inventory validation, September timing, and the need to
protect store operations during cutover.

This tier should not be finalized until three inputs are confirmed: product export quality, customer
merge rules, and whether gift cards or historical orders are in scope.
```

Why it works:

- ties tier to scope drivers
- uses conditional language
- names missing inputs
- avoids invented ROI

## Example 3: Weak Risk Register

Weak output:

```text
Risk: migration delays.
Mitigation: Kaizen will manage the project carefully.
```

Why it fails:

- vague risk
- no owner
- no trigger
- no evidence gate

Strong output:

```text
Risk: product variants or SKUs do not map cleanly from Square into Shopify.
Trigger: sample export shows duplicate SKUs, missing option values, or product-level data repeated
on variant rows.
Mitigation: run sample data validation before final import planning, isolate cleanup rules, and
approve the target product model before generating the full migration package.
Owner: Kaizen technical lead.
Client responsibility: provide untouched source exports and approve any product model decisions.
```

Why it works:

- concrete
- testable
- owned
- connected to scope and client responsibility
