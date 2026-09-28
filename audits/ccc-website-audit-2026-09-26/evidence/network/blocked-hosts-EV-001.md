# EV-001: Network egress policy denials (this session)

Environment: Claude Code remote container; outbound HTTPS via policy-enforcing agent proxy. Denials are org/environment network policy, not site failures.
Collected: 2026-09-26T09:00Z to 09:12Z. Raw proxy status: agentproxy-status.json (recentRelayFailures).

Hosts denied with CONNECT 403 (curl) and/or EGRESS_BLOCKED (WebFetch):
- www.clearconciseconsulting.com  (audit target)
- clearconciseconsulting.squarespace.com  (built-in Squarespace domain)
- archive.org, web.archive.org  (public archive; would have provided dated snapshots)
- www.salesforceben.com, salesforcebreak.com, medium.com, engineering.nyu.edu  (third-party corroboration sources)
- developers.google.com, schema.org  (primary sources for structured-data requirements)
- www.soliantconsulting.com, www.demandchain.com  (competitor pages)

Hosts reachable: github.com (WebFetch), WebSearch tool (search-engine index only).
Not attempted: Playwright/Chromium against the target (same proxy path; policy denial would repeat). No retries beyond the single confirmation per host, per proxy guidance.

Consequence: no raw HTML, headers, robots.txt, sitemap, JSON-LD, rendered DOM, performance, or accessibility observation of the live site was possible in this run. All first-party page observations in this workspace come from search-engine index titles/snippets or owner-provided documentation, and are labeled as such.
Fix: add www.clearconciseconsulting.com (and, for archives/corroboration, web.archive.org, archive.org, www.salesforceben.com, developers.google.com, schema.org) to the environment's allowed domains, or raise the network access level, then run evidence/tools/ccc_bounded_crawl.py.
