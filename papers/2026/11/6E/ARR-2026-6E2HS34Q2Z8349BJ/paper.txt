                  Local retention and spherical reconstruction
                            for Boolean Doob chains
                                              Lluis Eriksson

                                           18 November 2026


                                                 Abstract
         We study transitions restricted to a Hamming ball for the noise Doob kernel of a positive
     potential. At noise correlation one half, a floor on the stationary density and a cap on its
     third moment force the killed operator norm on every ball of radius at most L/96 to decay
     exponentially in dimension L. The estimate is uniform in the potential and needs no stationary
     marginal matching. Its proof combines a bound on the reciprocal noise average using the
     entropy of a transition row with an exponentially weighted row estimate. Exact symmetrization
     of the stationary density can nevertheless strictly decrease
                                                          √       the conditional retention of a ball: we
     construct examples with matching through order C L, a fixed perturbation amplitude, and ball
     radius proportional to dimension. On the half-noise balls of the example the relative conductance
     difference is exponentially small. We also obtain control of projected stationary edge laws under
     low-degree matching. These results concern local escape and leave the unrestricted spectral gap
     open.


1    Model and observables
Write µ for uniform probability on {−1, 1}L . The noise operator P = Pρ flips each coordinate
independently with probability (1 − ρ)/2, where 0 < ρ < 1. Fix h > 0 with Eµ hP h = 1 and set

                   g = P h,    π = hg,     ν = πµ,        K(x, y) = P (x, y)h(y)/g(x).

The stationary edge probability is J(x, y) = µ(x)P (x, y)h(x)h(y). It is symmetric, and both
marginals are ν. For a nonempty proper cut A, define the retention rh (A) = J(A, A)/ν(A) and
the conductance Φh (A) = 1 − rh (A). The killed operator KAA discards trajectories on their first
exit from A. Its norm on L2 (ν|A ) bounds rh (A) by the Rayleigh quotient of 1A . A scalar rescaling
of h leaves K unchanged. In constructions using an unnormalized potential we explicitly give its
energy.
    The standing moment hypotheses for the first two theorems are π ≥ b and Eµ π s ≤ 2, with
0 < b < 1 and s = (1 + ρ)/(1 − ρ). A separate matching assumption, when imposed, means
Eµ πχT = 0 for every nonconstant Walsh character χT of degree at most k. Write |x| for the
number of minus signs. The operator R averages a function over all coordinate permutations.
Radial reconstruction replaces π with Rπ and solves uP u = Rπ. This preserves every shell mass.
It need not preserve the conditional transition probability of a shell.




                                                      1
2    Exponential escape from a ball at half noise
Theorem 2.1. For ρ = 1/2 let A be any nonempty subset of a ball of radius at most L/96 about
any vertex. Under the standing moment hypotheses,

                ∥KAA ∥ ≤ min{1, Cb γ L },      γ = 36/5 2−29/15 (101/100)2/3 51/144 < 1.

The estimate applies without any symmetry, matching, or assumed lower bound on g or h.

Proof. All norms of functions in this argument use µ. Forward Boolean hypercontractivity gives
∥Pt f ∥v ≤ ∥f ∥u for 1 < u ≤ v and t2 ≤ (u − 1)/(v − 1) [1, 2]. With Q = P√ρ , energy normalization
yields ∥Qh∥2 = 1. The floor and Jensen give g ≥ bP (1/g) ≥ b/(P g). Now P g = Pρ3/2 Qh. At
half noise this implies g −1 9 ≤ b−1 . Since h = π/g, Hölder gives ∥h∥9/4 ≤ 21/3 /b. The identity
P g = P1/4 h and another use of the floor give g −1 21 ≤ 21/3 /b2 . Consequently

                     ∥h∥21/8 ≤ 22/3 /b2 ,    ∥g∥15/2 ≤ ∥h∥21/8 ≤ Mb := 22/3 /b2 .

The last exponents satisfy (21/8 − 1)/(15/2 − 1) = 1/4.
   We keep the logarithm before applying the floor estimate. For the row law px = P (x, ·),

                                   log(1/g(x)) ≤ − log b + Epx log g.

For v = 15/2, Jensen applied under px to g v /(dpx /dµ) gives

                                  v Epx log g ≤ log Eµ g v + D(px ∥µ).

