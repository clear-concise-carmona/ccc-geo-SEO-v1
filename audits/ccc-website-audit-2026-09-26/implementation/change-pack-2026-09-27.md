# Change pack: approved strings for clearconciseconsulting.com (2026-09-27)

Source of authority: owner decisions of 2026-09-27 (evidence/owner/owner-decisions-EV-048.md) applied to the Confluence canon (EV-045) and the live text captured in EV-038 and EV-047. Every "Live" string below is quoted from the saved HTML; every "Replace with" string uses only facts marked APPROVED or DECIDED in CANONICAL-BUSINESS-FACTS.md. Square brackets mark the few places where the owner still supplies a fact. Nothing here has been published; edits are made in Squarespace by the owner or an implementer, in this order (implementation/squarespace-instructions.md section 0).

Voice check: replacement copy was scanned against the owner's forbidden-word list and contains no em dashes.

## Batch 0. Before the first edit
- Export the analytics and Search Console baseline (ISS-026; MEASUREMENT-AND-ROADMAP.md section 2) so a before/after record exists.
- Keep a copy of each page's current text (Squarespace version history covers this; rollback notes in implementation/rollback-notes.md).

## Batch 1. Fix on sight (ISS-027, ISS-031, ISS-022)

**1.1 /terms-conditions: six placeholder links (EV-038).** Each anchor points at a claude.ai/chat/ URL. Keep the anchor text, change the target:

| Anchor text (live) | Live target | Replace target with |
|---|---|---|
| Diversity, Equity & Inclusion Policy | https://claude.ai/chat/link-to-full-policy | /policies-commitments (the page exists) or remove the link if the policy is not on that page |
| Environmental Policy | https://claude.ai/chat/link-to-full-policy | /policies-commitments, same condition |
| Privacy Policy | https://claude.ai/chat/link-to-privacy-policy | /privacy-policy |
| Data Processing Agreement | https://claude.ai/chat/link-to-dpa | the DPA document URL if one is published; otherwise remove the link and keep the words |
| Terms & Conditions | https://claude.ai/chat/link-to-full-terms | remove the link (it would point at this page) |
| Book 15-minute policy discussion | https://claude.ai/chat/link-to-calendar | the one scheduler URL: https://scheduler.zoom.us/jeremy-carmona/free-consultation |

Same page, contact block: "General Inquiries: info@clearconciseconsulting.com" becomes "General Inquiries: contact@clearconciseconsulting.com" (decision 4). "Policy Questions: policies@..." and the environmental-partnerships address are specialized mailboxes; the owner keeps or folds them into contact@.

**1.2 /contact: dated availability line (EV-038).**
Live: "Currently booking for Q3 2026 · Response within 24 hours"
Replace with: "Now booking new engagements · Response within 24 hours"

**1.3 /faqs: Gumroad anchor text (EV-038, EV-045).**
Live: anchor text "gumroad.com/clearconciseconsulting" with href https://jeremycarmona.gumroad.com/
Replace with: anchor text "jeremycarmona.gumroad.com" (href unchanged). Update the matching FAQPage answer text in the same edit.

## Batch 1b. Link pass and hygiene session (added 2026-09-28; EV-050, EV-051)
No approved strings beyond the checklist's own anchor text ("Common questions about working with CCC" for the /services link to /faqs) and the link text "Salesforce AI Data Readiness Assessment". Items: ISS-043, ISS-044, ISS-048 to ISS-052, ISS-021, and ISS-029 (widened). Where and in what order: implementation/squarespace-instructions.md section 0 addendum; mappings in implementation/redirects-and-indexing.md sections B and H. Status: DRAFT until the owner confirms the checklist items.

## Batch 2. Price ladder (decision A; ISS-006, ISS-038, ISS-041)

