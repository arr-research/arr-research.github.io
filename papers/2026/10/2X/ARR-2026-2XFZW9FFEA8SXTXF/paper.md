# Finite convex interpolation for polynomial Lyapunov existence

Extracted text; the canonical PDF controls mathematical notation.

Finite convex interpolation for polynomial Lyapunov existence
Lluis Eriksson
18 October 2026
Abstract
We characterize polynomial Lyapunov existence over all degrees for planar homoge-
neous polynomial ﬁelds with nonvanishing angular velocity. A moment threshold sepa-
rates strict polynomial certiﬁcates from the absence of local analytic weak certiﬁcates in
the stable case. Classical conﬂuent Nevanlinna–Pick interpolation gives a ﬁnite convex
semialgebraic formulation, with exact boundary decision for algebraic coeﬃcients. For
each odd ﬁeld degree, the certiﬁcate region is open and semialgebraic, and compact admis-
sible families have a computable common certiﬁcate degree. For rational ﬁelds in dense
binary encoding, we prove polynomial-time additive approximation of the threshold and
polynomial-time decision under a supplied positive gap promise. Explicit inner and outer
radii permit a classical weak convex optimization reduction; a uniform functional pertur-
bation argument handles algebraic poles without constructing their common number ﬁeld.
This approximates a value and does not bound the output size of a Lyapunov polynomial
polynomially. Jackson bounds and a constructive suﬃcient-degree estimate complement
the ﬁnite formulation. An exact cubic example has an algebraic threshold and minimum
Lyapunov degree eight at one rational parameter. Beyond the rotating class, a boundary-
factor obstruction produces a full twelve-dimensional rational box of stable quintic ﬁelds
with sign-changing angular velocity and no local analytic weak certiﬁcate. One explicit
rational C1 Lyapunov function works for the entire box. The latter result is a suﬃcient
obstruction, not a general classiﬁcation with angular zeros. General certiﬁed solver imple-
mentations are not supplied.
1 The certiﬁcate problem
Consider a real planar homogeneous polynomial vector ﬁeld X of degree d ≥ 1. Write its
polar equations as
˙r = rdF(θ), ˙θ = rd−1G(θ). (1)
We assume that G never vanishes. Its sign is constant; reﬂecting the plane if necessary makes
G > 0. Antipodal parity then forces d to be odd, and F, G are π-periodic trigonometric
polynomials. Deﬁne
a = − 1
2π
∫2π
0
F(θ)
G(θ) dθ, q (ϕ) = F(ϕ/2)
G(ϕ/2) + a. (2)
The proﬁle q is real analytic and has zero mean.
A weak Lyapunov function here satisﬁes V (0) = 0 , is positive away from the origin in
its domain, and has LXV ≤ 0. A strict function has LXV < 0. Homogeneous polynomial
certiﬁcates are required globally; analytic certiﬁcates may be deﬁned only near the origin. We
study the stable rotating case a > 0.
Theorem 1.1 (Finite decision in the rotating class) . For a planar homogeneous polynomial
ﬁeld with real algebraic coeﬃcients and G of one strict sign, existence of a strict polynomial
Lyapunov function is decidable by a ﬁnite algorithm. In the case a > 0, the following are
equivalent:
1

(i) a strict homogeneous polynomial Lyapunov function exists;
(ii) a weak polynomial Lyapunov function exists;
(iii) a positive local real-analytic weak Lyapunov function exists.
The algorithm also decides inputs on the boundary between existence and nonexistence. It
uses ﬁnite semialgebraic interpolation data, without prescribing a Lyapunov degree. Exact
boundary decision uses quantiﬁer elimination. Polynomial-time approximation and promised-
gap decision for dense rational inputs are established separately in Theorem 5.3.
Theorem 1.1 concerns existence of a particular kind of certiﬁcate. Stability in this class
already follows from the sign of the classical polar average a. The distinction matters: Liu and
Fitzsimmons [ 1] exhibit a stable homogeneous cubic ﬁeld with no polynomial or local analytic
weak Lyapunov function. Their family, stability analysis and original counterexample are prior
results. We use the same factorization and leading-term viewpoint, extending the certiﬁcate
problem to every proﬁle in ( 2).
Earlier results show that polynomial Lyapunov degree cannot be bounded solely by di-
mension and vector-ﬁeld degree [ 2, 3]; this does not rule out an input-dependent decision
procedure. Fixed-degree semialgebraic searches and converse sums-of-squares results address
diﬀerent questions. Gram and Toeplitz methods also provide suﬃcient certiﬁcates for sys-
tems with angular variables [ 8]. Our ﬁnite interpolation formulation decides existence over all
polynomial degrees for the rotating homogeneous class.
Korda’s recent stability decision procedure covers planar homogeneous ﬁelds, including
angular zeros [ 9]; Part III of its supplement explicitly distinguishes stability from polynomial-
certiﬁcate existence. Its Theorem 20.3 already computes the normalized polar mean as an
algebraic residue sum. We use that established calculation in our normalization. The addi-
tional problem here is the existence of a polynomial certiﬁcate of some degree.
The analytic tools used below are classical: Fejér–Riesz factorization [ 7], positive-real
representations, Jackson kernels [ 4], semideﬁnite duality, conﬂuent interpolation [ 5], and real
quantiﬁer elimination [ 6]. The contribution is the reduction connecting them to this all-degree
certiﬁcate problem.
2 A moment threshold and ﬁnite error bounds
For a real 2π-periodic function use the conventions
⟨v⟩ = 1
2π
∫2π
0
v(t) dt, q (t) =
∑
k∈Z
qkeikt, H cos kt = sin kt, H sin kt = − cos kt.
Assume for now that q ∈ C2, q0 = 0 . For N ≥ 1, set
TN (m) = ( mk−j)N
j,k=0, m −k = mk.
Deﬁne the ﬁnite optimum
aN (q) = min {b : m0 = 1 , T N (m) ⪰ 0, T N (w) ⪰ 0,
w0 = b, w k = imk − qk (1 ≤ k ≤ N)}. (3)
The diagonal of TN (w) imposes b ≥ 0. The choice mk = 0 , b ≥ max q, is feasible, since
b − q ≥ 0. Principal minors give |mk| ≤ 1, so the minimum is attained after restricting
b ≤ max q. Principal submatrices also show
0 ≤ a1(q) ≤ a2(q) ≤ · · · ≤ max q.
2

Thus
A(q) = sup
N≥1
aN (q) (4)
is well deﬁned. The integer N is a moment order, not a Lyapunov polynomial degree.
Theorem 2.1 (Finite brackets) . Let ϑN = π/(N + 2). Then
0 ≤ A(q) − aN (q) ≤ EN := π2
4 (1 − cos ϑN )
q′′
∞ ≤ π4 ∥q′′∥∞
8(N + 2)2 . (5)
Independently, if the weighted Fourier sum converges,
0 ≤ A(q) − aN (q) ≤ π2
(N + 2)2
∑
k≥1
k2|qk|. (6)
The two right-hand majorants need not be ordered.
Proof. Put
vj =
√
2
N + 2 sin((j + 1)ϑN ), 0 ≤ j ≤ N, K N (t) =
⏐⏐⏐⏐⏐⏐
N∑
j=0
vjeijt
⏐⏐⏐⏐⏐⏐
2
.
The kernel is even, nonnegative and has mean one. Its real Fourier coeﬃcients are
κk =
N−k∑
j=0
vjvj+k (0 ≤ k ≤ N), κ k = 0 ( k > N ),
with κ0 = 1 and κ1 = cos ϑN . These are the classical Jackson coeﬃcients:
κk = (N + 2 − k) cos(kϑN ) + cot( ϑN ) sin(kϑN )
N + 2 (0 ≤ k ≤ N); (7)
see [ 4, eq. (2.11)]. Extending v by zero to ℓ2(Z) and using the bilateral shift gives
1 − κk = 1
2
v − Skv

