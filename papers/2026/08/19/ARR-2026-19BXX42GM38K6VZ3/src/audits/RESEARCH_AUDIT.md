# Research and claim audit

Audit date: 2026-08-24.  This is a conservative provenance and scope record,
not a priority claim.

## What is proved in this draft

1. The escape-or-Gauss-fiber rank alternative and its binomial branch extend
   to algebraically closed fields of arbitrary characteristic.  The new step
   is the Frobenius/radicality replacement for the characteristic-zero
   derivative contradiction.
2. Direct arbitrary-support first-jet blocks give the growing lower bound
   `J(d,m)` without requiring a positive-characteristic extension of the
   cited complex jet-ampleness literature.
3. If the original embedding is the complete `H`-embedding,
   `H=A tensor B`, and both factors separate ordered pairs of distinct
   points, the original Gauss map is injective on closed points.  The paper
   now includes an explicit incomplete-subsystem counterexample showing that
   completeness cannot be omitted.
4. Over the complex numbers, smooth hypersurfaces realize the binomial bound
   exactly inside the exceptional Gauss branch for every `d>=2, m>=3`.

The paper does not claim a classification, an exact global minimum in all
parameters, a positive-characteristic Bertini construction, or exhaustive
priority.

## Public-corpus sweep

A read-only sweep of the public `lluiseriksson` GitHub account found 33 public
repositories: 26 research-labelled repositories, one mathlib fork, and six
non-scientific repositories.  The mathematical corpus also exposed 135
ai.viXra records dated from 2025-12-17 through 2026-08-11 and four versioned
Zenodo deposits.  Two older theses were outside the immediate mathematical
line.  No peer-reviewed external validation of the 2025--2026 mathematical
corpus was located in that sweep.

The closest public antecedents occur in
[`hodge-conjecture-research-front`](https://github.com/lluiseriksson/hodge-conjecture-research-front):

- [B196](https://github.com/lluiseriksson/hodge-conjecture-research-front/blob/main/proofs/B196-lower-degree-tangent-span-absorption.md): annihilator/absorption criterion.
- [B219](https://github.com/lluiseriksson/hodge-conjecture-research-front/blob/main/proofs/B219-arbitrarily-large-special-gauss-fibers.md): large special Gauss fibers and the hypersurface construction.
- [B220](https://github.com/lluiseriksson/hodge-conjecture-research-front/blob/main/proofs/B220-factorized-polarization-has-injective-gauss-map.md): factorized-polarization Gauss injectivity.
- B214 and B215 contain second-jet and mixed interpolation directions that
  are not promoted to theorems here.

The successor manuscript reproves the B219/B220 inputs and labels those
records as authorial antecedents, not independent validation.  Repository
status labels such as `PROVED` are not treated as peer review.

## Reproducibility boundary

The public repository's visible CI checks repository consistency through
`verify_repository.py`; its own description does not make it a proof checker,
and the sweep did not find evidence that it executes the full collection of
roughly 224 replay scripts.  Accordingly, public reproducibility was assessed
as partial rather than complete.

This package improves the boundary by shipping a single exact runner and
machine-readable JSON for every finite fixture used here.  It still does not
mechanize the universal algebraic-geometric arguments or Bertini.

## Primary-literature boundary

- Ballico--Chiantini, *Milan Journal of Mathematics* 89 (2021), Theorem 3.5:
  complex first-jet independence criterion; DOI
  [10.1007/s00032-020-00324-5](https://doi.org/10.1007/s00032-020-00324-5).
- Beltrametti--Di Rocco--Sommese, *Revista Matemática Complutense* 12 (1999),
  Proposition 2.3: tensor-product behavior of jet-ampleness; DOI
  [10.5209/rev_REMA.1999.v12.n1.17182](https://doi.org/10.5209/rev_REMA.1999.v12.n1.17182).
- De Stefani--Grifo--Jeffries, *Journal für die reine und angewandte
  Mathematik* 761 (2020): differential/symbolic-power context over perfect
  fields; DOI
  [10.1515/crelle-2018-0012](https://doi.org/10.1515/crelle-2018-0012).
- Ballico--Brambilla--Santarsiero, arXiv:2603.15103: strong base loci and
  their distinction from Terracini loci.
- Vainsencher, *Journal of Algebraic Geometry* 4 (1995), 503--526, treats
  enumeration of `n`-fold tangent hyperplanes to surfaces in generic settings
  for `1<=n<=6`; [primary preprint](https://arxiv.org/abs/alg-geom/9312012).
- Holweck, *Journal of Algebra* 337 (2011), 369--384, studies bitangent
  components in singular loci of dual varieties; DOI
  [10.1016/j.jalgebra.2011.04.023](https://doi.org/10.1016/j.jalgebra.2011.04.023).

These sources establish context and inputs only to the extent stated in the
manuscript.  This audit does not infer publication priority from a selective
search.
