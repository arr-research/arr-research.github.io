# Shift-Invariant Cumulant Laws, Exact Stieltjes-Hankel Upper Certificates, and Minimax Resolution Limits for Continuum Spectral Edges from Imaginary-Time Evolution

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-07TQHSTB0V8RQ90D` (v1)  
**Intake Receipt:** `SUB-F9BA19FD317EDE8C`  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/continuum-edge-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `5ad9f81ae15957930b0516dc99a5c0024c612d4f4ee012fc0c54f65d8f1811a3`

## Abstract

Extracting the spectral gap Delta = E_th - E_0 and continuum threshold exponent alpha > 0 of an infinite-dimensional quantum Hamiltonian from imaginary-time evolution (ITE) was recently placed on a rigorous asymptotic footing by Karapetyan, Bondar, Marecek, and Wodecki (arXiv:2611.06454). At finite imaginary time tau, however, the logarithmic decay rate g(tau) = -d/dtau log F(tau) = Delta + alpha/tau + O(tau^-2) suffers an O(alpha/tau) systematic bias that confounds Delta with alpha, offers no assumption-free finite-tau certificate, and degrades only logarithmically as O(1/log(1/sigma)) under additive shot noise sigma. We resolve all three bottlenecks with exact cumulant identities, zero-dependency Lean 4 formalizations, and zero-floating-point-trust exact-Q moment certificates. First, we prove an exact covariance-boundary identity for the variance-corrected estimator Delta_VF(tau) = g(tau) - tau*kappa_2(tau): for any continuum density w(x) = x^(alpha-1) e^(-V(x)) on (0, B), Delta_VF(tau) - Delta = tau^-2 Cov_{U_tau}(U_tau, U_tau V'(U_tau/tau)) + B_B(tau) with a nonnegative upper-edge boundary term B_B(tau) when B < infinity, yielding non-asymptotic one-sided bounds at every finite tau > 0 via Chebyshev's association inequality (plus an exact modified-Bessel crossover law for the 1D van Hove band). Second, we introduce the shift-invariant cumulant estimators Delta_SI(tau) = g(tau) - 2*kappa_2(tau)^2/kappa_3(tau) and alpha_SI(tau) = 4*kappa_2(tau)^3/kappa_3(tau)^2: both are identically exact on the three-parameter Gamma-Exponential family x^(alpha-1) e^(-lambda x), and on general smooth continuum edges an exact O(tau^-2) cancellation between 2*kappa_2^2 and kappa_3 delivers two-order bias reduction—Delta_SI(tau) - Delta = c_2 alpha(alpha+1)/(tau+lambda)^3 + O(tau^-4) and alpha_SI(tau) - alpha = -3 c_2 alpha(alpha+1)/(tau+lambda)^2 + O(tau^-3)—where c_2 = (log phi)''(0) is the edge log-curvature. Third, we prove a spectral-edge trichotomy showing that tau^2 kappa_2(tau) uniquely classifies discrete excited states (-> 0 exponentially), power-law continua (-> alpha), and stretched-exponential pseudogaps (~ tau^(gamma/(gamma+1)) -> +infinity). Fourth, without any smoothness or monotonicity assumption, we derive interval-sound Stieltjes-Hankel upper certificates witnessed by rational vectors v in Q^(n+1) and verified strictly over Q (including exact unquantized rational logarithm upper bounds). Fifth, we establish poly-logarithmic additive-noise minimax resolution limits Omega((log(sqrt(K)/sigma))^-3) for Delta and Omega((log(sqrt(K)/sigma))^-2) for alpha in the asymptotic window via an explicit closed-form Le Cam two-point construction. All 16 core algebraic theorems are formalized in zero-dependency Lean 4 (v4.35.0, 0 sorry, 0 Classical.choice), and validated on 1D/3D one-center point interactions (267x-397x gap accuracy gain at tau=20), L=401 tight-binding impurity exact diagonalization (169x gain), 1D van Hove bands (7,630x gain), 6 exact-Q Hankel certificates (2.35x tighter than raw g(tau_max) with 200/200 noisy interval soundness), and additive shot-noise scaling.

## Full Extracted Text

--- Page 1 ---
Shift-Invariant Cumulant Laws, Exact
Stieltjes–Hankel Upper Certificates, and Minimax
Resolution Limits for Continuum Spectral Edges from
Imaginary-Time Evolution
Lluis Eriksson∗
November 24, 2026
Abstract
Extracting the spectral gap∆ = Eth −E0 and continuum threshold exponentα >0
of an infinite-dimensional quantum Hamiltonian from imaginary-time evolution (ITE) was
recently placed on a rigorous asymptotic footing by Karapetyan, Bondar, Mareček, and
Wodecki [6]. At finite imaginary time τ, however, the logarithmic decay rate g(τ) =
−∂τ logF(τ) = ∆ + α/τ + O(τ−2)suffers an O(α/τ)systematic bias that confounds∆
with α, offers no assumption-free finite-τ certificate, and degrades only logarithmically as
O(1/log (1/σ))under additive shot noise σ. We resolve all three bottlenecks with exact
cumulant identities, zero-dependency Lean 4 formalizations, and zero-floating-point-trust
exact-Q moment certificates. First, we prove an exact covariance–boundary identity for
the variance-corrected estimator ˆ∆VF(τ) := g(τ) −τκ 2(τ): for any continuum density
w(x) = xα−1e−V(x) on(0 ,B), ˆ∆VF(τ)−∆ = τ−2 CovUτ (Uτ,UτV′(Uτ/τ))plus a nonnegative
upper-edge boundary term whenB <∞, yielding non-asymptotic one-sided bounds at every
finite τ >0via Chebyshev’s association inequality. Second, we introduce theshift-invariant
cumulant estimators ˆ∆SI(τ) := g(τ) −2κ2(τ)2/κ3(τ)and ˆαSI(τ) := 4κ2(τ)3/κ3(τ)2: both
are identically exact on the three-parameter Gamma–Exponential familyxα−1e−λx, and on
general smooth continuum edges an exactO(τ−2)cancellation between2 κ2
2 and κ3 delivers
two-order bias reduction—ˆ∆SI(τ) −∆ = c2α(α+ 1)/(τ + λ)3 + O(τ−4)and ˆαSI(τ) −α =
−3c2α(α+ 1)/(τ + λ)2 + O(τ−3)—where c2 = (logϕ)′′(0)is the edge log-curvature. Third,
we prove a spectral-edge trichotomy showing thatτ2κ2(τ)uniquely classifies discrete excited
states (→0exponentially), power-law continua (→α), and stretched-exponential pseudogaps
(∼τ γ/(γ+1) →+∞). Fourth, without any smoothness or monotonicity assumption, we derive
interval-sound Stieltjes–Hankel upper certificates witnessed by rational vectorsv∈Q n+1
and verified strictly overQ (including exact rational logarithm upper bounds). Fifth, we
establish poly-logarithmic additive-noise minimax resolution limits in the asymptotic window
via an explicit closed-form Le Cam two-point construction. All 16 core algebraic theorems
are formalized in zero-dependency Lean 4 (v4.35.0, 0sorry, 0Classical.choice), and
validated on 1D/3D one-center point interactions (267×–397×gap accuracy gain atτ = 20),
L = 401tight-binding impurity exact diagonalization (169 ×gain), 1D van Hove bands
(7,630×gain), 6 exact-Q Hankel certificates (2.35×tighter than rawg(τmax)with 200/200
noisy interval soundness), and additive shot-noise scaling.
1 Introduction
In infinite-dimensional quantum mechanics and thermodynamic-limit many-body systems, the
ground-state energyE0 is typically separated by a spectral gap∆ =Eth −E0 > 0from the
∗Independent researcher (Sweden). Research, zero-dependency Lean 4 proofs, exact- Q Stieltjes–Hankel
certificate verifiers, and numerical benchmarks prepared with AI assistance (Google Antigravity) and publicly
archived athttps://github.com/lluiseriksson/continuum-edge-certificates.
1

--- Page 2 ---
bottom edgeEth of a continuous scattering or quasiparticle spectrum [9, 2]. Imaginary-time
evolution (ITE)—implemented via quantum imaginary-time evolution (QITE) [8], quantum
Monte Carlo, or tensor networks—projects an initial stateψ0 onto the ground state, yet extracting
excitations aboveE0 is far subtler when the first excitation is a continuum edge rather than an
isolated eigenvalue.
In a landmark recent paper, Karapetyan, Bondar, Mareček, and Wodecki [6] developed a
rigorous mathematical framework showing that the excited imaginary-time decay function
F(τ) =
∫∞
∆
e−τω dν(ω) =e −τ∆
∫∞
0
e−τx w(x)dx(1)
(arising from the ground-state-subtracted survival amplitude or connected observable correlation
along ITE) detects the continuum edge∆whenever the spectral density obeys a power laww(x) ∼
cxα−1 (α> 0) nearx= 0+, producing a logarithmic correctionlogF(τ) = −τ∆ −αlogτ + O(1)
whose coefficient encodes the threshold exponentα.
Three fundamental challenges remain open for finite-τ, finite-sample, and certified applica-
tions:
1. Finite-τ Bias and(∆ ,α)Confounding.The raw logarithmic decay rate g(τ) :=
−d
dτ logF(τ) = ∆ + α
τ + O(τ−2)has an O(1/τ)bias that decays painfully slowly and
entangles∆with the unknown exponent α (e.g., atτ = 20on the 1D point interaction with
∆ = 1,α= 3/2,g(20)still errs by+7.2%).
2. Non-Asymptotic Certificates Without Distributional Assumptions.Asymptotic
Watson-lemma expansions [5] do not certify strict bounds on∆at finite τ, nor do they
distinguish power-law continuum edges from isolated discrete levels or pseudogaps without
prior spectral knowledge.
3. ExponentialSignalDecayUnderAdditiveShotNoise.Because F(τ) ∼c Γ(α)τ−αe−τ∆
vanishes exponentially inτ, any additive measurement noiseσ imposes a hard horizon
τmax = O(∆−1 log(1/σ)), trapping O(τ−1)estimators at a sluggish O(1/log (1/σ))error
floor.
Summary of Contributions.We resolve all three challenges and build a complete machine-
checked verification pipeline (complementing our recent finite-sample QC-QMC [4] and reflection-
positive purity-bootstrap [3] certificates):
• Cumulant–Covariance Identity & Chebyshev Sign Law (Theorem 2.1):Expresses
ˆ∆VF(τ) −∆as an exact scaled covariance, yielding non-asymptotic upper or lower bounds
ateveryfiniteτ >0determined solely by the monotonicity ofxV ′(x).
• Shift-Invariant Cumulant Estimators & ExactO(τ−2)Cancellation (Theorem 2.3):
Introduces ˆ∆SI(τ) = g−2κ2
2/κ3 and ˆαSI(τ) = 4κ3
2/κ2
3, provingexactinvarianceontheGamma–
Exponential family and exact leading errorsc2α(α+ 1)/(τ+ λ)3 and −3c2α(α+ 1)/(τ+ λ)2
on general smooth continuum edges.
• Spectral-Edge Trichotomy (Theorem 3.1):Proves that τ2κ2(τ)cleanly separates
discrete excited levels (→0), power-law continuum edges (→α), and stretched-exponential
pseudogaps (∼τγ/(γ+1) →+∞).
• Zero-Float-Trust Exact-Q Stieltjes–Hankel Certificates (Theorem 4.1):Derives
interval-sound rational witness vectorsv∈Q n+1 certifying∆ <∆Q
ub strictly overQ (including
exact rational logarithm upper bounds) foranypositive spectral measure.
• Additive-Noise Minimax Resolution Limits (Theorem 5.1):Establishes poly-
logarithmic minimax rates via Le Cam’s two-point method and documents both the
O((log(1/σ))−3)speedup and the honest finite-noise bias–variance crossover.
2

--- Page 3 ---
• Zero-Dependency Lean 4 Formalization & Physical Benchmarks (Sections 6–
7):Formalizes all 16 core algebraic theorems in Table 1 in Lean 4 (v4.35.0, 0sorry, 0
Classical.choice) and validates across 1D/3D point interactions,L= 401tight-binding
impurity ED, 1D/2D band continua, 6 exact-Q Hankel certificates, and Monte Carlo shot
noise.
2 Cumulant–Covariance Identity and Shift-Invariant Estimators
Let F(τ) =
∫∞
∆ e−τω dν(ω) >0for τ >0be the Laplace transform of a nonzero positive excited
spectral measureν supported on[∆ ,∞)with∆ = inf supp(ν). Let Xτ denote the exponentially
tilted random variable on[0,∞)with probability law
dPτ(x) = e−τx dν(∆ +x)∫∞
0 e−τy dν(∆ +y) .
The first three cumulants of the shifted energyω= ∆ + Xτ are given directly by logarithmic
derivatives ofF(τ):
g(τ) :=− d
dτ logF(τ) = ∆ +E[X τ], κ 2(τ) := d2
dτ2 logF(τ) = Var(X τ),
κ3(τ) :=− d3
dτ3 logF(τ) =E
[
(Xτ −E[Xτ])3]
.(2)
2.1 Exact Cumulant–Covariance Identity and Non-Asymptotic Sign Law
Define thevariance-free(Richardson-corrected) gap estimator and dimensionless cumulant
exponent:
ˆ∆VF(τ) :=g(τ)−τκ 2(τ), ˆαVF(τ) :=τ 2 κ2(τ).(3)
Theorem 2.1(Exact Cumulant–Covariance Identity and Chebyshev Sign Law).Suppose
dν(∆ + x) = cxα−1e−V(x) dx on(0 ,B)( B∈ (0,∞], α > 0, c > 0) with ϕ(x) := e−V(x) ,
V∈C 1((0,B)), x(1 + x)|V′(x)| ∈L1(dPτ′)for τ′ in a neighborhood of τ (with a locally
integrable dominating function justifying Leibniz differentiation), and either (i)B = ∞with
xαϕ(x)e−τx →0as x→∞ , or (ii)B <∞with finite upper-edge limitϕ(B−) ∈[0,∞). Let
Uτ :=τX τ andZ(τ) :=
∫B
0 xα−1ϕ(x)e−τx dx. Then foreveryτ >0:
ˆ∆VF(τ)−∆ = d
dτ
(
τE[Xτ]
)
= 1
τ2 Cov
(
Uτ, UτV′(Uτ/τ)
)
+B B(τ),(4)
where the upper-edge boundary termBB(τ) := Bαϕ(B−)e−τB
Z(τ) (B−E [Xτ])vanishes identically if
B = ∞or ϕ(B−) = 0, and satisfiesBB(τ) >0whenever B <∞and ϕ(B−) >0. Consequently,
by Chebyshev’s association inequality (formalized in discrete form in Lean 4; Table 1):
(a) If x↦→xV′(x)is nondecreasing on(0 ,B)(which holds for every nonincreasing log-concave
ϕ, every compact linear stepϕ(x) = 1 −x/B , and every power-law/Lorentzian decay
ϕ(x) = (x+ κ2)−γ with γ >0), then ˆ∆VF(τ) ≥∆forall τ >0(for both B = ∞and finite
B <∞).
(b) If B = ∞(or ϕ(B−) = 0) andx↦→xV′(x)is nonincreasing on(0 ,B)(e.g., an algebraically
growing threshold envelopeϕ(x) = (1 + x/a)γ with γ >0, wherexV′(x) = −γx
x+a), then
ˆ∆VF(τ)≤∆forallτ >0.
(c) On the Gamma–Exponential familyV(x) = λx(B = ∞), (4) evaluates explicitly toˆ∆VF(τ)−
∆ = αλ
(τ+λ)2 (Lean:gamma_exp_vf_excess).
3

--- Page 4 ---
Proof. Since −d
dτE[Xτ] = Var(Xτ) = κ2(τ), the product rule givesˆ∆VF(τ) −∆ = E[Xτ] −
τκ2(τ) = d
dτ(τE[Xτ]). Changing variables tou=τxyields
τE[Xτ] = N(τ)
D(τ) :=
∫τB
0 uαe−uϕ(u/τ)du
∫τB
0 uα−1e−uϕ(u/τ)du
, D(τ) =τ αZ(τ).
Differentiating under the integral sign via Leibniz’s rule (using∂τϕ(u/τ) = τ−2uV′(u/τ)ϕ(u/τ)
and upper-limit derivative d
dτ(τB) =BwhenB <∞) yields
d
dτ
(
τE[Xτ]
)
= 1
τ2
(
E
[
Uτ ·UτV′(Uτ/τ)
]
−E[Uτ]E
[
UτV′(Uτ/τ)
])
+ B(τB) α−1e−τBϕ(B−)
D(τ)
(
τB−τE[X τ]
)
= 1
τ2 Cov
(
Uτ, UτV′(Uτ/τ)
)
+BB(τ).
Since Xτ <B almost surely whenB <∞, BB(τ) ≥0always (and BB = 0if B = ∞or ϕ(B−) =
0). Parts (a) and (b) then follow from Chebyshev’s association inequality:Cov(f(U),g(U)) =
1
2 E[(f(U)−f(U′))(g(U)−g(U′))] ≥0(resp. ≤0) whenf,g are comonotone (resp. anti-monotone).
For part (c),V′(x) =λandB=∞giveτ −2 Cov(Uτ,λUτ) =λVar(X τ) = αλ
(τ+λ)2 .
Remark 2.2(Upper-Edge Singularities and the 1D van Hove Band).For the 1D tight-binding
van Hove densityw(x) = [ x(B−x )]−1/2 (α = 1 /2, ϕ(x) = ( B−x )−1/2), the upper-edge
van Hove singularity violatesϕ(B−) <∞ and x|V′|∈L 1(dPτ), yet the Laplace transform
evaluates in closed form via the modified Bessel functionI0: F(τ) = πe−τ(∆+B/2) I0(τB/2),
giving τE[Xτ] = z(1 −I1(z)/I0(z))with z := τB/2. Differentiating directly withI′
0 = I1 and
I′
1 =I0 −I1/zgives the exact law
ˆ∆VF(τ)−∆ = B
2
[
1−z+z I1(z)2
I0(z)2
]
z=τB/2
,
which changes sign at the unique positive rootz∗≈1.7024(so ˆ∆VF(τ) >∆at tiny τ <2z∗/B
where the upper band edge dominates, andˆ∆VF(τ) <∆strictly for all τ >2z∗/B, matching
the decreasing slopexV′(x) = − x
2(B−x) throughout the scaling regimeτ≥ 1when B = 4, since
2z∗/4≈0.8512).
2.2 Shift-Invariant Cumulant Estimators and ExactO(τ−2)Cancellation
Although ˆ∆VF(τ)improves the error from O(τ−1)to O(τ−2), Theorem 2.1(c) reveals why a
residual O(τ−2)bias persists: any exponential envelopee−λx shifts τ↦→s:= τ+λin the Gamma
moments, breaking scale homogeneity inτ. Eliminating the unknown shiftλ algebraically using
the third cumulantκ3(τ)yields ourshift-invariantcontinuum-edge and threshold-exponent
estimators:
ˆ∆SI(τ) :=g(τ)− 2κ2(τ)2
κ3(τ) , ˆαSI(τ) := 4κ2(τ)3
κ3(τ)2 .(5)
Theorem 2.3(Shift-Invariant Exactness and Two-Order Bias Cancellation).Supposedν(∆ +
x) = cxα−1ϕ(x) dx on(0 ,B)with α> 0, ϕ(0) >0,
∫B
0 xα−1ϕ(x)e−τ0xdx<∞ for someτ0 >0,
and ϕ smooth near0 + so that log(ϕ(x)/ϕ(0)) = −λx+ 1
2 c2x2 + O(x3)as x→ 0+, where
c2 = (logϕ) ′′(0)is the continuum-edge log-curvature. Lets=τ+λ. Then:
(a) Exactness on the 3-Parameter Gamma–Exponential Family.Wheneverϕ(x) =
ϕ(0)e−λx (c2 = 0, B = ∞), ˆ∆SI(τ) = ∆and ˆαSI(τ) = α holdidentically for every τ >0,
for allα>0andλ≥0(Lean:gamma_exp_si_gap_exact,gamma_exp_si_alpha_exact).
4

--- Page 5 ---
(b) Exact O(τ−3)and O(τ−2)Leading-Error Laws.As τ→∞ , the O(c2s−2)correc-
tions in2 κ2(τ)2 and κ3(τ)cancel identically (Lean: si_perturbation_cancellation,
si_alpha_perturbation_exact), yielding
ˆ∆SI(τ)−∆ = c2 α(α+ 1)
(τ+λ) 3 +O(τ −4), ˆαSI(τ)−α=− 3c2 α(α+ 1)
(τ+λ) 2 +O(τ −3).(6)
In particular, locally log-convex edges (c2 >0, such as 1D/3D point interactions and 1D
van Hove bands) satisfyˆ∆SI(τ) >∆and ˆαSI(τ) <α at largeτ, whereas locally log-concave
edges (c2 <0, such as 2D linear steps) satisfyˆ∆SI(τ)<∆and ˆαSI(τ)>α.
Proof. For part (a),F(τ) = cϕ(0)Γ(α)s−αe−τ∆ gives g= ∆ + α/s, κ2 = α/s2, κ3 = 2α/s3, so
2κ2
2/κ3 = (2α2/s4)/(2α/s3) =α/sand4κ 3
2/κ2
3 = (4α3/s6)/(4α2/s6) =αidentically.
For part (b), applying Watson’s lemma [5] directly to each of the four shifted Laplace moment
integralsmr(τ) =
∫B
0 xα+r−1e−sx(
1 + 1
2 c2x2 +O(x3)
)
dx(r= 0,1,2,3, withs=τ+λ) yields
mr(τ) = Γ(α+r)
sα+r
(
1 + c2 (α+r)(α+r+ 1)
2s2 +O(s−3)
)
(r= 0,1,2,3).
Forming the exact moment ratiosµr = mr/m0 and cumulantsg= ∆ + µ1, κ2 = µ2 −µ2
1, and
κ3 = µ3 −3µ1µ2 + 2µ3
1 (without term-by-term differentiation of asymptotic remainders) and
settingε :=c2(α+ 1)/s2 gives
g(τ) = ∆ + α
s(1 +ε) +O(s−4), κ 2(τ) = α
s2 (1 + 3ε) +O(s−5), κ 3(τ) = 2α
s3 (1 + 6ε) +O(s−6).
Crucially, by the exact rational identity proved in Lean 4 (si_perturbation_cancellation),
(1 + 3ε)2
1 + 6ε = 1 + 9ε2
1 + 6ε = 1 +O(s −4),
so2 κ2(τ)2/κ3(τ) = α
s + O(s−4)haszero O(c2s−3)correction! Subtracting from g(τ) = ∆ +
α
s + αε
s + O(s−4)immediately leaves ˆ∆SI(τ) −∆ = αε/s+ O(s−4) = c2α(α+ 1)/s3 + O(s−4).
Similarly, bysi_alpha_perturbation_exact,
(1 + 3ε)3
(1 + 6ε)2 = 1−3ε+ 27ε2 + 135ε3
(1 + 6ε)2 = 1−3ε+O(s −4),
giving ˆαSI(τ) =α(1−3ε) +O(s −3) =α−3c 2α(α+ 1)/s2 +O(s−3).
3 Spectral-Edge Trichotomy via Cumulant Invariants
Before trusting an asymptotic continuum-edge estimate, one must know whether the first
excitation above E0 is an isolated discrete eigenvalue, a power-law continuum edge, or an
exponentially suppressed pseudogap (where [6]’s power-law assumption fails). The dimensionless
cumulant ˆαVF(τ) =τ 2κ2(τ)cleanly classifies all three regimes.
Theorem 3.1(Spectral-Edge Trichotomy).Let ν be a positive excited spectral measure with
∆ = inf supp(ν). Asτ→∞:
(i) Isolated Discrete Excited State:Ifν = w1δ∆ +˜νwith w1 >0and supp(˜ν) ⊂[∆+δ21,∞)
(δ21 >0), then ˆαVF(τ) =O(τ 2e−τδ21)→0exponentially fast.
(ii) Power-Law Continuum Edge:If dν(∆ + x) = cxα−1ϕ(x) dx (α >0, ϕ smooth with
ϕ(0)>0), then ˆαVF(τ) =α+O(τ −1)→α, while ˆαSI(τ) =α+O(τ −2).
5

--- Page 6 ---
(iii) Stretched-Exponential Pseudogap:If dν(∆ + x) = exp(−cx−γ) ϕ(x) dx near0 + with
c> 0,γ >0and smooth ϕ(0) >0, then Laplace saddle-point asymptotics aroundx∗(τ) =
(cγ/τ) 1/(γ+1) yield
ˆαVF(τ) =τ 2κ2(τ)∼ (cγ)1/(γ+1)
γ+ 1 τ
γ
γ+1 −→+∞.(7)
Proof. In case (i), writingZ(τ) = w1 +
∫∞
δ21 e−τxd˜ν(∆ + x) = w1 + O(e−τδ21)gives E[Xτ] =
O(e−τδ21)and Var(Xτ) ≤E [X2
τ] = O(e−τδ21), soτ2κ2(τ) = O(τ2e−τδ21) →0. Case (ii) follows
directly from Theorem 2.3. For case (iii), the exponentΦτ(x) := τx+ cx−γ has unique minimizer
x∗ = ( cγ/τ)1/(γ+1) →0+ with curvatureΦ ′′
τ(x∗) = cγ(γ + 1)x−(γ+2)
∗ = ( γ + 1)τ/x∗. Since
Φ′′′
τ (x∗)/(Φ′′
τ(x∗))3/2 =O(τ − γ
2(γ+1) )→0, Laplace’s method [5] establishes asymptotic normality
of Xτ around x∗ with variance κ2(τ) ∼1/Φ′′
τ(x∗) = x∗/((γ + 1)τ), and multiplying byτ2
gives (7).
4 Assumption-Free Exact-Q Stieltjes–Hankel Upper Certificates
We now dropallsmoothness, power-law, and monotonicity hypotheses on the spectral measure
ν. Suppose we observeF(τ)on a uniform imaginary-time gridτk = τ0 + kδ (k= 0,1,..., 2n+ 1,
δ >0) with certified finite-sample interval enclosures
0≤m −
k ≤m k :=F(τ 0 +kδ)≤m +
k (k= 0,...,2n+ 1).(8)
Setting z= e−δω ∈[0,e−δ∆]and d˜ν(z) = e−τ0ωdν(ω)transforms the grid values into an exact
Stieltjes–Hausdorff moment sequence [1, 10]:
mk =
∫e−δ∆
0
zkd˜ν(z), k= 0,...,2n+ 1.
For any witness vectorv = (v0,...,v n) ∈Q n+1, define the exact rational sign-split interval
quadratic forms
Qub
0 (v) :=
n∑
i,j=0
{
vivj m+
i+j vivj ≥0,
vivj m−
i+j vivj <0, Qlb
1 (v) :=
n∑
i,j=0
{
vivj m−
i+j+1 vivj ≥0,
vivj m+
i+j+1 vivj <0. (9)
Theorem 4.1(Assumption-Free Exact-Q Stieltjes–Hankel Upper Certificate).Let ν beany
nonzero positive spectral measure supported on[∆,∞)(discrete, continuous, or mixed) whose
grid moments satisfy(8) (with probability at least1−α). Suppose there existu0 ∈Q∩ (0,1)
andv∈Q n+1 such that the exact rational inequality
u0 Qub
0 (v)−Q lb
1 (v)<0(10)
holds. Thensupp(˜ν)̸⊂[0,u 0], hencee−δ∆ >u0 and
∆< 1
δlog
(1
u0
)
≤∆ Q
ub := 1
δlogub
Q
(1
u0
)
(11)
(with probability at least1 −α), wherelogub
Q (x) ∈Q is the exact rational strict upper bound
obtained by binary range reductionx = 2 kr (r∈ [1,2)) and the geometric tail enclosure
2 ∑M−1
j=0
t2j+1
2j+1 + 2t2M+1
(2M+1)(1−t2) >log( 1+t
1−t)fort= (r−1)/(r+ 1)∈[0,1/3).
6

--- Page 7 ---
Proof. Write Pv(z) = ∑n
i=0 vizi. If supp(˜ν) ⊂[0,u0], then the shifted Hankel quadratic form
satisfies
u0 v⊤M0v−v ⊤M1v=
∫u0
0
(u0 −z)P v(z)2 d˜ν(z)≥0
(formalized in Lean 4 asshifted_hankel_psd). By sign-splitting(9) (Lean: interval_term_
upper_bound), we havev⊤M0v≤Q ub
0 (v)and Qlb
1 (v) ≤v⊤M1v, sou0 ≥0implies u0 v⊤M0v−
v⊤M1v≤u 0 Qub
0 (v) −Qlb
1 (v) < 0(Lean: interval_hankel_witness_sound), contradicting
support in[0 ,u0]( hankel_witness_refutes_support). Therefore e−δ∆ > u0, i.e.,∆ <
δ−1 log(1/u0). Finally, for every t∈ [0,1/3), the omitted tail Stail = ∑
j≥M
t2j+1
2j+1 satisfies
Stail ≤t2M+1
2M+1 + t2Stail, sogeometric_tail_term_le gives Stail ≤ t2M+1
(2M+1)(1−t2) , certifying (11)
strictly overQwith zero floating-point trust.
Notice thatn= 0,v = [1]recovers the elementary two-point bound∆ <δ −1 log(m+
0 /m−
1 )
(two_point_hankel_special_case), whereas increasing n = 1 ,..., 5atfixedsmall τ0 = 1
tightens∆ Q
ub dramatically—beating even the raw instantaneous log-derivativeg(τmax)at the
largest grid timeτmax =τ0 + (2n+ 1)δwhile making zero assumptions ondν!
5 Finite-Sample Additive-Noise Minimax Resolution Limits
In realistic quantum or Monte Carlo imaginary-time protocols, one observesˆF(τj) = F(τj) + εj
with independent additive noiseεj ∼N(0,σ2)(e.g., σ = M−1/2 from M measurement shots)
on a finite set of timesτj. Because F(τ) = Θ(τ−αe−τ∆ )decays exponentially while unknown
high-energy continuum structure only becomes negligible at largeτ, any estimator operating in
the asymptotic imaginary-time window faces a fundamental poly-logarithmic resolution barrier.
Theorem 5.1(Poly-Logarithmic Minimax Resolution Limits under Additive Shot Noise).Fix
∆0 >0, α0 >0, andC >0, and consider the classF2(∆0,α0,C)of smooth continuum densities
w(x) = cxα−1ϕ(x)on(0 ,∞)with∆ ∈[∆0/2,2∆0], α∈ [α0/2,2α0], ϕ(0) = 1, and edge
log-derivatives |λ|,|c2|≤C , observed atK≥ 1imaginary times τ1,...,τ K under independent
additive Gaussian noiseN(0,σ 2)as the effective signal-to-noise ratioSNReff :=
√
K/σ→∞.
(a) Asymptotic-Window Le Cam Lower Bound.LetW >0be any fixed half-width, and
suppose theK observations lie in an asymptotic-regime window[τc−W,τc+ W]centered at
τc ≥τeff := 1
∆0
log
(√
K
σ
)
−α0+6
∆0
log log
(√
K
σ
)
. Then any estimator( ˆ∆,ˆα)obeys the minimax
lower bounds (with implicit constants depending on∆0,α0,C,W)
inf
ˆ∆
sup
F∈F2
E
⏐⏐ˆ∆−∆(F)
⏐⏐= Ω
(
1
(
log(
√
K/σ)
)3
)
,
inf
ˆα
sup
F∈F2
E
⏐⏐ˆα−α(F)
⏐⏐= Ω
(
1
(
log(
√
K/σ)
)2
)
.(12)
(b) Optimal-Horizon Upper Bounds.Evaluating the 5-point discrete finite-difference
estimators at steph = Θ(1)and optimal horizon τ∗(σ) = 1
∆ log(1/σ) −O(log log(1/σ))
yields bias–variance balanced RMSE rates:
RMSE(ˆgraw) =O
( 1
log(1/σ)
)
,RMSE( ˆ∆VF) =O
( 1
(log(1/σ))2
)
,
RMSE( ˆ∆SI) =O
( 1
(log(1/σ))3
)
,RMSE( ˆαSI) =O
( 1
(log(1/σ))2
)
,
matching the asymptotic-window lower bounds(12)up to constant factors at fixedK.
7

--- Page 8 ---
Proof.For (a), consider two exhaustive regimes for the window centerτc ≥τeff:
Case 1: τc ∈[τeff,2τeff].Fix an explicit positiveC2-curved densityw1(x) = c1xα1−1e−λ1x(1 +
1
2 c2x2)with∆ 1 = ∆0, α1 = α0, λ1 = C/4, c1 >0, andc2 ∈(0,C/2]sufficiently small (chosen
below). Its Laplace transform is closed-form exact for allτ >0:
F1(τ) =c 1Γ(α1)(τ+λ 1)−α1e−τ∆1
(
1 + c2 α1(α1 + 1)
2(τ+λ 1)2
)
.
Set s1 := τc + λ1 = Θ(τeff). Now define the Gamma–Exponential partnerF0(τ) = c0Γ(α′
0)(τ +
λ0)−α′
0e−τ∆′
0 (c2 = 0)explicitlyby solving the four-equation cumulant-matching system atτc:
∆′
0 := ˆ∆SI(F1;τc), α ′
0 := ˆαSI(F1;τc), λ 0 := 2κ2,1(τc)
κ3,1(τc) −τc,
and choosingc0 >0so that F0(τc) = F1(τc). By direct substitution into the Gamma–Exponential
cumulants g0 = ∆′
0 + α′
0/(τc + λ0), κ2,0 = α′
0/(τc + λ0)2, and κ3,0 = 2α′
0/(τc + λ0)3, h(τ) :=
logF1(τ) −logF0(τ)vanishes identically to third order atτc: h(τc) = h′(τc) = h′′(τc) = h′′′(τc) =
0. By Theorem 2.3(b),
∆′
0 −∆ 1 = c2 α1(α1 + 1)
s3
1
+O(s−4
1 ), α ′
0 −α1 =− 3c2 α1(α1 + 1)
s2
1
+O(s−3
1 ),
and λ1 −λ0 = 3c2(α1 + 1)s−1
1 + O(s−2
1 ), so F0 ∈F2(∆0,α0,C)for sufficiently large SNReff.
Moreover,h(4)(τ) = 6c2α1(α1 +1)s−6
1 +O(s−7
1 )uniformly on[ τc−W,τc+W], so Taylor’s theorem
gives|h(τ)|≤C 4c2W4s−6
1 and hence
max
1≤j≤K
|F1(τj)−F 0(τj)| ≤2F1(τc −W)· C4c2W4
s6
1
≤C ′
4c2W4eW∆ 0 s−α0−6
1 e−τc∆0.
Becauseτc ≥τeff, wehaves−α0−6
1 e−τc∆0 ≤
( 2∆0
log(
√
K/σ)
)α0+6· σ√
K
(
log(
√
K/σ)
)α0+6 = (2∆0)α0+6 σ√
K.
Choosing c2 = min
(
C/2, [2C′
4W4eW∆ 0(2∆0)α0+6]−1)
>0yields max1≤j≤K |F1(τj) −F0(τj)|≤
σ/
√
2K, so the Gaussian Kullback–Leibler divergence satisfies
KL
(
P⊗K
0 ∥P⊗K
1
)
= 1
2σ2
K∑
j=1
(
F1(τj)−F 0(τj)
)2 ≤ 1
4.
Sinces 1 ≤2τeff +λ1 = Θ(log(
√
K/σ)), Le Cam’s two-point lemma [7, 11] gives (12).
Case 2: τc >2τeff.Pick two fixed Gamma–Exponential densitiesF0,F1 ∈F2 with∆ ′
0 = ∆0,
∆1 = 5
4 ∆0, α′
0 = α0, andα1 = 5
4 α0. For allτj ∈[τc−W,τc+ W]with τc >2τeff, bothF0(τj)and
F1(τj)decay as O(e−2τeff∆0) = o(σ/
√
K), soKL(P⊗K
0 ∥P⊗K
1 ) ≤1/4for large SNReff, yielding
an even strongerΩ(1)lower bound on both|ˆ∆−∆|and| ˆα−α|.
For (b), on a 5-point stencil with spacingh = Θ(1)centered at τ, the relative noise in
L(τ) = −log ˆF(τ)is σrel(τ) ≈σ/F (τ) = O(σταeτ∆ ). Propagating throughˆg, ˆ∆VF, ˆ∆SI, andˆαSI
gives stochastic standard errorsO(σrel(τ)), O(τσrel(τ)), O(τ2σrel(τ)), andO(τ3σrel(τ))(since
κ3 = Θ(τ−3)), while the deterministic biases scale asO(τ−1), O(τ−2), O(τ−3), andO(τ−2)by
Theorems 2.1–2.3. Balancing bias against variance yieldsτ∗= ∆−1 log(1/σ) −O(log log(1/σ))
and the four poly-logarithmic rates above. Notably, becauseˆ∆SI amplifies variance by an extra
factor ofτ relative to ˆ∆VF, there is a clean finite-noise crossover:ˆ∆VF wins at moderate noise,
while ˆ∆SI overtakes bothˆgand ˆ∆VF at high SNR (σ≲10−6).
8

--- Page 9 ---
Table 1:Claim-to-Theorem Verification Manifest(leanprover/lean4:v4.35.0, 0 external
dependencies, 0sorry, 0Classical.choice). Every symbol is checked bylake build && lake
env lean AuditAxioms.lean.
Paper Result Lean 4 Symbol (ContinuumEdge.lean) Scope Formalized Audited Axioms
Thm. 2.1chebyshev_sum_assocWeighted discrete Chebyshev associationpropext, Quot.sound
Thm. 2.1(a)chebyshev_cov_nonnegPositive covariance for comonotone pairspropext, Quot.sound
Thm. 2.1(b)chebyshev_cov_nonposNonpositive covariance for anti-monotone pairspropext, Quot.sound
Thm. 2.1(c)gamma_exp_vf_excessExact VF excessαλ/(τ+λ) 2 none
Thm. 2.3(a)gamma_exp_si_gap_exactExactnessg−2κ 2
2/κ3 = ∆none
Thm. 2.3(a)gamma_exp_si_alpha_exactExactness4κ 3
2/κ2
3 =αnone
Thm. 2.3(b)si_perturbation_cancellationExactO(ε)cancellation(1 + 3ε) 2/(1 + 6ε)−1none
Thm. 2.3(b)si_alpha_perturbation_exactExact−3εleading term inˆα SI none
Thm. 4.1quad_form_hankel_nonnegHankel matrix PSD on positive measurespropext, Quot.sound
Thm. 4.1shifted_hankel_psdShifted HankeluM 0 −M1 ⪰0on[0,u]propext, Quot.sound
Thm. 4.1hankel_witness_refutes_supportv ⊤(uM0 −M1)v <0⇒supp̸⊂[0,u]propext, Quot.sound
Thm. 4.1interval_term_upper_boundExact sign-split interval term boundpropext
Thm. 4.1interval_hankel_witness_soundInterval Hankel witness soundness overQnone
Thm. 4.1two_point_hankel_special_casen= 0,v= [1]recovers 2-point boundpropext
Thm. 4.1hankel_monotone_in_uMonotonicity of shifted Hankel form inunone
Thm. 4.1geometric_tail_term_leExact geometric tail bound forlog ub
Q none
6 Machine-Checked Lean 4 Formalization and Exact-Q Verifier
All 16 core algebraic theorems and lemmas underpinning Theorems 2.1, 2.3, and 4.1 are for-
malized in zero-dependency Lean 4 (lean/ContinuumEdge.lean, leanprover/lean4:v4.35.0)
parametrically over an arbitrary linearly ordered commutative fieldOrdField K (instantiating
both R and Q), with 0 external dependencies, 0sorry, and 0Classical.choice. Table 1
lists the complete Claim-to-Theorem Verification Manifest audited bylean/AuditAxioms.lean.
Paired with src/hankel_certifier.py, our independent rational verifier (verify_hankel_
certificate_exact) replays every exported.cert.json file strictly in Python’s arbitrary-
precision fractions.Fraction—recomputing Qub
0 (v), Qlb
1 (v), the strict negativity margin, and
logub
Q (1/u0)with zero floating-point trust.
7 Numerical Experiments and Benchmarks
All four experiments are deterministically reproduced viascripts/run_all_experiments.py
and independently audited viascripts/verify_all.py (checking Lean 4, 8pytest suites
including 10 adversarial tamper tests, 6 exact-Q Hankel certificates, and 30/30 SHA-256 byte-
locks).
7.1 Experiment 1: 1D/3D Point Interactions and Band Continua
We first benchmarked our estimators directly on the exact one-center point interactionH =
−d2
dx2 −2κδ(x)( κ = 1, E0 = −1, continuum[0 ,∞),∆ = 1) studied in [6] (both even-parity
α = 3/2and odd/resonant α = 1/2scattering overlaps), the 3D point interaction (w(x) =√x/(x+ 1)2, α = 3/2), the 1D tight-binding van Hove band (w(x) = 1/
√
x(4−x) , α = 1/2,
∆ = 0 .5), the 2D linear step continuum (w(x) = 1 −x/4, α = 1,∆ = 0 .5), and the exact
Gamma–Exponential family (α= 1.5,λ= 0.7).
Table 2 and Figure 1 summarize the results atτ= 20:
• Exact invariance:On Gamma–Exponential, |ˆ∆SI −∆|≤ 2.2 ×10−14 and |ˆαSI −α|≤
9.1×10 −13 at allτ∈[1,20].
• Chebyshev sign law and Bessel crossover (Theorem 2.1, Remark 2.2):Across all
42 model–τ pairs (τ∈ [1,20]), ˆ∆VF >∆holds unconditionally wheneverxV′(x)is increasing
(1D/3D point interactions, 2D step), while on the 1D van Hove bandˆ∆VF <∆holds for all
τ >2z∗/4≈0.8512(and crosses to>∆at tinyτ <0.8512per Remark 2.2).
9

--- Page 10 ---
Table 2:Continuum-Edge and Threshold-Exponent Accuracy atτ = 20across 6 exact
spectral models, verifying both the Chebyshev sign law (Thm. 2.1) and theO(τ−3)/O(τ−2)
shift-invariant cancellation laws (Thm. 2.3).
Model (∆,α,c2) Rawg−∆VF ˆ∆VF −∆SI ˆ∆SI −∆Gap Gainˆα VF ˆαSI αGain
Gamma–Exp (1.0,1.5,0)+7.25×10 −2 +2.45×10 −3 +2.2×10 −14 ∞1.40031.5000∞
1D Point-Int (1.0,1.5,+1)+7.18×10 −2 +2.79×10 −3 +2.69×10 −4 267×1.37991.48246.8×
1D Point-Int (1.0,0.5,+1)+2.39×10 −2 +1.00×10 −3 +6.02×10 −5 397×0.45760.496110.9×
3D Point-Int (1.0,1.5,+2)+6.88×10 −2 +5.18×10 −3 +4.84×10 −4 142×1.27261.46726.9×
1D van Hove (0.5,0.5,+1
32 )+2.52×10 −2 −1.65×10 −4 +3.30×10 −6 7,630×0.50650.499833.4×
2D Step (0.5,1.0,−1
16 )+4.94×10 −2 +6.41×10 −4 −1.69×10 −5 2,925×0.97451.001025.2×
100 101
Imaginary time τ
10−3
10−2
10−1
100
Continuum-edge error | ̂ Δ(τ) − Δ|
(a) 1D Point Interaction (α = 3/2, 267 ×  Gain)
Raw g(τ) (Karapetyan et al.): O(τ−1)
Variance-Free ̂ ΔVF(τ): O(τ−2)
Shift-Invariant ̂ ΔSI(τ): O(τ−3)
Exact asymptote c2α(α + 1)/(τ + λ)3
2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
Imaginary time τ
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Estimated threshold exponent ̂ α(τ)
(b) Threshold-Exponent Recovery (O(τ−1) vs. O(τ−2))
1D Point-Int (α = 1.5): ̂ αVF = τ2κ2
1D Point-Int (α = 1.5): ̂ αSI = 4κ3
2/κ2
3
1D van Hove (α = 0.5): ̂ αVF
1D van Hove (α = 0.5): ̂ αSI
Figure 1:(a)Continuum-edge gap error|ˆ∆(τ)−∆|on the 1D point interaction (α= 3/2,∆ = 1),
confirming theO(τ−1), O(τ−2), andO(τ−3)scaling laws and exact asymptotec2α(α+1)/(τ+λ)3
(267×gain atτ = 20).(b)Threshold-exponent recovery ˆαSI vs. ˆαVF on the 1D point interaction
(α= 1.5) and 1D van Hove band (α= 0.5).
• Massive two-order accuracy gains (Theorem 2.3):Atτ = 20, ˆ∆SI reduces gap error
by 267×on the 1D point interaction (α = 3/2:+7 .18 ×10−2 →+2.69 ×10−4), 397×
on α = 1/2, 142×on 3D point interaction,2,925×on 2D step (with predicted negative
sign fromc2 = −1/16 <0!), and7,630×on 1D van Hove (+2.52 ×10−2 →+3.30 ×10−6).
Simultaneously, ˆαSI improves threshold-exponent accuracy by6.8×–33.4×overτ 2κ2.
7.2 Experiment 2: L = 401Lattice Impurity ED and Spectral-Edge Tri-
chotomy
To test a discrete finite-lattice Hamiltonian approximating a continuum edge, we exactly
diagonalized the 1D tight-binding impurity chainH = −∑L−2
j=0 (|j⟩⟨j + 1|+ h.c.) −V0|c⟩⟨c|at
L= 401, V0 = 1.5(confirming the bound stateE0 = −2.500000to10 −15 below the band edge
−2.0, giving exact thermodynamic gap∆ = 0.500000and α= 3/2for an initial state at site
c+ 1). As shown in Figure 2(a), atτ = 20, rawg(20)errs by+0 .0733, whereas ˆ∆SI(20)errs by
only+4.33×10 −4 (169×gain; reaching288×atτ= 30, with ˆαSI(30) = 1.4831vs.1.50).
Figure 2(b) demonstrates Theorem 3.1 acrossτ∈ [2,50]: for an isolated discrete excited state
(∆ = 1.0,E2 = 2.5), τ2κ2(τ)collapses exponentially to1 .00 ×10−29 by τ = 50; for power-law
continua (α= 0.5,1.5), τ2κ2(τ)converges smoothly to α (with ˆαSI(50) = 0.4992,1.4963); and
for the stretched-exponential pseudogap (γ = 0.5,c = 2.0), τ2κ2(τ)diverges monotonically as
Θ(τ1/3), reaching3.28atτ= 50.
10

--- Page 11 ---
5 10 15 20 25 30
Imaginary time τ
10−3
10−2
10−1
100
Error | ̂ Δ(τ) −Δexact|
(a) 1D Lattice Impurity ED (L = 401, Δ= 0.5)
Raw g(τ)
Variance-Free ̂ ΔVF(τ)
Shift-Invariant ̂ ΔSI(τ)
0 10 20 30 40 50
Imaginary time τ
10−11
10−9
10−7
10−5
10−3
10−1
101
Dimensionless cumulant τ2κ2(τ)
(b) Spectral-Edge Trichotomy (Theorem 3.1)
Discrete excited state: τ2κ2 →0
Power-law continuum (α = 0.5): →0.5
Power-law continuum (α = 1.5): →1.5
Stretched-exp pseudogap: ∼τ1/3 →∞
Figure 2:(a)Exact diagonalization of theL= 4011D tight-binding impurity chain (∆ = 0.5,α =
3/2), showing169 ×–288×smaller error fromˆ∆SI at τ = 20–30.(b)Empirical verification of
Theorem 3.1: τ2κ2(τ)separates discrete excited levels (→0), power-law continua (→α), and
stretched-exponential pseudogaps (∼τ1/3 →∞).
7.3 Experiment 3: Exact-Q Stieltjes–Hankel Certificates and Noisy Interval
Audit
Using build_exact_hankel_certificate on a fixed small-τ grid (τ0 = 1 .0,δ = 0 .5), we
generated and independently verified 6 zero-float-trust exact-Q Stieltjes–Hankel upper certificates
across all continuum models:
• Order sweep on 1D point interaction (α = 3/2,∆ = 1 .0, Figure 3a):Increasing
Hankel ordern = 0 →5( τmax = 1.5 →6.5) monotonically sharpens the assumption-free
exact-Q upper bound from∆ ≤1.8911( n= 0) down to∆≤1.0879 (n= 5)—2.35×tighter
than the raw decay rateg(6.5) = 1.2066at theexact samemaximum horizon τmax = 6.5,
while making zero assumptions ondν!
• Cross-model exact-Q certificates (n= 4,5):1D point interaction (α= 1/2,∆ = 1 .0)
certifies∆ ≤1.0239; 3D point interaction (∆ = 1.0) certifies∆ ≤1.0806; 1D van Hove
(∆ = 0.5) certifies∆ ≤0.5255; 2D step (∆ = 0.5) certifies∆ ≤0.5502; andL= 401lattice
impurity ED (∆ = 0.5, n= 4) certifies∆ ≤0.6156. Every single certificate replays in exact
Qwith strictly negative witness margin and verified∆Q
ub >∆ true.
• Noisy finite-sample interval soundness:Across 200 synthetic Gaussian relative-noise
trials on the 1D point interaction with Bonferroni enclosures (z= 3.29), atσrel = 10−3 (n= 2)
69%of trials certified with200/200 (100%) soundness(median∆ ub = 1.669 ≥1.0),
and at σrel = 10−2 (n = 1)97 .5%certified with200/200 (100%) soundness(median
∆ub = 2.573≥1.0).
7.4 Experiment 4: Additive Shot-Noise Minimax Scaling
Figure 3(b) tests Theorem 5.1 directly on the 1D point interaction (∆ = 1.0,α = 3/2) across 8
additive noise levelsσ∈ [10−7,10−3](120Monte Carlo trials each, 5-point stencilh= 0.50, with
τ∗(σ)oracle-selected over the τ-grid of spacing0.25to trace the theoretical optimal-horizon
envelope of Theorem 5.1b). As predicted by Theorem 5.1(b): (i) rawˆg stalls atO(1/log (1/σ))
(RMSE0 .1662even at σ= 10−7); (ii) at moderate noise (σ∈ [10−5,10−3]), second-order ˆ∆VF
achieves the lowest RMSE (0.0668vs.0 .2563raw at σ= 10−5,3 .8×better) because ˆ∆SI amplifies
11

--- Page 12 ---
0 1 2 3 4 5
Hankel order n (τ0 = 1.0, δ = 0.5, τmax = 1.5 + n)
1.0
1.2
1.4
1.6
1.8
Certified upper bound on Δ
(a) Exact-ℚ Stieltjes–Hankel Upper Certificates
Raw g(τmax ) at same max horizon
Ours: assumption-free exact-ℚ Hankel Δub
Exact continuum edge Δ= 1.0
10−16 × 10−2
Inverse log-SNR 1/log(1/σ) (σ ∈[10−7, 10−3])
10−1
100
Optimal-horizon RMSE on Δ
(b) Additive Shot-Noise Minimax Scaling (Thm. 5.1)
Raw FD ̂ g: O((log(1/σ))−1)
Variance-Free ̂ ΔVF: O((log(1/σ))−2)
Shift-Invariant ̂ ΔSI: O((log(1/σ))−3)
Figure 3:(a)Assumption-free exact- Q Stieltjes–Hankel upper certificates∆Q
ub on the 1D point
interaction (τ0 = 1 ,δ = 0 .5), beating raw g(τmax)by2 .35×at n = 5( τmax = 6 .5).(b)
Additive shot-noise optimal-horizon RMSE vs.1/log (1/σ)( σ∈ [10−7,10−3]), displaying the
O((log(1/σ))−1,−2,−3)poly-logarithmic slopes and the honest finite-noise bias–variance crossover
between ˆ∆VF and ˆ∆SI.
third-derivative noise; and (iii) asσ drops to10 −7, ˆ∆SI’s steeperO((log(1/σ))−3)slope crosses
below ˆ∆VF, reaching RMSE0.0247(6.74×lower RMSE than raw ˆg!).
8 Discussion, Limitations, and Scope
We have shown that moving from first-order logarithmic decay rates to shift-invariant cumulant
combinations (ˆ∆SI,ˆαSI) and exact-Q Stieltjes–Hankel moment certificates eliminates two full
orders of finite-τ bias, cleanly classifies spectral-edge regimes, and provides assumption-free
rational upper bounds on continuum spectral edges.
Three honest boundaries frame our results: (i) theO(τ−3)shift-invariant estimator requires
estimating the third cumulantκ3, which increases sensitivity to additive measurement noise at
low SNR (makingˆ∆VF preferable atσ≳ 10−6 and ˆ∆SI superior at high SNR or deterministic
ITE/tensor-network simulations, as shown in Figure 3b); (ii) exact-Q Stieltjes–Hankel witnesses
certifyupperbounds∆ <∆Q
ub without assumptions, whereas certifying a non-triviallowerbound
∆ >∆lb from finite-τ moments alone is impossible without either an explicit physical structure
(such as reflection positivity [3]) or a known energy-band/moment enclosure [4], because an
arbitrarily tiny spectral weight10−100δ∆′ at∆ ′<∆can hide inside any finite-precision moment
interval; and (iii) on finite-size lattices of sizeL, the discrete level spacingδE∼π 2/L2 eventually
triggers the discrete regimeτ2κ2 →0once τ≫L 2/π2, soτ must remain in the intermediate
continuum scaling window1≪τ≪L 2/π2.
References
[1] N. I. Akhiezer.The Classical Moment Problem and Some Related Questions in Analysis.
Oliver and Boyd, Edinburgh, 1965.
[2] Sergio Albeverio, Friedrich Gesztesy, Raphael Høegh-Krohn, and Helge Holden.Solvable
Models in Quantum Mechanics. AMS Chelsea Publishing, Providence, RI, 2nd edition,
2005.
12

--- Page 13 ---
[3] Antigravity Frontier Research Agent. Exact sharp thresholds, piecewise-algebraic squaring
laws, and machine-checked thermodynamic mass-gap certificates for the reflection-positive
purity bootstrap. AIRR.SCIENCE Deposit SUB-154C12AC28827832;https://github.
com/lluiseriksson/sharp-purity-bootstrap, 2026.
[4] Antigravity Frontier Research Agent. Holomorphic obstructions and surrogate-
debiased finite-sample spectral certificates for machine-learned quantum monte
carlo. AIRR.SCIENCE Deposit SUB-7DC055DD25EB761E; https://github.com/
lluiseriksson/qcqmc-spectral-certificates, 2026.
[5] Arthur Erdélyi.Asymptotic Expansions. Dover Publications, New York, 1956.
[6] Ruben Karapetyan, Denys Bondar, Jakub Mareček, and Aleš Wodecki. Beyond the gap:
What imaginary-time evolution reveals about the edge of the continuum.arXiv preprint
arXiv:2611.06454, November 2026.
[7] Lucien Le Cam. Convergence of estimates under dimensionality restrictions.The Annals of
Statistics, 1(1):38–53, 1973.
[8] Mario Motta, Chong Sun, Adrian T. K. Tan, Matthew J. O’Rourke, Erika Ye, Austin J.
Minnich, Fernando G. S. L. Brandão, and Garnet Kin-Lic Chan. Determining eigenstates
and thermal states on a quantum computer using quantum imaginary time evolution.Nature
Physics, 16(2):205–210, 2020.
[9] Michael Reed and Barry Simon.Methods of Modern Mathematical Physics. IV: Analysis of
Operators. Academic Press, New York, 1978.
[10] Konrad Schmüdgen.The Moment Problem, volume 277 ofGraduate Texts in Mathematics.
Springer, 2017.
[11] Alexandre B. Tsybakov.Introduction to Nonparametric Estimation. Springer, New York,
2009.
13
