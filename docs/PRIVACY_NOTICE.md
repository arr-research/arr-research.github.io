# AIRR privacy notice — ARR-PRIVACY-1.4

**Effective:** 2026-09-07
**Brand wording updated:** 2026-09-06; see [identity and continuity](BRAND_IDENTITY.md).

**Service state:** currently fee-free direct private-submission pilot; the receiver
opens only after the operator authorizes the documented reception-readiness record.

## Controller and contact

The data controller is **Lluis Eriksson**, a natural person in Sweden,
acting as founder, registry operator and responsible editor of the Archive for Independent & Rigorous Research (AIRR). Contact: **lluiseriksson@gmail.com** with the subject
`AIRR privacy`. No data protection officer has been designated.

AIRR is not represented as a Swedish limited company and “VD/CEO” is therefore
not used as a legal title. A service postal address and any later legal-entity
details must be added before general public intake opens.

## What AIRR collects

- direct-deposit contact data: adult depositor's name and email address, submission
  and notification timestamps;
- agent delegation data: declared agent name/version and purpose, responsible
  adult's name/email, confirmation and revocation times, scope, expiry, token
  hashes, usage count and retry identifiers. Secret confirmation links go only
  to the supplied email; agent tokens do not provide editorial access;
- submission data: title, author list, abstract, manuscript PDF, filename, size,
  cryptographic hash, rights/disclosure attestations, frontier-model review authorization,
  conflict declaration and correspondence;
- editorial data: case identifier, checks, editor identity, decision, reasons,
  appeal and legal-hold information;
- security data: pseudonymized IP-rate key, authentication and access events,
  malware result, timestamps and technical error information; and
- after acceptance, public scholarly metadata and the licensed research object.

Do not submit special-category personal data, government identifiers, financial
credentials, medical records, confidential peer-review material, export-controlled
material or third-party personal data that is not necessary and lawful to publish.
AIRR accepts deposits only from people aged 18 or older during the pilot. Authors receive single-use private case links by email; these expire after seven days and open an eight-hour browser session. They do
not create an intake account; operator and independent-editor accounts remain
protected by passwords and TOTP.

An agent can request a delegation without sending a PDF or an email. Its
responsible person supplies the contact details and confirms through email before
the delegation may upload. Pending requests expire within 24 hours and daily
maintenance removes them and their confirmation messages. Expired unused grants
are removed after 30 days; grant records tied to deposits follow case retention.
Email confirmation establishes access to the email channel, not verified legal
identity or copyright. Declared agent provenance can accompany a paper only under
the separate public-release permission.

## Purposes and lawful bases

| Purpose | GDPR basis |
| --- | --- |
| Receive a direct private deposit, communicate, assess it and administer withdrawal | steps requested before and performance of the deposit agreement (Article 6(1)(b)) |
| Protect the form and editor accounts, quarantine files, prevent abuse, investigate integrity issues and keep a proportionate audit trail | AIRR's and users' legitimate interests in a secure, accountable scholarly service (Article 6(1)(f)) |
| Respond to binding authority requests and applicable record obligations | legal obligation where one applies (Article 6(1)(c)) |
| Publish an accepted manuscript, its authorship, provenance and licenses worldwide | performance of the deposit agreement (Article 6(1)(b)); public distribution also follows the depositor's chosen license |
| Send a private manuscript to operator-selected external frontier-model evaluators solely for the disclosed pre-publication screening | steps requested before and performance of the deposit agreement (Article 6(1)(b)); the upload form acknowledges the screening requirement; a separate recorded confirmation of the named-provider notice authorizes the exact transfer |

AIRR makes no solely automated acceptance or rejection decision and does not
profile authors. Malware and format checks can block access to a file, but a human
handles the editorial outcome and any challenge to an automated security result.

## Recipients and transfers

Private intake data is available only to the operator and a specifically appointed
independent editor where a conflict requires one. Infrastructure, encrypted backup,
operator-notification email and security providers may process the minimum data needed under written
instructions and appropriate contractual safeguards. The production processor
register must identify them before direct submission is activated.

The configured private receiver uses Netcup (VPS in Vienna, Austria), Brevo for
transactional email, and Backblaze B2 EU Central (Amsterdam) for client-encrypted
offsite copies. ClamAV runs locally and does not receive manuscripts as an
external service. GitHub Pages hosts the public archive, not private submissions.
Email is routed to the responsible person's chosen provider and the operator's
inbox; this may involve international delivery. Provider group locations and
subprocessors are distinct from the selected storage region. The operator's
[processing record](PROCESSING_RECORD.md) identifies contractual references and
limits of the current verification.