2
≤ k2(1 − κ1), k ≥ 1. (8)
Take an optimizer in ( 3) and set
uN (t) = 1 + 2 Re
N∑
k=1
κkmkeikt, w N (t) = aN + 2 Re
N∑
k=1
κkwkeikt.
For zj(t) = vjeijt, these are respectively z(t)∗TN (m)z(t) and z(t)∗TN (w)z(t). Both are non-
negative, and
wN = aN − qN − HuN , q N = KN ∗ q.
With E = ∥q − qN ∥∞, the two nonnegative densities uN and wN + E − (q − qN ) give feasible
moments at every order at damping aN + E. Hence A ≤ aN + E. This argument constructs
compatible full moment sequences; it does not assume that arbitrary simultaneous truncations
extend.
Taylor’s theorem, evenness of the kernel, and t2 ≤ (π2/2)(1 − cos t) on [−π, π] yield
E ≤ ∥q′′∥∞
2
⣨
t2KN (t)
⟩
≤ π2
4
q′′
∞ (1 − κ1).
Finally 1 − cos ϑN ≤ ϑ2
N /2 gives ( 5). Applying ( 8) directly to the Fourier series gives E ≤
2(1 − κ1) ∑
k≥1 k2|qk|, proving ( 6).
3

3 All degrees of polynomial certiﬁcates
For |α| < 1, deﬁne the positive quadratic form
Qα(x, y) = (1 + |α|2)(x2 + y2) − 2 Re(α)(x2 − y2) + 4 Im( α)xy. (9)
Its circle proﬁle is |1 − αe2iθ|2.
Theorem 3.1 (Strict threshold) . For a > 0 and a real mean-zero C2 proﬁle q, the following
are equivalent:
(i) a > A (q);
(ii) a ﬁnite product P = ∏M
j=1 Qαj , |αj| < 1, satisﬁes
−a + q(2θ) + p′(θ)
2Mp(θ) < 0, p (θ) = P(cos θ, sin θ);
(iii) some positive homogeneous polynomial of even degree satisﬁes the corresponding weak
inequality with ≤ 0.
In particular equality a = A(q) > 0 admits no such weak certiﬁcate.
Proof. For a positive homogeneous polynomial of degree 2M, Fejér–Riesz factorization of its
circle proﬁle, choosing the factor with all zeros outside the closed disk, gives
p(θ) = C
M∏
j=1
|1 − αje2iθ|2, |αj| < 1.
Factors with αj = 0 pad the actual Fourier degree to M. Diﬀerentiation gives
p′(θ)
2Mp(θ) = Im h(e2iθ), h (z) = 1
M
M∑
j=1
1 + αjz
1 − αjz , h (0) = 1 . (10)
Thus u = Re h has a strictly positive minimum on the circle. If w = a − q − Hu ≥ 0, its
coeﬃcients satisfy wk = imk − qk, where mk are the coeﬃcients of u. Both moment matrices
are positive, so A ≤ a.
To prove the necessary strict inequality, let Q(z) = 2 ∑
k≥1 qkzk. The C2 hypothesis
implies absolute convergence on the closed disk. For small ε > 0,
hε = (1 − ε)h + ε(1 − iQ)
still has positive real part and hε(0) = 1 . Since Im(1 − iQ) = −q on the circle, its slack is
a − q − Im hε = (1 − ε)w + εa.
It remains positive after replacing a by a − εa/2. This gives A < a , using a > 0.
Conversely suppose a > A . Theorem 2.1 supplies N with aN + EN < a . Form the
nonnegative densities uN , wN in its proof, and let hN (z) = 1 + 2 ∑ κkmkzk. For r < 1 close
enough to one,
Re hN (rz) > 0 ( |z| ≤ 1), a − q − Im hN (reit) = ( wN )r + (a − aN ) − [q − (qN )r] > 0.
Here a subscript r means Poisson smoothing. The Herglotz representation of hN has a prob-
ability measure on the circle. Approximate it by equal-weight empirical measures. For this
ﬁxed r < 1, the kernel is uniformly continuous on the closed disk, so the resulting functions
hM (z) = 1
M
M∑
j=1
1 + re−itj z
1 − re−itj z
approximate hN (rz) uniformly. They retain the strict slack when M is large. Equation ( 10)
now gives the required product of positive quadratic forms.
4

Proposition 3.2 (Local analytic and global polynomial certiﬁcates) . For the ﬁeld (1) with
G > 0 and a > 0, the three conditions in Theorem 1.1 are equivalent to a > A (q).
Proof. For P = r2M p(θ),
LXP
2Mrd−1GP = −a + q(2θ) + p′(θ)
2Mp(θ). (11)
Thus Theorem 3.1 handles homogeneous certiﬁcates. If V is local analytic, take its ﬁrst
nonzero homogeneous Taylor term Pm. Positivity of V and homogeneity of X give Pm ≥ 0
and LXPm ≤ 0. For pm = Pm|S1 ,
p′
m + m(F/G)pm ≤ 0.
If pm(θ0) = 0 , multiplication by exp(m
∫θ
θ0 F/G) yields a nonnegative nonincreasing function
starting at zero, over a full following period. This forces pm ≡ 0, a contradiction. Hence Pm
is positive deﬁnite, m is even, and Theorem 3.1 gives a > A (q). A polynomial is analytic; a
strict homogeneous polynomial is itself a local analytic weak certiﬁcate.
The local leading-term mechanism follows the argument used for the speciﬁc cubic coun-
terexample in [ 1]. For completeness, the classical stability statement is also direct. A periodic
primitive B′(θ) = F/G + a gives
Vsm(r, θ) = r2e−2B(θ), L XVsm = −2ard−1GVsm.
This function is coercive and C1 at the origin; for a > 0 it proves global asymptotic stability.
If a = 0 the polar trajectories are closed, and if a < 0 they spiral outward. Neither case
admits a strict Lyapunov function. This does not exclude weak ﬁrst integrals when a = 0 .
4 A ﬁnite interpolation representation
We now assume
q(t) = R(eit), (12)
where R is rational, has no pole on the unit circle, is real there and has zero circle mean.
Algebraic coeﬃcients will be needed only for the eﬀective decision conclusion.
4.1 The quadrant dual
Lemma 4.1 (Finite dual) . The number aN (q) equals the maximum of
⟨q Im f⟩ − c (13)
over analytic polynomials f of degree at most N such that f(0) = c+i, c ≥ 0, and Re f, Im f ≥
0 on the circle.
Proof. Positive semideﬁnite Gram multipliers for the two Toeplitz constraints correspond to
nonnegative trigonometric polynomials U, V of degree at most N. Every such polynomial has
a Gram representation by Fejér–Riesz. With formal moments of u, ⟨u⟩ = 1 , the Lagrangian
is
b − ⟨uU⟩ − ⟨(b − q − Hu)V ⟩ = b(1 − ⟨V ⟩) + ⟨qV ⟩ − ⟨u(U + HV )⟩ .
We used skew-adjointness of H under the real circle pairing. Stationarity requires ⟨V ⟩ = 1
and U + HV = c constant, with c = ⟨U⟩ ≥ 0. This says exactly that f = U + iV is
analytic, f(0) = c + i. The dual objective is ( 13). The primal is strictly feasible at mk = 0 ,
b > max q; its ﬁnite optimum is attained. Finite-dimensional semideﬁnite strong duality
proves the assertion.
5

