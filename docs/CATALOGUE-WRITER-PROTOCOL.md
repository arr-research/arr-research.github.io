# Private historical catalogue: mandatory writer protocol

The historical catalogue is a private predecessor snapshot, distinct from the
public static website catalogue. Its production file is
`/srv/airr-private/historical-revisions/catalogue.json`; its coordination lock is
the SQLite writer transaction on the **same**
`/srv/airr-private/instance/intake.sqlite3` used by the running intake service.
Using another database, copying over the file outside this protocol, or releasing
the transaction before replacement is not a supported live update.
Before applying, verify that the running service's configured `DATABASE` and
`HISTORICAL_REVISION_CATALOGUE` resolve to those same physical files; matching
source literals alone is not deployment evidence of a shared lock.

## Grant issuers

`programme-artifact-grants` and `authorize-historical-revision` must acquire
`BEGIN IMMEDIATE` before reading/validating a catalogue used for a new or renewed
historical grant. Retain it through all grant inserts/renewals and commit, rolling
back on every failure. Existing author, operator, contract, rights, exact binding,
one-use and quota checks continue to apply. Scope-extension authorization already
reads its catalogue inside the same transaction. Inspection/preparation reads
alone do not authorize a grant; the issuing operation revalidates under the lock.
Before any cached historical-grant response or expired-grant renewal, compare its
stored whole-catalogue hash with that locked current snapshot. A missing/stale
binding is HTTP 409 requiring reconciliation of the original authorization; leave
expiry, stored binding and evidence unchanged. An unrelated catalogue change also
counts. Do not silently rebind or issue another grant to evade this refusal.

## Catalogue writers

Every supported writer must acquire that same `BEGIN IMMEDIATE`, check the native
published-case requirements where applicable and **all** active approved unused
historical grants (not only this paper), and refuse mutation if any exist. Under
the retained lock, read/validate the current snapshot, preserve all unrelated
entries, make an exclusive private backup and fsynced temporary file, atomically
replace, and verify readback before releasing the lock. Default operation remains
read-only. Already-current no-op output is not proof of zero unused grants.

Legacy writers may retain a speculative pre-lock snapshot only if they compare
its exact bytes with the live catalogue **inside** the lock immediately before
the backup/replacement sequence and abort on any difference. No cooperating
writer can change the file between this comparison and replacement. The new
official-release helper instead takes its initial snapshot inside the lock too.

The supported live-writer inventory at the 226C race-fix freeze is:

* `operator_reconcile_turan212.py`
* `operator_reconcile_turan_v2_212.py`
* `operator_reconcile_perron_v2_213.py`
* `operator_reconcile_parity_v2_215.py`
* `operator_register_parity_predecessor215.py`
* `operator_reconcile_integrated_v11_217.py`
* `operator_reconcile_integrated_v12_221.py`
* `operator_reconcile_integrated_v13_223.py`
* `operator_reconcile_matrix_v14_226C.py` (original mirror gate, unchanged)
* `operator_reconcile_matrix_v14_official_release_226C.py`
* `operator_reconcile_rectangular_v15_232B.py` (v15: both official asset and AIRR mirror)
* `operator_register_window_predecessor354.py` (absent v1: exact native published case,
  official asset and AIRR mirror; verifies the running service's actual configuration)

The v1 window helper requires absolute, equal canonical configured paths and
the same process mount view, not merely hard-linked file identities. It opens
only an existing database, rejects duplicate JSON keys at every depth, creates
private backup and temporary files with initial mode 0600, and reads back through
the configured service paths while retaining the writer lock. The AIRR mirror
must finish on the AIRR origin; an official-asset redirect cannot stand in for it.
The running release factory and both corrected grant-issuer source files are
pinned. These checks do not prove loaded worker state: the operator must verify
the effective unit/options and immutable deployment, with no concurrent deploy,
before applying. A PID plus process start time detects ordinary process replacement.

These scripts use the same database path and retain the transaction across the
final file comparison, replacement and readback. The regression inventory check
must be extended for any new supported writer. Deployment must include both
corrected grant issuers before any live catalogue reconciliation; deploying only
the helper does not resolve the rejected stale-grant race. Initial installation
or administrative restore must use this same lock/check protocol, or take the
service offline and drain/verify all grant issuance first. There is no supported
uncoordinated live installer. Public metadata/site writers do not write this
private file; scope preparation scripts only read it and then use native CLIs.

## Limits and recovery

This is cooperative exclusion, not protection against arbitrary privileged
out-of-contract filesystem writes, a second service using another database, or
manual edits. SQLite rollback does not restore an already replaced file. After
a post-replacement failure, inspect the actual file and private backup under the
same writer lock before deciding whether to restore; do not blindly retry or
claim atomicity across SQLite and the filesystem. Existing helpers fsync file
contents but do not fsync parent directories: full power-loss durability is not
claimed. A process crash releases the SQLite lock; an exclusive leftover backup
or temporary file intentionally makes a conflicting retry fail for inspection.

The official-release witness does not pass, replace or alter the original AIRR
website mirror criterion. It creates no grant, scope, receipt, permission,
publication decision, quota exception or acceptance. All original release hashes,
author identities, native-case and publication gates remain in force.


The v15 successor requires BOTH actual official v15 release-asset membership/bytes
and exact AIRR mirror bytes; it cannot use the v14 pending-mirror route. Exact
v15 published case, 93 unrelated entries and global zero active unused historical
grants are required even for its already-current no-op. Actual asset ID and immutable
metadata commit come from the completed public release; no new authority is created.
