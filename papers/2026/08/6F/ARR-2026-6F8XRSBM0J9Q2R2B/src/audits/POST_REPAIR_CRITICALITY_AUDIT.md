# Post-repair criticality and proof audit

**Date:** 2026-08-15  
**Status:** mathematical GO after the criticality repair; global optimization
and the associated all-distortion RDF remain outside scope.

## 1. Defect in the original version

The original proof inferred that the orbit-tangent Hessian vanished merely
because the invariant potential was constant on the orbit.  This is false at
a noncritical point: a normal gradient couples to the second fundamental
form.  The orbit

`(a S^1) x (b S^1) subset S^3`, `a != b`,

under `SO(2) x SO(2)` has a one-dimensional irreducible but trivial normal
representation.  For the exponential orbital potential its normal
derivative is nonzero; at `a^2=3/4`, `b^2=1/4`, `t=1` the replay obtains
`-0.09823040855859072`.  Thus the original theorem was false as written.

## 2. Corrected universal theorem

The revised manuscript separates three statements.

1. The squared-harmonic coefficient and strict negative spherical-Laplacian
   identity require no criticality assumption and remain unchanged.
2. Invariance gives
   `grad_S U(v) in (N_v O)^{G_v}`.  Hence a zero fixed-vector space is a
   sufficient criticality criterion.
3. At a critical orbit, differentiating `dU(X#)=0` gives
   `Hess(U)(Z,X#)=0` for arbitrary `Z`; tangent and mixed entries therefore
   vanish.  Only at this stage may the Laplacian be identified with the trace
   of the normal Hessian.  Schur equivariance and the stated transitive
   block symmetry then make that normal Hessian a common scalar, whose strict
   negativity follows from the Laplacian identity.

The additional symmetry in the reducible case is now explicitly required to
fix the source point and preserve the potential while permuting the normal
summands.

## 3. Half-Grassmann application

At the balanced projector, the spherical normal is the direct sum of the two
block-diagonal traceless self-adjoint modules.  A vector fixed by the block
stabilizer is scalar on each block; tracelessness forces both scalars to zero.
Therefore `(N_v O)^{G_v}={0}` over the real, complex, and quaternionic
families.  Criticality follows from the new guard.  The isometry
`A -> -W A W*` fixes the balanced point, preserves the potential by
conjugation invariance plus antipodality, and exchanges the two normal
modules.  The repaired universal theorem therefore proves the balanced
no-spinodal result without assuming criticality.

## 4. Independent components rechecked

- The harmonic setup now states `N>=3`, the domain on which the displayed
  normalized Gegenbauer formula is literal; the unused circle case is
  explicitly separated as a Fourier/Chebyshev analogue.
- A new two-block criticality lemma proves that the tilted posterior mean is
  block-scalar under `U(k) x U(m)`, so its traceless part is radial along
  `A_k`.  This supplies first-order stationarity before the operators in
  equation (6.6) are called constrained-Hessian eigenvalues.
- The Jacobi generator identities are independent of the repaired universal
  argument.
- The two constrained-Hessian operators and the `k=2r/3` weak-field threshold
  are unchanged.
- The absent `k=1` module, the fourth-order boundary sign, and the Stein tail
  reduction remain symbolically verified.
- The replay now includes the torus counterexample so a future regression
  cannot silently remove the criticality guard.

## 5. Residual claim boundary

The corrected paper proves local Morse--Bott rigidity and exact two-block
metastability.  It does not prove global balanced optimality, rule out
separated coexistence, classify every external spectrum, or derive the full
projector rate--distortion function.  Those omissions are explicit in the
abstract, scope section, and ARR metadata.
