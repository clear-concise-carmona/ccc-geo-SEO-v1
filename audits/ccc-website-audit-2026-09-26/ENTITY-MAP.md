# Entity Map: Clear Concise Consulting

Workspace: ccc-website-audit-2026-09-26 | Evidence basis: deployed JSON-LD and page content fetched 2026-09-27 (EV-038), HEAD probes (EV-039, EV-043), the 2026-09-26 index sample (EV-002 to EV-031), one direct GitHub fetch (EV-007), owner strategy documents (EV-032 to EV-035).

## 1. Core entities (as deployed)

| Entity | Type deployed | @id deployed | Observed names | Status |
|---|---|---|---|---|
| Clear Concise Consulting | Organization + ProfessionalService (custom block, every page); Organization and LocalBusiness (Squarespace-native blocks, every page); WebSite (native) | https://www.clearconciseconsulting.com/#organization (custom block); native blocks have no @id | "Clear Concise Consulting", "CCC", "Clear Concise Consulting, LLC" (footer), "Clear Concise Consulting LLC" (BBB) | Three organization descriptions per page (F-06, F-12). Use one. LocalBusiness only if a customer-facing location and real hours are confirmed (FACT-25) |
| Jeremy Carmona | Person (/about), referenced as founder from the custom Organization block; mainEntity of an AboutPage node | https://www.clearconciseconsulting.com/about#jeremy-carmona | "Jeremy Carmona", "Jeremy A. Carmona" (LinkedIn slug), jobTitle "Salesforce Architect and Founder" | Consistent. The pass-1 proposal of /about#person is withdrawn; drafts now use the deployed @id |

## 2. Deployed structured data inventory (EV-038)

| Block | Where | Key properties observed | Notes |
|---|---|---|---|
| WebSite (native) | every page | url, name, empty description, logo image | fine |
| Organization (native) | every page | address "228 Park Avenue South, New York, NY, 10003", telephone, email j.carmona@, sameAs x6 (Medium, LinkedIn company, GitHub, Instagram, Facebook, YouTube) | derives from Squarespace Business Information; duplicates the custom block with a different sameAs set |
| LocalBusiness (native) | every page | address, image, openingHours "Mo 08:00-17:00, Tu 08:00-17:00, We 08:00-17:00, Th 08:00-17:00, Fr 08:00-17:00, , " | trailing empty items; hours unverified; decision FACT-25 |
| Organization + ProfessionalService (custom) | every page | @id #organization, url, description, telephone, PostalAddress (streetAddress "228 Park Ave S #871721"), founder -> /about#jeremy-carmona, sameAs x7 (LinkedIn company, GitHub, Instagram, Facebook, YouTube, Medium, Gumroad) | the block to keep; reconcile sameAs |
| FAQPage | /, /faqs (27 questions), /services/data-governance, three Headless 360 posts, Pardot beginners post | on / the block appears twice, identical | remove one source on / (ISS-028) |
| Service | four service pages and the assessment page | assessment: @id .../salesforce-ai-data-readiness-assessment#service, name "Salesforce AI Data Readiness Assessment", serviceType, provider -> #organization, areaServed "United States", no offers | offers block only after FACT-15 |
| BreadcrumbList | /services/data-governance, /services/salesforce-implementation, /services/salesforce-training, /services/salesforce-nonprofit-consulting | | missing on the assessment page and case study |
| Person + AboutPage | /about | Person sameAs x4 (LinkedIn personal, Trailblazer salesforce.com/trailblazer/jeremy-carmona, Medium, Salesforce Ben author); AboutPage mainEntity -> Person | good; extend sameAs to the agreed set |
| Article | all 26 fetched posts | author "Jeremy Carmona", datePublished, dateModified, publisher, image on every post | complete; BlogPosting duplicated on 3 posts |
| CaseStudy | /case-studies/enterprise | | not a schema.org type (schema.org/CaseStudy returns 404, EV-043); use Article |
| HowTo | /blog/salesforce-validation-rules-guide | | valid type; rich result retired; harmless |

