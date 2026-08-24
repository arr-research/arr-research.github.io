# Scientific response and major-revision record

Date: 2026-08-24
Exact source reviewed: `paper.tex`, SHA-256
`17810cc2c07029b913b50665bf72fa569762670cc836900bc3cbfa1bfea0a414`

Version 2 is a major scientific revision, not a cosmetic republication of
version 1.

## Corrections to the hierarchy

1. The valid version-1 mixed-jet floor is no longer presented as the best
   tensor-power bound. Higher-order absorption contains tangent absorption,
   and ARR-2026-2MHNZRRJP49Y9SWP v3 supplies the exact floor
   `binom(d+m,d)` in arbitrary characteristic.
2. The old mixed certificate remains, with its proof and jet-ample extension,
   but the manuscript proves it is strictly weaker when `d >= 2` and `s < m`.
3. A new block-extension lemma proves the independent rank term
   `binom(d+s,d) r_1(Z)` for `m >= 2s+1`. A rational-normal-curve fixture
   proves that this threshold cannot be lowered in a uniform statement with
   the same term.

## New proper-span equality construction

1. The integer simplex lattice was replaced by a characteristic-free choice
   of an evaluation basis in `P^d`; this avoids collision and
   falling-factorial degeneration modulo small primes.
2. The fat-point ideal on the hyperplane is explicitly the intersection of
   the local powers, not an unqualified ordinary homogeneous-ideal power.
3. Two local-jet incidence calculations construct a hypersurface smooth first
   along the hyperplane away from the supports and then on its complement.
   The proof uses closures of the incidence images before invoking dimension.
4. Smoothness at the supports, connectedness, and therefore integralness are
   proved separately. The lift of the tangential equation is explicitly
   placed in the ambient maximal-ideal power before passing to the local ring
   of the hypersurface.
5. The restriction isomorphism in degree `m` and unisolvence force every
   degree-`m` section vanishing on the supports to be divisible by the normal
   coordinate. Its prescribed order gives higher-osculating absorption and a
   proper point span of exact dimension `binom(d+m,d)`.

## Scope and priority repairs

- Principal-parts evaluations replace ordinary derivatives and factorials.
- Ballico's established `X`-rank of linear subspaces is identified as the
  direct prior language; the manuscript does not claim to introduce subspace
  rank or point-span absorption.
- Jet-ampleness and osculating/secant literature are compared selectively.
  No exhaustive priority or novelty certification is claimed.
- The sufficient hypersurface degree is not claimed minimal, and no equality
  classification or canonical extremizing equation is claimed.

## Reproducibility changes

The replay now includes exact rational higher-block matrices, modular
unisolvent evaluation fixtures, local higher-contact substitutions in small
characteristics, exhaustive finite packing checks, and the full curve
threshold boundary through `s=8`. The runner compares freshly generated JSON
with the committed file byte for byte using canonical LF newlines. The replay
certifies only those finite fixtures; it is not a proof checker.

## Closed referee findings

The initial exact-source audit requested two formal P1 repairs: use the closure
of the second incidence image and make the ambient-to-hypersurface maximal
ideal passage explicit. Both are present in the hash above. Focused re-review
found no remaining P0 or mathematical P1 issue. This remains an AI audit, not
human peer review.
