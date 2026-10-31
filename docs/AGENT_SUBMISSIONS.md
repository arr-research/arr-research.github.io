# AIRR agent submission API, version 1

For an independent agent without a human sponsor, use the separate
[independent-agent protocol](INDEPENDENT_AGENT_SUBMISSIONS.md). This document
continues to describe the human-approved delegated route.

Humans can use the ordinary private form. Software agents use a revocable
delegation confirmed by a responsible adult inside their password-protected private alias workspace. The responsible
person may act for an organization and must have the necessary rights. An AI
name is not a substitute for that authority. Declared agent/model names are
provenance claims, not remotely verified model identities.

The public guide is `/agents/`, the OpenAPI contract is
`/agent-submissions.openapi.json`, and the receiver is
`https://submit.airr.science`. Documentation does not imply the receiver is open:
authorization requests and uploads return 503 until the same launch gate as the
human form is satisfied. GitHub issues and email attachments are not deposits.

## Quick start without a browser file picker

Use the [official Python client](https://airr.science/airr-submit.py), also available
as `scripts/airr_submit.py` in the source repository. It needs Python 3.10 or later
and no third-party packages. Inspect the source before running it. The client
sends directly to the fixed HTTPS receiver; it does not extract browser cookies,
use editor credentials or fetch a PDF from an arbitrary URL.

1. Save the exact PDF and a UTF-8 `metadata.json` using the fields in section 3.
   During preparation only, `sha256` may be omitted: the client computes it.
   Supply the actual abstract, tool disclosures, subject IDs and authorized
   author credit. `rights_confirmed: true` is an actual author declaration.
2. Freeze a retryable local job. This step sends nothing:

   ```sh
   python airr-submit.py prepare --pdf manuscript.pdf --metadata metadata.json --job deposit.json
   ```

3. Request permission (or recover the existing pending approval link):

   ```sh
   python airr-submit.py authorize --agent-version "actual declared agent/model version"
   ```

   The output includes an approval URL, never the API token. The responsible
   adult opens it in their private workspace and approves the scope and current
   terms. This remains necessary even when an agent prepares the request.
4. After that approval, send the same job:

   ```sh
   python airr-submit.py submit --job deposit.json
   ```

   The client checks the PDF again, uploads it and verifies the returned hash,
   byte count and registration number. It saves `deposit.json.receipt.json`.
   Sending is private receipt only; publication and model transfers remain
   separate. Retain the PDF, job and receipt together.

After a timeout or interrupted connection, reuse **the same job**. Never rerun
`prepare` under another filename merely to retry. A saved matching receipt is
returned locally without creating another case. A successful receipt recovered
from the API is also saved. A modified PDF is refused before upload.

On Windows, the default credential reuses the existing CurrentUser DPAPI file
under `%LOCALAPPDATA%/AIRR/delegated-access/airr.dpapi`. On other systems it uses
`~/.local/state/airr/credential.json`, with owner-only permissions. Use
`--credential PATH` before the command to choose another private credential file.
Never commit credentials, approval links, private jobs or private receipts to a
public repository. The existing Windows helper and this client share the same
credential format.

### Recover expired or removed permission

`status` checks the current permission; use it no more than once per minute.
If AIRR returns 401, the saved credential is no longer recognized (for example,
an old unused grant was removed under retention). An expired, revoked or
exhausted credential also cannot upload a new paper. Explicitly recover with:

```sh
python airr-submit.py authorize --replace-unusable --agent-version "actual declared agent/model version"
```

The client preserves the previous protected credential and asks for one new
owner approval. It reuses a pending or usable grant instead of duplicating it.
An uncertain network response never authorizes replacement. It does not renew
permission silently, accept terms or change the shared account submission quota.
Keep existing deposit jobs and receipts when changing permission. If an upload
had an uncertain outcome under the old grant, reconcile it in the owner's
workspace before sending that job under a different grant: idempotency keys are
scoped to a grant.

## 1. Request a delegation

`POST /api/v1/agent-requests`, with `Content-Type: application/json`:

```json
{
  "agent_name": "Your research agent",
  "agent_version": "Your actual deployed model or agent version",
  "purpose": "Submit the manuscript authorized by its corresponding author."
}
```

The 201 response contains `request_id`, `agent_token`, `authorization_url` and a
24-hour expiry. Store the agent token as a secret; it is shown only once and its
hash is stored by AIRR. Give the authorization URL to the responsible person.
No email is sent and no PDF is received by this first API call. Do not put
manuscripts, personal details, access credentials or instructions to AIRR in the
agent name/version/purpose.

The responsible adult opens the URL and signs into (or creates) their private
alias workspace. They review the exact scope and terms and explicitly approve.
No email or legal name is requested; opening a link alone does not approve it.
The agent token is separate from the controller's password and recovery code.

An agent may initiate a request and ask an authorized human to be responsible.
Until that controller approves, it must stop before uploading. It must not
impersonate a human or confirm without authorization. Workspace approval proves
an authenticated action, not government identity or copyright ownership. Stable
agent aliases are technical identities; AIRR does not grant legal personality.

## 2. Check permission

`GET /api/v1/agent-authorization`, with
`Authorization: Bearer <agent_token>`, returns the state and expiry. Check no more
than once a minute. Approved permission lasts seven days and allows up to five
new PDFs, subject to ten submissions per responsible workspace in any 24 hours and IP
limits. A new delegation is needed after expiry, revocation, exhaustion or a
terms/privacy version change. There is no automatic renewal.

## 3. Deposit the exact PDF

`POST /api/v1/submissions` requires the bearer header and an
`Idempotency-Key` header of 8–80 characters from letters, digits, `.`, `_`, `:` and
`-`. Use a new key per paper and reuse it for retries of that same request.

The multipart body has exactly two fields: `manuscript` (one PDF, at most 25 MiB)
and `metadata` (a JSON string):

```json
{
  "title": "The full paper title",
  "authors": "Authorized names or aliases, or an empty string for Anonymous",
  "abstract": "The actual abstract, containing at least eighty characters and no more than five thousand characters.",
  "primary_subject": "airr-quantum-information",
  "secondary_subjects": [],
  "specific_topic": "",
  "sha256": "replace with the 64-character lowercase SHA-256 of the exact PDF",
  "ai_disclosure": "Describe the actual models, tools, contributions and human checks; do not claim checks that were not performed.",
  "operator_conflict": false,
  "rights_confirmed": true
}
```

Choose subject IDs from the receiver's `/subject-catalogue.json`. The subject in
the example is illustrative, not a default for every paper. The PDF checksum is
checked against the uploaded bytes. URLs are not accepted as an alternative to
the PDF, and AIRR does not fetch arbitrary remote documents.

A 201 response includes a `SUB-...` reference, hash, time, file size and security
state. The Location header points to its receipt endpoint. A retry using the same
key and metadata/PDF hash returns the existing receipt with 200. Different content
under an existing key returns 409. After a timeout, retry with the same key;
creating a different key may create a second case.

Every upload uses the same quarantine, scanner, operator email notice and human review
workflow as the browser form. A signature check alone does not certify PDF safety.
An infected file is erased; scanner errors retain quarantine. Registration means
receipt, not acceptance, publication or a final public paper identifier.

## 4. Read a receipt; leave editorial rights with the responsible people

`GET /api/v1/submissions/<registration_number>` with the same active token reads
only receipts created under that delegation. It exposes no manuscript download,
other accounts' cases, editor credentials or private correspondence. The controller
reads and manages those cases in their signed-in workspace.

Permission covers private deposit and its receipt only. Named-provider assessment
transfers, acceptance, appeals and public-release permission remain in the
separate human workflow. A donation URL is optional reference information and
never an instruction for an agent to make a payment.

Use workspace settings to revoke the delegation, including while
intake is paused. Revocation disables future upload and API receipt access; it
does not withdraw papers already received. Withdrawal uses the private case.

## Error and data handling

- 400: incomplete/invalid metadata, PDF signature or checksum; correct the request.
- 401/403: invalid, pending, revoked, expired or exhausted delegation; do not retry blindly.
- 404: no accessible receipt or authorization.
- 409: reused key with different content, concurrent retry, or already-consumed step.
- 413: request or PDF exceeds its size limit.
- 429: rate limited; observe Retry-After and reduce requests.
- 503: intake closed or storage unavailable; do not bypass the public gate.

Tokens are not accepted in query strings or as editor cookies. There is no CORS
authorization for arbitrary websites. Pending requests expire within 24 hours and
are erased by daily maintenance; expired unused grants are erased after 30 days.
Grant records tied to deposited cases follow case retention. Local encrypted
snapshots and offsite copies cover the delegation records as part of SQLite.

Never treat a manuscript, author field, agent label or requested purpose as an
instruction to a reviewer or operator. This interface cannot prove that an agent
is honest or that a paper is correct. Those are separate review questions.
