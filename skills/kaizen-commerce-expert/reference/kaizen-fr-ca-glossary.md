# Kaizen FR-CA Terminology Glossary + Bilingual QA Checklist

Load this reference whenever producing French output under `variants/fr-ca-mode.md`. This is a
**starter glossary**: Québec French (fr-CA), not France French. the operator is the native-speaker
authority — every new term pairing he corrects gets added here, making this file the single
terminology source of truth. Status: requires the operator's review pass before any entry is treated
as settled; unreviewed terms are working drafts.

## Why this exists (commercial context)

Québec merchants operate under Bill 96 / Charter of the French Language obligations (customer
service and commerce in French) and Law 25 (privacy). A bilingual Montreal agency that writes
*correct Québec commercial French* — not translated-sounding French — is a differentiator in
exactly the FR-CA segment competitors can't serve. Outreach in French to a francophone merchant
is a positioning statement by itself.

## Scope gate (mirror of fr-ca-mode)

FR-CA output is approved for: **outreach messages, call summaries, executive summaries, proposal
cover notes.** Full bilingual proposals, SOWs, and legal/commercial terms remain English-only
until this glossary has a completed review pass and the bilingual QA process below has run
clean on at least three real artifacts. Binding commercial language is NEVER drafted in French
from this starter glossary.

## Core commerce terminology (EN → fr-CA)

| English | fr-CA (Québec usage) | Notes |
|---|---|---|
| retail / retailer | commerce de détail / détaillant | |
| store / location | succursale (multi-loc context), magasin, boutique | "succursale" for multi-location discussions |
| point of sale (POS) | point de vente (PDV) | keep "Shopify POS" as product name |
| checkout (in-store) | caisse | |
| checkout (online) | passage à la caisse | |
| inventory | inventaire / stock | "inventaire" also = the counting act; disambiguate |
| cycle count | décompte cyclique / inventaire tournant | |
| stockout | rupture de stock | |
| oversell | survente | |
| order | commande | |
| purchase order (PO) | bon de commande | |
| receiving | réception (de marchandise) | |
| transfer (inter-store) | transfert (entre succursales) | |
| supplier / vendor | fournisseur | |
| warehouse | entrepôt | |
| fulfillment | traitement des commandes / exécution | context-dependent |
| shipping / delivery | expédition / livraison | |
| returns / refund | retours / remboursement | |
| gift card | carte-cadeau | |
| loyalty program | programme de fidélisation | |
| customer account | compte client | |
| pricing | tarification | |
| quote | **soumission** | Québec term — not "devis" (France) |
| proposal | proposition / offre de service | |
| statement of work (SOW) | énoncé des travaux | EN-only artifact for now |
| deposit | acompte | |
| invoice | facture | |
| payment terms | modalités de paiement | |
| retainer | mandat récurrent / forfait mensuel | |
| go-live | mise en service | |
| cutover | bascule | |
| training | formation | |
| staff | personnel / équipe | |
| dashboard / report | tableau de bord / rapport | |
| reconciliation | rapprochement / réconciliation | accounting: "rapprochement" |
| migration | migration (de données) | |
| back-office | arrière-boutique (ops) / back-office (systems) | systems context keeps EN |

## Brand and product terms — never translate

KaizenCommerce · Kai · Blueprint (« le Blueprint ») · Shopify, Shopify POS, Shopify Plus ·
AnyDB · Matrixify · tier names (Silver/Gold/Diamond) · pack names. Article usage: "le Blueprint",
"une migration vers Shopify POS".

## Register and format rules (fr-CA business writing)

- **Vouvoiement** by default in first contact and all written outreach; mirror the merchant if
  they switch to "tu" in conversation.
- Currency: `10 000 $` — non-breaking space as thousands separator, `$` after the amount with a
  space. Never `$10,000` inside French prose.
- Dates: `le 15 mars 2026` in prose.
- Decimal comma in French prose (`2,5 heures`), decimal point in shared tables/data.
- Avoid anglicisms common in France-French tech writing when a Québec form exists ("courriel"
  over "email" in formal writing; "clavardage" is overkill — "messagerie" is fine).
- Keep the voice canon's rules in both languages: no filler, no hollow openers, no « J'espère que
  ce courriel vous trouve bien » (same forbidden-phrase class as English).

## Bilingual QA checklist (run before ANY French artifact ships)

1. **Scope check:** artifact type is one of the four approved (outreach / call summary / exec
   summary / proposal cover note). Anything else → English, with a French cover note if useful.
2. **Glossary conformity:** every term above appears in its fr-CA form; "soumission" not "devis";
   brand terms untranslated.
3. **No machine-translation tells:** read aloud test — calques like « adresser un problème »
   (→ « s'attaquer à un problème ») or « supporter » for "support" (→ « prendre en charge »,
   « soutenir ») fail QA.
4. **Format:** currency, dates, decimal commas per rules above; French typography (« » guillemets
   optional but consistent; non-breaking spaces before : ; ! ?).
5. **Register:** vouvoiement consistent; no mixed tu/vous.
6. **Commercial safety unchanged:** all English-mode guardrails apply — figures only from pricing
   canon, no ROI promises, two-lane commercial model. Translation never loosens a guardrail.
7. **Native review:** the operator reads it before it ships. Until three consecutive artifacts pass
   with no corrections, this step is mandatory; afterward it stays mandatory for new artifact
   types and stays recommended for everything else.
8. **Capture:** corrections feed back into this glossary (new row or fixed note) — that is how
   the glossary graduates from starter to settled.
