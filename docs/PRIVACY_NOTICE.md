# ARR privacy notice — ARR-PRIVACY-1.0

**Effective:** 2026-08-30  
**Service state:** currently fee-free, invitation-only pilot; general public intake is not open.

## Controller and contact

The data controller is **Lluis Eriksson**, a natural person in Stockholm, Sweden,
acting as founder, registry operator and responsible editor of the Archive for
Rigorous Research (ARR). Contact: **lluiseriksson@gmail.com** with the subject
`ARR privacy`. No data protection officer has been designated.

ARR is not represented as a Swedish limited company and “VD/CEO” is therefore
not used as a legal title. A service postal address and any later legal-entity
details must be added before general public intake opens.

## What ARR collects

- invitation and account data: name, email address, password hash, account role,
  account timestamps and invitation state;
- submission data: title, author list, abstract, manuscript PDF, filename, size,
  cryptographic hash, rights/disclosure attestations, optional AI-review choice,
  conflict declaration and correspondence;
- editorial data: case identifier, checks, editor identity, decision, reasons,
  appeal and legal-hold information;
- security data: pseudonymized IP-rate key, authentication and access events,
  malware result, timestamps and technical error information; and
- after acceptance, public scholarly metadata and the licensed research object.

Do not submit special-category personal data, government identifiers, financial
credentials, medical records, confidential peer-review material, export-controlled
material or third-party personal data that is not necessary and lawful to publish.
ARR accepts accounts only from people aged 18 or older during the pilot.

## Purposes and lawful bases

| Purpose | GDPR basis |
| --- | --- |
| Create an invited account, receive a deposit, communicate, assess it and administer withdrawal | steps requested before and performance of the deposit agreement (Article 6(1)(b)) |
| Protect accounts, quarantine files, prevent abuse, investigate integrity issues and keep a proportionate audit trail | ARR's and users' legitimate interests in a secure, accountable scholarly service (Article 6(1)(f)) |
| Respond to binding authority requests and applicable record obligations | legal obligation where one applies (Article 6(1)(c)) |
| Publish an accepted manuscript, its authorship, provenance and licenses worldwide | performance of the deposit agreement (Article 6(1)(b)); public distribution also follows the depositor's chosen license |
| Send a private manuscript to a named external AI evaluator | separate, optional and withdrawable consent (Article 6(1)(a)); no transfer occurs until ARR identifies the provider and reconfirms the choice |

ARR makes no solely automated acceptance or rejection decision and does not
profile authors. Malware and format checks can block access to a file, but a human
handles the editorial outcome and any challenge to an automated security result.

## Recipients and transfers

Private intake data is available only to the operator and a specifically appointed
independent editor where a conflict requires one. Infrastructure, encrypted backup,
email and security providers may process the minimum data needed under written
instructions and appropriate contractual safeguards. The production processor
register must identify them before live invitations are issued.

Private manuscripts are not stored in the public GitHub repository. If accepted,
the disclosed author information, scholarly metadata and licensed research object
are intentionally published worldwide through ARR, GitHub and mirrors. The public
nature and practical irreversibility of third-party copies will be shown again
before final publication. Optional AI transfer is off by default.

## Public-site activity measurement

ARR currently sets no analytics cookies and runs no per-page visitor analytics.
The public site displays cumulative download counters reported by GitHub for each
canonical PDF release asset. ARR receives an aggregate integer through GitHub's
public release API, not a reader identity or per-reader download history.

Page views and unique visitors are shown as **not measured**. ARR will not enable
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

## Your rights

Subject to the GDPR and applicable exceptions, you may request access,
rectification, erasure, restriction, portability, or object to legitimate-interest
processing. You may withdraw optional AI consent before transfer without affecting
earlier lawful processing. Email the controller; identity may be verified
proportionately. ARR aims to acknowledge requests within 7 days and responds
within the statutory period.

You may complain to the Swedish Authority for Privacy Protection (IMY) or another
competent EEA supervisory authority. IMY's complaint service is at
<https://www.imy.se/en/individuals/forms-and-e-services/file-a-gdpr-complaint/>.

## Security and incidents

ARR uses invitation-bound accounts, password hashing, editor TOTP, secure cookies,
CSRF protection, rate limits, non-public random filenames, strict PDF limits,
malware quarantine, fail-closed scanning, role separation, an audit log and timed
erasure. Email must not contain manuscript attachments or sensitive material.

Suspected personal-data incidents are documented and assessed. Where required,
ARR notifies IMY within 72 hours of awareness and informs affected people when the
GDPR requires it. Security reports use the private instructions in `SECURITY.md`.

## Changes

The accepted privacy version is recorded with every submission. Material changes
do not apply retroactively without notice and, where necessary, renewed agreement.
Earlier versions remain in repository history.