The product row has entropy relative to µ equal to LI, where I = (3/4) log 3 − log 2. Thus
g(x)−2 ≤ b−2 Mb2 exp(4LI/15) at every vertex. This intermediate bound may grow exponentially
with L.
                                                  √
    Set U = h/g = π/g 2 . Conjugation by π identifies KAA with the compression of S =
M√U P M√U in the uniform inner product. This matrix is positive semidefinite because the Walsh
eigenvalues of P are ρ|T | . Translate center to the all-plus vertex, take t = 1/20, and test the pos-
                                 p the2|x|/3
itive matrix on A against vx = U (x)t        . Its largest eigenvalue is at most maxx∈A (SAA v)x /vx by
diagonal similarity and the row-sum bound. Factor out (3/4)L from the noise row. The remaining
ratio is bounded by
                                                                              2/3

                        b−2 Mb2 e4LI/15 (2L+1 )1/3        3−3d(x,y)/2 t|y|−|x| 
                                                       X
                                                                                      .
                                                   y∈A


Here Hölder uses y π(y)3 ≤ 2L+1 in counting measure. With κ = 3−3/2 < 1/5, extending the
                   P

nonnegative sum over the cube factors it into

                            (1 + κt)L−|x| (1 + κ/t)|x| ≤ (101/100)L 5L/96 .

Combining the factors gives the claimed constant with Cb = 21/3 b−2 Mb2 . For an explicit sign check,
use log 3 < 1.099, log 2 > 0.693, log 5 < 1.610 and log(101/100) < 0.01. Substitution gives log γ <
−0.003. The first three rational bounds follow, for example, by truncating 2 j≥0 z 2j+1 /(2j + 1)
                                                                                  P

at j = 12 with z = (x − 1)/(x + 1) and bounding the tail by 2z 27 /(27(1 − z 2 )). Markov contraction
gives the cutoff at one.


                                                   2
   The two features of the proof matter at this radius. For comparison, the unweighted row test
and ∥U ∥27/11 ≤ Hb give
                                                        16/27

                                             3−27d(x,y)/16 
                                       X
                      Hb β L max                                  ,       β = (3/4)211/27 .
                             x∈A
                                       y∈A

Indeed the preceding estimates give g −1 27 ≤ 22/3 /b3 from P g = P1/4 h, then Hölder gives the
stated U moment. For the full ball of radius ⌊L/96⌋ and L divisible by 100, the center row includes
the layer L/100. Since Lj ≥ (L/j)j , its sum is at least (100/9)L/100 . The resulting exponential
base exceeds one: log β = log 3 − (43/27) log 2 > −0.008 and (16/2700) log(100/9) > 0.012. Thus
that estimate with its norm-one cutoff gives no decay for these balls.
Corollary 2.2. For any ball as in Theorem 2.1, |Φh (A)/Φu (A) − 1| ≤ ϵL /(1 − ϵL ) whenever
ϵL = Cb γ L < 1, with uP u = Rπ about its center.
Proof. Averaging preserves mean one and the floor; Jensen preserves the cap. Positive reconstruc-
tion exists by Lemma 3.1 below. Both retentions lie in [0, ϵL ]. Subtracting their complementary
conductances proves the bound.


3    Failure of exact radial domination
Lemma 3.1. For any positive w there is a unique positive solution of uP u = w. If w = 1 + af ,
∥f ∥∞ ≤ 1, B = (⌈L/2⌉ + 2)/2 and 4B 2 |a| < 1, then

                            u = 1 + a(I + P )−1 f + e,                 ∥e∥∞ ≤ 4B 3 a2 .

Proof. Minimize 21 x,y µ(x)P (x, y) exp(vx + vy ) − x µ(x)w(x)vx . Positive diagonals give strict
                    P                                          P

convexity. For m = max vx a diagonal term gives a lower bound of the form ce2m − mEw. On a
sublevel set m is bounded above; positivity of all linear weights then also bounds each coordinate
below. Stationarity gives u = ev as required.
    Write T = (I − P )/2. Its absolute row sums are at most one, and its L2 norm is at most
