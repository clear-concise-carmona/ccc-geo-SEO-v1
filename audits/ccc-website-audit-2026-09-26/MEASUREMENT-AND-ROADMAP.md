# Measurement Plan and 30/60/90 Roadmap

Workspace: ccc-website-audit-2026-09-26 | Status: DRAFT (no analytics access this run)

## 1. Baseline availability

| Measure | Availability this run | Source needed | Notes |
|---|---|---|---|
| Organic impressions and clicks (Google) | unavailable | Google Search Console (GSC) export, 16 months | Choose baseline and comparison windows per section 5 |
| Organic impressions and clicks (Bing) | unavailable | Bing Webmaster Tools | IndexNow is owner-reported as deployed (EV-032) |
| Branded vs non-branded discovery | unavailable | GSC query export with a brand regex (clear concise, ccc salesforce, jeremy carmona) | |
| Priority landing-page activity (/, assessment page, /scorecard, /about, /faqs) | unavailable | GA4 pages report | |
| Scorecard starts and completions | unavailable | scorecard tool events or GA4 custom events | Tool that runs the scorecard not identified this run |
| Assessment CTA clicks | unavailable | GA4 click events | |
| Form starts and successful submissions | unavailable | Squarespace form analytics or GA4 events | |
| Call bookings | unavailable | Zoom Scheduler (scheduler.zoom.us/jeremy-carmona) exports or outbound click events | |
| Qualified inquiries | unavailable | owner CRM or inbox tagging against the definition in section 4 | |
| AI referrals | unavailable | GA4 session source contains chatgpt.com, perplexity.ai, copilot.microsoft.com, gemini.google.com, claude.ai | Low volume expected; report counts, not rates |
| Live-site technical baseline | unavailable | evidence/tools/ccc_bounded_crawl.py after ISS-000 | Captures HTML, headers, JSON-LD, titles, canonicals before any change |

Missing measurements are recorded as unavailable, not zero.

## 2. Instrumentation plan (inspect existing tracking first)

Before adding anything: export the current GA4 event list, check whether Squarespace's built-in analytics or a GA4 tag is present, and confirm the consent mechanism (a GDPR cookie tool is referenced in owner context). Do not put names, emails, or free-text form content into event parameters.

| Event | Trigger | Success condition | Destination | Dedup | QA |
|---|---|---|---|---|---|
| scorecard_start | first question answered or "Start" clicked on /scorecard | event count = 1 per session on /scorecard | GA4 | once per session (session-scoped flag) | GA4 DebugView on desktop and mobile |
| scorecard_complete | results screen rendered | one per completion; parameter score_band (low/mid/high), no raw PII | GA4 (mark as key event) | once per completion id if the tool exposes one | complete a test run; confirm one event |
| assessment_cta_click | click on any CTA whose destination is the assessment page or an assessment inquiry | parameter cta_location (hero, footer, article, scorecard_results) | GA4 | none (clicks are countable) | click each CTA; verify parameter |
| form_start | first field focus on /contact form | one per session | GA4 | session-scoped | focus a field; verify |
| generate_lead | form submission confirmed (thank-you state) | one per submission; parameter form_id | GA4 key event | Squarespace confirmation page or success callback | submit via the owner's approved test plan only |
| call_booking_click | outbound click to scheduler.zoom.us | parameter cta_location | GA4 | none | click; verify |
| gumroad_click | outbound click to Gumroad | parameter product_slug if available | GA4 | none | click; verify |

Diagnostic events (clicks, starts) are reported separately from commercial outcomes (generate_lead, booked call, qualified inquiry). A CTA click is never counted as a lead.

Live form submissions, bookings, or test leads were not made and are not authorized. Test plan: implementation/form-test-plan.md.

## 3. Funnel definitions

| Stage | Definition | Page(s) | Primary CTA | Secondary CTA | Commercial purpose |
|---|---|---|---|---|---|
| Discovery | first session from search, AI referral, LinkedIn, Salesforce Ben, GitHub | articles, /, /about | article: contextual link to assessment or scorecard | none | none (credibility deposit) |
| Education | reads a governance or data-quality article; visits /faqs | articles, /faqs | assessment page link | scorecard | problem recognition |
| Trust | visits /about, case study, policies | /about, /case-studies/enterprise, /policies-commitments | book a call | read articles | risk reduction |
| Appropriate next step (two paths) | (a) high intent: /contact or scheduler directly; (b) mid intent: /scorecard | /contact, scheduler, /scorecard | (a) request assessment / book consultation; (b) start scorecard | (b) results call | qualification begins |
| Qualified conversation | free consultation held; fit assessed against section 4 | offline | scoping document | none | qualification |
| Paid assessment or engagement | fixed-price SOW signed | offline | none | none | revenue |

Rule: high-intent visitors are never diverted into the free scorecard as a required step. The scorecard is a side door for the undecided.

## 4. Qualified inquiry definition (PROPOSAL: owner must approve; no thresholds invented)

An inquiry is qualified when the owner confirms, after the free consultation, that:
- the organization runs Salesforce (not another CRM), and
- it is a nonprofit, government, healthcare, or enterprise organization, and
- the need involves AI governance, data governance or readiness, or implementation architecture (not offshore admin capacity or first-time setup), and
- the contact has budget or decision influence for a fixed-price engagement, and
- there is a stated timeframe.

Anti-persona matches from the owner's audience document (hourly-rate shoppers, "turn AI on, compliance later") are recorded as unqualified. The owner sets any budget floor; none is proposed here.

## 5. Baseline and comparison periods

