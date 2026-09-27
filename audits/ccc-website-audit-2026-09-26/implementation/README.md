# implementation/: what is here and what it is not

Mode: AUDIT_AND_DRAFT. Nothing in this folder has been applied to the website, and none of it is publication-ready. The CMS is Squarespace: verified from the live responses on 2026-09-27 (`Server: Squarespace` header, the Squarespace robots.txt banner, squarespace-cdn asset hosts; EV-038). The scorecard instrument is separate: an iframe served from the owner's GitHub Pages repository (clear-concise-carmona.github.io/ccc-artifacts/), which was not modified.

| File | Contents | Status |
|---|---|---|
| metadata-drafts.md | Live (2026-09-27) vs proposed SEO titles and descriptions for 15 pages, with character counts; five rows are now NO_CHANGE since the live values already match or are acceptable | DRAFT / APPROVAL_REQUIRED per row |
| jsonld/ | Deployed-state notes, Organization+Person+WebSite reconciliation target (deployed @ids), sameAs target list built from the three deployed arrays, Service draft as a diff against the deployed block | see jsonld/README.md |
| squarespace-instructions.md | Where each open backlog change is made in Squarespace; controls verified from the live site are marked; resolved items listed at the end | DRAFT |
| redirects-and-indexing.md | Verified redirect results (EV-039, EV-043), the mirror-host state, index residuals, and the plan any URL change must follow | DRAFT |
| rollback-notes.md | How to reverse each class of change, including the GitHub Pages instrument | DRAFT |
| form-test-plan.md | How to test the assessment form, the contact page scheduler, the scorecard iframe, and outbound links without creating live leads | DRAFT (no live submissions authorized) |

Approval model:
- DRAFT: wording is proposed; may be edited freely.
- APPROVAL_REQUIRED: depends on a HOLD fact or a Squarespace control that changes site behavior; owner signs off on the exact string.
- OWNER_DECISION_REQUIRED: a business decision (offer price, client names, location, intake path) must be made first.
- NO_CHANGE: the live value is already correct or acceptable.
- PUBLICATION_READY: none at this time.

Two items need no decision and can be fixed on sight: the six placeholder links on /terms-conditions (ISS-027) and the dated "Currently booking for Q3 2026" line on /contact (ISS-031).

IMPLEMENT_APPROVED_LOCALLY does not apply to this site: there are no website source files in this repository. Squarespace changes are made in the CMS by the owner or an authorized implementer, after approval of specific ISS IDs. Approval to edit does not authorize domain, DNS, or billing changes.
