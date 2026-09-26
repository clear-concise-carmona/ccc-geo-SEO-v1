# Form, scorecard, and scheduler test plan (no live submissions authorized this run)

Purpose: verify conversion elements without creating leads, bookings, or test records the owner did not approve.

| Element | Test | Method | Pass condition | Do not |
|---|---|---|---|---|
| /contact form | keyboard traversal, labels, focus order, error states, mobile layout | browser DevTools + keyboard only; stop before submit; use the Squarespace form's own preview if available | every field reachable by Tab; visible labels; error text readable; submit button reachable | submit |
| /contact form submission path | confirmation experience and event firing | with owner approval only: one submission using an owner-designated test address and the word TEST in the message; owner deletes the entry afterward | thank-you state shown; generate_lead fires once; notification email received | run without approval |
| Scorecard | start, progress, completion, results, follow-up CTA | with owner approval: one run with clearly fake org data; confirm whether the tool stores responses and where | scorecard_start and scorecard_complete fire once each; results page shows the method statement matching FACT-16 | enter real data |
| Scheduler (scheduler.zoom.us/jeremy-carmona) | outbound click event; availability page loads; no booking | click through; close before choosing a time | call_booking_click fires; page loads on mobile | book |
| Gumroad links | click event; store resolves | click; close | gumroad_click fires; store URL matches the canonical (CLM-040) | purchase |
| Accessibility scope | keyboard usability, labels, focus, contrast of CTA buttons, error states | manual checks plus Lighthouse accessibility in the crawl phase | issues logged with screenshots | claim a full accessibility certification |