- Baseline: the 12 full weeks before the first published change from this workspace. If GSC history allows, also pull the same 12 weeks one year earlier to check seasonality (September to December likely includes fiscal-year and grant-cycle effects for nonprofit and government buyers).
- Comparison: 12 full weeks after the last change in a batch is live and confirmed indexed. Do not read results before the recrawl window has passed.
- Log every concurrent change (blog publications, LinkedIn campaigns, Salesforce Ben articles, pricing edits) in evidence/change-log.csv so alternative explanations are visible. An increase after publication does not establish causation.
- Low volume: report counts with the observation window, not percentages, for anything under about 30 events per period.

## 6. Experiments for uncertain P2/P3 changes

Traffic volume is unknown; classical A/B tests are not prescribed. Before-and-after with guardrails is the proportionate design.

| ID | Hypothesis | Change | Pages | Primary metric | Guardrails | Window | Success | Stop / rollback |
|---|---|---|---|---|---|---|---|---|
| EXP-1 (ISS-007) | Naming the call's duration and purpose at every CTA reduces abandonment between CTA click and booking | CTA labels state "15-minute results call" or "30-minute scoping call" consistently | /, /scorecard, /faqs, /contact | call_booking_click to booking ratio (Zoom Scheduler export) | generate_lead count not lower than baseline | 12 weeks | ratio not lower; qualitative confusion reports drop | revert labels via Squarespace edit history |
| EXP-2 (ISS-011) | Differentiating the two Trust Layer articles increases combined impressions without cannibalizing | distinct titles, cross-links, one definitional and one configuration-focused | two blog URLs | combined GSC impressions and clicks for the query cluster | neither URL loses more than it gains; no 404s | 8 to 12 weeks | combined clicks not lower; one URL dominates the cluster | restore original titles; no redirects involved unless consolidated |
| EXP-3 (ISS-023) | llms.txt has no measurable effect on qualified inquiries; it is a consistency artifact | keep llms.txt aligned to the register | /llms.txt | AI referral sessions (count) | none | 12 weeks | any change is reported as observation only | remove file if it drifts from facts |
| EXP-4 (ISS-009) | Retiring or rewriting legacy pages does not reduce qualified inquiries | 301 or rewrite per owner decision | /new-clients, /who-we-help | qualified inquiries (count); GSC clicks to redirected URLs | no rise in 404s; no drop in brand impressions | 12 weeks | inquiries stable or up | remove redirects, restore pages from Squarespace trash |

## 7. AI visibility observation log (template, no results recorded this run)

For each check record: platform; date; exact prompt; settings (web search on/off, location); whether CCC is mentioned, cited (URL shown), or neither; which URLs are cited; competing brands cited; screenshot filename in evidence/ai-checks/. Suggested prompts: "Who offers a Salesforce AI readiness assessment for nonprofits?"; "Salesforce AI governance consultant for healthcare"; "What is the Einstein Trust Layer?"; "Jeremy Carmona Salesforce." Run monthly, same prompts, same settings. Distinguish mentions, citations, referrals (GA4), and qualified leads (owner CRM). None of these are promised outcomes.

## 8. 30/60/90-day roadmap (no results promised by any date)

**Days 0 to 30: unblock, baseline, decide**
| Step | Owner | Dependency | Approval | Review point |
|---|---|---|---|---|
| Allow the target host in the environment; run the bounded crawler; convert URL-INVENTORY rows to observed (ISS-000) | Jeremy or implementer | none | environment settings only | crawl output reviewed; findings re-scored where HTML contradicts the index |
| Export GSC, Bing, GA4 baselines; save to evidence/baseline/ (ISS-026) | Jeremy | account access | none | baseline saved before any publish |
| Owner decisions 1 to 8 in CANONICAL-BUSINESS-FACTS.md | Jeremy | none | these are the approvals | register updated; HOLD facts move to APPROVED or are withheld |
| Verify built-in domain and non-www redirects; fix /cart indexing (ISS-001, 002, 003) | implementer | crawl | Squarespace settings changes: owner approval | status codes confirmed |
| Deploy the three owner-confirmed 301s and the og:description update (ISS-013, 014) | implementer | none | already owner-confirmed per EV-032; confirm still wanted | curl checks |

**Days 31 to 60: truth and entity fixes**
| Step | Owner | Dependency | Approval |
|---|---|---|---|
| Publish homepage title/description and og tags (PKG-HOME, ISS-004) | implementer | decisions 1, 5 | metadata approval |
| Scorecard method statement (PKG-SCORECARD, ISS-005) | Jeremy | decision 2 | copy approval |
| FAQ corrections including client-name permissions (PKG-FAQS, ISS-018) | Jeremy | decision 3 | copy approval |
| About page corrections (PKG-ABOUT, ISS-017) | Jeremy | decisions 4 | copy approval |
| Schema reconciliation: sameAs parity, contactPoint, LocalBusiness decision (ISS-015, 016) | implementer | decisions 5, 7; crawl of deployed JSON | schema approval; validate on live URL |
| Custom SEO titles on the nine default-pattern pages (ISS-010) | implementer | none | metadata approval |

**Days 61 to 90: discovery and conversion**
| Step | Owner | Dependency | Approval |
|---|---|---|---|
| Assessment landing page (PKG-ASSESS, ISS-006) with Service schema | Jeremy + implementer | decision 1; deliverables list | copy, price, schema approval |
| Internal links from QUERY-PAGE-MAP.csv INTERNAL_LINK rows | implementer | assessment page live | none beyond copy |
| Trust Layer articles decision (ISS-011, EXP-2) | Jeremy | GSC data | editorial |
| Legacy pages decision (ISS-009, EXP-4) | Jeremy | GSC/GA4 data | redirect approval |
| First AI visibility observation log; first 12-week read scheduled | Jeremy | baseline | none |

Review points: end of each 30-day block, re-open PRIORITIZED-BACKLOG.csv, mark approval_status and outcomes, and update RUN-STATUS.md.
