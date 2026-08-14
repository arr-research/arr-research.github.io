# Algebraic Query Support for Unitary Oracles

This directory contains the manuscript, exact verifier, deterministic figure
source, and release metadata for Paper 19.

## Reproduce

From `verification/`:

```powershell
python verify_oracle_varieties.py
python make_figure.py
```

From `paper/`:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error oracle_varieties_query_support.tex
bibtex oracle_varieties_query_support
pdflatex -interaction=nonstopmode -halt-on-error oracle_varieties_query_support.tex
pdflatex -interaction=nonstopmode -halt-on-error oracle_varieties_query_support.tex
```

From the package root, freeze or verify the release:

```powershell
python package_release.py
python package_release.py --check
```

The ZIP contains both the compiled source-tree PDF and the canonical PDF.
Consequently `--check` also runs directly after extraction, without requiring
a LaTeX rebuild.

Reference environment used for the figure: Python 3.12.6, NumPy 2.5.1,
Matplotlib 3.11.1. The exact verifier uses only the Python standard library.

## Scope

The arbitrary-variety Hilbert law is a causal forward-query theorem. The
stronger general-tester probability cap is proved only for compact transitive
unitary orbits. Controlled-U, U-dagger, postselection, and altered oracle
models are outside scope. The manuscript does not claim that all general
process matrices are physically realizable.

## AI disclosure

OpenAI Codex assisted with symbolic exploration, literature triage, drafting,
and reproducibility checks. The author retains responsibility for every
definition, proof, claim, citation, and submission decision.
