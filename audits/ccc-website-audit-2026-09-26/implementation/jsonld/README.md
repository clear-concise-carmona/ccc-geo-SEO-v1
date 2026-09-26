# JSON-LD drafts: status and rules

| File | Status | Blocking facts | Where it would go (Squarespace, per EV-032) |
|---|---|---|---|
| organization-person.reconciliation.json | RECONCILIATION TARGET, APPROVAL_REQUIRED | FACT-03 (no certification count included until confirmed), FACT-24 (no contactPoint until one address is chosen), FACT-25 (no address, no LocalBusiness until location decision) | Settings > Advanced > Code Injection > Header (site-wide). Compare against the deployed blocks after the crawl; do not add a second Organization block. |
| sameas-target-list.json | APPROVAL_REQUIRED | CLM-040 (Gumroad), Facebook page confirmation | Every deployed block that carries sameAs |
| service-ai-data-readiness.draft.json | DRAFT, OWNER_DECISION_REQUIRED | FACT-15 (name, URL), FACT-14 (price: no offers block included until confirmed), deliverables list | Assessment page > Settings > Advanced > Code Injection (page-level) |

Rules applied:
- Every property maps to visible, register-approved content. No ratings, reviews, awards, addresses, service areas, or credentials are included that the register holds as HOLD.
- Uses https://schema.org and @id on every node, matching the owner's suppression-script signature so custom blocks are not removed (EV-032).
- Validity was checked as JSON syntax only (python json.load). Schema.org and Google requirements could not be checked against primary sources this run (hosts blocked). Validate on the live URL with the Rich Results Test and the Schema.org validator after deployment, per the owner's rule (never paste raw JSON).
- Eligibility note: Organization, Person, WebSite, and Service markup are for entity understanding; none of them earns a Google rich result for a consulting site. Do not claim otherwise.
- HowTo and CaseStudy schemas listed as pending in EV-032: HowTo rich results were removed by Google in 2023 (toolkit doc), so HowTo markup is entity decoration at best; CaseStudy is not a schema.org type (consider Article with about/mentions, or a plain Article). Both need a decision, not deployment.
