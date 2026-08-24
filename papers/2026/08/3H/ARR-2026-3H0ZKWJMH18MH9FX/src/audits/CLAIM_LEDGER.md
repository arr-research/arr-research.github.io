# Claim ledger

## Safe exact claims

1. Johnston--Lovitz--Russo--Sikora's learning-width/factor-width criterion is
   equivalent to identity membership in the realization-sensitive
   annihilator projector cone (AC).  The general criterion is prior art; the
   physical-space translation is used here.
2. Whenever perfect decoding is possible, a perfect decoder exists with at
   most `r^2` outcomes.  This is a standard conic-Caratheodory/factor-width-rank
   consequence and is not a novelty claim.  For the finite Hodge POVM, the
   manuscript gives an explicit nullspace-elimination algorithm attaining the
   bound; this is an implementation of the standard conic reduction.
3. Every `N`-ray full-spark ensemble in `C^r` admitting strictly positive
   tight representatives has exact perfect-list threshold `N-r+1`.
4. The Hodge duals of all `(r-1)`-fold weighted frame wedges give an explicit
   POVM. Unit-norm tight frames are a special case, not a required hypothesis.
5. The fixed flat consecutive-support rank-`r` probe for the complete
   `d`-dimensional Weyl ensemble has exact perfect-list threshold `d-r+1`.
   An arithmetic-support probe with the same rank has threshold `d/r` when
   `r` divides `d`, proving that support pattern matters.
6. When `r|d`, optimization over all pure Schmidt-rank-`r` probes is exact:
   `min_probe ell_min = d/r`.  The converse is the support-dimension bound
   `1 <= ell*D/d^2 <= ell*r/d`.
7. The support-matroid and summed-projector obstructions are strictly
   insufficient on an infinite subfamily.
8. For arbitrary nonnegative priors and density operators,
   `P_err >= r gamma_ell`, where `gamma_ell` is the minimum smallest
   eigenvalue of the omitted-prior operators.  For full-spark pure states
   with every prior positive it is positive below threshold and stable under
   the stated operator-norm perturbation budget.  This is a simple scalar
   dual witness derived here, not a claim of a new quantum-decision principle.
9. For the consecutive-support rank-two Weyl probe, the entire one-shot list
   curve is exact:
   `P_succ^*=[ell+sin(pi ell/d)/sin(pi/d)]/d` for `1<=ell<=d`.

## Forbidden strengthenings

1. Do not state the threshold for arbitrary full-spark frames: strict
   scalability is necessary for the construction and a three-state
   counterexample is given.
2. Do not state the threshold for arbitrary tight frames: duplicates lower
   it.
3. Do not claim the global Weyl optimum for `r` not dividing `d`, or for
   adaptive/multiuse testers.
4. Do not claim a complete sub-threshold success curve outside the specified
   consecutive-support rank-two Weyl family, or claim that the general
   spectral floor is always attained.
5. Do not claim exterior powers of tight frames, full-spark harmonic frames,
   quantum state exclusion, or Weyl dense coding as new ingredients.
6. Do not claim the general list-feasibility, learning-width, or factor-width
   criterion as new; arXiv:2510.20789 is the direct prior source.
7. The `r^2` outcome compression uses the weak exclusion convention, allowing
   zero effects and unused lists; do not promote it to strong exclusion or
   advertise the Caratheodory bound as new.
8. Do not claim robustness of zero error itself: the perturbation theorem is
   a quantitative lower bound on unavoidable error.