## 3. Verified relationships (observed on the live site and at least one independent or linked surface)

| Relationship | Evidence | Confidence |
|---|---|---|
| Jeremy Carmona founded and leads Clear Concise Consulting | / and /about text; custom Organization founder property; EV-007; EV-025 | high |
| Jeremy Carmona is the author of Salesforce Ben articles | /about links three salesforceben.com URLs and displays the published title of one; author page indexed (EV-005, EV-018); article pages not read (origin 403) | high |
| Jeremy Carmona publishes on Medium (@jcarmona86) | linked from /about, native and custom sameAs, Person sameAs; indexed | high |
| Clear Concise Consulting maintains open-source Salesforce tools on GitHub (clear-concise-carmona) | linked from / and /about; sameAs; EV-007 direct fetch | high |
| LinkedIn company page and personal profile | company page linked from / and /about and in sameAs; personal profile in Person sameAs and llms.txt | high |
| Trailhead credential profile | "Verify on Trailhead" link on /about; Person sameAs; llms.txt (different URL form) | high that it is linked; credentials not read (host not allowlisted) |
| Instagram, Facebook, YouTube, Gumroad accounts | deployed in native and custom sameAs (EV-038) | owner-asserted; not fetched |
| BBB profile (Brooklyn, NY) | indexed (EV-025); not linked from the site | medium |

## 4. First-party-only relationships (published by CCC; independent corroboration not obtained)

| Relationship | Where published | What would corroborate |
|---|---|---|
| 13 Salesforce certifications (three tracks listed) | /about, / | the Trailhead page linked from /about |
| Taught Salesforce Administration at NYU Tandon; 160+ students; 80% placement | /about, /services | NYU listing; cohort records; placement method |
| Work involving USCIS, EDF, UnitedHealth Group, HRSA, NYU; GovCloud implementation for USCIS in 8 weeks | /services, /faqs (text and schema), /who-we-help | owner documentation of relationship type and permission |
| Testimonial from a named USCIS staff member | /contact, /about | written permission |
| Enterprise CPQ engagement (40% across 30 regions) | /case-studies/enterprise H1 | client confirmation or measurement note |
| Founded 2018 | footer copyright line | registration record |

## 5. Public profiles for sameAs (target list)

Deployed today in three different arrays (EV-038):
- Native Organization (6): Medium, LinkedIn company, GitHub, Instagram (clearconcisecarmona), Facebook (profile.php?id=61565894325721), YouTube (@clearconciseconsulting)
- Custom Organization (7): the six above plus https://jeremycarmona.gumroad.com/
- Person on /about (4): https://www.linkedin.com/in/jeremy-a-carmona/, https://www.salesforce.com/trailblazer/jeremy-carmona, Medium, https://www.salesforceben.com/author/jeremy-carmona/

Also in /llms.txt: LinkedIn company with a trailing slash, https://trailblazer.me/id/jcarmona86, Instagram (rubberduckconfessions).

Target (implementation/jsonld/sameas-target-list.json): one combined array on every block. Core set (verified as indexed or directly fetched, and deployed): LinkedIn personal, LinkedIn company, Salesforce Ben author, Medium, Salesforce Break author (indexed, EV-005; not deployed today), GitHub. Owner-deployed set to carry over once one URL form is chosen for each: Instagram (business account), YouTube, Facebook, Gumroad, Trailblazer. Exclude the personal-brand Instagram from the Organization and Person blocks unless the owner wants it as an identity anchor; exclude BBB unless wanted.

