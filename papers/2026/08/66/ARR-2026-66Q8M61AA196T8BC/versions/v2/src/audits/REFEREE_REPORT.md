# Independent Codex referee report — version 2

Date: 2026-08-24

Role: independent adversarial Codex referee

Exact source SHA-256:
`17810cc2c07029b913b50665bf72fa569762670cc836900bc3cbfa1bfea0a414`

Human peer review: **no**

## Verdict

- P0: **none**.
- Mathematical P1: **none residual**.
- Score: **7.9/10 with uncertainty ±0.4** on the scale where 10.0 denotes an
  unconditional correct solution of a Millennium Prize Problem.
- Verdict: **scientifically publishable**, subject to separate compilation and
  replay verification.

| Dimension | Score |
|---|---:|
| Correctness | 9.0 |
| Depth | 7.5 |
| Verifiable novelty | 6.7 |
| Applications | 5.8 |
| Reproducibility declared | 7.0 |
| External validation | 3.5 |

The numerical assessment is an AI evaluation, not certification.

## Mathematical reconstruction

The exact floor follows because order-`s` osculating absorption contains
tangent absorption, to which the cited exact arbitrary-characteristic theorem
applies with matching quantifiers.

The rank-sensitive proof correctly selects a degree-one evaluation basis,
uses `e^(s+1)` to kill preceding order-`s` neighbourhoods, and uses
`m-s-1 >= s` to generate every new jet. The resulting direct sum has dimension
`binom(d+s,d) r_1(Z)`. On `P^1`, `m+1` full-span points show that the formula
fails throughout `m<=2s`, establishing sharpness of the uniform threshold.

For proper-span equality, the characteristic-free evaluation-basis argument
supplies distinct unisolvent supports. Both singularity incidences have one
more condition than the dimension of their moving point. Their image closures
are therefore proper. The three geometric strata cover all possible singular
points; connectedness plus smoothness proves integralness. The ambient lift of
the tangential equation lies in the required maximal-ideal power, so the
normal coordinate has order at least `s+1` on the hypersurface. Finally, the
degree-`m` restriction isomorphism and unisolvence give the kernel equality,
exact rank, and properness of the span.

Boundary cases `d=1,m=s=1`, `s=m`, `m=2s`, and characteristics dividing `m!`
were checked in the proof audit; no counterexample was found.

## Closed findings

The first exact-source audit requested two formal repairs:

1. use the closure of the second incidence image before applying its dimension
   bound;
2. state explicitly that the lift independent of the normal coordinate lies
   in the ambient maximal-ideal power before passing to the hypersurface.

Both are closed. Two final P2 wording suggestions were also incorporated:
“contributions of this revision” replaces potentially absolute novelty
language, and very ampleness is invoked explicitly to separate the selected
evaluation supports. Focused re-check of the final hash found no newly
introduced P0/P1 and no missing static citation.

## Scientific reservations

The exact floor is invoked from a separate ARR paper by the same author, so it
is not independent external validation. Literature comparison correctly
recognizes Ballico's `X`-rank language and uses primary jet/osculating sources,
but remains selective and cannot certify priority. Minimal hypersurface degree,
equality classification, and optimal sub-threshold rank refinements remain
open.

This report audits the manuscript only. Artifact compilation and replay
results are recorded separately in `VERIFICATION.md` and `QA_RESULTS.json`.
