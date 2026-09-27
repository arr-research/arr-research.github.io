# Private intake retention and erasure schedule

Deletion runs daily and records an audit event. A file under a documented legal
hold is skipped and the hold is reviewed at least every 90 days.

| Data | Trigger | Erasure or review |
| --- | --- | --- |
| Optional public-site daily page totals | UTC collection date | erased by daily sweep after 400 days; encrypted snapshots may survive up to 7 additional days |
| Pseudonymized rate-limit events | collection | erased after 90 days |
| Authentication/security audit | event | reviewed and erased or aggregated after 12 months, unless an incident needs it |
| Infected uploaded bytes | scanner detection | immediately |
| Withdrawn private manuscript | withdrawal | 7 days |
| Declined private manuscript and detailed abstract | decision | 30 days, allowing the appeal window |
| Expired/incomplete private submission | 30 days without completion | 30 days after expiry notice |
| Superseded private revision | replacement received | 30 days |
| Accepted private working copy | verified immutable public release | 30 days |
| Private source disclosure and detailed originality/rights evidence | case-copy erasure deadline | erase narrative, match details and source disclosure; retain only minimal exact-hash outcome/date/policy/editor records |
| Independent-agent credential/provenance | token expiry or account inactivity | token valid 90 days unless rotated/revoked; erase private profile and revoke token at the existing 180-day inactive-account deadline when no active case |
| Minimal case/decision record | terminal decision | 3 years, then erase or irreversibly aggregate |
| Private workspace alias and credentials | no use for 180 days, no active private case, and no recent case activity | deactivate, erase alias/password/recovery hash, revoke agent grants and pseudonymize the legacy user row; minimal case records follow their separate schedule |
| Public accepted record | publication | preserved long-term under the deposit license; corrections/withdrawals use versioning/tombstones |

“Minimal case/decision record” means case identifier, work title, submitter identity
or a pseudonymous substitute where feasible, integrity hash, agreement versions,
dates, originality outcome/scan reference and editor, publication license, decision/reason code, conflict handling and erasure evidence. It excludes the
rejected manuscript bytes and detailed abstract after their deadline.

The commands `mark-published` and `retention-sweep` start and enforce private-copy,
rate-event and inactive contact/editor-account deadlines. Production scheduling and
annual retention review are mandatory operator controls in `INTAKE_OPERATIONS.md`.
