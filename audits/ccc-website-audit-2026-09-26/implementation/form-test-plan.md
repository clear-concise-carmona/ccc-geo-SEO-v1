# Form, scorecard, and scheduler test plan (no live submissions authorized this run)

Purpose: verify conversion elements without creating leads, bookings, or test records the owner did not approve.

What the live HTML shows (2026-09-27, EV-038): /contact has no form element in its HTML; it embeds the Zoom scheduler (scheduler.zoom.us/jeremy-carmona/free-consultation) in an iframe and shows contact@ as a mailto. The assessment page's "Request an Assessment" button targets #application-form; no form element is in the HTML, so the form renders client-side; info@ is the visible fallback. /scorecard loads the instrument from an iframe on clear-concise-carmona.github.io/ccc-artifacts/. GA4 gtag.js and an app.sparkplugin.com script load on /scorecard.

| Element | Test | Method | Pass condition | Do not |
|---|---|---|---|---|
| Assessment page form (#application-form) | renders without errors; keyboard traversal; labels; focus order; error states; mobile layout | browser DevTools with JavaScript on, then with JavaScript off to confirm the fallback (mailto info@) is visible; stop before submit | every field reachable by Tab; visible labels; error text readable; submit reachable; fallback visible without JS | submit |
| Assessment page form submission | confirmation experience and event firing | with owner approval only: one submission using an owner-designated test address and the word TEST in the message; owner deletes the entry afterward | thank-you state shown; generate_lead fires once; notification email received | run without approval |
| /contact scheduler iframe | loads; availability page renders on mobile; the plain scheduler URL is reachable as a link (after ISS-033) | click through; close before choosing a time | iframe loads; call_booking_click fires on the plain link | book |
| Scorecard iframe | start, progress, completion, results, follow-up CTA inside the iframe | with owner approval: one run with clearly fake org data; confirm whether the tool stores responses and where (GitHub Pages is static; any storage would be third-party) | scorecard_start and scorecard_complete fire once each from inside the iframe; results text matches FACT-16 | enter real data |
| Scorecard method text parity | Squarespace page text vs iframe text | read both | identical method statement and bands | edit the instrument without a repository commit (rollback-notes.md) |
| Gumroad links (/resources) | click event; store resolves | click; close | gumroad_click fires; store URL matches the chosen canonical (CLM-040) | purchase |
| /terms-conditions links | every href resolves | crawl or click each | zero claude.ai hrefs; each policy link resolves (ISS-027) | none |
| Accessibility scope | keyboard usability, labels, focus, CTA contrast, error states, alt text (ISS-029) | manual checks plus Lighthouse accessibility when a rendering pass is authorized | issues logged with screenshots | claim a full accessibility certification |