one half. Therefore T j ∞→∞ ≤ min(1, 2L/2−j ). Summation gives (I + P )−1 ∞→∞ ≤ B. With
H = (I + P )−1 , solve z = H(af − zP z) on the sup ball of radius 2B|a|. The displayed condition
makes the map a contraction into that ball. Its fixed point satisfies ∥z − aHf ∥∞ ≤ 4B 3 a2 , and
1 + z is positive. This proves the expansion.

Theorem 3.2. Fix ρ, b ∈ (0, 1) and C > 0. Put s = (1 + ρ)/(1 − ρ) and α = 1/(1 + 32s). For all
             large L = 4m there are potentials satisfying the standing hypotheses and exact matching
sufficiently √
through ⌊C L⌋ for which rh (A) > ru (A). Here A is the ball about all-plus whose radius is the
largest odd integer at most αL. The same family works with a fixed nonzero perturbation amplitude
as m varies. At half noise α = 1/97, so Corollary 2.2 simultaneously bounds the relative difference
of conductances.
Proof. Use four disjoint coordinate blocks B1 , . . . , B4 of size m and write ξj = χBj . Set v =
(ξ1 − ξ2 )(ξ3 − ξ4 )/4, z = ρ2m and h0 = 1 + δv. Then P v = zv, Rv = 0, and

          v 2 = (1 − ξ1 ξ2 − ξ3 ξ4 + ξ1 ξ2 ξ3 ξ4 )/4,          w = h0 P h0 = 1 + (1 + z)δv + zδ 2 v 2 .

The common energy is Z = 1 + zδ 2 /4. No nonconstant Walsh term of w has degree
                                                                            √   below 2m.
                             2       2                   2s
Choose 0 < δ < 1 with (1 − δ) /(1 + δ /4) ≥ b and (1 + δ) ≤ 2. Then h = h0 / Z satisfies the

                                                         3
                                                                                              √
claims about its density in all large dimensions. Reconstruct u0 P u0 = Rw and set u = u0 / Z. Its
stationary mass agrees with that of h on every radial set.
    Let a = zδ 2 , f = Rv 2 , D = (I + P )−1 f . If φj is the average of Walsh characters of degree j,
then on shell i                           "                         #
                                        1 1
                                                 2φL/2 (i)    (−1)i
                                   Di = 4 2 −              +          .
                                                   1+z       1 + z2
On odd shells complementary half-size subsets cancel, so Di ≤ −1/16 when z 2 ≤ 1/3. On even
shells Di ≤ 7/8. Write qi = P (x, A) on shell i and Wi = µ(|x| = i)qi . Rows of noise from adjacent
vertices have likelihood ratio bounded by s pointwise. When i is below the radius r,

                       Wi /Wi+1 ≤ s(i + 1)/(L − i) ≤ sr/(L − r + 1) ≤ 1/32.

Each even shell up to r pairs with the following odd shell. It follows that

                                 ⟨1A D, P 1A ⟩ ≤ −(9/264)⟨1A , P 1A ⟩.

The unnormalized internal mass for h0 is at least the reference ⟨1A , P 1A ⟩: the linear perturbation
vanishes by spherical averaging and the quadratic term δ 2 ⟨1A v, P (1A v)⟩ is nonnegative. Lemma 3.1
gives uniformly u0 (x)u0 (y) = 1 + a(D(x) + D(y)) + O(B 3 a2 ). Summing on the same internal edges
gives at most 1 − (9/264)a times the reference for large m, since B 3 a → 0. The conditional
retentions have equal unnormalized stationary denominators. This proves the strict comparison.
The guaranteed fractional reduction of the internal mass in this proof can decay exponentially.


4    Coordinate cuts and projected edges
Balls of positive radius fraction use all coordinates. A second regime consists of cuts identified
after few coordinate queries. Here matching gives a direct comparison of edge probabilities, even
for pairs of rare patterns.

Theorem 4.1. At any 0 < ρ < 1, assume exact matching through k and ∥π∥p ≤ B0 for p > 1 + ρ.
No stationary floor is needed. Put η 2 = ρ max(1, 1/(p − 1)), e = B0 η k+1 , um = (1 + 1/ρ)m/2 e,
and ∆m = e2 + 2um + u2m . On any m coordinates the projected actual and ordinary stationary pair
probabilities satisfy
                                  |JI (i, j)/J0,I (i, j) − 1| ≤ ∆m
