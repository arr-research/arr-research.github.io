# Private intake production runbook

## Launch gate

The invitation pilot may receive real manuscripts only after every item is signed
and dated by the operator:

- [ ] Swedish/EU counsel reviewed terms, privacy, DSA/e-commerce classification,
  complaints and the intended hosting arrangement.
- [ ] A stable service/postal address is published without exposing a home address.
- [ ] Every infrastructure/email/backup/scanning processor, DPA, location,
  subprocessor and transfer safeguard is recorded in `PROCESSING_RECORD.md`.
- [ ] The intake instance directory and backups are encrypted, private and outside
  the public Git checkout; restore and erasure have been tested.
- [ ] HTTPS, HSTS, a 32-byte-or-longer persistent session secret and secure cookies
  are verified; proxy forwarded headers are trusted only from the actual proxy.
- [ ] ClamAV definitions are current and a harmless EICAR test proves detection.
  The service proves fail-closed behavior when the scanner is stopped.
- [ ] Operator TOTP and a recovery procedure are tested; an independent editor has
  been appointed for conflicts/appeals and also uses TOTP.
- [ ] Daily `scan-pending` and `retention-sweep`, monitoring and encrypted backups
  are scheduled; failed jobs alert the operator.
- [ ] A breach tabletop verifies containment, evidence, risk assessment and the
  conditional 72-hour IMY process.
- [ ] An end-to-end dummy case proves invitation, upload, clean/infected paths,
  manual accept/decline, conflict escalation, appeal and deletion.

Until every item is complete, the public site may invite **expressions of interest
without attachments** but must not issue live upload credentials.

## Per-case procedure

1. Receive only name, email, field and title in the invitation request. Reject email
   attachments and ask the sender to delete/resend safely.
2. Create one email-bound, single-use invitation expiring in 7 days.
3. The author creates an account, accepts the versioned notices and uploads a PDF.
4. The service stores random bytes outside the web root and scans. No editor can
   download until status is `clean`; scan errors stay in quarantine.
5. Verify identity/authority, scope, rights, disclosures, conflicts and minimum
   completeness before substantive assessment.
6. Review the exact SHA-256 version. External AI gets nothing unless the recorded
   optional choice is reconfirmed after the provider-specific notice.
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
