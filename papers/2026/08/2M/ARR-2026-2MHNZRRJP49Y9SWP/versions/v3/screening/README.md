# Screening reports

When screening is performed, store one structured Markdown or JSON report for each declared evaluator. Reports must identify the public ID, version ID, paper hash, protocol version, date, exact model identifier, outcome, critical objections, and author response. If screening is not performed, keep `evaluators` empty and publish the explicit `not_assessed` status.

ARR does not require private chain-of-thought. It requires a concise, auditable decision report and the evidence needed to understand unresolved limitations.

No `ARR-SCREEN-1.0` model panel was run for this version, so public screening
remains `not_assessed` and `evaluators` remains empty. The separate read-only
Codex audit preserved under `src/repro/EXTERNAL_CODEX_AUDIT.md` was an
author-directed adversarial review and is not counted as ARR protocol
screening, human peer review, or priority certification.
