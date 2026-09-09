# Private intake production runbook

## Local antivirus transport

The default `clamdscan` client streams to the configured local ClamAV daemon.
Passing file descriptors across the application's systemd mount namespace caused
AppArmor to reject an actual upload on 2026-09-08, despite a successful daemon
ping. Do not disable AppArmor or widen manuscript permissions to work around it.
Readiness now scans harmless bytes from the actual quarantine directory under
the application's service identity, with a four-second timeout and cleanup.

On the configured Netcup host, `/tmp` is tmpfs and ClamAV's stream limit is
26,214,400 bytes, matching the 25 MiB upload cap. Preserve local-only daemon
access and memory-backed scanner temporary storage when reprovisioning. A
custom scanner must pass the same actual-file readiness check.

## Planned upgrades and monitoring

Use the current `services/intake/deploy/upgrade.py` with a full pinned commit.
The helper first pauses the monitor timer and lets any running monitor finish.
It then pauses and drains other background jobs before stopping the application.
Executing oneshot jobs can be `activating`, so `is-active` alone is insufficient.
If a job does not finish within the bounded wait, the upgrade aborts before
application downtime and restores the timers.

On completion or rollback, background timers resume before monitoring. If a
worker fails to restart, the monitor is still resumed to report that real fault.
This ordering avoids alerts caused solely by the planned pause; it does not
disable health checks or notification settings. After an upgrade, inspect the
latest `/var/lib/airr-monitor/status.json` and check its timestamp and all results.

## Launch gate

The direct-submission pilot uses the versioned `AIRR-PILOT-1.0` readiness record.
The record identifies the real operator's authorization, its date and source,
and evidence for the checks below. An installation tool may record an explicit
operator instruction; it must not invent a signature or completed review.
Reception is separate from editorial acceptance and public release.

- [x] The operator supplied and authorized the service/postal contact in
  `LEGAL_AND_COMPLAINTS.md` on 2026-09-08. Verify the actual public contact page
  before installing the launch record.
- [ ] Terms, privacy, contact, complaint handling, actual infrastructure recipients,
  contracts, locations and transfer arrangements have a documented review in
  `PROCESSING_RECORD.md`. Record unresolved points and seek qualified advice where
  needed. A blanket requirement to hire counsel is not a technical reception gate,
  and the record must not claim external legal certification.
- [ ] The intake instance directory and backups are encrypted, private and outside
  the public Git checkout; restore and erasure have been tested.
- [ ] HTTPS, HSTS, a 32-byte-or-longer persistent session secret and secure cookies
  are verified; proxy forwarded headers are trusted only from the actual proxy.
- [ ] ClamAV definitions are current and a harmless EICAR test proves detection.
  The service proves fail-closed behavior when the scanner is stopped.
- [ ] Operator TOTP and a recovery procedure are tested. Independent editors require
  TOTP when appointed; their appointment is required before handling a conflicted
  final decision or an appeal, not before receiving an ordinary manuscript.
- [ ] Daily `scan-pending` and `retention-sweep`, monitoring and encrypted backups
  are scheduled; failed jobs alert the operator.
- [ ] The incident procedure covers containment, evidence, risk assessment and the
  conditional 72-hour IMY process. Record the technical exercises actually run;
  do not present an automated rehearsal as the operator's personal participation.
- [ ] The public receiver uses a bot trap plus IP and private-account limits; abuse
  monitoring and an emergency shutdown procedure are tested.
- [ ] The host uses `/readyz` for readiness and refuses traffic while HTTPS origin,
  secure cookies, the scanner or SMTP operator notice is missing.
- [ ] An end-to-end dummy case proves direct upload, operator email notification
  without an attachment, clean/infected paths, manual accept/decline, conflict
  escalation, appeal and deletion.

Independent custody of recovery keys is an ongoing continuity task: record its
actual status and owner. A verified restore does not prove independent custody.
Do not replace an existing unresolved task with a fictional completion date.

Until reception checks are complete, the public site must keep the direct-submit button
disabled. It must not solicit invitations or accept manuscript email attachments.
After recorded authorization and a successful `/readyz`, set the repository variable
`ARR_INTAKE_URL` to the receiver's HTTPS origin and redeploy Pages.

