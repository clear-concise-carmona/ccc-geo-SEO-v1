# Evidence index

Two passes: 2026-09-26 (index-only; EV-001 to EV-037) and 2026-09-27 (live crawl after the allowlist change; EV-038 to EV-043). Times UTC.

| ID | File | Method | Collected (UTC) | Notes |
|---|---|---|---|---|
| EV-001 | network/blocked-hosts-EV-001.md; network/agentproxy-status.json; headers-mirror-home.txt (empty: request denied) | proxy status + curl/WebFetch denials | 2026-09-26 09:00 to 09:12 | policy denials, not site failures |
| EV-002 to EV-031 (excluding 007, 013) | search-results/EV-0xx.json | WebSearch tool: titles, URLs, snippet-derived observations | 09:00 to 09:11 | EV-013 (Squarespace CDN query) returned nothing attributable and was not saved; EV-020 saved as a null result |
| EV-007 | github-readme-fetch-EV-007.md | WebFetch of GitHub profile README | 09:03 | only successful direct fetch |
| EV-032 | owner skill: ccc-squarespace-operations v1.0 (2026-05-06) | owner-provided documentation, loaded in session | n/a | platform, deployed schema types, open items, scores as of April 2026 |
| EV-033 | owner skill: ccc-positioning-strategy | owner-provided | n/a | category, proof vault, product ladder |
| EV-034 | owner skill: ccc-conversion-psychology | owner-provided | n/a | CTA rules, intake call framing, $8,000 assessment |
| EV-035 | owner skill: ccc-audience-mapping | owner-provided | n/a | verticals, buyers, anti-personas |
| EV-036 | toolkit-revision.txt; pytest run (14 passed) | git + pytest | 09:05 | toolkit identity and health |
| EV-037 | tools/ccc_bounded_crawl.py; tools/fixture-test-output-EV-037.csv; tools/fixture-test-log-EV-037.txt | local fixture server test | 09:10 | proves the crawler runs; not a site observation |
| EV-038 | crawl/ (50 x .html + .json, url-inventory-observed.csv, robots.json, sitemap-discovered.json, excluded.json, crawl-log.txt, crawl-run-EV-038.md) | bounded live crawl with the toolkit's fetch_page (50-page cap, 1s delay, robots honored) | 2026-09-27 17:30 to 17:31 | 38 HTML 200, 2 HTML 404, robots.txt, sitemap.xml, llms.txt, 10 sitemap-discovered posts; 25 URLs excluded by the cap |
| EV-039 | network/head-probes-EV-039.txt | curl -I status probes (no bodies) | 17:28 to 17:33 | non-www redirects, built-in domain state, canonical assessment URL, redirect targets |
| EV-040 | network/allowlist-recheck-EV-040.md | host probes after the owner's allowlist change | 17:27 to 17:29 | target hosts allowed; PyPI denied (offline install); web.archive.org relay resets; salesforceben.com origin 403 |
| EV-041 | sitemap-analysis-EV-041.md; tools/seeds-run2-priority.txt | parse of the fetched sitemap.xml | 17:40 | 116 URLs; 74 not fetched (10 non-blog); lastmod near-uniform |
| EV-042 | citability/*.json; citability/citability-summary.csv | toolkit citability_scorer.py run against the saved EV-038 HTML through a local HTTP server (no refetch) | 17:45 | 45 pages; heuristic passage scores, not a citation measure |
| EV-043 | network/docs-corroboration-EV-043.md | HEAD probes for owner-reported redirect sources; schema.org type pages; Google Search Central FAQPage and HowTo docs | 17:50 | primary-source checks that were blocked on 2026-09-26 |

Owner skill files are not copied into this workspace (they live in the owner's Claude skills directory); their relevant statements are quoted in the claims inventory with the EV ID.
