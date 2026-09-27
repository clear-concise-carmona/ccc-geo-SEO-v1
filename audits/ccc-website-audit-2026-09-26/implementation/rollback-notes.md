# Rollback notes

| Change class | Rollback | Time to revert | Evidence to keep |
|---|---|---|---|
| SEO title / description / og edits | Re-enter the previous string from the crawl cache (evidence/crawl/*.json 'title' and 'description') | minutes | before/after JSON |
| Page body copy | Squarespace page version history or the saved before-state HTML in evidence/crawl/ | minutes | before HTML |
| JSON-LD in Code Injection | Restore the previous block from evidence/crawl/*.json 'structured_data' (exact prior JSON) | minutes | before JSON-LD |
| URL Mappings | Delete the mapping line; the old URL serves again if the page still exists | minutes | mapping list before/after |
| Page deletion | Restore from Squarespace trash (30-day window); never delete without a live mapping first | minutes within 30 days | page export |
| Footer JS (H1 rewrite) | Remove the script block | minutes | script text |
| Crawler toggle | Flip back; robots.txt regenerates | minutes plus recrawl | robots.txt before/after |
| Index removals | Cancel the temporary removal in GSC/Bing | hours to days | removal request IDs |
| Scorecard instrument (GitHub Pages, ccc-artifacts repository) | git revert of the commit that changed ccc-ai-readiness-scorecard.html; Pages redeploys | minutes | commit hash before/after |
| Squarespace Business Information (native schema source) | Re-enter the previous address, hours, and social links | minutes | screenshot of the settings page before the change |

No change in this workspace has been applied, so nothing currently needs rollback. The before-state of every fetched page is in evidence/crawl/ (raw HTML and parsed JSON, 2026-09-27).
