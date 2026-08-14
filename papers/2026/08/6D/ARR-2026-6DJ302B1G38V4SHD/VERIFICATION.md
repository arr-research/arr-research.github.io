# Verification record for ARR-2026-6DJ302B1G38V4SHD v1

Date: 2026-08-14

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The canonical PDF is 468,754 bytes with SHA-256
  `3848730dfd1e4883f8b9de9a63c5ae0c123cf389569829d671503e5cbfe642a6`.
- PDF inspection found 13 A4 pages, one vector figure, no encryption, no forms,
  and no JavaScript.
- All 13 pages were rendered with Poppler and visually inspected, including
  full-resolution checks of the title, differentiated Weyl–Bessel proof,
  convex-envelope curvature, figure, scope statement, and bibliography.
- The final pdfLaTeX/Biber build completed with no undefined references or
  citations, package warnings, or overfull/underfull boxes.
- `paper.md` and `paper.txt` are machine-readable renditions of the exact PDF,
  not replacements for the canonical typography.
- LaTeX, bibliography, figure, generator, replay programs, frozen JSON, and
  dependency versions were copied from the frozen author release and rehashed
  during ingestion. The generator received only a path-layout adaptation for
  the ARR directory structure.

## Reproducibility — partial

Both bounded deterministic replay programs completed successfully on the
ingestion machine:

```text
powershell -ExecutionPolicy Bypass -File src/replay/replay_all.ps1
```

The exact coherent-orbit replay completed in approximately 0.08 seconds. The
broader semiclassical-family replay completed in approximately 3.88 seconds.
The packaged figure generator also executed successfully with the declared
NumPy, SciPy, and Matplotlib versions.

This is labelled **partial**, not pass, because the uniform differentiated
Weyl–Bessel saddle, entropy-duality theorem, global contact localization, and
matched boundary-layer limit are analytic arguments rather than formally
certified computations.

## Scope

The source is a classical phase-sensitive coherent-amplitude vector. This is
not quantum rate-distortion, quantum channel coding, click simulation, a
particle-dynamics model, or a derivation of Born's rule. Eventual uniqueness
is proved only for the global minimizing origin contact. The fixed-distortion
limit excludes exact zero distortion, and boundary convergence is locally
uniform only on compact subsets of the positive boundary coordinate.

## Not assessed / not applicable

- Bibliographic integrity under ARR protocol: **not assessed**.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific reproduction: **not assessed**.
- Numerical interval certification: **not assessed**.
- Lean 4: **not applicable**.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent
editorial or scientific assessment is claimed.
