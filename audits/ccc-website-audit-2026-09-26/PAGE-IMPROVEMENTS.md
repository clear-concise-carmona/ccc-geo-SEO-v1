# Page Improvement Packages

Workspace: ccc-website-audit-2026-09-26 | Status of every package: DRAFT. Nothing here is publication-ready until the HOLD facts it depends on are resolved in CANONICAL-BUSINESS-FACTS.md and the live page has been read.

Conventions:
- "Current (as indexed)" = the title returned by search results, which reflects the SEO title at last crawl. Current meta descriptions were not observable; the observed snippet is given for context only.
- "Proposed" wording uses only APPROVED_FOR_DRAFT_USE facts unless marked [HOLD: FACT-xx].
- Character counts are in implementation/metadata-drafts.md.
- No em dashes; owner's forbidden-word list respected in proposed copy.
- Page selection: homepage and the assessment offer page were required by the brief; /scorecard (secondary goal), /about (entity layer), and /faqs (truth layer, where prices and client names live) were selected from the evidence. Service pages for implementation and data governance were not selected because no defect beyond title-pattern hygiene was observed for them.

---

## PKG-HOME: https://www.clearconciseconsulting.com/

**Audience:** first-time visitors from search or referral: operations, IT, and compliance leaders in nonprofit, healthcare, government, and enterprise organizations; some admins and recruiters.
**Search intent:** navigational (brand) and commercial ("Salesforce AI governance consulting", "Salesforce consultant NYC" per FACT-25 decision).
**Funnel role:** Discovery and Trust. Must answer in one screen: what CCC does, who does it, for whom, and the next step.
**Conversion goal:** primary, a qualified inquiry about the paid assessment or an engagement; secondary, a scorecard start.

**Current vs proposed metadata**

| Field | Current (as indexed) | Proposed |
|---|---|---|
| Title | Two variants indexed: "Salesforce Consultant NYC \| 13x Certified Architect" and "Salesforce AI Governance & Architecture" (EV-006, EV-014) | "Salesforce AI Governance Consulting \| Clear Concise Consulting" |
| Meta description | unavailable. Snippet observed: "Salesforce implementation, data governance, and AI governance services for nonprofit, government, healthcare, and enterprise organizations. Jeremy Carmona, a 13x certified Salesforce Architect, leads every engagement from scoping to go-live." | "Architect-led Salesforce AI governance and data governance for nonprofit, government, healthcare, and enterprise organizations. One architect, end to end." |
| og:title / og:description | owner-reported stale og:description (EV-032) | same as title and description above |

Note: "13x certified" is omitted from the description until FACT-03 is confirmed; it can be added back as "13x certified Salesforce Architect" after confirmation. If the owner decides NYC is a target market (FACT-25), append "New York City" to the description, not the title.

**Recommended H1 and heading structure**

- H1: "Salesforce AI governance for organizations that hold sensitive data"
- H2: "Who this is for" (four verticals, one sentence each, situation-based: an AI feature is planned or live and nobody has reviewed what data it touches)
- H2: "What Clear Concise Consulting does" (three items: AI governance and data readiness; data governance; implementation architecture)
- H2: "How an engagement starts" (free consultation, fixed-price scoping document, one architect end to end)
- H2: "Evidence" (one case metric [HOLD: FACT-21], one credential line [HOLD: FACT-03], one publication line FACT-06)
- H2: "Start here" (primary and secondary CTA)

**Targeted replacement copy (direct-answer passage, for the first section under the H1):**

"Clear Concise Consulting is a Salesforce consulting practice led by Jeremy Carmona, a Salesforce Architect who has worked on the platform since 2012 [HOLD: FACT-04]. It provides AI governance and data readiness, data governance, and implementation architecture for nonprofit, government, healthcare, and enterprise organizations. Jeremy leads every engagement from scoping to go-live. Most projects are fixed price, set from a scoping document you approve before work begins, and every engagement begins with a free consultation."

