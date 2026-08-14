# Global projective memory and resonant bottlenecks

This directory contains the source of the paper proving that the passive
McMillan state cost of every finite line-routing table equals its minimum
projective interpolation degree. It also gives exact full-support laws for
line-to-subspace incidence in orthogonal bands, an intrinsic error operator,
the exact border-memory deletion law, and a high-delay compactness theorem.

Build from this directory:

```powershell
python make_phase_figure.py
pdflatex -interaction=nonstopmode -halt-on-error global_projective_memory.tex
bibtex global_projective_memory
pdflatex -interaction=nonstopmode -halt-on-error global_projective_memory.tex
pdflatex -interaction=nonstopmode -halt-on-error global_projective_memory.tex
```

Exact certificate from the repository root:

```powershell
python verification\verify_global_projective_memory.py `
  --check results\global_projective_memory\certificate.json
python verification\verify_planar_projective_memory.py
```

The global verifier uses exact SymPy rational arithmetic and compares its
complete normalized JSON output byte-for-byte with the frozen certificate.
The planar verifier independently replays the explicit planar strata used as
audit fixtures in the second half of this single global paper.  The former
standalone planar draft is provenance only and is not a second submission.
