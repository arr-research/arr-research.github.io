# Reproducibility and visual audit

## Frozen checks

- Python 3.12.6, isolated mode (`python -I`).
- Replay at every rank through ambient dimension 20: PASS.
- Optimized Python (`python -O`): deliberately rejected before verification.
- MiKTeX-pdfTeX 4.23 (MiKTeX 25.12), two clean manuscript passes: PASS.
- Undefined references/citations and overfull boxes: none.
- Poppler 26.05.0 rendered every page at 150 dpi.
- Visual inspection of all nine pages: no clipping, overlap, truncated text, or
  unreadable equations; links, table, theorem boxes, and references are legible.

The single underfull bibliography line reported by TeX is typographic and does
not affect legibility. PDF byte identity across toolchains is not claimed.

## Scope

The replay checks the finite exact arithmetic described in Section 8. It does
not formalize the arbitrary-dimensional analytic proof or the imported Horn
theorem and does not constitute peer review or an independent novelty finding.
