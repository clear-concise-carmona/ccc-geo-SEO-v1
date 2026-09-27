# EV-038: bounded live crawl of www.clearconciseconsulting.com (2026-09-27)

- Command: `.venv/bin/python audits/ccc-website-audit-2026-09-26/evidence/tools/ccc_bounded_crawl.py --toolkit . --seeds <40 www URLs from URL-INVENTORY.csv> --out audits/ccc-website-audit-2026-09-26/evidence/crawl`
- Toolkit functions used: fetch_page, fetch_robots_txt, crawl_sitemap, DEFAULT_HEADERS from scripts/fetch_page.py at commit 383829485f8620e7ca20a333e16db023644f5545.
- Limits honored: robots.txt read first (all seeds allowed); 50-page cap; 1.0s delay; 30s timeout; sequential (1 concurrent). No 429/503 seen.
- Window (UTC): 2026-09-27T17:30:28Z to 2026-09-27T17:31:29Z. Rows written: 50 (38 HTML pages with 200, 2 HTML 404s, robots.txt, sitemap.xml, llms.txt, and 10 sitemap-discovered blog posts). Queue: 40 seeds + 35 new sitemap URLs = 75; 25 excluded by the cap (excluded.json).
- Files: <12-char sha1 of URL>.html (raw body) and .json (fetch_page output: status, redirect_chain, headers, meta_tags, title, description, canonical, h1_tags, heading_structure, word_count, text_content, links, images, structured_data, has_ssr_content, security_headers). url-inventory-observed.csv is the machine-readable summary; robots.json, sitemap-discovered.json, excluded.json, crawl-log.txt record the run.
- Not fetched (cap): 74 sitemap URLs including 10 non-blog pages (see sitemap-analysis-EV-041.md). No page on the built-in domain or non-www host was fetched (HEAD probes only, EV-039).
- Post-processing: EV-042 citability scoring was run against these saved files through a local HTTP server, so no page was fetched twice.
