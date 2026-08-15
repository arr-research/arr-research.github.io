# ARR-2026-7D2BBEC8MJ8BM80S v1

This is a founder-owned ARR record for Lluis Eriksson's paper, *Cellulation-Independent Boundary Gauge Averaging and Sharp Class-Sector Gaps in Two-Dimensional Yang--Mills*.

## Files

- `paper.pdf` is the canonical deposited manuscript. SHA-256: `ee51663a977f1932da74670956aafe39e6f43ac355c6d27b472a4285a2b3fe34`.
- `paper.tex` preserves the complete LaTeX source used for the final build; `references.bib` provides the bibliography in a reusable pure-text format.
- `paper.md` and `paper.txt` are mechanically extracted, machine-readable renditions. Mathematical typography may be degraded; verify quotations and formulae against the PDF.
- `src/repro/` preserves the Python replay, Lean modules, axiom audit, pinned toolchain and Lake manifest, exact reproduction driver, supplied release manifest, and complete Git bundle containing both cited commits.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, and `CITATION.cff` describe this exact version.
- `VERIFICATION.md` records only the checks actually performed.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial**; the numerical replay passes and both cited Lean checkouts build, but the compact-group/topological theorem is not a monolithic formal theorem and the complete network-fresh driver was not run end to end.
- Bibliography: **not assessed** by ARR.
- Lean 4: **L2**; source, successful builds, and an axiom audit are supplied. No L3 full-manuscript correspondence claim is made.
- Frontier-model screening and independent peer review: **not assessed**.

The author is also ARR's current founder-editor. This conflict is explicit in the public metadata. Publication is not peer review and does not certify correctness, novelty, or importance.