(68 words. Uses FACT-01, FACT-02, FACT-08, FACT-09; FACT-04 flagged.)

**CTAs**
- Primary: "Ask about an AI data readiness assessment" -> /contact (or the scheduler, owner decision FACT-09/24). Label wording depends on the offer name [HOLD: FACT-15].
- Secondary (below the fold): "Take the free two-minute AI Readiness Scorecard" -> /scorecard.
- Do not place the scorecard above the fold: high-intent visitors should reach the inquiry path first.

**Internal links (source -> destination, anchor)**
- / -> assessment landing page (candidate /services/salesforce-ai-data-preparation), anchor "[offer name]" [HOLD: FACT-15]
- / -> /scorecard, anchor "free AI Readiness Scorecard"
- / -> /about, anchor "Jeremy Carmona"
- / -> /services/data-governance, anchor "Salesforce data governance"
- / -> /blog/salesforce-ai-data-readiness-checklist, anchor "pre-Agentforce data checklist"
- / -> /case-studies/enterprise, anchor "enterprise CPQ case study" (metric wording pending FACT-21)

**JSON-LD:** Organization and WebSite are owner-reported as deployed. No new type recommended. Actions: reconcile sameAs (ISS-016), one contactPoint (FACT-24), remove LocalBusiness unless a customer-facing office is confirmed (ISS-015). Draft: implementation/jsonld/organization-person.reconciliation.json.

**Evidence:** EV-006, EV-014, EV-028, EV-032, EV-033. **Unresolved:** FACT-03, FACT-04, FACT-15, FACT-21, FACT-25. **Publication status:** DRAFT / APPROVAL_REQUIRED.

---

## PKG-ASSESS: assessment offer page (candidate URL https://www.clearconciseconsulting.com/services/salesforce-ai-data-preparation)

**Precondition:** the owner confirms this URL is the landing page for the paid assessment, or names another existing page. If a new page is preferred, that is a URL change and needs the redirect, internal-link, sitemap, and validation plan in implementation/redirects-and-indexing.md. Nothing below is publishable until FACT-15 is resolved.

**Audience:** operations and IT leaders about to enable Agentforce, Einstein, or Data Cloud; compliance officers in healthcare and government.
**Search intent:** commercial ("Salesforce AI readiness assessment", "Agentforce data readiness assessment").
**Funnel role:** Appropriate next step for high-intent visitors; Education for mid-intent visitors arriving from the checklist article.
**Conversion goal:** assessment inquiry (form or scheduler).

**Current vs proposed metadata**

| Field | Current (as indexed) | Proposed |
|---|---|---|
| Title | "Salesforce AI Data Preparation Services — Clear Concise Consulting" (default pattern, EV-002/009) | "Salesforce AI Data Readiness Assessment \| Clear Concise Consulting" [HOLD: FACT-15 name] |
| Meta description | unavailable. Snippet: "jargon-free approach that simplifies complex data challenges into manageable steps"; "comprehensive data audit"; "focused cleanup 2-4 weeks; complete transformation 2-3 months" | "An architect-led review of the data, permissions, and automation your Salesforce AI features depend on, with a written list of gaps and what to fix first." |

**Recommended H1 and heading structure**
- H1: "Is your Salesforce data ready for AI?" (question heading; the first paragraph answers it)
- H2: "Who this assessment is for" (situations, not titles: an Agentforce or Einstein rollout is planned; a pilot produced results nobody trusts; a compliance review asked what the AI can see)
- H2: "What the assessment covers" (data quality, permissions and field-level security, automation maturity, integration risk; mirrors the published checklist article, EV-015)
- H2: "What you receive" [HOLD: owner to confirm deliverables]
- H2: "Timeline and price" [HOLD: FACT-14/15]
- H2: "What happens after" (fixed-price scoping for remediation, or nothing: the assessment stands alone)
- H2: "Who does the work" (Jeremy Carmona, one architect end to end; link to /about)
- H2: "Not ready for an assessment?" (scorecard)

