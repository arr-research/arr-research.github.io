# Paper 16 reproducibility package

The canonical manuscript is `statistical_gap_boundary.tex`.

Build from this directory with two runs of:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error statistical_gap_boundary.tex
```

Lightweight replays from the repository root:

```powershell
python verification/finite_window_gap_certificates/verify_all.py
python verification/statistical_gap_boundary/certify_statistical_boundary.py
python verification/statistical_gap_boundary/verify_weighted_boundary.py
```

The archived ANNNI `L=14,16` records were generated in Colab Pro+ and are
verified by hash; they need not be recomputed locally. The submission sheet and
claim ledger state all scope gates and prohibited overclaims.
