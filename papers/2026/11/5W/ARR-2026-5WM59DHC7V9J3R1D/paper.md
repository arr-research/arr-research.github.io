# Constructive Lean 4 Kernel and Exact Zero-Float Certificates for Unconditional L_N[1/3, 105] Las Vegas Integer Factorization

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5WM59DHC7V9J3R1D` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/cogentic-l13-factorization-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `ff64e8fb21fa42f3ab8795a85a4fed8a3f1594a978d5ca08192a8f64f124761d`

## Abstract

A November 25, 2026 companion preprint from Google Research's Cogentic framework proposes the first unconditional uniform zero-error Las Vegas integer factorization algorithm running in expected time L_N[1/3, 105] and deterministic workspace L_N[1/3, 40], aiming to bridge the 34-year gap between Lenstra-Pomerance's unconditional L_N[1/2, 1] bound and the heuristic L_N[1/3, c] Number Field Sieve. Rather than assuming peer-reviewed validation of its analytic sieve pillars, we deliver an independent, explicitly scoped, zero-floating-point verification companion for its discrete lattice, mod-3 Laplace ensemble, 3-adic Newton-Hensel square-root, Dixon splitting, and strong-induction mechanisms. Layer 1 (CogenticL13Factorization.lean) proves 18 standalone constructive Lean 4.35.0 algebraic, lattice, and arithmetic sub-lemmas (zero sorry, zero axiom, zero Classical.choice, zero warnings; 4 zero-axiom none and 14 [propext, Quot.sound]). Layer 2 (L13FACT-COGENTIC-CERT-1.0) is a pure-stdlib Python int/Fraction 4-mode auditor certifying 16 canonical finite witnesses in 0.081-0.609 ms and rejecting 68/68 live adversarial forgeries with exact branch assertions (74/74 pytest checks).

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Kernel and Exact Zero-Float Certificates
for UnconditionalL N[1/3,105]Las Vegas Integer Factorization
Lluis Eriksson∗
November 25, 2026
Abstract
A November 25, 2026 companion preprint from Google Re-
search’s Cogentic framework [6, 3] proposes the first uncon-
ditional uniform zero-error Las Vegas integer factorization
algorithm running in expected timeLN[1/3,105]and de-
terministic workspace LN[1/3,40], targeting the 34-year
gap between Lenstra–Pomerance’s unconditionalLN[1/2,1]
bound and the heuristic LN[1/3,c]Number Field Sieve.
Rather than assuming peer-reviewed validation of its an-
alytic sieve pillars, we deliver an independent, explicitly
scoped, zero-floating-point verification companion for its
discrete lattice, mod-3 discrete Laplace ensemble, deter-
ministic 3-adic Newton–Hensel square-root, Dixon split-
ting, and strong-induction mechanisms. Layer 1 (Cogent
icL13Factorization.lean ) proves 18 standalone con-
structive Lean 4.35.0 algebraic, lattice, and arithmetic sub-
lemmas (zerosorry, zeroaxiom, zeroClassical.choice,
zero warnings; 4 zero-axiom none and 14 [propext,
Quot.sound]). Layer 2 (L13FACT-COGENTIC-CERT-1.0) is
a pure-stdlib Pythonint/Fraction 4-mode auditor certi-
fying 16 canonical finite witnesses in0.081–0.609 ms and
rejecting 68/68 live adversarial forgeries with exact branch
assertions (74/74 pytest checks).
1 Introduction and Scope Calibra-
tion
For more than three decades, unconditional Las Vegas gen-
eral integer factorization stood at Lenstra–Pomerance’s
LN[1/2,1][ 8], while the General Number Field Sieve
(GNFS) [2] achieved LN[1/3,(64/9)1/3]only under un-
proved smoothness and algebraic heuristics. The Novem-
ber 25, 2026 Cogentic companion preprint [6, 3] proposes
an unconditional uniform zero-error Las Vegas multitape
Turing machine achieving expected timeLN[1/3,105]and
deterministic spaceLN[1/3,40]by coupling four discrete-
algebraic engines with Siegel-zero-free analytic sieves:
1. Mod-N LLL Lattices & 2D Lagrange–Gauss
Smooth Ratio Splitting (Props. 2.2–2.3):(3/4)-
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with
transparent AI coding, formalization, and drafting assistance via
Google Antigravity; all Lean 4 theorems, exact zero-float verifiers,
and adversarial tests were independently compiled and verified locally.
Repository: github.com/lluiseriksson/cogentic-l13-factoriza
tion-certificates.
LLL reduction [7] onΛ n = {h∈Z n : ∑hsms
N ≡0
(modN )}(g1mN ≡g0 (modN ), gn−1
1 >N/2) supports
exact layer-cake box sampling, while Lagrange–Gauss
reduction on Lz = {(x,y) ∈Z 2 : x≡zy (modN )}
splits blinded squareswm ≡z 2
m (modN )into disjoint
r0-prime ratiosx1/y1 below 1
2
√
N.
2. Mod-3 Discrete Laplace Ensemble & Geomet-
ric Ladder (Defs. 2.7, 4.1, Lem. 4.2):Pinning
f˜c(X,1) ≡h 0(X) ( mod 3)to a monic odd-degree irre-
ducible h0 ∈F 3[X]enforces3 ∤f ˜c(a,b)on all primi-
tive pairs and enables step-2 geometric descent across
Y0 >Y1 >···>Y J =B.
3. Deterministic 3-Adic Newton–Hensel Square
Roots (Lem. 5.2):Odd degree d forces4 |(3d + 1),
giving explicit initializationβ0 = α(3d+1)/4
0 in F×
3d and
quadratic lifting modulo(32k
, ˜fι)to exact global roots
ˆβι(X)2 ≡˜Γι(X) (mod ˜fι).
4. Adleman Characters, Blinded Dixon Splitting
& Strong Induction (Lems. 5.1, 5.3, Thm. 1.1):
Degree-1 quadratic characters cut the obstruction kernel
to dimF2 (E1 ×E 2) ≤ 2 < 3, unsealing zm splits N
via gcd(Z−Y,N )[ 5], and recursive calls on[2,⌊1
2
√
N⌋]
contract via21.15 + 104·2 −1/3 <103.72<104<105.
Honest Two-Layer Verification Scope.
1. Layer 1 (Lean 4.35.0 Kernel, Standalone Sub-
Lemmas): lean/CogenticL13Factorization.lean
proves 18 standalone constructive algebraic, lattice, 3-
adic Hensel, and rational-contraction sub-lemmas (Ta-
ble 1) extracted from Propositions 2.2–2.3, Lemmas 2.8,
4.2, 5.1–5.3, and Theorem 1.1 of [6].
2. Layer 2 (Exact Zero-Float Auditor): L13FACT-
COGENTIC-CERT-1.0 audits 16 finite exact witnesses
across mod-N (3/4)-LLL lattices and Lagrange–Gauss
ratio splits (N≤ 100,160,063), mod-3-pinned forms
(d∈{ 3,5}) with geometric ladders and smooth special-q
points, 3-adic Newton–Hensel lifting traces (K≤ 5), and
end-to-end two-field blinded Dixon splits (N≤64,507).
3. Explicit Non-Claims:We donotformalize in Lean 4
Gevrey-2 Mellin cutoffs, hybrid large sieves, truncated
Brun sieves, Siegel-zero-free local Euler cancellation (Sec-
tion 3), discrete Laplace sub-averaging and backward
path telescoping (Lemmas 4.3–4.6), Stark–Chebotarev/
Landau–Page density bounds (Lemma 5.1(3)), AKS pri-
1

--- Page 2 ---
mality [1], or multitape Turing-machine bit-cost account-
ing (Section 6); those analytic pillars remain unverified
outside the companion preprint [6].
2 Constructive Lean 4.35.0 Kernel
lean/CogenticL13Factorization.lean compiles stan-
dalone under Lean 4.35.0 [4] with zero external imports,
zero warnings, zero sorry, and zero Classical.choice.
Auditing viaAuditAxioms.lean confirms 4 zero-axiom the-
orems (none: #9, #15, #17, #18) and 14 [propext,
Quot.sound]theorems (P,Q; Table 1).
Proposition 1(Constructive Lean 4 Kernel Scope).
All 18 sub-lemmas in Table 1 compile construc-
tively under Lean 4.35.0 without external libraries
or Classical.choice. Notably, Theorems 4–6 prove
Lagrange–Gauss quadratic-form coercivity, determinant
bounds, andratio-splitinjectivityover Z; Theorems8 and11
prove the exact geometric ladder identity7∑9t16r−1−t +
9r = 16r and layer-cake telescoping universally by induction;
Theorems 12–14 prove4|(32k+1+1)and quadratic Newton–
Hensel convergence (M→M 2); Theorem 15 constructively
exhibits a nonzero kernel vector inF3
2 →F 2
2 with zero
axioms; and Theorems 17–18 certify Theorem 1.1’s strong-
induction runtime (103.70 < 104 < 105) and workspace
(37.40<38<40) contractions via exact integer cubes.
3 Exact Zero-Float Certificate Au-
ditor
The modules l13fact_exact.py and l13fact_
certifier.py (under src/) use exclusively Python
int, fractions.Fraction, and exactmath.gcd (statically
audited viaast.walk for zero float/complex literals, true
division /, or floating-pointmath.* calls). Deterministic
primality uses 13-base Miller–Rabin (bases2... 41, exact
below3 .317 ×1024). Strict JSON parsing rejects floats,
NaN/Infinity, and duplicate keys via parse_float,
parse_constant, andobject_pairs_hook.
Definition 1( L13FACT-COGENTIC-CERT-1.0 Predi-
cates).A certificate with protocol="L13FACT-COGENTIC-
CERT-1.0" is accepted iff every field passes strict schema
checks and its mode predicate holds:
• Mode 1 ( mod_n_lattice_and_lagrange_split_
cert):Audits odd N≥ 15, g1mN ≡g 0 (modN ),
gn−1
1 > N/2, exactΛ n membership of every column
of Blat, Bareiss |detB lat| = N, integer adjugate
AadjBlat = NIn, exact rational(3 /4)-LLL reduction
and Prop. 2.2(1) bound ∥bj∥2
2 ≤ 2n+3G2, plus 2D
Lagrange–Gauss reduction( v1,v2)on Lz (z≡st 2
(modN )) and smooth split(x1,y1) = (∏
p∈Ap,∏
q∈B q)
on disjointr0-prime setsA,B⊆[2,Q]with4Q 2r0 ≤N.
• Mode 2 (mod3_laplace_ladder_and_smooth_cert):
Audits gcd(N,6) = 1,3 |M ,6 W≤M , Rabin irre-
ducibility of monic odd-degreeh0 ∈F 3[X], mod-3-pinned
Figure 1:(a)Leading-term bit-operation exponents compar-
ing deterministicO(exp(3(lnN)3/4)), Lenstra–Pomerance
LN[1/2,1], Cogentic LN[1/3,105], and heuristic GNFS
LN[1/3,1.923].(b)Theorem 1.1 strong-induction expo-
nent contraction budgets (103.70 < 104 < 105runtime;
37.40<38<40deterministic workspace).
Figure2:(a)Deterministic3-adicNewton–Henselquadratic
precision doubling2 klog2 3recovering exact global square
roots atk= 4(25 .36 bits) ford= 3(19-bit root) andd= 5
(21-bit root).(b)Exact skip-2 geometric ladder path sum
1
2
∑r−1
t=0 (9/16)t monotonically bounded by8/7≈1.1429.
form f˜c(g0,g1) ≡ 0 ( modN ), strictly decreasing lad-
der Y0 >···> Y J ≥ 2, special-q root f˜c(rq,1) ≡ 0
(modq ), primitive lattice point( a,b) ∈ Λq,rq with
3 ∤f˜c(a,b)and non-vacuously smooth cofactorf˜c(a,b)/q
(2≤cap<cofactor), and exact layer-cake telescoping.
• Mode 3 (adic3_newton_hensel_sqrt_cert):Audits
monic odd-degree ˜f∈Z [X]irreducible mod 3,4 |
(3d + 1), ˜Γ = ˜f′(θ)2 ∏(cdaν −bνθ), independent Euler
square check and lifting trace(βk,γk)satisfying β2
k ≡˜Γ
(mod 32k
, ˜f)and2 βkγk ≡1 ( mod 32max(0,k−1)
, ˜f), bal-
anced bound|ˆbj|≤ (32K
−1)/2, and exact global square
ˆβ(X)2 ≡˜Γ(X) (mod ˜f)inZ[X].
• Mode 4 (dixon_character_and_induction_split_
cert):Audits odd composite N, canonical0 ≤
mN,Y,Z < N, two mod-3-pinned forms( f1,f2)van-
ishing at( g0,g1) ( modN ), degree-1 Adleman charac-
ters( ℓ,s)with ˜fι(s) ≡ 0 ( modℓ ), per-relation non-
empty algebraic factor lists and Eq. (6.1) congruences
with wm ≡z2
m (modN ), F2 right-nullspace mask, both
Lemma 5.2 3-adic roots( ˆβ1,ˆβ2), exact Y2 ≡Z 2 ≡∏
Tx
wm (modN ), nontrivial split1 <gcd (Z−Y,N ) <
N, and Theorem 1.1 integer-cube contraction guards.
2

--- Page 3 ---
Table 1: Complete inventory of all 18 constructive Lean 4.35.0 sub-lemmas inlean/CogenticL13Factorization.lean
(zero sorry, zero axiom, zero Classical.choice, zero warnings; none for #9, #15, #17, #18 and [propext,
Quot.sound](P,Q) for the remaining 14).
# Theorem Identifier Ref. [6] Exact Machine-Checked Statement & Hypotheses Ax.
1prop22_lll_basis_norm_boundProp. 2.21≤j≤n=⇒(4·2 n−j + (2n −2 n−j+1))S≤4·2 n−1S.P,Q
2prop22_dual_lattice_gapProp. 2.20<t,2t<N, N <2g n−1
1 , gn−1
1 |t=⇒False(dual gap).P,Q
3prop22_box_inclusion_marginProp. 2.2η≥ 2, Wmin ≤W i, 6η≤W min =⇒ (Wi+1)(Wmin−6η) ≤
(Wi+1−(4η+2))Wmin.
P,Q
4prop23_lagrange_gauss_quad_formProp. 2.30≤n 1 ≤n2,|2g|≤n 1 =⇒x 2
1n1 +x2
2n2 ≤2(x2
1n1 + 2x1x2g+x 2
2n2).P,Q
5prop23_lagrange_det_boundsProp. 2.30≤n 1 ≤n2,4g 2 ≤n2
1 =⇒3n 1n2 ≤4(n1n2 −g2)≤4n 1n2.P,Q
6prop23_ratio_split_injectiveProp. 2.30≤H,4H 2 ≤N, ui,vi ∈[1,H], N|(u 1v2 −u2v1) =⇒u 1v2 =u2v1.P,Q
7prop23_alternating_sign_nonnegProp. 2.3 2K≤M Q, 4r2
0MQ ≤(s−2r0)2, j < r0 =⇒ 2(K−j)(2r0−2j)(2r0−2j−1) ≤
(j+1)(s−2r0+2j+2)(s−2r0+2j+1).
P,Q
8lem28_ladder_geometric_sumLem. 2.8∀r∈N,7
∑r−1
t=0 9t16r−1−t + 9r = 16r (certifies 8
7 lnQ0).P,Q
9lem28_exponent_ratio_identitiesLem. 2.8 Ground schedule ratios:8 + 1 + 8 = 17,3·6−1 = 17,17·6 = 102<108.none
10lem42_mod3_irreducible_nondivLem. 4.2¬(3|a∧3|b),(3|b⇒f%3 =a d%3),(3∤b⇒f%3̸= 0) =⇒3∤f.P,Q
11lem42_laplace_layer_cake_telescopeLem. 4.2∀z∈Z, a,m∈N, (1 −z) tail(z,a,m ) = (2a+ 1)za(1 −z) + 2(za+1 −za+m+1). P,Q
12lem52_three_pow_odd_div_fourLem. 5.2∀k∈N,4|(3 2k+1 + 1)(exactF ×
3d root exponent).P,Q
13lem52_newton_inv_quad_stepLem. 5.2∀M,b,g∈Z, M|(1−2bg) =⇒M 2 |(1−2b(g(2−2bg))).P,Q
14lem52_newton_sqrt_quad_stepLem. 5.2M|(b 2 −G), M|(1−2bg ′) =⇒M 2 |((b+ (G−b 2)g′)2 −G).P,Q
15lem51_kernel_dim_pigeonholeLem. 5.1∀v 1,v2,v3 ∈F 2
2,∃λ∈F 3
2 \{0}, λ1v1 ⊕λ2v2 ⊕λ3v3 = (0,0).none
16lem53_dixon_congruence_splitLem. 5.3Y≤Z, N| (Z−Y)(Z+Y), N∤ (Z−Y), N∤ (Z+Y) =⇒ ¬Cop(N,Z−Y ) ∧
¬Cop(N,Z+Y).
P,Q
17thm11_runtime_contraction_105Thm. 1.1 1043 ·1003 < 2 ·82553,2115 +8255 < 10372 < 10400 < 10500,104 3 ·1003 <
10·4828 3,7160<10400.
none
18thm11_workspace_and_phase_successThm. 1.138 3 ·100 3 <2·3017 3,3740<3800<4000, and3·29106>80000(>1/3).none
4 Exact Findings, Worked Wit-
nesses, and Audit
All experiments ran locally on Windows 11 (Python 3.12.6,
Lean 4.35.0; 7-run means after warm-up).
1. Complexity Regimes, 3-Adic Convergence &
Ladder Geometry (Figs. 1–2).Figure 1(b) confirms
Theorem 1.1’s strong-induction margins: recursive calls
on[2 ,⌊1
2
√
N⌋]shrink the cind = 104exponent by2 −1/3
to82 .5448 ···< 82.55, so smooth-ratio collection sums
to21 .15 + 82.55 = 103 .70 < 103.72 < 104 < 105, while
descent-tree recursion on[2 ,N1/10]shrinks by10 −1/3 to
48.2725 ···< 48.28(total71 .60 < 104), and workspace
contracts via38 ·2−1/3 < 30.17(37 .40 < 38 < 40). In
Figure 2(a), deterministic 3-adic quadratic lifting doubles
precision from3 .17to101 .44bits in k= 6steps (0 .159 ms
for d = 3,0 .393 ms for d = 5), crossing both19-bit and
21-bit global roots cleanly atk= 4(25 .36bits). Figure 2(b)
verifies exact rational convergence of1
2
∑r−1
t=0 (9/16)t to8 /7
across depthsr= 1...12.
2. Hand-Verifiable Worked Exact Witnesses (One
per Mode).
• Mode 1 ( C01, N = 101 ·103 = 10 ,403,G =
50,g0 = 79 ,g1 = 83 ,n = 3):83 ·1505 ≡ 79
(mod 10403),83 2 = 6889 > 5201.5;(3 /4)-LLL basis
columns( −8,−10,−9)⊤,(7,12,−12)⊤,(−34,17,−2)⊤
have|detB lat|= 10,403,max∥b j∥2
2 = 1449≤2 6 ·50 2 =
160,000, andAadjBlat = 10,403I3; fors= 8934,t = 17,
z= 1982 ≡10 ·21−1 (mod 10403), Lagrange–Gauss re-
turns v1 = (10,21) = (2 ·5,3 ·7)( Q= 7,4 ·74 = 9604 ≤
10403).
• Mode 2 (C05, N = 323 ,d = 3 ,M = 180 ,W =
25,h0 = X3 + 2X + 1):With ˜c= (−15,−25,−18,0),
Figure 3:(a)Mean exact zero-float verification latency
across all 16 canonical certificates (0.081–0.609 ms, log
scale).(b)Live adversarial red-team audit rejecting 68/68
forgeries across five attack classes with exact error-branch
assertions.
f˜c(X,Y ) = 256X3 −54X2Y− 73XY2 −44Y3 satisfies
f˜c(7,11) = −61,693 = 323 ·(−191) ≡0 ( mod 323)and
f˜c(10,1) ≡0 ( mod 23); primitive point(33,1) ∈Λ23,10
gives f˜c(33,1)/23 = 397,331 = 11 ·41 ·881(2500-smooth,
3∤397,331).
• Mode 3 (C09, ˜f = X3 + 2X+ 1, K = 3,3 8 = 6561):
Pairs(2 ,1)2(3,1)2 yield β0 = θ2 + θ, β1 = 4θ2 + θ, β2 =
67θ2 + 64θ+ 54,β3 = 6547θ2 + 6544θ+ 6534 (mod 6561),
balancing to exactˆβ(X) = −14X2 −17X− 27 ∈Z [X]
with ˆβ(θ)2 ≡˜Γ(θ) (mod ˜f).
• Mode 4 (C13, N = 17 ·19 = 323,g0 = 7,g1 = 11,mN =
30):Mod-3-pinned forms (ascending coefficients) f1 =
(−44,−73,−54,256)and f2 = (−37,−73,−69,259)with
6 Adleman characters and 4 blinded relations yield
F2-nullspace mask[1 ,1,0,0]( w0 = 254 = 106 2,w1 =
172 = 227 2 (mod 323)); K = 53-adic roots (as-
cending) ˆβ1 = (18219008 ,92672,−1482)and ˆβ2 =
(−22136730,−145040,2262)assemble Y = 27, while
unsealing gives Z = 106 ·227 ≡ 160 ( mod 323)
3

--- Page 4 ---
Table 2: Canonical 16-certificate L13FACT-COGENTIC-
CERT-1.0 atlas (exp1_certificate_atlas.json; all 16
verified).
Certificate ID M Exact Certified Witness Summary ms
m1_lattice_lagrange_n10403_d3M1N=10403,n=3:r0=2,(10,21),λ2
1=5410.118
m1_lattice_lagrange_n64507_d3M1N=64507,n=3:r0=2,(33,35),λ2
1=23140.118
m1_lattice_lagrange_n256027_d4M1N=256027,n=4:r0=2,(26,55),λ2
1=37010.192
m1_lattice_lagrange_n100160063_d4M1N=100160063,n=4:r0=3,(238,429)0.196
m2_mod3_laplace_n323_d3M2N=323,d=3:q=23,P +=881≤25000.085
m2_mod3_laplace_n1763_d3M2N=1763,d=3:q=29,P +=233≤80000.081
m2_mod3_laplace_n10403_d3M2N=10403,d=3:q=37,P +=3989≤250000.095
m2_mod3_laplace_n1763_d5M2N=1763,d=5:q=47,P +=56489≤600000.198
m3_adic3_sqrt_d3_p2_k3M3d=3, 4 pairs,K=3:max| ˆbj|=270.219
m3_adic3_sqrt_d3_p3_k4M3d=3, 6 pairs,K=4:max| ˆbj|=4083200.209
m3_adic3_sqrt_d5_p2_k4M3d=5, 4 pairs,K=4:max| ˆbj|=470.450
m3_adic3_sqrt_d5_p3_k5M3d=5, 6 pairs,K=5:max| ˆbj|=17612800.547
m4_dixon_split_n323_17x19M417·19: 6 chars,K=5,Y=27,Z=160→190.606
m4_dixon_split_n1763_41x43M441·43: 6 chars, 3-adic roots→430.609
m4_dixon_split_n10403_101x103M4101·103: 6 chars, 3-adic roots→1030.570
m4_dixon_split_n64507_251x257M4251·257: 6 chars, 3-adic roots→2570.607
(272 ≡1602 ≡83 ( mod 323)) andgcd(160 −27,323) =
gcd(133,323) = 19.
3. 16-Certificate Atlas & 74-Test Red-Team Audit
(Table 2, Fig. 3).Table 2 lists all 16 canonical certificates
verified in0.081–0.609 ms. tests/test_suite.py runs 74
pytest checks: 1 full 16-certificate replay, 3 raw-JSON parser
guards (float,NaN, duplicate keys), 2 exact regressions (re-
jecting the 12-base Sorenson–Webster strong pseudoprime
318,665,857,834,031,151,167,461and rejecting non-squares
in F×
3d), and 68 parametrized live adversarial forgeries (12
schema/parser + 13 Mode 1 + 14 Mode 2 + 13 Mode 3 +
16 Mode 4), each asserting an exact regex on its intended
CertificateError branch. scripts/verify_all.py en-
forces all 5 gates including strict axiom whitelisting and a
41-file SHA-256 manifest.
5 Conclusion
We built an independent, explicitly scoped, zero-floating-
point verification companion for the discrete lattice, mod-
3 Laplace ensemble, deterministic 3-adic Newton–Hensel
square-root, blinded Dixon splitting, and strong-induction
mechanisms of the CogenticLN[1/3,105]integer factor-
ization preprint [6, 3], pairing 18 constructive Lean 4.35.0
sub-lemmas (zerosorry, zeroClassical.choice) with the
pure-int/Fraction 4-mode auditor L13FACT-COGENTIC-
CERT-1.0, 16 canonical exact finite witnesses, and 68/68
live adversarial forgery rejections.
References
[1] Manindra Agrawal, Neeraj Kayal, and Nitin Saxena. PRIMES is
in P.Annals of Mathematics, 160(2):781–793, 2004.
[2] J. P. Buhler, H. W. Lenstra, Jr., and Carl Pomerance. Factoring
integers with the number field sieve. InThe Development of the
Number Field Sieve, volume 1554 ofLecture Notes in Mathematics,
pages 50–94. Springer-Verlag, 1993.
[3] Yang Cai, Vishal Gupta, Yiding Jiang, Christopher Liaw, Aranyak
Mehta, Grigoris Velegkas, and Di Wang. Cogentic: Multi-agent
orchestration for automated proof discovery. arXiv preprint
arXiv:2609.40324, 2026.
[4] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem
prover and programming language. InAutomated Deduction –
CADE 28, volume 12699 ofLNCS, pages 625–635. Springer, 2021.
[5] John D. Dixon. Asymptotically fast factorization of integers.
Mathematics of Computation, 36(153):255–260, 1981.
[6] Google Research Cogentic. Unconditional subexponential integer
factorizationintime LN[1/3,105]. UnrefereedCompanionPreprint
(Google Research Cogentic), November 2026. Proposes a uniform
zero-error Las Vegas multitape Turing machine factoring every
integer N≥ 2in expected time LN[1/3,105]and deterministic
spaceL N[1/3,40].
[7] A. K. Lenstra, H. W. Lenstra, Jr., and L. Lovász. Factoring
polynomials with rational coefficients.Mathematische Annalen,
261:515–534, 1982.
[8] H. W. Lenstra, Jr. and Carl Pomerance. A rigorous time bound for
factoring integers.Journal of the American Mathematical Society,
5(3):483–516, 1992.
4
