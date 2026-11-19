      Rank defects and spectral stability of Boolean Doob chains
                                             Lluis Eriksson

                             Research manuscript, 18 November 2026


                                                 Abstract
          A reversible Doob transform of half-correlated Boolean noise can have a small spectral gap
      even when many stationary marginals are uniform. We bound its entire ordered spectrum
      using the rank of four disjoint coordinate families in the Walsh span of its stationary density.
      A stationary second-moment bound suffices, without a dimension-uniform positive floor. A
      fixed spectral discrepancy forces a subcode whose support is small relative to its dimension.
      Recovery persists under a fixed, pointwise multiplicative perturbation of a structured stationary
      law, even when the perturbed law has full Walsh span. The perturbation argument combines
      stability of symmetric scaling in stationary Lp spaces with ambient tests of a quotient weight.


1     Setting and prior results
Write µ for uniform probability on FL2 and E for its expectation. For 0 < λ < 1, Pλ flips each
                                                                                             Pinput
bit independently with probability (1−λ)/2. It multiplies the Walsh character χS (x) = (−1) i∈S xi
by λ|S| . All function norms use µ unless a density is displayed. Matching through order k means
that every set of at most k coordinates has uniform joint law.
    The metastable shell construction shows that cubic-mean convergence and extensive matching
can coexist with an exponentially small gap. Earlier moment-transfer bounds relate the potential
to the stationary law, and local retention estimates control the killed chain on small balls. Our
question is which stationary structures guarantee recovery for all ambient modes. Sections below
give an exact-code criterion and a perturbation theorem.


2     The rank defect bound
On the uniform cube let P = P1/2 , Q = P1/√2 , h > 0, g = P h, π = hg, Eπ = 1, U = h/g,
and K(x, y) = P (x, y)h(y)/g(x). Suppose ∥π∥2 ≤ B and all its nonconstant Walsh coefficients
through ambient degree k ≥ 1 vanish. Use the binary code C spanned by the Walsh support of π.
Equivalently π(x) depends on Ax, where the rows of A form a basis of C. A larger representing
row space also works. Write d = dim C.

2.1   Two conclusions of one estimate
Let r be the least nonnegative integer such that four disjoint sets of columns of A each have rank
at least d − r. Define ∆ as the maximum distance between corresponding ordered eigenvalues of
K and P , with ambient multiplicities. Then

                                       ∆ ≤ min{1, CB 233r−k/28 }.


                                                     1
In particular r = o(k) suffices for full spectral recovery as k → ∞. One can append s arbitrary
parity measurements to a four-basis quotient and allow arbitrary dependence on their values. The
original four sets still have rank at least dold , so r ≤ s after eliminating linearly dependent output
rows. Matching and the second-moment cap must still hold for the new stationary law. No lower
bound on its minimum uniform in dimension, and no norm-smallness of its dependence on those
parities, is required.
    Conversely, if ∆ ≥ η > 0, the Walsh span contains a subcode V with

                              dim V − 14 |supp V | ≥ k/924 − OB,η (1).

Here the support of a subcode is the union of its words’ supports. This is a restriction on where
many independent parities must live. It does not assert that π itself has a low-degree coefficient.
The numerical constants are sufficient and have not been optimized.

2.2   Forward and reverse estimates when the four spans differ
Take four disjoint independent column families spanning subspaces of codimension at most r,
trimming redundant columns. On functions of Ax, each family acts on every one of its cosets
as ordinary independent-bit noise, expressed in its own basis. The cosets are equiprobable. For
ordinary forward exponents 1 < a ≤ b, the normalized outer norms on at most 2r cosets cost at
most 2r(1/a−1/b) in passing from a to b. This follows by applying the contractive estimate on each
coset, then the finite-space norm inequality. Consequently for four successive families,

                        ∥Pλ f ∥b ≤ 2r(1/a−1/b) ∥f ∥a ,       b − 1 ≤ (a − 1)λ−8 .

One may choose the four intermediate exponents by distributing the required gain equally on a
logarithmic scale. All remaining column factors commute and are contractions.
    There is a corresponding estimate on the negative side. For positive v, on each coset the reverse
inequality bounds the Lb norm of the reciprocal output by the La norm of the reciprocal input, for
0 < a ≤ b, 1 + b ≤ (1 + a)λ−2 in one family. Passing to the global reciprocal norms costs the same
finite-space factor as above. Four steps therefore give

                     ∥(Pλ v)−1 ∥b ≤ 2r(1/a−1/b) ∥v −1 ∥a ,      1 + b ≤ (1 + a)λ−8 .

