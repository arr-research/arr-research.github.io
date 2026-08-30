# Capacity and migration plan

ARR is designed to grow without changing public identifiers or rewriting accepted records. Capacity is added only when measured load justifies it.

## Three planes

1. **Intake plane:** private, rate-limited and temporary. Untrusted submissions are quarantined and never enter the public repository directly.
2. **Registry plane:** authoritative metadata, state transitions, version links, integrity manifests and public export events.
3. **Artifact plane:** immutable source bundles, PDFs, code, data and build logs. Storage is addressed through provider-independent object keys.

The public catalogue is a projection of accepted registry events. It is not the intake database and it is never the only preservation copy.

## Stable addressing

- `record_id` is a globally unique UUID-backed identifier that survives provider and domain changes.
- `version_id` identifies one immutable version.
- `id` is a human-facing `ARR-YYYY-<16 Crockford Base32 characters>` identifier.
- Git paths are sharded as `papers/YYYY/MM/PP/ARR-...`, where `PP` is the first two characters of the suffix.
- Later Git-backed versions are stored at `papers/YYYY/MM/PP/ARR-.../versions/vN/`; the initial root layout remains valid for backward compatibility.
- Future object storage uses `records/YYYY/PP/<record_id>/versions/<version_id>/...`.
- SHA-256 manifests bind each release to its exact files.

## Capacity phases

| Phase | Public records | Operating model | Migration trigger |
|---|---:|---|---|
| Pilot | 0–1,000 | Git, GitHub Releases and Pages | Catalogue build or moderation becomes operationally slow |
| Initial archive | 1,000–10,000 | Partitioned Git plus independent preservation mirror | Repository approaches 1 GB or PR throughput becomes limiting |
| Public service | 10,000–100,000 | PostgreSQL registry, object storage, queue workers and CDN | Sustained intake, search or storage needs exceed one service |
| Large scale | 100,000+ | Horizontally partitioned intake, dedicated search, multiple storage/preservation providers | Measured latency, cost or resilience targets require it |

Thresholds are review points, not promises. ARR migrates before a provider hard limit is reached.

## Required invariants

- Accepted versions are immutable.
- Corrections receive new `version_id` values and link to the superseded version.
- Public exports are rebuildable from registry events.
- Catalogue consumers can use year/prefix NDJSON partitions and a machine-readable partition index instead of a monolithic export.
- Blobs are never the sole source of metadata.
- No storage URL is a permanent identifier.
- Intake data has a retention deadline and can be deleted without affecting public records.
- Provider exports and disaster-recovery tests are performed before accepting external submissions.

## What remains intentionally unbuilt

ARR's direct private-upload service is implemented but remains closed until its production gate and external host are complete. ARR does not run author accounts, payments, comments, social scores, automated quality scores or untrusted-code execution. New features must not weaken quarantine or human editorial control.
