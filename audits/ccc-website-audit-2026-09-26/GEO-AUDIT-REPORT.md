# GEO and SEO Audit Report: clearconciseconsulting.com

Workspace: ccc-website-audit-2026-09-26 | Run date: 2026-09-26 | Mode: AUDIT_AND_DRAFT
Toolkit: clear-concise-carmona/ccc-geo-SEO-v1 @ 383829485f8620e7ca20a333e16db023644f5545 (branch claude/ccc-website-seo-geo-audit-a4t65i)
Decision sequence: TRUTH -> ENTITY -> DISCOVERY -> CONVERSION

## 1. Executive summary

The live site could not be fetched from this environment. The network policy denied www.clearconciseconsulting.com, the Squarespace built-in domain, and the Internet Archive (EV-001). No HTML, headers, robots.txt, sitemap, JSON-LD, rendered DOM, performance, or accessibility observation was possible. The `/geo audit` command, which depends on those fetches, did not run. The toolkit's composite GEO Score is not reported.

What was possible: a bounded review of what search engines have indexed for the domain (titles, URLs, snippets across 28 queries), one direct first-party fetch (the CCC GitHub README), and a reconciliation of published claims against the owner's own strategy documents. That was enough to establish the TRUTH and ENTITY layers to a useful degree, and to surface several index-level defects that do not need HTML to confirm they exist.

Five supported findings:

1. **The paid assessment offer that the business goal depends on is not findable by name.** No indexed CCC page carries "Salesforce AI Data Readiness Assessment." The site names a "data quality assessment from $5,000"; owner documents name an "$8,000 AI Governance Assessment" and a paid tier called "AI Readiness Scorecard," which is also the name of the free tool. (F-01; ISS-006; CLM-013 to CLM-016)
2. **The free scorecard's method is described two incompatible ways** in indexed text: 15 questions across five categories, and 30 questions on a 1-to-5 scale with 120 and 60 thresholds. One of these is wrong or stale. (F-02; ISS-005)
3. **Stale surfaces are still indexed and contradict current positioning:** five URLs on clearconciseconsulting.squarespace.com (including a page titled "FAQs 2" describing a team "network" and "growing businesses"), two non-www URLs with duplicate titles, the commerce cart page, and legacy pages /new-clients and /who-we-help ("Small Business"). (F-03; ISS-001, ISS-002, ISS-003, ISS-009)
4. **The homepage is indexed under two different titles**, one local-consultant framing and one AI-governance framing. Which is live is unknown; the split itself is the finding. (F-04; ISS-004)
5. **Entity facts are consistent where it matters but under-substantiated where liability is highest.** Credentials, founding year, NYU teaching, the 80% placement statistic, the five named client organizations, and case-study metrics all rest on first-party statements without visible method or permission notes. (F-05; ISS-018, ISS-019; FACT-03 to FACT-07, FACT-21 to FACT-23)

No change is recommended for security headers, Lighthouse performance, robots.txt edits, or Cloudflare (platform-controlled, owner-documented). No page deletions are recommended.

## 2. Scope and coverage

| Item | Result |
|---|---|
| Target | https://www.clearconciseconsulting.com/ |
| Pages discovered | 44 first-party URLs (37 on www, 2 on non-www host, 5 on the built-in Squarespace domain) plus 3 owner-reported/not-observed URLs. See URL-INVENTORY.csv |
| Pages fetched | 0 (network policy, EV-001) |
| Pages audited from index data | 44 (titles, snippets, host, path) |
| Discovery method | WebSearch queries (site: operators and topical queries), GitHub README, owner documentation. robots.txt and sitemap.xml were not readable |
| Coverage statement | This is a search-index sample, not site coverage. Pages that are not indexed, or not surfaced by the 28 queries, are not represented. Blog coverage in particular is partial (16 of an owner-reported 54+ posts). |
| Excluded | Nothing excluded by choice; everything excluded by network policy |
| Rate limits | Not applicable (no requests reached the origin) |

