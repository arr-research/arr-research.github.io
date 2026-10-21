# A sharp circle-root residual barrier and its collapse with one interior zero

Extracted text; the canonical PDF controls mathematical notation.

A sharp circle-root residual barrier
and its collapse with one interior zero
Lluis Eriksson
18 October 2026
Abstract
F or degree-n polynomials with all zeros on the unit circle, the least normalized residual
∥P′ − λP∥H2 /∥P∥H2 tends to 1/
√
8, both for arbitrary complex λ and for the restricted
slope λ = P′(0), P(0) = 1 . W e prove the sharp lower limit through the classical Mathieu
ground state and give an explicit circle-root family attaining it in every large degree. In
contrast, exactly one zero strictly inside the disk, with all remaining zeros on the circle,
permits restricted residual O(n−1/6), giving the exact zero-count threshold for collapse. More
generally , for each fixed A > 0, a fixed number MA of interior zeros permits O(n−A). Their
distance and radial gap from 1 have ordern−1/3; explicit algebraic parameters in the one-root
case, and an implicit-function construction in general, correct both degree rounding and the
exact slope. F or all disk-root polynomials and arbitrary slope, we also prove a uniform lower
bound exp(−C√n) for every C >
p
(8/3) log 17, explicitly exp(−3√n) for n ≥ 104. This
refines the known residual method for exterior power sums; the negative answer to Erdős
Problem 973 was already known. The optimal disk and one-root decay rates, and small
exterior power-sum constructions, remain unresolved.
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
P ∈Sn
λ∈C
∥P′ − λP∥2
∥P∥2
.
There is no normalization at the origin in this definition.
Theorem 1. Put C0 =
p
(8/3) log 17. F or every C > C 0 there is NC such that
sn ≥ e−C√n (n ≥ NC). (1)
The fol lowing explicit bound also holds:
sn ≥ e−3√n (n ≥ 104). (2)
1

F or comparison, T an, W ang, Huang and Chen [1, Theorem 1.1] considered the restricted
infimum
rn = inf
P ∈Sn
P (0)=1
∥P′ − P′(0)P∥2
∥P∥2
and proved rn ≥ exp(−(1 + o(1))√n log n). F or an individual normalized polynomial we write
ρ(P) = ∥P′ − P′(0)P∥2/∥P∥2. Theorem 3 identifies the positive limiting residual when every
root lies on the circle. Theorem 11 shows that one interior root suﬀices to make it vanish,
establishing the minimal zero-count threshold. These statements concern the global weighted
boundary norm, including the exact restricted slope.
Since sn ≤ rn, Theorem 1 strengthens that quantitative estimate and allows an arbitrary
scalar slope. Their maximum-point normalization, segment integration and projected Newton
identity are retained here, with attribution. The two changes are a local analytic bound for the
logarithmic derivative and a bounded test polynomial. These remove the logarithmic factor in
the exponent.
Luo, Y ang and Zhu [2, Theorem 1.1] had already proved that exterior power sums cannot
be exponentially small in the degree, answering Erdős Problem 973 negatively . The application
in Section 5 is a quantitative refinement of that established conclusion. No new solution of the
original yes-or-no problem is asserted.
Theorem 2 (Superalgebraic decay). F or every A > 0, there are constants CA, NA such that
rn ≤ CAn−A for every integer n ≥ NA.
The polynomials can be chosen with real coeﬀicients, exactlyMA zeros strictly inside the unit disk,
where MA is independent of n, and al l other zeros on its boundary. The interior zeros approach
1 with distance and radial gap Θ(n−1/3). T ogether with Theorem 1, this implies superalgebraic
decay of both sn, rn, while s1/n
n , r1/n
n → 1.
The proof in Section 6 fixes the cancellation order and finite integer multiplicities first, then
lets the reciprocal root scale grow as n1/3. It provides no effective bounds on MA, CA, NA
or uniform control as A grows. Section 7 explains why a fixed strict root radius precludes
superalgebraic decay of a single sequence.
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
Theorem 3. The unrestricted and restricted circle-root residuals satisfy
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
2

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
. (3)
W riteE(L) for the lowest periodic eigenvalue of −d2/dt2 − L cos t, for L ≥ 0. In odd degree, |p|
is periodic in H1 and has the same quadratic-form values as p. Thus in both parities ( 3) is at
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
3

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
3 A finite residual certificate
W e first give conditions that can be checked at a fixed degree. The asymptotic and explicit
choices will then be elementary .
Lemma 4 (Normalization and separation) . Suppose P ∈ Sn, λ ∈ C, y > 0, and
∥P′ − λP∥2
∥P∥2
≤ e−y,
√
n + 1 e −y ≤ 1.
Set
γn = 2 + log(2
√
n + 1), η = y − γn
n . (4)
If η > 0, there are numbers v1, . . . , vn and moments mk = n−1 P
j vk
j such that
m1 ∈ R, m 1 ≥ 1
2 , Re vj ≥ 1
2 , |vj|2 ≤ Re vj
η . (5)
They are the reciprocals vj = (1 − βj)−1 of the complex displacements from the zeros to a
normalized maximum point.
4

