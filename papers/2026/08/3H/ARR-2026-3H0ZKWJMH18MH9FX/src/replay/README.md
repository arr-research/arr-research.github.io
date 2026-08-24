# Reproducibility

Tested on Windows 11 with Python 3.12.13, NumPy 2.5.1, pypdf 6.4.0, and MiKTeX
pdfTeX 1.40.28.  The numerical replay is lightweight and requires no network.

From the ARR record root, create an isolated environment and install the
pinned Python dependencies before running the checker:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r src/replay/requirements.txt
```

## Verify the frozen mathematical replay

```powershell
python src/replay/verify_full_spark_list_threshold.py --check src/replay/results/full_spark_list_threshold_certificate.json
```

The replay checks 15 harmonic frames with `3 <= N <= 7`, all relevant minors,
the exterior Hodge identity, constructive nullspace compression of a Hodge
POVM to at most `r^2` effects, an unequal-norm Parseval full-spark fixture whose
unit representatives are not tight, three arithmetic-support multiplicity
fixtures saturating the divisor-branch dimension converse, exact covariant
rank-two list POVMs for every `2<=d<=10` and every list size, a harmonic-frame
spectral floor with a perturbation check, and the two hypothesis
counterexamples.  It does not certify the
all-dimensional proof.

## Rebuild the manuscript

The ARR record flattens the canonical manuscript sources into its root. On the
tested Windows/MiKTeX setup, run from that record root:

```powershell
pdflatex --interaction=nonstopmode --halt-on-error paper.tex
bibtex paper
pdflatex --interaction=nonstopmode --halt-on-error paper.tex
pdflatex --interaction=nonstopmode --halt-on-error paper.tex
```

## Supplied pre-deposit helpers

`build_final_local.ps1` and `package_release.py` are preserved byte-for-byte as
provenance from the author's pre-deposit tree. They expect that original tree
layout and are not the ARR release driver after flattening. ARR validates this
record with `scripts/validate_papers.py`, builds the catalogue with
`scripts/build_site.py`, and creates the immutable release with
`scripts/package_paper.py`.
