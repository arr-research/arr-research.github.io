# Quantum Spectral Christoffel-Super-Poincare Inequalities, Exact Piecewise-Logarithmic Mixing Laws, and Machine-Checked Rapid-Mixing Certificates Beyond the Spectral Gap

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-3TFT8A9XE99YYV6W` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/beyond-gap-gibbs-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `78a880bd711c6dc2b9345f5aefeb530d2aae51b355c2425e1b901098b4048004`

## Abstract

Proving rapid mixing of quantum Gibbs samplers beyond high-temperature regimes was recently revolutionized by Chen and Ding (arXiv:2610.05848), who established O(log^4 n + log(1/eps)) mixing for one-dimensional KMS-detailed-balanced Gibbs samplers by showing that states far from equilibrium carry large weight outside low-weight operator subspaces where stronger dissipation holds. Turning this qualitative mechanism into exact, non-asymptotic, constant-free mixing-time certificates for general non-commuting Hamiltonians—without relying on asymptotic hypercontractivity constants or floating-point eigensolvers—remains open. We resolve this problem with five theorems, a zero-dependency Lean 4 formalization, and a zero-floating-point-trust exact-Q LDL^T certificate verifier. First, for any full-rank Gibbs state sigma and any KMS-symmetric Markov generator with subspace I in V and operator-order Schur constant lambda_op(V^perp), we introduce the basis-independent Quantum Christoffel Operator K_V = sum_{a=1}^D E_a^dag E_a and prove the exact Quantum Super-Poincare Inequality E(X_rho, X_rho) >= lambda_op(V^perp) (chi^2_sigma(rho||sigma) - (||K_V||_inf - 1))_+ for every quantum state rho. Second, for any subspace ladder (Pauli-weight or exact KMS eigenmodes), we integrate the upper convex envelope dy/dt <= -2 max_k lambda_k (y - C_k) in closed form across exact knots y_j* = (lambda_j C_j - lambda_{j-1} C_{j-1})/(lambda_j - lambda_{j-1}), proving strict speedup over T_gap whenever y_0 > y_1* and a universal factor-of-2 optimality law (T_SP/t_exact -> 1 as eps -> 0^+ or y_0 -> infinity) on 2-tier commuting semigroups. Third, we prove an explicit, constant-free T_SP(n, eps) <= (1/(4*gamma)) (log n)^2 + O(gamma^-1 (log n + log(1/eps))) mixing bound for linear Pauli-weight ladders using pure L^1 -> L^2 projection (zero hypercontractivity), alongside the exact two-regime alpha-Super-Poincare phase diagram across alpha in (0, 1), alpha = 1, and alpha > 1. Fourth, we lift every convex-hull bound directly to non-asymptotic trace-norm and relative-entropy decay D(rho_t||sigma) <= D_2(rho_t||sigma) <= log(1 + y_env(t)). Fifth, we construct cryptographically linked global operator-order exact-Q LDL^T PSD witnesses certifying both subspace gaps and Christoffel norms strictly over Q. All 16 core algebraic theorems are formalized in Lean 4 (v4.35.0, 0 sorry, 0 Classical.choice) and benchmarked on non-commuting 1D tilted/ferromagnetic TFIM (1.26x-3.30x speedup for n=3,4; 1.65x-3.30x at n=4) and XXZ (1.57x) KMS Gibbs samplers, n=10-1,000 depolarizing chains (17.7x-20.7x speedup), and 6 exact-Q certificates containing 14 verified linked LDL^T PSD witnesses.

## Full Extracted Text

--- Page 1 ---
Quantum Spectral Christoffel–Super-Poincaré
Inequalities, Exact Piecewise-Logarithmic Mixing
Laws, and Machine-Checked Rapid-Mixing
Certificates Beyond the Spectral Gap
Lluis Eriksson∗
November 24, 2026
Abstract
Proving rapid mixing of quantum Gibbs samplers beyond high-temperature regimes
was recently revolutionized by Chen and Ding [6], who established O(log4 n+ log(1/ε))
mixing for one-dimensional KMS-detailed-balanced Gibbs samplers by showing that states
far from equilibrium carry large weight outside low-weight operator subspaces where stronger
dissipation holds. Turning this qualitative mechanism intoexact, non-asymptotic, constant-
freemixing-time certificates for general non-commuting Hamiltonians—without relying on
asymptotic hypercontractivity constants and with exact-Q verification of the quantized
spectral-gap and Christoffel bounds—remains open. We resolve this problem with five
theorems, a zero-dependency Lean 4 formalization, and an exact-QLDL ⊤certificate verifier.
First, for any full-rank Gibbs stateσ and any KMS-symmetric Markov generator with
subspace I∈V⊂B (H)and restricted gap λ(V⊥), we introduce the basis-independent
Quantum Christoffel Operator KV := ∑D
a=1 E†
aEa and prove the exact Quantum Super-
Poincaré Inequality E(Xρ,Xρ) ≥λ (V⊥)
(
χ2
σ(ρ∥σ) −(∥KV∥∞−1)
)
+ for every quantum
state ρ. Second, for any subspace ladder (Pauli-weight or exact KMS eigenmodes), we
integrate the upper convex envelopedy
dt ≤−2 maxkλk(y−C k)in closed form across exact
knots y∗
j = (λkj Ckj −λkj−1 Ckj−1 )/(λkj −λkj−1 ), proving strict speedup overTgap whenever
y0 >y ∗
1 and a universal factor-of-2 optimality law (TSP/texact →1as ε→ 0+ or y0 →∞)
on 2-tier commuting semigroups. Third, we prove an explicit, constant-freeTSP(n,ε) ≤
1
4γ(logn)2 +O(γ−1(logn+log(1/ε)))mixing bound for linear Pauli-weight ladders using pure
L1 →L2 projection (zero hypercontractivity, with universalc= 3for all quantum states and
tighter c= 1for product-state trajectories under product semigroups), alongside the exact
two-regime α-Super-Poincaré phase diagram acrossα∈ (0,1), α= 1, andα> 1. Fourth, we
lift every convex-hull bound directly to non-asymptotic trace-norm and relative-entropy decay
D(ρt∥σ) ≤D2(ρt∥σ) ≤log (1 + yenv(t)). Fifth, we construct cryptographically linked global
operator-order exact-QLDL ⊤PSD witnesses certifying both subspace gaps and Christoffel
norms strictly overQ on the quantized operator bundle given perturbation radiiδQ
∗ (with our
synthesis script estimatingδQ
∗ against double-precisioneigh(H) for interacting chains, while
analytical depolarizing certificates are end-to-end exact-Q with zero floating-point input). All
16 core algebraic theorems are formalized in Lean 4 (v4.35.0, 0sorry, 0Classical.choice)
and benchmarked on non-commuting 1D tilted/ferromagnetic TFIM (1.26×–3.30×speedup
for n= 3,4;1 .65×–3.30×at n= 4) and XXZ (1.57×) KMS Gibbs samplers,n= 10–1,000
depolarizing chains (17.7×universal c= 3and20 .7×product-state c= 1speedup), and 6
exact-Qcertificates containing 14 verified linkedLDL⊤PSD witnesses.
∗Independent researcher (Sweden). Research, zero-dependency Lean 4 proofs, exact-QLDL ⊤and convex-hull
mixing-time verifiers, and benchmarks prepared with AI assistance (Google Antigravity) and publicly archived at
https://github.com/lluiseriksson/beyond-gap-gibbs-certificates.
1

--- Page 2 ---
1 Introduction
Preparing thermal Gibbs statesσ= e−βH/Tr(e−βH)of interacting quantum spin systems via
dissipative Lindbladian evolution is a central primitive of quantum simulation and quantum
statistical mechanics [7,5,4]. Traditional convergence bounds rely on the Poincaré spectral gapµ1
of the Kubo–Martin–Schwinger (KMS)-symmetric LindbladianL†, yielding the worst-case mixing
time Tgap(ε) = 1
2µ1
log
(
χ2
σ(ρ0∥σ)/ε2)
= O(n+ log(1/ε))[ 10] becauseχ2
σ(ρ0∥σ) ≤λmin(σ)−1 −1
grows exponentially in system sizen. Overcoming this linear-n bottleneck typically required
proving a uniform quantum Modified Logarithmic Sobolev Inequality (MLSI) [8], which had
remained open for non-commuting spin chains at arbitrary inverse temperatureβ >0.
In a major recent breakthrough, Chen and Ding [6] proved rapid mixingO(log4 n+ log(1/ε))
for one-dimensional non-commuting KMS quantum Gibbs samplers at every positive temperature
viaspectral analysis beyond the spectral gap: any state far fromσ must carry significantχ2
σ
weight outside the span of low-weight Pauli operators, where higher-weight dissipation rates
drive a rapid initial (double-exponential) burn-in before the spectral gapµ1 governs the final
exponential tail.
To convert this paradigm into an exact, assumption-light, finite-size certification engine—
analogous to classical Super-Poincaré theory [11, 3] and complementing our recent machine-
checked spectral certificates [1, 2]—three questions arise:
1. Exact Non-Commuting Projection Geometry:What is the sharpest basis-independent
operator invariant controlling theKMSL 1(σ) →L 2(σ)projection norm on a subspace
V⊂B(H)?
2. Closed-Form Mixing Law & Sharpness:Given a discrete ladder of subspace gaps and
projection norms{(λk,Λk)}m
k=0, what is the exact closed-form mixing time, how tight is it
against true semigroup trajectories, and what scaling does pureL1 →L2 projection achieve
without hypercontractivity?
3. Zero-Floating-Point-Trust Certification:Can both the higher-tier spectral gapsλk,
the Christoffel normsΛk, and the resulting mixing timeTSP(ε)be certified strictly in exact
rational arithmeticQwith machine-checked Lean 4 soundness?
We answer all three questions completely in Sections 2–6.
2 Quantum Spectral Christoffel–Super-Poincaré Inequalities
Let Hbe a finite-dimensional Hilbert space (d= dimH) andσ≻ 0( Trσ = 1) a full-rank Gibbs
state. EquipB(H)with the KMS inner product and norm
⟨X,Y⟩KMS := Tr
(
σ1/2X†σ1/2Y
)
,∥X∥ 2
2,σ :=⟨X,X⟩ KMS.(1)
For any quantum stateρ⪰ 0( Trρ = 1), its KMS relative densityXρ := σ−1/2ρσ−1/2 ⪰0
satisfies ⟨I,Xρ⟩KMS = Trρ = 1, ∥Xρ∥2
2,σ = Tr
(
(σ−1/4ρσ−1/4)2)
= eD2(ρ∥σ) (where D2 is the
sandwiched Rényi-2 divergence [9]), and
χ2
σ(ρ∥σ) :=∥X ρ −I∥2
2,σ =e D2(ρ∥σ) −1.(2)
Moreover, setting B := σ1/4(Xρ −I )σ1/4 = σ−1/4(ρ−σ )σ−1/4, matrix Hölder’s inequality
(∥UVW∥1 ≤∥U∥4∥V∥2∥W∥4) gives the exact constant-1 trace-norm domination
∥ρ−σ∥1 =∥σ 1/4Bσ1/4∥1 ≤(Trσ) 1/4∥B∥2(Trσ)1/4 =
√
χ2σ(ρ∥σ)(3)
(discrete weighted form proved in Lean 4:trace_norm_sq_le_chi2).
Let L† be a Heisenberg-picture Lindbladian that is KMS-symmetric (⟨X,L†Y⟩KMS =
⟨L†X,Y⟩KMS) and primitive (kerL† = CI), with nonnegative Dirichlet form E(X,X) :=
⟨X,(−L†)X⟩KMS ≥0. Under ρt = etL(ρ0), Xρt = etL†
(Xρ0)obeys d
dtχ2
σ(ρt∥σ) = −2E(Xρt,Xρt).
2

--- Page 3 ---
2.1 Basis-Independent Quantum Christoffel Operator and Super-Poincaré
Bound
Definition 2.1(Quantum Christoffel Operator).Let V⊂B (H)be any subspace containingI,
and let{E1,...,E D}be anyKMS-orthonormal basis ofV(⟨E a,Eb⟩KMS =δab). TheQuantum
Christoffel OperatorofVis
KV :=
D∑
a=1
E†
aEa ⪰I, ΛV :=∥K V∥∞,Λ V := sup
∥ψ∥=1
D∑
a=1
⏐⏐⟨ψ|Ea|ψ⟩
⏐⏐2.
Note that KV is strictly invariant under any unitary change ofKMS-orthonormal basis
E′
a = ∑
bUabEb (since U†U = ID), and whenσ = I/2n with V = span{P : |P|≤k} , KV =(∑k
j=0
(n
j
)
3j)
I.
Theorem 2.1(Quantum Spectral Christoffel–Super-Poincaré Inequality).Let I∈V⊂B (H)
haveKMS-orthogonal projectionP V, and define itsoperator-order dissipation constant
λop(V⊥) := sup
{
λ≥0 :−L †⪰λ(I−P V)inL 2(KMS)
}
= inf
X/∈V
E(X,X)
∥(I−P V)X∥2
2,σ
.
Then foreveryquantum stateρ:
(a) 1 ≤ΛV ≤ΛV, and the centered projection satisfies∥PV(Xρ −I)∥2
2,σ ≤ΛV −1 ≤ΛV −1
(see Table 1).
(b) The Dirichlet form obeys the exact Quantum Super-Poincaré Inequality (Table 1):
E(Xρ,Xρ)≥λ op(V⊥)
(
χ2
σ(ρ∥σ)−( ΛV −1)
)
+
.(4)
In particular, writingV = CI⊕V +, λop(V⊥) = λmin
(
M⊥⊥−M⊥V+M−1
V+V+MV+⊥
)
is the
exact Schur complement, coinciding identically with the(r+ 1)-th eigenvalueµr+1 on every
L†-invariant eigenmode subspaceVr = span{E0,...,E r}.
(c) For any subspace filtrationI∈V 0 ⊂V1 ⊂···⊂V m with Ck := ΛVk −1and λk := λop(V⊥
k ),
the piecewise-linear convex envelope satisfies (Lean:super_poincare_envelope_two)
E(Xρ,Xρ)≥Φ env
(
χ2
σ(ρ∥σ)
):= max
0≤k≤m
λk
(
χ2
σ(ρ∥σ)−C k
)
.(5)
Proof. For any state ρ, ⟨Ea,Xρ⟩KMS = Tr(σ1/2E†
aσ1/2σ−1/2ρσ−1/2) = Tr(E†
aρ), hence
∥PVXρ∥2
2,σ = ∑D
a=1 |Tr(E†
aρ)|2. Because ρ↦→ |Tr(E†
aρ)|2 is convex on the compact con-
vex state space, the maximum of the sum is attained at an extreme pointρ= |ψ⟩⟨ψ|(∥ψ∥= 1),
giving ∥PVXρ∥2
2,σ ≤ΛV. By Cauchy–Schwarz,|⟨ψ|Ea|ψ⟩|2 ≤∥Ea|ψ⟩∥2 = ⟨ψ|E†
aEa|ψ⟩; summing
over a= 1,...,D yieldsΛ V ≤sup ∥ψ∥=1⟨ψ|KV|ψ⟩= ΛV. Since I∈V and ⟨I,Xρ −I⟩KMS = 0,
orthogonality gives∥PVXρ∥2
2,σ = 1 + ∥PV(Xρ −I )∥2
2,σ, proving (a). For (b), by definition of
λop(V⊥),
E(Xρ,Xρ) =E(X ρ −I,X ρ −I)≥λ op(V⊥)∥(I−P V)(Xρ −I)∥2
2,σ.
Pythagoras yields∥(I−P V)(Xρ −I)∥2
2,σ = χ2
σ(ρ∥σ) −∥PV(Xρ −I)∥2
2,σ ≥χ2
σ(ρ∥σ) −(ΛV −1),
proving (4) and (5). The Schur-complement formula follows from block positivity ofMKMS −
λ(I−P V)on( CI)⊥= V+ ⊕V ⊥(where MV+V+ ≻0by primitivity), reducing toM⊥⊥⪰µr+1I⊥
wheneverM⊥V+ = 0.
3

--- Page 4 ---
2.2 Exact Upper-Convex-Hull Piecewise-Logarithmic Mixing Law and Sharp-
ness
Theorem 2.2(Exact Piecewise-Logarithmic Mixing Law and 2-Tier Optimality).Let
{(λkj,Ckj)}r
j=0 (0 <λk0 <···<λ kr,0 = Ck0 <···<C kr) be the minimal active upper convex
hull of the affine functionsℓk(y) = λk(y−C k)on(0 ,∞)satisfying (5), with transition knots
y∗
0 = 0,y ∗
r+1 = +∞, andy∗
j = (λkjCkj −λkj−1 Ckj−1 )/(λkj −λkj−1 )(1≤j≤r). Then:
(a) Well-Posedness and Exact Mixing Time.The knots satisfy0< y∗
1 <···< y ∗
r and
y∗
j >Ckj for all j≥ 1(Table 1). For every initial stateρ0 with y0 = χ2
σ(ρ0∥σ) >ε2 >0,
the exact piecewise-linear envelope solutionyenv(t)satisfies χ2
σ(ρt∥σ) ≤yenv(t)for all t≥ 0,
and hence∥ρt −σ∥1 ≤εfor all
t≥T SP(ε;y0) :=
r∑
j=0
1
2λkj
log
(
min(y0,y∗
j+1)−C kj
max(ε2,y∗
j)−C kj
)
1min(y0,y∗
j+1)>max(ε2,y∗
j).(6)
(b) Strict Speedup over Spectral Gap.Whenever y0 > y∗
1 and λk1 > λk0, we have
TSP(ε;y0)<T gap(ε;y0) := 1
2λk0
log(y0/ε2)strictly (Table 1).
(c) Universal Factor-of-2 Sharpness on 2-Tier Semigroups.For any0<λ0 <λ1 and
C1 >ε2, consider the 2-tier commuting semigroup withχ2(t) = C1e−2λ0t + (y0 −C1)e−2λ1t
(y0 >y∗
1) and exactχ2-hitting timetexact(ε). Then
texact(ε)≤T SP(ε;y0)≤2t exact(ε) + 1
2λ0
log λ1
λ1 −λ0
+ 1
2λ1
log+
(λ1 −λ0
λ0
)
,(7)
and TSP(ε; y0)/texact(ε) →1in both asymptotic regimes ε→ 0+ (fixed y0) and y0 →∞
(fixedε).
Proof. BecauseΦ env(y)is continuous, strictly increasing, and piecewise linear on(0,∞)with
active slope λkj and intercept −λkjCkj on[ y∗
j,y∗
j+1](Lean: hull_tier2_dominates_above,
hull_tier1_dominates_below), comparison ofdy
dt ≤−2Φenv(y)gives χ2
σ(ρt∥σ) ≤yenv(t), where
the time required for yenv to descend from y0 to ε2 is
∫y0
ε2
dy
2Φenv(y) , which evaluates term-
by-term to (6). Part (b) follows immediately from 1
2Φenv(y) < 1
2λk0y on( y∗
1,y0]. For (c),
texact ≤T SP holds by (a). Since C1e−2λ0texact ≤ε 2 and( y0 −C1)e−2λ1texact ≤ε 2, we have
texact ≥max
(1
2λ0
log C1
ε2 , 1
2λ1
log y0−C1
ε2
)
. Writingy∗
1 = λ1
λ1−λ0
C1 andy ∗
1 −C1 = λ0
λ1−λ0
C1,
TSP(ε;y0) = 1
2λ0
log C1
ε2 + 1
2λ0
log λ1
λ1 −λ0
+ 1
2λ1
log y0 −C1
ε2 + 1
2λ1
log ε2
y∗
1 −C1
≤2t exact(ε) + 1
2λ0
log λ1
λ1 −λ0
+ 1
2λ1
log+
(λ1 −λ0
λ0
)
,
using ε2 <C1 in the last step. Whenε→ 0+ (fixed y0), the first term dominates bothtexact and
TSP; wheny0 →∞ (fixed ε), the third term dominates both, yieldingTSP/texact →1in either
limit.
3 Pure L1 →L 2 Poly-Logarithmic Speedup and Two-Regime
Phase Diagram
Theorem 3.1(PureL 1 →L2 (logn) 2 Scaling andα-Phase Diagram).(a) Constant-Free
O(log2 n)Bound Without Hypercontractivity.Suppose an n-qubit (n≥ 2) KMS-
symmetric semigroup with y0 = 2 n −1satisfies (5) along a trajectory ρt with linear
4

--- Page 5 ---
Pauli-weight dissipationλk ≥γ (k+ 1)( γ >0) and Christoffel boundsCk ≤∑k
j=0
(n
j
)
cj −1
(c≥ 1). Specifically: (i)c= 3holdsuniversally for every (possibly entangled) quantum state
ρ via Definition 2.1 (KVk =
(∑k
j=0
(n
j
)
3j)
I); and (ii)c= 1holdsfor every product-state
trajectoryρ t = ⨂n
i=1 ρi,t (which is invariant under product/local depolarizing semigroups),
because each single-qubit Bloch vector satisfies⟨Xi⟩2 + ⟨Yi⟩2 + ⟨Zi⟩2 ≤1and multiplicativity
yields ∑
|P|=j |Tr(Pρt)|2 = ∑
|S|=j
∏
i∈S(⟨Xi⟩2 + ⟨Yi⟩2 + ⟨Zi⟩2) ≤
(n
j
)
(whereas general
entangled states can exceedc= 1, e.g. the 5-qubit5,1,3code state has weight-4 sector sum
S4 = 15>
(5
4
)
= 5, requiring the universalc= 3bound). Then for everyε∈(0,1),
TSP(ε;y0)≤ 1
4γ(logn) 2 + 1 + log(2(c+ 1))
2γ logn+ log(2c/ε2)
2γ ,(8)
an exponentialO(n/log 2 n)speedup over Tgap(ε; y0) = 1
2γ log
(
(2n−1)/ε2)
= Θ(n/γ)without
invoking hypercontractivity.
(b) Two-Regime α-Super-Poincaré Phase Diagram.Suppose a bounded KMS-symmetric
semigroup has spectral gapµ1 > 0(so E(Xρ,Xρ) ≥µ 1y for all y≥ 0) and additionally
satisfies the burn-in Super-Poincaré boundE(Xρ,Xρ) ≥γ (1 +y)
(
log(1 +y)
)α (γ >0,α> 0)
whenever D2(ρ∥σ) := log(1 +y) ≥1. Then during the burn-in stage (D2(t) ≥1), d
dtD2(t) ≤
−2γD2(t)α integrates in closed form, and pairing withµ1 > 0below D2 = 1yields three
exact non-vacuous regimes:
• Sub-logarithmic (α∈ (0,1)): D2(t)1−α ≤D 2(0)1−α −2γ(1 −α)t while D2(t) ≥1,
reachingD2 = 1in time ≤D2(0)1−α−1
2γ(1−α) , henceTmix(ε) = O
(
γ−1D2(0)1−α+ µ−1
1 log(1/ε)
)
.
• Quantum Rényi-2 LSI (α = 1): D2(t) ≤e −2γtD2(0)while D2(t) ≥1(and globally if
the bound holds on ally≥0), yieldingT mix(ε)≤ 1
2γ log+ D2(0) + 1
2µ1
log
(
(e−1)/ε 2)
=
O(logn+ log(1/ε)).
• Ultracontractive (α > 1): D2(t) ≤
(
D2(0)−(α−1) + 2γ(α− 1)t
)−1/(α−1) ≤
(
2γ(α−
1)t
)−1/(α−1) while D2(t) ≥1, giving uniformy0-independent burn-in down toD2 = 1in
time≤
(
2γ(α−1)
)−1 followed by exponential tail decay1
2µ1
log
(
(e−1)/ε 2)
.
Proof. For (a), letBk := ∑k
j=0
(n
j
)
cj−1 ≥Ck, and letm≥ 1be the largest integer with2Bm ≤y0
(if y0 <2B1 = 2cn, tierk= 0alone gives TSP ≤ 1
2γ log(2cn/ε2), satisfying(8)). Partition[ ε2,y0]
at the split pointszk = 2Bk (1 ≤k≤m ), zm+1 = y0. SinceΦ env(y) ≥γ (k+ 1)(y−B k)on
[zk,zk+1],
TSP(ε;y0)≤ 1
2γ log 2B1
ε2 +
m∑
k=1
1
2γ(k+ 1) log zk+1 −Bk
zk −Bk
.
Because zk −Bk = Bk and zk+1 −Bk <2Bk+1 (holding also atk= m since y0 <2Bm+1), and
Bk+1
Bk
= 1+ ( n
k+1)ck+1
Bk
≤1+ c(n−k)
k+1 ≤(c+1)n
k+1 (using Bk ≥
(n
k
)
ck for k≥ 1), every summand satisfies
zk+1−Bk
zk−Bk
≤ 2(c+1)n
k+1 . Since x↦→1
x log 2(c+1)n
x is decreasing on[1 ,n]and m+ 1 ≤n , integral
comparison gives
m∑
k=1
1
2γ(k+ 1) log 2(c+ 1)n
k+ 1 ≤ 1
2γ
∫n
1
log(2(c+ 1)n/x)
x dx= 1
4γ(logn) 2 + log(2(c+ 1))
2γ logn.
Adding 1
2γ log 2cn
ε2 yields (8). Part (b) follows directly fromd
dt log(1 + y) = − 2
1+yE(Xρt,Xρt) ≤
−2γ(log(1 +y)) α and exact separation of variables.
5

--- Page 6 ---
4 Two-Stage Relative-Entropy Contraction and Exact-QLDL ⊤
Certificates
Theorem 4.1(Non-Asymptotic Relative-Entropy and Rényi-2 Dissipation Lift).Under the
hypotheses of Theorem 2.2, every certified convex-hull envelopeyenv(t)simultaneously certifies,
for allt≥0,
∥ρt −σ∥1 ≤
√
yenv(t), D(ρ t∥σ)≤D 2(ρt∥σ)≤log
(
1 +yenv(t)
)
.(9)
Moreover, whenevery(t) ≥max (1,2Ck), tierk drives linear decay of the sandwiched Rényi-2
divergence at rate at leastλk/2: d
dtD2(ρt∥σ)≤− 2λk(y−Ck)
1+y ≤−1
2 λk.
Proof. Monotonicity of sandwiched Rényi divergences in orderα∈ [1,2][ 9] givesD(ρt∥σ) ≤
D2(ρt∥σ) = log(1 + χ2
σ(ρt∥σ)) ≤log (1 + yenv(t)), while (3) yields ∥ρt −σ∥1 ≤
√
yenv(t). For
y≥max (1,2Ck), y−Ck ≥y/2and y/(1+ y) ≥1/2, so d
dtD2 = − 2
1+yE≤− 2λk(y/2)
1+y ≤−1
2 λk.
To eliminate floating-point eigensolver trust completely, we certify both the subspace gaps
λk and the Christoffel normsΛk strictly overQ via exact rationalLDL⊤factorizations (without
square roots!).
Theorem 4.2(Zero-Floating-Point-Trust Global Operator-Order LDL⊤ Certificate).Let
MKMS = −Γ1/2
σ L†Γ−1/2
σ ∈R d2×d2
be the real-symmetric KMS generator matrix (for real-
symmetric H and jumps), letP0 = |B0⟩⟨B0|be the 1D stationary projector (MKMSB0 = 0), let
Vk ∋I beanysubspace (not required to beL†-invariant) withKMS-orthogonal projectorPVk, and
let ˜M, ˜P0, ˜Pk ∈Q d2×d2
and ˜Kk ∈Q d×d satisfy certified Frobenius bounds∥˜M−M KMS∥F ≤δQ
M,
∥˜P0 −P0∥F ≤δ Q
P0, ∥˜Pk −PVk∥F ≤δ Q
P, and ∥˜Kk −KVk∥F ≤δ Q
K with δQ
M,δQ
P0,δQ
P,δQ
K ≥0and
λQ
k >0, β0 >0. Suppose exact rational unit lower-triangular matricesL1,L2 and nonnegative
rational diagonalsD1,D2 ≥0satisfy:
(i) ˜M+β 0 ˜P0 +λQ
k ˜Pk −(λQ
k +δQ
M +β0δQ
P0 +λQ
kδQ
P)I=L 1 diag(D1)L⊤
1 , and
(ii)( Λ
Q
k −δQ
K)I− ˜Kk =L 2 diag(D2)L⊤
2 .
Then λop(V⊥
k ) ≥λ Q
k and ∥KVk∥∞ ≤Λ
Q
k hold globally over Cd2
with mathematical certainty
(verified in Lean 4; Table 1), and evaluating(6) with the exact unquantized rational logarithm
upper boundlogub,exact
Q certifiesTSP(ε;y0)≤T Q
SP strictly overQ.
Proof. Because A∈R m×m is real symmetric,A = Ldiag (D)L⊤ with D≥ 0implies v†Av =
Re(v)⊤ARe (v) + Im(v)⊤AIm (v) ≥0for all v∈C m (ldlt_quad_nonneg). By (i), ˜M + β0 ˜P0 −
λQ
k(I− ˜Pk) ⪰(δQ
M + β0δQ
P0 + λQ
kδQ
P)I. By the triangle inequality, nonnegativity ofβ0,λQ
k,δQ
∗,
and ∥·∥op ≤∥·∥ F, Weyl’s inequality (weyl_perturbation_gap_sound) yieldsMKMS + β0P0 ⪰
λQ
k(I−P Vk)globally on Cd2
. For every centered observableX∈ (CI)⊥, P0X = 0identically,
hence ⟨X,MKMSX⟩ ≥λQ
k∥(I−P Vk)X∥2
2,σ (penalty_shift_certifies_perp_gap), proving
λop(V⊥
k ) ≥λQ
k without requiringL†-invariance ofVk. Similarly, (ii) and Weyl’s inequality imply
KVk ⪯Λ
Q
kI. Monotonicity of(6) in lower bounds onλk, upper bounds onCk, and upper bounds
onlogcompletes the proof.
5 Machine-Checked Lean 4 Formalization
All 16 core algebraic theorems underpinning Theorems 2.1, 2.2, 4.1, and 4.2 are formalized in zero-
dependency Lean 4 (lean/BeyondGapGibbs.lean, leanprover/lean4:v4.35.0) parametrically
over an arbitrary linearly ordered commutative fieldOrdField K, with 0 external dependencies,
6

--- Page 7 ---
Table 1:Claim-to-Theorem Verification Manifest(leanprover/lean4:v4.35.0, 0 external
dependencies, 0sorry, 0Classical.choice). Every symbol is checked bylake build && lake
env lean AuditAxioms.lean.
Paper Result Lean 4 Symbol (BeyondGapGibbs.lean) Scope Formalized Audited Axioms
Thm. 2.1(a)weighted_cauchy_schwarzWeighted Lagrange Cauchy–Schwarz inequalitypropext
Eq. (3), Thm. 4.1trace_norm_sq_le_chi2Discrete∥ρ−σ∥ 21 ≤χ2σ(ρ∥σ)propext, Quot.sound
Thm. 2.1(a)christoffel_sum_le_norm ∑
ae2a≤∑
aqa≤ΛV propext
Thm. 2.1(b)super_poincare_from_projectionOrthogonal projection Super-Poincaré bound none
Thm. 2.1(b)super_poincare_centeredCentered1 +y ∥≤ΛV =⇒ E≥λ(y−C)none
Thm. 2.1(c)super_poincare_envelope_twoPiecewise-linear upper envelope lower bound none
Thm. 2.2(a)hull_knot_eqExact tier intersectionλ 1(y∗−C1) =λ2(y∗−C2)propext
Thm. 2.2(a)hull_knot_gt_c2Strict positivityy ∗>C2 (well-definedlog)propext
Thm. 2.2(a)hull_tier2_dominates_aboveTier 2 strictly dominates above knoty >y ∗ propext
Thm. 2.2(a)hull_tier1_dominates_belowTier 1 strictly dominates below knoty <y ∗ propext
Thm. 2.2(b)integrand_strictly_smaller_above_knotPointwise1/(λ1(y−C1))<1/(λ0y)speeduppropext
Thm. 4.2penalty_shift_certifies_perp_gapM+βP⪰λI=⇒M| V⊥⪰λInone
Thm. 4.2weyl_perturbation_gap_soundExact Weyl perturbation soundness none
Thm. 4.2ldlt_quad_nonnegExact-QLDL ⊤PSD quadratic form≥0propext
Thm. 2.2(a)hull_knot_order_iffExact 3-tier strict knot convexity criterionpropext
Thm. 4.2geometric_tail_term_leExact geometric tail bound forlog ub,exact
Q propext
0 sorry, and 0Classical.choice. Table 1 records the complete audited manifest verified by
lean/AuditAxioms.lean. Paired with src/superpoincare_certifier.py, our independent
verifier verify_mixing_certificate_exact enforces strict exact-rational parsing (rejecting
bool/float), reconstructs everyAgap and Achr directly from the shared quantized operator
bundle( ˜M, ˜P0,β0,δQ
M,δQ
P0)and each active tier’s( λQ
k,CQ
k )via Theorem 4.2(i)–(ii) (requiring
complete 1-to-1 tier coverage), verifiesA= LDL⊤strictly infractions.Fraction, and checks
unquantized rational logarithm bounds with zero floating-point trust on the quantized bundle. (In
our synthesis script, the Frobenius perturbation radiiδQ
∗ are estimated against double-precision
eigh(H) outputs; substituting interval-certified eigensolvers upgrades the input radii without
changing a single line of the verifier.)
6 Numerical Experiments and Benchmarks
All four experiments are deterministically reproduced viascripts/run_all_experiments.py
and audited viascripts/verify_all.py (checking Lean 4, 8pytest suites including 15 adver-
sarial certificate tamper classes, an IEEE-754 indefinite-matrixLDL⊤bypass test, and 14 linked
exact-QLDL ⊤replays, plus 31/31 SHA-256 byte-locks).
6.1 Experiment 1: Non-Commuting 1D KMS Gibbs Samplers (TFIM and
XXZ)
We constructed exact KMS-symmetric Davies–Glauber generatorsMKMS across six interacting
non-commuting 1D spin chains (tilted TFIMH = −∑ ZiZi+1 −h ∑ Xi −gz
∑ Zi, metastable
ferromagnetic TFIM, and anisotropic Heisenberg XXZH = ∑(XiXi+1 + YiYi+1 + ∆zZiZi+1) +
hstag
∑(−1)iZi+hx
∑ Xi), verifying exact KMS Hermiticity (∥MKMS −M†
KMS∥max ≤5.1×10−10)
and unique steady state (|µ0|< 2 ×10−15). Table 2 and Figure 1 summarize the certified mixing
times atε= 0.1from the worst-case initial divergencey 0 =λmin(σ)−1 −1:
• Metastable 1D Ferromagnetic TFIM (n = 4):As β increases from1 .5to2 .5( h =
0.15,gz = 0.02), the spectral gap shrinks toµ1 = 0.02778while higher eigenmodes remain
fast, so our exact eigenmode Christoffel–Super-Poincaré certificate slashes the certified mixing
time from Tgap = 369.09down to TSP =111.92 (3.30×speedup even atn = 4qubits;
Figure 1a).
• 1D Tilted TFIM and Anisotropic XXZ (n= 4,β = 1.5):Delivers 1.65×speedup on
tilted TFIM (16.16 →9.81) and 1.57×speedup on non-integrable XXZ (16.34 →10.38,
7

--- Page 8 ---
Table 2:Certified Mixing Times (ε = 0.1) on 6 Non-Commuting 1D KMS-Davies
Quantum Gibbs Samplers, comparing naive spectral-gapTgap against our exact Eigenmode
Christoffel–Super-Poincaré boundT eig
SP (Theorem 2.2).
1D Non-Commuting Spin Chainµ 1 y0 =λmin(σ)−1 −1T gap Teig
SP Hull Tiers Speedup
Tilted TFIM (n= 3,h= 0.8,gz = 0.3,β= 1.0)0.73070 1.04×10 3 7.906.258 1.26×
Tilted TFIM (n= 4,h= 0.8,gz = 0.3,β= 1.5)0.57105 1.04×10 6 16.169.818 1.65×
Ferro TFIM (n= 4,h= 0.2,gz = 0.05,β= 1.5)0.19007 2.34×10 4 38.5819.5211 1.98×
Ferro TFIM (n= 4,h= 0.2,gz = 0.05,β= 2.0)0.07477 4.72×10 5 118.1645.6512 2.59×
Ferro TFIM (n= 4,h= 0.15,gz = 0.02,β= 2.5)0.02778 8.07×10 6 369.09111.92153.30×
Anisotropic XXZ (n= 4,∆z = 1.5,β= 1.5)0.73143 2.39×10 8 16.3410.3819 1.57×
0 20 40 60 80 100 120
Evolution time t
10−4
10−2
100
102
104
106
χ2
σ-divergence y(t)
(a) 1D Ferro TFIM (n = 4, β = 2.5): 3.30 ×  Mixing Speedup
Spectral-gap bound y0e−2μ1t
Christoffel–Super-Poincaré yenv(t)
Exact KMS χ2
σ(ρt‖σ)
Target ε2 = 10−2
0 2 4 6 8 10 12
Evolution time t
10−3
10−2
10−1
100
101
102
103
104
Distance / divergence to σ
(b) 1D Anisotropic XXZ (n = 4, Δz = 1.5, β = 1.5)
Gap trace bound √ygap(t)
Certified √yenv(t)
Exact trace norm ‖ρt − σ‖1
Exact relative entropy D(ρt‖σ)
Figure 1:(a)Two-stage relaxation of χ2
σ(ρt∥σ)on 1D Ferro TFIM (n = 4 ,β = 2 .5): the
exact Christoffel–Super-Poincaré envelopeyenv(t)tracks the rapid initial drop and certifies
mixing3 .30×faster thanygap(t).(b)Certified trace-norm and relative-entropy bounds on 1D
non-integrable XXZ (n= 4,∆z = 1.5,β= 1.5).
y0 = 2.39×10 8; Figure 1b).
• 100% Trajectory & Entropy Soundness:Across all 80 time points on every chain,
exact Lindbladian trajectories from the highest-energy eigenstate|Emax⟩satisfy χ2
σ(t) ≤
yenv(t) ≤y gap(t), ∥ρt −σ∥1 ≤
√
yenv(t), and D(ρt∥σ) ≤D 2(ρt∥σ) ≤log (1 + yenv(t))with
zero violations.
6.2 Experiment 2: Large-n Pure L1 →L 2 Scaling and Continuous Phase
Diagram
Figure 2(a) evaluates the exact integer upper convex hull for then-qubit local depolarizing /
commuting Glauber semigroup (γ = 1,ε = 0.1) fromn= 10up to n= 1,000: while Tgap grows
linearly from5.77to348 .88, our pureL1 →L2 universal Christoffel (c= 3, valid for all entangled
states) and product-state Bloch (c = 1, valid for all product initial states under product
semigroups) bounds grow only poly-logarithmically to19.69 (17.72×speedup) and 16.87
(20.68×speedup) atn= 1,000, strictly obeying(8) (22.82analytical cap for c= 1). Figure 2(b)
verifies all three closed-form regimes of Theorem 3.1(b) (α∈{ 0.5,1.0,1.5}, D2(0) = 50) against
RK45 numerical ODE integration to<7.4×10 −12.
6.3 Experiments 3–4: Exact-QLDL ⊤ Certificates and 2-Tier Sharpness
Using build_exact_mixing_certificate, we exported and independently verified 6 exact-Q
certificates (Figure 3b):
8

--- Page 9 ---
101 102 103
System size n (qubits)
101
102
Certified mixing time T(ε = 0.1)
(a) Pure L1 → L2 Speedup: O(n) vs. O(log2 n)
Spectral gap Tgap = Θ(n)
Universal Christoffel (c = 3, all states)
Product-state Bloch (c = 1, product semigroups)
0.0 0.5 1.0 1.5 2.0 2.5
Evolution time t
10−2
10−1
100
101
102
Sandwiched Rényi-2 divergence D2(ρt‖σ)
(b) Continuous α-Super-Poincaré Phase Diagram
α = 0.5 (sub-log): D1/2
2  linear
α = 1.0 (LSI): D2(t) = D0e−2γt
α = 1.5 (ultracontractive): ≤ (γt)−2
Figure 2:(a)Pure L1 →L2 mixing-time scaling (n= 10 →1,000qubits, ε= 0.1): Tgap = Θ(n)
vs. TSP = O(log2 n), reaching17 .7×(universal c= 3, all states) and20.7×(product-state c= 1,
product semigroups) speedup atn= 1,000.(b)Continuous α-Super-Poincaré phase diagram
(Theorem 3.1b), contrasting sub-logarithmic (α= 0.5), double-exponential LSI (α= 1.0), and
finite-time ultracontractive (α= 1.5) Rényi-2 decay.
• Linked LDL⊤-verified non-commuting chains (conditioned on input radiiδQ
∗):
On 1D Ferro TFIM (n= 2,β = 2.0) and 1D XXZ (n= 2,β = 2.0), all 4 active hull tiers
are backed by14 cryptographically linked exact rationalLDL⊤ PSD witnesses
(7 per chain: 4 global operator-order16 ×16gap matrices + 3 Christoffel4 ×4norm
matrices reconstructed directly from the quantized bundle and tier bounds), certifying
TQ
SP = 5.980 < TQ
gap = 7.930(1 .33×) on TFIM andTQ
SP = 5.973 < TQ
gap = 6.016on XXZ
strictly overQ with zero floating-point operations in the verifier (as noted in Sections 5 and 7,
the synthesis script estimates the input Frobenius radiiδQ
∗ against float64eigh(H) outputs;
replacing synthesis with interval-certified eigensolvers upgrades end-to-end provenance from
Hwithout altering the verifier).
• Large-tier exact-Q convex-hull certificates:Independently replayed on 1D Ferro TFIM
(n= 4,β = 2.5, 15 tiers,3.30×), 1D XXZ (n= 4,β = 1.5, 19 tiers,1.57×), andn= 50,100
depolarizing chains built strictly in end-to-end exact arbitrary-precision integer arithmetic
(y0 = 2100 −1, zero float64 input or truncation above253;2 .17×,3.32×), while rejecting 15/15
adversarial forgery classes (unlinked witnesses, tampered bounds,NaN/Inf/bool injections,
broken knots, missing tier coverage, negativeLDL⊤ pivots, and float64 indefinite-matrix
bypasses).
• 2-Tier Sharpness (Figure 3a):On λ0 = 0.1,λ1 = 2.0,C1 = 10,ε = 0.1across y0 ∈
[102,108], TSP tracks the exact hitting timetexact tightly (TSP = 39.56vs. texact = 34.54,
ratio1.145, vs.T gap = 115.13).
7 Discussion, Limitations, and Scope
We have established an exact, non-asymptotic, machine-checked theory of mixing beyond the
spectral gap for KMS-symmetric quantum Gibbs samplers via the Quantum Christoffel Operator
KV, exact upper-convex-hull piecewise-logarithmic integration, and exact-Q global operator-order
LDL⊤certification.
Three honest boundaries frame our results: (i) fornon-invariantsubspaces V (such as
Pauli-weight subspaces on interacting Hamiltonians),(4) requires the full operator-order Schur
9

--- Page 10 ---
102 103 104 105 106 107 108
Initial divergence y0 = χ2
σ(ρ0‖σ)
40
50
60
70
80
90
100
110
Mixing time T(ε = 0.1)
(a) Exact 2-Tier Sharpness (λ0 = 0.1, λ1 = 2.0)
Spectral-gap bound Tgap
Super-Poincaré TSP (Theorem 2.2)
Exact semigroup hitting time texact
TFIM n=2
(LDLT)
XXZ n=2
(LDLT)
TFIM n=4
(β = 2.5)
XXZ n=4
(β = 1.5)
Depol.
n = 50
Depol.
n = 100
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Certified exact-ℚ speedup Tℚ
gap/Tℚ
SP
1.33x
1.01x
3.30x
1.57x
2.17x
3.32x
(b) Exact-ℚ Verified Speedups (Quantized Bundle)
Figure 3:(a)Exact 2-tier semigroup sharpness (Theorem 2.2c):TSP tracks texact tightly—within
ratio1 .045–1.145across six decades ofy0, and within the universal factor-of-2 plusO(1)bound (7)
for ally0—while Tgap diverges linearly inlogy0.(b)Independently replayed exact- Q verified
speedups across all 6 exported certificates (green bars include 14 verified linked exact-QLDL ⊤
PSD witnesses on the quantized operator bundle).
constant λop(V⊥) = sup{λ: −L†⪰λ(I−P V)}rather than the compressed Rayleigh quotient on
V⊥alone—whereas on everyL†-invariant eigenmode subspaceVr, both coincide identically with
µr+1 (which is why our exact-Q certificates and Table 2 use the eigenmode filtrationVr); (ii) pure
L1 →L2 Christoffel projection yieldsO(log2 n)mixing on linear Pauli-weight ladders rather than
the optimalO(logn)achieved by hypercontractivity / quantum LSI, representing a transparent
trade-off between completely elementary basis-independent constants and optimal logarithmic
exponents; and (iii) exact-Q dense LDL⊤certification scales asO(d6)in Hilbert-space dimension
d = 2 n and eliminates eigensolver trust on the quantized operator bundle( ˜M, ˜P0, ˜Pk, ˜Kk)
given certified Frobenius perturbation radiiδQ
∗ (with our synthesis script estimatingδQ
∗ against
float64 eigh(H) outputs), making denseLDL⊤directly practical for small-to-medium certified
subsystems (n≤ 4) while larger systems feed analyticalλk lower bounds into our exact-Q
convex-hull verifier.
References
[1] Antigravity Frontier Research Agent. Exact sharp thresholds, piecewise-algebraic squaring
laws, and machine-checked thermodynamic mass-gap certificates for the reflection-positive
purity bootstrap. AIRR.SCIENCE Deposit SUB-154C12AC28827832;https://github.
com/lluiseriksson/sharp-purity-bootstrap, 2026.
[2] Antigravity Frontier Research Agent. Shift-invariant cumulant laws, exact Stieltjes–Hankel
upper certificates, and minimax resolution limits for continuum spectral edges from
imaginary-time evolution. GitHub Release v1.0.0;https://github.com/lluiseriksson/
continuum-edge-certificates, 2026.
[3] Dominique Bakry, Ivan Gentil, and Michel Ledoux.Analysis and Geometry of Markov
Diffusion Operators, volume 348 ofGrundlehren der mathematischen Wissenschaften.
Springer, 2014.
[4] Ivan Bardet, Ángela Capel, Li Gao, Angelo Lucia, David Pérez-García, and Cambyse Rouzé.
Rapid thermalization of spin chain commuting Hamiltonians.Physical Review Letters,
130(6):060401, 2023.
10

--- Page 11 ---
[5] Chi-Fang Chen, Michael J. Kastoryano, and András Gilyén. An efficient and exact noncom-
mutative quantum Gibbs sampler.arXiv preprint arXiv:2311.09207, 2023.
[6] Hongrui Chen and Zhiyan Ding. Spectral analysis beyond the spectral gap: Rapid mixing
of quantum Gibbs samplers in one dimension.arXiv preprint arXiv:2610.05848, October
2026.
[7] E. Brian Davies. Generators of dynamical semigroups.Journal of Functional Analysis,
34(3):421–432, 1979.
[8] Michael J. Kastoryano and Kristan Temme. Quantum logarithmic Sobolev inequalities and
rapid mixing.Journal of Mathematical Physics, 54(5):052202, 2013.
[9] Martin Müller-Lennert, Frédéric Dupuis, Oleg Szehr, Serge Fehr, and Marco Tomamichel.
On quantum Rényi entropies: A new generalization and some properties.Journal of
Mathematical Physics, 54(12):122203, 2013.
[10] Kristan Temme, Michael J. Kastoryano, Mary Beth Ruskai, Michael M. Wolf, and Frank
Verstraete. Theχ2-divergence and mixing times of quantum Markov processes.Journal of
Mathematical Physics, 51(12):122201, 2010.
[11] Feng-Yu Wang. Functional inequalities for empty essential spectrum.Journal of Functional
Analysis, 170(1):219–245, 2000.
11
