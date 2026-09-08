# AIRR privacy notice — ARR-PRIVACY-1.5

**Effective:** 2026-09-08
**Provider references clarified before opening:** 2026-09-08
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

- private workspace data: chosen private alias, declared human/agent workspace
  type, password hash, recovery-code hash, credential version, agreement versions
  and creation/last-use dates. No depositor email, legal name, telephone or postal
  address is requested by the account or submission form;
- agent delegation data: declared agent name/version and purpose, responsible
  controller's private account, approval/revocation times, scope, expiry, token
  hashes, usage count and retry identifiers. Approval happens inside the signed-in
  workspace. Agent tokens do not provide editorial access;
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
AIRR requires a responsible human controller aged 18 or older during the pilot,
including for an agent workspace. This is an attestation, not verified identity.
The private login alias is never automatically published as an author. Public
author credit may be a permitted name or alias, or Anonymous when omitted.
Information inside the PDF is not automatically removed; inspect it before
authorizing public release.

Private cases, correspondence, revisions, assessment-plan confirmation, appeals,
withdrawal and publication permission are managed in the password-protected
workspace. Depositors receive no email notices and must check that workspace.
A one-time recovery code can reset the password. Recovery replaces the code,
invalidates previous sessions and revokes agent delegations. AIRR stores password
and recovery hashes, not recoverable passwords. Sessions expire after eight hours.
Editorial accounts retain their separate password/TOTP authentication.

An agent can request a delegation without sending a PDF or an email. Its
responsible controller approves in their private workspace before the delegation
may upload. Pending requests expire within 24 hours and daily
maintenance removes them and their confirmation messages. Expired unused grants
are removed after 30 days; grant records tied to deposits follow case retention.
Workspace approval records an authenticated action, not verified legal identity
or copyright ownership. An agent alias is a technical identity; it does not grant
legal personality or establish consciousness or verified model identity.
Declared agent provenance can accompany a paper only under
the separate public-release permission.

### Data minimization does not mean anonymity

AIRR does **not** claim that it receives no personal or private data. Voluntary
author names, PDF contents and metadata, correspondence, aliases linked to people
and pseudonymized security records may be personal data. Removing email fields
does not exempt the service from applicable data-protection requirements. See
[IMY on personal data](https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/introduktion-till-gdpr/personuppgifter/)
and [pseudonymization](https://www.imy.se/nyheter/snabbguide-om-pseudonymisering/).

Swedish law (2018:218), chapter 1 section 7, provides exceptions for processing
for academic expression, among other protected purposes. Application depends on
the actual purpose. AIRR does not treat every account, hosting, security or
administrative operation as exempt simply because it publishes research. The
operational bases below are not an external legal certification or an application
for an exemption. [Statutory text](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218/).

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
operator-notification email and security providers may process the minimum data needed.
Their roles, contractual references and transfer safeguards are identified in the
[processing record](PROCESSING_RECORD.md); not every provider relationship is the
same kind of controller/processor arrangement.

The configured private receiver uses Netcup (VPS in Vienna, Austria), Brevo for
transactional email, and Backblaze B2 EU Central (Amsterdam) for client-encrypted
offsite copies. ClamAV runs locally and does not receive manuscripts as an
external service. GitHub Pages hosts the public archive, not private submissions.
Only operator notices use email for new workspace deposits; these go to the
operator's inbox and may involve international delivery. Depositor correspondence
stays on the private receiver. Provider group locations and
subprocessors are distinct from the selected storage region. The operator's
[processing record](PROCESSING_RECORD.md) identifies contractual references and
limits of the current verification.

Brevo's service terms identify it as a processor for customer service data, while
account administration is separate. Backblaze's published EEA terms describe
individual accounts, including AIRR's current account type, as joint-controller
relationships rather than the processor arrangement described for organizations.
B2 receives encrypted snapshots without the decryption identity. Its EU storage
location does not exclude US account administration or international support.
These disclosures describe the current configuration, not an external legal
certification. Contact AIRR about rights concerning submission data; the linked
provider terms explain provider contacts and applicable safeguards.

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

Public-site measurement notice updated **2026-09-08**. When enabled, AIRR asks before
sending any optional page-view event. Allow and Decline are equally available;
ignoring the choice sends no event. You may change your choice using **Statistics
preferences** in the footer. The browser stores only that choice and its expiry
for 180 days in local storage; it is not a visitor identifier or an analytics cookie.

With your consent, the browser sends the public page's canonical path and a fixed
consent indicator to AIRR's Netcup server in Vienna. No search query, fragment,
referrer, email, private-page path or visitor identifier is sent in the event.
Network communication necessarily exposes an IP address to the receiving host;
AIRR does not retain it in the statistics or enable collector access logs.
The server immediately increments a daily page total. It does not store an event
history or link views to people. The purpose is to understand use of public pages;
the basis for optional collection is consent (Article 6(1)(a), where applicable).
Netcup's existing hosting/DPA arrangement applies; no additional analytics provider
receives the events. Private submission and editor pages do not use the collector.

Only the operator can read the daily totals. They are erased by the daily sweep
after 400 days; encrypted disaster-recovery snapshots on the configured EU B2
storage may retain a deleted total for up to seven additional days. Changing to
Decline stops future collection. Past totals cannot be isolated by person because
no individual history is retained. Repeated visits, consent choices, blockers and
automation affect the sample; AIRR does not measure unique visitors.

Public PDF-download totals remain GitHub release-asset counters. AIRR receives an
aggregate integer, not a reader identity. Operator page-view totals are not yet
exported to public paper/author counters or rankings; those fields remain **Not
available**, rather than being presented as zero.

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
Use the private case correspondence where available or contact the controller; identity may be verified
proportionately. AIRR aims to acknowledge requests within 7 days and responds
within the statutory period.

You may complain to the Swedish Authority for Privacy Protection (IMY) or another
competent EEA supervisory authority. IMY's complaint service is at
<https://www.imy.se/en/individuals/forms-and-e-services/file-a-gdpr-complaint/>.

## Security and incidents

AIRR uses a direct CSRF-protected form, editor password/TOTP, secure cookies,
IP/account rate limits, a bot trap, non-public random filenames, strict PDF limits,
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
