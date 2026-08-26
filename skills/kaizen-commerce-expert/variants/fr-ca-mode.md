# FR-CA Mode Variant

Use this variant when output should be in Québec French: the merchant or contact is francophone
(French website, French correspondence, francophone Québec market), or the operator asks for output
"en français" / "in French".

## Scope — approved French artifact types only

1. Outreach messages (all five outreach modes)
2. Call summaries (qualify POST-CALL)
3. Executive summaries (diagnose §2, as a standalone French companion)
4. Proposal cover notes (a 1-page French cover over an English proposal)

Everything else — full proposals, SOWs, Blueprint reports, legal or payment terms — stays
English until `reference/kaizen-fr-ca-glossary.md` completes its review pass and the bilingual
QA process has run clean three times. Offer a French cover note instead, never a partial
translation of a binding document.

## Required Context

- Merchant language signal (site, correspondence, contact preference)
- The artifact type requested and its English-mode skill route
- `reference/kaizen-fr-ca-glossary.md` loaded — terminology, register, format, QA checklist

## Default Skill Chain

1. Route the artifact through its normal skill first (`skills/kaizen-outreach.md`,
   `skills/kaizen-qualify.md`, `skills/kaizen-diagnose.md`, `skills/kaizen-propose.md`)
2. Apply this variant + glossary for the French rendering
3. Run the bilingual QA checklist (glossary §QA) before delivery

## Variant Depth Additions

- Write French natively from the brief — never draft English then translate; translated structure
  reads as translated.
- Bill 96 awareness is an outreach angle for QC merchants (French-language commerce obligations),
  stated as a business reality, never as legal advice.
- All English-mode commercial guardrails carry over unchanged: pricing canon for figures,
  two-lane commercial model, no ROI promises, voice canon discipline in French.

## Anti-Selection Rules

- Do not select this variant just because the merchant is in Québec — anglophone QC merchants get
  English.
- Do not select for artifact types outside the approved four, even on explicit request — explain
  the gate and offer the cover-note alternative (the operator can override knowingly).
- Mixed-language thread: follow the merchant's latest language choice.

## Known Failure Modes

- France-French vocabulary ("devis") slipping in — glossary conformity check catches it.
- Anglicism calques from machine-translation patterns — read-aloud QA step.
- Currency/typography formatted English-style inside French prose.
- Register drift (tu/vous mixing) across a sequence of messages.
- Guardrail loosening during translation — figures or promises appearing that the English mode
  would block.

## Default Evidence Gates

- Same as English mode: proof points only per the proof bank's Provenance & Capture Schema;
  platform claims per vendor-freshness protocol; figures from pricing canon only.
- Plus: native review (the operator) per the QA checklist before any French artifact ships.

## Operating Hooks

- Memory hook: record the client's language preference in client memory on first detection.
- Flywheel: French-language objections or terminology corrections feed the glossary; competitive
  or outcome evidence feeds the proof bank as usual.

## Output Shape By Mode

- Outreach: same structure and word caps as `skills/kaizen-outreach.md`, French.
- Call summary: same POST-CALL structure as `skills/kaizen-qualify.md`, French; confidence tags
  stay ✅/💡/❓ with French labels (✅ CONFIRMÉ · 💡 INFÉRÉ · ❓ À VALIDER).
- Exec summary: 2-3 French paragraphs mirroring diagnose §2; delivered alongside the English
  report, labeled as a companion.
- Proposal cover note: one page — situation recap, recommendation in one paragraph, the
  next step, and a line noting the full proposal is in English with French discussion available.

## Source-Of-Truth

- Terminology and QA: `reference/kaizen-fr-ca-glossary.md` (single authority; corrections land
  there, not in this variant)
- Voice rules: `reference/kaizen-voice.md` (applies in both languages)
- Money: `reference/kaizen-pricing.md` — amounts rendered per glossary format rules
- Scope gate graduation: glossary review pass + three clean QA runs, recorded in the glossary

For the underlying legal/tax facts (Bill 96 obligations, QST, Interac behavior), load
`../reference/kaizen-canada-retail-compliance.md`; this variant owns language and tone, not
compliance claims.
