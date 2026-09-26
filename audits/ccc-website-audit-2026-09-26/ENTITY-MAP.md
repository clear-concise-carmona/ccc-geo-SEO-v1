# Entity Map: Clear Concise Consulting

Workspace: ccc-website-audit-2026-09-26 | Evidence basis: search-index observations, one direct first-party fetch (GitHub README, EV-007), owner-authored strategy documents (EV-032 to EV-035). No live-site HTML or deployed JSON-LD was observable this run (EV-001).

## 1. Core entities

| Entity | Type (schema.org) | Proposed @id | Observed names | Status |
|---|---|---|---|---|
| Clear Concise Consulting | Organization (ProfessionalService is acceptable; LocalBusiness only if a customer-facing location is confirmed, ISS-015) | https://www.clearconciseconsulting.com/#organization | "Clear Concise Consulting", "CCC", "Clear Concise Consulting LLC" (BBB, EV-025) | Legal name vs brand name: use legalName "Clear Concise Consulting LLC" only after owner confirms |
| Jeremy Carmona | Person | https://www.clearconciseconsulting.com/about#person | "Jeremy Carmona", "Jeremy A. Carmona" (LinkedIn slug jeremy-a-carmona), "Carmona" (Salesforce Ben author page title) | Consistent; use "Jeremy Carmona" everywhere |

## 2. Verified relationships (observed in at least one first-party and one independent surface)

| Relationship | Evidence | Confidence |
|---|---|---|
| Jeremy Carmona founded and leads Clear Concise Consulting | EV-006, EV-007, EV-025 | high |
| Jeremy Carmona is the author of Salesforce Ben articles (author page + one article URL indexed) | EV-005, EV-018 | high (URLs indexed; pages not fetched) |
| Jeremy Carmona publishes on Medium (@jcarmona86) and Salesforce Break (author page) | EV-005, EV-017 | high (indexed) |
| Clear Concise Consulting maintains open-source Salesforce tools on GitHub (org clear-concise-carmona) | EV-007 (direct fetch) | high |
| Clear Concise Consulting has a LinkedIn company page and a BBB profile (Brooklyn, NY) | EV-025 | high (indexed) |
| Jeremy Carmona has a LinkedIn profile linked from the GitHub README | EV-007 | high |

## 3. First-party-only relationships (published by CCC; independent corroboration not obtained this run)

| Relationship | Evidence | What would corroborate |
|---|---|---|
| Jeremy Carmona holds 13 Salesforce certifications, including Application Architect, Data Architecture and Management Designer, Sharing and Visibility Designer, Nonprofit Cloud Consultant | EV-005, EV-007, EV-031 | Trailhead credential verification page |
| Jeremy Carmona taught Salesforce Administration at NYU Tandon | EV-007, EV-017 | NYU program page naming the instructor (host blocked) |
| CCC worked with USCIS, EDF, UnitedHealth Group, HRSA, NYU | EV-011, EV-023 | Owner documentation of relationship type and permission |
| CCC delivered the enterprise CPQ engagement (40% cycle reduction) | EV-010, EV-027 | Client confirmation or measurement note |
| CCC founded in 2018 | EV-025, EV-028 | State registration record or BBB "in business since" |

## 4. Services and assets (as observed)

| Offer / asset | URL observed | Entity role | Notes |
|---|---|---|---|
| Salesforce implementation | /services/salesforce-implementation | Service | Price range consistent (FACT-10) |
| Data governance | /services/data-governance | Service | Timeline claims qualified (FACT-18) |
| AI data preparation | /services/salesforce-ai-data-preparation | Service; candidate landing page for the paid assessment | Offer name unresolved (FACT-15) |
| Training and documentation | /services/salesforce-training | Service | |
| Administration retainer; ad hoc support | non-www /services/salesforce-administration; /services/ad-hoc-support | Service (index state unclear, ISS-002) | |
| Architecture advisory retainer | described on /faqs | Service | |
| Workshops (AI readiness, training) | described on /faqs and built-in-domain /ai-services | Service | |
| AI Readiness Scorecard (free) | /scorecard | Lead asset | Method statement unresolved (FACT-16) |
| Digital products | Gumroad (two handles observed, CLM-040) | Product catalog | Canonical URL decision needed |
| Open-source tools | github.com/clear-concise-carmona | Software / credibility asset | Ten tools listed (EV-007) |
| Case study: enterprise CPQ | /case-studies/enterprise | CreativeWork (case study) | Only case-study URL indexed |
| Governance narratives | /blog/six-governance-checkpoints-engagement; /blog/ai-reversibility-rollback-plan | Article | Anonymized; labeling needed (FACT-23) |
| Methodologies | pre-Agentforce data checklist; six governance checkpoints; org health 30-60-90 roadmap; scorecard categories | First-party frameworks | Good candidates for definitional passages and internal links |

