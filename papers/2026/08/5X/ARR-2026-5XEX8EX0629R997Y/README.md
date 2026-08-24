# Euler-Reduced Tjurina Floors for Osculating-Absorbing Gauss Fibres

ARR record candidate ARR-2026-5XEX8EX0629R997Y, version v1.

The canonical research source is paper.tex. The repository also preserves
the inspected eight-page paper.pdf, a plain-text extraction, a
machine-readable Markdown rendition, exact finite replays, and the audit
record.

## Reproduce the finite checks

From this directory run:

    python src/repro/run_all_replays.py

The driver runs exact integer checks for 1 <= d <= 8, 1 <= s <= 20,
exact SymPy Gröbner checks over QQ for the sharp plane family
1 <= s <= 12, and explicitly delimited two-prime modular fixtures. It writes
src/repro/results.json.

These computations certify only the displayed finite fixtures. The general
claims are established by the manuscript proofs; they are not formally
verified.

## Scope and limitations

- All theorems are stated over the complex numbers.
- The universal local floor is proved in every dimension, but sharpness is
  established only in dimension two.
- The global equality construction is for surfaces and uses a sufficient,
  non-optimized degree threshold.
- The bibliographic comparison is selective and does not certify exhaustive
  novelty or priority.
- No human peer review, ARR screening, formal verification, or independent
  reproduction is claimed.
- The author is also ARR's founder-editor; the conflict is declared in
  metadata.json.

## Licenses

Manuscript and prose are CC-BY-4.0, Python replay code is Apache-2.0, and JSON
replay data and catalogue metadata are CC0-1.0. See LICENSES.json and
LICENSES/.
