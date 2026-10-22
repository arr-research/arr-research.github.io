# A sharp polynomial Lyapunov threshold for a stable cubic family

Extracted text; the canonical PDF controls mathematical notation.

A sharp polynomial Lyapunov threshold
for a stable cubic family
Lluis Eriksson
21 October 2026 (version 2)
Abstract
We determine exactly when the globally asymptotically stable cubic family introduced by
Liu and Fitzsimmons admits polynomial Lyapunov certificates. In their normalization, with
dampinga >0 and angular forcingb∈R, the criterion is
|b|2/3 <1 +a 2/3.
The same strict inequality characterizes positive homogeneous polynomial certificates with
weak nonpositive Lie derivative, strict polynomial certificates, and local real-analytic certifi-
cates. Equality admits none of them. Below the threshold we construct a certificate as a
finite product of positive quadratic forms. The proof pairs positive harmonic functions with
an explicit analytic square-root test and constructs a complementary limiting harmonic pair
at the boundary. Poisson smoothing and equal-weight quantiles then produce a polynomial
with a strict margin. For fixed b, an explicit sufficient degree is Ob(δ−3), where δ is the
damping excess above the threshold, while the minimum degree diverges; no matching degree
rate is asserted. The threshold persists for every single even angular harmonic and nonzero
angular speed. Classical binary-form factorization gives the corresponding sum-of-squares
consequence without increasing the Lyapunov degree. The family, its global stability, the
original counterexample to a polynomial converse theorem and the nonexistence of weak
polynomial certificates for |b| ≥2(a + 1) are prior results of Liu and Fitzsimmons. Our
classification concerns certificates, not a change in dynamical stability.
1 The family and the exact certificate region
Fora >0 andb∈R, consider
˙x=−a(x2 +y 2)x+b(x 2 −y 2)x−(x 2 +y 2)y,
˙y=−a(x2 +y 2)y+b(x 2 −y 2)y+ (x 2 +y 2)x.
(1)
In polar coordinatesx=rcosθ, y=rsinθ, this is
˙r=r 3(−a+bcos 2θ), ˙θ=r 2.(2)
Liu and Fitzsimmons introduced this family [ 1, Sec. IV-D]. They prove, for every a >0 and
b∈R , global asymptotic stability of the origin through the Lyapunov function r2e−bsin 2θ, and,
for a >0 and |b| ≥2(a + 1), that no positive definite homogeneous polynomial has nonpositive
Lie derivative [1, Theorem IV.3]. The bound behind the latter is |b|/2 < a+ 1, obtained from
the second Fourier coefficient of the normalized logarithmic derivative together with |g2|< 1 [1,
Lemma III.3]. For the single field ( a, b) = (1, 5) they also exclude local real-analytic Lyapunov
functions by a leading-term argument [ 1, Theorem II.2(4), Sec. III-D]; the family version [ 1,
Theorem IV.3] is stated for homogeneous polynomials only, and the extension of the analytic
statement to the region |b| ≥2(a + 1) is a routine consequence of their argument (see Section 6),
not a statement we find there. Their work already refutes the homogeneous polynomial Lyapunov
1

0 1 2 3 4
Damping a > 0
0
2
4
6
8
10
12Forcing amplitude |b|
Strict polynomial
certificates
No polynomial or local
analytic certificate
Exact threshold (1 + a2/3)3/2
Earlier obstruction 2(a + 1)
Figure 1: Certificate regions for the stable cubic family. All displayed parameters with a >0
give globally asymptotically stable dynamics. The solid curve is excluded from the polynomial
and local analytic certificate region. The dashed line marks the sufficient nonexistence condition
for polynomial certificates in [1, Theorem IV.3]; it is not a stability boundary.
converse. We determine the exact polynomial and local analytic certificate region of this family;
it lies strictly inside |b|< 2(a + 1) (Remark 2). The test functions below pair the whole sequence
of Fourier coefficients at once, not only the second one.
For a vector field f, write Lf V = ∇V·f . Aweak certificatemeans V (0) = 0, V > 0 away
from the origin, and Lf V≤ 0. Astrict certificatehas Lf V < 0 away from the origin. For a
local analytic certificate these conditions are required on a punctured neighborhood of zero. All
homogeneous certificates below have positive degree.
Theorem 1.For(1), the following are equivalent:
1.|b|<(1 +a 2/3)3/2.
2. There exists a positive definite homogeneous polynomial weak certificate.
3. There exists a strict homogeneous polynomial certificate that is a finite product of positive
definite real quadratic forms.
4. There exists a local real-analytic weak certificate.
Thus equality at the threshold is excluded even for weak certificates. Every system in (1) is
nevertheless globally asymptotically stable.
The stability assertion is recalled from [ 1, Sec. IV-D], not new. For orientation, its nonpoly-
nomial certificate is
H(r, θ) =r2 exp(−bsin 2θ), L f H=−2ar 2H.
It is positive, coercive, continuously differentiable at the origin, and smooth away from it. The
new assertion in Theorem 1 is the exact algebraic and analytic threshold.
Unbounded required polynomial degree in fixed dimension and field degree was already
established by Ahmadi and Parrilo [ 2, Theorem 4.3]. Ahmadi and El Khadir [ 3, Proposition
6.1] also compare polynomial and rational certificate complexity (a degree-five family). Our
degree result concerns approach to the explicit boundary above. Compactness, positive harmonic
representations, and the binary-form sum-of-squares principle are classical tools, not new general
converse theorems.
2

