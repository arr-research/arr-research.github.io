# Verification record for ARR-2026-5XEX8EX0629R997Y v1

Date: 2026-08-25  
Protocol: ARR-VERIFY-1.0

## Source integrity — pass

- Canonical paper.tex: 22,255 bytes; SHA-256
  2db091b3368f51b70f6321f28b47dc87890d5c1c95339cc8b6337b65204f13e1.
- Inspected local paper.pdf: 384,321 bytes; SHA-256
  e683324a12f5d76b9697d179f6193a90eb770c703f37f3f1858c254b26452efa.
- Two MiKTeX-pdfTeX passes produced an eight-page A4 PDF.
- The final log has no LaTeX errors, undefined references, or overfull boxes.
  It has two underfull boxes in one bibliography entry.
- All eight pages were rendered at 150 dpi and visually inspected.
- paper.md and paper.txt were extracted from the final PDF with an explicit
  warning that mathematical typography may be degraded.

The ARR release workflow recompiles paper.tex under Ubuntu TeX Live. Its PDF
is independently derived and need not be byte-identical to the inspected
MiKTeX rendering. Release hashes are checked after publication.

## Exact finite checks — pass

The command

    python src/repro/run_all_replays.py

completed successfully under CPython 3.12.6 and regenerated results.json at
SHA-256
3fd064e33deee50d1649e6ef2db6cef4d1c12b17040231c797140452308a0213.

The replay checks:

- exact integer optimization and inequalities for 1 <= d <= 8 and
  1 <= s <= 20;
- exact SymPy Gröbner bases over QQ for the sharp plane family
  1 <= s <= 12;
- explicitly listed local quotient fixtures over two large prime fields.

The exploratory script records that a naive higher-dimensional monomial
defect product fails and is not a theorem of the paper.

These are finite diagnostics. They do not prove the universal local theorem,
finite contact determinacy, the global incidence argument, Gauss-fibre
identification, novelty, or priority.

## Reproducibility label — partial

The integer and Gröbner checks are deterministic and deposited with their
outputs. The modular fixtures are finite cross-checks. The universal
algebraic-geometric arguments are not mechanized, and no independent
implementation is deposited. The correct label is therefore partial.

## Bibliographic comparison — partial

Primary records checked include Briançon–Granger–Maisonobe (1988),
Canino–Gimigliano–Idà (published 2025 and arXiv v2), Greuel–Lossen–Shustin
(2007), Liu (2018), and Almirón (2022), together with the three related ARR
records. A recent Ma–Zuo preprint was noted but not used as an ingredient.

The exact plane value is attributed as classical in the ordinary
multiple-point class. No source was found in the focused search for the same
universal statement over arbitrary isolated plane germs, but the search is
not exhaustive and does not certify priority.

## Separate Codex referee — not ARR screening

A separate read-only Codex referee audited the final source hash shown above.
It found no P0, P1, or P2 issue and judged the version ARR-ready. Its preceding
full audit scored the work 8.70/10 with uncertainty 0.45 on the author's
requested scale, where 10 denotes an unconditional correct solution of a
Millennium Prize problem.

This is an AI-assisted audit, not ARR-SCREEN-1.0, human peer review, formal
verification, independent reproduction, or priority certification. ARR
screening remains not_assessed.

## Material limitations

- Everything is over the complex numbers; no positive-characteristic theorem
  is asserted.
- The higher-dimensional optimized floor is not proved sharp.
- Exact global equality is proved only for surfaces.
- The explicit global degree threshold is sufficient and may be far from
  minimal.
- No equality classification in higher dimension, exhaustive priority
  review, human peer review, or formal verification is claimed.
- The author is also ARR's founder-editor.

## Licenses

The manuscript and prose are CC-BY-4.0, replay Python is Apache-2.0, and JSON
data and catalogue metadata are CC0-1.0. Declarations are synchronized in
metadata.json, LICENSES.json, and LICENSES/.
