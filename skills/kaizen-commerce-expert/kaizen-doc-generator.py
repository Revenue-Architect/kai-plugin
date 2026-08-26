#!/usr/bin/env python3
"""KaizenCommerce DS v2 — Document Preview (11 types × 3 pages)

Faithful to reference/kaizen-ds-v2.html:
  Fonts   EB Garamond = display / headings / wordmark / stats (serif authority)
          Hanken Grotesk = body, labels, tables, UI (functional sans)
  Pages   Dark bookends (cover + close) on #0e0e0e; light body on #F5F7F9
  Headers serif heading + alpha-muted eyebrow + hairline rule (no color bands)
  Tables  contextual header bar (black / red / navy), bold first column, alpha rows
  Accents Red #a8201a (problem/CTA), Navy #0D1B2A (process/trust/Gold), Ice Blue #aaccdb (text on Navy only)
"""
import subprocess

OUT_PDF = "/tmp/kaizen-ds-preview.pdf"
OUT_HTML = "/tmp/kaizen-ds-preview.html"

# ── Palette ───────────────────────────────────────────────────────────────
# Brand: Black #0e0e0e · Mid #181818 · Navy #0D1B2A · Red #a8201a · White #F5F7F9 · Ice #aaccdb
# Muted text, quiet fills, and hairlines use alpha variants of black/white, not extra fixed hexes.

CSS = """
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap');

@page { size: letter; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family:'Hanken Grotesk', Helvetica, Arial, sans-serif; font-size:10.5pt; color:rgba(14,14,14,0.66); background:#F5F7F9; }

.page { width:8.5in; height:11in; overflow:hidden; position:relative; page-break-after:always; background:#F5F7F9; }
.page:last-child { page-break-after:auto; }

/* ── Dark cover / bookend ── */
.void { background:#0e0e0e; }
.cover-inner { position:absolute; top:0; left:0; right:0; bottom:0; padding:96pt 72pt 84pt; display:flex; flex-direction:column; justify-content:space-between; }
.brand-lbl  { font-family:'EB Garamond', Georgia, serif; font-size:30pt; font-weight:600; letter-spacing:-0.01em; color:#F5F7F9; margin-bottom:8pt; }
.brand-pos  { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:8pt; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:rgba(245,247,249,0.35); }
.doc-lbl    { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:9pt; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:#a8201a; margin-bottom:14pt; }
.cover-title { font-family:'EB Garamond', Georgia, serif; font-size:40pt; font-weight:500; line-height:1.1; color:#F5F7F9; margin-bottom:8pt; max-width:440pt; }
.cover-sub  { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:11pt; font-weight:400; color:rgba(245,247,249,0.35); margin-bottom:0; }
.meta-grid  { display:grid; grid-template-columns:1fr 1fr; gap:20pt 40pt; max-width:380pt; margin-bottom:34pt; }
.meta-lbl   { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:7.5pt; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:rgba(245,247,249,0.35); display:block; margin-bottom:5pt; }
.meta-val   { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:10pt; font-weight:400; color:rgba(245,247,249,0.75); display:block; }
.cover-tag  { font-family:'EB Garamond', Georgia, serif; font-size:12pt; font-style:italic; color:rgba(245,247,249,0.35); }

/* White cover — SOPs, Change Orders, Training */
.wcover { background:#F5F7F9; }
.wcover .brand-lbl  { color:#0e0e0e; }
.wcover .brand-pos  { color:rgba(14,14,14,0.42); }
.wcover .cover-title { color:#0e0e0e; }
.wcover .cover-sub  { color:rgba(14,14,14,0.55); }
.wcover .meta-lbl   { color:rgba(14,14,14,0.42); }
.wcover .meta-val   { color:#0e0e0e; font-weight:500; }
.wcover .cover-tag  { color:rgba(14,14,14,0.42); }

/* ── Section header (light page) — serif heading + alpha-muted eyebrow + hairline ── */
.sec-band { padding:40pt 64pt 0; }
.sec-lbl  { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:8pt; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:rgba(14,14,14,0.42); display:block; margin-bottom:10pt; }
.sec-band h1 { font-family:'EB Garamond', Georgia, serif; font-size:27pt; font-weight:500; color:#0e0e0e; line-height:1.12; padding-bottom:14pt; border-bottom:0.75pt solid rgba(14,14,14,0.08); }

/* ── Body ── */
.body { padding:18pt 64pt 58pt; }
.body h2 { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:12pt; font-weight:700; color:#0e0e0e; margin-top:18pt; margin-bottom:8pt; }
.body h3 { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:10.5pt; font-weight:700; color:#0e0e0e; margin-top:12pt; margin-bottom:5pt; }
.body p  { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:10pt; color:rgba(14,14,14,0.66); line-height:1.62; margin-bottom:10pt; }
.body p strong { color:#0e0e0e; font-weight:700; }

/* Scope list */
ul.sl { list-style:none; padding:0; margin:6pt 0 14pt; }
ul.sl li { display:flex; align-items:flex-start; gap:10pt; font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:10pt; color:rgba(14,14,14,0.66); line-height:1.55; padding:4pt 0; }
ul.sl li .mk { color:#0D1B2A; font-size:10pt; font-weight:700; flex-shrink:0; line-height:1.55; }

/* ── Callouts — flat alpha panels, caps label, no border ── */
.callout { background:rgba(14,14,14,0.05); padding:16pt 20pt; margin:14pt 0; }
.cl { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:8.5pt; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; display:block; margin-bottom:8pt; }
.callout p { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:9.5pt; margin:0; line-height:1.6; color:rgba(14,14,14,0.66); }
.ci .cl { color:#0D1B2A; }   /* note / info */
.ca .cl { color:#a8201a; }   /* emphasis / warning — red */
.cs .cl { color:#0D1B2A; }   /* scope / policy — navy */

/* ── Tables — contextual header, bold first column, alpha alt rows ── */
table.dt { width:100%; border-collapse:collapse; margin:14pt 0; font-size:9.5pt; }
table.dt thead th { font-family:'Hanken Grotesk', Helvetica, sans-serif; background:#0e0e0e; padding:11pt 13pt; text-align:left; color:#F5F7F9; font-size:8pt; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; line-height:1.3; }
table.dt.dt-red thead th  { background:#a8201a; }
table.dt.dt-navy thead th { background:#0D1B2A; }
table.dt tbody td { font-family:'Hanken Grotesk', Helvetica, sans-serif; padding:11pt 13pt; color:rgba(14,14,14,0.66); border-bottom:0.5pt solid rgba(14,14,14,0.08); vertical-align:top; line-height:1.5; }
table.dt tbody tr:nth-child(even) td { background:rgba(14,14,14,0.035); }
table.dt tbody td:first-child { color:#0e0e0e; font-weight:700; }
table.dt tbody td:first-child strong { font-weight:700; }

/* Severity — plain bold caps text, no pill, no border */
.bdc { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:8.5pt; font-weight:700; letter-spacing:0.02em; }
.b-crit { color:#a8201a; }
.b-imp  { color:rgba(168,32,26,0.72); }
.b-ok   { color:#0D1B2A; }
.b-done { color:#0e0e0e; }

/* ── Page footer ── */
.pg-foot { position:absolute; bottom:0; left:0; right:0; padding:10pt 64pt 24pt; }
.foot-rule { height:0.5pt; background:rgba(14,14,14,0.08); margin-bottom:8pt; }
.foot-inner { display:flex; justify-content:space-between; align-items:center; }
.ft { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:7.5pt; color:rgba(14,14,14,0.42); letter-spacing:0.04em; }

/* ── Dark data panel (Navy) ── */
.dp { background:#0D1B2A; padding:48pt 64pt 40pt; display:flex; flex-direction:column; }
.dp-top { padding-bottom:18pt; margin-bottom:28pt; border-bottom:0.75pt solid rgba(245,247,249,0.14); }
.dp-lbl  { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:8pt; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:#aaccdb; display:block; margin-bottom:10pt; }
.dp-title { font-family:'EB Garamond', Georgia, serif; font-size:26pt; font-weight:500; color:#F5F7F9; line-height:1.12; }
.stat-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:14pt; margin-bottom:28pt; }
.stat-card { background:#181818; padding:18pt 16pt; }
.stat-val { font-family:'EB Garamond', Georgia, serif; font-size:30pt; font-weight:500; color:#F5F7F9; line-height:1; margin-bottom:7pt; }
.stat-lbl { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:7.5pt; font-weight:600; letter-spacing:0.10em; text-transform:uppercase; color:rgba(245,247,249,0.5); }

table.pt { width:100%; border-collapse:collapse; }
table.pt thead th { font-family:'Hanken Grotesk', Helvetica, sans-serif; padding:9pt 11pt; text-align:left; color:#aaccdb; font-size:7.5pt; font-weight:700; letter-spacing:0.10em; text-transform:uppercase; border-bottom:0.75pt solid rgba(245,247,249,0.14); }
table.pt tbody td { font-family:'Hanken Grotesk', Helvetica, sans-serif; padding:9pt 11pt; color:rgba(245,247,249,0.75); border-bottom:0.5pt solid rgba(245,247,249,0.07); font-size:9pt; line-height:1.45; vertical-align:top; }
table.pt tbody td.cy { color:#aaccdb; font-weight:600; }

.dp-foot { margin-top:auto; padding-top:18pt; border-top:0.75pt solid rgba(245,247,249,0.10); display:flex; justify-content:space-between; align-items:center; }
.dp-ft { font-family:'Hanken Grotesk', Helvetica, sans-serif; font-size:7.5pt; color:rgba(245,247,249,0.35); letter-spacing:0.04em; }

/* ── Numbered step rows ── */
.step { display:flex; align-items:flex-start; gap:14pt; margin-bottom:14pt; }
.step-n { font-family:'EB Garamond', Georgia, serif; font-size:24pt; font-weight:500; color:#aaccdb; line-height:1; flex-shrink:0; width:34pt; }
.step-b h3 { margin-top:3pt !important; }

/* Two-col */
.two-col { display:grid; grid-template-columns:1fr 1fr; gap:20pt; margin:12pt 0; }
"""

