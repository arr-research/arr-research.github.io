# Verification report

- Record: `ARR-2026-6WX2JF38WE87GB2M v1`
- Protocol: `ARR-VERIFY-1.0`
- Canonical PDF SHA-256:
  `b88efdbc4f3cbd39c4160e0803c795c4a1e640b5dac919b95edc681a6f4e1cec`
- Canonical PDF size: `422028` bytes
- Canonical PDF geometry: 14 A4 pages

## Checks performed

1. Recomputed the PDF SHA-256, byte count, page count, and page geometry.
2. Compiled the preserved LaTeX source with MiKTeX `pdflatex` and `bibtex`;
   the final log contained no unresolved references, undefined citations,
   overfull boxes, or LaTeX/package warnings.
3. Rendered all 14 pages with Poppler and visually inspected the manuscript for
   clipping, overlap, broken tables, malformed equations, and missing text.
4. Ran `verify_oracle_varieties.py`: **PASS**. It uses exact integer and
   rational arithmetic to check the quadric, conic, and Segre Hilbert ranks;
   rational spherical and planar-axis spectra; purity identities; endpoint
   branches; and the stated finite tightness fixtures.
5. Ran `make_figure.py` twice in clean temporary output locations. Both PDF
   figures had SHA-256
   `399180ce75b7ceada1dd461b8b419557675f74a3ce368eb6cffe4f0d82c14be2`,
   identical to the preserved figure.
6. Rebuilt and checked the supplied deterministic reproducibility ZIP, then
   extracted it to a fresh directory and reran its release check. Its SHA-256
   is `d2c3d5220593b52a2142ac436058fde280472dfc47f8b269d110df167f798946`.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial**. The replay checks finite exact identities and
  representative rank/spectrum formulae. It is not a formal proof of the
  universal Hilbert-function theorem, the general-tester domination argument,
  or the novelty claims.
- Bibliography: **not assessed** under an ARR bibliography protocol.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific validation: **not assessed**.

ARR publication records technical preservation and the checks above. It is not
an independent finding that every theorem or novelty claim is correct.
