# Block-Isospectral Invariance Obstructions, Multi-Subspace Dissipation, Product-Formula Stability Bifurcations, and Subset-Optimal Weight Duality for Excited-State Double-Bracket Flows

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-7G96BR0A8Y9R1A8Z` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/paper145-double-bracket-flows (`v1.0.3`)  
**Canonical PDF SHA-256:** `9c9a3b3429b9133feee17f897514549b4e476df87e8e9c3ddaf04caffe46ad94`

## Abstract

Aghaei Saem, Sahebi, Holmes, and Suzuki (2026, arXiv:2611.34871v1) established a double-bracket flow (DBF) framework for simultaneously preparing the r lowest eigenstates of a d-dimensional Hamiltonian H via continuous-time, discretized, and product-formula evolutions on rank-r mixtures, proving the overlap necessary condition A_i = <lambda_i|P_r|lambda_i> > 0, the dissipation lower bound ||[rho, H]||_HS^2 >= 2 DeltaE (gamma_min - DeltaE), step-size bounds s_bar = 2/gamma_max and 12/(7 gamma_max), Chebyshev scheduling, and degenerate-weight single-excited-state preparation (Theorem EM1). We resolve four foundational structural, dynamical, stability, and optimization questions left open by their theory via four exact theorems backed by 20 constructive Lean 4.36.0 theorems (zero external imports, zero sorry, zero Classical.choice, zero warnings), 16 AST-audited zero-float exact-rational SHA-256 certificates (MANIFEST SHA-256: 94fb63331545e03fce19c45b2838227491d7f329ba304ab199d5fcf46b048010), and 60 adversarial tests: (1) Exact Block-Isospectral Invariance, Strict Separation from Eq. (6), and Complete Hyperbolic Morse-Index Classification: any spectral projector Pi_S commuting with rho_ref commutes identically with rho under all three DBFs and all step sizes s_k > 0, conserving all power traces Tr((Pi_S rho Pi_S)^m) and requiring multiset block-spectral compatibility spec(Pi_{S_m} rho_ref Pi_{S_m}) = {p_a : a in S_m} on connected components of G(rho_ref); an explicit d=3, r=2 rational witness satisfies A_1 = 1/2 > 0, A_2 = 1 > 0, and rank(Pi_2 P_2 Pi_2) = 2 yet stays permanently trapped at DeltaE(rho) >= gamma_{1,2} = 1/3 > 0, while all d!/(d-r)! fixed points rho_sigma are classified as hyperbolic critical points with exact Jacobian eigenvalues mu_{ab}(sigma) = -(q_a - q_b)(lambda_b - lambda_a), unstable real dimension 2 inv(q) in [0, r(2d-r-1)], unique sink, exact r index-1 saddles, unique source, and multi-level excess bound DeltaE(rho_sigma) >= sum_{j=1}^r gamma_{j,j+1} k_j(sigma); (2) Exact Cross-Subspace Dissipation Identity, Concentration-Ratio Sharpening Above gamma_min, Global Tightness, and Strictly Tighter Discrete Contraction: ||[rho, H]||_HS^2 = 2 sum (delta p_j)^2 l_j + 4 sum_{j<m} delta p_j delta p_m l_{j,m} sharpens Lemma 1 via the concentration ratio C(rho) = sum x_j^2 / (DeltaE)^2 in [1/r, 1] to ||[rho, H]||_HS^2 >= 2 DeltaE (gamma_bar(rho) - C(rho) DeltaE) with exact nonnegative surplus 2 sum (gamma_{j,j+1} - gamma_min) x_j + 4 sum_{j<m} x_j x_m certifying strictly positive dissipation up to r gamma_min, while the 2-level geodesic |lambda_{j*}> <-> |lambda_{j*+1}> attains exact global equality in Lemma 1, Lemma G.2, and Theorem G.1(1), and discrete logistic contraction tightens to y_{k+1} <= y_k (1 - 2 b_k gamma_min / (1 + 2 b_k x_0)) < y_k / (1 + 2 b_k gamma_min), reducing step counts to (kappa + x_0/gamma_min) ln(c_0/eps) and (7 kappa/6 + x_0/gamma_min) ln(c_0/eps); (3) Discretized Period-Doubling Stall Bifurcation, Exact Product-Formula Complex Spectrum, and Unbalanced-Mode Chebyshev Instability: exact 2-level reduction theta_{k+1} = theta_k - s_k gamma sin(theta_k) proves algebraic breakdown DeltaE(rho_k) ~ 3 gamma / (8k) at u = 2 and a unique locally asymptotically stable symmetric period-2 stall orbit sin(theta*)/theta* = 2/u for all u in (2, pi) (explaining Fig. 6(a)), while the exact product-formula linearized multiplier |mu_{ab}^PF|^2 = 1 - 8 sin(u_H/2) sin(u_rho/2) cos((u_H+u_rho)/2) and 2-level nonlinear energy step reproduce all three fourth-order constants (1/6, 1/6, 1/4) of Theorem C.3, prove AM-GM optimality of theta/tau = Omega/p_1 with sharp threshold s_crit^PF = pi^2/(4 gamma_max) > 2/gamma_max > 12/(7 gamma_max), and establish the unbalanced-mode Chebyshev dichotomy (m = 2 stable for all kappa >= 1 vs. m = 4 unstable at kappa = 100 with sum u_k sin(u_k) < -1/2, explaining Fig. 15(b)); and (4) Subset-Optimal Degenerate Weight Duality and Exact Adaptive Untracked-Gap Asymmetry: for any target subset T with boundary set J(T) (permitting exact degeneracies delta lambda_{j+1} = 0 outside J(T)), gamma_min(p) <= (sum_{j in J(T)} j/delta lambda_{j+1})^{-1} and kappa(p) >= Omega sum_{j in J(T)} 1/delta lambda_{j+1}, strictly beating Theorem EM1 for T = {r} whenever delta lambda_r != delta lambda_{r+1} by up to 2x in kappa and (2r-1)/(r-1) in (2, 3]x in gamma_min, while perturbed inverse-gap weights obey kappa(p_hat) = Omega (sum 1/g_hat_j)(max g_hat_j/delta lambda_{j+1}) <= (c_+/c_-) kappa*(T) with an exact (r-1)-to-1 untracked-gap asymmetry explaining Fig. 13's min-rule advantage.

## Full Extracted Text

--- Page 1 ---
Block-Isospectral Invariance Obstructions,
Multi-Subspace Dissipation, Product-F ormula
Stability Bifurcations, and Subset-Optimal W eight
Duality for Excited-State Double-Bracket Flows
Lluis Eriksson∗
November 28, 2026
Abstract
Aghaei Saem, Sahebi, Holmes, and Suzuki ( arXiv:2611.34871v1) introduced a unified
framework for simultaneously preparing the r lowest eigenstates of a d-dimensional Hamilto-
nian H via continuous-time, discretized, and product-formula double-bracket flows (DBF s)
on rank- r density matrices ρref = ∑r
i=1 pi|ϕi⟩⟨ϕi|, establishing an overlap necessary con-
dition Ai = ⟨λi|Pr|λi⟩ > 0, a quadratic dissipation bound ∥[ρ, H]∥2
HS ≥ 2∆E(γmin − ∆E),
step-size guarantees ¯s = 2 /γmax and ¯s = 12 /(7γmax), Chebyshev scheduling, and degenerate-
weight single-excited-state preparation. Here we resolve four foundational structural, dy-
namical, stability , and optimization questions left open by their theory , with the underlying
finite algebraic identities, rational witnesses, and T aylor brackets backed by 20 construc-
tive Lean 4.36.0 theorems (zero external imports, zero sorry, zero Classical.choice, zero
warnings), 16 AST-audited zero-float exact-rational SHA-256 certificates, and 60 adversarial
tests:
1. Exact Block-Isospectral Invariance, Strict Separation from Eq. (6), and Hy-
perbolic Morse-Index Classification (Theorem 1): Any spectral projector ΠS
commuting with ρref commutes identically with ρ under all three DBF s and all step
sizes sk > 0, conserving all power traces Tr((ΠSρΠS)m). Convergence to ρ∗ there-
fore requires multiset spectral compatibility spec(ΠSmρref ΠSm) = {pa : a ∈ Sm} on
every connected component Sm of the eigenbasis support graph G(ρref ). An explicit
rational witness at d = 3 , r = 2 satisfies A1 = 1 /2 > 0, A2 = 1 > 0, and even
rank(Π2P2Π2) = 2 , yet remains permanently trapped at ∆E(ρ(t)) ≥ γ1,2 = 1 /3 > 0.
W e further classify all d!/(d − r)! fixed points ρσ as hyperbolic critical points with ex-
act Jacobian eigenvalues µab(σ) = −(qa − qb)(λb − λa), exact unstable real dimension
2 inv( q) ∈ [0, r(2d − r − 1)], unique sink, exact r index-1 saddles, unique source, and
multi-level excess bound ∆E(ρσ) ≥ ∑r
j=1 γj,j+1kj(σ).
2. Exact Cross-Subspace Dissipation, Concentration-Ratio Sharpening Above
γmin, Global Tightness, and Tighter Discrete Contraction (Theorem 2): W e
prove the exact identity ∥[ρ, H]∥2
HS = 2 ∑r
j=1(δpj)2lj + 4 ∑
1≤j<m≤r δpjδpmlj,m and
sharpen Lemma 1 via the subspace concentration ratio C(ρ) = ∑
j x2
j /(∆E)2 ∈ [1/r,1]
to ∥[ρ, H]∥2
HS ≥ 2∆E(¯γ(ρ) − C (ρ)∆E) with exact nonnegative surplus 2 ∑
j(γj,j+1 −
γmin)xj + 4 ∑
j<m xjxm, certifying strictly positive dissipation up to rγmin. Along the 2-
level geodesic |λj∗ ⟩ ↔ | λj∗+1⟩, Lemma 1, Lemma G.2, and Theorem G.1(1) are globally
tight. In discrete time, we tighten Eq. (G5) to yk+1 ≤ yk(1 − 2bkγmin/(1 + 2 bkx0)) <
yk/(1 + 2 bkγmin) with exact gap 4b2
kγmin(γmin − x0)/((1 + 2 bkγmin)(1 + 2 bkx0)) > 0,
cutting step counts from (1 +κ) ln(c0/ε) and (1 + 7κ/6) ln(c0/ε) to (κ+x0/γmin) ln(c0/ε)
and (7κ/6 + x0/γmin) ln(c0/ε).
∗ Independent Researcher. ORCID: 0009-0006-7494-9040. Code and Lean 4 formalization: MIT License;
manuscript: CC-BY-4.0. Repository: https://github.com/lluiseriksson/paper145-double-bracket-flows
(v1.0.3).
1
AIRR:ARR-2026-7G96BR0A8Y9R1A8Z v1  [Quantum information]  28 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
3. Discretized Period-Doubling Stall Bifurcation, Exact Product-F ormula Com-
plex Spectrum, and Unbalanced-Mode Chebyshev Instability (Theorem 3):
An exact 2-level reduction ϑk+1 = ϑk −skγ sin ϑk proves algebraic breakdown ∆E(ρk) ∼
3γ/(8k) at u = 2 (unimprovability of ¯s = 2 /γmax) and a unique locally asymptoti-
cally stable symmetric period- 2 stall orbit sin ϑ∗/ϑ∗ = 2 /u for all u ∈ (2, π), explaining
the stalled runs in Fig. 6(a) of 2611.34871v1. F or arbitrary (d, r), we derive the exact
product-formula linearized complex multiplierµPF
ab = 1 −4ei(uρ−uH)/2 sin(uH/2) sin(uρ/2)
and squared modulus |µPF
ab |2 = 1 −8 sin(uH/2) sin(uρ/2) cos((uH + uρ)/2), show that the
exact 2-level nonlinear step reproduces all three fourth-order constants (1/6, 1/6, 1/4) of
Theorem C.3, and prove AM–GM optimality of θ/τ = Ω /p1 yielding the sharp threshold
sPF
crit = π2/(4γmax) > 2/γmax > 12/(7γmax). Finally , the exact unbalanced-mode Cheby-
shev expansion proves m = 2 is stable for all κ ≥ 1 while m = 4 destabilizes at large κ
(∑4
k=1 uk sin uk < −1/2 certified at κ = 100 ), explaining Fig. 15(b).
4. Subset-Optimal Degenerate W eight Duality and Adaptive Untracked-Gap
Asymmetry (Theorem 4): F or any target subsetT ⊆ {1, . . . , r } with minimal bound-
ary set J(T)—permitting exact Hamiltonian degeneracies δλj+1 = 0 for j /∈ J(T)—
we establish the sharp dual bounds γmin(p) ≤ γ⋆
min(T) = ( ∑
j∈J(T) j/δλj+1)−1 and
κ(p) ≥ κ⋆(T) = Ω ∑
j∈J(T) δλ−1
j+1. F or single excited state T = {r}, this strictly outper-
forms Theorem EM1/Corollary H.2 whenever δλr ̸= δλr+1, cutting κ by up to 2× and
expanding γmin by up to (2r − 1)/(r − 1) ∈ (2, 3]×. F or estimated gaps ˆgj, we prove
κ(ˆp) = Ω( ∑
j∈J ˆg−1
j )(maxj∈J ˆgj/δλj+1) ≤ (c+/c−)κ⋆(T) and uncover an exact (r − 1)-
to-1 untracked-gap asymmetry: overestimating ˆgr by α > 1 incurs (α − 1)Ω ∑r−1
j=1 δλ−1
j+1
versus (α − 1)Ω/δλr+1 for underestimation, explaining the empirical dominance of the
min rule in Fig. 13.
1 Introduction and Setting
Computing multiple low-lying eigenstates of a Hermitian Hamiltonian H is a central bottle-
neck across quantum many-body physics, quantum chemistry , and fault-tolerant quantum algo-
rithms [1, 2, 3]. Double-bracket flows (DBF s)—originally introduced in classical matrix analysis
and continuous-time optimization by Brockett [ 4] and Helmke and Moore [ 5, 6], and indepen-
dently in renormalization-group physics by W egner [ 7] and Głazek and Wilson [ 8]—have re-
cently emerged as a powerful quantum-compatible paradigm for both ground-state preparation
(r = 1 ) [9, 10] and full diagonalization ( r = d) [11, 12].
In a landmark recent contribution, Aghaei Saem, Sahebi, Holmes, and Suzuki [ 13] (see also
the concurrent study [ 14]) systematically developed the intermediate-rank regime 1 < r < d ,
evolving a rank- r reference mixture
ρref =
r∑
i=1
pi|ϕi⟩⟨ϕi|, p 1 ≥ p2 ≥ · · · ≥ pr > 0 = pr+1 = · · · = pd,
r∑
i=1
pi = 1 , (1)
under three unitary-orbit flows minimizing the ensemble energy E(ρ) = Tr( ρH) [15]:
Continuous-time DBF: ∂tρ(t) = [ W(t), ρ(t)], W (t) := [ ρ(t), H], (2)
Discretized DBF: ρk+1 = VkρkV †
k , V k = eskWk , W k := [ ρk, H], (3)
Product-formula DBF: ρk+1 = VkρkV †
k , V k = eiτkHeiθkρk e−iτkHe−iθkρk , τ kθk = sk, (4)
where H = ∑d
a=1 λa|λa⟩⟨λa| with ordered spectrum λ1 ≤ λ2 ≤ · · · ≤ λd (strictly ordered
λ1 < · · · < λ d in Theorems 1–3, and permitting exact degeneracies in Theorem 4), spectral
width Ω := λd−λ1, and target global minimum ρ∗ := ∑r
i=1 pi|λi⟩⟨λi| with energy E∗ := Tr(ρ∗H)
and excess energy ∆E(ρ) := E(ρ) − E∗.
Throughout this paper we use a single, consistent indexing convention:
δpj := pj − pj+1 ≥ 0, δλ j+1 := λj+1 − λj ≥ 0, γ j,j+1 := δpj δλj+1, j ∈ {1, . . . , r },
(5)
2

--- Page 3 ---
with γab := ( pa − pb)(λb − λa) for 1 ≤ a < b ≤ d, γmax := γ1,d = p1Ω, γmin := min {γj,j+1 :
1 ≤ j ≤ r, δp j > 0}, and condition number κ := γmax/γmin. (Note that Proposition I.3 of [ 13]
temporarily wrote δλj for λj+1 −λj; keeping δλj+1 = λj+1 −λj everywhere aligns Appendices D–
I uniformly .)
F our open structural gaps in [ 13]. Although [ 13] established the core convergence guar-
antees and rich numerical diagnostics (including transverse-field Ising model [ 16] simulations in
Figs. 5–16), four deep analytical gaps remained open:
1. Invariance obstructions beyond Eq. (6): Theorem E.1 of [13] proves that Ai := ⟨λi|Pr|λi⟩ > 0
(∀i ≤ r, where Pr = ∑r
j=1 |ϕj⟩⟨ϕj|) is necessary for ρ → ρ∗, leaving open whether Ai > 0 (or
full target-subspace rank rank(ΠrPrΠr) = r) captures all invariant-submanifold obstructions,
and leaving the full Morse-index classification of the d!/(d − r)! fixed points unproved.
2. Dissipation above γmin and discrete contraction slack: Lemma 1 of [ 13] certifies positive
dissipation only for ∆E(ρ) < γ min and drops all cross-subspace couplings in Eq. (F12),
whereas Figs. 5(b) and 12 show rapid decay from cold starts far above γmin; furthermore,
Eq. (G34) discards a strictly positive O(b2
k) term in discrete logistic contraction, inflating
step-count guarantees.
3. Exact nonlinear bifurcation, product-formula linear spectrum, and Chebyshev instability:
Fig. 6(a) of [13] exhibits stalled runs just above ¯s = 2 /γmax; Theorem C.3 guarantees energy
descent for the group-commutator product formula [ 17] only up to ¯s = 12 /(7γmax), leaving
its true linear stability threshold unknown; and Fig. 15(b) shows that a period- 4 Chebyshev
schedule [18, 19, 20] can destabilize under product-formula implementation even in the linear
regime.
4. General target subsets, degenerate spectra, and adaptive gap-estimation asymmetry: Corol-
lary H.2 (Theorem EM1) of [ 13] fixes equal weight gaps δpr−1 = δpr = 1 /(2r − 1) for
preparing a single excited state |λr⟩, which is suboptimal whenever δλr ̸= δλr+1, and Fig. 13
empirically finds that estimating the untracked gap δλr+1 by the min rule strongly outper-
forms the mean rule without an analytical explanation.
The next four sections resolve all four problems via exact, self-contained theorems (Theo-
rems 1–4), followed in Section 6 by a complete audit of our Lean 4 formalization and zero-float
cryptographic verification pipeline.
2 Theorem 1: Block-Isospectral Invariance, Separation, and
Morse-Index Classification
F or any density matrixρ expressed in the eigenbasis {|λa⟩}d
a=1 of H, define its eigenbasis support
graph G(ρ) = ( V, E) with vertex set V = {1, . . . , d} and undirected edge {a, b} ∈ E (a ̸= b)
if and only if ⟨λa|ρ|λb⟩ ̸ = 0 . F or any S ⊆ V , let ΠS := ∑
a∈S |λa⟩⟨λa| denote the spectral
projector onto span{|λa⟩ : a ∈ S}, and let spec(ΠSρΠS) denote the multiset of |S| eigenvalues
of the restriction of ΠSρΠS to Ran(ΠS).
Theorem 1 (Block-Isospectral Invariance, Strict Separation from Eq. (6), and Hyperbolic
Morse Classification). Let 1 ≤ r < d , let H = ∑d
a=1 λa|λa⟩⟨λa| have strictly ordered eigenvalues
λ1 < · · · < λ d, and let ρref = ∑r
i=1 pi|ϕi⟩⟨ϕi| have distinct positive weights p1 > · · · > p r > 0
(with pa := 0 for a > r ).
(i) Exact block-isospectral conservation. If S ⊆ { 1, . . . , d} satisfies [ρref , ΠS] = 0 , then
under all three flows (2)–(4) (and any higher-order product formula generated by e±iτH and
e±iθρk ) and for every step-size sequence sk > 0, one has [ρ, ΠS] = 0 at al l times/iterations,
3

--- Page 4 ---
the block restriction ΠSρΠS evolves by unitary conjugation within Ran(ΠS), and al l block
Casimir invariants Tr((ΠSρΠS)m) (m ≥ 1) and the multiset spectrum spec(ΠSρΠS) are
exactly conserved.
(ii) Sharp block-compatibility obstruction and strict separation from Eq. (6). Let
S1, . . . , SM be the connected components of G(ρref ). Convergence ρ → ρ∗ under any of (2)–
(4) and any sk > 0 requires
spec(ΠSmρref ΠSm) = {pa : a ∈ Sm} as multisets, for al l m ∈ {1, . . . , M }. (6)
Condition (6) strictly generalizes Eq. (6) of [13] (Ai = ⟨λi|Pr|λi⟩ > 0 for i ≤ r). Specifical ly,
for d = 3 , r = 2 , H = diag(0 , 1, 3), p = (2 /3, 1/3, 0), and
|ϕ1⟩ = |λ2⟩, |ϕ2⟩ = 1√
2
(
|λ1⟩ + |λ3⟩
)
, (7)
the reference state satisfies A1 = 1 /2 > 0, A2 = 1 > 0, and ful l target-subspace rank
rank(Π2P2Π2) = 2 , yet G(ρref ) splits into S1 = {2} and S2 = {1, 3} with spec(ΠS1 ρref ΠS1 ) =
{2/3} ̸= {1/3}, trapping every trajectory of al l three DBFs at
∆E(ρ) ≥ γ1,2 = γmin = 1
3 > 0 for al l t ≥ 0 (or k ≥ 0). (8)
(iii) Complete hyperbolic Morse-index classification and multi-level excess bound.
Adapting the classical Hermitian isospectral Morse theory of Brockett [ 4] and Helmke–
Moore [ 5] to the rank- r excited-state flag manifold Op = {Uρref U† : U ∈ U(d)} of real
dimension r(2d − r − 1), every fixed point ρσ = ∑d
a=1 qa|λa⟩⟨λa| (qa := pσ(a)) is hy-
perbolic under (2): its Jacobian on Tρσ Op diagonalizes in the off-diagonal coordinates
{δρab : 1 ≤ a < b ≤ d, q a ̸= qb} with exact real eigenvalues (each of real multiplicity 2)
µab(σ) = −(qa − qb)(λb − λa) ̸= 0 . (9)
Hence the unstable manifold of ρσ has exact real dimension (real Morse index) 2 inv( q),
where inv(q) := |{(a, b) : 1 ≤ a < b ≤ d, q a < qb}| ∈
[
0, r (2d−r −1)/2
]
. Among al l d!/(d−
r)! fixed points, there is a unique sink (inv(q) = 0 , namely ρ∗), exact r minimal non-trivial
saddles (inv(q) = 1 , real Morse index 2, namely the adjacent swaps ρσj,j+1 for j = 1 , . . . , r ),
and a unique source (inv(q) = r(2d − r − 1)/2, with q = (0 , . . . , 0, pr, . . . , p1)). Moreover,
letting kj(σ) := j−Tr(Pj(ρσ)Πj) ∈ {0, . . . , min(j, d−j)} be the subspace displacement count,
every fixed point obeys
∆E(ρσ) ≥
r∑
j=1
γj,j+1 kj(σ). (10)
Proof. (i) Since ΠS is a spectral projector of H, [H, ΠS] = 0 . Whenever [ρ, ΠS] = 0 , the Jacobi
identity gives
[W,ΠS] = [[ ρ, H], ΠS] = −[[H, ΠS], ρ] − [[ΠS, ρ], H] = 0 ,
and repeating once more yields [[W, ρ], ΠS] = 0 (formalized universally for all dimensions n in
Lean thm01). Thus the submanifold MS = {ρ : [ ρ, ΠS] = 0 } is invariant under the smooth
vector field [[ρ, H], ρ] of ( 2); by Picard–Lindelöf uniqueness, [ρ(t), ΠS] = 0 for all t ≥ 0,
and the unitary propagator U(t) solving ∂tU = W(t)U satisfies [U(t), ΠS] = 0 . F or ( 3),
[Wk, ΠS] = 0 implies [eskWk , ΠS] = 0 by power-series convergence for every sk > 0. F or ( 4)
(and any product of factors e±iτH , e±iθρk ), [H, ΠS] = [ ρk, ΠS] = 0 implies every exponential
factor commutes with ΠS, hence [Vk, ΠS] = 0 for all τk, θk ∈ R. By induction, [ρk, ΠS] = 0 and
ΠSρk+1ΠS = (Π SVkΠS)(ΠSρkΠS)(ΠSVkΠS)†, where ΠSVkΠS is unitary on Ran(ΠS). Unitary
similarity conserves spec(ΠSρΠS) and Tr((ΠSρΠS)m) for all m ≥ 1.
4

--- Page 5 ---
(ii) By definition of the connected components S1, . . . , SM of G(ρref ), ⟨λa|ρref |λb⟩ = 0 when-
ever a ∈ Sm and b /∈ Sm, so [ρref , ΠSm] = 0 for each m. By part (i), spec(ΠSmρΠSm) is constant
along the flow; by continuity of eigenvalues, any limit point ρ∗ must satisfy spec(ΠSmρ∗ΠSm) =
spec(ΠSmρref ΠSm), yielding (6). If Ai = 0 for some i ≤ r, then ρref |λi⟩ = 0 , so {i} is an isolated
component with spec(Π{i}ρref Π{i}) = {0} ̸= {pi} since pi > 0; hence (6) strictly implies Eq. (6).
F or the explicit witness ( 7), ⟨ϕ1|ϕ2⟩ = 0 , ⟨ϕ1|ϕ1⟩ = ⟨ϕ2|ϕ2⟩ = 1 , and in the eigenbasis
{|λ1⟩, |λ2⟩, |λ3⟩}:
P2 =


1/2 0 1 /2
0 1 0
1/2 0 1 /2

, ρ ref =


1/6 0 1 /6
0 2 /3 0
1/6 0 1 /6

.
Thus A1 = 1 /2 > 0, A2 = 1 > 0, and Π2P2Π2 = diag(1 /2, 1, 0) has rank(Π2P2Π2) = 2 .
Y et G(ρref ) has components S1 = {2} and S2 = {1, 3}, with ΠS1 ρref ΠS1 = 2
3 |λ2⟩⟨λ2| and
spec(ΠS2 ρref ΠS2 ) = {1/3, 0}. By part (i), along any trajectory of ( 2)–(4), the S1-block stays
frozen with energy 2
3 λ2 = 2
3 , while the S2-block has diagonal entries d1, d3 ≥ 0 summing to 1/3,
so d1λ1 + d3λ3 = 3 d3 ≥ 0 (Lean thm02, thm05; Cert. C02). Since E∗ = 2
3 (0) + 1
3 (1) = 1
3 and
γ1,2 = ( 2
3 − 1
3 )(1 − 0) = 1
3 < γ2,3 = 2
3 , we obtain ∆E(ρ) ≥ 2
3 − 1
3 = γ1,2 = γmin > 0 for all t or k,
while ∆E(ρref ) = 7
6 − 1
3 = 5
6 decays strictly to the trapped saddle ρσ1,2 (Figure 1(a)).
(iii) Any fixed point ρ ∈ O p of ( 2) satisfies 0 = Tr( H[[ρ, H], ρ]) = −∥[ρ, H]∥2
HS, hence
[ρ, H] = 0 ; because H has simple spectrum λ1 < · · · < λ d, ρ is diagonal in {|λa⟩} with
eigenvalues (q1, . . . , qd) obtained by placing the r distinct positive weights (p1, . . . , pr) at r
distinct slots and 0 at the remaining d − r slots (indexed by cosets σ ∈ Sd/Sd−r, giving exactly
d!/(d − r)! fixed points ρσ). W riting a nearby point on Op as ρ = eKρσe−K = ρσ + δρ + O(K2)
with K† = −K and Kab = 0 whenever qa = qb, the tangent space Tρσ Op is parametrized by
the complex entries δρab = ( qb − qa)Kab for 1 ≤ a < b ≤ d with qa ̸= qb. There are
(r
2
)
pairs among the r distinct positive weights and r(d − r) pairs between a positive weight and
a zero weight, giving complex dimension
(r
2
)
+ r(d − r) = r(2d − r − 1)/2 and real dimension
r(2d−r −1) (Lean thm03). Linearizing ( 2) at ρσ (using [ρσ, H] = 0 ) gives W = [ δρ, H ] +O(δρ2)
with Wab = ( λb − λa)δρab, and hence
∂t(δρ)ab = [ W, ρσ]ab + O(δρ2) = ( qb − qa)(λb − λa)δρab + O(δρ2) = µab(σ) δρab + O(δρ2),
establishing (9). Since λb −λa > 0 and qa ̸= qb, every µab(σ) ̸= 0 (hyperbolicity), with µab(σ) >
0 ⇐ ⇒ qa < qb. Each unstable complex mode contributes real dimension 2, so the Morse index
is 2 inv( q). Clearly inv(q) = 0 ⇐ ⇒ q1 ≥ · · · ≥ qd ⇐ ⇒ ρσ = ρ∗; inv(q) = r(2d − r − 1)/2 ⇐ ⇒
q1 ≤ · · · ≤ qd (unique source); and inv(q) = 1 requires an adjacent inversion qj < q j+1 whose
swap eliminates the sole inversion and recovers q = ( p1, . . . , pr, 0, . . . , 0), yielding precisely the r
adjacent swaps ρσj,j+1 (j = 1 , . . . , r ). Finally , combining Eq. (D7) ( ∆E(ρσ) = ∑r
j=1 δpjεj(ρσ))
with Lemma D.1 (εj(ρσ) ≥ δλj+1[j−Tr(Pj(ρσ)Πj)] = δλj+1kj(σ)) of [13] immediately yields (10)
(Lean thm04b, Cert. C04).
3 Theorem 2: Cross-Subspace Dissipation, Sharpening, Tight-
ness, and Discrete Contraction
F ollowing Appendices D and F of [13], let Vj := span {|ϕ1⟩, . . . , |ϕj⟩} (1 ≤ j ≤ r) with projector
Pj, subspace energy excess εj := Tr( PjH) − ∑j
i=1 λi ≥ 0, weighted subspace excess xj :=
δpjεj ≥ 0 (so ∆E(ρ) = ∑r
j=1 xj), and single-subspace leakage lj := ∥(I − Pj)HPj∥2
HS =∑j
i=1
∑d
k=j+1 |Hik|2, where Hik := ⟨ϕi|H|ϕk⟩ in an eigenbasis {|ϕi⟩}d
i=1 of ρ. F or every 1 ≤ j <
5

--- Page 6 ---
Figure 1: Theorems 1 and 2. (a) Exact block-isospectral trapping of the d = 3 , r = 2
separation witness ( 7) ( A1 = 1 /2, A2 = 1 , rank(Π2P2Π2) = 2 ) at ∆E = γ1,2 = 1 /3 across
all three DBF s ( s = 0 .25), contrasted with escape to ρ∗ under a cross-block perturbation
ϵ = 0 .02. (b) Concentration-ratio dissipation lower bound ( 14) versus Lemma 1 of [ 13] (C = 1 ),
certifying strictly positive dissipation up to rγmin and verified by the exact rational witness of
Certificate C06 at ∆E ≈ 1.95 γmin.
m ≤ r, define the cross-subspace leakage
lj,m := ∥(I − Pm)HPj∥2
HS =
j∑
i=1
d∑
k=m+1
|Hik|2 ≥ 0. (11)
F or∆E(ρ) > 0, define the excess-weighted effective rate and subspace concentration ratio
¯γ(ρ) :=
∑r
j=1 γj,j+1xj
∆E(ρ) ≥ γmin, C(ρ) :=
∑r
j=1 x2
j
(∆E(ρ))2 ∈
[1
r , 1
]
. (12)
Theorem 2 (Cross-Subspace Dissipation, Sharpening, Tightness, and Contraction) . Let 1 ≤
r < d , let H have strictly ordered eigenvalues λ1 < · · · < λ d, and let ρ = ∑r
i=1 pi|ϕi⟩⟨ϕi| have
p1 > · · · > pr > 0.
(i) Exact cross-subspace dissipation identity. The energy dissipation rate satisfies the
exact decomposition
∥[ρ, H]∥2
HS = 2
r∑
j=1
(δpj)2lj + 4
∑
1≤j<m≤r
δpj δpm lj,m. (13)
(ii) Concentration-ratio sharpening above γmin. Whenever ∆E(ρ) > 0,
∥[ρ, H]∥2
HS ≥ 2∆E(ρ)
(
¯γ(ρ) − C(ρ)∆E(ρ)
)
≥ 2∆E(ρ)
(
γmin − ∆E(ρ)
)
, (14)
with exact nonnegative surplus between the middle and right-hand expressions
2∆E(ρ)
(
¯γ(ρ) − C(ρ)∆E(ρ)
)
− 2∆E(ρ)
(
γmin − ∆E(ρ)
)
= 2
r∑
j=1
(γj,j+1 − γmin)xj + 4
∑
1≤j<m≤r
xjxm ≥ 0. (15)
Consequently, ∥[ρ, H]∥2
HS > 0 is certified throughout the region∆E(ρ) < ¯γ(ρ)/C(ρ), reaching
up to rγmin for balanced multi-subspace excitations (C(ρ) = 1 /r).
6

--- Page 7 ---
(iii) Exact global tightness along the 2-level geodesic. Choose j∗ ∈ { 1, . . . , r } attain-
ing γj∗,j∗+1 = γmin, and define the 1-parameter geodesic ρ(ϑ) (ϑ ∈ [0, π]) rotating only
span{|λj∗⟩, |λj∗+1⟩} via
|ϕj∗(ϑ)⟩ = cos ϑ
2 |λj∗⟩ + sin ϑ
2 |λj∗+1⟩,
with |ϕj∗+1(ϑ)⟩ = −sin ϑ
2 |λj∗⟩+cos ϑ
2 |λj∗+1⟩ when j∗ < r and |ϕi⟩ = |λi⟩ otherwise. W riting
fi(|ϕi⟩) := |⟨λi|ϕi⟩|2 for the i-th eigenstate fidelity ( Fi(k) := |⟨λi|ϕi(k)⟩|2 at discrete step
k), along ρ(ϑ) Lemma 1, Lemma G.2, and the continuous-time bound of Theorem G.1(1)
in [ 13] al l hold with exact global equality :
1 − fj∗(|ϕj∗(ϑ)⟩) = ∆E(ρ(ϑ))
γmin
, ∥[ρ(ϑ), H]∥2
HS = 2∆ E(ρ(ϑ))
(
γmin − ∆E(ρ(ϑ))
)
,
∆E(ρ(t))
γmin − ∆E(ρ(t)) = c0e−2γmint. (16)
(iv) Strictly tighter discrete logistic contraction and reduced step complexity. Under
the discretized DBF (3) (¯s = 2 /γmax) or product-formula DBF (4) (¯s = 12 /(7γmax) with
θk/τk = Ω /p1), if x0 := ∆ E(ρref ) < γ min and 0 < s k < ¯s, let xk := ∆ E(ρk), yk :=
xk/(γmin − xk), c0 := y0, and bk := sk(1 − sk/¯s). Then at every step k ≥ 0 with yk > 0,
yk+1 ≤ yk
(
1 − 2bkγmin
1 + 2 bkx0
)
< yk
1 + 2 bkγmin
, (17)
(and yk+1 = 0 whenever yk = 0 ), with exact positive contraction-factor gap
1
1 + 2 bkγmin
−
(
1 − 2bkγmin
1 + 2 bkx0
)
= 4b2
kγmin(γmin − x0)
(1 + 2 bkγmin)(1 + 2 bkx0) > 0. (18)
At constant step s = ¯s/2, achieving 1 − Fi(K) ≤ ε for al l i ∈ { 1, . . . , r } requires at most
⌈Kdisc⌉ (respectively ⌈KPF⌉) iterations, where the continuous iteration thresholds satisfy
Kdisc =
(
κ + x0
γmin
)
ln c0
ε < (1 + κ) ln c0
ε ,
KPF =
(7κ
6 + x0
γmin
)
ln c0
ε <
(
1 + 7κ
6
)
ln c0
ε , (19)
strictly improving the continuous prefactors of Eqs. (G49)–(G50) in [13] uniformly for every
x0 ∈ (0, γmin).
Proof. (i) F rom Eq. (F8) of [ 13], ∥[ρ, H]∥2
HS = 2 ∑
1≤i<k≤d(pi − pk)2|Hik|2. Substituting the
telescoping sum pi − pk = ∑r
j=1 δpj 1i≤j<k into both factors of (pi − pk)2 gives
(pi − pk)2 =
r∑
j=1
(δpj)2 1i≤j<k + 2
∑
1≤j<m≤r
δpj δpm 1i≤j<m<k
(Lean thm06). Multiplying by 2|Hik|2, summing over 1 ≤ i < k ≤ d, and exchanging summation
order yields ( 13) directly via ( 11).
(ii) Dropping the nonnegative cross-subspace term in ( 13) and applying Lemma F.2 of [ 13]
(lj ≥ εj(δλj+1 − εj)) to each term gives
∥[ρ, H]∥2
HS ≥ 2
r∑
j=1
(δpj)2lj ≥ 2
r∑
j=1
δpjεj
(
δpjδλj+1 − δpjεj
)
= 2
r∑
j=1
xj(γj,j+1 − xj).
7

--- Page 8 ---
Using (12), ∑
j γj,j+1xj = ¯γ(ρ)∆E(ρ) and ∑
j x2
j = C(ρ)(∆E(ρ))2, which gives the first inequal-
ity in ( 14). By Cauchy–Schwarz and nonnegativity of xj, (∆E)2 ≤ r ∑r
j=1 x2
j ≤ r(∆E)2,
so C(ρ) ∈ [1/r,1] (Lean thm08). Subtracting 2∆E(γmin − ∆E) and applying (∑
j xj)2 −∑
j x2
j = 2 ∑
j<m xjxm yields ( 15) identically (Lean thm07). Explicit rational witness C06
(d = 6 , r = 3 , H = diag(0 , 10, 20, 30, 40, 50), p = (1 /2, 1/3, 1/6, 0, 0, 0) with Pythagorean rota-
tions (12/13, 5/13), (24/25, 7/25), (40/41, 9/41) on pairs (1, 4), (2, 5), (3, 6)) achieves ∆E/γmin ≈
1.946 > 1, where Lemma 1 is strictly negative while ( 14) certifies positive dissipation (Fig-
ure 1(b)).
(iii) Along ρ(ϑ), only the 2×2 block {j∗, j∗+1} is rotated, giving ∆E(ρ(ϑ)) = γmin sin2(ϑ/2),
1−fj∗(|ϕj∗(ϑ)⟩) = sin 2(ϑ/2) = ∆ E/γmin, and |[ρ(ϑ), H]j∗,j∗+1| = 1
2 γmin sin ϑ, so ∥[ρ(ϑ), H]∥2
HS =
1
2 γ2
min sin2 ϑ = 2∆ E(γmin−∆E) (Lean thm09, Cert. C07). By Theorem 1(i), the block {j∗, j∗+1}
is invariant under (2), so ρ(t) = ρ(ϑ(t)) solves ∂t∆E = −2∆E(γmin − ∆E) exactly , integrating
to ∆E(ρ(t))/(γmin − ∆E(ρ(t))) = c0e−2γmint for all t ≥ 0.
(iv) By Eq. (G33) of [ 13], every step obeys
yk+1 ≤ yk
1 − 2bk(γmin − xk)
1 + 2 bkxk
= yk
(
1 − 2bkγmin
1 + 2 bkxk
)
.
Since 0 ≤ xk ≤ x0 < γ min by monotonic energy decrease (Eq. (G30)), we have 1 + 2 bkxk ≤ 1 +
2bkx0 < 1 + 2bkγmin, proving (17). Combining fractions over the common positive denominator
(1 + 2 bkγmin)(1 + 2 bkx0) gives
(1 + 2 bkx0) − (1 + 2 bkγmin)(1 + 2 bkx0 − 2bkγmin) = 4 b2
kγmin(γmin − x0) > 0,
proving (18) (Lean thm10, Cert. C08). Setting uk := 2 bkγmin/(1 + 2 bkx0) ∈ (0, 1) (as 2bkγmin ≤
γmin/γmax ≤ 1) and using 1 − uk ≤ e−uk yields yK ≤ c0 exp(−∑K−1
k=0 uk). F or constant step
s = ¯s/2, bk = ¯s/4, so u−1
k = 2
¯sγmin
+ x0
γmin
; substituting ¯s = 2 /γmax and ¯s = 12 /(7γmax)
gives (19).
4 Theorem 3: Discretized Stall Bifurcation, Product-F ormula
Complex Spectrum, and Unbalanced Chebyshev Instability
W e now establish the exact nonlinear and spectral stability boundaries of both discrete imple-
mentations ( 3) and ( 4), resolving the empirical instabilities observed in Figs. 6(a) and 15(b)
of [13].
Theorem 3 (Discretized Bifurcation, PF Spectrum, and Chebyshev Instability) .
(i) Exact 2-level discretized reduction and period-2 stal l bifurcation. On any invariant
2-level block {a, b} with γ = γab = ( pa −pb)(λb −λa) > 0 (in particular {1, d} with γ = γmax),
writing
ρ(ϑ) = pa + pb
2 I + pa − pb
2 (cos ϑ σz + sin ϑ σx)
reduces the discretized DBF (3) exactly to the 1-dimensional map
ϑk+1 = Fuk (ϑk) := ϑk − uk sin ϑk, u k := skγ, ∆E(ρ(ϑ)) = γ sin2(ϑ/2). (20)
F or constantu = sγ:
• At u = 2 (s = ¯s = 2 /γmax), F2(ϑ) = −ϑ+ 1
3 ϑ3 +O(ϑ5), and F2 has a unique positive zero
˜ϑ ≈ 1.89549 ∈ (π/2, π) solving ˜ϑ = 2 sin ˜ϑ; for every nonzero initial angle ϑ0 ∈ (−˜ϑ, ˜ϑ) \
{0} (and more general ly every ϑ0 ∈ (−π, π) outside the countable zero-orbit preimage
set ∪
k≥0 F−k
2 (0)), the iterates decay only algebraical ly as ϑ2
k ∼ 3
2k and ∆E(ρk) ∼ 3γ
8k ,
proving that ¯s = 2 /γmax is unimprovable for exponential convergence.
8

--- Page 9 ---
• F orevery u ∈ (2, π), there exists a unique symmetric period- 2 stal l orbit {±ϑ∗(u)} with
ϑ∗(u) ∈ (0, π/2) solving
sin ϑ∗
ϑ∗ = 2
u. (21)
Its 2-step Floquet multiplier satisfies (Fu ◦Fu)′(ϑ∗) = (1 −u cos ϑ∗)2 = (1 −2ϑ∗ cot ϑ∗)2 ∈
[0, 1) (vanishing at the superstable parameter u0 = 2 ϑ∗
0/ sin ϑ∗
0 ≈ 2.5366 where tan ϑ∗
0 =
2ϑ∗
0), certifying local asymptotic stability throughoutu ∈ (2, π) (and instability for u > π ).
Along {±ϑ∗(u)}, ∆E(ρk+1) = ∆ E(ρk) = γ sin2(ϑ∗/2) > 0 is strictly constant, causing
energy-stagnation stopping rules to terminate prematurely away from ρ∗.
(ii) Exact product-formula complex spectrum, exact 2-level nonlinear step, and
sharp threshold sPF
crit = π2/(4γmax). F or arbitrary(d, r), linearizing the group-commutator
product-formula DBF (4) at ρ∗ yields, for every off-diagonal mode (a, b) (a < b, p a > p b)
with uH := τ(λb − λa) and uρ := θ(pa − pb), the exact complex multiplier and squared
modulus
µPF
ab (τ, θ) = 1 − 4ei(uρ−uH)/2 sin uH
2 sin uρ
2 ,
|µPF
ab (τ, θ)|2 = 1 − 8 sin uH
2 sin uρ
2 cos uH + uρ
2 . (22)
On the 2-level block {a, b}, the exact nonlinear one-step energy change is
E(ρ1) − E(ρ0) = −∥W0∥2
HS
γ
[
sin uH sin uρ − cos ϑ (1 − cos uH)(1 − cos uρ)
]
, (23)
whose fourth-order expansion at ϑ → 0+ is −s∥W0∥2
HS(1 − 1
6 u2
H − 1
6 u2
ρ − 1
4 uHuρ + O(u4)),
proving that al l three error constants (1/6, 1/6, 1/4) in Theorem C.3 of [ 13] are exact at
fourth order. Moreover, by AM–GM ( uH + uρ ≥ 2√sγmax), the angle ratio θ/τ = Ω /p1
uniquely maximizes the primary linear stability boundary uH + uρ < π , yielding the exact
sharp threshold
sPF
crit = π2
4γmax
> 2
γmax
> 12
7γmax
. (24)
(iii) Unbalanced-mode Chebyshev instability dichotomy. Under an m-periodic Chebyshev
schedule s−1
k = γmax+γmin
2 + γmax−γmin
2 cos (2k−1)π
2m (k = 1 , . . . , m) with θk/τk = Ω /p1, any
unbalanced mode (a, b) with relative energy gap η := ( λb − λa)/Ω ∈ (0, 1] and vanishing
weight gap ϵ := pa − pb → 0+ (e.g., a ≥ 2, b = d with pa ≪ p1 and λa − λ1 ≪ Ω, so
(a, b) ̸= (1 , d) and uρ = ϵθk → 0+) has per-cycle squared amplification
m∏
k=1
|µPF
ab (τk, θk)|2 = 1 − 2ϵ
p1
Sm(κ; η) + O(ϵ2), S m(κ; η) :=
m∑
k=1
uk sin(ηuk), (25)
where uk := τkΩ = √skγmax and Sm(κ) := Sm(κ; 1) is the near-maximal-gap limit η → 1−:
• F or m = 2 , 0 < u 1 < u 2 <
√
4 + 2
√
2 < 3 < π for all κ ≥ 1, so S2(κ; η) > 0
unconditional ly for every η ∈ (0, 1] and every κ ≥ 1.
• F orm = 4 , u4 → 1/ sin(π/16) ≈ 5.126 ∈ (π, 2π) as κ → ∞, destabilizing near-maximal-
gap unbalanced modes for large κ; in particular, at κ = 100 , exact rational T aylor
brackets certify S4(100) < −1/2 < 0, and Lipschitz continuity |S4(100; η) − S4(100)| ≤
(1 −η) ∑4
k=1 u2
k < 27(1 −η) guarantees S4(100; η) < 0 (hence per-cycle amplification > 1
for al l suﬀiciently smal l ϵ > 0) for every unbalanced mode with η ∈ [53
54 , 1).
9

--- Page 10 ---
Proof. (i) In the {a, b} block with H = λa+λb
2 I − λb−λa
2 σz, direct Pauli algebra yields W =
[ρ(ϑ), H] = iγ sin ϑ
2 σy, so Vk = eskW = ei uk sin ϑ
2 σy rotates the Bloch vector (sin ϑ, 0, cos ϑ) in
the (x, z)-plane by −uk sin ϑ, giving ( 20) exactly . At u = 2 , for every ϑ ∈ (0, π) we have
0 < sin ϑ < ϑ , hence −ϑ < F 2(ϑ) < ϑ and |F2(ϑ)| < |ϑ| with no nonzero fixed point of |F2| on
(0, π); moreover, F2(ϑ) = ϑ − 2 sin ϑ is strictly negative on (0, ˜ϑ) (where ˜ϑ ≈ 1.89549 ∈ (π/2, π)
is its unique positive zero) and strictly positive on ( ˜ϑ, π). By odd symmetry , for every ϑ0 ∈
(−˜ϑ, ˜ϑ) \ {0} (and more generally every ϑ0 ∈ (−π, π) \ ∪
k≥0 F−k
2 (0): on ( ˜ϑ, π), 0 < F 2(ϑ) < ϑ
with no fixed point of F2 on (0, π), so iterates decrease strictly and cross below ˜ϑ in finitely
many steps), no iterate vanishes and |ϑk| ↓ 0 strictly , entering [−1, 1] \ {0} in finitely many
steps. Once 0 < |ϑk| ≤ 1, the alternating T aylor bracket ϑ − ϑ3/6 ≤ sin ϑ ≤ ϑ − ϑ3/6 + ϑ5/120
gives ϑ − ϑ3/3 ≤ − F2(ϑ) ≤ ϑ − ϑ3/3 + ϑ5/60 < ϑ (Lean thm11, Cert. C09). Hence |ϑk| ↓ 0
monotonically and ϑ−2
k+1 − ϑ−2
k = 2
3 + O(ϑ2
k); Cesàro averaging yields ϑ2
k ∼ 3
2k and ∆E(ρk) =
γ sin2(ϑk/2) ∼ γ
4 ϑ2
k ∼ 3γ
8k .
F oru > 2, a symmetric period- 2 orbit satisfies Fu(ϑ∗) = −ϑ∗ ⇐ ⇒ sin ϑ∗/ϑ∗ = 2 /u. Since
g(ϑ) = sin ϑ/ϑ is continuous and strictly decreasing on (0, π) with g(0+) = 1 and g(π−) = 0 , a
unique root ϑ∗(u) ∈ (0, π) exists for every u > 2, with ϑ∗(u) ∈ (0, π/2) ⇐ ⇒ 2/u > g (π/2) =
2/π ⇐ ⇒ u ∈ (2, π). By odd symmetry Fu(−ϑ) = −Fu(ϑ), (Fu ◦ Fu)′(ϑ∗) = ( F′
u(ϑ∗))2 =
(1−u cos ϑ∗)2 = (1 −2ϑ∗ cot ϑ∗)2. F or allϑ∗ ∈ (0, π/2), 0 < ϑ∗ < tan ϑ∗ implies 0 < ϑ∗ cot ϑ∗ < 1,
hence −1 < 1 − 2ϑ∗ cot ϑ∗ < 1 and (Fu ◦ Fu)′(ϑ∗) ∈ [0, 1) (Lean thm12, Cert. C10), with
superstable vanishing at the unique root tan ϑ∗
0 = 2 ϑ∗
0 in (0, π/2). F or u > π , ϑ∗ ∈ (π/2, π)
gives cos ϑ∗ < 0 so 1 − u cos ϑ∗ > 1 (unstable). Finally , ∆E(ρ(−ϑ∗)) = γ sin2(−ϑ∗/2) =
∆E(ρ(ϑ∗)) > 0.
(ii) Since e−iθρρeiθρ = ρ, Eq. ( 4) simplifies to V ρV † = eiτH eiθρXe−iθρe−iτH , where X :=
e−iτH ρeiτH = ρ∗ +δX and δXab = eiuH δρab for ρ = ρ∗ +δρ. By Duhamel’s formula, eiθ(ρ∗+δρ) =
eiθρ∗
(I + Φ( δρ) + O(δρ2)) with Φ(δρ)ab = δρab(1 − e−iuρ)/(pa − pb), hence [Φ(δρ), ρ∗]ab =
(e−iuρ − 1)δρab. Conjugating ρ∗ + [Φ(δρ), ρ∗] + δX by eiθρ∗
(factor eiuρ) and eiτH (factor e−iuH )
yields
µPF
ab (τ, θ) = e−iuH
(
1−eiuρ +ei(uρ+uH))
= 1 −(1−e−iuH )(1−eiuρ) = 1 −4ei(uρ−uH)/2 sin uH
2 sin uρ
2 .
T aking the squared modulus and applying the identitycos((uρ−uH)/2)−2 sin(uH/2) sin(uρ/2) =
cos((uH + uρ)/2) yields ( 22) (verified algebraically in Lean thm13). F or the 2-level nonlinear
step, Eq. (C28) of [ 13] gives E(ρ1) = Tr( A(τ)B(θ)) with A(τ) = e−iτH ρ0eiτH and B(θ) =
e−iθρ0 Heiθρ0 . On the Bloch sphere, A(τ) rotates ˆn = (sin ϑ, 0, cos ϑ) around ˆz by −uH to
ˆnA = (sin ϑ cos uH, −sin ϑ sin uH, cos ϑ), while B(θ) rotates ˆz around ˆn by +uρ to
ˆzB =
(
sin ϑ cos ϑ(1 − cos uρ), −sin ϑ sin uρ, 1 − sin2 ϑ(1 − cos uρ)
)
.
Computing ˆnA · ˆzB and using ∥W0∥2
HS = 1
2 γ2 sin2 ϑ gives ( 23), whose T aylor expansion at
cos ϑ = 1 matches (1/6, 1/6, 1/4) identically (Lean thm14, Cert. C11). F or stability |µPF
ab |2 < 1
on the primary lobe uH, uρ > 0, we require uH + uρ < π . On the maximal mode (1, d) where
uHuρ = sγmax, AM–GM yields uH + uρ ≥ 2√sγmax with equality iff θ/τ = Ω /p1, giving
2√sγmax < π ⇐ ⇒ s < π 2/(4γmax). At this ratio, every other mode obeys uH(a, b) ≤
uH(1, d) < π/ 2 and uρ(a, b) ≤ uρ(1, d) < π/ 2, so uH(a, b) + uρ(a, b) < π simultaneously; above
π2/(4γmax), cos((uH + uρ)/2) < 0 makes |µPF
1,d|2 > 1.
(iii) Substituting uρ = ϵθk and uH = τk(λb −λa) = ηuk into (22) as ϵ → 0+ (with θk = uk/p1
under θk/τk = Ω /p1) yields
|µPF
ab (τk, θk)|2 = 1 − 4ϵθk sin ηuk
2 cos ηuk
2 + O(ϵ2) = 1 − 2ϵ
p1
uk sin(ηuk) + O(ϵ2);
multiplying over k = 1 , . . . , m yields ( 25). When m = 2 , cos(π/4) =
√
2/2, so for all κ ≥ 1,
u−2
2 = 1+κ−1
2 − 1−κ−1
2
√
2
2 > 2−
√
2
4 > 1
8 > 1
9 > 1
π2 , forcing 0 < ηu 1 < ηu 2 < 3 < π and S2(κ; η) > 0
10

--- Page 11 ---
Figure 2: Theorem 3. (a) Exact 2-level discretized DBF bifurcation diagram showing the
critical algebraic breakdown at u = 2 , the unique locally asymptotically stable symmetric
period-2 stall orbit ±ϑ∗(u) on u ∈ (2, π) (shaded), and the exact threshold hierarchy 12/7 <
2 < π 2/4 < π . (b) Unbalanced-mode Chebyshev stability sum Sm(κ) = ∑m
k=1 uk sin uk: m = 2
remains strictly positive for all κ ≥ 1, whereas m = 4 crosses zero near κ ≈ 52 and is certified
below −1/2 at κ = 100 (Certificate C12).
for every η ∈ (0, 1]. When m = 4 at κ = 100 , the roots c1 = cos( π/8) and c2 = cos(3 π/8) of
8c4 − 8c2 + 1 = 0 are bracketed by c1 ∈ ( 9238
10000 , 9239
10000 ) and c2 ∈ ( 3826
10000 , 3827
10000 ), giving u1 ≤ 1.02,
u2 ≤ 1.21, u3 ≤ 1.79, and 4.57 ≤ u4 ≤ 4.59. Applying sin x ≤ x − x3/6 + x5/120 to u1, u2,
sin u3 ≤ 1, and −sin u4 = sin( u4 −π) ≥ w −w3/6 at w = 1 .42 ≤ u4 −π yields the exact rational
bound
S4(100) ≤ − 61939305404015
120000000000000 ≈ −0.5162 < −1
2 < 0
(Lean thm15, Cert. C12; Figure 2(b)). Moreover, since |sin(ηuk) − sin uk| ≤ (1 − η)uk and∑4
k=1 u2
k ≤ 1.022 + 1.212 + 1.792 + 4.592 = 26 .7767 < 27, every near-maximal-gap unbalanced
mode with η ∈ [53
54 , 1) obeys S4(100; η) < −1
2 +27(1−η) ≤ 0 (strictly negative because S4(100) <
−1
2 and ∑u2
k < 27), proving per-cycle amplification for all suﬀiciently small ϵ > 0. Note
that the maximal mode (1, d) itself has ϵ = p1 (not small) and is not governed by ( 25); the
instability specifically targets unbalanced near-maximal-gap modes such as (2, d) with p2 ≪ p1
and λ2 − λ1 ≤ 1
54 Ω.
5 Theorem 4: Subset-Optimal Degenerate W eight Duality and
Adaptive Untracked-Gap Asymmetry
Suppose an application requires preparing only a non-empty subsetT ⊆ {1, . . . , r } of eigenstates
(with r = max T < d ). By Theorem H.1(4) of [ 13], isolating every |λi⟩ (i ∈ T) requires positive
weight gaps δpj > 0 precisely on the minimal boundary index set
J(T) :=
∪
i∈T
(
{i − 1, i} ∩ {1, . . . , r }
)
⊆ {1, . . . , r }. (26)
Crucially , because terms with δpj = 0 drop out of ∆E(ρ) = ∑
j∈J(T) δpjεj and γmin, the
Hamiltonian H need only be nondegenerate across J(T): we allow exact spectral degeneracies
δλj+1 = 0 for any j /∈ J(T)!
11

--- Page 12 ---
Theorem 4 (Subset-Optimal Degenerate W eight Duality and Exact Adaptive Untracked-Gap
Asymmetry). Let 1 ≤ r < d , let T ⊆ {1, . . . , r } be non-empty with minimal boundary set J(T)
(r = max T), and let H satisfy δλj+1 > 0 for al l j ∈ J(T) (permitting δλj+1 = 0 for j /∈ J(T)).
(i) Subset-optimal weight duality. F or every valid weight vector p1 ≥ · · · ≥ pr > 0
(∑r
i=1 pi = 1 ) with δpj > 0 for al l j ∈ J(T) and δpj = 0 whenever δλj+1 = 0 (which
guarantees γmin(p) > 0; by convention κ(p) := + ∞ if γmin(p) = 0 ),
γmin(p) ≤ γ⋆
min(T) :=

 ∑
j∈J(T)
j
δλj+1


−1
, κ (p) ≥ κ⋆(T) := Ω
∑
j∈J(T)
1
δλj+1
. (27)
Both bounds are attained simultaneously and uniquely by the degenerate inverse-gap weights
δp⋆
j = γ⋆
min(T)/δλj+1 for j ∈ J(T) and δp⋆
j = 0 for j /∈ J(T).
(ii) Strict improvement over Theorem EM1 / Corol lary H.2 for single excited state
T = {r} (r ≥ 2). W ritingg− := δλr, g+ := δλr+1, δλmin := min( g−, g+), and δλmax :=
max(g−, g+), the subset-optimal weights for T = {r} (J({r}) = {r − 1, r}) are
p⋆
1 = · · · = p⋆
r−1 = g− + g+
(r − 1)g+ + rg−
, p ⋆
r = g−
(r − 1)g+ + rg−
, (28)
giving γ⋆
min({r}) = g−g+
(r−1)g++rg−
and κ⋆({r}) = Ω( g−1
− + g−1
+ ). Compared against Theo-
rem EM1 ( γEM1
min = δλmin/(2r − 1), κEM1 = 2Ω /δλmin), whenever g− ̸= g+ we obtain strict
simultaneous improvements:
κEM1
κ⋆({r}) = 2
1 + δλmin/δλmax
∈ (1, 2),
γ⋆
min({r})
γEM1
min
= 2r − 1
(r − 1)(δλmin/g−) + r(δλmin/g+) ∈
(
1, 2r − 1
r − 1
)
, (29)
achieving up to a 2× reduction in κ and up to a 2r−1
r−1 ∈ (2, 3]× expansion of the convergence
basin γmin (reaching 3× at r = 2 ).
(iii) Exact perturbation formula and adaptive untracked-gap asymmetry. Suppose
inverse-gap weights ˆp are constructed from positive gap estimates {ˆgj}j∈J(T) via δˆpj ∝ ˆg−1
j
(j ∈ J(T)) and δˆpj = 0 (j /∈ J(T)). Then
κ(ˆp) = Ω

 ∑
j∈J(T)
1
ˆgj


(
max
j∈J(T)
ˆgj
δλj+1
)
≤ c+
c−
κ⋆(T) (30)
whenever c−δλj+1 ≤ ˆgj ≤ c+δλj+1 (0 < c − ≤ c+). In ful l tracking J = {1, . . . , r } where
ˆgj = δλj+1 for j = 1 , . . . , r − 1 and only the untracked gap ˆgr is misestimated by a factor
α > 1, overestimation ( ˆgr = αδλr+1) versus underestimation ( ˆgr = δλr+1/α) obey
κover(α) − κ⋆ = ( α − 1)Ω
r−1∑
j=1
1
δλj+1
, κ under(α) − κ⋆ = ( α − 1) Ω
δλr+1
. (31)
Hence overestimation incurs an (r − 1)-term global penalty whereas underestimation incurs
only a single-term local penalty, with exact gapκover(α)−κunder(α) = ( α−1)Ω(∑r−1
j=1 δλ−1
j+1 −
δλ−1
r+1) (strictly positive whenever ∑r−1
j=1 δλ−1
j+1 > δλ −1
r+1, and reversing otherwise).
12

--- Page 13 ---
Figure 3: Theorem 4. (a) Exact condition-number speedup κEM1/κ⋆({r}) → 2× and
convergence-basin expansion γ⋆
min({r})/γEM1
min → (2r − 1)/(r − 1) ∈ (2, 3]× over Theorem EM1
for single excited state T = {r}. (b) Exact adaptive untracked-gap asymmetry ( 31) for the
r = 10 TFIM spectrum of Fig. 13 in [ 13]: underestimating by 3× (min rule) incurs only a
+22.1% single-term penalty , while overestimating by 3× incurs a +177.9% global penalty .
Proof. (i) By telescoping summation pi = ∑r
j=i δpj, normalization and top weight obey 1 =∑r
i=1 pi = ∑r
j=1 j δpj ≥ ∑
j∈J(T) j δpj and p1 = ∑r
j=1 δpj ≥ ∑
j∈J(T) δpj. Since γmin(p) ≤
δpjδλj+1 for every j ∈ J(T), we have δpj ≥ γmin(p)/δλj+1, yielding
1 ≥ γmin(p)
∑
j∈J(T)
j
δλj+1
, p 1 ≥ γmin(p)
∑
j∈J(T)
1
δλj+1
,
which establish both inequalities in ( 27) (Lean thm16, Cert. C13). Equality holds in both iff
δpj = 0 for all j /∈ J(T) and δpjδλj+1 = γ⋆
min(T) for all j ∈ J(T).
(ii) Specializing part (i) to J({r}) = {r−1, r} directly yields (28) and the ratios (29). When
g− ̸= g+, δλmin/δλmax < 1 gives κEM1/κ⋆({r}) ∈ (1, 2), while at least one of δλmin/g−, δλmin/g+
is strictly below 1, making (r − 1)(δλmin/g−) + r(δλmin/g+) < 2r − 1; as g+/g− → ∞ , the
denominator approaches r −1, giving the sharp supremum (2r −1)/(r −1) ∈ (2, 3] (Lean thm17,
Cert. C14; Figure 3(a)).
(iii) Let δˆpj = c/ˆgj for j ∈ J(T) where c = ( ∑
j∈J(T) j/ˆgj)−1. Then ˆp1 = c ∑
j∈J(T) ˆg−1
j
and γmin(ˆp) = c minj∈J(T)(δλj+1/ˆgj) = c(maxj∈J(T) ˆgj/δλj+1)−1. The normalization factor
c cancels identically in κ(ˆp) = ˆp1Ω/γmin(ˆp), proving the equality in ( 30); substituting ˆg−1
j ≤
(c−δλj+1)−1 and ˆgj/δλj+1 ≤ c+ yields the upper bound (Lean thm18, Cert. C15). Finally , setting
Sr−1 := ∑r−1
j=1 δλ−1
j+1 and sr := δλ−1
r+1 in ( 30): for ˆgr = αδλr+1 (α > 1), maxj(ˆgj/δλj+1) = α
gives κover(α) = Ω( Sr−1 + sr/α)α = Ω( αSr−1 + sr); for ˆgr = δλr+1/α, maxj(ˆgj/δλj+1) = 1
gives κunder(α) = Ω( Sr−1 + αsr), yielding ( 31) (Lean thm19). In the Fig. 13 TFIM regime
of [ 13] ( r = 10 , Ω = 2 , δλmin = 0 .0042, δλ11 = 0 .0126 = 3 δλmin, S9 = 640 ), the min rule
underestimates by α = 3 and inflates κ by only +22.1% (κunder/κ∗ < 5/4), whereas a symmetric
3× overestimation inflates κ by +177.9% (> 11/4; Lean thm20, Cert. C16; Figure 3(b)).
6 F ormal V erification and Cryptographic Certificate Audit
The finite algebraic identities, universal polynomial/rational inequalities, exact separation wit-
nesses, and rational T aylor brackets underlying Theorems 1–4 (complementing the continuous-
time ODE, matrix-exponential, and analytic proofs in Sections 2–5) are machine-checked across
three independent layers (archived at tag v1.0.3):
13

--- Page 14 ---
T able 1:T raceability matrix linking Theorems1–4 to Lean 4.36.0 constructive theorems (thm01–
thm20, 0 Classical.choice) and exact-rational SHA-256 certificates (C01–C16, 8-hex prefixes).
Result Lean 4 Certs SHA-256 Prefixes
Thm. 1 (Invariance & Morse) thm01–thm05 C01 –C04 54dad7c3 , 9f9474d5, a8f01b17, 1fd33fc9
Thm. 2 (Dissipation & Logistic) thm06–thm10 C05 –C08 643bee85 , 90e12979, e16e5c6a, 4f24ec04
Thm. 3 (Bifurcations & PF/Cheb.) thm11–thm15 C09 –C12 ac300956 , 157e59de, 40898db1, d7c18832
Thm. 4 (W eight Duality & Asym.) thm16–thm20 C13 –C16 e9d5a5b8 , 53ff8bd4, 6085a6c0, 50bc989c
1. Constructive Lean 4.36.0 F ormalization:T wenty constructive theorems (thm01–thm20)
in lean/DoubleBracketFlowBarriers.lean (pure Lean 4 core, zero external imports ) com-
pile cleanly under lean -DwarningAsError=true (exit code 0, zero warnings, zero sorry,
zero grind). Running #print axioms on all 20 theorems confirms zero occurrences of
Classical.choice or sorryAx (using only constructive propext and Quot.sound, with
thm04, thm15, thm20 depending on no axioms at all).
2. AST-Audited Zero-Float Exact-Rational V erifier: Our pure Python standard-library
verifier ( verification/verify_double_bracket_flows.py) uses only int and exact rational
Fraction arithmetic. Its built-in AST self-auditor verifies 0 float/complex/math viola-
tions and emits 16 canonical SHA-256 certificates ( C01–C16) aggregated into the determin-
istic manifest digest:
MANIFEST SHA-256: 94fb63331545e03fce19c45b2838227491d7f329ba304ab199d5fcf46b048010
3. Adversarial T est Suite ( tests/test_adversarial.py): 60 automated pytest checks
(60/60 passing in 1.02 s) testing every positive certificate, negative counterexample (non-
block perturbations, degenerate-Hamiltonian hyperbolicity failure, x0 > γ min logistic rever-
sal, u > π period-2 instability , sr > S r−1 asymmetry reversal), boundary equality , AST
tamper injection, and SHA-256 tamper detection.
7 Conclusion
W e have established a complete structural, dynamical, stability , and optimization theory ex-
tending the excited-state double-bracket flow framework of [ 13]. Practically , our results deliver
four immediate algorithmic prescriptions: (i) verify eigenbasis-graph connectivity and block-
spectral compatibility ( 6) rather than merely subspace overlap Ai > 0; (ii) spread initial exci-
tations across subspaces (minimizing C(ρ)) to retain certified positive dissipation up to rγmin;
(iii) respect the exact step-size boundaries s < 2/γmax (discretized) and s < π 2/(4γmax) (group-
commutator PF at θ/τ = Ω /p1), while limiting first-order PF Chebyshev cycles to m = 2 or
deploying higher-order commutator formulas when κ ≳ 50; and (iv) use subset-optimal degener-
ate inverse-gap weights ( 27)–(28) together with conservative (underestimating) untracked-gap
rules such as the min rule to avoid (r − 1)-fold condition-number inflation.
References
[1] Oscar Higgott, Daochen W ang, and Stephen Brierley . V ariational Quantum Computation
of Excited States. Quantum, 3:156, 2019.
[2] Ken M. Nakanishi, Kosuke Mitarai, and Keisuke F ujii. Subspace-search variational quan-
tum eigensolver for excited states. Physical Review Research, 1:033062, 2019.
[3] Lin Lin and Y u T ong. Near-optimal ground state preparation. Quantum, 4:372, 2020.
14

--- Page 15 ---
[4] Roger W. Brockett. Dynamical systems that sort lists, diagonalize matrices, and solve
linear programming problems. Linear Algebra and its Applications , 146:79–91, 1991.
[5] Uwe Helmke and John B. Moore. Optimization and Dynamical Systems . Communications
and Control Engineering. Springer, London, 1994.
[6] John B. Moore, Robert E. Mahony , and Uwe Helmke. Numerical gradient algorithms
for eigenvalue and singular value calculations. SIAM Journal on Matrix Analysis and
Applications, 15(3):881–902, 1994.
[7] F ranz W egner. Flow-equations for Hamiltonians. Annalen der Physik , 506:77–91, 1994.
[8] Stanisław D. Głazek and Kenneth G. Wilson. Renormalization of Hamiltonians. Physical
Review D, 48:5863–5872, 1993.
[9] Marek Gluza, Jeongrak Son, Bi Hong Tiang, Raphael Zander, Raphael Seidel, Y udai
Suzuki, Zoë Holmes, and Nelly H. Y. Ng. Double-bracket quantum algorithms for quantum
imaginary-time evolution. Physical Review Letters, 136:020601, 2026.
[10] Matteo Robbiati, Edoardo Pedicillo, Andrea Pasquale, Xiaoyue Li, Oriel Kiss, A. W right,
R. M. S. F arias, K. U. Giang, Jeongrak Son, Johannes Knörzer, S. T. Goh, J. Y. Khoo,
Nelly H. Y. Ng, Zoë Holmes, Stefano Carrazza, and Marek Gluza. Double-bracket quantum
algorithms for high-fidelity ground-state preparation. Physical Review Research, 8:033078,
2026.
[11] Marek Gluza. Double-bracket quantum algorithms for diagonalization. Quantum, 8:1316,
2024.
[12] Jeongrak Son, Marek Gluza, Ryuji T akagi, and Nelly H. Y. Ng. Quantum dynamic pro-
gramming. Physical Review Letters, 134:180602, 2025.
[13] Reyhaneh Aghaei Saem, Mehrad Sahebi, Zoë Holmes, and Y udai Suzuki. Simultaneous
computation of multiple excited states via double bracket flows. arXiv:2611.34871 [quant-
ph], November 2026.
[14] S. A. Rahman, Özkan Karabacak, and Rafael Wisniewski. Double-bracket quantum algo-
rithms for preparing multiple excited states. arXiv:2611.22774 [quant-ph], 2026.
[15] E. K. U. Gross, L. N. Oliveira, and W. Kohn. Rayleigh-Ritz variational principle for
ensembles of fractionally occupied states. Physical Review A, 37:2805–2808, 1988.
[16] Pierre Pfeuty . The one-dimensional Ising model with a transverse field. Annals of Physics,
57:79–90, 1970.
[17] Y u-An Chen, Andrew M. Childs, Mohammad Hafezi, Zhang Jiang, Hwanmun Kim, and
Yijia Xu. Eﬀicient product formulas for commutators and applications to quantum simu-
lation. Physical Review Research, 4:013191, 2022.
[18] David Y oung. On Richardson’s method for solving linear systems with positive definite
matrices. Journal of Mathematics and Physics , 32:243–255, 1953.
[19] Gene H. Golub and Richard S. V arga. Chebyshev semi-iterative methods, successive over-
relaxation iterative methods, and second order Richardson iterative methods – Part II.
Numerische Mathematik , 3:157–168, 1961.
[20] V. I. Lebedev and S. A. Finogenov. Ordering of the iterative parameters in the cyclical
Chebyshev iterative method. USSR Computational Mathematics and Mathematical Physics,
11:155–170, 1971.
15
