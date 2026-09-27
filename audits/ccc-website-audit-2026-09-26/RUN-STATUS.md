# RUN-STATUS: CCC website audit, 2026-09-26 (pass 1) and 2026-09-27 (pass 2)

## Identity
- Target: https://www.clearconciseconsulting.com/
- Toolkit: https://github.com/clear-concise-carmona/ccc-geo-SEO-v1, branch claude/ccc-website-seo-geo-audit-a4t65i, commit 383829485f8620e7ca20a333e16db023644f5545 (evidence/toolkit-revision.txt), unchanged across both passes. The fork was used as specified; no upstream update or install script was executed; toolkit code, docs, tests, and installers were not modified.
- Mode: AUDIT_AND_DRAFT. No website change was applied. No content was published. No live form, booking, or message was sent. No test lead was created.
- Workspace: audits/ccc-website-audit-2026-09-26/ on the branch above. Pass 2 worked directly in this committed copy; the pass-1 copy outside the repo (/home/user/ccc-website-audit-2026-09-26) was not updated and is superseded.
- Run windows (UTC): pass 1, 2026-09-26 08:59 to about 09:40; pass 2, 2026-09-27 17:27 to about 18:45.

## Environment and tools
- Pass 1: WebSearch (28 queries), one WebFetch (GitHub README), curl for proxy status. Target host, Squarespace built-in domain, archive.org, and every corroboration host were denied by the environment network policy (EV-001).
- Pass 2: the owner changed the environment's network access to Custom allowed domains. Target hosts became reachable (EV-040). pypi.org and files.pythonhosted.org were denied (x-deny-reason: host_not_allowed), so the toolkit requirements were installed offline from the local uv cache into .venv (beautifulsoup4, requests 2.34.2, lxml 6.1.3, playwright 1.63.0 package only; no browser run). Toolkit tests: 14 passed (pytest 9.1.1, also installed offline). web.archive.org: connection reset by the relay twice; not used. www.salesforceben.com: HTTP 403 from the origin; not retried. developers.google.com and schema.org: reachable; used for EV-043.
- Tools run against the target in pass 2: evidence/tools/ccc_bounded_crawl.py (toolkit fetch_page, fetch_robots_txt, crawl_sitemap); curl HEAD probes (20 URLs); the toolkit's citability_scorer.py run against the saved HTML through a local HTTP server, so no page was fetched twice.
- Not run: `/geo audit` (skills not installed; the brief bars overwriting Claude skills without approval), Playwright rendering, Lighthouse, brand_scanner.py (Reddit, YouTube, Wikipedia not allowlisted), llmstxt_generator.py (llms.txt already exists and was read directly).
- Request accounting for pass 2 against CCC-owned hosts: 50 GET (crawler, one per URL, 1.0 s apart) plus 20 HEAD (1 s apart) = 70 requests; sequential; robots.txt honored; no 429 or 503.

## Blocker status
- Pass-1 blocker (target host denied) cleared on 2026-09-27.
- Remaining constraints: (a) the 50-page cap was reached with 74 sitemap URLs unfetched, 10 of them non-blog pages; a second bounded pass needs owner authorization (ISS-035); (b) PyPI is denied, so a fresh container without the uv cache cannot install the requirements until the package-manager default list is re-enabled in the environment; (c) archive and Salesforce Ben corroboration remain impossible from this environment.

## Completed
Pass 1 (2026-09-26): toolkit inspection; index-based discovery (44 URLs); claims inventory (44); facts register (27 facts); entity map; query-page map (20); backlog (27); five page packages; measurement plan; implementation drafts; evidence folder; report.

Pass 2 (2026-09-27):
13. Live bounded crawl: 50 URLs (38 HTML 200, 2 HTML 404, robots.txt, sitemap.xml, llms.txt, 10 sitemap-discovered posts); EV-038; evidence/crawl/.
14. HEAD status probes: 20 URLs (non-www, built-in domain, canonical assessment URL, owner-reported redirect sources, /home, llms.txt targets); EV-039, EV-043.
15. URL-INVENTORY.csv rebuilt: 132 rows (47 FETCHED, 1 FETCHED_VIA_REDIRECT, 1 REDIRECTED_TO_CANONICAL, 2 HTTP_404, 2 REDIRECT_OBSERVED_HEAD, 6 HEAD_ONLY, 73 DISCOVERED_IN_SITEMAP_NOT_FETCHED), with live titles, descriptions, H1s, schema types, indexability signals, and CTAs.
16. BUSINESS-CLAIMS-INVENTORY.csv: 52 claims (30 rows updated with live evidence; CLM-045 to CLM-052 added).
17. PRIORITIZED-BACKLOG.csv: 38 items (ISS-027 to ISS-037 added; ISS-010, 013, 014, 017 resolved live; ISS-002, 003 downgraded to monitor; ISS-009, 019 raised to P1).
18. CANONICAL-BUSINESS-FACTS.md: 31 facts; live verification dates; 9 owner decisions.
19. ENTITY-MAP.md rebuilt from the deployed JSON-LD (three sameAs arrays, deployed @ids, profile set).
20. PAGE-IMPROVEMENTS.md, implementation/metadata-drafts.md, MEASUREMENT-AND-ROADMAP.md, QUERY-PAGE-MAP.csv, and every implementation/ file updated to the live state.
21. Citability heuristic on 45 saved pages (EV-042; evidence/citability/).
22. Primary-source checks: schema.org type pages; Google Search Central FAQPage and HowTo documentation (EV-043).
23. GEO-AUDIT-REPORT.md rewritten: 17 findings; five resolved-live items recorded.

