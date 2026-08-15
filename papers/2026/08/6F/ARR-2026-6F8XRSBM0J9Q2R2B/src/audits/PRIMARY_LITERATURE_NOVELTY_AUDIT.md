# Paper 15 primary-literature and novelty audit

**Date:** 2026-08-15  
**Candidate:** *All-Field Morse--Bott Stability of Homogeneous Orbital
Potentials: Half-Grassmann No-Spinodal Rigidity and Exact Jacobi
Metastability*  
**Verdict:** provisional **GO after hostile proof and release QA**.

## 1. Exact claim searched

The claim is not that positive-definite kernels, orbital integrals,
matrix-Bingham normalizers, Jacobi ensembles, or Morse--Bott theory are new.
The searched conjunction was:

1. an invariant measure on a proper antipodal orthogonal orbit embedded in an
   ambient sphere;
2. an analytic positive-definite zonal kernel evaluated with its external
   center at a point of the same orbit;
3. conversion of squared orbital harmonic coefficients into an all-field
   negative ambient spherical Laplacian;
4. conversion, under an isotropy representation hypothesis, into strict
   transverse Morse--Bott maximality;
5. application to the balanced real/complex/quaternionic half-Grassmann
   matrix-Bingham branches; and
6. an exact Jacobi-generator classification of weak-field complex two-block
   metastability at the threshold `k=2r/3`.

No primary source located in targeted title/abstract/full-text searches states
this conjunction or the half-Grassmann conclusions.

## 2. Primary prior art and ownership boundary

- Schoenberg (1942), DOI `10.1215/S0012-7094-42-00908-6`, owns the
  nonnegative Gegenbauer expansion for positive-definite spherical kernels.
- Gangolli (1967), *Ann. IHP B* 3(2), 121--226, owns broad positive-definite
  kernel theory on homogeneous spaces.
- Damelin--Levesley--Ragozin--Sun (2009), DOI
  `10.1016/j.jco.2008.09.001`, use group-invariant kernels and energies for
  quadrature/discrepancy on compact homogeneous manifolds. Their variable is
  a measure or point set on the manifold, not an ambient external direction,
  and they do not state the transverse Hessian/no-spinodal theorem.
- James (1964), DOI `10.1214/aoms/1177703550`, and Muirhead (1982), DOI
  `10.1002/9780470316559`, own matrix-variate beta and hypergeometric
  infrastructure.
- Forrester--Kumar (2022), DOI `10.1016/j.physd.2022.133220`, study the
  beta-Jacobi trace distribution and differential recurrences. They do not
  derive the fixed-Frobenius two-block Hessian operators or the threshold
  `k=2r/3`.
- Kent (1994), DOI `10.1111/j.2517-6161.1994.tb01978.x`, Bagyan--Richards
  (2024), DOI `10.3842/SIGMA.2024.094`, and Cazzella et al. (AISTATS 2026)
  occupy matrix-Bingham definition, normalization/asymptotics, and
  information-geometry territory.
- Sra (2016), DOI `10.1016/j.ejc.2015.07.005`, and McSwiggen--Sahi,
  arXiv:2605.12680v2, own normalized-Schur and logarithmic-convexity
  majorization inequalities. They do not order the incomparable fixed-trace,
  fixed-Frobenius half-Grassmann spectra.

## 3. Same-author lineage

- `ARR-2026-61Y0FFA39M8KMBJ5` proves the exceptional global all-field
  `Gr_C(2,4)` rank-two result.
- `ARR-2026-6FDEKPVJ0W8BHBMC` proves eventual high-field rank-r optimality and
  the exact high-fidelity RDF segment.
- The present theorem does not repackage either result. It proves all-field
  **local** balanced stability in every rank and over all three division
  algebras, and an exact metastability obstruction for every complex
  two-block multiplicity. It explicitly leaves global ordering and the
  all-distortion RDF open.

## 4. Unsafe and safe claims

Unsafe:

- “first positive-definite orbital-kernel theorem”;
- “complete Grassmann phase diagram”;
- “global balanced optimizer”;
- “exact all-distortion rank-r RDF”;
- “all unbalanced spectra are saddles”; and
- interpreting local maxima as physical thermodynamic phases without a
  separate physical model.

Safe:

> We derive a squared-orbital-harmonic Laplacian identity and use it to prove
> all-field transverse Morse--Bott maximality under an explicit isotropy
> hypothesis. For real, complex, and quaternionic half-Grassmann projector
> orbits this excludes a balanced radial spinodal. In the complex case exact
> Jacobi--Stein Hessian operators yield a sharp weak-field multiplicity
> threshold and prove the existence of near-balanced metastable two-block
> strata.

## 5. Publication assessment

The universal theorem plus the three-family application and the exact
metastability obstruction is a coherent paper. On the severe scale used for
this programme, the current proof-complete package is estimated at
**7.2--7.7**, with manuscript quality contingent on full derivations and
release QA. It is materially stronger scientifically than Paper 14's
application-specific finite-sample synthesis, although it deliberately does
not reach the higher 8+ ceiling of the still-open global half-rank Laplace
order.

## 6. Remaining gates

1. Independent line-by-line audit of the normal-isotropy and Jacobi-Hessian
   normalizations.
2. Verify that the `k=1` absent positive-block module is scoped explicitly.
3. Rebuild after final bibliography correction and inspect every rendered
   page.
4. Freeze replay, source, PDF, and hashes before any ARR deposit.
