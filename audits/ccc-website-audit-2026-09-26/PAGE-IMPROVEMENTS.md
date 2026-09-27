# Page Improvement Packages

Workspace: ccc-website-audit-2026-09-26 | Status: the owner approved the strings and decisions on 2026-09-27 (EV-048); packages are READY_FOR_CMS_EDIT except where a line says the owner still supplies a fact (method texts, narrative labels). Nothing is published from this workspace. Live pages were read on 2026-09-27 (EV-038); each package now states what is already live and what remains.

Conventions:
- "Current (live 2026-09-27)" = the <title>, meta description, and H1 fetched from the live page (EV-038). The 2026-09-26 draft used search-index titles, several of which were stale; those values remain in evidence/search-results/ and are no longer quoted here.
- "Proposed" wording uses only APPROVED_FOR_DRAFT_USE or DECIDED facts; a bracketed note marks the few places where the owner still supplies a fact.
- Character counts are in implementation/metadata-drafts.md.
- No em dashes; owner's forbidden-word list respected in proposed copy.
- Page selection: homepage and the assessment offer page were required by the brief; /scorecard (secondary goal), /about (entity layer), and /faqs (truth layer, where prices and client names live) were selected from the evidence. Service pages for implementation and data governance were not selected; live checks found only a 164-character description on the implementation page and the $5,000 to $8,000 data quality table on data governance, which PKG-FAQS references.

---

## PKG-HOME: https://www.clearconciseconsulting.com/

**Audience:** first-time visitors from search or referral: operations, IT, and compliance leaders in nonprofit, healthcare, government, and enterprise organizations; some admins and recruiters.
**Search intent:** navigational (brand) and commercial ("Salesforce AI governance consulting", "Salesforce consultant NYC" per FACT-25 decision).
**Funnel role:** Discovery and Trust. Must answer in one screen: what CCC does, who does it, for whom, and the next step.
**Conversion goal:** primary, a qualified inquiry about the paid assessment or an engagement; secondary, a scorecard start.

**Current vs proposed metadata**

| Field | Current (live 2026-09-27) | Proposed |
|---|---|---|
| Title | "Salesforce AI Governance & Architecture" (39 characters; no brand name; og:title identical) (EV-038) | "Salesforce AI Governance Consulting \| Clear Concise Consulting" |
| Meta description | "Architect-led Salesforce AI readiness, data governance, and architecture for nonprofit, government, healthcare, and enterprise organizations." (141 characters; og:description identical) (EV-038) | No change. The live description already states FACT-01; the earlier proposal is withdrawn. |
| og:title / og:description | equal to the live title and description (EV-038); the owner-reported stale version (EV-032) is gone | follow the title change only |

Live structure (EV-038): H1 "Salesforce AI Governance and Architecture for Complex Organizations"; H2 stat tiles rendered as bare numbers ("13", "Since 2012", "NYU", "1"); H2s "Your Salesforce platform should make work clearer, not harder.", "Know What Salesforce AI Is Building On", "Salesforce Services Built Around Governance and Accountability", "Evidence Before Assumptions", "Why Clear Concise Consulting", "A Three Step Engagement Process", "Get a Clear View of Your Salesforce Risk"; buttons "REQUEST AN ASSESSMENT" -> /salesforce-ai-data-readiness-assessment and "TAKE THE FREE SCORECARD" -> /scorecard above the fold; FAQPage block present twice. Citability heuristic 39.9 (9 blocks, 3 graded F) (EV-042).

Note: the live description is kept. If the owner decides NYC is a target market (FACT-25), append "New York City" to the description, not the title. The numeric tiles should get metric-naming headings (ISS-037).

**Recommended H1 and heading structure**

- H1: "Salesforce AI governance for organizations that hold sensitive data"
- H2: "Who this is for" (four verticals, one sentence each, situation-based: an AI feature is planned or live and nobody has reviewed what data it touches)
- H2: "What Clear Concise Consulting does" (three items: AI governance and data readiness; data governance; implementation architecture)
- H2: "How an engagement starts" (free consultation, fixed-price scoping document, one architect end to end)
- H2: "Evidence" (one case metric with its method note, FACT-21 [owner supplies the note text]; one credential line FACT-03; one publication line FACT-06)
- H2: "Start here" (primary and secondary CTA)

