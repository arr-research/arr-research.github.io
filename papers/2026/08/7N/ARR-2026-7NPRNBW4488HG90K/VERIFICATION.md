# Verification record for ARR-2026-7NPRNBW4488HG90K v1

Date: 2026-08-30

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 341,892 bytes; SHA-256
  `0f45a998063e687cc689b8e43c2887194c0937c8587c34b783a1631f8974776d`.
- The final LaTeX and BibTeX logs contain no warning, overfull or underfull
  box, missing-character, unresolved-reference, or unresolved-citation marker.
- Poppler rendered all nine pages, and every page was visually inspected at
  high detail. Equations, theorem boxes, references, links, margins, and page
  breaks are legible and complete, with no clipping or overlap.
- `paper.md` and `paper.txt` were extracted mechanically from the exact
  canonical PDF and are machine-reading renditions, not substitutes for its
  typography.

## Exact-arithmetic replay — pass within declared scope

The frozen source package and a clean extracted copy both passed:

```text
python -m pip install -r src/repro/requirements.txt
python src/repro/run_replay.py
```

Observed checks include 160 exact balanced quadrilateral and flux identities,
the corrected shear/Gram-determinant lower certificate, an exact noncommuting
counterexample to the discarded preliminary inequality, 15 one-spike,
reflected, and zero-padded constructors, and exact symbolic singular-spectrum,
stability, triangle, and square checks. The two output hashes are:

```text
7095534026866159b37de40e2055b30ca9e765401a38f3fca4809bac2bf3d9cd  src/repro/results/four_kick_gram.json
b455b13c193dfbe101bf53632da046ff08575d507b7c104286470f9af0c35b5a  src/repro/results/symbolic_constructors.json
```

These finite computations audit algebra and indexing. They do not prove the
arbitrary-dimensional theorem or formalize Horn's theorem.

## Proof and literature audits

The retained mathematical audit reports no unresolved P0/P1 issue after the
four-kick lower proof was repaired with the valid Gram-area argument. The final
recheck also covers strict Schur concavity and the exact switching ratio. The
priority audit distinguishes classical weighted shifts, Horn feasibility,
polygonal isoperimetry, earlier low-dimensional author records, the prior
sign-paired equality face, and the complementary rank-adaptive ARR paper.

Bibliography is labelled **partial**: directly adjacent sources and author
self-overlap were checked, but exhaustive priority is neither possible nor
claimed.

## ARR labels and limitations

- Bibliography: **partial**.
- Reproducibility: **partial** despite the clean exact replays, because the
  analytic proof and imported Horn theorem are not formalized.
- Lean 4: **not applicable**.
- Scientific scope: finite-dimensional complex matrices with the unnormalized
  Hilbert--Schmidt norm. No general formula for spectra with both sign
  multiplicities above one, classification of all optimizing matrices or
  loops, infinite-dimensional theorem, operator-norm result, or five-kick law
  is claimed.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a
technically valid founder-owned publication, not independent editorial or
scientific certification.
