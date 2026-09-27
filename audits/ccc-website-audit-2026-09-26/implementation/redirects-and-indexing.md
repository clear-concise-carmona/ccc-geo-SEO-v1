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
| /home | 200, in sitemap | duplicate homepage URL; canonical not read (ISS-036) |
| https://clearconciseconsulting.squarespace.com/ (root, /faqs, /services) | 200, no redirect | mirror host serves the site (ISS-001 open) |
| mirror /ai-services, /salesforce-consulting-services | 301 within the mirror host | redirects do not leave the mirror |
| mirror /services/non-profit | 404 | |

Every Squarespace URL-mapping redirect observed returns an http:// Location first, then 301s to https:// (two hops). Platform behavior; no owner control identified (ISS-032).

## B. URL Mappings status

The three owner-confirmed mappings (/about-ccc, /about-section, /nonprofit-salesforce-consulting) are live. No new mapping is proposed except, at the owner's option:

```
/new-clients -> /contact 301
/blog/category/Career+Transition+Resources -> /resources/beginners-career-changers 301
```
Both are optional; honest 404s are acceptable for pages with no traffic evidence.

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
A rel=canonical instruction is not a substitute for the information-architecture decisions in QUERY-PAGE-MAP.csv. Consolidations use 301s; differentiations use distinct titles and cross-links; canonicals stay self-referencing. Check /home in the second pass: if it does not canonicalize to /, ask Squarespace support how to remove it from the sitemap.

## G. Rate limits for verification
Squarespace tolerated 1 request per second for 70 sequential requests with no 429 or 503 (EV-038). The owner-documented 8 to 10 seconds between curl calls remains the polite default for manual checks; always pass --compressed.
