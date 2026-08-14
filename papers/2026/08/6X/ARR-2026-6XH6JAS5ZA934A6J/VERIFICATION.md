# Verification record for ARR-2026-6XH6JAS5ZA934A6J v1

Date: 2026-08-14

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The canonical PDF is 374,586 bytes with SHA-256 `01678e31e1fc652a1d1b8c8b00023ad6bc192439bc27267a0abde4d4568ede51`.
- PDF inspection found 11 A4 pages, one vector figure, no encryption, no forms, and no JavaScript.
- All 11 pages were rendered independently with Poppler and visually inspected, including full-resolution checks of the title, saddle proof, figure, projective corollary, and bibliography.
- The final pdfLaTeX/Biber build completed with no undefined references or citations, package warnings, or overfull/underfull boxes.
- `paper.md` and `paper.txt` are machine-readable renditions of the exact PDF, not replacements for the canonical typography.
- LaTeX, bibliography, vector figure, generator, replay programs, and frozen JSON were copied from the frozen author release and rehashed during ingestion.

## Reproducibility — partial

The bounded replay command completed successfully on the ingestion machine:

```text
powershell -ExecutionPolicy Bypass -File src/replay/replay_all.ps1
```

Observed checks include 728 exact rectangular-dimension identities, 728 Hodge-complement identities, 196 independent Weyl/hook/hypergeometric coefficient checks, exact exceptional cumulants, the complex-sphere hypergeometric reduction to relative error below `2.1e-15`, and bounded scalar activation/asymptotic diagnostics.

This is labelled **partial**, not pass, because the all-representation Cartan-product rigidity, standard-Borel Shannon converse and attainment, and uniform asymptotic theorem are analytic arguments rather than formally certified computations.

## Scope

The source is a classical phase-sensitive amplitude vector. This record is not a quantum rate–distortion theorem, a click-only Born-probability model, a derivation of Born's rule, or a particle-dynamics model. Sugita's integer coherent-state moment theorem is prior work and is explicitly identified as an input.

## Not assessed / not applicable

- Bibliographic integrity under ARR protocol: **not assessed**.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific reproduction: **not assessed**.
- Lean 4: **not applicable**.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