Let ζj be the interior poles of R(z)/z, of orders nj. For any analytic f on D, deﬁne the
ﬁnite jet functional
ΛR(f) =
∑
|ζj|<1
Resz=ζj
R(z)f(z)
z . (14)
Only derivatives through order nj −1 at ζj occur. For polynomials, the residue theorem gives
ΛR(f) = ⟨qf⟩. For a general analytic f, ( 14) is the deﬁnition; a boundary integral is not
required.
Proposition 4.2 (Quadrant formulation) . Let Qc be the analytic maps from D to the open
ﬁrst quadrant with f(0) = c + i, where c > 0. Then
A(q) = sup
c>0, f ∈Qc
(
Im ΛR(f) − c
)
. (15)
Proof. Any dual polynomial with c > 0 belongs to Qc by the strong minimum principle for
its two harmonic parts. A dual polynomial with c = 0 is identically i and contributes zero.
Constants c + i already have objectives tending to zero as c ↓ 0.
For f ∈ Q c and r < 1, both parts of f(rz) have positive minima on the closed disk. Its
Taylor polynomials converge uniformly there and eventually preserve both positive parts, with
the same constant term. Their objectives approach Im ΛR(f(r ·)) − c. Every interior jet in
(14) converges to the jet of f as r ↑ 1. The union of the ﬁnite duals therefore has the same
supremum as ( 15).
4.2 Interior jets and a Pick matrix
Include 0 among the nodes, adding multiplicity one if it is not already a pole of R(z)/z.
Let the distinct nodes be ζ1, . . . , ζs, with multiplicities nj, and put m = ∑ nj. Introduce
normalized jet variables
ujp = f(p)(ζj)
p! , 0 ≤ p < n j.
At node 0, impose the value c + i. Require
c > 0, Re uj0 > 0, Im uj0 > 0. (16)
Deﬁne the jets of the proposed square g = f2 by
vjp =
p∑
ℓ=0
ujℓuj,p−ℓ.
Form the Hermitian m × m matrix
P(j,p),(k,ℓ) = ∂p
z ∂ ℓ
¯w
p!ℓ!
g(z) − g(w)
i(1 − z ¯w)
⏐⏐⏐⏐⏐
z=ζj, w =ζk
. (17)
The right-hand side uses only the speciﬁed jets v. In particular for values alone its entry is
(vj0 − vk0)/(i(1 − ζj ¯ζk)).
Lemma 4.3(Classical conﬂuent interpolation) . The tuples satisfying (16), the value condition
at 0, and P ⪰ 0, are exactly the jet tuples of the functions in ⋃
c>0 Qc.
Proof. If f maps to the ﬁrst quadrant, g = f2 maps to the upper half-plane. Its positive Pick
kernel and its derivatives give P ⪰ 0.
Conversely, classical interior conﬂuent Nevanlinna–Pick interpolation provides an analytic
g with Im g ≥ 0 and the prescribed jets when P ⪰ 0, including singular semideﬁnite data.
6

This is the half-plane theorem; see [ 5, Section 3, pp. 246–247], after multiplication of g by −i.
The normalized derivative kernels in ( 17) and the repeated-node basis there are related by an
invertible change of basis. All interpolation nodes are interior.
At zero, g(0) = ( c+i)2 has imaginary part 2c > 0; the minimum principle implies Im g > 0
throughout D. The unique analytic square root taking values in the ﬁrst quadrant exists on the
upper half-plane. The inequalities in ( 16) select this root at each node. Successive derivatives
of f2 = g recover all higher prescribed jets, since the coeﬃcient of the next jet is 2uj0 ̸= 0 .
Theorem 4.4(Finite algebraic threshold) . For a rational proﬁle (12), A(q) is the supremum
of the ﬁnite problem
sup{J(c, u) : ( c, u) ∈ SR}, J (c, u) = Im Λ R(u) − c, (18)
where SR is deﬁned by (16), the value at 0, and P ⪰ 0. If R has algebraic coeﬃcients, SR
is semialgebraic over real algebraic numbers, A(q) is algebraic, and its comparison with any
algebraic number is decidable. The supremum in (18) need not be attained.
Proof. Proposition 4.2 and Lemma 4.3 give ( 18). Interior poles and residue coeﬃcients of an
algebraic rational function are algebraic and eﬀectively computable. Each matrix entry in
(17) is a polynomial of degree at most two in the real jet variables, with algebraic coeﬃcients.
The denominators 1−ζj ¯ζk are nonzero constants. Hermitian positivity can be expressed using
principal minors, or a real symmetric block matrix. Thus SR is semialgebraic and J is aﬃne.
The set is nonempty, and its supremum is ﬁnite and nonnegative by ( 4). For algebraic
a > 0, the condition a > A (q) is the ﬁrst-order real sentence
∃ε > 0 ∀(c, u) [( c, u) ∈ SR =⇒ J(c, u) ≤ a − ε]. (19)
Real quantiﬁer elimination [ 6] decides this sentence. The supremum itself is deﬁned by the
conditions that B is an upper bound and that, for each ε > 0, some feasible J exceeds B − ε.
Eliminating quantiﬁers describes the singleton {A(q)} over the real algebraic numbers. Such a
singleton is algebraic, and real root isolation gives an eﬀective speciﬁcation. No compactness
or maximizer of ( 18) is assumed.
Proof of Theorem 1.1. The no-zero condition on the angular component is decidable on the
unit circle by real quantiﬁer elimination. Reﬂect if needed. The functions F, G have only even
angular frequencies, so F/G is rational in z = e2iθ with algebraic coeﬃcients and no circle
poles. Its mean is a sum of interior residues of (F/G)(z)/z, and hence a in ( 2) is algebraic and
computable; see also [ 9, Supplement, Theorem 20.3]. For a ≤ 0 there is no strict certiﬁcate,
as noted after Proposition 3.2. For a > 0, form R = F/G + a, its interior nodes and the
ﬁnite problem ( 18). Decide ( 19) and apply Proposition 3.2. Equality a = A(q) > 0 yields a
negative answer by the strict threshold theorem.
Remark 4.5. The matrix P has size determined by the poles of the input proﬁle, rather than
a candidate Lyapunov degree. Its entries are quadratic in the jets, so this representation is
not a linear matrix inequality in the displayed variables. Nevertheless, SR is convex: convex
combinations of quadrant maps with Im f(0) = 1 remain in that class, and taking jets is linear.
Lemma 4.3 identiﬁes its image with SR. Thus ( 18) is a convex semialgebraic optimization
problem. This observation alone supplies neither a ﬁnite lifted semideﬁnite representation nor
an eﬃciency bound. The ﬁnite moment programs ( 3) are also convex, but their approximation
alone does not decide equality.
7

5 Polynomial-time additive approximation
The convexity of the jet set has a quantitative consequence. The input model throughout this
section is dense binary rational data: all coeﬃcients or jets up to the indicated degree are
explicit. The statements do not apply to compressed exponent encodings.
Theorem 5.1 (Rational jet data) . Let ζj ∈ Q[i] ∩ D be distinct nodes including zero, with
positive multiplicities nj, and let
Λ(f) =
∑
j,p<nj
bjp
f(p)(ζj)
p! , b jp ∈ Q[i], Λ(1) = 0 .
Over quadrant maps f(0) = c + i, c > 0, deﬁne AΛ = sup(Im Λ( f) − c). For rational
0 < ε ≤ 1, a rational approximation to AΛ with absolute error at most ε can be computed
in time polynomial in the binary encoding of the data and the tolerance. In particular, the
cost for ε = 2 −p is polynomial in p. This is a value approximation, not a polynomial-time
construction of a Lyapunov polynomial.
Proof. Write f = c + iH. Then H(0) = 1 , Re H > 0, and Herglotz representation gives, for
|z| ≤ r < 1,
|H(z)| ≤ U0(r) := 1 + r
1 − r,
⏐⏐⏐⏐⏐
H(p)(z)
p!
⏐⏐⏐⏐⏐≤ Up(r) := 2
(1 − r)p+1 (p ≥ 1). (20)
Take the rational radii rj = (1 + |ζj|2)/2, which dominate |ζj|, and put
B = 1 +
∑
j,p
(| Re bjp| + | Im bjp|)Up(rj).
Since Λ(1) = 0 , the aﬃne objective is J = Re Λ( H) − c ≤ B − c. Constants c + i show
0 ≤ AΛ ≤ B, and near-maximizers may be chosen with c ≤ B + 1.
For 0 < δ ≤ 1/2, let Kδ be the feasible jet set with δ ≤ c ≤ C := 2 B + 2 . It is convex.
Harnack gives the positive closed value bounds
Re f(ζj) ≥ δ 1 − rj
1 + rj
, Im f(ζj) ≥ 1 − rj
1 + rj
.
Add the interval for c and the Pick PSD condition. Lemma 4.3 shows that these closed
conditions characterize Kδ exactly. Equation ( 20) bounds all remaining coordinates, so this
body is compact. Take a nearly optimal map. Its convex combination with the constant 1 + i,
using weights 1 − δ, δ, shows
0 ≤ AΛ − max
Kδ
J ≤ δ(B + 1). (21)
This does not assume attainment of the original supremum.
Put m = ∑ nj and remove the ﬁxed coordinate Im f(0) = 1 , leaving n = 2 m − 1 real
coordinates. Let x0 be the jets of 1 + i, and let the conﬂuent Vandermonde matrix be
V(j,p),ℓ =
(
ℓ
p
)
ζℓ−p
j (0 ≤ ℓ < m ),
with zero entries if ℓ < p . It is invertible. Deﬁne
T = max

