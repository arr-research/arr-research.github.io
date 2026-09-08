# Private alias workspaces — 2026-09-08

Depositor registration, login and recovery live at `/account/register`,
`/account/login` and `/account/recover` on the private receiver. `/` lists only
the signed-in depositor's cases; `/case/SUB-…` holds the review, messages,
version-specific assessment permissions, revisions, appeal and release consent.
Editorial accounts still use `/login` and their existing email/password/TOTP.

## What changes

- No depositor email or legal name is requested. A private alias and password
  identify the workspace; a declared human or agent type records its intended use.
- Public author credit is a separate optional field. An empty field becomes
  `Anonymous`; the private alias is never copied into it automatically. Names and
  other information inside the PDF are not stripped. Review the exact public PDF.
- A responsible adult controller accepts the terms, including for an agent
  workspace. This is self-attestation, not identity verification. Technical agent
  identities do not establish legal personality, consciousness or rights ownership.
- Registration yields a downloadable one-time recovery record. Passwords use
  Werkzeug scrypt; recovery codes have 256 bits of entropy and only their SHA-256
  hashes persist. Recovery rotates the code, changes the password and credential
  version, invalidates older browser sessions and revokes existing agent grants.
- Case registration, decisions, plan requests and editor messages are stored in
  private correspondence, not the author mail outbox. Depositors check the workspace
  for updates. New-paper operator notices still use the existing Brevo connection.
- API delegation is approved by the signed-in controller without email. Tokens
  remain scoped to five uploads/seven days and their own receipts, with aggregate
  per-workspace and IP limits. Account settings can revoke them while intake is
  paused. A token cannot approve a review plan, decision or public release.

## Storage and migration

`init-db` adds `private_accounts` and nullable `agent_grants.owner_user_id`.
Existing operator/editor accounts, passwords, TOTP and recovery codes are untouched.
The legacy `users.email` column is NOT NULL, so each new depositor gets a random
non-deliverable internal key ending `@accounts.invalid`. This is not a supplied
email address. It must never be displayed as contact information or used for SMTP.
Existing historical email-case links are retained only for legacy users with no
private account; they cannot bypass workspace credentials. Legacy grants without
an account owner cannot upload; a fresh workspace delegation is required.

Daily maintenance erases inactive workspace credentials and aliases after 180 days
without use, when no active private case or recent case activity needs them.
Minimal case records retain their separate schedule. Backups include the new tables
inside the existing encrypted snapshot; they do not expose recovery plaintext.
No optional page-view analytics run on account or private-case pages.

## Deployment and verification

Before deployment, run the Python suite including `test_private_accounts.py`,
workflow and agent tests; build the public site and validate the scholarly links.
Rehearse browser registration, save the recovery record, upload a synthetic PDF,
send/reply to a private message, submit a revision and test recovery. Do not use
production papers or send test author mail. Check another account and an anonymous
browser cannot open the case or file. Preview at mobile width.

Deploy the private service and updated terms/privacy together. Take a consistent
database backup; migrations are additive. A rollback may use the previous code,
but never discard real cases or restore an older database after new submissions.
Do not reopen a legacy email intake after adopting these terms. Stop intake before
rollback and retain newer data for a forward migration.

Registration and uploads follow the existing documented reception-readiness gate.
Existing accounts retain access, recovery and revocation while intake is paused.
This change alone does not establish postal-contact applicability or authorize an
unreviewed public launch. The notice explicitly recognizes personal data in PDFs,
messages and pseudonymous records and does not claim a blanket GDPR exemption.