Proof. This is the normalization and separation argument of [1, Sections 2.1–2.2], with the scalar
slope left arbitrary . Choose |τ| = 1 at a maximum of |P|, and put
G(w) = P(τw)
P(τ) , µ = τλ, E = G′ − µG.
The denominator is nonzero because P is nonzero. W e have G(1) = ∥G∥∞ = 1 , ∥G∥2 ≤ 1, and
∥E∥2 ≤ e−y. Differentiating |G(eit)|2 at its maximum shows that d = G′(1) is real. Bernstein’s
polynomial inequality gives |d| ≤ n. The coeﬀicient bound ∥E∥∞ ≤ √n + 1∥E∥2 therefore yields
|µ − d| = |E(1)| ≤ 1, |µ| ≤ n + 1. (6)
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
Lemma 5 (Local analytic estimate) . With the normalization above, let r > 0 and suppose
q = r
√
n + 1 exp
 
−y + (2n + 1)r

≤ 1
2 . (7)
Then G has no zero in |w − 1| ≤ r, and, for every integer k ≥ 2,
|mk| ≤ 2√n + 1
n exp
 
−y + (2n + 1)r

r1−k. (8)
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
Using the straight segment and ( 6), we obtain |h(u)| ≤ q ≤ 1/2. Thus G is nonzero on that
closed disk and on a neighborhood of it. The analytic function F = G′/G − µ = E/G satisfies
|F(1 + u)| ≤ 2
√
n + 1 e −y+(2n+1)r (|u| ≤ r).
Cauchy’s derivative estimate and logarithmic differentiation give
|F(k−1)(1)|
(k − 1)! ≤ 2
√
n + 1 e −y+(2n+1)rr1−k, F (k−1)(1) = ( −1)k−1(k − 1)! nmk.
This proves ( 8). There is no restriction k ≤ n + 1 : F is an analytic rational function on the
specified disk.
5

Proposition 6 (Finite certificate). Fix n ≥ 1, y, r > 0, and an integer K ≥ 2. Define η by (4)
and set a = 2 η. Suppose 0 < η ≤ 2, √n + 1e−y ≤ 1, and (7) holds. Put
B = 2√n + 1 r
Kan exp

−y + (2n + 1)r + K log

1 + a
r

