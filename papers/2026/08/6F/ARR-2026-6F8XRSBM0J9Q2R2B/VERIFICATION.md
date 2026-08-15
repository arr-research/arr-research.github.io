# Verification report

Record: `ARR-2026-6F8XRSBM0J9Q2R2B v1`  
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 11 A4 pages, 414,801 bytes.
- SHA-256: `4d14c983c342a64c56f4f6620edbe4c2d84b1f9ef0d9bc0bf53c631fa7a27853`.
- The deposited PDF is byte-identical to the final audited build.
- A complete pdfLaTeX/Biber build completed without undefined citations or references, overfull boxes, or substantive warnings.
- All 11 pages were rendered after the final criticality repairs and visually inspected for clipping, overlap, and missing glyphs.
- Embedded PDF title and author agree with the public metadata.

## Reproducibility — partial

`src/python/verify_orbital_metastability.py` completed successfully in a bounded local run. It checks exact moment and Taylor algebra, the weak-field threshold identities, a finite tail closure, the explicit torus-orbit derivative counterexample, and bounded Bessel positivity diagnostics. The frozen output is `src/python/orbital_metastability_verification.json`.

These computations support selected algebraic and diagnostic claims. They do not certify the harmonic-analysis proof, the Morse--Bott argument, the Jacobi generator derivation, or global scientific correctness.

## Bibliography — not assessed

Primary-source metadata and novelty boundaries were audited during manuscript preparation and the audit files are preserved under `src/audits/`. ARR did not perform an independent bibliography assessment.

## Lean 4 — not applicable

No Lean source was supplied. No kernel-checked theorem or formal correspondence claim is made.

## Screening and review — not assessed

No ARR frontier-model screening or independent peer review was performed. The author is ARR's founder-editor; this conflict is disclosed in `metadata.json`.
