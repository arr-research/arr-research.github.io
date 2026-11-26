# Mito-Polaritons Meet the Resource Boundary: Exact Hopfield A^2 Invariants, Thermodynamic Maintenance Horizons, and Constructive Lean 4 Certificates for the 71-THz Mitochondrial Quantum State

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-1E91AXEJYT890TQC` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/mito-polariton-resource-boundary-certificates (`v1.0.2`)  
**Canonical PDF SHA-256:** `802961ba37cd8be849381ec5bbf9cb37ef71cc2ee2a0b667bd428d99d0302dd8`

## Abstract

We apply our operational coherence-maintenance and resource-boundary framework (ARR-2025-2AQXS44H6Z8GQAG2 and companion 2025-2026 AIRR.SCIENCE records) to audit the 71.0-THz mitochondrial cristae mito-polariton model of Yang, Gu, and Song (bioRxiv:10.64898/2026.09.10.750628v1, Sep. 2026). Backed by a zero-floating-point verification suite (MITO-POLARITON-BOUND-CERT-1.0) comprising 18 constructive Lean 4.35.0 theorems (0 sorry, 0 custom axioms, 0 Classical.choice), 16 canonical JSON certificates, and 30 unit/forgery/AST tests, we prove: (i) at nu_- = 71 THz and omega_0 = 87 THz, coupling enters the ultrastrong regime (eta = 1264/6177 ~ 0.2046 > 0.1), where the gauge-invariant Hopfield A^2 Thomas-Reiche-Kuhn sum rule predicts an upper polariton at 7569/71 ~ 106.61 THz (+3.61 THz above RWA's 103 THz), testable in D2O; (ii) at T = 310 K, bulk-water picosecond dephasing exceeds the mitochondrial ATP power budget by 5e5, separating zero-maintenance passive vacuum-dressed polaritons (Regime I, C_Delta = 0) from active non-equilibrium coherence (Regime II, requiring kappa_down <= 2e6 s^-1); (iii) cristae collar suppression (RIP-U) cannot eliminate an irreducible omega = 0 Davies pure-dephasing floor; (iv) for N bosonic CH2 stretches in the vacuum regime (n_th < 2e-6 at 310 K), exact 4x4 Bogoliubov diagonalization of the Coulomb-gauge A^2 Hamiltonian yields lower-polariton matter weight w_mat^Coul = 7569/12610 ~ 0.6002 > 1/2, forcing local Markovian dephasing into N-1 dark modes at rate w_mat^Coul ((N-1)/N) gamma_loc > (1/4) gamma_loc (zero 1/N collective protection), while an S-lamella coupled cristae stack outperforms factorized single-bilayer water-band shielding whenever C_S(delta+beta)+r < 1; and (v) a four-test experimental falsification matrix discriminates classical artifacts, Regime I, and Regime II.

## Full Extracted Text

--- Page 1 ---
Mito-Polaritons Meet the Resource Boundary: Exact Hopfield
A2 Invariants, Thermodynamic Maintenance Horizons, and
Constructive Lean 4 Certificates for the 71-THz Mitochondrial
Quantum State
Lluis Eriksson
Independent Researcher (https://github.com/lluiseriksson)
Operational Synthesis ConnectingARR-2025-2AQXS44H6Z8GQAG2andbioRxiv:2026.09.10.750628v1
November 26, 2026
Abstract
In September 2026, Yang, Gu, and Song
(bioRxiv:10.64898/2026.09.10.750628v1) reported
an anomalous 71.0-THz mid-infrared oscillation mode unique
to living cells and intact mitochondrial cristae, modeling it as
a lipid CH2 vibrational polariton (“mito-polariton”) splitting
the 87-THz CH2 stretch into 71 THz and 103 THz branches
and showing ∼ 10% ATP modulation under weak resonant
irradiation. Here we apply our previously published opera-
tional coherence-maintenance and resource-boundary frame-
work (ARR-2025-2AQXS44H6Z8GQAG2, Dec. 2025 / Jul. 2026,
and its 2025–2026 AIRR.SCIENCE companion series) to
audit the mito-polariton hypothesis quantitatively and derive
sharp, falsifiable predictions backed by a zero-floating-point
verification suite (MITO-POLARITON-BOUND-CERT-1.0) with
18 constructive Lean 4.35.0 theorems (0 sorry, 0 custom ax-
ioms, 0 Classical.choice), 16 canonical JSON certificates,
and 30 unit/forgery/AST tests. Five exact results emerge:
(i) at ν− = 71 THz and ω0 = 87 THz, coupling enters the
ultrastrong regime (η = g/ω0 = 1264/6177 ≈ 0.2046 > 0.1),
where the gauge-invariant Hopfield A2 term (Thomas–
Reiche–Kuhn sum rule ν+ν− = ω2
0) predicts an upper
polariton at νHop
+ = 7569/71 ≈ 106.61 THz—a +3.61 THz
blue-shift over RWA’s 103 THz, directly testable in D2O
where water’s O–D stretch clears the 100–110 THz window;
(ii) by our Conditional Maintenance Work Theorem at
T = 310 K ( kBT≈ 26.71 meV, ∆ GATP ≈ 518.2 meV),
bulk-water picosecond dephasing ( κbulk ∼ 1012 s−1)
exceeds the entire mitochondrial ATP power budget
(Pmito/kBT∼ 1.94 × 106 s−1) by 5 × 105, cleanly separating
a zero-maintenance passive vacuum-dressed polariton
(Regime I, C∆ = 0) from active non-equilibrium coherence
(Regime II, C∆ > 0, requiring κ↓ ≲ 2 × 106 s−1); (iii) cristae
collar suppression (rip-u) and spectral detuning into
the 60–80 THz quiet window suppress ω̸ = 0 decay but
cannot remove an irreducible Davies ω = 0 pure-dephasing
floor κ0; (iv) for N bosonic CH2 stretches in the vacuum
regime (¯nth < 2 × 10−6 at 310 K), exact 4 × 4 Bogoliubov
diagonalization of the Coulomb-gauge A2 Hamiltonian
splits the N dipoles into 1 bright mode and N− 1 or-
thogonal dark modes with lower-polariton matter weight
wCoul
mat = ω2
0/(ω2
0 +ν2
−) = 7569/12610 ≈ 0.6002 > 1/2, forcing
local vibrational dephasing to scatter into the dark manifold
at rate Γ MP−→D = wCoul
mat
N−1
N γloc > 1
4 γloc (zero 1 /N
collective protection against Markovian local dephasing),
while an S-lamella coupled cristae stack outperforms
factorized single-bilayer water-band shielding whenever
CS(δ+β)+ r <1; and (v) we deliver a four-test experimental
falsification matrix separating classical artifacts, Regime I,
and Regime II.
1 Introduction, Scope, and Prior
Program
In December 2025 (revised July 2026), we formulated
an operational resource-boundary program [ 3] (supported
by [2, 7, 5, 6, 4]) connecting three layers:geometryas cross-
interface suppressibility,membranesas engineered collars
implementing upper-rate suppression (rip-u), andlifeoper-
ationally as sustained maintenance of internal organization
under finite thermodynamic power budgets. Nine months
later, Yang, Gu, and Song [ 12] reported FTIR evidence for
a 71.0-THz (2368 cm−1) mode present exclusively in living
cells, intact tissues, and structurally preserved mitochondria,
disappearing upon cristae disruption or drying, and linked
via resonant 71/87-THz irradiation to an approximate 10%
increase in cellular ATP production.
Scope and epistemic hygiene.We emphasize two strict
boundaries. First, [ 12] is anunrefereed bioRxiv preprint
whose experimental claims await independent replication; we
neither endorse nor assume its unverified biological conclu-
sions, but rather apply exact algebraic and open-quantum-
system theorems to extract hard physical constraints and fal-
sifiable tests. Second, following [3], our thermodynamic main-
tenance bounds are unconditional in the law-grade energy-
pinching ∆-track (C∆(ρ) = S(ρ∥∆[ρ])) and explicitly condi-
tional on approximate Petz/Pythagorean sufficiency [8] when
lifted to general membrane coarse-grainings (E-track).
1

--- Page 2 ---
2 Five Exact Theoretical Bridges
1. Gauge-Invariant Hopfield A2 Shift vs. Naive RWA.
Yang, Gu, and Song [ 12] model the 71 .0-THz line as the
lower polariton MP− of lipid CH2 stretches (ω0 ≈ 87 THz)
coupled to cristae-confined infrared modes, inferring a sym-
metric rotating-wave-approximation (RWA) upper branch
νRWA
+ = 87 + 16 = 103 THz hidden inside the 90–110 THz
H2O/amide-A band. However, at resonant coupling ωc = ω0
with splitting ΩR ≳ 32 THz (η = g/ω0 > 0.2), RWA breaks
gauge invariance and violates the Thomas–Reiche–Kuhn
(TRK) sum rule [ 10, 11, 9]. Including the diamagnetic A2
coefficient D = g2/ω0, the exact Hopfield secular equation
forλ=ν 2 is
λ2 −(ω 2
c +ω 2
0 + 4g2)λ+ω 2
c ω2
0 = 0.(1)
At resonance ( ωc = ω0), (1) yields ν+ν− = ω2
0 and ν+ −
ν− = 2g identically (Lean Thm. 1), with strictly positive
discriminant (ω2
c −ω 2
0)2 +8g2(ω2
c +ω2
0)+16 g4 ≥ 0 preventing
superradiant collapse (Thm. 2). Setting ω0 = 87 THz and
ν− = 71 THz forces
νHop
+ = 872
71 = 7569
71 ≈106.6056 THz,
νHop
+ −ν RWA
+ = 256
71 ≈+3.61 THz,
(2)
and normalized coupling η = g/ω0 = 1264/6177 ≈ 0.2046 >
1/5 (Thms. 3–4, Fig. 1). Because D2O shifts the water
stretch from ∼ 102 THz down to ∼ 74.9 THz (2500 cm−1),
substituting D2O clears the 100–110 THz window to directly
resolve 103 THz vs. 106.61 THz, while CD2 lipid deuteration
shifts bareω 0 to 87/
√
2∈(61.5,61.6) THz (Thm. 5).
2. Bioenergetic ATP Resource Horizon (Regime I vs.
Regime II).By Theorem 4.1 and Theorem 9.1 of [ 3, 2],
under battery-assisted thermal operations at bath temper-
ature T with Markovian thermal-fixed-point generator and
rate floor ˙C∆,loss(ρ) ≥κ ↓(ϵ)C∆(ρ), sustaining coherence
C∆(ρ)≥C 0 demands minimal continuous power
P⋆
maint(ρ)≥k BT ˙C∆,loss(ρ)≥k BT κ↓(ϵ)C 0.(3)
At physiological T = 310 K ( kBT≈ 26.71 meV,
kBT/h≈ 6.46 THz), one ATP hydrolysis releases ∆ GATP ≈
50 kJ/mol≈ 518.2 meV≈ 19.40 kBT (while h· 71 THz≈
293.63 meV≈ 11.0 kBT, so 2 hν− ≈ 587.3 meV> ∆GATP,
Thm. 9). Even allocating a mitochondrion’s full flux
RATP ∼ 105 ATP/s gives Pmito/(kBT) ≈ 1.94 × 106 s−1.
Consequently, bulk-water picosecond vibrational dephasing
(κbulk ∼ 1012 s−1) exceeds the entire mitochondrial budget
at C0 = 1 nat by a factor of 5 × 105 (Thms. 6–8, Fig. 2a).
This proves a sharp operational dichotomy:
 Regime I (Passive Vacuum-Dressed Polariton,
C∆ = 0):The 71-THz mode is a stationary energy
eigenstate of the cristae cavity. Its ∆-track active co-
herence maintenance power is identically zero (Thm. 7);
metabolic work maintains membrane geometry, not off-
diagonal coherence.
 Regime II (Active Non-Equilibrium Coherence,
C∆ > 0):Thermodynamically feasible at C0 ∼ 1 nat
onlyif cristae engineering suppresses the effective de-
phasing floor below κ↓ ≲ 2 × 106 s−1 (τcoh ≳ 0.5 µs).
Moreover, by [5] (Thm. 10), periodic endpoint refresh
(W0/Tper → 0) must never be conflated with continuous
holding under (3).
3. Cristae Collar RIP-U vs. Irreducible ω = 0Davies
Floor.Detuning ν− = 71 THz into the 60–80 THz quiet
gap moves three times further from the 95-THz water/amide
edge than bare 87 THz (∆− = 24 = 3∆0), giving a Lorentzian
bath-density suppression factor (∆ 2
− + Γ2)/(∆2
0 + Γ2) ≥ 5
whenever Γ ≤ ∆0 (Thm. 14). Simultaneously, the lipid bi-
layer collar enforces an upper-rate ceiling κ↑(ϵ) ≤κ 0 + B0qϵ
(rip-u, [3]). Yet by [ 7] (Thms. 12–13, Fig. 2b), slow fluc-
tuations of the membrane potential ∆Ψ m at ω≃ 0 enter
the Davies Dirichlet form [ 1] E(0)
σ (O) = γ(0)
2 ∥[S(0), O]∥2
2,σ
(audited in Mode 3a via the equivalent GNS trace norm
γ0
2 Tr(σ[S(0), O]†[S(0), O]), matching KMS identically on
maximally mixed σ and sharing the exact vanishing con-
dition [ S(0), O] = 0): whenever S(0) distinguishes MP±
(s− ̸= s+), κ↓(ϵ) ≥κ 0 > 0 persists foreverycollar thickness
ϵ, fixing an unremovable resource horizon.
4. Bosonic Dark-Mode Leakage and Lamellar Crista
Stack Mapping.Coupling N identical bosonic lipid CH2
stretches {bj}N
j=1 (ω0 = 87 THz) uniformly ( g0 = g/
√
N) to
one crista cavity photon mode a isolates a single symmetric
bright Dicke mode B = N−1/2 PN
j=1 bj and N− 1 orthogonal
dark modes D (Thm. 15). At physiological T = 310 K,
ℏω0/(kBT) = h· 87 THz/(kB · 310 K) ≈ 13.47 > 13, so the
Bose–Einstein thermal occupation satisfies ¯nth = (eℏω0/kBT −
1)−1 < 2 × 10−6 (true value ≈ 1.41 × 10−6, placing the
lipid ensemble firmly in the vacuum/single-excitation bosonic
regime, distinct from half-filled fermionic SSH chains [ 6]).
From exact 4 × 4 Bogoliubov diagonalization of the resonant
Coulomb-gauge A2 Hamiltonian HC = ω0a†a + ω0B†B +
ig(a+a†)(B−B †)+ g2
ω0
(a+a†)2 (ν+ν− = ω2
0), the diamagnetic
A2 term blue-shifts the cavity mode ( ω0 7→
p
ω2
0 + 4g2),
pushing MP− closer to the unshifted matter oscillator ω0
with exact matter and photonic weights
wCoul
mat =|u b|2 − |vb|2 = ω2
0
ω2
0 +ν 2
−
= 7569
12610 ≈0.6002> 1
2,
wCoul
phot =|u a|2 − |va|2 = ν2
−
ω2
0 +ν 2
−
= 5041
12610 ≈0.3998,
(4)
making MP− 60.02% matter-like (Thm. 16, Fig. 3a).
Under site-uncorrelated Markovian vibrational dephasing
γloc
PN
j=1 D[b†
jbj], each single-site excitation |j⟩ = b†
j|0⟩
has overlap |⟨B|j⟩|2 = 1 /N with the bright mode and
1 − 1/N with D, yielding exact bright-to-dark scattering
rate Γ B→D = γloc(1 − 1/N) and polariton-to-dark rate
ΓMP−→D = wCoul
mat
N−1
N γloc ≥ 1
2 wCoul
mat γloc > 1
4 γloc for every
N≥ 2 (Thms. 15–16): unlike static inhomogeneous disor-
der (suppressed when σω ≪ ΩR), local Markovian dephas-
ing enjoyszero1 /N collective protection as N→ ∞, and
2

--- Page 3 ---
the Coulomb-gauge A2 cavity blue-shiftamplifiesmatter-
mediated dark-mode leakage above 50%. Conversely, map-
ping a stack of S lamellar mitochondrial cristae (spacing 20–
40 nm, coupled via crista junctions) directly to the passive
multi-port filter tuple ( S, CS, δ, β, r) of [4]—with S coupled
bilayer cavities, passband tolerance δ across the 60–80 THz
quiet window, inter-crista junction loss defect β, 3(S− 1)
single-port tangential calibration constraints with singular-
value constantCS, and coupled-stack stopband transmittance
r across the 90–110 THz water/amide band—Theorem 17
proves that whenever CS(δ + β) + r < 1, any factorized
single-bilayer model suffers worst-case water-band leakage
≥ 1 −C S(δ + β) > r(Fig. 3b), explaining why intact multi-
crista stacking is necessary for broadband shielding.
3 Constructive Lean 4.35.0 Kernel
and Zero-Float Audit
We formalize all 18 algebraic and thermodynamic pillars
in lean/MitoPolaritonBoundCert.lean under Lean 4.35.0
without Mathlib, audited via #print axioms to depend
strictly on propext and Quot.sound (0 sorry, 0 custom ax-
ioms, 0 Classical.choice, 0 warnings; Table 1). Our stan-
dalone verifier src/mito polariton bound verifier.py en-
forces an AST-audited zero-float invariant (zero float lit-
erals, zero float() calls, zero / or /=, zero math/numpy
imports). All 16 canonical certificates ( C01–C16, Table 2)
pass python -m src.mito_polariton_bound_verifier
certificates, and all 30 unit/forgery/AST tests pass un-
derpytest -q.
4 Experimental Falsification Matrix
Table 3 upgrades Section 11 of [ 3] into four concrete ex-
periments decisively discriminating classical artifacts ( H0),
passive vacuum-dressed polaritons (H1: Regime I,C ∆ = 0),
and actively maintained quantum coherence ( H2: Regime II,
C∆ >0).
5 Reproducibility and Availability
All source code, Lean 4 proofs, certificates, figure scripts,
and SHA-256 manifest ( MANIFEST.sha256) are archived
at https://github.com/lluiseriksson/mito-polar
iton-resource-boundary-certificates under MIT
(code/Lean/data) and CC-BY-4.0 (manuscript/figures) li-
censes. Reproduction requires three commands: (cd lean
&& lake build), python -m src.mito_polariton_bound
_verifier certificates, andpytest -q.
AI Assistance Disclosure.Google Antigravity assisted
with Lean 4 proof engineering, zero-float verifier implemen-
tation, test/figure automation, and LaTeX drafting. The
author verified every mathematical derivation, Lean axiom
audit, certificate check, and visual figure inspection, and
takes full responsibility for all contents.
References
[1] E. Brian Davies. Markovian master equations.Commu-
nications in Mathematical Physics, 39:91–110, 1974.
[2] Lluis Eriksson. The conditional maintenance work the-
orem: Operational power lower bounds from energy
pinching and a split-inclusion blueprint for type III
AQFT, December 2025. AIRR.SCIENCE record ARR-
2025-76C3S3SSMP8HJ8NF (ai.viXra:2512.0061).
[3] Lluis Eriksson. Geometry, membranes, and life as
a resource boundary: A correct-by-construction op-
erational pipeline from static suppression to mainte-
nance costs, December 2025. AIRR.SCIENCE record
ARR-2025-2AQXS44H6Z8GQAG2 (ai.viXra:2512.0085,
v1 Dec 2025; v2 Jul 2026).
[4] Lluis Eriksson. Architecture-dependent decoherence
suppression in passive quantum networks: Irreducible
channel mixing, squared rate gaps, and the price in dwell
time, August 2026. AIRR.SCIENCE record ARR-2026-
4F7SF8FXM18ANAXH.
[5] Lluis Eriksson. Maintenance is not restoration:
Endpoint no-go theorems, exact SSH resource
horizons, and quantum rapid-replacement equality,
July 2026. AIRR.SCIENCE record ARR-2026-
77MR0BB1E487CAYR.
[6] Lluis Eriksson. Many-body filling turns soft spec-
tral leakage into a maintenance floor: Exact filled-
SSH sum rules and an interaction-stable obstruc-
tion, July 2026. AIRR.SCIENCE record ARR-2026-
6YFENMGGBY9PPBF1.
[7] Lluis Eriksson. RIP-U and the ω = 0 obstruction in
Davies dynamics: Upper envelopes, witness floors, and
falsification protocols for separation-dependent deco-
herence rates, January 2026. AIRR.SCIENCE record
ARR-2026-53WA9C4RB39JRRXF.
[8] Omar Fawzi and Renato Renner. Quantum conditional
mutual information and approximate Markov chains.
Communications in Mathematical Physics, 340:575–611,
2015.
[9] Anton Frisk Kockum, Adam Miranowicz, Simone De Lib-
erato, Salvatore Savasta, and Franco Nori. Ultrastrong
coupling between light and matter.Nature Reviews
Physics, 1:19–40, 2019.
[10] John J. Hopfield. Theory of the contribution of excitons
to the complex dielectric constant of crystals.Physical
Review, 112(5):1555–1567, 1958.
[11] Kazimierz Rz¸ a˙ zewski, Krzysztof W´ odkiewicz, and
W. ˙Zakowicz. Phase transitions, two-level atoms, and
the A2 term.Physical Review Letters, 35(7):432–434,
1975.
[12] Yu Yang, Zhenglong Gu, and Bo Song. A quantum
state of mitochondria in the living cell, September
3

--- Page 4 ---
Table 1: All 18 constructive Lean 4.35.0 theorems in MitoPolaritonBoundCert.lean (0 sorry, 0 Classical.choice), with
exact statements.
# Lean Theorem Identifier Exact Formalized Statement (overZorN)
1hopfield trk vieta invariantsν +ν− =ω 2
0 ∧ν + −ν − = 2g=⇒ν 2
+ +ν 2
− = 2ω2
0 + 4g2 ∧ν 2
+ν2
− =ω 4
0
2hopfield no superradiant instabilitya, b, g 2 ≥0 =⇒(a+b+ 4g 2)2 −4ab= (a−b) 2 + 8g2(a+b) + 16g 4 ≥0
3mito 71 87 103 rwa vs hopfield shift71·103 + 16 2 = 872 = 7569; 10660·71<756900<10661·71; 7·71<2·256
4mito ultrastrong coupling regime7569−71 2 = 2528,2·71·87 = 12354, η= 1264/6177>1/5 (5·1264>6177)
5isotope cd2 and d2o window clearance2·615 2 <870 2 <2·616 2 (87/
√
2∈(61.5,61.6)); 75<100<103<7569/71
6maintenance power pythagorean splitk BT, Fdiag ≥0∧k BTσ≤P min ∧σ=F diag +C loss ∧κ ↓C0 ≤C loss =⇒k BTκ↓C0 ≤P min
7passive equilibrium zero coherence costk BT, κ0, C0 >0 =⇒k BT(κ0 ·0) = 0∧0< k BT(κ0C0) (Regime I vs. II)
8mito resource horizon five order gap20·10 5 = 2·10 6 ∧(5·10 5)·(2·10 6) = 1012 (bulk dephasing horizon)
9two photon 71thz exceeds atp10·267<2936<11·267∧5182<2·2936∧2200<2936 (0.1 meV units)
10endpoint restoration vs continuous holdingM, k BT, κ0, C0 ≥1∧MW 0 < T=⇒MW 0 < T(kBTκ0C0)∧W 0 < T(kBTκ0C0)
11fawzi renner fidelity gap algebraic1≤a≤b=⇒(b−a)a≤(b−a)b∧(a < b→(b−a)a <(b−a)b)
12rip u ceiling vs floor quantifier hygienek BT, C0 ≥0∧κ 0 ≤κ ↓ ≤κ ↑ ≤κ 0 +B ϵ ∧k BTκ↓C0 ≤P min =⇒k BTκ0C0 ≤P min
13davies omega0 dirichlet nonnegγ 0 >0 =⇒γ 0((s− −s +)o12)2 ≥0 (>0 whens − ̸=s + ∧o 12 ̸= 0)
14spectral gap detuning suppression ratio0≤G≤D 0 =⇒5(D 2
0 +G 2)≤(3D 0)2 +G 2 (Lorentzian suppression≥5×)
15collective n dipole bright dark partitionN≥2 =⇒1 + (N−1) =N∧N≤2(N−1)∧γ locN≤2γ loc(N−1)
16bosonic hopfield matter weight and vacuum regime0< ν − < ω0 =⇒2ν 2
− < ω2
0 +ν 2
− <2ω 2
0; 71 2 + 872 = 12610; 13·267<3598
17passive network channel mixing margin0≤r∧C S(δ+β) +r < u=⇒0< u−C S(δ+β)∧r < u−C S(δ+β)
18falsification matrix decidability7569−103·71 = 256>0∧10 12/(2·10 6) = 5·10 5 ∧10<11
Table 2: Summary of all 16 verified MITO-POLARITON-BOUND-CERT-1.0 canonical certificates (C01–C16), with live outputs
fromverify file.
ID Mode / Submode Verified Instance Exact Certified Metrics
C01M1a Hopfield TRKω 0 = 87, ν− = 71 THzν RWA
+ = 103,ν Hop
+ = 7569/71≈106.61, shift +256/71,η= 1264/6177 (USC)
C02M1a Hopfield TRKω 0 = 87, ν− = 79 THzν Hop
+ = 7569/79≈95.81 THz, shift +64/79≈+0.81 THz,η≈0.0966
C03M1b Isotope CD 2 ωc = 87, ω0 = 61.5, g= 15 THz Exact bracketν − ∈[56,57] THz (56.06 THz), no collapse (disc>0)
C04M1b Detuned USCω c = 90, ω0 = 87, g= 18 THz Exact bracketν − ∈[72,73] THz (72.25 THz), disc>0
C05M2a ATP Horizon Regime I (C 0 = 0,κ= 10 12 s−1)P req = 0≤P mito = 1.94×10 6 kBT/s (feasible: passive equilibrium)
C06M2a ATP Horizon Bulk water (C 0 = 1,κ= 10 12 s−1)P req = 1012 >1.94×10 6 kBT/s (infeasible by 5.15×10 5×)
C07M2a ATP Horizon Regime II (C 0 = 1,τ= 1µs)P req = 106 ≤1.94×10 6 kBT/s (feasible active coherence window)
C08M2b Energetics 71-THz vs. ATP + 10 ms refreshhν −/kBT≈10.99, 2hν −/∆GATP ≈1.13, holding/endpoint = 1000×
C09M3aω= 0 Floors − = 3
2 , s+ =− 1
2 , γ0 = 106 Literal 2×2 commutatorC 12 = 2, GNS rateE (0) = 2×10 6 s−1 >0
C10M3a Commutings − =s + = 1, γ0 = 106 CommutatorC= 0,E (0) = 0 (zero-floor decoherence-free subspace)
C11M3b Collarrip-uκ 0 = 5×10 5,B 0 = 1012,q= 1
10 Ceiling 1012 →5.1×10 5 ≥κ 0; Lorentzian bath suppression = 5×exact
C12M3b Deep Collarκ 0 = 105,ω b = 100,Γ = 5 THz Ceiling 2.5×10 10 →4.8×10 5; Lorentzian suppression = 433/97≈4.46×
C13M4a Bosonic DarkN= 10 6 CH2, 71/87 THz, 310 Kw Coul
mat = 7569/12610≈0.6002, Γ/γ loc ≈0.6002, ¯nth <2×10 −6
C14M4a Bosonic DarkN= 10 8 CH2, 79/87 THz, 310 Kw Coul
mat = 7569/13810≈0.5481, Γ/γ loc ≈0.5481, ¯nth <2×10 −6
C15M4b StackS= 5 30 nm cristae,C S = 12, δ=β= 10 −2 12 calibrations; reducible LB 19/25 = 0.76 vs. irreducible 0.01 (76×gap)
C16M4b StackS= 9 25 nm cristae,C S = 25, δ=β= 5×10 −3 24 calibrations; reducible LB 3/4 = 0.75 vs. irreducible 10 −3 (750×gap)
Table 3: Four-test experimental falsification matrix separat-
ing H0 (artifact), H1 (Regime I passive polariton), and H2
(Regime II active coherence).
ProtocolH 0 (Artifact)H 1 (C∆ = 0)H 2 (C∆ >0)
D2O FTIR No 106.6 peak MP + 106.6±0.5 MP + 106.6±0.5
CD2 lipid Unshifted 71ν − →56–58ν − →56–58
2D-IR/∆Ψm No echo PureT 1/inhom.T ∗
2 ≥0.5µs
Oligomycin Unchanged Persists (intact) Drops w/ ATP
2026. bioRxiv preprint 10.64898/2026.09.10.750628v1,
15 September 2026 (unrefereed).
4

--- Page 5 ---
Figure 1:Gauge-Invariant Hopfield A2 Spectrum and Isotope Tests.(a) Exact Hopfield TRK polariton branches
(ν+ν− = ω2
0) versus naive RWA (ω0 ±g ) across η = g/ω0, with live certified witnesses C01 (η = 0.2046, USC) and C02.
(b) Direct +3.61 THz blue-shift of MP + (106.61 vs. 103 THz) exposed when D 2O shifts water absorption to 74.9 THz.
Figure 2:Bioenergetic ATP Resource Horizon and Cristae Collar Suppression.(a) Exact log-log feasibility phase
diagram from Theorem 9.1 at T = 310 K comparing whole-mitochondrion (10 5 ATP/s) and single-crista budgets against
bulk-water dephasing (C06, infeasible by 5 × 105) and microsecond-suppressed Regime II ( C07, feasible). (b)rip-ugeometric
collar decay hitting an irreducibleω= 0 Davies floor (C11).
Figure 3:Bosonic Dark-Mode Dephasing Transfer and Multi-Crista Stack Shielding.(a) Exact Coulomb-gauge
Hopfield lower-polariton matter weight wCoul
mat = ω2
0/(ω2
0 + ν2
−) > 1/2 and dark-mode dephasing transfer Γ MP−→D/γloc =
wCoul
mat
N−1
N vs. η, with certified witnesses C13 (71 THz, 60 .0%) and C14 (79 THz, 54 .8%). (b) Live Mode 4b water-band
transmittance separation between factorized single-bilayer filters and irreducible coupled S-lamella cristae stacks ( C15, C16).
5
