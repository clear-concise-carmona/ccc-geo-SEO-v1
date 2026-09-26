# Squarespace implementation instructions (owner-reported platform; verify each control on the live account)

Source for control locations: owner Squarespace operations document (EV-032). Controls marked [VERIFY] were not confirmed in this run.

| Issue | Change | Squarespace location | Notes |
|---|---|---|---|
| ISS-001 built-in domain indexed | Confirm primary domain and that the built-in domain 301s | Settings > Domains: primary domain set to www.clearconciseconsulting.com | Squarespace redirects the built-in domain automatically once a primary is set [VERIFY with curl -I on each mirror URL]. Then: Google Search Console > Removals (temporary) for the mirror host, and let recrawl clear the rest. |
| ISS-002 non-www duplicates | Confirm non-www 301s to www; check the two paths | Settings > Domains (www as primary) and Settings > Advanced > URL Mappings | If /services/salesforce-administration and /services/ad-hoc-support are live pages, give each a unique SEO title or map them 301 to the page that owns the topic. |
| ISS-003 /cart indexed | Prevent indexing of the cart | [VERIFY] Squarespace does not expose per-URL noindex for system pages; check Settings > Selling (if commerce is unused, disabling commerce removes /cart) or Marketing > SEO settings for "hide from search" | Also request removal in GSC. Record which control worked. |
| ISS-004 homepage title/og | Set SEO title and description; update social description | Home page > Settings > SEO > SEO Title / SEO Description; Settings > Marketing > Social Sharing > site description and image | Strings in metadata-drafts.md after approval. |
| ISS-005 scorecard method text | Edit page body and SEO description | /scorecard page editor; Settings > SEO | Also check the scorecard tool's own intro text if the instrument is embedded from a third-party tool [VERIFY tool]. |
| ISS-006 assessment page | Retitle, restructure headings, add Service JSON-LD | Page editor; Page > Settings > SEO; Page > Settings > Advanced > Code Injection (page-level) for Service schema | Only after FACT-15. If a new URL is chosen, follow redirects-and-indexing.md. |
| ISS-007 CTA durations | Edit button labels | Page editors (button blocks) | Consistent labels per FACT-09 decision. |
| ISS-008 contact address | Footer, contact page, schema contactPoint | Footer editor; /contact page; Header Code Injection (Organization block) | One address. |
| ISS-009 legacy pages | Rewrite or redirect | Page editor + Settings > SEO, or Settings > Advanced > URL Mappings + delete page | Never delete before the mapping is live. Noindex option: Page > Settings > SEO > "Hide this page from search results" [VERIFY exact label]. |
| ISS-010 default titles | Set SEO Title on nine pages | Each page > Settings > SEO > SEO Title | Use the " | Clear Concise Consulting" pattern; remove em dash. |
| ISS-011 Trust Layer articles | Retitle/cross-link or consolidate | Blog post editor; URL Mappings if consolidating | Decision after GSC review. |
| ISS-012 blog H1 fix | Deploy the owner-drafted DOM rewrite | Settings > Advanced > Code Injection > Footer | JS-side fix only; raw HTML keeps the H1s. Document this limitation. |
| ISS-013 og:description | Update | Settings > Marketing > Social Sharing | |
| ISS-014 three 301s | Add mappings | Settings > Advanced > URL Mappings | Format: /source -> /destination 301 (one per line). Confirm /services/salesforce-nonprofit-consulting exists first. |
| ISS-015 LocalBusiness | Remove or keep per decision | Settings > Advanced > Code Injection > Header | Suppression script for Squarespace's auto LocalBusiness stays as is (EV-032). |
| ISS-016 sameAs parity | Replace arrays in every block | Header Code Injection; Blog Settings > Advanced > Post Blog Item Code Injection; /about page Code Injection | Byte-identical arrays. Blog Settings injection does not render JSON-T variables: static values only. |
| ISS-024 AI crawlers | Check the crawler setting | [VERIFY] Settings > Crawlers (Squarespace offers a toggle to block known AI crawlers; name and location to be confirmed against current Squarespace help) | Decide retrieval vs training access explicitly; record in RUN-STATUS. |

Platform limits (owner-documented, no action): robots.txt cannot be edited directly; security headers cannot be added; render-blocking assets are platform-controlled; Cloudflare proxy is not an option.

Rate limits for verification: 8 to 10 seconds between curl calls to Squarespace (owner-documented) and always pass --compressed.
