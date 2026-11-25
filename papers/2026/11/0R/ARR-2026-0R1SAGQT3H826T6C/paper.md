# Exact-Q Finite-Setting Steering Gap Laws, Rational Polytope Certificates, and Machine-Checked Two-Copy Superactivation of PVM-Critical Two-Qubit States

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-0R1SAGQT3H826T6C` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/critical-steering-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `3c9cb6c77dbbbd85018b640eeeba818906bdb003195775fddf97992a9e72cd3f`

## Abstract

Einstein-Podolsky-Rosen (EPR) steering of two-qubit states exhibits sharp critical behavior at the projective-measurement (PVM) unsteerability boundary v_c = 1/2 of the Werner family rho_v = v|Psi^-><Psi^-| + (1-v)I/4. Very recently, Zhang and Chen (arXiv:2611.09321, November 2026) proved that every PVM-critical entangled two-qubit state is superactivated by two copies with separable conditional states on Bob's side, while every fixed finite bound m on the number of measurement settings leaves an unsteerable neighborhood around criticality. Here we turn both phenomena into exact, closed-form rational theorems over Q, backed by a zero-dependency Lean 4 formalization and a pure-stdlib zero-floating-point-trust certificate verifier (EPR-STEER-CERT-1.0). First, by combining exact great-circle cell counting (R(m) <= m(m-1) + 2), a spherical-cap centroid rearrangement inequality (||m_r||_2 <= alpha_r(1-alpha_r)), and Cauchy-Schwarz, we prove the universal non-asymptotic finite-setting unsteerability law v_m^* >= 1/2 + 1/(2(m^2 - m + 1)) valid for every m >= 1 and every choice of m projective measurements on S^2, matching the exact v_1^* = 1 at m=1, coming within 1.0% of optimal at m=3 (4/7 vs. 1/sqrt(3)), and establishing the quantitative Omega(m^-2) gap law with zero hidden constants. Second, via squared-rational primal-dual steering polytope certificates across m in {2,3,4,6,7,12,15}, we prove that the rational cuboctahedron (m=6, exact threshold v_6^cub = sqrt(5/18) ~= 0.5270, bracketed over Q by a 24-state LHS model at v=21/40=0.525 and a witness at v=53/100=0.530) strictly outperforms the Platonic icosahedron (exact threshold v_6^ico = (1+sqrt(5))/6 ~= 0.5393, (v_6^ico)^2 = (3+sqrt(5))/18) in exact 6-setting steering threshold. Third, for two copies rho_v^{otimes 2} under partially entangled Bell measurements |psi_j(t)>, we derive exact closed-form partial-transpose eigenvalues lambda_min^PT = (1 - v^2(1+2s))/4 (proving strict conditional separability lambda_min^PT >= 1/16 > 0 at v=1/2 for all s in [0,1]), and construct an unconditional, zero-float exact-Q proof of two-copy superactivation of rho_{1/2}^{otimes 2} (extending strictly below criticality to v = 49999/100000 < 1/2) via a Bell sign-parity identity, a degree-5 sum-of-squares polynomial factorization, and the exact spherical moment E_{S^2}[x^2 y^2 z^2] = 1/105. All 18 foundational theorems are machine-checked in zero-dependency Lean 4 (v4.35.0, 0 sorry, 0 Classical.choice, 0 warnings), validated against 100,000-sample Haar SO(3)xSO(3) Monte Carlo (z = 0.96) and 40 matrix PPT checks (error 1.11e-16), and operationalized in 14 exact-Q certificates rejecting 46/46 live adversarial attacks.

## Full Extracted Text

--- Page 1 ---
Exact-QFinite-Setting Steering Gap Laws, Rational
Polytope Certificates, and Machine-Checked
Two-Copy Superactivation of PVM-Critical
Two-Qubit States
Lluis Eriksson*
November 2026
Abstract
Einstein–Podolsky–Rosen (EPR) steering of two-qubit states exhibits sharp critical behav-
ior at the projective-measurement (PVM) unsteerability boundary vc = 1/2 of the Werner
family ρv = v|Ψ−⟩⟨Ψ−| + (1 −v )I/4. Very recently, Zhang and Chen ( arXiv:2611.09321,
November 2026) proved that every PVM-critical entangled two-qubit state is superacti-
vated by two copies with separable conditional states on Bob’s side, while every fixed
finite bound m on the number of measurement settings leaves an unsteerable neighborhood
around criticality. Here we turn both phenomena into exact, closed-form rational theorems
over Q, backed by a zero-dependency Lean 4 formalization and a pure-stdlib zero-floating-
point-trust certificate verifier ( EPR-STEER-CERT-1.0). First, by combining exact great-circle
cell counting ( R(m) ≤m (m− 1) + 2), a spherical-cap centroid rearrangement inequality
(∥mr∥2 ≤α r(1 −α r)), and Cauchy–Schwarz, we prove the universal non-asymptotic finite-
setting unsteerability law v∗
m ≥ 1
2 + 1
2(m2−m+1) valid forevery m≥ 1 andeverychoice of
m projective measurements on S2—matching the exact v∗
1 = 1 at m = 1, coming within
1.1% of optimal at m = 3 (4/7 vs. 1 /
√
3), and establishing the quantitative Ω( m−2) gap
law with zero hidden constants. Second, via squared-rational primal–dual steering poly-
tope certificates across m∈ {2, 3, 4, 6, 7, 12, 15}, we prove that the rational cuboctahedron
(m = 6, exact threshold vcub
6 =
p
5/18≈ 0.5270, bracketed over Q by a 24-state LHS
model at v = 21/40 = 0.525 and a witness at v = 53/100 = 0.530) strictly outperforms the
Platonic icosahedron (exact threshold vico
6 = (1 +
√
5)/6 ≈ 0.5393, (vico
6 )2 = (3 +
√
5)/18)
in exact 6-setting steering threshold. Third, for two copies ρ⊗2
v under partially entan-
gled Bell measurements |ψj(t)⟩, we derive exact closed-form partial-transpose eigenvalues
λPT
min = (1 −v 2(1 + 2s))/4 (proving strict conditional separability λPT
min ≥ 1/16 > 0 at v = 1/2
for all s∈ [0, 1]), and construct an unconditional, zero-float exact- Q proof of two-copy
superactivation of ρ⊗2
1/2 (extending strictly below criticality to v = 49999/100000 < 1/2) via
a Bell sign-parity identity, a degree-5 sum-of-squares polynomial factorization, and the exact
spherical moment ES2 [x2y2z2] = 1/105. All 18 foundational theorems are machine-checked
in zero-dependency Lean 4 ( v4.35.0, 0 sorry, 0 Classical.choice, 0 warnings), validated
against 100,000-sample Haar SO(3) ×SO (3) Monte Carlo ( z = 0.96) and 40 matrix PPT
checks (error 1.11 × 10−16), and operationalized in 14 exact- Q certificates rejecting 46/46
live adversarial attacks.
1 Introduction
Einstein–Podolsky–Rosen (EPR) steering [ 11, 1, 9] occupies the strict operational hierarchy
between entanglement and Bell nonlocality: a bipartite state ρAB is unsteerable from Alice
* Independent researcher (Sweden). Prepared with AI assistance (Google Antigravity). Code, zero-dependency
Lean 4 formalization, and exact-Qcertificates (MIT license):
https://github.com/lluiseriksson/critical-steering-certificates.
1

--- Page 2 ---
to Bob under a measurement set {Ma|x} if Bob’s unnormalized conditional states σa|x =
TrA((Ma|x ⊗I )ρAB) admit a local hidden state (LHS) decomposition σa|x = P
λ pλD(a|x, λ)ρλ.
For the canonical two-qubit Werner family [10]
ρv =v|Ψ −⟩⟨Ψ−|+ (1−v) I4
4 = 1
4
 
I⊗I−v
3X
k=1
σk ⊗σ k
!
, v∈[0,1],(1)
entanglement begins at v >1/3, whereas continuous projective-measurement (PVM) steering
begins precisely at the critical thresholdv c = 1/2 [11].
Two remarkable features of steering criticality have crystallized over the past decade and
culminated in the November 2026 breakthrough of Zhang and Chen [12] (arXiv:2611.09321):
1. Superactivation of PVM-critical states:Building on Quintino, Brunner, and Huber [ 7]
and Palazuelos [5], Zhang and Chen [12] proved thateveryPVM-critical entangled two-qubit
state becomes steerable with two copies ρ⊗2 using joint measurements whose conditional
states on Bob’s two qubits remain completely separable.
2. Finite-setting unsteerable gap:Simultaneously, Zhang and Chen [12] proved qualitatively
that restricting Alice to any fixed finite number m of measurement settings always leaves an
unsteerable neighborhood around the critical boundary.
Despite this structural clarity, three quantitative and certification gaps remain open:
 Non-asymptotic universal finite-m gap law:Can one prove a closed-form, zero-constant
rational lower bound v∗
m ≥ 1
2 + ∆univ(m) valid forevery m≥ 1 andeveryconfiguration of m
projective measurements onS 2?
 Exact-Q primal–dual polytope thresholds:Previous finite- m steering benchmarks [8,
4, 1] rely on floating-point semidefinite programming (SDP) solvers. Can both upper bounds
(linear steering witnesses) and lower bounds (explicit finite LHS ensembles) be certified
strictly overQwith zero floating-point trust?
 Unconditional machine-checked two-copy superactivation:Can two-copy superac-
tivation of ρ⊗2
1/2 (and even strictly below v = 1/2)—together with exact conditional-state
separability on Bob’s two qubits—be certified purely in exact rational arithmetic without
numerical integration or floating-point SDP relaxations?
Summary of Contributions.We resolve all three problems with exact rational algebra, a
zero-dependency Lean 4 kernel (18 theorems), and a pure-stdlib verifier ( EPR-STEER-CERT-1.0):
1. Universal Finite-m Steering Gap Law (Theorem 3.1):For every m≥ 1 and every
m projective axes {u1, . . . ,um} ⊂S2, ρv is provably unsteerable for all v≤ m2−m+2
2(m2−m+1) =
1
2 + 1
2(m2−m+1) , quantifying the Ω(m−2) gap abovev c = 1/2 with zero hidden constants.
2. Exact-Q Polytope Duality and Cuboctahedral Supremacy (Theorem 3.2):We
establish squared-rational primal–dual steering certificates across m∈ {2, 3, 4, 6, 7, 12, 15},
proving that at m = 6 the rational cuboctahedron (exact threshold vcub
6 =
p
5/18≈ 0.5270,
with an exact primal–dual rational bracket 0.525 <
p
5/18< 0.530) strictly outperforms the
Platonic icosahedron (exact thresholdv ico
6 = (1 +
√
5)/6≈0.5393, (v ico
6 )2 = (3 +
√
5)/18).
3. Exact-Q Two-Copy Superactivation with Separable Conditionals (Theorem 3.3):
We derive the closed-form PPT spectrum of Bob’s two-qubit conditional states ( λPT
min =
(1−v 2(1+2 s))/4 ≥ 1/16 > 0 at v = 1/2) and prove unconditionally over Q that ρ⊗2
v violates
all two-qubit LHS models atv= 1/2 (margin +1199/134064) and strictly below criticality
atv= 49999/100000<1/2.
2

--- Page 3 ---
4. Lean 4 Formalization and EPR-STEER-CERT-1.0 Verifier (Theorem 3.4):All 18 core
theorems are verified in zero-dependency Lean 4 ( v4.35.0, 0 sorry, 0 Classical.choice,
0 warnings); 14 standalone exact- Q certificates across 4 mutually exclusive modes pass
independent verification while rejecting 46/46 live adversarial attacks.
2 Preliminaries
For Alice’s projective measurement along a unit Bloch vectoru x ∈S 2 with outcomes a∈
{−1, +1} (Ma|x = I+au x·σ
2 ), the Werner state ρv produces Bob’s unnormalized conditional states
σa|x = TrA
 
(Ma|x ⊗I)ρ v

= 1
2
I−avu x ·σ
2

.(2)
An m-setting LHS model specifies probabilities pλ > 0 (P
λ pλ = 1), deterministic responses
a(λ)
x ∈ {−1,+1}, and valid qubit hidden statesρλ = I+n(λ)·σ
2 (∥n(λ)∥2
2 ≤1) satisfying
X
λ
pλn(λ) =0,
X
λ
pλa(λ)
x = 0,
X
λ
pλa(λ)
x n(λ) =vu x ∀x∈ {1, . . . , m},(3)
encoding respectively Bob’s isotropic marginal P
a σa|x = I/2, Alice’s uniform outcome prob-
abilities Tr(σ±|x) = 1 /2, and exact Bloch correlations (absorbing the global minus sign into
a(λ)
x 7→ −a(λ)
x ). For any linear steering witness {f1, . . . ,fm} ⊂R3 with Pm
x=1 ux · fx > 0, every
LHS model obeys the Cauchy–Schwarz bound
v
mX
x=1
ux ·f x =
X
λ
pλn(λ) ·
 mX
x=1
a(λ)
x fx
!
≤max
a∈{−1,+1}m

mX
x=1
axfx

2
.(4)
On two copies ρ⊗2
v distributed across (A1B1)(A2B2), any partially entangled Bell basis on A1A2
parameterized by rational entanglement ratiot∈Q∩[0,1] (c:= 1−t2
1+t2 ,s:= 2t
1+t2 ,c 2 +s 2 = 1),
|ψ0(t)⟩= |00⟩+t|11⟩√
1 +t 2 ,|ψ 1(t)⟩= t|00⟩ − |11⟩√
1 +t 2 ,
|ψ2(t)⟩= |01⟩+t|10⟩√
1 +t 2 ,|ψ 3(t)⟩= t|01⟩ − |10⟩√
1 +t 2 ,(5)
occurs with uniform probabilityp j = 1/4 and induces Bob’s conditional state
ρ(0)
B1B2 (v, t) =1
4

I⊗I−vc(Z⊗I+I⊗Z) +v 2 
s X⊗X−s Y⊗Y+Z⊗Z

,(6)
with ρ(1,2,3)
B1B2 obtained from the Bell sign patterns (+ s,−s, +1), ( −s, +s, +1), (+ s, +s,−1),
(−s,−s,−1) and local signs (+c,+c), (−c,−c), (+c,−c), (−c,+c).
3 Main Theorems
3.1 Universal Exact-QFinite-mSteering Gap Law
Theorem 3.1(Universal Finite- m Unsteerability Radius).For every integer m≥ 1andevery
configuration of m projective measurement axes {u1, . . . ,um} ⊂S2, the two-qubit Werner state
ρv is unsteerable for all
v≤v univ(m) := m(m−1) + 2
2
 
m(m−1) + 1
 = 1
2 + 1
2(m2 −m+ 1) ,(7)
3

--- Page 4 ---
admitting an explicit finite LHS model with at most Rmax(m) = m(m− 1) + 2pure hidden states
at the critical radius v = 1/(2S) ≥v univ(m)(and for every v≤v univ(m)via convex mixing
with the isotropic v = 0model, using at most2 Rmax(m)deterministic response–state pairs). In
particular, vuniv(1) = 1(exact), vuniv(m)is strictly decreasing in m, and every m-setting PVM
protocol leaves a provably unsteerable neighborhood of width∆ univ(m) = 1
2(m2−m+1) = Ω(m−2)
strictly above the critical boundaryv c = 1/2.
Proof. The m great circles Cx = {n ∈S 2 :n · ux = 0} (x = 1, . . . , m) partition S2 \ S
x Cx
into R open spherical cells D1, . . . , DR. Inductively, the k-th distinct great circle intersects the
preceding k− 1 circles in at most 2( k− 1) points, dividing itself into at most 2( k− 1) arcs that
each split at most one region, so R≤R max(m) = 2 + Pm
k=2 2(k− 1) = m(m− 1) + 2 (Lean 4
Theorem 1).
On each cell Dr of fractional area αr := 1
4π
R
Dr
dΩ > 0 (PR
r=1 αr = 1), the sign vector
a(r) = (sgn(n · ux))m
x=1 ∈ {−1, +1}m is constant. Define the cell centroidm r := 1
4π
R
Dr
n dΩ,
its norm sr := ∥mr∥2, and total norm S := PR
r=1 sr. Because 1
4π
R
S2 sgn(n · ux)n dΩ = 1
2 ux,R
S2 n dΩ =0, and antipodal symmetry pairs each cell Dr with −Dr of equal centroid norm
s−r = sr and negated sign vectora (−r) = −a(r), setting pr := sr/S and pure Bloch vectors
ˆnr :=m r/sr ∈S 2 (for sr > 0) yields a valid R-state LHS model satisfying P
r pra(r)
x = 0,P
r pr ˆnr =0, and P
r pra(r)
x ˆnr = 1
2S ux for all x = 1, . . . , m, certifying unsteerability for all
v≤ 1
2S .
To upper-bound sr, set ˆer =m r/sr ∈S 2 and let Cr = {n ∈S 2 :n · ˆer ≥t r} be the polar
cap centered at ˆer of equal fractional area αr = (1 −t r)/2 (so tr = 1 − 2αr). Sincen · ˆer ≥t r on
Cr \D r andn · ˆer ≤t r on Dr \C r while Area(Cr \D r) = Area(Dr \C r), rearrangement yields
sr = 1
4π
Z
Dr
(n· ˆer)dΩ≤ 1
4π
Z
Cr
(n· ˆer)dΩ = 1
2
Z 1
tr
z dz= 1−t 2
r
4 =α r(1−α r),
whose cleared-denominator algebraic identity is verified in Lean 4 (Theorem 2). Summing over
r = 1, . . . , Rand applying Cauchy–SchwarzPR
r=1 α2
r ≥ 1
R (PR
r=1 αr)2 = 1
R (Lean 4 Theorems 3–4)
gives
S=
RX
r=1
sr ≤
RX
r=1
αr(1−α r) = 1−
RX
r=1
α2
r ≤1− 1
R ≤1− 1
Rmax(m) = Rmax(m)−1
Rmax(m) ,
whence v≤ 1
2S ≥ Rmax(m)
2(Rmax(m)−1) = 1
2 + 1
2(m2−m+1) . Strict positivity above 1 /2, monotonicity in m,
and exact tightnessv univ(1) = 1 are proved in Lean 4 (Theorems 5–7).
3.2 Exact-QPolytope Steering Duality and Cuboctahedral Supremacy
Theorem 3.2(Squared-Rational Polytope Certificates and Cuboctahedral Supremacy).Let
w1, . . . ,wm ∈Q 3 satisfy ∥wx∥2
2 = Nu ∈Q >0 for all x (defining unit axesu x =w x/√Nu ∈S 2).
1. Zero-Square-Root Primal–Dual Certification:For any rational witness {fx} ⊂Q3
with P
x wx ·f x >0,ρ v ism-setting steerable whenever
v2
Nu
 mX
x=1
wx ·f x
!2
>max
a∈{−1,+1}m

mX
x=1
axfx

2
2
inQ.(8)
Conversely, any rational ensemble {(pλ, a(λ), b(λ))} with pλ > 0, Ppλ = 1, ∥b(λ)∥2
2 ≤N u,Ppλb(λ) =0, Ppλa(λ)
x = 0, and Ppλa(λ)
x b(λ) = vwx (∀x) certifies m-setting unsteerability
ofρ v strictly overQ.
4

--- Page 5 ---
2. Exact Cuboctahedral Threshold and Supremacy over the Icosahedron (m = 6):For
the6-axis rational cuboctahedronw x ∈ {(1,±1, 0), (1, 0,±1), (0, 1,±1)} (Nu = 2), the exact6-
setting steering threshold is vcub
6 =
p
5/18≈ 0.527046, attained on both sides by the canonical
witnessf x =w x (maxa ∥Paxwx∥2
2 = 20) and the uniform24-state LHS ensemble of signed
permutations of α(2, 1, 0)( ∥b∥2
2 = 5α2 ≤ 2, v = 5
6 α). By contrast, for the6-axis Platonic
icosahedron, the exact6-setting steering threshold is vico
6 = 1+
√
5
6 ≈ 0.539345(( vico
6 )2 = 3+
√
5
18 ),
attained on both sides by the canonical witness and the uniform12-state icosahedral-vertex
LHS ensemble. Thus the rational cuboctahedron strictly beats the Platonic icosahedron in
exact6-setting steering threshold, since 5
18 < 3+
√
5
18 ⇐ ⇒(5 − 3)2 < 5 ⇐ ⇒4 < 5(Lean 4
Theorem 8).
Proof. Part 1 follows directly from squaring (4) and rescalingn (λ) =b (λ)/√Nu in (3). For
Part 2, summing 6 cuboctahedron vectors with optimal signs gives ∥(4, 2, 0)∥2
2 = 20, so (vcub
6 )2 =
2·20
122 = 5
18 . Conversely, for the 24 signed permutationsb (λ) of α(2, 1, 0) with pλ = 1 /24
and a(λ)
x = sgn(wx · b(λ)), antipodal symmetry gives P
λ pλb(λ) =0and P
λ pλa(λ)
x = 0,
while P24
λ=1 |wx · b(λ)| = 40 α yields 1
24
P
λ a(λ)
x b(λ) = 5
6 αwx. Taking α =
p
2/5 matchesp
5/18 identically, while the rational choice α = 63/100 (5α2 = 19845/10000 ≤ 2) certifies
v = 21/40 = 0 .525. For the 6 icosahedral axesu x ∈ 1√
1+φ2 {(0,±1,±φ ) cyclic} (φ = 1+
√
5
2 ),
every pair of distinct axes satisfies |ux · uy| = 1/
√
5. Aligning signs with one vertexu 0 and its 5
nearest neighbors gives ∥P6
x=1 axux∥2 = 1 +
√
5 (squared norm 6 + 2
√
5), yielding vico
6 = 1+
√
5
6
and ( vico
6 )2 = 6+2
√
5
36 = 3+
√
5
18 ; conversely, the uniform 12-state LHS ensemblen (λ) = ±uy
(pλ = 1/12, a(λ)
x = sgn(ux · n(λ))) reproduces 1
6 (1 + 5 · 1√
5 )ux = 1+
√
5
6 ux with zero marginals,
establishing vico
6 = 1+
√
5
6 as the exact 6-setting threshold. Comparing squared thresholds yields
5
18 < 3+
√
5
18 ⇐ ⇒2<
√
5⇐ ⇒4<5 (Lean 4 Theorem 8).
3.3 Exact-Q Two-Copy Superactivation with Strictly Separable Conditionals
Theorem 3.3(Conditional Separability and Unconditional Exact- Q Two-Copy Superactivation).
Consider two copiesρ ⊗2
v of the two-qubit Werner state.
1. Exact Rational PPT Spectrum of Conditional States:Under the partially entangled
Bell basis (5) with c = 1−t2
1+t2 and s = 2t
1+t2 (t∈ [0, 1]), the four exact eigenvalues of Bob’s
partial-transposed conditional stateρ (j)T 2
B1B2 are
λ1,2 = 1∓2vc+v 2
4 , λ 3,4 = 1−v 2 ±2v 2s
4 .(9)
By the Peres–Horodecki criterion [6], all four conditional states on B1B2 are separable if and
only if v2(1 + 2s) ≤ 1. In particular, for all v≤ 1/
√
3 (including v≤ 1/2), every conditional
state is separable for alls∈[0,1], withλ PT
min ≥1/16>0atv= 1/2(Lean 4 Theorem 18).
2. Unconditional Exact-Q Two-Copy Superactivation:Define the two-copy steering
functional Wγ (γ∈Q >0) combining local WJD single-copy witnesses on copies1and2
(weight γ) with the SO(3) ×SO (3)-averaged full Bell-basis correlation witness ( t = s = 1).
Its quantum value on ρ⊗2
v is Qγ(v) = 2γv + 3v2, whileeverytwo-qubit LHS model (with
arbitrary separable or entangled hidden states σλ on B1B2) satisfies the exact rational upper
bound
Lγ ≤L ub
γ := 5167
7056 +γ+ 1
γ .(10)
At γ = 114, Q114(1/2) −L ub
114 = 1199
134064 > 0, certifying exact- Q two-copy superactivation of
the PVM-critical state ρ⊗2
1/2, and extending strictly below criticality to v = 49999
100000 < 1
2 (Lean 4
Theorem 17).
5

--- Page 6 ---
Proof. For Part 1, partial transposition on B2 sends Y7→ −Y in (6), yielding ρ(0)T2
B1B2 block-
diagonal in the computational basis {|00⟩,|11⟩} ⊕ {|01⟩,|10⟩} with eigenvalues (9); the other
outcomes j = 1, 2, 3 are locally unitarily equivalent, so all four share the identical spectrum (9).
Since 1−2vc+v 2 ≥(1−v) 2 ≥0, PPT holds iffλ 4 = (1−v 2(1 + 2s))/4≥0.
For Part 2, on ρ⊗2
v each local WJD witness scores v (total 2 γv) and the full Bell-basis
correlation witness Fj = Tr(T⊤
j (R⊤
1 σ1 ⊗R ⊤
2 σ2)) scores v2 Tr(T⊤
j Tj) = 3 v2, giving Qγ(v) =
2γv + 3v2. For any LHS model, convexity restricts the maximum to pure two-qubit hidden
states |ϕ⟩ ∈C4. By SO(3) ×SO (3) invariance and the Schmidt decomposition, we may set
|ϕq⟩ = cosq| 00⟩+sinq| 11⟩ (q∈ [0, π/4]), which has local Bloch norms∥b1∥2 = ∥b2∥2 = cos 2q and
correlation matrix CB = diag(sin 2q,−sin 2q, 1) = Cprod+(sin 2q)Cent, where Cprod = diag(0, 0, 1)
and Cent = diag(1,−1, 0). Thus the local term equals γ
2 (cos 2q + cos 2q) = γcos 2q, while
subadditivity of maxj gives
Ljoint(q)≤L joint(0) + (sin 2q)ER1,R2
h
max
j=0..3
Xj(R⊤
1 CentR2)
i
.
For the entangled remainder B = R⊤
1 CentR2, the four outcomes Xj(B) sum to 0 and obeyP3
j=0 Xj(B)2 = 4(B2
00 + B2
11 + B2
22) (Lean 4 Theorem 15). By the zero-sum Cauchy–Schwarz
bound 4X 2
k ≤3 P3
j=0 X2
j (Lean 4 Theorem 14) and Jensen’s inequality,
E
h
max
j
Xj(B)
i
≤
q
3E[B 2
00 +B 2
11 +B 2
22] =
r
3·3· ∥Cent∥2
F
9 =
√
2.
For the product baseline q = 0, letu= R⊤
1 ˆz,v= R⊤
2 ˆz∼Unif (S2) independently and set
p1 = |u1v1|, p2 = |u2v2|, p3 = |u3v3| (Ppi ≤ ∥u∥2∥v∥2 = 1). Because the four Bell sign
patterns have sign-product −1, our exact Bell sign-parity identities (Lean 4 Theorems 9–10) give
maxj Xj(A) = p1 + p2 + p3 when sgn(u1v1u2v2u3v3) = −1 and p1 + p2 + p3 − 2 min(p1, p2, p3)
when +1, each with exact probability 1/2 by octant symmetry. Hence
Ljoint(0) =E[p 1 +p 2 +p 3]−E[min(p 1, p2, p3)] = 3
4 −E[min(p 1, p2, p3)].
By our degree-5 sum-of-squares factorization 256 − 3125p(1 −p )4 = (5p− 1)2 
16 + (1−p )(240 −
325p+125p2)

≥ 0 with 4(240 −325p+125p2) = 5((10p− 13)2 +23) > 0, we prove 3125p2
1p2
2p2
3 ≤
16 min(p1, p2, p3) pointwise (Lean 4 Theorems 11–13). Taking expectations with the exact
spherical moment ES2 [x2y2z2] = 1/105 yields E[min(p1, p2, p3)] ≥ 3125
16 · 1
1052 = 125
7056 and thus
Ljoint(0) ≤ 3
4 − 125
7056 = 5167
7056 . Finally, 2D Cauchy–Schwarz and Lean 4 Theorem 16 give γcos 2q +√
2 sin2q≤
p
γ2 + 2< γ + 1
γ , establishing (10). Evaluating (10) at γ = 114 proves strict
superactivation atv= 1/2 andv= 49999/100000 (Lean 4 Theorem 17).
3.4 Zero-Floating-Point-TrustEPR-STEER-CERT-1.0Soundness
Theorem 3.4(Soundness and Primal–Dual Exclusivity of EPR-STEER-CERT-1.0).Every
accepted EPR-STEER-CERT-1.0 certificate is verified solely in exact Q arithmetic across
four mutually exclusive modes: finite m steering witness (exhaustively evaluating all
2m−1 sign patterns), finite m lhs model (verifying probability normalization, Bloch-ball
validity ∥b(λ)∥2
2 ≤N u, Bob’s isotropic marginal Ppλb(λ) =0, Alice’s uniform marginalsPpλa(λ)
x = 0, and exact correlations), universal finite m gap (replaying Theorem 3.1), and
two copy superactivation (enforcing single-copy PVM unsteerability v≤ 1/2alongside both
parts of Theorem 3.3). By the3D Cauchy–Schwarz weak duality (4) (Lean 4 Theorem 18),
no pair( v,{ ux})can simultaneously admit a valid finite m steering witness and a valid
finite m lhs model(oruniversal finite m gap) certificate.
6

--- Page 7 ---
Table 1: All 18 machine-checked theorems in lean/CriticalSteering.lean (Lean 4 v4.35.0,
zero external dependencies, 0sorry, 0Classical.choice, 0 warnings).
# Lean 4 Theorem Identifier Formalized Mathematical Statement
1great circleregionsclosedformR(m) =m(m−1) + 2 for allm≥1
2cap centroidareaidentityD 2−(D−2a)2 = 4a(D−a) (cap centroid identity)
3discretecauchyschwarznonneg( Par)2 ≤RPa2r overList Int
4universalfinitem gapboundR maxSnum≤(Rmax−1)D2 (Theorem 3.1)
5finite m gapstrictlyabovehalf0< m(m−1) + 1< m(m−1) + 2 (v univ>1/2)
6finite m gapmonotone1≤m 1 < m2 =⇒vuniv(m2)< vuniv(m1) (strict)
7finite m singlesettingexactoneR(1) = 2(R(1)−1) (v univ(1) = 1 exact)
8cuboctahedronbeatsicosahedron(5−3) 2 <5 (5/18<(3 +√5)/18⇐⇒vcub6 < vico6 )
9bell signparityoddnegOdd-sign Bell max =p 1+p2+p3
10bell signparityevennegEven-sign Bell max =p 1+p2+p3−2 min(p1, p2, p3)
11sos poly256minus3125identity256D 5−3125a(D−a)4 = (5a−D)2(· ··)
12sos cubicfactorstrictlypos240D 2−325aD+ 125a2 ≥0 via SOS
13sos minlowerboundcleared3125(p 1p2p3)2 ≤16p1D5 (p1+p2+p3 ≤D)
14zero sumfourcauchyschwarz P3j=0xj = 0 =⇒4x20 ≤3P3j=0x2j
15bell foursquaresidentity P
Bell signs(±a±b±c)2 = 4(a2+b2+c2)
16rigidityenveloperationalupper(g 2n+ 2g2d)g2n <(g2n+g2d)2 (pγ2+ 2< γ+ 1/γ)
17two copysuperactivationatandbelowhalfQ 114(v)> Lub114atv= 1/2 andv= 49999/100000
18ppt conditionalseparabilityandwitnessdualityλPTmin(1/2, s)≥1/16 and 3D Cauchy–Schwarz (n·f)2 ≤ ∥n∥2∥f∥2
Proof. Suppose (v,{ ux}) admits both a valid finite m lhs model certificate {(pλ, a(λ), b(λ))}
and a valid finite m steering witness certificate {fx}. Applying the 3D Lagrange–Cauchy–
Schwarz inequality (Lean 4 Theorem 18) to each hidden staten (λ) =b (λ)/√Nu (∥n(λ)∥2 ≤ 1)
yields SQ = v√Nu
P
x wx · fx ≤L LHS, contradicting S2
Q > L2
LHS. The same contradiction holds
againstuniversal finite m gapvia Theorem 3.1.
4 Zero-Dependency Lean 4 Kernel and Exact-QVerifier
All 18 algebraic, combinatorial, SOS, and duality theorems underlying Theorems 3.1–3.4 are for-
malized in lean/CriticalSteering.lean using pure Lean 4 [ 2] (leanprover/lean4:v4.35.0)
withzeroexternal dependencies, 0 sorry, 0 Classical.choice, and 0 warnings (verified by
lean/AuditAxioms.lean). Table 1 catalogs all 18 theorems.
Remark4.1 (Transparent Formalization Scope).Our Lean 4 kernel formally verifies the entire
discrete, algebraic, SOS, and rational-arithmetic backbone of Theorems 3.1–3.4: great-circle
region counting, the cap-centroid algebraic identity, discrete Cauchy–Schwarz, the universal gap
bound and strict monotonicity, cuboctahedral supremacy (4 < 5), both Bell sign-parity identities,
the degree-5 SOS factorization 256 − 3125p(1 −p )4 and cubic factor positivity, the cleared-
denominator bound 3125 p2
1p2
2p2
3 ≤ 16p1D5, the zero-sum four-variable Cauchy–Schwarz and
four-squares identities, the rational rigidity envelope
p
γ2 + 2< γ+ 1/γ, exact superactivation
at v = 1/2 and v = 49999/100000, PPT conditional separability, and the 3D Lagrange–Cauchy–
Schwarz duality bound. The continuous spherical rearrangement integral, Haar averaging of
ES2 [x2y2z2] = 1 /105, and Schmidt decomposition are proved analytically in Section 3 and
independently validated numerically in Section 5.
Zero-Float Verifier (EPR-STEER-CERT-1.0). src/steering certifier.py imports strictly
Python stdlib ( fractions.Fraction, math, re), enforcing strict recursive type whitelisting,
single-line ASCII identifier hygiene on cert id, exact dictionary key sets, an anchored ASCII
canonical rational parser, distinct projective measurement axes (rejecting duplicates and antipodal
axes), Bloch-ball state validity, exhaustive sign-pattern checking, and all four theorem replays.
7

--- Page 8 ---
Table 2: Experiment 1: 14 independently verified zero-float EPR-STEER-CERT-1.0 certificates
across all four modes (exact JSON files archived inresults/certificates/*.cert.json).
# Certificate ID Mode VerdictmExactv∈QFloat ms
C1witnessm2squarev71 finite msteeringwitness STEERABLE2 71/100 0.71000 1.50
C2witnessm3octahedronv58 finite msteeringwitness STEERABLE3 29/50 0.58000 0.30
C3witnessm6cuboctahedronv53 finitemsteeringwitness STEERABLE6 53/100 0.53000 0.98
C4witnessm12pyth221v56 finite msteeringwitness STEERABLE12 14/25 0.56000 50.52
C5witnessm15octpyth221v52 finitemsteeringwitness STEERABLE15 13/25 0.52000 489.03
C6lhs m2squarev70 finite mlhsmodel UNSTEERABLE LHS2 7/10 0.70000 0.36
C7lhs m3octahedronv57 finite mlhsmodel UNSTEERABLE LHS3 57/100 0.57000 0.64
C8lhs m4cubediagv57 finite mlhsmodel UNSTEERABLE LHS4 57/100 0.57000 0.46
C9lhs m6cuboctahedronv525 finitemlhsmodel UNSTEERABLE LHS6 21/40 0.52500 1.74
C10univgapm3v47 universal finitemgap UNIV UNSTEERABLE3 4/7 0.57143 0.12
C11univgapm6v1631 universal finitemgap UNIV UNSTEERABLE6 16/31 0.51613 0.16
C12univgapm100v49519901 universalfinitemgap UNIV UNSTEERABLE100 4951/9901 0.50005 0.10
C13superacttwocopyvhalf two copysuperactivation SUPERACTIVATEDPPT— 1/2 0.50000 0.23
C14superacttwocopybelowhalf twocopysuperactivation SUPERACTIVATEDPPT— 49999/100000 0.49999 0.18
5 Computational Experiments and Adversarial Red-Teaming
All four experiments reproduce deterministically in < 5 s via scripts/run all experiments.py
and pass full Gate-2 verification viascripts/verify all.py.
Experiment 1: Atlas of14Exact- Q Certificates.Table 2 summarizes all 14 indepen-
dently verified EPR-STEER-CERT-1.0 certificates spanning all four modes. Notably, lhs m6
cuboctahedron v525 (24 rational hidden states at v = 21 /40 = 0 .525) and witness m6
cuboctahedron v53 (v = 53/100 = 0.530) bracket the exact cuboctahedral threshold
p
5/18≈
0.527046 from both sides strictly over Q; univ gap m100 v4951 9901 certifies 100-setting un-
steerability strictly above 1/2 in 0.10 ms; and superact two copy v half and superact two
copy below half certify exact-Q two-copy superactivation at v = 1/2 and v = 49999/100000 in
0.18–0.23 ms.
Experiment 2: Finite- m Polytope Ladder vs. Universal Cap-Cell Bound.Table 3
and Figure 1 compare seven exact- Q polytope families plus the Platonic icosahedron ( m = 6)
and dodecahedron ( m = 10) against Theorem 3.1. For m∈ {2, 3, 4, 6, 10}, the canonical witness
fx =w x matches the dual LHS ensemble, giving exact thresholdsv∗
m; for the non-vertex-transitive
rational families m∈ {7, 12, 15} (marked with †), Table 3 reports the certifiedcanonical-witness
upper bound vcan
m ≥v ∗
m (which non-canonical rational weightsf x ̸=w x can strictly improve).
Every single polytope sits cleanly above vuniv(m); at m = 3 our universal bound 4 /7 ≈ 0.5714
lies within 1.1% (1.03%) of the exact octahedral threshold 1 /
√
3≈ 0.5774, and at m = 6 the
rational cuboctahedron (
p
5/18≈ 0.5270) beats the Platonic icosahedron (0 .5393) while sitting
within 2.1% of vuniv(6) = 16/31 ≈ 0.5161. Adding the 3 octahedral axes to the 12 Pythagorean
(2, 2, 1)/3 axes certifies v∗
15 ≤v can
15 =
p
547/2025≈ 0.5197, strictly beating the dodecahedron
(0.5236) with purely rational coordinates.
Experiments 3 & 4: Haar Monte Carlo Cross-Check and Conditional-State PPT
Phase Diagram.In Experiment 3, 100 ,000 independent Haar SO(3) ×SO (3) samples inde-
pendently validate Theorem 3.3: ES2 [x2y2z2] = 0.009492 vs. exact 1 /105 = 0.009524 (z = 0.96);
Ljoint(0) = 0.68505 ± 0.00069 lies strictly below our exact- Q SOS bound 5167 /7056 ≈ 0.73228 <
3/4; and Ljoint(q) ≤ 5167
7056 +
√
2 sin2q holds across all 21 Schmidt angles q∈ [0, π/4] (Figure 2a).
Sweeping γ confirms that the tight continuous witness reaches v(2)
tight ≈ 0.4933 < 1/2 at γ = 3,
while our zero-float exact- Q certificate crosses below 1 /2 analytically for all γ >7056/125 =
56.448 (integers γ≥ 57; first plotted grid point γ = 70) and reaches v(2)
cert ≈ 0.499961 < 1/2
at γ = 114 (Figure 2b). In Experiment 4, all 40 grid checks of (9) match direct 4 × 4 matrix
8

--- Page 9 ---
Table 3: Experiment 2: Exact primal–dual thresholds v∗
m (m∈ {2, 3, 4, 6, 10}) and certified
canonical-witness (fx =w x) upper bounds vcan
m ≥v ∗
m (†, m∈ {7, 12, 15}) versus Theorem 3.1’s
universal boundv univ(m) = 1
2 + 1
2(m2−m+1) .
Polytope FamilymExact (v can
m )2 v∗
m /v can
m vuniv(m)v univ float ∆ m =v m −1/2
Square (exact) 2 1/2 0.70711 2/3 0.66667 0.20711
Octahedron (exact) 3 1/3 0.57735 4/7 0.57143 0.07735
Cube diagonals (exact) 4 1/3 0.57735 7/13 0.53846 0.07735
Cuboctahedron (exactQ) 6 5/18 0.52705 16/31 0.51613 0.02705
Icosahedron (Platonic, exact) 6 (3 +
√
5)/18 0.53934 16/31 0.51613 0.03934
Oct. + 4 Pyth. (2,2,1) (†) 7 139/441≤0.56142 22/43 0.51163≤0.06142
Dodecahedron (Platonic, exact) 10 (7 + 3
√
5)/50 0.52361 46/91 0.50549 0.02361
Pythagorean (2,2,1)/3 (†) 12 25/81≤0.55556 67/133 0.50376≤0.05556
Oct. + 12 Pyth. (2,2,1) (†) 15 547/2025≤0.51973 106/211 0.50237≤0.01973
Figure 1: Experiment 2:(a)Exact finite- m steering polytope thresholds ( m∈ {2, 3, 4, 6, 10})
and certified canonical-witness upper bounds vcan
m ≥v ∗
m (m∈ {7, 12, 15}) (squares: exact
Q; diamonds: Platonic) versus Theorem 3.1’s universal cap-cell lower bound vuniv(m) = 1
2 +
1
2(m2−m+1) (green curve and shaded unsteerable region), highlighting cuboctahedral supremacy
over the icosahedron at m = 6.(b)Log-log scaling of the gap above vc = 1/2 confirming the
non-asymptotic Ω(m−2) law up tom= 100.
partial-transpose eigendecompositions to machine precision ( max err = 1.11 × 10−16), mapping
the exact PPT boundarys swap(v) = (1−v 2)/(2v2) (Figure 3a).
Adversarial Red-Team Verification (46/46Attacks Rejected).The automated suite
tests/test suite.py subjects verify steering certificate exact to 46 live forgery at-
tempts spanning schema, type, and identifier tampering, canonical rational parser bypasses,
unviolated or forged witnesses, duplicate or antipodal axes, Bloch-ball violations ( ∥b∥2
2 > Nu),
non-isotropic Bob marginals, non-uniform Alice marginals ( Ppλa(λ)
x ̸= 0), probability-sum
violations, universal-bound violations, forged Bell constants, already single-copy steerable fake
superactivation (v = 11/20 > 1/2), and non-PPT conditional states (v = 3/5 with λPT
min = −1/50).
All 46/46 attacks raiseValueError.
6 Discussion and Limitations
Our results provide exact rational witnesses and machine-checked proofs for both sides of Zhang
and Chen’s critical EPR steering picture [ 12]: every finite- m protocol is bounded away from
9

--- Page 10 ---
Figure 2: Experiment 3:(a)Exact- Q SOS + subadditivity upper bound 5167
7056 +
√
2 sin(2q)
(red dashed) strictly dominates 100 ,000-sample Haar MC Ljoint(q) (blue) across all two-qubit
hidden-state Schmidt angles q∈ [0, π/4] while remaining strictly below Qjoint(1/2) = 3 /4 at
q = 0.(b)Two-copy steering threshold v(2)(γ) crossing strictly below vc = 1/2 both numerically
(0.4933 at γ = 3) and via zero-float exact- Q certification (γ≥ 57 analytically, first plotted grid
pointγ= 70, optimal 0.499961 atγ= 114).
vc = 1/2 by at least 1
2(m2−m+1) , while two copies ρ⊗2
v unconditionally superactivate at and
strictly belowv= 1/2 with strictly separable conditional states.
Two limitations point to natural extensions. First, our exact- Q two-copy superactivation
witness uses the maximally entangled Bell measurement ( t = s = 1) rather than arbitrarily weak
measurement entanglement (t→ 0+), and targets the isotropic Werner boundary rather than
general anisotropic Bell-diagonal states; extending our SOS-moment technique to arbitrarily
small t >0 and general T-states [3] is a compelling next step. Second, exhaustive sign-pattern
verification in finite m steering witness scales as O(2m−1) (0.49 s at m = 15); certifying
larger m≥ 20 polytopes will benefit from symmetry-orbit reduction or exact branch-and-bound
zonotope certificates.
References
[1] Daniel Cavalcanti and Paul Skrzypczyk. Quantum steering: a review with focus on
semidefinite programming.Reports on Progress in Physics, 80(2):024001, 2017.
[2] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prover and programming
language. InAutomated Deduction – CADE 28, volume 12699 ofLecture Notes in Computer
Science, pages 625–635. Springer, 2021.
[3] Sania Jevtic, Michael J. W. Hall, Malcolm R. Anderson, Marcin Zwierz, and Howard M.
Wiseman. Einstein–Podolsky–Rosen steering and the steering ellipsoid.Journal of the
Optical Society of America B, 32(4):A40–A49, 2015.
[4] H. Chau Nguyen and Thanh Vu. Necessary and sufficient condition for steerability of
two-qubit states by the geometry of steering outcomes.Europhysics Letters, 115(1):10003,
2016.
[5] Carlos Palazuelos. Superactivation of quantum nonlocality.Physical Review Letters,
109(19):190401, 2012.
10

--- Page 11 ---
Figure 3: Experiments 1 & 4:(a)Exact conditional-state PPT separability phase diagram on
Bob’s two qubits B1B2 showing sswap(v) = (1 −v 2)/(2v2) (red) and strict interior separability
λPT
min ≥ 1/16 > 0 along the entire PVM-critical line v = 1/2 (blue dashed).(b)Pure-stdlib
EPR-STEER-CERT-1.0verifier runtime (log scale) across all 14 certificates (C1–C14).
[6] Asher Peres. Separability criterion for density matrices.Physical Review Letters, 77(8):1413–
1415, 1996.
[7] Marco T´ ulio Quintino, Nicolas Brunner, and Marcus Huber. Superactivation of quantum
steering.Physical Review A, 94(6):062123, 2016.
[8] Dylan J. Saunders, Steve J. Jones, Howard M. Wiseman, and Geoff J. Pryde. Experimental
EPR-steering using Bell-local states.Nature Physics, 6:845–849, 2010.
[9] Roope Uola, Ana C. S. Costa, H. Chau Nguyen, and Otfried G¨ uhne. Quantum steering.
Reviews of Modern Physics, 92(1):015001, 2020.
[10] Reinhard F. Werner. Quantum states with Einstein-Podolsky-Rosen correlations admitting
a hidden-variable model.Physical Review A, 40(8):4277–4281, 1989.
[11] Howard M. Wiseman, Steve J. Jones, and Andrew C. Doherty. Steering, entanglement, non-
locality, and the Einstein-Podolsky-Rosen paradox.Physical Review Letters, 98(14):140402,
2007.
[12] Yu-Xuan Zhang and Jing-Ling Chen. Critical properties of EPR steering.arXiv preprint
arXiv:2611.09321, 2026.
11
