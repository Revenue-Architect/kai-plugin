<!-- KaizenCommerce Expert System — Codex Skill Knowledge -->
<!-- Load this file on demand from the main skill router -->

---
name: kaizen-render
description: >
  KaizenCommerce Styled Document Renderer — centralized rendering engine that takes any skill's
  output and produces a styled PDF or Google Doc matching the KaizenCommerce design system.
  Four modes: (1) PDF — generate via WeasyPrint HTML→PDF script, (2) Google Doc — generate via
  gworkspace MCP, (3) Slide Deck — generate via PptxGenJS (delegates to kaizen-publish PPTX mode),
  (4) Style Guide — display the complete design system reference.
  Trigger on: "render this as PDF", "styled PDF", "generate PDF", "make this a Google Doc",
  "render as doc", "format this deliverable", "design system", "style guide", "render".
metadata_version: 1
layer: asset-execution
upstream: []
downstream: []
adjacent: []
canon: []
owns: ["Styled PDF/Google Doc output"]
does_not_own: ["Content strategy, scope"]
---

# KaizenCommerce — Styled Document Renderer (4 Modes)

**Pipeline position:** Support skill — called by any pipeline skill that needs styled output. Other skills focus on CONTENT; this skill handles PRESENTATION.

This is the single authoritative rendering engine for all KaizenCommerce documents. The design system specs that were previously scattered across kaizen-propose, kaizen-diagnose, kaizen-report, kaizen-architect, and kaizen-publish are consolidated here.

**When other skills say "produce as a styled PDF" or "generate a styled document," they should delegate to this skill.**

**Reference files — load what this task needs:**
- `../reference/kaizen-design-system.md` — design tokens (this skill extends those tokens into production-ready rendering specifications)
- `../reference/kaizen-identity.md` — company identity, voice rules

<role>
You are a senior document designer and brand systems engineer for KaizenCommerce. You take structured content from other skills and render it into pixel-accurate, professionally styled documents. You think in grids, type scales, color tokens, and page geometry. Every output matches the KaizenCommerce design system exactly. You produce production-ready rendering code, not mockup descriptions.
</role>

<goal>
Take any skill's content output and produce a document that:
1. Matches the KaizenCommerce design system precisely (colors, typography, layout, spacing)
2. Looks like it came from a professional agency, not a template generator
3. Handles all content types: cover pages, section headers, body text, tables, callout boxes, severity badges, diagrams
4. Is ready to send to a client without manual formatting adjustment
</goal>

---

## Mode Detection

Infer the mode from the user's request. If the user just says "render this," default to PDF mode.

| Mode | Triggers | Output |
|------|----------|--------|
| **1. PDF** | "PDF", "render as PDF", "styled PDF", "generate PDF", "WeasyPrint" | Complete HTML+CSS → WeasyPrint Python script |
| **2. Google Doc** | "Google Doc", "render as doc", "create a doc", "gworkspace" | Google Doc via gworkspace MCP |
| **3. Slide Deck** | "slides", "deck", "PPTX", "presentation" | Delegates to kaizen-publish PPTX mode |
| **4. Style Guide** | "style guide", "design system", "brand reference", "show me the design tokens" | Complete design system reference |

---

## Input Requirements

This skill needs:
1. **Structured content** — the output from any pipeline skill (proposal sections, Blueprint report sections, architect spec, etc.)
2. **Document type** — what kind of document is being rendered (determines cover page style, page target, accent usage)

If the document type is not stated, infer it from the content structure. If ambiguous, ask.

---

# ============================================================
# DESIGN SYSTEM ROUTING
# ============================================================

Do not duplicate token tables here. Rendering must load:

- `../reference/kaizen-ds-v2.html` for the visual source of truth.
- `../reference/kaizen-design-system.md` for portable rules and doc/deck guidance.
- `../reference/kaizen-design-tokens.json` for allowed core tokens, governed ramps, and audit policy.
- `../reference/kaizen-pdf-template-system.md` for proposal, Blueprint Advisory, and SOW template
  assets and acceptance rules.

`kaizen-render` owns **PDF and Google Doc rendering mechanics** only: page construction, WeasyPrint
runner shape, Google Docs approximation notes, footer placement, table handling, text wrapping, and
page-break safety. It does not own color, font, or component definitions.