This argument permits different subspaces at each step. The factor telescopes because it bounds
each step in the same global uniform measure. Extra averaging factors contract reciprocal norms
by Jensen applied to u−b . These coset estimates are used only on one side of zero at a time. The
mixed-sign step below is performed on the entire cube. The Boolean inputs are classical. Bonami,
Borell, Mossel, Oleszkiewicz and Sen, including Remark 1.13.

2.3   Recovering an inverse moment on the actual chain
As in the four-basis proof, the uniqueness of positive h given hP h ensures that h, g, U are quotient
functions. Indeed, for two positive solutions with the same density, the ratio of their noise
averages is the reciprocal of the ratio of potentials. If the latter has distinct extrema m, M , strict
positivity of the kernel puts the former strictly between them everywhere. At the two extrema
this would imply both mM < 1 and mM > 1. The constant ratio must be one. Applying this
uniqueness to translations in ker A gives the invariance. Put F = Qh, a0 = Eh. Then ∥F ∥2 = 1,
and matching gives 1 − a20 ≤ a20 B 2 2−(k+1) and ∥g − 1∥2 ≤ CB 2−k/2 . To recall the key estimate,


                                                    2
1 = (Ehg)2 ≤ a0 Eπg; the constant q
                                  component contributes a20 , and the part of g = QF above
degree k has norm at most 2−(k+1)/2 1 − a20 . Thus a0 is bounded away from zero solely in terms
of B.
    Split Q = Pλ1 Pλ0 with λ20 = 7/8, λ21 = 4/7. Interpolation gives ∥F ∥1/16 ≥ a31
                                                                                 0 . For v = Pλ0 F ,
ordinary full-cube reverse hypercontractivity from order 1/16 to −1/16 yields ∥v −1 ∥1/16 ≤ a−31
                                                                                               0
since 7/8 < 15/17. Now apply the negative coset estimate to g = Pλ1 v with reciprocal exponents
1/16 and 7. Its condition holds since (17/16)(7/4)4 > 8. We obtain

                            ∥g −1 ∥7 ≤ CB 216r ,       ∥U ∥14/11 ≤ CB 232r ,

the last by U = π/g 2 and 11/14 = 1/2 + 2/7.

2.4   Returning to all ambient modes
For a nonzero nonnegative quotient weight W , the strictly positive matrix Pλ MW Pλ commutes
with kernel translations of A. Its unique positive unit top eigenvector is a quotient function. The
forward estimate thus implies on the full cube

               ∥Pλ MW Pλ ∥2→2 ≤ 22r(1/2−1/b) ∥W ∥s ,         b = 2s/(s − 1) ≤ 1 + λ−8 .

For zero weight the conclusion is immediate. With Ek = {|g − 1| > 2−k/8 }, we have µ(Ek ) ≤
CB 2−3k/4 . On its complement, |U − π| ≤ C2−k/8 π for large k. On Ek , Hölder at 6/5 < 14/11
gains µ(Ek )1/21 . Applying the full multiplier estimate at Q, s = 6/5, b = 12, costs 25r/6 . Hence

                                    ∥QMU −π Q∥ ≤ CB 233r−k/28 .

    For the signed stationary term factor Q = R2 , R = P2−1/4 . The full multiplier estimate for
|π−1| at R uses s = 2, b = 4 ≤ 5 and costs 2r/2 . Split the inner R at degree j = ⌊k/2⌋. The two low
factors give zero against π − 1 by matching; every other term includes at least one factor with norm
2−(j+1)/4 or smaller. Weighted Cauchy-Schwarz therefore gives ∥QMπ−1 Q∥ ≤ 3(B + 1)2r/2−(j+1)/4 .
Adding proves the same claimed bound (up to CB ) for ∥QMU Q − P ∥. The Gram products of
M√U Q and stationary conjugation identify the ordered eigenvalues as in the four-basis proof. Both
kernels have spectrum in [0, 1]. This also absorbs bounded k.

2.5   Identifying the obstruction and checking both directions
In fact the rank deficit can be read without choosing four bases:
                                                                    
                                r = max{dim V − |supp V |/4} .
                                         V ≤C

Include V = 0. For a candidate integer deficit u ∈ [0, d], truncate the column matroid to rank
d − u. Four disjoint bases of the truncation exist exactly when every column subset T satisfies

                                 L − |T | ≥ 4(d − u − rank(AT )).

Negative right sides are vacuous. This is the matroid base-packing theorem applied to the truncated
rank. The subcode of words vanishing on T has dimension d − rank(AT ) and support contained in
T c . Conversely, for any V take T to be the complement of its support: all of V vanishes on T .
These two comparisons give the displayed ceiling formula. If the spectral discrepancy is at least η,

                                                   3
taking logarithms in the upper bound and allowing one for the ceiling gives the claimed subcode.
Edmonds and Fulkerson, Theorem 2.
    For a concrete positive test, let z be the parity of m ≥ 4 bits and let y1 , . . . , ys be additional