Remark2.For a >0 one has 1 + a <(1 + a2/3)3/2 ≤
√
2 (1 + a) < 2(1 + a). Indeed, for x, y >0
and p = 2/3, the p-power sum satisfies x+y≤ (xp +yp)1/p ≤ 21/p−1(x+y); take x = 1, y= a. So
the new threshold is strictly below the earlier sufficient nonexistence bound, and the polynomial
and analytic obstruction of [1] covers only part of the excluded region.
2 Polynomial certificates as positive harmonic data
Use normalized circle averages ⟨v⟩ = (2π)−1 R2π
0 v(ϕ) dϕ. The circular Hilbert transform H is
normalized by
Hcos(kϕ) = sin(kϕ),Hsin(kϕ) =−cos(kϕ),H1 = 0, k≥1.
On smooth real functions it is skew-adjoint for this average. The formulas used below can equally
be verified termwise from Fourier series.
Lemma 3.Let P be a positive definite real homogeneous polynomial of degree2 N, N≥ 1, and
setp(θ) =P(cosθ,sinθ). There existα 1, . . . , αN ∈Dsuch that
h(z) = 1
N
NX
j=1
1 +α jz
1−α jz , p′(θ)
2Np(θ) = Imh(e 2iθ).
Here h(0) = 1, and u = Reh has a strictly positive minimum on the closed disk. The weak
certificate condition is equivalent to
w(ϕ) :=a−bcosϕ− Hu(ϕ)≥0.(3)
Proof.The strict Fej´ er–Riesz factorization writes
p(θ) =|C| 2
LY
j=1
|1−α je2iθ|2, L≤N,|α j|<1.
This is the factorization of [1, Lemma III.2 and proof of Lemma III.3]; for completeness here is
a direct proof. The even trigonometric polynomial p has only the frequencies 2 j, |j| ≤N, so
q(ψ) = p(ψ/2) = P
|j|≤L cjeijψ is a positive trigonometric polynomial of actual degree L≤N ,
with c−j = ¯cj and cL ̸= 0. If L = 0, p is constant and nothing is to be proved. Otherwise
A(z) = zL P
j cjzj is a polynomial of degree 2 L with A(0) ̸= 0, A(eiψ) = e iLψq(ψ) ̸= 0,
and A(z) = z2LA(1/¯z). Hence its roots are not on the unit circle and come in pairs ζ, 1/¯ζ
with equal multiplicity. Let ζ1, . . . , ζL be the roots in D (none is zero). For |z| = 1 one has
|z−ζ| = |1 − ¯ζz| and |z− 1/¯ζ| = |1 − ¯ζz|/|ζ| , so q(ψ) = |A(eiψ)| = K Q
l |1 −α leiψ|2 with αl = ¯ζl,
K = |cL|/ Q
l |ζl|> 0. Put ψ = 2θ and |C|2 = K. Pad the list with zero parameters to length N.
Each kernel has real part
Re 1 +αz
1−αz = 1− |αz|2
|1−αz| 2 >0 (|z| ≤1).
Differentiating the logarithm of a factor gives twice the imaginary part of that kernel, proving
the angular identity. The imaginary part ofhisHubecauseh(0) = 1. Finally,
Lf P= 2Nr 2N+2 p(θ)

−a+bcos 2θ+ p′(θ)
2Np(θ)

,
which proves (3).
3

