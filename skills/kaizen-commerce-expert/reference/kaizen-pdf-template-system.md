# KaizenCommerce PDF Template System

This reference owns the template routing for styled PDF deliverables. Load it when producing or
reviewing proposals, Blueprint Advisory PDFs, SOWs, engagement agreements, invoices, or change
orders.

## Canonical Assets

| Deliverable | Template asset | Calibration source | Audit |
|---|---|---|---|
| Proposal / Blueprint Advisory PDF | `../assets/templates/kaizen-proposal-template.pdf` | `../examples/kaizen-blueprint-advisory-example.pdf` | `scripts/audit_pdf_templates.py` verifies byte-identical parity and PDF structure. |
| SOW / Engagement Agreement | `../assets/templates/kaizen-sow-template.html` and `../assets/templates/kaizen-sow-template.pdf` | Derived from the Proposal / Blueprint Advisory visual system | `scripts/audit_pdf_templates.py` verifies required sections, DS v2 colors, brand fonts, forbidden styling absence, and WeasyPrint renderability. |

The proposal template is the exact canonical example supplied by the operator. The SOW template is derived
from that proposal system because there is no separate canonical SOW artifact yet.

## Proposal Rules

- Start from the Proposal / Blueprint Advisory visual language: dark bookend cover, EB Garamond
  title hierarchy, Hanken functional labels, alpha hairlines, branded footer, and contextual
  tables.
- Blueprint Advisory / Blueprint Report PDFs must render to 15-20 pages unless the operator explicitly
  asks for a compressed executive version. Under 15 pages is a content-depth failure, not a design
  preference.
- Use `kaizen-render` for final PDF generation. The template is a calibration asset and acceptance
  reference, not a reason to hardcode proposal content.
- Keep proposals specific to the merchant. The template controls visual rhythm; it does not replace
  Situation, Business Case, Scope, Risk Register, Economics, Timeline, and Next Step logic from
  `skills/kaizen-propose.md`.
- Run both audits before delivery when files exist locally:
  - `scripts/audit_proposal_protocol.py <proposal.md> --pdf <proposal.pdf> --internal-qa <internal-qa.md>`
  - `scripts/audit_pdf_templates.py`

## SOW Rules

- Base the SOW on `../assets/templates/kaizen-sow-template.html` unless the operator supplies a newer
  signed SOW reference.
- Preserve the same dark cover system as the proposal template.
- Use direct, non-legalese language. The SOW is formal, but it should still be readable by an
  operator.
- Every SOW must include:
  - Parties
  - Engagement overview tied to the accepted proposal
  - Services and deliverables
  - Acceptance criteria for every deliverable
  - Scope boundaries and exclusions
  - Client responsibilities
  - Timeline
  - Investment, Blueprint credit, and Net 7 terms
  - Change order process
  - Acceptance/signature block
- Scope boundaries are framed as delivery clarity, not adversarial protection.
- Do not produce a plain Markdown or default PDF SOW unless the operator explicitly asks for that format.

## Rendering Contract

All client-facing PDFs should visually pass these checks:

- Dark cover is full-bleed `#0e0e0e` with no top bar, grid overlay, glow, or decorative brackets.
- Wordmark and title use EB Garamond; labels, metadata, body, tables, and footer use Hanken
  Grotesk.
- Red is reserved for document type, risk/action emphasis, or contextual table headers.
- Tables use contextual Black, Navy, or Red header bars with flat rows and alpha separators.
- Severity/status is plain bold in-cell text, never pills or badges.
- No rounded cards, shadows, gradients, atmospheric effects, or decorative icon clutter.
- Governed ramps are allowed only for dense PDF readability, print/export reliability, or
  reference fidelity as defined in `kaizen-design-tokens.json`.
