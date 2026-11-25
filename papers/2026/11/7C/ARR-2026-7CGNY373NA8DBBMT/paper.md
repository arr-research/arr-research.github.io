# Constructive Lean 4 Formalization and Exact-Rational Certificates for Dynamic-Streaming Euclidean Diameter Bounds

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-7CGNY373NA8DBBMT` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/euclidean-diameter-streaming-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `0d495d0b90b4df2790dde014a1a7421a63c193122b6f13681675efc79fbc9d0e`

## Abstract

Jeff Giliberti and MohammadTaghi Hajiaghayi (arXiv:2611.33139, Nov. 24, 2026) resolved the update-time versus space tradeoff for high-dimensional Euclidean diameter in fully dynamic streams: for every fixed c > sqrt(3), their one-pass algorithm maintains a current witness pair with approximation factor c in O~(N^(1-eps_c) poly(d)) space (explicitly eps_2 = 10^-10 at c = 2) and worst-case update time poly(d, log N), while every constant-factor c-approximation requires N^Omega(1/(c^2 log(c+1))) words even on short binary set streams of at most 2N-1 updates. We present a standalone, zero-dependency Lean 4.35.0 formalization (EuclideanDiameterStreaming.lean) of 18 core algebraic, variance-hull, Cauchy-Schwarz, parallel-axis, nested-cap shrinkage, Appendix A.1 Table 3 factor-2 parameter, non-circular submodular diagonal-squared, and baseline positivity theorems (0 sorry, 0 warnings, 0 Classical.choice), paired with a zero-floating-point exact-Q four-mode certificate auditor (EUCLID-DIAM-CERT-1.0). Across 16 canonical certificates (0.129-3.412 ms), the auditor verifies an exact zero-slack 12-point two-simplex attainment in Q^13 (a = 13/7, diam(H_a(S))^2 = (289/49) diam(S)^2), Lemma 4.1 anchor-variance parallel-axis composition, all Appendix A.1 Table 3 factor-2 inequalities, and exhaustive Lemma 10.2 submodular diagonal-squared bounds D^2 <= 2sZ while rejecting 60/60 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Formalization and Exact-Rational
Certificates for Dynamic-Streaming Euclidean Diameter
Bounds
Lluis Eriksson∗
November 25, 2026
Abstract
Jeff Giliberti and MohammadTaghi Hajiaghayi
(arXiv:2611.33139, Nov. 24, 2026) resolved the
update-time versus space tradeoff for high-dimensional
Euclidean diameter in fully dynamic streams: for every
fixed c >
√
3, their one-pass algorithm maintains a
current witness pair with approximation factor c in
˜O(N1−εc poly(d))space (explicitly ε2 = 10 −10 at factor
c= 2) and worst-case update timepoly(d,logN ), while on
the hardness side every constant-factorc-approximation
requires NΩ(1/(c2 log(c+1))) words even on linear-length
binary set streams of at most2 N− 1updates. We
present a standalone, zero-dependencyLean 4.35.0
formalization ( EuclideanDiameterStreaming.lean)
of 18 core algebraic, variance-hull, Cauchy–Schwarz,
parallel-axis, nested-cap shrinkage, Appendix A.1 Table 3
factor-2 parameter, submodular diagonal-squared, and
baseline positivity theorems (0 sorry, 0 warnings,
0 Classical.choice; all 18 using only [propext,
Quot.sound]), paired with a zero-floating-point exact-Q
four-mode certificate auditor (EUCLID-DIAM-CERT-1.0).
Across 16 canonical certificates (0 .129–3.412 ms exact
replay latency), the auditor independently verifies an
exact zero-slack 12-point two-simplex attainment inQ13
(a = 13 /7, diam(Ha(S))2 = 289
49 diam(S)2), Lemma 4.1
anchor-variance parallel-axis composition, all Appendix A.1
Table 3 factor-2 inequalities (2a2 −1 = 3 .999122 < 4,
ε0 >1/6345504000 >10−10), and exhaustive Lemma 10.2
submodular diagonal-squared bounds D2 ≤2sZ, while
rejecting 60/60 live adversarial forgery attacks (plus 2 raw
IEEE-754/NaNparser rejections).
1 Introduction
Maintaining the Euclidean diameterdiam(Pt)of a high-
dimensional point setPt ⊂[−∆,∆]d ∩Z d under arbitrary
insertions and deletions separates polynomial space from
polynomial update time [1, 4, 5, 6]. Giliberti and Haji-
∗Independent Researcher. Code, Lean 4 proofs, and certifi-
cates: MIT License; manuscript and figures: CC-BY-4.0. Pre-
pared with transparent AI coding, formalization, and drafting as-
sistance via Google Antigravity; all Lean 4 theorems, exact- Q
verifiers, and adversarial tests were independently compiled and
verified locally. Repository: https://github.com/lluiseriksson/
euclidean-diameter-streaming-certificates.
aghayi [3] established both sides of this separation via four
exact mathematical pillars:
1. Farthest-Distance Hull & Tight Two-Simplex At-
tainment (Sec. 5.1, Lem. 5.1):Expanding every
ball containing a frozen sampleS by a >
√
2 yields
Ha(S) = ⋂
qB(q,aRS(q)) = ⋃
λB(µλ,
√
(a2 −1)Vλ),
forcing diam(Ha(S)) ≤
√
2a2 −1 diam(S)with ex-
act two-simplex attainment h2 + 2 V = 1, h +
2
√
(a2 −1)V =
√
2a2 −1 , and witness radius bound
RS(q)<D univ/(a−1).
2. Anchor-Variance Composition (Sec. 4.2,
Lem. 4.1):Every exposed candidate ball with
convex anchor weights λz, mean q, and vari-
ance V satisfies the exact parallel-axis identity∑
z∈K λz∥z−s ∗∥2 = V + ∥q−s ∗∥2 ≤L 2
node, giving
mixed-pair factor
√
(1 +η) 2 +a2κ2 strictly below√
2a2 −1for smallη >0,κ→1.
3. Nested Spherical Caps & Explicit Factor-2 Ta-
ble 3 (Sec. 6.2, App. A.1):For
√
2< λ <
√
3,
mλ := λ2/2 −1 > 0gives the exact quadratic mar-
gin( λ−t )2 −q≥m λ on t2 + q≤ 1, shrinking
cap radii by r2
i+1 = r2
i −m λ/2. At c = 2, Ap-
pendix A.1’s exact rational tuple (a = 1581
1000 , λ = 79
50 ,
κ = 109
100 , ηin = 1
100 , s = 1
2003 , ρ = 1
4006 , Bκ = 2000,
G= 32) satisfies every approximation, two-mask, oracle-
work (s(Bκ + 1) −1 = − 2
2003 < 0), and space-saving
(ε0 > 1
6345504000 >10 −10) inequality strictly.
4. Submodular Diagonal-Squared Lower Bound
(Sec. 10, Lem. 10.2, Thm. 10.1):Turning the
streaming state into a deterministic messageM of sbits
defines the monotone submodular conditional entropy
f(A) = H(M|X P\A); anym cap-target pairs( Bi,zi)
(with repetitions permitted) satisfy D2 ≤ 2sZ for
Aij = f(Bi∪{zj}) −f(Bi), D= ∑
iAii, Z = ∑
i,jAij,
while the antipodal vs. cap separation(1 −δ0)/r =
g−1/100 >c forces NΩ(1/(c2 log(c+1))) words on streams
of≤2N−1updates.
Contributions and Explicit Scope.All probabilistic
Gaussian-projection, VC-net, Sion minimax, Beta-chord
concentration, and streaming-schedule theorems belong
to [3] (which notes separate Mathlib-based Lean formaliza-
tions on GitHub). Here we deliver an independent,zero-
dependency(no Mathlib) verification stack separating two
audited layers: (i) 18 zero-sorry, zero-Classical.choice
1

--- Page 2 ---
Lean 4.35.0[2] algebraic, inductive parallel-axis, nested-
cap, Table 3, and quadratic-optimization theorems in
EuclideanDiameterStreaming.lean; (ii) the pure-stdlib
exact-Q verifier EUCLID-DIAM-CERT-1.0; (iii) 16 canonical
certificates across four modes; and (iv) a 60-attack live
red-team suite (plus 2 raw JSON IEEE-754/NaN rejections)
with 39-file SHA-256 manifest enforcement.
2 Constructive Lean 4.35.0 Kernel
The standalone module lean/EuclideanDiameter
Streaming.lean compiles cleanly under Lean 4.35.0 with
zero external dependencies, zero warnings, and zerosorry.
Auditing all 18 theorems via lean/AuditAxioms.lean
confirms all 18 use only[propext, Quot.sound] with0
Classical.choiceorLean.ofReduceBool(Table 1).
Proposition 1(Constructive Streaming-Diameter Kernel).
The 18 theorems in Table 1 constructively certify four exact
layers overZand inductive lists:
1. Hull & Anchor Composition (Thms. 1–6):Certifies1 +
a2,2 <2a2 −1, exact Lagrange identities for Lemma 5.1
and Lemma 4.1 Cauchy–Schwarz bounds, two-simplex
attainment (h2 + 2V = 1, squared hull distance2a2 −1),
witness radius boundRS(q) <Duniv/(a−1), and the full
inductive parallel-axis decompositionW∑ wi(zi−s)2 =
(W∑ wiz2
i −M2) + (M−Ws )2 over arbitrary weighted
anchor lists.
2. Nested Spherical Caps (Thms. 7–9, 15):Proves
quadratic completion( λ−t )2 −q≥m λ, cap-radius
shrinkage inequality1 −t2
i ≤r 2
i −mλ/2, cap ball con-
tainment( t−ti)2 +q≤ 1−t2
i, and the3K local-snapshot
decoder budget.
3. Factor-2 Table 3 & Baseline (Thms. 10–14, 18):Cer-
tifies all Table 3 factor-2 constants (ε2 = 10−10), both
two-stage mask inequalities, Eq. (29) parabolic identity,
Eq. (32) coupled tail rate, and Appendix A.3.3’s degree-4
baseline polynomial positivity.
4. Lower-Bound Separation & Submodular Optimization
(Thms. 16–17):Proves antipodal separationg−1/100 >
c and derivesD2 ≤2sZ non-circularly from the cleared
chain bound2 prD−p 2Z≤ 2sr2 together with the La-
grange maximality identity of Lemma 10.2.
3 Exact-Rational Verifier Architec-
ture
The pure-stdlib verifier EUCLID-DIAM-CERT-1.0
(src/diameter_exact.py,src/diameter_certifier.py)
uses Python int and fractions.Fraction exclusively
(source-audited for zero float(, math., or numpy).
It rejects IEEE-754 tokens and NaN/Infinity, non-
ASCII/Unicode digits ( isascii() and isdigit()),
strings > 2000chars, unreduced or leading-zero ra-
tionals, -0, booleans-as-ints, unknown keys, duplicate
points/probes, and nesting depth>20:
Definition 1(FourEUCLID-DIAM-CERT-1.0Modes).
Figure 1: (a) Hull factor
√
2a2 −1 vs. ideal mixed factor√
1 +a2 for a >
√
2, highlighting the factor-2 pointa =
1581/1000(2 a2 −1 = 3.999122) and our exact zero-slack
rational two-simplex attainment ata= 13/7(
√
2a2 −1 =
17/7). (b) Axial separation margin(λ−t )2 −(1 −t2) ≥
mλ = 1241/5000at λ= 79/50with Stage-1 cap boundary
t= 3/5.
1. Mode 1( hull_variance_and_simplex_cert): Re-
computes diam(S)2, convex means µ1,µ2, variances
V1,V2, verifies h2 + V1 + V2 = E∥s−t∥2 ≤diam (S)2,
checks Lemma 5.1 hull membership∥yi −µi∥2 ≤(a2 −
1)Vi, verifies∥y1−y2∥2 ≤(2a2−1)diam(S)2, and checks
exact tight-attainment equality.
2. Mode 2( anchor_composition_and_mixed_cert):
Recomputes anchor meanq, varianceV, F2 = ∥q−s∗∥2,
verifies ∑ λz∥z−s ∗∥2 = V + F2 ≤L2
node, and checks
max{(1 +η) 2 + 1,(1 +η) 2 +a2κ2}<2a 2 −1<c 2.
3. Mode 3(factor2_table3_and_masks_cert): Audits
all Appendix A.1 Table 3 inequalities, both two-stage
masks (mλ, 65
24 mλ >(1+ ηm)r2
2, g(3/5) <0, Flb(3/5) =
79
75 > 21
20 ), oracle-work and space exponents (εlb
0 >
10−10), Appendix A.3.3 baseline positivity, and exact
axial/parabolic checks on distinct unit-disk probes(t,q).
4. Mode 4( submodular_diagonal_lowerbound_cert):
Exhaustively verifiesf(∅) = 0, monotonicity, and sub-
modularity across all2n subsets (n≤ 10), recomputes
the exactm×m gain matrixAij = f(Bi∪{zj}) −f(Bi)
(allowing repeated targets), certifies Lemma 10.2D2 ≤
2sZ, and checks Theorem 10.1 separation(1−δ0)/r>c .
4 Empirical Atlas and Red-Team
Audit
Running scripts/run_all_experiments.py (Win-
dows 11, Python 3.12) deterministically emits 16 canonical
certificates (4 per mode) and 4 experiment JSONs, audited
end-to-end by scripts/verify_all.py with SHA-256
verification across all 39 tracked repository files.
1. Exact Zero-Slack Two-Simplex Attainment & Ta-
ble 3 Margins (Figs. 1–2).Solving the Pell-like equa-
tion2 p2 −q2 = r2 at( p,q,r ) = (13,7,17)yields a= 13/7,
2a2 −1 = (17 /7)2, h = 7/17, and V = 120/289; taking
m = 6vertices per simplex gives exact rational simplex
scale ssimp =
√
6
5 V = 12/17and hull radius
√
(a2 −1)V =
120/119, yielding a 12-point rational instance in Q13
2

--- Page 3 ---
Table 1: All 18 Lean 4.35.0 theorems inEuclideanDiameterStreaming.lean (0 sorry, 0 warnings, 0Classical.choice;
all 18 use only[propext, Quot.sound]), showing exact cleared-integer / inductive statements and references to [3].
# Lean 4 Theorem Identifier Exact Formalized Statement (ClearedZ/ Inductive Type) Ref. [3]
1hull_factor_exceeds_mixed_and_cand2a2
d<a2n⇒a2
d+a2n<2a2n−a2
d∧2a2
d<2a2n−a2
d(1+a2,2<2a2−1) Lem. 4.1
2hull_cauchy_schwarz_squared(h+CR) 2 + (Ch−R)2 = (1 +C2)(h2 +R2)∧(h+CR) 2 ≤(1 +C2)(h2 +R2)Lem. 5.1
3two_simplex_tight_attainmenth 2H=a2
dD,VH= (a2n−a2
d)D⇒(h2+2V)H=DH(h2+2V=1, squared hull dist= 2a2−1) Sec. 5.1
4witness_ball_radius_bounda nR<adD+adR⇒(an−ad)R<adD(RS(q)<Duniv/(a−1)) Eq. (13)
5anchor_variance_parallel_axis_sum∀xs:List(Z×Z), W ∑wi(zi−s)2 = (W∑wiz2
i −M2) + (M−Ws)2 (W2(V+F2)) Eq. (7)
6mixed_pair_cauchy_schwarz(Ar+BF) 2 + (Br−AF)2 = (A2 +B2)(r2 +F2)∧(Ar+BF) 2 ≤(A2 +B2)(r2 +F2)Eq. (4)
7axial_separation_margin_quadratict 2 +q≤D 2 ⇒λ2 −2D2 ≤2((λ−t)2 −q)((λ−t) 2 −q≥m λ) Sec. 6.2
8cap_shrinkage_step_radius0<D,r 2 ≤D,0≤η,4η≤m,u cap ≤(D+η)r2 −Dm⇒2ucap ≤2Dr2 −DmSec. 6.2
9cap_containment_ball_radius0≤t i≤t∧t 2 +q≤D 2 ⇒(t−ti)2 +q≤D 2 −t2
i Sec. 6.2
10factor2_table3_approximation_bounds2a2−1 = 3.999122<4, mixed= 3.9898284241<3.999122, cand= 2.0201, oracle1.084441>1.0801Table 3
11factor2_table3_space_exponentss(B κ+1)−1 =−2
2003, 2000
2003,4005
4006 <1−10−10,96000·2003·33 = 6345504000<1010 App. A.1.6
12factor2_two_masks_exact_positivitymλ= 1241
5000, 65
24mλ= 16133
24000> 84
125,Flb(3
5) =79
75 >21
20,g( 3
5) =−5437
12500<0App. A.1.2
13potential_parabolic_identity_eq29D2(λ−t)2 −(λ2 −D2)(D2 −t2) = (λt−D2)2 ≥0Eq. (29)
14coupled_tail_rate_inequality_eq324ABu≤(A+Bu) 2 ∧75·17152 = 1286400<1340064 = 24·4·297·47Eq. (32)
15local_snapshot_age_3K_boundcur≤K∧snap−cur≤2K⇒snap≤3KLem. 7.2
16lower_bound_diameter_gap_exceeds_cg=c+ 1⇒100c<100g−1((1−δ 0)/r=g−1/100>c) Sec. 10.1.2
17submodular_diagonal_squared_quad_optZ >0∧(∀p,r,2prD−p2Z≤2sr2)⇒D2 ≤2sZ∧Z(2Dq−Zq2) + (Zq−D)2 =D2 Lem. 10.2
18baseline_factor2_poly_positive0<p∧100p≤q⇒9pq 3 −28p2q2 −17p3q−8p4 >0(γ∈(0,1/100]) App. A.3.3
Figure 2: (a) Strict rational slack (LHS/RHS< 1) across
all six Appendix A.1 Table 3 and two-stage mask inequali-
ties. (b) Exact Mode 4 Lemma 10.2 submodular diagonal-
squared ratiosD2/(2sZ) ≤1across four audited families
(including repeated targets and27 = 128-subset coverage).
(hull_two_simplex_tight_a13_7) with diam(S)2 = 1
and ∥y1 −y2∥2 = 289 /49 = (2 a2 −1)diam(S)2 (exact
zero-slack attainment, replayed in3.412 ms). Figure 2(a)
confirms strict slack (<1) across all six Appendix A.1 Ta-
ble 3 & mask inequalities (tightest ratio0.9998for2 a2−1 =
3.999122 <4), while Fig. 2(b) audits Lemma 10.2 across
four submodular families up to27 = 128subsets, reaching
exact ratioD2/(2sZ) = 1/2on the sharp modular instance
(submod_modular4_sharp_half_c3) and289 /704 ≈0.411
with repeated targets.
2. 16-Certificate Atlas & 60/60 Red-Team Audit
(Table 2, Fig. 3).All 16 canonical certificates replay in
0.129–3.412 ms with zero floats. Intests/test_suite.py,
60 live adversarial forgery attacks (16 global AST/Unicode-
digit/length/depth + 11 per mode) plus 2 raw JSON IEEE-
754/NaN checks achieve60/60 (100%)red-team rejection
(63/63pytestchecks passing in0.12 s).
5 Conclusion
We delivered a standalone, zero-dependency, zero-floating-
point verification stack for Giliberti and Hajiaghayi’s
Figure 3: (a) Zero-float exact replay latency across all
16 canonical EUCLID-DIAM-CERT-1.0 certificates (0.129–
3.412 ms). (b) 60/60 live adversarial forgery rejections
across global AST/Unicode and Modes 1–4.
dynamic-streaming Euclidean diameter bounds [3], pairing
18 zero-sorry, zero-Classical.choice Lean 4.35.0 theo-
rems with the exact-Q auditor EUCLID-DIAM-CERT-1.0, 16
canonical certificates (including an exact zero-slack rational
two-simplex attainment inQ13), and 60/60 live adversarial
forgery rejections.
References
[1] Pankaj K. Agarwal and R. Sharathkumar. Stream-
ing algorithms for extent problems in high dimensions.
Algorithmica, 72(1):83–98, 2015.
[2] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, pages 625–635. Springer,
2021.
[3] Jeff Giliberti and MohammadTaghi Hajiaghayi. On
euclidean diameter in dynamic streams.arXiv preprint
arXiv:2611.33139, November 2026.
[4] Piotr Indyk. Better algorithms for high-dimensional
proximity problems via asymmetric embeddings. In
Proceedings of the 14th Annual ACM–SIAM Symposium
on Discrete Algorithms (SODA), pages 539–545, 2003.
3

--- Page 4 ---
Table 2: All 16 canonical exact-QEUCLID-DIAM-CERT-1.0
certificates (zero IEEE-754 arithmetic; 20-run mean latency
in ms).
Certificate Stem Mode Exact Certified Witness ms
hull_two_simplex_tight_a13_7M1Q13,a=137, tight∥y1−y2∥2=28949 3.412hull_octahedron_factor2_a1581M1Q3,a=15811000,diam2=4, pair90.390hull_square_a3_2M1Q 2,a=32,2a2−1=72, pair40.209hull_4d_a25_17M1Q 4,a=2517,2a2−1=961289, pair132 0.301anchor_factor2_canonical_3dM2 Table 3(a,η,κ),L2node=512 ≥V+F2=180.184anchor_asymmetric_4d_c19_10M2c=1910,a=32, mixed3381310000<72 0.222anchor_tight_c9_5_2dM2c= 95,a=2920, mixed<641200<8125 0.129anchor_5pt_cluster_c5_2M2c=52,a=1710, 5 anchors inQ3 0.204table3_canonical_factor2_exactM3 Table 3 exact,εlb0= 16345504000, 6 probes 0.240table3_sharper_s2002_G30M3s=12002,G=30,εlb0= 15957952000 0.201table3_tighter_hull_a1580M3a=7950,2a2−1=49911250<4, 4 probes 0.188table3_conservative_s2005M3s=12005,κ=10891000,γ=11000 0.197submod_cov6_cycle_c2M42 6subsets,D2/(2sZ)=14, gap299100>20.677submod_hit5_repeated_targets_c3_2M425subsets, rep. tgts, ratio289704, gap299100 0.302submod_modular4_sharp_half_c3M424subsets, sharp ratio12, gap399100>30.140submod_cov7_overlap_c4M427subsets, ratio4413634, gap499100>41.647
[5] Sanjeev Khanna, Ashwin Padaki, Krish Singal, and
Erik Waingarten. A polynomial space lower bound for
diameter estimation in dynamic streams. InProceedings
of the 66th IEEE Annual Symposium on Foundations
of Computer Science (FOCS), pages 119–148, 2025.
[6] Ashwin Padaki, Krish Singal, and Erik Waingarten.
A near-optimal space lower bound for euclidean diam-
eter estimation in dynamic streams.arXiv preprint
arXiv:2609.19089, 2026.
4
