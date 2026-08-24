# Verification record for ARR-2026-2MHNZRRJP49Y9SWP v1

Date: 2026-08-24

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical `paper.tex`: 28,796 bytes; SHA-256
  `bdf18f2ca24b31b71259436e441f10ed90a013588df38a40af08a954e8f28b28`.
- Rendered `paper.pdf`: 417,151 bytes; SHA-256
  `235bf613b5f3a1f9f7a81a6d4d0f0f027cadc7564d37f77643edfbd8a8cae7cd`.
- PDF inspection found 9 A4 pages. The three-pass MiKTeX log contains no
  LaTeX warnings, undefined references, or overfull/underfull boxes.
- All 9 pages were rendered to PNG and visually inspected for cropping,
  overlap, missing glyphs, unreadable mathematics, and broken layout.
- `paper.md` and `paper.txt` were mechanically extracted from this exact PDF.
- The historical root log was excluded. The clean final log was inspected and
  is preserved in the immutable release bundle rather than the Git source
  tree.

## Exact replay — pass

The following commands were rerun on the deposited pure Python sources:

```text
python src/repro/verify_exact_projection_floor.py
python src/repro/verify_common_tangent_extremizer.py
```

Both use standard-library `fractions.Fraction` Gaussian elimination.

- Projection-floor replay: 20/20 fixtures passed, covering `1 <= d <= 4`,
  `1 <= m <= 5`, up to `binom(d+m,d)=126`, plus deleted-node falsification
  boundaries.
- Common-tangent local replay: 6/6 fixtures passed, checking equal value and
  double-point ranks and the local second-order normal-coordinate mechanism.

## ARR reproducibility label — partial

ARR reran the supplied exact fixtures and checked their deterministic JSON
outputs. The scripts are diagnostic witnesses, not the universal proof. No
independent implementation, global computational smoothness certificate,
or full equality-classification computation was supplied. The public label is
therefore `partial`, not `pass`.

## External Codex audit — not protocol screening

A separate read-only Codex task audited the v0.6 proof from scratch. It found
no fatal error and recommended publication after minor revisions. After those
revisions it rechecked the source, final PDF, and clean build log and confirmed
that no new defect prevented publication. This evidence is preserved in
`src/repro/EXTERNAL_CODEX_AUDIT.md`, but it is not `ARR-SCREEN-1.0`, human peer
review, formal verification, or priority certification.

## Not assessed and limitations

- Bibliographic integrity under an ARR protocol: **not assessed**.
- Frontier-model screening under `ARR-SCREEN-1.0`: **not assessed**.
- Lean 4: **not applicable**; no formalization was supplied.
- Human peer review, independent reproduction, novelty, and publication
  priority: **not assessed**.
- The theorem is restricted to smooth projective integral varieties over
  characteristic zero and nonempty finite reduced supports.
- The Bertini construction proves existence; the replay checks local algebra
  and does not certify global smoothness of a particular explicit member.

## Conflict disclosure

The author and ARR founder-editor are the same person. No independent
editorial or scientific certification is claimed.
