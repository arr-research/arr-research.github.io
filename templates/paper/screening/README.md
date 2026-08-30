# Screening reports

When screening is performed, store one structured Markdown or JSON report for each declared evaluator. Reports must identify the public ID, version ID, paper hash, protocol version, date, exact model identifier, outcome, critical objections, and author response. If screening is not performed, keep `evaluators` empty and publish the explicit `not_assessed` status.

ARR does not require private chain-of-thought. It requires a concise, auditable decision report and the evidence needed to understand unresolved limitations.

New releases are fail-closed: `scripts/package_paper.py` refuses to create release assets until this exact version records a screening pass, three distinct evaluator reports and zero unresolved critical objections. Use `scripts/prepare_model_assessment.py ARR-ID --version vN` for the score-bearing public assessment prompt; preserve every valid response obtained, not only favourable ones.
