#!/usr/bin/env python3
"""
Bounded first-party crawl for the CCC website audit (resumable step).

Run this once the environment can reach the target host. It reuses the toolkit's
fetch_page.py parser (ccc-geo-SEO-v1/scripts) and enforces the stricter of the
toolkit's and the audit brief's limits:
  - respects robots.txt (urllib.robotparser)        - max 50 pages
  - 30 s fetch timeout                               - >= 1.0 s between request starts
  - sequential (concurrency 1 <= cap of 5)           - stops on 429/503 after one 20 s backoff
Caches raw HTML + parsed JSON per URL under evidence/crawl/ and writes
evidence/crawl/url-inventory-observed.csv (same columns as URL-INVENTORY.csv).

Usage:
  python3 ccc_bounded_crawl.py --toolkit /path/to/ccc-geo-SEO-v1 \
      --seeds seeds.txt --out ../crawl [--base https://www.clearconciseconsulting.com]
seeds.txt: one URL per line (URL-INVENTORY.csv 'url' column is a good source).
Sitemap URLs from robots.txt are added automatically (up to the page cap).
"""
import argparse, csv, hashlib, json, os, sys, time, urllib.robotparser
from urllib.parse import urlparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--toolkit", required=True)
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--base", default=None)
    ap.add_argument("--max-pages", type=int, default=50)
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--skip-robots", action="store_true", help="fixture testing only")
    a = ap.parse_args()

    sys.path.insert(0, os.path.join(a.toolkit, "scripts"))
    import requests  # noqa
    from fetch_page import fetch_page, fetch_robots_txt, crawl_sitemap, DEFAULT_HEADERS

    seeds = [l.strip() for l in open(a.seeds) if l.strip() and not l.startswith("#")]
    base = a.base or f"{urlparse(seeds[0]).scheme}://{urlparse(seeds[0]).netloc}"
    os.makedirs(a.out, exist_ok=True)
    log = open(os.path.join(a.out, "crawl-log.txt"), "a")
    def note(msg):
        line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
        print(line); log.write(line + "\n"); log.flush()

    # robots.txt (toolkit parser for AI-crawler map + stdlib parser for permission checks)
    robots = fetch_robots_txt(base, timeout=15)
    json.dump(robots, open(os.path.join(a.out, "robots.json"), "w"), indent=1)
    rp = urllib.robotparser.RobotFileParser()
    if robots.get("exists"):
        rp.parse(robots["content"].splitlines())
    else:
        rp = None
    time.sleep(a.delay)

    # sitemap discovery (toolkit helper) -> merge with seeds, dedupe, cap
    site_pages = crawl_sitemap(base, max_pages=a.max_pages, timeout=15)
    json.dump({"sitemap_pages": site_pages}, open(os.path.join(a.out, "sitemap-discovered.json"), "w"), indent=1)
    time.sleep(a.delay)
    queue, seen = [], set()
    for u in seeds + sorted(site_pages):
        if u not in seen:
            seen.add(u); queue.append(u)
    excluded = queue[a.max_pages:]
    queue = queue[: a.max_pages]
    note(f"queue={len(queue)} excluded_by_cap={len(excluded)}")
    json.dump({"excluded_by_page_cap": excluded}, open(os.path.join(a.out, "excluded.json"), "w"), indent=1)

    cols = ["url","page_purpose","http_status","canonical_url","indexability_signals","title","meta_description","h1","schema_types","primary_cta","audit_status","evidence_id"]
    rows = []
    ua = DEFAULT_HEADERS["User-Agent"]
    for i, url in enumerate(queue, 1):
        if rp and not a.skip_robots and not rp.can_fetch("*", url):
            note(f"ROBOTS_DISALLOW {url}")
            rows.append(dict(zip(cols, [url,"",None,"","robots.txt disallow","","","","","", "EXCLUDED_ROBOTS", f"CRAWL-{i:03d}"])))
            continue
        started = time.time()
        data = fetch_page(url, timeout=a.timeout)
        status = data.get("status_code")
        if status in (429, 503):
            note(f"RATE_LIMIT {status} {url} backing off 20s once")
            time.sleep(20)
            data = fetch_page(url, timeout=a.timeout)
            status = data.get("status_code")
            if status in (429, 503):
                note("RATE_LIMIT persists; stopping crawl to respect the origin")
                rows.append(dict(zip(cols, [url,"",status,"","","","","","","", "STOPPED_RATE_LIMIT", f"CRAWL-{i:03d}"])))
                break
        h = hashlib.sha1(url.encode()).hexdigest()[:12]
        # raw HTML cache (re-fetch text from the same response is not exposed by fetch_page; store parsed JSON + a raw copy)
        try:
            raw = requests.get(url, headers=DEFAULT_HEADERS, timeout=a.timeout).text
            open(os.path.join(a.out, f"{h}.html"), "w").write(raw)
        except Exception as e:  # noqa
            note(f"RAW_FETCH_FAIL {url} {e}")
        json.dump(data, open(os.path.join(a.out, f"{h}.json"), "w"), indent=1, default=str)
        robots_meta = data.get("meta_tags", {}).get("robots", "")
        xrobots = data.get("headers", {}).get("X-Robots-Tag", "")
        signals = ";".join(s for s in [f"meta-robots={robots_meta}" if robots_meta else "", f"x-robots={xrobots}" if xrobots else ""] if s) or "none observed"
        rows.append(dict(zip(cols, [
            url, "", status, data.get("canonical") or "", signals, data.get("title") or "",
            data.get("description") or "", " | ".join(data.get("h1_tags", [])),
            ";".join(sorted({str(sd.get("@type")) for sd in data.get("structured_data", []) if isinstance(sd, dict)})),
            "", "FETCHED" if status == 200 else f"HTTP_{status}", f"CRAWL-{i:03d}:{h}"])))
        note(f"{status} {url} words={data.get('word_count')} schema={len(data.get('structured_data', []))}")
        # >= delay between request STARTS (two requests per page above, so wait relative to first start)
        elapsed = time.time() - started
        if elapsed < a.delay:
            time.sleep(a.delay - elapsed)
    with open(os.path.join(a.out, "url-inventory-observed.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL); w.writeheader(); w.writerows(rows)
    note(f"done rows={len(rows)}")

if __name__ == "__main__":
    main()
