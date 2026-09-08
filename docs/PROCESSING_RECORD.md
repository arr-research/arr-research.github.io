# GDPR Article 30 processing record — operator copy

Controller: Lluis Eriksson, Sweden — lluiseriksson@gmail.com. This record
must be updated with every production processor, hosting location, subprocessor and
transfer safeguard before live data reaches that provider.

| Activity | People/data | Purpose/basis | Recipients | Erasure | Security summary |
| --- | --- | --- | --- | --- | --- |
| Direct-deposit contact | adult depositors; name, email, submission/notice dates | administer agreement; Art. 6(1)(b) | operator; intake host; notification-email provider | case retention schedule | no author account; TLS; CSRF; IP/email rate limits |
| Agent delegation | responsible adult and declared software identity; name/email, scope, token hashes, confirmation/revocation, expiry, usage and retry keys | administer requested delegation; Art. 6(1)(b); pre-confirmation abuse prevention Art. 6(1)(f) | operator, intake host, email provider and encrypted backup host | pending expiry within 24h plus daily sweep; expired unused grants 30 days; used grants follow case retention | email-confirmed scope, revocable seven-day token, five-upload cap, idempotency, no editorial or publication access |
| Private intake | depositor/authors; metadata, PDF, attestations | assess requested deposit; Art. 6(1)(b) | operator; unconflicted editor; host/scanner | 7/30 days after withdrawal/decline | separate quarantine, random names, access control, malware scan |
| Security/audit | users; pseudonymous rate key, events, case decisions | security/accountability; Art. 6(1)(f) | operator; security provider if appointed | rate 90 days; auth 12 months; decision 3 years | HMAC pseudonymization, least privilege, append-oriented log |
| Required pre-publication frontier-model screening | depositor/authors; exact manuscript, case hash, prompt/result and provider/model provenance | administer disclosed deposit/acceptance protocol; Art. 6(1)(b) | operator-selected frontier-model providers under reviewed service controls | private report follows case retention; published structured assessment is preserved with the accepted record | recorded transfer authorization; exact hash; provider/model log; no-training or enterprise-confidentiality control where available; human-only final decision |
| Voluntary support | donor; PayPal transaction identity, contact, amount, currency, identifier and optional note/published-paper or submission-registration reference | support/payment/refund administration, fraud handling, accounting and legal obligations; Arts. 6(1)(b), 6(1)(c) and 6(1)(f) as applicable | PayPal and legally required recipients | applicable accounting/payment limitation period; no mailing list or public donor ranking | external PayPal link only; no PayPal widget or script on AIRR; submission references are not access credentials and are shared only at the donor's choice, no editorial influence or linkage to assessment/ranking records |
| Public archive | authors/readers; accepted research, metadata, license, provenance | publish agreement; Art. 6(1)(b) | public worldwide; GitHub/mirrors | long-term scholarly preservation | immutable versions, hashes, takedown/correction process |
| Legal/rights cases | requesters/affected people; notice, evidence, correspondence | legal duty or legitimate claims; Art. 6(1)(c)/(f) as applicable | operator, counsel, authority | case-specific review; legal hold | restricted case access, minimization, logged actions |

Current risk determination: a small direct-submission pilot that prohibits sensitive
data is not intended for high-risk processing. The operator must repeat the risk
assessment and determine whether a DPIA is required before systematic AI analysis,
sensitive-data research, large-scale processing or new
tracking/identity technologies.

## Configured services and contract evidence, 2026-09-08

This register distinguishes configured controls and available contract evidence
from an independent legal review. Account identifiers, executed customer contracts
and recovery secrets belong in the private operational record, not in this file.

| Service | Actual use/location | Contract and verification basis | Remaining review |
| --- | --- | --- | --- |
| netcup GmbH | Private VPS in Vienna, Austria: contact data, SQLite, quarantine and local scanning; encrypted volume | The operator completed the CCP DPA on 2026-09-06; the prior installation record recorded the generated contract. [DPA documentation](https://helpcenter.netcup.com/en/wiki/general/dpa/) | Retain/review the executed PDF and its current subprocessors; current session expiry prevented a fresh download, not evidence that the existing agreement vanished |
| Brevo | Transactional confirmation/case notices and protected links; no PDF or abstract. Minimum case metadata in operator notices | [Terms dated 2025-10-01](https://www.brevo.com/legal/termsofuse/), Appendix 3: customer controller/Brevo processor for service data; account administration is separate. Annex 2 lists OVH France, GCP Belgium, Cloudflare EU/US and international support; transfer provisions include SCCs and supplementary measures | Review changes to terms, log retention and optional features; recipient inboxes have their own providers. No marketing, SMS or optional AI service is enabled by this record |
| Backblaze, Inc. | Client-encrypted age snapshots in EU Central, Amsterdam; decryption identity is not provided to B2 | [EEA DPA dated 2022-09-20](https://www.backblaze.com/company/policy/dpa-for-eea-eu-residents) is integrated into the service terms and includes SCCs. It describes individual customers, including the current account type, as joint controllers; organization accounts are described differently. [Provider list dated 2025-12-03](https://www.backblaze.com/company/policy/subprocessors) identifies Interxion Netherlands for EU Central and US account/support services | Do not describe the individual account as an independently verified standard Article 28 processor arrangement. Region and client encryption do not establish a blanket legal certification. Reassess contractual roles when changing account type or scope |
| ClamAV | Local software on Netcup; signatures are updated over the network, manuscript bytes are scanned locally | No separate remote manuscript-processing service is used | Preserve configuration and signature-update evidence |
| GitHub Pages/Actions | Public records, static site and external availability checks; private PDFs and intake secrets excluded from Git | Existing repository/public hosting arrangement | Review public-host/visitor-data terms separately from the private-intake providers |
| Operator and recipient email providers | Operator currently uses Gmail; authors choose their own inbox provider | Inbox delivery is separate from Brevo SMTP | Do not represent a personal Gmail account as Google Workspace with an executed enterprise DPA; minimize notice content and review inbox handling |

No external model assessment provider is approved generically by this table.
Each assessment plan needs its specific confidentiality, retention and transfer
notice and the responsible depositor's recorded confirmation before transfer.