**Targeted replacement copy (direct-answer passage, for the first section under the H1):**

"Clear Concise Consulting is a Salesforce consulting practice led by Jeremy Carmona, a Salesforce Architect who has worked on the platform since 2012. It provides AI governance and data readiness, data governance, and implementation architecture for nonprofit, government, healthcare, and enterprise organizations. Jeremy leads every engagement from scoping to go-live. Most projects are fixed price, set from a scoping document you approve before work begins, and every engagement begins with a free consultation."

(68 words. Uses FACT-01, FACT-02, FACT-04, FACT-08, FACT-09.)

**CTAs**
- Primary: live "REQUEST AN ASSESSMENT" -> /salesforce-ai-data-readiness-assessment is already the right destination and label; keep it (the offer name is confirmed, FACT-15).
- Secondary: live "TAKE THE FREE SCORECARD" -> /scorecard sits beside the primary above the fold. Acceptable. If assessment inquiries stay low after instrumentation, test moving it below the fold (EXP-1 family).

**Internal links (source -> destination, anchor)**
- / -> /salesforce-ai-data-readiness-assessment, anchor "Salesforce AI Data Readiness Assessment" (live as a button only; add one in-copy text link)
- / -> /scorecard, anchor "free AI Readiness Scorecard"
- / -> /about, anchor "Jeremy Carmona"
- / -> /services/data-governance, anchor "Salesforce data governance"
- / -> /blog/salesforce-ai-data-readiness-checklist, anchor "pre-Agentforce data checklist"
- / -> /case-studies/enterprise, anchor "enterprise CPQ case study" (metric wording pending FACT-21)

