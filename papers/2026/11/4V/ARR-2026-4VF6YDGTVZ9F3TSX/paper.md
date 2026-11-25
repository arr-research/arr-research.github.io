# Constructive Lean 4 Kernel and Exact Zero-Float Certificates for OpenAI's Matching Matrix Multiplication Lower Bound omega_F = 9/4

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-4VF6YDGTVZ9F3TSX` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/openai-omega-nine-fourths-lower-bound-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `85709d32321c5b9ee9e71deffbc450e4c21086c0c90fc15b0df96c1454ee536d`

## Abstract

A November 24, 2026 companion preprint from OpenAI proposes a matching lower bound showing that the matrix multiplication exponent equals omega_F = 9/4 over every field, with geometric border rank at least n^(9/4), at least ceil(n^(9/4)/2) nonscalar multiplication or division gates, dual exponent alpha_F <= 2/3, and refutation of Strassen's tight-tensor conjecture. Rather than assuming peer-reviewed validation of its CAT(0) spectral-space and tensor-network compression pillars, we deliver an independent, explicitly scoped, zero-floating-point verification companion for its discrete algebraic, symbolic dual-number bilinearization, tight-support, tagged-permutation, harmonic-star, and tripod AM-HM rigidity mechanisms. Layer 1 (OpenAIOmegaLowerBound.lean) proves 18 standalone constructive Lean 4.35.0 algebraic, combinatorial, and rational-rigidity sub-lemmas (zero sorry, zero axiom, zero Classical.choice, zero warnings; 4 zero-axiom none and 14 [propext, Quot.sound]). Layer 2 (OMEGA94-LB-CERT-1.0) is a pure-stdlib Python int/Fraction 4-mode auditor certifying 16 canonical finite witnesses in 0.027-2.466 ms and rejecting 70/70 live adversarial forgeries with exact branch assertions (76/76 pytest checks).

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Kernel and Exact Zero-Float Certificates
for OpenAI’s Matching Matrix Multiplication Lower Bound
ωF = 9/4
Lluis Eriksson∗
November 25, 2026
Abstract
A November 24, 2026 companion preprint from OpenAI [5]
proposes a matching lower bound showing that the expo-
nent of square matrix multiplication equalsωF = 9/4over
every fieldF, with geometric border rankR(Tn) ≥n9/4, at
least ⌈n9/4/2⌉nonscalar multiplication or division gates for
every n≥ 2, dual exponentαF ≤2/3, and a refutation of
Strassen’s tight-tensor conjecture. Rather than assuming
peer-reviewed endorsement of itsCAT(0)spectral-space and
tensor-network compression pillars, we deliver an indepen-
dent, explicitly scoped, zero-floating-point verification com-
panion for its discrete algebraic, symbolic dual-number bi-
linearization, tight-support, tagged-permutation, harmonic-
star, and tripod arithmetic–harmonic mean (AM–HM) rigid-
ity mechanisms. Layer 1 (OpenAIOmegaLowerBound.le
an) proves 18 standalone constructive Lean 4.35.0 alge-
braic, combinatorial, and rational-rigidity sub-lemmas (zero
sorry, zero axiom, zero Classical.choice, zero warn-
ings; 4 zero-axiomnone and 14[propext, Quot.sound]).
Layer 2 (OMEGA94-LB-CERT-1.0) is a pure-stdlib Python
int/Fraction 4-mode auditor certifying 16 canonical finite
witnesses in0 .027–2.466 ms and rejecting 70/70 live adver-
sarial forgeries with exact branch assertions (76/76 pytest
checks).
1 Introduction and Scope Calibra-
tion
Since Strassen’s seven-product algorithm [7], the matrix
multiplication exponentωF has been a central open prob-
lem in algebraic complexity. On the lower-bound side,
Bläser proved ordinary rank≥5
2 n2 −3n[2] and Landsberg–
Michałek proved border rank ≥ 2n2 −⌈log 2 n⌉− 1[ 4],
leaving the asymptotic exponent lower bound stuck at2.
Following the9/4upper bound established overC by Ope-
nAI [6] and over every fieldF by Amanov, van den Berg,
and Zuiddam [1], OpenAI’s November 24, 2026 companion
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with
transparent AI coding, formalization, and drafting assistance via
Google Antigravity; all Lean 4 theorems, exact zero-float verifiers,
and adversarial tests were independently compiled and verified locally.
Repository: github.com/lluiseriksson/openai-omega-nine-fourt
hs-lower-bound-certificates.
preprint [5] proposes the matching lower boundωF = 9/4
over every fieldF via four discrete-algebraic and geometric
pillars:
1. Finite-Size Rank, Gate, Rectangular & Tight-
Tensor Consequences (Cors. 1.2–1.3, Sec. 2.4):
R(Tn) ≥n9/4 yields ≥⌈n9/4/2⌉nonscalar gates, rectan-
gular bound R(Ta,b,c) ≥max{ab,bc,ca, (abc)3/4}, dual
exponent1 /2 ≤αF ≤2/3, refutation of Sun’s217 esti-
mate atn= 28 [9] (exact lower bound218), and refuta-
tion of Strassen’s tight-tensor conjecture [8].
2. Dual-Number Circuit Bilinearization (Lem. 2.4):
Evaluatingaformalcircuitsymbolicallyon( A0+uX,B0+
vY)over F[X,Y ][u,v]/(u2,v2)proves rankF(Ts) ≤2q,
since each multiplication or division gate introduces at
most two new products of linear forms.
3. Tagged Permutation via Two List-Distinctness
Tests (Sec. 4.1):Encoding Tag(h,h)into two Dw
tests achieves exact signed-sum factorization∏
j(1 −
1xπ−1(j) ̸=yj) =∏
j1xπ−1(j) =yj in every characteristic.
4. Five-Arm Harmonic Star & Tripod AM–HM
Rigidity (Secs. 7.4, 8.2, 11.3, Cor. 11.1):A five-
arm harmonic comparison bounds the four-site label
rate D≤ 3/2; on a tripod with arm lengthsai > 0,
D∗(a) = ∑ai −(∑a−1
i )−1 ≥ 8
9
∑ai attains equality
iff a1 = a2 = a3, giving D∗(1,1,1) = 8/3and exact
perimeter-to-label ratio6/(8/3) = 9/4.
Honest Two-Layer Verification Scope.
1. Layer 1 (Lean 4.35.0 Kernel, Standalone
Sub-Lemmas): lean/OpenAIOmegaLowerBound.lean
proves 18 standalone constructive algebraic, combina-
torial, and sum-of-squares rigidity sub-lemmas (Ta-
ble 1) extracted from Corollaries 1.2–1.3, Proposition 2.3,
Lemma 2.4, and Sections 2.4, 3.2, 4.1, 7.4, 8.2, 9.3,
and 11.3 of [5].
2. Layer 2 (Exact Zero-Float Auditor): OMEGA94-
LB-CERT-1.0 audits 16 canonical finite exact witnesses
across square/rectangular lower bounds (n≤ 4096)
and exhaustive Strassen tight supports (n≤ 10), ex-
act symbolic dual-number circuit bilinearizations over
Fp[X,Y ][u,v]/(u2,v2)(including Strassen2 ×2with di-
vision and4 ×4circuits), exact2 N signed-sum Tag(h,h)
replays (h≤ 3), and exact rational five-arm star / tripod
1

--- Page 2 ---
AM–HM rigidity.
3. Explicit Non-Claims:We donotformalize in Lean 4
the CAT(0)spectral-space embedding, Gauss lifts over
valued fields (Theorem 6.1), strong minimum principle
on tripod faces (Section 11.2), fermionic sphere tensors
(Parts I–III), trivalent tensor-power compression (Theo-
rem 2.1), or the ports/no-ports list-distinctness volume
lower bound (Theorem 2.2); those geometric and an-
alytic pillars remain unverified outside the companion
preprint [5].
2 Constructive Lean 4.35.0 Kernel
lean/OpenAIOmegaLowerBound.lean compiles standalone
in1 .9 sunderLean4.35.0[ 3]withzeroexternalimports, zero
warnings, zerosorry, and zeroClassical.choice. Audit-
ing viaAuditAxioms.lean confirms 4 zero-axiom theorems
(none: #2, #9, #10, #13)and14[propext, Quot.sound]
theorems (P,Q; Table 1).
Proposition 1(Constructive Lean 4 Kernel Scope).
All 18 sub-lemmas in Table 1 compile construc-
tively under Lean 4.35.0 without external libraries or
Classical.choice. Notably, Theorems 1–4 formalize the
cleared-denominator gate bound n9 ≤ 16q4, the exact
n= 256Sun dyadic refutation, the cyclic rectangular can-
cellation( abc)9 ≤R 12 ⇒(abc)3 ≤R 4, and αF ≤2/3;
Theorems 5–6 prove Strassen’s tight-support zero-sum and
injectivity; Theorems 14–15 prove the tripod AM–HM in-
equality and equality rigidity (a1 = a2 = a3) via the exact
sum-of-squares identity∑
cyc a1(a2 −a3)2; and Theorems 16
and 18 prove the shifted three-block recurrence and geomet-
ric compression sum by induction.
3 Exact Zero-Float Certificate Au-
ditor
The modules omega94_lb_exact.py and omega94_lb_
certifier.py (under src/) use exclusively Pythonint
and fractions.Fraction (statically audited viaast.walk
for zero float/complex literals, true division/ or /=, ormath
imports). Strict JSON parsing rejects floats,NaN/Infinity,
and duplicate keys viaparse_float, parse_constant, and
object_pairs_hook.
Definition 1(OMEGA94-LB-CERT-1.0 Predicates).A cer-
tificate with protocol="OMEGA94-LB-CERT-1.0" is ac-
cepted iff every field passes strict schema checks and its
mode predicate holds:
• Mode 1 (rank_gate_and_tight_support_cert):Au-
dits exact integer binary-search ceilings ⌈n9/4⌉ and
⌈n9/4/2⌉ (plus direct 4th-power brackets r4 ≥
n9 > (r− 1)4), Corollary 1.3 rectangular bound
max{ab,bc,ca,⌈ (abc)3/4⌉}, exhaustiven3-triple Strassen
tight-support zero-sum and factor injectivity (n<B≤
104), and strict Sun dyadic refutation (ub<⌈n 9/4
sun⌉,
2≤n sun ≤10 4).
Figure 1:(a)Exact Corollary 1.2 border-rank ( ⌈n9/4⌉)
and nonscalar gate (⌈n9/4/2⌉) lower bounds vs. Landsberg–
Michałek [4] (2n2 −⌈log 2 n⌉−1), highlighting the refuted
Sun n = 28,217 point [9].(b)Exact improvement factor
over LM18 growing asn1/4/2(2 .00×at n= 256,4.00×at
n= 4096).
Figure 2:(a)Tripod ratio Perim(1,1,b)/D∗(1,1,b)attain-
ing its unique global maximum9 /4 = 2.25at b = 1.
(b)Corollary 11.1 AM–HM rigidity defect D∗(1,1,b) −
8
9 (2 +b)vanishing iffb= 1.
• Mode 2 (dual_number_bilinearization_cert):En-
forces canonical[0 ,p−1]field entries, simulates a formal
arithmetic circuit (const, add, sub, mul, div)symbol-
icallyover Fp[X,Y ][u,v]/(u2,v2)on( A0+uX,B0+vY)
(tracking all1 + 2s2 + s4 coordinates), counts exact sym-
bolically nonscalar multiplications/divisionsq, verifies
Lemma 2.4’srank≤ 2q, and checks alls2 outputs equal
(A0B0,XB0,A0Y,XY) (modp)identically in(X,Y).
• Mode 3 ( tagged_perm_two_dw_reduction_cert):
Evaluates Section 4.1’s exact reduction of Tag(h,h)
(h∈{ 1,2,3},N = 2h) to two list-distinctness callsDw,
explicitly summing over all2N selector masks inZ and
certifying exact equality with directTag(h,h)on every
instance.
• Mode 4 ( tripod_harmonic_and_amhm_rigidity_
cert):Audits Figure 4’s exact5 ×4five-arm har-
monic slope matrix (zero column sums and exact
canonical arm rows up to scalek≥ 1), exact rational
D∗(a), perimeter2 ∑ai, ratioPerim/D∗(a)(= 9 /4iff
a1 = a2 = a3, strictly < 9/4otherwise), non-negative
AM–HM defect D∗(a) − 8
9
∑ai, and Section 8.2’s
D∗(1,1,b) =b+ 3
2 + 1
4b+2 .
2

--- Page 3 ---
Table 1: Complete inventory of all 18 constructive Lean 4.35.0 sub-lemmas inlean/OpenAIOmegaLowerBound.lean (zero
sorry, zeroaxiom, zeroClassical.choice, zero warnings;none for #2, #9, #10, #13 and[propext, Quot.sound]
(P,Q) for the remaining 14).
# Theorem Identifier Ref. [5] Exact Machine-Checked Statement & Hypotheses Ax.
1cor12_gate_lower_bound_from_rankCor. 1.2∀n,r,q∈N, r≤2q∧n 9 ≤r4 =⇒n 9 ≤16q4 (certifiesq≥⌈n 9/4/2⌉).P,Q
2cor12_sun_dyadic_refutation_256Cor. 1.2(2 8)9 = (218)4 ∧(2 17)4 <(2 8)9 (exactn= 256Sun conflict).none
3cor13_rectangular_cyclic_productCor. 1.3∀a,b,c,R∈N,(abc) 9 ≤R12 =⇒(abc) 3 ≤R4 (cube cancellation).P,Q
4cor13_dual_exponent_upper_two_thirdsCor. 1.3∀p,q∈N,3(2q+p)≤8q=⇒3p≤2q(certifiesα F ≤2/3).P,Q
5sec24_tight_support_sum_zeroSec. 2.4∀i,j,k,B∈Z,(i−Bj) + (Bj−B 2k) + (B2k−i) = 0.P,Q
6sec24_tight_support_injectiveSec. 2.4∀n,B,i 1,j1,i2,j2 ∈Z, n<B, 0 ≤i1,i2 <n, i1 −Bj1 = i2 −Bj2 =⇒i 1 =
i2 ∧j1 =j2.
P,Q
7lem24_bilinear_product_expansionLem. 2.4∀a ·,b· ∈Z, (a00b11 +a10b01)+( a01b10 +a11b00) = (a00b11 +a11b00)+( a10b01 +
a01b10).
P,Q
8lem24_bilinear_quotient_expansionLem. 2.4∀a 11,b·,f· ∈Z, b 00f11 + b11f00 + b10f01 + b01f10 = a11 =⇒b 00f11 =
a11 −b11f00 −b10f01 −b01f10.
P,Q
9sec41_tagged_perm_signed_factorSec. 4.1∀eq∈Bool,1−(ifeqthen0else1) = (ifeqthen1else0)inZ.none
10sec74_five_arm_harmonic_column_sumsSec. 7.4 Fig. 4 five-arm depth-slope column sums:1 −1−1+1+0 = 0( ×3) and
1+1+1+1−4 = 0.
none
11sec74_common_label_four_site_boundSec. 7.4∀p,q∈Z,0≤3(q−p) +p=⇒2p≤3q(D≤3/2).P,Q
12sec82_tripod_asymptotic_contact_boundSec. 8.2∀b∈N,(b+ 2)(4b+ 2)−2b= (2b+ 3)(2b+ 1) + 1(D ∗(1,1,b)).P,Q
13prop81_balanced_tripod_nine_fourthsProp. 8.13·3−1 = 8∧6·3·4 = 9·8(D ∗(1,1,1) = 8/3,6/(8/3) = 9/4).none
14sec113_am_hm_tripod_inequalitySec. 11.3∀a 1,a2,a3 ∈Z, ai ≥0 =⇒9a 1a2a3 ≤(a1+a2+a3)(a1a2+a2a3+a3a1).P,Q
15cor111_maximal_wire_equality_rigidityCor. 11.1∀a 1,a2,a3 ∈Z, a i ≥ 1 ∧(a1+a2+a3)(a1a2+a2a3+a3a1) = 9a1a2a3 =⇒
a1=a2 ∧a2=a3.
P,Q
16sec93_profile_three_block_iterationSec. 9.3t 0=t, tn+1=3tn+1 =⇒ ∀t,n∈N,2t n+ 1 = 3n(2t+ 1).P,Q
17sec32_cat0_midpoint_variance_gapSec. 3.2∀m,a,b,d∈Z, d̸= 0∧4m 2 ≤2a2 + 2b2 −d2 =⇒4m 2 <2a2 + 2b2.P,Q
18prop23_compression_recurrence_contractionProp. 2.3∀M,J∈N, M≥2 =⇒(M−1)
∑J−1
r=0 Mr + 1 =MJ.P,Q
Figure 3:(a)Mean exact zero-float verification latency
across all 16 canonical certificates (0.027–2.466 ms, log
scale).(b)Live adversarial red-team audit rejecting 70/70
forgeries across five attack classes with exact error-branch
assertions.
4 Exact Findings, Worked Wit-
nesses, and Audit
All experiments ran locally on Windows 11 (Python 3.12.6,
Lean 4.35.0; 7-run means after warm-up).
1. Finite-Size Separation, Tripod Rigidity & Ex-
haustive Tag(1,1)(Figs. 1–2).Exact integer-ceiling
sweeps across n∈ {2,4,..., 4096}show Corollary 1.2’s
⌈n9/4⌉surpassing Landsberg–Michałek’s2 n2 −⌈log 2 n⌉−1
by2 .00×at n = 256(262 ,144vs.131 ,063) and4 .00×at
n= 4096(134,217,728vs.33 ,554,419). Figure 2 plots ex-
act rational evaluations ofD∗(1,1,b)across b∈ [1/8,32]:
the ratioPerim/D∗peaks uniquely at9/4for b= 1(zero
AM–HM defect) and drops to11/5 = 2.20at(1 ,2,3)(de-
fect4 /33) and20502 /10201 ≈2.0098at(1 ,1,100)(defect
726/67). Exhaustively enumerating all26 = 64inputs to
Tag(1,1)confirms64 /64exact agreement (8 accepted, 56
rejected) with Section 4.1’s two-Dw signed-sum reduction.
2. Hand-Verifiable Worked Exact Witnesses (One
per Mode).
• Mode 1 (C02, n = 256 = 28, rect(16 ,4,16), tight
T6):256 9 = 272 = (218)4, certifying border rank
≥ 262,144 > 217 = 131,072(refuting Sun [ 9]) and
≥ 131,072nonscalar gates; for T16,4,16,(1024) 3/4 ≈
181.0 <max (64,64,256) = 256; forT6 with B = 7, all
63 = 216triples satisfy(i−7j)+(7 j−49k)+(49 k−i) = 0
with36distinct weights per factor.
• Mode 2 ( C06,2 ×2Strassen + division over
F257[X,Y ][u,v]/(u2,v2)):Routing M1 through( M1d)/d
with regular nonconstant d = a00 + b11 + 1uses 30
gates (q = 9symbolically nonscalar: 8 mul + 1 div,
Lemma 2.4 rank bound2 q = 18) and symbolically
matches( A0 + uX)(B0 + vY)across all1 + 8 + 16 = 25
coordinates per output entry modulo 257.
• Mode 3 (C10, Tag(2,2), N = 4):On valid permutation
π = [2,0,3,1]with x = [1,3,2,0],y = [3,0,1,2]( xi =
yπ(i)), D(1)
w = 1and the2 4 = 16-term signed sum yields
+1; mutatingx3 →1collapses the signed sum to0, and
collidingπ 2 →2givesD (1)
w = 0.
• Mode 4 (C13 & C14):On(1 ,1,1), D∗ = 3−1
3 = 8
3 ,
perimeter= 6, ratio= 6/(8/3) = 9/4, AM–HM margin
= 0, andD∗(1,1,5) = 7− 5
11 = 72
11 = 5 +3
2 + 1
22 . On
scale-1 maximal( 3
8 ,3
8 ,3
8 )(Cor. 11.1), D∗= 1, all three
wire lengths equal3
4 , and perimeter= 9/4.
3. 16-Certificate Atlas & 76-Test Red-Team Audit
(Table 2, Fig. 3).Table 2 lists all 16 canonical certificates
verified in0.027–2.466 ms. tests/test_suite.py runs 76
pytest checks: 1 full 16-certificate replay, 3 raw-JSON parser
guards (float,NaN, duplicate keys), 2 exact regressions (ex-
haustive 64-inputTag(1,1)agreement and balanced tripod
peak / Sunn= 256refutation), and 70 parametrized live
3

--- Page 4 ---
Table 2: Canonical 16-certificate OMEGA94-LB-CERT-1.0
atlas (exp1_certificate_atlas.json; all 16 verified).
ID Certificate Name M Exact Certified Witness Summary ms
C01m1_bounds_n16_rect4x4x4M1n=16:R ≥512, gates≥256,T4,4,4≥230.038
C02m1_bounds_n256_sun_refuteM1n=256:R≥218>217, gates≥1310720.077
C03m1_bounds_n1024_rect64x16x64M1n=1024:R≥5931642,T8 (512triples) 0.125
C04m1_bounds_n4096_rect256x64x256M1n=4096:R≥227,T10 (1000triples) 0.229
C05m2_dual_strassen_2x2_f101M2F101,2×2Strassen:q=7,2q=140.132
C06m2_dual_strassen_div_2x2_f257M2F257,2×2Strassen+div:q=9,2q=180.169
C07m2_dual_schoolbook_div_3x3_f509M2F509,3×3+div:q=29,2q=580.499
C08m2_dual_schoolbook_4x4_f1009M2F1009,4×4symbolic:q=64,2q=1282.466
C09m3_tag_h1_exhaustive_4casesM3Tag(1,1)(N=2): 4 instances (2 acc.) 0.027
C10m3_tag_h2_valid_and_collisionsM3Tag(2,2)(N=4): 4 instances (16 masks) 0.060
C11m3_tag_h3_cyclic_perm_n8M3Tag(3,3)(N=8): cyclic (256 masks) 0.610
C12m3_tag_h3_involution_n8M3Tag(3,3)(N=8): invol. (256 masks) 0.301
C13m4_tripod_balanced_unit_1_1_1M4(1,1,1):D∗=8/3, ratio9/4, margin00.045
C14m4_tripod_maximal_scale1_3_8M4(38,38,38):D∗=1, wires34,9/40.046
C15m4_tripod_asymmetric_1_2_3M4(1,2,3):D∗=60/11, ratio11/5, marg.4/330.044
C16m4_tripod_stretched_1_1_100M4(1,1,100): ratio20502/10201,b=1000.047
adversarial forgeries (12 schema/parser, 14 Mode 1, 16
Mode 2 including aq=1single-direction cheat and non-
canonical field/constant entries, 14 Mode 3, and 14 Mode 4
including a forged zero-column-sum star matrix), each as-
serting an exact regex on its intendedCertificateError
branch. scripts/verify_all.py enforces all 5 gates in-
cluding strict axiom whitelisting and a 41-file SHA-256
manifest.
5 Conclusion
We built an independent, explicitly scoped, zero-floating-
point verification companion for the discrete algebraic,
symbolic dual-number bilinearization, tight-tensor, tagged-
permutation, harmonic-star, and tripod AM–HM rigidity
mechanisms of OpenAI’sωF = 9/4lower-bound preprint [5],
pairing 18 constructive Lean 4.35.0 sub-lemmas (zerosorry,
zero Classical.choice) with the pure-int/Fraction 4-
mode auditor OMEGA94-LB-CERT-1.0, 16 canonical exact
finite witnesses, and 70/70 live adversarial forgery rejec-
tions.
References
[1] Alimzhan Amanov, Maxim van den Berg, and Jeroen Zuiddam.
Multiplying matrices via polynomials: Exposition and barriers.
arXiv:2610.30054v1, 2026.
[2] Markus Bläser. Lower bounds for the bilinear complexity of
associative algebras.Computational Complexity, 9:73–112, 2000.
[3] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem
prover and programming language. InAutomated Deduction –
CADE 28, volume 12699 ofLNCS, pages 625–635. Springer, 2021.
[4] J. M. Landsberg and Mateusz Michałek. A2n2 −log2(n)−1lower
bound for the border rank of matrix multiplication.International
Mathematics Research Notices, 2018(15):4722–4733, 2018.
[5] OpenAI. The matrix multiplication exponent is nine fourths.
Unrefereed Companion Preprint (OpenAI Math Release,https:
//github.com/openai/math/blob/main/preprints/The-matri
x-multiplication-exponent-is-nine-fourths-November-24-2
026/paper.pdf ), November 2026. Proposes the matching lower
bound ωF = 9/4over every field, geometric border rank≥n 9/4,
and⌈n 9/4/2⌉nonscalar gates.
[6] OpenAI. An upper bound of 9/4 for the matrix multiplication
exponent. OpenAI Math Release Preprint (October 2, 2026; es-
tablishesω C ≤9/4), October 2026.
[7] Volker Strassen. Gaussian elimination is not optimal.Numerische
Mathematik, 13(4):354–356, 1969.
[8] Volker Strassen. Algebra and complexity. InFirst European
Congress of Mathematics, Vol. II, volume 120 ofProgress in
Mathematics, pages 429–446. Birkhäuser, 1994.
[9] Zhi-Wei Sun. Tensor degenerations for matrix multiplication.
arXiv:2610.13971v1, 2026.
4