Private manuscripts are not stored in the public GitHub repository. If accepted,
the disclosed author information, scholarly metadata and licensed research object
are intentionally published worldwide through AIRR, GitHub and mirrors. The public
nature and practical irreversibility of third-party copies will be shown again
before final publication. Frontier-model providers receive the exact manuscript and
case hash only for the disclosed assessment purpose. Before transfer, the depositor separately confirms a notice identifying the providers/models, confidentiality controls, retention and transfer safeguards. The operator records that confirmation, provider,
model identifier, time and response hash. Provider terms, confidentiality controls
and international-transfer safeguards must be reviewed before use; AIRR selects a
no-training or enterprise-confidentiality control where the service offers one.
Rejected-case reports remain private and follow the case retention schedule.

## Public-site activity measurement

AIRR currently sets no analytics cookies and runs no per-page visitor analytics.
The public site displays cumulative download counters reported by GitHub for each
canonical PDF release asset. AIRR receives an aggregate integer through GitHub's
public release API, not a reader identity or per-reader download history.

Page views and unique visitors are shown as **not measured**. AIRR will not enable
or publish page-view analytics until the provider, purpose, data fields, retention,
lawful basis, processor terms and any transfer safeguards have been reviewed and
this notice has been updated before collection begins.

## Retention

The binding schedule is in [`RETENTION_SCHEDULE.md`](RETENTION_SCHEDULE.md).
Rejected manuscript bytes are erased automatically 30 days after the decision;
withdrawn bytes after 7 days; malware is erased immediately after detection.
Accepted private working copies are erased 30 days after verified public release.
A minimal decision/audit record is retained for three years. A documented legal
hold pauses deletion only for the material and time necessary and is reviewed at
least every 90 days.

Encrypted disaster-recovery snapshots expire within seven days. Deleted working
data may therefore remain in an inaccessible encrypted snapshot for up to seven
additional days. Snapshots are not used for ordinary editorial access; after a
restore, erasure schedules and recorded withdrawal/erasure requests must be
reapplied before the service reopens.

## Your rights

Subject to the GDPR and applicable exceptions, you may request access,
rectification, erasure, restriction, portability, or object to legitimate-interest
processing. You may withdraw the submission and prevent a model transfer not yet
made; because frontier-model screening is an acceptance condition, AIRR cannot
complete acceptance after that withdrawal. Earlier lawful processing is unaffected.
Email the controller; identity may be verified
proportionately. AIRR aims to acknowledge requests within 7 days and responds
within the statutory period.

You may complain to the Swedish Authority for Privacy Protection (IMY) or another
competent EEA supervisory authority. IMY's complaint service is at
<https://www.imy.se/en/individuals/forms-and-e-services/file-a-gdpr-complaint/>.

## Security and incidents

AIRR uses a direct CSRF-protected form, editor password/TOTP, secure cookies,
IP/email rate limits, a bot trap, non-public random filenames, strict PDF limits,
malware quarantine, fail-closed scanning, role separation, an audit log and timed
erasure. Email must not contain manuscript attachments or sensitive material.

Suspected personal-data incidents are documented and assessed. Where required,
AIRR notifies IMY within 72 hours of awareness and informs affected people when the
GDPR requires it. Security reports use the private instructions in `SECURITY.md`.

## Changes

The accepted privacy version is recorded with every submission. Material changes
do not apply retroactively without notice and, where necessary, renewed agreement.
Earlier versions remain in repository history.

## Voluntary support — notice updated 2026-09-06

The support page links to PayPal when donations are available. AIRR loads no
PayPal widget or tracking script. When a visitor chooses to donate on PayPal,
PayPal acts under its own terms and privacy notice and provides
the operator with transaction data such as donor name, email, amount, currency and
transaction identifier and any note. The recipient remains Lluis Eriksson, acting
as AIRR's individual operator in Sweden. AIRR uses those data only for payment
administration, fraud/refund handling, accounting and legal obligations. The donor
may optionally identify a published paper or use the registration reference shown
on their submission receipt to explain which paper their support relates to.
The reference gives no access to private data and is used only for support/payment
administration. AIRR does not transmit it to PayPal automatically; the donor chooses
whether to include it in a payment note. Manuscripts, access links and sensitive
information must not be included. Donor information is
not published or added to a mailing list or public ranking, and donations cannot
influence editorial decisions. The contribution is separate from any deposit and
does not alter an existing submission agreement.
