# Verification record for ARR-2026-19BXX42GM38K6VZ3 v1

Date: 2026-08-24

Protocol: ARR-VERIFY-1.0

## Source integrity - pass

- Canonical paper.tex: 32,904 bytes; SHA-256
  1e8986b9a754ffb9f0ccaf500ed2c271790cf7caf4d989ca1b37cd91054f5c95.
- Rendered paper.pdf: 420,380 bytes; SHA-256
  ba43d293b0153dff84e76866d54a1e2a6c9a5afbdc260d1c064ee3261d21bf20.
- Three pdfLaTeX passes produced a 10-page A4 PDF.
- The final log contains no LaTeX or package warnings, undefined references,
  overfull or underfull boxes, errors, emergency stops, or fatal errors.
- All ten pages were rendered at 150 dpi and visually inspected for clipping,
  overlap, missing glyphs, unreadable mathematics, broken links, and layout
  defects.
- paper.md and paper.txt were regenerated from this exact PDF.

The ARR release workflow recompiles paper.tex under Ubuntu TeX Live before
packaging. Its released PDF is therefore a separately derived artifact and
need not be byte-identical to the inspected MiKTeX rendering recorded above.
After publication, the release manifest and an independently downloaded
release-PDF hash must be reported separately; neither may be substituted for
the canonical paper.tex hash.

## Exact finite fixtures - pass

The deposited standard-library Python runner was rerun:

    python src/repro/run_all_replays.py
    python src/repro/verify_successor_fixtures.py --json

All six fixtures passed:

1. Cubic simplex lattice in P2: value rank 10 and value-plus-first-jets rank 10.
2. Cubic simplex lattice in P3: value rank 20 and value-plus-first-jets rank 20.
3. Three prescribed triple jets in P2, degree 9: rank 18 of 18.
4. Four sampled quadratic-Veronese tangent spaces: each tangent rank 3 and
   every pairwise union rank 5.
5. The displayed incomplete O(5) subsystem: both endpoint tangents have rank
   2 and coincide.
6. Frobenius zero-derivative sanity checks in characteristics 2, 3, and 5.

The scripts use exact rational Gaussian elimination and exact reduction of
finite-field coefficients. They certify only the displayed finite matrices.

## ARR reproducibility label - partial

The exact fixtures and deterministic JSON outputs were rerun. They do not
mechanize the universal algebraic-geometric arguments, radicality/Frobenius
proof, Gauss-map theorem, Bertini step, global smoothness, or a classification.
No independent implementation was supplied. The label is therefore partial.

## Bibliography - partial

The deposit audit checked the cited primary sources and DOI/arXiv identifiers
selectively, including Ballico-Chiantini, Beltrametti-Di Rocco-Sommese,
De Stefani-Grifo-Jeffries, Vainsencher, Holweck, and the related ARR record.
The search was not exhaustive and does not certify novelty or priority.

## External Codex referee - not ARR protocol screening

A separate Codex referee performed an adversarial mathematical review of this
paper, reported no invalidating gap or P0 defect, and assigned
6.8/10 with uncertainty plus or minus 0.7 on the author's scale. The report is
preserved at src/audits/REFEREE_REPORT.md. This is not ARR-SCREEN-1.0, human
peer review, formal verification, independent reproduction, or priority
certification. ARR screening remains not assessed.

## Material limitations

- The main rank bounds assume an algebraically closed field and nonempty
  finite reduced supports.
- The smooth hypersurface equality construction is only claimed over the
  complex numbers and is existential.
- No positive-characteristic Bertini realization or equality classification
  is claimed.
- The related ARR record proves a sharper exact global binomial floor in
  characteristic zero; this paper does not supersede that result.
- The author and ARR founder-editor are the same person.

## Licenses

The author explicitly delegated the license choice for this publication.
ARR applies CC-BY-4.0 to the manuscript, Apache-2.0 to the Python replay code,
and CC0-1.0 to JSON fixture data and catalogue metadata. The declarations are
scoped in metadata.json and LICENSES.json and the complete texts are preserved
under LICENSES/.
