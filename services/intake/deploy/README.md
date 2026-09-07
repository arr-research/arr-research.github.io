# Debian private installation

These systemd units run the receiver as the non-login `airr-intake` system user,
listening **only on 127.0.0.1:8000**. They are the internal test stage, not an
internet-facing launch. They do not configure DNS, TLS, SMTP, an operator account
or backups and must not be used to claim that public submissions are available.

Expected layout:

- `/opt/airr-intake/releases/<git-commit>/`: a verified source archive, owned by root.
- `/opt/airr-intake/current`: symlink to the selected release.
- `/opt/airr-intake/venv/`: Python environment with the release's requirements.
- `/etc/airr-intake/intake.env`: persistent configuration, root-owned mode 0600.
- `/var/lib/airr-intake/`: private database and quarantine, mode 0700.

The source archive must contain `services/intake/`, `scripts/subjectlib.py`,
`scripts/donationlib.py`, `registry/euroscivoc.json`,
`registry/subject-extensions.json`, `site/donations.json` and `site/subjects.js`
from the same commit.
Record the commit and archive SHA-256 before copying; verify that digest on the
server before extracting. Do not copy the public PDF archive or personal files.

Install Python venv support, ClamAV, `clamdscan` and signature updates from the
distribution's signed package repositories. The application uses `clamdscan
--fdpass`, allowing private files to remain inaccessible to other system users.
Keep the ClamAV socket local and restrict it to the `clamav` group; give the
application that supplementary group. Verify that definitions are downloaded
and the daemon is running before testing uploads.

Create a random session secret on the server without printing it. The initial
configuration is:

```ini
ARR_INTAKE_INSTANCE=/var/lib/airr-intake
ARR_SESSION_SECRET=<a persistent, cryptographically random value of at least 32 bytes>
ARR_INTAKE_ORIGIN=http://127.0.0.1:8000
ARR_COOKIE_SECURE=1
ARR_BEHIND_PROXY=0
```

SMTP stays unset at this stage. `GET /healthz` should return 200 and
`GET /readyz` should return 503 because HTTPS and operator email delivery are not
configured. Check both; readiness failure here is intentional.

Copy the units to `/etc/systemd/system`, run `systemd-analyze verify` on them,
reload systemd and enable the service and timer. First run maintenance manually
and inspect its exit status. Signature updates remain managed by the ClamAV
package's service. The timer records failures in the system journal; external
failure alerts still need configuring before launch.

Validate malware detection with the harmless EICAR test in an isolated,
temporary directory owned by the service account. Verify that scanner failures
leave files quarantined. Use synthetic metadata and a separate disposable test
database for submission tests; do not create public paper records or send mail
to real recipients as part of these tests.

Before manuscript upload is enabled, complete the operating runbook in
[`docs/INTAKE_OPERATIONS.md`](../../../docs/INTAKE_OPERATIONS.md), including
encrypted storage/backups and restore, operator authentication, email delivery,
TLS, readiness enforcement and end-to-end verification. Plain local file
permissions alone do **not** provide encryption at rest. Do not set
`ARR_INTAKE_URL` during this private installation stage.

HTTPS may expose only the closed-intake page and protected editor setup/login
while that checklist is pending. The application defaults to `ARR_INTAKE_OPEN=0`
and also requires the signed launch-approval record. See [OPERATIONS.md](OPERATIONS.md)
for the encrypted volume, proxy and backup layout used by the deployed receiver.

For an update, back up the private instance, verify the next archive, prepare a
new release directory, stop the service, switch `current`, run `init-db` and
restart. Never overwrite the session secret or remove an existing database as
part of an update. A failed migration needs database-aware recovery; switching
the source symlink alone is not a complete rollback.

To pause the private installation, stop and disable `airr-intake.service` and
`airr-intake-maintenance.timer`. Keep the instance and configuration until the
operator explicitly authorizes their removal.