Conversely, an equal-weight average of these kernels yields a polynomial of degree 2 N.
Explicitly, put
Qα(x, y) = (1 +|α|2)(x2 +y 2)−2 Reα(x 2 −y 2) + 4 Imα xy.(4)
Its eigenvalues are (1 −|α|)2, (1 +|α|)2. The product P = Q
j Qαj is positive definite and satisfies
the angular identity in Lemma 3. A strict margin in (3) therefore gives a strict polynomial
certificate.
3 The strict obstruction
Rotation byπ/2 changes the sign ofb, so assumeb≥0. Forc >0, define
s=
p
1 +c 2, η= c+i
s ,
Mc(z) =c 2 −1 + 2ic 1 +ηz
1−ηz , f c(z) =
p
Mc(z).
(5)
The Cayley transform has positive real part on D; hence Mc takes values in the upper half-plane.
We choose the analytic square root in the first quadrant. In particular,
fc(0) =c+i, f ′
c(0) = 2ic
s .(6)
For 0 < σ <1, write fc(σeiϕ) = Fσ(ϕ) + iGσ(ϕ). Both functions are positive and smooth.
Their means and first coefficient give
⟨Fσ⟩=c,⟨G σ⟩= 1,⟨G σ cosϕ⟩= σc
s , F σ +HG σ =c.(7)
If u, wcome from a weak polynomial certificate, then ⟨u⟩ = 1, u≥ε > 0, and w≥ 0. Using (3)
and skew-adjointness,
⟨uFσ +wG σ⟩=⟨u(F σ +HG σ)⟩+a⟨G σ⟩ −b⟨Gσ cosϕ⟩
=c+a− bσc
s ≥εc.(8)
Every function in this computation is smooth for σ <1; no singular boundary pairing is assumed.
Lettingσ↑1 yields
b≤ (a+c)s
c −εs < (a+c)
√
1 +c 2
c .(9)
The derivative of the last expression is
c3 −a
c2√
1 +c 2 .
Its minimum occurs at c = a1/3, with value (1 + a2/3)3/2. This proves the strict necessary
inequality, including nonexistence at equality. The positive minimum of u, rather than mere
nonnegativity, is what excludes the boundary.
4 An explicit limiting pair on the boundary
The converse needs more than a necessary moment inequality. We construct positive harmonic
data at the critical parameters, then approximate them while retaining a positive margin.
4

Fixc >0, withs, η, fc as above, and put
a0 =c 3, b 0 =s 3.
Define
qc(z) = 1−c 4 + b0
2

(c−i)z+ (c+i)z −1
,(10)
hc(z) =ia 0 − ib0
2 (z+z −1) +i qc(z)
fc(z) .(11)
Lemma 4.The function hc is analytic in D (it extends analytically across zero), continuous on
D, and satisfiesh c(0) = 1. Its boundary data obey
uc = Reh c ≥0, w c =a 0 −b 0 cosϕ−Imh c(eiϕ)≥0,
and ucwc ≡ 0: wc vanishes on one closed arc of the circle and uc on the complementary closed
arc. MoreoverReh c >0inD.
Proof. Step 1: algebra.Sincec+i=sηandc−i=s¯η,
Mc(z) = (c+i) 2 −ηz(c−i) 2
1−ηz =s 2 η2 −¯ηz
1−ηz ,(12)
because η¯η2 = ¯η. Using η2 + ¯η2 = 2(c2 −1)/s2 and 1−c4 = s2(1−c2), expansion of the right-hand
side shows
qc(z) =− s2
2 Mc(z)(1−ηz)(1−¯η/z) =− s4
2 (η2 −¯ηz)(1−¯η/z).(13)
So Mc is a M¨ obius map with its only pole atz = ¯ηand its only zero at z = η3 (since η2/¯η= η3).
Both lie on the unit circle and are distinct, becauseη 4 ̸= 1 forc >0.
Step 2: branch and interior. Mc is analytic near D\ {¯η}, and in DImM c = 2cRe 1+ηz
1−ηz > 0.
The square root with values in the closed first quadrant is continuous on the closed upper
half-plane and analytic on the open one. Hence fc is analytic and zero-free in D and continuous
on D\ {¯η}. By (6), fc(0) = c + i and f′
c(0) = M′
c(0)/(2fc(0)) = 2ic/s. In qc/fc only the term in
z−1 is singular at 0. Its coefficient is b0
2
c+i
fc(0) = b0
2 , which cancels the term −ib0
2 z−1 of (11). The
constant coefficient ofh c is
ia0 + i(1−c 4)
fc(0) − ib0
2
f′
c(0)
fc(0) =ic 3 + (1−c 2)(1 +ic) +c(c−i) = 1,
using 1/(c+i) = (c−i)/s 2. Henceh c is analytic inDandh c(0) = 1.
Step 3: the circle away from the exceptional points.Write η = eiβ, z = eiϕ, ψ = ϕ + β. Then
Mc(eiϕ) =c 2 −1−2ccot(ψ/2),
which is real and strictly increasing for ψ∈ (0, 2π), from −∞ to +∞. So Mc < 0 on one open
arc and Mc > 0 on the complementary open arc, the zero η3 and the pole ¯ηbeing the endpoints.
The boundary root is fc = √Mc > 0 where Mc > 0, and fc = iG with G = √−Mc > 0 where
Mc < 0. On the circle 1 −¯η/z= 1−ηz , so by (13)q c = −s2
2 Mc|1 −ηz| 2 is real: negative where
Mc > 0 and positive where Mc < 0. The terms ia0 −ib 0 cosϕ of (11) are purely imaginary there.
Where Mc > 0, iqc/fc is purely imaginary, so uc = 0 and wc = −qc/fc > 0. Where Mc < 0,
iqc/fc =q c/Gis real, sou c =q c/G >0, Imhc =a 0 −b 0 cosϕandw c = 0.
Step 4: the two exceptional points.For z∈ D\ {0,¯η}we have |fc|2 = |Mc| and, by (12),
|Mc| = s2|z−η 3|/|z−¯η|(use |η2 −¯ηz|= |z−η 3| and |1−ηz| = |z−¯η|). With |1−¯η/z|= |z−¯η|/|z|,
(13) gives qc(z)
fc(z)
 = s2
