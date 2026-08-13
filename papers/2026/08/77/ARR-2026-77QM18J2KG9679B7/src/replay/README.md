# Finite-Sample Spectral-Gap Falsification: reproducibility

The package preserves the source layout used by the LaTeX figure paths.

## Lightweight theorem replay

From the package root:

```powershell
python verification/finite_window_gap_certificates/verify_all.py
python verification/statistical_gap_boundary/certify_statistical_boundary.py
python verification/statistical_gap_boundary/verify_weighted_boundary.py
```

All three commands are deterministic and finish in seconds. The archived
ANNNI `L=14,16` records were generated in Colab Pro+ and are checked by hash;
they need not be recomputed locally.

## Manuscript build

```powershell
cd papers/paper16-statistical-gap-boundary
pdflatex -interaction=nonstopmode -halt-on-error statistical_gap_boundary.tex
pdflatex -interaction=nonstopmode -halt-on-error statistical_gap_boundary.tex
```

The terminal PDF has 23 pages, four figures, and two tables. The manifest uses
SHA-256 and covers every packaged file except itself.
