# EV-047: second bounded crawl pass (owner-authorized), 2026-09-27

Class: fetch (first-party, live). Authorization: owner message of 2026-09-27 ("yes to all other items you suggest is best"), recorded in owner/owner-decisions-EV-048.md, item 8.

## Method
- Tool: evidence/tools/ccc_bounded_crawl.py (toolkit fetch_page, fetch_robots_txt, crawl_sitemap), unchanged from pass 2.
- Seeds: evidence/tools/seeds-run2-priority.txt (10 non-blog URLs chosen in EV-041).
- Limits: --max-pages 10, --delay 1.0, --timeout 30, sequential, robots.txt honored (robots.json). The 50-page audit cap was exceeded by design with the owner's authorization; this run stayed under it on its own.
- Window (UTC): 19:34:50 to 19:35:01. Log: crawl-log.txt. Excluded by the cap: 10 sitemap URLs (excluded.json).
- One additional GET on https://clearconciseconsulting.squarespace.com/ (mirror-home.json; text content not stored) under the same authorization, to settle ISS-001.
- Requests to CCC-owned hosts this pass: 10 page GETs + robots.txt + sitemap.xml + 1 mirror GET = 13. Running total across passes: 85. No 429 or 503.
- Set-Cookie headers were removed from all saved JSON records before commit. The raw HTML is stored as fetched.

## Results
| URL | Status | Words | Schema types (raw HTML) | Citability avg (EV-049) | Note |
|---|---|---|---|---|---|
| /home | 200 | 737 | FAQPage;LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 39.9 (9 blocks) | canonical -> https://www.clearconciseconsulting.com; FAQPage twice |
| /services/ai-governance | 200 | 2833 | BreadcrumbList;LocalBusiness;Organization;Service;WebSite;['Organization', 'ProfessionalService'] | 43.5 (21 blocks) | visible "start at $5,000"; Service OfferCatalog 8000-15000 and 15000-40000 USD |
| /org-health | 200 | 613 | LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 37.1 (11 blocks) | "The assessment that costs $12,000 and saves $80,000"; present-tense NYU instructor tile |
| /case-studies | 200 | 233 | LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 29.5 (2 blocks) | "Real projects. Real numbers. Zero handoffs. Every CCC engagement..."; $30,000/$8,000 anecdote |
| /case-studies/government | 200 | 772 | CaseStudy;LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 35.4 (5 blocks) | "Federal Agency"; 8 weeks; 35 documentation assets; "CCC completed"; CaseStudy type |
| /case-studies/healthcare | 200 | 832 | CaseStudy;LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 50.6 (5 blocks) | "National Health Services Provider"; $8,000 assessment; 12,000 duplicates; CaseStudy type |
| /case-studies/nonprofit | 200 | 875 | CaseStudy;LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 53.0 (5 blocks) | 70,000+ records; $4.2M vs $42,000; "CCC delivered"; CaseStudy type |
| /ai-center-of-excellence | 200 | 1054 | BreadcrumbList;LocalBusiness;Organization;Service;WebSite;['Organization', 'ProfessionalService'] | 32.5 (15 blocks) | six-row service ladder (free / $8,000 / $18,000 / custom / custom / $3,500 / $2,500); Service + BreadcrumbList |
| /ai-coe-practice-map | 200 | 561 | LocalBusiness;Organization;WebSite;['Organization', 'ProfessionalService'] | 45.4 (5 blocks) | three H1s; reference page |
| /salesforce-ai-data-readiness-assessment | 200 | 1878 | LocalBusiness;Organization;Service;WebSite;['Organization', 'ProfessionalService'] | 40.1 (30 blocks) | direct GET; $9,500 and $2,500 confirmed; ancillary remediation price table |

Mirror homepage: 200, no redirect, rel=canonical https://www.clearconciseconsulting.com, no meta robots or X-Robots-Tag; all six internal links stay on the squarespace.com host.

## What this pass settled
- ISS-036: /home canonicalizes to /. No action.
- ISS-001: the mirror declares the www canonical; duplicate indexing is mitigated; re-scored to P3 monitor.
- ISS-006 scope: the retired $5,000 price is live on /services/ai-governance (visible) with an $8,000 to $15,000 schema price on the same page (ISS-038).
- New: an AI CoE service ladder not in the canon as read on 2026-09-27 (ISS-039); case-study attribution and labeling (ISS-040); /org-health price and credential tense (ISS-041); an ancillary remediation price table on the assessment page (ISS-042).

## Files
- <sha1-12>.html / .json per URL; url-inventory-observed.csv; robots.json; sitemap-discovered.json; excluded.json; crawl-log.txt; mirror-home.json.
