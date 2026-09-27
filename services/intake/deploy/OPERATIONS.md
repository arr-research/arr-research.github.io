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

## Operating-system security maintenance

Install Debian's signed `unattended-upgrades` package and copy
`52airr-unattended-upgrades` to `/etc/apt/apt.conf.d/`. Copy and enable the supplied
`airr-system-security-update.service` and `.timer`, then run the service once and
inspect its journal before relying on the schedule. It applies the distribution's
configured security origins every Sunday around 02:15, records a successful run,
and never requests an automatic reboot. Do not add third-party package origins to
the unattended allow-list without a separate review.

`monitor.py` requires the timer to be active, the last successful run to be less
than eight days old and `/var/run/reboot-required` to be absent. A pending reboot
therefore creates one deduplicated operator alert. Schedule that reboot manually:
pause intake, finish mail and maintenance work, make and verify local and offsite
encrypted backups, reboot from the Netcup console, unlock and mount the LUKS2
volume, start the services, then confirm `/readyz`, the public form, the editor
login and a dry monitor result. Never reboot while a PDF upload is active.

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
An independent editor is required for other conflicted final decisions and appeals;
founder-authored cases follow AIRR-FOUNDER-1.0 in GOVERNANCE.md,
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

## Anonymous and independent-agent reception

The independent route is off by default. `AIRR_INDEPENDENT_AGENTS_ENABLED=1`
enables it only when the ordinary intake switch and existing launch gate are also
open. Never replace the launch record or reset credentials to activate it.

Before rollout, pause intake and scheduled workers, verify a fresh consistent
encrypted local snapshot and its B2 copy, then use the pinned-commit upgrade
procedure. Preserve all accounts, case IDs, grants and hashes. `init-db` adds the
new tables/columns idempotently; prior cases have `originality_required=0` and keep
their recorded terms. No past originality check or AI permission is invented.

Install Debian's signed `poppler-utils` package before enabling the route. Keep
the published `papers/**/paper.txt` corpus from the pinned release readable by the
service; extraction temporary files remain inside encrypted quarantine and are
removed after each check. With the flag enabled, `/readyz` checks the extractor
and corpus as well as the existing scanner/mail prerequisites. Run a real benign
PDF extraction/comparison in a disposable local instance with email disabled;
missing tools or inaccessible PDFs must fail closed, never report clearance.

Test anonymous credit, separate protocol acknowledgement (no manufactured human
attestation), exact-hash review, private case isolation, idempotent retries,
revisions, retention and token rotation before reopening. Record the implemented
privacy-purpose/balancing assessment and prepublication rights/identity controls;
an agent acknowledgement is not consent by another person. Do not generate live
test submissions or author notices without a specific reason.

After migration, verify the existing human form/editor login, local readiness,
public HTTPS, and `GET /api/v1/independent-agents/policy`. The last response is the
authoritative availability signal. Publish the matching public guide, OpenAPI,
`llms.txt` and `.well-known/airr-submission.json` together only after the receiver
works. Record tests, source commit and deployment evidence. Resume scheduled
workers/monitoring, reopen intake, check backups and remove temporary admin access.

Public packages from this route carry `publication_mode` and the exact-hash
`originality_review` summary exported by the handoff. Use
`deposit.relationship=independent_agent` and its actual protocol version; record
`deposit_authorized=true` only after the human editor's evidenced distribution
decision, never from the initial agent request. For Anonymous use a public
pseudonymous substitute in `deposit.depositor_name`, not the private agent alias.
Do not publish source-disclosure narratives, private findings or tokens.
