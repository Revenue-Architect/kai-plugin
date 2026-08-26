# Good vs Bad: Decision Review

Use when running `kaizen-check` Mode 6 or stress-testing a recommendation.

## Bad

"The recommendation seems sound. Shopify POS is a good fit, AnyDB may be useful later, and the
main risk is implementation complexity."

## Why It Fails

- No evidence separation
- No kill condition
- No runner-up option
- "Implementation complexity" is vague
- Does not tell the operator what to do next

## Good

"Verdict: SOUND WITH CONDITIONS.

Recommendation being reviewed: sell Blueprint/advisory, not full implementation, for a 6-location
retailer currently on Lightspeed with unknown data quality.

Evidence base:
- Confirmed: 6 locations, Lightspeed is current POS, merchant wants Shopify POS.
- Inferred: Gold is the likely implementation tier if the Blueprint confirms normal data volume.
- Assumed: product/customer counts are inside Gold's 150K cap.
- Estimated: 5-10 week implementation window, subject to export quality and training availability.

Strongest reason this could be wrong: if the merchant has clean exports, low data volume, no
gift cards, and no ERP, a Silver-like scope may be commercially more accurate despite 6 locations.

Runner-up option: quote implementation now. It loses because data volume, export quality, gift
cards, and staff readiness are not confirmed.

Kill conditions:
1. If final product/customer count exceeds 150K, re-scope beyond Gold.
2. If ERP owns product or inventory, architecture review becomes mandatory before implementation.

Required fix before committing: ask for sample exports and confirm gift card/loyalty requirements
inside the Blueprint."

## Why It Works

- Makes confidence explicit
- Tests the recommendation against a credible alternative
- Names what changes the recommendation
- Ends with one practical action
