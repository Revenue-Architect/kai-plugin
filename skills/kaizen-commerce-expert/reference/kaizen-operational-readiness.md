---
name: kaizen-operational-readiness
description: Merchant operational maturity model — Emerging / Established / Advanced across 5 dimensions. Scores readiness, shapes SI dependency language, and drives retainer tier positioning. Load in kaizen-diagnose (current state) and kaizen-propose (SI dependency, retainer pitch).
---

# Operational Readiness Model

Framework for assessing a merchant's organizational maturity during Shopify implementation planning. Used in the Blueprint current-state section to make scope and SI-dependency decisions explicit rather than assumed.

Applies whether Shopify has been chosen (execution readiness) or is being evaluated (platform fit). For pre-Shopify prospects, this model informs how Kaizen should position the engagement and what post-launch support will be needed.

---

## 1. Maturity Scoring

Score each dimension as Emerging (1), Established (2), or Advanced (3). Average across dimensions:
**1.0–1.6 = Emerging | 1.7–2.3 = Established | 2.4–3.0 = Advanced**

If ANY single dimension scores Emerging while the rest are Advanced, flag it as a **critical gap** — the weakest link determines real maturity.

| Dimension | Emerging | Established | Advanced |
|-----------|----------|-------------|----------|
| **Tech operations** | Systems managed manually or entirely by outside vendor. No documented runbooks. Break-fix model. | Core systems documented. Someone on staff owns tech vendors. Mix of manual + automated monitoring. | Documented processes for every system. Internal ownership. Monitoring in place. Clear escalation paths. |
| **Data & reporting** | No consistent reporting. Decisions made on feel or periodic spot checks. Multiple spreadsheets, no single source of truth. | Regular reporting from one or two systems. Some manual exports/reconciliation. Leadership reads reports. | Real-time or near-real-time reporting. Single source of truth per domain. Staff trained to act on data. |
| **Integration & sync** | Systems don't talk to each other. Manual data transfer (CSV uploads, copy-paste). High error rate. | 1–2 integrations in place, mostly stable. Some automated syncs but manual reconciliation still needed. | Systems integrated and synchronized. Automated reconciliation. Issues surface via alerts, not customer complaints. |
| **Staff & process** | No standard operating procedures. Heavy reliance on 1–2 key people who know "how things work." | Written procedures for core workflows. Training exists. Some reliance on key people but distributed knowledge. | Role-based SOPs. Onboarding materials. Cross-trained staff. Procedures updated as systems change. |
| **Change management** | "We'll figure it out." No formal process for rolling out system changes. Changes pushed live without testing. | Changes communicated in advance. Someone coordinates rollouts. Issues addressed post-launch. | Formal change management process. UAT before go-live. Rollback plan documented. Impact communicated to staff. |

---

## 2. Architecture Mapping by Maturity

### Emerging → Conservative, SI-heavy

- **Shopify config:** Shopify native everything — no custom apps, no complex integrations at launch. Native POS, native online store, minimal third-party apps.
- **Integrations:** Start with native Shopify connectors (Klaviyo, accounting connector). No custom middleware at launch.
- **AnyDB:** If needed, simple schema with basic automations. Kaizen manages post-launch for the first retainer period.
- **Timeline:** Add 2–4 weeks buffer — staff decisions take longer, approvals stall.
- **SI dependency:** Heavy. Kaizen handles most operational decisions for first 60–90 days. Retainer **Tier 2** is appropriate.
- **Training:** 4–6 weeks. Hands-on walkthroughs. Quick reference guides for every workflow.
- **Risk posture:** Phased migration if over 5 locations. Staggered location rollout. Extended parallel-run.
- **Coaching note:** Set expectations in kickoff that this merchant will lean on Kaizen heavily. Scope protection and change-order discipline are critical.

### Established → Balanced, shared ownership

- **Shopify config:** Shopify native core + 1–2 integrations (ERP or CRM). Custom apps only if there's a clear, scoped gap.
- **Integrations:** iPaaS or native connector (Celigo, Patchworks) for ERP. Webhook-driven for order and inventory sync.
- **AnyDB:** Standard build covers their operational workflows. Staff can manage day-to-day.
- **Timeline:** Standard tier timelines apply.
- **SI dependency:** Balanced. Kaizen leads implementation; merchant team takes ownership 30 days post-launch. Retainer **Tier 1** or **Tier 2** depending on integration complexity.
- **Training:** 2–3 weeks. Focus on platform patterns (Flow, POS Admin, API-backed operating model, and Matrixify only if that lane remains in use).
- **Risk posture:** Standard parallel-run. Single or phased cutover depending on location count.

### Advanced → Light-touch, merchant-led

- **Shopify config:** Full capability set available. Custom apps, Shopify Functions, complex integrations if needed.
- **Integrations:** ERP + WMS + CRM via webhooks and iPaaS. Potentially real-time inventory sync.
- **AnyDB:** Advanced schema, complex automations. Merchant team takes full ownership post-build.
- **Timeline:** Tightest timeline. Merchant can move fast.
- **SI dependency:** Light. Kaizen delivers, merchant owns. Retainer **Tier 1** for monitoring and iterative improvements.
- **Training:** 1–2 weeks. Focus on Shopify-specific constraints (rate limits, Functions limitations, checkout hosting model).
- **Risk posture:** Compressed parallel-run acceptable. Big-bang cutover viable with proper plan.

---

## 3. Maturity-Specific Risks

Cross-reference with `kaizen-risk-matrix.md` — these risks shift severity based on merchant maturity.

| Risk | Emerging | Established | Advanced |
|------|----------|-------------|----------|
| Staff not trained on Shopify | CRITICAL — may stall go-live | Moderate — targeted training | Low — quick adaptation |
| No change management process | High — uncoordinated changes break things | Moderate — manageable with Kaizen guidance | Low — merchant handles it |
| Integration breaks in production | High — no one knows where to look | Moderate — some monitoring in place | Low — alerts fire, team acts |
| Post-launch ownership gap | High — merchant depends on Kaizen indefinitely | Moderate — transition plan needed | Low — natural handoff |
| Data quality in legacy system | High — no one has audited it in years | Moderate — some cleanup needed | Low — data is managed |

---

## 4. How to Surface This in a Blueprint

In `kaizen-diagnose`, include a one-page **Operational Readiness Assessment** section with:

1. Score per dimension (table above, 1–3 scale)
2. Overall maturity classification
3. Specific flagged gaps with concrete examples from discovery
4. Architecture implications (what Kaizen recommends **because** of this maturity level)
5. SI dependency and retainer recommendation (framed as client benefit, not upsell)

Frame it as: "This is what we found, this is what it means for the implementation, and this is how we've scoped the engagement to account for it."

**Never frame maturity as a negative judgment.** An Emerging merchant is not a bad client — they're a merchant who needs more Kaizen, which is a revenue and relationship opportunity.
