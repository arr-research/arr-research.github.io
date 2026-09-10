# Historical operator-authored revision intake (disabled by default)

This adds a private revision receipt linked to a public historical record without
inventing an `author_case`. Netcup remains the receiver/storage host; Backblaze B2
remains backup storage. No hosting or DNS change is needed.

## Trust and scope

The operator installs a reviewed catalogue snapshot keyed by public AIRR ID. Each
entry contains `record_id`, `version_id`, `version`, `canonical_sha256`, and
`authors` (list). It must describe the latest published version; check it against
the immutable public release and actual canonical PDF before installing it. The
receiver never fetches an agent-controlled URL. The entire catalogue is hashed;
any subsequent change invalidates unconsumed revision bindings until authorized
again. This is a trusted operator-installed snapshot, not live proof of ownership
or a cryptographically signed public registry.

Only records whose sole author equals configured `AIRR_HISTORICAL_OPERATOR_AUTHOR`
qualify. The configured MFA operator explicitly attests authorship and assigns
their real private depositor workspace. This is an operator-recorded external
author instruction, not a simulated web signature or independent adjudication.
Multi-author and third-party historical records are outside this first scope.

Existing five-upload grants cannot create revisions. A new grant covers only
`revision:create` and `submission:receipt`, one exact new PDF, one new version ID,
and 24 hours. No automatic renewal, editorial access, assessment-provider consent,
acceptance or publication is granted. Existing workspace revocation applies.

## Explicit authorization on the authenticated host

After review, deployment and migration, run:

```
flask --app services.intake.app authorize-historical-revision /private/evidence.json
```

Capture stdout in a protected file: it contains the one-time bearer token. Never
send it to logs or commit it. Server tables retain only the token hash. The
command requires an active configured MFA operator and a real depositor profile.
Authenticated host administration is the trust boundary of this CLI, matching the
existing host preparation commands; it is not remotely callable via the API.

Evidence fields (exact set): `owner_user_id`, `agent_name`, `agent_version`,
`binding`, `author_instruction`, `source_reference`, `recorded_at`, `scope`,
`terms_version`, `privacy_version`, `operator_authorship_confirmed`. Record the
actual instruction and source, current terms/privacy acknowledgment and a recent
offset-aware timestamp (not future, at most seven days old). Set scope exactly to
`["revision:create", "submission:receipt"]`; authorship confirmation must be true.
Do not populate missing human evidence with invented text.

Binding fields: `paper_id`, `record_id`, `supersedes_version_id`, `parent_sha256`,
`version`, `version_id`, `sha256`, `changelog`. The first identities/hashes must
match the catalogue; version is the next integer version and version_id is a new
`arr:version:UUID`. Changelog has exactly `mathematics`, `scope`, `reproducibility`,
`version`, `editorial`, each with an explicit explanation (including unchanged).

## Receiving the PDF

`POST /api/v1/revisions` uses the same multipart metadata, actual PDF, Bearer
header and stable Idempotency-Key as `/api/v1/submissions`. Do not add binding
fields to metadata: they are already locked in the separately authorized grant.
The new hash, author and conflict disclosure must match. Both the initial upload
and retries check actual PDF bytes. New-deposit/revision tokens are mutually
excluded from the other's endpoint.

The existing storage/scanner/limits/notifications remain in force. In the same
database transaction, receipt identity is associated with the frozen binding in
`historical_revisions`. The private case's parent_id remains NULL and its private
revision counter stays distinct from the public version label. A unique version
ID prevents two receipts claiming that same public candidate; failed reservations
roll back the file and grant consumption. Malware results remain safety outcomes,
never scientific acceptance. No public record/PDF/tag is changed.

Receipt JSON includes `historical_revision` with the complete binding/changelog.
The depositor/operator case also retains the binding in agent provenance. Fetch
the receipt through `GET /api/v1/submissions/<SUB>` with its active owning grant.
Expired/revoked grants stop API receipt access; the owner's private case remains
subject to the existing workspace workflow. After expiry do not resend blindly:
use that case to reconcile a previously uncertain result.

## Activation on the existing Netcup host

1. Review this change and its tests; take the existing consistent encrypted backup.
2. Deploy code without enabling the feature. Run existing `init-db`: migration is
   additive and idempotent. Preserve production records and existing grants.
3. Install the verified latest-public-version catalogue as a root-managed private
   file, readable by the service. Set `AIRR_HISTORICAL_REVISION_CATALOGUE` to it,
   `AIRR_HISTORICAL_OPERATOR_AUTHOR` to the exact public author name, and only then
   explicitly enable `AIRR_HISTORICAL_REVISIONS_ENABLED=1` and restart normally.
4. Record actual operator authorization for the prepared v2 and real owner ID.
   Issue the scoped grant and store its token securely. This is a new explicit
   permission, never an expansion of the earlier deposit grant.
5. Upload the already prepared v2 bytes, verify the returned hash and historical
   binding, then follow the existing authorized assessment workflow. No evaluation
   or publication follows automatically from this receipt.

To stop new historical revisions, disable the flag; receipt reads remain available
to active grants. Revocation disables both uses. Rollback must retain the additive
tables and newly received PDFs. Do not restore an old database over real cases.

Private bindings follow case retention: erasing a private manuscript erases its
receipt binding; subsequent grant cleanup removes its authorization evidence.
Keep the research version/provenance package independently with the original
sources. This private intake is not an immutable public preservation service.

No production deployment, catalogue installation or grant issuance is performed
by committing this code.