2 |Mc|1/2 |1−ηz||1−¯η/z|= s3
2
|z−η 3|1/2 |z−¯η|3/2
|z| .
5

This is bounded and tends to 0 as z→η 3 or z→¯η within D, with orders 1/2 and 3/2 respectively.
Since qc/fc is continuous elsewhere on D\ {0}, hc extends continuously to the whole closed disk,
with hc = ia0 −ib 0 cosϕ at both exceptional points. There uc = 0 and wc = 0, so the inequalities
of Step 3 hold at the endpoints of both arcs.
Step 5: the interior. Reh c is harmonic in D, continuous on D and ≥ 0 on the circle. By the
minimum principle Reh c ≥0 inD, and strictly positive because Reh c(0) = 1.
This limiting pair is not a polynomial certificate at ( a0, b0). Its real part vanishes on an arc,
unlike the strictly positive boundary real part in Lemma 3.
5 Constructing a finite polynomial certificate
By the rotation byπ/2 assumeb≥0, and put
a∗(b) =
 
max{b2/3 −1,0}
3/2,(14)
so that b <(1 + a2/3)3/2 is equivalent to a > a∗(b). We first fix acritical function h∗ for each
b≥0: an analytic function onD, continuous on D, withh ∗(0) = 1, Reh ∗ ≥0 on the circle and
Imh ∗(eiϕ) +bcosϕ≤a ∗(b) (ϕ∈R).(15)
 If b >1, take c =
p
b2/3 −1 , so that b0 = s3 = b and a0 = c3 = a∗(b), and h∗ = hc. Then
(15) is the inequalityw c ≥0 of Lemma 4.
 If 0 ≤b≤ 1, take h∗(z) = 1−ibz. On the circle Reh ∗ = 1+ bsinϕ≥ 0 and Imh ∗ +bcosϕ =
0 = a∗(b). This treats b = 0 and b = 1 without the singular endpoint c = 0 of the critical
formula.
In both cases the measure dµ(t) = Reh ∗(eit) dt/2π has a continuous density, hence no atoms,
and total mass Reh ∗(0) = 1. Poisson’s formula for Reh ∗ and its harmonic conjugate, together
withh ∗(0) = 1, give for 0< σ <1
h∗(σz) =
Z 2π
0
Kσ(t, z)dµ(t), K σ(t, z) =1 +σe −itz
1−σe −itz ,|z| ≤1; (16)
the imaginary constant is zero becauseh ∗(0) = 1.
Poisson smoothing. Imh ∗(σeiϕ) and bσcosϕ are the Poisson integrals at radius σ of Imh ∗(eiϕ)
and bcosϕ . Integrating (15) against the positive Poisson kernel gives Imh ∗(σeiϕ) + bσcosϕ≤
a∗(b), hence
Imh ∗(σeiϕ) +bcosϕ≤a ∗(b) +b(1−σ).(17)
Discretization.Approximating µ by equal-weight empirical measures, with the kernel contin-
uous jointly in t and |z| ≤1, gives uniform approximation on the closed disk. Thus for σ <1
witha ∗(b) +b(1−σ)< a, and then for sufficiently largeN,
hN (z) = 1
N
NX
j=1
1 +α jz
1−α jz , α j =σe −itj ,
retains a strict margin in (17). The product of the quadratic forms (4) is then a strict certificate.
The next proposition gives an explicit choice of a sufficientN, valid for everyb≥0.
Proposition 5(A sufficient degree bound).Let b≥ 0, a∗ = a∗(b)as in (14), and δ = a−a ∗ > 0.
Set
τ= min{1/2, δ/(4b)}(τ= 1/2ifb= 0), σ= 1−τ, N= max

