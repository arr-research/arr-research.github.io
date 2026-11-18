    A metastable Hamming shell with exactly matched stationary
                           marginals
                                                 Lluis Eriksson

                                            18 November 2026

                                                Abstract
         We construct finite reversible Doob chains for Boolean noise of correlation one half whose
     spectral gaps tend to zero exponentially. Their normalized stationary densities have any pre-
     scribed fixed floor below one, converge exponentially to one in cubic mean, and have exactly
     uniform marginals through a positive fraction of the coordinates. A single Hamming sphere
     of exponentially small stationary mass traps the chain for exponentially many steps. The con-
     struction adjusts the potential on the shells typically reached in one and two noise steps, then
     calibrates an additional spike using the ordinary return probability of the target sphere. A
     binary type estimate makes the spike affordable at the critical stationary moment. We give a
     localized norm inequality showing that the critical moment of the normalized weighting density
     diverges exponentially in the same family. These conclusions concern finite Boolean noise chains.


1    Setting and result
Let µ be uniform on {−1, 1}L , let P = P1/2 keep each sign with probability 3/4 independently, and
let h > 0 with Eµ hP h = 1. Put
     g = P h,   π = hg,       ν = πµ,    U = h/g,      r = U/Eµ U,       K(x, y) = P (x, y)h(y)/g(x).
Thus π and r are distinct probability densities. The stationary edge measure µ(x)P (x, y)h(x)h(y)
is symmetric. gap(K) = 1 − λ2 (K) uses the second largest eigenvalue. Let m(x) = L−1 i xi . A
                                                                                         P

sphere S = {m = d} is contained in the ball of radius (1 − d)L/2 about the all-plus vertex. All
function norms below use µ unless a different measure is indicated.
Theorem 1.1. There exist fixed d, β, c > 0 with 0 < d < 1 and an infinite arithmetic progression
of dimensions such that the following holds. For every fixed b < 1, b > 0, and every sufficiently
large L on the progression there is a positive radial potential satisfying
                    π ≥ b,      ∥π − 1∥3 ≤ e−cL ,          Eµ πχT = 0   (1 ≤ |T | ≤ ⌊βL⌋).
                             In particular Eµ π 3 ≤ 2 eventually. The sphere S = {m = d} has ν(S) ≤
                Q
Here χT (x) =    i∈T xi .
e−cL and
                       sup K(x, S c ) ≤ e−cL ,       gap(K) ≤ e−cL ,       ∥r∥3 ≥ ecL .
                       x∈S
Exponents may be decreased to use one common c.
                                                 √
    The marginal condition exceeds any fixed C L for large L. This refutes a dimension-uniform
positive gap and a dimension-uniform critical weighting moment under the stationary assumptions
of [4]. The sufficient escape estimate for radii up to L/96 at half noise in [5] coexists with the
trapping example at a larger fixed radius fraction. In particular that sufficient estimate cannot be
extended to every fraction below 1/2. We do not locate the optimal radius.

                                                       1
2    Cost of returning to the same sphere
For |s| < 1 put
           I(s) = 21 [(1 + s) log(1 + s) + (1 − s) log(1 − s)],       J(d) = 34 I(4d/3) − I(d).
Fix a small positive rational d. Take L along common multiples of the denominators of 3/8 ± d/2,
1/8, and (1 + d)/2. Write q = P (x, S) for x ∈ S, which is constant by permutation symmetry.
Lemma 2.1. µ(S) ≤ e−LI(d) and, with constants depending on d,
                                                                  2
                                    e−LJ(d)−O(log L) ≤ q ≤ e−Ld /8 .
Moreover J(d) = d2 /6 + O(d4 ) and I(d) = d2 /2 + O(d4 ) as d → 0.
Proof. The first bound is the binomial Chernoff estimate, also obtained from Lj ≤ eLH(j/L) with
                                                                                        