## Not completed (and why)
- 10 non-blog and 64 blog sitemap URLs (50-page cap). Seeds for the second pass: evidence/tools/seeds-run2-priority.txt. Highest-value gap: /services/ai-governance (probable home of the $8,000 governance-assessment text) and the mirror homepage canonical.
- Composite GEO Score (pipeline not run; not estimated; component observations in the report, section 4).
- Rendering, Core Web Vitals, Lighthouse (no Playwright pass).
- Built-in domain canonicals and content (HEAD only).
- Third-party corroboration (Salesforce Ben, archive, Trailhead, NYU, BBB, LinkedIn).
- Competitor page review beyond snippets; brand-mention scan.
- Baseline analytics (no access provided).

## Assumptions recorded for owner review
- A1: Business goals as stated in the brief (paid assessment inquiries primary; scorecard engagement secondary) remain working assumptions.
- A2: RESOLVED. The CMS is Squarespace: `Server: Squarespace` response header, Squarespace robots.txt banner, squarespace-cdn asset hosts (EV-038).
- A3: RESOLVED. The assessment landing page is https://www.clearconciseconsulting.com/salesforce-ai-data-readiness-assessment; the pass-1 candidate URL 301s to it.
- A4: Owner strategy documents represent intent as of April to May 2026. Where they conflict with the live site (assessment price $8,000 vs $9,500), the live site is treated as current and the conflict is reported for decision.
- A5: REVISED. Search-index titles lagged the live site by weeks; they are treated as historical observations, not current state.
- A6: Committing the workspace to the toolkit fork's feature branch is acceptable for persistence and review; the owner may move it elsewhere.
- A7: The 30-question scorecard text (CLM-012) was a search-tool artifact or a retired version; it appears on none of the 45 crawled pages.
- A8: The suite-numbered Park Avenue South address published in the footer and schema reads like a mail-handling address. This is a hypothesis for the owner to confirm, not a finding.

## Approvals and decisions still required
CANONICAL-BUSINESS-FACTS.md "Owner decisions required": 9 items. No change ID has been approved. IMPLEMENT_APPROVED_LOCALLY does not apply (no website source files; Squarespace edits are made in the CMS; the scorecard instrument lives in the owner's ccc-artifacts GitHub Pages repository, which was not modified).

Two backlog items need no decision and can be fixed on sight: ISS-027 (six placeholder links on /terms-conditions) and the dated line in ISS-031 (/contact "Currently booking for Q3 2026").

## Resumable next action
1. Owner: authorize a second bounded pass of 10 pages (exceeds the 50-page audit cap by design; same limits otherwise), or accept the gap. Command from the toolkit repo root with the venv active:
   ```
   python3 audits/ccc-website-audit-2026-09-26/evidence/tools/ccc_bounded_crawl.py --toolkit . --seeds audits/ccc-website-audit-2026-09-26/evidence/tools/seeds-run2-priority.txt --out audits/ccc-website-audit-2026-09-26/evidence/crawl-run2 --max-pages 10
   ```
   Then merge the 10 rows into URL-INVENTORY.csv and re-score ISS-006 (with /services/ai-governance) and ISS-036 (/home canonical). If the owner also authorizes one GET on the mirror homepage, re-score ISS-001.
2. Owner: make the 9 decisions in CANONICAL-BUSINESS-FACTS.md; fix ISS-027 and the dated line in ISS-031.
3. Implementer: publish metadata and copy from PAGE-IMPROVEMENTS.md and implementation/metadata-drafts.md in the roadmap order (MEASUREMENT-AND-ROADMAP.md section 8), after the baseline export (ISS-026).
4. Re-run the crawler after publishing to refresh the before/after record.
