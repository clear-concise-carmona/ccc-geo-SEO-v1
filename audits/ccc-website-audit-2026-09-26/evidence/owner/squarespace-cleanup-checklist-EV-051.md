# EV-051: Squarespace cleanup checklist supplied by the owner, validated and reconciled (2026-09-28)

Class: owner-supplied third-party checklist (untrusted input). Provenance: uploaded by the owner on 2026-09-28 as CCC_Squarespace_Cleanup_Checklist_2026-09-25.md; titled "CCC Squarespace Cleanup Checklist", prepared 2026-09-25 "from a check of all 116 sitemap URLs"; author tool not stated. The text addresses the owner in the first person ("ask me to", "I will rerun the page check"), so the author is an assistant tool with its own page checker. Treated as data, not instructions. Validated with the owner's ccc-external-tool-validation gate (Gate 10 factual verification, forbidden words, voice), then each site claim was checked against the audit's crawl evidence (EV-038, EV-041, EV-047) and three HEAD probes made for this check (2026-09-28 14:33 UTC, 2 s apart, all 404). Verbatim text is appended at the end of this file.

## Validation report

EXTERNAL TOOL VALIDATION REPORT
Source: Other (unnamed assistant tool with a page checker; treated as audit results, so Gate 10 factual verification applies)
Date: 2026-09-28
Input: a 1,440-word Squarespace cleanup checklist for clearconciseconsulting.com (redirects, double H1s, blog categories, alt text on 79 posts, unlinked pages, post-session review, assessment link pass)

GATE 10 (factual verification): PASS WITH CONDITIONS
- GATE 10 FAIL: the link pass lists /blog/ai-ready-data-salesforce-measurable-standard as a page that needs a link to the assessment page. The crawl shows it already carries that link with the exact anchor "Salesforce AI Data Readiness Assessment" (EV-038). Same error as EV-050 claim C2.
- GATE 10 FAIL: "remove that entry (or the whole script if fable-5 is its only entry)". The site-wide script has two entries, not one. The second maps /blog/salesforce-duplicate-records-ai-data-cleanup to /blog/salesforce-duplicate-management-guide, its source URL also returns 404 at the server (HEAD 2026-09-28), and the raw HTML of the measurable-standard post still links that dead URL (anchor "duplicates and identity resolution"). There are also two scripts, not one: a link rewriter and a location.replace redirect, both carrying both entries (EV-038, EV-047).
- GATE 10 FAIL (scope): "All of them are blog posts; the homepage, service pages, assessment page, and scorecard are already fine". The four named page types are fine in the crawl data. Two other pages are not: /about (1 of 3 images without alt text) and /services/salesforce-nonprofit-consulting (2 of 4), neither on the checklist (EV-038).
- UNVERIFIED: five of the six posts listed with two H1s were not crawled (the security guide was: two H1s confirmed). H1 counts on the 11 category archives were not read. Per-post alt-text counts for the 56 listed posts outside the crawl are the checklist's own; the 23 posts common to both lists match exactly.
- UNVERIFIED: the ordering of section 4a as "the pages that get the most search traffic" (Search Console; consistent with the July figures in EV-050, which were also unverified).
- UNVERIFIED: a post-title heading-level control in Design > Site Styles. The owner's operations record documents only a JavaScript rewrite as the known fix (EV-032), and Confluence closed the /blog H1 item as Won't Fix (EV-045, ISS-012). The checklist hedges correctly ("if the template has no such setting, note it and skip").
- UNVERIFIED: whether a URL Mapping for /home fires when the homepage still owns that slug. The canonical on /home already points at / (EV-047), so the outcome is low-stakes either way.
- UNVERIFIED origin: /blog//blog/npsp-to-nonprofit-cloud-migration-tools and /blog/c2FsZXNmb3 appear in no crawled HTML (60 pages), the sitemap, or the search-index sample. Both return 404 (HEAD 2026-09-28). The checklist does not say where they came from.
- Dates are specific (Monday review from 2026-09-28; alt-text target 2026-10-31). No product or GA claims. No internal contradictions found; the arithmetic checks (79 posts, 131 missing images, 167 images listed; 7 + 12 = 19 pages with more than one H1; 11 category URLs in the sitemap).