single bits, with s ≥ 1. Put

                           π = 1 + (1 − ϵ)z(1 + s−1
                                                        P
                                                        i yi )/2,   0 < ϵ < 1.

Its mean is one, its minimum is ϵ, its maximum is at most two and matching holds through m − 1.
Its nonconstant characters z, zyi generate the full span of z, y1 , . . . , ys . Every yi requires its own
column, so four full bases are impossible. Each of the four column families can still contain one
copy of the z-direction, giving r ≤ s. The positive symmetric scaling for π exists on the finite cube
by the positive scaling result in Moment transfer and spectral bounds, v3. The intrinsic deficit is
exactly ⌈3s/4⌉: the raw singletons span a subcode of dimension and support size s, while assigning
them as evenly as possible to four distinct copies of the z-column leaves maximum rank deficit
s − ⌊s/4⌋. Taking ϵ ↓ 0, s = o(m) tests both the missing uniform floor and a growing number of
defects.
    For a negative test, the published shell, v1 has bounded stationary second moment, matching
k proportional to dimension and λ2 (K) → 1, whereas λ2 (P ) = 1/2. Thus its Walsh span must
have the displayed extensive subcode obstruction. This also excludes a universal stability criterion
based solely on a small stationary L2 error from a structured law: that shell converges even in
cubic mean to the uniform law. The necessary structural condition alone does not construct a
trap.


3     Stability under perturbations of the stationary density
Continue with the same Boolean noise kernel. Suppose a positive reference probability density π0
has ∥π0 ∥2 ≤ B and depends on a binary quotient with four disjoint column families of rank deficit
at most r. For another positive probability density π, assume exact ambient Walsh matching to
order k ≥ 1 and
                                   ∥ log(π/π0 )∥∞ ≤ 1/4096.
There is no requirement of matching for π0 , symmetry for π, or a common positive floor. For the
actual chain with stationary density π,

                           max |λj (K) − λj (P )| ≤ min{1, CB 233r−3k/224 }.
                             j

In particular a fixed-width relative neighbourhood of a four-basis quotient law has exponential
recovery along matched densities, even when their Walsh spans are the full ambient space. The
width and exponents are sufficient values.

3.1    Stability of positive symmetric scaling
For f = log(π/π0 ), let ϵ = ∥f ∥∞ and πt = π0 etf , without renormalizing along the path. Write
ht P ht = πt (pointwise product). Existence and smooth dependence in finite dimension follow by
minimizing                  X                           X
                          1
                          2    µ(x)P (x, y)eu(x)+u(y) −   µ(x)πt (x)u(x).
                             x,y                            x

Positive diagonal terms already give a coercive lower bound and a positive definite Hessian. The
minimizer has ht = eu ; the implicit function theorem applies. The associated Kt is Markov,

                                                    4
reversible, and positive semidefinite in L2 (πt dµ) by stationary conjugation and positivity of the
Boolean noise spectrum. Differentiating gives

                                       (I + Kt ) ∂t log ht = f.

The operator Ht = (I−Kt )/2 has L2 norm at most 1/2 and L∞ norm at most one. Interpolation and
the geometric series for (I+Kt )−1 = (I−Ht )−1 /2 give Lp operator norm at most 1/[2(1−2−2/p )] ≤ p
for 2 ≤ p < ∞. Comparing the path measures to π0 and integrating yields, for v = log(h1 /h0 ),

                                     ∥v∥Lp (π0 ) ≤ e2ϵ/p pϵ ≤ 2pϵ.

Here and below Lp (π0 ) uses probability measure π0 dµ. Expanding the exponential, the terms of
order j ≥ 2 in Eπ0 e168|v| are bounded by (336eϵ)j using j! ≥ (j/e)j ; the first moment is bounded by
the second. Thus e2v−f has uniformly bounded L84 (π0 ) norm. This estimate concerns stationary
scaling, and uses a finite-p bound with constants independent of small atom masses. For related
stability theory see Nutz and Wiesel.

3.2   A reserve of integrability for arbitrary ambient test vectors
Put g0 = P h0 , F0 = Qh0 , a0 = Eh0 . Normalization gives ∥F0 ∥2 = 1 and ∥g0 ∥2 ≤ 1. Cauchy-
Schwarz in h0 dµ yields 1 ≤ a0 Eπ0 g0 ≤ a0 B. The inverse-moment proof from the rank-defect
estimate therefore gives ∥g0−1 ∥7 ≤ CB 216r even without matching of the reference.
    For q = 21/20 and every ambient unit L2 vector x, we claim

                                    ∥g0−2 |Qx|2 ∥Lq (π0 ) ≤ CB 233r .