**JSON-LD (deployed, EV-038):** six blocks in the raw HTML: native WebSite; native Organization (address, telephone, j.carmona@ email, six sameAs); native LocalBusiness (address, opening hours Monday to Friday 08:00-17:00 with trailing empty items); FAQPage twice (identical); the custom Organization+ProfessionalService block (@id #organization, PostalAddress, founder -> /about#jeremy-carmona, seven sameAs). Actions: remove the duplicate FAQPage source (ISS-028); reconcile sameAs (ISS-016); remove LocalBusiness and the hours, keep the address (ISS-015, decided 2026-09-27); contactPoint contact@clearconciseconsulting.com (FACT-24, decided). Target: implementation/jsonld/organization-person.reconciliation.json.

**Evidence:** EV-038, EV-042, EV-006, EV-014, EV-028, EV-032, EV-033. **Unresolved:** FACT-21, FACT-25 (FACT-15 decided in canon: from $9,500; strings need owner approval). **Publication status:** APPROVED_BY_OWNER 2026-09-27 (EV-048); READY_FOR_CMS_EDIT (title change; the heading restructure is optional).

---

## PKG-ASSESS: https://www.clearconciseconsulting.com/salesforce-ai-data-readiness-assessment (live; the former /services/salesforce-ai-data-preparation URL 301s here)

**Precondition (revised 2026-09-27):** the page exists and carries the offer name in its title, Service schema, header navigation, and homepage CTA (EV-038). No URL change is needed. The open item is price: this page says "Starting at $9,500"; /services says $8,000 for "the governance assessment"; /faqs prices only a $5,000 data quality assessment and never names this offer. Confluence settles the price: the Positioning Canvas v2.2 (129826843, canonical) sets $9,500 and retires the $5,000 to $8,000 range, so the live page is correct and /services and /faqs are the pages to edit (EV-045). Price copy below is publishable once the owner approves the strings.

**Audience:** operations and IT leaders about to enable Agentforce, Einstein, or Data Cloud; compliance officers in healthcare and government.
**Search intent:** commercial ("Salesforce AI readiness assessment", "Agentforce data readiness assessment").
**Funnel role:** Appropriate next step for high-intent visitors; Education for mid-intent visitors arriving from the checklist article.
**Conversion goal:** assessment inquiry (form or scheduler).

**Current vs proposed metadata**

| Field | Current (live 2026-09-27) | Proposed |
|---|---|---|
| Title | "Salesforce AI Data Readiness Assessment \| Clear Concise Consulting" (66 characters) (EV-038) | No change. |
| Meta description | "Find the data quality, governance, security, automation, and documentation gaps that could put your Salesforce AI or Agentforce initiative at risk." (147 characters) (EV-038) | No change; the earlier proposal is withdrawn. |

Live structure (EV-038): H1 "AI Does Not Fix a Messy Salesforce Org. It Exposes It."; H2s "Trusted Salesforce Architecture Without the Consulting-Firm Handoffs", "Your AI Initiative Is Only as Reliable as the Salesforce Environment Behind It", "Before You Activate AI in Salesforce, You Need Clear Answers", "What the Assessment Reviews" (seven areas including human review and escalation controls), "What You Receive", "How the Assessment Works", fit and not-fit sections, "Investment" (table: Trust Test from $2,500; assessment from $9,500; remediation $15,000-$75,000; deduplication; migration tiers), "Not Ready for the Full Assessment?", "Why Clear Concise Consulting", "FAQs", "Send Us a Note". Service schema present; no BreadcrumbList. Citability heuristic 40.1 (30 blocks, 10 graded F: many one-line paragraphs and table cells) (EV-042). The live structure already covers the recommended sections; what follows is reduced to deltas.

**Recommended H1 and heading structure**
- H1: keep the live headline or use the question form "Is your Salesforce data ready for AI?"; either way, the first paragraph should say what the assessment is in one sentence (direct-answer passage below)
- H2: "Who this assessment is for" (situations, not titles: an Agentforce or Einstein rollout is planned; a pilot produced results nobody trusts; a compliance review asked what the AI can see)
- H2: "What the assessment covers" (data quality, permissions and field-level security, automation maturity, integration risk; mirrors the published checklist article, EV-015)
- H2 "What You Receive": live; no hold
- H2 "Investment": live ("Starting at $9,500", three to four weeks, Trust Test from $2,500), and matches canon (FACT-15, FACT-28). No hold
- H2: "What happens after" (fixed-price scoping for remediation, or nothing: the assessment stands alone)
- H2: "Who does the work" (Jeremy Carmona, one architect end to end; link to /about)
- H2: "Not ready for an assessment?" (scorecard)

**Direct-answer passage (first paragraph):**

"A Salesforce AI data readiness assessment is a fixed-scope review of the data, permissions, and automation an AI feature will depend on, done before that feature goes live. Clear Concise Consulting's assessment is led by Jeremy Carmona, a Salesforce Architect, and covers data quality, field-level access, automation maturity, and integration risk. You receive a documented list of gaps, the order to fix them, and the reasoning behind each decision, so your team can act on it with or without further help."

(77 words. Align the deliverable sentence with the live "What You Receive" section.)

**Boundary statement (to include under "What the assessment covers"):** "This is not a data cleanup engagement and not an Agentforce build. It tells you what is in the way and what to do first. Cleanup and governance work are separate, fixed-price engagements."

**CTAs**
- Primary: live "Request an Assessment" -> #application-form (on-page form, rendered client-side; not present in the raw HTML). Keep it and keep the visible email fallback; add a plain-text link to /contact for non-rendering agents (ISS-033).
- Secondary: live "Take the Free AI Readiness Scorecard" -> /scorecard appears three times; one instance has no href. Fix that one.

**Internal links**
- /blog/salesforce-ai-data-readiness-checklist -> this page, anchor "Salesforce AI Data Readiness Assessment" (today the post reaches this page only through the header button)
- /blog/six-governance-checkpoints-engagement -> this page, anchor "AI data readiness assessment"
- /blog/ai-reversibility-rollback-plan -> this page, anchor "assess data readiness before go-live"
- /scorecard results state -> this page, anchor "book the full assessment"
- /services/data-governance -> this page, anchor "pre-AI data readiness assessment" and back-link with anchor "ongoing data governance"
- /faqs -> this page from a new answer that names the assessment, its starting price, and the Trust Test (ISS-006)

**JSON-LD (deployed, EV-038):** Service with @id .../salesforce-ai-data-readiness-assessment#service, name "Salesforce AI Data Readiness Assessment", provider -> #organization, areaServed "United States", no offers. The draft at implementation/jsonld/service-ai-data-readiness.draft.json is now a diff against this block (description wording, optional audience); add offers only after FACT-15; add a BreadcrumbList to match the four service pages.

**Evidence:** EV-038, EV-039, EV-042, EV-004, EV-015, EV-030, EV-033, EV-034. **Unresolved:** none (FACT-15 decided in canon: from $9,500, EV-045). **Publication status:** metadata NO_CHANGE; copy deltas DRAFT; price APPROVED_BY_OWNER 2026-09-27 (EV-048).

---

## PKG-SCORECARD: https://www.clearconciseconsulting.com/scorecard

**Audience:** admins and operations leads doing homework; board-prompted "are we ready for AI" questions (audience skill, EV-035).
**Search intent:** informational-to-transactional ("Salesforce AI readiness scorecard", "AI readiness self-assessment").
**Funnel role:** Education and Trust; problem recognition through self-scoring.
**Conversion goal:** scorecard completion, then a 15-minute results call for those who want one. Not every completer should be pushed to a call.

**Current vs proposed metadata**

| Field | Current (live 2026-09-27) | Proposed |
|---|---|---|
| Title | "Salesforce AI Readiness Scorecard \| Free 2-Minute Assessment \| Clear Concise Consulting" (87 characters) (EV-038) | "Free Salesforce AI Readiness Scorecard \| Clear Concise Consulting" (65) |
| Meta description | "Take the free Salesforce AI Readiness Scorecard. 15 questions. 2 minutes. Get a personalized report across Data Quality, Governance, Automation, AI Preparedness, and Documentation Health." (187 characters) (EV-038) | "Score your Salesforce org's AI readiness in 15 questions: data quality, governance, automation, AI preparedness, and documentation health. Free, two minutes." (157; count confirmed live, FACT-16) |

Live structure (EV-038): H1 "How Ready Is Your Salesforce Org for AI?"; a method statement is present in the HTML ("Fifteen questions, three per category ... 80 to 100 are Ready, 60 to 79 are Caution, 40 to 59 are At Risk, and 0 to 39 are Not Ready"); the instrument is an iframe from https://clear-concise-carmona.github.io/ccc-artifacts/ccc-ai-readiness-scorecard.html; 188 words of own HTML; GA4 gtag.js and app.sparkplugin.com scripts load; the only button in the HTML is the header "REQUEST AN ASSESSMENT". Citability heuristic 54.3 (3 blocks) (EV-042).

**Recommended H1 and heading structure**
- H1: keep the live question H1 or "Salesforce AI Readiness Scorecard"; both are acceptable
- H2: "What it measures" (the five categories, FACT-17)
- H2 "How Is the Score Calculated?": live and complete (15 questions, 3 per category, 1-to-5 scale, normalized categories, weighted total, four bands). Add one sentence labeling the bands as professional judgment
- H2: "What you get" (the report; what it does not do: it is self-reported and not an audit)
- H2: "After your results" (optional 15-minute results call; link to the assessment for those who want a full review)

**Targeted replacement copy (adds the judgment label to the live method statement):**

"The scorecard has 15 questions, 3 per category, across five categories: data quality, governance readiness, automation maturity, AI preparedness, and documentation health. Each answer is scored on a 1-to-5 maturity scale, each category is normalized to 100, and the overall score is weighted toward the categories that most often block AI rollouts. The bands (Ready, Caution, At Risk, Not Ready) reflect our professional judgment from client engagements. They are a starting point for a conversation, not a prediction." (FACT-16, FACT-17; only the last two sentences are new.)

**CTAs**
- Primary: "Start the scorecard"
- Post-results: whatever the iframe shows after completion was not observable in the HTML. Add a server-rendered "After your results" block on the Squarespace page: "Book a 15-minute results call" -> scheduler (FACT-09 decided in canon: 15 minutes, qualification only) and "Read about the full assessment" -> /salesforce-ai-data-readiness-assessment (ISS-033).

**Internal links**
- /scorecard -> /blog/salesforce-ai-data-readiness-checklist, anchor "the checklist behind these questions"
- /scorecard -> /salesforce-ai-data-readiness-assessment, anchor "Salesforce AI Data Readiness Assessment" (today only the header button)
- /blog/salesforce-ai-data-readiness-checklist -> /scorecard, anchor "score your org in two minutes"

**JSON-LD:** no change recommended. No schema type gives this page an eligible enhancement, and Quiz or FAQPage markup here would be decoration. WebPage inherited from the site-wide WebSite block is sufficient. Live: site-wide blocks only, as expected (EV-038).

**Evidence:** EV-038, EV-042, EV-003, EV-014, EV-034. **Unresolved:** none (FACT-09 decided in canon: 15-minute fit call, qualification only, EV-045). **Publication status:** metadata DRAFT; method label DRAFT; results block DRAFT. Instrumentation note: events must originate inside the iframe (MEASUREMENT-AND-ROADMAP.md section 2).

---

## PKG-ABOUT: https://www.clearconciseconsulting.com/about

**Audience:** prospects verifying credentials; editors; procurement reviewers; AI systems resolving the Person entity.
**Search intent:** navigational ("Jeremy Carmona Salesforce").
**Funnel role:** Trust.
**Conversion goal:** a call booking from warm visitors; otherwise, entity clarity.

**Current vs proposed metadata**

| Field | Current (live 2026-09-27) | Proposed |
|---|---|---|
| Title | "About Jeremy Carmona \| Salesforce Architect \| Clear Concise Consulting" (70 characters) (EV-038) | No change recommended. |
| Meta description | "Meet Jeremy Carmona, founder of Clear Concise Consulting and a Salesforce architect focused on implementation, data governance, AI readiness, training, and clear technical guidance." (181 characters) (EV-038) | "Jeremy Carmona founded Clear Concise Consulting and leads each engagement. Salesforce Architect since 2012, former NYU Tandon instructor, Salesforce Ben author." (160) (FACT-05 approved: former instructor) |

Live structure (EV-038): H1 "13x Certified Salesforce Architect"; H2 stat tiles "13", "14", "160+", "80%" (the last two twice); H2s "Architecture Track", "Consultant Track:", "Builder Track:", "Why a Journalism Background Matters", "From Confused Beginner to Certified Architect", "NYU Tandon Salesforce Instructor", "What Clients Say", "The Approach", "Results, Not Promises"; "Verify on Trailhead" link; three Salesforce Ben links; "Schedule a Consultation" -> /contact; Person and AboutPage schema. Citability heuristic 34.1 (14 blocks, 8 graded F: tiles and short paragraphs) (EV-042).

**Recommended heading structure**
- H1: "About Jeremy Carmona" (the live H1 is a credential, not the entity name; the Person should lead)
- H2: "What I do" (one paragraph, FACT-01/02)
- H2: "Background" (since 2012; Environmental Defense Fund; journalism; NYU teaching 2022 to 2023, FACT-05 approved)
- H2: "Credentials": the live page lists every certification in three tracks with a "Verify on Trailhead" link (good). Lead with the 3 to 5 relevant to governance and data architecture and summarize the rest (FACT-03, CLM-036)
- H2: "Writing and tools" (Salesforce Ben with the published title FACT-06; Medium; GitHub open-source tools)
- H2: "How I work" (editorial policy link FACT-20; documentation-for-handoff principle, observed snippet)
- H2: "Talk to me" (CTA)

**Direct-answer passage:**

"Jeremy Carmona is the founder of Clear Concise Consulting and a Salesforce Architect. He has worked on Salesforce since 2012, beginning at Environmental Defense Fund, taught Salesforce Administration at NYU Tandon School of Engineering from 2022 to 2023 (FACT-05, approved), and writes on AI governance and data quality for Salesforce Ben, including '5 Questions Salesforce Admins Must Ask Before Turning on AI.' He leads every Clear Concise Consulting engagement personally."

**Corrections to make on this page**
- Salesforce Ben is already cited by its displayed title with three linked pieces (ISS-017 resolved). Add the author page link.
- Replace the "14 Years in Salesforce Ecosystem" tile with "Since 2012" so it stops aging (FACT-04).
- Teaching tense is settled in canon: "Former NYU Tandon Salesforce instructor" (Positioning Canvas v2.2), 2022 to 2023 per Resume Variants (FACT-05). Change the heading "NYU Tandon Salesforce Instructor" to "Former NYU Tandon Salesforce Instructor" and fix the sentence "taught the first Salesforce Administration at NYU Tandon", which is missing the word "course".
- The "80% Student Job Placement Rate" and "160+ Students Trained" tiles are live, twice each. Document the method and denominator or take them down (CLM-004, ISS-019, ISS-037).
- The "What Clients Say" testimonial names a USCIS staff member: confirm written permission or anonymize to role (CLM-049, ISS-031).
- If the page lists all 13 certifications, keep the list but lead with the 3 to 5 relevant to governance and data architecture (owner proof-architecture rule, EV-033).

**CTAs**
- Primary: live "Schedule a Consultation" -> /contact, with copy "Schedule a free 30-minute consultation". Keep the destination; change the copy to the canonical 15-minute fit call (FACT-09).
- Secondary: "Read the AI governance articles" -> /blog (or a governance category page if one exists).

**Internal links**
- every blog byline -> /about
- /about -> /policies-commitments, anchor "editorial policy"
- /about -> https://github.com/clear-concise-carmona, anchor "open-source Salesforce tools" (live)
- /about -> https://www.salesforceben.com/author/jeremy-carmona/, anchor "Salesforce Ben author page" (today three article links, no author page link)

**JSON-LD (deployed, EV-038):** Person (@id /about#jeremy-carmona, jobTitle "Salesforce Architect and Founder", worksFor -> #organization, four sameAs) and AboutPage (mainEntity -> the Person) are live alongside the site-wide blocks. Actions: sameAs parity (ISS-016: four entries here, six and seven on the Organization blocks); optional knowsAbout limited to published topics. The reconciliation draft uses the deployed @id.

**Evidence:** EV-038, EV-042, EV-005, EV-007, EV-017, EV-018. **Unresolved:** FACT-05, CLM-004, CLM-049. **Publication status:** APPROVED_BY_OWNER 2026-09-27 (EV-048); READY_FOR_CMS_EDIT (title: NO_CHANGE).

---

## PKG-FAQS: https://www.clearconciseconsulting.com/faqs

**Audience:** buyers comparing options; procurement; anyone checking prices.
**Search intent:** commercial-informational ("Salesforce consultant pricing", "how much does a Salesforce consultant cost").
**Funnel role:** Trust and the truth layer: this is where prices, process, and client names live.
**Conversion goal:** move a price-checker to a consultation with expectations set.

**Current vs proposed metadata**

| Field | Current (live 2026-09-27) | Proposed |
|---|---|---|
| Title | "Salesforce Consulting FAQs \| CCC \| Clear Concise Consulting" (59 characters) (EV-038) | No change; the earlier proposal is withdrawn. |
| Meta description | "Answers about CCC’s Salesforce assessments, implementation approach, data governance, AI readiness, engagement process, and next steps." (135 characters) (EV-038) | No change. |

Live structure (EV-038): H1 "Frequently Asked Questions"; FAQPage schema with 27 question pairs, including the $5,000 answer and the client list; visible answers: data quality assessment from $5,000, implementation $15,000 to $75,000, workshops $2,500 to $15,000, retainers from $3,000/month, ad hoc $175/hour; "book a 15-minute call" twice; "Book a Call" -> scheduler.zoom.us/jeremy-carmona/free-consultation; "How do I contact CCC? Email: j.carmona@...". No mention of the AI Data Readiness Assessment or the Trust Test. Citability heuristic 53.9 (34 blocks, 4 optimal-length passages: the best-structured commercial page) (EV-042).

**Content corrections (targeted, not a rewrite)**
1. Assessment answer: rewrite FAQ 2 with the offer name, "from $9,500", three to four weeks, a line on the Trust Test from $2,500, and a link to /salesforce-ai-data-readiness-assessment (FACT-15, FACT-28, decided in canon). Remove the "$5,000" data quality line or label it historical (FACT-14 retired). Update the FAQPage schema in the same edit.
2. Retainers: one sentence distinguishing the administration retainer from the architecture advisory retainer (FACT-12/13).
3. Workshops: define the $15,000 tier once (FACT-11).
4. Consultation: one 15-minute fit call, qualification only, no free technical scoping (FACT-09, decided in canon). The FAQ already says 15 minutes; add the qualification-only purpose in one clause.
5. Client names: the relationship type is settled (Jeremy's career experience, not CCC engagements, FACT-22). Change "CCC has worked with" to "Jeremy's experience includes" in the visible answer and the FAQPage schema; permission to name the organizations was asserted by the owner on 2026-09-27 (EV-048); keep the written permissions on file. This is the highest-liability edit in the workspace, and the same change applies to the four case-study pages (ISS-040).
6. Add one FAQ: "Who does the work?" answered with FACT-02 (including the delivery-partner caveat already published on the homepage).
7. Contact answer: the FAQ gives j.carmona@; the footer and /privacy-policy give contact@ (FACT-24); use contact@clearconciseconsulting.com (decided 2026-09-27, EV-048). Update the FAQPage schema in step with every visible edit; it currently repeats the $5,000 answer and the client names.
8. Gumroad answer: the anchor text reads gumroad.com/clearconciseconsulting (a 404) and the href points at https://jeremycarmona.gumroad.com/ (EV-038, EV-045). Change the anchor text to jeremycarmona.gumroad.com so text and link agree. Safe now, independent of Roadmap Decision P1 (ISS-022).

**Direct-answer passage (for the pricing section):**

"Most Clear Concise Consulting projects are fixed price. The price comes from a scoping document you approve before work begins. Architect-led implementations range from $15,000 to $75,000 depending on complexity. Workshops run from $2,500 for a half day to $15,000 for two days plus follow-up. Every engagement begins with a free 15-minute fit call; technical analysis starts in paid work." (FACT-08, FACT-10, FACT-11, FACT-09; all decided in canon, EV-045.)

**CTAs**
- Primary: "Book a 15-minute fit call" -> scheduler (FACT-09 decided in canon) (contact@clearconciseconsulting.com, decided 2026-09-27).
- Secondary: none above the fold; bottom link to /scorecard for the undecided.

**Internal links**
- /faqs -> assessment page (price answer)
- /faqs -> /services/salesforce-implementation (implementation price answer)
- /faqs -> /blog/how-much-does-a-salesforce-implementation-cost-in-2026, anchor "implementation cost guide"
- /blog/how-much-does-a-salesforce-implementation-cost-in-2026 -> /faqs, anchor "our published price ranges"

**JSON-LD (deployed, EV-038):** FAQPage with 27 questions, live. Keep, but only for questions whose visible answers match the register; the pairs containing the $5,000 price and the client names are decided in canon (FACT-14 retired; FACT-22 career experience, not CCC clients) and wait only on string approval and the permission check for named organizations. Do not expect FAQ rich results: Google's documentation states the feature is shown only for well-known, authoritative government and health websites (checked 2026-09-27, EV-043). Validate on the live URL after edits.

**Evidence:** EV-038, EV-042, EV-043, EV-010, EV-011, EV-022. **Unresolved:** none for copy (contact@ decided; permissions asserted, EV-048); the Gumroad anchor text and the /faqs price answer are ready to edit. FACT-09, FACT-11, FACT-12, FACT-15, and FACT-22 are decided in canon (EV-045); their strings need owner approval. **Publication status:** metadata NO_CHANGE; copy DRAFT / APPROVED_BY_OWNER 2026-09-27 (EV-048); Gumroad anchor text FIX_ON_SIGHT.
