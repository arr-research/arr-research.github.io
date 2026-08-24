# Verification record for ARR-2026-0WAPCGQHNC82S8VJ v1

Date: 2026-08-24  
Protocol: ARR-VERIFY-1.0

## Source integrity — pass

- Canonical `paper.tex`: 25,277 bytes; SHA-256
  `1dcee79755257e0e4c46e63f259c3a2f3f9fc832c063d229057db3f383854770`.
- Inspected local `paper.pdf`: 385,598 bytes; SHA-256
  `d1462aad6ef51ea33255ebc30737d012ba980c90133982ac514161096304c435`.
- Three MiKTeX-pdfTeX passes produced an eight-page A4 PDF.
- The final log has no LaTeX/package warnings, undefined references, errors,
  emergency stops, fatal errors, or overfull boxes. Five underfull boxes occur
  only in long bibliography URLs and are visually harmless.
- All eight pages were rendered and visually inspected.
- `paper.md` was converted from the final TeX and given an explicit title and
  abstract; `paper.txt` was extracted from the final PDF.

The ARR release workflow recompiles `paper.tex` under Ubuntu TeX Live. Its PDF
is independently derived and need not be byte-identical to the inspected
MiKTeX rendering. Release hashes are checked after publication.

## Exact finite checks — pass

The command

    python src/repro/run_all_replays.py

regenerated `results.json` and matched it byte for byte at SHA-256
`3948e982b774dca3e48215178dc844ded15f83b2a04b96872a3bc7bf1df2497e`.
The verifier checks 105 numerical floor cases, 100 cases where the predecessor
rank term collapses on a Gauss fibre, four exact rational simplex-evaluation
matrices, and five monomial Jacobian quotient fixtures.

These are finite diagnostics. They do not prove the incidence arguments,
Gauss normalization, the classical multiplicity–Milnor and tangent-cone
theorems, the universal claims, novelty, or priority.

## Reproducibility label — partial

The replay is deterministic, standard-library-only, and uses exact integers
and `Fraction` arithmetic. The universal algebraic-geometric arguments are not
mechanized and no independent implementation is deposited. The correct label
is therefore `partial`.

## Bibliographic comparison — partial

Primary sources were checked for the multiplicity–Milnor formula, its broader
extensions, and recent dual-hypersurface applications. Dimca's 1987
Proposition 11.24 is cited for the tangent-cone cycle. Public authorial
antecedents B218/B219 and both related ARR records were compared directly.
The search is selective and does not certify novelty or priority.

## Independent Codex referee — not ARR screening

A separate read-only Codex referee audited the exact mathematical source hash
before the final editorial version-label change. After the substantive P1/P2
repairs it reported no remaining P0/P1/P2, scored the work 7.9/10 with
uncertainty 0.4 on the author's requested scale, and judged it scientifically
ready for ARR given the build and replay checks above.

This is an AI audit, not ARR-SCREEN-1.0, human peer review, formal verification,
independent reproduction, or priority certification. ARR screening remains
`not_assessed`.

## Material limitations

- The dual-singularity theorem is over the complex numbers.
- `Z` is the complete reduced Gauss fibre; the scheme-theoretic fibre is not
  classified and may be nonreduced.
- The hypersurface-degree threshold is sufficient, not minimal.
- For `s=1`, distinct branch tangent hyperplanes are not called a simple
  normal-crossing divisor without the required general-position condition.
- No analytic branch classification, equality classification, exhaustive
  priority review, human peer review, or formal verification is claimed.
- The author is also ARR's founder-editor.

## Licenses

The manuscript and prose are CC-BY-4.0, replay Python is Apache-2.0, and JSON
data and catalogue metadata are CC0-1.0. Declarations are in `metadata.json`,
`LICENSES.json`, and `LICENSES/`.