1,
∑
a,b
(| Re(V −1)ab| + | Im(V −1)ab|)

, r 0 = (4 T)−1.
8

Any real jet perturbation of Euclidean norm at most r0 has a Hermite interpolating polynomial
p with supD |p| ≤ Tr0 ≤ 1/4. Thus 1 + i + p stays in the quadrant and its anchor has real
part in [3/4, 5/4]. Consequently B(x0, r0) ⊆ Kδ. With U = max j,p Up(rj), the rational radius
R0 = 2 n(C + U + 2) contains Kδ about both zero and x0.
Membership of rational tuples in Kδ is polynomial-time: form the quadratic squared-
map jets and the rational Hermitian Pick matrix, test the scalar bounds, and test PSD by
exact Schur elimination. A negative diagonal rejects; a zero diagonal requires its row to be
zero; a positive pivot allows a Schur complement. Rational pivots are ratios of minors, so
determinant bounds control their bit lengths polynomially. No enumeration of all principal
minors is needed. This exact test is a valid weak-membership oracle.
Apply the classical centered-convex-body oracle theorem of Grötschel–Lovász–Schrijver
[10, Corollary 4.3.12]. Its hypotheses are the rational center, inner and outer radii just exhib-
ited and weak membership. For tolerance η < r 0, it returns ˆx within η of Kδ, whose objective
is at least the maximum on its η-interior minus η. The empty-interior alternative is impossi-
ble because of the inner ball. Write J(x) = w · x + j0, W = max(1 , ∑ |wi|). Contracting a
maximizer toward x0 by η/r0 puts it in that interior and loses at most ηWR 0/r0. Proximity
bounds any excess objective by ηW . Therefore
|J(ˆx) − max
Kδ
J| ≤ η[1 + W(1 + R0/r0)].
Choose
δ = ε
4(B + 1) , η = min
(r0
2 , ε
4[1 + W(1 + R0/r0)]
)
.
Together with ( 21), this gives error at most ε/2. All displayed rational data have polynomial
binary length: powers have exponents O(m), and rational matrix inversion and determinant
bounds control the inverse Vandermonde. Tiny geometric radii aﬀect their logarithms, not
the number of bits exponentially. The oracle theorem bounds both the number and size of its
queries, completing the ordinary Turing polynomial-time reduction.
The theorem uses classical weak optimization, not a new general convex optimization
algorithm or an asserted ﬁnite LMI lift. It already applies to trigonometric polynomials with
rational Fourier coeﬃcients, since their functionals use only jets at zero. Equality and the
size of an explicit certiﬁcate remain separate issues.
5.1 Rational proﬁles with algebraic poles
Exact arithmetic in the compositum of all pole ﬁelds need not have polynomial degree. The
next argument avoids that arithmetic by approximating the objective on a ﬁxed analytic
function class.
Lemma 5.2(Uniform perturbation of the functional) . Let fp = f(p)/p!, and suppose that the
functionals
Λ(f) =
∑
bjpfp(ζj), ˜Λ(f) =
∑ ˜bjpfp(˜ζj)
annihilate constants. Suppose corresponding nodes have the same jet orders and all nodes
have modulus at most ρ < 1. Then
|AΛ − A˜Λ| ≤
∑
j,p
|bjp − ˜bjp|Up(ρ) +
∑
j,p
|˜bjp|(p + 1)Up+1(ρ)|ζj − ˜ζj|.
Proof. Write f = c + iH as before. Constants cancel exactly in both objectives. Since
H′
p = ( p + 1) Hp+1, integrate the derivative bound along the chord between corresponding
nodes. Equation ( 20) bounds the coeﬃcient error. Taking suprema over the same class of
quadrant maps proves the assertion. No continuity claim about perturbed Pick feasible sets
is used.
9

Theorem 5.3 (Polynomial-time value approximation for rational ﬁelds) . Let S = N/D,
N, D ∈ Q[i][z], be given densely, real on the unit circle, with D having no zeros there. Both
µ = ⟨S⟩ and A(S − µ) admit rational additive ε-approximations in time polynomial in the
dense binary input length and the tolerance encoding.
Consequently, given a rational planar homogeneous ﬁeld with nonvanishing angular speed,
and a rational promised separation γ > 0, existence of a strict polynomial Lyapunov function
of some degree can be decided in polynomial time on inputs satisfying |a − A(q)| ≥ γ. For
stable inputs a > 0, this also decides existence of a local analytic weak certiﬁcate under the
same promise. The latter equivalence is not asserted for centers.
Proof. Clear a common denominator of N, D, scaling both together, and put Q = zD. At an
interior root ζj of Q of multiplicity nj, set
Ej(t) =
∑
k≥0
Q(nj+k)(ζj)
(nj + k)! tk, c jp = [ tnj−1−p]N(ζj + t)
Ej(t) .
Then ΛS(f) = ∑ cjpfp(ζj) is the residue functional, and µ = ∑
j cj0. Include the anchor
zero with multiplicity at least one. The normalized functional Λ = Λ S − µf(0) has the same
derivative coeﬃcients, and its zeroth anchor coeﬃcient is
b00 = −
∑
ζj̸=0
cj0.
Thus it annihilates constants without ﬁrst constructing the algebraic mean in a common
number ﬁeld. Removable poles may be cancelled by rational polynomial gcd, or retained with
zero residues.
We record the bit bounds needed to approximate these data. Let n, τ bound degrees and
cleared integer coeﬃcient lengths; both are polynomial in the dense input. Deﬁne Q#(z) =
zdeg QQ(1/¯z). The primitive squarefree part P of
zQQ#Q Q#
is an integer polynomial of polynomial degree and coeﬃcient length; bars on polynomial
factors here conjugate coeﬃcients. Its roots include zero, all roots of Q, and the reciprocal
conjugates of their nonzero roots. Squarefree extraction uses polynomial gcd and preserves
polynomial bit bounds.
For P of degree d0 ≥ 2 and height H0 ≥ 1, Cauchy’s root bound and its nonzero integral
discriminant give the conservative separation σ = (4 H0)−d2
0 between distinct roots. Indeed
all roots have modulus at most 2H0, and isolating one squared distance in the discriminant
product, while bounding every other distance by 4H0, proves this lower bound. When d0 = 1
only zero is relevant and we set σ = 1 . For an interior nonzero root with |ζ| > 1/2,
σ ≤ |ζ − 1/¯ζ| = 1 − |ζ|2
|ζ| , 1 − |ζ| ≥ σ/4.
Hence β = min(1 /2, σ/4) is a lower bound for the distance of every interior node from the
unit circle. The reciprocal argument likewise separates exterior roots from it. Both σ and β
have polynomial binary length.
The multiplicities and number of distinct roots of Q are computed by gcd over Q[i]. Certi-
ﬁed complex root isolation and reﬁnement have polynomial bit complexity here; for example,
the geometric bounds of Mehlhorn–Sagraloﬀ–Wang [ 11, Theorems 3–4] apply. Root mag-
nitudes, inverse separations and inverse products of root diﬀerences in those bounds have
polynomial logarithms by the preceding estimates. The rational coeﬃcient oracle is exact.
Reﬁning to 2−k accuracy therefore costs a polynomial in the original input and k.
10

