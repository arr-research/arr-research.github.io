# Separate internal review — asymmetric degree-one routing

Reviewer: root research agent, 5 September 2026. The proof and replay were constructed by passive_cycle2; the reviewer did not construct them. This is an internal AI review, not external refereeing.

Disposition: no material mathematical error or omitted degeneracy found. Accept the all-T law for the fixed nodes 1,(3-4i)/5,i and the all-gap law at T=1, with the stated restrictions. The general sharpness criterion is conditional and is not misrepresented as a complete all-gap/all-T formula.

The review checked the original-coordinate transformation s=cot(phi/2), the positive quadratic denominator, and the equivalence between its eigenvalue ratio and the squared global Poisson peak. The ellipse support maximization is exact. The lower Lagrange certificate correctly has a negative coefficient at the interior point; discarding a nonnegative numerator value therefore gives the intended inequality even with extra output ports.

For F=A/D, strict positivity of (A'D-AD')'=A''D+2A proves uniqueness of the scalar minimizer. At stationarity, H(s)-F D(s)=(1+F)(s-t)^2, which independently verifies both active endpoint identities. The residual-power condition is a global Rayleigh-quotient condition, not merely a three-node fit. It gives exactly t^2(1+F)<=p^2. For u=2,v=1 the bounds -1/2<t<0 and F<=T^2/2 prove this condition strictly for every T>=1. Uniform convergence on that interval justifies the asymptotic constant 3/2.

The lossless completion is analytic because h is an outer scalar spectral factor. On the circle its columns are orthonormal and its determinant is h-sharp/h. Positive boundary denominator and the absence of a common numerator zero yield a degree-one inner matrix, with the claimed Poisson peak. The T=1 proof separately provides the positive affine interpolation weights and a globally bounded attaining intensity. T<1 only permits constants, whose optimum chordal error is 1/sqrt(2).

The full replay source was inspected. Its rational square-root enclosures and root-branch sign conditions retain the unsquared equation after quartic elimination. The high-precision construction fixtures are explicitly supplementary; they do not establish a sampled approximation to a global frequency supremum. The claimed global peak is checked through its analytic formula. The root reviewer reruns the script as part of delivery validation.

Limits: no general solution is claimed when the positivity condition fails, for degree at least two, extra interpolation nodes, loss, nonorthogonal targets, fixed phases, or a physical time calibration. Classical scalar factorization and Potapov completion are attributed. External priority in constrained filter design has not been established.
