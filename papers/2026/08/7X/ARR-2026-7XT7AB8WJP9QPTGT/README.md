# ARR-2026-7XT7AB8WJP9QPTGT v1

This is a founder-owned ARR pilot record for Lluis Eriksson's paper, *Certified Localized Weil Positivity Through Support 0.72: Multiband Schur Complements and a Complete Stieltjes Hierarchy*.

## Files

- `paper.pdf` is the canonical deposited manuscript. SHA-256: `e4fd12894f2d15bd503370a016f259aa0e2f619810ba309108ca6a1150a02935`.
- `paper.md` and `paper.txt` are mechanically extracted, machine-readable renditions. Mathematical typography may be degraded; verify quotations and formulae against the PDF.
- `src/manuscript/` preserves the final LaTeX source and vector figures.
- `src/repro/` exposes the pure-text verifier, patched source, audit records, and environment description. The full reproducibility ZIP, including the binary NPZ certificate objects and frozen source archive, is preserved as a release asset.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, and `CITATION.cff` describe this exact version.
- `VERIFICATION.md` records the checks actually performed.

## Evidence labels

- Source integrity: **pass**.
- Supplied terminal verifier: **pass**.
- ARR reproducibility label: **partial**, because ARR ran the frozen-object adjudication and independent audit but did not repeat the expensive 512-bit generation of the proof objects.
- Bibliography: **not assessed**.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.

The result is explicitly bounded to support `a <= 0.72` and is not represented as a proof of the Riemann hypothesis.

The author is also ARR's current founder-editor. This conflict is explicit in the public metadata. Publication is not peer review and does not independently certify that the claims are correct.