## 3. Methodology and evidence classes

Evidence classes used in this workspace:

- **Direct observation (index):** URL, title, and snippet text as returned by the search tool. Titles are strong evidence of the SEO title at last crawl. Snippets are weaker: they may be truncated, rewritten, or blended across sources by the tool.
- **Direct observation (fetch):** GitHub README only (EV-007).
- **Owner-provided documentation:** the CCC Squarespace operations, positioning, conversion, and audience skills (EV-032 to EV-035). Treated as statements of intent and as owner-reported site state as of their dates (April to May 2026). Not treated as live-site observation.
- **Tool heuristics:** none executed against the target. SEOmator scores quoted in owner docs are third-party heuristics and are not repeated as findings.
- **Hypotheses:** query-page map topics, conversion friction, and competitive observations are labeled as such.
- **Checks not completed:** every live-site check. Listed in section 9 and RUN-STATUS.md.

Every finding below cites evidence IDs that resolve to files under evidence/ (see evidence/evidence-index.md). Claim IDs (CLM-) resolve to BUSINESS-CLAIMS-INVENTORY.csv; issue IDs (ISS-) to PRIORITIZED-BACKLOG.csv; fact IDs (FACT-) to CANONICAL-BUSINESS-FACTS.md.

## 4. Toolkit rubric coverage (composite score not computable)

Rubric: geo-seo-claude composite GEO Score, weights per geo/SKILL.md and docs/scoring-methodology.md at the revision above. Inputs are heuristic; the score is a diagnostic rubric, not a search metric or citation probability.

| Category | Weight | Required inputs | Available this run | Status |
|---|---|---|---|---|
| AI Citability and Visibility | 25% | page HTML for passage scoring; robots.txt for crawler access | none | NOT SCORED |
| Brand Authority Signals | 20% | platform presence checks (YouTube, Reddit, Wikipedia, LinkedIn) | partial: LinkedIn (person and company), Medium, GitHub, BBB, Facebook observed as indexed; no Wikipedia entity found; Reddit and YouTube not checked | NOT SCORED (component notes in section 6) |
| Content Quality and E-E-A-T | 20% | article bodies, bylines, dates | titles and snippets only | NOT SCORED |
| Technical Foundations | 15% | HTML, headers, robots, sitemap, rendering | none | NOT SCORED |
| Structured Data | 10% | raw HTML JSON-LD | none; owner-reported types only | NOT SCORED |
| Platform Optimization | 10% | all of the above | none | NOT SCORED |

Per the brief, missing inputs were not replaced with zero and weights were not adjusted. Component findings and coverage are reported instead.

## 5. Findings

Format: ID | layer | observation | evidence | class | confidence | consequence | action | verification.

**F-01 | TRUTH/CONVERSION | Paid assessment offer not findable by name; offer names and prices diverge across surfaces.**
Observation: no indexed page or snippet uses "Salesforce AI Data Readiness Assessment." /faqs states "a data quality assessment starts at $5,000." Owner positioning and conversion documents describe an "$8,000 AI Governance Assessment" and a $5,000-$10,000 tier labeled "AI Readiness Scorecard," which the website presents as free. Evidence: EV-004, EV-011, EV-022, EV-033, EV-034. Class: direct observation (index) + owner documentation. Confidence: high that the gap exists. Consequence: a buyer or an answer engine cannot locate or describe the primary offer; internal materials would misprice or misname it. Action: ISS-006 (owner decision on one name, scope, price, landing page; then PKG-ASSESS). Verification: after live crawl, one page title and one FAQ answer carry the offer name and price; Service schema validates on the live URL.

