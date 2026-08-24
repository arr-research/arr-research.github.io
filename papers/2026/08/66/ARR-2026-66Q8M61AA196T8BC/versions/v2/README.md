# ARR-2026-66Q8M61AA196T8BC v2

This major revision of Lluis Eriksson's paper is titled *Exact Floors and
Proper-Span Extremizers for Higher Osculating Absorption*.

Version 1 proved a valid mixed-jet floor. The later exact tangent-absorption
theorem, ARR-2026-2MHNZRRJP49Y9SWP v3, strictly improves that numerical floor
for tensor powers. Version 2 records the corrected hierarchy: it derives the
exact binomial floor from tangent absorption, proves a rank-sensitive
higher-block refinement above its sharp uniform threshold, and constructs
proper-span equality examples in every allowed dimension, degree, osculating
order, and characteristic.

## Package map

- `paper.tex` is the canonical source; `paper.pdf` is its inspected rendering.
- `paper.md` and `paper.txt` are machine-readable renditions extracted from
  the final PDF; mathematical typography remains governed by the source/PDF.
- `src/repro/` contains exact replay code and committed JSON output.
- `src/audits/` contains the adversarial audit, referee report, response, and
  artifact QA record for this exact version.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, `CITATION.cff`, and
  `VERIFICATION.md` describe this version.

## Evidence boundary

- Source integrity and exact finite replays: **pass** after the final hashes
  recorded in `VERIFICATION.md`.
- Reproducibility: **partial**. The finite matrices and identities replay
  exactly; the universal algebraic-geometric proofs are not mechanized.
- Bibliographic verification: selective primary-source comparison, not an
  exhaustive priority review.
- Human peer review, formal verification, independent reproduction, novelty
  certification, and ARR protocol screening: **not assessed**.

The independent Codex referee report is an AI audit, not human peer review or
scientific certification. The author is also ARR's founder-editor; that
conflict is explicit. Deposit preserves a citable research object and its
evidence without certifying its claims.

## Licenses

The manuscript is CC-BY-4.0, Python replay code is Apache-2.0, and JSON data
and catalogue metadata are CC0-1.0. Full texts and machine-readable scope
declarations are preserved under `LICENSES/` and in `LICENSES.json`.
