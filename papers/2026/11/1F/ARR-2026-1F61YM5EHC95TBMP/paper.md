# Constructive Lean 4 and Zero-Float Exact Rational Certificates for the Thermodynamic Budget of Objectivity and Biological Resource Horizons

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-1F61YM5EHC95TBMP` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/thermodynamic-budget-objectivity-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `181324be45884aa8de8c98cc5ba31ffb5b922f68a3368e54887df18985db4d52`

## Abstract

We present a constructive Lean 4.35.0 formalization and zero-float exact-rational verification framework (THERMO-OBJECTIVITY-CERT-1.0) for the exact algebraic, combinatorial, and thermodynamic inequalities governing objective classical records established by Chung (arXiv:2611.34909v1, Nov. 2026), together with an explicit quantitative bridge to bioenergetic maintenance horizons (ARR-2025-2AQXS44H6Z8GQAG2). Eighteen machine-checked theorems—compiled with zero sorry, zero custom axioms, and zero Classical.choice—certify the nonnegativity and source-preservation algebra of the Landauer-linear creation bound W >= R k_B T ln 2 (1-delta) H(epsilon), decreasing c_1/M staircase excess via constructive rationals, the exact binary-symmetric-channel convolution inverse e_1* = (e*-q)/(1-2q) and critical-angle impossibility beyond theta_c = 2 arcsin sqrt(H_2^{-1}(delta)), the adversary access threshold k_min = R - R_min + 1, inter-record parity work extraction W_ext = (k-1) k_B T ln 2, the event-inclusive sector second law Sigma_{eA} = Sigma_A + I_i - I_f, zero-gap thermal permutation invariance and (D,M) contrast-polarization swapping, the branch-averaged Cauchy-Schwarz emergence speed limit 2 Sigma A >= B^2, the exact factor-R parallel-broadcast advantage, maintenance-power scaling, intersubjectivity agreement bounds, and SI-2019 adiabatic drift-filter flight arithmetic. A zero-float Python verifier audits 16 canonical certificates across four verification modes using certified rational series brackets for ln, log_2, H_2, multi-copy noisy BSC mutual information, and (f/2)coth(f/2), passing 33 unit, forgery-rejection, and AST tests.

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 and Zero-Float Exact Rational
Certificates for the Thermodynamic Budget of Objectivity
and Biological Resource Horizons
Lluis Eriksson
Independent Researcher (AIRR-FOUNDER-1.0)
Repository:https://github.com/lluiseriksson/thermodynamic-budget-objectivity-certificates
November 26, 2026
Abstract
We present a constructive Lean 4.35.0 formalization
and zero-float exact-rational verification framework
(THERMO-OBJECTIVITY-CERT-1.0) for the exact algebraic,
combinatorial, and thermodynamic inequalities govern-
ing objective classical records established by Chung
(arXiv:2611.34909v1, Nov. 2026), together with an ex-
plicit quantitative bridge to bioenergetic maintenance hori-
zons (ARR-2025-2AQXS44H6Z8GQAG2). Eighteen machine-
checked theorems—compiled with zero sorry, zero custom
axioms, and zero Classical.choice—certify the nonneg-
ativity and source-preservation algebra of the Landauer-
linear creation bound W≥Rk BTln 2(1 −δ )H(ε), de-
creasing c1/M staircase excess via constructive rationals,
the exact binary-symmetric-channel convolution inverse
e∗
1 = (e∗ −q )/(1 − 2q) and critical-angle impossibility be-
yond θc = 2 arcsin
q
H−1
2 (δ), the adversary access thresh-
old kmin = R−Rmin+1, inter-record parity work extraction
Wext = (k− 1)kBTln 2, the event-inclusive sector second
law ΣεA = ΣA + Ii −I f , zero-gap thermal permutation
invariance and (D, M) contrast–polarization swapping, the
branch-averaged Cauchy–Schwarz emergence speed limit
2ΣA≥B 2, the exact factor- R parallel-broadcast advan-
tage, maintenance-power scaling, intersubjectivity agree-
ment bounds, and SI-2019 adiabatic drift-filter flight arith-
metic. A zero-float Python verifier audits 16 canonical
certificates across four verification modes using certified
rational series brackets for ln, log2, H2, multi-copy noisy
BSC mutual information, and ( f/2) coth(f/2), passing 33
unit, forgery-rejection, and AST tests.
1 Introduction and Scope
Quantum Darwinism identifies classical objectivity with
redundant environmental encoding: an event ε becomes
a fact at level ( R, δ) when at least R disjoint environ-
ment fragments each retain accessible mutual information
at least (1 −δ )H(ε) [2, 3]. InThe thermodynamic bud-
get of objectivity[1], Chung computes the complete mini-
mal thermodynamic accounting for creating, maintaining,
propagating, and un-making objective records in a driven
broadcast model with N initially thermal qubit registers,
and instantiates the budget on two physical instruments
(a total-absorption calorimeter and an adiabatic magnetic
drift filter).
A central structural insight of [1]—that objective records
in re-thermalizing media are nonequilibrium steady states
whose persistence requires continuous dissipation P =
RkBTln 2 γ g(δ)—directly parallels the thermodynamic
Resource Boundaryformalism for living systems [ 6], where
finite bioenergetic throughput bounds the maintenance
of non-equilibrium structural order. Here we deliver an
independently auditable formal verification suite covering
both the exact mathematical core of [1] and its quantitative
crossing into physiological ATP maintenance horizons at
T= 310 K.
Boundary of formalization.Our Lean 4.35.0 devel-
opment formalizes the exact finite-dimensional algebraic,
combinatorial, order-theoretic, and SI-2019 rational in-
equalities underlying Eqs. (1)–(7) and Secs. II–IX of [ 1];
continuous-time quantum master equations, Mrs. Gerber’s
Lemma over general channels, and experimental detector
noise models are taken as cited premises [ 1, 4, 5] whose
algebraic consequences and concrete parameter witnesses
are audited without floating-point error.
2 Constructive Lean 4.35.0 Formal-
ization
The file lean/ThermoObjectivityCert.lean com-
piles cleanly under Lean 4.35.0 ( lake build, 1.0 s, zero
warnings) and passes an automated #print axioms au-
dit confirming zero sorryAx, zero custom axioms, and
zero Classical.choice across all 18 exported theorems
(Table 1).
Two theorems merit particular mathematical emphasis:
 Exact BSC Misalignment Dichotomy (Theo-
rems 4–6).Writing q = sin2(θ/2) and e∗ = H−1
2 (δ)
in common denominator D >0, Theorem 4 proves
1

--- Page 2 ---
Table 1:Summary of the 18 constructive Lean 4.35.0 theorems in lean/ThermoObjectivityCert.lean (zero sorry, zero
Classical.choice, zero warnings).
# Lean Theorem Identifier Ref. in [1] Exact Certified Statement (Scaled Integers / Naturals)
1creation_work_linear_lower_boundEq. (2)k BTln 2,1−δ, H≥0∧W≥Rk BTln 2(1−δ)H⇒W≥0
2creation_per_fragment_sum_preservedEq. (1)→(2)I sum ≥req∧I fin ≥H⇒I sum +I fin −H≥req
3staircase_excess_decreases_with_stepsSec. IVk BT, L,1
2 −e≥0∧0< M 1 ≤M 2 ⇒c 1/M2 ≤Q c1/M1
4misalignment_bsc_inverse_identityEq. (4)e ∗
1(D−2q) =D(e ∗ −q)⇒e ∗
1(D−q) + (D−e ∗
1)q=De ∗
5misalignment_beyond_critical_impossibleEq. (3) 0< D∧2q < D∧0≤e 1 ∧e ∗ < q⇒De ∗ < e1(D−q) + (D−e 1)q
6misalignment_inner_error_monotoneEq. (4) 2e ∗ ≤D∧q 1 ≤q 2 ⇒(e ∗ −q 2)(D−2q 1)≤(e ∗ −q 1)(D−2q 2)
7access_threshold_impossibilitySec. VIR min ≤R∧k < R−R min + 1⇒R−k≥R min
8access_threshold_tightnessSec. VI 1≤R min ≤R⇒k min ≤R∧R−k min =R min −1< Rmin
9inter_record_extraction_balanceSec. VI 1≤k∧0≤L⇒kL−(k−1)L=L∧(2≤k⇒L≤W ext)
10sector_second_law_erasure_and_consolidationEq. (5) Σ A ≥0⇒(I f = 0⇒Σ εA ≥I i)∧(Σ A = 0∧I f =I i ⇒Σ εA = 0)
11zero_gap_permutation_no_recordSec. VIIIp 0 =p 1 =m⇒D c =M=D flip
c =M flip = 0
12controlled_flip_swaps_contrast_and_polarizationSec. VIII (p 0, p1)7→(p 0, D−p1)⇒D ′
c =M∧M ′ =D c ∧ |D′
c|+|M ′|=|D c|+|M|
13speed_limit_branch_cauchy_schwarzEq. (7) Σ bAb ≥2L 2
b ∧L 0 +L 1 ≥B∧2Σ = Σ 0 + Σ1,2A=A 0 +A 1 ⇒2ΣA≥B 2
14parallel_vs_sequential_dissipation_ratioSec. VIII Σ par(2aτ) =RB 2 ∧Σ seq(2aτ) =R 2B2 ⇒Σ seq =RΣ par
15emergence_rate_geometric_mean_boundSec. VIII 2(¯στ)(¯aτ)≥(R∆) 2 ⇒(R∆) 2 ≤2¯σ¯aτ2
16maintenance_power_propertiesEq. (6)k BTln 2, γ >0∧1−2e ∗,log 2 ≥0⇒P≥0∧(1−2e ∗ = 0⇒P= 0)
17agreement_upper_bound_scaledSec. IIe≤D∧1≤R⇒(D−e) R +e R ≤D R
18drift_filter_flight_arithmeticSec. IXc= 299792458, v z = 260000⇒1153< c/v z <1154∧33< r 10m/c(ns)<34
that e∗
1 = (e∗−q)/(1−2q) is the exact inverse of binary-
symmetric-channel convolution, e∗
1(1−q)+(1 −e∗
1)q =
e∗. Theorem 5 proves constructively that for q > e∗
and any e1 ≥ 0, the composed flip error strictly ex-
ceeds e∗, certifying that objectivity at deficit δ is im-
possible at any work beyond θc = 2 arcsin
√
e∗ (Fig. 1).
Theorem 6 certifies the monotonicity ( q1 ≤q 2 ⇒
e∗
1(q2) ≤e ∗
1(q1)), explaining why optimal work rises
monotonically fromRk BTln 2(1−δ) atθ= 0 to the
full Landauer ceilingRk BTln 2 atθ=θ c.
 Constructive Branch Cauchy–Schwarz Speed
Limit (Theorems 11–14).Theorems 11–12 es-
tablish that zero-gap thermal registers admit zero
record creation under permutations alone and that
an ε-controlled flip exchanges branch contrast Dc
with common polarization M, keeping |Dc| + |M|
invariant. Theorem 13 proves the exact two-
branch Cauchy–Schwarz composition (Σ0 + Σ1)(A0 +
A1) ≥ 2B2 from per-branch optimal-transport bounds
ΣbAb ≥ 2L2
b and L0 + L1 ≥B via the nonnegative
square (Σ 0A1 − Σ1A0)2 ≥ 0 without invoking real
square roots. Theorem 14 establishes the exact factor-
R dissipation advantage of parallel broadcasting over
sequential writing under a shared deadline τ and per-
register activity capa cap (Fig. 2).
3 Zero-Float Verifier and 16
Canonical Certificates
Our standalone verifier src/thermo_objectivity_verif
ier.py enforces strict JSON typing (rejecting bool/int
coercion) and zero floating-point arithmetic, confirmed by
an AST audit forbidding float constants and floating-
point libraries. Every transcendental quantity is enclosed
by exact rational series with certified remainder bounds:
1. ln (x) is reduced to r∈ [2/3, 4/3] via x = 2kr with
ln 2 = 2 ln(4/3) + ln(9/8) and evaluated by ln(r) =
Figure 1:Optimal creation work per record W/(RkBTln 2) =
1 −H 2(e∗
1) versus basis misalignment θ for four deficits, with
exact critical angles θc(δ) (dots) hitting the Landauer ceiling.
Diamonds and crosses mark verified certificates C02 (e∗
1 = 1/18)
andC04(super-criticalq= 1/6> e ∗ = 1/10, unreachable).
2 PT−1
m=0 u2m+1/(2m + 1) (u = (r− 1)/(r + 1), |u| ≤
1/5) plus exact geometric remainder 2 |u|2T+1 /((2T +
1)(1 −u 2)), yielding exact brackets for log2, H2(p),
andg(δ) = 1
2 (1−2e ∗) log2((1−e ∗)/e∗).
2. (f/2) coth(f/2) for constant-affinity driving (Sec. VIII
of [1]) is bracketed via scaling y = f/2m ≤ 1/2, Taylor
truncation of ey with Lagrange remainder 2yN+1 /(N +
1)!, andm-fold squaring.
3. SI-2019 physical constants are represented
as exact rationals: c = 299 792 458 m/s,
h = 662 607 015 /1042 J·s , kB/e =
138 064 900/1 602 176 634 meV/K.
Table 2 summarizes all 16 canonical certificates
(C01–C16) across four independent verification modes.
2

--- Page 3 ---
Figure 2: Left:Emergence speed limit Σ A≥ 1
2 R2(1 −2e∗)2 at R = 10, e∗ = 0.1, comparing the asymptotic boundary ( f→ 0),
the constant-affinity f = 2 drive (exact factor coth 1 ≈ 1.3130), saturated certificate C09 (2ΣA = 64), and ruled-out sub-bound
witness C10 (2ΣA = 60 < 64).Right:Exact factor- R dissipation advantage of parallel broadcasting ( ∝R ) over sequential
recording (∝R 2) ata capτ= 10.
Table 2:Canonical certificate suite (THERMO-OBJECTIVITY-CERT-1.0, 16/16 verified by zero-float verifier).
ID Mode Target Regime / Physical Witness Exact Certified Quantities
C01Mode 1 Pointer basis (q= 0),R= 10,e ∗ = 1/10,M= 20 staircaseδ∈[0.468995,0.468996],W min/(kBTln 2)∈[5.310044,5.310045]
C02Mode 1 Sub-critical misalignmentq= 1/20< e∗ = 1/10,R= 8 Exacte ∗
1 = 1/18,Wopt/(kBTln 2)∈[5.523652,5.523653]
C03Mode 1 Critical angle boundaryq=e ∗ = 1/8 (θc),R= 12 Exacte ∗
1 = 0, hits Landauer ceilingWopt/(kBTln 2) = 12
C04Mode 1 Super-criticalq= 1/6> e ∗ = 1/10, biasedp= 1/4,R= 6reachable = false; witnesse 1 = 0 gives error 1/6>1/10
C05Mode 2 Access impossibility:R= 12, Rmin = 5, k= 7< kmin = 8can reduce = false, 5 survive; parityWext = 6kBTln 2
C06Mode 2 Silent CNOT consolidation atk=k min = 8 (R= 12, Rmin = 5)can reduce = true, ΣA = 0, If =Ii ⇒ΣεA = 0
C07Mode 2 Full erasure ofk= 10 perfect copies (R= 10, Rmin = 1) ExtractsW ext = 9kBTln 2, dissipates ΣεA = ln 2
C08Mode 2 Noisyk= 2 BSC(e= 0.1) extraction (Chung Sec. VI) Σ A = 0,Wext/kBT∈[0.221753,0.221754], ΣεA =Ii ∈[0.514374,0.514375]
C09Mode 3 Speed-limit saturation:R= 10, e∗ = 1/10,Σ = 4, A= 8 2ΣA= 64 =R 2(1−2e∗)2;g(δ)∈[1.267970,1.267971]
C10Mode 3 Forbidden sub-bound witness:R= 10, e∗ = 1/10,Σ = 3, A= 10admissible = false: 2ΣA= 60<64
C11Mode 3 High-fidelity divergencee∗ = 1/100,f= 2 affinity driveg(δ)∈[3.248384,3.248385], (f/2) coth(f/2)∈[1.313035,1.313036]
C12Mode 3 Relaxed deficite ∗ = 1/4 + zero-gap thermal invarianceg(δ)∈[0.396240,0.396241],p 0 =p1 = 1/2⇒D′ =M ′ = 0
C13Mode 4 Adiabatic drift filter (1 T, 28 GHz, 0.66 meV,r= 10 m)c/v z ∈[1153.047,1153.048],r/c∈[33.356,33.357] ns,Tq ∈[1.3437,1.3438] K
C14Mode 4 Total-absorption calorimeter (20 GeV hadron shower) Quadratureσ 2 = 1.6025 %2; variance reduction (2.1/1.29)2 ≈2.650
C15Mode 4 Bio Resource Boundary (Regime II, 310 K,R= 100, γ= 104) Required∈[46 956.856,46 956.857] ATP/s<5×10 5 ATP/s cap
C16Mode 4 Bio Resource Boundary breach (310 K,R= 1000, e∗ = 0.01, γ= 106) Required∈[1.2029×10 8,1.2030×108] ATP/s>5×10 5 ATP/s cap
4 Instruments and the Biological
Resource-Boundary Bridge
Mode 4 certifies exact per-event energetics across both
physical instruments in [ 1] and extends Eq. (6) to cel-
lular bioenergetics. In C13, exact SI-2019 arithmetic
confirms that an 18 .6 keV electron drifting at vz =
2.6 × 105 m/s in a 1 T adiabatic drift filter is outrun
by its 28 GHz cyclotron photons by a factor c/vz ∈
[1153.047, 1153.048], escaping a 10 m laboratory radius in
r/c∈ [33.356, 33.357] ns, with entry-quantum temperature
Tq = hν/kB ∈ [1.3437, 1.3438] K and mean photon count
Erad/(hν)∈[5.6995,5.6996] at 28 GHz (or∼9 across the
decelerating chirp spectrum).
In C15–C16 (Fig. 3), we evaluate Chung’s exact main-
tenance law P = RkBTln 2 γ g(δ) at physiological tem-
perature T = 310 K ( kBT≈ 26.714 meV) against the
5 × 105 ATP/s single-mitochondrion bioenergetic ceiling
(∆GATP ≈ 500 meV) analyzed in the Resource-Boundary
framework [ 6]. Maintaining R = 100 noisy records
(e∗ = 0 .10, γ = 10 4 s−1) consumes 4 .696 × 104 ATP/s
(sustainable Regime II, C15), whereas tightening fidelity to
e∗ = 0.01 at R = 1000 and γ = 106 s−1 drives maintenance
power to 1.203 × 108 ATP/s—exceeding the mitochondrial
ceiling by 240× (C16). This quantitatively demonstrates
how Chung’s logarithmic divergence g(δ) → ∞as δ→ 0
enforces a sharp thermodynamicObjectivity Horizonin
living systems.
5 Reproducibility and Verification
Every theorem, certificate, figure, and negative test repro-
duces deterministically from the public repository:
3

--- Page 4 ---
Figure 3: Left:Logarithmic divergence of the maintenance coefficient g(δ) as e∗ → 0 with certified operating points C11, C09,
and C12.Right:Evaluation of Eq. (6) in ATP/s at T = 310 K against a single-mitochondrion 5 × 105 ATP/s Resource Horizon,
separating sustainable Regime II (C15) from horizon breach (C16).
1. Lean 4.35.0 kernel verification: (cd lean &&
lake build) (18 theorems, zero sorry, zero
Classical.choice).
2. Zero-float certificate audit: python -m src.thermo_o
bjectivity_verifier certificates(16/16PASS).
3. Unit, forgery-rejection, and AST test suite: pytest
-q (33/33 passing, rejecting 15 adversarial certificate
forgeries across all 4 modes).
4. Cryptographic integrity: all source files, certificates,
figures, and PDF are pinned inMANIFEST.sha256.
AI Disclosure and Licensing.Prepared by Lluis
Eriksson using Google Antigravity for Lean 4 proof engi-
neering, zero-float verifier construction, and adversarial
audit; all mathematical claims were machine-checked by
the Lean 4.35.0 kernel and exact rational tests. Manuscript
and figures are licensed CC-BY-4.0; code, Lean proofs, and
certificates are licensedMIT.
References
[1] W. Chung,The thermodynamic budget of objectivity,
arXiv:2611.34909v1[quant-ph] (2026).
[2] W. H. Zurek,Quantum Darwinism, Nat. Phys.5, 181
(2009).
[3] H. Ollivier, D. Poulin, and W. H. Zurek,Environment
as a witness, Phys. Rev. A72, 042113 (2005).
[4] A. D. Wyner and J. Ziv,A theorem on the entropy of
certain binary sequences, IEEE Trans. Inf. Theory19,
769 (1973).
[5] J. M. Horowitz, K. Zhou, and J. L. England,Minimum
energetic cost to maintain a target nonequilibrium state,
Phys. Rev. E95, 042102 (2017).
[6] L. Eriksson,Geometry, Membranes, and Life
as a Resource Boundary, AIRR.SCIENCE
ARR-2025-2AQXS44H6Z8GQAG2(2025/2026).
4
