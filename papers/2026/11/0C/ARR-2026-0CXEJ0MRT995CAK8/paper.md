# Thermodynamic Bounds on Infrared-Modulated ATP Synthesis: Separating Photothermal Heating, Passive Polaritonic Catalysis, and Coherent Ratchets at 71 THz

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Thermodynamic Bounds on Infrared-Modulated ATP
Synthesis: Separating Photothermal Heating, Passive
Polaritonic Catalysis, and Coherent Ratchets at 71 THz
Lluis Eriksson
Independent Researcher (https://github.com/lluiseriksson)
Bioenergetic Audit Continuing ARR-2025-2AQXS44H6Z8GQAG2 and ARR-2026-1E91AXEJYT890TQC
November 27, 2026
Abstract
In September 2026, Yang, Gu, and Song
(bioRxiv:10.64898/2026.09.10.750628v1, unrefer-
eed) reported an approximately 10% increase in cellular
ATP levels when living cells are exposed to weak resonant
71/87 THz mid-infrared irradiation, attributing the
effect to a mitochondrial cristae polariton. While our
companion record ARR-2026-1E91AXEJYT890TQC audited
the spectral Hopfield A2 invariants and coherence-holding
horizon, the physical mechanism of the +10% ATP
enhancement remained unaudited. Here we establish
sharp, machine-checked thermodynamic bounds separat-
ing four distinct mechanisms for a +10% steady-state
mitochondrial ATP-synthesis flux (JATP) boost—direct
stoichiometric photon-to-ATP conversion, polaritonic
catalysis (distinguishing static dark-cavity vacuum
ZPE ceilings from irradiance-driven resonant cataly-
sis), micro-hotspot versus bulk photothermal heating,
and active coherent ratchets—while noting that cellu-
lar ATP concentration ([ATP]) can also rise without
mitochondrial flux acceleration via reduced consump-
tion or glycolysis. Backed by a zero-floating-point
verification suite (MITO-ATP-MODULATION-CERT-1.0)
comprising 20 constructive Lean 4.36.0 integer/rational
theorems (0 sorry, 0 grind, 0 Classical.choice,
-DwarningAsError=true), 16 SHA-256 canoni-
cal certificates (C01–C16), and 58 adversarial
pytest checks, five exact results emerge: (i) by
the First Law at ∆GATP = 518.2 meV and
h · 71 THz = 293.63 meV, stoichiometric conversion
requires 2591/1468 ≈ 1.765 > 1.76 absorbed 71-THz pho-
tons per extra ATP (tightened strictly by Carnot eﬀiciency
ηC = 1 − T /Trad); (ii) rational Mercator partial sums
11437/120000 < ln(11/10) < 143/1500 pin the Eyring bar-
rier shift at T = 310 K to |∆Ea|10% ∈ (2.545, 2.547) meV;
deriving the resonant Hopfield A2 upper branch
ν+ = 7569/71 ≈ 106.61 THz gives single-mode ZPE
shift ∆EZPE = 128 71 h · THz ≈ 7.456 meV > 2.92 |∆Ea|10%
as an undiluted collective energetic ceiling, while 1/N
dipole dilution closes static single-enzyme dark catal-
ysis across N ∼ 106–108 uncorrelated dipoles and
an Iinc > 0 flux boost over dark control requires
driven resonant catalysis (forcing +10% oligomycin-
sensitive ATP-linked OCR under fixed P/O stoichiom-
etry); (iii) exact finite-difference Arrhenius kinetics
(∆T10% ∈ (1.52, 1.54) K at Ea = 50 kJ/mol) and
steady-state spherical conduction yield a π-free micro-
hotspot flux floor Imicro = 4κth∆T /R > 729 W/cm2
(734.4 W/cm2 at midpoint 1.53 K), excluding single-
organelle hotspots under 10 mW/cm2 mid-IR by
> 72,900× while exposing ≥ 2000× bulk dish amplifica-
tion; (iv) the dimensionally homogeneous Barato–Seifert
TUR (Var(Jτ ) στ ≥ 2kB ⟨Jτ ⟩2 at explicit window τ = 1 s)
bounds classical Markovian NESS catalysis while First-
Law additive power conservation (Pmaint + PATP ≤ Pin,
with Pmaint ∼ 5 × 105P mito ATP ) constrains active coherent
ratchets; and (v) a four-protocol experimental matrix
separates mitochondrial flux acceleration from con-
sumption/glycolytic [ATP] shifts, bulk heating, and
stoichiometric conversion.
1 Introduction and Epistemic
Scope
In ARR-2025-2AQXS44H6Z8GQAG2 [3], we estab-
lished an operational thermodynamic pipeline link-
ing membrane geometry to continuous coherence
maintenance power. Applying that framework in
ARR-2026-1E91AXEJYT890TQC [4] to the unrefereed
preprint of Yang, Gu, and Song [7] proved that bulk-
water dephasing exceeds the mitochondrial ATP power
budget by 5 × 105, cleanly separating passive vacuum-
dressed polaritons (Regime I, C∆ = 0) from active
non-equilibrium coherence (Regime II, C∆ > 0).
A central empirical claim of [7], however, is that weak
resonant 71/87 THz irradiation elevates cellular ATP lev-
els by ∼ 10% over dark controls. As in [4], we treat [7]
strictly as an unrefereed preprint awaiting independent
replication; our goal is to derive exact, machine-checked
thermodynamic inequalities distinguishing heating arti-
1
```

---

## Page 2

```text
facts, polaritonic catalysis, stoichiometric photon conver-
sion, and active ratchets.
2 Four Exact Bioenergetic Bounds
2.1 First-Law Stoichiometric and Carnot
Photon Floors
At physiological T = 310 K, ATP hydrolysis releases
∆GATP ≈ 50 kJ/mol ≈ 518.2 meV, whereas a single
71 THz photon carries hν− ≈ 293.63 meV. By the First
Law, any direct stoichiometric photon-to-ATP conversion
demands (Lean Thm. 1; C01–C04, Fig. 1a):
∆GATP
hν−
= 5182 2936 = 2591 1468 ≈ 1.765 > 7 4 ph/ATP, (1)
or Φstoich 71 > 1.76 × 104 photons/s/mitochondrion (∼
0.83 fW) for a +10% boost on JATP = 105 ATP/s. Under
a finite effective radiation temperature Trad > T (bench-
marked parametrically in C01–C03 at Trad = 3100 K
and 620 K; for high-brightness narrowband mid-IR lasers
ηC → 1), Carnot eﬀiciency ηC = 1 − T /Trad < 1 strictly
tightens Pin ≥ PATP/ηC > PATP whenever PATP > 0
(Thm. 2).
2.2 Eyring Catalysis, Collective ZPE Ceil-
ing, and Mitochondrial OCR
Under Eyring transition-state kinetics [5] at fixed T =
310 K, multiplying turnover rate by 11/10 requires an
activation-barrier shift |∆Ea|10% = kB T ln(11/10). By
the classical alternating-series error bound for the Merca-
tor expansion of ln(1 + x) at x = 1/10 (prose calculus;
rational partial sums certified over Z in Lean Thm. 3):
11437
120000 < ln
( 11
10
)
< 143 1500
=⇒ |∆Ea|10% ∈ (2.545, 2.547) meV (2)
at kB T = 26.713 meV (Thm. 4). To benchmark against
the resonant Hopfield A2 polariton energy scale (ωc =
ω0 = 87 THz, ν− = 71 THz, η = g/ω0 = 1264/6177 ≈
0.205 [4]), the TRK invariant ν+ν− = ω2 0 fixes the upper
polariton at ν+ = 7569/71 ≈ 106.61 THz, giving the exact
single-mode ground-state zero-point energy (ZPE) shift
(Thm. 5; C05–C08, Fig. 1b):
∆EZPE = 1 2 h(ν+ + ν− − 2ω0) = h(ω0 − ν−)2 2ν−
= 128 71 h · THz ≈ 7.456 meV > 2.92 |∆Ea|10%.
(3)
Crucially, (3) and C05–C08 benchmark only the undiluted
collective single-mode ZPE scale against |∆Ea|10%. Two
physical obstructions prevent naive static vacuum cataly-
sis from explaining [7]: (a) across N ∼ 106–108 uncorre-
lated lipid dipoles, per-molecule vacuum shifts dilute as
O(∆EZPE/N ), closing static single-enzyme catalysis un-
less an enzyme reaction coordinate couples coherently to
the collective bright mode or a localized few-dipole mi-
crodomain; and (b) dark-cavity vacuum ZPE exists al-
ready at Iinc = 0, so an irradiance-triggered +10% boost
over a dark control (Iinc > 0 vs. 0) requires irradiance-
driven resonant polaritonic catalysis (weak resonant 71-
THz excitation of MP− carrying hν− = 293.63 meV per
quantum, saturating sub-linearly as Iinc/(Iinc + Isat) at
high irradiance, Thm. 20).
Flux vs. cellular abundance distinction. Im-
portantly, cellular ATP concentration ([ATP]) reported
in [7] can rise without accelerating oxidative phospho-
rylation if cellular ATP consumption drops, glycolysis
compensates, or ATP synthase operates near equilib-
rium under fixed demand. Conditional on the hypoth-
esis that the +10% increase reflects a +10% boost in
steady-state mitochondrial ATP-synthesis flux JATP under
Mitchell’s chemiosmotic coupling [6] with fixed H+/ATP
and P/O stoichiometry, catalytic acceleration leaves the
coupled P/O ratio invariant (Thm. 19) and forces an exact
+10% increase in oligomycin-sensitive ATP-linked OCR
(Thm. 13). For antimycin/rotenone-corrected mitochon-
drial OCR (Jmito = JATP-linked + Jleak), whenever pro-
ton leak stays fixed at ≤ 25%, total mitochondrial OCR
rises by ≥ +7.5% (Thm. 17; non-ohmic proton leak may
decrease modestly if ∆p drops slightly under faster ATP
synthesis). Conversely, observing a +10% [ATP] rise with
zero oligomycin-sensitive OCR increase immediately sep-
arates reduced ATP demand, glycolytic shift, or direct
non-O2 work from mitochondrial oxidative catalysis. Un-
der CCCP/FCCP uncoupling (∆p → 0), forward chemios-
motic ATP synthesis vanishes (and F1Fo-ATPase typically
reverses to hydrolyze ATP, eliminating any forward cat-
alytic synthesis gain, Thm. 16).
2.3 Exact Finite-Difference Arrhenius
and π-Free Micro-Hotspot No-Go
Under Arrhenius heating (incorporating the Eyring T pref-
actor reduces ∆T10% by ∼ 5% to ∼ 1.45 K, leaving
the micro-hotspot exclusion > 69,000× unchanged), a
+10% rate jump obeys the exact finite-difference identity
(Thm. 6; zero linearization error):
Ea
kB T − Ea kB (T + ∆T ) = ln ( 11 10 )
⇐⇒ ∆T10% = T ∆Ea Ea − ∆Ea . (4)
With (2) at T = 310 K, respiratory activation en-
ergy Ea = 50 kJ/mol (518.2 meV) forces ∆T10% ∈
(1.52, 1.54) K (> 1.90 K at 40 kJ/mol, > 1.26 K at
60 kJ/mol, Thm. 7, Fig. 2a).
By the steady-state spherical heat equation [1], sustain-
ing ∆T across a mitochondrion of radius R = 0.5 µm in
aqueous cytosol (κth = 3/5 W/(m · K)) requires absorbed
power Pmicro = 4πκthR∆T > 5.7 µW (nearly 1010× the
2
```

---

## Page 3

```text
0.83 fW stoichiometric floor, Thm. 9). Dividing by cross-
section A = πR2 cancels π identically (Thm. 8):
Imicro = Pmicro πR2 = 4κth∆T R
= 734.4 W/cm2 (1.53 K), > 729.6 W/cm2 (1.52 K).
(5)
Since absorbed flux satisfies Iabs ≤ Iinc (even at
100% single-organelle absorption), weak mid-IR irradia-
tion (Iinc ≤ 10 mW/cm2 = 100 W/m2) falls short of
single-organelle micro-thermal heating by > 72,900× (>
73,400× at midpoint 1.53 K, Thm. 10; C09–C12, Fig. 2b),
and basal respiratory self-heating stays below 10−8 K
(Thm. 12). By contrast, collective heating across a 1 mm
culture dish amplifies ∆T by at least L/R = 2000× in
3D spherical scaling (Thm. 11, down to ∼ 0.37 W/cm2)—
and further under 1D planar substrate thermal resistance
or cm-scale illumination—making an off-resonance water-
absorption-matched IR control the primary discriminator
separating bulk heating (Hbulk) from weak-field resonant
catalysis (Hcat).
2.4 Classical Markovian TUR (Window
τ = 1 s) and Ratchet Power Floor
For autonomous classical Markovian non-equilibrium
steady states observed over an explicit time window τ
(overdamped biochemical catalysis, C13–C16 evaluated at
τ = 1 s, Fig. 3a), integrated ATP-flux precision obeys
the dimensionally homogeneous Barato–Seifert thermody-
namic uncertainty relation [2]:
Var(Jτ )
⟨Jτ ⟩2
στ
kB
≥ 2 (σ ≥ 0, τ > 0), (6)
where στ /kB is strictly dimensionless (with στ := στ
replacing σ in the cleared integer implication of Lean
Thm. 14; C13–C14 use illustrative Var(Jτ )/⟨Jτ ⟩2 =
10−2, 10−3). Classical periodically driven ratchets (C∆ =
0) can bypass the autonomous TUR without incurring
quantum coherence-maintenance costs and remain con-
strained by First-Law power balance PATP + Ploss = Pin
(Thm. 15). By contrast, an active Regime II quantum-
coherent ratchet (C∆ > 0) must satisfy the exact addi-
tive power floor Pmaint + PATP ≤ Pin (Thm. 15): taking
the bulk-water dephasing maintenance estimate Pmaint ∼
5 × 105 P mito ATP ∼ 4 nW per mitochondrion from [4], this
exceeds the total weak mid-IR power incident on a sin-
gle mitochondrion (IincπR2 ≈ 78.5 pW at 10 mW/cm2,
R = 0.5 µm) by > 50× even at 100% absorption.
3 Formal Certification Scope and
Reproducibility
Exact verification boundary. Layer 1
(src/lean/MitoAtpModulationCert.lean, 20 con-
structive integer/rational theorems compiled under
Lean 4.36.0 -DwarningAsError=true, 0 sorry, 0
grind, 0 Classical.choice, Table 1) certifies the
exact rational partial-sum, TRK-to-ZPE, Arrhe-
nius, π-free flux, OCR, TUR-implication, and ad-
ditive power-balance inequalities over Z. Layer 2
(src/python/mito_atp_modulation_verifier.py,
AST-audited zero-float, zero /, zero **, zero
limit_denominator) verifies all 16 SHA-256
certificates (C01–C16, Table 2, archived in
data/certificates/MANIFEST.json) and passes all 58
adversarial checks. Analytical series-remainder bounds
(ln(11/10)), continuum conduction, chemiosmotic kinet-
ics, classical TUR applicability, and unrefereed empirical
inputs from [7] reside in prose and Table 3 rather than
inside the Lean kernel.
AI Assistance Disclosure. Authored by Lluis Eriks-
son with Google Antigravity assisting Lean 4 proof en-
gineering, zero-float verifier implementation, adversarial
testing, 300-DPI figures, and LaTeX drafting. All Lean 4
proofs (src/lean/), zero-float verifier (src/python/),
and 16 JSON certificates (data/certificates/) are
archived directly in this public AIRR record under MIT
(code/Lean/data) and CC-BY-4.0 (manuscript/figures).
References
[1] Guillaume Baffou, Hervé Rigneault, Didier Marguet, and Lu-
dovic Jullien. A critique of methods for temperature imaging in
single cells. Nature Methods, 11:899–901, 2014.
[2] Andre C. Barato and Udo Seifert. Thermodynamic uncertainty
relation for biomolecular processes. Physical Review Letters,
114:158101, 2015.
[3] Lluis Eriksson. Geometry, membranes, and life as a resource
boundary: A correct-by-construction operational pipeline from
static suppression to maintenance costs. 2025. AIRR.SCIENCE
record ARR-2025-2AQXS44H6Z8GQAG2 (ai.viXra:2512.0085,
v1 Dec 2025; v2 Jul 2026).
[4] Lluis Eriksson. Mito-polaritons meet the resource boundary: Ex-
act Hopfield A2 invariants, thermodynamic maintenance hori-
zons, and constructive Lean 4 certificates for the 71-THz mito-
chondrial quantum state. 2026. AIRR.SCIENCE record ARR-
2026-1E91AXEJYT890TQC (accepted Nov 26, 2026).
[5] Henry Eyring. The activated complex in chemical reactions.
Journal of Chemical Physics, 3:107–115, 1935.
[6] Peter Mitchell. Coupling of phosphorylation to electron and hy-
drogen transfer by a chemi-osmotic type of mechanism. Nature,
191:144–148, 1961.
[7] Yu Yang, Zhenglong Gu, and Bo Song. A quantum state
of mitochondria in the living cell. 2026. bioRxiv preprint
10.64898/2026.09.10.750628v1, 15 September 2026 (unrefereed).
3
```

---

## Page 4

```text
Table 1: All 20 constructive Lean 4.36.0 theorems in src/lean/MitoAtpModulationCert.lean (0 sorry, 0 grind,
0 Classical.choice, -DwarningAsError=true).
# Lean Theorem Identifier Exact Formalized Statement (over Z)
1 first_law_stoichiometric_photon_floor 5182/2936 = 2591/1468 ∈ (1.76, 2) (> 7/4 photons/ATP)
2 carnot_tightening_stoichiometric_power 0 < PATP ∧ 0 < T < Trad ∧ PATP Trad ≤ Pin (Trad − T ) =⇒ PATP < Pin
3 exact_mercator_ln_11_10_bracket 953/10000 < 11437/120000 < 143/1500 < 954/10000 (Mercator partial sums)
4 eyring_passive_catalytic_barrier_310k 2545 < 26713 · (11437/120000) and 26713 · (143/1500) < 2547 (µeV)
5 hopfield_zpe_exceeds_catalytic_barrier_2p9x ν+ ν− = ω2 0 =⇒ ν− (ν+ + ν− − 2ω0 ) = (ω0 − ν− )2 ; ∆EZPE ∈ (7.455, 7.457) meV
6 exact_finite_difference_arrhenius_identity Ea ∆T = L kB T (T + ∆T ) =⇒ (Ea − LkB T )∆T = LkB T 2
7 arrhenius_delta_t_brackets_310k ∆T10% ∈ (1.52, 1.54) K (50 kJ/mol), > 1.90 K (40), > 1.26 K (60)
8 pi_free_micro_hotspot_flux_nogo Imicro R = 4κth ∆T ; Imicro = 7344000 W/m2 > 734 W/cm2 (1.53 K)
9 micro_hotspot_vs_stoichiometric_power_gap Pmicro > 5.7 µW > 5 × 109 fW vs. Pstoich < 1 fW
10 weak_ir_micro_hotspot_exclusion 0 < Iinc ≤ 100 W/m2 =⇒ 73400 Iinc < 7344000 (> 73400× at 1.53 K)
11 bulk_vs_micro_thermal_length_amplification L/R ≥ 2000 (1 mm dish vs. 0.5 µm organelle)
12 basal_mitochondrion_self_heating_negligible 20000 < 4 · 314 · 6 · 5 (∆Tbasal < 10−8 K)
13 catalytic_ocr_proportionality_law Fixed ATP-linked stoichiometry ∧ 10 ∆JATP = JATP =⇒ 10 ∆JO2 = JO2
14 barato_seifert_tur_entropy_floor eD > 0 ∧ στ ≥ 0 ∧ 2kB J 2 ≤ Var · στ ∧ Var · eD ≤ eN J 2 =⇒ 2kB J 2 eD ≤ eN J 2 στ
15 active_coherent_ratchet_dual_floor Pmaint , PATP , Ploss ≥ 0 ∧ Pmaint + PATP + Ploss = Pin =⇒ Pmaint + PATP ≤ Pin
16 uncoupler_collapses_passive_catalysis ∆p = 0 =⇒ (11kcat ) · 0 = (10kcat ) · 0 = 0 (CCCP collapse)
17 proton_leak_adjusted_ocr_lower_bound Jmito = Jc + Jleak ∧ 4Jleak ≤ Jmito ∧ 10∆J = Jc =⇒ 40∆J ≥ 3Jmito (≥ +7.5%)
18 atp_mechanism_discriminator_decidability Joint numerical check: > 1.76 ph/ATP, > 2.92× ZPE scale, > 73400× micro, 2000× bulk
19 catalytic_po_ratio_invariance 2(P/O)JO2 = JATP =⇒ 2(P/O)(11JO2 ) = 11JATP
20 catalytic_saturation_strict_ceiling A, Isat > 0 ∧ I ≥ 0 =⇒ AI < A(I + Isat ) (sub-linear saturation ceiling)
Table 2: Summary of all 16 verified MITO-ATP-MODULATION-CERT-1.0 canonical certificates (C01–C16, SHA-256 hashed
in data/certificates/MANIFEST.json).
ID Mode Verified Instance Exact Certified Metrics
C01 M1 Stoich/Carnot 71 THz, ∆G = 518.2 meV, Tr = 3100 K 2591/1468 ≈ 1.765 ph/ATP (1st Law), 1.961 (Carnot ηC = 9/10)
C02 M1 Stoich/Carnot 87 THz, ∆G = 518.2 meV 1.440 ph/ATP (1st Law), 1.600 ph/ATP (Carnot)
C03 M1 Stoich/Carnot 71 THz, Tr = 620 K (ηC = 1/2) 3.530 ph/ATP (exact 2× Carnot tightening)
C04 M1 Stoich/Carnot 71 THz, ∆G = 621.8 meV (60 kJ/mol) 2.118 ph/ATP (> 2.1 photons/ATP)
C05 M2 ZPE Ceiling 71/87 THz (η ≈ 0.205), +10% |∆Ea | ∈ (2.545, 2.547) meV, ZPE/|∆Ea | > 2.92× (1/N dil.)
C06 M2 ZPE Ceiling 71/87 THz, +25% ATP, 310 K |∆Ea | ≈ 5.96 meV, collective ZPE/|∆Ea | > 1.25×
C07 M2 ZPE Ceiling 79/87 THz (η ≈ 0.097), +10% ZPE = 1.675 meV < 2.55 meV (ratio ≈ 0.66, below barrier)
C08 M2 ZPE Ceiling 65/87 THz (η ≈ 0.296), +10% Deep USC ZPE = 15.4 meV, collective ratio > 6.0×
C09 M3 Photothermal Ea = 50 kJ/mol, I = 10 mW/cm2 ∆T ∈ (1.52, 1.54) K, Imicro > 729 W/cm2 (> 72,900× excl.)
C10 M3 Photothermal Ea = 40 kJ/mol, I = 10 mW/cm2 ∆T > 1.90 K (1.91 K), excluded by > 91,000×
C11 M3 Photothermal Ea = 60 kJ/mol, I = 10 mW/cm2 ∆T > 1.26 K (1.274 K), excluded by > 60,400× (61,176× exact)
C12 M3 Photothermal Ea = 50 kJ/mol, I = 1 W/cm2 Even at 1 W/cm2 , micro-hotspot excluded by > 729×
C13 M4 Classical TUR NADH (P/O = 5/2), στ /kB = 2 × 106 (τ = 1 s) Classical TUR sat. (2 × 104 ≥ 2), ATP-linked ∆OCR = +10%
C14 M4 Classical TUR FADH2 (P/O = 3/2), στ /kB = 1.2 × 106 (τ = 1 s) Classical TUR sat. (1200 ≥ 2), P/O = 3/2 invariant
C15 M4 TUR Control Synth. στ /kB = 103 (τ = 1 s), Var/J 2 = 10−6 (Var/J 2 )(στ /kB ) = 10−3 < 2 (classical TUR viol.)
C16 M4 TUR Boundary Exact sat. στ /kB = 2 × 105 (τ = 1 s), 10−5 (Var/J 2 )(στ /kB ) = 2 exact classical TUR boundary
Table 3: Four-protocol experimental discriminator separating mechanisms for a +10% steady-state mitochondrial
ATP-flux (JATP) increase under 71-THz IR (off-resonance water-matched IR is the primary separator between Hbulk
and Hcat; empirical Isat is not derived from first principles).
Protocol Hbulk (Bulk Heat) Hmicro (Hotspot) Hcat (Driven VSC Catalysis) Hstoich (Direct Photon/Ratchet)
Off-res. H2 O-matched IR +10% ATP Excluded 0% (sharp 71 THz) 0% (off-res.)
Oligomycin-sens. ATP-OCR +10% (Arrh.) Excluded +10% (if flux-driven; 0% if demand) ≈ 0% (no extra O2 )
CCCP / FCCP (∆p → 0) Collapses fwd. syn. Excluded Collapses fwd. syn. (Thm. 16) Persists only if direct (non-∆p)
Irradiance sweep (auxiliary) Linear (below harm) Excluded Linear ≪ Isat ; saturates ≳ Isat Linear below absorber/enzyme sat.
4
```

---

## Page 5

```text
Figure 1: Stoichiometric Photon Floor and Collective Single-Mode ZPE Scale. (a) First-Law and Carnot-
tightened photons per extra ATP vs. mid-IR frequency (C01–C03, showing both First-Law 1.77 and Carnot 1.96 for
C01). (b) Undiluted single-mode Hopfield ZPE-to-catalytic-barrier ratio across normalized coupling η = g/ω0 (C07:
η ≈ 0.097, 0.66×; C05: η ≈ 0.205, 2.93×; C08: η ≈ 0.296, 6.05×), representing a collective energetic ceiling subject to
1/N dipole dilution.
Figure 2: Photothermal Micro-Hotspot Exclusion vs. Bulk Dish Heating. (a) Exact finite-difference Arrhe-
nius ∆T10% vs. activation energy Ea (C09–C11). (b) π-free absorbed flux law Iabs = 4κth∆T /L (Iabs ≤ Iinc) excluding
single-mitochondrion hotspots (> 729 W/cm2, 734.4 W/cm2 at midpoint) by > 72,900× at 10 mW/cm2 while expos-
ing ≥ 2000× bulk dish amplification.
5
```

---

## Page 6

```text
Figure 3: Classical Markovian TUR Region (τ = 1 s) and Experimental ATP-Linked OCR Discriminator.
(a) Dimensionally homogeneous classical NESS TUR boundary (στ /kB = 2/(Var(Jτ )/⟨Jτ ⟩2) at τ = 1 s) with illus-
trative points (C13, C14), exact saturation (C16, product 2), and synthetic violation control (C15, product 10−3). (b)
Conditional on +10% mitochondrial JATP, sharp +10% oligomycin-sensitive ATP-linked OCR vs. 0% signature sep-
arates driven polaritonic catalysis (Hcat) from direct stoichiometric conversion (or reduced-demand/glycolytic [ATP]
shifts).
6
```
