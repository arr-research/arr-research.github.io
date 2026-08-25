# Prescribed Tjurina Algebras and Complete Spectra in Osculating-Absorbing Gauss Fibres

ARR record candidate `ARR-2026-4FYHCBAQ0T8FHRBT`, version v1.

The canonical research source is `paper.tex`. This package also preserves the
inspected eight-page PDF, full plain-text and machine-readable renditions,
exact finite replays, audit reports, provenance, licensing, and integrity
metadata.

## Reproduce the finite checks

From this directory run:

    python src/repro/run_all_replays.py

The driver checks exact binomial formulas through (s=50), exact rational
strong-Lefschetz ranks through (s=8), direct quotient fixtures over two large
prime fields for (2\le s\le7), simplex-lattice evaluation ranks in dimensions
1 through 4, and all surface-spectrum decompositions in the stated finite
fixture grid.

These computations certify only the displayed finite cases. The universal
claims are established by the manuscript proofs; they are not formally
verified.

## Scope and limitations

- All theorems are over the complex numbers.
- The ambient-degree thresholds are sufficient and are not claimed minimal.
- Wahl's numerical three-variable minimum, the plane local spectrum, finite
  determinacy, strong Lefschetz, and dual multiplicity are attributed to their
  sources; no exhaustive priority claim is made.
- The separate Codex referee audit is an AI audit, not human peer review,
  formal verification, or independent reproduction.
- ARR screening is `not_assessed`.
- The author is also ARR's founder-editor; the conflict is declared in
  `metadata.json`.

## Licenses

Manuscript and prose are CC-BY-4.0, Python replay code is Apache-2.0, and JSON
replay data and catalogue metadata are CC0-1.0. See `LICENSES.json` and
`LICENSES/`.