**2.1 /services: the anecdote (EV-038).**
Live: "Implementation cost: $30,000. The governance assessment that would have caught it: $8,000."
Replace with: "Implementation cost: $30,000. The assessment that would have caught it: the Salesforce AI Data Readiness Assessment, from $9,500."
Alternative if the owner wants the project figure kept: "The governance assessment that would have caught it cost $8,000 at 2025 project pricing; the Salesforce AI Data Readiness Assessment now starts at $9,500."

**2.2 /faqs: "How much does a typical engagement cost?" (EV-038).**
Live: "It depends on scope. A data quality assessment starts at $5,000. A full Salesforce implementation ranges from $15,000 to $75,000 depending on complexity. Training workshops range from $2,500 (half-day) to $15,000 (executive session). Every engagement begins with a f[ree consultation]..."
Replace the whole answer with: "It depends on scope. The Salesforce AI Trust Test starts at $2,500 and takes about five business days. The Salesforce AI Data Readiness Assessment starts at $9,500 and takes three to four weeks. Architect-led implementations range from $15,000 to $75,000 depending on complexity. Training workshops run $2,500 for a half day, $7,500 for a full day, and $15,000 for two days plus follow-up. Retained Advisory starts at $3,000 per month with a three-month minimum. Ad hoc architect support is $175 per hour. Every engagement begins with a free 15-minute fit call; technical analysis starts in paid work. Read more about the assessment at clearconciseconsulting.com/salesforce-ai-data-readiness-assessment."
Also update: the same question's acceptedAnswer text in the FAQPage JSON-LD (page Header Code Injection). Full replacement block with this answer, the attribution answer (4.2), and the Retained Advisory answer already applied: implementation/jsonld/faqpage-faqs.approved.json. (FACT-08 to FACT-12, FACT-15, FACT-28, FACT-29)

**2.3 /services/data-governance: "Timeline and investment" table (EV-038).**
Live row: "Data quality assessment | 1-2 weeks | $5,000-$8,000"
Replace with two rows: "Salesforce AI Trust Test | ~5 business days | Starting at $2,500" and "Salesforce AI Data Readiness Assessment | 3-4 weeks | Starting at $9,500"
Hold (not approved yet): the rows "Deduplication project $8,000-$15,000", "Data migration $10,000-$20,000 / $20,000-$40,000", and "Ongoing governance (monthly retainer) $1,500-$3,000/month" are not in the canonical offers page as read (ISS-042; CLM-059, CLM-064). Leave them until the owner confirms them in Confluence or removes them.

**2.4 /services/ai-governance: pricing paragraph (EV-047).**
Live: "Pricing: AI Governance Assessments start at $5,000 for orgs with fewer than 50 users and 5 or fewer AI touchpoints. Complex environments (multiple Clouds, GovCloud, HIPAA requirements) are scoped individually after a 15-minute con[sultation]."
Replace with: "Pricing: the Salesforce AI Data Readiness Assessment starts at $9,500 for one production environment and takes three to four weeks. Smaller scopes start with the Salesforce AI Trust Test from $2,500. Complex environments (multiple Clouds, GovCloud, HIPAA requirements) are scoped individually after a free 15-minute fit call."
Also update: the Service block's hasOfferCatalog in the page Header Code Injection. Full replacement block: implementation/jsonld/service-ai-governance.approved.json. The catalog it carries:

```json
"hasOfferCatalog": {
  "@type": "OfferCatalog",
  "name": "Salesforce AI governance offers",
  "itemListElement": [
    {"@type": "Offer", "name": "Salesforce AI Trust Test",
     "description": "About five business days.",
     "priceSpecification": {"@type": "PriceSpecification", "minPrice": "2500", "priceCurrency": "USD"}},
    {"@type": "Offer", "name": "Salesforce AI Data Readiness Assessment",
     "url": "https://www.clearconciseconsulting.com/salesforce-ai-data-readiness-assessment",
     "description": "Three to four weeks, one production environment.",
     "priceSpecification": {"@type": "PriceSpecification", "minPrice": "9500", "priceCurrency": "USD"}},
    {"@type": "Offer", "name": "Remediation and implementation",
     "description": "Scoped after the assessment.",
     "priceSpecification": {"@type": "PriceSpecification", "minPrice": "15000", "maxPrice": "75000", "priceCurrency": "USD"}}
  ]
}
```

