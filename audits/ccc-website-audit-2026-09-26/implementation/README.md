# implementation/: what is here and what it is not

Mode: AUDIT_AND_DRAFT. Nothing in this folder has been applied to the website, and none of it is publication-ready. The CMS is Squarespace 7.1 per owner documentation (EV-032); the platform could not be fingerprinted from live HTML this run (EV-001), so treat the CMS identification as owner-reported.

| File | Contents | Status |
|---|---|---|
| metadata-drafts.md | Current (as indexed) vs proposed SEO titles and descriptions for 13 pages, with character counts and blocking facts | DRAFT / APPROVAL_REQUIRED per row |
| jsonld/ | Organization+Person+WebSite reconciliation target, sameAs target list, Service draft, README with rules | see jsonld/README.md |
| squarespace-instructions.md | Where each backlog change is made in Squarespace, with uncertain controls marked | DRAFT |
| redirects-and-indexing.md | Redirect checks, URL mappings, index removals, and the plan any URL change must follow | DRAFT |
| rollback-notes.md | How to reverse each class of change | DRAFT |
| form-test-plan.md | How to test forms, scorecard, and scheduler without creating live leads | DRAFT (no live submissions authorized) |

Approval model:
- DRAFT: wording is proposed; may be edited freely.
- APPROVAL_REQUIRED: depends on a HOLD fact or a Squarespace control that changes site behavior; owner signs off on the exact string.
- OWNER_DECISION_REQUIRED: a business decision (offer name, price, client names, location) must be made first.
- PUBLICATION_READY: none at this time.

IMPLEMENT_APPROVED_LOCALLY does not apply to this site: there are no website source files. Squarespace changes are made in the CMS by the owner or an authorized implementer, after approval of specific ISS IDs. Approval to edit does not authorize domain, DNS, or billing changes.