for every pair of coordinate patterns. A cut D decided after at most d ≤ k coordinate queries, of
mass τ > 0, consequently has rh (D) ≤ (1 + ∆min(2d,L) )τ (1−ρ)/(1+ρ) .

Proof. Put Q = P√ρ , c = Eh and v = 1 − c2 = ∥Qh − c∥22 . Let p′ = p/(p − 1). For p′ > 2, split
                                                                        ′
Q = P1/√p′ −1 P√ρ(p′ −1) . The first factor is contractive from L2 to Lp ; on degrees > k the second
has L2 norm at most η k+1 . For p′ ≤ 2 use monotonicity and the noise multipliers. Thus the part
                                                             √                                  √
of g = Q(Qh) above degree k has p′ norm at most η k+1 v. Matching gives Eπg ≤ c + e v. By
                                                            √
Cauchy–Schwarz, 1 = (Ehg)2 ≤ c E(hg 2 ) = c Eπg, hence v ≤ ce.
     Let Qout apply Q only to the coordinates outside I. By the product kernel formula, JI (i, j)/J0,I (i, j) =
⟨Fi , Fj ⟩ with Fi = (Qout h)(i, ·) in the complementary uniform space. Expand Qh − c in Walsh char-
acters on I with vector coefficients bT . Their squared norms sum to v. Inverting Q on I multiplies
                                                                                  √
the coefficients by ρ−|T |/2 ; Cauchy–Schwarz now gives ∥Fi − c∥2 ≤ (1 + 1/ρ)m/2 v ≤ um . Expand-
ing the inner product and using 1 − c2 = v ≤ e2 proves the estimate.


                                                    4
    A decision tree has disjoint accepting leaves and their one-time probabilities match the uniform
probabilities. A pair of leaves restricts at most 2d distinct coordinates. Sum the joint atom
inequalities on these coordinates, then over all accepting pairs. Finally ⟨1D , P 1D ⟩ = ∥Q1D ∥22 ≤
µ(D)2/(1+ρ) by forward hypercontractivity. Division by τ = µ(D) finishes the proof.


5    Scope, antecedents and review context
Bonami’s inequality and Boolean noise analysis provide the forward hypercontractive estimates
[1, 2]. Polyanskiy and Samorodnitsky study improved hypercontractivity on small supports and
concentration on the cube [3]. Their reference semigroup is the ordinary cube semigroup. Here
the potential alters both stationary mass and transition probabilities; the row-entropy bound con-
trols the extra reciprocal noise average. Boyd and collaborators analyze symmetry reduction for
reversible chains with symmetries [4]. Reconstructing a new chain from spherical averages of
stationary masses changes the transition law. Earlier work in this programme develops moment
transfer and full spectrum estimates for specific Boolean Doob families [5]. Our estimates address
killed operators, projected edges and a comparison between two different chains. Global priority,
optimal ball radius and the full gap for unrestricted potentials remain open.

Model assessments and review context
The author used OpenAI Codex for analytic development and manuscript preparation. The math-
ematical checks represented here are same-context algebraic checks. No numerical oracle or proof-
assistant verification is asserted. Any exact-PDF assessment, its score, model identification and
involvement declaration belong to the version-specific publication record. No score from the earlier
working paper has been carried over.


References
[1] A. Bonami, Etude des coefficients de Fourier des fonctions de Lp (G), Ann. Inst. Fourier 20
    (1970), 335–402. https://doi.org/10.5802/aif.357.

[2] R. O’Donnell, Analysis of Boolean Functions, corrected edition. https://arxiv.org/abs/
    2105.10386.

[3] Y. Polyanskiy and A. Samorodnitsky, Improved log-Sobolev inequalities, hypercontractivity and
    uncertainty principle on the hypercube, J. Funct. Anal. 277 (2019). https://arxiv.org/abs/
    1606.07491.

[4] S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, Symmetry Analysis of Reversible Markov Chains,
    Internet Math. 2 (2005), 31–71. https://web.stanford.edu/~boyd/papers/symmetry.html.

[5] L. Eriksson, Moment transfer and spectral bounds for Boolean Doob kernels, AIRR Working
    paper, v3 (2026). https://airr.science/papers/ARR-2026-4T35VQ6MZB8F99F4/versions/
    v3/.




                                                 5
