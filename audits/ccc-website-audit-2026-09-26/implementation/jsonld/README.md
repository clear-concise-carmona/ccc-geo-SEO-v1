# JSON-LD drafts: deployed state, status, and rules

## Deployed state observed 2026-09-27 (EV-038)

Every page carries, in raw HTML: a native WebSite block; a native Organization block (address, telephone, email j.carmona@, six sameAs); a native LocalBusiness block (address, image, openingHours with two trailing empty items); and the custom Organization+ProfessionalService block (@id https://www.clearconciseconsulting.com/#organization, PostalAddress with suite number, founder -> https://www.clearconciseconsulting.com/about#jeremy-carmona, seven sameAs). /about adds Person (@id .../about#jeremy-carmona, four sameAs) and AboutPage. The assessment page carries a Service block (@id .../salesforce-ai-data-readiness-assessment#service, no offers). The homepage carries its FAQPage block twice. Three posts carry both Article and BlogPosting. The case study uses "CaseStudy", which is not a schema.org type (EV-043).

The pass-1 drafts proposed a Person @id of /about#person. The deployed value /about#jeremy-carmona is kept everywhere; changing a working identifier would gain nothing.

| File | Status | Blocking facts | Where it would go (Squarespace) |
|---|---|---|---|
| organization-person.reconciliation.json | RECONCILIATION TARGET, APPROVAL_REQUIRED | FACT-24 (no contactPoint until one address is chosen), FACT-25 (no address or LocalBusiness until the location decision), FACT-27 (URL-form choices for Trailblazer, Facebook, Gumroad) | Settings > Advanced > Code Injection > Header, replacing the custom block; the native blocks come from Settings > Business Information and are removed by clearing those fields, not by code (ISS-015) |
| sameas-target-list.json | APPROVAL_REQUIRED | FACT-27 | Every deployed block that carries sameAs (custom Organization, Person on /about; the native block follows Business Information social links) |
| service-ai-data-readiness.draft.json | DIFF against the deployed Service block; DRAFT | FACT-15 (no offers block until the price is settled) | Assessment page > Settings > Advanced > Code Injection (page-level) |

Rules applied:
- Every property maps to visible, register-approved content. No ratings, reviews, awards, service areas beyond the deployed "United States", or credentials that the register holds as HOLD.
- Uses https://schema.org and @id on every node, matching the deployed identifiers.
- Validity checked as JSON syntax (python json.load). schema.org type pages were reachable this pass (EV-043) and every type used here exists. Validate on the live URL with the Rich Results Test and the Schema.org validator after deployment, reading the raw HTML, not the rendered DOM (client-side suppression does not change what crawlers receive).
- Eligibility: Organization, Person, WebSite, and Service markup help machines identify the entities; none earns a Google rich result for a consulting site. FAQPage rich results are shown only for well-known, authoritative government and health websites per Google's documentation (EV-043).
- CaseStudy: replace with Article (about: the client's sector, not a named client unless FACT-22 permits) or drop. HowTo on the validation-rules post: valid type; the rich result is retired; leave it.
- One FAQPage source per page; one article node per post (Article or BlogPosting, not both).