Residue coeﬃcients have the same approximation property, even at multiple poles. At
multiplicity r, ⏐⏐⏐⏐⏐
Q(r)(ζ)
r!
⏐⏐⏐⏐⏐= | lead(Q)|
∏
w̸=ζ
|ζ − w|mult(w) ≥ σdeg Q.
The leading coeﬃcient is a nonzero Gaussian integer. For an explicit bound let n ≥ 1 dominate
both polynomial degrees, let 2τ bound real and imaginary coeﬃcient parts, and put
C0 = ( n + 1)32τ+2n+4, h = σdeg Q, B 0 = 2 C0/h.
On |z| ≤ 2, C0 bounds all factorial-normalized derivatives of N, Q and their ﬁrst derivatives,
by the binomial theorem. Within distance ρ0 = min(1 /4, h/(2C0)) of the root, the series
denominator’s constant term has modulus at least h/2. Write its coeﬃcients as ej(w), and
those of the translated numerator as aj(w). Series division obeys
tℓ = aℓ − ∑ℓ
j=1 ejtℓ−j
e0
.
Induction gives |tℓ| ≤ B0(1 + B0)ℓ. Diﬀerentiating the recurrence gives
|t′
ℓ| ≤ B0

1 +
∑
k<ℓ
|tk| +
∑
k<ℓ
|t′
k| + |tℓ|

.
A second induction bounds every derivative for ℓ ≤ n by L0 = ( n + 2) B2
0(1 + B0)2n, whose
logarithm is polynomial in the input. Root accuracy min(ρ0, δ/(2L0)), followed by rounding
within δ/2, gives residue error at most δ. Exact rational series evaluation has polynomial
bit growth: at order ℓ its denominator introduces at most ℓ + 1 powers of the common
constant denominator, in addition to polynomial coeﬃcient and evaluation denominators.
Thus the computation is polynomial in the input and requested precision bits, treating each
pole separately.
Let m be the total interior multiplicity including the anchor. Coarse certiﬁed coeﬃcient
enclosures supply rational M ≥ 1 + max |bjp| with polynomial length. Set
ρ = 1 − β/2, U = max
0≤p≤m
Up(ρ), δ = min
(β
8 , σ
8 , ε
8mU(1 + 2 mM)
)
.
Keep zero exact, approximate other nodes within δ, and approximate all coeﬃcients except
b00 within δ/(m + 1) . Set the new anchor coeﬃcient to minus the sum of the other zeroth
coeﬃcients. Every coeﬃcient error is at most δ; constants cancel exactly. Nodes remain
distinct inside radius ρ and |˜bjp| ≤ 2M. Lemma 5.2 bounds the threshold error by mδU +
2m2MδU ≤ ε/8. Theorem 5.1, with tolerance ε/2, approximates the new rational functional.
It need not itself arise from a real circle proﬁle. The total error is less than ε, with polynomial
encoding throughout. Approximating and summing the zeroth residues separately gives the
asserted approximation of the real mean µ.
Finally, a dense rational homogeneous ﬁeld gives Laurent F, G of degree at most (d+ 1)/2,
with polynomial bit cost. Multiplication by that power of z represents F/G with polynomial
numerator and denominator degrees at most d + 1 . After reﬂection if necessary, G > 0;
its denominator has no unit-circle root. Approximate −µ and A to γ/4 to distinguish the
promised cases. For γ ≥ 1, ﬁxed smaller tolerances suﬃce. The strict-certiﬁcate criterion also
rejects a ≤ 0; the equivalence with weak analytic certiﬁcates is used only for a > 0, as in
Theorem 1.1.
11

Neither theorem makes exact equality polynomial-time, bounds the output size of a poly-
nomial certiﬁcate polynomially, or implements the classical oracle algorithm. The gain is
precision dependence: increasing the Jackson hierarchy alone gives no corresponding polyno-
mial bound in log(1/ε). The primary ingredients remain classical interpolation, convex-body
optimization and root reﬁnement; the reduction establishes their hypotheses for this certiﬁcate
threshold.
6 A semialgebraic region of certiﬁcate existence
The preceding construction is uniform in the coeﬃcients, even when interior poles collide or
cancel. This gives a statement about families without ﬁxing a certiﬁcate degree.
Theorem 6.1 (Uniform coeﬃcient region) . Fix an odd integer d ≥ 1. In the coeﬃcient
space R2(d+1) of planar homogeneous ﬁelds of degree d, let Rd denote the ﬁelds whose angular
component has one strict sign, and let Cd ⊂ R d denote those admitting a strict polynomial
Lyapunov function of some degree. Then Cd is open and semialgebraic, with an eﬀectively
constructible ﬁrst-order real deﬁnition over Q. The interpolation matrix in this deﬁnition has
size at most d + 2, including the normalization node at zero.
Proof. The condition deﬁning Rd is a strict sign condition on the unit circle, hence semialge-
braic and open. Treat G > 0; a ﬁxed reﬂection treats G < 0. Put k = ( d + 1)/2. The Laurent
polynomials F, G in z = e2iθ have degrees at most k, so
N(z) = zkF(z), D (z) = zkG(z)
are polynomials of degree at most d + 1 . Their coeﬃcients depend Q[i]-linearly on the ﬁeld
coeﬃcients. The polynomial D is nonzero and has no root on the unit circle.
There are ﬁnitely many degree and root-multiplicity patterns for D. For each pattern
introduce its leading coeﬃcient and distinct complex roots, impose the coeﬃcient identities
for their product, and specify which roots satisfy |ζ| < 1 and which satisfy |ζ| > 1. All these
conditions are real semialgebraic. Taking the ﬁnite union of patterns handles collisions and
degree drops without a continuous choice of root labels.
The mean −a is the sum of interior residues of N/(zD). On a ﬁxed pattern these residues
are rational functions of coeﬃcients and root variables: repeated poles require only ﬁnitely
many derivatives. All denominators are nonzero on the pattern, and auxiliary inverse variables
turn each division into a polynomial equality. This classical mean computation, also explicit
in [ 9, Supplement, Theorem 20.3], therefore deﬁnes a semialgebraically in the parameters.
Set R = N/D+a. In ( 14) and ( 17), use the interior roots of zD with their full denominator
multiplicities. This includes zero with multiplicity at least one. Removable poles may be
retained: their unused residue coeﬃcients vanish. The extra jets do not change the feasible
objectives, because every quadrant map supplies them and Lemma 4.3 still characterizes the
full jet tuples. The total multiplicity is at most deg D + 1 ≤ d + 2. If D(0) = 0 , the node zero
is counted once with its multiplicity increased by one.
Both the residue objective and the Pick matrix entries are rational functions of the root
and coeﬃcient variables, polynomial of degree at most two in the jets. Their denominators,
including 1−ζj ¯ζℓ, do not vanish. Thus the anchor condition, quadrant inequalities and positive
semideﬁniteness are semialgebraic jointly in all parameters. Existentially quantify the root
and mean variables, require a > 0, and then impose ( 19), with its quantiﬁers over the feasible
jets. Any admissible root listing describes the same proﬁle and threshold. The ﬁnite union
of these formulas deﬁnes exactly Cd; real quantiﬁer elimination gives the asserted eﬀective
semialgebraic description over Q.
12

