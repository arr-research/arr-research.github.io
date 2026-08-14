# Verification report

- Record: `ARR-2026-7CCV86W3Y59VS8PN v1`
- Protocol: `ARR-VERIFY-1.0`
- Canonical PDF SHA-256:
  `e7ee32ac72a58ed620deb2e5598e54acf33713616dbb57e5676efcd2c236c534`
- Canonical PDF size: `385441` bytes
- Canonical PDF geometry: 14 A4 pages

## Checks performed

1. Recomputed the canonical PDF SHA-256, byte count, page count, title,
   authorship metadata, and A4 page geometry.
2. Compiled the preserved LaTeX source with MiKTeX `pdflatex` and `bibtex`;
   the final log contained no unresolved references, undefined citations,
   overfull or underfull boxes, or LaTeX/package warnings.
3. Rendered all 14 pages with Poppler and visually inspected the manuscript for
   clipping, overlap, broken equations, malformed tables, and missing text.
4. Ran `verify_canonical_tester_compression.py`: **PASS**. It uses exact SymPy
   arithmetic to check a genuinely singular Moore-Penrose compression, a mixed
   rank-two Rado support fixture, the full-rank-noise spectral-tail fixture,
   exact prior-profile examples, and the weighted Gram identity.
5. Ran the supplied deterministic package builder and checker: **PASS**. The
   release ZIP has SHA-256
   `7db8d4d1e8b6b80388a9747e7ffcb437df06c9b0203c1f0a3cc1ea9bbd37f5a7`.
   The ZIP was extracted to a fresh directory; its self-contained package
   check and exact verifier both passed.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial**. The executable evidence checks exact finite
  fixtures and formula identities. It is not a formal proof of the universal
  Rado-tester theorem, spectral-tail theorem, or novelty claims.
- Bibliography: **not assessed** under an ARR bibliography protocol.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific validation: **not assessed**.

ARR publication records technical preservation and the checks above. It is not
an independent finding that every theorem or novelty claim is correct.