1,
16πσ
δτ 2

.
6

There is a strict polynomial certificate of degree2 N whose normalized angular margin a−bcos 2θ−
p′/(2Np)is at leastδ/2. If0< δ≤2b, one may use
N≤
256πb2
δ3

,
and if δ >2b (in particular for b = 0), one may use N≤max{ 1,⌈32π/δ⌉}. This is a sufficient
bound, not the minimum degree.
Proof. Use h∗ and µ as above. Partition [0 , 2π] into N successive quantile intervals Ij, each
of µ-mass 1/N (possible since µ has no atoms), and choose tj ∈I j. Intervals may cross zero-
density gaps; their lengths still sum to 2 π. For the kernel Kσ(t, z) in (16), with w = σe−itz,
∂tKσ =−2iw/(1−w) 2, so
sup
t,|z|≤1
|∂tKσ(t, z)| ≤ 2σ
(1−σ) 2 = 2σ
τ2 .
The integral-minus-empirical error is therefore at most
X
j
Z
Ij
2σ
τ2 |Ij|dµ= 2σ
τ2 · 1
N
X
j
|Ij|= 4πσ
Nτ 2 ≤ δ
4.
The smoothing loss in (17) is bτ≤δ/ 4, so Imh N + bcosϕ≤a ∗ + δ/2, a margin at least δ/2
in a. If δ≤ 2b, then τ = δ/(4b) ≤ 1/2 and σ≤ 1 give N≤ ⌈16π· 16b2/δ3⌉. If δ >2b, then
τ=σ= 1/2 andN= max{1,⌈32π/δ⌉}.
Locating the quantiles with rigorous numerical enclosures is an additional computational task.
Proposition 5 is an analytic construction and degree bound, not a claim that the floating-point
experiment below implements a certified algorithm.
6 Local analytic certificates and degree divergence
We complete the equivalences of Theorem 1. Let V be a local real-analytic weak certificate, with
Taylor expansion V = Pm + Pm+1 + ··· at the origin, where Pj is homogeneous of degree j and
Pm ̸= 0. Along each ray, V (tx) = tmPm(x) +O(tm+1) > 0 gives Pm ≥ 0. Since f is homogeneous
of degree three, Lf V (tx) = tm+2Lf Pm(x) + O(tm+3) ≤ 0, so Lf Pm ≤ 0 (the polynomial Lf Pm
may well vanish identically; only the inequality is used). With Pm(r, θ) = rmpm(θ) and (2), this
reads
p′
m(θ) +m(−a+bcos 2θ)p m(θ)≤0.(18)
Lemma 6.If p≥ 0is a continuous,2 π-periodic, piecewise C1 function, not identically zero,
satisfyingp ′ +m g p≤0for a continuous periodicg, thenp >0everywhere.
Proof. Let ρ(θ) = exp
Rθ
0 m g ds >0. Then ( ρp)′ ≤ 0. If p(θ0) = 0, the function ρp is nonnegative,
nonincreasing on [θ0, θ0 +2π] and zero at θ0, hence zero throughout, and by periodicity p≡ 0.
Hence Pm is positive definite. Its degree m is even, since Pm(−x) = (−1)mPm(x) and Pm ≥ 0,
Pm ̸= 0. So Pm is a positive definite homogeneous weak polynomial certificate, and the strict
obstruction of Section 3 applies to it. This is the leading-term mechanism already used in [ 1,
Sec. III-D] for the single field ( a, b) = (1, 5); the argument is unchanged for every a >0, b∈R ,
so combining it with [ 1, Theorem IV.3] also gives local analytic nonexistence for |b| ≥2(a + 1).
Conversely, the constructed polynomial is analytic. Together with the preceding sections this
proves Theorem 1.
Proposition 7.For fixed b >1, the minimum degree among positive homogeneous polynomial
weak certificates tends to infinity asa↓a ∗(b) = (b2/3 −1) 3/2.
7

