# Account-free paper management (2026-10-29)

The primary human entry is `/paper/new` (also reached from `/submit`). Selecting
a PDF opens the details and a 256-bit key on the same page, without a private
account. The initial request creates only an empty draft and isolated internal
depositor; it does not upload the PDF. The file input stays intact. With JavaScript
off, the existing key-first form remains available. Subject search uses the shared
catalogue. Optional title/abstract extraction uploads a scanned temporary copy
without using an external AI service. Draft autosave contains metadata only.
`/manage` accepts the key by POST, never via a URL. The database stores only its
SHA-256 digest; signed sessions contain a paper identifier/generation/expiry,
not the key. Rotation invalidates old sessions on every protected request.

Draft text is saved on the server. Submission reservation and revision links are
committed with the PDF record, preventing duplicate retries and parallel forks.
Previously published/reviewed versions and their approvals are never inherited
or overwritten. Private withdrawal uses the existing seven-day retention sweep;
public withdrawal creates an editorial request. No automatic public deletion or
public release is claimed. No test upload is needed in production.

Deployment: deploy the intake first with `init-db`, check `/paper/new`, `/manage`,
`/readyz`, and the isolated tests, then deploy GitHub Pages. Do not deploy the
new public promise while the receiver still runs the old code. The migration is
additive. Run `paper-draft-sweep` daily to expire never-submitted draft details
older than 90 days; it does not erase published/submitted cases or key hashes.

# AIRR private intake service

This service is the direct private-submission boundary in front of the public AIRR
repository. Authors use one secret key per paper, without registration, author
email or legal name. Existing alias/password workspaces remain available for their
existing papers and delegated agents. The service accepts PDF manuscripts into
non-public quarantine, fails closed when malware scanning is unavailable, emails
the operator a protected case link without attaching the manuscript, and records
human decisions. It never publishes a submission or writes to `papers/`.

The form uses the shared multidisciplinary subject vocabulary, with one main
subject, up to two additional subjects and an optional emerging topic. The
versioned selection is stored with the case and shown on receipts and editor
pages. Run `init-db` before upgrading an existing installation; its additive
classification migration is idempotent. See
[`docs/SUBJECT_TAXONOMY.md`](../../docs/SUBJECT_TAXONOMY.md) for scope, provenance,
selection rules and publication handoff.

After storing an upload, the receiver redirects to a session-protected receipt
with the assigned `SUB-...` registration number, received timestamp, manuscript
hash, current state and a downloadable text receipt. The number proves receipt,
not approval or publication; it is not the final identifier of a published paper.
The receipt displays the shared destination from `site/donations.json`, an optional
PayPal link and a copyable registration reference. No paper data is automatically
sent to PayPal. Payment notes have no effect on editorial decisions.

`/receipt` and `/receipt/download` show the latest receipt in the submitting
browser session. The persistent case and its correspondence are available after
entering the paper key at `/manage` (or the original account at `/account` for
older workspace submissions). The registration number is
never an access credential. Receipts, forms and editor pages carry `no-store` and
`noindex` responses. Safety-rejected files get a rejection explanation rather
than a donation invitation. Each account has a rolling allowance of 10 papers in
24 hours shared by form and delegated agents; see the production runbook for
attempt limits and delegation scopes.

The hosted AIRR pilot opened on 8 September 2026 after recorded operator
authorization and production checks. Every new installation still requires its
own evidence under [`docs/INTAKE_OPERATIONS.md`](../../docs/INTAKE_OPERATIONS.md);
this README does not open an installation or authorize publication.

## Keep an author workspace and editorial account signed in

When signing in to an editorial account from an authenticated author workspace,
select **Keep my author workspace signed in on this browser**. The reverse
option is available on workspace sign-in. Both accounts must be authenticated
with their existing credentials; editorial sign-in still requires the second
factor or a valid unused recovery code. No alias-to-editor link is inferred.

The signed-in page offers a button to switch between the two authenticated
accounts. Only the selected account's permissions apply to each request; this
does not merge roles, grant editorial access to an author, or waive the
author-editor conflict and review rules. This is one browser session containing
two independently authenticated identities, not a permanent account link.
Retention is opt-in; leaving the option unchecked replaces the earlier account
as before. Signing out explicitly clears both. Workspace credential changes and
account deactivation are checked before a saved account can be selected. Session
expiration and the existing secure-cookie settings remain unchanged. Each
account keeps its own idle deadline: activity as author cannot keep an unused
editorial sign-in alive past the configured session lifetime, or vice versa.

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
Do not set the variable before the reception-readiness record is complete and authorized.

## Editorial workflow and controlled opening

`ARR_INTAKE_OPEN` defaults to `0`. HTTPS/editor setup can operate while public
upload remains closed. Opening requires both `ARR_INTAKE_OPEN=1` and an evidenced
`ARR_LAUNCH_APPROVAL_FILE` (default `/etc/airr-intake/launch-approval.json`) covering
the `AIRR-PILOT-1.0` reception checks and real authorization source, plus an active
operator TOTP account. An independent editor is still required for other conflicted
final decisions and appeals; founder-authored decisions follow AIRR-FOUNDER-1.0.
The example file contains no approvals. `flask launch-status`
reports this gate.

Authors manage new papers with their individual secret keys; existing workspace
users retain their password and recovery code. New submissions do not request author email or send author access
links. The operator still receives minimal email notifications. Legacy queued
mail/token paths remain for compatibility and retention of older records; they
are not the current sign-in flow. Never enable URL/access logging at the proxy.
`send-pending-mail` handles queued messages; uncertain SMTP results require
investigation, not automatic retry.

Editors declare the exact providers/models and their service-specific notice
before recording reports. The author separately confirms the plan. After the
first report the declared set cannot be changed. Each required model must have a
report before acceptance. A signed, evidenced adjudication may explain an
inapplicable blocking report without altering its score or original response.
Conflicted adjudications and final decisions require an independent editor.

After a changes request, the author may upload a corrected PDF using their private
case session. The original and reports remain separate; the correction has its
own ID, parent link, revision number and hash, and needs a new authorized audit.
An appeal pauses deletion and can be resolved only by an independent editor other
than the original decision-maker. Public distribution permission is a separate
author action on the accepted exact version. The release handoff exports approved
scholarly metadata/reports/adjudications without author email or access links; it
does not commit to GitHub or publish a record.

Use `invite-editor EMAIL --name NAME --role operator|independent_editor` for a
24-hour setup link. Give it directly to the intended person. They choose their
own password, prove possession of their authenticator, and save eight one-use
recovery codes. Do not open the setup page on their behalf or copy its secrets.
The command cannot replace active credentials. `workflow-sweep` expires setup and
access links and erases delivered email bodies after seven days.