## 5. Verified public profiles for sameAs (target list)

Core set (observed as indexed or directly fetched; owner to confirm each is official):
- https://www.linkedin.com/in/jeremy-a-carmona/ (Person; linked from GitHub README, EV-007)
- https://www.linkedin.com/company/clear-concise-consulting (Organization; EV-025)
- https://www.salesforceben.com/author/jeremy-carmona/ (Person; EV-005, EV-018)
- https://medium.com/@jcarmona86 (Person; EV-005, EV-018)
- https://salesforcebreak.com/author/cccjeremycarmona/ (Person; EV-005)
- https://github.com/clear-concise-carmona (Organization; EV-007)

Candidates pending owner confirmation:
- Gumroad: https://jeremycarmona.gumroad.com OR https://gumroad.com/clearconciseconsulting (CLM-040)
- Facebook: https://www.facebook.com/people/Clear-Concise-Consulting/61565894325721/ (EV-025; confirm official and active)
- BBB profile (EV-025): include only if the owner wants it as an identity anchor

Owner rule (EV-032): every deployed sameAs array must be identical. The reconciliation file is implementation/jsonld/sameas-target-list.json.

## 6. Inconsistencies and gaps

| Item | Detail | Related |
|---|---|---|
| Positioning drift across surfaces | Current pages: AI governance for four verticals. Legacy: "Small Business" (/who-we-help), "Tailored Salesforce Solutions" (/new-clients), "growing businesses" (built-in domain FAQ), BBB description (admin, migration, project management) | CLM-029 to CLM-033; ISS-009, ISS-001 |
| Homepage title variants | Local-consultant framing vs AI governance framing both indexed | CLM-038; ISS-004 |
| Team description | "leads every engagement" vs "backed by a network of administrators, developers and trainers" (stale surface) | CLM-027/028 |
| Offer naming | Free scorecard and a paid tier share the name "AI Readiness Scorecard" in owner docs; the brief's offer name is absent from the site | CLM-015, CLM-016; ISS-006 |
| Publication title | Working title vs published Salesforce Ben title | CLM-043; ISS-017 |
| Contact identity | Three emails; two Gumroad handles | CLM-039, CLM-040 |
| Local entity | NYC in titles and LocalBusiness schema without a verified customer-facing office; national client footprint | CLM-034; ISS-015 |
| Teaching tense | "teaches" vs "former instructor" | CLM-003 |

## 7. Internal-linking and structured-data opportunities (no fabrication; all targets observed)

- Every blog byline -> /about (Person page), and /about -> /policies-commitments (editorial policy, FACT-20).
- /blog/salesforce-ai-data-readiness-checklist -> assessment landing page (once named) and /scorecard.
- /blog/six-governance-checkpoints-engagement and /blog/ai-reversibility-rollback-plan -> assessment landing page; each other.
- /blog/salesforce-validation-rules-guide, /blog/salesforce-duplicate-management-guide, /blog/salesforce-org-health-roadmap -> /services/data-governance.
- /about -> GitHub org page (open-source tools) and Salesforce Ben author page (external, sameAs-aligned).
- Person schema: jobTitle "Salesforce Architect", worksFor -> #organization, alumniOf/affiliation for NYU only if the owner confirms current wording; knowsAbout limited to topics with published articles (AI governance, data governance, Salesforce data quality, Nonprofit Cloud).
- Organization schema: founder -> #person, sameAs core set, contactPoint one address (FACT-24), address only if accurate, no aggregateRating, no review markup, no areaServed beyond the verified footprint.

## 8. Cautions

- Do not infer a customer-facing office from the BBB Brooklyn listing or a mailing address.
- Do not add Wikipedia/Wikidata sameAs entries: none exist for CCC or Jeremy Carmona in observed results, and creating them is out of scope for this audit.
- Do not present the toolkit's or SEOmator's heuristic scores as evidence of AI visibility.