Finally a strict homogeneous certiﬁcate P for X has positive minima of P and −LXP on
the circle. The same P remains strict under small coeﬃcient changes in X, while the sign of
G persists. Proposition 3.2 supplies a homogeneous certiﬁcate at every point of Cd, proving
openness.
Corollary 6.2 (Finitely many parameter transitions) . For a polynomial or rational one-
real-parameter family of ﬁxed odd degree, with real algebraic coeﬃcients and a semialgebraic
parameter domain over the real algebraic numbers, assume its rational denominators do not
vanish on that domain. The parameters where the ﬁeld belongs to Cd form a ﬁnite union of
intervals and points with algebraic ﬁnite endpoints. If the domain is open, this set is relatively
open and has no isolated point.
Proof. Take the inverse image of Cd under the semialgebraic coeﬃcient map. One-dimensional
semialgebraic sets have the stated form; continuity gives the additional openness assertion.
Corollary 6.3 (A computable degree for compact families) . Given a compact semialgebraic
coeﬃcient set K, deﬁned over real algebraic numbers, inclusion K ⊂ Cd is decidable. If it holds,
an algorithm ﬁnds an even degree 2M such that every X ∈ K admits a strict homogeneous
certiﬁcate of degree 2M. The certiﬁcate may depend on X.
Proof. Decide inclusion using Theorem 6.1. A strict homogeneous certiﬁcate at each X ∈ K
works on a neighborhood. Compactness gives a ﬁnite cover with ﬁnitely many certiﬁcate
degrees. Taking positive integer powers raises these certiﬁcates to their least common multiple
degree and preserves strictness. Hence some even degree works throughout K.
For M = 1 , 2, . . ., quantiﬁer elimination decides
∀X ∈ K ∃P ∈ R[x, y]2M ∀(x, y) : x2 + y2 = 1 = ⇒ P(x, y) > 0 and − LXP(x, y) > 0,
where R[x, y]2M denotes homogeneous forms of degree 2M and the existential variables are
their coeﬃcients. The search terminates by the ﬁnite-cover argument. For empty K it may
return degree two. This is a common degree, not necessarily a common polynomial, and no
eﬃciency bound is asserted.
These are consequences of the ﬁnite interpolation representation; they do not give a new
decision procedure for stability itself.
7 Eﬀective separation and a suﬃcient degree
The ﬁnite brackets also have a quantitative use independent of quantiﬁer elimination. If
a < A (q), some aN > a excludes certiﬁcates of every degree. If a > A (q), some aN + EN < a
proves existence. For nonzero separation, it suﬃces to use
N = O
(
max
{
1,
√
∥q′′∥∞
|a − A(q)|
})
.
This statement concerns exact bounds on the ﬁnite optimum. A numerical implementation
needs certiﬁed errors smaller than the separation; ﬂoating solver statuses do not supply them.
Theorem 7.1(Constructive suﬃcient degree) . Let ∆ = a−A(q) > 0 and L = 2 ∑
k≥1 k|qk| <
∞. If L = 0 , P = x2 + y2 is a certiﬁcate. Otherwise let
τ = min {1/2, ∆/(4L)}, r = 1 − τ, M = max
{
1,
⌈ 8πr
∆(1 − r2)
⌉}
.
There is a product of M positive quadratic forms with normalized slack at least ∆/2. When
∆ ≤ 2L, one may use M ≤ ⌈32πL/∆2⌉. The Lyapunov polynomial degree is 2M.
13

Proof. Take a diagonal subsequence of ﬁnite optimizers. The bounds |mk| ≤ 1, aN ≤ max q,
and closedness of every ﬁnite positive cone give compatible full moments. The classical positive
trigonometric moment representation yields a probability measure µ and a positive measure
ν of mass A, with νk = iµk − qk, k ≥ 1. Poisson smoothing at radius r loses at most
∥q − qr∥∞ ≤ L(1 − r) ≤ ∆/4.
The smoothed Herglotz function thus has slack at least 3∆/4.
Choose a cut of the circle with no atom of µ, and use its M midpoint quantiles with
equal weights. Their cumulative discrepancy is at most 1/(2M), also in the presence of atoms.
Integration by parts and the total variation of the Herglotz kernel give, uniformly on the
closed disk,
∥hM − hr∥∞ ≤ 1
2M
∫2π
0
2r
|1 − reit|2 dt = 2πr
M(1 − r2) ≤ ∆/4.
Use ( 10). The last bound on M follows from τ = ∆ /(4L) and r/(1 − r2) ≤ 1/τ.
No optimality of the exponent or constants is claimed. Strict binary forms are sums of
two squares of real forms, so both the constructed P and −LXP admit such decompositions.
This is the classical binary positivity fact, not a new general SOS theorem. A small rational
perturbation of the coeﬃcients of P preserves both strict inequalities on the unit circle. Thus
for a rational input ﬁeld a rational-coeﬃcient certiﬁcate exists whenever the strict criterion
holds. This does not assert a two-square decomposition over the rationals.
8 Two explicit proﬁles
8.1 One harmonic
If q is a trigonometric polynomial of degree s, the functional only uses Taylor coeﬃcients at
zero:
ΛR(f) =
s∑
k=1
qkfk, f 0 = c + i.
Put gk = ∑k
ℓ=0 fℓfk−ℓ. The ﬁnite interpolation condition reduces to
Ts(µ) ⪰ 0, µ 0 = 2 c, µ k = gk/(2i) ( k ≥ 1).
This is the classical Carathéodory–Fejér condition for −ig to have nonnegative real part; its
imaginary constant is unrestricted.
For q = b cos ϕ, b ≥ 0, the 2 × 2 condition is
|f1| ≤ 2c√
1 + c2 .
The objective is (b/2) Im f1 − c, so
A(b cos ϕ) = sup
c>0
( bc√
1 + c2 − c
)
= ( b2/3 − 1)3/2
+ . (22)
The maximum for b > 1 occurs at c =
√
b2/3 − 1; for b ≤ 1 the supremum is zero. Changing the
phase replaces b by |b|. Consequently the stable cubic family with G = 1 and F = −a+b cos 2θ
has a polynomial or analytic weak certiﬁcate exactly when |b| < (1 + a2/3)3/2. The family
itself is from [ 1].
14

8.2 A rational proﬁle with nonconstant angular speed
Consider
q(ϕ) = 3 cos ϕ
1 + (3 /5) cos ϕ + 5
4. (23)
Writing C = 25 /4, r = 1 /3, one has q = C(1 − P−r), where P−r(ϕ) = (1 − r2)/|1 + reiϕ|2.
Thus
ΛR(f) = −C [f(−r) − f(0)].
Set f(0) = c + i, f(−r) = x + iy, with c, x, y > 0. The two-node Pick condition reduces
exactly to
D(c, x, y) := 18 cxy − (c2 − 1 − x2 + y2)2 − 4(c + xy)2 ≥ 0. (24)
Therefore
A(q) = 25
4 − inf
c,x,y>0
D(c,x,y)≥0
(
c + 25
4 y
)
. (25)
Proposition 8.1 (An exact algebraic instance) . Let
R(t) = 16777216 t12 − 8141930496t10 + 1537904087040t8
− 104707265987520t6 + 2126206939995165t4
− 15011745808074246t2 + 81397225546445341.
It has a unique root t∗ in (0, 19/4), and the proﬁle (23) satisﬁes A(q) = 25 /4−t∗. In particular
1.657217310707 < A(q) < 1.657217310708. (26)
The endpoints in (26) are exact decimal rationals.
Proof. The feasible rational triple (c, x, y) = (1 , 1, 3/5) has D = 94 /625 > 0 and objective
19/4 < 25/4. Restrict a minimizing sequence to objective at most 19/4. The equivalent disk
condition ⏐⏐⏐⏐(x + iy)2 −
(
c2 − 1 + 5
2ic
)⏐⏐⏐⏐≤ 3
2c (27)
bounds x, as c, y are already bounded. If c → 0, the squared value tends to −1, forcing x → 0,
y → 1; the objective would tend to 25/4, a contradiction. Hence c is bounded below. The
imaginary part of ( 27) gives 2xy ≥ c, so x, y also stay bounded away from zero. A minimum
is attained in the positive octant and lies on D = 0 .
At a regular minimizing boundary point, the multiplier equations, and at a singular point
the vanishing gradient, imply
D = 0 , D x = 0 , 4Dy − 25Dc = 0 , 4t − 4c − 25y = 0 . (28)
Exact rational elimination in the variable order x, c, y, t gives the univariate eliminant
t2(4t − 25)2(4t + 25)2(t2 + 1)2 R(t). (29)
The supplementary program recomputes a graded reverse lexicographic Gröbner basis over
Q, converts it to lexicographic order, veriﬁes ( 29) and its zero remainder, and performs exact
Sturm root counts. These give one root of R in (0, 19/4), no endpoint root, and one root in
(4592782689292
1012 , 4592782689293
1012
)
.
Since every minimizer satisﬁes ( 28) and 0 < t ≤ 19/4, none of the other factors in ( 29)
vanishes. Existence of the minimum identiﬁes it with the unique root t∗, giving ( 26). No
numerical optimizer is used for global optimality.
15