FORBIDDEN WORDS: PASS
- 0 violations in prose (167-word list, whole-word and phrase matches). Two live URL slugs contain "harnessing" and "mastering"; they are URLs the site already publishes, not copy (ISS-020 covers the live titles).

VOICE COMPLIANCE: N/A (internal checklist, not publication copy). Incidentally clean: 0 em dashes, 0 conjunction openers. The bracket checkboxes are fine here; they are banned only in content pasted into Squarespace (owner formatting rule, EV-032).

URGENCY CHECK: No urgent items (not a Monthly Ops Review). The checklist's own dates: Monday review 2026-09-28; alt-text target 2026-10-31.

OVERALL: PASS WITH CONDITIONS
- Add the second redirect entry and fix the raw link on the measurable-standard post before either script is removed.
- Drop the measurable-standard post from the link pass, or only confirm its anchor.
- Add /about and /services/salesforce-nonprofit-consulting to the alt-text list.
- Treat the /home mapping as a test with a known fallback; read the canonical, not the status code, at the Monday review.
- Run the assessment link pass first, not "if time allows": it is the only P1 item in the checklist.

## Claim-by-claim check against the audit evidence

| # | Claim in the checklist | Audit evidence | Verdict |
|---|---|---|---|
| C1 | 116 sitemap URLs | EV-041: 116 (90 posts, 26 other pages) | Confirmed |
| C2 | /home returns the homepage as a page | EV-043 HEAD 200; EV-047 GET 200 with canonical https://www.clearconciseconsulting.com | Confirmed; the canonical already consolidates (ISS-036) |
| C3 | /blog//blog/npsp-to-nonprofit-cloud-migration-tools exists as a requested URL | Not in any crawled HTML, the sitemap, or the index sample; HEAD 2026-09-28: 404 | Status confirmed; origin unverified |
| C4 | /blog/c2FsZXNmb3 exists as a requested URL | Same; HEAD 2026-09-28: 404; the path is a base64 fragment ("salesfo") | Status confirmed; origin unverified |
| C5 | /blog/fable-5-salesforce-consultant-nyc-scoping should map to /services/salesforce-implementation | EV-050: 404 (HEAD); no raw href to it on any crawled page; the target matches the script | Confirmed |
| C6 | A site-wide JavaScript redirect map contains the fable-5 entry with that target ("confirmed") | EV-038, EV-047: present on every crawled page, in two scripts (href rewriter; location.replace) with two entries each | Confirmed and widened: a second entry exists |
| C7 | /ai-coe-practice-map has 3 H1s | EV-047: "AI COE PRACTICE MAP", "Most CoE diagrams are conceptual.", "The map is a reference. The practice is the implementation." | Confirmed |
| C8 | Six blog posts have 2 H1s | EV-038: /blog/salesforce-security-guide has 2; the other five were not crawled; no crawled page outside the list has more than one H1 apart from /blog | One confirmed, five unverified, no omissions found |
| C9 | The other 12 flagged pages are /blog and the category archives | EV-038: /blog has 21 H1s; EV-041: 11 category archives in the sitemap (not crawled) | /blog confirmed; archives consistent, unverified |
| C10 | 11 categories, two near-duplicate pairs; merging leaves 9 | EV-041 sitemap: Nonprofits and Nonprofit+Salesforce, Career+Development and Salesforce+Careers both listed | Confirmed. Added: the footer on every crawled page links /blog?category=Career Development (EV-038) |
| C11 | Site Styles may expose a post-title heading level | EV-032, EV-045: only a JS rewrite is documented; item closed Won't Fix | Unverified; the checklist's hedge accepted |
| C12 | 131 images on 79 posts lack alt text; the homepage, service pages, assessment page, and scorecard are fine | EV-038 toolkit image data: 23 of 23 overlapping posts match exactly; /, /services, assessment page, /scorecard, /faqs: 0 missing; /about 1 of 3 and /services/salesforce-nonprofit-consulting 2 of 4 missing | Confirmed for the overlap; two non-blog pages omitted |
| C13 | /services and the assessment page do not link to /faqs; /policies-commitments is footer-only | EV-038, EV-047: no /faqs link on either page; no crawled page links /faqs at all (header nav and footer lack it); /policies-commitments is in the footer of 56 crawled pages | Confirmed and widened: /faqs is an orphan |
| C14 | Baselines: missing alt 131; pages with more than one H1 19; category pages in sitemap 11; /home returns a page | See C12, C8, C9, C10, C2 | 11 and /home confirmed; 131 and 19 partly verified |
| C15 | Link pass: the checklist post, agentic-readiness-audit, agentforce-data-governance, measurable-standard, headless-360-vs-agentforce, /services/ai-governance (both sections), /scorecard, /org-health | ISS-043 (EV-050): same set except headless-360-vs-agentforce, which has 7 internal links and none to the assessment page (EV-038); the measurable-standard post already links it with the exact anchor | One addition correct; one entry already done |
| C16 | Assessment H1: lead with the offer name, keep the hook as the second line | ISS-044 (EV-050, EV-047) | Consistent; a second Heading 1 block would reintroduce a double H1 |
| C17 | Section 4a posts get the most search traffic | No Search Console access in this audit | Unverified |

