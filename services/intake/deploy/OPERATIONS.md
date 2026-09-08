# Encrypted VPS operation and release gates

The public catalogue remains on GitHub Pages. `submit.airr.science` points only to
the private Netcup receiver. Caddy terminates TLS and overwrites all trusted
forwarding headers before sending traffic to loopback. Its liveness check permits
editor setup while `ARR_INTAKE_OPEN=0`; the application enforces the recorded opening
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
key custody status in the deployment evidence, not merely in this guide.
The latest three local snapshots are kept, none older than seven days, and cleanup
only follows a successful new snapshot. Target no more than seven days offsite,
allowing for provider lifecycle scheduling (see the configuration below). Reapply erasure
schedules and known requests before reopening a restored instance. Deployment
rollback copies must also be removed after their documented rollback window.

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
`monitor.py` checks the services, actual scanner readiness, uncertain email and
local snapshot age. Run it without `--notify` first; notification mode reports
only changed failures to the operator, without author data. The separate GitHub
scheduled workflow checks the public archive and HTTPS login from outside Netcup;
its schedule is best effort and GitHub failure-notification preferences must be
verified by the operator. The external availability check does not prove that an
offsite transfer succeeded; the on-host monitor also checks the verified offsite
status when configured.

## Backblaze B2 offsite copies

Install `rclone` from the operating system's signed package repository. The
transfer uses its S3 interface with a private B2 EU Central bucket, not a public
URL or a replication service. Create a one-year application key restricted to
that bucket and the `intake/` prefix; never use the account's master key. The
provider's Read and Write preset can include bucket-setting and delete
capabilities in addition to file read/write. Account restrictions, encryption and
short retention are not protection against every action of a compromised root.

Store the following root-only configuration inside the encrypted volume:

- `secrets/b2-rclone.conf`: remote named `airrb2`, S3 provider `Other`, key ID and
  application key, endpoint `https://s3.eu-central-003.backblazeb2.com`, region
  `eu-central-003`, `no_check_bucket = true`, `force_path_style = true`.
- `secrets/offsite.json`, linked from `/etc/airr-intake/offsite.json`: `enabled`,
  `bucket`, `prefix` (`intake/`), `region`, `max_snapshot_bytes` (at most
  500,000,000), and the actual ISO8601 `key_expires_at`. Both files are included
  in encrypted snapshots. Never place the offline age identity in this folder.

`offsite.py` accepts only a completed, recent age archive whose sidecar hash
matches. It copies the immutable snapshot, checks its size, downloads it again
and compares SHA-256, then copies the checksum sidecar. It performs neither a
remote sync nor remote deletion. Failed or partial transfers never advance the
success record in `/var/lib/airr-offsite/status.json`; a failure record replaces
the success state so the monitor reports the problem. The encrypted archive is
downloaded once per run, so repeated manual runs also consume download quota.

Configure a lifecycle restricted to `intake/`: hide after four days, delete one
day after hiding, and cancel unfinished large uploads after one day. This leaves
room for the provider's daily processing within the seven-day target; deletion
is not instantaneous. Verify effective retention in service operation and
escalate delays or outstanding erasure requests. Do not enable Object Lock when
it conflicts with the erasure schedule. References:
[B2 lifecycle processing](https://www.backblaze.com/docs/cloud-storage-lifecycle-rules)
and [application keys](https://www.backblaze.com/docs/cloud-storage-application-keys).

On the initial account, verified caps were $0 / 10 GB storage, $0 / 1 GB daily
downloads and 2,500 daily Class B/C requests, with operator alerts. Preserve these
caps until the owner explicitly approves changing them. The 500 MB snapshot
guard leaves download headroom for a verification and recovery download. If the
archive grows beyond the guard, backup transfer fails visibly and needs capacity
review; it must not silently buy capacity or skip verification.

After a successful manual upload and disposable restore, install the supplied
offsite service/timer. It runs at 04:40 with up to five minutes of jitter in the
server's timezone, after the 04:10 local backup and its 15-minute jitter. Confirm
both timers' actual next run. The monitor flags unsuccessful transfers, disabled
timers, snapshots or verification older than 30 hours, missing configuration
after activation, and a key expiring within 30 days. Run the monitor without
`--notify` before resuming notifications.

A recovery drill must download from the remote bucket, verify SHA-256, decrypt
with the separately held identity, and inspect the restored database, operator
access and protected configuration in disposable encrypted storage. The initial
live drill contained one operator and no submitted PDFs; a separate synthetic-PDF
drill does not establish coverage of future real submissions. Keep recovery keys
under independent operator custody and record restore evidence outside Git.

The `AIRR-PILOT-1.0` launch example has every check false. Each required check needs
an evidence reference, plus the real operator's authorization identity, date and
source. A tool may record an existing explicit instruction; it must not call that
an electronic signature or invent completed checks. Postal contact, data handling,
restoration, HTTPS, operator MFA, scheduled backups, monitoring, incident handling
and end-to-end receipt must be reviewed before enabling the switch and GitHub URL.
An independent editor is required for conflicted final decisions and appeals,
not for ordinary receipt. Record incomplete recovery-key custody honestly as an
ongoing continuity task. See `docs/INTAKE_OPERATIONS.md` for the reception policy.


## Deploying agent intake

Run `flask --app services.intake.app init-db` as the intake service user with its
protected environment after switching the source and before restarting workers.
The migration adds delegation tables and provenance columns without replacing
accounts, TOTP secrets, recovery codes or existing case IDs. Stop maintenance and
mail workers during the migration, keep a consistent encrypted rollback snapshot,
and verify SQLite integrity and the operator count before resuming.

Multipart uploads now spool under the configured quarantine directory, including
before the receiving view runs. A private per-service `/tmp` alone would not keep
large incoming PDF fragments on the encrypted volume. Maintain the encrypted
mount requirement and the private filesystem permissions on the whole instance.

The new API and browser form share PDF persistence, malware scanning and editorial
notification. A deployed API does not open intake: it enforces the recorded
launch authorization. Confirm the human form, authorization request and upload all
return 503 before the operator completes that approval.
