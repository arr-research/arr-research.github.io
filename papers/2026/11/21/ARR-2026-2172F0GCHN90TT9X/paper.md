# Two-Band Lipid CH2 Cubic Hopfield Interlacing, Middle-Polariton Suppression, and 1/N Anharmonic 2D-IR Discriminators for 71-THz Mito-Polaritons

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Two-Band Lipid CH2 Cubic Hopfield Interlacing,
Middle-Polariton Suppression, and 1/N Anharmonic
2D-IR Discriminators for 71-THz Mito-Polaritons
Lluis Eriksson∗
November 27, 2026
Abstract
Real inner-mitochondrial-membrane phospholipid bilayers (cardiolipin and phosphatidyl-
choline) do not possess a single isolated 87 THz vibrational oscillator; instead, their aliphatic
methylene (CH2) chains form a resolved two-band stretching doublet at ν1 = νs ≈ 85.4 THz
(2849 cm−1) and ν2 = νas ≈ 87.5 THz (2919 cm−1). Continuing our exact audit series
(ARR-2025-2AQXS44H6Z8GQAG2, ARR-2026-1E91AXEJYT890TQC, and Wave M1) of the unrefer-
eed preprint by Yang, Gu, and Song (bioRxiv:10.64898/2026.09.10.750628v1, Sep. 2026,
awaiting independent experimental replication), we establish the exact gauge-invariant two-
band cubic Hopfield theory and derive falsifiable spectroscopic discriminators for 71 THz
ultrastrong-coupling (USC) mito-polaritons. Backed by the zero-floating-point verification
suite MITO-TWOBAND-CUBIC-HOPFIELD-CERT-1.0 comprising 20 constructive Lean 4.36.0 the-
orems (-DwarningAsError=true, 0 sorry, 0 grind, 0 Classical.choice), an AST-audited
zero-float/zero-slash/zero-power Python verifier, 16 SHA-256 JSON certificates (C01--C16),
and 57 adversarial tests, we prove six exact results: (i) exact Thomas–Reiche–Kuhn (TRK)
diamagnetic cancellation P3(0) = −ω2 c ω2 1 ω2 2 < 0 and global stability P3(−u) < 0 for all u ≥ 0;
(ii) strict Cauchy–Hopfield root interlacing 0 < ν2 − < ω2 1 < ν2 MP < ω2 2 < ν2 + < Tr(M2),
mandating a Middle Polariton (MP0) strictly trapped inside (85.4, 87.5) THz across all cavity
detunings; (iii) a universal calculus-free proof of strict two-band zero-point energy positiv-
ity ν− + νMP + ν+ > ωc + ω1 + ω2 (∆νZPE = 3.6153 THz, ∆EZPE ≈ 7.476 meV for C01);
(iv) a universal analytic ceiling proving > 100× USC suppression of MP0 photonic weight
(wc,MP = 0.33% in C01 vs. 35.5% at crossover C05); (v) exact 1/N collective Kerr anharmonic-
ity suppression giving a > 5.8 × 106× two-dimensional infrared (2D-IR) discriminator separat-
ing collective crista polaritons (∆−− = 7.21×10−7 THz at N = 106) from local N = 1 artifacts
(∆−− = 0.721 THz); and (vi) exact dark-manifold leakage bounds contrasting LP polaron
protection (ηleak ≤ 1/576 < 0.18%) against MP0 fluid-bilayer mixing (ηleak ≤ 16/49 ≈ 32.7%),
paired with a CH2 → CD2 lipid deuteration protocol shifting (ν−, νMP) to (58.36, 64.24) THz,
more than 10 THz clear of the 75 THz D2O O–D interference band.
1 Introduction
The unrefereed preprint of Yang, Gu, and Song [1] (Sep. 2026; awaiting independent experimental
replication) proposes that inner mitochondrial membrane cristae sustain ultrastrongly coupled
(USC) vibrational polaritons near ν− ≈ 71 THz via coupling of an electromagnetic cavity mode to
phospholipid methylene (CH2) stretching vibrations near 87 THz. In our prior resource-boundary
studies [2,3] and Wave M1 audit papers [4], we modeled the lipid matter sector as a single effective
∗Independent researcher and founder/operator of AIRR.SCIENCE (AIRR-FOUNDER-1.0; operator_conflict:
true). Formalization, exact-Q certification, and manuscript drafting were carried out with Google Antigravity
AI assistance; all mathematical claims are independently machine-checked by Lean 4.36.0 and AST-audited exact
rational Python verification. Contact: lluiseriksson@gmail.com.
1
```

---

## Page 2

```text
collective oscillator at ω0 = 87 THz, deriving exact electrodynamic confinement horizons, dressed
USC ground-state thermodynamics, and bioenergetic bounds on ATP modulation.
Real biological phospholipid bilayers, however, never exhibit a single isolated CH2 stretching
resonance [5, 6]. Instead, aliphatic hydrocarbon chains present two well-resolved, dipole-active
stretching normal modes: the symmetric CH2 stretch ν1 = νs ≈ 85.4 THz (2849 cm−1) and the
antisymmetric CH2 stretch ν2 = νas ≈ 87.5 THz (2919 cm−1), separated by a narrow doublet
gap ν2 − ν1 = 2.1 THz (∼ 70 cm−1). Incorporating both bands into the gauge-invariant Hopfield
Hamiltonian [7, 8] replaces the two-branch quadratic secular equation with a three-branch cubic
dispersion whose mathematical structure yields sharp, falsifiable spectroscopic tests that do not
exist in any single-band model.
Specifically, we address four questions essential to experimentally adjudicating the mito-
polariton hypothesis:
1. Spectrum and stability: Does two-band coupling preserve Thomas–Reiche–Kuhn (TRK)
stability against superradiant collapse, and where does the mandatory third branch—the
Middle Polariton (MP0)—lie?
2. Linear IR visibility: If a 71 THz USC lower polariton exists, why might MP0 escape
casual detection in linear mid-IR absorption, and what exact bound governs its photonic
brightness?
3. Collective vs. local artifacts in 2D-IR: How can two-dimensional infrared (2D-IR) spec-
troscopy [9–11] quantitatively distinguish genuine N ≳ 106 collective USC polaritons from
local single-molecule resonances, thermal filters, or dielectric artifacts?
4. Disorder and clean isotopic control: How does fluid-bilayer inhomogeneous broadening
(σinh ≈ 0.6 THz) act asymmetrically on LP vs. MP0 [12], and can lipid acyl-chain deuter-
ation (CH2 → CD2) test the polariton dispersion without colliding with the 75 THz D2O
O–D solvent band flagged in Wave M1 [4]?
2 Gauge-Invariant Two-Band Cubic Hopfield Theory
2.1 Hamiltonian, TRK Diamagnetic Shift, and Exact Secular Polynomial
Consider a single electromagnetic cavity mode a of bare angular/linear frequency ωc > 0 coupled
to two collective bright molecular modes Bj = N −1/2 j ∑Nj m=1 bj,m (j ∈ {1, 2}, 0 < ω1 < ω2)
with collective vacuum Rabi couplings g1, g2 > 0. The gauge-invariant Coulomb/TRK Hopfield
Hamiltonian [7, 8] is
HHop = ℏωca†a +
2∑
j=1
ℏωj B† j Bj +
2∑
j=1
ℏgj (a + a†)(Bj + B† j ) + ℏD(a + a†)2, D = g2 1 ω1 + g2 2 ω2 . (1)
Introducing canonical quadratures qc = (a + a†)/√2ωc, pc = i √ ωc/2(a† − a) and qj = (Bj +
B† j )/√2ωj , pj = i √ ωj /2(B† j − Bj ) casts Eq. (1) into HHop = ℏ 2 ∑ k p2 k + ℏ 2 q⊤M2q + const., with
real symmetric squared-frequency dynamical matrix
M2 =