**2.5 /org-health (EV-047).**
Live: "The assessment that costs $12,000 and saves $80,000."
Replace with one of: (a) if $12,000 is a project figure: "The $12,000 assessment that saved $80,000 [owner adds: which engagement, and how the $80,000 was counted]"; (b) if it describes the offer: "The assessment that starts at $9,500 and heads off five-figure rework." The owner picks; (b) needs no method note.
Live: "NYU Tandon instructor: 160+ students trained, 80% job placement rate."
Replace with: "Former NYU Tandon instructor (2022 to 2023): 160+ students trained, about 80% job placement rate [method note: owner supplies the counting method and window]."
Live: "Book a Free Consultation"
Replace with: "Book a 15-minute fit call"

**2.6 /case-studies and /case-studies/healthcare: the $8,000 anecdote (EV-047).** This describes a past engagement, so label rather than restate: after the first "$8,000" on each page add "(2025 project pricing; the assessment now starts at $9,500)". The healthcare H1 "$30,000 AI failure prevented with an $8,000 assessment." can stay if the label appears in the first paragraph. Edit together with Batch 4.3.

**2.7 /ai-center-of-excellence: service table (EV-047).** HOLD (ISS-039). The six-row ladder is not in the canonical offers page as read. Owner decides in Confluence first. Whatever is decided, the row "Governance Assessment ... $8,000" becomes "Salesforce AI Data Readiness Assessment ... Starting at $9,500" and "Governance Training ... $2,500" should match the canonical half-day workshop (FACT-11).

## Batch 3. Intake and credential (decisions B and C; ISS-007, FACT-05, ISS-037)

**3.1 /about, closing CTA (EV-038).**
Live: "Schedule a free 30-minute consultation. We'll discuss your current challenges, identify quick wins, and determine if working together makes sense."
Replace with: "Book a free 15-minute fit call. We confirm scope and fit in that call; technical analysis starts in paid work."

**3.2 /services/salesforce-nonprofit-consulting (EV-038).**
Live: "Schedule a free 30-minute consultation to discuss your nonprofit's Salesforce needs."
Replace with: "Book a free 15-minute fit call to confirm scope and fit for your nonprofit's Salesforce work."

**3.3 /about, founder paragraph (EV-038).**
Live: "He has 14 years in the Salesforce ecosystem, taught the first Salesforce Administration at NYU Tandon School of Engineering, and has published in Salesforce Ben on AI governance and data quality."
Replace with: "He has worked on Salesforce since 2012, taught the first Salesforce Administration course at NYU Tandon School of Engineering (2022 to 2023), and has published in Salesforce Ben on AI governance and data quality."

**3.4 /about, credential heading and sentence (EV-038).**
Live: heading "NYU Tandon Salesforce Instructor"; sentence "Since 2022, I've taught Salesforce Administration to career changers at NYU Tandon School of Engineering through PathStream's certificate program"
Replace with: heading "Former NYU Tandon Salesforce Instructor (2022 to 2023)"; sentence "From 2022 to 2023 I taught Salesforce Administration to career changers at NYU Tandon School of Engineering through PathStream's certificate program."

**3.5 /about, stat tiles (EV-038; ISS-037).** Tiles appear twice on the page; show each once.
Live: "14 Years in Salesforce Ecosystem" -> "In the Salesforce ecosystem since 2012"
Live: "80% Student Job Placement Rate" and "80% JOB PLACEMENT RATE" -> "About 80% job placement rate" plus a one-line method note under the tile: "[Owner supplies: how placement was counted and over what window; the cohort is the 160+ students taught 2022 to 2023]"
Live: "160+ Students Trained at NYU Tandon" -> keep.

## Batch 4. Attribution (decision D; permissions asserted; ISS-018, ISS-040, ISS-019)

