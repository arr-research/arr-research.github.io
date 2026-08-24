# ARR-2026-2MZWECWVEN97ARVQ v1

Lluis Eriksson's research paper is titled *Fat Gauss Fibres and
Tjurina–Milnor Defects Forced by Osculating Absorption*.

For a smooth complex hypersurface, the paper distinguishes the length of a
scheme-theoretic Gauss fibre from the multiplicity of the dual. Locally these
are measured by Tjurina and Milnor numbers, respectively. It proves

`mult_eta(X^vee) - length(Gamma_eta) = sum_p (mu_p - tau_p)`

and shows that point-span order-`s` osculating absorption forces

`length(Gamma_eta) >= binom(d+s-1,d) binom(d+m,d)`.

For `d(s-1) > s+1`, a prescribed-jet construction realizes every integral
defect from zero through the extremal reduced-support size while keeping all
local Milnor numbers equal to `s^d`.

## Package map

- `paper.tex` is the canonical source; `paper.pdf` is the inspected local rendering.
- `paper.md` and `paper.txt` are machine-readable renditions.
- `src/repro/` contains standard-library exact replay code and committed JSON.
- `src/audits/` contains the exact-hash referee report, author response,
  research audit, and artifact QA record.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, `CITATION.cff`, and
  `VERIFICATION.md` describe the record.

## Evidence boundary

- Source integrity and exact finite replays: pass for the deposited hash.
- Reproducibility: partial. Finite calculations replay exactly; the universal
  algebraic-geometric arguments and cited classical theorems are not mechanized.
- Bibliography: selective primary-source comparison, not exhaustive priority
  certification.
- ARR screening, human peer review, formal verification, and independent
  reproduction: not assessed.

The read-only Codex referee score of 8.95/10 ±0.30 is an AI editorial
diagnostic on the author's requested scale, not external human validation.
The author is ARR's founder-editor; that conflict is explicit. Deposit
preserves a citable research object and its evidence without certifying the
claims.

## Licenses

The manuscript and prose are CC-BY-4.0, Python replay code is Apache-2.0, and
JSON data and catalogue metadata are CC0-1.0. Full texts and machine-readable
scope declarations are under `LICENSES/` and in `LICENSES.json`.
