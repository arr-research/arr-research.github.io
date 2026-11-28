# Exact Dipole Inner-Product Geometry, Sharp K = 16 Phase Transitions, Uniform-Sign Collapse, Odd-K Cyclotomic Dichotomies, and Global Minimax Radii for Huffman Sequences

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6GGEN2JJ8S8MSRH0` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/paper148-huffman-distance-barriers (`v1.0.1`)  
**Canonical PDF SHA-256:** `f9c4e0017e02eb53d761d593cfb847becc38271e3e9e06123908719152d96cba`

## Abstract

Huggins, Sahin, and Erkip (2026, arXiv:2611.34807v1) characterized pairwise Euclidean distances between spectral factors sharing an aperiodic autocorrelation function (AACF) via ternary flip patterns s in {-1, 0, 1}^K, proving Dihedral invariance for Huffman codes, asymptotic small-R and even-K large-R lower bounds, and a numerical conjecture that the piecewise single-flip/alternating bound Eq. (16) is globally tight for all even K <= 14 while breaking down at K = 16. We resolve the analytic, combinatorial, arithmetic, and global minimax structure of Huffman sequence distances via four self-contained theorems backed by 20 constructive Lean 4.36.0 theorems (zero external imports, zero sorry, zero Classical.choice, zero warnings), 16 AST-audited zero-float exact-Q/cyclotomic SHA-256 certificates (MANIFEST SHA-256: 5d22c0012d4cc4d2314a12eb722bb82b97ea44f7eb7e2ebd4a0ac8544a0beff8), and 69 adversarial tests: (1) Exact Dipole Law, Sharp K = 16 Phase Transition, and Universal O(1/K) Ceiling: via Cauchy residue calculus on |z| = 1, we derive the closed-form dipole inner product I_{e0 - em}(R) and its exact positivity-factored squared modulus, proving strict monotonicity in 1 - cos(2*pi*m/K) (m = 1 maximizes |I| for all R > 1, K >= 2, uniquely up to dihedral reflection), resolving the crossover root R_0 > 1 of p_K(R) = R^{2K} - R^{2K-1} - 4R^K - R + 1 to show |I_{s2}(R_0)| > |I_{e0}(R_0)| = |I_{sa}(R_0)| iff u_crit(R_0) > 1 - cos(2*pi/K) (false for all even K in {2..14}, K=14 ratio 0.9564 < 1; true for all even K >= 16, K=16 ratio 1.0096 > 1, bridged unconditionally to K >= 34), and establishing the non-asymptotic universal ceiling sup_{R>1} d_min^2(R) < 7E/K with exact asymptotic limit C_* E = f_2(x_*) E approx 6.26130 E < 2*pi E (attained at x_* approx 3.20820 > pi); (2) Universal Uniform-Sign Hamming-Weight Collapse: every uniform-sign pattern in {0, 1}^K or {0, -1}^K of weight w satisfies I_s(R) = E(R^{K-w} + R^{-(K-w)})/(R^K + R^{-K}) independent of support, collapsing 2(2^K - 1) nonzero patterns onto K rational curves, yielding exact non-dihedral collisions (including (-1,-1,0,0) vs (-1,0,-1,0) at K = 4 and a mixed-vs-uniform collision at K = 6) and tightening distinct-distance counts strictly below Dihedral orbit counts; (3) Complete Odd-K Arithmetic Dichotomy and Cyclotomic Galois Vanishing-DFT Bound: via irreducibility of Phi_q(X) over Q, we prove m_0(s) <= K/p_min(K) with equality iff s has minimal period p_min(K), separating composite odd K (Theta_K(R^{-2K/p_min(K)}), e.g. Theta(R^{-6}) at K = 9) from every odd prime K = p >= 3 (Theta_p(R^{-2}), with exact constants at K = 3, 5 and twin-dipole O(p^{-4} R^{-2}) suppression for all odd primes p >= 5); and (4) Exact Global Minimax Radii (K = 2, 3, 4) and Phase Separation: unconditional global minimax optimality at R_* = phi^2 (d_min^2 = 8E/7, I = 3E/7) for K = 2, R_*^2 + R_*^{-2} = (5 + sqrt(29))/2 (|I|^2 = (37 + 6*sqrt(29))E^2/325) for K = 3, and R_0 = rho^2 (plastic ratio squared) for K = 4 via positive-coefficient polynomial dominance over all D_K x Z_2 orbits, plus unbounded unphased-vs-phase-invariant separation on anti-palindromic patterns.

## Full Extracted Text

--- Page 1 ---
Exact Dipole Inner-Product Geometry , Sharp K = 16
Phase T ransitions, Uniform-Sign Collapse, Odd-K
Cyclotomic Dichotomies, and Global Minimax Radii
for Huffman Sequences
Lluis Eriksson∗
November 28, 2026
Abstract
Huggins, Şahin, and Erkip [ 1] ( arXiv:2611.34807v1) recently characterized pairwise
Euclidean distances between spectral factors sharing an aperiodic autocorrelation function
(AACF) via ternary flip patterns s ∈ {−1, 0, 1}K, proving Dihedral invariance for Huffman
codes H, asymptotic small-R and even-K large-R lower bounds, and a numerical conjecture
that the piecewise single-flip/alternating bound [ 1, Eq. (16)] is globally tight for all even
K ≤ 14 while breaking down at K = 16 . Here we resolve the analytic, combinatorial, arith-
metic, and global minimax structure of Huffman sequence distances via four self-contained
theorems, backed by 20 constructive Lean 4.36.0 theorems (zero external imports, zero
sorry, zero Classical.choice, zero compiler warnings), 16 AST-audited zero-float exact-
Q/cyclotomic SHA-256 certificates ( MANIFEST SHA-256 : 5d22c0012d4cc4d2314a12eb722b
b82b97ea44f7eb7e2ebd4a0ac8544a0beff8), and 69 adversarial tests. (1) Exact Dipole
Law, Sharp K = 16 Phase T ransition, and Universal O(1/K) Ceiling: Via Cauchy
residue calculus on |z| = 1 , we derive the closed-form dipole inner product Ie0−em(R)
and its exact factored squared modulus, proving strict monotonicity in 1 − cos(2πm/K)
(m = 1 maximizes |Ie0−em(R)| for all R > 1, K ≥ 2). At the crossover root R0 > 1 of
pK(R) = R2K −R2K−1 −4RK −R+1, we prove |Is2 (R0)| > |Ie0 (R0)| = |Isa(R0)| holds if and
only if ucrit(R0) > 1−cos(2π/K), which is false for every evenK ∈ {2, 4, . . . , 14} (K = 14 ra-
tio 0.9564 < 1; K = 2 exact tie) and true for every even K ≥ 16 (K = 16 ratio 1.0096 > 1),
bridged unconditionally to all K ≥ 34. Combining Ie0 and Is2 yields a non-asymptotic
minimax ceiling supR>1 d2
min(R) ≤ 7E/K for all K ≥ 2 with exact asymptotic constant
limK→∞ K supR>1 min(d2
e0 , d2
s2 ) = C∗E ≈ 6.26130E < 2πE (attained strictly above the
crossing x = π, at the unique root x∗ ≈ 3.20820 of (x2 − π2) sinh(2x) = 2 x(x2 + π2)). (2)
Universal Uniform-Sign Hamming-W eight Collapse: By direct residue/Laurent co-
eﬀicient extraction, every uniform-sign pattern s ∈ {0, 1}K or {0, −1}K of weight w = ∥s∥1
has real inner product Is(R) = E(RK−w + R−(K−w))/(RK + R−K) independent of sup-
port, collapsing all 2(2K − 1) nonzero uniform-sign patterns onto K rational curves, pro-
ducing exact non-dihedral collisions (e.g. (−1, −1, 0, 0) vs. (−1, 0, −1, 0) at K = 4 and a
mixed-vs-uniform collision at K = 6 ), and strictly tightening distinct-distance counts below
Dihedral orbit counts. (3) Odd- K Arithmetic Dichotomy and Cyclotomic Galois
V anishing-DFT Bound: Using irreducibility of cyclotomic polynomials Φd(X) over Q,
we prove the sharp bound m0(s) ≤ K/pmin(K) for every nonzero balanced ternary pat-
tern, with equality if and only if s has minimal period pmin(K). Consequently , as R → ∞,
d2
min(R) = Θ K(R−2K/pmin(K)) for composite K (e.g. Θ(R−6) at K = 9 ) versus ΘK(R−2)
for every odd prime K = p ≥ 3, with closed-form constants for K = 3 , 5 and twin-
dipole O(p−4R−2) suppression for all odd primes p ≥ 5. (4) Exact Global Minimax
∗ Independent Researcher. ORCID: 0009-0006-7494-9040. Code, Lean 4 formal proofs, and exact ratio-
nal/cyclotomic certificates: https://github.com/lluiseriksson/paper148-huffman-distance-barriers (tag
v1.0.1). Manuscript and figures licensed under CC-BY-4.0; code, Lean 4 proofs, and tests under MIT.
1
AIRR:ARR-2026-6GGEN2JJ8S8MSRH0 v1  [Information theory]  28 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
Radii ( K = 2 , 3, 4) and Phase Separation: W e prove unconditional global minimax
optimality at R∗ = φ2 (d2
min = 8 E/7, I = 3 E/7) for K = 2 , at R2
∗ + R−2
∗ = (5 +
√
29)/2
(|I|2 = (37 + 6
√
29)E2/325) for K = 3 , and at R0 = ρ2 (plastic ratio squared) for K = 4 via
positive-coeﬀicient polynomial dominance over all DK ×Z2 orbits, and establish unbounded
unphased-versus-phase-invariant separation on anti-palindromic patterns.V erification scope:
Finite algebraic identities, rational brackets, cyclotomic DFT s, and shifted polynomial dom-
inance certificates are machine-checked constructively in Lean 4 and exact- Q Python; com-
plex contour integrals, cyclotomic irreducibility over Q, and asymptotic K → ∞ / K ≥ 34
bridges are proved analytically in the text.
1 Introduction and Preliminaries
Huffman sequences [2] are finite-length complex sequences whose aperiodic autocorrelation func-
tion (AACF) vanishes at every nonzero lag except the extreme lags ±K. Originally studied for
radar pulse compression [3, 4, 5] and shown to admit neither uniform-magnitude [ 6] nor generic
integer solutions [ 7], Huffman sequences have recently found renewed utility in noncoherent
short-packet communication and integrated sensing and communication (ISAC) [ 8, 9, 10].
F ollowing Huggins, Şahin, and Erkip [ 1], let x = [ x0, . . . , xK]T ∈ CK+1 have z-transform
X(z) = PK
k=0 xkzk, energy E = ∥x∥2
2 > 0, and AACF
AH(z) = E(−ηz−K + 1 − ηzK), η := 1
RK + R−K , R > 1. (1)
The zeros of AH(z) lie uniformly on two conjugate-reciprocal circles of radii R and R−1, at
αk = Rϕk and 1/α∗
k = R−1ϕk where ϕ := e2πi/K and k ∈ [K] := {0, 1, . . . , K − 1}. Starting
from the minimum-phase spectral factor X0(z) (all zeros inside the unit circle), every spectral
factor Xi(z) of AH(z) with fixed global phase θ = Arg( x(0)
K ) is indexed by a binary flip vector
b(i) ∈ ZK
2 :
Xi(z) = X0(z)
Y
k:b(i)
k =1
Bk(z), B k(z) := 1
R
z − Rϕk
z − R−1ϕk . (2)
F or any pairxi, xj in the resulting Huffman code H ⊂ CK+1, Huggins et al. [1, Eq. (8), Prop. 1,
Cor. 1] proved that their correlation Xi(z)X∗
j (z−1) = AH(z)Ps(z) and inner product ⟨xi, xj⟩ =
Is(R) depend solely on the ternary signed flip pattern s := b(i) − b(j) ∈ {−1, 0, 1}K, where
Ps(z) :=
Y
k:sk=1
Bk(z)
Y
k:sk=−1
Bk(z)−1, (3)
and the phase-invariant lower bound on minimum squared Euclidean distance across arbitrary
global-phase assignments θ = ( θ0, . . . , θ2K−1) [1, Eq. (10)–(11)] is
d2
min(R) := min
s∈{−1,0,1}K\{0}
 
2E − 2|Is(R)|

, R ∗ := arg max
R>1
d2
min(R). (4)
Using (K + 1)-point Parseval summation [ 1, Eq. (3), (13)], Huggins et al. established Dihedral
invariance under DK ([1, Prop. 3]), small- R dominance of the single-flip patterns ±ek giving
Ie0 (R) = Eη(RK−1 + R−(K−1)) ([1, Prop. 4]), and for even K large-R dominance of the alter-
nating patterns ±sa = ±[1, −1, . . . , 1, −1]T giving |Isa(R)| = E(1 − 4η) for R ≥ (2 +
√
3)1/K
([1, Prop. 5]). Equating these two curves produces the unique root R0 ∈ (1, 3) of
pK(R) := R2K − R2K−1 − 4RK − R + 1 = 0 , (5)
prompting the conjecture [ 1, Sec. IV-B] that the piecewise single-flip/alternating formula [ 1,
Eq. (16)] is exact for all even K ≤ 14, whereas numerical checks at K = 16 found the adjacent
dipole s2 = [1 , −1, 0, . . . , 0]T overtaking both patterns near R0.
2

--- Page 3 ---
Our Contributions. Replacing the discrete (K +1)-point DFT sum of [1] with direct Cauchy
residue calculus on the unit circle |z| = 1 unlocks exact closed-form rational and cyclotomic
laws across every regime left open by [ 1]:
1. Theorem 2.1 (Section 2): Exact closed-form dipole inner product Ie0−em(R), exact
positivity factorization proving strict monotonicity in 1 − cos(2πm/K), sharp analytic
resolution of the K = 14 vs. K = 16 phase transition at R0(K) (and all even K ≥ 16),
and a non-asymptotic universal O(1/K) minimax ceiling supR>1 d2
min(R) ≤ 7E/K with
exact asymptotic limit C∗E ≈ 6.26130E < 2πE.
2. Theorem 3.1 (Section 3): Universal uniform-sign Hamming-weight collapse Is(R) =
E(RK−w + R−(K−w))/(RK + R−K), exact general Cauchy-residue formula for arbitrary
s ∈ {− 1, 0, 1}K, non-dihedral collisions (including a K = 6 mixed-vs-uniform collision),
and strict distinct-distance tightening.
3. Theorem 4.1 (Section 4): Complete odd-K arithmetic dichotomy via cyclotomic Galois
theory: m0(s) ≤ K/pmin(K) with equality iff s has minimal period pmin(K), proving
ΘK(R−2K/pmin(K)) decay for composite K vs. ΘK(R−2) for every odd prime K = p ≥ 3
with twin-dipole O(p−4R−2) suppression.
4. Theorem 5.1 (Section 5): Unconditional global minimax optimality across all DK ×Z2
orbits for K = 2 , 3, 4 (R∗ = φ2, R2
∗ + R−2
∗ = (5 +
√
29)/2, and R0 = ρ2), plus exact
separation between unphased and phase-invariant distance metrics.
Throughout, we normalize without loss of generality by E > 0; every identity scales linearly
in E, and d2/E is scale-free.
2 Exact Dipole Inner-Product Law, Sharp K = 16 T ransition,
and Universal O(1/K) Ceiling
By Cauchy’s integral formula, the constant term c0 of the Laurent polynomial Xi(z)X∗
j (z−1) =
AH(z)Ps(z) equals
Is(R) = 1
2πi
I
|z|=1
AH(z)Ps(z)dz
z . (6)
Deforming the constant and −ηzK terms inward (to poles in |z| < 1) and the −ηz−K term
outward (to poles in |z| > 1, avoiding the order- (K + 1) pole at z = 0 ) yields closed forms
directly .
Theorem 2.1 (Dipole Law, Sharp K = 16 Phase T ransition, andO(1/K) Ceiling). Let K ≥ 2,
R > 1, X := R2K, and E > 0.
(a) (Exact Dipole F ormula and Monotonicity)F or every dipoles = e0−em (1 ≤ m < K )
with w := e2πim/K and c := cos(2 πm/K),
Ie0−em(R) = E (X + 1)(R2 + w − 2) + 2( R2 − 1)(w − 1)
(X + 1)(R2w − 1) . (7)
Setting A := X(R2 − 2) − R2 and B := X + 2R2 − 1, one has A + B = ( X + 1)(R2 − 1),
AB + (X + 1)2R2 = 2( R2 − 1)(R2 + X)(X − 1) > 0, and
|Ie0−em(R)|2
E2 = (X + 1)2(R2 − 1)2 − 2AB(1 − c)
(X + 1)2 
(R2 − 1)2 + 2R2(1 − c)

= 1 − 4(1 − c)(R2 − 1)(R2 + X)(X − 1)
(X + 1)2 
(R2 − 1)2 + 2R2(1 − c)
. (8)
3

--- Page 4 ---
Consequently, |Ie0−em(R)| is strictly decreasing in 1−c, so the adjacent dipole s2 := e0 −e1
maximizes |Ie0−em(R)| among al l dipoles1 ≤ m < K for every R > 1 and K ≥ 2 (uniquely
up to dihedral reflection m ↔ K − m, i.e., m ∈ {1, K − 1} for K ≥ 3).
(b) (Sharp K = 16 Refutation of the Even- K Crossover Conjecture) Let K ≥ 2 be
even and R0 ∈ (1, 3) be the unique root of pK(R) = 0 in (5), where |Ie0 (R0)| = |Isa(R0)| =
E(1 − 4η(R0)). With y := RK
0 ,
ucrit(R0) := 2y(y − 1)(R2
0 − 1)2
(R2
0 − 1)(R2
0 + y2)(y + 1) − 4R2
0y(y − 1), (9)
satisfies |Is2 (R0)| > |Ie0 (R0)| if and only if ucrit(R0) > 1−cos(2π/K). This condition fails
for al l even K ∈ {2, 4, 6, 8, 10, 12, 14} (exact tie at K = 2 ; ratio ucrit/(1 − cos(2π/K)) ≈
0.9564 < 1 at K = 14 ) and holds strictly for every even K ≥ 16 (ratio ≈ 1.0096 > 1 at
K = 16 ). Thus [ 1, Eq. (16)] is strictly greater than the true phase-invariant bound (4)
near R0 for al l even K ≥ 16.
(c) (Universal O(1/K) Minimax Distance Ceiling) F or every K ≥ 2 and every R > 1,
d2
min(R) ≤ min
 
d2
e0 (R), d 2
s2 (R)

< 7E
K , (10)
with sharp asymptotic ceiling
lim
K→∞
K sup
R>1
min
 
d2
e0 (R), d2
s2 (R)

= C∗E := 4π2x∗ tanh(x∗)
x2∗ + π2 E ≈ 6.26130E < 2πE,
where x∗ ≈ 3.20820 > π is the unique positive root of (x2 − π2) sinh(2x) = 2 x(x2 + π2)
(strictly exceeding the crossing value 2π tanh(π)E ≈ 6.25976E).
Proof. Part (a). F ors = e0 −em, Ps(z) = (z−R)(z−R−1w)
(z−R−1)(z−Rw) has simple poles at zin = R−1 (inside
|z| = 1 ) and zout = Rw (outside |z| = 1 ), with residues
α := Res z=R−1 Ps(z) = −(R2 − 1)(w − 1)
R(R2w − 1) , β := Res z=Rw Ps(z) = R(R2 − 1)w(w − 1)
R2w − 1 .
Splitting ( 6) via AH(z) = E(1 − ηzK − ηz−K): (i) inside |z| < 1, Ps(z)/z has poles at 0
(residue Ps(0) = 1 ) and R−1 (residue Rα), giving 1 + Rα = ( R2 + w − 2)/(R2w − 1); (ii)
zK−1Ps(z) is analytic at 0 and has a single interior pole at R−1, contributing −ηR1−Kα =
ηR−K(R2 − 1)(w − 1)/(R2w − 1); (iii) z−K−1Ps(z) = O(z−K−1) as z → ∞ has zero residue
at ∞, so deforming |z| = 1 outward picks up −Resz=Rw
 
−ηz−K−1Ps(z)

= η(Rw)−K−1β =
ηR−K(R2 − 1)(w − 1)/(R2w − 1) since wK = 1 . Since ηR−K = ( X + 1)−1, summing the three
pieces gives ( 7).
W ritingw = c+ is (s2 = 1 −c2), the numerator of (7) is (X + 1)(R2 −1) + ((X + 1) + 2(R2 −
1))(c+is−1) (equivalently A+Bw), whose squared modulus expands via (X+1)(R2−1) = A+B
and w + w−1 = 2 c to (X + 1)2(R2 −1)2 −2AB(1 −c), while |R2w −1|2 = ( R2 −1)2 + 2R2(1 −c).
Subtracting from 1 uses AB+(X+1)2R2 = 2( R2−1)(R2+X)(X−1) > 0 (verified constructively
in Lean 4, thm02), giving ( 8). Since (1 − c)/((R2 − 1)2 + 2 R2(1 − c)) is strictly increasing in
1 − c > 0, |Ie0−em(R)| is strictly maximized at m = 1 (thm03).
Part (b). At R0 > 1, Ie0 (R0) = E(1−4y/(y2+1)), so 1−Ie0 (R0)2/E2 = 8 y(y−1)2/(X+1)2.
Equating the second equality in (8) with 1−Ie0 (R0)2/E2 cancels (X +1)2 and 4(y −1), yielding
the exact threshold ucrit(R0) in (9). F or K = 2 , p2(R) = ( R+ 1)2(R2 −3R+ 1) gives ucrit(R0) =
2 = 1 − cos π (since s2 = sa). F or K ∈ { 4, 6, 8, 10, 12, 14} and K ∈ { 16, 18, . . . , 32}, exact
rational enclosures of R0 and cos(2π/K) (Certificates C02–C03; Lean 4 thm04 for K = 14 , 16)
establish failure for K ≤ 14 and strict exceedance for 16 ≤ K ≤ 32. F or all even K ≥ 34: since
4

--- Page 5 ---
(1 + c/K)K−1 < e c/(1 + c/K) with c = 3 .7 and cec < 4(34 + c), we have pK(1 + c/K) < 0
and hence R0 > 1 + 3 .7/K and y = RK
0 > (1 + 3 .7/34)34 > 33. Meanwhile 1.1525(0.15) > 4
implies pK(1.15) > 0, so R0 < 1.15. Substituting R0 − 1 = 4 R0y/(y2 − R0) into ( 9) gives
ucrit(R0) = ( R0 + 1)2(R0 − 1)2/(2Dratio) with
Dratio := R0

1 + ( R0 + 1)
(y2 + R2
0)(y + 1)
(y2 − R0)(y − 1) − 1

< 1.32,
yielding K2ucrit(R0) > 4 · 3.72/(2 · 1.32) > 20.7 > 2π2 > K 2(1 − cos(2π/K)) (Certificate C04).
Part (c). If 1 < R ≤ 1 + π/K, then
d2
e0 (R)
E = 2 (R − 1)(RK−1 − R−K)
RK + R−K < 2R − 1
R ≤ 2π
K + π < 2π
K < 7
K .
If R ≥ 1 + π/K, AM–GM gives (R2 − 1)2 + 2R2u1 ≥ 2√2u1 R(R2 − 1) (Lean 4 thm05), where
u1 := 1 − cos(2π/K) and √2u1 = 2 sin( π/K) < 2π/K. Using (X − 1)/(X + 1) < 1 and
(R2 + X)/(R(X + 1)) < R−1 + R−(2K−1), we obtain 1 − |Is2 (R)|2/E2 < δK, where
δK := 2π
K
 K
K + π +

1 + π
K
−(2K−1)
.
F orK = 2 , 3, the trivial bound d2
min ≤ 2E < 7E/K holds; for K = 4 , Certificate C05 checks
2δ4/(1+ √1 − δ4) < 7/4 directly . F or every integerK ≥ 5, binomial expansion (1+ π/K)2K−1 >
1+ 9
5 π+ 36
25 π2 + 84
125 π3 > 40 yields (1+ π/K)−(2K−1) < 1
40 and δK < 2π
5+π + 2π
200 < 0.81 < 1. Hence
d2
s2 (R)/E ≤ 2δK/(1 + √1 − δK) = 2(1 − √1 − δK) < 7/K holds iff δK < 7
K − 49
4K2 ; clearing
4K2(K+π) > 0 against 2π
K
  K
K+π + 1
40

reduces this to (28−41
5 π)K2 +(28π−π2
5 −49)K−49π > 0,
which holds for all K ≥ 5 since both leading coeﬀicients are positive and the value at K = 5
exceeds 86 (Certificate C05).
Finally , write R = ex/K (x > 0) and define f1(x) := 2 x tanh x and f2(x) := 4π2x tanh x
x2+π2 . On
(0, π], f1(x) ≤ f2(x) with equality at x = π, where f′
2(π) = 2 π sech2(π) > 0; thus min(f1, f2)
increases past x = π and attains its unique global maximum on (0, ∞) at the unique root x∗ > π
of f′
2(x) = 0 , i.e. (x2 − π2) sinh(2x) = 2 x(x2 + π2), with x∗ ∈ (3.208, 3.209) and C∗ = f2(x∗) ∈
(6.261, 6.262) (Certificate C05). F or the asymptotic limit, evaluating at RK = ex∗/K gives
lim infK→∞ K supR>1 min(d2
e0 , d2
s2 )/E ≥ min(f1(x∗), f2(x∗)) = C∗. Conversely , for x ∈ (0, 2],
Kd2
e0 (ex/K)/E < 2K(1−e−x/K) ≤ 2x ≤ 4 < C∗; for all x ≥ 13 and K ≥ 2, using 1+ |Is2 |/E ≥ 1,
(X − 1)/(X + 1) < 1, (R2 + X)/(X + 1) < 1 + e−13, u1 ≤ 2π2/K2, and R2 − 1 ≥ 2x/K in (8)
yields Kd2
s2 (ex/K)/E < 8π2(1+e−13)
13 < 6.074 < C∗ (Certificate C05); and on the compact interval
[2, 13], Kd2
e0 (ex/K)/E → f1(x) and Kd2
s2 (ex/K)/E → f2(x) uniformly as K → ∞ , giving
lim supK→∞ K supR>1 min(d2
e0 , d2
s2 )/E ≤ maxx∈[2,13] min(f1(x), f2(x)) = C∗.
3 Universal Uniform-Sign Collapse and General Residue F or-
mula
A striking consequence of replacing the Parseval DFT sum [ 1, Eq. (13)] with residue calculus is
that all 2K uniform-sign flip patterns depend solely on their Hamming weight.
Theorem 3.1 (Uniform-Sign Collapse, General Residue F ormula, and Tightened Distance
Counts). Let K ≥ 2, R > 1, and E > 0.
(a) (Universal Hamming-W eight Col lapse) F or every uniform-sign pattern s ∈ {0, 1}K
or s ∈ {0, −1}K of Hamming weight w := ∥s∥1 ∈ {0, 1, . . . , K },
Is(R) = E RK−w + R−(K−w)
RK + R−K , (11)
5

--- Page 6 ---
Figure 1: (a) Sharp K = 16 phase transition of ucrit(R0)/(1 − cos(2π/K)) across even K ∈
{2, . . . , 28}, showing K = 2 exact tie, K = 4 , . . . , 14 sub-threshold failure ( K = 14 : 0.9564),
and K ≥ 16 exceedance ( K = 16 : 1.0096). (b) Normalized minimax distance ceiling K ·
supR>1 min(d2
e0 , d2
s2 )/E converging to C∗ = f2(x∗) ≈ 6.2613 < 2π, with inset showing the scaled
asymptotic profiles f1(x), f2(x) versus x = K log R peaking at x∗ ≈ 3.208 (strictly above x = π).
purely real and completely independent of the support of s. Consequently, Is(R) is strictly
decreasing in w for al l R > 1, and al l 2(2K − 1) nonzero uniform-sign patterns col lapse
onto K distinct rational curves.
(b) (General Cauchy-Residue F ormula) F or arbitrary s ∈ {−1, 0, 1}K with S± := {k ∈
[K] : sk = ±1} and w± := |S±|, let αm := Res z=R−1ϕm Ps(z) (m ∈ S+) and βn :=
Resz=Rϕn Ps(z) (n ∈ S−). Then
Is(R) = E
2
4Rw+−w− + R2K
R2K + 1
X
m∈S+
Rϕ−mαm + 1
R2K + 1
X
n∈S−
R−1ϕ−nβn
3
5. (12)
(c) (Non-Dihedral Col lisions and Distinct-Distance Bound) Let OK be the number of
nonzero DK ×Z2 orbits in {−1, 0, 1}K \{0} and UK be the number of uniform-sign orbits.
Then the number of distinct nonzero distances in H is at most OK −UK +K. Moreover, at
K = 4 the non-dihedral orbits (−1, −1, 0, 0) and (−1, 0, −1, 0) col lide identical ly (w = 2 ),
and at K = 6 the mixed-sign pattern (−1, 0, 0, 0, −1, 1) col lides identical ly with the weight-
5 uniform pattern (−1, −1, −1, −1, −1, 0), yielding I(R) = ER5(R2 + 1) /(R12 + 1) and
tightening the K = 6 count to 44 < 45 < 51 < 364 = (3 6 − 1)/2.
Proof. Part (a). Suppose s ∈ { 0, 1}K with support S := S+, |S| = w. Using AH(z) =
−Eηz−K QK−1
k=0 (z − Rϕk)(z − R−1ϕk) and Bk(z) = R−1(z − Rϕk)/(z − R−1ϕk), the integrand
numerator cancels all (z − R−1ϕk) poles on S, leaving
AH(z)Ps(z) = −Eηz−KR−w(zK − RK) QS(z), Q S(z) :=
Y
k∈S
(z − Rϕk)
Y
k /∈S
(z − R−1ϕk).
Since QS(z) = zK +PK−1
j=1 qjzj +q0 is monic of degree K, the coeﬀicient of zK in (zK −RK)QS(z)
is q0 − RK, independent of q1, . . . , qK−1. Because QK−1
k=0 ϕk = ( −1)K−1, we have q0 = QS(0) =
(−1)K(−1)K−1Rw−(K−w) = −R2w−K, so extracting the constant term yields
Is(R) = −EηR−w(−R2w−K − RK) = Eη(Rw−K + RK−w) = E RK−w + R−(K−w)
RK + R−K .
6

--- Page 7 ---
F ors ∈ {0, −1}K, Hermitian symmetry I−s(R) = Is(R)∗ and reality of ( 11) give the identical
expression. Strict monotonicity in w follows because f(t) = Rt + R−t is strictly increasing for
t ≥ 0 (verified for K = 4 in Lean 4, thm06–thm07).
Part (b). F or general s, Ps(z) has Ps(0) = Rw+−w−, interior simple poles {R−1ϕm : m ∈
S+}, and exterior simple poles {Rϕn : n ∈ S−}. Splitting AH(z) = E(1 − ηzK − ηz−K) and
evaluating the first two terms via interior residues and the third via exterior residues (using
z−K−1Ps(z) = O(z−K−1) at ∞ and ϕK = 1 ) yields ( 12), noting 1 − ηR−K = R2K/(R2K + 1)
and ηR−K = ( R2K + 1)−1.
Part (c). Replacing all UK uniform-sign orbits by the K distinct Hamming-weight curves
w ∈ {1, . . . , K } gives at most OK − UK + K distinct distances (e.g. 40 → 12 → 11 at K = 4 ;
121 → 21 → 19 at K = 5 ; 364 → 51 → 45 at K = 6 , Lean 4 thm09). Clearing denominators via
−R12+1
E z6AH(z)Ps(z) = R6 Q5
k=0(z − Rϕk)(z − R−1ϕk)Ps(z) produces a polynomial of degree
at most 12 in R whose z6 coeﬀicient is −R12+1
E Is(R). Explicit expansion in Z[ω6] (ω2
6 = ω6 − 1)
confirms that (−1, 0, 0, 0, −1, 1) and (−1, −1, −1, −1, −1, 0) share the identical z6 coeﬀicient
−R5(R2 + 1) (verified in Lean 4 thm08 at R = 2 , 3, and proved identically as a polynomial in
R by 13-point exact interpolation in Certificate C07), reducing the K = 6 exact distinct count
to 44.
4 Odd- K Arithmetic Dichotomy and Cyclotomic Galois Bound
While Huggins et al. [1, Prop. 5] proved d2
min(R) → 8Eη = Θ( R−K) for even K via the alternat-
ing pattern sa, the odd- K large-R behavior was left open [ 1, Sec. V]. W e resolve it completely
across all K ≥ 2.
F or any balanced ternary pattern s ∈ {− 1, 0, 1}K \ { 0} (PK−1
k=0 sk = 0 ), let bs(m) :=PK−1
k=0 skϕkm (m ∈ [K]) be its DFT and define m0(s) := min {m ≥ 1 : bs(m) ̸= 0 }.
Theorem 4.1 (Cyclotomic Galois V anishing-DFT Bound and Odd-K Decay Dichotomy). Let
K ≥ 2 and let pmin(K) denote the smal lest prime divisor of K.
(a) (Cyclotomic Galois Bound) F or every nonzero balanced patterns ∈ {−1, 0, 1}K \ {0},
m0(s) ≤ K
pmin(K), (13)
with equality m0(s) = K/pmin(K) attained if and only if s is periodic with minimal period
pmin(K) (i.e. sk+pmin(K) = sk for al l k mod K).
(b) (Large-R Decay Dichotomy) As R → ∞, every balanced pattern satisfies
|Is(R)|
E = 1 − |bs(m0(s))|2
m0(s)2 R−2m0(s) + O
 
R−(2m0(s)+1)
. (14)
Consequently, for every odd K ≥ 3:
• If K is composite (so pmin(K) ≤ K/3), d2
min(R) = Θ K
 
R−2K/pmin(K)
(e.g. at K = 9 ,
(1, −1, 0)3 achieves m0 = 3 , |bs(3)|2 = 27 , and d2(R) = 6 ER−6 + O(R−7)).
• If K = p ≥ 3 is an odd prime, every nonzero balanced pattern has m0(s) = 1 , forcing
d2
min(R) = Θ p(R−2) with exact coeﬀicient 2E mins |bs(1)|2: at p = 3 , min |bs(1)|2 = 3 ;
at p = 5 , the twin-dipole (−1, 0, 1, −1, 1) achieves min |bs(1)|2 = 5 − 2
√
5 ≈ 0.5279;
and for every odd prime p ≥ 5, the twin-dipole e0 − e1 + e(p−1)/2 − e(p+1)/2 achieves
fourth-order prime suppression
|bs(1)|2 = 16 sin 2
π
p

sin2
 π
2p

< 4π4
p4 .
7

--- Page 8 ---
Proof. Part (a). Associate to s the integer polynomial S(X) := PK−1
k=0 skXk ∈ Z[X], so
bs(m) = S(ϕm). F or any m ∈ { 1, . . . , K − 1}, write g := gcd( m, K), m = gr, K = gq with
q ≥ 2 and gcd(r, q) = 1 . Since ϕg is a primitive q-th root of unity , its minimal polynomial
over Q is the q-th cyclotomic polynomial Φq(X), which is irreducible over Q [11, Ch. 13.6].
Because ϕm = ( ϕg)r is a Galois conjugate of ϕg in Gal(Q(ϕg)/Q) ∼= (Z/qZ)×, we obtain the
exact equivalence
bs(m) = 0 ⇐⇒ Φq(X) | S(X) ⇐⇒ S(ϕg) = bs(gcd(m, K)) = 0 .
F or every1 ≤ m < K , q = K/ gcd(m, K) > 1 divides K, hence q ≥ pmin(K) and gcd(m, K) ≤
K/pmin(K) (Lean 4 thm11). If m0(s) > K/p min(K), then bs(gcd(m, K)) = 0 for all 1 ≤ m < K ,
so bs(m) = 0 for all m ∈ [K] (as bs(0) = 0 ), forcing s = 0 by inverse DFT, a contradiction. Thus
m0(s) ≤ K/pmin(K).
When equality holds, d := K/pmin(K) = m0(s). If d ∤ m (1 ≤ m < K ), then gcd(m, K) ≤ d
and gcd(m, K) ̸= d, so gcd(m, K) < m 0(s), forcing bs(m) = 0 . Hence bs is supported solely on
multiples m = jd (1 ≤ j < p min(K)), and inverse DFT gives
sk+pmin(K) = 1
K
pmin(K)−1X
j=1
bs(jd)ϕ−jd(k+pmin(K)) = sk
since ϕd pmin(K) = ϕK = 1 . Because bs(d) ̸= 0 and pmin(K) is prime, pmin(K) is the minimal
period. Conversely , any balanced nonzero pattern of period pmin(K) has bs(m) = 0 whenever
d ∤ m, forcing m0(s) = d.
Part (b). On |z| = 1 , Bk(z) = −ϕkz−1(1 − R−1ϕ−kz)/(1 − R−1ϕkz−1). T aking logarithms
for large R, summing with weights sk (noting PK−1
k=0 sk = 0 cancels the prefactor z− ∑sk = 1 ),
and using bs(−m) = bs(m)∗,
Ps(z) = eiϑ0 exp
0
@ X
m≥m0
R−m
m
 bs(m)z−m −bs(m)∗zm
1
A, ϑ 0 ∈ R.
Expanding to order R−2m0 and extracting the z0 Laurent term in (6) proves (14); crucially , nei-
ther m = K nor −ηz±K disturbs the R−2m0 coeﬀicient even when K is even and 2m0 = K, be-
cause bs(K) = bs(0) = 0 vanishes by balance and [z∓K]Ps(z) = O(R−K) implies −η[z∓K]Ps(z) =
O(R−2K). F or any unbalanced pattern ( w+ − w− = PK−1
k=0 sk ̸= 0 ), Ps(z) = eiϑ0 z−(w+−w−) +
O(R−1) and AH(z) = E + O(R−K) uniformly on |z| = 1 while 1
2πi
H
|z|=1 z−(w+−w−) dz
z = 0 , so
|Is(R)| = O(R−1) → 0 and d2
s(R) → 2E; unbalanced patterns are therefore strictly excluded
from d2
min(R) = O(R−2) for all suﬀiciently large R. F or composite odd K, period- pmin(K) bal-
anced patterns exist because pmin(K) ≥ 3 allows (1, −1, 0, . . . , 0) repeated K/pmin(K) times;
at K = 9 , (1, −1, 0)3 satisfies bs(0) = bs(1) = bs(2) = 0 and |bs(3)|2 = 27 (Lean 4 thm14).
F or odd primes K = p ≥ 3, gcd(m, p) = 1 forces m0(s) = 1 (thm12), and the twin-dipole
stwin = e0 −e1 +e(p−1)/2 −e(p+1)/2 has bstwin(1) = (1 −ϕ)(1 + ϕ(p−1)/2) = (1 −e2πi/p)(1 −e−πi/p),
giving |bstwin(1)|2 = 16 sin 2(π/p) sin2(π/(2p)) < 4π4/p4 (Lean 4 thm13, thm15; Certificates C09–
C11).
5 Exact Global Minimax Radii ( K = 2, 3, 4) and Phase Separa-
tion
Huggins et al. [ 1, F ootnote 1] noted that p2(R) = 0 and p4(R) = 0 are solved by R0 = φ2
and R0 = ρ2 (golden and plastic ratios squared, paralleling Gonchar polynomials [ 12]), and
conjectured global minimax optimality of R0 for even K ≤ 14. Using our exact residue formulas
8

--- Page 9 ---
Figure 2: (a) Universal uniform-sign collapse for K = 4 , showing all 15 nonzero uniform-sign
patterns collapsing onto w ∈ { 1, 2, 3, 4} (with exact DFT checks confirming the non-dihedral
collision (−1, −1, 0, 0) ≡ (−1, 0, −1, 0)); inset compares (3K − 1)/2, DK × Z2 orbits, and exact
distinct distance counts for K = 3 , . . . , 6. (b) Odd- K large-R decay dichotomy: odd primes
K = 3 , 5, 7 obey Θ(R−2) with O(p−4) twin-dipole suppression, while composite K = 9 achieves
Θ(R−6) via the period-3 pattern (1, −1, 0)3.
across al l DK × Z2 orbits, we prove unconditional global minimax optimality for K = 2 , 3, 4
(including the first odd- K exact minimax radius at K = 3 ) and explain the separation between
unphased and phase-invariant metrics.
Theorem 5.1 (Global Minimax Optimality for K = 2 , 3, 4 and Phase Separation) . Let E > 0
and let d2
min(R) be the phase-invariant bound (4).
(a) (K = 2 Global Minimax) Across al l 3 nonzero D2 × Z2 orbits, d2
min(R) is uniquely
maximized global ly at R∗ = φ2 = (3 +
√
5)/2 with exact rational optimum
|Ie0 (φ2)| = |Isa(φ2)| = 3E
7 , d 2
min(φ2) = 8E
7 .
(b) (K = 3 Global Minimax) Across al l 5 nonzero D3 × Z2 orbits, d2
min(R) is uniquely
maximized global ly at the unique real root R∗ > 1 of R8 − 5R6 + R4 − 5R2 + 1 = 0 , given
explicitly by R2
∗ + R−2
∗ = (5 +
√
29)/2, i.e.,
R∗ =
s
5 +
√
29 +
p
38 + 10
√
29
4 ≈ 2.234339,
where |Ie0 (R∗)|2 = |Ie0−e1 (R∗)|2 = 37+6
√
29
325 E2 and d2
min(R∗) = 2 E
 
1 −
√
481+78
√
29
65

≈
1.076388E.
(c) (K = 4 Global Minimax) Across al l 12 nonzero D4 × Z2 orbits, d2
min(R) is uniquely
maximized global ly at R∗ = R0 = ρ2 ≈ 1.754878 (the unique positive root of R3 − 2R2 +
R − 1 = 0 , where ρ3 = ρ + 1 ), with |Ie0 (R0)| = |Isa(R0)| ≈ 0.582871E and d2
min(R0) ≈
0.834259E.
(d) (Real vs. Complex Inner Products and Metric Separation) If s is uniform-sign
or palindromic under some reflection σ ∈ DK (σs = s), then Im Is(R) = 0 identical ly. By
contrast, anti-palindromic patterns ( σs = −s) can sustain Im Is(R) ̸= 0 : for K = 4 and
s = ( −1, 0, 0, 1),
I(−1,0,0,1)(R) = E 2R4 − i(R2 − 1)2(R4 − 1)
R8 + 1 ,
9

--- Page 10 ---
so as R → ∞ the phase-invariant distance vanishes (O(R−2)) while the unphased Euclidean
distance 2E − 2 Re Is(R) → 2E (already exceeding 7.96× separation at R = 4 ). Similarly,
for K = 3 under a fixed global phase, Re Ie0−e1 (R) → − E/2 < 0 gives d2 → 3E while
d2
min(R) → 0.
Proof. Part (a). The 3 orbits for K = 2 are e0, sa = (1 , −1), and 12 = (1 , 1), with Ie0 =
E R(R2+1)
R4+1 , Isa = −E R4−4R2+1
R4+1 , and I12 = E 2R2
R4+1 < I e0 (R) for all R > 1. Direct polynomial
factorization (Lean 4 thm16) gives
7R(R2 + 1) − 3(R4 + 1) = −(R2 − 3R + 1)(3R2 + 2R + 3),
7(R4 − 4R2 + 1) − 3(R4 + 1) = 4( R2 − 3R + 1)(R2 + 3R + 1),
proving max(|Ie0 (R)|, |Isa(R)|) ≥ 3E/7 for all R > 1 with unique equality at R2 − 3R + 1 = 0 ,
i.e. R∗ = φ2.
Part (b). Setting u := R2 > 1, the 5 orbits of K = 3 have exact squared moduli
Nj(u)E2/(u3 + 1)2:
N1 = u(u2 + 1)2 (e0), N 2 = u6 − 6u5 + 12u4 − 10u3 + 12u2 − 6u + 1 ( e0 − e1),
N3 = 4 u(u2 − 3u + 1) 2 for (−1, −1, 1), N4 = u2(u + 1) 2 for (−1, −1, 0), and N5 = 4 u3 for
(−1, −1, −1). Notice N1(u) − N2(u) = −(u − 1)2(u4 − 5u3 + u2 − 5u + 1), whose unique root
u∗ > 1 satisfies u∗ + u−1
∗ = (5 +
√
29)/2 (u∗ ≈ 4.9923). Since |Ie0 |2/E2 = v2/((v + 2)(v − 1)2)
with v = u∗+u−1
∗ , substituting v2 = 5 v+1 verifies 325y2 −74y+1 = 0 with y = (37+6
√
29)/325
(Lean 4 thm17). Setting u = 1 + t (t > 0) gives N1 − N4 = t2(t3 + 4t2 + 6t + 3) > 0, N1 − N5 =
t2(t3 + 5t2 + 8t+ 4) > 0, and N1 −N3 = 3 u(u−1)2(−u2 + 6u−1) > 0 on u ∈ (1, 3 + 2
√
2). Since
5 < 3+2
√
2, this gives N1 > N3, N4, N5 on (1, 5], covering (1, u∗] directly and (u∗, 5] via N2 > N1
on (u∗, 5]; setting u = 5 + s (s ≥ 0) covers [5, ∞) via positive-coeﬀicient polynomials N2 − Nj
in s (positivity of the shifted polynomials is verified in Lean 4 thm18, while exact polynomial
difference identities across all orbits are verified in Certificate C13). F or the normalized squared-
modulus ratios gj(u) := Nj(u)/(u3 + 1)2 = |Isj (√u)|2/E2, exact differentiation yields
g′
1(u) = −(u − 1)(u2 + 1)(u4 + u3 + 6u2 + u + 1)
(u3 + 1)3 < 0 ( ∀u > 1),
and g′
2(u) = 6( u−1)(u6−3u5+3u4−10u3+3u2−3u+1)/(u3+1)3, where shifting u = 4+ s (s ≥ 0,
covering [4, ∞) ⊃ [u∗, ∞) since u∗ ≈ 4.9923) turns the sextic factor into s6 + 21 s5 + 183 s4 +
838s3 + 2091s2 + 2613s + 1189 > 0 (Certificate C13). Hence g1 is strictly decreasing on (1, ∞)
and g2 is strictly increasing on [u∗, ∞): for 1 < u < u ∗, maxs |Is(√u)|2/E2 ≥ g1(u) > g 1(u∗),
and for u > u ∗, maxs |Is(√u)|2/E2 ≥ g2(u) > g2(u∗) = g1(u∗), proving R∗ = √u∗ is the unique
global maximizer.
Part (c). The polynomial p4(R) factors as (R + 1)2(R3 − 2R2 + R − 1)(R3 − R2 + 2R − 1)
(Lean 4 thm19), so R0 = ρ2 satisfies u0 = R2
0 ∈ (3, 3.1). Expressing all 11 squared-modulus
numerators Mj(u) of the 12 D4 ×Z2 orbits (listed explicitly in T able1; recall (−1, −1, 0, 0) and
(−1, 0, −1, 0) collapse by Theorem 3.1), exact Möbius transformation u = (1+ 31
10 t)/(1+ t) yields
nonnegative coeﬀicients with strictly positive higher-degree terms ( t0 = t1 = 0 from the double
root at u = 1 and t2, . . . , t8 > 0) for (1 + t)8(Me0 (u) − Mj(u)) on u ∈ (1, 3.1], while shifting
u = 3+ s (s ≥ 0) yields nonnegative coeﬀicients with strictly positive constant term s0 > 0 (and
s8 = 0 when leading u8 terms cancel) for Msa(3 + s) − Mj(3 + s) across every non-dominant
orbit (Lean 4 thm19 certifies the p4 factorization and shifted positivity for 100m and 110m, while
Certificate C14 verifies all 11 orbit polynomials and Möbius/shifted coeﬀicients).
Part (d). Reflection f ∈ DK conjugates the zeros and hence coeﬀicients, giving Ifs(R) =
Is(R)∗. Thus σs = s implies Is(R) = Is(R)∗ ∈ R. By contrast, σs = −s gives Iσs = I−s = I∗
s
with no reality constraint. Applying (12) at K = 4 , s = ( −1, 0, 0, 1) yields Im Is(R)/E = −(R2−
1)2(R4 − 1)/(R8 + 1) < 0 (Lean 4 thm10, thm20; Certificate C15), while ( 7) at K = 3 , m = 1
gives Re Ie0−e1 (R) → E cos(2π/3) = −E/2 as R → ∞.
10

--- Page 11 ---
Figure 3: (a) Unconditional global phase-invariant d2
min(R)/E across all DK × Z2 orbits for
K = 2 , 3, 4, peaking at R∗ = φ2 (d2
min = 8 /7), R∗ ≈ 2.234 (d2
min ≈ 1.076), and R0 = ρ2 ≈
1.755 (d2
min ≈ 0.834). (b) Separation between unphased 2(1 − Re Is)/E and phase-invariant
2(1 − |Is|)/E on anti-palindromic (−1, 0, 0, 1) (> 7.96× gap at R = 4 ) versus palindromic
(−1, 0, 1, 0) (Im I = 0 ).
T able 1:Explicit squared-modulus numerator polynomials Mj(u) (|Is(√u)|2/E2 = Mj(u)/(u4 +
1)2, u = R2) across all 12 nonzero D4 × Z2 orbits at K = 4 (Theorem 5.1(c), Certificate C14).
Orbit Representative Type Numerator Polynomial Mj(u)
(−1, 0, 0, 0) (e0) Uniform (w = 1, small-R dom.) u7 + 2u4 + u
(−1, 1, −1, 1) (sa) Alternating (large-R dom.) u8 − 8u6 + 18u4 − 8u2 + 1
(−1, −1, −1, −1) Uniform (w = 4) 4u4
(−1, −1, −1, 0) Uniform (w = 3) u5 + 2u4 + u3
(−1, −1, −1, 1) Balanced-asym. mixed 9u6 − 48u5 + 82u4 − 48u3 + 9u2
(−1, −1, 0, 0) ≡ (−1, 0, −1, 0) Uniform (w = 2, 2 orbits) u6 + 2u4 + u2
(−1, −1, 0, 1) Mixed weight-3 5u7 −28u6 +60u5 −70u4 +60u3 −28u2 +5u
(−1, −1, 1, 1) Balanced palindrome u8 −16u7 +96u6 −272u5 +386u4 −272u3 +
96u2 − 16u + 1
(−1, 0, −1, 1) Non-uniform weight-3 u7 − 4u6 + 10u4 − 4u2 + u
(−1, 0, 0, 1) Anti-palindromic (Im I ̸= 0) u8−4u7+4u6+4u5−6u4+4u3+4u2−4u+1
(−1, 0, 1, 0) Non-adjacent dipole u8 − 8u7 + 24u6 − 40u5 + 50u4 − 40u3 +
24u2 − 8u + 1
6 V erification, F ormalization Scope, and Artifact Integrity
All algebraic identities, integer-cleared brackets, cyclotomic ring norms, and shifted dominance
certificates are independently verified in two layers, summarized in T able 2, and archived pub-
licly at https://github.com/lluiseriksson/paper148-huffman-distance-barriers (tag
v1.0.1).
Honest F ormalization Scope. The Lean 4 module lean/HuffmanDistanceBarriers.lean
uses pure Lean 4.36.0 core with no external imports, no sorry, grind, native_decide, or
Classical.choice, and zero compiler warnings ( -DwarningAsError=true). The Python veri-
fier verification/verify_huffman_distances.py passes a built-in AST self-audit with zero
floating-point literals, calls, or math libraries, operating solely in exact Q (Fraction) and
cyclotomic fields Q[X]/(ΦK(X)), emitting 16 deterministic certificates ( MANIFEST SHA-256 :
5d22c0012d4cc4d2314a12eb722bb82b97ea44f7eb7e2ebd4a0ac8544a0beff8) and passing all
11

--- Page 12 ---
T able 2: Correspondence between manuscript theorems, Lean 4.36.0 proofs ( lean/ module),
and zero-float SHA-256 certificates ( verification/ module).
Result Lean 4 Theorems Certificates Scope Machine-Checked
Theorem 2.1 thm01–thm05 C01–C05 A + B, AB positivity ,K = 14 /16 brackets,
K ∈ [2, 32] & K ≥ 34
Theorem 3.1 thm06–thm10 C06–C08 K = 4 collapse, coeff. collapse, K = 6 Z[ω6]
collision, counts
Theorem 4.1 thm11–thm15 C09–C11 gcd(m, K)pmin ≤ K, prime m0 = 1 , K =
3, 5, 7, 9 Z[ωK] norms
Theorem 5.1 thm16–thm20 C12–C16 K = 2 , 3, 4 dominance polynomials, R = 2 , 4
metric separation
69 checks in tests/test_adversarial.py. The analytic Cauchy contour integrals on |z| = 1 ,
irreducibility of Φq(X) over Q, and the K → ∞ limiting profile C∗ = f2(x∗) are established by
classical proofs in Sections 2–5, while all finite algebraic, rational, cyclotomic, and polynomial
dominance steps are machine-checked.
7 Conclusion
By replacing finite-point DFT summation with exact unit-circle residue calculus and cyclotomic
Galois theory , we have resolved the open structural questions raised by Huggins, Şahin, and
Erkip [ 1]: (i) precisely locating the K = 16 phase transition where adjacent dipoles break
the even-K crossover conjecture and establishing an unconditional O(1/K) minimax distance
ceiling; (ii) collapsing all 2(2K −1) nonzero uniform-sign flip patterns onto K Hamming-weight
rational curves (or K + 1 curves including w = 0 ); (iii) resolving the odd- K large-R decay
dichotomy between ΘK(R−2K/pmin(K)) for composite K and Θp(R−2) with O(p−4R−2) twin-
dipole suppression for odd primes; and (iv) certifying unconditional global minimax radii for
K = 2 , 3, 4 alongside metric separations induced by complex anti-palindromic correlations.
References
[1] Parker Huggins, Alphan Şahin, and Elza Erkip. On the distance properties of Huffman
sequences. arXiv:2611.34807v1 [cs.IT], November 2026.
[2] David A. Huffman. The generation of impulse-equivalent pulse trains. IEEE T ransactions
on Information Theory , 8(5):10–16, September 1962.
[3] M. Ackroyd. The design of Huffman sequences. IEEE T ransactions on Aerospace and
Electronic Systems, pages 790–796, November 1970. no. 6.
[4] M. Ackroyd. Synthesis of eﬀicient Huffman sequences. IEEE T ransactions on Aerospace
and Electronic Systems, pages 2–8, January 1972. no. 1.
[5] R. Ojeda and E. T acconi. Huffman sequences with uniform time energy distribution.Signal
Processing, 37(1):141–146, May 1994.
[6] D. White, J. Hunt, and L. Dresel. Uniform Huffman sequences do not exist. Bul letin of
the London Mathematical Society , 9(2):193–198, July 1977.
[7] J. Hunt and M. Ackroyd. Some integer Huffman sequences. IEEE T ransactions on Infor-
mation Theory, 26(1):105–107, January 1980.
12

--- Page 13 ---
[8] P . W alk, P . Jung, and B. Hassibi. Short-message communication and FIR system identifi-
cation using Huffman sequences. In Proc. IEEE International Symposium on Information
Theory (ISIT), pages 968–972, June 2017.
[9] P . W alk, P . Jung, and B. Hassibi. MOCZ for blind short-packet communication: Basic
principles. IEEE T ransactions on Wireless Communications, 18(11):5080–5097, November
2019.
[10] P . Huggins and A. Şahin. On the optimal radius and subcarrier mapping for binary modu-
lation on conjugate-reciprocal zeros. In Proc. IEEE Military Communications Conference
(MILCOM), pages 1–6, October 2024.
[11] D. Dummit and R. F oote. Abstract Algebra. John Wiley & Sons, Hoboken, NJ, USA, 3rd
edition, 2004.
[12] J. Brauchart, P . Dragnev, E. Saff, and C. van de W oestijne. A fascinating polynomial
sequence arising from an electrostatics problem on the sphere.Acta Mathematica Hungarica,
137(1–2):10–26, March 2012.
13
