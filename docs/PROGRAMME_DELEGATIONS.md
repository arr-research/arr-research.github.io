# Continuous author programme delegation

An authenticated host operator can record **one actual initial author instruction**
for a named, sole-author programme. That instruction remains active until revoked.
The agent can then request exact-PDF intake permissions without claiming that the
author has supplied a new reply for each PDF. This feature is disabled by default;
set `AIRR_PROGRAMME_DELEGATIONS_ENABLED=1` only after reviewed deployment and `init-db`.

This does not disable authentication, quotas, malware scanning, rights checks,
historical-predecessor validation or editorial controls. It does not alter existing
ordinary grants or historical single-PDF grants. A controller token cannot upload,
read cases, transfer manuscripts to models, accept papers or publish them.

## Initial instruction, recorded once

Use the existing authenticated host, with the service environment loaded:

```
flask --app services.intake.app authorize-programme /private/actual-instruction.json
```

The evidence JSON has exactly these fields:

```
owner_user_id, programme, author, author_instruction, source_reference, recorded_at,
terms_version, privacy_version, rights_confirmed, operator_authorship_confirmed,
paper_ids, allow_new_submissions, pdf_license, metadata_license, publication_status
```

Use the real active human depositor ID, configured sole operator-author, original
instruction and its real source. Initial `recorded_at` is offset-aware, no more
than seven days old. Rights/authorship attestations must actually be true. Use an
explicit list of existing AIRR paper IDs and boolean permission for new manuscripts.
This route supports `CC-BY-4.0`, `CC0-1.0`, `working_paper` only. It does not turn a
standing licence instruction into editorial acceptance. Never invent a fresh human
assent on renewal. Changed terms/privacy require an updated initial instruction.

Capture stdout privately: it contains `programme_id` and `controller_token`. Store
the token in the current user's protected credential store. The database retains
only its hash. There is no expiry on the initial programme instruction; the owner
can revoke it in their normal private workspace, or an authenticated host operator
can run `revoke-programme PRG-...`. Password changes and account recovery revoke it
as well. Inactive/erased workspaces cannot issue or use child grants.

## Per-artifact machine step

`POST /api/v1/programme-artifact-grants`, HTTPS Bearer controller token:

```json
{
  "sha256": "the exact lowercase PDF SHA256",
  "kind": "revision",
  "binding": "the existing complete historical binding object, not a string",
  "agent_name": "Actual preparing agent",
  "agent_version": "Actual declared version"
}
```

For a new manuscript, `kind` is `submission` and `binding` is null. A revision must
match the trusted installed latest-public catalogue and one of the instruction's
paper IDs. No agent-provided predecessor URL is fetched or trusted. The response
contains a normal **24-hour, one-use exact PDF** grant and its explicit scope. Use
it at `/api/v1/revisions` or `/api/v1/submissions` as appropriate, with the existing
stable upload idempotency key. Metadata must identify the sole authorized author,
confirm rights and disclose operator conflict. Actual uploaded bytes are checked.

Identical artifact requests return the same grant, token and original expiry;
they do not create new cases or silently renew expired permission. After an
expired grant, reconcile the existing case before retrying. A caller may add
`renew_expired_unused: true`; the server renews the SAME grant only if both its
usage counter is zero and no receipt mapping exists. A consumed or revoked grant
cannot be renewed. Preserve original receipts and exact artifact records.
No additional human confirmation is required while the initial scope is valid.
An initial token cannot be used as an upload or editorial credential. Revocation
and changed contracts stop both issuance and existing child upload/receipt access.

Account quotas and rate limits remain in force across all child grants; obtaining
several grants does not obtain extra upload capacity. Exhaustion is a queue state,
not a reason to create another account or bypass the limit. Existing receipt,
malware, publication-permission and Working-paper release procedures remain in force.

## Deployment

Follow the existing deployment runbook: consistent encrypted backup and verified
recovery, additive migration, existing data preservation, service validation and
readiness before reopening. Install code before enabling the flag. Keep original
author instruction and every PDF/assessment/receipt/release manifest linked by hash.
Do not claim continuous execution or release before checking the public PDF bytes.
Repository tests cover multiple exact artifacts under one unchanged instruction,
retry identity, normal new deposits, wrong authors/bytes, scope separation,
revocation, disabled feature, stale catalogue, changed terms, expiry and quota.
