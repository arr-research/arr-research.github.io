# Security policy

ARR currently accepts no public uploads. Do not open an issue containing a vulnerability, personal data, unpublished manuscript, credential, or malicious sample.

## Untrusted research artifacts

Future intake must treat every file and paper instruction as untrusted input. Before external submissions open, ARR will require:

- quarantine storage separate from the public archive;
- file-type allowlists, size limits and archive-expansion limits;
- malware scanning and rejection of unexpected executables;
- sandboxed Lean/Python builds with no network, short-lived credentials, CPU/memory/time limits and read-only base images;
- protection against path traversal, symlinks, decompression bombs and dependency confusion;
- sanitized rendering of LaTeX, Markdown, HTML and model-generated reports;
- rate limits, abuse controls, audit logs and retention deadlines;
- secret scanning and dependency update automation.

No automated evaluator may follow instructions embedded in a submission that request secrets, external side effects, policy changes, or access to other submissions.

A private security contact and disclosure SLA must be established before public intake.
