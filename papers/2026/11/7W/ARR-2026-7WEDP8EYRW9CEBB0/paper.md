# Sharp Geometric-Horizon Parameterization, Exact Pairwise Fredman Extremality, and Zero-O(.) Comparison Certificates for Deterministic Linear-Time Minimum Spanning Trees

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-7WEDP8EYRW9CEBB0` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/deterministic-linear-mst-geometric-certificates-and-fredman-sharp-bounds (`v1.0.0`)  
**Canonical PDF SHA-256:** `6426088f3bb6e41e7e25b0f50dc1a92214cdabf471efdb240e54c42bc81a861b`

## Abstract

In a landmark result of November 2026, Khanna, Putterman, and Song proved that the deterministic comparison complexity of the minimum spanning tree (MST) problem is linear, T*(m, n) = O(m), using a recursive portal-spoke certificate procedure with polynomial depth schedule t_d = gamma d^3, r_d = 8 t_d^3 that hides all multiplicative constants inside asymptotic O_eps(.) notation. We establish three sharp, zero-O(.) structural theorems backed by 20 constructive Lean 4.36.0 theorems and 16 zero-float rational certificates. First, we sharpen three combinatorial primitives: the exact maximum bad-round count in any t x t monotone block schedule is strictly 2t - 1 (attained for all t >= 1), greedy portal covering obeys |P'| <= (2r^2 - 2r + 1)/r^3 * n < 2n/r, and the exact pairwise maxima-vector maximum is M(n, 2) = floor((n^2 + n + 2)/3) for all n >= 3, strictly below Fredman's binomial ceiling C(n+1, 2) by an asymptotic factor of 2/3. Second, we expose a hidden factorial polylogarithmic blowup in polynomial schedules (sum d^21/4^(d-1) > 1.547e17, sum (d-1)d^19.5/2^(d-1) > 5.662e22, forcing C_{1/8}^KPS > 7.882e33 and k_Bor >= 230) and prove that a geometric-horizon schedule t_d = ceil(gamma rho^(d-1)), r_d = 2 kappa t_d^3 is jointly stable if and only if 1 < rho < kappa^(1/13). Third, at (theta, eps, kappa, rho, gamma) = (1/2, 7/16, 32, 13/10, 80), we certify a > 4.779e16x reduction in C_eps (to < 1.650e17), save 106 Boruvka phases (230 -> 124), establish an explicit zero-O(.) comparison bound T*(m, n) <= 944 m (including a base-case-free T_PICK(N) <= 23 N proof for all N >= 1 and Komlos's non-asymptotic directed verification theorem), and certify end-to-end exact Boruvka, portal-spoke, and cycle-support filtering invariance on canonical graphs.

## Full Extracted Text

--- Page 1 ---
Sharp Geometric-Horizon Parameterization, Exact
Pairwise Fredman
Extremality, and Zero- O(·) Comparison Certiﬁcates
for
Deterministic Linear-Time Minimum Spanning Trees
Lluis Eriksson∗
November 27, 2026
Abstract
In a landmark result of November 2026, Khanna, Putterman, and Song [ 7] proved that
the deterministic comparison complexity of the minimum spanning tree (MST) problem
is linear, T∗(m, n) = O(m), settling the classical problem via Pettie and Ramachandran’s
optimal reduction [ 9]. Their recursive portal-spoke certiﬁcate procedure uses a polynomial
depth schedule td = γd3, rd = 8 t3
d and hides all multiplicative constants, recursion sums,
and preprocessing Borůvka phase counts inside asymptotic Oε(·) notation. In this paper
we analyze the exact ﬁnite-dimensional combinatorics and non-asymptotic constants of the
portal-spoke certiﬁcation framework, proving three sharp, zero- O(·) structural theorems
backed by 20 constructive Lean 4.36.0 theorems and 16 zero-ﬂoat rational certiﬁcates. First,
we sharpen three combinatorial building blocks: (i) in any t-block × t-round monotone
preference schedule, the exact maximum number of bad rounds per edge is strictly 2t − 1
(attained for every t ≥ 1) rather than 2t; (ii) greedy frequency covering of n sets of size r2
uses at most 2r2−2r+1
r3 n < 2n
r portals; and (iii) for Fredman’s maxima-vector theorem [ 5],
we prove the exact pairwise count |X(S1, S2)| = |S1||S2| − c(c − 1) (c = |S1 ∩ S2|) and
determine the exact extremal maximum M(n, 2) = ⌊(n2 + n + 2)/3⌋ (n ≥ 3), strictly sepa-
rating Fredman’s bound
( n+1
2
)
by an asymptotic factor of 2/3. Second, we expose a hidden
factorial polylogarithmic blowup in polynomial schedules: because r2
dtd ∝ d21, the KPS d3
schedule incurs ∑
d≥1 d21/4d−1 > 1.547 × 1017 and ∑
d≥1(d − 1)d19.5/2d−1 > 5.662 × 1022,
forcing CKPS
1/8 > 7.882 × 1033 and kBor ≥ 230 Borůvka phases. Replacing td = γd3 by
a geometric-horizon schedule td = ⌈γρd−1⌉, rd = 2 κt3
d is jointly stable across all ﬁve re-
cursion series if and only if 1 < ρ < κ 1/13 (sharp critical exponent), collapsing every
polylogarithmic sum into closed-form rational geometric series. Third, at the certiﬁed op-
timum (θ, ε, κ, ρ, γ ) = (1 /2, 7/16, 32, 13/10, 80), we reduce Cε by a certiﬁed factor exceed-
ing 4.779 × 1016× (to C7/16 < 1.650 × 1017), eliminate 106 Borůvka preprocessing phases
(230 → 124), establish an explicit zero- O(·) master comparison bound T∗(m, n) ≤ 944 m
(including a ﬁrst-principles TPICK(N) ≤ 23 N proof valid for all N ≥ 1 and Komlós’s non-
asymptotic directed veriﬁcation theorem), and certify end-to-end Borůvka, portal-spoke,
and cycle-support ﬁltering invariance on canonical graphs.
∗Independent Researcher. Research, constructive formal veriﬁcation in Lean 4.36.0, zero-
ﬂoat exact rational certiﬁcate veriﬁcation, adversarial testing, and manuscript typesetting were
conducted with transparent assistance from Google Antigravity. Code is released under MIT;
manuscript and ﬁgures under CC-BY-4.0. Repository: https://github.com/lluiseriksson/
deterministic-linear-mst-geometric-certificates-and-fredman-sharp-bounds (v1.0.0).
1
AIRR:ARR-2026-7WEDP8EYRW9CEBB0 v1  [Computer and informatio...]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
1 Introduction
Determining the worst-case deterministic comparison complexity T∗(m, n) of computing a mini-
mum spanning forest (MSF) on an undirected n-vertex, m-edge graph with opaque real weights
stood open for a century after Borůvka’s 1926 algorithm [ 2, 10, 4, 3]. While Komlós [ 8] proved
that O(m) comparisons suﬃce to verify a candidate spanning tree, and Karger, Klein, and
Tarjan [6] achieved expected linear time via random sampling and ﬁltering, the best determinis-
tic comparison bound remained Chazelle’s O(mα(m, n)) [3] until Pettie and Ramachandran [ 9]
proved that a uniform deterministic pointer-machine algorithm runs in optimal O(T∗(m, n))
time. On November 23, 2026, Khanna, Putterman, and Song [ 7] resolved the problem uncondi-
tionally by proving T∗(m, n) = O(m) through a recursive deterministic portal-spoke certiﬁcate
proceduresatisfying
|F| + |U(F)| +
ℓ∑
i=1
|Ei| ≤ εm + Cε
√mn, (1)
where F ⊆ E(G) is an admissible forest, U(F) is the set of edges unsupported by F, and
E1, . . . , Eℓ are the edge sets passed to exact recursive MSF calls. Preceding ( 1) by kBor Borůvka
phases reduces the non-isolated vertex count to n′ ≤ n/2kBor ; choosing kBor large enough that
Cε
√
mn′ ≤ (θ −ε)m yields the linear halving recurrence T(m) ≤ ∑
i T(mi) + Bm with ∑
i mi ≤
θm (θ = 1 /2 in [ 7]).
Despite settling the asymptotic complexity, the original analysis of [ 7] leaves open the ex-
act ﬁnite-dimensional tightness of its combinatorial primitives and hides the magnitude of Cε,
kBor, and the linear comparison constant inside Oε(·). Our investigation uncovers a striking phe-
nomenon: the polynomial depth schedule td = γd3, rd = 8 t3
d used in [ 7] triggers a hidden factorial
polylogarithmic blowup ∑
d≥1 d21/4d−1 > 1.547 ×1017 and ∑
d≥1(d −1)d19.5/2d−1 > 5.662 ×1022
that inﬂates C1/8 past 7.882 × 1033 and requires at least kBor = 230 Borůvka phases. By shift-
ing to a slow geometric schedule td = ⌈γρd−1⌉, rd = 2 κt3
d inside its sharp stability domain
1 < ρ < κ 1/13 and tracking every constant in exact rational arithmetic, we establish three
zero-O(·) theorems:
1. Exact Portal-Spoke Combinatorics and Pairwise Fredman Extremality (The-
orem 1). We prove the exact bad-round ceiling 2t − 1 (tight for every t ≥ 1), the
sharpened greedy portal bound 2r2−2r+1
r3 n, and the exact pairwise maxima-vector maxi-
mum M(n, 2) = ⌊(n2 + n + 2)/3⌋ (n ≥ 3), strictly below Fredman’s
( n+1
2
)
by a factor of
2/3.
2. Polylogarithmic Blowup vs. Optimal Geometric-Horizon Stability (Theorem 2).
We certify the 1017–1022 factorial blowup of polynomial schedules, prove that 1 < ρ < κ 1/13
is the exact sharp stability domain for geometric-horizon schedules, and derive closed-form
rational upper bounds for all ﬁve recursion sums.
3. Zero-O(·) Borůvka Compression, T∗(m, n) ≤ 944 m, and Graph Certiﬁcates (The-
orem 3). We certify a > 4.779 × 1016× reduction in Cε, a 106-phase Borůvka reduction
(230 → 124), an explicit zero- O(·) linear comparison bound T∗(m, n) ≤ 944 m (deriv-
ing a complete base-case-free TPICK(N) ≤ 23 N selection bound for all N ≥ 1, uncon-
ditional per-round Claim 3.12 estimation, projection-record admissibility, and Komlós’s
non-asymptotic directed veriﬁcation bound), and end-to-end exact graph certiﬁcates.
2 Exact Portal-Spoke Combinatorics and Pairwise Fredman Ex-
tremality
In the certiﬁcate procedure of [ 7], a call at recursion level d ≥ 1 executes t2 rounds partitioned
into t blocks of t rounds. Within each block, spokes remain ﬁxed and forest connectivity only
2

--- Page 3 ---
grows, so every edge’s preferred action proﬁle is monotone of the form Ppb Ft−pb (0 ≤ pb ≤ t) in
each block b ∈ [t]. A round is bad for edge e if it is either the last P round in its block, or an F
round inside the last block b∗ containing any F. In batch processing, each vertex v selects k = r2
lightest admissible neighbor representatives Sv; portals are chosen greedily while some vertex
hits ≥ r uncovered k-sets, followed by one vertex from each remaining uncovered set. To bound
the number of possible preference histories, [ 7] invokes Fredman’s maxima-vector theorem [ 5]:
for m nonempty subsets S1, . . . , Sm ⊆ [n], the set X(S1, . . . , Sm) := {(maxπ S1, . . . , maxπ Sm) :
π ∈ Sn} satisﬁes |X(S1, . . . , Sm)| ≤
( n+m−1
m
)
.
Theorem 1 (Sharp Bad-Round Ceiling, Greedy Portal Bound, and Pairwise Fredman Ex-
tremality).
(a) Exact 2t − 1 bad-round ceiling: For every t ≥ 1 and every monotone block proﬁle
(p1, . . . , pt) ∈ {0, . . . , t}t, the number of bad rounds satisﬁes
B(p1, . . . , pt) ≤ 2t − 1 < 2t, (2)
with exact equality attained for every t ≥ 1 (e.g., (p1, . . . , pt−1, pt) = ( t, . . . , t, 0) and
(t, . . . , t, 1)). In particular, the worst-case bad-round fraction is (2t −1)/t2 (strictly resolv-
ing the degenerate t = 1 case where 2t = 2 > t2 = 1 ).
(b) Sharpened greedy portal bound: For every r ≥ 2 and every collection of at most n subsets
Sv ⊆ V of size r2, greedy frequency covering selects a high-frequency portals (≥ r uncovered
sets each) and u residual portals satisfying ar + u ≤ n and ur2 ≤ n(r − 1), whence the
total portal set P′ obeys
|P′| ≤ a + u ≤ 2r2 − 2r + 1
r3 n < 2n
r . (3)
(c) Exact pairwise Fredman extremality: For any two nonempty subsets S1, S2 ⊆ [n] with
p = |S1 \S2|, q = |S2 \S1|, and c = |S1 ∩S2|, the exact number of reachable maxima pairs
is
|X(S1, S2)| = pq + (p + q)c + c = |S1| |S2| − c(c − 1). (4)
Maximizing over all pairs of nonempty subsets of [n] yields M(2, 2) = 2 and, for every
n ≥ 3,
M(n, 2) := max
S1,S2̸=∅
|X(S1, S2)| =
⌊
n2 + n + 2
3
⌋
, limn→∞
M(n, 2)( n+1
2
) = 2
3, (5)
strictly below Fredman’s multiplicity ceiling
( n+1
2
)
for all n ≥ 2 (Lean thm06–thm10).
Proof. Proof of (a). If no block contains F, each of the t blocks has one bad P round, totaling
t ≤ 2t − 1. Otherwise, let b∗ ∈ [t] be the last block containing at least one F, and let f =
t − pb∗ ∈ [1, t] be its F-count. Each block b ̸= b∗ contributes at most one bad P round and zero
bad F rounds, totaling at most t − 1. Inside block b∗, if f = t then pb∗ = 0 , contributing 0 bad
P rounds and t bad F rounds; if 1 ≤ f ≤ t − 1, block b∗ contributes 1 bad P round and f bad F
rounds, totaling 1 + f ≤ t. Summing yields B ≤ (t − 1) + t = 2 t − 1, attained whenever pb ≥ 1
for all b ̸= b∗ and pb∗ ∈ {0, 1} (Lean thm01–thm02, Certiﬁcate cert01).
Proof of (b). Each of the a greedy portals covers at least r previously uncovered sets, leaving u
uncovered sets, so ar+u ≤ n. Upon termination of the greedy loop, each of the n vertices lies in
at most r − 1 uncovered sets, so total remaining incidences satisfy ur2 ≤ n(r − 1). Multiplying
ar + u ≤ n by r2 and ur2 ≤ n(r − 1) by r − 1 and summing gives
(a + u)r3 = ( ar3 + ur2) + ur2(r − 1) ≤ nr2 + n(r − 1)2 = (2 r2 − 2r + 1)n < 2r2n
3

--- Page 4 ---
Figure 1: Exact combinatorial sharpenings (Theorem 1). (a) Exact pairwise maxima-
vector maximum M(n, 2) = ⌊(n2 + n + 2) /3⌋ vs. Fredman’s bound
( n+1
2
)
across n ∈ [3, 24],
showing the exact 1/3 asymptotic slack (Certiﬁcate cert04). (b) Sharp bad-round fraction
(2t − 1)/t2 vs. 2/t, exhaustively veriﬁed over all (t + 1) t monotone block proﬁles for t ≤ 5
(Certiﬁcate cert01).
for all r ≥ 2 (Lean thm03, Certiﬁcate cert02).
Proof of (c). A pair (x, y) ∈ S1 × S2 occurs as (maxπ S1, maxπ S2) for some π ∈ Sn if and
only if: (i) x = y ∈ S1 ∩ S2 (c diagonal pairs, realized by placing x ﬁrst in π), or (ii) x ̸= y
and it is not the case that both x ∈ S1 ∩ S2 and y ∈ S1 ∩ S2 (since whichever of two common
elements ranks higher in π dominates the other in both sets; conversely, if x /∈ S2, placing x
above y above all remaining elements realizes (x, y), and symmetrically if y /∈ S1). Subtracting
the c(c − 1) ordered distinct pairs inside (S1 ∩ S2)2 from |S1||S2| = ( p + c)(q + c) proves ( 4)
(Lean thm06).
For the upper bound ( 5), put s = p + q so s + c ≤ n. Two elementary AM–GM inequalities
give 12pq ≤ 3s2 and 4(s + 2)c ≤ (s + 2)2 + 4c2. Adding 8sc + 4c + 4 to their sum yields
4 · 3(pq + sc + c) + 4 ≤ 4
(
(s + c)2 + (s + c) + 2
)
≤ 4(n2 + n + 2),
whence 3(pq + sc + c) ≤ n2 + n + 2 (Lean thm07). Conversely, for every n ≥ 3, writing
n = 3 k + r (k ≥ 1, r ∈ { 0, 1, 2}) and setting (p, q, c) = ( k, k, k) for r = 0 , (k, k, k + 1) for
r = 1 , and (k, k + 1, k + 1) for r = 2 satisﬁes p + q + c = n, p + c ≥ 1, q + c ≥ 1, and achieves
equality pq + (p + q)c + c = ⌊(n2 + n + 2)/3⌋ across all three residue classes (Lean thm08–thm09,
Certiﬁcates cert03–cert04).
3 Polylogarithmic Blowup vs. Geometric-Horizon Parameteri-
zation
Consider a general parameterization of Algorithm 1 of [ 7] at recursion depth d ≥ 1 with block
parameter td ≥ 1 and portal-covering parameter rd = 2 κt3
d for an integer contraction factor
κ ≥ 2. In any call c on nc vertices, each of the tc batch updates adds at most 2nc/rc portals
(even tighter by Theorem 1(b)), so |P| ≤ 2tcnc/rc; summing across all t2
c child calls yields total
child vertices at most t2
c (2tcnc/rc) = nc/κ (Lean thm04). By induction, the total vertex count
nd and total edge count md across all calls at depth d ≥ 1 satisfy
nd ≤ n
κd−1 , m d ≤ m,
∑
c at depth d
√mcnc ≤ √mdnd ≤
√mn
κ(d−1)/2 . (6)
4

--- Page 5 ---
Moreover, since the root graph has no isolated vertices, n ≤ 2m implies n2 ≤ 2mn, so nd ≤√
2mn/κd−1 unconditionally (Lean thm19).
Tracking every constant explicitly without O(·):
• History cardinality (Lemma 3.10 of [ 7]): Using ln(1+x) ≤ √x and Fact 2.1 (
( m+n
n
)
≤
e2√mn, certiﬁed in exact integers via (p + q)m+n ≥
( m+n
n
)
pnqm in Certiﬁcate cert13),
the three components (spokes, forests, and Fredman preference vectors) satisfy ln |Hc| ≤
(2 + 3
√
2) t2
c
√mcnc.
• Total errors Etot (Lemma 3.11 + Claim 3.12 of [ 7]): By Theorem 1(a), the bad-
round fraction is at most (2tc − 1)/t2
c < 2/tc, so the deterministic schedule ρ∗ plus prefer-
ence estimation incur at most
Ec ≤ 2 + 3
√
2
ln 2 t2
c
√mcnc +
(
1 + 2
ln 2
) mc
tc
< 10 t2
c
√mcnc + 4 mc
tc
(7)
errors in call c (Lean thm20 certiﬁes (2 + 3
√
2)/ ln 2 < 10 and 1 + 2 / ln 2 < 4 via
√
2 <
1415/1000 and ln 2 > 693/1000).
• Total edge budget |F| + |U(F)| + ∑
i |Ei|: Combining |F| ≤ n − 1 ≤
√
2mn, |U(F)| ≤
Etot, rejected-edge MSF inputs ≤ Etot, and non-rejected exact MSF inputs ∑
c[(2t2
c +
tc)(nc − 1) + tcr2
c nc] ≤ ∑
d≥1(2t2
d + td + 4κ2t7
d)
√
2mn/κd−1 yields the completely explicit
zero-O(·) bound
|F|+|U(F)|+
ℓ∑
i=1
|Ei| ≤ m
∑
d≥1
8
td
+√mn

√
2 + 20
∑
d≥1
t2
d
κ(d−1)/2 +
√
2
∑
d≥1
4κ2t7
d + 2t2
d + td
κd−1

.
(8)
• Non-MSF comparison budget (zero- O(·)): Each edge enters at most one batch across
the recursion ( ∑ |B| ≤ m). To eliminate all small-input base-case gaps in linear-time
selection [1], deﬁne SELECT(N, k) as merge sort ( ≤ N⌈log2 N⌉ ≤ 10N < 23N comparisons)
for 1 ≤ N < 680, and group-of- 5 median-of-medians for N ≥ 680: computing the median
of each of the g = ⌊N/5⌋ ﬁve-tuples together with its two smaller and two larger elements
requires only 6 comparisons per ﬁve-tuple (pair (a, b) and (c, d), compare winners to
exclude the larger winner above the median, pair the excluded winner’s partner with e,
compare the two remaining pair-winners to exclude the second element above the median,
and compare the remaining two candidates to obtain the exact median; exhaustively
veriﬁed over all 5! = 120 permutations in Certiﬁcate cert09), costing ≤ 6g comparisons;
recursively selecting the median of those g medians uses ≤ 23g, partitioning the N − 1
remaining keys uses N−1, and at least 3⌈g/2⌉ elements lie on each side of the pivot, leaving
a subproblem of size at most N −3⌈g/2⌉ ≤ ⌊ 7N/10⌋+3 (checked directly for every residue
N mod 10 ∈ { 0, . . . , 9}). Hence TPICK(N) ≤ 29⌊N/5⌋ + ( N − 1) + 23( ⌊7N/10⌋ + 3) ≤
23N holds for every N ≥ 1 by strong induction (inductive step machine-checked for all
N ≥ 680 in Lean thm20; base cases N < 680 in Certiﬁcate cert09). In Lemma 3.3
of [ 7], ﬁnding the median ( ≤ 23N) and partitioning ( N − 1) uses < 24N comparisons
per halving level, giving ≤ 48dv on the main recursion spine plus ≤ 48dv across disjoint
quota-1 searches per vertex v, totaling ∑
v 96dv = 192 |B| per batch and ≤ 192m globally,
plus ≤ tdnd ≤
√
2 tdκ−(d−1)/2√
mn′ spoke-update comparisons summed across depth d
(using the root bound nd ≤
√
2mn′/κd−1 so isolated portals in child calls need not satisfy
nc ≤ 2mc). At vertex v (dv ≥ 1), Lemma 3.3 runs ≤ 2r2
c (log2(dv + 1) + 1) ≤ 4r2
c
√dv
successful admissibility tests; two Cauchy–Schwarz steps give ≤ 4
√
2 r2
c
√tcmcnc tests per
call, each checking 2(d−1) spokes at depth d, totaling ≤ 32
√
2 κ2(d−1)t13/2
d κ−(d−1)/2√
mn′
comparisons. Each failed admissibility test scans from the root to its ﬁrst invalid projection
5

--- Page 6 ---
level dc (2dc spoke comparisons), costing ∑
c 2dcEc ≤ m ∑
d≥1
8d
td
+ 20 ∑
d≥1
dt2
d
κ(d−1)/2
√
mn′.
In Claim 3.12 of [ 7], in every round i ∈ {1, . . . , t2
c } of call c, the active edge set is a subset
of the call’s mc edges (requiring no disjointness across rounds) and the preference ground
set has size ≤ 2nc, so ln |A| ≤ 2√2mcnc unconditionally and |S∗| = ⌈2tc(ln |A| + 1)⌉ ≤
6tc
√mcnc + 2 tc + 1 (4
√
2 < 6). Splitting each undirected path-max query at its LCA
into 2 directed ancestor–descendant queries ( |Q| = 2 |S∗|) for Komlós’s non-asymptotic
directed veriﬁcation theorem [ 8, Theorem 1] (valid for all nc ≥ 1 and |Q| ≥ 0, with nc = 1
using 0 ≤ 5 comparisons) takes ≤ 5nc + nc log2(1 + 2 |S∗|/nc) ≤ 5nc + 4|S∗| comparisons
(using log2(1 + x) ≤ 2x), plus |S∗| comparisons to combine each pair of half-path maxima
and at most 3|S∗| spoke/edge comparisons to determine each sampled edge’s preference,
totaling ≤ 5nc + 8|S∗| per round. Summing over all t2
c rounds and all nonempty calls at
depth d (using 5t2
dnd ≤ 5
√
2 t2
d
√
mn′/κd−1 ≤ 8t2
d
√
mn′/κ(d−1)/2 and 1 ≤ √mcnc) yields
≤ (64t3
d + 16t2
d)κ−(d−1)/2√
mn′ comparisons at depth d.
Theorem 2 (Polylogarithmic Factorial Blowup vs. Optimal Geometric-Horizon Stability) .
(a) Factorial blowup of polynomial schedules: For any polynomial schedule td = γdp, con-
vergence of the failed-admissibility comparison series ∑
d≥1 d/td requires p ≥ 3 among
integer exponents. At the KPS parameters (p, κ) = (3 , 4) (td = γd3, rd = 8 t3
d), the domi-
nant MSF and exact successful-admissibility series obey the exact zero-ﬂoat lower bounds
(Lean thm14, Certiﬁcate cert06):
∑
d≥1
d21
4d−1 > 1.547×1017 (peak d = 15) ,
∑
d≥1
(d − 1) d19.5
2d−1 > 5.662×1022 (peak d = 30) .
(9)
(b) Sharp geometric stability domain 1 < ρ < κ 1/13: For the geometric-horizon schedule
td = ⌈γρd−1⌉ (γ ≥ 1, ρ > 1) and rd = 2 κt3
d (κ ≥ 2), all recursion series in (8) and the
non-MSF comparison bound converge simultaneously if and only if
1 < ρ < κ 1/13, (10)
where the admissibility ratio qadm := ρ13/2/√κ < 1 strictly implies the MSF ratio qmsf :=
ρ7/κ < 1 (Lean thm11).
(c) Closed-form rational sums: Writing γ+ := γ +1 so that γρd−1 ≤ td ≤ γ+ρd−1 for all d ≥ 1,
every series in (8) and the comparison bound collapses to an explicit rational function of
(γ, ρ, κ):
∑
d≥1
8
td
≤ 8ρ
γ(ρ − 1),
∑
d≥1
8d
td
≤ 8ρ2
γ(ρ − 1)2 ,
∑
d≥1
t7
d
κd−1 ≤ γ7
+
1 − ρ7/κ,
∑
d≥1
(d − 1) t13/2
d
κ(d−1)/2 ≤ γ13/2
+
(1 − ρ13/2/√κ)2 . (11)
Proof. For (a), ∑
d≥1 d/dp = ζ(p−1) converges iﬀ p > 2, forcing p ≥ 3 among integer exponents.
The partial sums over 1 ≤ d ≤ 60 (for d21/4d−1) and 1 ≤ d ≤ 100 (for (d − 1)d19.5/2d−1,
using exact integer lower bounds ⌊106√
d⌋/106 ≤
√
d) are certiﬁed in Certiﬁcate cert06; even
the single d = 15 term 1521/414 > 1016 and squared d = 30 term 292 · 3039/258 > 1042 (i.e.
29 · 3019.5/229 > 1021) are certiﬁed directly inside Lean thm14. For (b), since td = Θ( ρd−1) and
ρ > 1, the ﬁve series converge iﬀ ρ−1 < 1, ρ2/√κ < 1, ρ7/κ < 1, and ρ13/2/√κ < 1; since ρ > 1,
ρ13 < κ =⇒ ρ7 < ρ 13/ρ6 < κ (Lean thm11) and ρ4 < ρ 13 < κ , making 1 < ρ < κ 1/13 both
necessary and suﬃcient. For (c), since ρd−1 ≥ 1, γρd−1 ≤ ⌈γρd−1⌉ < γρ d−1+1 ≤ (γ+1)ρd−1, and
the closed-form bounds follow directly from ∑
d≥1 qd−1 = (1 −q)−1 and ∑
d≥1 dqd−1 = (1 −q)−2
for 0 < q < 1.
6

--- Page 7 ---
Figure 2: Polylogarithmic factorial blowup vs. geometric-horizon stability (Theo-
rem 2). (a) Per-level recursion terms across depths d ∈ [1, 40]: KPS d3 polynomial terms surge
past 1016 (MSF) and 1021 (admissibility), whereas our geometric schedule (κ = 32 , ρ = 1 .30)
decays monotonically with closed-form MSF sum 1.24. (b) Exact stability phase diagram show-
ing the sharp critical curve ρ = κ1/13 vs. the MSF-only boundary ρ = κ1/7 (Certiﬁcate cert07).
4 Zero- O(·) Borůvka Compression, Master Recurrence, and Cer-
tiﬁcates
Given ( 1) with explicit constant Cε, executing kBor Borůvka phases reduces the non-isolated
vertex count to n′ ≤ n/2kBor (Lean thm05), so using n ≤ 2m,
Cε
√
mn′ ≤ Cε
√
2 2−kBor/2 m.
For a target edge-contraction factor θ ∈ (0, 1) (so ∑
i mi ≤ θm across all recursive exact-MSF
calls plus F ∪U(F)), we require ε < θ and 2C2
ε ≤ (θ−ε)22kBor . Crucially, because Cε ∝ γ7
+ ∝ ε−7,
increasing ε toward θ slashes Cε by a seventh power while tightening (θ−ε) only linearly. Jointly
optimizing (θ, ε, κ, ρ) over exact rational grids (Certiﬁcate cert15) reveals that θ = 1 /2 with
ε = 7 /16, κ = 32 , ρ = 13 /10, γ = 80 minimizes the eﬀective Borůvka master multiplier
kBor/(1 − θ) = 248 .
Theorem 3 (Zero-O(·) Borůvka Compression and Explicit Linear Constant T∗(m, n) ≤ 944 m).
(a) Certiﬁed > 4.779 × 1016× constant reduction and 106-phase Borůvka compression: At
θ = 1 /2, the original KPS d3 parameterization ( ε = 1 /8, κ = 4 , γ = 128 ) satisﬁes
the exact lower bounds CKPS
1/8 > 7.882 × 1033 and kKPS
Bor ≥ 230 (even at its tightened
γ = 77 , C1/8 > 2.247 × 1032 and kBor ≥ 219). By contrast, our geometric-horizon
schedule (ε = 7 /16, κ = 32 , ρ = 13 /10, γ = 80) satisﬁes the exact zero-ﬂoat upper bounds
(Lean thm12–thm16, Certiﬁcate cert08):
Cgeom
7/16 < 1.650×1017,
CKPS
1/8
Cgeom
7/16
> 4.779×1016, k geom
Bor = 124 = kKPS
Bor −106. (12)
(b) Explicit zero- O(·) linear comparison bound: Using 2m comparisons per Borůvka phase,
at most 192m total comparisons for Lemma 3.3 batch selection via our base-case-free
TPICK(N) ≤ 23 N selection bound (all N ≥ 1, Lean thm20), at most 8ρ2
γ(ρ−1)2 m = 169
90 m <
2m comparisons for failed admissibility tests (Lean thm15), strictly fewer than 3m com-
parisons for outer directed Komlós veriﬁcation [ 8, Theorem 1] of U(F) on the contracted
7

--- Page 8 ---
graph G′ with n′ ≤ 2m/2kjoint
Bor vertices (splitting ≤ m undirected edges at their LCA into
≤ 2m directed queries plus 2m half-path comparisons; Lean thm20), and kjoint
Bor = 137
Borůvka phases to simultaneously enforce C7/16
√
mn′ ≤ m/16 and crush the exact sum
Ccomp
√
mn′ of all four
√
mn′ non-MSF comparison tails below 1 · m, the multi-branch
master recurrence T(m) ≤ ∑
i T(mi) + Bm (∑
i mi ≤ m/2, B = 2 kjoint
Bor + 198 = 472 )
yields (Lean thm17–thm18, Certiﬁcate cert09):
T∗(m, n) ≤ 2Bm = 944 m (all m-edge multigraphs without isolated vertices ). (13)
(c) End-to-end zero-ﬂoat graph certiﬁcates: On canonical complete and bipartite weighted
graphs (K8, K12, K16, K20, K6,6, K8,8), exact integer implementations of Borůvka contrac-
tion, Lemma 3.2 portal-spoke batch selection, and cycle-support ﬁltering certify 2n′ ≤ n,
≤ 2m comparisons per Borůvka phase, |P′|r3 ≤ (2r2 −2r+1)n, 77%–90% single-pass edge
elimination, and exact preservation MSF(G) = MSF( G[F ∪ U(F)]) (Certiﬁcates cert10–
cert12).
Proof. Part (a) follows by substituting (ε, κ, ρ, γ) = (7 /16, 32, 13/10, 80) into ( 8) and ( 11)
via exact rational arithmetic: 8·13
80·3 = 13
30 < 7
16 (Lean thm15) and qmsf = 13 7/(32 · 107) =
62,748,517/320,000,000, so exact rational evaluation of (1 − qmsf )−1 = 320 ,000,000/257,251,483
in Certiﬁcate cert08 yields Cgeom
7/16 < 1.650×1017 (while even the coarse bound (1−qmsf )−1 < 5/4
in Lean thm13 and thm16 already certiﬁes Cgeom
7/16 < 1.7 × 1017 and 2(16Cgeom
7/16 )2 < 2124); con-
versely, the 60-term rational lower bound on CKPS
1/8 exceeds 7.882×1033 and violates 2(8CKPS
1/8 /3)2 ≤
2229 (Lean thm16, Certiﬁcate cert08).
For (b), at (κ, ρ, γ) = (32 , 13/10, 80) (γ+ = 81 , γ13/2
+ = 9 ·816, qadm < 98/100 by Lean thm13,
so (1−qadm)−2 < 2500), summing the four explicit
√
mn′ comparison coeﬃcients from Section 3
in exact rational arithmetic (Certiﬁcate cert09) gives
Ccomp = 32
√
2 · 322 · 9 · 816 · 2500  
< 2.9465×1020 (succ. adm.)
+ 20 · 812
(1 − q2)2
  
< 2.67×105
+ 64 · 813
1 − q3
+ 16 · 812
1 − q2  
< 5.58×107
+
√
2 · 81
1 − q1  
< 150
< 2.947 × 1020,
where qj := ρj/
√
32 (j = 1 , 2, 3). Setting kjoint
Bor = 137 certiﬁes 2C2
comp < 2137 (so Ccomp
√
2 2−137/2 <
1) as well as kjoint
Bor ≥ 124. On the contracted graph G′ with n′ ≤ 2m/2137, splitting ≤ m undi-
rected edges at their LCA into |Q| ≤ 2m directed queries for Komlós’s directed veriﬁcation
theorem [ 8, Theorem 1] and testing each edge weight against both half-path maxima takes at
most
5n′ + n′ log2
(
1 + 2m
n′
)
+ 2m ≤
(
2 + 2(5 + 138)
2137
)
m < 3m
comparisons (Lean thm20, since 1 + 2 m/n′ ≤ 2138 at n′ = 2 m/2137 and x log2(1 + 2 /x) is
increasing on (0, 2/2137]). Adding all per-level comparisons ( 2 · 137 = 274 Borůvka, 192 ﬁrst-
principles BFPRT batch selection, 2 failed admissibility via 169/90 < 2, 3 outer directed Komlós
veriﬁcation, 1
√
mn′ tail) gives B = 472 . By constructive strong induction (Lean thm18), any
function T : N → N with T(0) = 0 and T(m) ≤ ∑
i T(mi) + Bm whenever 2 ∑
i mi ≤ m
satisﬁes T(m) ≤ 2Bm = 944 m. Part (c) is directly certiﬁed by exact integer executions in
Certiﬁcates cert10–cert12.
8

--- Page 9 ---
Table 1: Zero-O(·) comparison of polynomial KPS schedules [ 7] vs. geometric-horizon schedules
at θ = 1 /2 (Certiﬁcates cert08 and cert15). KPS values are exact rational lower bounds
(60-term partial sum); geometric values are exact rational upper bounds.
Schedule family ε κ ρ γ C ε (exact bound) kBor kBor/(1 − θ)
KPS td = γd3 (baseline) 1/8 4 — 128 > 7.882 × 1033 ≥ 230 ≥ 460
KPS td = γd3 (tight γ) 1/8 4 — 77 > 2.247 × 1032 ≥ 219 ≥ 438
Geometric (KPS κ, ε) 1/8 4 27 /25 864 < 5.742 × 1022 156 312
Geometric (opt κ, ρ) 1/8 32 13 /10 278 < 9.488 × 1020 144 288
Geometric (mid ε) 3/8 32 13 /10 93 < 4.676 × 1017 125 250
Geometric (optimal) 7/16 32 13 /10 80 < 1.650 × 1017 124 248
Geometric ( κ = 64) 7/16 64 27 /20 71 < 2.666 × 1017 125 250
Figure 3: Borůvka phase compression and end-to-end graph certiﬁcates (Theorem 3).
(a) Certiﬁed Borůvka phases kBor and log10 Cε across polynomial KPS baselines vs. geometric-
horizon schedules, showing the 106-phase reduction and > 4.779 × 1016× constant compression
(Certiﬁcate cert08). (b) Single-pass cycle-support edge elimination ( 77%–90% discarded) with
exact MSF invariance veriﬁed on K12, K16, K20, and K8,8 (Certiﬁcate cert12).
Remark 1 (Scope of the 944 m Comparison Bound) . The explicit constant T∗(m, n) ≤ 944 m
in ( 13) bounds edge-weight comparisons (the decision-tree depth T∗(m, n)) with zero hidden
asymptotic factors for all m, n ≥ 1: our linear-time selection bound TPICK(N) ≤ 23 N is proved
from ﬁrst principles for every N ≥ 1 (Section 3 and Lean thm20), while path-maximum veriﬁca-
tion consistently imports Komlós’s explicit non-asymptotic Theorem 1 [ 8] ( ≤ 5n′ + n′ log2(1 +
|Q|/n′) comparisons for |Q| directed ancestor–descendant path-maximum queries on an n′-vertex
rooted forest, valid for all n′ ≥ 1 and |Q| ≥ 0, with n′ = 1 trivial; undirected queries are split at
their LCA into two directed queries). Translating T∗(m, n) to uniform pointer-machine running
time via Pettie and Ramachandran [ 9] multiplies by their table-lookup overhead, which remains
O(1) independently of (m, n).
5 Formal Veriﬁcation Architecture and Scope
Our veriﬁcation artifact strictly separates machine-checked constructive proofs from prose deriva-
tions and exact rational certiﬁcates:
• Layer 1 — Constructive Lean 4.36.0 Kernel (lean/DeterministicLinearMst.lean):
Twenty theorems compiled with lean-DwarningAsError=true, zero external imports,
zero sorry, zero grind, zero Classical.choice, and zero custom axioms (audited via
9

--- Page 10 ---
#print axioms). Layer 1 formalizes the exact 2t − 1 bad-round ceiling and attainment
(thm01–thm02), the sharpened greedy portal bound (a + u)r3 ≤ (2r2 − 2r + 1)n (thm03),
exact vertex contraction and Borůvka halving ( thm04–thm05), the exact pairwise Fredman
identity, pure-N AM–GM upper bound 3(|X|) ≤ n2 + n + 2, exact attainment across all
n ≥ 3, 2/3 asymptotic gap, and ﬁnite table ( thm06–thm10), the critical stability implica-
tion ρ13 < κ =⇒ ρ7 < κ (thm11), exact stability, geometric sum, polylogarithmic blowup
(1521/414 > 1016 and 292·3039 > 1042·258), error budget, and Borůvka compression inequal-
ities ( thm12–thm16), constructive strong-induction proofs of the binary and arbitrary-list
master halving recurrences ( thm17–thm18), non-isolated vertex bound ( thm19), and exact
error-coeﬃcient, outer Komlós overhead, and all- N ≥ 680 BFPRT selection inductive-
step bounds ( thm20). The underlying correctness of Algorithm 1 of [ 7] (admissibility
backward induction, Claim 3.12 sampling existence, Komlós’s non-asymptotic veriﬁcation
theorem [ 8, Theorem 1], and Pettie–Ramachandran reduction) is cited from [ 7, 8, 9] and
validated end-to-end on ﬁnite instances in Layer 2.
• Layer 2 — Zero-Float Python Veriﬁer (verification/verify_deterministic_
linear_mst.py): An AST-audited pure standard-library veriﬁer using strictly int and
Fraction (zero ﬂoats, zero numeric /, zero **, zero limit_denominator), emitting 16
SHA-256 certiﬁcates ( cert01–cert15 plus the cross-checked master summary cert16) in
certificates/MANIFEST.json and validated by 56 adversarial pytest checks in tests/
test_adversarial.py. Layer 2 exhaustively checks all (t + 1)t monotone block proﬁles
(t ≤ 5), exhaustively checks all
( 2n−1+1
2
)
subset pairs ( n ≤ 5) and small- m Fredman max-
ima, computes exact 60- and 100-term rational partial sums for the KPS polylogarithmic
blowup (including the exact admissibility series (d − 1)d19.5/2d−1), certiﬁes exact rational
Cε, kBor, Ccomp, the 6-comparison median-of- 5 circuit over all 5! = 120 permutations,
BFPRT base cases N < 680, and KMST = 944 , and runs exact Borůvka, portal-spoke,
and cycle-support ﬁltering checks on canonical complete and bipartite graphs.
References
[1] M. Blum, R. W. Floyd, V. Pratt, R. L. Rivest, and R. E. Tarjan, Time bounds for selection ,
J. Comput. System Sci. 7 (1973), no. 4, 448–461.
[2] O. Borůvka, O jistém problému minimálním , Práce Moravské přírodovědecké společnosti
3 (1926), no. 3, 37–58.
[3] B. Chazelle, A minimum spanning tree algorithm with inverse-Ackermann type complexity ,
J. ACM 47 (2000), no. 6, 1028–1047.
[4] M. L. Fredman and R. E. Tarjan, Fibonacci heaps and their uses in improved network
optimization algorithms , J. ACM 34 (1987), no. 3, 596–615.
[5] R. L. Graham, A. C. Yao, and F. F. Yao, Information bounds are weak in the shortest
distance problem , J. ACM 27 (1980), no. 3, 428–444.
[6] D. R. Karger, P. N. Klein, and R. E. Tarjan, A randomized linear-time algorithm to ﬁnd
minimum spanning trees , J. ACM 42 (1995), no. 2, 321–328.
[7] S. Khanna, A. Putterman, and J. Song, A deterministic linear time algorithm for mini-
mum spanning tree , Electronic Colloquium on Computational Complexity (ECCC), Report
No. 339, November 23, 2026.
[8] J. Komlós, Linear veriﬁcation for spanning trees , Combinatorica 5 (1985), no. 1, 57–65.
10

--- Page 11 ---
[9] S. Pettie and V. Ramachandran, An optimal minimum spanning tree algorithm , J. ACM
49 (2002), no. 1, 16–34.
[10] A. C.-C. Yao, An O(|E| log log |V |) algorithm for ﬁnding minimum spanning trees , Inform.
Process. Lett. 4 (1975), no. 1, 21–23.
11
