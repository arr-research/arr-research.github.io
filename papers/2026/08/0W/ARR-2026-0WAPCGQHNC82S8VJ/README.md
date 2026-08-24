# ARR-2026-0WAPCGQHNC82S8VJ v1

Lluis Eriksson's research paper is titled *Exact Multiplicity Floors for Dual
Singularities from Absorbing Gauss Fibres*.

For a complete reduced Gauss fibre whose point span absorbs order-`s`
osculating spaces in the complete `O_X(m)` embedding, the paper combines an
absorption-forced contact estimate with the classical Dimca–Parusiński
multiplicity–Milnor formula and the exact tangent-absorption floor. It obtains

`mult_W(X^vee) >= s^d |Z| >= s^d binom(d+m,d)`

over the complex numbers and constructs proper-span equality examples with
exact reduced Gauss fibre and an explicit tangent-cone cycle.

## Package map

- `paper.tex` is the canonical source; `paper.pdf` is the inspected local
  rendering.
- `paper.md` and `paper.txt` are machine-readable renditions.
- `src/repro/` contains standard-library exact replay code and committed JSON.
- `src/audits/` contains the exact-hash referee report, author response,
  research audit, and artifact QA record.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, `CITATION.cff`, and
  `VERIFICATION.md` describe the record.

## Evidence boundary

- Source integrity and exact finite replays: pass for the deposited hash.
- Reproducibility: partial. Finite calculations replay exactly; the universal
  algebraic-geometric arguments and classical duality theorems are not
  mechanized.
- Bibliography: selective primary-source comparison, not exhaustive priority
  certification.
- ARR screening, human peer review, formal verification, and independent
  reproduction: not assessed.

The Codex referee score of 7.9/10 ±0.4 is an AI editorial diagnostic on the
author's requested scale, not external human validation. The author is ARR's
founder-editor; that conflict is explicit. Deposit preserves a citable
research object and its evidence without certifying the claims.

## Licenses

The manuscript and prose are CC-BY-4.0, Python replay code is Apache-2.0, and
JSON data and catalogue metadata are CC0-1.0. Full texts and machine-readable
scope declarations are under `LICENSES/` and in `LICENSES.json`.