## Reconciliation with the audit's decisions and backlog

| # | Checklist action | Audit position | Result |
|---|---|---|---|
| R1 | /home -> / 301 in URL Mappings | ISS-036 RESOLVED: canonical already points at /; a mapping on a live slug is unverified | Optional test; ISS-036 annotated; Monday metric should be the canonical |
| R2 | Map /blog//blog/... and /blog/c2FsZXNmb3 to live targets | Origin unknown; the owner's own rule keeps honest 404s for stale URLs with no source (EV-032) | Added as ISS-052: find the referrer first; mappings harmless if preferred |
| R3 | Map the fable-5 URL and remove the script entry | Two entries, two scripts, one raw dead link in a post | Added as ISS-049 (both mappings, the post link, then remove both scripts); ISS-046 annotated |
| R4 | Change body Heading 1 blocks to Heading 2 on seven pages | Two confirmed, five unverified; formatting only, so the ISS-039 hold on the CoE ladder does not block it | Added as ISS-050 |
| R5 | Merge two category pairs, add two mappings, check Site Styles | New; the footer category link must be repointed; ISS-021's approved mapping belongs in the same session | Added as ISS-051 (decision on the surviving names); ISS-021 annotated; ISS-012 annotated |
| R6 | Alt text on 79 posts, priority list first, target under 20 by 2026-10-31 | ISS-029 (approved) covered 41 of 99 images on crawled pages | ISS-029 widened to the checklist's list plus /about and the nonprofit service page |
| R7 | Body links to /faqs from /services and the assessment page | The audit had not noticed the orphan state; PKG-FAQS proposes cross-links from the cost post | New finding F-21; added as ISS-048 with a footer link as the site-wide fix |
| R8 | Leave /policies-commitments footer-only | Agreed | No change |
| R9 | Resubmit the sitemap in Search Console; Monday review against four baselines | ISS-026 baseline export; MEASUREMENT-AND-ROADMAP.md section 5 | Baselines recorded as owner-supplied; one metric reworded |
| R10 | Assessment link pass last, "if time allows" | ISS-043 is P1, the only P1 in the checklist | Reordered first; headless-360-vs-agentforce added; measurable-standard post removed |
| R11 | Assessment H1 with the hook as a second line | ISS-044 | One H1 (ISS-044 wording) or the hook as a Heading 2 or paragraph |
| R12 | Session location labels: Settings > Developer Tools | The audit's instructions file says Settings > Advanced | Same panel under Squarespace's current label; both kept, unverified in the account |

## Suggested order for the session (2 to 3 hours as estimated, reordered by payoff)

1. Assessment link pass (ISS-043, 15 minutes): seven pages plus the H1 (ISS-044).
2. URL Mappings session (10 minutes): ISS-049 (two lines), ISS-021 (one line, approved), ISS-051 (two lines, after the category decision), /home as a test. ISS-052 only after the referrer check.
3. Double H1s (ISS-050, 30 minutes) and the /faqs links (ISS-048, 15 minutes, footer first).
4. Change-pack Batch 1 (ISS-027, ISS-031, ISS-022; 20 minutes): the same editor session, higher payoff than the category merge.
5. Category merge (ISS-051) and alt text (ISS-029) as background work toward the 2026-10-31 target.

Requests made for this check: 3 HEAD requests to www.clearconciseconsulting.com (2026-09-28 14:33 UTC, 2 s apart, audit user agent, robots.txt honored). No pages were fetched; no forms touched.

