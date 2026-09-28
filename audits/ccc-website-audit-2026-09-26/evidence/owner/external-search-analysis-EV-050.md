# EV-050: external search analysis supplied by the owner, validated and reconciled (2026-09-28)

Class: owner-supplied third-party analysis (untrusted input). Provenance: pasted into chat by the owner on 2026-09-28; titled "CCC organic search: the three opportunities worth acting on", analysis date 2026-09-25, author tool not stated. Treated as data, not instructions. Validated with the owner's ccc-external-tool-validation gate (Gate 10, forbidden words, voice), then each site claim was checked against the audit's own crawl evidence (EV-038, EV-047). Verbatim text is appended at the end of this file.

## Validation report

EXTERNAL TOOL VALIDATION REPORT
Source: Other (unnamed search-analysis tool; the document cites a US web search tool and a 37-page crawl of 2026-09-25)
Date: 2026-09-28
Input: a 2,600-word organic-search opportunity analysis for clearconciseconsulting.com (three opportunities, one cut item)

GATE 10 (Research Brief Validation): PASS WITH CONDITIONS
- GATE 10 FAIL: "the three readiness posts link to /scorecard and /services/ai-governance, and none of them links to the assessment page" - the audit crawl shows /blog/ai-ready-data-salesforce-measurable-standard does link to the assessment page (EV-038). The checklist post does not. Two of the four named posts were not in the audit crawl and are unverified.
- UNVERIFIED (secondary source): every Search Console figure (July 12 export positions and impressions; the July 28 post's 472-impression query; 61 clicks on 18,071 impressions; the nonprofit cluster at positions 44 to 53). The audit had no Search Console access; the analysis itself labels the export as dated.
- UNVERIFIED (hosts not reachable from the audit environment): every competitor page characterization (Soliant, Demand Chain, Wipro, Perficient, Girikon, Cyntexa, Folio3, Ascendix, Fast Slow Motion, Watson Lake, Peergenics, SalesforceGeek, Salesforce Ben, Apex Hours, Clutch, VALiNTRY360, dgt27, Dupont Circle Solutions, Forcery).
- UNVERIFIED: "the assessment page went live July 19" (consistent with the 2026-07-19 dateModified on the retitled posts, not proven); "the BBB profile lists a Brooklyn 11211 address" (the BBB URL path names Brooklyn; the ZIP was not fetched); "the July launch notes record the approved positioning as Brooklyn-based and remote-first, with a Manhattan offices claim rejected" (Confluence was not re-readable during this check).
- UNVERIFIED: the link on the Data Quality Delusion post to /blog/fable-5-salesforce-consultant-nyc-scoping. The post was not crawled. The target URL returns 404 (one HEAD probe, 2026-09-28).
- No product presented as GA without basis; no deadlines; no beta claims. The "Essentials" naming point is plausible (Salesforce retired the Essentials edition name in favor of Starter) but should go through the salesforce-fact-check gate before the post is edited.

FORBIDDEN WORDS: PASS
- 0 violations found (167-word list, whole-word and phrase matches).

VOICE COMPLIANCE: N/A (internal analysis, not publication copy). Incidentally clean: no em dashes, no conjunction openers.

URGENCY CHECK: No urgent items (not a Monthly Ops Review).

OVERALL: PASS WITH CONDITIONS
- Correct the one factual error (the measurable-standard post already links to the assessment page) before the link pass is scoped.
- Treat every ranking and impression figure as a July snapshot until a fresh Search Console export replaces it.
- Two of its recommendations conflict with decisions already recorded in this audit (see reconciliation, rows R2 and R7).

## Claim-by-claim check against the audit crawl

| # | Claim in the analysis | Audit evidence | Verdict |
|---|---|---|---|
| C1 | Readiness checklist post links to /scorecard and /services/ai-governance, not to the assessment page | EV-038: 13 internal links; /scorecard yes; /services/ai-governance yes; assessment no | Confirmed |
| C2 | None of the readiness posts links to the assessment page | EV-038: /blog/ai-ready-data-salesforce-measurable-standard links to it; agentic-readiness-audit and agentforce-data-governance not crawled | Contradicted for one post; two unverified |
| C3 | /services/ai-governance body links go to the Trust Layer post, /contact, and three PDFs, not the assessment page | EV-047: internal links are the Trust Layer post, /cart, /contact, three /s/*.pdf files; no assessment link | Confirmed |
| C4 | /scorecard wrapper has zero body links | EV-038: one internal link (/cart, commerce chrome) | Confirmed in substance |
| C5 | Assessment H1 is the hook; the title carries the offer name | EV-047: H1 "AI Does Not Fix a Messy Salesforce Org. It Exposes It."; title "Salesforce AI Data Readiness Assessment \| Clear Concise Consulting" | Confirmed |
| C6 | Body links to the assessment page exist on /, /ai-center-of-excellence, trust-layer-explained, org-health-roadmap | EV-038, EV-047: all four true; /org-health has none | Confirmed |
| C7 | Cost, timeline, and Einstein Trust Layer posts: zero tables, no FAQPage, no visible updated label; dateModified July or August 2026; 1,000 to 1,500 words | EV-038: 0, 0, 0 tables; Article only; dateModified 2026-07-19, 2026-07-19, 2026-08-30; 1,096, 1,027, 1,489 words; no "Updated <Month> <Year>" text | Confirmed (visible date format not checked) |
| C8 | The timeline post links to no service page | EV-038: no /services link | Confirmed |
| C9 | The cost post still cites "Essentials" | EV-038: one occurrence; zero "Starter Suite" | Confirmed |
| C10 | Homepage body has zero mentions of New York, NYC, Brooklyn, Manhattan | EV-038: 0, 0, 0, 0 | Confirmed |
| C11 | The only NYC mention is the training page meta description | EV-038: "... NYC and remote." on /services/salesforce-training | Confirmed for that page; site-wide exclusivity not checked |
| C12 | Schema carries a Squarespace LocalBusiness block with the Park Avenue South address and weekday hours | EV-038, EV-047: on every crawled page (audit F-06) | Confirmed |
| C13 | /blog/fable-5-salesforce-consultant-nyc-scoping returns 404 | HEAD 2026-09-28: 404 | Confirmed (link source unverified) |

## Reconciliation with the audit's decisions and backlog

| # | Analysis recommendation | Audit position | Result |
|---|---|---|---|
| R1 | Link pass to the assessment page from the readiness posts, both assessment H2 sections on /services/ai-governance, the /scorecard wrapper, and /org-health | Not previously in the backlog; consistent with F-17 (thin conversion wrappers) and the query map's assessment row | Added as ISS-043 |
| R2 | Proof block on the assessment page using the nonprofit case-study metrics | ISS-040: those figures match the Environmental Defense Fund work that canon classes as career experience; attribution and labels are owner-supplied and still open | Accepted only after ISS-040 clears; noted on ISS-043 |
| R3 | Rewrite the assessment H1 to lead with the offer name, hook as second clause | PAGE-IMPROVEMENTS.md PKG-ASSESS left the H1 open (keep or question form) | Added as ISS-044; the analysis's option is now the recommended one |
| R4 | Rebuild the cost, timeline, and Trust Layer posts (tables, FAQ with FAQPage schema, visible updated date, current edition names, service links); merge the sibling Trust Layer post | ISS-011 already holds the Trust Layer merge pending Search Console data; the post rebuilds are new. Caveat from EV-043: Google shows FAQ rich results only for government and health sites, so FAQPage on these posts serves AI answer extraction, not a rich result | Added as ISS-045 |
| R5 | Repair or remove the 404 link on the Data Quality Delusion post | New | Added as ISS-046 (source unverified, target confirmed) |
| R6 | New NYC landing page, links from /about, /services, /who-we-help, footer; Google Business Profile as a service-area business with the address hidden | The query map already carries "Salesforce consultant NYC / New York" with no target page; decision 3 (EV-048) settled LocalBusiness removal but not the address of record | Added as ISS-047, OWNER_DECISION_REQUIRED |
| R7 | Suppress the Squarespace LocalBusiness block with the footer script | F-06 and ISS-015: client-side suppression removes nothing from the HTML crawlers read; the decided method is Business Information (clear hours) plus the custom block | Rejected as method; goal already covered by ISS-015 |
| R8 | NAP conflict: schema and footer say Park Avenue South 10003, BBB says Brooklyn 11211, page copy says nothing | FACT-25 and assumption A8 (mailing-address hypothesis) | New evidence recorded on FACT-25; the address of record is added to the owner-supplied list |
| R9 | Nonprofit cluster cut for off-site authority reasons | Consistent with the audit's no-change stance on the nonprofit page beyond the intake-call and attribution edits | No change |
| R10 | Pull a fresh Search Console export before content work | ISS-026 baseline export | Already required; the analysis strengthens the case |

## Verbatim text as supplied

# CCC organic search: the three opportunities worth acting on

Analysis date: September 25, 2026. Site: https://www.clearconciseconsulting.com (substituted for the aliensofbrooklyn.com placeholder in the prompt).

## Summary

**The business.** Clear Concise Consulting is a one-architect Salesforce consultancy. The live site sells five services (implementation, AI governance, data governance and migration, training, ongoing administration), a paid Salesforce AI Data Readiness Assessment starting at $9,500, a free AI Readiness Scorecard, and a library of roughly 80 blog guides. Target customers are nonprofit, government, healthcare, and enterprise organizations. Geography: the schema on every page lists a New York, NY address, the BBB lists Brooklyn, and the page copy names no location at all. Engagements are remote-first.

**The search market.** Three query families matter: commercial AI-readiness queries (assessment, checklist, Agentforce readiness), high-volume informational Salesforce queries the blog already earns impressions for (implementation cost, timeline, Einstein Trust Layer), and local commercial queries ("Salesforce consultant NYC") that the project brief names as a target.

**Limitations.** No live Search Console, analytics, or paid keyword tool access. Ranking and impression figures come from two dated sources: the July 12, 2026 GSC export recorded in project notes, and the figures Jeremy published in The AI Queries in My Search Console (90-day window, 19,483 impressions). Search-tool samples below come from a US web search tool on September 25 and are not Google rankings; absence from a sample is not proof of not ranking. Keyword volumes and difficulty scores are unavailable. Two competitor fetches failed (Sailwayz, Kelley Austin) and are not characterized. Site observations come from a sequential crawl of 37 pages on September 25. One standing caveat: the July 9 GSC notes showed 29 URLs never crawled and a crawl rate near 6 to 7 requests per day. The July 18 indexing sprint targeted that; current coverage is unverified and should be re-pulled before any content work, since an unindexed post cannot rank.

## Opportunity 1: Make the assessment page the site's one answer for AI-readiness queries

**Opportunity:** Consolidate internal signals around https://www.clearconciseconsulting.com/salesforce-ai-data-readiness-assessment. Affected existing URLs: /services/ai-governance, /scorecard, /ai-center-of-excellence, and the readiness posts salesforce-ai-data-readiness-checklist, salesforce-agentic-readiness-audit, salesforce-agentforce-data-governance, and ai-ready-data-salesforce-measurable-standard. No new page.

**Evidence.** Target queries: "salesforce ai readiness assessment", "agentforce readiness assessment", "salesforce ai readiness checklist", "agentforce data readiness", "is my salesforce org ready for agentforce". Intent is commercial-investigational: a buyer deciding whether to turn on AI and looking for someone to check the org first.

Ranking: the July 12 GSC export (project notes) put AI-readiness-assessment queries at average positions 17 to 23, page two. The assessment page went live July 19, so those impressions were earned by the blog posts and service page; the page's own query data has not been pulled since.

Search-tool samples (September 25, six queries): CCC appeared twice, both times via the blog checklist post (ninth of nine for "salesforce ai readiness assessment" and for "salesforce ai readiness checklist"). The assessment page did not appear in any sample. Verified, and consistent with the blog post being the entry point for this intent.

Site gap (verified by crawl): the three readiness posts link to /scorecard and /services/ai-governance, and none of them links to the assessment page. /services/ai-governance carries the H2s "How CCC's AI Governance Assessment Works" and "What Gets Measured in an AI Readiness Assessment", yet its body links go to the Trust Layer post, /contact, and three PDFs, not to the page that sells the assessment. The /scorecard Squarespace wrapper has zero body links (the iframe widget was not inspected). Body-content links to the assessment page exist on the homepage, /ai-center-of-excellence, the trust-layer-explained post, and the org-health-roadmap post, plus the header nav. The page's H1 is a hook ("AI Does Not Fix a Messy Salesforce Org. It Exposes It.") with none of the query language; the title tag does carry it.

Competitor pages (fetched September 25): Soliant (about 2,300 words, "Free AI Audit", no price, no FAQ), Demand Chain (a 200-word gated-paper page with no H1), Wipro (about 280 words, no price or duration), Perficient (redirects to a general partner hub; the companion blog is about 850 words), Girikon and Salesforce's own post (checklist blogs). No fetched competitor states a price; only Perficient states a duration. CCC's page states both, lists six named deliverables, ten FAQs, fit and not-fit criteria, and a credentialed author. What competitors have and CCC lacks: testimonials, client logos or case-study proof on the page, and a downloadable asset.

What the comparison shows: the page's substance already beats the field. The site is failing to tell search engines it is the primary page for this intent, and the page shows no proof.

**Why it matters.** This is the flagship $9,500 offer, the queries sat on page two before the page even existed, and the pages that do get surfaced (the checklist posts) are one link away from routing that demand. Internal linking is the cheapest ranking lever CCC controls, and the competing landing pages are thin. A page-two-to-page-one move on a commercial query is worth more than any informational traffic on the site.

**Concrete next action.** In one Squarespace session: add a contextual link with the anchor "Salesforce AI Data Readiness Assessment" inside the body of the four readiness posts, inside both assessment H2 sections on /services/ai-governance, in the /scorecard wrapper text ("what happens after the scorecard"), and on /org-health. Rewrite the assessment H1 to lead with the phrase and keep the hook as the second clause. Add a proof block using the nonprofit case-study metrics already published on /case-studies/nonprofit, subject to the launch-notes rule that unverified figures stay off the page. Then assign each overlapping page one job (checklist post = informational entry, assessment = commercial close, scorecard = lead capture) and, once GSC shows which URLs share queries, merge the agentic-readiness-audit post into the checklist post if they cannibalize.

**Impact, effort, and confidence.** Impact: high, relative to the site's other options, since it is the highest-value query family and the closest to page one. Effort: low, links, an H1, and a proof block, no new pages or development. Confidence: medium-high; the position data is from July and predates the page, so a fresh GSC pull for the page's own queries is the dependency, along with verified case-study numbers.

## Opportunity 2: Rebuild the three high-impression posts to the depth of the pages ranking around them

**Opportunity:** Expand and restructure how-much-does-a-salesforce-implementation-cost-in-2026, salesforce-implementation-timeline, and what-is-the-salesforce-einstein-trust-layer (plus a merge decision on its sibling salesforce-trust-layer-explained). Existing URLs only.

**Evidence.** Target queries: "salesforce implementation cost", "how much does a salesforce implementation cost", "how long does a salesforce implementation take", "einstein trust layer", "what is the einstein trust layer". Intent is informational, with buyer overlap on the cost and timeline queries.

Ranking: the July 12 GSC export (project notes) recorded 2,755 impressions for the cost post, 2,501 for the Trust Layer post, 1,737 for the validation-rules post, and 957 for the timeline post with zero clicks, all at average positions 6 to 11; site-wide, 61 clicks on 18,071 impressions (0.34% CTR). Jeremy's July 28 post reports one Trust Layer query at 472 impressions, average position 2.97, zero clicks, which reads as an AI Overview or answer box absorbing the click (inference).

Search-tool samples (September 25): the cost post appeared eighth or ninth for "how much does a salesforce implementation cost" and "salesforce implementation cost 2026", and was absent for "salesforce implementation cost small business"; the timeline post appeared seventh for "how long does a salesforce implementation take"; the Trust Layer post appeared ninth for "what is the einstein trust layer" and "einstein trust layer explained". The sample still shows the cost post's pre-July title ("Salesforce Implementation Cost Guide 2026"), not the live "$15K to $150K Breakdown" tag: either a stale crawl or engine rewriting, unverified either way.

Site gap (verified by crawl): all three posts have zero HTML tables, no FAQ block or FAQPage schema, a visible date with no year ("Apr 7", "Apr 14", "Apr 13") and no visible "updated" label; the schema dateModified reads July or August 2026, so the refresh is invisible to readers. The timeline post links to no service page. Body copy runs roughly 1,000 to 1,500 words each.

Competitor pages (fetched September 25): for cost, Cyntexa (about 7,500 words, three tables, license-versus-implementation split, regional hourly rates, five FAQs, modified July or August 2026), Folio3 (about 4,500 words, five tables, 18 FAQs, modified July 30, 2026), Ascendix (five tables, e-books, title still says 2025), and Fast Slow Motion (about 1,900 words, closest in shape to CCC). For timeline, Watson Lake has a project-type table and a week-by-week 14-week grid with six FAQs; Peergenics uses size-based case timelines and five FAQs. For the Trust Layer, SalesforceGeek runs one H2 per component including zero-data retention and toxicity scoring, with diagrams and FAQs; Salesforce Ben embeds video; Apex Hours uses the official architecture diagram. Three of four cost competitors use current edition names (Starter Suite, Pro Suite, Enterprise, Unlimited, Agentforce 1); CCC's post still cites "Essentials".

What the comparison shows: the pages around CCC win on format and completeness (tables, FAQs, current dates, diagrams), not on credentials. CCC's distinctive material (a first-party rate card, the solo-architect versus firm comparison, the "what it misses" governance critique) is something no competitor publishes.

**Why it matters.** This is the largest impression pool on the site, roughly 8,000 impressions across four posts in three months, producing almost no clicks. Positions 6 to 11 sit below AI Overviews, ads, and three or four organic results; the July title rewrites addressed the snippet but not the reason the posts sit there. CCC already holds page-one placement in the samples, so this is a top-five push, not a cold start.

**Concrete next action.** Start with the cost post. Add a license-by-edition table using current Salesforce naming, a cost-by-scope table (the $15K, $40K, $75K, $100K+ tiers already in the prose), a license-versus-implementation-versus-ongoing split, a five-question FAQ block with FAQPage schema (fair price, hidden costs, solo architect versus firm, nonprofit pricing, timeline), a visible "Updated September 2026", and contextual links to /services/salesforce-implementation and the assessment page. Repeat for the timeline post (project-type table, week-by-week grid, a hypercare section, FAQ, link to the implementation service) and the Trust Layer post (one H2 per component including zero-data retention and toxicity detection, one diagram, FAQ, and execute the merge of the sibling post that the July notes already recommended).

**Impact, effort, and confidence.** Impact: medium-high; the demand is proven by impressions, and the query intent is adjacent to buying. Effort: medium, content and formatting work in Squarespace, no development. Confidence: medium; positions are from July, and AI Overviews may cap CTR on the Trust Layer queries regardless of position. Dependency: a fresh GSC export to confirm positions after the July rewrites and to check which Trust Layer URL earns which queries.

## Opportunity 3: Build a New York City landing page and fix the local entity signals behind it

**Opportunity:** Proposed new page (for example /salesforce-consultant-nyc) plus a NAP cleanup. No existing page serves this intent: the live homepage title is "Salesforce AI Governance & Architecture" and its body contains zero mentions of New York, NYC, Brooklyn, or Manhattan (verified by crawl). The only NYC mention on the site is the training page meta description ("NYC and remote"). The search-tool sample still shows the homepage's pre-July title, "Salesforce Consultant NYC | 13x Certified Architect", meaning the July homepage rewrite dropped the site's only page targeting the term. A link on the Data Quality Delusion post points to /blog/fable-5-salesforce-consultant-nyc-scoping, which returns 404: a planned NYC piece that never shipped.

**Evidence.** Target queries: "salesforce consultant nyc", "salesforce consultant new york", "salesforce consulting firms nyc", "salesforce implementation partner new york", "salesforce nonprofit consultant nyc". Intent is local commercial: find a firm to hire.

Search-tool samples (September 25, five queries): CCC absent from all. Directories and job boards take most slots: Clutch's NYC list shows 84 companies with sponsored placements on top, and no firm smaller than 10 to 49 employees; GoodFirms, crm.consulting, forceperformers, Indeed, and LinkedIn Jobs fill the rest. The agency pages that do appear are templated city-swap pages: VALiNTRY360 is an Orlando-area firm with statewide boilerplate, dgt27 is in Maplewood, NJ, Dupont Circle Solutions is an Arlington, VA firm with a 600-word page, and only Forcery has a Manhattan address. None of the four names a borough or neighborhood, and none showed detectable LocalBusiness or FAQ schema. The "salesforce nonprofit consultant nyc" sample returned only national nonprofit specialists with no NYC-localized page.

Local entity signals (verified): the schema on every CCC page carries a Squarespace-generated LocalBusiness block with "228 Park Avenue South, New York, NY 10003" and Monday-to-Friday 8-to-5 opening hours, plus an Organization block with the same Park Ave S suite; the BBB profile lists a Brooklyn 11211 address; the July launch notes record the approved positioning as Brooklyn-based and remote-first, with a "Manhattan offices" claim rejected. The structured data, the BBB listing, and the page copy currently disagree with each other.

Unavailable: query volume, whether NYC queries already earn impressions in GSC, whether a Google Business Profile exists, and what the local pack shows.

**Why it matters.** Local commercial queries carry buying intent and the page-level competition is weak: out-of-state agencies with interchangeable copy and no local proof. CCC has local entity facts competitors cannot copy (NY LLC, BBB record, NYU Tandon teaching, an EDF start). A dedicated page also protects the homepage's AI-governance positioning instead of re-cramming NYC into it. It ranks third since volume and current rankings are unverified and the head terms are directory-heavy.

**Concrete next action.** First settle the NAP: if Brooklyn and remote-first is the position, suppress the Squarespace-generated LocalBusiness block (the July notes already describe the footer-script method) and make the Organization schema, BBB, and any GBP say the same thing, with areaServed set to New York City and remote. Then publish the page with: an H1 "Salesforce Consultant in New York City", who it serves (NYC nonprofits, healthcare, government, and enterprise teams), how engagements run (remote-first, on-site in the five boroughs when needed), local proof (NYU Tandon, EDF, any NYC clients that can be named), the five services with links to each service page and the assessment, and an FAQ (on-site availability, fixed-scope pricing, nonprofit fit, timeline). Link to it from /about, /services, /who-we-help, and the footer; repair or remove the 404 link. Register or verify a Google Business Profile as a service-area business with the address hidden (a mailbox suite is not eligible as a storefront) and point it at the new page.

**Impact, effort, and confidence.** Impact: medium, modest volume but highly qualified. Effort: medium, one page, schema cleanup, and a GBP. Confidence: medium-low, since no volume, impression, or local-pack data was available. Dependencies: GBP eligibility, the NAP decision, and a GSC check for existing NYC-query impressions.

## What did not make the cut

The nonprofit service page cluster (nonprofit money queries at positions 44 to 53 with about 840 impressions in the July export) is real demand, and /services/salesforce-nonprofit-consulting reaches most of the site only through footer links. It was cut since every sampled result for those queries ("salesforce nonprofit consultant", "npsp vs nonprofit cloud", "npsp to nonprofit cloud migration cost") was a national Salesforce.org partner or Salesforce Ben, and the June 6 Confluence lessons already name off-site authority as the binding constraint. On-site work alone will not move position 48 to page one.

## Do this first

Run the Opportunity 1 link pass. It takes one working session, needs no new content, no development, and no decisions from anyone else, and it applies to the query family closest to page one and closest to revenue. Pull a fresh GSC export the same day so Opportunities 2 and 3 start from current positions instead of July's.