# ─── Helpers ────────────────────────────────────────────────────────────────

def foot(n):
    return f'<div class="pg-foot"><div class="foot-rule"></div><div class="foot-inner"><span class="ft">KaizenCommerce &nbsp;|&nbsp; Confidential</span><span class="ft">{n}</span></div></div>'

def dp_foot(doc, page):
    return f'<div class="dp-foot"><span class="dp-ft">KaizenCommerce &nbsp;|&nbsp; Confidential</span><span class="dp-ft">{page}</span></div>'

def sec(num, name, heading):
    return f'<div class="sec-band"><span class="sec-lbl">Section {num:02d} &nbsp;·&nbsp; {name}</span><h1>{heading}</h1></div>'

def ci(label, text): return f'<div class="callout ci"><span class="cl">{label}</span><p>{text}</p></div>'
def ca(label, text): return f'<div class="callout ca"><span class="cl">{label}</span><p>{text}</p></div>'
def cs(label, text): return f'<div class="callout cs"><span class="cl">{label}</span><p>{text}</p></div>'

def sl(items):
    lis = ''.join(f'<li><span class="mk">→</span>{i}</li>' for i in items)
    return f'<ul class="sl">{lis}</ul>'

def stat(val, lbl):
    return f'<div class="stat-card"><div class="stat-val">{val}</div><div class="stat-lbl">{lbl}</div></div>'

def cover_dark(file_num, sector, tier, doc_lbl, title_main, title_sub, sub, client, m2l, m2v, m3l, m3v, _unused=""):
    return f"""
<div class="page void">
  <div class="cover-inner">
    <div>
      <div class="brand-lbl">KaizenCommerce</div>
      <div class="brand-pos">Montreal&nbsp;/&nbsp;Shopify Plus&nbsp;/&nbsp;Operations Architecture</div>
    </div>
    <div class="cover-mid">
      <div class="doc-lbl">{doc_lbl}</div>
      <h1 class="cover-title">{title_main}</h1>
      <div class="cover-sub">{sub}</div>
    </div>
    <div class="cover-bot">
      <div class="meta-grid">
        <div><span class="meta-lbl">Prepared For</span><span class="meta-val">{client}</span></div>
        <div><span class="meta-lbl">Prepared By</span><span class="meta-val">KaizenCommerce</span></div>
        <div><span class="meta-lbl">{m2l}</span><span class="meta-val">{m2v}</span></div>
        <div><span class="meta-lbl">{m3l}</span><span class="meta-val">{m3v}</span></div>
      </div>
      <div class="cover-tag">Built by people who built Shopify.</div>
    </div>
  </div>
</div>"""

def cover_white(file_num, sector, doc_lbl, title, sub, client, m2l, m2v, m3l, m3v):
    return f"""
<div class="page wcover">
  <div class="cover-inner">
    <div>
      <div class="brand-lbl">KaizenCommerce</div>
      <div class="brand-pos">Montreal&nbsp;/&nbsp;Shopify Plus&nbsp;/&nbsp;Operations Architecture</div>
    </div>
    <div class="cover-mid">
      <div class="doc-lbl">{doc_lbl}</div>
      <h1 class="cover-title">{title}</h1>
      <div class="cover-sub">{sub}</div>
    </div>
    <div class="cover-bot">
      <div class="meta-grid">
        <div><span class="meta-lbl">Prepared For</span><span class="meta-val">{client}</span></div>
        <div><span class="meta-lbl">Prepared By</span><span class="meta-val">KaizenCommerce</span></div>
        <div><span class="meta-lbl">{m2l}</span><span class="meta-val">{m2v}</span></div>
        <div><span class="meta-lbl">{m3l}</span><span class="meta-val">{m3v}</span></div>
      </div>
      <div class="cover-tag">Built by people who built Shopify.</div>
    </div>
  </div>
</div>"""

# ─── Document type pages ────────────────────────────────────────────────────

