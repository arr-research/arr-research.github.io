# Verification report

- Record: `ARR-2026-5KS70GV7KK9DYA69 v1`
- Protocol: `ARR-VERIFY-1.0`
- Canonical PDF SHA-256:
  `bb1e9ccc4176c73834a5d8dd6c91ac0cf91d20c7f4b5d74016d89cc82d108863`
- Canonical PDF size: `413708` bytes
- Canonical PDF geometry: 12 A4 pages

## Checks performed

1. Recomputed the PDF SHA-256, byte count, page count, and page geometry.
2. Compiled the preserved LaTeX source with MiKTeX `pdflatex` and `bibtex`;
   the final log contained no unresolved references, undefined citations,
   overfull boxes, or LaTeX/package warnings.
3. Rendered all 12 pages with Poppler and visually inspected the manuscript for
   clipping, overlap, broken tables, malformed equations, and missing text.
4. Ran `verify_coherent_order_echo.py`: **PASS**. This script combines exact
   symbolic word/resultant calculations with numerical root finding and
   tolerance-based class grouping.
5. Ran `verify_two_use_a4.py`: **PASS**. It uses NumPy and an explicit numerical
   tolerance to audit the two-copy spectrum, clamp, and the `q=1/2` parallel
   fixture.
6. Ran `verify_two_use_causal_qhalf.py`: **PASS**. It uses exact rational
   arithmetic in the quotient by
   `t^8+12t^6-10t^4-20t^2-239` to verify the comb normalization, six-Kraus
   realization, algebraic orbit weights, and `K C K = K` identity at `q=1/2`.
7. Rebuilt the supplied deterministic reproducibility ZIP and checked its
   internal manifest. Its SHA-256 is
   `2b1bd571bf288a0b434972e69182006d62cbf6bf2907745e2fc8b8e857fd8559`.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial**. The central causal certificate is exact; the
  other two replays contain transparent numerical diagnostics and do not
  constitute machine proofs of the universal analytic arguments.
- Bibliography: **not assessed** under an ARR bibliography protocol.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific validation: **not assessed**.

ARR publication records technical preservation and the checks above. It is not
an independent finding that every theorem or novelty claim is correct.
