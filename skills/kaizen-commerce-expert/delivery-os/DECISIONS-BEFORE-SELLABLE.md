# Decisions KaizenCommerce Must Make Before This Wedge Is Sellable

The Delivery OS is structurally complete (Blueprint built deep, packs 2–5 outlined, and the Engagement Baseline now supports Shopify Referral exceptions). These are the open commercial and technical decisions that the partners must resolve before promoting this as a fixed-scope or repeatable package. Each is a partner-judgment call the OS deliberately does not pre-decide.

## Commercial decisions
1. **Fixed-scope vs scoped-from-Baseline.** Does the wedge ever get a published fixed price, or does every engagement stay scoped from an approved Engagement Baseline? Current brain says two lanes: Blueprint/advisory or full implementation after scoping — confirm whether published package pricing ever replaces partner-scoped pricing.
2. **Blueprint credit mechanics.** The [BLUEPRINT_FEE] credits against implementation. Confirm: credits against any tier? Expires? Applies to AnyDB builds too, or POS only?
3. **Shopify Referral economics.** If a Shopify referral skips the paid Blueprint, confirm whether a paid discovery-validation step replaces the Blueprint fee, whether any referral-specific terms apply, and exactly how the proposal shows no Blueprint credit.
4. **Ops Care default attach.** Is Ops Care offered to every launched account by default, or only where the Engagement Baseline scores retainer fit? Sets the post-launch revenue model.
5. **Tier boundaries at the edges.** A 5-vs-6 location merchant straddles Silver/Gold. Decide the tiebreaker rule (location count vs data volume vs complexity).
6. **Data cap enforcement.** How strictly is the cap enforced before a change order fires? Define the tolerance band.

## Technical decisions
7. **API-first lane criteria.** Define the explicit conditions under which the lane drops from API to Matrixify to Admin CSV. The decision tree in Pack 2 needs these thresholds from the CTO.
8. **Shopify behaviors needing current-doc verification.** Several areas (gift card / store credit migration, metaobjects, B2B/POS permission mapping) carry `[FLAG]` markers. The CTO should verify each against current Shopify documentation before any of it becomes a written commitment. **Do not let these flags ship in a client SOW unverified.**
9. **Referral validation thresholds.** Decide which `[DISCOVERY-INFERRED]` items can remain as SOW assumptions and which must be validated before the SOW is sent, beyond the Pack 2 rule that migration-critical inferred items block Dry Run/cutover.
10. **Reconciliation tolerance.** What count-match tolerance is acceptable at cutover (exact, or a defined band per entity)?
11. **Rollback definition.** What "rollback" actually means given Shopify's model — define it precisely before promising it.

## Asset-build decisions
12. **Single owner per pack.** Assign a partner as owner of each pack's content so it stays current as engagements teach you more.

## Inputs still needed from the partners
- The CTO's lane-decision thresholds (drives Pack 2)
- Verified Shopify behavior for the flagged edge cases (drives Pack 2 + Pack 5)
- A real recent engagement to pressure-test the Engagement Baseline against (does the Baseline capture everything that actually came up?)
- Confirmed pricing edges, Blueprint credit rules, and Shopify Referral economics (drives Pack 5)

*KaizenCommerce | kaizencommerce.ca | Internal — Confidential*
