# Redirects, URL mappings, and index hygiene

## A. Checks to run first (after ISS-000), 8 to 10 seconds apart

```
for u in \
  https://clearconciseconsulting.squarespace.com/faqs \
  https://clearconciseconsulting.squarespace.com/ai-services \
  https://clearconciseconsulting.squarespace.com/services \
  https://clearconciseconsulting.squarespace.com/services/non-profit \
  https://clearconciseconsulting.squarespace.com/salesforce-consulting-services \
  https://clearconciseconsulting.com/services/salesforce-administration \
  https://clearconciseconsulting.com/services/ad-hoc-support \
  https://www.clearconciseconsulting.com/cart \
  https://www.clearconciseconsulting.com/about-ccc \
  https://www.clearconciseconsulting.com/about-section \
  https://www.clearconciseconsulting.com/nonprofit-salesforce-consulting \
  https://www.clearconciseconsulting.com/services/salesforce-nonprofit-consulting ; do
  curl -sS -I --compressed -H "User-Agent: Mozilla/5.0" "$u" | sed -n '1p;/^[Ll]ocation/p'; sleep 9; done
```
Expected: mirror and non-www URLs return 301 to the www equivalent; the three owner-confirmed sources return 301 after ISS-014; the nonprofit target returns 200.

## B. URL Mappings to add (owner-confirmed per EV-032; re-confirm before deploying)

```
/about-ccc -> /about 301
/about-section -> /about 301
/nonprofit-salesforce-consulting -> /services/salesforce-nonprofit-consulting 301
```
Two stale Bing-indexed URLs were classified by the owner as honest 404s with no target; leave them (EV-032).

## C. Plan required for ANY proposed URL change (assessment page rename, legacy page retirement, article consolidation)

1. Redirect: 301 from old to new in URL Mappings; test with curl -I.
2. Internal links: update every link to the old URL (search the crawl cache in evidence/crawl/*.html for the old path).
3. Sitemap: Squarespace regenerates sitemap.xml automatically; confirm the old URL is gone and the new one present.
4. Canonical: confirm the new page's canonical is self-referencing (Squarespace default).
5. Validation: GSC URL Inspection on old (redirect) and new (indexed); watch 404 report for four weeks.
6. Rollback: remove the mapping and restore the page from Squarespace trash within 30 days.

## D. Index removals
- Mirror host: after redirects are confirmed, request temporary removal for the mirror host prefix in GSC and Bing; recrawl clears permanently.
- /cart: after the control in squarespace-instructions.md is applied, request removal.

## E. Canonical vs editorial target
A rel=canonical instruction is not a substitute for the information-architecture decisions in QUERY-PAGE-MAP.csv. Consolidations use 301s; differentiations use distinct titles and cross-links; canonicals stay self-referencing.