Proof. Suppose not. Then there are N and an ↓a ∗ and positive definite homogeneous weak
certificates Pn of degree at most 2 N at parameters (an, b); passing to a subsequence, all have
the same degree 2 N′ ≤ 2N. Let pn(θ) = Pn(cosθ,sinθ ) and normalize maxp n = 1 (scaling
Pn). The map from binary forms of degree 2 N′ to trigonometric polynomials with frequencies
0,±2, . . . ,±2N′ is a linear isomorphism of spaces of dimension 2N′ + 1. The coefficients of Pn are
bounded, because max|p n| = 1 and all norms on this finite-dimensional space are equivalent. A
subsequence therefore converges, with all derivatives, to p = P(cosθ,sinθ ) for a binary form P of
degree 2N′ (possibly of lower Fourier degree, which does not matter), with p≥ 0 and maxp = 1.
Passing to the limit in p′
n + 2N′(−an + bcos 2θ)pn ≤ 0 gives the same inequality for p at a = a∗.
By Lemma 6, p >0, so P is a positive definite homogeneous polynomial with Lf P≤ 0 at the
excluded boundaryb 2/3 = 1 +a 2/3
∗ . This contradicts Theorem 1.
This compactness method has antecedents in [ 2, Theorem 4.3]. Propositions 5 and 7 do not
give matching upper and lower degree rates.
7 Single harmonics, angular speed and sum of squares
The same extremal argument applies to a family in every odd degree. Let k≥ 1, a >0, b∈R ,
andω̸= 0, and consider
˙r=r 2k+1(−a+bcos 2kθ), ˙θ=ωr 2k.(19)
It is a polynomial vector field of degree 2k+ 1:
f(x, y) =

−a(x2 +y 2)k +bRe(x+iy) 2k
(x, y) +ω(x2 +y 2)k(−y, x).
Corollary 8.For (19), homogeneous polynomial weak, strict polynomial, and local real-analytic
weak certificates exist exactly when
|b|2/3 < a2/3 +|ω| 2/3.(20)
All these fields are globally asymptotically stable. The degree bound of Proposition 5, applied to
a/|ω|and|b|/|ω|, becomes2kNfor these fields.
Proof. Reductions.Multiplying the field by a positive constant does not change the certificates,
since Lλf V = λLf V ; this replaces ( a, b, ω) by (a, b, ω)/|ω|. The reflection ( x, y) 7→ (x,−y ) is a
linear change of variables sending θ7→ −θ; it leaves cos 2kθ and r unchanged and reverses the
sign of θ′ = ωr2k, so it maps (19) with ω to (19) with −ω, and polynomial or analytic certificates
to certificates of the same kind and degree. The rotation by π/(2k) maps cos 2kθ to −cos 2kθ and
keeps θ′, so it replaces b by −b. Hence we may assume ω = 1, b≥ 0; (20) becomes b2/3 < 1 +a2/3
(witha, breplaced bya/|ω|,|b|/|ω|).
The Lie derivative.For a homogeneousP=r mp(θ) andω= 1,
Lf P= ˙r ∂rP+ ˙θ ∂θP=r m+2k
m(−a+bcos 2kθ)p+p ′
.
Let m = 2N and P be positive definite. By Lemma 3, p′/(2Np) = Imh (e2iθ); with ϕ = 2θ,
Lf P≤0 is exactly
w(ϕ) :=a−bcos(kϕ)− Hu(ϕ)≥0, u= Reh,⟨u⟩= 1, u≥ε >0.(21)
Necessity (any k, any candidate polynomial).Use the test fc(σzk) in place of fc(σz), z = eiϕ:
write fc(σeikϕ) = Fσ(ϕ)+iGσ(ϕ). This is the boundary value of the functionz7→f c(σzk), analytic
in D and continuous on D, so Gσ = HFσ + ⟨Gσ⟩ and Fσ + HGσ = ⟨Fσ⟩, with ⟨Fσ⟩ = Ref c(0) = c
and ⟨Gσ⟩ = Imf c(0) = 1. Because Fσ + iGσ takes values in the open first quadrant, Fσ, Gσ > 0.
8

