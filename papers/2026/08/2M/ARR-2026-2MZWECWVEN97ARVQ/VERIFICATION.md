# Verification record for ARR-2026-2MZWECWVEN97ARVQ v1

Date: 2026-08-25  
Protocol: ARR-VERIFY-1.0

## Source integrity — pass

- Canonical `paper.tex`: 26,132 bytes; SHA-256
  `36db52e07b299dedb47873c87fd8383261c4364a0e73b4eb41af1516b2be7c2c`.
- Inspected local `paper.pdf`: 413,796 bytes; SHA-256
  `ce0f5f606d51ba2c03676ddc66f361d64e3167e4133a041cd9b173049110ba38`.
- Three MiKTeX-pdfTeX passes produced a nine-page A4 PDF.
- The final log has no LaTeX errors, undefined references, overfull boxes, or
  underfull boxes.
- All nine pages were rendered and visually inspected.
- `paper.md` was converted from the final TeX and supplied with an explicit
  title and abstract; `paper.txt` was extracted from the final PDF.

The ARR release workflow recompiles `paper.tex` under Ubuntu TeX Live. Its PDF
is independently derived and need not be byte-identical to the inspected
MiKTeX rendering. Release hashes are checked after publication.

## Exact finite checks — pass

The command

    python src/repro/run_all_replays.py

ran twice and regenerated `results.json` byte for byte at SHA-256
`9a6de0530eb18af5c236ef6aba14ff70c589a2e8f0f7b7fb34e9cff2d6b59c82`.
The verifier checks three exact local Macaulay-quotient fixtures, 36 fat-point
and Milnor-floor cases, 22 defect-one formula cases, 60 support/absorption
cases, and exact Euler and initial-Hessian identities for the displayed plane
fixture.

These are finite diagnostics. They do not prove finite contact determinacy,
the incidence arguments, Gauss normalization, the classical
multiplicity–Milnor formula, Saito's criterion, the universal claims, novelty,
or priority.

## Reproducibility label — partial

The replay is deterministic, standard-library-only, and uses exact integers
and `Fraction` arithmetic. The universal algebraic-geometric arguments are not
mechanized and no independent implementation is deposited. The correct label
is therefore `partial`.

## Bibliographic comparison — partial

Primary sources were checked for the jet-incidence description, the
multiplicity–Milnor formula, quasihomogeneity criterion, finite contact
determinacy, Hessian ramification, and related interpolation results. The
author's public corpus and three related ARR records were compared directly.
The search is selective and does not certify novelty or priority.

## Independent Codex referee — not ARR screening

A separate read-only Codex referee audited the exact final source hash. It
reported P0=0, P1=0, no substantive P2, scored the work 8.95/10 with
uncertainty 0.30 on the author's requested scale, and judged it scientifically
ARR-ready after the build and replay checks.

This is an AI audit, not ARR-SCREEN-1.0, human peer review, formal verification,
independent reproduction, or priority certification. ARR screening remains
`not_assessed`.

## Material limitations

- Everything is over the complex numbers; no positive-characteristic extension is asserted.
- The fibre is over one reduced dual point; varying contact loci are not covered.
- The lower length floor is not proved sharp for `s>1`.
- The Fitting equality concerns ramification on the normal source, not a
  canonical branch/discriminant scheme on the nonnormal dual.
- The global degree threshold is sufficient and may be far from minimal.
- No equality classification, exhaustive priority review, human peer review,
  or formal verification is claimed.
- The author is also ARR's founder-editor.

## Licenses

The manuscript and prose are CC-BY-4.0, replay Python is Apache-2.0, and JSON
data and catalogue metadata are CC0-1.0. Declarations are in `metadata.json`,
`LICENSES.json`, and `LICENSES/`.