def doc_proposal():
    p1 = cover_dark("KC-2026-042","RETAIL-POS","GOLD TIER","Implementation Proposal",
        "Shopify POS Migration — 8 Locations","",
        "Prepared for Northwall Supply Co.",
        "Northwall Supply Co.","Tier","Gold","Timeline","7–9 Weeks")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"SCOPE OF WORK","Scope of Work")}
  <div class="body">
    <p>This engagement covers a full Shopify POS implementation across all eight Northwall Supply Co. locations, migrating from Lightspeed Retail. The scope below is fixed at the Gold tier. Items outside this boundary require a signed change order before work begins.</p>
    <h2>Included Deliverables</h2>
    {sl(["Full Matrixify product and customer data migration (up to 150K records)",
         "Shopify POS Pro configuration at 8 locations — Smart Grid, staff roles, payment terminals",
         "AnyDB operations build: purchase order workflow, inventory transfer, daily reconciliation",
         "3 Shopify Flow automations: low-stock alert, end-of-day close trigger, reorder escalation",
         "Hardware plan and network assessment for all 8 locations",
         "Two-day staff training delivered remotely — floor staff and managers",
         "30-day post-go-live support window"])}
    <h2>Out of Scope</h2>
    {sl(["ERP or accounting system integration (QuickBooks, Sage) — change order required",
         "Custom Shopify theme development or storefront work",
         "Physical hardware procurement or on-site installation",
         "Data migration beyond 150K product/customer records"])}
    {ci("Note","Blueprint credit of [BLUEPRINT_FEE] applied against the Gold tier investment. Net investment reflects this credit.")}
    {ca("Assumption","Product catalog provided by client in Lightspeed CSV export format by Week 1 kickoff. Delay in export delivery will shift the go-live date accordingly.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page dp">
  <div class="dp-top">
    <span class="dp-lbl">05 · INVESTMENT SUMMARY</span>
    <div class="dp-title">Investment &amp; Timeline</div>
  </div>
  <div class="stat-grid">
    {stat("$9,000","Net Investment (USD)")}
    {stat("8","Locations")}
    {stat("9wk","Est. Timeline")}
  </div>
  <table class="pt">
    <thead><tr><th>Line Item</th><th>Value</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Gold Tier — POS Migration</td><td class="cy">[GOLD_POS_PRICE]</td><td>8 locations, up to 150K records</td></tr>
      <tr><td>Blueprint Credit Applied</td><td class="cy">-[BLUEPRINT_FEE]</td><td>Completed April 2026</td></tr>
      <tr><td>AnyDB Standard Build</td><td class="cy">$8,500</td><td>PO workflow + 3 automations</td></tr>
      <tr><td><strong>Net Investment</strong></td><td class="cy"><strong>$17,500</strong></td><td>All-in, excluding hardware</td></tr>
      <tr><td>Retainer (optional)</td><td class="cy">$750/mo</td><td>Tier 2 — 10 hrs/mo, quarterly review</td></tr>
    </tbody>
  </table>
  {dp_foot("Proposal",3)}
</div>"""
    return p1 + p2 + p3

def doc_blueprint():
    p1 = cover_dark("KC-2026-031","RETAIL-POS","SILVER — BLUEPRINT","Migration Blueprint + Risk Register",
        "Pre-Implementation Discovery — 4 Locations","",
        "Prepared for Westbrook Outfitters · May 2026",
        "Westbrook Outfitters","Locations","4","Completed","April 14, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"KEY FINDINGS","Key Findings")}
  <div class="body">
    <p>Four-location diagnostic completed over six days. The findings below represent the critical gaps between Westbrook's current Lightspeed R-Series setup and a production-ready Shopify POS configuration. All severity ratings reflect operational risk at go-live.</p>
    <table class="dt">
      <thead><tr><th>Finding</th><th>Area</th><th>Severity</th><th>Impact</th></tr></thead>
      <tbody>
        <tr><td>Product catalog contains 3,200 duplicate SKUs across locations</td><td>Data</td><td><span class="bdc b-crit">Critical</span></td><td>Inventory miscount at launch</td></tr>
        <tr><td>No barcode standardization — 4 separate label formats in use</td><td>Data</td><td><span class="bdc b-crit">Critical</span></td><td>POS scan failures at checkout</td></tr>
        <tr><td>End-of-day cash reconciliation done manually via spreadsheet</td><td>Operations</td><td><span class="bdc b-imp">Important</span></td><td>30–45 min/day per location lost</td></tr>
        <tr><td>Store Wi-Fi on consumer-grade routers — no VLAN separation</td><td>Hardware</td><td><span class="bdc b-imp">Important</span></td><td>POS terminal drops under load</td></tr>
        <tr><td>Staff have shared PINs — no individual accountability trail</td><td>Security</td><td><span class="bdc b-imp">Important</span></td><td>Audit and theft risk</td></tr>
        <tr><td>No customer loyalty or email capture process in place</td><td>Commerce</td><td><span class="bdc b-ok">Nice to Have</span></td><td>Missed retention opportunity</td></tr>
      </tbody>
    </table>
    {ci("Finding","Two of the four locations run Lightspeed R-Series on Windows 7 machines. These cannot run the Shopify POS app and will require hardware replacement before go-live.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(3,"RECOMMENDATIONS","Recommendations")}
  <div class="body">
    <p>The following actions are sequenced to resolve Critical findings before Silver tier work begins. Items 1–2 must be complete before Week 1 of implementation.</p>
    <div class="step"><div class="step-n">01</div><div class="step-b"><h3>Deduplicate the product catalog</h3><p>Export full Lightspeed catalog to CSV. Run deduplication script against SKU and barcode fields. Estimated 2 days with Antigravity-assisted cleaning. Client provides export by April 28.</p></div></div>
    <div class="step"><div class="step-n">02</div><div class="step-b"><h3>Standardize barcodes to GS1-128 format</h3><p>Re-label all SKUs at two locations with highest variance. Client ops team handles physical re-label. Kaizen provides the barcode export and validation checklist.</p></div></div>
    <div class="step"><div class="step-n">03</div><div class="step-b"><h3>Replace hardware at Locations 2 and 4</h3><p>Minimum spec: iPad 10th Gen + Shopify Tap to Pay or WisePad 3. Recommend Ethernet over Wi-Fi for POS terminals. Hardware plan delivered in Week 1.</p></div></div>
    <div class="step"><div class="step-n">04</div><div class="step-b"><h3>Build AnyDB end-of-day automation</h3><p>Replace the manual spreadsheet with an AnyDB reconciliation workflow triggered at 9PM nightly. Estimated 40-minute savings per location per day across 4 stores.</p></div></div>
    {cs("Scope Boundary","Recommendations 1–2 are pre-implementation prerequisites. If not complete at kickoff, go-live date shifts and a change order may be required.")}
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_anydb():
    p1 = cover_dark("KC-2026-038","OPS-BUILD","STANDARD BUILD","AnyDB Operations Spec",
        "Workflow Design &amp; Schema Specification","",
        "Prepared for Meridian Hardware · May 2026",
        "Meridian Hardware","Build Tier","Standard","Automations","5 Workflows")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"SCHEMA OVERVIEW","Database Schema")}
  <div class="body">
    <p>The AnyDB build for Meridian Hardware covers three workflow domains: purchase orders, inventory transfers, and vendor management. All tables below are primary entities. Junction tables and computed fields are documented in the full schema appendix.</p>
    <table class="dt">
      <thead><tr><th>Table</th><th>Key Fields</th><th>Linked To</th><th>Type</th></tr></thead>
      <tbody>
        <tr><td><strong>purchase_orders</strong></td><td>po_number, vendor_id, status, expected_date</td><td>vendors, line_items</td><td>Primary</td></tr>
        <tr><td><strong>po_line_items</strong></td><td>po_id, sku, qty_ordered, qty_received, unit_cost</td><td>purchase_orders, products</td><td>Junction</td></tr>
        <tr><td><strong>vendors</strong></td><td>vendor_id, name, lead_days, payment_terms, contact</td><td>purchase_orders</td><td>Primary</td></tr>
        <tr><td><strong>inventory_transfers</strong></td><td>transfer_id, from_location, to_location, status</td><td>transfer_lines, locations</td><td>Primary</td></tr>
        <tr><td><strong>locations</strong></td><td>location_id, shopify_id, name, type</td><td>transfers, inventory</td><td>Reference</td></tr>
      </tbody>
    </table>
    {ci("Integration","All purchase_order records sync to Shopify inventory on status change to 'received'. The sync uses the Shopify Admin REST API — inventory_levels/adjust endpoint. Rate limit: 2 calls/sec.")}
    {ca("Assumption","Meridian's vendor list will be provided as an Excel export. Kaizen will normalize and seed the vendors table in Week 2. Vendor IDs must be stable — do not reassign after seeding.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"AUTOMATIONS","Workflow Automations")}
  <div class="body">
    <p>Five automations are included in the Standard Build scope. Each automation is an AnyDB workflow triggered by a record event or a time-based cron. Shopify Flow handles the storefront-side triggers; AnyDB handles the back-office state.</p>
    <table class="dt">
      <thead><tr><th>Automation</th><th>Trigger</th><th>Action</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td><strong>PO Auto-Create</strong></td><td>Inventory level &lt; reorder_point</td><td>Draft PO created in AnyDB, email to buyer</td><td><span class="bdc b-ok">Scoped</span></td></tr>
        <tr><td><strong>Receiving Confirmation</strong></td><td>PO status → received</td><td>Shopify inventory adjusted, PO closed</td><td><span class="bdc b-ok">Scoped</span></td></tr>
        <tr><td><strong>Transfer Request</strong></td><td>Manual trigger in AnyDB portal</td><td>Transfer record created, both locations notified</td><td><span class="bdc b-ok">Scoped</span></td></tr>
        <tr><td><strong>Overdue PO Alert</strong></td><td>Daily cron — expected_date passed</td><td>Slack alert to ops manager, PO flagged in AnyDB</td><td><span class="bdc b-ok">Scoped</span></td></tr>
        <tr><td><strong>Vendor Scorecard</strong></td><td>Monthly cron — 1st of month</td><td>On-time rate calculated, scorecard emailed to buyer</td><td><span class="bdc b-ok">Scoped</span></td></tr>
      </tbody>
    </table>
    {cs("Scope Boundary","Automations above are fixed in the Standard Build. Additional automations or custom portal views require a change order at $1,500–$3,000 per workflow depending on complexity.")}
    <h2>Integration Points</h2>
    <div class="two-col">
      <div><h3>Shopify Admin API</h3><p>Read: inventory_levels, products, locations. Write: inventory_levels/adjust on PO receive event. Auth: private app token, scoped to inventory write only.</p></div>
      <div><h3>Email / Slack</h3><p>Outbound notifications via AnyDB's built-in notification layer. Slack webhook configured per client workspace. No inbound integration in Standard Build scope.</p></div>
    </div>
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_integration_map():
    p1 = cover_dark("KC-2026-044","SYS-INTEGRATION","GOLD TIER","Integration Map",
        "Platform Architecture &amp; Data Flow","",
        "Prepared for Cascade Cycling · May 2026",
        "Cascade Cycling","Systems","6 Platforms","Complexity","High")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"SYSTEM CONNECTIONS","Integration Architecture")}
  <div class="body">
    <p>Cascade Cycling operates across six platforms that must exchange data at go-live. The table below documents each connection: direction, trigger, and the data owner responsible for maintaining credentials and field schemas.</p>
    <table class="dt">
      <thead><tr><th>From</th><th>To</th><th>Direction</th><th>Trigger</th><th>Fields</th></tr></thead>
      <tbody>
        <tr><td>Shopify POS</td><td>AnyDB</td><td>→ Push</td><td>Sale completed</td><td>order_id, line_items, location_id, staff_id</td></tr>
        <tr><td>AnyDB</td><td>Shopify Admin</td><td>→ Push</td><td>PO received</td><td>inventory_levels/adjust per SKU</td></tr>
        <tr><td>Shopify</td><td>Klaviyo</td><td>→ Push</td><td>Customer created / order placed</td><td>email, first_name, tags, total_spent</td></tr>
        <tr><td>Trek Vendor Portal</td><td>AnyDB</td><td>← Pull</td><td>Daily 6AM cron</td><td>SKU, available_qty, ETA, unit_cost</td></tr>
        <tr><td>Square (legacy)</td><td>Shopify</td><td>One-time</td><td>Migration only</td><td>customers, products, historical orders</td></tr>
        <tr><td>QuickBooks Online</td><td>AnyDB</td><td>Bi-directional</td><td>Invoice events</td><td>vendor invoices, PO costs — read-only from QBO</td></tr>
      </tbody>
    </table>
    {ca("Assumption","QuickBooks Online integration requires client to provide OAuth2 credentials and enable the Accounting API scope. This is a client-side action — Kaizen cannot proceed without it.")}
    {ci("Note","Square → Shopify is a one-time historical migration handled in the Migration Runbook. It is not a live integration and requires no ongoing credentials after go-live.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page dp">
  <div class="dp-top">
    <span class="dp-lbl">02 · CONNECTION STATUS</span>
    <div class="dp-title">Platform Connection Summary</div>
  </div>
  <div class="stat-grid">
    {stat("6","Platforms")}
    {stat("4","Live Integrations")}
    {stat("1","Pending Auth")}
  </div>
  <table class="pt">
    <thead><tr><th>Platform</th><th>Auth Status</th><th>Owner</th><th>Go-Live Risk</th></tr></thead>
    <tbody>
      <tr><td>Shopify POS → AnyDB</td><td class="cy">Configured</td><td>KaizenCommerce</td><td>Low</td></tr>
      <tr><td>AnyDB → Shopify Admin API</td><td class="cy">Configured</td><td>KaizenCommerce</td><td>Low</td></tr>
      <tr><td>Shopify → Klaviyo</td><td class="cy">Configured</td><td>Client</td><td>Low</td></tr>
      <tr><td>Trek Vendor Portal → AnyDB</td><td class="cy">Pending API key</td><td>Client — Trek rep</td><td>Medium</td></tr>
      <tr><td>QuickBooks Online → AnyDB</td><td class="cy">Pending OAuth2</td><td>Client — controller</td><td>High</td></tr>
      <tr><td>Square → Shopify (migration)</td><td class="cy">Complete</td><td>KaizenCommerce</td><td>None</td></tr>
    </tbody>
  </table>
  {dp_foot("Integration Map",3)}
</div>"""
    return p1 + p2 + p3

def doc_sops():
    p1 = cover_white("KC-2026-047","RETAIL-OPS","Standard Operating Procedures",
        "Standard Operating Procedures","Post-Go-Live Operations Reference",
        "Ridgeline Tools","Locations","3","Effective","May 1, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"END-OF-DAY","End-of-Day Close Procedure")}
  <div class="body">
    <p>This procedure applies to all three Ridgeline Tools locations. Complete steps in sequence. The AnyDB reconciliation automation runs at 9PM — the manual close must be completed before that trigger fires.</p>
    <div class="step"><div class="step-n">01</div><div class="step-b"><h3>Close open transactions</h3><p>Ensure no sales are mid-transaction. Void any incomplete holds. Check Shopify POS → Orders → Open for any stalled carts older than 2 hours.</p></div></div>
    <div class="step"><div class="step-n">02</div><div class="step-b"><h3>Count cash drawer</h3><p>Use the Shopify POS built-in cash count flow. Enter actual count — system calculates variance against expected. Variance &gt;$20 requires manager override note.</p></div></div>
    <div class="step"><div class="step-n">03</div><div class="step-b"><h3>Close the POS session</h3><p>Tap End Session in Shopify POS. Session summary emails automatically to the manager on record. Do not skip — the AnyDB automation reads session status to trigger reconciliation.</p></div></div>
    <div class="step"><div class="step-n">04</div><div class="step-b"><h3>Verify AnyDB reconciliation record</h3><p>By 9:15PM, open AnyDB → Reconciliation and confirm today's record shows status: Complete. If it shows Pending after 9:15PM, contact the manager — do not re-trigger manually.</p></div></div>
    {ci("Reminder","If POS terminal goes offline mid-shift, complete transactions in offline mode. Shopify syncs offline transactions when connectivity restores. Do not power-cycle the terminal — call the support line.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"INVENTORY","Inventory Management Procedures")}
  <div class="body">
    <p>All inventory adjustments must go through Shopify POS or the AnyDB transfer workflow. Direct edits to inventory counts in Shopify Admin are not permitted after go-live — all changes create an audit trail through AnyDB.</p>
    <table class="dt">
      <thead><tr><th>Scenario</th><th>Correct Action</th><th>Who</th><th>System</th></tr></thead>
      <tbody>
        <tr><td>Receiving a vendor shipment</td><td>Open PO in AnyDB → mark lines received → auto-adjusts Shopify</td><td>Receiving staff</td><td>AnyDB</td></tr>
        <tr><td>Moving stock between locations</td><td>Create Transfer in AnyDB → approve at destination</td><td>Ops manager</td><td>AnyDB</td></tr>
        <tr><td>Damaged or lost item</td><td>Shopify POS → Inventory → Adjust → select "Damaged"</td><td>Floor staff</td><td>Shopify POS</td></tr>
        <tr><td>Cycle count discrepancy</td><td>Adjust in Shopify Admin → add note with count date</td><td>Manager only</td><td>Shopify Admin</td></tr>
        <tr><td>Vendor return</td><td>Create return PO in AnyDB → update PO status to "returned"</td><td>Buyer</td><td>AnyDB</td></tr>
      </tbody>
    </table>
    {cs("Policy","Any inventory adjustment above $500 in value requires manager sign-off. AnyDB will flag adjustments above this threshold and hold them in a 'Pending Approval' queue.")}
    <h2>Cycle Count Schedule</h2>
    {sl(["Full store count: First Saturday of each month, before open",
         "High-velocity SKUs (top 50): Weekly, Tuesday close",
         "Seasonal departments: Quarterly, aligned to buying cycle",
         "Spot-check trigger: Any variance &gt;5 units on a single SKU"])}
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_runbook():
    p1 = cover_dark("KC-2026-029","MIGRATION","SILVER TIER","Migration Runbook",
        "Lightspeed → Shopify POS — 3 Locations","",
        "Prepared for Northern Sports · May 2026",
        "Northern Sports","Locations","3","Go-Live","May 12, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"CUTOVER TIMELINE","Go-Live Timeline")}
  <div class="body">
    <p>The cutover window is Saturday May 11 at 6PM through Sunday May 12 at 8AM. All three locations close at the same time. Shopify POS goes live simultaneously across locations to avoid split inventory state.</p>
    <table class="dt">
      <thead><tr><th>Time</th><th>Action</th><th>Owner</th><th>Fallback</th></tr></thead>
      <tbody>
        <tr><td>Sat 6:00PM</td><td>Lightspeed final export — products, customers, inventory counts</td><td>Client ops</td><td>Delay window by 2hrs max</td></tr>
        <tr><td>Sat 6:30PM</td><td>Freeze Lightspeed — no new transactions</td><td>Client ops</td><td>Mandatory — no fallback</td></tr>
        <tr><td>Sat 7:00PM</td><td>Final Matrixify import run — products and customers</td><td>Kaizen</td><td>Rerun from checkpoint file</td></tr>
        <tr><td>Sat 8:30PM</td><td>Inventory count import via Shopify Admin CSV</td><td>Kaizen</td><td>Manual entry for top 200 SKUs</td></tr>
        <tr><td>Sat 9:00PM</td><td>POS terminal activation and payment terminal pairing</td><td>Client IT</td><td>Call Shopify POS support line</td></tr>
        <tr><td>Sat 10:00PM</td><td>Dry-run transaction test — one sale per location</td><td>Kaizen + Client</td><td>Revert terminal if PIN fails</td></tr>
        <tr><td>Sun 8:00AM</td><td>Stores open on Shopify POS — go-live</td><td>All</td><td>Rollback plan in Section 4</td></tr>
      </tbody>
    </table>
    {ca("Assumption","Client IT confirms Wi-Fi and Ethernet are operational at all three locations by May 9. Network failures discovered at cutover will delay go-live — we cannot configure POS terminals remotely.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"FIELD MAPPING","Lightspeed → Shopify Field Map")}
  <div class="body">
    <p>The Matrixify import uses the column mapping below. Fields marked <span class="bdc b-crit">Transform</span> require preprocessing before import. Fields marked <span class="bdc b-done">Direct</span> map 1:1 with no modification.</p>
    <table class="dt">
      <thead><tr><th>Lightspeed Field</th><th>Shopify / Matrixify Field</th><th>Type</th><th>Notes</th></tr></thead>
      <tbody>
        <tr><td>ItemNumber</td><td>Variant SKU</td><td><span class="bdc b-done">Direct</span></td><td>Verify no leading zeros stripped</td></tr>
        <tr><td>Description</td><td>Title</td><td><span class="bdc b-done">Direct</span></td><td>Truncate at 255 chars</td></tr>
        <tr><td>UPC</td><td>Variant Barcode</td><td><span class="bdc b-crit">Transform</span></td><td>Pad to 13 digits (EAN-13)</td></tr>
        <tr><td>Price</td><td>Variant Price</td><td><span class="bdc b-done">Direct</span></td><td>Strip currency symbol first</td></tr>
        <tr><td>Category / SubCategory</td><td>Type / Tags</td><td><span class="bdc b-crit">Transform</span></td><td>Concatenate as "Category: SubCategory" tag</td></tr>
        <tr><td>VendorName</td><td>Vendor</td><td><span class="bdc b-done">Direct</span></td><td>Must match AnyDB vendors table exactly</td></tr>
        <tr><td>QtyOnHand (per store)</td><td>Inventory — Location [n]</td><td><span class="bdc b-crit">Transform</span></td><td>Split into 3 location columns</td></tr>
        <tr><td>CustomerEmail</td><td>Email</td><td><span class="bdc b-done">Direct</span></td><td>Deduplicate on email before import</td></tr>
      </tbody>
    </table>
    {ci("Note","Run the Matrixify Dry Run first. Do not import to production until Dry Run returns 0 critical errors. Warning-level errors on product images are acceptable — images are imported separately.")}
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_training():
    p1 = cover_white("KC-2026-051","STAFF-TRAINING","Training Program",
        "Staff Training Program","Shopify POS — Floor Staff &amp; Manager Tracks",
        "Granite Outdoor","Locations","3","Delivery","Remote · May 14–15, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"PROGRAM OVERVIEW","Training Modules")}
  <div class="body">
    <p>Training is delivered in two tracks over two days: Floor Staff (4 hours) and Manager (6 hours). Sessions are remote via Zoom. Each location participates together. A recording is provided for staff who miss the live session.</p>
    <h2>Floor Staff Track — Day 1 (4 hrs)</h2>
    {sl(["Module 1 — Shopify POS navigation: Smart Grid, product search, customer lookup (45 min)",
         "Module 2 — Processing sales: standard checkout, split tender, returns and exchanges (60 min)",
         "Module 3 — Inventory basics: receiving shipments, stock adjustments, cycle count entry (45 min)",
         "Module 4 — End-of-day close: POS session close, cash count, AnyDB check (30 min)",
         "Module 5 — Practice session: guided transactions on the sandbox store (60 min)"])}
    <h2>Manager Track — Day 2 (6 hrs)</h2>
    {sl(["Module 6 — Shopify Admin: orders, inventory, reports, staff permissions (60 min)",
         "Module 7 — AnyDB portal: PO management, transfers, reconciliation review (90 min)",
         "Module 8 — Reporting: end-of-day summary, inventory variance, sales by location (60 min)",
         "Module 9 — Troubleshooting: offline mode, payment terminal issues, escalation path (45 min)",
         "Module 10 — Live Q&A with KaizenCommerce implementation lead (45 min)"])}
    {cs("Guarantee","If any staff member cannot complete a module after two attempts, Kaizen will provide a 1:1 follow-up session at no additional charge within the 30-day support window.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"QUICK REFERENCE","Quick Reference — Common Scenarios")}
  <div class="body">
    <p>This page is designed to be printed and kept at each POS terminal. Covers the 12 most common edge cases reported in post-go-live support across prior implementations.</p>
    <table class="dt">
      <thead><tr><th>Scenario</th><th>Steps</th><th>If That Fails</th></tr></thead>
      <tbody>
        <tr><td>Customer wants to return without receipt</td><td>POS → Orders → search by name or email → process return to store credit</td><td>Manager override required — check ID</td></tr>
        <tr><td>Card declined but customer insists it works</td><td>Retry once. Try tap if chip failed. Ask for alternate payment.</td><td>Switch terminal — issue may be hardware</td></tr>
        <tr><td>Barcode won't scan</td><td>Use POS search by SKU or product name. Scan the manual entry field.</td><td>Check for barcode damage — reprint from AnyDB</td></tr>
        <tr><td>POS terminal offline</td><td>Continue in offline mode — POS stores transactions locally and syncs when restored</td><td>Do NOT restart POS — call manager</td></tr>
        <tr><td>Item priced wrong at checkout</td><td>Manager applies manual discount with note. Flag SKU for price audit in AnyDB.</td><td>Void sale and re-ring with correct price</td></tr>
        <tr><td>Inventory shows zero but item is on shelf</td><td>Complete the sale. Flag for inventory adjustment by manager after close.</td><td>Manager adjusts in Shopify Admin with count date note</td></tr>
      </tbody>
    </table>
    {ci("Support Line","During the 30-day post-go-live window, reach KaizenCommerce at support@kaizencommerce.ca or Slack #northwall-support. Response SLA: 2 hours during business hours.")}
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_health_check():
    p1 = cover_dark("KC-2026-053","POST-GO-LIVE","90-DAY REVIEW","Health Check Report",
        "Post-Go-Live Performance Review","",
        "Prepared for Ridgeline Tools · May 2026",
        "Ridgeline Tools","Days Since Go-Live","92","Period","Feb–Apr 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"PERFORMANCE METRICS","Performance at 90 Days")}
  <div class="body">
    <p>Ridgeline Tools went live on Shopify POS across three locations on January 28, 2026. The metrics below cover the first 90 operating days. All figures sourced from Shopify Analytics and AnyDB reporting.</p>
    <h2>Operations</h2>
    <table class="dt">
      <thead><tr><th>Metric</th><th>Baseline (Lightspeed)</th><th>Current (Shopify)</th><th>Change</th></tr></thead>
      <tbody>
        <tr><td>End-of-day close time</td><td>38 min average</td><td>9 min average</td><td><span class="bdc b-done">−76%</span></td></tr>
        <tr><td>Inventory variance (monthly count)</td><td>4.2% avg discrepancy</td><td>1.1% avg discrepancy</td><td><span class="bdc b-done">−74%</span></td></tr>
        <tr><td>PO processing time (create to receive)</td><td>Manual, 45 min</td><td>AnyDB, 8 min</td><td><span class="bdc b-done">−82%</span></td></tr>
        <tr><td>Support tickets to Kaizen</td><td>N/A</td><td>6 in 90 days</td><td><span class="bdc b-ok">On Track</span></td></tr>
      </tbody>
    </table>
    {ci("Highlight","The AnyDB end-of-day automation has fired 276 times across three locations with zero failures. One manual override was required on March 3 due to a network outage at Location 2 — resolved in 12 minutes.")}
    <h2>Open Issues</h2>
    {sl(["Barcode scanner at Location 3 intermittently drops Bluetooth — hardware replacement recommended",
         "Shopify Reports custom date range export times out for ranges &gt;60 days — Shopify known issue, workaround documented",
         "Staff turnover at Location 1 — two new hires need Module 1–4 training (covered in retainer)"])}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page dp">
  <div class="dp-top">
    <span class="dp-lbl">02 · SCORE SUMMARY</span>
    <div class="dp-title">Health Score — 90 Days</div>
  </div>
  <div class="stat-grid">
    {stat("94","Health Score / 100")}
    {stat("−76%","Close Time Reduction")}
    {stat("$0","Unplanned Overages")}
  </div>
  <table class="pt">
    <thead><tr><th>Domain</th><th>Score</th><th>Status</th><th>Next Action</th></tr></thead>
    <tbody>
      <tr><td>POS Operations</td><td class="cy">97 / 100</td><td>Healthy</td><td>No action required</td></tr>
      <tr><td>Inventory Accuracy</td><td class="cy">92 / 100</td><td>Healthy</td><td>Monthly cycle count — on schedule</td></tr>
      <tr><td>AnyDB Automations</td><td class="cy">99 / 100</td><td>Healthy</td><td>No action required</td></tr>
      <tr><td>Staff Proficiency</td><td class="cy">88 / 100</td><td>Watch</td><td>Train 2 new hires — booked May 20</td></tr>
      <tr><td>Hardware</td><td class="cy">85 / 100</td><td>Watch</td><td>Replace Location 3 scanner — est. $180</td></tr>
      <tr><td>Reporting</td><td class="cy">90 / 100</td><td>Healthy</td><td>Shopify bug — workaround documented</td></tr>
    </tbody>
  </table>
  {dp_foot("Health Check Report",3)}
</div>"""
    return p1 + p2 + p3

def doc_change_order():
    p1 = cover_white("KC-2026-CO-003","SCOPE-CHANGE","Change Order",
        "Change Order #CO-2026-003","Additional Scope — Shopify Flow + Custom Reporting",
        "Northwall Supply Co.","Original Engagement","KC-2026-042","Issued","April 20, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"SCOPE CHANGE","Additional Scope")}
  <div class="body">
    <p>During Week 4 of the Gold tier engagement, Northwall Supply Co. requested two items outside the original signed scope: a custom Shopify Flow automation for wholesale customer tagging, and a Shopify Analytics custom report dashboard for the CFO. This change order documents the additional work, investment, and revised timeline.</p>
    <h2>Additional Deliverables</h2>
    {sl(["Shopify Flow: Wholesale Customer Tagger — auto-applies 'wholesale' tag when an approved order-value threshold is reached within the agreed evaluation window. Triggers price list switch to the B2B catalog.",
         "Custom Shopify Analytics Report: CFO Dashboard — weekly email with gross margin by location, top 20 SKUs by revenue, and inventory turn rate. Built in Shopify Analytics + exported via Klaviyo.",
         "Documentation for both: trigger logic, edge cases, maintenance guide"])}
    <h2>Out of Scope for This Change Order</h2>
    {sl(["Changes to the existing Gold tier POS implementation scope",
         "Additional Shopify Flow automations beyond the two above",
         "B2B portal or Shopify B2B features — separate engagement if needed"])}
    {cs("Scope Protection","This change order does not extend or modify the original go-live date of May 12, 2026. Both deliverables will be completed during the 30-day post-go-live window.")}
    {ca("Assumption","Client provides the wholesale customer criteria (approved order-value threshold, evaluation window, and customer tags) in writing by April 25. Confirm these inputs before work begins; no threshold or window is implied by this sample.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"INVESTMENT","Revised Investment")}
  <div class="body">
    <p>The investment below is additive to the original Gold tier engagement (KC-2026-042). Unless an approved alternative or signed agreement controls, payment follows the standard 50% / 25% / 25% implementation schedule: 50% deposit on signature, 25% at named mid-project acceptance, and 25% at agreed completion, with Net 7 terms.</p>
    <table class="dt">
      <thead><tr><th>Item</th><th>Fee (USD)</th><th>Timeline</th></tr></thead>
      <tbody>
        <tr><td>Shopify Flow — Wholesale Customer Tagger</td><td>$1,200</td><td>Week 1 post-go-live</td></tr>
        <tr><td>CFO Analytics Dashboard (build + Klaviyo setup)</td><td>$1,800</td><td>Week 2 post-go-live</td></tr>
        <tr><td>Documentation (both deliverables)</td><td>Included</td><td>Delivered with each item</td></tr>
        <tr><td><strong>Change Order Total</strong></td><td><strong>$3,000</strong></td><td>50% deposit; 25% mid-project acceptance; 25% agreed completion — Net 7</td></tr>
      </tbody>
    </table>
    <h2>Approval</h2>
    <p>This change order is valid for 7 days from the issue date. Signature constitutes approval of the scope and investment above. Work will not begin until a signed copy is returned.</p>
    <table class="dt" style="margin-top:20pt;">
      <thead><tr><th>Party</th><th>Name</th><th>Signature</th><th>Date</th></tr></thead>
      <tbody>
        <tr><td>KaizenCommerce</td><td>Kaizen Commerce operator</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        <tr><td>Northwall Supply Co.</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
      </tbody>
    </table>
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_hardware():
    p1 = cover_dark("KC-2026-033","HARDWARE-NET","SILVER TIER","Hardware Plan",
        "Device Specification &amp; Network Architecture","",
        "Prepared for Peak Supply · May 2026",
        "Peak Supply","Locations","3","Assessment","April 18, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"DEVICE SPECIFICATION","Device Specification")}
  <div class="body">
    <p>The hardware plan below covers all three Peak Supply locations. Quantities are per-location unless noted. All hardware is client-procured — Kaizen provides the spec and configuration guide. Shopify POS Pro license is included in the Silver tier engagement fee.</p>
    <table class="dt">
      <thead><tr><th>Device</th><th>Model</th><th>Qty / Location</th><th>Purpose</th><th>Est. Cost</th></tr></thead>
      <tbody>
        <tr><td>POS Terminal</td><td>iPad 10th Gen (10.9")</td><td>2</td><td>Primary checkout, returns</td><td>$449 each</td></tr>
        <tr><td>iPad Stand</td><td>Shopify POS Stand (USB-C)</td><td>2</td><td>Counter mount</td><td>$149 each</td></tr>
        <tr><td>Payment Terminal</td><td>Shopify WisePad 3</td><td>2</td><td>Chip, tap, swipe</td><td>$49 each</td></tr>
        <tr><td>Barcode Scanner</td><td>Zebra DS2208 (USB)</td><td>2</td><td>Receiving + checkout</td><td>$189 each</td></tr>
        <tr><td>Receipt Printer</td><td>Star Micronics TSP143IV</td><td>1</td><td>Paper receipts (optional)</td><td>$299 each</td></tr>
        <tr><td>Network Switch</td><td>TP-Link TL-SG108 (8-port)</td><td>1</td><td>POS + back office Ethernet</td><td>$35 each</td></tr>
        <tr><td>Wi-Fi Access Point</td><td>Ubiquiti U6 Lite</td><td>1</td><td>POS VLAN + guest VLAN</td><td>$99 each</td></tr>
      </tbody>
    </table>
    {ci("Recommendation","Run POS terminals on Ethernet via the iPad USB-C port and the Shopify POS Stand's built-in Ethernet passthrough. Wi-Fi is acceptable but Ethernet eliminates the most common cause of mid-transaction drops.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"NETWORK ARCHITECTURE","Network Architecture")}
  <div class="body">
    <p>Each location requires two VLANs: one isolated POS VLAN and one general office/guest VLAN. POS terminals must never share a subnet with general browsing devices. The Ubiquiti U6 Lite supports VLAN tagging natively via the UniFi controller.</p>
    <table class="dt">
      <thead><tr><th>VLAN</th><th>ID</th><th>Devices</th><th>Internet</th><th>Cross-VLAN</th></tr></thead>
      <tbody>
        <tr><td>POS Network</td><td>VLAN 10</td><td>iPads, WisePad terminals, receipt printers</td><td>Yes — Shopify only (whitelist)</td><td>Blocked</td></tr>
        <tr><td>Office / Back of House</td><td>VLAN 20</td><td>Manager laptop, AnyDB access, inventory PC</td><td>Yes — unrestricted</td><td>Blocked from POS</td></tr>
        <tr><td>Guest Wi-Fi</td><td>VLAN 30</td><td>Customer devices, staff personal phones</td><td>Yes — rate limited</td><td>Blocked from both</td></tr>
      </tbody>
    </table>
    {ca("Assumption","ISP modem/router at each location supports VLAN tagging or can be placed in bridge mode. If not, client must replace the ISP-provided device with a business-grade router (TP-Link ER605 recommended at $60).")}
    <h2>Pre-Go-Live Network Checklist</h2>
    {sl(["VLAN 10 and 20 confirmed operational at all 3 locations by May 9",
         "Each POS terminal can reach api.shopify.com and checkout.shopify.com on VLAN 10",
         "Payment terminal paired and test transaction completed per location",
         "WisePad firmware updated to latest version before go-live",
         "Ubiquiti U6 Lite SSIDs: 'PeakPOS' (hidden) and 'PeakGuest' (visible)"])}
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

def doc_validation():
    p1 = cover_white("KC-2026-035-V2","MIGRATION-QA","Validation Report",
        "Import Validation Report","Dry Run #2 — Products &amp; Customers",
        "Northern Sports","Dry Run","#2 of 2","Run Date","April 17, 2026")

    p2 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(1,"VALIDATION RESULTS","Dry Run Results")}
  <div class="body">
    <p>Dry Run #2 was executed on April 17 against the Northern Sports staging store. The import covered 18,400 products and 6,200 customers. Results below are the full error and warning log — all Critical errors must resolve to zero before the production import.</p>
    <table class="dt">
      <thead><tr><th>#</th><th>Error / Warning</th><th>Severity</th><th>Count</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>1</td><td>Duplicate SKU: same SKU mapped to two variant rows</td><td><span class="bdc b-crit">Critical</span></td><td>47</td><td><span class="bdc b-ok">Fixed in v3</span></td></tr>
        <tr><td>2</td><td>Barcode field exceeds 14 characters (EAN-13 violation)</td><td><span class="bdc b-crit">Critical</span></td><td>12</td><td><span class="bdc b-ok">Fixed in v3</span></td></tr>
        <tr><td>3</td><td>Product type not in Shopify allowed list — special characters</td><td><span class="bdc b-imp">Important</span></td><td>89</td><td><span class="bdc b-ok">Fixed in v3</span></td></tr>
        <tr><td>4</td><td>Customer email missing @ — malformed records from Lightspeed export</td><td><span class="bdc b-imp">Important</span></td><td>14</td><td>Client to provide corrected list</td></tr>
        <tr><td>5</td><td>Image URL returns 404 — images not uploaded to CDN yet</td><td><span class="bdc b-ok">Warning</span></td><td>2,140</td><td>Expected — images import separately</td></tr>
        <tr><td>6</td><td>Inventory level set to negative — legacy Lightspeed backorder records</td><td><span class="bdc b-imp">Important</span></td><td>6</td><td>Set to 0 in v3 cleaning script</td></tr>
      </tbody>
    </table>
    {ci("Status","Dry Run #2 result: 2 Critical errors remain (items 4 above — client action required). All Kaizen-side errors are resolved in the v3 import file. Production import is blocked until item 4 is resolved.")}
  </div>
  {foot(2)}
</div>"""

    p3 = f"""
<div class="page" style="background:#F5F7F9;">
  {sec(2,"RESOLUTION PLAN","Resolution Plan &amp; Sign-Off")}
  <div class="body">
    <p>One action remains with the client before production import can proceed. All Kaizen-side fixes are complete and verified in the v3 import file (northern-sports-products-v3.csv, northern-sports-customers-v3.csv).</p>
    <h2>Client Action Required</h2>
    {sl(["Provide corrected customer records for the 14 malformed email addresses — either corrected email or confirmation to exclude those records from the import",
         "Deadline: April 22, 2026. Import will not proceed without this confirmation.",
         "Send corrected list to operations@kaizencommerce.ca with subject: Northern Sports — Customer Email Fix"])}
    {ca("Blocking Item","The 14 malformed customer records will fail silently in Matrixify — they will be skipped without error. If Kaizen proceeds without correction, those customers will not exist in Shopify at go-live. This is a client decision: exclude them or fix them.")}
    <h2>Production Import Checklist</h2>
    {sl(["v3 product file validated — 0 critical errors confirmed",
         "v3 customer file validated — 0 critical errors (pending email fix)",
         "Staging store import matches expected product count: 18,400",
         "Inventory levels seeded correctly — spot-check 20 SKUs against physical count",
         "Client sign-off received on this report before production import begins"])}
    {cs("Sign-Off","By approving this report, Northern Sports confirms that Dry Run #2 results have been reviewed and the production import may proceed once the client action above is complete.")}
    <div style="margin-top:20pt;">
      <table class="dt">
        <thead><tr><th>Approved By</th><th>Role</th><th>Signature</th><th>Date</th></tr></thead>
        <tbody>
          <tr><td>&nbsp;</td><td>Northern Sports Operations</td><td>&nbsp;</td><td>&nbsp;</td></tr>
          <tr><td>Kaizen Commerce operator</td><td>KaizenCommerce Lead</td><td>&nbsp;</td><td>April 17, 2026</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  {foot(3)}
</div>"""
    return p1 + p2 + p3

# ─── Assemble ───────────────────────────────────────────────────────────────

def build_full_html():
    sections = [
        ("01 — Proposal",          doc_proposal()),
        ("02 — Blueprint Report",  doc_blueprint()),
        ("03 — AnyDB Spec",        doc_anydb()),
        ("04 — Integration Map",   doc_integration_map()),
        ("05 — SOPs",              doc_sops()),
        ("06 — Migration Runbook", doc_runbook()),
        ("07 — Training Materials",doc_training()),
        ("08 — Health Check",      doc_health_check()),
        ("09 — Change Order",      doc_change_order()),
        ("10 — Hardware Plan",     doc_hardware()),
        ("11 — Validation Report", doc_validation()),
    ]

    pages_html = ""
    for label, html in sections:
        pages_html += f"\n<!-- ═══ {label} ═══ -->\n" + html

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
{CSS}
</style>
</head>
<body>
{pages_html}
</body>
</html>"""


def main():
    full_html = build_full_html()
    with open(OUT_HTML, "w") as f:
        f.write(full_html)

    print(f"HTML written: {OUT_HTML}")

    result = subprocess.run(
        ["weasyprint", OUT_HTML, OUT_PDF],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"PDF rendered: {OUT_PDF}")
    else:
        print("STDERR:", result.stderr[-3000:])
        print("Return code:", result.returncode)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
