# Verification record for ARR-2026-66Q8M61AA196T8BC v1

Date: 2026-08-24  
Protocol: ARR-VERIFY-1.0

## Source integrity — pass

- Canonical `paper.tex`: 19,216 bytes; SHA-256
  `e4b06da72f88a333e461fbd202ace9678be6b39d25f1989fba982f794de29ed1`.
- Rendered `paper.pdf`: 380,200 bytes; SHA-256
  `b7e0a8d83fd067c769903ac8432df5f6c09ef4e0d837d52cdb03b75a79cf76cc`.
- Three pdfLaTeX passes produced a seven-page A4 PDF.
- The final log contains no LaTeX or package warnings, undefined references,
  overfull/underfull boxes, errors, emergency stops, or fatal errors.
- All seven pages were rendered at 130 dpi and visually inspected for
  clipping, overlap, missing glyphs, unreadable mathematics, and layout
  defects.
- `paper.md` and `paper.txt` were regenerated from this exact PDF.

The ARR release workflow recompiles `paper.tex` under Ubuntu TeX Live before
packaging. Its released PDF is independently derived and need not be
byte-identical to the inspected MiKTeX rendering recorded above. The release
manifest and downloaded release-PDF hash are verified after publication.

## Exact finite checks — pass

The deposited standard-library Python runner was rerun:

    python src/repro/run_all_replays.py

It passed four rational-normal-curve value/Hasse-jet fixtures, two top-order
simplex-lattice fixtures, 250 exhaustive finite packing cases, the first-order
formula comparison in the configured range, and configured monotonicity
checks. The saved `src/repro/results.json` exactly matches fresh output.

The scripts use exact integer and rational arithmetic. They certify only the
displayed finite matrices and identities. In the full-rank fixtures, the
value rows already span the complete target, so appending jet rows is a
consistency check rather than additional evidence for absorption.

## ARR reproducibility label — partial

The exact fixtures and deterministic JSON output were rerun. They do not
mechanize the universal algebraic-geometric argument, validate arbitrary
characteristic, classify equality, or establish novelty. No independent
implementation was supplied. The label is therefore partial.

## Bibliography — partial

Primary sources were checked selectively. In particular, the definition of
jet ampleness and the tensor rule used in the corollary were verified against
Beltrametti–Di Rocco–Sommese (1999), Proposition 2.3. The
Mallavibarrena–Piene (2024) journal record and DOI were checked, and the other
osculating/secant references were used only as context. The search was not
exhaustive and does not certify novelty or priority.

## External Codex referee — not ARR protocol screening

A separate Codex referee performed an adversarial review independently of the
authoring audit. The initial assessment found no P0 defect and scored the work
6.4/10 plus or minus 0.9. After the citation-dependent combined corollary was
replaced by a self-contained jet-ample variant and four formal issues were
repaired, focused re-review found no P0 or internal-correctness P1 issue and
raised the score to 7.2/10 plus or minus 0.8. The report is preserved at
`src/audits/REFEREE_REPORT.md`.

This is not ARR-SCREEN-1.0, human peer review, formal verification,
independent reproduction, or priority certification. ARR screening remains
`not_assessed`.

## Material limitations

- The theorem assumes a smooth projective integral positive-dimensional
  variety over an algebraically closed field and nonempty finite reduced
  supports.
- The complete `H^m` system is essential to the elementary separator proof;
  the general corollary instead assumes full `M`-jet ampleness.
- No formula for `s>m` is asserted in the power case.
- No nontrivial sharpness example or equality classification is supplied for
  `d>=2` and `s<m`.
- Literature comparison is selective and no exhaustive priority claim is
  made.
- The author and ARR founder-editor are the same person.

## Licenses

The author explicitly delegated the license choice. ARR applies CC-BY-4.0 to
the manuscript, Apache-2.0 to the Python replay code, and CC0-1.0 to JSON
fixture data and catalogue metadata. Declarations are scoped in
`metadata.json` and `LICENSES.json`; complete texts are under `LICENSES/`.