## Verbatim text as supplied

# CCC Squarespace Cleanup Checklist

Site: clearconciseconsulting.com. Prepared September 25, 2026 from a check of all 116 sitemap URLs. Estimated time: 2 to 3 hours in one session. Work top to bottom; sections are ordered by risk and payoff.

Before starting:
- [ ] Log in to Squarespace and open the site editor
- [ ] Note today's date and time; the Monday review compares against the Sep 25 baseline

---

## 1. Redirects (10 minutes)

Location: **Settings > Developer Tools > URL Mappings**. Paste these lines exactly:

```
/home -> / 301
/blog//blog/npsp-to-nonprofit-cloud-migration-tools -> /blog/npsp-to-nonprofit-cloud-migration-tools 301
/blog/c2FsZXNmb3 -> /blog 301
/blog/fable-5-salesforce-consultant-nyc-scoping -> /services/salesforce-implementation 301
```

- [ ] Save the mappings
- [ ] The fable-5 target matches the existing site-wide JavaScript redirect map (confirmed). Open **Settings > Developer Tools > Code Injection**, find the script containing `oldPath` and `fable-5`, and remove that entry (or the whole script if fable-5 is its only entry)
- [ ] Test in a private window: each old URL should land on its target
- [ ] Optional check: https://www.clearconciseconsulting.com/home should no longer show the homepage at /home

---

## 2. Double H1 headings (30 minutes)

For each page: open it in the editor, find any text block styled **Heading 1** in the body, and change it to **Heading 2**. The page or post title stays the only H1.

- [ ] `/ai-coe-practice-map` (3 H1s)
- [ ] `/blog/5-tips-for-new-salesforce-admins` (2)
- [ ] `/blog/harnessing-salesforce-technologies-for-international-ngos` (2)
- [ ] `/blog/journalist-to-salesforce-admin-transition` (2)
- [ ] `/blog/nonprofits-lose-donations-giving-tuesday` (2)
- [ ] `/blog/salesforce-experience-cloud-guide` (2)
- [ ] `/blog/salesforce-security-guide` (2)

The other 12 flagged pages are /blog and the category archives. Those are fixed in section 3.

---

## 3. Blog category pages (45 minutes)

**Decision needed first:**
- [ ] Merge "Nonprofits" into "Nonprofit Salesforce"
- [ ] Merge "Career Development" into "Salesforce Careers"

(Or pick the other name of each pair. Either way, 11 categories become 9.)

To merge: open the blog, filter posts by the retiring category, add the kept category to each post, remove the retiring one. When the old category has no posts, it disappears.

- [ ] Add URL mappings for the retired categories:
```
/blog/category/Nonprofits -> /blog/category/Nonprofit+Salesforce 301
/blog/category/Career+Development -> /blog/category/Salesforce+Careers 301
```
- [ ] Blog list heading level: go to **Design > Site Styles**, select the blog page, and look for the post title heading setting. If it can be set to Heading 2 or Heading 3, change it. This fixes the H1 count on /blog and all category pages at once. If the template has no such setting, note it and skip; do not add custom code yet.

Not doing today: adding noindex to category pages with code. Only revisit if category pages start drawing impressions away from posts in Search Console.

---

## 4. Image alt text (60 to 90 minutes, can be split)

131 images across 79 pages have no alt text. All of them are blog posts; the homepage, service pages, assessment page, and scorecard are already fine.

How: click the image, open **Edit > Image**, fill in **Image Alt Text** (in some blocks it is the "Filename / Alt text" field or the caption). Describe what the picture shows in plain words, for example "Salesforce duplicate rule setup screen with matching rule selected". No keyword stuffing. Purely decorative images can stay empty.

### 4a. Priority posts first (the pages that get the most search traffic)
- [ ] `/blog/headless-360-vs-agentforce` (1 of 2 images)
- [ ] `/blog/how-much-does-a-salesforce-implementation-cost-in-2026` (2 of 2)
- [ ] `/blog/what-is-the-salesforce-einstein-trust-layer` (2 of 2)
- [ ] `/blog/salesforce-trust-layer-explained` (2 of 2)
- [ ] `/blog/salesforce-agentforce-data-governance` (2 of 2)
- [ ] `/blog/npsp-vs-nonprofit-cloud` (2 of 2)
- [ ] `/blog/salesforce-sandbox-management` (2 of 2)

