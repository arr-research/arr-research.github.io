# Certified Verification of Asymptotic (1-epsilon)-MMS Allocations

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5V4TDD4KME94RA75` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/mms-allocations-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `6913830de52e356bb5d1b2fd04b74874269c686fd1fc10473a99528e7d79bac1`

## Abstract

We construct a standalone zero-dependency Lean 4.35.0 formalization of 18 core Abel-summation, prefix-LP duality, checkpoint-rounding, deadline-assignment, small-slack dual-price, M2''-sharing, cyclic-compression, and eta-faithfulness theorems (zero sorry, zero warnings, zero Classical.choice) for Zehan Lin, Shengxin Liu, Biaoshuai Tao, Xiaowei Wu, and Yuhao Zhang (arXiv:2611.33052, Nov 2026), paired with a zero-floating-point exact rational/integer four-mode certificate verifier (MMS-ASYMP-CERT-1.0). Across 16 canonical certificates (0.671-25.122 ms, total 64.84 ms), all exact primal-dual witnesses, Algorithm 3.1 deadline allocations, Lemma A.1 cyclic compressions, Lemma 3.11 fractional sharings, and Appendix B comparison groupings and eta-faithful auxiliary valuations replay deterministically while rejecting 60/60 live adversarial forgery attacks.

## Full Extracted Text

--- Page 1 ---
Certified Verification of Asymptotic(1−ε )-MMS Allocations
Lluis Eriksson∗
November 25, 2026
Abstract
Zehan Lin, Shengxin Liu, Biaoshuai Tao, Xiaowei Wu,
and Yuhao Zhang (arXiv:2611.33052, Nov. 2026) re-
solved Feige and Grinberg’s asymptotic maximin share
(MMS) conjecture, proving that for every fixedε∈ (0,1)
and sufficiently large n, polynomial-time algorithms—
and polynomial bundle-comparison protocols—compute
(1 −ε)-MMS allocations for goods (Thm. 3.1) and(1 +
ε)-MMS allocations for chores (Thm. C.1). We con-
struct a standalone zero-dependencyLean 4.35.0for-
malization of 18 core Abel-summation, prefix-LP du-
ality, checkpoint-rounding, deadline-assignment, small-
slack dual-price,M′′
2 -sharing, cyclic-compression, andη-
faithfulness theorems (zero sorry, zero warnings, zero
Classical.choice) paired with a zero-floating-point ex-
act Q/Z verifier (MMS-ASYMP-CERT-1.0). Across 16 canon-
ical certificates (0.671–25.122 ms, total64.84 ms), all exact
primal-dual witnesses, Algorithm 3.1 deadline allocations,
Lemma A.1 cyclic compressions, Lemma 3.11 fractional
sharings, and Appendix B comparison groupings replay
deterministically while rejecting 60/60 live adversarial
forgery attacks.
1 Introduction
Since Budish introduced the maximin share (MMS) bench-
mark [3] and Kurokawa, Procaccia, and Wang proved exact
MMS can fail forn= 3[ 8], multiplicative approximations
improved via normalization [1] to7 /9-MMS [7], while im-
possibility bounds shrank to1−Ω(1/log 2 n)for large n[5].
Building on Feige and Grinberg’s agent-redundancy theo-
rem [6] and comparison-query fair division [2], Lin et al. [9]
proved that the optimal MMS factor converges to1for
both goods and chores through four discrete pillars:
1. Prefix-Relaxation Configuration LP & Scaled
Dual (Sec. 3.1, 3.3, Def. 3.7, Lem. 3.8):On a
normalized IDO instance with candidate bundle families
Bi (|Bi|≤n +2m), minimizingλsubject to prefix loads
≤λj yields total slack∆ = n(1 −λ)and nonincreasing
dual item pricesp(ek) = ∑m
j=k αj summing ton with∑
i(1 −ζi) = ∆, partitioning agents into ordinaryNo
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with AI
coding, formalization, and drafting assistance from Google Antigrav-
ity; all proofs, exact rational/integer verifiers, and adversarial tests
were independently compiled and verified locally. Repository:https:
//github.com/lluiseriksson/mms-allocations-certificates
and reservedNr (|Nr|L4 ≤n∆) andisolating a common
high-value prefixM1.
2. Large-Slack Checkpoint Rounding & Deadline
Assignment (Alg. 3.1, Lem. 3.4–3.6):When
∆ ≥2R, iterative checkpoint rounding halves the frac-
tional support |F′| ≤ |F|/2while preserving prefix
loads; Step 2 assigns thek-th sorted request to slot
⌈k/λ⌉ ≤j, leaving |U∩M [j]| ≥(1 −λ)j so Abel
summation Eq. (3.1) guaranteesvi(U) ≥∆for Step 3
greedy bag-filling.
3. Small-Slack M′′
2 Sharing, Even/Odd Matching,
& Cyclic Compression (Lem. 3.11, 3.12, A.1):
Cyclic compression mergesm items into ≤2h items
with column values and max-deficit rebalancing errors
≤2n/h; deterministic deadline sharing ofM′′
2 gives
vi(Zi) ≥s ivi(M′′
2 ) −u1; even slots2 j≤b (4j < b)
avoid odd backup positions.
4. Comparison-Query Grouping &η-Faithful Valua-
tions (App. B, Lem. B.2–B.3):Recursive weighted-
median splitting produces≤8kn2 + 1groups retaining
≥(1−1/k)µi, andη-faithful auxiliary valuations satisfy
w(S)≥(1−η)µ(w)⇒v i(S)≥(1−8η)µ i.
Contributions and Scope.We do not formalize asymp-
totic O(·)LP-solver runtimes inside Lean 4; instead, we
machine-check the exact finite algebraic, duality, round-
ing, compression, and faithfulness invariants of [9]: (i) 18
zero-sorry, zero-Classical.choice Lean 4.35.0[4] the-
orems inMMSAsymptotic.lean; (ii) the exactQ/Z verifier
MMS-ASYMP-CERT-1.0; (iii) 16 canonical certificates across
all four modes; and (iv) a 60-attack live red-team suite
with 39-artifact SHA-256 manifest enforcement.
2 Constructive Lean 4.35.0 Kernel
The standalone module MMSAsymptotic.lean
(in lean/) defines exact list primitives sumInt,
subsetSum, abelSumAux/abelSum, NonincNonneg,
PrefixCountLower, allItemsSum, suffixPrices,
weightedSumAux, bundlePrice, dualPrefixAlphaAux,
AllNonneg, and ListNonincNonneg. It compiles under
Lean 4.35.0 in1 .2 swith zero external dependencies,
zero warnings, and zero sorry. Auditing all 18 theo-
rems via #print axioms (AuditAxioms.lean) confirms
all 18 use solely [propext, Quot.sound] and0use
Classical.choiceorLean.ofReduceBool(Table 1).
Proposition 1(Machine-Checked Asymptotic MMS In-
variants).The Lean 4.35.0 kernel establishes the follow-
1

--- Page 2 ---
Table 1: All 18 machine-checked Lean 4.35.0 the-
orems in MMSAsymptotic.lean (zero sorry, zero
Classical.choice).
# Lean Theorem Identifier Paper Ref. Axioms
1abel_prefix_summation_eq31Eq. (3.1)p, Q
2prefix_slack_value_lower_boundLem. 3.6p, Q
3dual_price_sum_eq_weighted_alphaSec. 3.3p, Q
4dual_bundle_price_eq_prefix_alphaSec. 3.3p, Q
5dual_prices_monotone_nonincreasingSec. 3.3p, Q
6weak_duality_prefix_lpSec. 3.3p, Q
7dual_zeta_le_one_from_partitionSec. 3.3p, Q
8reserved_agents_markov_boundDef. 3.7p, Q
9checkpoint_gap_preserved_loadLem. 3.4p, Q
10fractional_support_halving_boundLem. 3.5p, Q
11deadline_ceiling_slot_feasibilityLem. 3.6p, Q
12greedy_bag_filling_sufficient_slackLem. 3.6p, Q
13lemma38_small_item_price_boundLem. 3.8p, Q
14m1_bundle_cardinality_kappa_boundSec. 3.3p, Q
15even_odd_deadline_matching_disjointLem. 3.12p, Q
16m2_fractional_share_value_boundLem. 3.11p, Q
17cyclic_compression_column_boundLem. A.1p, Q
18eta_faithful_auxiliary_boundLem. B.3p, Q
Axiom key:p, Q=[propext, Quot.sound](all 18/18 theorems; 0Classical.choice).
ing universal results over arbitrary finite integer lists and
cleared-denominator bounds:
1. Abel Summation & Scaled LP Duality (Thms. 1–8):
Exact identity∑
j∈S sj = ∑
j |S∩[j]|(sj −sj+1)implies
Dv(U) ≥Nv (M)under prefix densityD|U∩[j]|≥Nj ;
suffix pricesp(ek) = ∑
j≥k αj satisfy ∑p(ek) = ∑jαj,∑|S∩ [j]|αj = p(S), monotonicity, weak duality
D∑ζi ≤DnΛ,nζ≤n, and|N r|L4 ≤n∆.
2. Rounding, Sharing, Compression, & Faithfulness
(Thms. 9–18):Checkpoint gaps preserve λj;4 C≤
F∧ 2F′ ≤ 2C + F′ ⇒ 2F′ ≤F ; ceiling slots
(kq + p− 1)/p satisfy ≤j and strict monotonicity;
greedy bag-filling leaves > σ; Lemma 3.8 segment
prices sum to ≤K (p(B) −ζ )and |Pi
j ∩M 1|< κ ;
4j < b⇒ 2j≤b∧ 2j̸ = 2 r + 1; M′′
2 -sharing
achieves Dv(Z) ≥Nv (M′′
2 ) −Du 1; cyclic columns
obey hv(Ck) ≤2n; and η-faithfulness guaranteesp≥
µ(w)−2ηandw(S)≥p−2η.
3 ExactQ/ZCertificate Verifier
The verifier MMS-ASYMP-CERT-1.0
(src/mms_certifier.py, src/mms_exact.py) uses
pure Python int and fractions.Fraction exclusively
(source-audited for zerofloat(, math., ornumpy). Every
payload enforces strict JSON typing (rejecting floats,
bool-as-int, int-as-bool), canonical reduced rationals
(forbidding "-0" and "/1"), nesting-depth cap32, full
ASCII control-character filtering, 2048-bit integer caps,
and exact container/key validation across four modes:
1. Mode 1 (Sec. 3.1, 3.3, Def. 3.7, Lem. 3.8 Primal-
Dual Audit):Builds exact 3-type candidate fami-
lies Bi, checks primal prefix loads ≤λj , dual suf-
fix prices p(ek), strong duality∑
i ζi = nλ,( No,Nr)
Markov bound, prefix M1, and Eq. (3.2) small-item
price bounds.
2. Mode 2 (Alg. 3.1 & Lem. 3.6 Large-Slack Dead-
Figure 1: (a) Exact Lemma A.1 cyclic compression max
column value and max rebalancing deficit versus2n/h
across h∈ {4,6,..., 14}(n = 4 ,m = 40). (b) Exact
Lemma 3.11 M′′
2 fractional-sharing shortfall and safety
margin versus ceilingu1 = 1/5acrossℓ∈{6,9,...,24}.
line Allocation):Checks integral prefix loads≤λj ,
replays Step 2 ceiling slots⌈k/λ⌉, verifies Abel iden-
tity Eq. (3.1)vi(U) ≥∆, and replays Step 3 greedy
bag-filling to certify a completeσ-MMS allocation.
3. Mode 3 (Lem. A.1 Compression & Lem. 3.11
M′′
2 Sharing):Replays cyclic compression into≤2h
items and max-deficit rebalancing (|δj|≤ 2n/h), plus
deterministic ⌊sib⌋-deadline sharing certifyingvi(Zi) ≥
sivi(M′′
2 )−u 1.
4. Mode 4 (Lem. B.2 Grouping & Lem. B.3 η-
Faithfulness):Replays recursive weighted-median
splitting (≤8kn2 + 1groups, grouped MMS ≥(1 −
1/k)µi) and exhaustively audits all2m bundles forη-
faithfulness (w(S) ≥(1−η)µ(w) ⇒vi(S) ≥(1−8η)µi).
4 Empirical Atlas and Red-Team
Audit
Running run_all_experiments.py generates 16 canon-
ical certificates (4 per mode) and four exact datasets,
audited end-to-end byverify_all.py with SHA-256 ver-
ification across all 39 tracked artifacts.
Compression & M′′
2 Sharing (Fig. 1).Mode 3
(0.671–1.616 ms) certifies cyclic compression acrossm∈
{15,24,32,10} → {8,12,16,10} with max column
values3 /8,1/3,21/55,0and max rebalancing deficits
1/8,1/9,0,0, all strictly below2n/h∈{ 3/2,4/3,1,6/5}.
Across h= 4 ... 14on m= 40, max column value decays
from4 /5to1 /6while max deficit stays ≤1/6. On M′′
2
sharing (ℓ= 6 ... 24, u1 = 1/5), exact shortfalls remain be-
tween0 .0239and0 .0686, keeping safety margins≥0.1314
abovesiv(M′′
2 )−u 1.
LP Duality, Deadline Allocation, & Comparison
Grouping (Fig. 2).Mode 1 (0 .871–1.316 ms) certifies
exact strong duality across zero-slack (λ = 1 ,∆ = 0),
large-slack (λ = 2/3,∆ = 4/3), Lemma 3.8M1/M2 sep-
aration (|M1| = 4 ,p(M2) = 0 ,v(M2) = 2 /5), and an
ordinary/reserved split (|No|= 3,|Nr|= 1,λ = 3/4,∆ =
1). Mode 2 (1.011–2.348 ms) replays Algorithm 3.1 for
2

--- Page 3 ---
Figure 2: (a) Exact Lemma B.2 weighted-median grouping
MMS retention ratio versus theoretical floor1−1/kacross
k∈ {1,..., 5}(m = 14). (b) Exact total slack∆ =
n(1−λ)and optimal λacross all eight Mode 1 and Mode 2
certificates.
Figure 3: (a) ExactQ/Z replay latency (0.671–25.122 ms)
across all 16 canonicalMMS-ASYMP-CERT-1.0 certificates.
(b) Live adversarial red-team audit rejecting 60/60 forged
payloads across all five categories.
λ∈{ 2/3,1/2,3/5}(∆ ∈{2,3}), serving 1–2 unserved
agents by greedy bag-filling to achieve exact σ-MMS
(minvi(Xi) ∈{2/3,3/4}). Mode 4 (2.088–25.122 ms) cer-
tifies Lemma B.2 groupings (8–14groups, nonsingleton
ratios ≤2/7) and exhaustively verifiesη-faithfulness for
η∈{ 1/20,1/24,1/32,1/40}across35–209qualifying bun-
dles.
Replay Latency and 60/60 Red-Team Audit
(Fig. 3).All 16 canonical certificates replay deter-
ministically in0 .671–25.122 ms (total64 .84 ms). The
live adversarial suite (tests/test_suite.py) tests 60
targeted forgeries—12 global schema/typing/canonical-
rational/depth/control-char attacks plus 12 domain at-
tacks per mode (IDO violations, unnormalized partitions,
non-Bi bundles, broken strong duality, prefix-load over-
flows, forged leftover pools,h < n, ∑si > 1, corrupted
weighted-median groups,η≥ 1/16, int-as-bool flags, and
unfaithful auxiliary valuations)—achieving60/60 (100%)
rejection.
5 Conclusion
We delivered a standalone, zero-floating-point verification
framework for Lin et al.’s asymptotic(1−ε)-MMS the-
ory [9], combining 18 zero-sorry, zero-Classical.choice
Lean 4.35.0 theorems with the exact Q/Z verifier
MMS-ASYMP-CERT-1.0, 16 canonical certificates, and 60/60
live adversarial forgery rejections.
References
[1] Hannaneh Akrami, Jugal Garg, Eklavya Sharma, and
Setareh Taki. Simplification and improvement of MMS
approximation. InProceedings of the 32nd Interna-
tional Joint Conference on Artificial Intelligence (IJ-
CAI), pages 2485–2493, 2023.
[2] Xiaolin Bu, Zihao Li, Shengxin Liu, Jiaxin Song, and
Biaoshuai Tao. Logarithmic comparison-based query
complexity for fair division of indivisible goods. InWeb
and Internet Economics (WINE 2024), volume 15534
ofLecture Notes in Computer Science, pages 348–365.
Springer, 2024.
[3] Eric Budish. The combinatorial assignment problem:
Approximate competitive equilibrium from equal in-
comes.Journal of Political Economy, 119(6):1061–1103,
2011.
[4] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, volume 12699 ofLecture
Notes in Computer Science, pages 625–635. Springer,
2021.
[5] Tomer Ezra and Tamar Garbuz. Improved im-
possibility bounds for maximin share allocations.
arXiv:2609.15085 [cs.GT], 2026.
[6] Uriel Feige and Vadim Grinberg. Almost-MMS alloca-
tions with small agent redundancy. arXiv:2611.05360
[cs.GT], 2026.
[7] Xin Huang and Shengwei Zhou. A strongly polynomial-
time7 /9-approximation algorithm for maximin share
allocations. arXiv:2511.13056 [cs.GT], 2026.
[8] David Kurokawa, Ariel D. Procaccia, and Junxing
Wang. Fair enough: Guaranteeing approximate max-
imin shares.Journal of the ACM, 65(2):8:1–8:27, 2018.
[9] Zehan Lin, Shengxin Liu, Biaoshuai Tao, Xiaowei
Wu, and Yuhao Zhang.(1 −ε )-MMS allocations.
arXiv:2611.33052 [cs.GT], November 2026.
3