Finally, expanding fc(ζ) = P
n≥0 φnζn, only n = 1 contributes to ⟨Gσ coskϕ⟩ , namely Im(σφ1)/2,
andφ 1 =f ′
c(0) = 2ic/s:
⟨Gσ coskϕ⟩= σc
s , F σ +HG σ =c.
(These are the identities (7) for k = 1; they were also checked numerically for k = 1 , 2, 3,
see Section 8.) The pairing (8) then holds verbatim with cosϕ replaced by coskϕ : by skew-
adjointness of H, ⟨uFσ +wG σ⟩ = ⟨u(Fσ +HG σ)⟩ + a⟨G σ⟩ −b⟨Gσ coskϕ⟩ = c + a−bσc/s≥εc .
As in Section 3 this gives b <(a + c)
√
1 +c 2/c for every c >0, hence b <(1 +a2/3)3/2. No k-fold
angular symmetry of the candidate is assumed.
Sufficiency.Let b≥ 0, a > a∗(b), and let α1, . . . , αN be the nodes of Proposition 5, with hN
the corresponding strict-margin function: Imh N (eiψ) +bcosψ≤a−δ/2 for allψ. Put
P(x, y) =
NY
j=1
(x−iy) k −α j(x+iy) k2 =
NY
j=1
h
(1 +|α j|2)(x2 +y 2)k −2 Re
 
αj(x+iy) 2ki
.
Each factor is a positive definite binary form of degree 2 k (on the circle it equals |1 −α je2ikθ|2 ≥
(1 − |αj|)2), and P has degree 2kN. Differentiating the logarithm of each factor, with ζ = e2ikθ,
gives d
dθ log|1−αζ| 2 = 4kIm αζ
1−αζ = 2kIm 1+αζ
1−αζ , hence
p′(θ)
2kNp(θ) = Imh N (e2ikθ), Lf P
2kN r2kN+2k p ≤ −δ
2 <0
on the circle by the formula for Lf P above (with m = 2kN, ψ = 2kθ). Hence P is a strict
polynomial certificate of degree 2 kN. The reductions above restore arbitrary ω̸ = 0 and b∈R
without changing the degree. The reflection and rotation reductions, the product formula and
the sign of Lf P were also checked numerically in Cartesian coordinates for several ( k, a, b, ω),
includingk= 2,3,ω <0 andb <0 (Section 8).
Local analytic certificates.The argument of Section 6 carries over: for a local analytic weak
certificate with leading term Pm one has Pm ≥ 0 and Lf Pm = rm+2k[p′
m +m(−a+bcos 2kθ)pm] ≤
0 (ω = 1). Lemma 6 gives that Pm is positive definite, hence of even degree, and the necessity
argument above applies to it.
Stability.For ω̸ = 0 let H = r2 exp[− b
kω sin 2kθ]. Then ∂rH = 2 H/r and ∂θH =
−2b
ω cos(2kθ)H, so
Lf H=r 2k+1(−a+bcos 2kθ) 2H
r − 2b
ω cos(2kθ)ωr 2kH=−2ar 2kH.
Its bounded positive angular factor gives e −βr2 ≤H≤ eβr2, β = |b|/(k|ω|), and C1 regularity
at zero (as for k = 1, by [1, Lemma III.1]). Decrease of H bounds all trajectories and prevents
finite-time escape; with Lf H <0 away from the origin, Lyapunov’s direct method gives global
asymptotic stability.
For k = 1, write bcos 2θ + dsin 2θ = ρcos (2θ−γ ) with ρ =
√
b2 +d 2; the rotation of
coordinates by γ/2 (which commutes with θ′ = ωr2) turns it into ρcos 2θ. The criterion becomes
(b2 +d 2)1/3 < a2/3 +|ω| 2/3.
No result for ω = 0 or a general sum of different angular harmonics follows from this argument.
Corollary 9(Classical binary-form SOS consequence).The strict certificate region in Theorem 1
and Corollary 8 is also the region admitting a homogeneous certificate P such that P and −Lf P
are positive definite sums of squares. The same sufficient Lyapunov degree bounds apply.
9

