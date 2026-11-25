# Constructive Lean 4 Formalization and Exact-Rational Certificates for Query-Sample Tradeoffs in Revenue Maximization

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-78692NDYXK8B3R6S` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/revenue-query-sample-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `b5dd01c7537f98deff88bbf03713c9485703f16e3b7ff0f3d9441ba4ee967b5c`

## Abstract

Yaonan Jin, Wei Tang, Yifan Wang, and Mengxiao Zhang (arXiv:2611.31982, Nov. 2026) established tight query-sample tradeoffs for (1-epsilon)-approximate monopoly revenue maximization across MHR, quasi-MHR, regular, and quasi-regular valuation families. We present a standalone, zero-dependency Lean 4.35.0 formalization (RevenueTradeoff.lean) of 18 core algebraic, structural, and cleared-integer theorems spanning all four families plus Appendix A multiplicative-DKW Bernstein optimization and Appendix B quantile-cutoff revenue retention (0 sorry, 0 warnings, 0 Classical.choice), paired with a zero-floating-point exact-Q certificate auditor (REV-TRADEOFF-CERT-1.0). Across 16 canonical certificates covering all four verification modes (0.298-0.663 ms exact replay latency), every tent join, concave ternary discard inequality, hard-distribution chi-squared KL bound, C^1 convex hazard bump, and Bernstein exponent identity replays identically while rejecting 60/60 live adversarial forgery attacks.

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Formalization and Exact-Rational
Certificates for Query-Sample Tradeoffs in Revenue
Maximization
Lluis Eriksson∗
November 25, 2026
Abstract
Yaonan Jin, Wei Tang, Yifan Wang, and Mengxiao Zhang
(arXiv:2611.31982, Nov. 2026) established tight query-
sample tradeoffs for(1 −ε)-approximate monopoly rev-
enue maximization across all four standard valuation fam-
ilies: MHR (L-shaped corner atS = Θ(ε−3/2 log(1/δ)),
Q = Θ(ε−2 log(1/δ))), quasi-MHR (continuous slope-−1
frontier S·Q = Θ(ε−4 log2(1/δ))for c∈ [0,1]), regular (L-
shaped corner atΘ(ε−3 log(1/δ))), and quasi-regular (loga-
rithmic boundary separatingQ= Θ(ε−3 log(1/ε) log(1/δ))
from S = Θ( ε−3 log(1/δ))). We present a stan-
dalone, zero-dependencyLean 4.35.0formalization
(RevenueTradeoff.lean) of 18 core algebraic, structural,
and cleared-integer theorems spanning all four families plus
Appendix A’s multiplicative-accuracy DKW Bernstein
optimization and Appendix B’s quantile-cutoff revenue
retention (0sorry, 0 warnings, 0Classical.choice, ev-
ery theorem audited to[propext, Quot.sound]), paired
with a zero-floating-point exact- Q certificate auditor
(REV-TRADEOFF-CERT-1.0). Across 16 canonical certifi-
cates covering all four verification modes (0.298–0.663 ms
exact replay latency), every tent continuity join, concave
ternary discard inequality, hard-distributionχ2 KL bound,
C1 convex hazard bump, and Bernstein exponent identity
replays identically while rejecting 60/60 live adversarial
forgery attacks (plus 2 raw IEEE-754/NaN parser rejec-
tions).
1 Introduction
Learning an approximately optimal posted price from
buyer feedback is foundational in algorithmic pricing [3, 4].
Jin, Tang, Wang, and Zhang [4] unified two classic feedback
models—exact buyer value samples (S) and binary posted-
price purchase queries (Q)—across the four-family valu-
ation poset (MHR⊂Quasi-MHR⊂Quasi-Regular and
MHR⊂Regular⊂Quasi-Regular , withQuasi-MHR and
∗Independent Researcher. Code, Lean 4 proofs, and certifi-
cates: MIT License; manuscript and figures: CC-BY-4.0. Pre-
pared with transparent AI coding, formalization, and drafting assis-
tance via Google Antigravity; all Lean 4 theorems, exact rational
verifiers, and adversarial tests were independently compiled and
verified locally. Repository: https://github.com/lluiseriksson/
revenue-query-sample-certificates.
Regular incomparable), revealing sharp qualitative distinc-
tions across their(α,β)Pareto frontiers whereS = ˜Θ(ε−α)
andQ= ˜Θ(ε−β):
1. Quasi-Regular (Thm. 11, Lem. 12–14, Thm. 36):
A multi-alternative tent perturbation on q∈ [(i−
1)/K,i/K]with harmonic weights wi = 1/i enforces
32(L+ 1)2E[S] + E[T] ≥1
2 K3Wlog (1/δ), proving that
S≤O (ε−(3−c) log(1/δ))cannot remove the log(1/ε)
factor fromQ= Ω(ε −3 log(1/ε) log(1/δ)).
2. Regular (Thms. 15–16, Lem. 17):Noisy concave
ternary search eliminates thelog(1/ε)factor via a single-
discard concavity boundD≤ 4d≤ 8ζˆr∗(ζ = ε/1000),
matched by a two-distribution hard pair(F(0),F(1))
withB= 1−6ε,u=B/(6ε), andC= 2 −17.
3. Quasi-MHR (Thms. 20–21, Lem. 22–24):Sample-
based bin sparsification and aK = Θ( ε−c)disjoint-
interval lower-bound family on[5/4,3/2]( w= 1/(8K),
ρ= 16Kε) yield the exact continuous tradeoff(2−c) +
(2 +c) = 4forc∈[0,1](A= 100,C= 2 −12/100).
4. MHR & Multiplicative DKW (Thms. 27, 31,
Lem. 28–30):A C1 piecewise-quadratic cumulative-
hazard bump ψ(t)of width d = 10 √ε maintains
convexity1 + ψ′′ ≥ 1/2, separates optimal prices
by 8
3 ε >log (1/(1 −ε )), and yields A = 15 ·104,
C = 1/(32A), while Appendix A’s reverse-martingale
DKW bound optimizesλ=nqε ′/(1 +ε′/3).
Contributions and Explicit Scope.We do
notformalize measure-theoretic probability, Bern-
stein/Chernoff/Doob tail inequalities, or Median
Elimination [2]/DKW [5] convergence inside Lean 4;
all probabilistic theorems belong to [4]. Instead, we
machine-check and exactly audit every deterministic
algebraic, convexity, continuity, separation,χ2-divergence,
and tradeoff-exponent pillar of [4]: (i) 18 zero- sorry,
zero-Classical.choice Lean 4.35.0[ 1] theorems
in RevenueTradeoff.lean; (ii) the pure- Q/Z verifier
REV-TRADEOFF-CERT-1.0; (iii) 16 canonical certificates
across all four modes plus quantitative frontier and
χ2-tightness profiles; and (iv) a 60-attack live red-team
suite (plus 2 raw JSON parser tests) with SHA-256
manifest locking.
1

--- Page 2 ---
2 Constructive Lean 4.35.0 Kernel
The standalone module lean/RevenueTradeoff.lean
compiles under Lean 4.35.0 with zero external de-
pendencies, zero warnings, and zero sorry. Run-
ning lean/AuditAxioms.lean verifies all 18 theorems
depend strictly on [propext, Quot.sound] with0
Classical.choice and0 Lean.ofReduceBool (Table 1).
Proposition 1(Machine-Checked Core Invariants).
Every theorem in Table 1 is constructively proved
in RevenueTradeoff.lean over exact integers without
floating-point or classical choice:
1. Quasi-Regularity & Tent Family (Thms. 1–7):Clearing
common denominator D >0proves pQp(D−Qs) ≤
sQs(D−Qp) ⇒D (pQp−sQs) ≤QsQp(p−s)(Lem. 6)
and exact cutoff retention a≤Q ˜pand D˜pQ˜p ≥
(D−a)R (Thm. 36 Eq. (9)). Theorems 3–7 certify the
tent joins at4 K and peak4 K+1, strict positivity of
both R(i)
qt (q)/(1−q)slope coefficients,(1 −ε)(1+2ε) >1,
(1−x)−2−1 ≤3x for0 ≤x≤ 1
8 , and weighted-KL
half-budget transferMW≤2T.
2. Regular Concave Search & Pair (Thms. 8–11):The-
orem 8 proves that under64 ζ≤ 1, rℓ ≥ 1
4 ˆr∗,
0 ≤d≤ 2ζˆr∗, trisection ratios ≤ 2,4, and con-
cavity D(rℓ∆x−d ∆xh) ≤dr ℓ∆xℓ, the first discard
loses at most D≤ 4d≤ 8ζˆr∗; Theorem 9 gives
(1−ε
16 ) −11 ε
1000 = 1 − 147
2000 ε >1 −ε; Theorems 10–
11 certify exact branch continuityQ0(u) = Q1(u) = 6ε
andC= 2 −17.
3. Quasi-MHR, MHR, & Multiplicative DKW (Thms. 12–
18):Theorems 12–14 certify(1 −ε)(1+4
3 ε) > 1, A =
100, C = 2 −12/100, and(2 −c) + (2+c) = 4. Theo-
rems 15–17 certifyC0/C1 joins and convexity1+ψ′′≥
1
2 of the MHR bumpψ, the exact disjointness margin
8
3 ε > 2ε, and A = 15 ·104, C = 1 /(32A). Theo-
rem 18 proves the exact optimal Bernstein cancellation
−λε′+ λ2
2nq(1−λ/(3nq)) =− nq(ε′)2
2(1+ε′/3) .
3 Exact-Rational Verifier Architec-
ture
The pure-stdlib verifier REV-TRADEOFF-CERT-1.0
(src/revenue_exact.py, src/revenue_certifier.py)
computes exclusively with Python int and
fractions.Fraction (source-audited for zero float(,
math., or numpy). Its parser rejects IEEE-754 JSON
tokens andNaN/Infinity, non-ASCII/Unicode digits (via
isascii() and isdigit()), unreduced or leading-zero
rationals, -0, booleans-as-integers, unknown keys, and
nesting depth>20across four exact modes:
Definition 1(FourREV-TRADEOFF-CERT-1.0Modes).
1. Mode 1( quasi_regular_tent_cert): Recomputes
exact tent joins, R(i)
qt (q)/(1−q)continuity, peak sep-
aration(1 −ε)(1+ 1
4K) > 1, harmonic weight W =
Figure 1: (a) Four-family query-sample Pareto frontiers in
(α,β)exponent space (S = ˜Θ(ε−α), Q= ˜Θ(ε−β)). (b) Ex-
act rational quasi-MHR conservation(2−c) + (2+c) = 4
acrossc∈{0, 1
8 ,...,1}.
∑L+1
i=2 1/i≥ 1, Lemma 13 density shift|z(p)|≤ 3i
2K ≤
1
2 , and Lemma 14 Bernoulliχ2(Q0∥Qi)≤ i
8K3 .
2. Mode 2( regular_ternary_and_pair_cert): Inde-
pendently checks monotonicity and concavity of a
rational( q,R)grid, verifies both keep_right and
keep_left Theorem 15 discard boundsD≤ 4d≤ 8ζˆr∗,
checks Q0(u) = Q1(u) = 6 ε, and verifies Lemma 17
queryχ 2(Q0∥Q1)≤2 12ε3 for probesp>u.
3. Mode 3( quasi_mhr_tradeoff_family_cert): Au-
dits[5 /4,3/2]interval packing, ρw = 2 ε, ρ≤ 1
4 ,
(2−c) + (2 +c) = 4, peak revenue1 +2ε
ai
≥ 1+4
3 ε,
Lemma 23 density shift and sample KL ≤ 100Kε2,
and Lemma 24 queryχ2 ≤100ε2.
4. Mode 4(mhr_hazard_bump_and_dkw_cert): Audits
C0/C1 knots and convexity ofψ(t)across[ −2,4], ex-
act margin 8
3 ε, Lemma 30χ2 constant 225
16 ≤15, and
Theorem 31 Bernsteinλopt and exponent identity.
4 Empirical Atlas and Red-Team
Audit
Running scripts/run_all_experiments.py determin-
istically generates 16 canonical certificates (4 per
mode) and 4 experiment JSONs, audited end-to-end
by scripts/verify_all.py with SHA-256 verification
across all 39 tracked repository files.
1. Four-Family Frontiers & Exact KL Tight-
ness (Figs. 1–2).Figure 1 contrasts the L-shaped
MHR(3 /2,2)and regular(3 ,3)corners against the
quasi-MHR continuous tradeoff S·Q = ˜Θ(ε−4)and
the quasi-regular log(1/ε)boundary. Across tent scales
K∈{ 24,48,96,192,384}(L= 5K/24), exact rational har-
monic sums grow fromW = 29
20 = 1.45to W≈ 3.978, while
the exact midpoint queryχ2(Q0∥Qi)tracks Lemma 14’s
i/(8K3)bound at a tight, stable ratio of0.1693 →0.1587
(Fig. 2(a)); similarly, the regular hard pair’s queryχ2
at p = 2 u tracks Lemma 17’s2 12ε3 bound at ratio
0.0341 →0.0270across ε−1 ∈{48,..., 512}. Figure 2(b)
plots theC1 convex MHR bumpψ(t)and derivative ψ′(t),
highlighting the exact disjointness stepψ(1
5 ) −ψ(1
3 ) = 22
225
yielding the 8
3 εgap.
2

--- Page 3 ---
Table 1: All 18 Lean 4.35.0 theorems inRevenueTradeoff.lean (0 sorry, 0 warnings, 0Classical.choice; every
theorem audited to[propext, Quot.sound]).
# Lean 4 Theorem Identifier Paper Ref. & Cleared Statement
1quasi_regular_inverse_revenue_monotoneLem. 6:pQ p(D−Qs)≤sQ s(D−Qp)⇒D(pQ p−sQs)≤Q sQp(p−s)
2quasi_regular_quantile_cutoff_retentionThm. 36(9):Da˜p= (D−a)R⇒a≤Q ˜p∧(D−a)R≤D˜pQ ˜p
3quasi_regular_tent_continuity_and_peakLem. 12: tent joins4K, peak4K+1,p i,∗qi,∗= (4K+1)/(4K)
4quasi_regular_tent_monotonicity_coeffsLem. 12:1≤i≤K⇒3K−(i−1)>0∧K+i>0
5quasi_regular_good_price_separationSec. 3.4:0<2n<d⇒d 2 <(d−n)(d+2n)
6quasi_regular_density_ratio_boundLem. 13:0≤8a≤b⇒b(b 2−(b−a)2)≤3a(b−a) 2
7quasi_regular_weighted_kl_aggregationThm. 11:
∑L+1
i=2 i≤(L+1) 2 &64(L+1) 2S≤M⇒MW≤2T
8regular_concave_ternary_discard_boundThm. 15:64z≤Z,dZ≤2zR,R≤4r ℓ,concavity⇒D≤4d
9regular_ternary_final_revenue_guaranteeThm. 15:2000(d−n)<2000d−147nforn>0
10regular_hard_pair_branch_identityThm. 16:u−B= (d−n) 2/(nd)&Q 0(u) =Q1(u) =n/d
11regular_query_kl_constantsLem. 17/Thm. 16:576·6≤4096,512·32≤2 17 = 32·4096
12quasi_mhr_good_price_separationThm. 21:0<4n<d⇒3d 2 <(d−n)(3d+4n)
13quasi_mhr_kl_constantsLem. 23–24:72·32≤100·25,400≤900,128·32 = 4096
14quasi_mhr_tradeoff_exponent_sumThms. 20–21:(2−c) + (2+c) = 4,1≤2−c≤2+c≤3
15mhr_hazard_bump_c1_joins_and_convexityLem. 28:ψ∈C 1 at{−2,0,2,4},ψ(1) =−3/2,1+ψ ′′≥1/2
16mhr_good_price_disjointness_marginSec. 6.4:ψ(1/5)−ψ(1/3) = 22/225,100((22−16)/225) = 8/3>2
17mhr_query_kl_constantsLem. 30/Thm. 27:225≤15·16,15·10 4 =A,2·16 = 32
18multiplicative_dkw_bernstein_exponent_optThm. 31:λ<3M,1−λ/(3M) = 3e d/(3ed+en), quad. cancel
Figure 2: (a) Exact midpoint Bernoulliχ2(Q0∥Qi)versus
Lemma 14 upper boundi/(8K3)across K∈{ 24,..., 384}
(ratio0 .169 →0.159). (b) Exact MHR C1 convex haz-
ard bumpψ(t)and derivative ψ′(t)(Lemma 28) showing
ψ( 1
5 )−ψ( 1
3 ) = 22
225 .
2. 16-Certificate Atlas & 60/60 Red-Team Suite
(Table 2, Fig. 3).All 16 canonical certificates replay
in0 .298–0.663 ms (total6 .41 ms) with zero floats. In
tests/test_suite.py, 60 targeted live forgery attacks—
16 AST/schema/canonical-rational/Unicode-digit attacks
(including superscript-2U+00B2 and Arabic-Indic-8U+0668
digits plus depth-21 DoS) and 11 domain-specific attacks
per mode (tent corners, non-concave grids, invalid discard
branches, wrong constantsA,C, out-of-interval probes,
and wrong Bernstein exponents)—plus 2 raw JSON IEEE-
754/NaN file rejections achieve60/60 (100%)red-team
rejection (63/63pytestchecks passing).
5 Conclusion
We delivered a self-contained, zero-floating-point verifi-
cation suite for Jin, Tang, Wang, and Zhang’s query-
sample revenue maximization tradeoffs [4], pairing 18
zero-sorry, zero-Classical.choice Lean 4.35.0 theorems
with the exact-Q auditor REV-TRADEOFF-CERT-1.0, 16
sub-millisecond canonical certificates, and 60/60 live ad-
Figure 3: (a) Zero-float replay latency across all 16 canoni-
cal REV-TRADEOFF-CERT-1.0 certificates (0.298–0.663 ms).
(b) 60/60 live adversarial forgery rejections across global
AST/Unicode and Modes 1–4.
versarial forgery rejections.
References
[1] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, pages 625–635, 2021.
[2] Eyal Even-Dar, Shie Mannor, and Yishay Mansour. Ac-
tion elimination and stopping conditions for the multi-
armed bandit and reinforcement learning problems.
Journal of Machine Learning Research, 7:1079–1105,
2006.
[3] Zhiyi Huang, Yishay Mansour, and Tim Roughgarden.
Making the most of your samples.SIAM Journal on
Computing, 47(3):651–674, 2018.
[4] Yaonan Jin, Wei Tang, Yifan Wang, and Mengxiao
Zhang. Query-sample tradeoffs for revenue maximiza-
tion. arXiv:2611.31982 [cs.GT], November 2026.
3

--- Page 4 ---
Table 2: Summary of all 16 exact- Q
REV-TRADEOFF-CERT-1.0 certificates (zero IEEE-754
arithmetic; 20-run mean replay latency in ms).
Certificate Stem Mode Exact Certified Witness ms
qr_tent_K24_L5M1K=24,L=5,W= 2920, peak9796 0.376
qr_tent_K48_L10M1K=48,L=10,W≈2.020, peak193192 0.375
qr_tent_K96_L20M1K=96,L=20,W≈2.645, peak385384 0.398
qr_tent_K192_L40M1K=192,L=40,W≈3.303, peak769768 0.417
reg_pair_eps48_rightM2ε=148,u=7,D=1192000, right 0.298
reg_pair_eps64_leftM2ε=164,u=293 ,D= 1256000, left 0.302
reg_pair_eps128_rightM2ε=1128,u=613 ,D= 1512000, right 0.311
reg_pair_eps256_leftM2ε=1256,u=1253 ,D= 11024000, left 0.304
qmhr_slope_c0_sampleM3c=0,K=2,(α,β) = (2,2)0.454
qmhr_slope_c1_3_midM3c=13,K=4,(α,β) = (53,73)0.613
qmhr_slope_c1_2_balM3c=12,K=8,(α,β) = (32,52)0.648
qmhr_slope_c1_queryM3c=1,K=64,(α,β) = (1,3)0.663
mhr_bump_d8_dkw1M4d= 18,margin12400, DKW−1516 0.306
mhr_bump_d10_dkw2M4d= 110,margin13750, DKW−3751568 0.325
mhr_bump_d16_dkw3M4d= 116,margin19600, DKW−3756208 0.303
mhr_bump_d20_dkw4M4d= 120,margin115000, DKW−37524704 0.320
[5] Pascal Massart. The tight constant in the dvoretzky–
kiefer–wolfowitz inequality.The Annals of Probability,
18(3):1269–1283, 1990.
4