### 4b. Everything else (most missing first)
- [ ] `/blog/end-of-year-salesforce-data-governance-checklist` (3 of 3 images)
- [ ] `/blog/nonprofit-data-quality-risks` (3 of 3 images)
- [ ] `/blog/nonprofit-salesforce-flow-governance-checklist` (3 of 3 images)
- [ ] `/blog/nonprofit-salesforce-validation-rules` (3 of 3 images)
- [ ] `/blog/ai-queries-in-search-console` (2 of 2 images)
- [ ] `/blog/beginners-guide-to-pardot` (2 of 2 images)
- [ ] `/blog/beginners-guide-to-salesforce-marketing-cloud` (2 of 2 images)
- [ ] `/blog/experience-cloud-screening-guide-for-recruiters` (2 of 2 images)
- [ ] `/blog/harnessing-salesforce-technologies-for-international-ngos` (2 of 2 images)
- [ ] `/blog/how-to-know-if-your-candidate-actually-knows-data-cloud` (2 of 2 images)
- [ ] `/blog/how-to-know-if-your-candidate-actually-knows-marketing-cloud` (2 of 2 images)
- [ ] `/blog/journalist-to-salesforce-admin-transition` (2 of 2 images)
- [ ] `/blog/managing-burnout-improving-productivity` (2 of 2 images)
- [ ] `/blog/mastering-salesforce-devops-best-practices-for-seamless-delivery` (2 of 2 images)
- [ ] `/blog/nonprofit-ai-tools` (2 of 2 images)
- [ ] `/blog/nonprofit-salesforce-data-migration` (2 of 2 images)
- [ ] `/blog/pardot-email-deliverability-bounce-rates` (2 of 2 images)
- [ ] `/blog/pardot-engagement-studio-drip-campaigns` (2 of 2 images)
- [ ] `/blog/pardot-lead-scoring-grading-setup` (2 of 2 images)
- [ ] `/blog/proportional-ai-governance-risk-tiers` (2 of 2 images)
- [ ] `/blog/sales-cloud-screening-guide-for-recruiters` (2 of 2 images)
- [ ] `/blog/salesforce-400-object-org-audit` (2 of 2 images)
- [ ] `/blog/salesforce-admin-templates-efficiency` (2 of 2 images)
- [ ] `/blog/salesforce-admin-vs-consultant-vs-architect-what-recruiters-need-to-know` (2 of 2 images)
- [ ] `/blog/salesforce-ai-data-readiness-checklist` (2 of 2 images)
- [ ] `/blog/salesforce-certification-decoder-for-recruiters` (2 of 2 images)
- [ ] `/blog/salesforce-data-governance-framework` (2 of 2 images)
- [ ] `/blog/salesforce-data-migration-checklist` (2 of 2 images)
- [ ] `/blog/salesforce-data-standardization-guide` (2 of 2 images)
- [ ] `/blog/salesforce-experience-cloud-guide` (2 of 2 images)
- [ ] `/blog/salesforce-flow-spaghetti-audit` (2 of 2 images)
- [ ] `/blog/salesforce-govcloud-implementation` (2 of 2 images)
- [ ] `/blog/salesforce-implementation-timeline` (2 of 2 images)
- [ ] `/blog/salesforce-integration-documentation` (2 of 2 images)
- [ ] `/blog/salesforce-knowledge-guide` (2 of 2 images)
- [ ] `/blog/salesforce-org-health-roadmap` (2 of 2 images)
- [ ] `/blog/salesforce-reports-data-quality` (2 of 2 images)
- [ ] `/blog/salesforce-security-guide` (2 of 2 images)
- [ ] `/blog/salesforce-sharing-model-architecture` (2 of 2 images)
- [ ] `/blog/salesforce-validation-rules-guide` (2 of 2 images)
- [ ] `/blog/service-cloud-screening-guide-for-recruiters` (2 of 2 images)
- [ ] `/blog/use-salesforce-templates-save-time` (2 of 2 images)
- [ ] `/blog/5-tips-for-new-salesforce-admins` (1 of 2 images)
- [ ] `/blog/accountability-named-human-owner-ai-deployment` (1 of 2 images)
- [ ] `/blog/ai-ready-data-salesforce-measurable-standard` (1 of 4 images)
- [ ] `/blog/ai-reversibility-rollback-plan` (1 of 2 images)
- [ ] `/blog/data-first-salesforce-ai-governance` (1 of 2 images)
- [ ] `/blog/fable-5-salesforce-flow-governance-automation` (1 of 2 images)
- [ ] `/blog/from-journalism-to-salesforce-my-unexpected-career-pivot` (1 of 2 images)
- [ ] `/blog/headless-360-data-governance` (1 of 2 images)
- [ ] `/blog/headless-360-nonprofits` (1 of 2 images)
- [ ] `/blog/human-oversight-salesforce-ai-deployment` (1 of 2 images)
- [ ] `/blog/i-hate-branding-unfortunately-it-matters` (1 of 6 images)
- [ ] `/blog/introducing-the-ccc-ai-center-of-excellence` (1 of 2 images)
- [ ] `/blog/linkedin-is-not-a-resume-its-a-signal` (1 of 4 images)
- [ ] `/blog/nonprofit-cloud-screening-guide-for-recruiters` (1 of 2 images)
- [ ] `/blog/nonprofits-lose-donations-giving-tuesday` (1 of 2 images)
- [ ] `/blog/npsp-to-nonprofit-cloud-migration-tools` (1 of 1 images)
- [ ] `/blog/placeholder-values-are-the-data-quality-problem-nobody-measures` (1 of 1 images)
- [ ] `/blog/salesforce-agentic-readiness-audit` (1 of 2 images)
- [ ] `/blog/salesforce-ai-governance-questions` (1 of 2 images)
- [ ] `/blog/salesforce-builder-gap-tdx-2026` (1 of 2 images)
- [ ] `/blog/salesforce-data-quality-ai-bottleneck` (1 of 2 images)
- [ ] `/blog/salesforce-duplicate-management-guide` (1 of 2 images)
- [ ] `/blog/salesforce-duplicate-records-find-and-fix-before-ai-scales-the-damage` (1 of 1 images)
- [ ] `/blog/salesforce-job-description-templates` (1 of 2 images)
- [ ] `/blog/salesforce-org-autopsy-assessment-checklist` (1 of 2 images)
- [ ] `/blog/salesforce-recruiter-cheat-sheet` (1 of 2 images)
- [ ] `/blog/salesforce-terminology-for-recruiters` (1 of 2 images)
- [ ] `/blog/six-governance-checkpoints-engagement` (1 of 2 images)
- [ ] `/blog/the-data-quality-delusion-salesforce-data-governance-comes-before-ai` (1 of 2 images)
- [ ] `/blog/transparency-ai-governance-documentation` (1 of 2 images)

