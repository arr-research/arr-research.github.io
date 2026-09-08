# Optional public-site statistics

The existing Netcup service provides an operator-only dashboard at
`https://submit.airr.science/admin/statistics`. It uses the existing operator
account and MFA. Independent editors and authors cannot access it. It remains
separate from the public-intake opening switch.

## What it measures

Consenting public-page loads, grouped by UTC day and canonical page path. The
dashboard shows today's total, 7/30/90/365-day totals, daily activity and the top
40 pages. It cannot reconstruct past traffic, count unique people, attribute
referrers, or prove that a request came from a person rather than automation.
Reloads count again. Consent choices and blockers mean this is a sample.

`site/analytics.js` sends nothing until Allow is chosen. Allow and Decline have
equal controls. A footer control reopens preferences. Only the choice and its
180-day expiry are kept in browser local storage. Requests omit credentials and
referrers and contain only the canonical path and fixed consent indicator.
No measurement script is included in private intake/editor pages.

## Configuration and activation

- Server environment: `AIRR_ANALYTICS_ENABLED=1`; default `0` returns 503.
- GitHub repository variable: `AIRR_ANALYTICS=1` includes the script in production
  public pages on the next Pages build; absent/other values omit it.
- Start the server first, verify privacy/authentication and collector checks, then
  enable the public build. To stop collection immediately, set the server flag to
  `0` and restart the application. Remove the GitHub variable and rebuild to remove
  the preference UI/script too. Neither operation opens paper submissions.
- `POST /api/v1/pageviews` accepts only the two public origins, JSON up to 512
  bytes, a fixed consent value and a known public path. Unknown paths and extra
  fields are rejected. CORS grants no credentials. A per-worker global limit of
  120 valid-shape requests/minute limits bursts without identifying readers.

The public build emits `/analytics-pages.json` (public canonical paths/titles only).
Bundle it as `site/analytics-pages.json` in the server release. The server refreshes
from the fixed HTTPS URL at most every ten minutes with a two-second timeout and
bounded size. Errors retain the last good/bundled allowlist. No arbitrary request
path, search query, fragment, IP address or referrer is written to the counter DB.
Keep Gunicorn and Caddy collector access logging disabled; infrastructure network
processing is distinct from persisted visitor statistics.

## Storage, maintenance and recovery

`public_pageviews` in the existing encrypted SQLite database contains only `day`,
`path`, `views`. Schema migration is additive. The existing daily retention sweep
erases totals older than the rolling 400 UTC days, even if traffic stops. Daily
consistent database snapshots and age-encrypted B2 backups include this table;
backup retention adds at most seven days. Restore into isolated encrypted storage
and check the table before a production recovery.

There is no additional analytics subscription and no new account/password. Storage
and requests still use existing VPS/backup capacity. No public view-count export
or visitor ranking is enabled by this feature. Review the notice and this record
before extending collection to identities, locations, referrers or additional
providers.
