# EV-040: Network re-check after the owner changed the environment allowlist (2026-09-27)

Method: curl HEAD/GET status probes through the session's policy proxy, one request per host, no retries of policy denials (per proxy guidance). Times UTC, 2026-09-27 17:27 to 17:29.

| Host | Result | Interpretation |
|---|---|---|
| www.clearconciseconsulting.com | 200 | allowed; crawl proceeded |
| clearconciseconsulting.com | 301 -> https://www.clearconciseconsulting.com/ | allowed; non-www redirects to www |
| clearconciseconsulting.squarespace.com | 200 | allowed; built-in domain serves content (no redirect) |
| archive.org | 200 | allowed |
| web.archive.org | connection reset by peer, twice (proxy relay log: tunnel closed after 11s, code 1006) | relay failure, not a policy denial; one retry spent; not used |
| www.salesforceben.com | HTTP 403 from origin | origin-side block of the client (policy denials appear as CONNECT 403, this was an HTTP 403 after a completed TLS handshake); not retried |
| developers.google.com | 200 | allowed |
| schema.org | 200 | allowed |
| pypi.org, files.pythonhosted.org | HTTP 403, header x-deny-reason: host_not_allowed | policy denial; toolkit requirements were installed offline from the local uv cache instead (no network) |

Consequence: the crawl, HEAD probes, and local scoring ran. Archive corroboration and Salesforce Ben verification remain not done.