In Q = Pλ Pγ take γ 2 = 10/11, λ2 = 11/20. Ordinary ambient hypercontractivity gives ∥Pγ x∥2q ≤ 1.
Jensen gives |Qx|q ≤ Pλ |Pγ x|q , whose input has L2 norm at most one. The weight W = π0 g0−2q is
a quotient function, with

                           ∥W ∥5/4 ≤ B∥g0−1 ∥2q
                                             7 ,         4/5 = 1/2 + 2q/7.

For this weight, the full-space multiplier bound at Pλ applies since 10 ≤ 1 + (20/11)4 . It costs
24r/5 . Taking the qth root gives the claim because 32 + 4/(5q) < 33. The same proof with W = π0
bounds ∥|Qx|2 ∥Lq (π0 ) by CB 233r .

3.3   The perturbed chain
The identity U = π0 g0−2 e2v−f transports the preceding reserve to any set E, including sets that
cut every quotient fibre. Hölder with exponents 84, 21/20, 28 gives

                       E[1E U |Qx|2 ] ≤ CB 233r π0 (E)1/28 ≤ CB 233r µ(E)1/56 .

The notation π0 (E) means E π0 dµ. The same bound holds with π instead of U , by π ≤ eϵ π0 . The
                           R

three reciprocal exponents are 1/84, 80/84, 3/84.
    Apply the matching-energy estimate to the true π, whose second moment norm is at most eϵ B.
For E = {|P h1 − 1| > 2−k/8 }, it gives µ(E) ≤ CB 2−3k/4 . On its complement |U − π| ≤ C2−k/8 π
for large k. Combining the two estimates yields ∥QMU −π Q∥ ≤ CB 233r−3k/224 . For the signed term
QMπ−1 Q, the two low factors vanish by true matching. The positive quotient envelope 1 + eϵ π0
dominates |π − 1|, so the same split at ambient degree ⌊k/2⌋ as in the rank-defect note bounds
the remainder by CB 2r/2−(⌊k/2⌋+1)/4 . The Gram argument proves the asserted spectral bound for
all ordered eigenvalues. Bounded k is absorbed into the constant.

                                                   5
3.4    A full-span check and the boundary of the conclusion
Let L = 3m, m ≥ 4, let S be the first m coordinates, and let w be the remaining 2m coordinates.
Take
                                           PL
      π0 = 1 + (1 − am )χS ,   H = (χw +      i=1 χw△{i} )/(L + 1),     π = π0 (1 + H/16384),

where 0 < am < 1 tends to zero. The reference has four disjoint column bases of rank one and norm
at most two. Since |H| ≤ 1, the log ratio bound holds. Every new character and its product with
χS has degree at least 2m − 1. Hence π is normalized and matches through m − 1. All displayed
nonconstant coefficients are positive and the pairs w, w△{i} generate every singleton in the Walsh
span. Its intrinsic deficit is ⌈3L/4⌉, making the exact-code estimate uninformative here. Yet the
new result bounds the full spectral error by C2−3(m−1)/224 , although min π ≤ (1 + 1/16384)am → 0.
    The metastable shell is arbitrarily close to the uniform law in cubic mean and has a macroscopic
discrepancy in its second eigenvalue. Thus small cubic-mean error cannot replace this pointwise
log-ratio condition, even around the uniform law. What remains undecided is recovery for arbitrary
matched laws at the programme’s stationary moment endpoint, outside the neighbourhood
controlled here.


4     Observable moments
The finite-sample spectral certificate draft uses affine localizers on measured moments. For a
possible interface, let D = CB 233r−k/28 and S = QMU Q in the common uniform Hilbert space.
For every integer ℓ ≥ 1, telescoping the powers of the two contractions gives ∥S ℓ − P ℓ ∥ ≤ ℓD. In
a fixed isometric observation J, each compressed moment block J ∗ S ℓ J is therefore within ℓD in
operator norm of its comparator. For a scalar observation and an affine localizer with coefficient
matrices Hℓ , the deterministic margin is D ℓ ℓ∥Hℓ ∥. This applies to observations in the common
                                           P

Gram representation. Transfer of an observable fixed instead in the physical stationary coordinates
would also require identifying its transport. No finite-sample data, coverage claim or numerical
certificate is produced here.
    Samorodnitsky and the subsequent noisy-function inequalities for codes give primary precedents
for studying Boolean noise through coordinate restrictions. The present comparison uses a
deterministic packing of four deficient spanning families, an inverse stationary moment and an
ambient operator estimate.


Model assessments and review context
Codex assisted with the derivation, drafting and internal checks. The source notes and their
revision history are recorded in the programme repository. This source draft has no exact-PDF
assessment or independent peer review. Scores attached to earlier AIRR records concern other
documents.




                                                 6