binary entropy H. Under an ordinary stationary noise edge the sign pair probabilities, in or-
der ++, +−, −+, −−, are (3/8, 1/8, 1/8, 3/8). Prescribe the joint empirical frequencies (3/8 +
d/2, 1/8, 1/8, 3/8 − d/2). Both endpoints then lie in S. The multinomial formula and log n! =
n log n − n + O(log(n + 2)) bound the probability of this joint type below by exp[−(3L/4)I(4d/3) −
O(log L)]. The probability of all edges within S is µ(S)q, giving the lower bound. For independent
signs, possibly of different means, the one-sided deviation probability of their average by a is at
           2
most e−La /2 [1]. Here the mean from the sphere is d/2. Finally I(s) = s2 /2 + O(s4 ) by Taylor
expansion at zero.


3    A depression, two compensation bands and a spike
Set w = d/100 and k = d3 . Choose and fix the rational d sufficiently small that
      3k < w2 /8,   2k < d2 /500,    d2 /8 > 2k,    J(d) − I(d)/3 < k/2,       J(d) + k < 2I(d)/3.
All these conditions follow from Lemma 2.1 by taking d smaller. Small exponents in this construc-
tion are fixed before L increases. Define disjoint sets
             B = {|m − d/2| ≤ w},        C = {|m − d/4| ≤ w},         D = {|m − d| ≤ 4w}.
The background potential H0 equals e−kL on B, ekL on C ∪ D and one elsewhere. With S ⊂ D,
define
                    M = e−kL/2 /q,     H = H0 + M 1S ,    W = H P H.
By the upper bound on q, M ≥ ekL eventually.

Uniform floor. The mean magnetization after ordinary noise from x is m(x)/2. For x ∈ B, the
                                                    2
mean lies within w/2 of d/4, so P (x, C) ≥ 1 − 2e−Lw /8 . The factor ekL on C compensates e−kL on
B. For x ∈ D, H0 (x) ≥ ekL and P H0 (x) ≥ e−kL . Outside B ∪ D the mean is at distance greater
                                          2
than 2w from d/2, and P (x, B) ≤ 2e−Lw /2 . There H0 ≥ 1 and P H0 ≥ 1 − P (x, B). Consequently
                      2
inf W ≥ 1 − O(e−Lw /8 ) by positivity. The two compensation bands ensure this bound also at
vertices adjacent to the modified region.
                                                                                              2
Retention. For x ∈ S the landing mean is exactly d/2, so P H0 (x) ≤ e−kL + 2ekL−Lw /2 ≤ 2e−kL
eventually. The added spike contributes M q = e−kL/2 to P H(x) entirely inside S. It follows row
by row that
                      KH (x, S c ) ≤ P H0 (x)/(M q) ≤ 2e−kL/2   (x ∈ S).

                                                    2
Critical stationary cost. Write E = B ∪ C ∪ D. Every member has m(x) ≥ d/8, so µ(E) ≤
    2
e−Ld /128 . By contraction of P on L3 and ∥H0 ∥∞ ≤ ekL ,
                              ∥H0 P H0 − 1∥3 ≤ (1 + ekL )ekL µ(E)1/3 .
This decays exponentially by the choice of k. Outside S, the additional term is exactly H0 M P 1S .
Ordinary Boolean hypercontractivity at correlation 1/2 gives ∥P 1S ∥3 ≤ ∥1S ∥3/2 = µ(S)2/3 [2].
Thus its norm is at most exp[L(k/2 + J(d) − 2I(d)/3) + O(log L)]. On S, P H ≤ 3e−kL/2 and
H ≤ 2M eventually. In particular
              ∥1S W ∥3 ≤ 6e−kL µ(S)1/3 /q ≤ 6 exp[L(J(d) − I(d)/3 − k) + O(log L)].
