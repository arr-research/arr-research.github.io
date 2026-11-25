# Constructive Lean 4 Kernel and Exact Zero-Float Certificates for Google Research Cogentic's Sub-Quasi-Polynomial Discrete Logarithm Proof

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-2J6J7BBBKX9V5R3K` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/cogentic-discrete-log-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `3fe4e239e627690faa8a8890e11407e73f61326033a4e9186de89fce9fb7d82d`

## Abstract

A November 25, 2026 preprint from Google Research's Cogentic system proposes an unconditional classical zero-error Las Vegas algorithm for the Discrete Logarithm Problem (DLP) in F_{p^n}^x of fixed characteristic p with claimed expected runtime exp((2+o(1))/ln(ln(ln n)) * (ln n)^2) = (p^n)^{o(log n)}, improving upon the (p^n)^{Theta(log n)} barrier of Kleinjung-Wesolowski and Lido. Rather than assuming peer-reviewed validation of its analytic pillars, we deliver an independent, explicitly scoped, zero-floating-point verification companion for its deterministic algebraic, elliptic-Lang, linearized-monodromy, and factoring-free unimodular mechanisms. Layer 1 (CogenticDiscreteLog.lean) proves 18 standalone constructive Lean 4.35.0 algebraic, inductive, and arithmetic sub-lemmas (zero sorry, zero axiom, zero Classical.choice, zero warnings; 1 zero-axiom, 2 [propext], and 15 [propext, Quot.sound]). Layer 2 (DLP-COGENTIC-CERT-1.0) is a pure-stdlib Python int auditor across four modes that certifies 16 canonical finite witnesses in 1.133-36.640 ms—including live exact Lang-isogeny equations phi_q(I_0) = I_0 + Q across p in {2,3,5,7}, Moore/affine-Moore pencils with complete splitting, and factoring-free SL_2(Z) solves modulo unfactored composites up to M_L = 406,901—and rejects 61/61 live adversarial forgeries with exact branch assertions (65/65 pytest checks).

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Kernel and Exact Zero-Float Certificates
for Google Research Cogentic’s Sub-Quasi-Polynomial
Discrete Logarithm Proof
Lluis Eriksson∗
November 25, 2026
Abstract
A November 25, 2026 preprint from Google Research’s Co-
gentic system [4, 2] proposes an unconditional classical zero-
error Las Vegas algorithm for the Discrete Logarithm Prob-
lem (DLP) inF×
pn of fixed characteristicp with claimed ex-
pected runtimeexp
(2+o(1)
ln ln lnn(lnn)2)
= (pn)o(logn) , improv-
ing upon the(pn)Θ(logn) barrier of Kleinjung–Wesolowski
and Lido. Rather than assuming peer-reviewed validation
of its analytic pillars, we deliver an independent, explicitly
scoped, zero-floating-point verification companion for its de-
terministic algebraic, elliptic-Lang, linearized-monodromy,
and factoring-free unimodular mechanisms. Layer 1 (Coge
nticDiscreteLog.lean) proves 18 standalone constructive
Lean 4.35.0 algebraic, inductive, and arithmetic sub-lemmas
(zero sorry, zero axiom, zero Classical.choice, zero
warnings; 1 zero-axiom, 2[propext], and 15[propext,
Quot.sound]), including modular non-membership sound-
ness,2 ×2Frobenius-scalar and3 ×3affine Moore identities,
2×2transvection determinant and conjugation identities,
Möbius adjugate invariance, cocycle-coboundary rearrange-
ment, theq0 ≥3degree gap, Jordan transposition conju-
gation, Waterhouse’s coprimality dichotomy, parallelogram
Cauchy–Schwarz, constant-field pinch and Castelnuovo in-
duction, the exactB-adic descent-tree sum,SL2(Z)uni-
modular elimination, non-membership exponent soundness,
CRT recombination, and Theorem 1.2 rational threshold
guards. Layer 2 (DLP-COGENTIC-CERT-1.0 ) is a pure-
stdlib Pythonint auditor across four modes that certifies
16 canonical finite witnesses in1.133–36.640 ms—including
live exact Lang-isogeny equationsϕq(I0) = I0 + Q across
p∈{ 2,3,5,7}, Moore/affine-Moore pencils with complete
splitting, and factoring-freeSL2(Z)solves modulo unfac-
tored composites up toML = 406,901—and rejects 61/61
live adversarial forgeries with exact branch assertions (65/65
pytest checks).
∗Independent Researcher. Code, Lean 4 proofs, and certifi-
cates: MIT License; manuscript and figures: CC-BY-4.0. Pre-
pared with transparent AI coding, formalization, and drafting as-
sistance via Google Antigravity; all Lean 4 theorems, exact finite-
field/elliptic/unimodular verifiers, and adversarial tests were indepen-
dently compiled and verified locally. Repository:github.com/lluis
eriksson/cogentic-discrete-log-certificates.
1 Introduction and Scope Calibra-
tion
Given a primep≥ 2, a degree-n monic irreducible f∈
Fp[X]presenting Fpn = Fp[X]/(f(X)), andg,h∈F ×
pn, the
zero-error Las Vegas DLP (Definition 1.1 of [4]) demands
either x∈{ 0,...,p n −2}with gx = h or an explicit non-
membership exponentE∈{ 1,...,p n−1}satisfying gE = 1
and hE ̸= 1(without factoring pn −1). Prior heuristic [1]
and unconditional [5, 6] Frobenius descents usedPGL2-
orbits of Tq −T , reducing degrees by a constant factor
per step and hitting complexity(pn)Θ(logn) . The Cogentic
preprint [4,2] proposes breaking this barrier via two coupled
mechanisms:
1. Ordinary elliptic Lang presentation (Eq. (1)):
Choosing Q∈E (Fq)of exact order n and I0 ∈E (Fqn)
satisfying
ϕq(I0) =I0 +Q, x P(I0)q = ˜xP(I0),(1)
turns q-Frobenius into low-degree translationτQ+ϕq(P)
along the orbitI.
2. Sparse Fq0 -affine Frobenius pencils (Eq.(2)):Re-
placing degree-q dense polynomials (whose generic mon-
odromy isSq) by sparseFq0 -linearized pencils with inte-
ger shiftt≥1and degree parameterm≥1,
LZ(T) =
m−1∑
j=0
cj(Z)T qt+j
0 +
m∑
j=0
bj(Z)T qj
0 +d0(Z),(2)
traps the monodromy inside AGLN(Fq0 ) ×SNR, tar-
geting an unbounded degree-reduction factor B≍
(ln lnn)/(slnp )and shrinking tree depth to(lnn)/lnB .
Honest Two-Layer Verification Scope.We delineate
explicitly what is proved universally in Lean 4 vs. verified on
finite exact witnesses vs. left in the companion preprint [4]:
1. Layer 1 (Lean 4.35.0 Kernel, Universal Algebraic
& Inductive Sub-Lemmas): lean/CogenticDis
creteLog.lean proves 18 zero-dependency theorems
(Table 1) covering the exact discrete algebraic, induc-
tive, and rational-threshold sub-lemmas extracted from
Definition 1.1, Lemmas 3.1–3.4, 4.1–4.2, 5.1, 6.2–6.4,
Section 6.2, and Theorem 1.2 of [4].
1

--- Page 2 ---
2. Layer 2 (Exact Zero-Float Multi-Mode Auditor):
DLP-COGENTIC-CERT-1.0 audits finite exact instances
in Fp[X], F×
pn, canonical ordinary E/Fq and E/Fqn
across p∈{ 2,3,5,7}, Moore/affine-Moore determinants
and splitting linearized pencils, factoring-free SL2(Z)
SolveModM systems, and exact Theorem 1.2(2) parame-
ter tuples.
3. Explicit Non-Claims:We donotformalize in Lean 4
Waterhouse/Rück existence of ordinary elliptic curves,
general N×N Moore determinants or full group coho-
mology H1(GL(V),V ) = 0(Table 1 #2 and #7 for-
malize only the2 ×2scalar-substitution identity and
the cocycle-coboundary rearrangement step), Riemann–
Roch/Hasse–Weil/Hurwitz/Castelnuovo function-field
theorems, Artin–Schreier/Kummer indecomposability
(Lemma 4.8), Wan’s effective Dirichlet theorem, or mul-
titape Turing-machine bit-complexity accounting (Ap-
pendix A); those analytic and arithmetic-geometric pil-
lars remain unverified outside [4].
2 Constructive Lean 4.35.0 Kernel
lean/CogenticDiscreteLog.lean compiles standalone
in2 .1 sunder Lean 4.35.0 [3] with zero external imports,
zero warnings, zero sorry, and zero Classical.choice.
Auditing via AuditAxioms.lean confirms 1 zero-axiom
theorem (none: #18), 2[propext] theorems (P: #1, #9),
and 15[propext, Quot.sound]theorems (P,Q; Table 1).
Proposition 1(Constructive Lean 4 Kernel Scope).
All 18 sub-lemmas in Table 1 compile construc-
tively under Lean 4.35.0 without external libraries or
Classical.choice. Notably, Theorem 1 proves modular
non-membership soundness for all exponentsx∈N , Theo-
rem 8 proves theq0 ≥3degree gap universally by induction
on N≥ 2, Theorem 11 proves the Waterhouse interval
coprimality dichotomy forN1 = ⌊(q+ 1)/n⌋n,N2 = N1 −n
whenever p|q , Theorem 14 proves the exact geometric sum
and2 WjTloc bound for the recurrenceTj+1 = Tloc + WTj
by induction onj, Theorem 15 provesdet = 1for every
SL2(Z)elimination step, and Theorem 16 proves unfactored-
modulus non-membership divisibility wheneverdg,Eg ≥1.
3 Exact Zero-Float Certificate Au-
ditor
The modulesdlp_exact.py and dlp_certifier.py (un-
der src/) use exclusively Pythonint (statically audited
for zerofloat(, math., numpy, ornp.). Raw JSON inges-
tion rejects IEEE-754 decimals, NaN/Infinity, and du-
plicate keys via parse_float , parse_constant , and
object_pairs_hook , followed by a strict AST whitelist
(depth ≤ 20, int bits ≤ 4096, str len ≤ 2000), canoni-
cal decimal integer string parsing, and canonical trimmed
polynomial checks.
Definition 1(DLP-COGENTIC-CERT-1.0 Acceptance Pred-
icates).A certificate with schema="DLP-COGENTIC-CER
Figure 1:(a)Exact group orders log10 |AGLN(Fq0 )|vs.
log10 |SqN
0
|(q0 ∈{3,4}, N = 2 ... 6).(b)Monodromy com-
pression ratiolog|SqN
0
|/log|AGL N(Fq0 )|for q0 ∈{3,4,5}
(up to2 ,009.2×; full table inexp2 reaches34 ,507.6×at
q0 = 8,N= 6).
T-1.0" is accepted iff every claimed value matches exact
recomputation and its mode predicate holds:
• Mode 1 (dlp_zero_error_certificate ):Verifies
primality ofp∈ [2,1009], exact Rabin irreducibility of
monicdegree-nf∈F p[X], nonzerog,h∈F ×
pn, andeither
LOG (0 ≤x≤p n−2with gx ≡h (modf ), plus optional
Section 6.2 CRT splitS·L = pn −1, σSS + σLL =
1, gxS
S = hS, gxL
L = hL, and exact recombinedx) or
NOT_IN_SUBGROUP (1 ≤E≤p n −1, gE ≡1, hE ̸≡1
(modf)).
• Mode 2 (ordinary_elliptic_lang_presentation ):
Verifies canonical ordinary modelE/Fq (q≤ 64) [7] for
p = 2( a1 = 1 ,a4 = 0 ,a6 ̸= 0), p = 3( a1 = a4 =
0,a2,a6 ̸= 0), or p≥ 5( a1 = a2 = 0,4a3
4 + 27a2
6 ̸= 0);
checks exact exhaustive point countNE = |E(Fq)|, Hasse
bound( q + 1 −NE)2 ≤ 4q, ordinarity p∤ (q + 1 −
NE), exact order ord(Q) = n, Rabin irreducibility of
monic degree-n Mx ∈F q[Y], I0 ∈E (Fqn), exact Eq.(1)
ϕq(I0) = I0 + Q, and xP(I0)q = ˜xP(I0)for witness
P∈E(F q).
• Mode 3 (sparse_moore_linearized_pencil ):Over
Fq0 ⊆F q (q0 = ps ≥3,q≤ 729), checksdetMq0 (z) ̸= 0
via BOTH Gaussian elimination and Lemma 3.1(1)’s
exact product formula, checks detMaff
q0 (z) ̸= 0, veri-
fies all four Lemma 3.3 pencil hypotheses (A1)–(A4)
(∆1,∆2 ̸= 0, gcd(A0,A1) = gcd(L0,L1) = 1), checks
exact |AGLN(Fq0 )|, and verifies complete splitting of
Lz0 (T)intoq N
0 distinct roots inFq.
• Mode 4 ( unimodular_composite_dlp_solve
r):Given unfactored composite ML | (pn −1),
nontrivial γ∈G L \{1} (γML = 1; full order
ord(γ) = ML is intentionally unverified without fac-
toring ML, while LOG/NOT_IN_SUBGROUP soundness
holds unconditionally), δ1,...,δ K ∈G L, and rela-
tion rows ∏
jδEr,j
j = γar in F×
pn, executes exact
deterministic SL2(Z) SolveModM(ML,E,a )(never fac-
toring ML), verifies δj = γyj, audits Lemma 6.4
LOG or NOT_IN_SUBGROUP deduction from( e(g),e(h)),
and verifies exact Theorem 1.2(2) parameter tuples
(ℓ2,ℓ3,ℓp,s,B,m)withℓ 3 ≥10,B≥4and8msℓ p <ℓ2.
2

--- Page 3 ---
Table 1: Complete inventory of all 18 constructive Lean 4.35.0 theorems inlean/CogenticDiscreteLog.lean (zero
sorry, zeroaxiom, zeroClassical.choice, zero warnings;none for #18,[propext] (P) for #1, #9, and[propext,
Quot.sound](P,Q) for the remaining 15).
# Theorem Identifier Ref. [4] Exact Machine-Checked Statement & Hypotheses Ax.
1def11_not_in_subgroup_soundnessDef. 1.1g E ≡1 (modM)∧h E ̸≡1 (modM) =⇒ ∀x∈N, g x ̸≡h(modM).P
2lem31_moore_det_2x2_identityLem. 3.1z 2=cz1, qz2 =qcqz1 , qc=c=⇒z 1qz2 −z2qz1 = 0(2×2scalar step).P,Q
3lem31_affine_moore_reductionLem. 3.1∀z i,ui ∈Z,3×3affine Moore det equals(z 2−z1)(u3−u1)−(z 3−z1)(u2−u1).P,Q
4lem32_transvection_det_one_2x2Lem. 3.2ϕ 1u1+ϕ2u2=0 =⇒det(I+uϕ ⊤) = 1andT ϕ,u(Tϕ,−u(v)) =v.P,Q
5lem32_transvection_conjugation_sumLem. 3.2ϕ 2(w) =−1 =⇒ϕ 2(v−ϕ 1(v)w) =ϕ 2(v) +ϕ1(v)(dual subspace closure).P,Q
6lem33_mobius_det_invarianceLem. 3.3 Adjugateadj(Γ)Γ = ∆ 1I2 (∆1 =a0Na10 −a1Na00) and slope shift identity.P,Q
7lem33_cocycle_coboundary_vanishLem. 3.3c z +ζcg =cg +gcz =⇒(ζ−1)c g =gcz −cz (coboundary step).P,Q
8lem33_degree_gap_q0_ge_3Lem. 3.3∀q 0 ≥3, N≥2, d≥1, q N
0 −qN−1
0 ≥6∧1 +dq N−1
0 <dqN
0 .P,Q
9lem34_jordan_transposition_conjLem. 3.4 Pairwise distincta,b,c∈N=⇒ ∀x∈N,(ab)◦(bc)◦(ab)(x) = (ac)(x).P
10lem42_parallelogram_cauchy_schwarzLem. 4.2d 1 ≥1∧(−β 0)2d1 + (−β0)(2d1)β0 + (2d1)2d2 ≥0 =⇒β 2
0 ≤4d1d2.P,Q
11lem41_waterhouse_interval_coprimeLem. 4.1p≥ 2, n≥ 5, q≥ 16n2, p|q , N1=⌊q+1
n ⌋n, N2=N1−n =⇒
Ni≤q+1, q+1−N1<n, q+1−N2<2n,∃i, p∤(q+1−N i).
P,Q
12lem51_linear_disjointness_pinchLem. 5.1G≥1, d geom=G, darith=k1dgeom ∈[dgeom,G] =⇒k 1 = 1∧d arith =G.P,Q
13lem51_castelnuovo_induction_stepLem. 5.1i≥1, g i−1 ≤(i−1)di−1, di=n1di−1, n1n2 ≤di =⇒n 1gi−1 +n1n2 ≤idi.P,Q
14lem62_recursion_tree_boundLem. 6.2W≥ 2, T0=Tloc, Tj+1=Tloc+WTj =⇒ (W−1)Tj+Tloc=Wj+1Tloc ∧
Tj≤2WjTloc.
P,Q
15lem63_unimodular_step_det_oneLem. 6.3d≥1, u=du ′, v=dv′, su+tv=d=⇒su ′+tv′=1∧(−v ′)u+u′v=0.P,Q
16lem64_nonmembership_exponent_soundLem. 6.4d g≥1, Eg≥1, Yg=dgqg, ML=dgEg, dg ∤Yh =⇒M L |YgEg ∧ML ∤YhEg.P,Q
17sec62_crt_recombination_soundSec. 6.2σ SS+σLL=1, x=xSσLL+xLσSS=⇒SL|L(x−x S)∧SL|S(x−x L).P,Q
18thm12_parameter_asymptotic_guardsThm. 1.2 Ground guards:3·8<32,204 + 163<600,489<600,2 10 = 1024,8 12 >8.none
Figure 2:(a)Exact Theorem 1.2(2) degree-reduction fac-
tor B(ℓ2)across ℓ2 ≥ 1024, with first B≥ 4activa-
tion at non-dyadic ℓ2 = 25 ,088( p∈{ 2,3}) and25 ,344
(p∈{ 5,7}).(b)Factoring-free SL2(Z) SolveModM scaling
(0.024–1.390 ms) forK = 2 ... 12( R= 2K) modulo 38-bit
compositeM= 137,725,284,593.
4 Exact Findings, Atlas, and Red-
Team Audit
All experiments ran locally on Windows 11 (Python 3.12.6,
Lean 4.35.0; 7-run means after warm-up).
1. Live Lang Presentations Across All Characteris-
tics & Monodromy Collapse (Fig. 1).Mode 2 imple-
ments Cogentic Lemma 4.1(2) directly viaΨQ(X,Xq)and
Cantor–Zassenhaus to construct and certify exact Lang-
isogeny presentationsϕq(I0) = I0 +Qand xP(I0)q = ˜xP(I0)
across four prime characteristics spanning all three canon-
ical ordinary Weierstrass regimes (p = 2, p = 3, p≥ 5):
p = 2( q = 16 ,NE = 20 ,t = −3), p = 3( q = 9 ,NE =
15,t = −5), p = 5( q = 25,NE = 35,t = −9), andp = 7
(q = 7 ,NE = 5 ,t = 3), all with exact order-5point Q.
Figure 1 quantifies why sparseFq0 -affine pencils shatter
the Sq monodromy barrier: at q0 = 4 ,N = 3(degree
64), |AGL3(F4)|= 11,612,160( log10 = 7.0649) vs.|S64|≈
1089.1034 (12.61×exponent collapse); byq0 = 8,N = 6(de-
Figure 3:(a)Mean exact zero-float verification latency
across all 16 canonical certificates (1.133–36.640 ms, log
scale).(b)Live adversarial red-team audit rejecting 61/61
forgeries across five attack classes with exact error-branch
assertions.
gree262 ,144), the exponent compression reaches34,507.6×!
2. Exact Theorem 1.2(2) Onset Discovery &
Factoring-Free Unimodular Scaling (Fig. 2).Let
ℓp := ⌈log2 p⌉denote the prime bit-length (ℓp ∈{1,2,3,3}
for p∈ {2,3,5,7}) and ℓ3 := ⌊log2 ℓ2⌋. Sweeping The-
orem 1.2(2)’s exact integer formulass = max(3,⌈ℓ2
3/ℓp⌉)
and B = ⌊ℓ2/(32sℓp)⌋reveals that whileℓ3 ≥10begins
at ℓ2 = 1024, at dyadic pointsℓ2 = 2ℓ3 we obtainB = 0
for ℓ3 ∈ {10,11,12}, B = 1at ℓ3 = 13( ℓ2 = 8 ,192),
and B = 2at ℓ3 = 14( ℓ2 = 16,384); theexact first ac-
tivationof B≥ 4occurs at non-dyadic ℓ2 = 25 ,088for
p∈{ 2,3}(ℓ3 = 14,s∈{ 196,98},B = 4,m = 12, cofactor
ratio8 msℓp/ℓ2 = 0 .75) and ℓ2 = 25 ,344for p∈ {5,7}
(ℓp = 3 ,s = ⌈196/3⌉= 66, shifted by+256via ceiling
rounding). Meanwhile, deterministic SL2(Z) SolveModM
solves R= 2K overdetermined systems modulo 38-bit un-
factored M = 137,725,284,593(17 ·257 ·65537 ·13 ·37) in
0.024–1.390 msforK= 2...12with zero factorization.
3. 16-Certificate Atlas & 65-Test Red-Team Audit
(Table 2, Fig. 3).Table 2 lists all 16 canonical certifi-
3

--- Page 4 ---
Table 2: Canonical 16-certificateDLP-COGENTIC-CERT-1.0
atlas (results/exp1_certificate_atlas.json ; all 16
verified).
Certificate ID M Exact Certified Witness Summary ms
m1_dlp_f2_16_log_crtM1F ×
216:LOGx=41927, CRT15·43691.815
m1_dlp_f3_12_log_crtM1F ×
312:LOGx=314159, CRT80·66432.022
m1_dlp_f2_20_not_in_subgroupM1F×
220:NOT_IN_SUBGROUPE=2097151.231
m1_dlp_f5_10_not_in_subgroupM1F×
510:NOT_IN_SUBGROUPE=8877841.133
m2_lang_p2_f16_order5M2p=2,q=16:N E=20,t=−3, Eq. (1) ok 10.417
m2_lang_p3_f9_order5M2p=3,q=9:N E=15,t=−5, Eq. (1) ok 5.946
m2_lang_p5_f25_order5M2p=5,q=25:N E=35,t=−9, Eq. (1) ok 10.330
m2_lang_p7_f7_order5M2p=7,q=7:N E=5,t=3, Eq. (1) ok 4.253
m3_pencil_p2_q0_4_N2M3q 0=4,q=64,N=2:|AGL|=2880, 16 rts 5.111
m3_pencil_p2_q0_4_N3M3q 0=4,q=256,N=3:|AGL|=1.16·107, 64 rts 33.177
m3_pencil_p3_q0_3_N2M3q 0=3,q=81,N=2:|AGL|=432, 9 rts 4.730
m3_pencil_p5_q0_5_N2M3q 0=5,q=125,N=2:|AGL|=12000, 25 rts 7.430
m4_unimodular_f2_16_composite_logM4ML=4369:LOG,K=4,R=8,B=419.666
m4_unimodular_f3_12_composite_nonmemM4ML=6643:NONMEM,K=4,R=8,B=517.052
m4_unimodular_f2_20_composite_logM4ML=13981:LOG,K=5,R=10,B=736.640
m4_unimodular_f5_10_composite_nonmemM4ML=406901:NONMEM,K=5,R=10,B=1431.176
cates verified in1.133–36.640 ms. tests/test_suite.py
executes 65 pytest functions: 1 aggregate replay of all 16
certificates, 3 raw-JSON parser checks (IEEE-754 float,NaN,
duplicate keys), and 61 parametrized live adversarial forgery
tests (12 schema/parser + 12 each for Modes 1–3 + 13 for
Mode 4, including supersingular curve forgery, Lang-sign
negation ϕq(−I0) ̸= −I0 +Q, all four Lemma 3.3 (A1)–(A4)
breaks, trivialγ = 1base forgery, rank-deficient composite
relation matrices, andℓ2 = 25,087sub-threshold B = 3),
each asserting an exact regex match on the expected rejec-
tion branch. scripts/verify_all.py enforces all 5 gates
including strict axiom whitelisting and a 41-file SHA-256
manifest.
5 Conclusion
We delivered an independent, explicitly scoped, zero-
floating-point verification companion for the discrete
algebraic and unimodular mechanisms of the Cogen-
tic Discrete Logarithm preprint [4, 2], pairing 18 con-
structive Lean 4.35.0 sub-lemmas (zero sorry, zero
Classical.choice) with the pure-int auditor DLP-COG
ENTIC-CERT-1.0 , 16 canonical exact witnesses spanning
p∈{ 2,3,5,7}, exact Theorem 1.2(2) onset characterization
(ℓ2 = 25,088), and 61/61 live adversarial forgery rejections.
References
[1] Razvan Barbulescu, Pierrick Gaudry, Antoine Joux, and Em-
manuel Thomé. A heuristic quasi-polynomial algorithm for dis-
crete logarithm in finite fields of small characteristic. InAdvances
in Cryptology – EUROCRYPT 2014, volume 8441 ofLNCS, pages
1–16. Springer, 2014.
[2] Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw,
Aranyak Mehta, Grigoris Velegkas, and Di Wang. Cogentic: Multi-
agent orchestration for automated proof discovery. arXiv preprint
arXiv:2609.40324, 2026.
[3] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem
prover and programming language. InAutomated Deduction –
CADE 28, volume 12699 ofLNCS, pages 625–635. Springer, 2021.
[4] Google Research Cogentic. Discrete logarithms in finite fields of
fixed characteristic in sub-quasi-polynomial time. Google Research
Cogentic Preprint,https://github.com/google-research/goog
le-research/tree/master/cogentic_research_papers/discret
e_logarithm, November 2026.
[5] Thorsten Kleinjung and Benjamin Wesolowski. Discrete loga-
rithms in quasi-polynomial time in finite fields of fixed characteris-
tic.Journal of the American Mathematical Society, 35(2):581–624,
2022.
[6] Guido Lido. A provably quasi-polynomial algorithm for the dis-
crete logarithm problem in finite fields of small characteristic.
Finite Fields and Their Applications, 111:102753, 2026.
[7] Joseph H. Silverman.The Arithmetic of Elliptic Curves, volume
106 ofGraduate Texts in Mathematics. Springer, 2nd edition,
2009.
4
