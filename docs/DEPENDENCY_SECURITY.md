# Dependency security and preserved research environments

**Checked: 8 September 2026.** GitHub reports 111 open dependency alerts, covering
37 advisories repeated across three archived reproduction manifests. All concern
`pypdf==6.4.0`: 6 high, 96 medium and 9 low alert instances. These counts are a
dated snapshot, not a permanent assurance about subsequent advisories.

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
memory consumption on crafted documents. Version **6.16.1** is at or above the
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

## Why the archived pins remain visible

Published source snapshots, hashes, release tags and citations are immutable.
Silently editing the historical requirements would misrepresent the published
experiment. A fully revalidated environment belongs in a documented new version
or companion reproduction, with new evidence. This audit does **not** claim that
those scientific reproductions have been rerun.

The 111 historical alerts remain open. They have not been dismissed merely to
make the repository appear clean. Follow-up is to revalidate those three
environments; new platform dependencies must be maintained independently.
