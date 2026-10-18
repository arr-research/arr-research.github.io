# Optional public-site statistics

The existing Netcup service provides an operator-only dashboard at
`https://submit.airr.science/admin/statistics`. It uses the existing operator
account and MFA. Independent editors and authors cannot access it. It remains
separate from the public-intake opening switch.

## What it measures

Consenting public-page loads, grouped by UTC day and canonical page path, and
consenting PDF opens from AIRR record pages, grouped by UTC day and a fixed
per-version label (`/papers/ID/versions/vN/pdf/`). The dashboard reports PDF opens
separately from page views. The
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

## Cookie-free page counter (erikssonai.se)

Independent of the Netcup collector above, `page_shell()` in `scripts/build_site.py`
ends every generated public page with the `PAGE_COUNTER` constant: one minimal inline
script that adds `<script src="https://erikssonai.se/contador.js" data-sitio="airr" async>`
to the page unless the visitor chose Decline. The counter script belongs to the
operator's other site; it is only linked, never copied or modified here. Each page view
is sent to the operator's own function `contarFirma`
(`https://europe-west1-linguaula-web.cloudfunctions.net/contarFirma`, Google Cloud,
region europe-west1, Belgium). The function uses the IP address and browser type only in
memory to compute an encrypted fingerprint with a random key that changes every day; the
fingerprint deletes itself within 48 hours and the IP address is never stored. Only daily
totals (page views and different people) remain. The counter sets no cookie and writes
nothing to browser storage; the single exception is the marker saved in the operator's
own browser by opening the site with `?nocontar`, so that browser is not counted. The
daily figures appear in the private panel at `erikssonai.se/panel/` (tab *Webs*). The
`AIRR_ANALYTICS` variable does not switch it.

- **Decline is respected.** The inline loader reads (never writes) the same browser
  choice as `site/analytics.js`: local-storage key `airr-statistics-choice-v1`, value
  `{"value":"allow"|"decline","expires":<ms>}`. Only an unexpired `decline` stops the
  counter from being added. No choice, Allow, an expired or malformed value, or
  unreadable storage all load it (the same reading `site/analytics.js` gives them).
  Changing the choice in *Statistics preferences* applies from the next page load; the
  counter is not removed from the page already open.
- **Browser signals.** `contador.js` itself does not count visitors who send Global
  Privacy Control or Do Not Track, nor `localhost`, Firebase test channels or automated
  browsers (change made on 2026-10-13 at `erikssonai.se/contador.js`, not in this repo).
- GitHub Pages sets no Content-Security-Policy for `airr.science`. If one is ever
  added, allow `https://erikssonai.se` in `script-src` and
  `https://europe-west1-linguaula-web.cloudfunctions.net` in `connect-src`, and let the
  inline loader through with a `sha256-` hash of its text (a nonce does not suit static
  pages) rather than `'unsafe-inline'`; the hash changes whenever `PAGE_COUNTER` changes.
- To stop counting, remove `PAGE_COUNTER` from `page_shell()` (and the notices in
  `build_privacy`, `docs/PRIVACY_NOTICE.md`, `docs/PROCESSING_RECORD.md`), merge and let
  Pages rebuild. Never put the script on `submit.airr.science` pages.
- `tests/test_indexing.py` checks that the loader is on every page exactly once,
  immediately before `</body>`, that its storage key matches `site/analytics.js`, and
  (running it in Node) that it loads the counter with no choice or Allow and not after
  Decline.
