# Evidence index

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

Owner skill files are not copied into this workspace (they live in the owner's Claude skills directory); their relevant statements are quoted in the claims inventory with the EV ID.
