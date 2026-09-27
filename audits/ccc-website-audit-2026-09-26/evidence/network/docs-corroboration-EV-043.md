# EV-043: HEAD probes for owner-reported redirect sources and primary-source documentation checks (2026-09-27)

## HEAD probes (status only, 1s apart)

```
https://www.clearconciseconsulting.com/about-ccc                         301 -> http://www.clearconciseconsulting.com/about
https://www.clearconciseconsulting.com/about-section                     301 -> http://www.clearconciseconsulting.com/about
https://www.clearconciseconsulting.com/nonprofit-salesforce-consulting   301 -> http://www.clearconciseconsulting.com/services/salesforce-nonprofit-consulting
https://www.clearconciseconsulting.com/home                              200 -> 
```

## schema.org type existence (HTTP status of the type page)

```
schema.org/CaseStudy   404
schema.org/HowTo       200
schema.org/FAQPage     200
schema.org/ProfessionalService 200
schema.org/BlogPosting 200
```

## Google Search Central: FAQPage and HowTo eligibility (sentences matched on the live doc pages)

```
--- https://developers.google.com/search/docs/appearance/structured-data/faqpage
   Updated the FAQ structured data documentation to state that the feature is only shown for well-known, authoritative government and health websites.
   Why : The package tracking early adopters program is no longer accepting new partners.
   This change simplifies and reduces maintenance efforts for publishers who are creating AMP content, as they no longer need to update the AMP cache or configure signed exchanges.
--- https://developers.google.com/search/docs/appearance/structured-data/how-to
   Updated the FAQ structured data documentation to state that the feature is only shown for well-known, authoritative government and health websites.
   Why : The package tracking early adopters program is no longer accepting new partners.
   This change simplifies and reduces maintenance efforts for publishers who are creating AMP content, as they no longer need to update the AMP cache or configure signed exchanges.
```
