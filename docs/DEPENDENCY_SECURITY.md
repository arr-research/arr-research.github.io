# Dependency security and preserved research environments

**Initial check: 8 September 2026.** GitHub reported 111 open dependency alerts,
covering 37 advisories repeated across three archived reproduction manifests. All
concerned `pypdf==6.4.0`: 6 high, 96 medium and 9 low alert instances. These counts
are a dated snapshot, not a permanent assurance about subsequent advisories.

Affected records and manifests:

- `ARR-2026-7NPRNBW4488HG90K`: `src/repro/requirements.txt`.
- `ARR-2026-6WX2JF38WE87GB2M`: `src/replay/requirements.txt`.
- `ARR-2026-3H0ZKWJMH18MH9FX`: `src/replay/requirements.txt`.

They are under `papers/2026/08/` in their identifier shards. The production intake
requirements in `services/intake/requirements.txt` do not install `pypdf`, and none
of these alerts targets that manifest. The intake uses ClamAV for malware checks;
it does not execute deposited research code.

## Handling the affected environments

Do not use the old PDF parser with untrusted PDFs or expose those reproduction
environments as services. The known advisories include excessive runtimes and
memory consumption on crafted documents. Version **6.17.0** is above the
patched version listed for all 37 advisories in this audit. See the publisher's
[security advisories](https://github.com/py-pdf/pypdf/security/advisories) and the
latest reviewed [outlines](https://github.com/advisories/GHSA-23w6-3w8w-8484) and
[XForm](https://github.com/advisories/GHSA-763m-79hh-57f2) advisories.

For new PDF inspection, create a separate disposable environment and install
`security/requirements.txt`. It pins the reviewed parser and is monitored by
Dependabot. It is not a complete environment for reproducing a mathematical
result, nor a substitute for execution isolation and resource limits.

For reproduction of an affected paper, keep the original environment declaration
as evidence. Use an isolated copy with the updated parser, record that deviation
and recheck the results before claiming equivalence. Installing the old exact
pin together with a conflicting constraint does not upgrade it.

## Why the original pins remain visible in release history

Published release assets, hashes, release tags and citations are immutable. Their
original environment declaration remains preserved in release history and
provenance. A maintained repository requirement may advance after an explicit
security revalidation without changing the canonical paper.

## Revalidation and maintained environments — 9 September 2026

The three maintained repository requirements now use pypdf 6.17.0. Each exact
scientific verifier passed in a fresh Python 3.12 environment containing the other
declared dependencies. The three canonical PDFs were read and text-extracted with
6.17.0; page counts, byte counts and SHA-256 values matched their deposited
metadata. The 7N replay regenerated both frozen certificates byte-for-byte.

The preserved package checks could not be rerun from the flattened repository
trees because their pre-deposit `output/release/manifest.json` files are not part of
those trees. This is a packaging-layout limitation, not a pypdf failure; the exact
scientific checks and direct PDF checks above passed. The immutable release assets
retain their original environment declaration and should not be used to process
untrusted PDFs.

GitHub's 111 alerts should close from the updated default-branch manifests. They
have not been dismissed as tolerable risk. This does not erase the dated snapshot
or claim that future advisories cannot arise.