Owner rule (EV-032): every deployed sameAs array must be identical. Today they are not. History (Confluence 147095553, EV-045): in April 2026 the Person block carried 7 entries (with GitHub, X/Twitter, Salesforce Ben) and the Organization 6 (with X/Twitter), both validated in the Rich Results Test; the live arrays have regressed (no X anywhere, no GitHub on the Person). Gumroad: the Product Roadmap (178028545) records the CCC-named storefront as a 404 and jeremycarmona.gumroad.com as live; Decision P1 is open.

## 6. Inconsistencies and gaps (live)

| Item | Detail | Related |
|---|---|---|
| Three organization blocks per page | native Organization, native LocalBusiness, custom Organization+ProfessionalService, with two address formats and three sameAs sets | ISS-015, ISS-016, ISS-028 |
| Local entity | LocalBusiness with weekday hours and a suite-numbered Park Avenue South address; national client footprint | FACT-25, CLM-052 |
| Offer price | $9,500 (assessment page) vs $8,000 (/services, owner docs) vs FAQ that prices only the $5,000 data quality assessment | FACT-15, ISS-006 |
| Trust Test | appears on one page only | FACT-28 |
| Positioning drift | /who-we-help (Small Business, career changers, "Tailored"); /llms.txt (omits healthcare and enterprise); mirror host FAQ ("growing businesses", per index) | CLM-030, CLM-051, ISS-009, ISS-023, ISS-001 |
| Contact identity | five email addresses; three scheduler paths; two Trailblazer URL forms; two Gumroad URL forms; X/Twitter present in April 2026 arrays, absent today | FACT-24, FACT-27 |
| Client attribution | live pages attribute USCIS, EDF, UnitedHealth Group, HRSA, and NYU work to CCC; the Client Roster lists none of them and the resume lists them as Jeremy's career experience (EV-045) | FACT-22, ISS-018 |
| Teaching tense | past-tense prose, present-tense heading and tile | FACT-05 |
| Duplicate schema | FAQPage twice on /; Article + BlogPosting on 3 posts; invalid CaseStudy | ISS-028 |
| Headings | numeric-only H2 tiles on / and /about; 21 H1s on /blog; 2 H1s on the security guide; H1 typo on the nonprofit page | ISS-037, ISS-012, ISS-034 |

## 7. Internal-linking and structured-data opportunities (all targets live)

- Every blog byline ("Written By Jeremy Carmona") -> /about; /about -> /policies-commitments (editorial policy, FACT-20).
- /blog/salesforce-ai-data-readiness-checklist, /blog/six-governance-checkpoints-engagement, /blog/ai-reversibility-rollback-plan -> /salesforce-ai-data-readiness-assessment as in-copy text links (today the assessment is reachable from these posts only through the header button).
- /blog/salesforce-validation-rules-guide, /blog/salesforce-duplicate-management-guide, /blog/salesforce-org-health-roadmap -> /services/data-governance.
- /faqs -> /salesforce-ai-data-readiness-assessment from a new price answer (ISS-006).
- /about -> the Salesforce Ben author page (today three article links, no author page link).
- Person schema: keep jobTitle and worksFor; extend sameAs to the agreed array; knowsAbout limited to published topics (AI governance, data governance, Salesforce data quality, Nonprofit Cloud); no awards or affiliations that are not on the page.
- Organization schema: one block; founder -> /about#jeremy-carmona; agreed sameAs; contactPoint with the chosen address (FACT-24); PostalAddress and LocalBusiness only per FACT-25; no aggregateRating, no review markup, no areaServed beyond the verified footprint (the deployed Service uses "United States", which is defensible).
- BreadcrumbList on the assessment page and the case study to match the four service pages.

## 8. Cautions

- Do not infer a customer-facing office from the published address, the BBB listing, or the native LocalBusiness block.
- Do not add Wikipedia or Wikidata sameAs entries: none exist for CCC or Jeremy Carmona in observed results, and creating them is out of scope.
- Do not present the toolkit's or SEOmator's heuristic scores as evidence of AI visibility.
- Client-side suppression scripts do not change what crawlers receive; validate the raw HTML.
