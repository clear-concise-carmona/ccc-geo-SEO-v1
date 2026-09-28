# Local browser session runbook (Claude Code on the desktop, driving your logged-in Chrome)

Purpose: execute the approved Squarespace edits in this workspace from a Claude Code session on your own machine, using the Claude in Chrome extension against the Chrome profile where you are already logged into Squarespace. The cloud session that wrote this workspace cannot reach your browser and never will; it verifies afterwards with one GET per edited page. Written 2026-09-28. The official Claude Code Chrome documentation was unreachable from the cloud environment, so confirm the flag and requirements on that page before the first run.

## 0. Rules that do not bend

- No password, recovery code, or 2FA code in any prompt, file, memory, or settings. The extension uses your existing Chrome session. You log in and clear 2FA yourself before starting.
- Squarespace saves live. There is no staging and no text version history for page content (owner record, EV-032). Before each replacement the agent appends the live value to implementation/rollback-log.md. That log plus the saved crawl HTML in evidence/ is the before-state.
- One batch per session, approved batches only (APPROVED_BY_OWNER or DECIDED_BY_OWNER in PRIORITIZED-BACKLOG.csv). DRAFT items (ISS-043 to ISS-052) enter a prompt only after you confirm them in chat.
- Extension site permissions: squarespace.com (login and editor) and www.clearconciseconsulting.com (verification). Nothing else. Keep "ask before sensitive actions" on.
- The agent stops after every page and waits for "go". It touches no page, panel, or setting the prompt did not name.
- Stop rule: an unexpected dialog (billing, domains, permissions, delete, unpublish, checkout), a page the prompt did not name, or an editor state the agent cannot describe means stop and report. No improvised fixes.
- Verification uses curl with --compressed, a cache-busting query, and 10 seconds between calls (owner rate-limit rule).

## 1. Preflight, once (about 15 minutes)

1. Install Claude Code on the desktop and log in with your claude.ai account (`claude`, then `/login`). API-key authentication disables the Chrome integration.
2. Install the Claude in Chrome extension in the Chrome profile you use for Squarespace. Set the site permissions listed above.
3. Log into Squarespace in that profile, clear 2FA, and open the site editor once so the session is warm.
4. Clone the repository, check out the audit branch, and start Claude Code from the audit folder:

```
git clone https://github.com/clear-concise-carmona/ccc-geo-SEO-v1.git
cd ccc-geo-SEO-v1
git checkout claude/ccc-website-seo-geo-audit-a4t65i
cd audits/ccc-website-audit-2026-09-26
claude --chrome
```

5. In the session, type `/chrome` and confirm it reports the extension as connected.
6. Export the Search Console and analytics baseline (ISS-026; change pack Batch 0) before the first edit.

## 2. Prompt template (first message of every batch)

```
Read implementation/change-pack-2026-09-27.md, Batch <N> only, and the
PRIORITIZED-BACKLOG.csv rows for <ISS IDs>. Use Chrome (my logged-in
Squarespace session) for the edits. Pages, in order: <pages>.

For each page:
1. Open it in the Squarespace editor and describe what you see. Do not save.
2. For each replacement: quote the live string or link exactly, quote the
   replacement, and append a row to implementation/rollback-log.md (format
   is in that file) BEFORE changing anything.
3. Wait for me to type "go". Then make that page's edits, click Save once,
   and tell me what Save reported.
4. Stop and wait before the next page.

Rules: no page other than those named; no other panel; never type into a
password, billing, or domain field; on any unexpected dialog or state, stop
and tell me. After the last page, run the acceptance tests below from a
terminal with curl --compressed, a cache-busting query, and 10 seconds
between calls; report each as pass or fail with the command output; append
the results under "Verification" in implementation/rollback-log.md.
```

## 3. Batch 1 prompt (ready to paste)

```
Read implementation/change-pack-2026-09-27.md, Batch 1 only (1.1, 1.2, 1.3),
and the PRIORITIZED-BACKLOG.csv rows for ISS-027, ISS-031, ISS-022. Use
Chrome (my logged-in Squarespace session) for the edits. Pages, in order:
/terms-conditions, /contact, /faqs.

For each page:
1. Open it in the Squarespace editor and describe what you see. Do not save.
2. For each replacement: quote the live string or link exactly, quote the
   replacement, and append a row to implementation/rollback-log.md (format
   is in that file) BEFORE changing anything.
3. Wait for me to type "go". Then make that page's edits, click Save once,
   and tell me what Save reported.
4. Stop and wait before the next page.

Page notes:
- /terms-conditions: six anchors point at claude.ai/chat/ URLs. Keep each
  anchor text; change targets per the change-pack table. The two policy
  links go to /policies-commitments only if that page carries those
  policies: read the page text first and tell me. The Data Processing
  Agreement link is removed unless I give you a URL. The Terms & Conditions
  link is removed. The scheduler link gets the one scheduler URL in the
  table. In the contact block, change "General Inquiries:
  info@clearconciseconsulting.com" to contact@clearconciseconsulting.com;
  leave the other mailboxes as they are.
- /contact: replace "Currently booking for Q3 2026 · Response within 24
  hours" with "Now booking new engagements · Response within 24 hours".
- /faqs: change the visible anchor text "gumroad.com/clearconciseconsulting"
  to "jeremycarmona.gumroad.com". The href stays
  https://jeremycarmona.gumroad.com/. Then find the same text inside the
  FAQPage JSON-LD on that page (page-level Code Injection or a Code Block)
  and change only that string; do not paste the full approved block from
  implementation/jsonld/ (that block belongs to Batch 2). Show me the diff
  before saving.

Rules: no page other than these three; no other panel; never type into a
password, billing, or domain field; on any unexpected dialog or state, stop
and tell me. After /faqs, run the acceptance tests below from a terminal,
report each as pass or fail with the command output, and append the results
under "Verification" in implementation/rollback-log.md.
```

