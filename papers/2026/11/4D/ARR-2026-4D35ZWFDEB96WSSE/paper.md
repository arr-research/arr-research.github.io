# Constructive Lean 4 Kernel and Exact Zero-Float Certificates for OpenAI's Exponential Sunflower Bound

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-4D35ZWFDEB96WSSE` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/openai-erdos-rado-sunflower-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `1e29993df5abcb95572b89824b7a18d57546071b8a818c68c6747bd4e2d76e62`

## Abstract

A November 24, 2026 companion preprint from OpenAI proposes a proof of the 66-year Erdos-Rado fixed-petal sunflower conjecture: for every r >= 3, every r-sunflower-free family of distinct sets of size at most k has at most B_r^k members with log B_r = O((log r)^4 (log log(2r))^(5/2)), independent of k. Rather than assuming peer-reviewed endorsement of its Euclidean asymptotic-spectrum pricing, majority-vote differentiation, or multi-level binary-layout recursion pillars, we deliver an independent, explicitly scoped, zero-floating-point verification companion for its discrete combinatorial, planar-semiperimeter, Behrend-sphere broadcast, F_2^b XOR-matching equality filter, and two-head inclusion-exclusion cancellation mechanisms. Layer 1 (OpenAISunflowerExp.lean) proves 18 standalone constructive Lean 4.35.0 combinatorial and algebraic sub-lemmas (zero sorry, zero axiom, zero Classical.choice, zero warnings; 1 none, 2 [propext], and 15 [propext, Quot.sound]). Layer 2 (SUNFLOWER-EXP-CERT-1.0) is a pure-stdlib Python int/Fraction 4-mode auditor certifying 16 canonical finite witnesses in 0.024-19.286 ms and rejecting 74/74 live adversarial forgeries with exact branch assertions (80/80 pytest checks).

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Kernel and Exact Zero-Float Certificates
for OpenAI’s Exponential Sunflower Bound
Lluis Eriksson∗
November 25, 2026
Abstract
A November 24, 2026 companion preprint from OpenAI [9]
proposes a proof of the 66-year Erdős–Rado fixed-petal
sunflower conjecture: for everyr≥ 3, every r-sunflower-
free family of distinct sets of size at mostk has at most
Bk
r members withlogBr = O((logr)4(log log(2r))5/2), in-
dependent of k. Rather than assuming peer-reviewed
endorsement of its Euclidean asymptotic-spectrum pric-
ing, majority-vote differentiation, or multi-level binary-
layout recursion pillars, we deliver an independent, explic-
itly scoped, zero-floating-point verification companion for
its discrete combinatorial, planar-semiperimeter, Behrend-
sphere broadcast,Fb
2 XOR-matching equality filter, and two-
head inclusion–exclusion cancellation mechanisms. Layer 1
(OpenAISunflowerExp.lean ) proves 18 standalone con-
structive Lean 4.35.0 combinatorial and algebraic sub-
lemmas (zerosorry, zeroaxiom, zeroClassical.choice,
zero warnings; 1 none, 2 [propext], and 15 [propext,
Quot.sound]). Layer 2 (SUNFLOWER-EXP-CERT-1.0) is a
pure-stdlib Pythonint/Fraction 4-mode auditor certify-
ing 16 canonical finite witnesses in0.024–19.286 ms and
rejecting 74/74 live adversarial forgeries with exact branch
assertions (80/80 pytest checks).
1 Introduction and Scope Calibra-
tion
Erdős and Rado [8] provedMr(k) ≤k!(r−1)k and conjec-
tured an exponential bound independent ofk. On the lower-
bound side, block transversals givebr ≥r− 1and Abbott–
Hanson–Sauer provedb3 ≥
√
10 [2]; on the upper-bound
side, Alweiss–Lovett–Wu–Zhang [4] and Bell–Chueluecha–
Warnke [6] reduced the base toO(rlog (k+ 1)). Building on
the transversal word reduction of Alon–Shpilka–Umans [3],
OpenAI’s November 24, 2026 companion preprint [9] pro-
posesM r(k)≤B k
r via four discrete-combinatorial pillars:
1. Transversal Words & Eq. (3.1) Agreement Rules
(Secs. 1, 2.1, 3.2):A column ofr words is admissible
iff constant or pairwise distinct; the rules(A,B) →Zi,
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with
transparent AI coding, formalization, and drafting assistance via
Google Antigravity; all Lean 4 theorems, exact zero-float verifiers,
and adversarial tests were independently compiled and verified locally.
Repository: github.com/lluiseriksson/openai-erdos-rado-sunfl
ower-certificates.
(A,Zi) →B ,( B,Zi) →A ,( Zi,Zj) →A (i < j) force
admissibility identically.
2. Planar Semiperimeter Placement & Surplus
(Sec. 3.2, Prop. 2.1):Setting t = 1
2(r−1) , η = t2/4,
D= 2+ηyields positive surplusρ= η
2+η = 1
32(r−1)2+1 >
0, rectanglegapd−t≥t , andtrianglegap
√
1+4t2−1
2 −η >
η.
3. Behrend-Sphere Broadcast Rigidity (Sec. 4,
Lem. 4.1, Eq. 4.1):Encoding controls on equal-norm
integer spheresH,Vu ⊂{0,...,q− 1}m (with equal inner
product withuon Vu) makes∑c
z=1 gz = cu+ ∑a
j=2 vj−
(a−1)v1 (modL )with L= (a+ c−1)(q−1) + 1force
gz =uandv j =v1 identically [5].
4. XOR Matching Equality Filter & Two-Head IE
(Secs. 5, 6, 11, 12.2):PairingFb
2 via {x,x⊕p} (p̸= 0)
yields2 b −1matches when x= y and the unique false
match p= x⊕y when x̸= y; for(1 + b′)-bit head–tail
masking, I0I1 −(I0 −T0)(I1 −T1)cancels 100% of false
ties on every violation.
Honest Two-Layer Verification Scope.
1. Layer 1 (Lean 4.35.0 Kernel, Standalone Sub-
Lemmas): lean/OpenAISunflowerExp.lean proves 18
standalone constructive combinatorial and algebraic sub-
lemmas (Table 1) extracted from Sections 1, 1.3, 2.1, 3.2,
4, 5, 6, 11, 12.1, and 12.3 of [9].
2. Layer 2 (Exact Zero-Float Auditor):SUNFLOWER-
EXP-CERT-1.0 audits 16 canonical finite witnesses across
transversal sunflower-free word families (r≤ 5) and
exhaustive Eq. (3.1) rule checks, exact rational planar
placements (r≤ 64), exhaustive Behrend-sphere Eq. (4.1)
broadcasts (m≤ 5), and exhaustiveFb
2 XOR matching
(b≤5) + two-head IE replays (b′≤4).
3. Explicit Non-Claims:We donotformalize in Lean 4
the Euclidean spectral-point existence theorem (Theo-
rem 2.2), Gaussian mean-width convexity, majority-vote
reading by differentiation (Section 8), binary-layout sep-
aration geometry (Section 9), guard composition (Sec-
tion 10), or the full Theorem 1.1 asymptotic bound; those
analytic and geometric pillars remain unverified outside
the companion preprint [9].
1

--- Page 2 ---
2 Constructive Lean 4.35.0 Kernel
lean/OpenAISunflowerExp.lean compiles standalone in
1.1 sunder Lean 4.35.0 [7] with zero external imports, zero
warnings, zerosorry, and zeroClassical.choice. Audit-
ing viaAuditAxioms.lean confirms 1 zero-axiom theorem
(none: #2), 2[propext] theorems (P: #15, #18), and 15
[propext, Quot.sound]theorems (P,Q; Table 1).
Proposition 1(Constructive Lean 4 Kernel Scope).
All 18 sub-lemmas in Table 1 compile construc-
tively under Lean 4.35.0 without external libraries or
Classical.choice. Notably, Theorems 1–3 formalize
block-transversal growth, the integer bracket3<
√
10< 4
for b3, andr = 3rule admissibility; Theorems 4–7 prove
positive planar surplus and cleared triangle semiperime-
ter gains; Theorems 8–10 formalize Behrend equal-norm
sphere/average rigidity and zero wrap-around moduloL;
Theorems 11–14 prove unique XOR false-matching cancel-
lation and the cleared AM–GM splitting inequality; and
Theorems 15–18 formalize two-head inclusion–exclusion,
recursive child-increment negativity, and Abbott supermul-
tiplicativity [1].
3 Exact Zero-Float Certificate Au-
ditor
The modules sunflower_exact.py and sunflower_
certifier.py (under src/) use exclusively Pythonint
and fractions.Fraction (statically audited viaast.walk
for zero float/complex literals, /, /=, or math imports).
StrictJSONparsingrejectsfloats, NaN/Infinity, anddupli-
cate keys viaparse_float, parse_constant, andobject_
pairs_hook.
Definition 1( SUNFLOWER-EXP-CERT-1.0 Predicates).A
certificate withprotocol="SUNFLOWER-EXP-CERT-1.0" is
accepted iff every field passes strict schema checks and its
mode predicate holds:
• Mode 1 (transversal_sunflower_and_rules_cert):
Exhaustively tests everyr-subset of a distinctk-word
family(cappedat
(|W|
r
)
≤50,000)for r-sunflowers, audits
exact equivalence between Eq. (3.1) agreement rules and
column admissibility across all|Σ|r columns (r≤| Σ|≤
5), and checks exactk!(r−1) k and(r−1) k.
• Mode 2 (planar_semiperimeter_surplus_cert):Au-
dits canonical lowest-terms rational Section 3.2 invari-
ants t = 1
2(r−1) , η = t2/4, D = 2 + η, ρ = η/D >0,
rectangle gapt/D (r≥ 4), and cleared triangle bound
(1 +t2)2 <1 + 4t2 forr∈[3,200].
• Mode 3 (behrend_sphere_broadcast_cert):Verifies
equal squared norms on H and equal norm + inner
product onVu ⊂{0,...,q− 1}m, checksL≥ (a+ c−
1)(q−1)+1, and exhaustively tests every tuple inVa
u ×Hc
across all coordinates to certify zero wrap-around modulo
L and that Eq. (4.1) forcesgz = u, vj = v1 with exact
solution count|Vu|.
Figure 1:(a)Historical 3-petal base M3(k)1/k growth:
Erdős–Rado [8], BCW [6], AHS
√
10 [2], and Theorem 1.1’s
k-independent base (schematic constant height).(b)Exact
Section 3.2 planar surplusρ(r) = 1/(32(r− 1)2 + 1) > 0
acrossr∈[3,64].
Figure 2:(a)Exhaustive two-head inclusion–exclusion cen-
sus across all83 = 512three-symbol columns (b′= 2):8 /8
constants preserved,336distinct admissible,168 /168viola-
tions killed to0(384false ties canceled).(b)Section 5 Fb
2
XOR matching pairs verified acrossb∈{2,3,4,5}.
• Mode 4 (xor_matching_and_mask_ie_cert):Exhaus-
tively checks all4b pairs( x,y) ∈(Fb
2)2 (b∈ [2,5]) for
Section 5’s XOR perfect matching filter (2b−1matches iff
x= y; unique false matchx⊕y iff x̸= y) and replays Sec-
tion 6/12.2’s(2 b′
)2-mask two-head inclusion–exclusion
(requiring at least one violating and one constant col-
umn), certifying 100% violation annihilation and full
constant-column preservation.
4 Exact Findings, Worked Wit-
nesses, and Audit
All experiments ran locally on Windows 11 (Python 3.12.6,
Lean 4.35.0; 7-run means after warm-up).
1. Exact Planar Surplus & Exhaustive 512-
Column Two-Head IE Census (Figs. 1–2).Across
r∈{ 3,4,5,..., 64}, Section 3.2’s planar surplus decays
cleanly asρ(r) = 1/(32(r−1)2 + 1)(from1 /129at r= 3to
1/127009at r = 64). Exhaustively testing all8 3 = 512
three-symbol columns over(1 + 2)-bit letters ( b′ = 2,
16mask pairs each) confirms exact partition:8constant
columns survive with all16mask pairs,336pairwise-distinct
columns are admissible, and all168/168violating columns
are canceled identically to0(384false ties removed by
I0I1 −(I0 −T0)(I1 −T1)).
2

--- Page 3 ---
Table 1: Complete inventory of all 18 constructive Lean 4.35.0 sub-lemmas inlean/OpenAISunflowerExp.lean (zero
sorry, zero axiom, zero Classical.choice, zero warnings; none for #2; [propext] (P) for #15, #18; [propext,
Quot.sound](P,Q) for the remaining 15).
# Theorem Identifier Ref. [9] Exact Machine-Checked Statement & Hypotheses Ax.
1sec1_block_transversal_lower_growthSec. 1∀r,k∈N,3≤r=⇒2 k ≤(r−1) k (induction onk).P,Q
2sec13_abbott_hanson_sauer_base3Sec. 1.33·3<10∧10<4·4(certifies3<
√
10<4forb 3).none
3sec21_rules_force_admissible_r3Secs. 2.1, 3.2∀a,b,c∈N, Eq. (3.1) rules (r=3)=⇒(a=b∧b=c)∨(a̸=b∧a̸=c∧b̸=c).P,Q
4sec32_planar_surplus_positiveSec. 3.2∀r∈N,3≤r=⇒128≤8M 2 ∧8M2 <8M 2 + 1withM= 2(r−1).P,Q
5sec32_satellite_rectangle_gapSec. 3.2∀d,t∈Z,2t≤d=⇒t≤d−t(certifies(d−t)/D≥t/D).P,Q
6sec32_triangle_semiperimeter_gainSec. 3.2∀M∈N,4≤M=⇒(M 2 + 1)2 <M 4 + 4M2 (cleared
√
1 + 4t2 −1>t 2).P,Q
7sec32_anchor_satellite_net_gapSec. 3.2∀e∈Z,0<e=⇒0<2e−e(certifiest 2/2−η=η >0).P,Q
8lem41_behrend_sphere_point_rigidityLem. 4.1∀x,u∈Z, x 2 =u2 ∧xu=u 2 =⇒x=u.P,Q
9lem41_behrend_average_rigidity_2Lem. 4.1∀v 1,v2,v3 ∈Z,2v 1 =v2 +v3 ∧v2
2 =v2
1 ∧v2
3 =v2
1 =⇒v 2 =v1 ∧v3 =v1.P,Q
10lem41_no_wraparound_mod_LLem. 4.1∀L,D,k∈Z,−L<D<L∧D=kL=⇒D= 0.P,Q
11sec5_xor_unique_false_matchingSec. 5∀x,y,p∈N,(x⊕p=y)⇐⇒(p=x⊕y).P,Q
12sec5_matching_count_lbSec. 5∀b∈N,1≤b=⇒2 b−1 ≤2 b −1(L b ≥2 b−1).P,Q
13sec5_two_broadcast_leading_costSec. 5∀w P ,wT ,wK,g∈Z, g = wP +wT −wK =⇒ (wK−wP )+(wK−wT ) = wK−g. P,Q
14sec5_amgm_convergence_splitSec. 5∀X,Y∈Z,4XY≤(X+Y) 2 (cleared AM–GM convergence split).P,Q
15sec6_two_head_inclusion_exclusionSec. 6∀I 0,I1,T0,T1 ∈Z, T0 =I0 ∨T1 =I1 =⇒I 0I1 −(I0 −T0)(I1 −T1) =I0I1.P
16sec11_disjoint_repeated_heads_boundSec. 11∀n∈N,2·⌊n/2⌋≤n(disjoint repeated-head count).P,Q
17lem121_child_increment_negativeLem. 12.1∀l,g 0,G∈N,1≤l∧g 0 ≤l=⇒3l+g 0 +G<10(l+G).P,Q
18sec123_abbott_supermultiplicative_powSec. 12.3∀B,k,l,M k,Ml ∈N, Bk ≤Mk ∧Bl ≤Ml =⇒B k+l ≤MkMl.P
Figure 3:(a)Mean exact zero-float verification latency
across all 16 canonical certificates (0.024–19.286 ms, log
scale).(b)Live adversarial red-team audit rejecting 74/74
forgeries across five attack classes with exact error-branch
assertions.
2. Hand-Verifiable Worked Exact Witnesses (One
per Mode).
• Mode 1 (C01, r= 3,k = 3, block family{0,1}3):All(8
3
)
= 56triples fail admissibility, confirming sunflower-
freeness at the exact block-transversal lower bound(3−
1)3 = 8(vs.3! ·23 = 48); all4 3 = 64columns satisfy
Eq. (3.1) iff admissible.
• Mode 2 (C06, r= 5): t= 1
8 , η= 1
256 , D= 513
256 , ρ= 1
513 ,
rectangle gap t
D = 32
513 , and cleared triangle inequality
(1 + 1
64 )2 = 4225
4096 < 4352
4096 = 1 + 4
64 .
• Mode 3 (C10, m = 4 ,q = 3 ,a = 2 ,c = 2 ,L = 7):
With u= (1,1,0,0)( ∥u∥2 = 2), H the 6 weight-2 binary
vectors, andVu the 4 vectors with∥v∥2 = 2,⟨u,v⟩ = 1,
all4 2 ·62 = 576tuples satisfy |diff|< 7and yield exactly
4diagonal solutionsg 1 =g2 =u,v 1 =v2.
• Mode 4 (C14, b= 3,b′= 3):All4 3 = 64pairs in( F3
2)2
match7masks iff x= y and uniquex⊕y iff x̸= y; on
violating column[2 ,2,11,11](both heads repeat), all8
false ties across64mask pairs are canceled identically to
0.
Table 2: Canonical 16-certificate SUNFLOWER-EXP-
CERT-1.0 atlas (exp1_certificate_atlas.json; all 16
verified).
ID Certificate Name M Exact Certified Witness Summary ms
C01m1_transversal_r3_k3_block8M1r=3,k=3: 8 words (sf), 64 rule cols 0.115
C02m1_transversal_r3_k3_has_sunflowerM1r=3,k=3: 5 words (non-sf), 27 cols 0.031
C03m1_transversal_r4_k3_block27M1r=4,k=3: 27 words (sf), 256 cols 19.286
C04m1_transversal_r5_k2_block16M1r=5,k=2: 16 words (sf), 3125 cols 5.880
C05m2_planar_surplus_r3M2r=3:t=1/4,ρ=1/129, anchor lb1/1290.024
C06m2_planar_surplus_r5M2r=5:t=1/8,ρ=1/513, anchor lb1/5130.025
C07m2_planar_surplus_r16M2r=16:t=1/30,ρ=1/72010.026
C08m2_planar_surplus_r64M2r=64:t=1/126,ρ=1/1270090.026
C09m3_behrend_m3_q4_a2_c1M3m=3,L=7:∥u∥ 2=5, 2 diag. sols 0.073
C10m3_behrend_m4_q3_a2_c2M3m=4,L=7:∥u∥ 2=2, 4 diag. sols 1.576
C11m3_behrend_m4_q4_a3_c1M3m=4,L=11:∥u∥ 2=8, 4 diag. sols 1.220
C12m3_behrend_m5_q3_a3_c2M3m=5,L=9:∥u∥ 2=3, 3 diag. sols 3.300
C13m4_xor_b2_tail2_colsM4b=2(16 pairs),b ′=2, 2 viol. killed 0.069
C14m4_xor_b3_tail3_colsM4b=3(64 pairs),b ′=3, 3 viol. killed 0.273
C15m4_xor_b4_tail3_colsM4b=4(256 pairs),b ′=3, 3 viol. killed 1.045
C16m4_xor_b5_tail4_colsM4b=5(1024 pairs),b ′=4, 3 viol. killed 8.820
3. 16-Certificate Atlas & 80-Test Red-Team Audit
(Table 2, Fig. 3).Table 2 lists all 16 canonical certifi-
cates verified in0 .024–19.286 ms. tests/test_suite.py
runs 80 pytest checks: 1 full 16-certificate replay, 3 raw-
JSON parser guards (float,NaN, duplicate keys), 2 exact
regressions (exhaustive 512-column two-head IE audit and
exact rational planar surplus), and 74 parametrized live ad-
versarial forgeries (12 schema/parser, 16 Mode 1, 16 Mode 2,
14 Mode 3, 16 Mode 4), each asserting an exact regex on
its intendedCertificateError branch. scripts/verify_
all.py enforces all 5 gates including strict axiom whitelist-
ing and a 41-file SHA-256 manifest.
5 Conclusion
We built an independent, explicitly scoped, zero-floating-
point verification companion for the discrete transversal,
planar-semiperimeter, Behrend-sphere broadcast, XOR-
matching equality filter, and two-head inclusion–exclusion
mechanisms of OpenAI’s exponential sunflower preprint [9],
pairing 18 constructive Lean 4.35.0 sub-lemmas (zerosorry,
zero Classical.choice) with the pure-int/Fraction 4-
mode auditorSUNFLOWER-EXP-CERT-1.0, 16 canonical ex-
3

--- Page 4 ---
act finite witnesses, and 74/74 live adversarial forgery re-
jections.
References
[1] H. L. Abbott. Some remarks on a combinatorial theorem of Erdős
and Rado.Canadian Mathematical Bulletin, 9(2):155–160, 1966.
[2] H. L. Abbott, D. Hanson, and N. Sauer. Intersection theorems
for systems of sets.Journal of Combinatorial Theory, Series A,
12(3):381–389, 1972.
[3] Noga Alon, Amir Shpilka, and Christopher Umans. On sunflowers
and matrix multiplication.Computational Complexity, 22:219–243,
2013.
[4] Ryan Alweiss, Shachar Lovett, Kewen Wu, and Jiapeng Zhang.
Improved bounds for the sunflower lemma.Annals of Mathematics,
194:795–815, 2021.
[5] Felix A. Behrend. On sets of integers which contain no three terms
in arithmetical progression.Proceedings of the National Academy
of Sciences of the United States of America, 32(12):331–332, 1946.
[6] Tolson Bell, Suchakree Chueluecha, and Lutz Warnke. Note on
sunflowers.Discrete Mathematics, 344:112367, 2021.
[7] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem
prover and programming language. InAutomated Deduction –
CADE 28, volume 12699 ofLNCS, pages 625–635. Springer, 2021.
[8] Paul Erdős and Richard Rado. Intersection theorems for systems
of sets.Journal of the London Mathematical Society, 35:85–90,
1960.
[9] OpenAI. An exponential bound for sunflowers. Unrefereed Com-
panion Preprint (OpenAI Math Release,https://github.com
/openai/math/blob/main/preprints/An-exponential-bound-f
or-sunflowers-November-24-2026/paper.pdf ), November 2026.
Proposes Mr(k) ≤B k
r with logB r = O((logr )4(log log(2r))5/2)
for the Erdős–Rado fixed-petal sunflower conjecture.
4