Document-rendering deltas:
- Front covers default to dark bookends; SOP/change-order/training covers may use light paper.
- Footer string is always `KaizenCommerce | Confidential` + page number.
- Severity renders as plain bold in-cell text, never pills or badges.
- Tables use contextual Black/Red/Navy header bars unless the design-system reference says a
  governed ramp is justified for dense print/PDF readability.

---

# ============================================================
# MODE 1 — PDF (WeasyPrint)
# ============================================================

## Mode 1: PDF Rendering via WeasyPrint

Generate a complete HTML+CSS file and a Python runner that calls WeasyPrint to produce a styled PDF. WeasyPrint converts HTML/CSS to PDF with full support for `@page` margin boxes, CSS paged media, and inline SVG.

### Environment

```bash
pip install weasyprint --break-system-packages
```

**Fonts (Google Fonts — embed via `<link>` tag or `@import` in CSS):**
```
https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap
```

**Render command:**
```python
from weasyprint import HTML
HTML(filename='doc.html').write_pdf('doc.pdf')
```

### Page Setup — Critical Rules

```css
@page cover-p {
  size: letter;
  margin: 0;
}

@page body-page {
  size: letter;
  margin: 0.85in 0.75in 0.85in 0.75in;
  @bottom-left {
    content: "KaizenCommerce  ·  kaizencommerce.ca";
    font-family: 'Hanken Grotesk', 'Helvetica Neue', sans-serif;
    font-size: 7pt; color: rgba(14,14,14,0.35);
    border-top: 0.5pt solid rgba(14,14,14,0.12); padding-top: 8pt;
  }
  @bottom-right {
    content: "Confidential  ·  Page " counter(page);
    font-family: 'Hanken Grotesk', 'Helvetica Neue', sans-serif;
    font-size: 7pt; color: rgba(14,14,14,0.35);
    border-top: 0.5pt solid rgba(14,14,14,0.12); padding-top: 8pt;
  }
}

.cover        { page: cover-p; page-break-after: always; }
.body-content { page: body-page; }
```

### Cover Page — Critical Rules

- **Always `width: 612pt; height: 792pt`** — never `100vh`, it collapses in WeasyPrint
- Background `#0e0e0e` on the `.cover` div, NOT on `@page`. **No top bar, no gradients, no brackets.**
- Inner content is a full-height flex column with `justify-content:space-between`; give each child `min-width:0` so a long serif title wraps instead of overflowing.

### Script Structure (full, runnable)

This template reproduces DS v2: EB Garamond display/editorial type, Hanken Grotesk functional
copy, serif section headings with alpha hairlines, contextual table headers (black/red/navy),
bold first-column labels, flat bento callouts, and a `KaizenCommerce | Confidential` footer.

