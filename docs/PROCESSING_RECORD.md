# GDPR Article 30 processing record — operator copy

Controller: Lluis Eriksson, Stockholm, Sweden — lluiseriksson@gmail.com. This record
must be updated with every production processor, hosting location, subprocessor and
transfer safeguard before live data reaches that provider.

| Activity | People/data | Purpose/basis | Recipients | Erasure | Security summary |
| --- | --- | --- | --- | --- | --- |
| Direct-deposit contact | adult depositors; name, email, submission/notice dates | administer agreement; Art. 6(1)(b) | operator; intake host; notification-email provider | case retention schedule | no author account; TLS; CSRF; IP/email rate limits |
| Private intake | depositor/authors; metadata, PDF, attestations | assess requested deposit; Art. 6(1)(b) | operator; unconflicted editor; host/scanner | 7/30 days after withdrawal/decline | separate quarantine, random names, access control, malware scan |
| Security/audit | users; pseudonymous rate key, events, case decisions | security/accountability; Art. 6(1)(f) | operator; security provider if appointed | rate 90 days; auth 12 months; decision 3 years | HMAC pseudonymization, least privilege, append-oriented log |
| Required pre-publication frontier-model screening | depositor/authors; exact manuscript, case hash, prompt/result and provider/model provenance | administer disclosed deposit/acceptance protocol; Art. 6(1)(b) | operator-selected frontier-model providers under reviewed service controls | private report follows case retention; published structured assessment is preserved with the accepted record | recorded transfer authorization; exact hash; provider/model log; no-training or enterprise-confidentiality control where available; human-only final decision |
| Voluntary support | donor; PayPal transaction identity, contact, amount, currency and identifier | payment/refund administration, fraud handling, accounting and legal obligations; Arts. 6(1)(b), 6(1)(c) and 6(1)(f) as applicable | PayPal and legally required recipients | applicable accounting/payment limitation period; no mailing list or public donor ranking | PayPal loads only on the support page; no editorial linkage or influence |
| Public archive | authors/readers; accepted research, metadata, license, provenance | publish agreement; Art. 6(1)(b) | public worldwide; GitHub/mirrors | long-term scholarly preservation | immutable versions, hashes, takedown/correction process |
| Legal/rights cases | requesters/affected people; notice, evidence, correspondence | legal duty or legitimate claims; Art. 6(1)(c)/(f) as applicable | operator, counsel, authority | case-specific review; legal hold | restricted case access, minimization, logged actions |

Current risk determination: a small direct-submission pilot that prohibits sensitive
data is not intended for high-risk processing. The operator must repeat the risk
assessment and determine whether a DPIA is required before systematic AI analysis,
sensitive-data research, large-scale processing or new
tracking/identity technologies.