This too decays exponentially. Since ∥1S ∥3 = µ(S)1/3 , the three bounds imply ∥W              −c0 L )
                                                            −c   L
                                                                                 √ −1∥3 = O(e
for some c0 > 0. For Z = EW it follows that Z = 1 + O(e        0   ). Now h0 = H/ Z gives π0 = W/Z
with the same convergence and inf π0 ≥ 1 − o(1). Normalization does not change the transition
law.


4    Exact matching and the spectral gap
For fixed β ∈ (0, 1/2) with binary entropy H(β) < c0 /2 in natural units, subtract the nonconstant
Walsh projection from π0 :                   X
                                   v = π0 −        (Eπ0 χT )χT .
                                                  1≤|T |≤βL

There are at most eLH(β) summands by the binomial bound and each coefficient is at most ∥π0 −1∥1 .
Thus ∥v − π0 ∥∞ = O(e−c0 L/2 ). The density v is radial with mean one; it satisfies the stated Fourier
identities, floor and cubic convergence.
    We include the stability argument of [4, Lemma 10.4] to check that exact matching preserves
the trap even if the gap is small. For a positive target u, minimize
                                  X                             X
                              1
                              2         µ(x)P (x, y)ezx +zy −       µ(x)u(x)zx .
                                  x,y                           x

The Hessian is positive definite by the diagonal terms. If the maximum coordinate tends to infinity,
its diagonal term dominates the linear part. When the maximum stays bounded above and a
coordinate tends to minus infinity, its positive linear weight forces divergence. Thus there is a
unique minimizer, solving ez P ez = u. Positive definiteness gives smooth dependence. Along
ut = (1 − t)π0 + tv, write ht = ezt and Kt for its Doob kernel. Logarithmic differentiation gives
(I + Kt )żt = (v − π0 )/ut . For large L, ut ≥ b∗ = (1 + b)/2. The stationary law has smallest
atom at least 2−L b∗ . The spectrum of Kt is in [0, 1] by positive semidefiniteness of Boolean noise
and reversible conjugation. For T = (I − Kt )/2 the absolute row sums are at most one and its
stationary L2 norm is at most 1/2. Hence
                                                                    (I + Kt )−1 = 12
                                                                                       X
                  ∥T j ∥∞→∞ ≤ min(1, 2(L/2)−j / b∗ ),                                        T j.
                                                      p

                                                                                       j≥0

The inverse norm is Ob (L+1) independent of the gap. Integration shows ∥ log(h1 /h0 )∥∞ = Ob ((L+
1)e−c0 L/2 ). Uniqueness gives radiality. Every transition changes by a factor between e−2η and e2η
for this logarithmic error η. In particular the exit bound persists, and h = h1 has stationary density
v.
    Since ν(S) ≤ ∥v∥3 µ(S)2/3 , its mass is exponentially small. The centered indicator of S has
Dirichlet energy at most ν(S) supS K(x, S c ) and variance ν(S)(1 − ν(S)). This proves the gap
upper bound. Starting anywhere on S, survival for n steps is at least (1 − supS K(x, S c ))n . In
particular the mean exit time grows exponentially.

                                                       3
5    The critical weighting moment
We prove the localized estimate needed to distinguish a large ratio at one vertex from divergence
of its critical moment. For each fixed α < 1/2, α ≥ 0, there exists aα > 0 such that on every subset
A of a ball of radius αL,
                                ∥KAA ∥L2 (ν)→L2 (ν) ≤ e−aα L ∥1A U ∥3 .                          (1)
In one coordinate use norms of uniform probability, p = 3/2, p′ = 3. Encode minus signs by j = 1,
plus by j = 0. Define Dt (j) = et(1/2−j) as a multiplication operator and N (t) = ∥Dt P Dt ∥p→p′ .
Positivity and Cauchy–Schwarz for its positive semidefinite quadratic form identify this with the
maximal quadratic form over nonnegative unit p-vectors. At zero the unique nonnegative maximizer
is one. Indeed, normalize the mean of a nonzero pair to one and write its entries as 1±x, 0 ≤ x ≤ 1.
Its
√ noise energy
           √      is 1 + x2 /2. The derivative of [(1 + x)3/2 + (1 − x)3/2 ]/2 is at least 3x/4 since
   1 + x + 1 − x ≤ 2. This exceeds the derivative of (1 + x2 /2)3/4 for x > 0; at zero both functions
are one.
     The derivative of ⟨1, Dt P Dt 1⟩ at zero vanishes by centering. Nonnegative maximizers for t ↓ 0
approach one by compactness and uniqueness. Taylor expansion in t is uniform on the unit sphere,
so comparison with the value at zero and testing on one yield log N (t) = o(t). The p-to-p′ tensor
norm is at most N (t)L , by successive coordinate estimates and Minkowski’s mixed-norm inequality
(p ≤ p′ ). On the centered ball the inverse product multiplier is at most e−t(1/2−α)L ; another center
follows by translation. Applying the product bound to both copies of a supported function gives

                                 ⟨f, P f ⟩ ≤ [N (t)e−2t(1/2−α) ]L ∥f ∥23/2 .
                                                                  √                           1/2
Choose small t > 0 so the bracket is below one. Substitute f = U z, use ∥f ∥3/2 ≤ ∥1A U ∥3 ∥z∥2
                                          √
for supported z, and conjugate KAA by π to obtain (1).
    Apply (1) with α = (1 − d)/2 and A = S. The Rayleigh quotient of 1S is at least 1 −
supS K(x, S c ), so ∥1S U ∥3 grows exponentially. Normalizing U by its mean preserves this conclusion.
Indeed π = hg ≥ b gives g ≥ bP (1/g) ≥ b/(P g) by Jensen. With Q = P√1/2 we have ∥Qh∥2 = 1
and P g = P(1/2)3/2 Qh. Hypercontractivity gives ∥1/g∥9 ≤ 1/b. Consequently EU = E(π/g 2 ) ≤
∥π∥3 ∥1/g∥23 ≤ 21/3 /b2 . This completes the proof of Theorem 1.1.


6    Relation to earlier results and review context
Bonami’s inequality supplies ordinary-cube norm estimates. Polyanskiy and Samorodnitsky de-
veloped improved hypercontractivity on small supports [3]. Here the stationary density and the
transition row both change with the potential. The earlier construction in [4, Section 11] has an
exponentially small noise denominator at a vertex but preserves the ordinary spectrum asymptot-
ically. The collective self-return of an entire sphere, calibrated by its conditional type probability,
changes the conclusion. The shell widths and exponents here are sufficient rather than optimized.
The construction requires arbitrarily large dimensions, gives a subsequence at fixed correlation, and
supplies no continuum or physical spectral statement. The literature comparison does not establish
global priority.

Model assessments and review context. OpenAI Codex assisted with the construction, proof
and manuscript. The analytic audit shares the preparation context. No proof assistant or numerical
oracle was used. The first exact-PDF assessment, its objections, identity information and score
belong to the version-specific record. Earlier scores concern different artifacts.

                                                     4
References
[1] W. Hoeffding, Probability inequalities for sums of bounded random variables, J. Amer. Statist.
    Assoc. 58 (1963), 13–30. https://doi.org/10.1080/01621459.1963.10500830.

[2] A. Bonami, Etude des coefficients de Fourier des fonctions de Lp (G), Ann. Inst. Fourier 20
    (1970), 335–402. https://doi.org/10.5802/aif.357.

[3] Y. Polyanskiy and A. Samorodnitsky, Improved log-Sobolev inequalities, hypercontractivity and
    uncertainty principle on the hypercube, J. Funct. Anal. 277 (2019). https://arxiv.org/abs/
    1606.07491.

[4] L. Eriksson, Moment transfer and spectral bounds for Boolean Doob kernels, AIRR working
    paper, v3 (2026). https://airr.science/papers/ARR-2026-4T35VQ6MZB8F99F4/versions/
    v3/.

[5] L. Eriksson, Local retention and spherical reconstruction for Boolean Doob chains, AIRR
    working paper, v1 (2026). https://airr.science/papers/ARR-2026-6E2HS34Q2Z8349BJ/
    versions/v1/.




                                                5