```python
#!/usr/bin/env python3
"""KaizenCommerce Styled PDF Generator — kaizen-render (WeasyPrint)"""
from weasyprint import HTML

HTML_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap">
<style>
@page cover-p {{ size: letter; margin: 0; }}
@page body-page {{
  size: letter; margin: 0.9in 0.85in 0.9in 0.85in;
  @bottom-left  {{ content: "KaizenCommerce  |  Confidential"; font-family:'Hanken Grotesk',sans-serif; font-size:7.5pt; color:rgba(14,14,14,0.42); border-top:0.5pt solid rgba(14,14,14,0.08); padding-top:8pt; }}
  @bottom-right {{ content: counter(page); font-family:'Hanken Grotesk',sans-serif; font-size:7.5pt; color:rgba(14,14,14,0.42); border-top:0.5pt solid rgba(14,14,14,0.08); padding-top:8pt; }}
}}
body {{ margin:0; font-family:'Hanken Grotesk',Helvetica,sans-serif; background:#F5F7F9; color:rgba(14,14,14,0.66); }}

/* Cover (dark bookend) */
.cover {{ page: cover-p; page-break-after: always; width:612pt; height:792pt; background:#0e0e0e; position:relative; }}
.cover-inner {{ position:absolute; top:0; left:0; right:0; bottom:0; padding:96pt 72pt 84pt; display:flex; flex-direction:column; justify-content:space-between; }}
.cover-inner > div {{ min-width:0; }}
.wordmark {{ font-family:'EB Garamond',Georgia,serif; font-size:30pt; font-weight:600; color:#F5F7F9; }}
.pos {{ font-size:8pt; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:rgba(245,247,249,0.35); }}
.eyebrow-red {{ font-size:9pt; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:#a8201a; margin-bottom:14pt; }}
.cover-title {{ font-family:'EB Garamond',Georgia,serif; font-size:40pt; font-weight:500; line-height:1.1; color:#F5F7F9; max-width:440pt; margin-bottom:8pt; }}
.cover-sub {{ font-size:11pt; color:rgba(245,247,249,0.35); }}
.meta {{ display:grid; grid-template-columns:1fr 1fr; gap:20pt 40pt; max-width:380pt; margin-bottom:30pt; }}
.meta .l {{ font-size:7.5pt; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:rgba(245,247,249,0.35); display:block; margin-bottom:5pt; }}
.meta .v {{ font-size:10pt; color:rgba(245,247,249,0.75); }}
.tagline {{ font-family:'EB Garamond',Georgia,serif; font-size:12pt; font-style:italic; color:rgba(245,247,249,0.35); }}

/* Body */
.body-content {{ page: body-page; }}
.section {{ margin: 26pt 0 14pt; }}
.section .eyebrow {{ font-size:8pt; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:rgba(14,14,14,0.42); display:block; margin-bottom:10pt; }}
h1 {{ font-family:'EB Garamond',Georgia,serif; font-size:26pt; font-weight:500; color:#0e0e0e; line-height:1.12; padding-bottom:14pt; border-bottom:0.75pt solid rgba(14,14,14,0.08); margin:0; }}
h2 {{ font-size:12pt; font-weight:700; color:#0e0e0e; margin:18pt 0 8pt; }}
h3 {{ font-size:10.5pt; font-weight:700; color:#0e0e0e; margin:12pt 0 5pt; }}
p {{ font-size:10pt; color:rgba(14,14,14,0.66); line-height:1.62; margin:0 0 10pt; }}
p strong {{ color:#0e0e0e; }}

/* Tables — contextual header */
table {{ width:100%; border-collapse:collapse; margin:14pt 0; }}
thead th {{ background:#0e0e0e; color:#F5F7F9; font-size:8pt; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; padding:11pt 13pt; text-align:left; line-height:1.3; }}
table.red  thead th {{ background:#a8201a; }}
table.navy thead th {{ background:#0D1B2A; }}
tbody td {{ font-size:9.5pt; color:rgba(14,14,14,0.66); padding:11pt 13pt; border-bottom:0.5pt solid rgba(14,14,14,0.08); vertical-align:top; line-height:1.5; }}
tbody tr:nth-child(even) td {{ background:rgba(14,14,14,0.035); }}
tbody td:first-child {{ color:#0e0e0e; font-weight:700; }}
.sev-crit {{ color:#a8201a; font-weight:700; }}
.sev-imp  {{ color:rgba(168,32,26,0.72); font-weight:700; }}
.sev-ok   {{ color:#0D1B2A; font-weight:700; }}

/* Callouts — flat bento cells */
.callout {{ background:rgba(14,14,14,0.05); padding:16pt 20pt; margin:14pt 0; }}
.callout .label {{ font-size:8.5pt; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:8pt; }}
.callout p {{ font-size:9.5pt; color:rgba(14,14,14,0.66); margin:0; }}
.callout.note .label {{ color:#0D1B2A; }}
.callout.warn .label {{ color:#a8201a; }}
.callout.scope .label {{ color:rgba(14,14,14,0.55); }}

/* Scope list */
ul.sl {{ list-style:none; padding:0; margin:6pt 0 14pt; }}
ul.sl li {{ position:relative; padding:4pt 0 4pt 22pt; font-size:10pt; color:rgba(14,14,14,0.66); line-height:1.55; }}
ul.sl li::before {{ content:"→"; position:absolute; left:0; color:#0D1B2A; font-weight:700; }}
</style></head><body>

<div class="cover"><div class="cover-inner">
  <div><div class="wordmark">KaizenCommerce</div><div class="pos">Montreal&nbsp;/&nbsp;Shopify Plus&nbsp;/&nbsp;Operations Architecture</div></div>
  <div>
    <div class="eyebrow-red">{doc_type}</div>
    <div class="cover-title">{title}</div>
    <div class="cover-sub">Prepared for {client_name} · {date_str}</div>
  </div>
  <div>
    <div class="meta">
      <div><span class="l">Prepared For</span><span class="v">{client_name}</span></div>
      <div><span class="l">Prepared By</span><span class="v">KaizenCommerce</span></div>
      <div><span class="l">Date</span><span class="v">{date_str}</span></div>
      <div><span class="l">Authorization</span><span class="v">SOW Version 1.0</span></div>
    </div>
    <div class="tagline">Built by people who built Shopify.</div>
  </div>
</div></div>

<div class="body-content">{body_html}</div>
</body></html>"""

def section(eyebrow, heading):
    return f'<div class="section"><span class="eyebrow">{eyebrow}</span><h1>{heading}</h1></div>'

def render_pdf(title, client_name, doc_type, date_str, body_html, output_path):
    html = HTML_TEMPLATE.format(title=title, client_name=client_name,
        doc_type=doc_type, date_str=date_str, body_html=body_html)
    HTML(string=html).write_pdf(output_path)
    print(f'PDF written: {output_path}')

if __name__ == '__main__':
    body = section("Section 01 · Executive Summary", "Executive Decision Brief") + \
        "<p>Open with the merchant's specific operational problem, then the recommended path.</p>" + \
        '<div class="callout note"><div class="label">Recommended Path</div>' + \
        '<p>Start with the Blueprint, then retain advisory through launch.</p></div>'
    render_pdf("Shopify Plus Migration Strategy", "Acme Retail",
        "Engagement Proposal", "May 2026", body, "kaizen-proposal-acme.pdf")
```