**4.1 /services (EV-038).**
Live: "Trusted by teams at USCIS, NYU, Environmental Defense Fund, UnitedHealth Group, and HRSA." and the logo-row heading "Trusted by teams at:"
Replace with: "Jeremy's experience includes Salesforce work at or for USCIS, NYU, Environmental Defense Fund, UnitedHealth Group, and HRSA." and heading "Experience includes:"
Live: "30+ implementations across nonprofit, government, healthcare, and enterprise organizations." -> HOLD until the owner confirms the count (FACT-33). Interim: "Implementations across nonprofit, government, healthcare, and enterprise organizations."

**4.2 /faqs (EV-038).**
Live: "CCC has worked with USCIS, Environmental Defense Fund, UnitedHealth Group, HRSA, and NYU."
Replace with: "Jeremy Carmona's experience includes Salesforce work at or for USCIS, Environmental Defense Fund, UnitedHealth Group, HRSA, and NYU."
Optional second sentence if the owner wants the distinction explicit: "These were roles and projects in Jeremy's architecture career, not Clear Concise Consulting engagements."
Also update: the same answer in the FAQPage JSON-LD.

**4.3 /who-we-help (EV-038).**
Live: "How CCC helps: CCC delivered a GovCloud implementation for USCIS in 8 weeks: environment management, CI/CD pipeline support, and security documentation."
Replace with: "How CCC helps: Jeremy's experience includes a GovCloud implementation for USCIS delivered in 8 weeks: environment management, CI/CD pipeline support, and security documentation."
The rest of the page: rewrite to the four canonical verticals per PAGE-IMPROVEMENTS.md and implementation/metadata-drafts.md (ISS-009, approved).

**4.4 Case studies (EV-047; ISS-040).** Approach approved; the owner fills the brackets before the edit.
/case-studies, intro: Live "Real projects. Real numbers. Zero handoffs. Every CCC engagement follows the same model: one architect from scoping to documentation. These four projects show what that looks like in practice."
Replace with: "Real projects. Real numbers. One architect from scoping to documentation. These four projects are drawn from Jeremy Carmona's work as a Salesforce architect, before and since founding Clear Concise Consulting."
Each case page, line under the H1: "[Real engagement, client anonymized | Composite drawn from N engagements | Illustrative scenario]. [Delivered by Jeremy Carmona before founding CCC | A Clear Concise Consulting engagement]."
/case-studies/government: "CCC completed the same scope in 8 weeks with a single architect." -> "Jeremy completed the same scope in 8 weeks as the single architect." "CCC delivered 35 documentation assets at handoff" -> "[The engagement that produced the 35 assets: owner confirms. The Client Roster attributes a 35-asset handoff to Goodway Technologies; if that is the source, move the figure to its own engagement and remove it here.]"
/case-studies/nonprofit: "CCC delivered a clean dataset in 3 weeks" -> "Jeremy delivered a clean dataset in 3 weeks" (the 70,000-record figure matches the Environmental Defense Fund work, career experience per FACT-22).
/case-studies/healthcare: "CCC's AI readiness assessment cost $8,000" -> "[The AI readiness assessment cost $8,000 (2025 project pricing) | if not a CCC engagement: Jeremy's assessment cost $8,000 (2025 project pricing)]"; "the methodology developed during this engagement" stays only if the label says CCC engagement.
Schema on all four pages: replace the CaseStudy block with Article (Batch 6.3).

## Batch 5. Contact identity (decision 4; ISS-008, ISS-033)
- /faqs "How do I contact CCC? Email: j.carmona@clearconciseconsulting.com." -> "Email: contact@clearconciseconsulting.com." (and the FAQPage answer)
- /salesforce-ai-data-readiness-assessment: "shoot us an email here: info@clearconciseconsulting.com" -> "or email contact@clearconciseconsulting.com"
- /terms-conditions: "General Inquiries: info@..." -> contact@ (Batch 1.1)
- Squarespace Business Information: email -> contact@clearconciseconsulting.com (feeds the native Organization block)
- Footer and /privacy-policy already show contact@ (no change)
- /contact: add a plain-text block with the address, contact@, and the scheduler link so the page has contact facts outside the iframe (ISS-033)
- Custom Organization block: email and contactPoint per implementation/jsonld/organization-person.reconciliation.json

