# Verification record for ARR-2026-66Q8M61AA196T8BC v2

Date: 2026-08-24
Protocol: ARR-VERIFY-1.0

## Source integrity — pass

- Canonical `paper.tex`: 29,998 bytes; SHA-256
  `17810cc2c07029b913b50665bf72fa569762670cc836900bc3cbfa1bfea0a414`.
- Rendered `paper.pdf`: 411,060 bytes; SHA-256
  `bc38ace5861ded29f0bf943e8825dac5d785a59f1ffbbaa917a7a154d02f2d7d`.
- Three MiKTeX-pdfTeX 4.23 passes produced a ten-page A4 PDF.
- The final log contains no configured LaTeX/package warnings, undefined
  references, overfull/underfull boxes, errors, emergency stops, or fatal
  errors. MiKTeX emitted only its local installation update reminder outside
  the LaTeX log.
- All ten pages were rendered at 130 dpi and visually inspected. After the two
  final wording changes, pages 2 and 7 were re-inspected and the other eight
  page renders were byte-identical to the already inspected renders.
- `paper.md` and `paper.txt` were regenerated from the exact final PDF.

The ARR release workflow recompiles `paper.tex` under Ubuntu TeX Live. Its PDF
is independently derived and need not be byte-identical to the inspected
MiKTeX rendering. Release hashes are verified after publication.

## Exact finite checks — pass

The command

    python src/repro/run_all_replays.py

regenerated `results.json` and matched it byte for byte at SHA-256
`b8283387b79f4a0d86a710ff805b4b2727fc2ea772195e8b3daa89019d830676`.
The exact checks comprise 250 exact-vs-legacy comparisons, 180 strict
dominance cases, 250 brute-force legacy packing cases, three rational
higher-block matrices, four modular unisolvent fixtures, three finite-field
local-contact fixtures, and 44 curve threshold counterexamples through
`s=8`.

These are diagnostic finite witnesses. They do not prove the incidence
dimension estimates, existence or smoothness of a general member, universal
rank claims, novelty, or priority.

## Reproducibility label — partial

The standard-library replay is deterministic and uses exact integer, rational,
and finite-field arithmetic. The universal algebraic-geometric arguments are
not mechanized and no independent implementation is deposited. The proper
label is therefore `partial`.

## Bibliographic comparison — selective

Primary sources were checked for Ballico's `X`-rank of linear subspaces,
jet-ampleness, principal-parts/osculating bundles, and adjacent osculating and
secant geometry. The exact tangent floor is cited to the author's separate ARR
record. The search was not exhaustive and does not certify novelty or
priority; metadata conservatively records bibliography as `not_assessed`.

## Independent Codex referee — not ARR screening

A separate read-only Codex referee audited the exact final source hash. It
found no P0 or mathematical P1 issue, reported 7.9/10 with uncertainty 0.4 on
the author's requested scale, and judged the paper scientifically publishable
subject to the separate compilation and replay checks recorded above. The
remaining reservations are selective priority coverage and dependence of the
exact-floor reduction on another paper by the same author. The report is at
`src/audits/REFEREE_REPORT.md`.

This is not ARR-SCREEN-1.0, human peer review, formal verification,
independent reproduction, or priority certification. ARR screening remains
`not_assessed`.

## Material limitations

- The higher-order hypothesis is explicit; tangent absorption alone is not
  claimed to imply higher absorption.
- The theorem assumes a complete tensor-power embedding, smooth integral
  positive-dimensional variety, algebraically closed field, and nonempty
  finite reduced support.
- The rank-sensitive second term requires `m >= 2s+1`; no optimal replacement
  is claimed below that threshold.
- The extremizer degree is sufficient, not minimal; equality sets are not
  classified.
- The author is also ARR's founder-editor.

## Licenses

The manuscript is CC-BY-4.0, replay Python is Apache-2.0, and JSON data and
catalogue metadata are CC0-1.0. Declarations are scoped in `metadata.json` and
`LICENSES.json`; complete texts are under `LICENSES/`.
