# ARR-2026-6WX2JF38WE87GB2M v1

This is a founder-owned ARR pilot record for Lluis Eriksson's research paper,
*Algebraic Query Support for Unitary Oracles: Exact Hilbert Laws, Harmonic
Spectra, and General-Tester Bounds*.

## Files

- `paper.pdf` is the canonical 14-page deposited manuscript. SHA-256:
  `b88efdbc4f3cbd39c4160e0803c795c4a1e640b5dac919b95edc681a6f4e1cec`.
- `paper.md` and `paper.txt` are mechanically extracted machine-readable
  renditions. Mathematical typography may be degraded; verify quotations and
  formulae against the PDF.
- `src/manuscript/` preserves the final LaTeX source, bibliography, and the two
  figure files without redefining the canonical PDF source of truth.
- `src/replay/` preserves the exact-arithmetic verifier, figure producer,
  pinned dependencies, supplied manifest, claim ledger, submission sheet, and
  release instructions.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, and `CITATION.cff`
  describe this exact version.
- `VERIFICATION.md` records only the checks actually performed for ARR.

## Evidence labels

- Source integrity: **pass**.
- Supplied exact-arithmetic replay: **pass**.
- Figure byte-reproduction check: **pass**.
- ARR reproducibility label: **partial**. The replay checks finite symbolic
  fixtures and formula identities; it does not formally verify every analytic
  theorem or the general-tester argument.
- Bibliography: **not assessed** under an ARR bibliography protocol.
- Lean 4: **not applicable**.
- Frontier-model screening and peer review: **not assessed**.

The paper concerns finite-dimensional, noiseless repeated access to the same
unitary channel under explicit promise varieties. It does not cover inverse
queries, controlled bypasses, noisy hardware, finite-sample inference, or
tester models beyond the stated standard framework. Query support is a linear
dimension and is not itself a physical memory cost or a guarantee that every
finite ensemble attains the resulting discrimination bound.

This record extends the all-`k` support geometry behind the `k=2` fixed-trace
defect used in `ARR-2026-5KS70GV7KK9DYA69`; it does not reuse that companion
paper's adaptive-attainment certificate.

The author is also ARR's current founder-editor. This conflict is explicit in
the public metadata. Publication is not peer review and does not independently
certify that the scientific claims are correct.