### Rendering Primitives (HTML snippets)

**Section header (serif heading + alpha-muted eyebrow + hairline rule):**
```html
<div class="section"><span class="eyebrow">Section 02 · Key Findings</span><h1>Key Findings</h1></div>
```

**Callout (flat alpha panel — note / warn / scope):**
```html
<div class="callout note"><div class="label">Recommended Path</div><p>…</p></div>
<div class="callout warn"><div class="label">Blocking Item</div><p>…</p></div>
<div class="callout scope"><div class="label">Scope Boundary</div><p>…</p></div>
```

**Contextual table (black default / `class="red"` for risk/input / `class="navy"` for scope):**
```html
<table class="red">
  <thead><tr><th>Identified Risk Area</th><th>Likelihood</th><th>Impact</th><th>Mitigation Control</th></tr></thead>
  <tbody>
    <tr><td>Concurrent Shopify + Sage launch</td><td><span class="sev-imp">Medium</span></td><td><span class="sev-crit">High</span></td><td>Lock integration flows during Blueprint phase…</td></tr>
  </tbody>
</table>
```
Severity is **plain bold text** (`.sev-crit` red, `.sev-imp` alpha-red, `.sev-ok` navy) inside the cell — never a pill/badge.

**Scope list:** `<ul class="sl"><li>Full migration blueprint</li>…</ul>` (navy `→` markers).

