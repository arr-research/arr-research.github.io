# Exact Rank Transitions through p=32 and a Half-Integral Optimum at p=53

Lluis Eriksson — 2 September 2026

## Abstract

For the traceless Hermitian target
`F_(p,q)=diag(q repeated p times, -p repeated q times)`, let `kappa(F)` be
one half of the least squared Hilbert--Schmidt norm of a factor `C` satisfying
`CC* - C*C = 2F`, and let `r_*(F)` be the least rank among minimizers. On
`q=2p+1`, this paper certifies the complete finite frontier for `4<=p<=32`.
The minimum-rank excess `r_*-q` equals 0 on `4<=p<=7`, 1 on `8<=p<=14`,
2 on `15<=p<=26`, 3 at `p=27`, and 4 on `28<=p<=32`. Thus `p=27` and
`p=28` are consecutive exact rank transitions. Writing
`M_p=kappa(F_(p,2p+1))-(3p^2+2p)`, the exact data prove `M_p=6p-30` on
`15<=p<=28` and `M_p=7p-58` on `29<=p<=32`, so the cost slope changes at
`p=29`. Separately, `kappa(F_(53,107))=8847` and `r_*=115`; the optimum is
half-integral, while an earlier integer candidate of trace 8843 is refuted by
an integral Farkas certificate.

## Exact finite phase diagram

For every displayed row, an exact rational primal hive attains the cost, an
unrestricted dual matches it, and a strict predecessor-rank dual proves the
least attaining rank.

| p range | exact rank excess `r_*-q` |
|---|---:|
| 4–7 | 0 |
| 8–14 | 1 |
| 15–26 | 2 |
| 27 | 3 |
| 28–32 | 4 |

The newly closed cases are:

| p | q | kappa | r_* | predecessor-face value |
|---:|---:|---:|---:|---:|
| 21 | 43 | 1461 | 45 | 1462 |
| 22 | 45 | 1598 | 47 | 1599 |
| 23 | 47 | 1741 | 49 | 1742 |
| 24 | 49 | 1890 | 51 | 1891 |
| 25 | 51 | 2045 | 53 | 2047 |
| 26 | 53 | 2206 | 55 | 2209 |
| 27 | 55 | 2373 | 58 | 2374 |
| 28 | 57 | 2546 | 61 | 2547 |
| 29 | 59 | 2726 | 63 | 2727 |
| 30 | 61 | 2912 | 65 | 2913 |
| 31 | 63 | 3104 | 67 | 3105 |
| 32 | 65 | 3302 | 69 | 3303 |

## The p=53 theorem

For `F_(53,107)`, an exact rational hive with denominator at most two gives
trace 8847 and rank 115. An unrestricted exact dual has value 8847; a second
dual on the rank-at-most-114 face has value 8848. A separate 636-row integral
Farkas combination refutes the former integer rank-115 candidate of trace
8843. The denominator-two primal and matching dual identify the same exposed
projected hive face, so half-integrality is not a floating-point artifact.

## Reproducibility

The frozen replay uses Python standard-library `Fraction` arithmetic. The
primary verifier checks every case `21<=p<=32`; an independently implemented
row and index reconstruction checks the p=53 theorem; and a separate replay
checks the Farkas contradiction. Optimized Python is refused. The preserved
release ZIP is deterministic and has SHA-256
`a241d2a82059cdfbd922cd5808ed339ab6d549385150fa7efb7f396a7e9478c9`.

## Scope and limitations

The results are finite and conditional on the classical Horn--Klyachko/hive
theorem. No all-parameter recurrence, classification of all minimizers,
proof-assistant formalization, exhaustive priority search, or independent
peer review is claimed.

The exact PDF is the canonical rendered manuscript. The Python builder in
`src/manuscript/` is the source of truth, and `paper.txt` is the complete text
extraction.
