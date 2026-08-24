# Release notes — version 0.6

## Status

Major mathematical rewrite of versions 0.1–0.4. This version is a research
paper, not a technical note. It has not received human peer review or a
priority certification.

## Main changes

- Replaces the former `(d+1)^2` baseline by the exact universal floor
  `binom(d+m,d)` for every `d,m >= 1`.
- Proves the result through a finite projection adapted to the finite support
  and the characteristic-zero fattening gap
  `alpha(I^(2)) >= alpha(I)+1`.
- Supplies proper-span equality examples in every dimension and degree using
  simplex-lattice interpolation and smooth common-tangent hypersurfaces.
- Proves that tangent absorption descends from `L^m` to every `L^k`,
  `1 <= k <= m`.
- Retains the squared-hyperplane and Gauss-fibre arguments only as secondary,
  rank-sensitive refinements for `m >= 3`.
- Adds two standard-library exact-arithmetic replays and explicit scope limits.
- Corrects and narrows literature and novelty statements.

## Mathematical boundary

The theorem assumes a smooth projective integral variety over an
algebraically closed field of characteristic zero and a nonempty finite
reduced support. No positive-characteristic, singular, nonreduced, mixed-
dimensional, or equality-classification claim is made.

## Reproducibility

Primary commands:

```powershell
python repro/verify_exact_projection_floor.py
python repro/verify_common_tangent_extremizer.py
```

Both scripts use exact `fractions.Fraction` elimination and require no
third-party Python package.

## External Codex audit

A separate read-only Codex task re-audited version 0.6 from scratch. It found
no fatal mathematical error and scored the manuscript `6.60/10.00` with
uncertainty interval `[5.65, 7.40]` on the requested scale where `10.00` is a
correct unconditional Millennium-problem solution. Component scores included
`9.20` for apparent correctness, `8.55` for rigor, and `8.85` for generality.
Its verdict was “publish after mandatory minor revision.” All identified
minor proof-exposition and bibliography changes were applied before the final
build. This remains an AI audit, not human peer review, formal certification,
or priority validation.