## Batch 6. Schema (decisions 3 and 4; ISS-015, ISS-016, ISS-028)
**6.1 Business Information (Squarespace settings):** clear the opening hours (removes the hours from the native LocalBusiness output). If the platform still emits LocalBusiness with the address, record it in RUN-STATUS as a platform limitation; the address stays public in the footer either way.
**6.2 Site-wide Header Code Injection:** replace the custom Organization+ProfessionalService block and the Person block with implementation/jsonld/organization-person.reconciliation.json (contact@; one combined 11-entry sameAs array from implementation/jsonld/sameas-target-list.json; no X/Twitter; PostalAddress kept). Remove the duplicate FAQPage source on / and /home (one of the two injection points).
**6.3 Case-study pages:** replace each CaseStudy block with an Article block:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://www.clearconciseconsulting.com/case-studies/government#article",
  "url": "https://www.clearconciseconsulting.com/case-studies/government",
  "headline": "6-month quoted timeline delivered in 8 weeks.",
  "description": "[the label line from Batch 4.4, then one sentence of scope]",
  "about": {"@type": "Thing", "name": "Salesforce Government Cloud implementation"},
  "author": {"@id": "https://www.clearconciseconsulting.com/about#jeremy-carmona"},
  "publisher": {"@id": "https://www.clearconciseconsulting.com/#organization"},
  "datePublished": "[owner supplies]",
  "dateModified": "[date of this edit]"
}
```
All four blocks (government, healthcare, nonprofit, and enterprise, which also carries a CaseStudy type) with the live H1s as headlines: implementation/jsonld/article-case-studies.draft.json. Fill the bracketed label and dates before pasting.
**6.4 Posts:** one of Article or BlogPosting per post, not both (ISS-028).

## Batch 7. Metadata and copy packages (approved)
- Titles and descriptions: implementation/metadata-drafts.md (homepage title with brand, ISS-004; shorter post suffix, ISS-030; /who-we-help rewrite, ISS-009).
- Page copy: PAGE-IMPROVEMENTS.md packages for /, the assessment page, /scorecard (label sentence and the server-rendered "After your results" block), /about, /faqs.
- /llms.txt (ISS-023): description line "Founder-led Salesforce consulting for nonprofit, government, and mission-driven organizations." -> "Architect-led Salesforce AI governance, data governance, and implementation for nonprofit, government, healthcare, and enterprise organizations." (FACT-01); Trailblazer link -> https://www.salesforce.com/trailblazer/jeremy-carmona; remove the personal-brand Instagram line (decision 4); add "Contact: contact@clearconciseconsulting.com"; replace the em dash in the closing paragraph. Full revised file: implementation/llms.approved.txt.
- URL mapping (ISS-021): add `/blog/category/Career+Transition+Resources -> /resources/beginners-career-changers 301` in Settings > Advanced > URL Mappings.
- Alt text (ISS-029), H1 fix on the scorecard page (ISS-034), three H1s on /ai-coe-practice-map reduced to one.

## Batch 8. Held until canon is reconciled
- ISS-039 AI CoE service ladder; ISS-042 remediation rows and the $1,500 to $3,000 retainer row on /services/data-governance. The owner updates Positioning and Offers in Confluence or retires the content. No edit before that.

## Batch 9. After publishing
- Validate each edited page's raw HTML in the Rich Results Test (not the rendered DOM).
- Re-run evidence/tools/ccc_bounded_crawl.py on the core pages and record the next EV.
- Record in Confluence: Decision P1 (Gumroad), contact@, any CoE ladder change, so canon matches the site.