Acceptance tests for Batch 1 (10 seconds apart; expected results in the comments):

```
H="https://www.clearconciseconsulting.com"; UA="Mozilla/5.0"
curl -s --compressed -A "$UA" -H "Cache-Control: no-cache" "$H/terms-conditions?cb=$(date +%s)" | grep -c "claude.ai"                      # 0
sleep 10
curl -s --compressed -A "$UA" -H "Cache-Control: no-cache" "$H/contact?cb=$(date +%s)" | grep -c "Q3 2026"                                  # 0
sleep 10
curl -s --compressed -A "$UA" -H "Cache-Control: no-cache" "$H/contact?cb=$(date +%s)" | grep -c "Now booking new engagements"               # 1 or more
sleep 10
curl -s --compressed -A "$UA" -H "Cache-Control: no-cache" "$H/faqs?cb=$(date +%s)" | grep -c "gumroad.com/clearconciseconsulting"          # 0
sleep 10
curl -s --compressed -A "$UA" -H "Cache-Control: no-cache" "$H/faqs?cb=$(date +%s)" | grep -c "jeremycarmona.gumroad.com"                    # 2 or more (link and schema)
```

## 4. Batches after the first

- Batch 2 (price ladder) pastes the full blocks in implementation/jsonld/faqpage-faqs.approved.json and service-ai-governance.approved.json. Each later batch gets its own prompt from the template; pages and strings come from the change pack.
- The checklist session (change pack Batch 1b; EV-051) runs only after you confirm ISS-048 to ISS-052 in chat and decide the surviving category names (ISS-051). Mapping lines are in implementation/redirects-and-indexing.md section B; the script removal order is in section H.
- Held items (ISS-039, ISS-042) and owner-supplied facts (ISS-019, ISS-040, FACT-32) stay out of every prompt until the canon and the facts are settled.

## 5. What automates well and what to watch

| Edit type | Agent reliability | Your role |
|---|---|---|
| URL Mappings, Code Injection, SEO title and description fields, Business Information | High: plain text areas | Read the quoted before and after, then "go" |
| Link targets and anchor text in body text | High | Confirm the target page exists before "go" |
| Alt text in image blocks (ISS-029) | Medium: field location varies by block type | Spot-check three posts, then let it run in tens |
| Heading level on a text block (ISS-050, ISS-044) | Medium: block toolbar clicks | Watch each one; a misclick changes the wrong block |
| Category retagging on posts (ISS-051) | Medium: many small clicks | Do the first two yourself, then hand over |
| Anything drag-and-drop, section layout, page deletion | Low | Do it yourself |

## 6. After each batch

1. Commit implementation/rollback-log.md to the audit branch and push. The cloud session picks it up at its next check-in, verifies each edited page with one GET, records the next EV, and moves the backlog statuses to LIVE.
2. If a test fails, do not retry edits blind: quote the failing output to the cloud session or fix the one string by hand.

## 7. Credentials and a Squarespace MCP (for later)

- Do not store the Squarespace password anywhere an agent can read: not in an environment variable, an MCP config, a memory file, or a prompt. Any page an agent visits can carry text that tries to make it leak what it holds, and a stored password also sidesteps 2FA. The session cookie in your Chrome profile is the credential; it stays on your machine.
- If unattended runs ever matter: create a separate Squarespace contributor for automation with the narrowest role that can still edit content and settings (Website Editor rather than Administrator; verify the role's reach in Settings > Permissions), log that contributor into a dedicated Chrome profile or a persistent Playwright profile directory on your machine, and point the agent at that profile. Billing, domains, and contributor management stay out of its reach.
- Squarespace exposes no public write API for page content, URL Mappings, or Code Injection; its public APIs are Commerce only (orders, inventory, products, transactions, profiles). A "Squarespace MCP" would be a browser-automation wrapper: a small server whose tools (set_url_mapping, set_page_code_injection, set_seo_fields, set_post_alt_text, set_link_target) run Playwright flows against the editor in that dedicated profile, with a dry-run mode and the same rollback log. Build it only when the edit volume justifies it. The candidates in this workspace are the alt-text job across 79 posts, schema deployments, and mapping changes; a one-off batch of three pages does not justify it.