**Direct-answer passage (first paragraph):**

"A Salesforce AI data readiness assessment is a fixed-scope review of the data, permissions, and automation an AI feature will depend on, done before that feature goes live. Clear Concise Consulting's assessment is led by Jeremy Carmona, a Salesforce Architect, and covers data quality, field-level access, automation maturity, and integration risk. You receive a documented list of gaps, the order to fix them, and the reasoning behind each decision, so your team can act on it with or without further help."

(77 words. Deliverable sentence [HOLD: owner confirms deliverables].)

**Boundary statement (to include under "What the assessment covers"):** "This is not a data cleanup engagement and not an Agentforce build. It tells you what is in the way and what to do first. Cleanup and governance work are separate, fixed-price engagements."

**CTAs**
- Primary: "Request the assessment" -> /contact or scheduler [HOLD: FACT-24].
- Secondary (bottom): "Not sure yet? Take the free two-minute scorecard" -> /scorecard.

**Internal links**
- /blog/salesforce-ai-data-readiness-checklist -> this page, anchor "[offer name]"
- /blog/six-governance-checkpoints-engagement -> this page, anchor "AI data readiness assessment"
- /blog/ai-reversibility-rollback-plan -> this page, anchor "assess data readiness before go-live"
- /scorecard results state -> this page, anchor "book the full assessment"
- /services/data-governance -> this page, anchor "pre-AI data readiness assessment" and back-link with anchor "ongoing data governance"
- /faqs (assessment price answer) -> this page

**JSON-LD:** Service draft at implementation/jsonld/service-ai-data-readiness.draft.json (APPROVAL_REQUIRED: name, price, and URL depend on FACT-15). Provider references #organization; no offers block until price is confirmed; no aggregateRating.

**Evidence:** EV-002, EV-004, EV-009, EV-015, EV-030, EV-033, EV-034. **Unresolved:** FACT-14, FACT-15, FACT-24, deliverables list. **Publication status:** DRAFT / OWNER_DECISION_REQUIRED.

---

## PKG-SCORECARD: https://www.clearconciseconsulting.com/scorecard

**Audience:** admins and operations leads doing homework; board-prompted "are we ready for AI" questions (audience skill, EV-035).
**Search intent:** informational-to-transactional ("Salesforce AI readiness scorecard", "AI readiness self-assessment").
**Funnel role:** Education and Trust; problem recognition through self-scoring.
**Conversion goal:** scorecard completion, then a 15-minute results call for those who want one. Not every completer should be pushed to a call.

**Current vs proposed metadata**

| Field | Current (as indexed) | Proposed |
|---|---|---|
| Title | "Salesforce AI Readiness Scorecard \| Free 2-Minute Assessment \| Clear Concise Consulting" (86 characters) | "Free Salesforce AI Readiness Scorecard \| Clear Concise Consulting" |
| Meta description | unavailable. Snippet: "free 15-question assessment ... five categories ... weighted risk score ... 2 minutes" | "Score your Salesforce org's AI readiness in [15] questions: data quality, governance, automation, AI preparedness, and documentation health. Free, two minutes." [HOLD: FACT-16 count] |

