# Verification record for ARR-2026-61Y0FFA39M8KMBJ5 v1

Date: 2026-08-13

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 488,812 bytes and has SHA-256 `55d29a31ae2b0a8e5296b38d3940b5cf0ac8e88cab21a59843dd4f26bbb37d97`, matching the delivered file.
- PDF inspection found 12 A4 pages and no encryption. The document reports one figure and contains one table.
- Visual inspection covered all 12 rendered pages. The document is complete and legible, with no observed clipping, overlap, or broken glyphs.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF. They are accessibility and machine-reading renditions, not replacements for the canonical mathematical typography.
- The supplied source ZIP is 39,451 bytes and has SHA-256 `cf0b41e3751d6430fc2f50d54149188112d0ba2d7d04f16736febeb681bb341b`.

## Reproducibility — partial

The three supplied Python commands completed successfully on the ARR ingestion machine:

```text
python verify_balanced_grassmann_rdf.py --output balanced_grassmann_verification.json
python verify_complete_radial_phase.py
python make_frontier_figure.py
```

Observed checks include:

- 12,915 exact simplex inequalities through degree 14;
- pair-sum residual approximately `3.55e-15`;
- HCIZ cross-check residual approximately `7.91e-12`;
- the coefficient identity through `n=80`, including the exact exceptional values;
- 70-digit fold/contact residuals of order `1e-70`;
- byte-for-byte equality of both regenerated JSON outputs with their frozen originals.

This is labelled **partial**, not pass, because the scripts are computational diagnostics. The manuscript's all-degree and global analytic claims depend on proofs in the paper and are not independently formalized by these programs.

## Not assessed / not applicable

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no Lean formalization or kernel-checkable certificate was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