. (9)
If
1
Kη + B < 1
2, (10)
then sn ≥ e−y.
Proof. Suppose an admissible P, λ had residual at most e−y. F or the numbers in Lemma 4,
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
ak−1vk. (11)
It has zero constant coeﬀicient, linear coeﬀicient one, and |Ψ(vj)| ≤ 2/(Ka) = 1 /(Kη). By
Lemma 5, its remaining averaged terms have modulus at most
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
contrary to (10). Each individual residual is therefore larger than e−y; taking its infimum gives
the asserted non-strict bound.
4 Choice of parameters
Proof of (1). Fix C > C 0, and choose t > 0 so small that
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
F or all suﬀiciently large n, the preliminary conditions of Proposition 6 hold: η ∼ C/√n, q → 0,
and √n + 1e−y → 0. Also Kη ≥ 2 + t, leaving a fixed positive margin in ( 10). W e have
K ∼ 2 + t
C
√n, a
r → 16,
and hence
−y + (2n + 1)r + K log(1 + a/r)√n − → −3C
4 + 2 + t
C log 17 < 0.
The prefactor in ( 9) is O(n−1). Thus B → 0, and the finite certificate applies.
6

Proof of (2). T aken ≥ 104 and choose
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
n. (12)
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
F rom (12) we obtain a/r ≤ 16 and K ≤ (14/19)√n + 1. Using log 17 < 3,
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
It follows that B < 1/(5n) ≤ 1/50000 < 1/42. All conditions of Proposition 6 are satisfied.
Remark 7. The constants 3 and 104 are convenient explicit choices. The same proof with
r = sy/n, 0 < s < 1/2, gives the suﬀicient asymptotic condition
C2 > 2 log(1 + 2 /s)
1 − 2s .
W e uses = 1 /8 to state a simple constant. Neither this expression nor C0 is asserted to be the
optimal residual constant.
5 Exterior power sums and Hardy norms
Corollary 8. Let |zj| ≥ 1, 1 ≤ j ≤ n, and write Mn = max 2≤k≤n+1 |P
j zk
j |. Then
Mn ≥ 1
ne−3√n (n ≥ 104).
F or every C > C 0, uniformly over al l such configurations, Mn ≥ n−1e−C√n for al l suﬀiciently
large n. No distinguished point z1 = 1 is needed.
7

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
Apply Theorem 1.
The factor 1/n is retained in these finite statements. It can be absorbed in a leading square-
root exponent with any strictly larger constant. This corollary strengthens the scale in [ 1]; the
earlier qualitative conclusion of [ 2] remains fully credited.
Corollary 9. Uniformly for 1 ≤ p ≤ ∞, P ∈ Sn, and λ ∈ C,
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
Theorem 1 with a constant strictly between C0 and C, and absorb 1
2 log(n + 1) = o(√n).
6 Superalgebraic upper bounds
W e prove the upper statement by cancelling a prescribed finite number of logarithmic-derivative
terms at a strict global maximum. All constants in this section may depend on the prescribed
cancellation order K. They are not asserted to be uniform as K → ∞.
Lemma 10 (A finite positive moment cone). Fix K ≥ 3. F or a rational point ζ = x+ iy, x > 0,
y ≥ 0, define the real column
V (ζ) =
(
(ζ2, . . . , ζ K)T , y = 0 ,
(2 Re ζ2, . . . , 2 Re ζK)T , y > 0.
There is a finite col lection of these columns whose cone is RK−1. The col lection can contain
any prescribed K distinct positive rational real points. Its column matrix A∞ admits a strictly
positive rational vector α0 satisfying
A∞α0 = (0 , 3/2, 0, . . . , 0)T .
8

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
Proof of Theorem 2. Fix K ≥ 3. Apply Lemma 10, with K designated distinct positive real
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
Choose a nearest integer in the specified congruence class; both bn, cn are positive eventually .
Then tn = cn/R = 2 S + O(ϵ) and un = bn/R3 = Q + O(ϵ2).
Let ξi vary near ζi, varying only the K designated real nodes. Define dϵ(ξ) = −ξ2/(ξ − ϵ)
for a real node, and twice its real part for a pair. Consider the K equations
0 = t/2 +
X
i
midϵ(ξi), (13)
0 = tϵ/4 +
X
i
miM2(ξi), (14)
0 = bjuϵj−3 + t2−jϵj−1 +
X
i
miMj(ξi), 3 ≤ j ≤ K. (15)
9

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
the circle. The interior zeros satisfy |1 − βi,n| ≍ 1 − |βi,n| ≍ R−1. Multiplying ( 13)–(15) by
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
F or a real group v = x > 1, its normalized squared modulus is 1 + 4 x(x − 1)s ≤ eT (v)s, with
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
|Pn(eiθ)/Pn(1)|2 ≤ exp[−κn sin2(θ/2)]. (16)
The zero-free neighborhood now shrinks with n. Choose a fixed δ > 0 so that on |z−1| ≤ δ/R
all |vi,n(z − 1)| ≤ 1/2, and the baseline zeros are excluded. Expanding v/(1 + v(z − 1)), the
exact cancellations above give
|P′
n(z)/Pn(z) − λn| ≤ CK(n + RK+1)|z − 1|K ≤ CKRK+1|z − 1|K. (17)
The geometric-series remainder is uniform on this shrinking disk. There are O(n) baseline
reciprocal variables of bounded size and onlyM interior variables of sizeO(R). By real symmetry
the first angular derivative of the normalized log modulus vanishes at zero; its second derivative
on a suitably smaller arc |θ| ≤ δ′/R is O(n + R2) = O(n). Hence the normalized squared
denominator is at least cn−1/2, by integration over |θ| ≤ n−1/2. Combining ( 16) and ( 17), the
local squared numerator is at most
CKR2K+2
Z
R
θ2Ke−cnθ2
dθ ≤ CKR2K+2n−K−1/2.
Outside the small arc use the polynomial product derivative. Normalized derivatives of a
baseline or extra factor are bounded; those of a real interior factor are O(R), and those of a pair
10

are O(R2). Removing a baseline factor reduces the positive global cost by three, removing an
extra factor reduces it by one, and removing an interior group increases it by its positive T(v).
Thus every derivative term is bounded by a polynomial in n times the same Gaussian bound,
up to a constant. On the outer arc n sin2(θ/2) ≥ cn/R2 ≍ n1/3. Its squared integral is therefore
at most poly(n)e−cn1/3
, negligible compared with every fixed inverse power. This estimate uses
no rational quotient at a boundary zero. Dividing by the denominator proves
ρ(Pn)2 ≤ CKR2K+2n−K ≤ CKn(2−K)/3, ρ (Pn) ≤ CKn(2−K)/6.
Choose K ≥ 6A + 2. Then MA = M is independent of n, as required. The proof does not give
effective bounds on MA, CA, or the starting degree as functions of A.
Theorem 11 (One interior zero suﬀices) . F or every suﬀiciently large integer n, there is a real
degree-n polynomial Pn, with Pn(0) = 1 , exactly one zero strictly inside the unit disk and al l
remaining zeros on the circle, such that ρ(Pn) = O(n−1/6). The interior zero is real and positive,
with distance and radial gap from 1 of ordern−1/3. In conjunction with Theorem 3, the minimum
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
2 v2 = ( n − 1)/4. (18)
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
11

Here the extra roots at −1 contribute k/2 to the slope difference and k/4 to the second moment;
the interior root contributes −v2/(v − 1) and v2, respectively . F or a conjugation-symmetric
multiset of N circle roots avoiding 1, its reciprocal moments satisfy
M◦
3 = 3
2 M◦
2 − N/4. (19)
This follows for each pair 1/2 ± iy, and also for the real reciprocal 1/2. Conjugation symmetry
is essential and holds here. T aking N = n − 1 and M◦
2 = −v2, ( 18) gives P
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
|Pn(eiθ)/Pn(1)|2 ≤ exp[−cn sin2(θ/2)] (20)
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
Finally , Theorem 3 excludes vanishing residuals with zero interior roots; this construction
permits them with one. This proves the zero-count threshold, not a sharp rate or the superalge-
braic conclusion with one root. No numerical starting degree or norm constant is claimed.
12

7 A fixed radial gap forces a polynomial barrier
The upper construction uses the full closed disk. A fixed strict root radius gives a complementary
obstruction, by the same local estimate and bounded test as the lower-bound proof.
Proposition 12. F or0 ≤ q < 1, let sn(q) denote the infimum defining sn with al l zeros restricted
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
in the proof of Lemma 5 is at most e3/n < 1/2. That local proof does not need the separate
zero-separation parameter η, and gives
|mj| ≤ 2√n + 1
n ρe3r1−j (j ≥ 2).
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
8 Scope and verification
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
but the optimal rate with one such root is not established. W e do not prove superalgebraic
decay with one interior root. The elementary radial barrier is a consequence of the same local
method. W e do not assert a theorem for arbitrary starting exponents, weighted power sums, or
Hp with p < 1. The elementary norm comparison in Corollary 9 is a consequence of the main
estimate.
13

The analytic proof of the explicit threshold uses only the displayed elementary inequalities. It
does not rely on optimization or sampling. The supplementary diagnostics check exact projected
Newton identities over Gaussian rationals, the bounded test on admissible reciprocal zeros,
binomial identities, and numerical instances of the finite certificate. Rational checks of constants
and high-precision evaluations are included for reproducibility . The circle-root family is checked
with complete exact coeﬀicient Parseval ratios. The one-interior-root family has symbolic and
high-precision checks of the cubic, slope, moments and circle parameters, without quadrature.
The independent audit covers all 34 degree classes at two scales. These finite checks do not
certify the full norm asymptotics. Symbolic identities support the constructions. Finite moment
searches motivated the general construction but are not premises of its arbitrary-order proof.
These checks do not establish historical priority or replace the proof.
The comparison uses the exact primary-source versions listed below. A targeted search did
not identify the bounds in this exact setting; exhaustive priority certification is not claimed. The
accessible Komarov versions listed below were used for the stated comparison. A related 2020
journal text was not available in full in this review; no exclusion of every possible bibliographic
overlap is claimed. AI tools assisted exploration, drafting and computational checking. Model
review is distinct from independent human peer review and formal proof verification.
References
[1] X. T an, Q. W ang, W. Huang and K. Chen, Residual bounds for Schur-stable polynomials ,
arXiv:2608.02043v3, 8 August 2026. https://arxiv.org/abs/2608.02043v3.
[2] Y. Luo, R. Y ang and K. Zhu,Exterior power sums, arXiv:2607.22017v1, 24 July 2026. https:
//arxiv.org/abs/2607.22017v1.
[3] M. A. Komarov, Rate of approximation by logarithmic derivatives of polynomials whose zeros
lie on a circle , arXiv:1804.08918v1, 24 April 2018. https://arxiv.org/abs/1804.08918v1.
[4] M. A. Komarov, Caratheodory type representation with unit weights and related approxima-
tion problems, arXiv:1807.06499v1, 17 July 2018 (Russian). https://arxiv.org/abs/1807.
06499v1.
[5] T. Erdélyi, D. P . Hardin and E. B. Saff, Inverse Bernstein inequalities and min-max-min
problems on the unit circle, arXiv:1307.4056v1, 15 July 2013. https://arxiv.org/abs/1307.
4056v1.
[6] P . Busch, J. Kiukas and R. F. W erner, Sharp uncertainty relations for number and angle ,
arXiv:1604.00566v2, §VI.A.2. https://arxiv.org/abs/1604.00566v2.
[7] NIST Digital Library of Mathematical F unctions, §§28.2 and 28.8, especially Eq. (28.8.1).
https://dlmf.nist.gov/28.2; https://dlmf.nist.gov/28.8. Accessed 18 October 2026.
14