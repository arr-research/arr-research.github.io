# ARR public activity metrics policy — ARR-METRICS-1.0

**Effective:** 2026-08-30  
**Scope:** public paper pages, author profiles and activity rankings.

## Purpose and boundary

ARR publishes reproducible activity signals so readers can see whether records are
being used. Activity is not evidence of correctness, novelty, importance, impact,
endorsement or editorial quality. ARR does not sell ranking placement and does not
use activity counts to accept or reject submissions.

## Canonical PDF downloads

For each ARR identifier, the displayed count is the sum of GitHub's public
`download_count` for the canonical PDF asset in every published version release.
The accepted asset name is exactly `{ARR-ID}-vN.pdf`; source archives and other
assets are excluded. Draft releases are excluded.

Direct reads of the same-directory PDFs served by ARR's GitHub Pages site are
not measured by these counters. The counters cover GitHub Release downloads only;
they must not be described as total PDF readership. Cold mirror-cache downloads
can increment GitHub's counters; cached copies are reused on subsequent builds.

The counter is cumulative, not unique, and may include repeat downloads, automated
clients, mirrors or bots. GitHub supplies an aggregate counter and ARR cannot audit
or identify individual downloaders from it. A paper with several authors contributes
its full count to every listed author's total; counts are not divided fractionally.

## Page views and unique visitors

ARR currently has no page-view analytics provider. Pages therefore say **Not
measured**, and no page-view ranking is generated. Zero is not substituted for
missing measurement.

Before activating views, ARR must document a privacy-reviewed provider, exact event
definition, measurement window, bot handling, retention and applicable privacy
terms. The provider export must enter the build through the documented interchange
format; values are never hand-authored in page templates.

## Refresh, ties and publication

The Pages workflow obtains a fresh GitHub Releases snapshot every six hours and on
every deployment. Rankings sort descending by the displayed integer; equal values
are ordered alphabetically. Every deployed snapshot is published at `/metrics.json`
with generation time, provider, definition and view availability.

Counts can move because providers correct data or ARR corrects which asset is
canonical. ARR does not promise monotonicity. Suspected manipulation may be noted or
excluded only through a documented, version-controlled rule applied consistently.

## Reproducibility

The implementation is `scripts/sync_metrics.py`; the snapshot contract is
`schema/metrics.schema.json`; stable author identities are in
`registry/authors.json`. The public source repository and deployment history are the
audit trail.