This is realized by a concrete cubic vector ﬁeld. With
ρ = x2 + y2, H = ρ + 3
5 (x2 − y2), K = ( −a + 5
4 )H + 3(x2 − y2),
take ˙x = Kx−Hy, ˙y = Ky+Hx. Then G = 1+(3 /5) cos 2θ > 0 and F = ( −a+5/4)G+3 cos 2θ.
It is globally asymptotically stable for every a > 0; polynomial and local analytic weak
certiﬁcates exist precisely for a > A (q). The algebraic boundary value is therefore an explicit
equality input to the ﬁnite decision theorem.
8.3 An exact minimum degree
At a = 2 , the preceding cubic has a strict integer-coeﬃcient certiﬁcate, while ﬁnite rational
identities exclude every smaller degree.
Proposition 8.2. For the cubic above at a = 2 , the minimum degree of a polynomial weak
Lyapunov function is eight, even allowing nonhomogeneous polynomials and inequalities only
near the origin, with V (0) = 0 . A homogeneous degree-eight strict certiﬁcate exists globally.
Proof. Deﬁne
P(x, y) = 216 x8 − 2260x7y + 12820x6y2 − 45066x5y3 + 99726x4y4
− 137242x3y5 + 113341x2y6 − 51276xy7 + 9784y8.
The descending x-coeﬃcients of 5(−LXP), of degree ten, are
2528, −28576, 65016, 322736, −1562236, 1039608,
5502688, −13799076, 13740768, −6471612, 1188936.
Exact signed Euclidean Sturm chains for P(t, 1) and −LXP(t, 1) have variations (4, 4) and
(5, 5) at minus and plus inﬁnity, respectively. Neither has a real root. Their values at (0, 1)
are 9784 and 1188936/5, and at the omitted projective point (1, 0) they are 216 and 2528/5.
Homogeneity proves both strict positivities.
For the lower bound write, at degree 2M,
p(ϕ) = p0 + 2 Re
M∑
k=1
pkeikϕ, d (ϕ) = −MF (ϕ)p(ϕ) − G(ϕ)p′(ϕ),
where ϕ = 2 θ, F = −3/4 + (51 /20) cos ϕ, and G = 1 + (3 /5) cos ϕ. On the circle −LXP = 2 d.
Let vM = (1 , 2 cos ϕ, −2 sin ϕ, . . . , 2 cos Mϕ, −2 sin Mϕ)T . For a real rational t, set cos ϕ =
(1 − t2)/(1 + t2), sin ϕ = 2 t/(1 + t2), and
bM (t) = −MF (ϕ)vM (ϕ) − G(ϕ)v′
M (ϕ).
Thus bM (t) is a rational column, and its pairing with the real Fourier coeﬃcients gives d(ϕ).
For the nodes in the following table form BM = [ bM (t1) · · · bM (t2M+1)], and deﬁne w =
−B−1
M (1, 0, . . . , 0)T . These formulas specify the weights exactly over Q.
M Nodes tj sign det BM minj wj >
1 −3/10, 17/20, 9/10 1 1
2 −7/20, 9/20, 1/2, 23/20, 6/5 −1 2
3 −7/20, 1/4, 3/10, 7/10, 3/4, 13/10, 27/20 1 6
16

Direct rational arithmetic gives the nonzero determinants and positive weight bounds dis-
played; the supplementary veriﬁer supplies the full rational weights and checks every coeﬃ-
cient of ∑
j
wjd(ϕj) = −p0.
For a nonzero nonnegative p, its mean p0 is positive. The identity is therefore incompatible
with d ≥ 0, excluding degrees two, four and six over arbitrary real coeﬃcients.
Finally, the ﬁrst nonzero homogeneous term of any local polynomial weak certiﬁcate with
V (0) = 0 is nonnegative, nonzero, of positive even degree, and has nonpositive Lie derivative.
If its total degree were below eight, one of the three excluded cases would occur. The exact
veriﬁer uses no optimizer; numerical searches only discovered the ﬁxed coeﬃcients and support
nodes.
This is a minimum-degree result for this instance. It does not give a general minimum-
degree law or a new positivity technique.
9 A robust obstruction when angular velocity changes sign
The preceding decision and complexity results require nonvanishing angular velocity. A suf-
ﬁcient obstruction extends to angular zeros and yields an explicit open set of stable systems
outside that class. This is not a complete characterization with angular zeros.
Lemma 9.1 (A mean obstruction with boundary factors) . For a homogeneous ﬁeld of odd
degree, let F, G be its real trigonometric polar proﬁles in ϕ = 2 θ, with G ̸≡ 0, and write
G(ϕ) =
s∑
k=−s
γkeikϕ, T G(α) = 2 Im
s∑
k=1
γkαk.
If
⟨F⟩ + min
|α|≤1
TG(α) > 0, (30)
then the homogeneous ﬁeld has no nonzero nonnegative homogeneous polynomial of positive
degree with nonpositive Lie derivative. It consequently has no positive local real-analytic weak
Lyapunov function.
Proof. A nonzero nonnegative homogeneous polynomial has degree 2M > 0 and circle restric-
tion
p(ϕ) = C
M∏
j=1
|1 − αjeiϕ|2, C > 0, |αj| ≤ 1.
Zero parameters may complete the factor list. Where p > 0, the Lie inequality is
F + G Im h ≤ 0, h (z) = 1
M
M∑
j=1
1 + αjz
1 − αjz .
Indeed ˙ϕ = 2 rd−1G and p′/(Mp) = Im h. A zero of p at which G ̸= 0 is impossible: on a
short interval with constant sign of G, the inequality Gp′ + MFp ≤ 0, an integrating factor,
and p ≥ 0 propagate that zero to a one-sided interval. The analytic trigonometric polynomial
would vanish identically.
For |α| < 1, Fourier expansion gives
⟨
G Im 1 + αeiϕ
1 − αeiϕ
⟩
= TG(α).
17

For a boundary factor |α| = 1 , its pole occurs at a zero of G. In a local coordinate t
about this point, G(t) = O(t), so its product with cot(t/2) extends continuously. The radial
regularization has imaginary part
2r sin t
(1 − r)2 + 2r(1 − cos t).
For |t| ≤ π, the inequalities |G(t)| ≤ L|t| and 1 − cos t ≥ 2t2/π2 bound the product uniformly
by Lπ2/2. Away from its pole it converges uniformly. Dominated convergence proves the
same mean identity for boundary factors. Averaging the Lie inequality therefore gives
0 ≥ ⟨F⟩ + 1
M
∑
j
TG(αj) ≥ ⟨F⟩ + min
|α|≤1
TG(α) > 0,
a contradiction. The ﬁrst nonzero homogeneous Taylor term of a positive analytic weak
certiﬁcate is nonnegative, of positive even degree, and has nonpositive Lie derivative. The
same contradiction excludes it; strict positivity of that leading term is not assumed.
Theorem 9.2(A full coeﬃcient box with a common rational certiﬁcate) . Consider the quintic
ﬁeld
f0 = −x5 + 16x3y2 − 3xy4, g 0 = x4y + 20x2y3 − y5.
Independently perturb each of the twelve real coeﬃcients of these two homogeneous quintics
by at most 1/240. Every resulting ﬁeld is globally asymptotically stable, its angular velocity
changes sign, and it admits no positive local analytic weak Lyapunov function. The same
function
V (x, y) = (11x2 + y2)11
(x2 + y2)10 ((x, y) ̸= 0) , V (0) = 0 , (31)
is a proper positive C1 certiﬁcate for the entire box, satisfying LXV ≤ −r4V/5.
Proof. The central polar proﬁles are
F0 = −1 + 5 sin 2 ϕ, G 0 = sin ϕ.
Each perturbing Cartesian component has at most six terms, each bounded by 1/240 on the
unit circle. Hence the changes in both F and G have uniform norm at most ϵ = 1 /20. The
proﬁles have trigonometric degree at most three in ϕ. Consequently
| ⟨F⟩ − 3/2| ≤ ϵ, ∥TG − TG0 ∥∞,D ≤ 6ϵ.
Since TG0 (α) = Re α, the obstruction margin in ( 30) is at least 1/2 − 7ϵ = 3 /20 > 0. Also
G(π/2) ≥ 19/20 and G(3π/2) ≤ −19/20, proving sign change.
For stability set v = ( ∂θ log V )/2. Directly,
v = − 55 sin ϕ
6 + 5 cos ϕ, F 0 + G0v = −1 − 25 sin2 ϕ(1 − cos ϕ)
6 + 5 cos ϕ ≤ −1.
The identity (6 + 5 t)2 − 11(1 − t2) = (5 + 6 t)2 implies |v| ≤ 5
√
11 < 17. Thus, for every ﬁeld
in the box,
F + Gv ≤ −1 + 18 ϵ = − 1
10, L XV = 2 r4V (F + Gv) ≤ − 1
5r4V.
The function satisﬁes r2 ≤ V ≤ 1111r2 and ∇V = O(r), so its extension is C1 and proper.
Its compact sublevel sets ensure forward completeness; the strict Lie inequality gives global
asymptotic stability.
18

