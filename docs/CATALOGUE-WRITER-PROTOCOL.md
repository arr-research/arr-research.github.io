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