Target: under 20 missing by October 31.

---

## 5. Unlinked pages (10 minutes)

- [ ] On `/services`, add a text link to `/faqs` (for example, "Common questions about working with CCC")
- [ ] On `/salesforce-ai-data-readiness-assessment`, add a link to `/faqs` near the existing FAQ section
- [ ] Leave `/policies-commitments` in the footer only

---

## 6. After the session

- [ ] In Search Console, resubmit `https://www.clearconciseconsulting.com/sitemap.xml` (or ask me to)
- [ ] Tell me which boxes are done; I will rerun the page check and confirm the counts
- [ ] The Monday review (starting Sep 28) will report progress against these baselines: missing alt 131, pages with more than one H1 19, category pages in sitemap 11, /home returning a page instead of a redirect

## Same session, if time allows: assessment page link pass

From Priority 1 of the SEO plan. Add a text link with the words **Salesforce AI Data Readiness Assessment** pointing to `/salesforce-ai-data-readiness-assessment` in the body of:
- [ ] `/blog/salesforce-ai-data-readiness-checklist`
- [ ] `/blog/salesforce-agentic-readiness-audit`
- [ ] `/blog/salesforce-agentforce-data-governance`
- [ ] `/blog/ai-ready-data-salesforce-measurable-standard`
- [ ] `/blog/headless-360-vs-agentforce`
- [ ] `/services/ai-governance` (in both assessment sections)
- [ ] `/scorecard` (short text above or below the widget: what happens after the scorecard)
- [ ] `/org-health`
- [ ] Assessment page H1: lead with "Salesforce AI Data Readiness Assessment", keep the current hook as the second line