**F-02 | TRUTH | Scorecard method described two ways.**
Observation: indexed text for /scorecard says 15 questions, five categories, about 2 minutes, weighted risk score; other indexed text attributed to the same page says thirty questions, five per category, 1-5 scale, thresholds at 120 and 60. The second description is also arithmetically inconsistent with five categories. Evidence: EV-003, EV-014, EV-021. Class: direct observation (index) with uncertain attribution for the second description. Confidence: medium. Consequence: the secondary business goal's asset carries a visible method contradiction at the decision point; thresholds read as predictive claims without validation evidence. Action: ISS-005; publish one method statement and label thresholds as professional judgment. Verification: live page text and meta description agree; snippet updates after recrawl.

**F-03 | DISCOVERY/TRUTH | Stale and utility surfaces indexed.**
Observation: (a) five URLs on clearconciseconsulting.squarespace.com are indexed, including "FAQs 2" with pre-governance positioning and a "network" team description, an "/ai-services" page, and an old nonprofit path; (b) two non-www URLs (/services/salesforce-administration, /services/ad-hoc-support) are indexed with titles identical to the implementation and training pages; (c) /cart is indexed; (d) /new-clients and /who-we-help carry legacy positioning and default title patterns. Evidence: EV-011, EV-016, EV-022, EV-023, EV-025, EV-026, EV-002, EV-031. Class: direct observation (index). Confidence: high that these are indexed; response codes and canonicals unknown. Consequence: duplicate hosts and legacy pages feed outdated entity descriptions to search engines and AI retrievers, and dilute the one-host signal. Action: ISS-001, ISS-002, ISS-003, ISS-009. Verification: status codes and canonicals from the crawl; site: queries after recrawl.