Corollary 9.3 (Higher-order local perturbations) . If a locally C1 vector ﬁeld satisﬁes X =
X5 + O(r6), with no terms of degree below ﬁve and X5 in the box of Theorem 9.2, the origin
is locally asymptotically stable and has no positive local analytic weak Lyapunov function.
Proof. The extra contribution to LXV is O(r7), whereas the negative term is at most −r6/5.
The ﬁrst nonzero Taylor term of a putative analytic certiﬁcate is governed by X5 and is
excluded by Lemma 9.1. This argument is local; arbitrary higher-order perturbations need
not preserve global stability.
Liu–Fitzsimmons already establish robust counterexamples within their two-parameter
rotating family [ 1, Section IV.D], using the factorization and Taylor methods that underlie our
lemma. Ahmadi–El Khadir’s rational converse theorem [ 3, Theorem 3.1] already guarantees
rational certiﬁcates for asymptotically stable homogeneous ﬁelds. The speciﬁc additional
conclusions here are the boundary-factor obstruction and a full twelve-dimensional rational
coeﬃcient box with angular sign changes and an explicit common certiﬁcate. The rational
expression is singular at the origin before extension; it is not an analytic certiﬁcate there.
Smooth nonanalytic Lyapunov functions are not excluded.
10 Veriﬁcation, scope and remaining questions
The principal equivalences are analytic proofs. The rational threshold additionally uses exact
symbolic elimination and Sturm counting; its program, equations, output and rational interval
are supplied for reproduction. Proposition 8.2 uses separate exact positivity checks and ra-
tional evaluation identities, including a veriﬁcation that does not call an optimizer. Separate
exact checks verify Fourier signs, Toeplitz quadratic-form identities, atomic quantile discrep-
ancy, the conﬂuent Pick kernel including a singular Gram example, determinant identities and
residues. The coeﬃcient-region proof additionally accounts for pole collisions, removable poles
and degree drops. Its quantiﬁer elimination is theoretical. The complexity results explicitly
invoke classical weak convex optimization and certiﬁed root reﬁnement; neither general algo-
rithm is implemented here. Additional exact checks cover the rational PSD oracle, conﬂuent
Hermite perturbations, irrational simple and repeated residue poles, functional perturbation
bounds on Cayley kernels, and the common rational quintic certiﬁcate. These ﬁnite checks
verify formulas and signs, not the full analytic or bit-complexity proofs. Reviewer checks are
recorded separately.
Floating computations are retained as diagnostics. The hierarchy experiment has ﬁfteen
solves, nine labelled optimal and six optimal_inaccurate. Eight further primal/dual com-
parisons include three inaccurate primal and two inaccurate dual solves. Small negative
numerical duality gaps are not certiﬁed bounds. A six-start numerical search with nonlinear
constraints for the rational example produced ﬁve infeasible failures and one apparent local
success; all are retained. Proposition 8.1 uses the separate exact elimination argument, not
that local success.
AI tools assisted the derivations, computation and writing. Proof dossiers were examined
by the same involved model reviewer requested as GPT-6 Astra with extra-high eﬀort. This
is not blind review, an additional independent vote, human peer review or formal veriﬁcation;
runtime identity is not independently attested. Any exact-manuscript assessment is a separate
record. No Lean proof is supplied.
The literature comparison is targeted, not exhaustive. The original stability counterex-
ample is credited to [ 1]; the kernels, interpolation and quantiﬁer elimination are classical.
Worldwide priority of this connection is unconﬁrmed. The all-degree characterization remains
restricted to nonvanishing angular velocity. Theorem 9.2 supplies a suﬃcient obstruction with
angular zeros, and Corollary 9.3 treats only the stated local higher-order perturbations. No
19

general nonhomogeneous or higher-dimensional classiﬁcation follows. The polynomial-time
claims concern additive values and supplied gap promises in dense encoding; they do not de-
cide equality eﬃciently or produce a polynomial-sized certiﬁcate. Practical certiﬁed solvers,
optimal minimum-degree laws, and a complete certiﬁcate criterion with angular zeros remain
open.
References
[1] J. Liu and M. Fitzsimmons, A globally asymptotically stable planar homogeneous polynomial vector
ﬁeld with no polynomial Lyapunov function , arXiv:2607.16171v1, 17 July 2026. https://arxiv.
org/abs/2607.16171v1.
[2] A. A. Ahmadi and P. A. Parrilo, Stability of polynomial diﬀerential equations: complex-
ity and converse Lyapunov questions , arXiv:1308.6833. https://web.mit.edu/~a_a_a/Public/
Publications/Selected_Papers/dTAC.pdf.
[3] A. A. Ahmadi and B. El Khadir, On algebraic proofs of stability for homogeneous vector
ﬁelds, IEEE Trans. Automat. Control 65 (2020), 325–332. https://optimization-online.org/
wp-content/uploads/2018/03/6502.pdf.
[4] E. de Klerk, R. Hess and M. Laurent, Improved convergence rates for Lasserre-type hierarchies of
upper bounds for box-constrained polynomial optimization , SIAM J. Optim. 27(1) (2017), 347–367.
https://doi.org/10.1137/16M1065264.
[5] D. N. Clark, On matrices associated with generalized interpolation problems , Paciﬁc J. Math. 27(2)
(1968), 241–253. https://msp.org/pjm/1968/27-2/pjm-v27-n2-p04-p.pdf .
[6] A. Tarski, A decision method for elementary algebra and geometry , second edition, University of
California Press, 1951. https://doi.org/10.1525/9780520348097.
[7] M. A. Dritschel and J. Rovnyak, The operator Fejér–Riesz theorem , arXiv:0903.3639. https:
//arxiv.org/abs/0903.3639.
[8] S. Tripathi, F. Ilhan, A. Gokcen, M. Kudeyt, S. Sahin and O. Karabacak, Construction of
Lyapunov certiﬁcates for oscillatory systems , preprint, 26 February 2026. https://doi.org/10.
20944/preprints202602.1723.v1.
[9] M. Korda, Lyapunov stability of polynomial vector ﬁelds is undecidable , arXiv:2609.22058v2, 25
September 2026, and Supplementary material , Part III, pp. 51–59. https://arxiv.org/abs/2609.
22058v2; https://homepages.laas.fr/mkorda/arnold_supplement.pdf.
[10] M. Grötschel, L. Lovász and A. Schrijver, Geometric Algorithms and Combinatorial Optimization ,
Springer, 1988, Corollary 4.3.12 and deﬁnitions in Section 2.1. https://www.zib.de/userpage/
groetschel/pubnew/paper/groetschellovaszschrijver1988.pdf.
[11] K. Mehlhorn, M. Sagraloﬀ and P. Wang, From approximate factorization to root isolation with ap-
plication to cylindrical algebraic decomposition , arXiv:1301.4870v2, 23 January 2014, Theorems 3–
4. https://arxiv.org/abs/1301.4870v2.
20