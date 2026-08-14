# ARR-2026-7CCV86W3Y59VS8PN v1

This is a founder-owned ARR pilot record for Lluis Eriksson's research paper,
*Matroidal Bayes Bounds for General Quantum Process Discrimination: Canonical
Compression, Support Congestion, and Exact Qubit Phase Families*.

## Files

- `paper.pdf` is the canonical 14-page deposited manuscript. SHA-256:
  `e7ee32ac72a58ed620deb2e5598e54acf33713616dbb57e5676efcd2c236c534`.
- `paper.md` and `paper.txt` are mechanically extracted machine-readable
  renditions. Mathematical typography may be degraded; verify quotations and
  formulae against the canonical PDF.
- `src/manuscript/` preserves the final LaTeX source, bibliography, figure
  generator, and frozen figure files.
- `src/replay/` preserves the exact verifier, deterministic package builder,
  supplied manifest, claim ledger, submission sheet, and pinned dependencies.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, and `CITATION.cff`
  describe this exact version.
- `VERIFICATION.md` records only checks actually performed for ARR.

## Evidence labels

- Source integrity: **pass**.
- Supplied exact-arithmetic replay: **pass**.
- Supplied deterministic package and extracted replay: **pass**.
- ARR reproducibility label: **partial**. The replay checks exact finite
  fixtures and identities; it does not formally prove every universal theorem.
- Bibliography: **not assessed** under an ARR bibliography protocol.
- Lean 4: **not applicable**.
- Frontier-model screening and peer review: **not assessed**.

The paper gives architecture-independent upper bounds within a stated physical
deterministic tester cone. It does not claim that every bound is attainable,
that support data determine every mixed-process optimum, or that the positive
low-rank core in the robust theorem is automatically optimal.

`ARR-2026-6WX2JF38WE87GB2M` is a companion record about global algebraic query
support. The present record instead resolves label-specific support congestion,
arbitrary priors, mixed supports, and spectral-tail robustness; neither record
replaces the other.

The author is also ARR's current founder-editor. This conflict is explicit in
the public metadata. Publication is not peer review and does not independently
certify that the scientific claims or novelty assessment are correct.
