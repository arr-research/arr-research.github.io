# Standing ordinary-deposit delegation

AIRR-STANDING-DELEGATION-1.0, 6 November 2026.

An authenticated host operator may record a genuine external instruction once
for an existing, previously approved ordinary agent delegation. This opt-in
extension removes that delegation's seven-day expiry and five-deposit lifetime
allowance. Other delegations retain their existing limits. It does not create a
new credential, change ownership, consume another user's grant or reset its uses.
Existing receipts and idempotency keys remain valid.

Run on the authenticated application host:

```
flask --app services.intake.app record-standing-agent-delegation /private/evidence.json
```

The evidence must contain exactly `grant_id`, `human_name`, `human_instruction`,
`source_reference`, `recorded_at` (recent timezone-aware timestamp), and `scope`
equal to `["submission:create", "submission:receipt"]`. Name the configured active
MFA operator and preserve the actual instruction. Store evidence only in the
private instance; never commit it or its bearer token to the public repository.
Replaying identical evidence is idempotent; conflicting evidence cannot silently
replace the existing record. The record is an operator-recorded external
instruction, not a simulated human browser signature.

The ordinary workspace revoke action remains authoritative, including after the
original expiry. Inactive/deleted owners, changed terms, closed intake, scanner,
size, integrity, rate controls and ordinary account rolling limits still apply.
Historical revision grants cannot be extended through this feature. No author
public permission, provider transfer consent, model review, editorial acceptance,
public license or publication scope is added.

Status returns `standing_delegation: true`, `expires_at: null` and
`uploads_remaining: null`; null means no lifetime cap for this one delegation,
not zero uses or a fabricated future expiry. A revoked standing grant still
reports revoked and cannot upload or read receipts. Uses continue to be counted.

Deployment is distinct from activation: migrate the database using `init-db`,
deploy the tested service, record the actual instruction on the host, then verify
the live status with the existing protected credential. A merged GitHub change
alone is not an active server policy. Keep a tested rollback and encrypted backup.