Proof. Any positive definite real binary formU of degree 2m is a sum of two squares of real forms of
degree m. Indeed U(x, 1) has positive leading coefficient and no real roots. Splitting its roots into
nonreal conjugate pairs gives U(x, 1) = F(x)F(x). Homogenizing F yields U = (ReF )2 +(ImF )2.
Apply this classical fact separately to the strict constructed P and −Lf P. The reverse implication
is immediate.
Ahmadi and Parrilo [ 2, Theorem 5.3] show that any homogeneous polynomial vector field
with a strict homogeneous polynomial Lyapunov function ( V and − ˙V positive definite) admits a
homogeneous SOS one,of possibly higher degree. In the planar case treated here the classical
two-square fact above keeps the degree; no new general SOS theorem is claimed. For any such
field the coefficients of Lf P depend linearly on those of P. Both P and −Lf P are strictly
positive on the compact unit circle, hence (by homogeneity) on R2 \ {0}, and this persists under
sufficiently small changes of the coefficient vector of P. A rational coefficient vector can be
chosen in that neighborhood, so a rational-coefficient strict polynomial certificate exists as well.
This does not assert a two-square decomposition over the rationals.
8 Verification and limitations
The proofs above use explicit analytic identities and inequalities, not a numerical optimization
result. The following computations are floating-point or high-precisionsanity checks, not part of
any proof, and none is interval-certified.
Reproducible checks in the supplement.The script check v2.py (Python with numpy
and mpmath, output check v2 output.json) evaluates, with 40-digit arithmetic, Lemma 4
for c∈ { 1/8, 1/2, 1, 5/2, 8}: hc(0) = 1, Reh c ≥ 0 on a polar grid of the closed disk
(the smallest value is of rounding size, below 10 −38 in modulus), wc ≥ 0 and ucwc = 0
on the circle, identity (13), and the vanishing orders 0 .5 and 1 .5 of qc/fc at η3 and ¯η
(measured slopes 0 .500000001, 1 .500000002). It also builds the products of Corollary 8
with N = 1024 factors and σ = 0 .98, directly in Cartesian coordinates, for ( k, a, b, ω) ∈
{(1, 1.2, 2, 1), (2, 1.2,−2,−1), (3, 2.4, 4, 2), (2, 0.6, 0.8, 1), (2, 0.5, 0, 1)}; the largest sampled value
of Lf P/(2kN P) on the circle (20001 angles) is negative in each case (for example −0.688 for the
first two, matching a−max (Imh N + bcos )). Finally it confirms the identities ⟨Fσ⟩ = c, ⟨Gσ⟩ = 1,
⟨Gσ coskϕ⟩=σc/s,F σ +HG σ =cfork= 1,2,3 to about 10 −13.
An anecdotal example from version 1.One finite product of 2048 quadratic factors was evalu-
ated at 8192 angular samples for a = 1.2, b = 2
√
2, σ = 0.98 (script check phase30.py, output
phase-checks-30.json); the sampled normalized margin was about 0 .1545. It is illustrative
only: it is not a certified positivity check, not a minimum-degree result, and nothing in the paper
depends on it. A further exploratory Toeplitz-relaxation program of version 1 is dropped from
the text; its script and stored output remain in the supplement, with their solver-status caveats,
and no conclusion here relies on them.
Review status.The manuscript was written with AI assistance. Version 1 received separate
automated reviews by Claude Sonnet 5.5 and Claude Haiku 5.5; version 2 responds to them.
These are not human, blind or independent peer reviews (the reviewer and the drafting assistant
belong to the same model family), and not formal verification. No Lean formalization of this
argument exists; the Lean development mentioned in [ 1] concerns their Theorem II.2 only. A
rigorously enclosed implementation of the quantile selection is not supplied; the quantitative
construction is analytic.
Sources.The comparison with Liu–Fitzsimmons uses the complete text of arXiv:2607.16171v1
(the only version found on 21 October 2026). The cited theorem statements of Ahmadi–Parrilo
(Theorems 4.3 and 5.3) and of Ahmadi–El Khadir (Proposition 6.1) were checked against their
texts, but those works were not read in full. Targeted searches did not locate this boundary;
worldwide priority is unconfirmed, particularly for the associated harmonic extremal problem.
Minimum-degree asymptotics and general multiharmonic classification remain open here.
10

References
[1] J. Liu and M. Fitzsimmons,A globally asymptotically stable planar homogeneous polynomial vector
field with no polynomial Lyapunov function, arXiv:2607.16171v1, 17 July 2026. https://arxiv.org/
abs/2607.16171v1.
[2] A. A. Ahmadi and P. A. Parrilo,Stability of polynomial differential equations: complexity and converse
Lyapunov questions, arXiv:1308.6833. Theorem numbers (4.3, 5.3) as in arXiv v1 and the author-hosted
manuscript:https://web.mit.edu/ ~a_a_a/Public/Publications/Selected_Papers/dTAC.pdf.
[3] A. A. Ahmadi and B. El Khadir,On algebraic proofs of stability for homogeneous vector fields, IEEE
Trans. Automat. Control65(2020), 325–332. Proposition 6.1 and Lemma 6.2 as numbered in the
2018 preprint (cited as Proposition VI.1 in [ 1]): https://optimization-online.org/wp-content/
uploads/2018/03/6502.pdf.
11