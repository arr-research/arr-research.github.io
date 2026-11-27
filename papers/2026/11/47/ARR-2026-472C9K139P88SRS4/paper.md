# Thermodynamic Channel Capacity, Gordon-Holevo Thermal Ceilings, and Intracellular Signaling Horizons of 71-THz Mito-Polariton Channels

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Thermodynamic Channel Capacity, Gordon–Holevo
Thermal Ceilings, and Intracellular Signaling
Horizons of 71-THz Mito-Polariton Channels
Lluis Eriksson∗
November 27, 2026
Abstract
Completing our six-paper machine-checked audit series (P1--P6) following ARR-2025-
2AQXS44H6Z8GQAG2, ARR-2026-1E91AXEJYT890TQC, and ARR-2026-1F61YM5EHC95TBMP
on the 71 THz mitochondrial cristae polariton hypothesis of Yang, Gu, and Song
(bioRxiv:10.64898/2026.09.10.750628v1, Sep. 2026, unrefereed preprint awaiting indepen-
dent experimental replication), we establish exact thermodynamic channel-capacity ceilings
and intracellular signaling horizons for bosonic thermal-loss mito-polariton waveguides Eη,NB .
Backed by MITO-POLARITON-CHANNEL-CAPACITY-CERT-1.0 (20 constructive Lean 4.36.0
theorems compiled with -DwarningAsError=true, 0 sorry, 0 grind, 0 Classical.choice;
AST-audited zero-float/zero-slash/zero-power Python verifier; 16 SHA-256 certificates
C01--C16; and 58 adversarial tests), we prove five exact bounds: (i) the Giovannetti–Holevo
classical capacity CHol(η, NS , NB ) = g(ηNS + (1 − η)NB ) − g((1 − η)NB ) obeys exact dyadic–
Mercator rational brackets, never exceeds the pure-loss ceiling g(ηNS ), and for every lossy
channel 0 < η < 1 obeys the exact tangent floor EHol bit ≥ hν ln 2/[η ln(1 + [(1 − η)NB ]−1)] >
kB T ln 2/[η(1 + kB T hν ln 1 1−η )] (uniformly > 2.790/η zJ for all η ≤ 1/2, converging to
2.967/η zJ at deep loss, C01--C08); (ii) antidegradability forces unassisted quantum capacity
Q(Eη,NB ) ≡ 0 whenever η ≤ 1/2 (L ≥ Latt ln 2, C03--C04), while for η > 1/2 unassisted
Q ≤ min(log2[η/(1 − η)], CHol) is distinguished from the unconstrained two-way PLOB
ceiling Q2 ≤ − log2(1 − η) (C02); (iii) we separate three receiver tiers at 71 THz, 310 K:
coherent Holevo or ideal dark-count-free sparse photon counting (floor > 2.790/η zJ for
η ≤ 1/2), single-quadrature homodyne reception (Ehom bit ≥ 1 2 hν ln 2/η = 16.305/η zJ, 5.50×),
and heterodyne reception or excess-noise intensity absorbers with Ndark ≥ 1 photon/mode
(Ehet bit ≥ hν ln 2/η = 32.609/η zJ, exact βhν ∈ (10.99, 11.00)× penalty, C05--C06); (iv) at
0.1 pW (1% basal mito power), 1 kbit/s signaling reaches Lmax ≈ 8.03 Latt (24.1 µm hetero-
dyne, C09) to 10.49 Latt (31.5 µm Holevo, C10), whereas 10 Mbit/s is forbidden for heterodyne
at η = 1 (C13), and 1 Gbit/s is forbidden by both thermal Landauer receiver bit erasure
(2.967 zJ/bit) and finite-bandwidth (B ≤ 71 THz) lossless Holevo bounds (> 1.77 zJ/bit,
C15) as well as at 10 pW under heterodyne (C16); and (v) we synthesize P1--P6 into a unified
audit matrix.
1 Introduction
Even when continuous-variable quantum entanglement across mitochondrial cristae is excluded
by metabolic maintenance power floors and sub-10 ps entanglement sudden death (Paper P5), a
distinct and physically legitimate question remains: how much classical or quantum information
could a 71 THz mito-polariton channel transmit per unit metabolic power, and over what intra-
cellular distance? Answering this question connects our mitochondrial audit series [1–3] directly
∗Independent researcher and founder/operator of AIRR.SCIENCE (AIRR-FOUNDER-1.0; operator_conflict:
true). Formalization, exact-Q certification, and manuscript drafting were carried out with Google Antigravity
AI assistance; all mathematical claims are independently machine-checked by Lean 4.36.0 and AST-audited exact
rational Python verification. Contact: lluiseriksson@gmail.com.
1
```

---

## Page 2

```text
to our prior bosonic thermal-loss signaling framework (ARR-2026-1F61YM5EHC95TBMP [4]) and to
the exact theorems of quantum optical communication [5–9].
Rather than assuming all intracellular photonic signaling is impossible, we draw the exact
quantitative phase boundary separating three regimes: (1) quantum-coherent state/entanglement
transmission (Q > 0), which terminates abruptly at the 3 dB antidegradability wall η = 1/2;
(2) high-rate classical signaling (R ≥ 10 Mbit/s to 1 Gbit/s), which is unconditionally forbidden
by Landauer–Holevo and heterodyne energy floors even at zero propagation loss (η = 1); and
(3) low-rate classical/incoherent signaling (R ∼ 1 kbit/s), which is thermodynamically allowed
over 8–10 attenuation lengths conditioned on the existence of a physical waveguide and emitter
(independently constrained by P1--P4).
2 Bosonic Thermal-Loss Capacity, PLOB Wall, and the 10.99×
Decoding Gap
Model a single-mode polariton waveguide segment of transmissivity η ∈ (0, 1], mean input signal
photon number NS > 0, and thermal environment occupation NB = (eβhν − 1)−1 at physiological
temperature T = 310 K (β = 1/(kB T ); using CODATA 2018 exact h and kB , βhν = 10.9918 and
NB = 1.684 × 10−5 at ν = 71 THz). By the theorem of Giovannetti, García-Patrón, Cerf, and
Holevo [8], the ultimate classical capacity in nats per channel use is
Cnat(η, NS , NB ) = g
(
ηNS + (1 − η)NB
)
− g
(
(1 − η)NB
)
, (1)
where g(x) = (x + 1) ln(x + 1) − x ln x = ln(1 + x) + x ln(1 + 1/x) is the bosonic entropy function
(g(0) = 0, strictly increasing and concave on [0, ∞)). To avoid conflating distinct physical receiver
architectures, we distinguish three single-mode reception tiers [5, 10]:
1. Coherent Holevo decoding or ideal dark-count-free sparse photon counting: Direct photon-
counting (intensity) detection without local-oscillator vacuum noise can, via sparse pulse-
position modulation at NB ≪ 1, approach the Holevo capacity ceiling of Eq. (1) (bounded
strictly by Theorem 1.1 below).
2. Single-quadrature homodyne detection: Obeys Chom,nat = 1 2 ln ( 1 + 4ηNS 2(1−η)NB +1 ) ≤ 2ηNS ,
giving Ehom bit ≥ hν ln 2 2η ≈ 16.305/η zJ (5.50× above deep-loss Holevo).
3. Heterodyne detection (or excess-noise intensity reception with receiver dark noise Ndark ≥ 1
photon/mode): Joint measurement of both conjugate quadratures (or any intensity absorber
with ≥ 1 noise photon per mode) incurs the standard 1-photon vacuum/noise floor:
Chet,nat(η, NS , NB ) = ln
(
1 + ηNS
(1 − η)NB + 1
)
≤ ηNS . (2)
Theorem 1 (Thermal-Loss Ceilings, Receiver Tiers, and Quantum Capacity Walls; Lean Thms. 1–7,
10–12). For every NS > 0 and thermal bath NB = (eβhν − 1)−1 > 0:
1. (Exact lossy Holevo floor for 0 < η < 1, vs. lossless η = 1 divergence) For any strictly lossy
channel η ∈ (0, 1), x0 := (1 − η)NB > 0 and concavity of g gives Cnat ≤ ηNS ln(1 + x−1 0 ) <
ηNS [βhν − ln(1 − η)] (Lean Thm. 2), while subadditivity gives Cnat(η, NS , NB ) ≤ g(ηNS ).
Dividing NS hν by Cnat/ ln 2 yields the exact lossy Holevo energy-per-bit floor
EHol bit (η, NB ) ≥ hν ln 2 η ln ( 1 + [(1 − η)NB ]−1) > kB T ln 2 η ( 1 + kB T hν ln 1 1−η ) (0 < η < 1). (3)
For every η ∈ (0, 1/2], − ln(1 − η) ≤ ln 2, giving the exact uniform channel floor EHol bit >
2.790/η zJ at 71 THz, 310 K (Lean Thm. 15), which converges to the deep-loss Landauer
2
```

---

## Page 3

```text
Figure 1: (a) Exact Giovannetti–Holevo classical capacity, heterodyne capacity, continuous unas-
sisted quantum ceiling max(0, log2[η/(1 − η)]), and two-way PLOB ceiling Q2 ≤ − log2(1 − η) vs.
transmissivity η at 71 THz, 310 K (NS = 0.1), highlighting the exact 3 dB antidegradability wall
(C03) and low-loss benchmark (C02). (b) Minimum energy per bit vs. attenuation in dB, certi-
fying the exact 10.99× separation between coherent deep-loss Holevo decoding and heterodyne
reception (C05--C06).
asymptote kB T ln 2/η ∈ (2.966, 2.967)/η zJ as η → 0+ (Lean Thm. 11). By contrast, in the
idealized lossless (η = 1) unbounded-bandwidth limit (B → ∞, NS → 0), Cnat(1, NS , NB ) =
g(NS ) satisfies g(NS )/NS → ∞ so no positive channel-only Holevo energy floor exists at
η = 1; a positive floor at η = 1 arises either from a finite carrier bandwidth B ≤ ν or from
the independent Landauer bit-erasure cost kB T ln 2 at a 310 K receiver [11].
2. (Heterodyne / Ndark ≥ 1 penalty for all η ∈ (0, 1]) By Eq. (2), heterodyne reception (or an
intensity receiver with Ndark ≥ 1 photon/mode) obeys
Ehet bit ≥ hν ln 2 η , h(71 THz) ln 2 ∈ (32.609, 32.610) zJ (Lean Thm. 12), (4)
valid for every η ∈ (0, 1] and exceeding the deep-loss Landauer–Holevo asymptote by βhν ∈
(10.99, 11.00)× at 71 THz, 310 K (Lean Thms. 5–6; Fig. 1b), while single-quadrature homo-
dyne detection sits exactly a factor of 2 lower (16.305/η zJ).
3. (Unassisted quantum capacity Q vs. two-way PLOB Q2; Lean Thms. 3–4) For any η ≤ 1/2,
Eη,NB is antidegradable and its unassisted quantum capacity vanishes identically, Q(Eη,NB ) ≡
0 [7]; for η > 1/2, unassisted quantum capacity obeys the continuous pure-loss ceil-
ing Q(Eη,NB ) ≤ min
(
log2 η 1−η , CHol(η, NS , NB ) ) (vanishing smoothly at η = 1/2; at η =
3/4, NS = 0.1 in C02, log2 3 ≈ 1.585 b and CHol = 0.392 b), whereas the unconstrained two-
way LOCC-assisted PLOB bound [9] obeys Q2(Eη,NB ) ≤ − log2(1 − η) (2.00 b at η = 3/4,
Fig. 1a). Any cristae-collar chain with per-collar transmission η1 ≤ 1/2 crosses the unas-
sisted Q = 0 wall at d = 1.
3 Bioenergetic Rate Ceilings and Intracellular Signaling Hori-
zons
For an exponential waveguide attenuation profile η(L) = e−L/Latt , sustaining a classical bit rate
Rmin within a metabolic signaling power budget Psig requires Psig/Rmin ≥ E(0) bit eL/Latt , where E(0) bit
3
```

---

## Page 4

```text
is either Ehet bit (1) = hν ln 2 ≈ 32.609 zJ (valid for all η ∈ (0, 1]) or the uniform η ≤ 1/2 Holevo
channel floor EHol,1/2 bit = 2.790 zJ (valid for all L ≥ Latt ln 2, Eq. (3)). Defining the bioenergetic
margin M := Psig/(RminE(0) bit ) yields:
Theorem 2 (Signaling Horizon and Zero-Loss Impossibility; Lean Thms. 8–9, 14–20). 1.
(Heterodyne zero-loss exclusion) If Psig ≤ Rminhν ln 2, incoherent heterodyne signaling at
rate Rmin is unconditionally forbidden even at η = 1.
2. (Lossless η = 1 Landauer and finite-bandwidth exclusion) At η = 1, a thermal receiver
resetting bits at T = 310 K requires Psig > RminkB T ln 2 [11]; independently, even without
receiver erasure, any single-mode channel with physical carrier bandwidth B ≤ ν = 71 THz
satisfies NS = Psig/(hνB) ≥ Psig/(hν2), bounding g(NS )/NS and yielding a strict positive
lossless Holevo energy-per-bit floor (at Psig = 0.1 pW, NS > 2−25 =⇒ EHol bit (η = 1, B ≤
ν) > 1.77 zJ/bit, Lean Thm. 19).
3. (Attenuation horizon) For M > 1 (and L ≥ Latt ln 2 in the Holevo case), the maximum
propagation distance obeys
Lmax(Psig, Rmin) = Latt ln
(
Psig
RminE(0) bit
)
. (5)
For a subwavelength slow-polariton mode (vg ∼ 0.01c ≈ 3 µm/ps) damped at γ = 1 THz
(1 ps−1), the characteristic attenuation length is Latt = vg/γ ≈ 3 µm (contrasted with the bulk
71 THz quiet-water window Latt = 40.5 µm from P1 [3]). Evaluating Eq. (5) at Psig = 0.1 pW
(1% of a 10 pW basal mitochondrion [12]) yields four sharp regimes (Fig. 2; Table 1):
• Low-rate classical signaling (1 kbit/s, C09--C11): Budget 100,000 zJ/bit gives M =
3,066.6 (heterodyne) and 35,842.3 (uniform η ≤ 1/2 Holevo), allowing Lmax = 24.08 µm
(8.03 Latt, C09) to 31.46 µm (10.49 Latt, C10), or 325.1 µm in bulk quiet water (C11)—
thermodynamically open if a physical waveguide/emitter exists.
• Megabit compression (1 Mbit/s, C12): Heterodyne compresses to M = 3.067, restricting
reach to Lmax = 3.36 µm (1.12 Latt, single-organelle scale).
• Quantum-decoding separation (10 Mbit/s, C13--C14): At 10 zJ/bit, incoherent het-
erodyne is unconditionally forbidden even at η = 1 (M = 0.307 < 1, C13; Lean Thm. 17),
whereas coherent Holevo decoding retains a narrow 3.83 µm window (M = 3.584, C14;
Lean Thm. 18).
• Gigabit bioenergetic wall (1 Gbit/s, C15--C16): At 0.1 pW (0.1 zJ/bit), signal-
ing fails both the 310 K Landauer erasure floor (2.967 zJ/bit, > 29× deficit) and the
finite-bandwidth B ≤ 71 THz lossless Holevo floor (> 1.77 zJ/bit, > 17× deficit, C15;
Lean Thm. 19); even dedicating 100% of total mitochondrial basal ATP power (10 pW)
still fails the heterodyne floor by > 3.26× at η = 1 (C16; Lean Thm. 20).
4 Unified Six-Paper Synthesis (P1--P6) and Verification Bound-
ary
Combining Wave M1 (P1--P3 [3]) and Wave M2 (P4--P6) completes a comprehensive, machine-
checked physical audit of the 71 THz mito-polariton program [1, 2, 13] across six orthogonal axes
(Fig. 3; Table 2):
4
```

---

## Page 5

```text
Figure 2: (a) Exact intracellular signaling horizon Lmax/Latt vs. required bit rate Rmin at
71 THz, 310 K, contrasted with the 3 dB quantum-capacity wall L3dB = Latt ln 2. (b) Zero-
loss (η = 1) bioenergetic feasibility map in the (Rmin, Psig) plane separating Landauer-erasure-
forbidden, coherent-decoding-only, and heterodyne-permitted regimes.
• Electrodynamic confinement (P1): Excludes passive lamellar/hyperbolic crista cavities
(> 39× diffraction mismatch, freq = 0.1675 exceeding fluid bilayer fbulk by 4–16×, R <
0.005 in 5–12 bilayers), while identifying 71 THz as an aqueous quiet window (Qloss = 106.8)
vs. overdamped H2O at 106.6 THz (Qloss = 3).
• Dressed USC ground-state thermodynamics (P2): Proves exact ground-state passiv-
ity (Werg = 0, zero dressed coherence), eliminating > 5,180× bare-basis master-equation
artifacts while quantifying positive ∆EZPE = 7.456 meV/mode.
• ATP modulation bioenergetics (P3): Excludes single-organelle photothermal hotspots
by > 73,400× under 10 mW/cm2 irradiation, exposes 2,000× bulk dish heating, proves
passive catalysis requires proportional +10% OCR at fixed P/O, and bounds active ratchets
via TUR.
• Two-band cubic spectroscopy (P4): Predicts a trapped Middle Polariton (MP0 at
86.2 THz, > 100× suppressed in USC linear IR), a > 5.8 × 106× 1/N 2D-IR anharmonicity
discriminator, and a clean CH2 → CD2 shift to 58.4/64.2 THz clear of D2O.
• Gaussian symplectic E-track (P5): Closes steady-state parametric entanglement (EN <
1 ebit ceiling; 9.75 nW or > 974× basal mito power for 0.5 ebit; tESD < 10 ps) and certifies
geometric cristae-collar MI/CMI decay.
• Channel capacity and signaling horizons (P6): Proves Q ≡ 0 beyond 3 dB loss,
excludes ≥ 10 Mbit/s heterodyne and ≥ 1 Gbit/s Holevo signaling at 0.1 pW, and bounds
low-rate classical reach by Lmax = Latt ln(Psig/(RminE(0) bit )).
Verification Boundary. All 20 theorems in MitoPolaritonChannelCapacityCert.lean
compile under lean -DwarningAsError=true and lake build with 0 sorry, 0 grind, and 0
Classical.choice (only constructive propext/Quot.sound or zero axioms). The Python ver-
ifier (src/mito_polariton_channel_capacity_verifier.py) is AST-audited zero-float/zero-
slash/zero-power, certifying C01--C16 and passing 58/58 adversarial pytest checks. Physical
channel estimates assume single-mode additive Gaussian thermal-loss propagation; spatial multi-
plexing over M independent parallel channels scales total bit rate by M only at M × the power
5
```

---

## Page 6

```text
Table 1: Complete set of all 16 exact-Q certificates (C01--C16)
from MITO-POLARITON-CHANNEL-CAPACITY-CERT-1.0 (SHA-256 locked in
certificates/MANIFEST.json).
Cert Regime Parameters Capacity / Margin Exact Verdict
C01 Lossless 71 THz η = 1, NS = 1 CHol = 2.000, Chet = 1.000 b EHol ≥ 23.5, Ehet ≥ 47.0 zJ
C02 Low-loss open η = 3/4, NS = 0.1 CHol = 0.392 b, Q ≤ 0.392 (1.585 uncl.) Q2 ≤ 2.00 b (PLOB open)
C03 Exact 3 dB wall η = 1/2, NS = 0.1 CHol = 0.290 b, Q ≡ 0 Antidegradable (Q2 ≤ 1.00 b)
C04 Single collar η = 1/4, NS = 10−2 CHol = 0.0251, Chet = 0.0036 b Q ≡ 0; Ehet/EHol ≈ 6.97×
C05 20 dB loss η = 10−2, NS = 10−3 EHol ≥ 303.4 zJ Ehet ≥ 3,261 zJ (10.75×)
C06 40 dB loss η = 10−4, NS = 10−2 EHol ≥ 29,745 zJ Ehet ≥ 326,097 zJ (10.96×)
C07 10 THz far-IR η = 1/4, NB = 0.27 CHol ∈ (0.0063, 0.0065) b βhν = 1.55; smaller gap
C08 Pure-loss ctrl η = 1/4, NB = 0 CHol = 0.02522 b Upper-bounds thermal C04
C09 1 kbit/s het 0.1 pW, Latt = 3 µm M = 3,066.6 Lmax ∈ (24.08, 24.09) µm
C10 1 kbit/s Holevo 0.1 pW, Latt = 3 µm M = 35,842.3 Lmax ≤ 31.46 µm (η ≤ 1/2 floor)
C11 1 kbit/s water 0.1 pW, Latt = 40.5 µm M = 3,066.6 Lmax ∈ (325.1, 325.2) µm
C12 1 Mbit/s het 0.1 pW, Latt = 3 µm M = 3.067 Lmax = 3.36 µm (single mito)
C13 10 Mbit/s het 0.1 pW (10 zJ/b) M = 0.307 < 1 Forbidden for het at η = 1
C14 10 Mbit/s Hol 0.1 pW (10 zJ/b) M = 3.584 > 1 Holevo / sparse count (≤ 3.83 µm)
C15 1 Gbit/s wall 0.1 pW (0.1 zJ/b) M = 0.0337 < 1 Forbidden (Landauer + B ≤ 71 THz)
C16 1 Gbit/s full 10 pW (10 zJ/b) M = 0.307 < 1 Forbidden for het (> 3.26×)
Figure 3: Unified log-scale summary of the certified physical barriers, master-equation artifact
factors, and falsifiable experimental discriminators established across Papers P1--P6.
budget, leaving energy-per-bit floors strictly invariant. The empirical claims of Ref. [13] remain
unrefereed and await independent experimental replication.
References
[1] Lluis Eriksson. Geometry and resource boundaries for biological polariton models.
AIRR.SCIENCE Record ARR-2025-2AQXS44H6Z8GQAG2, 2025.
[2] Lluis Eriksson. Mito-polariton resource-boundary certificates and exact thermodynamic au-
dits. AIRR.SCIENCE Record ARR-2026-1E91AXEJYT890TQC, 2026.
[3] Lluis Eriksson. Mitochondrial polariton audit series wave m1: Subwavelength con-
finement, dressed usc thermodynamics, and atp modulation bounds. AIRR.SCIENCE
Records ARR-2026-75841S47Z59VMSN2, ARR-2026-038Y5T8GYG9F7TTR, and ARR-
2026-0CXEJ0MRT995CAK8, 2026.
6
```

---

## Page 7

```text
Table 2: Unified six-paper audit matrix (P1--P6) for 71 THz mitochondrial polariton claims.
Paper Physical Axis Lean / Certs / Tests Decisive Quantitative Verdict
P1 Cavity confinement 18 Thms / 16 / 28 > 39× diffraction gap; freq = 0.1675; Qloss = 106.8 (71) vs 3 (106.6)
P2 Dressed USC thermo 18 Thms / 16 / 26 Werg = 0; ∆EZPE = 7.456 meV; > 470–610× dressed KMS
P3 ATP modulation 20 Thms / 16 / 58 > 73,400× micro-hotspot excluded; +10% OCR test; TUR ratchet bound
P4 Two-band 2D-IR 20 Thms / 16 / 57 Trapped MP0 (0.33%); 5.8 × 106× 1/N 2D-IR; CD2 clears D2O
P5 Symplectic E-track 20 Thms / 16 / 57 EN < 1 ceiling; 974× mito power (0.5 ebit); tESD < 10 ps; CMI decay
P6 Channel capacity 20 Thms / 16 / 58 Q ≡ 0 (η ≤ 1/2); 10.99× het/Hol gap; 1 Gbps Landauer wall
[4] Lluis Eriksson. Bosonic thermal-loss signaling bounds and thermodynamic resource horizons.
AIRR.SCIENCE Record ARR-2026-1F61YM5EHC95TBMP, 2026.
[5] J. P. Gordon. Quantum effects in communications systems. Proceedings of the IRE,
50(9):1898–1908, 1962.
[6] A. S. Holevo, M. Sohma, and O. Hirota. Capacity of quantum gaussian channels. Physical
Review A, 59(3):1820–1828, 1999.
[7] Michael M. Wolf, David Pérez-García, and Geza Giedke. Quantum capacities of bosonic
channels. Physical Review Letters, 98(13):130501, 2007.
[8] Vittorio Giovannetti, Raúl García-Patrón, Nicolas J. Cerf, and Alexander S. Holevo. Ul-
timate classical communication rates of quantum optical channels. Nature Photonics,
8(10):796–800, 2014.
[9] Stefano Pirandola, Riccardo Laurenza, Carlo Ottaviani, and Leonardo Banchi. Fundamental
limits of repeaterless quantum communications. Nature Communications, 8:15043, 2017.
[10] Christian Weedbrook, Stefano Pirandola, Raúl García-Patrón, Nicolas J. Cerf, Timothy C.
Ralph, Jeffrey H. Shapiro, and Seth Lloyd. Gaussian quantum information. Reviews of
Modern Physics, 84(2):621–669, 2012.
[11] Rolf Landauer. Irreversibility and heat generation in the computing process. IBM Journal
of Research and Development, 5(3):183–191, 1961.
[12] David G. Nicholls and Stuart J. Ferguson. Bioenergetics 4. Academic Press, 2013.
[13] Y. Yang, H. Gu, and B. Song. Mitochondrial cristae as mid-infrared polaritonic cavities mod-
ulating cellular atp synthesis. Unrefereed preprint, bioRxiv:10.64898/2026.09.10.750628v1,
September 2026. Unrefereed preprint awaiting independent experimental replication.
7
```
