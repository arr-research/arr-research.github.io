# Constructive Lean 4 Formalization and Exact-Rational Certificates for OpenAI's omega <= 9/4 Strassen Spectral Profile Proof

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5JHSRFTNKG8Z49RC` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/openai-strassen-nine-fourths-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `9c6960153b643975b9ee0b49aa6c0fc9b8d98bff74f0f624aaf4ed0f7ab47312`

## Abstract

OpenAI (Oct. 2, 2026) established the upper bound omega <= 9/4 for the complex matrix multiplication exponent via a compact spectral-profile mechanism: finite 5M -> M Fourier squared-mismatch degeneration (Prop. 3.1), a determinant filtration establishing discrete concavity 2P(a,b) >= P(a,b+1) + P(a,b-1) (Lem. 4.1), a three-sector decomposition giving shifted tripling P(a, 3h+a-1) >= 3P(a,h) (Lem. 4.2), and an elementary discrete growth proof forcing P(a,a) >= a^(4/3) (Lem. 5.1) and thus t <= 3/4 => omega = 3t <= 9/4. We present a standalone, zero-dependency, zero-floating-point verification stack pairing: (i) StrassenNineFourths.lean, 18 constructive Lean 4.35.0 theorems (zero sorry, zero axiom, zero Classical.choice, zero warnings; 1 zero-axiom and 17 [propext, Quot.sound]) mechanizing Proposition 3.1, Lemmas 4.1-4.2, and the complete universal inductive proof of Lemma 5.1 (P(a,a)^3 >= a^4 for all a >= 1) over a self-contained exact-rational structure QRat; and (ii) STRASSEN-94-CERT-1.0, a pure-stdlib Python Fraction auditor across four modes. Alongside certifying 16 canonical witnesses in 0.008-13.686 ms and rejecting 60/60 live adversarial forgeries (64/64 pytest checks), our exact audit reveals a 4x tightening of Proposition 3.1's degeneration degree from (M-1)^2 to floor((M-1)/2)^2 (degree 0 at M=2) and proves exact minimal integer refutation thresholds a*(t) for supercritical exponents t > 3/4.

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Formalization and Exact-Rational
Certificates for OpenAI’sω≤9/4Strassen Spectral Profile
Proof
Lluis Eriksson∗
November 25, 2026
Abstract
OpenAI (Oct. 2, 2026) established the upper bound
ω≤ 9/4for the complex matrix multiplication exponent
via a compact spectral-profile mechanism: finite5 M→
M Fourier squared-mismatch degeneration (Prop. 3.1),
a determinant filtration establishing discrete concavity
2P(a,b) ≥P (a,b + 1) +P(a,b− 1)(Lem. 4.1), a three-
sector decomposition giving shifted triplingP(a,3h+ a−
1) ≥ 3P(a,h)(Lem. 4.2), and an elementary discrete
growth proof forcingP(a,a) ≥a 4/3 (Lem. 5.1) and thus
t≤ 3/4 = ⇒ω = 3t≤ 9/4. We present a stan-
dalone, zero-dependency, zero-floating-point verification
stack pairing: (i) StrassenNineFourths.lean, 18 con-
structive Lean 4.35.0 theorems (zerosorry, zero axiom,
zero Classical.choice, zero warnings; 1 zero-axiom
and 17 [propext, Quot.sound]) mechanizing Proposi-
tion 3.1, Lemmas 4.1–4.2, and thecomplete universal
inductive proofof Lemma 5.1 ( P(a,a)3 ≥a 4 for all
a≥ 1) over a self-contained exact-rational structureQRat;
and (ii) STRASSEN-94-CERT-1.0, a pure-stdlib Python
Fraction auditor across four modes. Alongside certify-
ing 16 canonical witnesses in0.008–13.686 ms and rejecting
60/60 live adversarial forgeries (64/64 pytest checks), our
exact audit reveals a4 ×tightening of Proposition 3.1’s
degeneration degree from(M−1)2 to ⌊(M−1)/2⌋2 (degree
0at M = 2) and proves exact minimal integer refutation
thresholdsa ∗(t)for supercritical exponentst>3/4.
1 Introduction and Scope Calibra-
tion
Following Strassen’s2 ×2seven-product identity [ 5],
Strassen’s asymptotic spectrum of tensors [6], and the
Coppersmith–Winograd laser method [1], OpenAI’s Oc-
tober 2, 2026 preprint [4] proved ω≤ 9/4over C (com-
plemented by a matching lower boundωF = 9/4in [ 3])
without Coppersmith–Winograd optimization tables. For
any tensor characterλwith oriented dot-product exponents
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with
transparent AI coding, formalization, and drafting assistance via
Google Antigravity; all Lean 4 theorems, exact-Q verifiers, and adver-
sarial tests were independently compiled and verified locally. Repos-
itory: github.com/lluiseriksson/openai-strassen-nine-fourths
-certificates.
pX,pY,pZ ∈[0,1]and t:= (pX + pY + pZ)/3 >0, OpenAI
defines the symmetrized polynomial-multiplication profile
P(a,b) :=
( ∏
π∈S3
λπ(C(a,b))
)1/(6t)
,(1)
where C(a,b) = ∑a−1
i=0
∑b−1
j=0 xiyjzi+j has exact rank
R(C(a,b)) = a + b− 1. Symmetry, P(1,b) = b, in-
terpolation P(a,b) ≤ (a+ b− 1)1/t, discrete concavity
2P(a,b) ≥P (a,b + 1) +P(a,b− 1)(Lem. 4.1), and shifted
tripling P(a,3h + a− 1) ≥ 3P(a,h)(Lem. 4.2) force
P(a,a) ≥a4/3 for alla≥ 1(Lem. 5.1), which yieldst≤ 3/4
andω= 3t≤9/4.
Honest Two-Layer Verification Scope.We delineate
explicitly what is machine-checked in Lean 4 vs. verified on
finite witnesses vs. left in [4]:
1. Layer 1 (Lean 4.35.0 Kernel, Universal Algebraic
& Inductive Proofs): StrassenNineFourths.lean
proves 18 zero-dependency theorems (Table 1), includ-
ing thefull universal inductive proofof Lemma 5.1 over
an abstractSpectralProfile structure returning exact
positive rationals QRat: from symmetry, P(1,b) = b,
concavity, and shifted tripling, Theorems 10–17 con-
structively deriveH3
a ≥a and P(a,a)3 ≥a 4 forevery
a≥1.
2. Layer 2 (Exact- Q/Z Certificate Auditor):
STRASSEN-94-CERT-1.0 replays finite instances of
Prop. 3.1 (M4 phase-weight audits), Lem. 4.1 (ex-
act rational change-of-basis matrix factorizations of
C(a,b) ⊗BX(2)), Lem. 4.2 (exhaustive monomial sector
audits), and Lem. 5.1 (rational profiles plus exact finite
contradictionsa4p >(2a−1) 3q).
3. Explicit Non-Claims:We donotformalize Strassen’s
detecting-character existence theorem (Lem. 2.2 /
Schauder–Tychonoff fixed-point argument), Stirling’s
asymptotic entropy limit (Cor. 3.2), real-valued frac-
tional powers x1/(6t), or Bini’s interpolation limit in-
side Lean 4; those asymptotic/topological pillars remain
in [4].
2 Constructive Lean 4.35.0 Kernel
lean/StrassenNineFourths.lean compiles standalone in
3.3 sunder Lean 4.35.0 [2] with zero external imports,
1

--- Page 2 ---
zero warnings, zero sorry, and zero Classical.choice.
Rather than importing Mathlib’s Rat, we build a mini-
mal 95-line exact rational typeQRat (num : Int , den :
Int, hden : 0 < den ) with exact order transitivity, ad-
ditive/multiplicative monotonicity, and cubic monotonicity,
and prove all 18 theorems of Table 1.
Proposition 1(Universal Mechanization of Lemma 5.1
and Finite Degenerations).All 18 theorems in Table 1
compile constructively under Lean 4.35.0 without external
librariesor Classical.choice. Inparticular, Theorems10–
17formalizetheentirediscreteproofofLemma5.1of[ 4]over
exact rationals: for any positive symmetric profileP : N2 →
Q>0 with P(1,b) =b,2 P(a,b) ≥P (a,b + 1) +P(a,b− 1),
and P(a,3h+ a−1) ≥3P(a,h), we obtainP(a,a)3 ≥a4
for everya≥1.
3 Exact-QCertificate Auditor
The modules strassen_exact.py and
strassen_certifier.py (under src/) use exclusively
Python int and fractions.Fraction (statically audited
for zero float(, math., numpy, or np.). Raw JSON
ingestion rejects IEEE-754 decimals,NaN/Infinity, and
duplicate object keys viaparse_float, parse_constant,
and object_pairs_hook, followed by a strict AST type
whitelist, nesting-depth cap (20), and canonical ASCII-digit
lowest-terms rational parsing (len≤2000).
Definition 1(STRASSEN-94-CERT-1.0 Acceptance Predi-
cates).A witness with schema="STRASSEN-94-CERT-1.0"
is accepted iff every claimed integer/rational summary
matches exact recomputation and its mode predicate holds:
• Mode 1 (prop31_fourier_separation_cert):Given
1 ≤M≤ 12, exhaustively checks all M4 tuples
(g,h,u,v ) ∈[M]4 at L= 5M: verifies|u−v+2(g−h)|≤
3(M−1) <L, exact squared-mismatch weightg2 +(hu−
h2)−hv = (g−h)2 ≥0on every e≡ 0 (modL )survivor,
weight-0survival count= M2 precisely ong= h∧u = v,
and tight actual degree⌊(M−1)/2⌋2 ≤(M−1) 2.
• Mode 2 (lemma41_determinant_filtration_cert):
Given1 ≤a≤ 10,2 ≤b≤ 10, constructs the exact
Q change-of-basis matricesBb−1,Ba+b−2 for OpenAI’s
Lemma 4.1 quotient-lift and kernel basis (ue−ivis, vew,
Due−1−jvj), inverts Ba+b−2 via exact Gauss–Jordan
elimination, and verifies for every slicefr = ua−1−rvr ∈
Va−1 that Mfr = B−1
a+b−2SrBb−1 has an identically zero
upper-right block, upper-left block identicallyC(a,b+1),
and lower-right block identicallyC(a,b−1).
• Mode 3 ( lemma42_three_sector_tripling_cert):
Given1 ≤a,h≤ 25, exhaustively checks alla(3h+a−1)
monomials( x,y,x + y)of C(a,3h+ a−1): verifies zero
negative-weight terms, exact partition of weight-0terms
into three disjoint sectors of sizeah, exact weight-+1
drop counta(a−1), and exact bijection of the reversed
middle branch(u,r) ↦→(a−1−u,h +u+r,h+a−1+ r).
• Mode 4 (lemma51_spectral_profile_cert):Given a
positive rational tableP[1..amax][1..bmax](2 ≤a max ≤
Figure 1:(a)Exact Lemma 5.1 diagonal lower envelope
Dlb(a) =3a−1
2
∏a−1
m=1(1 + 1
3m)bounded strictly above a4/3
and below thet= 3/4interpolation ceiling(2 a−1)4/3 for
a≥ 2.(b)Exact minimal integer contradiction witnesses
a∗(t)where a4p >(2a−1)3q refutes supercriticalω= 3t>
9/4(a ∗= 7atω= 3up to32,761atω= 12/5).
Figure 2:(a)Sharp4 ×tightening of Proposition 3.1’s
survivingdegenerationdegreefrom( M−1)2 to⌊(M−1)/2⌋2
across M∈ [1,9].(b)Lemma 4.2 diagonal three-sector
weight-0survival fraction 3a
4a−1 converging monotonically
to3/4.
12, bmax ≥4amax −1), verifies P(1,b) = b, symmetry,
discrete concavity, shifted tripling, Eq. (5.2) recurrence
Ha/Ha−1 ≥ (3a− 2)/(3a− 3), H3
a ≥a , P(a,a)3 ≥
a4, and exact finite refutationa4p > (2a− 1)3q for a
supercritical rationaltrefute =p/q >3/4.
4 Exact Findings, Atlas, and Red-
Team Audit
All experiments ran locally on Windows 11 (Python 3.12.6,
Lean 4.35.0; 7-run means after warm-up).
1. Sharp4 ×Tightening of Proposition 3.1 Degree
(Fig. 2(a)).OpenAI [ 4] (p. 5) bounds the degree of the
transformed tensor in Proposition 3.1 by(M− 1)2. Ex-
haustive exact auditing acrossM = 1,..., 9reveals that
because surviving terms satisfy2( g−h ) = v−u with
u,v∈{ 1,...,M} , we necessarily have|g−h|≤⌊ (M−1)/2⌋,
tightening the maximum surviving weight by a factor of4
to ⌊(M− 1)/2⌋2: at M = 2the actual maximum weight
is0(zero-degree exact restriction!), and at M = 8it is9
versus49.
2. Exact Matrix Factorization, Sector Survival,
& Finite Contradiction Witnesses (Figs. 1–3).In
2

--- Page 3 ---
Table 1: Complete inventory of all 18 constructive Lean 4.35.0 theorems inlean/StrassenNineFourths.lean (zero
sorry, zeroaxiom, zeroClassical.choice, zero warnings; Theorem 5 is zero-axiom and the remaining 17 audit strictly
to[propext, Quot.sound]vialake env lean -j 1 AuditAxioms.lean).
# Theorem Identifier Ref. [4] Exact Machine-Checked Statement (UniversalZ/QRat/ Inductive Proofs)
1prop31_fourier_modulus_no_wrapProp. 3.11≤g,h,u,v≤M=⇒ |u−v+2(g−h)|≤3(M−1)<5M(no wrap modL= 5M).
2prop31_squared_mismatch_weightProp. 3.1u−v+ 2(g−h) = 0 =⇒g 2+(hu−h2)+(−hv) = (g−h)2 ≥0and( g−h)2 = 0 ⇐⇒g =
h∧u=v.
3prop31_degeneration_degree_boundProp. 3.11≤g,h,u,v≤M, u−v+2(g−h) = 0 =⇒4(g−h) 2 ≤(M−1) 2 (4×tightening).
4lemma41_determinant_exact_seq_dimEq. (4.7)1≤e=⇒2(e+1) = (e+2) +e(dim(V e⊗W1) = dimVe+1 + dimDVe−1).
5lemma41_block_triangular_weightsEq. (4.8)0+0+0 = 0∧0+(−1)+1 = 0∧0+0+1 = 1(zero-axiom diagonal/cross weights).
6lemma41_c22_filtration_identityLem. 4.1∀u,v,s,w∈Z, u(vw) =v 2s+v(uw−vs)(C(2,2)quotient/kernel split).
7lemma42_three_sector_weights_nonnegLem. 4.2∀a,h≥ 1, 0 ≤x<a, 0 ≤y <3h+a−1: wY(y)+wZ(x+y) ≥0and= 0 ⇐⇒matched
sector.
8lemma42_middle_branch_reversalLem. 4.2 0 ≤u < a, 0 ≤r < h =⇒x = a−1−u, y= h+u+r lies in middle sector with
x+y=h+a−1+r.
9sec4_six_perm_exponent_sumEq. (4.3)∀p X,pY,pZ ∈Z, pX+pX+pY+pY+pZ+pZ = 2(pX+pY+pZ)(
∑
π∈S3
p(π)
X = 6t).
10lemma51_increments_step_antitoneLem. 5.1∀sp:SpectralProfile, a≥1, b≥2 =⇒∆ a,b ≤∆ a,b−1 inQRat.
11lemma51_increments_antitoneLem. 5.1 Universal induction onk∈N:∀a,h≥1,∆ a,h+k ≤∆ a,h.
12lemma51_secant_upper_boundLem. 5.1 Universal induction onm∈N:P(a,h+m)−P(a,h)≤m·∆ a,h.
13lemma51_tripling_slope_boundLem. 5.1∀a≥1, H a := 2P(a,a)/(3a−1)≤∆ a,a (from shifted tripling ath=a).
14lemma51_H_step_recurrenceEqs. (5.1–2)∀a≥2, 3a−2
3a−3 Ha−1 ≤Ha (fromD a−Da−1 ≥Ha−1+Ha and symmetry).
15lemma51_cubic_step_inequalityLem. 5.1∀m≥1,(3m) 3(m+1)≤(3m+1) 3m(exact cleared(1+ 1
3m)3 ≥1+ 1
m).
16lemma51_H_cube_ge_aLem. 5.1 Universal induction ona≥1:a≤H 3
a inQRat(baseH 1 = 1).
17lemma51_main_diagonal_growth_a4_3Lem. 5.1 Full universal Lemma 5.1:∀sp,∀a≥1, a 4 ≤P(a,a) 3 (P(a,a)≥a 4/3).
18thm11_omega_nine_fourths_barrierThm. 1.1 4tn ≤3td ⇒4(3tn) ≤9td,2 < 9
4 < 2.371177 < 5
2 <log 2 7 < 3(2 5 < 72, 7 < 23),
133 <7 4.
Figure 3:(a)Mean exact- Q verification latency across
all 16 canonical certificates (0.008–13.686 ms).(b)Exact
rational overshoot ratiosHlb(a)3/a≥ 1and Dlb(a)3/a4 ≥1
acrossa∈{1,...,20}.
Mode 2, exactQ matrix conjugation confirms zero upper-
right entries across every slicefr ∈Va−1 of C(a,b)⊗BX(2),
with exact diagonal nonzerosa(b+1)and a(b−1)and cross-
block nonzeros equal toa−1(e.g.1for C(2,2)matching
u(vw) =v2s+ vD, and5for C(6,6)). In Mode 3,C(2,4)
yieldsexactly3 ×2 = 6weight-0termsand2droppedweight-
+1terms (matching Fig. 1 of [4]), and diagonal survival
efficiency 3a
4a−1 approaches3/4(Fig. 2(b)). In Mode 4, we
construct explicit rational spectral profiles—including the
zero-slack tight profileP1/3(a,b) =a+b−1+ 1
3 (a−1)(b−1)
(whereP(2,3h+1) = 3P(2,h)holdswithzeroslackforevery
h) and strictly concave rational familiesa+ b−1 +α(a−
1)(b−1) +β(a−1)(b−1)
a+b+c (β >0, c≥ 0,3 α−1 ≥2β)—and
compute exact minimal finite contradiction thresholdsa∗(t)
ruling out ω = 3at a∗ = 7(7 4 = 2401 > 2197 = 133,
also certified in Lean Theorem 18 alongside the chain2<
9
4 < 2.371177 < 5
2 <log 2 7 < 3comparing 9
4 to the prior
best bound2 .371177cited in [4, Sec. 1]), ω = 27/10at
a∗= 30,ω = 5/2at a∗= 508,ω = 27/11at a∗= 2,043,
andω= 12/5ata ∗= 32,761(Fig. 1(b)).
Table 2: Canonical 16-certificateSTRASSEN-94-CERT-1.0
atlas (results/exp1_certificate_atlas.json; all 16
verified).
Certificate ID M Exact Certified Witness Summary ms
prop31_fourier_M2_baseM1M=2,L=10,4surv.,4w0, deg0≤10.011
prop31_fourier_M4_quarticM1M=4,L=20,28surv.,16w0, deg1≤90.045
prop31_fourier_M6_hexM1M=6,L=30,92surv.,36w0, deg4≤250.210
prop31_fourier_M8_octalM1M=8,L=40,216surv.,64w0, deg9≤490.553
lem41_filtration_C2_2_paper_exM2C(2,2):4→6, UR0,∗= 1,+=6,−=20.358
lem41_filtration_C3_4_asymM2C(3,4):8→12, UR0,∗= 2,+=15,−=92.343
lem41_filtration_C4_5_midM2C(4,5):10→16, UR0,∗= 3,+=24,−=165.173
lem41_filtration_C6_6_squareM2C(6,6):12→22, UR0,∗= 5,+=42,−=3013.686
lem42_sectors_C2_4_fig1M3a=2,h=1,B=4:3×2w0,2drop,0neg 0.008
lem42_sectors_C3_8_tripledM3a=3,h=2,B=8:3×6w0,6drop,0neg 0.011
lem42_sectors_C5_16_midM3a=5,h=4,B=16:3×20w0,20drop 0.027
lem42_sectors_C8_31_diagM3a=8,h=8,B=31:3×64w0,56drop 0.069
lem51_profile_tight_alpha1_3M4amax=6,D6=58
3 , refutest=1(a=8) 0.686
lem51_profile_strict_concave_1_2M4amax=6,105strict conc., ref.t=5
6 (103) 0.728
lem51_profile_product_ab_amax8M4amax=8,D8=64, refutest=4
5 (5·104) 1.121
lem51_profile_concave_tight_amax7M4amax=7,150strict conc., ref.t=9
11 (2048) 0.984
3. 16-Certificate Atlas & 64-Check Red-Team Audit.
Table 2 summarizes all 16 canonical certificates verified in
0.008–13.686 ms. tests/test_suite.py executes 64 pytest
checks (all passing in0.13 s): all 16 canonical certificates, 3
raw-JSON IEEE-754/NaN/duplicate-key parser rejections,
and 60 live adversarial forgery attacks across schema/parser
bypasses (12), Mode 1 (10), Mode 2 (12), Mode 3 (10),
and Mode 4 (16).scripts/verify_all.py enforces all 5
gates including a strict axiom whitelist and 40-file SHA-256
manifest.
5 Conclusion
We delivered an independent, zero-dependency, zero-
floating-point verification stack for OpenAI’s ω≤ 9/4
Strassen spectral profile proof [4], pairing 18 construc-
tive Lean 4.35.0 theorems (including the complete uni-
versal inductive proof of Lemma 5.1,P(a,a)3 ≥a4 for all
a≥ 1, with zeroClassical.choice) with the exact-Q au-
ditor STRASSEN-94-CERT-1.0, 16 canonical witnesses, a4×
3

--- Page 4 ---
tightening of Proposition 3.1’s degeneration degree, exact
minimal finite refutation thresholdsa∗(t), and 60/60 live
adversarial forgery rejections.
References
[1] Don Coppersmith and Shmuel Winograd. Matrix mul-
tiplication via arithmetic progressions.Journal of Sym-
bolic Computation, 9(3):251–280, 1990.
[2] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, pages 625–635. Springer,
2021.
[3] OpenAI. The matrix multiplication exponent is nine
fourths. OpenAI Mathematics Preprint (github.com
/openai/math/tree/main/preprints/The-matrix-m
ultiplication-exponent-is-nine-fourths-Novem
ber-24-2026), November 2026.
[4] OpenAI. An upper bound of9/4for the matrix mul-
tiplication exponent. OpenAI Mathematics Preprint
(github.com/openai/math/tree/main/preprints/M
atrix-Multiplication-Nine-Fourths-October-2
-2026), October 2026.
[5] Volker Strassen. Gaussian elimination is not optimal.
Numerische Mathematik, 13(4):354–356, 1969.
[6] Volker Strassen. The asymptotic spectrum of ten-
sors.Journal für die reine und angewandte Mathematik,
384:102–152, 1988.
4
