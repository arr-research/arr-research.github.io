# Encrypted VPS operation and release gates

The public catalogue remains on GitHub Pages. `submit.airr.science` points only to
the private Netcup receiver. Caddy terminates TLS and overwrites all trusted
forwarding headers before sending traffic to loopback. Its liveness check permits
editor setup while `ARR_INTAKE_OPEN=0`; the application enforces the signed opening
gate separately on every public submission request. `/healthz` and `/readyz` are
not exposed by the supplied Caddy configuration.

The current operating layout is a LUKS2 container at `/var/lib/airr-private.luks`,
mounted at `/srv/airr-private` with `nodev,nosuid,noexec`. The instance lives in
`instance/`, the root-owned environment in `secrets/`. Service overrides require
the mount and grant writes only to the private instance. The encryption key is
kept outside the VPS. A reboot therefore needs an operator unlock; do not silently
store a plaintext unlock key on the server to make boot automatic. Encryption
protects a locked disk/snapshot, not data exposed to an administrator of a running
unlocked host. A tested, independently kept recovery key is essential.

`backup.py` makes a consistent SQLite backup, copies only referenced immutable
PDFs, verifies every copied PDF against its recorded SHA-256, includes protected
configuration, and streams an archive to `age`. Plaintext staging stays on the
encrypted volume. Only the age public recipient resides on the VPS. A snapshot
and checksum in `/var/backups/airr` are not an independent backup until transferred
and verified in another failure domain. A failed or incomplete snapshot is not a
successful backup. Keep scheduled offsite transfer, retention, alerts and recovery
key custody in the signed deployment evidence, not merely in this guide.

For recovery: verify the encrypted archive checksum, decrypt using the offline
identity into an encrypted staging volume, safely extract with `filter='data'`,
check SQLite integrity and every manifest fingerprint, and start a disposable
instance with email disabled before considering any replacement of production.
Never print the restored environment or key. A restore test must not overwrite the
current instance. Keep old deployment/database snapshots for rollback until the
new version has passed its production probes.

Pending mail is processed each minute. Uncertain SMTP handoffs remain marked
`uncertain`, avoiding silent duplicate deliveries. The editor must inspect provider
logs before issuing another case link. Daily maintenance scans quarantined cases,
applies case retention and expires links. Monitor timer failures and stale backups
and test an alert before opening. External server-down monitoring is separate
from an on-host timer.

The launch-approval example has every check false. Neither an installation nor a
passing unit suite creates a legal review, postal contact, independent editor,
restore-key handoff or offsite schedule. Evidence and the operator's signature
must be real before setting the public switch and GitHub intake URL.
