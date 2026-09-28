# Redirects, URL mappings, and index hygiene

## A. Verified results (HEAD probes, 2026-09-27; EV-039, EV-043; crawler redirect_chain, EV-038)

| URL | Result | Meaning |
|---|---|---|
| http://clearconciseconsulting.com/, https://clearconciseconsulting.com/, http://www.clearconciseconsulting.com/ | 301 -> https://www.clearconciseconsulting.com/ | host and scheme canonicalization in place |
| https://clearconciseconsulting.com/services/salesforce-administration | 301 -> www /services/salesforce-implementation | legacy path redirected (ISS-002 closed) |
| https://clearconciseconsulting.com/services/ad-hoc-support | 301 -> www /services/salesforce-training | legacy path redirected (ISS-002 closed) |
| /about-ccc, /about-section | 301 -> /about | owner-reported mapping live (ISS-014 closed) |
| /nonprofit-salesforce-consulting | 301 -> /services/salesforce-nonprofit-consulting (200) | owner-reported mapping live (ISS-014 closed) |
| /services/salesforce-ai-data-preparation | 301 -> /salesforce-ai-data-readiness-assessment (200) | old assessment URL redirected; canonical on the target is self-referencing |
| /cart | 200, meta robots noindex, not in sitemap | index residual only (ISS-003 monitor) |
| /new-clients | 404 | still in the index sample; decide 301 to /contact or leave (ISS-009) |
| /blog/category/Career+Transition+Resources | 404 | dead category URL (ISS-021) |
| /home | 200, in sitemap | duplicate homepage URL; canonical to / read in pass 4 (EV-047; ISS-036 resolved) |
| https://clearconciseconsulting.squarespace.com/ (root, /faqs, /services) | 200, no redirect | mirror host serves the site (ISS-001 open) |
| mirror /ai-services, /salesforce-consulting-services | 301 within the mirror host | redirects do not leave the mirror |
| mirror /services/non-profit | 404 | |

Every Squarespace URL-mapping redirect observed returns an http:// Location first, then 301s to https:// (two hops). Platform behavior; no owner control identified (ISS-032).

## B. URL Mappings status

The three owner-confirmed mappings (/about-ccc, /about-section, /nonprofit-salesforce-consulting) are live. Mappings proposed since, for one session in Settings > Developer Tools > URL Mappings (older menus label the panel Settings > Advanced):

```
/blog/category/Career+Transition+Resources -> /resources/beginners-career-changers 301
/blog/fable-5-salesforce-consultant-nyc-scoping -> /services/salesforce-implementation 301
/blog/salesforce-duplicate-records-ai-data-cleanup -> /blog/salesforce-duplicate-management-guide 301
```
The first is approved (ISS-021). The next two replace the client-side redirect scripts (ISS-049; section H). After the category decision (ISS-051):
```
/blog/category/Nonprofits -> /blog/category/Nonprofit+Salesforce 301
/blog/category/Career+Development -> /blog/category/Salesforce+Careers 301
```
Test each in a private window: the plus-sign form of a category URL inside a mapping is unverified. Optional, from the owner checklist (EV-051) and ISS-009:
```
/home -> / 301
/new-clients -> /contact 301
```
/home already carries the canonical to / (EV-047); whether a mapping fires on a slug the homepage still owns is unverified, so treat it as a test with no downside. Two more 404 sources named in the checklist (/blog//blog/npsp-to-nonprofit-cloud-migration-tools and /blog/c2FsZXNmb3) appear in no crawled page and have no known referrer; find the source before mapping them (ISS-052). Honest 404s are acceptable for pages with no traffic evidence.

## C. Mirror host (ISS-001)

Squarespace is serving the built-in domain without redirecting it. Steps: (1) Settings > Domains: confirm www.clearconciseconsulting.com is the primary domain; (2) read Squarespace's current documentation on built-in domain behavior (some plans canonicalize rather than redirect); (3) if no redirect control exists, confirm with one GET on the mirror homepage (authorized in the second pass, ISS-035) that rel=canonical points at www; (4) request temporary removal of the mirror host prefix in Google Search Console and Bing Webmaster Tools; recrawl clears the rest.

## D. Plan required for ANY future URL change

1. Redirect: 301 from old to new in URL Mappings; test with curl -I (expect the http hop, then https).
2. Internal links: update every link to the old URL (search evidence/crawl/*.html for the old path first).
3. Sitemap: Squarespace regenerates sitemap.xml; confirm the old URL is gone and the new one present.
4. Canonical: confirm the new page's canonical is self-referencing (observed to be the Squarespace default).
5. Validation: GSC URL Inspection on old (redirect) and new (indexed); watch the 404 report for four weeks.
6. Rollback: remove the mapping and restore the page from Squarespace trash within 30 days.

## E. Index removals
- Mirror host: after C, request removal for the mirror host prefix; recrawl clears permanently.
- /cart: optional removal request; the noindex is already live.
- /new-clients, category archive: optional; 404s drop out on recrawl.

## F. Canonical vs editorial target
A rel=canonical instruction is not a substitute for the information-architecture decisions in QUERY-PAGE-MAP.csv. Consolidations use 301s; differentiations use distinct titles and cross-links; canonicals stay self-referencing. Pass 4 read the canonical on /home: it points at / (EV-047). The owner checklist's /home mapping is an optional test (section B).

## G. Rate limits for verification
Squarespace tolerated 1 request per second for 70 sequential requests with no 429 or 503 (EV-038). The owner-documented 8 to 10 seconds between curl calls remains the polite default for manual checks; always pass --compressed.

## H. Client-side redirect scripts (EV-051; ISS-049)

Every crawled page carries two scripts in the site-wide code injection: one rewrites anchor hrefs for two retired paths on DOMContentLoaded, and one calls window.location.replace when the browser lands on either path. Paths: /blog/fable-5-salesforce-consultant-nyc-scoping (to /services/salesforce-implementation) and /blog/salesforce-duplicate-records-ai-data-cleanup (to /blog/salesforce-duplicate-management-guide). Both paths return 404 at the server (HEAD, 2026-09-28). Crawlers, link checkers, and agents that do not run JavaScript see two dead URLs, and the raw HTML of /blog/ai-ready-data-salesforce-measurable-standard still links the second one (anchor "duplicates and identity resolution"). Order of work: add the two mappings in section B; edit the post link; confirm both old URLs return 301 with curl -I --compressed; then remove both scripts. Rollback: the scripts are preserved verbatim in the saved HTML under evidence/crawl-run2/.