ω2 c + 4ωcD 2g1 √ωcω1 2g2 √ωcω2
2g1
√ωcω1 ω2 1 0
2g2
√ωcω2 0 ω2 2

 . (2)
Completing the squares immediately exhibits strict positive-definiteness:
q⊤M2q = ω2 c q2 c +
2∑
j=1
(
ωj qj + 2gj
√ωc
√ωj qc
)2
> 0 (∀q ̸= 0). (3)
2
```

---

## Page 3

```text
Figure 1: (a) Exact cubic secular polynomial P3(ν2) for canonical 71-THz lipid CH2 USC (C01:
νc = 86.5, ν1 = 85.4, ν2 = 87.5, g1 = 11, g2 = 14 THz), displaying strict sign alternation and
mandatory trapping of MP0 at 86.2206 THz. (b) Detuning anticrossing map demonstrating that
MP0 remains strictly confined inside (85.4, 87.5) THz for every bare cavity frequency νc.
The characteristic polynomial P3(X) = det(XI − M2) in X = ν2 reads
P3(X) = (X − ω2 c − 4ωcD)(X − ω2 1 )(X − ω2 2 ) − 4ωcg2 1 ω1(X − ω2 2 ) − 4ωcg2 2 ω2(X − ω2 1 ). (4)
Theorem 1 (TRK Cancellation, Global Stability, and Strict Cauchy–Hopfield Interlacing). For
all ωc > 0, 0 < ω1 < ω2, and g1, g2 > 0:
1. (Exact TRK factorization; Lean Thm. 1) P3(X) simplifies identically to
P3(X) = (X − ω2 c )(X − ω2 1 )(X − ω2 2 ) − 4ωcX
[ g2 1
ω1
(X − ω2 2 ) + g2 2 ω2 (X − ω2 1 ) ] . (5)
2. (Superradiant No-Go; Lean Thms. 2–3) P3(0) = −ω2 c ω2 1 ω2 2 < 0 independently of (g1, g2),
and P3(−u) < 0 for every u ≥ 0.
3. (Mandatory MP0 trapping; Lean Thms. 4–6) Evaluating P3 at the four pivots 0 < ω2 1 <
ω2 2 < Xmax := Tr(M2) = ω2 c + ω2 1 + ω2 2 + 4ωcD yields strict sign alternation
P3(0) < 0, P3(ω2 1 ) = 4ωcg2 1 ω1(ω2 2 − ω2 1 ) > 0,
P3(ω2 2 ) = −4ωcg2 2 ω2(ω2 2 − ω2 1 ) < 0, P3(Xmax) > 0. (6)
Consequently, the three polariton squared frequencies strictly interlace the bare lipid doublet:
0 < ν2 − < ω2 1 < ν2 MP < ω2 2 < ν2 + < Xmax. (7)
Proof. Expanding 4ωcD(X − ω2 1 )(X − ω2 2 ) in Eq. (4) and combining (X − ω2 j ) + ω2 j = X in each
band cancels the constant diamagnetic terms identically, giving Eq. (5). Setting X = −u (u ≥ 0)
makes the first term strictly negative and the second term non-positive. Direct substitution yields
P3(ω2 1 ) > 0 and P3(ω2 2 ) < 0. At Xmax = A + ω2 1 + ω2 2 with A = ω2 c + 4ωcD, termwise positivity
4ωc(g2 j /ωj ) < A gives P3(Xmax) > 0 (machine-checked over Z in Lean Thm. 6). Sign alternation
on the three open intervals certifies Eq. (7).
3
```

---

## Page 4

```text
2.2 Vieta Invariants and Calculus-Free Proof of Two-Band ZPE Positivity
Expanding Eq. (5) as P3(X) = X 3 − e1X 2 + e2X − e3 yields the exact Vieta invariants:
e1 = ν2 − + ν2 MP + ν2 + = ω2 c + ω2 1 + ω2 2 + 4ωcD > e(0) 1 , (8)
e2 = ν2 −ν2 MP + ν2 MPν2 + + ν2 +ν2 − = ω2 c (ω2 1 + ω2 2 ) + ω2 1 ω2 2 + 4ωc
( g2 1 ω2 2
ω1
+ g2 2 ω2 1
ω2
)
> e(0) 2 , (9)
e3 = ν2 −ν2 MPν2 + = ω2 c ω2 1 ω2 2 = e(0) 3 . (10)
In single-band Hopfield theory [4], ZPE positivity followed immediately from (ν+ + ν−)2 = (ωc +
ω0)2 + 4g2. For two bands, no single closed-form quadratic exists; remarkably, however, strict
ZPE positivity admits a completely elementary, calculus-free algebraic proof over the ordered
ring.
Theorem 2 (Universal Two-Band Positive ZPE Shift; Lean Thms. 7–8). Let s1 = ν− + νMP + ν+,
s2 = ν−νMP + νMPν+ + ν+ν−, s3 = ν−νMPν+, and let s(0) 1 , s(0) 2 , s(0) 3 denote the corresponding bare
symmetric sums of (ωc, ω1, ω2). Because s2 1 − 2s2 = e1 > e(0) 1 , s2 2 − 2s1s3 = e2 > e(0) 2 , and
s3 = s(0) 3 > 0, we have strictly
∆νZPE := (ν− + νMP + ν+) − (ωc + ω1 + ω2) > 0 (11)
for every detuning and every positive coupling (g1, g2) ∈ R2 >0.
Proof. Suppose for contradiction that s1 ≤ s(0) 1 . If s1 = s(0) 1 , then e1 > e(0) 1 implies s2 < s(0) 2 ,
whence e2 = s2 2 − 2s1s3 < (s(0) 2 )2 − 2s(0) 1 s3 = e(0) 2 , contradiction. If s1 < s(0) 1 , then 2(s(0) 2 − s2) =
((s(0) 1 )2 − s2 1) + (e1 − e(0) 1 ) > (s(0) 1 − s1)(s(0) 1 + s1), while e2 > e(0) 2 gives (s(0) 2 − s2)(s(0) 2 + s2) <
2(s(0) 1 − s1)s3. Combining the two inequalities and dividing by s(0) 1 − s1 > 0 forces (s(0) 1 +
s1)(s(0) 2 + s2) < 4s3. Yet the three-variable AM–GM identity (a + b + c)(ab + bc + ca) − 9abc =
a(b − c)2 + b(c − a)2 + c(a − b)2 ≥ 0 (Lean Thm. 7) gives s1s2 ≥ 9s3 and s(0) 1 s(0) 2 ≥ 9s3, implying
(s(0) 1 + s1)(s(0) 2 + s2) > 18s3 > 4s3, contradiction.
For canonical benchmark C01, exact rational bracketing certifies ∆νZPE = 3.6153 THz, corre-
sponding to ∆EZPE = 1 2 h∆νZPE ≈ 7.476 meV per coupled cavity mode—consistent within 0.27%
of our single-band 7.456 meV certificate in Wave M1 [4].
3 Universal USC Suppression of MP0 Photonic Brightness and
CD2 Isotope Control
For each polariton branch α ∈ {LP, MP, UP} with eigenvalue Xα = ν2 α, the normalized eigenvec-
tor of M2 has exact dynamical-matrix normal-mode weights
wc,α =
(
1 + A1
(Xα − ω2 1 )2 + A2 (Xα − ω2 2 )2
)−1
, wj,α = Aj (Xα − ω2 j )2 wc,α, (12)
where Aj := 4ωcωj g2 j > 0. By orthogonality of the eigenbasis of symmetric M2, both row and
column sums equal unity identically: wc,α + w1,α + w2,α = 1 and ∑ α wk,α = 1 (verified to < 10−4
across all 9 spectral certificates C01--C09).
Theorem 3 (Universal USC Suppression Ceiling on MP0 Photonic Weight; Lean Thm. 11).
Writing ∆2 := ω2 2 − ω2 1 > 0, the Middle Polariton photonic weight obeys the root-free universal
upper bound
wc,MP <
(
1 + 3 min(A1, A2) + A1 + A2
∆2 2
)−1
. (13)
4
```

---

## Page 5

```text
Figure 2: (a) Exact MP0 photonic weight wc,MP vs. collective coupling gtot and the root-free
universal ceiling of Theorem 3, quantifying the > 100× brightness suppression from crossover
(C05) to 71 THz USC (C01). (b) Certified CH2 → CD2 acyl-chain deuteration shifts (C08, C09)
relative to the D2O O–D (∼ 75 THz) and H2O O–H (∼ 104 THz) solvent absorption bands.
Proof. Set x = XMP −ω2 1 > 0 and y = ω2 2 −XMP > 0, so x+y = ∆2. Necessarily min(x, y) ≤ ∆2/2
and max(x, y) < ∆2. If x ≤ y, then 4x2 ≤ ∆2 2 and y2 < ∆2 2, yielding A1/x2 + A2/y2 >
(4A1 + A2)/∆2 2 ≥ (3 min(A1, A2) + A1 + A2)/∆2 2; the case y < x is symmetric. Inverting yields
Eq. (13).
Physically, Eq. (13) reveals a striking spectroscopic inversion (Fig. 2a). In the moderate
strong-coupling regime (g1 = 1, g2 = 1 THz, C05), MP0 carries 35.48% photonic character and
appears as a bright central absorption peak. As collective coupling enters the 71 THz USC regime
(C01: g1 = 11, g2 = 14 THz), the cavity repels LP and UP by ∼ 16–20 THz while squeezing MP0
into an almost pure symmetric–antisymmetric matter supermode with wc,MP = 0.003318 (0.33%,
strictly below the universal ceiling 0.647%; Lean Thm. 19)—a > 100× brightness suppression
relative to C05. Thus, failure to see a bright linear IR peak at 86.2 THz does not by itself exclude
USC, whereas observing a bright central peak at 86.2 THz quantitatively constrains gtot below
USC.
A second clean falsification lever is selective acyl-chain lipid deuteration (CH2 → CD2,
C08--C09), which shifts the bare symmetric and antisymmetric stretches to ν(D) 1 = 62.7 THz
(2091 cm−1) and ν(D) 2 = 65.8 THz (2195 cm−1) [6] while scaling the squared dipole couplings by
reduced mass g(D)2 j ≈ g2 j /2 (g(D) 1 = 7.8, g(D) 2 = 9.9 THz). Even in the unchanged 86.5 THz cavity
(C08), exact cubic bracketing (Lean Thm. 18) places the deuterated polariton triplet at
ν(D) − = 58.3597 THz, ν(D) MP = 64.2364 THz, ν(D) + = 95.1950 THz. (14)
Crucially, both ν(D) − and ν(D) MP shift > 10 THz below the 75 THz D2O O–D solvent stretch band
(Fig. 2b), resolving the aqueous D2O spectral overlap identified in Wave M1 [4]. If biological
modulation tracks the lipid polariton rather than an extraneous cavity or solvent resonance,
feeding perdeuterated fatty acids must abolish the 71 THz response and re-emerge near 58.4 THz
(or 53.0 THz if the cavity retunes with bilayer index, C09).
5
```

---

## Page 6

```text
4 1/N 2D-IR Anharmonicity Discriminator and Dark-Manifold
Leakage
4.1 Exact 1/N Collective Kerr Suppression
Each individual lipid CH2 bond carries an intramolecular mechanical anharmonicity − 1 2 ℏ∆j (b† j,m)2b2 j,m
with bare values ∆1 ≈ 3.6 THz (120 cm−1) and ∆2 ≈ 4.2 THz (140 cm−1) [9]. Projecting onto
the collective bright modes Bj = N −1/2 j ∑Nj m=1 bj,m attenuates the polariton Kerr shifts by exact
1/Nj factors [10, 13]:
∆αα = w2 1,α∆1 N1 + w2 2,α∆2 N2 , ∆αβ = 2 ( w1,αw1,β ∆1 N1 + w2,αw2,β ∆2 N2 ) (α ̸= β). (15)
(We note explicitly that retaining full USC Bogoliubov counter-rotating renormalization multi-
plies the q4 j quartic matrix element by (ωj /να)2 ≈ (86.5/70.6)2 ≈ 1.50, an O(1) prefactor that
leaves the 1/N scaling and six-order-of-magnitude collective-vs.-local separation completely in-
tact.)
Theorem 4 (Exact 1/N Anharmonicity Bound; Lean Thm. 12). For any branch α with non-
negative normalized weights w1,α + w2,α ≤ 1, oscillator counts N1, N2 ≥ Nmin ≥ 1, and bare
anharmonicities 0 ≤ ∆1, ∆2 ≤ ∆max,
∆αα ≤ ∆max Nmin . (16)
As certified in C10--C12 (Fig. 3a), a crista-scale collective ensemble (N1 = N2 = 106, C10)
suppresses the 71 THz LP diagonal anharmonicity to ∆−− = 7.21×10−7 THz—5.82×106× below
bare ∆2 and > 4 × 105× below a 0.3 THz homogeneous linewidth. By contrast, a local N = 1
defect, impurity, or single-molecule resonance (C12) retains ∆−− = 0.721 THz (∼ 24 cm−1),
immediately resolvable as a shifted excited-state absorption (ESA) doublet in diagonal 2D-IR.
Furthermore, in collective USC, the (N1 + N2 − 2) = 1,999,998 dark modes [10, 14] produce a
characteristic polariton–dark cross-peak and Rabi-contraction bleach at (νpump, νprobe) =
(71, 86.2–87.5) THz, which is strictly absent in a passive dielectric filter or thermal artifact.
4.2 Non-Markovian Dark-Manifold Support Leakage: LP Protection vs. MP0
Washout
Coupling N1 + N2 lipid oscillators to one cavity mode via two bright superpositions leaves exactly
(N1 − 1) + (N2 − 1) = N1 + N2 − 2 strictly dark eigenstates at ω1 and ω2 (Lean Thm. 13). Static
inhomogeneous frequency disorder δωj,m of root-mean-square width σinh couples each bright mode
Bj to its orthogonal dark subspace with exact Hilbert–Schmidt norm ∥VBj →Dj ∥2 = σinh. For a
polariton branch separated from the nearest dark continuum by detuning gap δgap > 0, second-
order Schur-complement perturbation bounds the dark-manifold leakage probability by [12]
ηleak ≤ σ2 inh δ2gap (17)
(monotonicity machine-checked in Lean Thm. 14). Evaluating Eq. (17) exposes an acute asym-
metry between LP and MP0 (Lean Thm. 15; Fig. 3b):
• LP Polaron Protection (C13): At ν− ≈ 71.0 THz, δgap = 85.4 − 71.0 = 14.4 THz.
Even under physiological fluid-bilayer disorder σinh = 0.6 THz (∼ 20 cm−1), ηleak(LP) ≤
(0.6/14.4)2 = 1/576 ≈ 0.174% < 1%. The lower polariton is strongly protected against
inhomogeneous broadening.
6
```

---

## Page 7

```text
Figure 3: (a) 1/N 2D-IR diagonal and cross-anharmonicity discriminator separating a collective
crista polariton (C10, N = 106) by six orders of magnitude from a local artifact (C12, N = 1).
(b) Non-Markovian inhomogeneous dark-manifold leakage bound ηleak ≤ (σinh/δgap)2, contrasting
> 188× stronger polaron protection of LP (C13, 0.17%) against MP0 mixing in fluid bilayers (C14,
32.7%) and clean resolution in ordered/gel-phase bilayers (C16, 2.0%).
Table 1: Selected exact-Q certificates from MITO-TWOBAND-CUBIC-HOPFIELD-CERT-1.0
(C01--C16; full SHA-256 manifest in certificates/MANIFEST.json).
Cert Regime / Protocol ν− (THz) νMP (THz) ν+ (THz) Key Certified Bound
C01 Canonical CH2 USC (11, 14) 70.5822 86.2206 106.2124 wc,MP = 0.332% (UB 0.647%)
C02 Asymmetric CH2 (9, 15.4) 70.7147 85.9507 106.3461 wc,MP = 0.271% (UB 0.781%)
C03 Deep USC (14, 19) 66.1812 86.1571 113.3589 wc,MP = 0.183%, ∆νZPE = 6.297
C04 Moderate SC (2, 3) 82.9930 86.0934 90.4629 wc,MP = 7.18% (IR bright)
C05 Crossover (1, 1) 84.7094 86.4800 88.2335 wc,MP = 35.48% (> 100× C01)
C08 CD2, same cavity 58.3597 64.2364 95.1950 > 10 THz below 75 THz D2O
C09 CD2, retuned 64.25 52.9535 63.9452 78.2821 ∆νZPE = 2.431 THz
C10 2D-IR collective (106) ∆−− = 7.21 × 10−7, ∆−,MP = 2.26 × 10−6 THz 5.82 × 106× suppressed
C12 2D-IR local (N = 1) ∆−− = 0.721, ∆−,MP = 2.265 THz O(1) THz ESA doublet
C13 LP leakage (σ = 0.6) δgap = 14.4 THz, ηleak ≤ 1/576 0.174% (protected)
C14 MP0 fluid (σ = 0.6) δgap = 1.05 THz, ηleak ≤ 16/49 32.65% (> 188× LP)
C16 MP0 gel (σ = 0.15) δgap = 1.05 THz, ηleak ≤ 1/49 2.04% (resolvable)
• MP0 Fluid-Bilayer Mixing and Washout (C14--C15): Because MP0 is trapped inside
the 2.1 THz doublet, its maximum possible gap is δgap ≤ 1.05 THz. At σinh = 0.6 THz,
ηleak(MP0) ≤ 16/49 ≈ 32.65% (> 188× larger than LP), and above σinh = 1.05 THz (C15,
σinh = 1.2 THz, ηleak = 1.306) MP0 washes completely into the dark reservoir.
• Ordered/Gel-Phase Resolution Window (C16): Cooling or stiffening model mem-
branes into the ordered gel phase narrows CH2 inhomogeneous disorder to σinh ≈ 0.15 THz
(∼ 5 cm−1) [6], dropping ηleak(MP0) to 1/49 ≈ 2.04% and reopening a sharp Raman/2D-IR
visibility window for MP0.
5 Verification Boundary, Spectroscopic Caveats, and Experimen-
tal Matrix
To preserve strict epistemic transparency, we separate our claims into three explicit layers:
7
```

---

## Page 8

```text
1. Lean 4.36.0 Kernel Layer (Machine-Checked): All 20 theorems in MitoTwoBandCubic
HopfieldCert.lean compile under lean -DwarningAsError=true and lake build with
0 sorry, 0 grind, and 0 Classical.choice (audited via #print axioms; only construc-
tive propext/Quot.sound or zero axioms). This layer proves the exact TRK cubic factor-
ization, global stability on (−∞, 0], strict Cauchy–Hopfield pivot signs, the calculus-free
AM–GM proof of universal two-band ZPE positivity, the root-free universal MP0 photonic
suppression inequality, the 1/N anharmonicity bound, dark-manifold dimensionality, leak-
age monotonicity, and exact integer-scaled root brackets for C01, C02, and C08.
2. Exact-Q Python Certificate Layer: The exact rational verifier module (src/mito_twoband_
cubic_hopfield_verifier.py) is AST-audited to contain zero floats, zero / or ** opera-
tors, and zero limit_denominator calls. It certifies 16 canonical JSON records (C01--C16,
SHA-256 locked in MANIFEST.json) and passes 57/57 adversarial pytest checks.
3. Physical Modeling Caveats and Unverified Experimental Hypotheses: Real fluid
phospholipid membranes exhibit weak Fermi-resonance mixing between the CH2 symmetric
stretch (∼ 2850 cm−1) and the CH2 scissoring overtone 2δ(CH2) (∼ 2890 cm−1) [5, 6], as
well as terminal CH3 stretches (∼ 2872/2960 cm−1); extending the secular polynomial to
K vibrational bands preserves exact TRK Cauchy interlacing with K − 1 trapped middle
polaritons. Moreover, our 71 THz couplings (g1, g2) are conditioned on the unrefereed
empirical claim of Ref. [1]; whether intact cristae actually achieve subwavelength cavity
confinement and USC oscillator strength remains unverified [4].
Together, our theorems prescribe a decisive three-experiment falsification protocol: (i) 2D-IR
diagonal anharmonicity at 71 THz (∆−− < 10−5 THz with (71, 86.2–87.5) THz cross-peak for
collective USC vs. ∆−− ∼ 0.7 THz for a local mode); (ii) ordered/gel-phase Raman or 2D-IR
search for the trapped MP0 near 86.0–86.2 THz (ηleak ≤ 2% at σinh = 0.15 THz); and (iii) acyl-
chain CH2 → CD2 deuteration shifting LP and MP0 cleanly to 58.4 and 64.2 THz, free of D2O
solvent interference.
References
[1] Y. Yang, H. Gu, and B. Song. Mitochondrial cristae as mid-infrared polaritonic cavities mod-
ulating cellular atp synthesis. Unrefereed preprint, bioRxiv:10.64898/2026.09.10.750628v1,
September 2026. Unrefereed preprint awaiting independent experimental replication.
[2] Lluis Eriksson. Geometry and resource boundaries for biological polariton models.
AIRR.SCIENCE Record ARR-2025-2AQXS44H6Z8GQAG2, 2025.
[3] Lluis Eriksson. Mito-polariton resource-boundary certificates and exact thermodynamic au-
dits. AIRR.SCIENCE Record ARR-2026-1E91AXEJYT890TQC, 2026.
[4] Lluis Eriksson. Mitochondrial polariton audit series wave m1: Subwavelength con-
finement, dressed usc thermodynamics, and atp modulation bounds. AIRR.SCIENCE
Records ARR-2026-75841S47Z59VMSN2, ARR-2026-038Y5T8GYG9F7TTR, and ARR-
2026-0CXEJ0MRT995CAK8, 2026.
[5] R. G. Snyder, S. L. Hsu, and S. Krimm. Vibrational spectra in the c–h stretching region
and the structure of the polymethylene chain. Spectrochimica Acta Part A: Molecular Spec-
troscopy, 34(4):395–406, 1978.
[6] Henry H. Mantsch and Ronald N. McElhaney. Phospholipid phase transitions in model and
biological membranes as studied by infrared spectroscopy. Chemistry and Physics of Lipids,
57(2–3):213–226, 1991.
8
```

---

## Page 9

```text
[7] J. J. Hopfield. Theory of the contribution of excitons to the complex dielectric constant of
crystals. Physical Review, 112(5):1555–1567, 1958.
[8] Anton Frisk Kockum, Adam Miranowicz, Simone De Liberato, Salvatore Savasta, and Franco
Nori. Ultrastrong coupling between light and matter. Nature Reviews Physics, 1:19–40, 2019.
[9] Peter Hamm and Martin Zanni. Concepts and Methods of 2D Infrared Spectroscopy. Cam-
bridge University Press, 2011.
[10] Bo Xiang, Raphael F. Ribeiro, Adam D. Dunkelberger, Jiaxi Wang, Yingmin Li, Blake S.
Simpkins, Jeffrey C. Owrutsky, Joel Yuen-Zhou, and Wei Xiong. Two-dimensional infrared
spectroscopy of vibrational polaritons. Proceedings of the National Academy of Sciences,
115(19):4845–4850, 2018.
[11] Adam D. Dunkelberger, Blake S. Simpkins, Igor Vurgaftman, and Jeffrey C. Owrutsky.
Vibration-cavity polariton chemistry and dynamics. Annual Review of Physical Chemistry,
73:429–451, 2022.
[12] R. Houdré, R. P. Stanley, and M. Ilegems. Vacuum-field rabi splitting in the presence of
inhomogeneous broadening: Resolution of a homogeneous linewidth in an inhomogeneously
broadened system. Physical Review A, 53(4):2711–2715, 1996.
[13] Raphael F. Ribeiro, Luis A. Martínez-Martínez, Matthew Du, Jorge Campos-Gonzalez-
Angulo, and Joel Yuen-Zhou. Polariton chemistry: controlling molecular dynamics with
optical cavities. Chemical Science, 9(30):6325–6339, 2018.
[14] Bo Xiang, Raphael F. Ribeiro, Matthew Du, Liying Chen, Zimo Yang, Jiaxi Wang, Joel Yuen-
Zhou, and Wei Xiong. Intermolecular vibrational energy transfer enabled by microcavity
strong light-matter coupling. Science, 368(6491):665–667, 2020.
9
```
