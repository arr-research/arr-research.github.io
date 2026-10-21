# Interior-zero complexity of polynomial differentiation residuals

Extracted text; the canonical PDF controls mathematical notation.

Interior-zero complexity of polynomial
differentiation residuals
Lluis Eriksson
18 October 2026
Abstract
W e classify the numbers of interior zeros that permit vanishing and superalgebraic dif-
ferentiation residuals for polynomials whose zeros lie in the closed unit disk. If a degree- n
polynomial has exactly M strictly interior zeros, then, for every complex slope, its normalized
H2 residual is at least n/[2
√
2 16M(n + 2M + 4)2M+2]. Consequently a prescribed budget bn
permits a superalgebraically small residual sequence if and only if bn → ∞. Suﬀiciency holds
with real coeﬀicients, normalization at the origin, the slope fixed by that normalization, and
exactly bn interior zeros. In contrast, one interior zero already permits residuals O(n−1/6),
with family-specific asymptotic constant
√
15/44/3, whereas the circle-only infimum tends to
1/
√
8. F or one interior zero we also prove a universal cn−13/6 lower bound; the optimal rate
remains open. The finite-budget obstruction combines a reciprocal identity with classical
Mahler, truncated-shift and Poisson-kernel estimates, and extends to a stable factor times a
self-inversive cofactor. F or unrestricted interior counts we prove exp(−C√n) lower bounds
for every C >
p
(8/3) log 17. The upper construction corrects both the exact slope and de-
gree rounding at every large degree. The resulting refinement of exterior power-sum bounds
uses a known residual method; the negative answer to Erdős Problem 973 was already known.
No matching fixed-budget rates or stretched-exponential upper bounds are claimed.
1 Statement and relation to previous work
All logarithms are natural. The measure on the unit circle is normalized to have mass one. Thus
for P(z) = Pn
j=0 ajzj,
∥P∥2
2 = 1
2π
Z 2π
0
|P(eit)|2 dt =
nX
j=0
|aj|2, ∥P∥∞ = max
|z|=1
|P(z)|.
W riteSn for the nonzero polynomials of exact degree n whose zeros are in D, including multi-
plicity and boundary zeros. Define
sn = inf
P∈Sn
λ∈C
∥P′ − λP∥2
∥P∥2
.
There is no normalization at the origin in this definition.
F or an individual nonzero polynomial write ρλ(P) = ∥P′ − λP∥2/∥P∥2. Our principal
classification concerns the number of strictly interior zeros; all root counts include multiplicity .
Theorem 1 (Finite interior-root budget) . Let P ∈ Sn have exactly M zeros in D, where n ≥ 1
and 0 ≤ M ≤ n. F or every λ ∈ C,
ρλ(P) ≥ n
2
√
2 16M (n + 2M + 4)2M+2 . (1)
In particular, for n ≥ 2M + 4, ρλ(P) ≥ 2−6M−4n−2M−1. Neither the exponent nor the constant
is asserted to be sharp.
1

Theorem 2 (Exact criterion for a growing budget) . Let (bn) be any integer sequence with
0 ≤ bn ≤ n. The fol lowing are equivalent:
1. bn → ∞.
2. There exist Pn ∈ Sn, with at most bn strictly interior zeros, and complex slopes λn, such
that ρλn (Pn) = o(n−A) for every fixed A > 0.
3. There exist real-coeﬀicient Pn ∈ Sn, with Pn(0) = 1 and exactly bn strictly interior zeros,
such that ρP′n(0)(Pn) = o(n−A) for every fixed A > 0.
F or residuals merely tending to zero under the “at most” budget, the necessary and suﬀicient
condition is instead bn ≥ 1 eventual ly, with the same choice of restricted slope available for
suﬀiciency.
No monotonicity of the budget is assumed. The suﬀiciency argument is existential: no
explicit quantitative thresholds for an arbitrary budget are supplied, and extra interior zeros
may lie arbitrarily close to the circle. Section 7 proves these statements and gives a necessary
count for stretched-exponential decay . Their ingredients include classical multiplication and
restricted Jensen estimates [8, 9, 10], and the logarithmic derivative of a finite Blaschke product
[11, Lemma 4.3]. These tools themselves are not new.
Theorem 3. Put C0 =
p
(8/3) log 17. F or every C > C 0 there is NC such that
sn ≥ e−C√n (n ≥ NC). (2)
The fol lowing explicit bound also holds:
sn ≥ e−3√n (n ≥ 104). (3)
F or comparison, T an, W ang, Huang and Chen [1, Theorem 1.1] considered the restricted
infimum
rn = inf
P∈Sn
P(0)=1
∥P′ − P′(0)P∥2
∥P∥2
and proved rn ≥ exp(−(1 + o(1))√n log n). F or an individual normalized polynomial we write
ρ(P) = ∥P′ − P′(0)P∥2/∥P∥2. Theorem 5 identifies the positive limiting residual when every
root lies on the circle. Theorem 13 shows that one interior root suﬀices to make it vanish,
establishing the minimal zero-count threshold. These statements concern the global weighted
boundary norm, including the exact restricted slope.
Since sn ≤ rn, Theorem 3 strengthens that quantitative estimate and allows an arbitrary
scalar slope. Their maximum-point normalization, segment integration and projected Newton
identity are retained here, with attribution. The two changes are a local analytic bound for the
logarithmic derivative and a bounded test polynomial. These remove the logarithmic factor in
the exponent.
Luo, Y ang and Zhu [2, Theorem 1.1] had already proved that exterior power sums cannot
be exponentially small in the degree, answering Erdős Problem 973 negatively . The application
in Section 5 is a quantitative refinement of that established conclusion. No new solution of the
original yes-or-no problem is asserted.
Theorem 4 (Superalgebraic decay). F or every A > 0, there are constants CA, NA such that
rn ≤ CAn−A for every integer n ≥ NA.
The polynomials can be chosen with real coeﬀicients, exactlyMA zeros strictly inside the unit disk,
where MA is independent of n, and al l other zeros on its boundary. The interior zeros approach
1 with distance and radial gap Θ(n−1/3). T ogether with Theorem 3, this implies superalgebraic
decay of both sn, rn, while s1/n
n , r1/n
n → 1.
2

The proof in Section 6 fixes the cancellation order and finite integer multiplicities first, then
lets the reciprocal root scale grow as n1/3. No explicit quantitative bounds are supplied here
on MA, CA, NA or uniform control as A grows. Section 8 explains why a fixed strict root radius
precludes superalgebraic decay of a single sequence.
Approximation by logarithmic derivatives and finite moment realization have substantial
prior history . Komarov [3] obtains geometric approximation on each fixed subdisk by logarith-
mic derivatives of circle-root polynomials; [ 4] also realizes prescribed initial moments with unit
weights. Those interior estimates do not supply the global weighted boundary norm used here,
with a target slope growing with degree. F or example, 1 + zn approximates zero logarithmi-
cally on subdisks but has restricted residual n/
√
2. The present contribution is the combination
of exact slope, global concentration and correction at every large degree, rather than moment
realization alone.
2 The sharp barrier when every zero is on the circle
Let s◦
n and r◦
n denote the same infima as sn, rn, with every zero required to lie on |z| = 1 .
Theorem 5. The unrestricted and restricted circle-root residuals satisfy
lim
n→∞
s◦
n = lim
n→∞
r◦
n = 1√
8.
The lower asymptotic bound also holds in the larger class of self-inversive polynomials. No
finite-degree extremizer is asserted.
Proof. W e first prove the lower bound, allowing an arbitrary complex slope. Rotating the
variable makes this slope real and nonnegative, denoted λ. Self-inversivity permits a constant
phase choice such that
P(eit) = e int/2p(t), p (t) ∈ R, p (t + 2π) = ( −1)np(t).
These operations preserve the unrestricted normalized residual. The familiar phase derivative
n/2 for circle-root polynomials appears explicitly in [5, (1.3)–(1.4)]; here we retain the additional
scalar subtraction. Direct differentiation gives
P′ − λP = e i(n/2−1)t
(n/2 − λ cos t)p − i(p′ + λ sin t p)

