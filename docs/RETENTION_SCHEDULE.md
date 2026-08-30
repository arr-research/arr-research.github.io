# Private intake retention and erasure schedule

Deletion runs daily and records an audit event. A file under a documented legal
hold is skipped and the hold is reviewed at least every 90 days.

| Data | Trigger | Erasure or review |
| --- | --- | --- |
| Pseudonymized rate-limit events | collection | erased after 90 days |
| Authentication/security audit | event | reviewed and erased or aggregated after 12 months, unless an incident needs it |
| Infected uploaded bytes | scanner detection | immediately |
| Withdrawn private manuscript | withdrawal | 7 days |
| Declined private manuscript and detailed abstract | decision | 30 days, allowing the appeal window |
| Expired/incomplete private submission | 30 days without completion | 30 days after expiry notice |
| Superseded private revision | replacement received | 30 days |
| Accepted private working copy | verified immutable public release | 30 days |
| Minimal case/decision record | terminal decision | 3 years, then erase or irreversibly aggregate |
| Depositor contact row | last case closed and no active submission | review after 180 days; erase or pseudonymize unless still required for the case |
| Public accepted record | publication | preserved long-term under the deposit license; corrections/withdrawals use versioning/tombstones |

“Minimal case/decision record” means case identifier, work title, submitter identity
or a pseudonymous substitute where feasible, integrity hash, agreement versions,
dates, decision/reason code, conflict handling and erasure evidence. It excludes the
rejected manuscript bytes and detailed abstract after their deadline.

The commands `mark-published` and `retention-sweep` start and enforce private-copy,
rate-event and inactive contact/editor-account deadlines. Production scheduling and
annual retention review are mandatory operator controls in `INTAKE_OPERATIONS.md`.
