# Exponential Bit-Complexity Tightening, Optimal b-ary Matching Trees, and Exact Sharp Support Thresholds for Normal-Form Correlated Equilibria in Extensive-Form Games

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5X7XQPHX8J8NCS54` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/extensive-form-nfce-sharp-gap-and-hardness (`v1.0.0`)  
**Canonical PDF SHA-256:** `ef5eab65c20149a2892c362c99ad2de40f2b0c55760f4e1a120a72a19857c697`

## Abstract

We establish three sharp structural, complexity-theoretic, and combinatorial advances over the recent PPAD-completeness proof for exact Normal-Form Correlated Equilibria (NFCE) in perfect-recall extensive-form games by Cheval, Horn, Paul, and Shirmohammadi (arXiv:2611.34897v1). First (Theorem 1), by exploiting active-support sparsity (eliminating zero-weight columns at optimal vertices), keeping the probability-simplex row unscaled, and replacing the raw payoff/chance denominator product B with per-player leaf-payoff least common multiples D_i, we sharpen the uniform rational LP reweighting gap of Lemma 14 from ((K+1)B)^{-(K+1)} to (sqrt(K) (K+1)^{K/2} D_max^K)^{-1}. This saves more than (K/2) log_2(K+1) + K log_2(B/D_max) bits of oracle precision (yielding >30x bit reduction on the authors' matching-tree instances at r=8, q=10), while proving exact two-player support dominance K - kappa_d = d_1^2 + d_2^2 - d_1 d_2 >= (d_1^2 + d_2^2)/2 (a 2x balanced reduction). Second (Theorem 2), generalizing the binary matching branch to arbitrary b-ary perfect-recall trees M_b(k) (m = b^k) shows that sequence-form dimensions d_1 = d_2 = m + r - 2 are invariant of b while node overhead f(b) = b + 2 + 2/(b-1) = 6 + (b-2)(b-3)/(b-1) achieves its unique integer minimum f(b) = 6 if and only if b in {2, 3}. This proves that the 1/36 node-quadratic constant of Corollary 20 is sharp across all b-ary matching trees, and that ternary trees (b=3) match the optimal node count 6m + r^2 + r - 3 while exponentially shrinking the pure-strategy space from r 2^{m-1} to r 3^{(m-1)/2} (over 10^{15}x smaller at m=243). Third (Theorem 3), we sharpen the PPAD-hardness matching-tree sizes by >=8x in the dimension-based reduction (m > r^2(r-1) vs 8r^3) and 32x-64x in the node-based reduction (m > r^2(r^2+r-3)/6 vs 8r^4), integrate the Kullback-Csiszar-Kemperman refined Pinsker bound, and prove an exact minimum-support dichotomy: an exact NFCE of support m^2 exists on Gamma_b(P,Q,k) if and only if (P,Q) admits an exact Nash equilibrium with probabilities in (1/m) Z, yielding a constructive ternary-vs-binary separation on an asymmetric 2x2 game with unique Nash equilibrium (2/3,1/3) x (1/3,2/3). All algebraic and combinatorial cores are formalized constructively in zero-dependency Lean 4.35.0 (18 theorems, 0 sorry, 0 Classical.choice) and verified by an AST-audited zero-float Python verifier issuing 16 SHA-256 certificates.

## Full Extracted Text

--- Page 1 ---
Exponential Bit-Complexity Tightening, Optimalb-ary
Matching Trees, and Exact Sharp Support Thresholds
for
Normal-Form Correlated Equilibria in Extensive-Form
Games
Lluis Eriksson∗
November 26, 2026
Abstract
In a recent breakthrough, Cheval, Horn, Paul, and Shirmohammadi (arXiv:2611.3
4897v1 ) proved that computing an exact Normal-Form Correlated Equilibrium (NFCE)
of quadratic support size in a perfect-recall extensive-form game belongs to PPAD, and
that the prescribed-support exact search problems for two players under dimension-based
(κd = (d1 + 1)(d2 + 1)) and node-based (κV = ⌊|V|2/36⌋) support caps are PPAD-complete.
We establish three sharp structural, complexity-theoretic, and combinatorial advances over
this framework. First (Theorem 1), by eliminating zero-weight columns at optimal LP
vertices, leaving the probability-simplex row unscaled, and replacing the raw payoff/chance
denominator productB = ∏
r∈R den(r)with per-player leaf-payoff least common multiples
Di = lcmz∈Z den(pc(z)ui(z)), we tighten the uniform rational LP reweighting gap of Lemma 14
from(( K + 1)B)−(K+1) to(
√
K(K + 1)K/2DK
max)−1. This saves more than K
2 log2(K +
1) + Klog 2(B/Dmax)bits of weak-Nash oracle precision (> 30×fewer bits on the authors’
matching-tree instances atr= 8,q = 10), while certifying exact two-player support dominance
K−κ d = d2
1 + d2
2 −d1d2 ≥ 1
2 (d2
1 + d2
2)(2 ×balanced reduction). Second (Theorem 2),
generalizing the binary matching branch to arbitraryb-ary perfect-recall treesMb(k)( m= bk)
shows that sequence-form dimensionsd1 = d2 = m+ r− 2are invariant of b while node
overhead f(b) = b+ 2 + 2
b−1 = 6 + (b−2)(b−3)
b−1 achieves its unique integer minimumf(b) = 6if
and only ifb∈{ 2,3}. This proves that Corollary 20’s1/36node-quadratic constant is exact
and unimprovable across allb-ary matching trees, and that ternary trees (b= 3) achieve the
identical minimal node count6m+ r2 + r−3while exponentially reducing the pure-strategy
space fromr2m−1 to r3(m−1)/2 (>1015×smaller atm= 243). Third (Theorem 3), we shrink
the PPAD-hardness matching trees by≥8×in the dimension-based reduction (m>r 2(r−1)vs.
8r3) and32×–64×in the node-based reduction (m>r 2(r2 + r−3)/6vs.8 r4), incorporate the
Kullback–Csiszár–Kemperman refined Pinsker bound, and prove an exact minimum-support
dichotomy: an exact NFCE of supportm2 exists onΓ b(P,Q,k )if and only if(P,Q)admits
an exact Nash equilibrium with probabilities in1
mZ, separating ternary from binary trees on
an explicit asymmetric2×2game G1/3. All algebraic and combinatorial cores are formalized
constructively in zero-dependency Lean 4.35.0 (18theorems,0 sorry,0 Classical.choice)
and verified by an AST-audited zero-float Python verifier issuing16SHA-256 certificates.
∗Independent researcher. Authored by Lluis Eriksson with AI-assisted formal verification, exact-arithmetic
software generation, and mathematical drafting (Google Antigravity). Manuscript and figures licensed CC-
BY-4.0; verification repository, Lean 4 formalization, and exact rational certificates licensed MIT athttps:
//github.com/lluiseriksson/extensive-form-nfce-sharp-gap-and-hardness.
1

--- Page 2 ---
1 Introduction
Normal-Form Correlated Equilibrium (NFCE) in extensive-form games [2] requires obedience with
respect to full normal-form strategy plans chosen prior to play, making its equilibrium polytope
exponentially large in the game tree. In [1], Cheval, Horn, Paul, and Shirmohammadi resolved a
major open problem by placing exact NFCE computation in PPAD [3, 4] via a three-stage pipeline:
(i) compute a weakϵΓ-Nash equilibrium via a PPAD oracle; (ii) compress its realization-equivalent
product into a supportS of size at mostK = 1 + ∑n
i=1 di(di + 1)using Carathéodory’s theorem
on the feature-expectation polytope; and (iii) solve a compact sequence-form reweighting LP [5, 6]
at t= 0, guaranteed feasible wheneverϵΓ <η where η= ((K+ 1)B)−(K+1) is a uniform rational
vertex gap (Lemma 14 / Theorem 6). For two players, they further establish PPAD-completeness
under quadratic support capsκd = (d1 + 1)(d2 + 1)and κV = ⌊|V|2/36⌋using a public-coin
reduction combining anr×rbimatrix game(P,Q)with a binary matching treeM(m= 2 k).
This work establishes sharp quantitative and structural improvements across every stage of [1]
(summarized in Table 1):
1. Active-support LCM–Hadamard LP-gap tightening (Section 2):Replacing B
by per-player LCMs Di and exploiting active-support sparsity eliminates a full factor
(K+ 1)B, takes the square root of the(K+ 1)K factor, and yields an unboundedly growing
multiplicative bit-precision reduction on the matching-tree family itself.
2. Optimal b-ary matching trees and sharpness of1/36(Section 3):Analyzing general
b-ary matching treesMb(k)proves that b∈{ 2,3}are the unique integer minimizers of node
overhead f(b) = 6, certifying that1/36cannot be improved by changing branching arity
while revealing that ternary trees (b= 3) exponentially compress the pure-strategy space.
3. 8×–64×hardness tree tightening and exactm2-support dichotomy (Section 4):
Tightening the Pinsker threshold shrinks the dimension-based and node-based hardness
trees by≥8×and32 ×–64×, and a rectangle-rigidity proof characterizes exactly when the
minimal support floorm2 is attained.
Table 1: Quantitative and structural advances over Cheval–Horn–Paul–Shirmohammadi [1].
Stage / Quantity CHPS (arXiv:2611.34897v1) This Work (Theorems 1–3)
Rational LP gapη(Lem. 14)((K+ 1)B) −(K+1) (
√
K(K+ 1) K/2DK
max)−1 (>30×fewer bits at
r= 8,q= 10)
2-player support capK= 1 +d 1(d1 + 1) +d2(d2 + 1)Exact gap
K−κ d =d2
1 +d2
2 −d1d2 ≥1
2 (d2
1 +d2
2)(2×at
d1 =d2)
Matching tree aritybBinary (b= 2) only Unique optimab∈{2,3}(f(b) = 6, sharp
1/36);b= 3cuts|Σ i|by(4/3) (m−1)/2
Dim-based hardnessm2 ⌈log2(8r3)⌉ 2⌈log2(r2(r−1)+1)⌉(≥8×smaller∀r≥2)
Node-based hardnessm2 ⌈log2(8r4)⌉(r≥5)2 ⌈log2(⌊r2(r2+r−3)/6⌋+1)⌉(32×–64×smaller)
Minimal support|supp|=m 2 Lower bound|supp|≥m 2 only Exact iff:( P,Q)has a 1
m Z-rational Nash;b= 3
vsb= 2split onG 1/3
2 Exponential LP-Gap Bit-Complexity Tightening and Support
Dominance
LetΓbe an n-player perfect-recall extensive-form game with normalized terminal payoffsui(z) ∈
[0,1], sequence-form dimensionsdi, and quadratic support boundK = 1 + ∑n
i=1 di(di + 1). For
each playeri∈[n], define theper-player leaf-payoff least common multiple
Di := lcmz∈Z den
(
pc(z)ui(z)
)
, D max := max
i∈[n]
Di.(1)
2

--- Page 3 ---
For any nonempty supportS⊆ Σwith |S|≤K , the reweighting LP (11) of [1] minimizest∈ [0,1]
overµ∈∆(S)subject toR i,σi,σ′
i
(µ)≤tfor alli,σ i ∈Ai, andσ′
i ∈Σ i.
Theorem 1(Active-support LCM–Hadamard LP gap and two-player support dominance).LetΓ
be any normalizedn-player perfect-recall extensive-form game and letS⊆ Σbe any nonempty
support with|S|≤K.
(a) Sharp active-support LCM–Hadamard vertex gap:At any optimal vertexx∗= (µ∗,t∗)
of LP (11) witht∗(S)>0and active support sizes:=|supp(µ ∗)|≤|S|≤K,
t∗(S)≥η sharp(s) := 1√s(s+ 1) s/2 ∏s
j=1 Dij
≥η sharp := 1√
K(K+ 1) K/2 DKmax
.(2)
Consequently, settingϵsharp
Γ := 1
2 ηsharp suffices for exact reweighting in Theorem 6 of [1]:
every unnormalizedϵsharp
Γ -NFCE supported onS can be reweighted in polynomial bit time to
an exact rational NFCE supported onS.
(b) Strict bit-precision reduction:For every1 ≤s≤K and1 ≤Dmax ≤B := ∏
r∈Rden(r),
ηsharp(s)>η CHPS = ((K+ 1)B) −(K+1) strictly, saving at least
log2
(ηsharp
ηCHPS
)
≥ K+ 1
2 log2(K+ 1) + log 2 B+Klog 2
( B
Dmax
)
(3)
bits of oracle precision. In particular, on CHPS’s matching-tree gameΓ2(P,Q,k )with
r×r rational payoffs of common denominatorq, Dmax ≤2q is independent ofm, whereas
B≥ 2 q2r2
, reducing required oracle precision at support capκd (m= m∗
d(r,2)) by>30×at
r= 8,q = 10(certified lower bound30 .62×in C02, continuous ratio33.3×in Figure 1(a)).
(c) Exact two-player support dominance:For every two-player game with dimensions
(d1,d2)̸= (0,0), the product supportκd = (d1 + 1)(d2 + 1)strictly beatsKwith exact gap
K−κ d =d2
1 +d2
2 −d1d2 = 1
2(d1 −d2)2 + 1
2(d2
1 +d2
2)≥ 1
2(d2
1 +d2
2)>0,(4)
achieving a2 ×support reduction alongd1 = d2 (Figure 1(b)), and replacingK by κd in (2)
halves the LP-gap exponent as well.
Proof. For (a), letx∗= (µ∗,t∗)be an optimal vertex witht∗>0and s= |supp (µ∗)|≥ 1. Since
t∗>0, the constraintt= 0is inactive; if t∗= 1then (2) holds trivially sinceηsharp(s) ≤1. Thus
we may assume0 <t∗<1, so the|S|+ 1linearly independent active constraints atx∗ consist
of: (i) |S|−s coordinate-zero equationsµ(τ) = 0for τ /∈supp(µ∗); (ii) the probability-simplex
equation ∑
τ∈S µ(τ) = 1; and (iii)sactive regret equalities∑
τ∈S Rj(τ)µ(τ) −t = 0( j = 1,...,s ),
where rowjbelongs to some playeri j ∈[n].
Eliminating the|S|−s zero variablesµ(τ) = 0leaves a nonsingular( s+ 1)×(s+ 1)linear
system Msy= e1 (where y= (µ∗|supp(µ∗),t∗)T and e1 = (1,0,..., 0)T). Its first row is(1,..., 1,0),
which is already integral with Euclidean norm√s. For each regret rowj∈{ 1,...,s} , every
pure-profile deviation differenceRj(τ) = ∑
z∈Z pc(z)uij (z)(χij (σ′
j,z) −χij (σj,z)) ∏
r̸=ij χr(τr,z)
satisfies |Rj(τ)|≤ 1and Dij Rj(τ) ∈Z . Multiplying rowj by Dij (and leaving row0unscaled)
yields an equivalent nonsingular integer systemAsy = e1 whose j-th regret row has Euclidean
norm at mostDij
√s+ 1 . By Cramer’s rule,t∗= det(As,t)/det (As)with |det (As,t)|≥ 1(since
As,t is integral andt∗>0). Applying Hadamard’s inequality to the rows ofAs yields
|det(As)| ≤√s
s∏
j=1
(
Dij
√
s+ 1
)
= √s(s+ 1) s/2
s∏
j=1
Dij ,
proving (2). Strict dominance overηCHPS and (3) follow directly by taking logarithms (squared-
integer dominance formalized in Lean 4 assharp_lp_gap_strictly_dominates_chps), and(4)
is verified in Lean 4 astwo_player_support_gap_exact and two_player_balanced_support_
factor.
3

--- Page 4 ---
Figure 1:Exponential LP-gap bit-precision savings and two-player support dominance.
(a) Required oracle bit precisionlog2(1/ϵΓ)on CHPS matching-tree instancesΓ2(P,Q,k )(at κd
and m= m∗
d(r,2)) comparing Lemma 14’s raw denominator productB against Theorem 1’s LCM–
Hadamard bound (Dmax ≤2q), saving33 .3×bits (> 30.6×certified in C02) atr = 8,q = 10.
(b) Ratio K/κd showing exact2 ×balanced saving along d1 = d2 and2 .5×along d2 = 2 d1
(certificateC03).
3 Optimal b-ary Matching Trees and Sharpness of the1/36Con-
stant
In Section 4.2 of [1], the hardness gameΓflips a public fair coin between a sourcer×r bimatrix
game G and a binary matching treeM with m = 2k labels. We generalize branch M to an
arbitrary **b-ary perfect-recall matching tree**Mb(k)(b∈Z ≥2,k≥1,m=b k): at each agreed
prefix w∈ [b]<k, Player 1 picks a digite1 ∈[b]and Player 2 pickse2 ∈[b]without observing e1
(forming one information set of sizeb for Player 2); ife1 ̸= e2 play terminates with payoff(0,1),
while ife1 = e2 play advances to prefixwe1 (or terminates with(1,0)at depth k). LetΓ b(P,Q,k )
denote the resulting public-coin game.
Theorem 2(b-ary structural invariants, optimality ofb∈{ 2,3}, and ternary strategy compres-
sion).For every branching factorb∈Z ≥2, depthk≥1(m=b k), and source sizer≥2:
(a) Exact invariants andb-invariance of sequence-form dimension:Γb(P,Q,k )has
perfect recall, exact chance-averaged payoffs(14)–(15)of [1] over[ m], and exact structural
parameters
d1 =d2 =m+r−2 (independent ofb!),(5)
|Vb|=f(b)m−
(
f(b)−1
)
+r2 +r+ 2, f(b) :=b+ 2 + 2
b−1 ,(6)
|Zb|= (b+ 1)m−b+r 2,|Σ 1|=|Σ 2|=rb (m−1)/(b−1).(7)
(b) Unique integer optimality ofb∈{ 2,3}and sharpness of1 /36:For every integer
b≥2,
f(b)−6 = (b−2)(b−3)
b−1 ≥0,(8)
with equalityif and only ifb∈{ 2,3}(and f(b) >6strictly for all b≥ 4). Consequently,
across the entireb-ary matching-tree family,limm→∞κd/|Vb|2 = 1/f(b)2 ≤1/36, proving that
Corollary 20’s node-quadratic constant1/36is exact and unimprovable by varying tree arity.
Moreover, for bothb= 2and b= 3, |Vb|= 6m+r2 +r−3and |Vb|−6(m+r−1) = r2 −5r+3,
which is nonnegative if and only ifr≥5(being−3,−3,−1forr= 2,3,4).
4

--- Page 5 ---
(c) Ternary exponential pure-strategy compression:At every matched label countm= 3k
(k≥ 1), the ternary gameΓ3 has theexact sameoptimal node count |V3|= 6m+ r2 + r−3
and sequence-form dimensiondi = m+ r− 2as a binary tree of sizem, while shrinking
each player’s pure-strategy space exponentially by the factor(4/3)(m−1)/2 (from r2m−1 to
r3 (m−1)/2, exceeding1015×atm= 243, Figure 2).
Proof. In Mb(k), the number of internal prefixesw∈ [b]<k is I := ∑k−1
j=0 bj = (m− 1)/(b− 1).
Each prefix contributes1Player 1 decision node,bPlayer 2 decision nodes (one information set of
bactions for each player), andb(b−1)mismatch leaves, plusmmatch leaves at depthk. Summing
Player 1’s free sequence-form coordinates gives(r−1) + I(b−1) = m+ r−2(and identically
for Player 2), proving(5). Summing leaves yieldsr2 + b(b−1)I+ m= (b+ 1)m−b + r2, while
summing all nodes (root chance node1, branchG nodes r2 + r+ 1, plus(b+ 1)I+ b(b−1)I+ m
nodes in Mb) gives(6). Each player picks one ofr actions in G and one ofb actions at each
of theI information sets inMb, giving(7). Clearing b−1 > 0in f(b) −6proves (8) (Lean 4:
bary_node_overhead_exact_optimality , bary_matching_tree_exact_counts , corollary2
0_node_dominance_exact_threshold). Finally,3 <4 = 22 yields3 (m−1)/2 <2m−1 for allm≥ 3
(ternary_beats_binary_pure_strategy_space).
Figure 2:Exact optimality of binary/ternary matching trees and ternary pure-strategy
compression.(a) Node overhead f(b) = b+ 2 + 2/(b−1)achieving its unique integer minimum
f(b) = 6at b∈{ 2,3}, proving sharpness of Corollary 20’s1/36constant (certificate C04). (b) Pure-
strategy spacelog10(|Σi|/r)at identical node count6 m+ r2 + r−3, where ternary trees (b= 3)
save a factor of(4/3)(m−1)/2 (>10 15×atm= 243, certificateC06).
4 Hardness Tree Sharpening and Exactm2-Support Dichotomy
InSection4.5of[ 1], decodingaweak1 /r-NashequilibriumfromanexactNFCE µwith|supp (µ)|≤
κ uses Lemma 19’s boundζ =
√
1
2 log(κ/m2)< 1/r, for which CHPS choosesm = 2⌈log2(8r3)⌉
(dimension-based) andm= 2⌈log2(8r4)⌉(node-based). We sharpen both reductions substantially
and characterize exact attainment of the support lower bound|supp(µ)|=m2 (Lemma 18).
Theorem 3(8×–64×hardness tree sharpening and exactm2-support dichotomy).
(a) Sharp dimension-based PPAD-hardness reduction (≥8×smaller):For every r≥ 2
and b∈{ 2,3}, settingm∗
d(r,b) := b⌈logb(r2(r−1)+1)⌉ satisfies 1
2 log(κd/m2) = log(1 + r−1
m ) <
r−1
m < 1
r2 and henceζ <1/r. Forb= 2, m∗
d(r,2)is strictly at least8×smaller than CHPS’s
2⌈log2(8r3)⌉ for everyr≥ 2(Table 2, Figure 3(a)). Using the Kullback–Csiszár–Kemperman
5

--- Page 6 ---
refined Pinsker inequalityDKL(p∥q) ≥2 TV(p,q)2 + 4
9 TV(p,q)4 [7] further tightens the
continuous threshold tom>(r−1)/(exp(r −2 + 2
9 r−4)−1)(certificateC10).
(b) Sharp node-based PPAD-hardness reduction (32×–64×smaller):For every r≥ 5
and b∈{ 2,3}, setting m∗
V(r,b) := b⌈logb(⌊r2(r2+r−3)/6⌋+1)⌉ ensures κd ≤κ V = ⌊|Vb|2/36⌋
and 1
2 log(κV/m2) ≤log (1 + r2+r−3
6m ) < 1
r2 , so ζ <1/r. For b = 2, m∗
V(r,2)reduces the
matching-tree size by32×–64×relative to CHPS’s2 ⌈log2(8r4)⌉ across all r≥ 5(Table 2,
Figure 3(b)).
(c) Exact m2-support dichotomy and ternary-vs-binary separation:Letm= bk (b≥
2,k≥ 1). The public-coin gameΓb(P,Q,k )admits an exact NFCEµ with minimal support
size |supp (µ)|= m2 if and only if(P,Q)admits an exact Nash equilibrium(x,y)whose
probabilities are integer multiples of1 /m (i.e. mx,my∈Z r
≥0). In particular, for the
asymmetric2×2game
G1/3 :P=
(
1 0
0 1/2
)
, Q=
(
0 1/2
1 0
)
,(9)
whose unique Nash equilibrium isx∗= (2/3,1/3),y ∗= (1/3,2/3):
• Ternary attainability:Γ 3(P,Q,k )achieves an explicit exact NFCE of supportm2 for
everyk≥1(m 2 = 9atk= 1, certificateC12).
• Binary impossibility:Because3 ∤ 2k for all k≥ 1(Lean 4: th re e_ no t_ dv d_ po w_
tw o),everyexact NFCE of CHPS’s binary gameΓ 2(P,Q,k )must satisfy |supp (µ)|≥
m2 + 1strictly.
Proof. For (a) and (b),log(1 + t) <t for t> 0implies ζ =
√
1
2 log(κ/m2)<
√
t< 1/r whenever
t< 1/r2, givingm>r 2(r−1)for κd and m>r 2(r2 +r−3)/6for κV (Lean 4:sharp_dim_hardne
ss_threshold, sharp_node_hardness_threshold, node_hardness_24x_saving; exact rational
ln(1 + t)verification in C08–C09). With DKL ≥2 TV2 +4
9 TV4, DKL ≤2 log(1 + r−1
m ) < 2
r2 + 4
9r4
forcesTV<1/r(refined_pinsker_strict_bonus).
For (c), if(x,y)is an exact Nash equilibrium withmx,my∈Z r
≥0, partition[m]into rblocks of
sizes mxa (defining y1 : [m] →[r]) andrblocks of sizesmyb′ (defining y2 : [m] →[r]). The uniform
product µ= Unif({(y1(x1),x1)}x1∈[m]) ⊗Unif ({(y2(x2),x2)}x2∈[m])has support m2, exact Nash
marginal(x,y)in branchG, and independent uniform(X 1,X2)in branchM b, hence is an exact
NFCE. Conversely, supposeµ is an exact NFCE with|supp (µ)|= m2, and letSi := supp(µi)be
the marginal supports. By Lemma 17 of [1], conditional on everyτ1 ∈S1, X2 is uniform on[m],
so eachτ1 ∈S1 pairs with at leastm distinct profiles inS2; hence|S2|≥m , and symmetrically
|S1|≥m . Since ∑
τ1∈S1 |{τ2 : (τ1,τ2) ∈supp (µ)}|= |supp (µ)|= m2 and every term is≥m ,
we must have|S1|= m and everyτ1 ∈S 1 pairs with exactlym profiles in S2; symmetrically
|S2|= m(Lean 4: exact_m2_rectangle_rigidity). Therefore supp(µ) = S1 ×S2, everyτ2 ∈S2
carries a distinct matching labelX2(τ2) ∈[m]with conditional probability1 /mgiven anyτ1 ∈S1,
and symmetrically µ(τ1,τ2) = 1
mµ1(τ1) = 1
mµ2(τ2). Summing over τ2 yields µ1(τ1) = 1 /m, so
µ= Unif(S1) ⊗Unif (S2)! Its branch-G marginal( x,y)therefore has entries in 1
mZ, zero mutual
information (I(Y1; Y2) = 0), and zero regret inG (exact Nash). ForG1/3, direct check shows zero
pure Nash equilibria and unique mixed Nashx∗= (2/3,1/3),y∗= (1/3,2/3), which lies in1
3k Z
(three_dvd_pow_three) but never in1
2k Z(three_not_dvd_pow_two).
5 Formal Verification Architecture and Scope
All algebraic, combinatorial, and exact-rational results are machine-verified across two independent
formal layers:
6

--- Page 7 ---
Figure 3:PPAD-hardness matching-tree sharpening.(a) Dimension-based reduction
comparing CHPS (2⌈log2(8r3)⌉) vs. our sharp binarym∗
d(r,2)( ≥8×smaller for allr≥ 2) and
ternary m∗
d(r,3)(certificate C08). (b) Node-based reduction comparing CHPS (2⌈log2(8r4)⌉) vs. our
sharp binarym∗
V(r,2)(32×–64×smaller across allr≥5, certificateC09).
Table 2: Exact matching-tree sizes comparing CHPS [1] against Theorem 3 (certificatesC08–C09).
rCHPSm d Sharpm ∗
d(r,2)Dim Saving CHPSm V Sharpm ∗
V (r,2)Node Saving
2 64 88×— — —
5 1,024 1288×8,192 12864×
8 4,096 5128×32,768 1,02432×
10 8,192 1,0248×131,072 2,04864×
16 32,768 4,0968×524,288 16,38432×
32 262,144 32,7688×8,388,608 262,14432×
64 2,097,152 262,1448×134,217,728 4,194,30432×
7

--- Page 8 ---
1. Constructive Lean 4.35.0 Formalization (lean/ExtensiveFormNfceSharp.lean ):
18zero-dependency theorems building cleanly in1 .2s with0 sorry,0custom axioms,0
Classical.choice, and0warnings. These certify squared-Hadamard LP-gap dominance
over CHPS Lemma 14, two-player support dominance and balanced2×scaling, b-ary
node-overhead optimality (b∈{ 2,3}) and exact node/leaf counts, ternary pure-strategy
dominance (3t < 4t), Corollary 20’sr≥ 5threshold,8 ×dimension-based and24 ×–64×
node-based hardness thresholds,3 ∤ 2k vs.3 |3k, exactm2 rectangle rigidity, refined Pinsker
strict bonus, and quadratic support superadditivity.
2. AST-Audited Zero-Float Rational Verifier (verification/verify_paper104.py ):
Pure Python standard-library verifier (fractions.Fraction, int) audited by its own
AST walker (C16) to forbid all float/complex literals,/, **, float, pow, getattr, and
numerical libraries. It verifies all16SHA-256 certificates listed in Table 3 under protocol
EFG-NFCE-SHARP-1.0 (MANIFEST.json SHA-256: 988e9daebba66694...cabc18dab52 ),
including explicit zero-regret exact NFCE checks onΓ2(Matching Pennies)andΓ 3(G1/3),
an explicit infeasible-support LP vertex gapt∗(S) = 1/6( C13), and exhaustive rejection of
all16uniform2×2assignments onΓ 2(G1/3,1)in the57-test pytest suite.
Delineation of scope.Classical background results—Hadamard’s determinant inequality,
Pinsker’s / Kullback–Csiszár–Kemperman’s inequality [7], and the PPAD-hardness of weak
1/r-Nash [4]—are standard theorems invoked with complete self-contained proofs of every new
deduction in Sections 2–4, while every integer/rational inequality, tree invariant, exact NFCE
construction, and adversarial counterexample is machine-checked in Lean 4.35.0 and exactQ.
Whether unrestricted NFCE computation without a support cap is PPAD-hard remains open [1].
A Cryptographic Certificate Ledger
Table 3: SHA-256 certificate ledger for protocolEFG-NFCE-SHARP-1.0 (MANIFEST.json SHA-256:
988e9daebba66694685e23fb17a80c68880f4ff659b9cdbcaa08fcabc18dab52).
ID SHA-256 Prefix (16 hex) Scope Certified in Zero-Float ExactQ
C01 27d89daf75331b5dActive-support Hadamard LP-gap dominance over CHPS Lemma 14
C02 dd2286deeaee7e8dBit-precision savings on CHPS matching-tree gamesΓ 2(P,Q,k)
C03 dff8fb053f601922Two-player support dominanceKvs.κ d (100pairs + balanced scaling)
C04 091c65ff66326feab-ary node-overhead optimality (f(b) = 6iffb∈{2,3}, sharp1/36)
C05 a8529d6e146f6912Exact node, leaf, andb-invariantd i counts forΓb(P,Q,k)
C06 c095bc4131dce1f7Ternary exponential pure-strategy space reduction (m= 3...243)
C07 75b06af9c61fbb1dCorollary 20 exact thresholdr≥5(|V|−6(m+r−1) =r 2 −5r+ 3)
C08 cf82abda5b558e71≥8×dimension-based PPAD-hardness tree sharpening (r= 2...64)
C09 64d72e0ca3063db032×–64×node-based PPAD-hardness tree sharpening (r= 5...64)
C10 a5d0c9f2d95351a3Kullback–Csiszár–Kemperman refined Pinsker threshold tightening
C11 36e04f067f9dc108Constructive exactm 2-support NFCE onΓ2(Matching Pennies)
C12 44e43c7ec3374497Exact ternary-vs-binarym 2-support separation on asymmetricG1/3
C13 f116cfede733bd67Explicit infeasible-support LP vertex gapt ∗(S) = 1/6vs.η sharp
C14 0fb64dc032324956Matching-pennies single-profile impossibility (|V|= 7,κ V = 1)
C15 3e24ffaf2cc1ad40Multi-player support comparison (Kvs. product support and1 +N(N−1))
C16 9fb5e55585a9104cSelf-referential AST zero-float and exact-arithmetic security audit
References
[1] V. Cheval, F. Horn, S. Paul, and M. Shirmohammadi,Computing Normal-Form Correlated
Equilibria in Extensive-Form Games is in PPAD, arXiv:2611.34897v1 [cs.GT], November 25,
2026.
[2] B. von Stengel and F. Forges,Extensive-form correlated equilibrium: Definition and computa-
tional complexity, Mathematics of Operations Research33(4), 1002–1022 (2008).
8

--- Page 9 ---
[3] C. H. Papadimitriou,On the complexity of the parity argument and other inefficient proofs of
existence, J. Comput. Syst. Sci.48(3), 498–532 (1994).
[4] X. Chen, X. Deng, and S.-H. Teng,Settling the complexity of computing two-player Nash
equilibria, J. ACM56(3), 14:1–14:57 (2009).
[5] D. Koller and N. Megiddo,The complexity of two-person zero-sum games in extensive form,
Games and Economic Behavior4(4), 528–552 (1992).
[6] D. Koller, N. Megiddo, and B. von Stengel,Efficient computation of equilibria for extensive
two-person games, Games and Economic Behavior14(2), 247–259 (1996).
[7] A. A. Fedotov, P. Harremoës, and F. Topsøe,Refinements of Pinsker’s inequality, IEEE Trans.
Inf. Theory49(6), 1491–1498 (2003).
9
