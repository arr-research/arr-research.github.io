# GDPR Article 30 processing record — operator copy

Controller: Lluis Eriksson, Stockholm, Sweden — lluiseriksson@gmail.com. This record
must be updated with every production processor, hosting location, subprocessor and
transfer safeguard before live data reaches that provider.

| Activity | People/data | Purpose/basis | Recipients | Erasure | Security summary |
| --- | --- | --- | --- | --- | --- |
| Invitations/accounts | adult applicants; name, email, password hash, role, dates | administer agreement; Art. 6(1)(b) | operator; intake host | inactive account review at 180 days | one-use token, hashed password, TLS, editor TOTP |
| Private intake | depositor/authors; metadata, PDF, attestations | assess requested deposit; Art. 6(1)(b) | operator; unconflicted editor; host/scanner | 7/30 days after withdrawal/decline | separate quarantine, random names, access control, malware scan |
| Security/audit | users; pseudonymous rate key, events, case decisions | security/accountability; Art. 6(1)(f) | operator; security provider if appointed | rate 90 days; auth 12 months; decision 3 years | HMAC pseudonymization, least privilege, append-oriented log |
| Optional AI assessment | depositor/authors; manuscript and prompt/result | optional assessment; Art. 6(1)(a) | specifically named provider | provider-specific notice before transfer | off by default; reconfirm; no unrelated model training by ARR instruction |
| Public archive | authors/readers; accepted research, metadata, license, provenance | publish agreement; Art. 6(1)(b) | public worldwide; GitHub/mirrors | long-term scholarly preservation | immutable versions, hashes, takedown/correction process |
| Legal/rights cases | requesters/affected people; notice, evidence, correspondence | legal duty or legitimate claims; Art. 6(1)(c)/(f) as applicable | operator, counsel, authority | case-specific review; legal hold | restricted case access, minimization, logged actions |

Current risk determination: a small invitation-only pilot that prohibits sensitive
data is not intended for high-risk processing. The operator must repeat the risk
assessment and determine whether a DPIA is required before adding public signup,
systematic AI analysis, sensitive-data research, large-scale processing or new
tracking/identity technologies.
