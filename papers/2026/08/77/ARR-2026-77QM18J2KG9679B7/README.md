# ARR-2026-77QM18J2KG9679B7 v1

Founder-owned ARR pilot record for Lluis Eriksson's paper, _Finite-Sample Spectral-Gap Falsification: Exact Weighted Visibility Minimax, Hidden-Atom LAN, and Honest Dependent Tests_.

## Files

- `paper.pdf` is the canonical deposited manuscript. SHA-256: `db6246f174d209eac2354b372af48649f1c55a9ced1d4ba9cdda59394aa8e668`.
- `paper.md` and `paper.txt` are mechanically extracted, machine-readable renditions.
- `src/manuscript/` preserves the supplied LaTeX source.
- `src/replay/` preserves pure-text code, notebooks, certificates, audit notes, and manifests from the supplied reproducibility archive.
- `src/formal/` preserves the commit-identified Lean 4 source and axiom audit when available.
- `VERIFICATION.md` records the checks actually performed.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial** (three deterministic replay commands passed; they do not prove all analytic claims).
- Bibliography: **not assessed**.
- Lean 4: **not assessed**. The exact source and axiom-audit files are preserved, but the pinned Mathlib dependency did not finish downloading within the 10-minute ingestion limit, so ARR does not claim an independent build.
- Frontier-model screening: **not assessed**.
  The paper's central boundary is deliberately limited: rejection may falsify an overstated gap, while non-rejection alone is not a positive gap certificate. The depositor reports that ai.viXra has not made this paper public and no public identifier is known.
  The author is also ARR's current founder-editor. This conflict is explicit. Publication is not peer review and does not certify that the claims are correct.