The readiness record does not grant editorial powers. If an independent reviewer
is unavailable, a blocking report cannot be overruled and an appeal stays
unresolved. A clean founder-authored round may use the disclosed self-publication
path; reception readiness itself never authorizes a decision.

## Per-case procedure

### Submission limits

Each account has a rolling 24-hour allowance of 10 submissions, shared by the
web form and all its agents. Each connection has a broader limit of 50 attempts
per channel (form or agent API) over the same period, allowing shared networks.
Existing rate counters survive upgrades. A completed agent retry with the same
idempotency key recovers its receipt without using another submission allowance.
Invalid attempts that reach a rate check can count toward it; limits do not reset
at midnight. PDFs remain limited to 25 MiB and the antivirus check still applies.
These limits do not enlarge any existing agent delegation's five-PDF scope.

### Delegated agents

The [agent API](AGENT_SUBMISSIONS.md) uses this same launch gate. An agent first
requests a delegation without uploading a PDF or sending an email. The responsible
adult signs into an alias workspace, reviews and approves the scope there.
Permission lasts seven days, permits at most five PDFs and can be revoked in
workspace settings even while intake is paused. Global, IP and account limits apply.

The API checks the declared PDF hash and uses idempotency keys to recover receipts
without duplicating cases. A token reads only its own receipts, never a PDF,
editor page, another grant's case, assessment authorization or release controls.
Workspace approval establishes an authenticated action, not verified legal identity.
The responsible person still needs the authority checked during screening.

Test pending/expired/revoked/exhausted grants, link previews, missing CSRF,
cross-grant access, changed-content retries, scanner failure, pending-authorization
erasure and large multipart spooling before opening. Agent labels, purpose and
manuscript metadata are untrusted data. Receipt donation information is not
permission for an agent to pay. Public release must preserve the declared agent
provenance where relevant and authorized.

### Browser form and shared review

1. The responsible adult signs into a private alias workspace, supplies scholarly
   metadata, accepts the versioned terms/privacy notice and uploads one PDF. No
   email, legal name or invitation is required; public author credit is optional.
2. The service enforces CSRF, bot-trap, per-IP and per-account limits before accepting
   the manuscript.
3. The service stores random bytes outside the web root and scans. No editor can
   download until status is `clean`; scan errors stay in quarantine.
   The depositor then sees a browser-session receipt with their assigned `SUB-...`
   registration number, timestamp, fingerprint and downloadable text. It explicitly
   distinguishes pending approval from registration. The optional PayPal reference
   is a non-secret registration number, not a manuscript access credential; it may
   be copied by the donor for support administration only. No donation is required
   and no donation fields enter the editorial data or ranking.
4. Email the operator only the case identifier, title, scanner state and protected
   editor URL. Never attach the PDF or abstract. SMTP failure is audited and alerted.
5. Verify identity/authority, scope, rights, disclosures, conflicts and minimum
   completeness before substantive assessment.
6. Review the exact SHA-256 version. External AI gets nothing until the depositor separately confirms the declared
   provider-specific notice in their private case. The initial screening
   acknowledgment is not transfer authorization.
7. Lluis records accept, decline or changes requested. A conflict routes acceptance
   to the independent editor. No decision publishes automatically.
8. Notify the depositor, explain the appeal window, then allow the separate public
   packaging/release workflow only for a final acceptance.
9. Run and audit retention erasure.

## Incident procedure

Contain access, preserve proportionate logs, rotate affected credentials, identify
data/people/impact, document the risk decision, notify the processor/controller as
applicable and assess IMY notification. A notifiable personal-data breach is sent
without undue delay and, where feasible, within 72 hours of awareness. Notify
affected people when legally required. Record why notification was or was not made.

## Private alias workspaces

See [PRIVATE_WORKSPACES.md](PRIVATE_WORKSPACES.md) for registration, recovery, no-email correspondence, migration, validation and rollback. Removing contact fields does not change the separate documented reception-readiness gate or prove a legal exemption.