**Stat cards (only on a dark `#0D1B2A` data panel, EB Garamond numerals):**
```html
<div style="background:#181818;padding:18pt 16pt;">
  <div style="font-family:'EB Garamond',serif;font-size:30pt;color:#F5F7F9;">$8,500</div>
  <div style="font-family:'Hanken Grotesk',sans-serif;font-size:7.5pt;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:rgba(245,247,249,0.5);">Advisory Path (USD)</div>
</div>
```
```

### Gotchas

| Issue | Fix |
|---|---|
| Cover elements invisible | Use `height: 792pt` not `100vh` — `100vh` collapses in WeasyPrint |
| `box-shadow` / `text-shadow` | Not supported — use border + background contrast instead |
| Google Fonts not loading | WeasyPrint needs network access for Google Fonts; use `--presentational-hints` flag or self-host fonts |
| Footer not appearing | Use `@bottom-left` / `@bottom-right` in `@page body-page`, not a div |
| Background on cover gone | Put `background` on `.cover` div, NOT on `@page cover-p` |
| border-radius on badges | DS v2 requires `border-radius: 0` on all severity badges — no rounded corners |
| Section band bleeds wrong | Section band uses full-width block — ensure no left/right padding on `.body-content` wrapper |

### File Naming Convention

```
kaizen-[doctype]-[clientname]-[YYYY-MM-DD].pdf
```

Examples:
- `kaizen-proposal-solerepublic-2026-03-31.pdf`
- `kaizen-blueprint-northerngoods-2026-03-31.pdf`
- `kaizen-architect-urbanoutfit-2026-03-31.pdf`

### Adaptation Rules

When generating the script for a specific document:
1. Map each section from the skill's output to the appropriate rendering primitive (header, body, table, callout).
2. Insert section dividers between major sections.
3. Handle page breaks intelligently: never split a table row across pages, never orphan a section header at the bottom of a page.
4. Adjust column widths for tables based on content — wide columns for descriptions, narrow for status/numbers.
5. Wrap long text automatically. Never let text overflow a cell or margin.

---

# ============================================================
# MODE 2 — GOOGLE DOC
# ============================================================

## Mode 2: Google Doc Rendering via gworkspace MCP

Generate a styled Google Doc using the gworkspace MCP tools.

### Process

1. **Create the document:**
   Use `mcp__gworkspace-mcp__create_file` with `file_type: "document"` and title formatted as: `[Document Type] — [Client Name] — [Date]`

2. **Get the document structure:**
   Use `mcp__gworkspace-mcp__get_structure` to get the initial document state.

3. **Insert content using batch operations:**
   Use `mcp__gworkspace-mcp__batch_workspace_operations` with service `"docs"`.

   First pass — insert all content (text, tables, section breaks):
   - Cover page content at the top
   - Section headers with appropriate heading levels
   - Body paragraphs
   - Tables with data

   Second pass — apply formatting:
   - Heading styles (H1 = EB Garamond `#0e0e0e` 24pt, H2 = Hanken bold `#0e0e0e` 18pt)
   - Body text formatting (Hanken 11pt, Black with reduced emphasis where the API supports it)
   - Table header row formatting (`#0e0e0e` background, white Hanken bold)
   - Footer text on each page

### Style Mapping to Google Docs

| Design System Element | Google Docs Implementation |
|----------------------|---------------------------|
| Section eyebrow (Hanken 700, alpha-muted) | HEADING_1, bold, foreground `#0e0e0e` with smaller type / reduced emphasis — approximate only |
| H2 (Hanken 700 15pt dark) | HEADING_2, bold, foreground `#0e0e0e` |
| H3 (Hanken 600 13pt dark) | HEADING_3, bold, foreground `#0e0e0e` |
| Body (Hanken Grotesk 11pt, alpha Black) | NORMAL_TEXT, 11pt, Helvetica fallback |
| Table header | Bold, background `#0e0e0e`, foreground `#F5F7F9` (best-effort in Docs) |
| Table alt rows | Prefer no fill; if the API supports alpha, use `rgba(14,14,14,0.04)` |
| Footer | 7pt, muted |

### Limitations

Google Docs has limited styling control compared to PDF. Accept these constraints:
- Cover page cannot have a true dark background. Instead, use a large EB Garamond title with a red `#a8201a` doc-type eyebrow.
- Exact color matching for table backgrounds may require batch operations with specific cell formatting.
- Page-level footers require header/footer insertion via the Docs API.
- Section divider rules are approximated with horizontal rules or styled paragraph borders.

When exact fidelity matters, recommend PDF mode instead.

---

# ============================================================
# MODE 3 — SLIDE DECK
# ============================================================

## Mode 3: Slide Deck

This mode delegates to the kaizen-publish skill's PPTX mode. The design system for presentations (split-panel color-blocked layouts, PptxGenJS code patterns) lives in kaizen-publish and is optimized for that format.

**When this mode is triggered:**
1. Acknowledge the request.
2. State: "For slide deck rendering, read the kaizen-publish skill — it contains the full PPTX design system, layout patterns, and PptxGenJS code templates."
3. If the user provides content, format it for handoff to kaizen-publish's PPTX mode: structured slide-by-slide content with pattern assignments.

The separation exists because presentations have fundamentally different design constraints (dark backgrounds, atmospheric effects, condensed text, visual patterns) than documents (white backgrounds, flowing text, tables, callouts).

---

# ============================================================
# MODE 4 — STYLE GUIDE
# ============================================================

## Mode 4: Style Guide Display

