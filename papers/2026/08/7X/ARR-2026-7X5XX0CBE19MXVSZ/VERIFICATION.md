# Verification record for ARR-2026-7X5XX0CBE19MXVSZ v1

Date: 2026-08-14

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The canonical PDF is 461,948 bytes with SHA-256
  `9db79aa3bbd6471e5eeb8e5d2b7387a013dbab9f5e5da65aa373a8599f51b42e`.
- PDF inspection found 12 A4 pages, no encryption, no forms, and no JavaScript.
- All 12 pages were rendered and visually inspected; no clipping, overlap,
  missing glyphs, blank pages, or malformed equations were found.
- The final pdfLaTeX/Biber build completed with no undefined references or
  citations, package warnings, or overfull/underfull boxes.
- `paper.md` and `paper.txt` are machine-readable renditions of the exact PDF,
  not replacements for the canonical typography.
- LaTeX, bibliography, and replay source were copied from the frozen author
  release and rehashed during ingestion.

## Reproducibility — partial

The bounded replay completed successfully:

```text
python src/python/verify_matricial_hausdorff.py
```

It verifies the parity-correct even/odd block identities, noncommuting atomic
weights, Loewner inversion, strict two-atom rational fixture, trace-norm power
scale, exact ordinary-dual certificate, a regular smooth-face tangent fixture,
and a scoped Gaussian local-power illustration.

This is labelled **partial**, not pass, because Gaussian coverage, the global
consistency theorem, LAN/cone-projection limit, and root-n separation result
are analytic arguments rather than formally certified computations.

## Scope

The support hypothesis concerns compatibility of the exposed finite
matrix-moment truncation with a positive matrix measure on `[0,s]`. It does
not identify a unique measure, microscopic dynamics, or physical mechanism.
Finite truncation cannot detect alternatives sharing all acquired covariance
blocks with a null law. The nonasymptotic band is Gaussian and conservative.
The LAN theorem assumes positive-definite covariance and the stated regularity
condition. The strictness theorem is relative to the precisely defined
predecessor test, not every conceivable support test.

## Not assessed / not applicable

- Bibliographic integrity under ARR protocol: **not assessed**.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific reproduction: **not assessed**.
- Empirical coverage calibration: **not assessed**.
- Lean 4: **not applicable**.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent
editorial or scientific assessment is claimed.
