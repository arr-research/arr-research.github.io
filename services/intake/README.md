# ARR private intake service

This service is the direct private-submission boundary in front of the public ARR
repository. Authors need no invitation or account. It accepts PDF manuscripts into
non-public quarantine, fails closed when malware scanning is unavailable, emails
the operator a protected case link without attaching the manuscript, and records
human decisions. It never publishes a submission or writes to `papers/`.

The service is suitable for a controlled pilot after the production checklist in
[`docs/INTAKE_OPERATIONS.md`](../../docs/INTAKE_OPERATIONS.md) has been signed.
It is not permission to open general public intake.

## Local setup

```console
python -m venv .venv
.venv/bin/pip install -r services/intake/requirements.txt
export ARR_INTAKE_INSTANCE=/absolute/path/outside/the/public/repository
export ARR_SESSION_SECRET=$(python -c 'import secrets; print(secrets.token_hex(32))')
flask --app services.intake.app init-db
flask --app services.intake.app create-operator
flask --app services.intake.app run --debug
```

On Windows, use `.venv\Scripts\pip`, set environment variables with PowerShell,
and run the same Flask commands. `create-operator` prints a TOTP secret once;
add it to an authenticator application before leaving the terminal.

Operational commands:

```console
flask --app services.intake.app scan-pending
flask --app services.intake.app retention-sweep
flask --app services.intake.app mark-published SUB-CASE https://example.org/immutable-release
flask --app services.intake.app legal-hold SUB-CASE
flask --app services.intake.app release-legal-hold SUB-CASE
```

Production requires HTTPS, a persistent session secret, ClamAV (`clamdscan` or
`clamscan`), an instance directory not served by the web server, encrypted
backups, and one daily run of both operational commands. Set
`ARR_BEHIND_PROXY=1` only behind a trusted reverse proxy that overwrites forwarded
headers.

Operator notification requires `ARR_SMTP_HOST`, `ARR_SMTP_PORT`,
`ARR_SMTP_FROM`, and—when applicable—`ARR_SMTP_USERNAME` and
`ARR_SMTP_PASSWORD`. Set `ARR_SMTP_SSL=1` for implicit TLS or leave
`ARR_SMTP_STARTTLS=1` for STARTTLS. Set `ARR_INTAKE_ORIGIN` to the public HTTPS
origin so the email contains the correct protected editor link. The notification
contains no PDF or abstract. SMTP delivery failures are recorded in the audit log
and must trigger operational monitoring.

`/healthz` proves the process and database are alive. `/readyz` returns HTTP 200
only when the HTTPS origin, secure cookie, malware scanner and operator SMTP notice
are configured; production routing must use `/readyz` as its readiness gate.

After the receiver is deployed and `/readyz` passes, set the GitHub Actions
repository variable `ARR_INTAKE_URL` to its HTTPS origin. The next Pages deployment
will turn the disabled control at `/submit/` into a direct link to the private form.
Do not set the variable before the production checklist is signed.