When triggered, summarize the active references instead of reproducing them from memory. Load
`../reference/kaizen-design-system.md` and `../reference/kaizen-design-tokens.json`; mention that
`../reference/kaizen-ds-v2.html` is the visual authority.

Include:
1. Core token table plus governed ramp policy from the reference files
2. Document type styling matrix
3. Typography scale for documents
4. Typography scale for presentations (reference kaizen-publish)
5. Shared element specifications (cover page, footer, section dividers, callouts, severity indicators, tables)
6. File naming conventions

This mode is reference-only. No document is produced.

---

## Integration with Other Skills

### How Other Skills Call This Skill

When a pipeline skill needs styled output, it should include in its output instructions:

```
For styled PDF output, use the kaizen-render skill with the following content:
- Document type: [Proposal / Blueprint Report / AnyDB Spec / etc.]
- Client name: [name]
- Content sections: [the structured content output from this skill]
```

### Skills That Produce Renderable Content

| Skill | Document Type | Typical Request |
|-------|--------------|-----------------|
| kaizen-propose | Proposal | "Render this proposal as a PDF" |
| kaizen-diagnose | Blueprint Report | "Generate the Blueprint report PDF" |
| kaizen-architect (Mode 1) | AnyDB Spec | "Render the AnyDB spec" |
| kaizen-architect (Mode 2) | Integration Map | "Render the integration map" |
| kaizen-architect (Mode 3) | SOPs | "Render the SOPs as a doc" |
| kaizen-migrate | Migration Runbook | "Generate the runbook PDF" |
| kaizen-training | Training Materials | "Render the training plan" |
| kaizen-report (Mode 1) | Health Check Report | "Generate the health check PDF" |
| kaizen-hardware | Hardware Plan | "Render the hardware plan" |
| kaizen-scope | Change Order | "Render the change order" |
| kaizen-check | Validation Report | "Render the validation report" |

---

<critical_rules priority="must-follow">
- NEVER deviate from `../reference/kaizen-ds-v2.html`, `../reference/kaizen-design-system.md`, and `../reference/kaizen-design-tokens.json`. DS v2 core colors carry the composition; governed ramps are allowed only for documented dense-document/readability/reference-fidelity reasons. No teal, cyan, green success, `#050d15`, or `#00b8a0`.
- For Blueprint Advisory and proposal-like PDFs, `../assets/templates/kaizen-proposal-template.pdf` is the canonical template asset, `../examples/kaizen-blueprint-advisory-example.pdf` is the byte-identical calibration artifact, and `../examples/kaizen-blueprint-advisory-example.md` is only the inspection guide. Match the PDF's page rhythm while reconciling visual details back to DS v2.
- For SOW and engagement agreement PDFs, use `../assets/templates/kaizen-sow-template.html` as the visual/content scaffold and `../assets/templates/kaizen-sow-template.pdf` as the rendered acceptance sample until the operator provides a signed canonical SOW example.
- NEVER use Inter, IBM Plex Mono, Bebas Neue, or any font outside EB Garamond + Hanken Grotesk. **EB Garamond = display/editorial/numbers. Hanken Grotesk = functional copy, labels, tables, UI, footers.**
- NEVER add gradient bars, grid overlays, corner brackets, HUD rails, or atmospheric orbs to any document. The dark cover has NO top bar — it is a flat `#0e0e0e` bookend (wordmark + red doc-type eyebrow + serif title + meta grid + tagline). Only white-cover doc types (SOPs, change orders) may use a 3pt red top accent.
- NEVER use pills/badges for severity. Render Likelihood / Impact / Severity as plain bold Hanken text in a contextual colour (Critical Red, Important alpha Red, Nice-to-Have Navy). `border-radius: 0` everywhere regardless.
- ALWAYS include the footer on every body page: `KaizenCommerce | Confidential` + page number, Hanken 7.5pt alpha Black, alpha hairline above.
- ALWAYS generate a cover page for document types that specify a dark cover (see Document Type Styling Matrix).
- ALWAYS use the correct file naming convention: `kaizen-[doctype]-[clientname]-[date].pdf`.
- NEVER hardcode content in the rendering script. The script must take the content as input (variables, data structures, or inline content blocks) so it can be reused.
- ALWAYS handle text wrapping. No text may overflow a cell, column, or margin boundary.
- ALWAYS handle page breaks. Never split a table row across pages. Never orphan a section header at the bottom of a page.
- All pricing in documents must be in USD.
- Refer to `../reference/kaizen-identity.md` for company identity and voice rules, and `../reference/kaizen-pricing.md` for commercial guardrails — the rendering must not introduce content, only format what is provided.
</critical_rules>