.
Integration of the cross term by parts is legitimate because p2 is periodic. Consequently the
squared residual is exactly
R2π
0 [p′2 + (n2/4 + λ2 − (n + 1)λ cos t)p2] dt
R2π
0 p2 dt
. (4)
W riteE(L) for the lowest periodic eigenvalue of −d2/dt2 − L cos t, for L ≥ 0. In odd degree, |p|
is periodic in H1 and has the same quadratic-form values as p. Thus in both parities ( 4) is at
least
gn(λ) = n2/4 + λ2 + E((n + 1)λ).
This is a variational lower bound, not an identification of the periodic and antiperiodic spectra.
The change of variables t = 2 x + π gives E(L) = a0(2L)/4, in the standard Mathieu con-
vention −d2/dx2 + 2q cos(2x); see [ 7, §28.2]. The use of this ground state in circular variational
problems is classical; compare [6, §VI.A.2]. The fixed-index expansion [ 7, (28.8.1), m = 0 , s = 1 ]
is
a0(q) = −2q + 2√q − 1
4 + O(q−1/2), E (L) = −L +
p
L/2 − 1
16 + O(L−1/2).
3

W e must minimize uniformly over λ, rather than applying this expansion only at a fixed shift.
The variational principle gives E(L) ≥ − L and Lipschitz continuity , so gn is continuous and
coercive, with
gn(λ) ≥ (λ − (n + 1)/2)2 − (2n + 1)/4.
The trial value λ = n/2 + 1/4 gives gn = 1 /8 + O(n−1). Every minimizer therefore has the form
n/2 + cn, where cn = O(√n). On this window (n + 1)λ ≍ n2, and the displayed single-variable
Mathieu remainder is uniformly O(n−1). Expanding its square root uniformly on the same
window yields
gn(n/2 + c) = ( c − 1/4)2 + 1
8 + O((c2 + 1)/n).
The upper bound on the minimum and absorption of the c2
n/n term imply cn = O(1). Applying
the expansion again proves infλ≥0 gn(λ) = 1 /8 + O(n−1). This supplies the required lower limit,
also for the restricted slope.
F or the upper bound, write n = 6 m + k, 0 ≤ k ≤ 5, and for m ≥ 3 choose
cm,k = cos tm,k = 1
2 + 2k − 1
8m ,
Bt(z) = (1 + z)4(1 − 2 cos t z + z2),
Pm,k(z) = Btm,k (z)m(1 + z)k.
All zeros lie on the circle, Pm,k(0) = 1 , and
P′
m,k(0) = n/2 + 1 /4, P ′
m,k(1)/Pm,k(1) = n/2.
The limiting factor is B∗ = (1 + z)4(1 − z + z2). With s = sin 2(θ/2), its squared normalized
modulus is cos6(θ/2) cos2(3θ/2), with a unique maximum at θ = 0 , and its logarithm is −3θ2 +
O(θ4). More explicitly , for the perturbed factor this modulus is
Hc(s) = (1 − s)4

1 − 2s
1 − c
2
.
Its secondary maximum has value (1 + c)6/[729(1 − c)2] < 1 for 0 ≤ c ≤ 3/4. All six parameter
sequences eventually lie in this interval. Local negative curvature and the strict outer gap are
uniform as c → 1/2. They give Gaussian domination near zero and an exponentially small outer
tail.
F orFm,k = P′
m,k/Pm,k − P′
m,k(0), the identity
B′
∗/B∗ − 3 = −3z(z − 1)2
z3 + 1
shows, on putting θ = u/√m, that
Fm,k(eiθ) − → −1
4 + 3
2 u2, |Pm,k(eiθ)/Pm,k(1)|2 − →e−3u2
.
Indeed the constant term of Fm,k at 1 is exactly −1/4, its linear term is O(1), and its quadratic
term is −3m/2 + O(1). A fixed zero-free neighborhood gives the local bound C(1 + |θ| + mθ2);
after rescaling, a polynomial times a Gaussian dominates. On the outer interval, differentiate
the polynomial product, removing one factor. Uniformly bounded normalized factor derivatives
give an outer squared numerator O(m2q2m−2), for some q < 1. Thus no estimate at a pole of
the logarithmic derivative is required. The ratio of the complete integrals tends to
R
R(−1/4 + 3 u2/2)2e−3u2
duR
R e−3u2
du = 1
16 − 3
4 · 1
6 + 9
4 · 1
12 = 1
8 .
Uniformity over the six values of k covers every suﬀiciently large degree. This proves the upper
bound for r◦
n, and s◦
n ≤ r◦
n completes both limits.
4

3 A finite residual certificate
W e first give conditions that can be checked at a fixed degree. The asymptotic and explicit
choices will then be elementary .
Lemma 6 (Normalization and separation) . Suppose P ∈ Sn, λ ∈ C, y > 0, and
∥P′ − λP∥2
∥P∥2
≤ e−y,
√
n + 1 e −y ≤ 1.
Set
γn = 2 + log(2
√
n + 1), η = y − γn
n . (5)
If η > 0, there are numbers v1, . . . , vn and moments mk = n−1 P
j vk
j such that
m1 ∈ R, m 1 ≥ 1
2 , Re vj ≥ 1
2 , |vj|2 ≤ Re vj
η . (6)
They are the reciprocals vj = (1 − βj)−1 of the complex displacements from the zeros to a
normalized maximum point.
Proof. This is the normalization and separation argument of [1, Sections 2.1–2.2], with the scalar
slope left arbitrary . Choose |τ| = 1 at a maximum of |P|, and put
G(w) = P(τw)
P(τ) , µ = τλ, E = G′ − µG.
The denominator is nonzero because P is nonzero. W e have G(1) = ∥G∥∞ = 1 , ∥G∥2 ≤ 1, and
∥E∥2 ≤ e−y. Differentiating |G(eit)|2 at its maximum shows that d = G′(1) is real. Bernstein’s
polynomial inequality gives |d| ≤ n. The coeﬀicient bound ∥E∥∞ ≤ √n + 1∥E∥2 therefore yields
|µ − d| = |E(1)| ≤ 1, |µ| ≤ n + 1. (7)
Let β be any zero of G, and set δ = 1 − Re β. Integrating the exact ODE along the segment
from β to 1 gives
1 =
Z 1
β
eµ(1−w)E(w) dw.
That segment lies in D. On it, Re(µ(1 − w)) ≤ nδ + 2, using d ∈ R, |d| ≤ n, |µ − d| ≤ 1, and
|1 − β| ≤ 2. Consequently
1 ≤ 2
√
n + 1 e nδ+2−y, δ ≥ η.
No zero equals 1, since G(1) = 1 . F or v = (1 − β)−1,
Re v = 1 − Re β
|1 − β|2 ≥ 1
2 , |v|2
Re v = 1
1 − Re β ≤ 1
η .
Finally nm1 = G′(1)/G(1) = d, so m1 is real and at least 1/2.
Lemma 7 (Local analytic estimate) . With the normalization above, let r > 0 and suppose
q = r
√
n + 1 exp
 