**F-04 | ENTITY/DISCOVERY | Homepage indexed under two titles.**
Observation: "Salesforce Consultant NYC | 13x Certified Architect" and "Salesforce AI Governance & Architecture" both appear as the homepage title across queries. Owner docs also report a stale og:description. Evidence: EV-006, EV-014, EV-028, EV-032. Class: direct observation (index). Confidence: high on the split; cause unknown (recent change vs SEO-title/page-title difference). Consequence: the single most-cited entity statement about CCC is ambiguous between a local generalist and a governance specialist. Action: ISS-004 (one title, matching og tags, aligned to FACT-01 and the owner's decision on NYC, FACT-25). Verification: live title, og:title, og:description match; GSC shows one title.

**F-05 | TRUTH/ENTITY | Authority and outcome claims lack visible substantiation or permission notes.**
Observation: 13 certifications, teaching at NYU Tandon, 160+ students with about 80% placement, founding year 2018, five named organizations, a 40% cycle-time reduction, and anonymized governance narratives are all published as first-party statements. None carries a source, method note, or permission statement in observed text. Evidence: EV-005, EV-007, EV-011, EV-017, EV-023, EV-027, EV-015. Class: first-party statements; one third-party corroboration for publication (Salesforce Ben author page indexed). Confidence: high that the statements are published; unknown whether documentation exists offline. Consequence: these are the claims most likely to be checked by a procurement reviewer or quoted by an AI system; an unsupported one damages the whole set. Action: ISS-018, ISS-019, FACT-03 to FACT-07, FACT-21 to FACT-23 owner confirmations; add method notes; cite the published Salesforce Ben title (ISS-017). Verification: register entries move from HOLD to APPROVED with a source per fact.

**F-06 | ENTITY | Local entity claims without a verified customer-facing location.**
Observation: "NYC" appears in two indexed titles; BBB lists Brooklyn; LocalBusiness schema is deployed (owner-reported); clients named are national. Evidence: EV-006, EV-025, EV-032. Class: index + owner documentation. Confidence: medium. Consequence: an inaccurate LocalBusiness entity misdescribes the business; a local headline may undersell a national footprint. Action: ISS-015 (owner decision). Verification: deployed JSON-LD matches the approved entity model; Rich Results Test on live URL.

**F-07 | DISCOVERY | Two Trust Layer articles target near-identical intent.**
Observation: /blog/what-is-the-salesforce-einstein-trust-layer and /blog/salesforce-trust-layer-explained. Evidence: EV-008, EV-010, EV-015. Class: index; hypothesis of overlap based on titles. Confidence: medium. Consequence: possible internal competition; not proven. Action: ISS-011 (review bodies and GSC before deciding DIFFERENTIATE vs CONSOLIDATE). Verification: GSC query overlap over 8 weeks.

**F-08 | DISCOVERY | Mixed title patterns and owner style-rule violations in metadata.**
Observation: nine indexed pages still use the Squarespace default "Page — Clear Concise Consulting" pattern with an em dash; others use custom "|" titles. Titles include "Mastering" and "Tailored," words on the owner's forbidden list. Evidence: EV-002, EV-009, EV-024, EV-028. Confidence: high. Consequence: uneven snippet control; inconsistency with the owner's own quality rules. Action: ISS-010, ISS-020 (drafts in implementation/metadata-drafts.md). Verification: crawl shows custom titles on all indexed pages.

**F-09 | CONVERSION | Intake path and contact identity are described inconsistently.**
Observation: "15-minute call" and "free 30-minute consultation" both appear; three public email addresses appear across surfaces; two Gumroad handles. Evidence: EV-016, EV-022, EV-026, EV-005, EV-024. Confidence: high on the text; medium on whether these are distinct offers. Consequence: small decision friction at CTAs; multiple contact facts for entity resolution. Action: ISS-007, ISS-008, ISS-022. Verification: consistent CTA labels and one address in live HTML and schema.

**F-10 | MEASUREMENT | No baseline is available.**
Observation: no analytics, Search Console, form, or scorecard data was provided or accessible. Consequence: no claim of improvement from any change can be supported later. Action: ISS-026 and MEASUREMENT-AND-ROADMAP.md before publishing changes.

**F-11 | ALL | Owner-reported open items not yet deployed (as of May 2026 documentation).**
Observation: blog index H1 fix drafted, three 301 redirects confirmed, og:description stale, CaseStudy and HowTo schema pending, internal linking not started. Evidence: EV-032. Class: owner documentation; not observed this run. Action: ISS-012, ISS-013, ISS-014; internal-linking items folded into QUERY-PAGE-MAP.csv. Verification: live crawl.

## 6. Layer summaries

**TRUTH.** 44 claims inventoried. 11 NO_CONFLICT_FOUND; 6 POTENTIALLY_OUTDATED (all on legacy or third-party surfaces); 3 GENUINE_CONTRADICTION candidates (scorecard method; paid-tier name vs free scorecard); 6 DIFFERENT_OFFER_OR_SCOPE (price differences that describe different services and are not contradictions); 9 AMBIGUOUS; 4 UNSUPPORTED. Different prices for implementation, workshops, retainers, and advisory were checked in context and are compatible. The one price question that matters commercially is which assessment costs what (F-01).

**ENTITY.** The Person and Organization are consistently named and well linked externally (LinkedIn, Salesforce Ben, Medium, Salesforce Break, GitHub, BBB). Gaps: no Wikipedia/Wikidata presence (expected for a solo practice; do not manufacture one), no review-platform or AppExchange listing surfaced (EV-020; absence in results is not proof of absence), sameAs parity unverifiable until the crawl, LocalBusiness type questionable (F-06).

**DISCOVERY.** The domain is indexed with a healthy spread of governance and data-quality articles, and the pre-Agentforce checklist article already appears alongside Perficient, Soliant, Demand Chain, Acxiom, and Girikon for AI-readiness queries (EV-019, EV-030). The problems are hygiene, not absence: duplicate hosts, utility pages, legacy pages, mixed titles, and a missing or unnamed landing page for the paid offer. Crawler access for AI retrieval bots is unknown (ISS-024); do not permit training-only crawlers just to satisfy a score.

**CONVERSION.** Observable path: article or search -> /scorecard (free) -> 15-minute results call, or -> /contact / scheduler -> free consultation -> fixed-price scoping. High-intent visitors have a direct route (contact and scheduler), which is correct; the route lacks a named assessment destination. Friction items are hypotheses until analytics exist: duration ambiguity, unnamed offer, three contact addresses. See MEASUREMENT-AND-ROADMAP.md section 3 for the funnel table.

## 7. Competitive context (snippet-level only; pages not fetched)

Observed competing pages for AI-readiness intent: Soliant, Acxiom, Demand Chain, Girikon, Perficient (solution-sheet PDF), Launch Consulting, Centric, Cyntexa, Clientell (EV-004, EV-019, EV-030). Observable differences from snippets: competitors present the assessment as a named productized offer with a deliverables list (maturity scorecard, gap analysis, 90-day roadmap) and a duration (4-6 weeks); several lead with firm scale ("500+ experts"). CCC's differentiators visible in its own snippets: named architect leading every engagement, fixed pricing published, four regulated verticals, published editorial policy, open-source tools, and Salesforce Ben authorship. What CCC lacks in the index relative to these pages is a named assessment page with deliverables and duration (F-01). No inference is made about competitor traffic, conversions, or authority.

## 8. No-change decisions

- Security headers (CSP, Permissions-Policy, Referrer-Policy): platform-controlled on Squarespace; Cloudflare proxy breaks SSL termination (owner-documented). No change.
- Lighthouse performance (owner-reported 54/100): platform-controlled. No change beyond image hygiene, which cannot be assessed without HTML.
- robots.txt direct edits: not possible on Squarespace. Crawler toggle to be verified (ISS-024).
- Pardot and recruiter-series articles: outside current positioning but useful and distinct. Keep; no commercial CTAs added.
- Career-changer resources: separate audience; keep isolated from buyer paths.
- /about title: already descriptive and custom. No change.
- llms.txt: optional experiment; verify content only (ISS-023). No ranking claim.
- FAQPage schema: valid to keep for machine readability; do not expect FAQ rich results for a consulting site under Google's 2023 restriction (verify against current documentation; host blocked this run).

## 9. Limitations and checks not completed

- All live-site checks: HTTP status codes, redirects, canonicals, meta robots, X-Robots-Tag, titles and descriptions as served, H1s, JSON-LD as deployed, internal links, images, mobile rendering, Core Web Vitals (lab or field), accessibility of forms and CTAs, robots.txt, sitemap.xml, llms.txt, AI-crawler access.
- Third-party corroboration fetches: Salesforce Ben, Salesforce Break, Medium, NYU program page, BBB (hosts blocked).
- Primary-source verification of structured-data requirements (developers.google.com, schema.org blocked).
- Competitor page content (hosts blocked).
- Analytics, Search Console, form, and scorecard data (not provided).
- Brand mention scanning (toolkit brand_scanner.py) and llms.txt validation (toolkit script) not executed: both require outbound fetches to blocked or unverified hosts.
- Snippet text is tool-generated and may blend sources; where attribution mattered (F-02) it is flagged.

## 10. Priorities

P0: ISS-000 (audit prerequisite: allow the host and run the crawler). No P0 site defects can be verified without it.
P1: ISS-006 offer architecture; ISS-005 scorecard method; ISS-004 homepage title/og; ISS-001 built-in domain; ISS-002 non-www duplicates; ISS-003 cart indexed; ISS-018 client-name permissions; ISS-026 instrumentation.
P2: ISS-007 to ISS-016, ISS-019.
P3: ISS-017, ISS-020 to ISS-024.
Sequencing and owners: MEASUREMENT-AND-ROADMAP.md section 6.

## 11. Deliverables in this workspace

URL-INVENTORY.csv, BUSINESS-CLAIMS-INVENTORY.csv, CANONICAL-BUSINESS-FACTS.md, ENTITY-MAP.md, QUERY-PAGE-MAP.csv, PRIORITIZED-BACKLOG.csv, PAGE-IMPROVEMENTS.md, MEASUREMENT-AND-ROADMAP.md, implementation/, evidence/, RUN-STATUS.md.