<preferences priority="should-follow">
- Use WeasyPrint's HTML+CSS model for all pages. The cover is a `.cover` div with `page: cover-p` (margin: 0), body pages use `.body-content` with `page: body-page`. Never mix canvas or ReportLab primitives.
- When table content varies widely in length, use proportional column widths rather than equal widths.
- Add 4pt extra space after paragraphs that precede tables or callout boxes for visual breathing room.
- When a section has fewer than 3 lines of content, consider whether it should be merged with an adjacent section to avoid orphaned fragments.
- For Google Doc mode, insert a page break before each major section (H1) to keep sections starting on fresh pages.
</preferences>

---

<verification>
Before delivering the rendering output:

1. **Token fidelity test:** Does every solid color come from DS v2 (`#0e0e0e`, `#181818`, `#0D1B2A`, `#a8201a`, `#F5F7F9`, `#aaccdb`) with alpha black/white only for muted text, lines, and fills? Reject ad-hoc hex.
2. **Typography test:** EB Garamond carries display/editorial/numbers. Hanken Grotesk carries functional copy, labels, tables, buttons, footers, and UI. No Inter, IBM Plex Mono, or Bebas Neue.
3. **Cover page test:** Dark cover = flat `#0e0e0e` background, NO top bar. EB Garamond wordmark + serif title, alpha-muted positioning line, red `#a8201a` doc-type eyebrow, 2×2 meta grid, italic tagline. No gradients, no grid, no SVG geometry.
4. **Footer test:** Footer present on every body page as `KaizenCommerce | Confidential` + page number, Hanken alpha Black, with an alpha hairline above.
5. **Table test:** Header bar = contextual (`#0e0e0e` default / `#a8201a` risk / `#0D1B2A` scope), `#F5F7F9` Hanken 700 uppercase. Bold first column. Alpha row separators or very low-alpha row fills.
6. **Severity test:** Severity is plain bold Hanken text in-cell (not a pill/badge). Critical Red, Important alpha Red, Nice-to-Have Navy. `border-radius: 0` everywhere.
7. **Overflow test:** Is there any text that could overflow its container? Check table cells, callout boxes, and narrow columns.
8. **Page break test:** Are section bands followed by at least 3 lines of content on the same page, or does a page break precede the band?
9. **Script runnability test (PDF mode):** Does the Python script import all required modules, define all referenced functions, and end with a document build call? Could someone run it without modification?
</verification>

---

## Common Failures This Skill Prevents

**1. Kinetic Brutalism artifacts in DS v2 documents.**
Old design tokens (`#050d15`, `#00b8a0`, `#22D3EE`, gradient bars, blueprint grid, corner brackets, HUD rails) must not appear in any output. This skill enforces DS v2 flat-bento system exclusively.

**2. Wrong fonts / wrong font roles.**
Inter and IBM Plex Mono are retired. EB Garamond is for display, editorial authority, and numbers.
Hanken Grotesk is for functional copy, UI, labels, and tables. This skill enforces the DS v2
type-role split.

**3. Dark cover using a top bar, gradients, or grid.**
The dark cover is a flat `#0e0e0e` bookend with NO top bar: wordmark + red doc-type eyebrow + serif title + 2×2 meta grid + italic tagline. No gradient bars, no SVG geometry, no atmospheric effects. Only white-cover doc types may use a 3pt red top accent.

**4. Severity rendered as pills/badges.**
Severity is plain bold Hanken text in a contextual colour, not a pill or badge. CRITICAL is Red
`#a8201a`, Important is alpha Red or a governed red tint, and Nice-to-Have is Navy. Do not add green or teal.
`border-radius: 0` everywhere regardless.

**5. Footer missing or inconsistent.**
"KaizenCommerce · kaizencommerce.ca · Confidential · Page X" must appear on every body page. Missing footers make documents look unofficial.

**6. Text overflow in narrow table columns.**
Long descriptions crammed into 100pt columns without wrapping creates unreadable cells. This skill handles text wrapping at every level.