−y + (2n + 1)r

≤ 1
2 . (8)
Then G has no zero in |w − 1| ≤ r, and, for every integer k ≥ 2,
|mk| ≤ 2√n + 1
n exp
 
−y + (2n + 1)r

r1−k. (9)
5

Proof. The disk centered at 1 can extend beyond D; the needed control there comes from the
coeﬀicients. F or |u| ≤ r,
|E(1 + u)| ≤
√
n + 1(1 + r)n∥E∥2 ≤
√
n + 1 e −y+nr.
Solving the ODE from G(1) = 1 gives
G(1 + u) = e µu(1 + h(u)), h (u) =
Z u
0
e−µsE(1 + s) ds.
Using the straight segment and ( 7), we obtain |h(u)| ≤ q ≤ 1/2. Thus G is nonzero on that
closed disk and on a neighborhood of it. The analytic function F = G′/G − µ = E/G satisfies
|F(1 + u)| ≤ 2
√
n + 1 e −y+(2n+1)r (|u| ≤ r).
Cauchy’s derivative estimate and logarithmic differentiation give
|F(k−1)(1)|
(k − 1)! ≤ 2
√
n + 1 e −y+(2n+1)rr1−k, F (k−1)(1) = ( −1)k−1(k − 1)! nmk.
This proves ( 9). There is no restriction k ≤ n + 1 : F is an analytic rational function on the
specified disk.
Proposition 8 (Finite certificate). Fix n ≥ 1, y, r > 0, and an integer K ≥ 2. Define η by (5)
and set a = 2 η. Suppose 0 < η ≤ 2, √n + 1e−y ≤ 1, and (8) holds. Put
B = 2√n + 1 r
Kan exp

−y + (2n + 1)r + K log

1 + a
r

. (10)
If
1
Kη + B < 1
2, (11)
then sn ≥ e−y.
Proof. Suppose an admissible P, λ had residual at most e−y. F or the numbers in Lemma 6,
|1 − avj|2 = 1 − 2a Re vj + a2|vj|2 ≤ 1.
Use the bounded Cesàro test
Ψ(v) = 1 − (1 − av)K
Ka = v +
KX
k=2
(−1)k+1
K
K
k

ak−1vk. (12)
It has zero constant coeﬀicient, linear coeﬀicient one, and |Ψ(vj)| ≤ 2/(Ka) = 1 /(Kη). By
Lemma 7, its remaining averaged terms have modulus at most
2√n + 1 r
Kan e−y+(2n+1)r

1 + a
r
K
− 1 − Ka
r

≤ B.
The triangle inequality and m1 ≥ 1/2 now imply
1
2 ≤ m1 ≤

1
n
X
j
Ψ(vj)

+ B ≤ 1
Kη + B,
contrary to (11). Each individual residual is therefore larger than e−y; taking its infimum gives
the asserted non-strict bound.
6

4 Choice of parameters
Proof of (2). Fix C > C 0, and choose t > 0 so small that
C2 > 4
3(2 + t) log 17.
Set
y = C√n, r = y
8n, η = y − γn
n , K =
2 + t
η

.
F or all suﬀiciently large n, the preliminary conditions of Proposition 8 hold: η ∼ C/√n, q → 0,
and √n + 1e−y → 0. Also Kη ≥ 2 + t, leaving a fixed positive margin in ( 11). W e have
K ∼ 2 + t
C
√n, a
r → 16,
and hence
−y + (2n + 1)r + K log(1 + a/r)√n − → −3C
4 + 2 + t
C log 17 < 0.
The prefactor in ( 10) is O(n−1). Thus B → 0, and the finite certificate applies.
Proof of (3). T aken ≥ 104 and choose
y = 3 √n, r = 3
8√n, K =
21
10η

.
First,
γn ≤ 3
20
√n, 19
20
y
n ≤ η ≤ y
n. (13)
Indeed γn/√n decreases for n ≥ 104, since the sign of its derivative is that of n/(n+ 1) −γn < 0.
At n = 10 4, γn < 10 < 15: e8 > 28 = 256 > 2
√
10001 suﬀices for the first inequality . In
particular 0 < η < 2. The condition √n + 1e−y < 1 is immediate, and
q = 3
8
r
1 + 1
n exp

−9
4
√n + 3
8√n

< 1
2.
Moreover Kη ≥ 21/10, so
1
2 − 1
Kη ≥ 1
42.
F rom (13) we obtain a/r ≤ 16 and K ≤ (14/19)√n + 1. Using log 17 < 3,
−y + (2n + 1)r + K log(1 + a/r) ≤

−9
4 + 14
19 log 17
√n + log 17 + 3
8√n
< − 3
76
√n + 3 + 3
8√n < 0.
The last expression decreases withn and is negative at104. F or an elementary check oflog 17 < 3,
the exponential series through degree five gives e3 > 18 > 17. Finally Ka ≥ 21/5, and therefore
2√n + 1 r
Kan ≤ 5
28n
r
1 + 1
n < 1
5n.
It follows that B < 1/(5n) ≤ 1/50000 < 1/42. All conditions of Proposition 8 are satisfied.
Remark 9. The constants 3 and 104 are convenient explicit choices. The same proof with
r = sy/n, 0 < s < 1/2, gives the suﬀicient asymptotic condition
C2 > 2 log(1 + 2 /s)
1 − 2s .
W e uses = 1 /8 to state a simple constant. Neither this expression nor C0 is asserted to be the
optimal residual constant.
7

5 Exterior power sums and Hardy norms
Corollary 10. Let |zj| ≥ 1, 1 ≤ j ≤ n, and write Mn = max 2≤k≤n+1 | P
j zk
j |. Then
Mn ≥ 1
ne−3√n (n ≥ 104).
F or every C > C 0, uniformly over al l such configurations, Mn ≥ n−1e−C√n for al l suﬀiciently
large n. No distinguished point z1 = 1 is needed.
Proof. W e use the projected Newton identity of [1, Proposition 3.1]. Put P(t) = Qn
j=1(1 − zjt)
and pk = P
j zk
j . Then P ∈ S n, P(0) = 1 , and P′(0) = −p1. Logarithmic differentiation near
zero, followed by coeﬀicient projection onto degrees at most n, gives exactly
P′ − P′(0)P = −Π≤n
" n+1X
k=2
pktk−1
!
P
#
.
Projection is contractive in H2, and multiplication by a polynomial S has H2 norm at most
∥S∥∞. Thus
sn ≤ ∥P′ − P′(0)P∥2
∥P∥2
≤
n+1X
k=2
|pk| ≤ nMn.
Apply Theorem 3.
The factor 1/n is retained in these finite statements. It can be absorbed in a leading square-
root exponent with any strictly larger constant. This corollary strengthens the scale in [ 1]; the
earlier qualitative conclusion of [ 2] remains fully credited.
Corollary 11. Uniformly for 1 ≤ p ≤ ∞, P ∈ Sn, and λ ∈ C,
∥P′ − λP∥Hp
∥P∥Hp
≥ e−3√n
√n + 1 (n ≥ 104).
F or every C > C 0, the lower bound e−C√n holds for al l suﬀiciently large n, uniformly over the
same parameters.
Proof. W riteR = P′ −λP, of degree at most n. F or1 ≤ p ≤ 2, bounding each F ourier coeﬀicient
by ∥R∥1 gives
∥R∥2 ≤
√
n + 1∥R∥1 ≤
√
n + 1∥R∥p, ∥P∥2 ≥ ∥P∥p.
F orp ≥ 2, use
∥R∥2 ≤ ∥R∥p, ∥P∥p ≤ ∥P∥∞ ≤
√
n + 1∥P∥2.
In both cases ∥R∥p/∥P∥p ≥ (∥R∥2/∥P∥2)/√n + 1. F or the asymptotic statement, first apply
Theorem 3 with a constant strictly between C0 and C, and absorb 1
2 log(n + 1) = o(√n).
6 Superalgebraic upper bounds
W e prove the upper statement by cancelling a prescribed finite number of logarithmic-derivative
terms at a strict global maximum. All constants in this section may depend on the prescribed
cancellation order K. They are not asserted to be uniform as K → ∞.
8

