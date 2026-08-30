# ARR private intake service

This service is the private, invitation-only boundary in front of the public ARR
repository. It accepts PDF manuscripts into non-public quarantine, fails closed
when malware scanning is unavailable, and records human decisions. It never
publishes a submission or writes to `papers/`.

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

Create a one-use, email-bound invitation:

```console
flask --app services.intake.app invite author@example.org
```

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