**Recommended H1 and heading structure**
- H1: "Salesforce AI Readiness Scorecard"
- H2: "What it measures" (the five categories, FACT-17)
- H2: "How scoring works" (one count, one scale, one threshold statement; thresholds described as Clear Concise Consulting's professional judgment based on client work, not a validated predictor) [HOLD: FACT-16]
- H2: "What you get" (the report; what it does not do: it is self-reported and not an audit)
- H2: "After your results" (optional 15-minute results call; link to the assessment for those who want a full review)

**Targeted replacement copy (method statement, replaces both current descriptions):**

"The scorecard has [15] questions, [3] per category, across five categories: data quality, governance readiness, automation maturity, AI preparedness, and documentation health. Each answer is scored on a [scale]. Your total is weighted toward the categories that most often block AI rollouts in the organizations we work with. The score bands reflect our professional judgment from client engagements. They are a starting point for a conversation, not a prediction." [HOLD: FACT-16 for every bracketed value]

**CTAs**
- Primary: "Start the scorecard"
- Post-results: "Book a 15-minute results call" -> scheduler [HOLD: FACT-09 duration wording]; secondary "Read about the full assessment" -> assessment page.

**Internal links**
- /scorecard -> /blog/salesforce-ai-data-readiness-checklist, anchor "the checklist behind these questions"
- /scorecard -> assessment page, anchor "[offer name]"
- /blog/salesforce-ai-data-readiness-checklist -> /scorecard, anchor "score your org in two minutes"

**JSON-LD:** no change recommended. No schema type gives this page an eligible enhancement, and Quiz or FAQPage markup here would be decoration. WebPage inherited from the site-wide WebSite block is sufficient.

**Evidence:** EV-003, EV-014, EV-021, EV-034. **Unresolved:** FACT-16, FACT-09. **Publication status:** DRAFT / OWNER_DECISION_REQUIRED.

---

## PKG-ABOUT: https://www.clearconciseconsulting.com/about

**Audience:** prospects verifying credentials; editors; procurement reviewers; AI systems resolving the Person entity.
**Search intent:** navigational ("Jeremy Carmona Salesforce").
**Funnel role:** Trust.
**Conversion goal:** a call booking from warm visitors; otherwise, entity clarity.

**Current vs proposed metadata**

| Field | Current (as indexed) | Proposed |
|---|---|---|
| Title | "About Jeremy Carmona \| Salesforce Architect \| Clear Concise Consulting" | No change recommended. |
| Meta description | unavailable. Snippet: "every configuration is documented for handoff and the next admin shouldn't need to call them to understand what was built" | "Jeremy Carmona founded Clear Concise Consulting and leads every engagement. Salesforce Architect since 2012, NYU Tandon instructor, Salesforce Ben author." [HOLD: FACT-04, FACT-05 tense] |

**Recommended heading structure**
- H1: "About Jeremy Carmona"
- H2: "What I do" (one paragraph, FACT-01/02)
- H2: "Background" (since 2012; Environmental Defense Fund; journalism; NYU teaching with years) [HOLD: FACT-04, FACT-05]
- H2: "Credentials" (name 3 to 5 relevant credentials with a Trailhead verification link; summarize the rest as "13 Salesforce certifications") [HOLD: FACT-03, CLM-036]
- H2: "Writing and tools" (Salesforce Ben with the published title FACT-06; Medium; GitHub open-source tools)
- H2: "How I work" (editorial policy link FACT-20; documentation-for-handoff principle, observed snippet)
- H2: "Talk to me" (CTA)

**Direct-answer passage:**

"Jeremy Carmona is the founder of Clear Concise Consulting and a Salesforce Architect. He has worked on Salesforce since 2012, beginning at Environmental Defense Fund [HOLD: FACT-04], has taught Salesforce Administration at NYU Tandon School of Engineering [HOLD: FACT-05], and writes on AI governance and data quality for Salesforce Ben, including '5 Questions Salesforce Admins Must Ask Before Turning on AI.' He leads every Clear Concise Consulting engagement personally."

**Corrections to make on this page**
- Cite the Salesforce Ben article by its published title (ISS-017).
- Resolve teaching tense (FACT-05). Do not publish the 80% placement figure until the method and denominator are documented (CLM-004).
- If the page lists all 13 certifications, keep the list but lead with the 3 to 5 relevant to governance and data architecture (owner proof-architecture rule, EV-033).

**CTAs**
- Primary: "Book a call" -> scheduler [HOLD: FACT-09 wording].
- Secondary: "Read the AI governance articles" -> /blog (or a governance category page if one exists).

**Internal links**
- every blog byline -> /about
- /about -> /policies-commitments, anchor "editorial policy"
- /about -> https://github.com/clear-concise-carmona, anchor "open-source Salesforce tools"
- /about -> https://www.salesforceben.com/author/jeremy-carmona/, anchor "Salesforce Ben author page"

**JSON-LD:** Person and AboutPage owner-reported as deployed. Actions: sameAs parity (ISS-016); jobTitle "Salesforce Architect"; worksFor -> #organization; knowsAbout limited to published topics; no unverified awards or affiliations. Draft in implementation/jsonld/organization-person.reconciliation.json.

**Evidence:** EV-005, EV-007, EV-017, EV-018, EV-029, EV-031. **Unresolved:** FACT-03, FACT-04, FACT-05. **Publication status:** DRAFT / APPROVAL_REQUIRED (title: NO_CHANGE).

---

## PKG-FAQS: https://www.clearconciseconsulting.com/faqs

**Audience:** buyers comparing options; procurement; anyone checking prices.
**Search intent:** commercial-informational ("Salesforce consultant pricing", "how much does a Salesforce consultant cost").
**Funnel role:** Trust and the truth layer: this is where prices, process, and client names live.
**Conversion goal:** move a price-checker to a consultation with expectations set.

**Current vs proposed metadata**

| Field | Current (as indexed) | Proposed |
|---|---|---|
| Title | "Salesforce Consulting FAQs \| Pricing, Process & Timeline \| Clear Concise Consulting" (82 characters) | "Pricing, Process, and Timeline FAQs \| Clear Concise Consulting" |
| Meta description | unavailable. Snippet: "free consultation ... data quality assessment starts at $5,000 ... implementation $15,000 to $75,000 ... USCIS, Environmental Defense Fund, UnitedHealth Group, HRSA, and NYU" | "How Clear Concise Consulting prices Salesforce work: fixed-price projects from an approved scoping document, published ranges, and a free consultation." |

**Content corrections (targeted, not a rewrite)**
1. Assessment answer: state the confirmed offer name and starting price once [HOLD: FACT-14/15]; link to the assessment page.
2. Retainers: one sentence distinguishing the administration retainer from the architecture advisory retainer (FACT-12/13).
3. Workshops: define the $15,000 tier once (FACT-11).
4. Consultation: state duration and purpose, and whether the 15-minute results call is a different thing (FACT-09).
5. Client names: keep only names with confirmed relationship type and permission; otherwise use the categorical wording in CLM-007 (FACT-22). This is the highest-liability edit in the workspace.
6. Add one FAQ: "Who does the work?" answered with FACT-02.

**Direct-answer passage (for the pricing section):**

"Most Clear Concise Consulting projects are fixed price. The price comes from a scoping document you approve before work begins. Architect-led implementations range from $15,000 to $75,000 depending on complexity. Workshops run from $2,500 for a half day to $15,000. Every engagement begins with a free consultation to confirm scope and fit." (FACT-08, FACT-10, FACT-11 [HOLD tier wording], FACT-09.)

**CTAs**
- Primary: "Book a free consultation" -> scheduler or /contact [HOLD: FACT-09/24].
- Secondary: none above the fold; bottom link to /scorecard for the undecided.

**Internal links**
- /faqs -> assessment page (price answer)
- /faqs -> /services/salesforce-implementation (implementation price answer)
- /faqs -> /blog/how-much-does-a-salesforce-implementation-cost-in-2026, anchor "implementation cost guide"
- /blog/how-much-does-a-salesforce-implementation-cost-in-2026 -> /faqs, anchor "our published price ranges"

**JSON-LD:** FAQPage owner-reported as deployed. Keep, but only for questions whose visible answers match the register; remove any Q/A pair that contains HOLD facts until resolved. Do not expect FAQ rich results (Google restricted FAQ rich results in 2023 to authoritative government and health sites; verify against current documentation, host blocked this run). Validate on the live URL after edits.

**Evidence:** EV-010, EV-011, EV-012, EV-022, EV-023. **Unresolved:** FACT-09, FACT-11 to FACT-15, FACT-22. **Publication status:** DRAFT / OWNER_DECISION_REQUIRED.
