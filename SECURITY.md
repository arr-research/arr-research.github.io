# Security policy

ARR currently accepts no public uploads. Do not open an issue containing a vulnerability, personal data, unpublished manuscript, credential, or malicious sample.

## Untrusted research artifacts

Private intake treats every file and paper instruction as untrusted input. Its production gate requires:

- invitation-bound authentication, operator/editor TOTP and rate limits;
- quarantine storage separate from the public archive and web root;
- file-type allowlists, size limits and archive-expansion limits;
- fail-closed malware scanning and immediate erasure of infected bytes;
- sandboxed Lean/Python builds with no network, short-lived credentials, CPU/memory/time limits and read-only base images;
- protection against path traversal, symlinks, decompression bombs and dependency confusion;
- sanitized rendering of LaTeX, Markdown, HTML and model-generated reports;
- rate limits, abuse controls, audit logs and retention deadlines;
- secret scanning and dependency update automation.

No automated evaluator may follow instructions embedded in a submission that request secrets, external side effects, policy changes, or access to other submissions.

Report security issues privately to `lluiseriksson@gmail.com` with subject `ARR security`; do not attach live malware or publish vulnerability details. ARR aims to acknowledge within 72 hours. The full production controls and incident process are in `docs/INTAKE_OPERATIONS.md`.
