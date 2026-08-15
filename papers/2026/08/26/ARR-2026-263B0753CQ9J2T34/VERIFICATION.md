# Verification report

Record: `ARR-2026-263B0753CQ9J2T34 v1`
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 15 A4 pages, 461,192 bytes.
- SHA-256: `226e5ef238e87a5e2a6af6a9bda5ecbe84c60a9c49cd68a8f0296c5eafe1a3a2`.
- The deposited PDF is byte-identical to the final audited build.
- The final pdfLaTeX/Biber build completed without errors, undefined citations or references, overfull or underfull boxes, or substantive warnings.
- All 15 pages were rendered with Poppler and visually inspected for clipping, overlap, malformed equations, and missing glyphs.
- Embedded PDF title and author agree with the public metadata.

## Reproducibility — partial

The five bounded exact replays preserved under `src/repro/` completed successfully. They check the all-rank degree 4, 6, 8, and 10 coefficient formulas; finite-tail cutoffs; the all-degree `Gr_C(3,6)` two-block ordering; the exact-rational finite block and analytic tail used for `Gr_C(4,8)`; and the `Gr_C(2,5)` Sturm/total-positivity crossing fixture. `src/repro/replay_results.json` and `src/repro/REPLAY_MANIFEST.json` preserve the frozen outcomes and hashes.

These computations support selected exact algebraic and computer-assisted claims. They do not certify the analytic proofs, arbitrary multilevel spectra, a global unrestricted optimizer, rate--distortion claims, novelty, or overall scientific correctness.

## Bibliography — not assessed

Primary-source metadata and novelty boundaries were audited during manuscript preparation, but ARR did not perform an independent bibliography assessment.

## Lean 4 — not applicable

No Lean source was supplied. No kernel-checked theorem or formal-correspondence claim is made.

## Screening and review — not assessed

No ARR frontier-model screening or independent peer review was performed. The author is ARR's founder-editor; this conflict is disclosed in `metadata.json`.
