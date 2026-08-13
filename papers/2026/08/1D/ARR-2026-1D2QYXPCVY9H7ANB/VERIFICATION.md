# Verification record for ARR-2026-1D2QYXPCVY9H7ANB v1

Date: 2026-08-13
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 499,166 bytes and has SHA-256 `48bd09c67edf1d1754941d3df211952449cf3f91534637a2ac2eb3f598a0ba15`, matching the depositor-supplied values.
- PDF inspection found 19 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 19 rendered pages. The document is complete and legible, with two figures and no tables.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF.
- The supplied replay ZIP is 310,509 bytes and has SHA-256 `54a0fd17a2b68bdfc62a188043be104ef533b1b20581789a9992ba912902821e`.

## Reproducibility — partial

Both supplied commands completed successfully on Python 3.12.6:

```text
python verify_frontier.py
python verify_thermodynamic_limit.py --max-d 100 --output-dir .
```

The first replay checked dimensions 2–5 and reported zero monotonicity violations, scalar self-consistency residuals below `2.59e-14`, and Gibbs dual residuals below `1.78e-12`. The second reproduced the coexistence constants and finite-dimensional first-contact diagnostics through dimension 100.
This remains **partial** because the scripts call themselves deterministic diagnostics and do not prove the all-degree spectral extremum, converse/achievability, thermodynamic Laplace principle, or source-universal capacity theorem.

## Not assessed / not applicable

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no formalization was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