Lemma 12 (A finite positive moment cone). Fix K ≥ 3. F or a rational point ζ = x+ iy, x > 0,
y ≥ 0, define the real column
V (ζ) =
(
(ζ2, . . . , ζ K)T , y = 0 ,
(2 Re ζ2, . . . , 2 Re ζK)T , y > 0.
There is a finite col lection of these columns whose cone is RK−1. The col lection can contain
any prescribed K distinct positive rational real points. Its column matrix A∞ admits a strictly
positive rational vector α0 satisfying
A∞α0 = (0 , 3/2, 0, . . . , 0)T .
Proof. A linear functional nonnegative on every such column would give a harmonic polynomial
h(z) = Re PK
j=2 ajzj nonnegative on Re z > 0, by density and conjugation symmetry . If its
largest nonzero degree is l ≥ 2, choose θ ∈ (−π/2, π/2) with al cos(lθ) < 0. Then h(teiθ) < 0
for large t, a contradiction. Thus the dual cone is zero and the closure of the generated cone is
the whole space. Approximate each positive and negative coordinate vector by a finite conical
combination closely enough that their convex hull still contains zero in its interior. The finite
union of the columns used in these combinations already generates the whole space. Append
the prescribed real points if necessary .
The resulting rational matrix has full row rank. F or each column si, express −si as a
nonnegative combination of its columns. This representation can be rational: a nonempty
rational polyhedron has a rational point. Adding these relations for all i gives a rational kernel
vector with every coordinate strictly positive. A rational solution of the displayed full-rank
system exists; adding a suﬀiciently large positive rational multiple of that kernel vector makes
all of its coordinates positive.
6.1 A fixed number of interior zeros
F or a real reciprocal variable v > 1, put β = 1 − 1/v and fv(z) = 1 − z/β. F or v = x + iy,
y > 0, use the conjugate-pair factor fv(z) = (1 − z/β)(1 − z/β). W rite νv = 1 , 2, respectively ,
and define
Mj(v) =
(
vj, v real,
2 Re vj, ℑv > 0, d(v) =
(
−v2/(v − 1), v real,
2 Re[−v2/(v − 1)], ℑv > 0.
Thus d(v) = f′
v(0) − f′
v(1)/fv(1), and Re v > 1/2 is equivalent to |β| < 1. Use the circle-root
baseline
B(z) = (1 + z)4(1 − z + z2), b j =
X
β: B(β)=0
(1 − β)−j.
It has degree six, constant coeﬀicient one, B′(0) = B′(1)/B(1) = 3 , b2 = 0 , and b3 = −3/2.
Proof of Theorem 4. Fix K ≥ 3. Apply Lemma 12, with K designated distinct positive real
nodes among the ζi. Clear the denominators of its strictly positive weights by an integer Q, and
put mi = Qα0
i . These are positive integer group multiplicities, fixed independently of n. Set
M =
X
i
νimi, S =
X
i
miM1(ζi) > 0.
The moments of orders 2, . . . , K are now (0, 3Q/2, 0, . . . , 0). F or every large integer n, define
R = ( n/(6Q))1/3, ϵ = R−1, c n ≡ n−M (mod 6) , |cn−2SR| ≤ 3, b n = ( n−M−cn)/6.
9

Choose a nearest integer in the specified congruence class; both bn, cn are positive eventually .
Then tn = cn/R = 2 S + O(ϵ) and un = bn/R3 = Q + O(ϵ2).
Let ξi vary near ζi, varying only the K designated real nodes. Define dϵ(ξ) = −ξ2/(ξ − ϵ)
for a real node, and twice its real part for a pair. Consider the K equations
0 = t/2 +
X
i
midϵ(ξi), (14)
0 = tϵ/4 +
X
i
miM2(ξi), (15)
0 = bjuϵj−3 + t2−jϵj−1 +
X
i
miMj(ξi), 3 ≤ j ≤ K. (16)
They vanish at (ϵ, t, u, ξ) = (0 , 2S, Q, ζ). The Jacobian in the designated real positions has
columns
mi(−1, 2ζi, 3ζ2
i , . . . , Kζ K−1
i )T .
It is a nonsingular scaled V andermonde matrix. The real implicit-function theorem at this fixed
limiting point gives ξi,n = ζi + O(ϵ) solving the equations at (ϵ, tn, un). Put vi,n = Rξi,n and
Pn(z) = B(z)bn (1 + z)cn
Y
i
fvi,n (z)mi .
F or large n, its degree is exactly n, its constant coeﬀicient is one, and its coeﬀicients are real.
Exactly M zeros, counted with multiplicity , lie strictly inside the disk; the other n − M lie on
the circle. The interior zeros satisfy |1 − βi,n| ≍ 1 − |βi,n| ≍ R−1. Multiplying ( 14)–(16) by
R, R2, . . . , RK, respectively , gives the exact identities
λn := P′
n(0) = P′
n(1)/Pn(1),
X
β: Pn(β)=0
(1 − β)−j = 0 (2 ≤ j ≤ K).
In particular integer rounding has been corrected, and λn = 3 bn + cn/2 + R P
i miM1(ξi,n) =
O(n).
W e give global estimates before using the cancellations locally . F ors = sin 2(θ/2),
|B(eiθ)/B(1)|2 = cos 6(θ/2) cos2(3θ/2) ≤ e−3s, |(1 + e iθ)/2|2 ≤ e−s.
F or a real group v = x > 1, its normalized squared modulus is 1 + 4 x(x − 1)s ≤ eT(v)s, with
T(v) = 4 x(x −1). F or a pair set Y = y2, U = x2 + Y , V = ( x −1)2 + Y . Its normalized squared
modulus is
1 + 8( x2 − x − Y )s + 16UV s 2 ≤ (1 + 4
√
UV s )2 ≤ e4(U+V )s.
Indeed UV − (x2 − x − Y )2 = (2 x − 1)2Y ≥ 0. Set T(v) = 4( U + V ) for this group. The fixed
number of interior factors has total cost P
i miT(vi,n) = O(R2). Since R ≍ n1/3,
3bn + cn −
X
i
miT(vi,n) = n/2 − O(R2) ≥ κn
for some fixed κ > 0 and all suﬀiciently large n. It follows globally that
|Pn(eiθ)/Pn(1)|2 ≤ exp[−κn sin2(θ/2)]. (17)
The zero-free neighborhood now shrinks with n. Choose a fixed δ > 0 so that on |z−1| ≤ δ/R
all |vi,n(z − 1)| ≤ 1/2, and the baseline zeros are excluded. Expanding v/(1 + v(z − 1)), the
exact cancellations above give
|P′
n(z)/Pn(z) − λn| ≤ CK(n + RK+1)|z − 1|K ≤ CKRK+1|z − 1|K. (18)
10

The geometric-series remainder is uniform on this shrinking disk. There are O(n) baseline
reciprocal variables of bounded size and onlyM interior variables of sizeO(R). By real symmetry
the first angular derivative of the normalized log modulus vanishes at zero; its second derivative
on a suitably smaller arc |θ| ≤ δ′/R is O(n + R2) = O(n). Hence the normalized squared
denominator is at least cn−1/2, by integration over |θ| ≤ n−1/2. Combining ( 17) and ( 18), the
local squared numerator is at most
CKR2K+2
Z
R
θ2Ke−cnθ2
dθ ≤ CKR2K+2n−K−1/2.
Outside the small arc use the polynomial product derivative. Normalized derivatives of a
baseline or extra factor are bounded; those of a real interior factor are O(R), and those of a pair
are O(R2). Removing a baseline factor reduces the positive global cost by three, removing an
extra factor reduces it by one, and removing an interior group increases it by its positive T(v).
Thus every derivative term is bounded by a polynomial in n times the same Gaussian bound,
up to a constant. On the outer arc n sin2(θ/2) ≥ cn/R2 ≍ n1/3. Its squared integral is therefore
at most poly(n)e−cn1/3
, negligible compared with every fixed inverse power. This estimate uses
no rational quotient at a boundary zero. Dividing by the denominator proves
ρ(Pn)2 ≤ CKR2K+2n−K ≤ CKn(2−K)/3, ρ (Pn) ≤ CKn(2−K)/6.
Choose K ≥ 6A + 2. Then MA = M is independent of n, as required. No explicit quantitative
bounds are supplied here on MA, CA, or the starting degree as functions of A.
Theorem 13 (One interior zero suﬀices) . F or every suﬀiciently large integer n, there is a real
degree-n polynomial Pn, with Pn(0) = 1 , exactly one zero strictly inside the unit disk and al l
remaining zeros on the circle, such that ρ(Pn) = O(n−1/6). The interior zero is real and positive,
with distance and radial gap from 1 of ordern−1/3. In conjunction with Theorem 5, the minimum
number of interior zeros permitting a sequence with vanishing residual is exactly one. No optimal
rate for one interior zero is asserted.
Proof. W e use two adjustable circle angles in the degree-34 baseline
Ba,c(z) = (1 − 2az + z2)15(1 − 2cz + z2)2, −1 < a, c < 1.
Its slope difference and second reciprocal moment are, respectively ,
D(a, c) = −30a − 4c − 17, T (a, c) = − 15a
1 − a − 2c
1 − c.
Both vanish at (a∗, c∗) = ( −2/3, 3/4). W rite n − 1 = 34 m + k, 0 ≤ k ≤ 33, and let v = vn > 3/2
be the unique solution of
v3 − 3
2 v2 = ( n − 1)/4. (19)
The left side is strictly increasing on this interval, and v ∼ (n/4)1/3. Set β = 1 − 1/v ∈ (0, 1).
F or largen, m > 0. Define the real targets
dn = v2/(v − 1) − k/2
m = O(n−2/3), t n = −v2 − k/4
m = O(n−1/3).
The following explicit formulas select circle parameters solving D(an, cn) = dn, T(an, cn) = tn:
L = (51 + dn)/2, U = 17 − tn,
X = UL + 221 +
p
(UL − 289)(UL − 169)
30U ,
Y = ( L − 15X)/2, a n = 1 − X, c n = 1 − Y.
11

Indeed these equations are equivalent to 15X + 2 Y = L, 15/X + 2 /Y = U; elimination gives
15UX 2 −(UL +221)X +15L = 0 . The positive-square-root branch above tends to X = 5 /3, Y =
1/4, since UL → 867/2 and the square root tends to 391/2. The denominators and discriminant
stay positive, and an, cn ∈ (−1, 1) eventually , with deviations O(n−1/3) from (a∗, c∗). These
statements are uniform over the 34 values of k.
Put
Pn(z) = Ban,cn (z)m(1 + z)k(1 − z/β).
It has exactly the claimed degree, constant term and zero locations. The two target equations
give the exact identities
P′
n(0) = P′
n(1)/Pn(1) =: λn,
nX
j=1
v2
j = 0 , v j = (1 − βj)−1.
Here the extra roots at −1 contribute k/2 to the slope difference and k/4 to the second moment;
the interior root contributes −v2/(v − 1) and v2, respectively . F or a conjugation-symmetric
multiset of N circle roots avoiding 1, its reciprocal moments satisfy
M◦
3 = 3
2 M◦
2 − N/4. (20)
This follows for each pair 1/2 ± iy, and also for the real reciprocal 1/2. Conjugation symmetry
is essential and holds here. T aking N = n − 1 and M◦
2 = −v2, ( 19) gives P
j v3
j = 0 exactly .
Moreover λn = ( n − 1)/2 + v = O(n).
W e verify the global norm control for this new baseline. In s = sin 2(θ/2), its limiting
normalized squared modulus is
H(s) = (1 − 6s/5)30(1 − 8s)4, 0 ≤ s ≤ 1.
Apart from its zeros 1/8, 5/6, the only interior stationary point is 5/24. Its values there and at
1 are
H(5/24) = (3 /4)30(2/3)4 < 1, H (1) = 7 4/530 < 1.
Since H(0) = 1 , zero is the unique global maximum. Also log H(s) = −68s + O(s2). The
nearby circle parameters retain uniform negative curvature near zero and, by compactness, a
strict modulus gap away from zero. Therefore, for some fixed κ > 0 and all suﬀiciently large n,
|Ban,cn (eiθ)/Ban,cn (1)|2 ≤ e−κs (−π ≤ θ ≤ π).
The interior factor contributes 1+4v(v−1)s ≤ exp(4v(v−1)s), whereas the −1 factors contribute
at most e−ks. Since m ∼ n/34 and v2 = O(n2/3), κm + k − 4v(v − 1) ≥ cn eventually . Thus
|Pn(eiθ)/Pn(1)|2 ≤ exp[−cn sin2(θ/2)] (21)
globally , for a fixed c > 0.
The circle reciprocals are uniformly bounded and only the interior reciprocal is large. On
|z − 1| ≤ δ/v, for a fixed small δ > 0, all denominators below stay separated from zero. The
exact slope and moment cancellations imply
Fn(z) := P′
n(z)/Pn(z) − λn = −(z − 1)3
nX
j=1
v4
j
1 + vj(z − 1).
Consequently |Fn(z)| ≤ C(n + v4)|z − 1|3 ≤ Cn4/3|z − 1|3. On a smaller angular window of
radius δ′/v, real symmetry makes the first derivative of the normalized log modulus zero at zero,
and its second derivative is O(n + v2) = O(n). As n−1/2 = o(v−1), integration on |θ| ≤ n−1/2
12

bounds the normalized squared denominator below by c′n−1/2. The local squared numerator is
at most
Cn8/3
Z
R
θ6e−c′nθ2
dθ = O(n−5/6).
On the outer arc differentiate the polynomial product, avoiding logarithmic-derivative poles.
The normalized derivative of a baseline factor is uniformly bounded, its multiplicity is O(n),
and the normalized interior derivative is v. Removing a baseline loses only κ in the global
exponent; removing the interior factor improves it. The extra-factor multiplicity is bounded.
The term −λnPn costs at most another O(n). Thus the outer squared integral is bounded by
a polynomial in n times exp(−c′n/v2) = exp( −c′′n1/3). Dividing both numerator estimates by
the same denominator gives ρ(Pn)2 = O(n−1/3), as required.
Finally , Theorem 5 excludes vanishing residuals with zero interior roots; this construction
permits them with one. This proves the zero-count threshold, not a sharp rate or the superal-
gebraic conclusion with one root. No explicit starting degree is claimed. The next proposition
identifies the asymptotic norm constant of this particular family .
Proposition 14 (Asymptotic constant for the explicit family). F or the polynomials constructed
in Theorem 13, through al l suﬀiciently large integer degrees,
ρ(Pn) ∼
√
15
44/3 n−1/6.
This constant describes that family, not a universal one-root optimum.
Proof. Retain the construction’s notation and put Gn = Pn/Pn(1), Fn = P′
n/Pn − λn, and
w = z −1. Its reciprocal zeros satisfy S1 = λn = ( n−1)/2+ v, S2 = S3 = 0 , and v/n1/3 → 4−1/3.
All boundary reciprocal zeros are uniformly bounded. The exact finite geometric remainder is
Fn(z) = −w3 X
j
v4
j
1 + vjw.
At z = exp( iu/√n), for each fixed real u, the boundary contribution to the sum is O(n), whereas
the single interior contribution is asymptotic to v4. Hence
n1/6Fn(eiu/√n) − →i4−4/3u3. (22)
The local logarithm, normalized to vanish at 1, has expansion
log Gn(1 + w) = λnw + O((n + v4)|w|4),
by the exact second- and third-moment cancellations. F or fixed u the remainder tends to zero,
and λn/n → 1/2, giving
|Gn(eiu/√n)|2 − →e−u2/2. (23)
The preceding proof gives the global Gaussian bound |Gn(eit)|2 ≤ exp[−cn sin2(t/2)], and lo-
cally |Fn(z)| ≤ Cn4/3|z−1|3 for |z−1| ≤ δ/v. In the rescaled variable u = t√n, the denominator
is dominated by exp(−c′u2). On the local region the rescaled numerator n1/3|GnFn|2 is domi-
nated by C|u|6 exp(−c′u2); that region expands to the whole line at rate n1/6. Outside it, the
product-derivative tail estimate from the same proof is polynomial in n times exp(−cn1/3), negli-
gible even after multiplication by n5/6. This use of the polynomial product avoids a logarithmic
quotient at a boundary zero. Dominated convergence in ( 22)–(23) therefore yields
√n∥Gn∥2
2 − → 1√
2π , n 5/6∥GnFn∥2
2 − →15 4−8/3
√
2π ,
where 15 is the sixth standard Gaussian moment. Dividing proves the claim. All constants in
the preceding construction are uniform over the finite set of 34 degree remainders, so the limit
holds through all suﬀiciently large integers.
13

7 Interior-root budgets and their obstruction
W e first prove the all-degree bound and then the existence criterion. The proof also identifies
the structural role of the circle roots.
7.1 Multiplication by a polynomial of small degree
F orT = c Q
j(z − γj), write M(T) = |c| Q
j max(1, |γj|) for its Mahler measure. The classical
coeﬀicient bound gives
∥T∥2 ≤
s2ℓ
ℓ

M(T) ≤ 2ℓM(T), ℓ = deg T. (24)
Indeed each coeﬀicient is bounded by the corresponding binomial coeﬀicient times M(T), by
expanding the product; sum their squares. See also [ 8, Lemma 1.6 and Exercise 1.11].
Lemma 15. If P has degree n and H ̸= 0 has degree at most d, then
∥HP ∥2 ≥ ∥H∥2(n + d + 2)−d∥P∥2.
Proof. F orV = PN
j=0 ajzj and γ ∈ C, Parseval gives
∥(z − γ)V ∥2
2 = (1 + |γ|2)∥V ∥2
2 − 2 Re
0
@γ
N−1X
j=0
ajaj+1
1
A.
The numerical radius of the truncated shift of dimension N + 1 is cN = cos( π/(N + 2)) ; this
is the classical extremal shift calculation in [ 9]. Directly , after a diagonal phase rotation its
real part is the path matrix with off-diagonal entries 1/2. Its eigenvectors have coordinates
sin((j + 1)kπ/(N + 2)), and its largest eigenvalue is cN . Thus the squared norm ratio is at least
1 + r2 − 2rcN , where r = |γ|. F or r ≤ 1, completing a square bounds this below by 1 − c2
N ; for
r ≥ 1, divide by r2 and use the same argument at 1/r. Consequently
∥(z − γ)V ∥2 ≥ max(1, |γ|) sin π
N + 2 ∥V ∥2.
F actorH into ℓ ≤ d linear factors and apply this estimate successively at degrees n, n+1, . . . , n +
ℓ − 1. Since sin(π/x) ≥ 2/x for x ≥ 2,
∥HP ∥2 ≥ M(H)
 2
n + d + 2
ℓ
∥P∥2 ≥ ∥H∥2(n + d + 2)−ℓ∥P∥2.
This implies the assertion; the constant-polynomial case is immediate.
7.2 A positive semicircle in the reciprocal identity
Proof of Theorem 1. W rite P = cAQ, where A(z) = QM
j=1(z − βj), |βj| < 1, is monic and
all roots of Q lie on the circle. F or a polynomial considered with degree parameter k, set
T∗(z) = zkT(1/¯z). Use parameters n for P, M for A, and importantly n for R = P′ − λP, even
if R has smaller actual degree. Self-inversivity of Q gives P/P ∗ = ωA/A∗ for some |ω| = 1 . The
identity z2(P∗)′ = nzP ∗ − R∗ − ¯λP∗, followed by differentiation of this quotient and clearing
denominators, yields
z2AA∗R + ωA2R∗ = HP, (25)
H = z2{A′A∗ − A(A∗)′} + (nz − λz2 − ¯λ)AA∗. (26)
14

These are polynomial identities, including at zeros of the factors. Here deg H ≤ d = 2 M + 2 ,
and on the circle |A∗| = |A| ≤ 2M , |R∗| = |R|. Hence
∥HP ∥2 ≤ 2 4M ∥R∥2. (27)
W e obtain a lower bound forH without a separation assumption. The finite Blaschke identity ,
also given in [ 11, Lemma 4.3], is
z (A/A∗)′
A/A∗ =
MX
j=1
1 − |βj|2
|z − βj|2 , |z| = 1 .
It follows either by differentiating each factor or by its Poisson kernel formula. Since AA∗ =
zM |A|2 on the circle,
z−M−1H(z) = ( n − 2 Re(λz))|A(z)|2 + KA(z), (28)
KA(z) =
MX
j=1
(1 − |βj|2)
Y
ℓ̸=j
|z − βℓ|2 ≥ 0.
Choose a semicircle E on which Re(λz) ≤ 0; if λ = 0 , choose either semicircle. Thus |H| ≥ n|A|2
on E.
Jensen’s formula for the monic stable polynomial A gives
R
T log |A| dt/(2π) = 0 . On the
complementary semicircle, log |A| ≤ M log 2. Therefore its average over E, with measure dt/π,
is at least −M log 2. Applying Jensen’s inequality to exp(4 log |A|) on E gives
1
π
Z
E
|A|4 dt ≥ 2−4M , ∥H∥2 ≥ n√
2 4M .
This restricted-arc Jensen argument is classical in origin; compare [ 10, Lemma 4.1]. The loga-
rithm is continuous on the circle for each strictly interior configuration, so no limiting interchange
as the roots approach the boundary is needed. In particular H ̸= 0 . Lemma 15 and ( 27) now
give (1). F or n ≥ 2M + 4, use n + 2M + 4 ≤ 2n and weaken 2−6M−7/2 to 2−6M−4.
Corollary 16 (Necessary quantitative count). Under the hypotheses of Theorem 1,
M ≥ log(1/ρλ(P)) − log n − log(98
√
2)
2 log n + log 784 .
In particular, a sequence with ρλn (Pn) ≤ exp(−cnα), where c, α > 0, necessarily has Mn ≥
(c/2 + o(1))nα/ log n.
Proof. Since M ≤ n, we have n + 2M + 4 ≤ 7n. T aking logarithms in (1) gives
log(1/ρλ(P)) ≤ (2M + 1) log n + M log 784 + log(98
√
2).
Rearrangement proves the result. This is only a necessary condition; Theorem 3 can also exclude
a proposed decay rate.
Remark 17 (Stable factor and self-inversive cofactor). The same bound ( 1) holds for any degree-
n P = cAQ with A monic of degree M, all its zeros strictly inside the disk, and Q = ηQ∗,
|η| = 1 . Indeed only this last identity was used for Q; the remaining estimates use the degree of
P and the zeros of A. The cofactor may therefore contain conjugate-reciprocal pairs inside and
outside the circle. In this extension M means the degree of the chosen stable factor, not the
total number of interior zeros of P. Not every polynomial has such a factorization. F or instance,
PR = 1 − z/R, R > 1, with λ = −1/R has residual 1/[R2√
1 + R−2] → 0 at fixed degree one; its
unpaired exterior root falls outside the hypothesis.
15

7.3 Suﬀiciency , necessity and exact saturation
Proof of Theorem 2. If bn does not tend to infinity , there are a finite B and infinitely many
degrees with bn ≤ B. F or every such suﬀiciently large n, Theorem 1 bounds any admissible
residual below by 2−6B−4n−2B−1, since its actual count M ≤ B. This contradicts superalgebraic
decay , so (2) implies (1).
Suppose now bn → ∞. F or each integerj ≥ 1, apply Theorem 4 with exponent 2j, obtaining
Mj, Cj, Nj. Choose strictly increasing integers Tj ≥ j so large that for every n ≥ Tj,
bn ≥ Mj, n ≥ Nj, n j ≥ Cj.
All auxiliary eventual conditions in that construction can also be included in Nj. With j(n) =
max{j : Tj ≤ n}, the constructed real normalized polynomial has exactly Mj(n) interior zeros
and restricted residual at most n−j(n). The index is finite and tends to infinity .
T o achieve exactlybn interior zeros while retaining reality , use the explicit boundary factor
in Section 6:
B6(z)u(1 + z)v, B 6(z) = (1 + z)4(1 − z + z2), u, v ≥ 0.
It supplies 4u + v real roots at −1 and u conjugate pairs, totaling 6u + v = n − Mj(n) roots.
Eventually u ≥ 1. Given the required additional count s = bn − Mj(n), take
q = min {u, ⌊s/2⌋}, r = s − 2q.
Then 0 ≤ q ≤ u and 0 ≤ r ≤ 4u + v. Move q conjugate pairs and r real roots radially inward
by a common suﬀiciently small positive amount. This preserves real coeﬀicients, the degree and
nonzero constant term. After normalizing at zero, the coeﬀicients and the restricted slope tend
to their original values as the displacement tends to zero. The restricted residual is continuous
because its norm denominator is nonzero. F or each n, choose the displacement so that the
residual increases by at most n−j(n). The final polynomial has exactly bn interior zeros and
residual at most 2n−j(n) = o(n−A) for every fixed A > 0. The finitely many initial degrees can
be filled arbitrarily with real normalized polynomials having the prescribed count. This proves
(1) implies (3), while (3) implies (2) immediately .
F or residuals merely tending to zero, infinitely many zero budgets would contradict Theo-
rem 5. Conversely , a budget at least one eventually accommodates the family of Theorem 13.
This last assertion concerns an upper budget, not saturation of every budget by that particular
family .
F or a fixed M, residual O(n−A) consequently requires A ≤ 2M + 1. This necessary relation
is not a matching tradeoff. The number MA in Theorem 4 depends on A; no single fixed count
gives a superalgebraic sequence.
7.4 A stronger obstruction for one interior zero
The reciprocal identity works for every count. At count one, the third and fourth reciprocal
moments give a stronger exponent.
Proposition 18. If n ≥ 4096, P ∈ Sn has exactly one strictly interior zero and al l other zeros
on the circle, then, for al l λ ∈ C,
ρλ(P) ≥ n−13/6
512
√
2 e3 .
Proof. Set C = 2
√
2 e3 and suppose for contradiction that ρ = ρλ(P) ≤ n−13/6/(256C). Rotate
a maximum point to 1 and normalize G(1) = ∥G∥∞ = 1 as in Lemma 6. Its initial part gives
|µ| ≤ n + 1 and S1 = G′(1) ∈ R, where Sk = P
j(1 − βj)−k uses the rotated zeros. The local
16

ODE proof of Lemma 7, at radius 1/n, does not require its separate separation parameter η.
Here its smallness parameter is at most e3/n < 1/2, and it yields the unaveraged estimates
|Sk| ≤ 2
√
n + 1ρe(2n+1)/nnk−1 ≤ Cρnk−1/2, k ≥ 2.
In particular,
|S2| ≤ n−2/3
256 , |S3| ≤ n1/3
256 , |S4| ≤ n4/3
256 . (29)
The n−1 boundary reciprocals are wj = 1 /2 +itj, tj ∈ R; the remaining reciprocal is v = x+iy,
x > 1/2. Since S1 is real, P
j tj = −y, so
Im S2 = (2 x − 1)y,
and, using Re w3
j = (3 /2) Re w2
j − 1/4,
x3 − 3
2 x2 − 3(x − 1
2 )y2 = n − 1
4 + Re S3 − 3
2 Re S2 ≥ n
8 .
The last inequality follows from ( 29) for n ≥ 4096. Both subtracted terms on the left are
nonnegative, so x ≥ n1/3/2 ≥ 8. Consequently 2x − 1 ≥ x, |xy| ≤ | S2|, and
Re v4 = x4 − 6x2y2 + y4 ≥ n4/3
16 − 6
65536n−4/3.
F or each boundary reciprocal, Re(1/2 + it)4 = ( t2 − 3/4)2 − 1/2 ≥ −1/2. It follows that
Re S4 ≥ n4/3
16 − 6
65536n−4/3 − n − 1
2 ≥ n4/3
64 ,
using n/2 ≤ n4/3/32. This contradicts ( 29).
T ogether with Theorem13, this leaves a gap between the universal one-root lower exponent
13/6 and the achieved upper exponent 1/6. No optimality of either is asserted.
8 A fixed radial gap forces a polynomial barrier
The upper construction uses the full closed disk. A fixed strict root radius gives a complementary
obstruction, by the same local estimate and bounded test as the lower-bound proof.
Proposition 19. F or0 ≤ q < 1, let sn(q) denote the infimum defining sn with al l zeros restricted
to |z| ≤ q. Set
a = 1 − q2, K = ⌈4/a⌉, ∆ = 1
1 + q − 1 + qK
Ka > 0, c q = min
 1√
2, ∆Ka
2
√
2e3(1 + a)K

.
Then sn(q) ≥ cqn3/2−K for every n ≥ 41.
Proof. W riteρ for an admissible residual. If ρ > 1/√n + 1, the conclusion is immediate. Oth-
erwise the maximum normalization gives |µ| ≤ n + 1. T ake r = 1 /n. The smallness parameter
in the proof of Lemma 7 is at most e3/n < 1/2. That local proof does not need the separate
zero-separation parameter η, and gives
|mj| ≤ 2√n + 1
n ρe3r1−j (j ≥ 2).
17

The exact image of |β| ≤ q under v = (1 − β)−1 is |v − 1/a| ≤ q/a. Thus |1 − av| ≤ q and
Re v ≥ 1/(1 + q). Use Ψ(v) = [1 − (1 − av)K]/(Ka), whose modulus is at most (1 + qK)/(Ka).
Estimating its higher averaged terms gives
∆ ≤ 2e3√n + 1ρ
Kan2 [(1 + an)K − 1 − Kan] ≤ 2e3√n + 1ρ
Kan2 (1 + an)K.
Now √n + 1 ≤
√
2n and 1 + an ≤ (1 + a)n. The resulting lower bound is the stated one. Finally
Ka ≥ 4, qK < 1, and 1/(1 + q) > 1/2 ensure ∆ > 0.
In particular, any single sequence of admissible degree- n polynomials with residual o(n−A)
for every fixed A > 0 must have its maximum root modulus tending to one. Otherwise an
infinite subsequence would satisfy a fixed polynomial lower bound. No sharp radial exponent is
asserted.
9 Scope and verification
The uniform slope formulation bounds approximate eigenvectors of polynomial differentiation
under a zero-location constraint. It does not describe the full unconstrained pseudospectrum.
F or example, for u = n/4 and Tn(z) = Pn
k=0(uz)k/k!,
T′
n − uTn = −un+1
n! zn, ∥T′
n − uTn∥2
∥Tn∥2
≤ n
4
e
4
n
,
using ∥Tn∥2 ≥ 1 and n! ≥ (n/e)n. Thus a root constraint is essential for a bound of our form.
The lower and upper disk bounds do not match in order. Whether the restricted exterior
power-sum minima stay bounded away from zero remains unresolved here, as does the optimal
order of sn and rn. The superalgebraic upper bound is not a stretched-exponential upper bound,
and its constants are not optimized. The minimal interior-root count permitting collapse is one,
but the optimal rate with one such root is not established. Theorem 1 excludes superalgebraic
decay for every fixed number of interior roots. The elementary radial barrier is a consequence of
the same local method. W e do not assert a theorem for arbitrary starting exponents, weighted
power sums, or Hp with p < 1. The elementary norm comparison in Corollary11 is a consequence
of the main estimate.
The analytic proof of the explicit threshold uses only the displayed elementary inequalities. It
does not rely on optimization or sampling. The supplementary diagnostics check exact projected
Newton identities over Gaussian rationals, the bounded test on admissible reciprocal zeros,
binomial identities, and numerical instances of the finite certificate. Rational checks of constants
and high-precision evaluations are included for reproducibility . The circle-root family is checked
with complete exact coeﬀicient Parseval ratios. The one-interior-root family has symbolic and
high-precision checks of the cubic, slope, moments and circle parameters. A separate calculation
by the same involved model reviewer covers all 34 degree classes at two scales. Additional exact
checks cover the reciprocal identity , its complex conjugations, the positive Poisson kernel, the
one-root moment obstruction and real-root saturation.
F or Proposition14, supplementary numerical norm diagnostics use two equispaced grids, of
sizes n + 1 and n + 2, at eight degrees up to 10 000 017. Such grids would integrate the squared
polynomial norms exactly in exact arithmetic. The implemented evaluations instead use rounded
parameters and omit underflow-scale weights. The cancellation-free remainder approximates
the exact family; it is not literally the exact residual of the polynomial with all parameters
rounded. Agreement between grids does not certify the common rounding or masking error.
These computations are not interval-certified norm evaluations and do not prove the asymptotic
limit. Finite moment searches motivated the general construction but are not premises of its
18

arbitrary-order proof. None of the checks establishes historical priority or replaces the analytic
arguments.
The comparison uses the exact primary-source versions listed below. A targeted search did
not identify the bounds in this exact setting; exhaustive priority certification is not claimed.
The accessible Komarov versions listed below were used for the stated comparison. A related
2020 journal text (DOI 10.1070/IM8901) was not available in full in this review; no exclusion
of every possible bibliographic overlap is claimed. AI tools assisted exploration, drafting and
computational checking. Model review is distinct from independent human peer review and
formal proof verification.
References
[1] X. T an, Q. W ang, W. Huang and K. Chen, Residual bounds for Schur-stable polynomials ,
arXiv:2608.02043v3, 8 August 2026. https://arxiv.org/abs/2608.02043v3.
[2] Y. Luo, R. Y ang and K. Zhu, Exterior power sums , arXiv:2607.22017v1, 24 July 2026.
https://arxiv.org/abs/2607.22017v1.
[3] M. A. Komarov, Rate of approximation by logarithmic derivatives of polynomials whose zeros
lie on a circle, arXiv:1804.08918v1, 24 April 2018. https://arxiv.org/abs/1804.08918v1.
[4] M. A. Komarov, Caratheodory type representation with unit weights and related approxi-
mation problems , arXiv:1807.06499v1, 17 July 2018 (Russian). https://arxiv.org/abs/
1807.06499v1.
[5] T. Erdélyi, D. P . Hardin and E. B. Saff, Inverse Bernstein inequalities and min-max-min
problems on the unit circle , arXiv:1307.4056v1, 15 July 2013. https://arxiv.org/abs/
1307.4056v1.
[6] P . Busch, J. Kiukas and R. F. W erner, Sharp uncertainty relations for number and angle ,
arXiv:1604.00566v2, §VI.A.2. https://arxiv.org/abs/1604.00566v2.
[7] NIST Digital Library of Mathematical F unctions, §§28.2 and 28.8, especially Eq. (28.8.1).
https://dlmf.nist.gov/28.2;
https://dlmf.nist.gov/28.8. Accessed 18 October 2026.
[8] F. Brunault and W. Zudilin, Many V ariations of Mahler Measures: A Lasting Symphony ,
Australian Mathematical Society Lecture Series 28, Cambridge University Press, 2020,
Chapter 1. https://doi.org/10.1017/9781108885553.
[9] U. Haagerup and P . de la Harpe, The numerical radius of a nilpotent operator on a
Hilbert space, Proc. Amer. Math. Soc. 115 (1992), 371–379. https://doi.org/10.1090/
S0002-9939-1992-1072339-6 .
[10] A. Defant and M. Mastyło, Lp-norms and Mahler’s measure of polynomials on the
n-dimensional torus , Constr. Approx. 44 (2016), 87–101. https://doi.org/10.1007/
s00365-015-9319-x .
[11] L. V. Kovalev and X. Y ang, Extreme values of the derivative of Blaschke products and
hypergeometric polynomials, arXiv:2007.09760v2, 25 June 2021; Bull. Sci. Math. 169 (2021),
102979. https://arxiv.org/abs/2007.09760v2.
19