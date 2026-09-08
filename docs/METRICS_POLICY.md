# AIRR public activity metrics policy — ARR-METRICS-1.0

**Effective:** 2026-08-30  
**Scope:** public paper pages, author profiles and activity rankings.

## Purpose and boundary

AIRR publishes reproducible activity signals so readers can see whether records are
being used. Activity is not evidence of correctness, novelty, importance, impact,
endorsement or editorial quality. AIRR does not sell ranking placement and does not
use activity counts to accept or reject submissions.

## Canonical PDF downloads

For each AIRR identifier, the displayed count is the sum of GitHub's public
`download_count` for the canonical PDF asset in every published version release.
The accepted asset name is exactly `{ARR-ID}-vN.pdf`; source archives and other
assets are excluded. Draft releases are excluded.

Direct reads of the same-directory PDFs served by AIRR's GitHub Pages site are
not measured by these counters. The counters cover GitHub Release downloads only;
they must not be described as total PDF readership. Cold mirror-cache downloads
can increment GitHub's counters; cached copies are reused on subsequent builds.

The counter is cumulative, not unique, and may include repeat downloads, automated
clients, mirrors or bots. GitHub supplies an aggregate counter and AIRR cannot audit
or identify individual downloaders from it. A paper with several authors contributes
its full count to every listed author's total; counts are not divided fractionally.

## Page views and unique visitors

GitHub repository Traffic is a separate measurement. Its full clones and
repository-page visitors do not measure visits to `airr.science`. A unique cloner
is not evidence of a reader, scientific reuse, endorsement or citation; automated
clients and development activity can contribute, and AIRR cannot identify their
purpose from these aggregates. See [GitHub's traffic documentation](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository).
Use the private operator statistics dashboard for the public site's consenting
page-view sample, with the limitations below.

Since the 2026-09-08 implementation, optional public-page measurement can be enabled
for the private operator dashboard. Only visitors who choose Allow contribute.
One page load contributes one view of its canonical public path; reloads may count
again. No visitor identifiers are created, so unique visitors are not measured.
Automation can affect totals; the collector's global burst limit is not a guarantee
of human readership. No events are collected from private submission/editor pages.
See `PRIVACY_NOTICE.md` and `ANALYTICS_OPERATIONS.md` for consent, Netcup hosting,
400-day daily aggregate retention and access controls.

These operator totals are not currently exported to public paper/author counters.
The public pages say **Not available**, and no page-view ranking is generated.
Zero is not substituted for missing publication data. Before publishing such
counts, an export must define its measurement window and coverage and enter the
build through the documented interchange format; values are never hand-authored.

## Refresh, ties and publication

The Pages workflow obtains a fresh GitHub Releases snapshot every six hours and on
every deployment. Rankings sort descending by the displayed integer; equal values
are ordered alphabetically. Every deployed snapshot is published at `/metrics.json`
with generation time, provider, definition and view availability.

Counts can move because providers correct data or AIRR corrects which asset is
canonical. AIRR does not promise monotonicity. Suspected manipulation may be noted or
excluded only through a documented, version-controlled rule applied consistently.

## Reproducibility

The implementation is `scripts/sync_metrics.py`; the snapshot contract is
`schema/metrics.schema.json`; stable author identities are in
`registry/authors.json`. The public source repository and deployment history are the
audit trail.
