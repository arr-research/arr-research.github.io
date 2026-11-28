# Sharpened Discrete Min-Cut Recurrences, Conflict-Chromatic Omega(1/d^2) Flexibility, and Universal Mutual-Exclusion Gadgets for d-Degenerate List Coloring

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-2D22NKE9TE90NT7R | v1 | 2026-11-28
Sharpened Discrete Min-Cut Recurrences,
Conflict-Chromatic Ω(1/d2) Flexibility, and Universal
Mutual-Exclusion Gadgets for d-Degenerate List
Coloring
Lluis Eriksson
Independent Researcher (lluiseriksson@gmail.com)
Public Repository: https://github.com/arr-research/arr-research.github.io
November 28, 2026
Abstract
Adak, Chandran, Gupta, Kaiser, Kalyanasundaram, Mathew, Nanoti, Sahoo, Shankar,
and Thomas (arXiv:2611.34348v1) recently proved three landmark results on flexible list
coloring of d-degenerate graphs: (d + 2, 1 (d+1)(d2 +d+1) )-flexibility (Theorem 1), (2d, 1 d+1 )-
flexibility (Theorem 2), and (⌊(d+2)(2−1/e)⌋, 1 d+1 )-flexibility (Theorem 3, strictly improving
2d for d ≥ 9), together with a 7-vertex 2-degenerate gadget refuting (3, 1/3)-flexibility. We
prove four new structural, probabilistic, and extremal theorems strictly advancing their
framework and directly addressing their open questions: (1) a Sharpened Discrete Min-
Cut Recurrence and Padé Shift Theorem eliminating the double-counting of r(uj ) in Adak
et al.’s Claim 9 via the exact indicator identity p − 1/M ≤ (1 − 1/M )p, yielding for every
k ≥ d+M the exact discrete criterion (d+2−1/M )(1−(1−1/M )max(0,d−k+S+M )) ≤ S for all
S ∈ {1, . . . , d} and a Padé denominator shift − ln(1−1/M ) < (M −1/2−1/(6M ))−1 (M ≥ 2);
this lowers the sub-2d crossover threshold for optimal ratio ϵ = 1/(d + 1) from d ≥ 9 to d ≥ 8
(k = 15 < 16), strictly improves min(2d, ⌊(d + 2)(2 − 1/e)⌋) on 50/93 (53.8%) of all integers
d ∈ [8, 100], and extends verbatim to weighted requests; (2) a Generalized s-Rank Global
Palette-Order Theorem proving that for every d ≥ 1, s ≥ 1, and monochromatic conflict
subgraph Hr = ( ˆV , {uv ∈ E(G[ ˆV ]) : r(u) = r(v)}), every d-degenerate graph is weighted
(d+1+s, s χ(Hr )(1+d(d+s)) )-flexible—recovering Adak et al.’s Theorem 1 at s = 1, χ(Hr ) ≤ d+1
and jumping to Ω(1/d2) for all bounded-conflict request assignments (including every proper
request coloring χ(Hr ) = 1); (3) a Universal All-d Mutual-Exclusion Family Gd on 2d + 3
vertices with (d + 1)-lists and 4 requests satisfying at most 1 request for every d ≥ 2,
generalizing Adak et al.’s d = 2 gadget uniformly to all degeneracies and ruling out (d + 1, ϵ)-
flexibility for every ϵ > 1/4 (while leaving (d + 1, 1/(d + 1)) open for d ≥ 3); and (4) a Sharp
Forest Double-Optimum and Claim 9 Criterion Asymptotic Theorem constructively proving
every 1-degenerate graph is weighted (2, 1/2)-flexible and proving that the exact asymptotic
limit of the suﬀicient Claim 9 min-cut criterion is (2 − 1/e)d. Twenty core theorems (T01–
T20) are formally verified in Lean 4.36.0 (0 sorry, 0 grind, 0 custom axioms), paired
with an AST-pure zero-float exact-Q/Z verifier, 16 canonical SHA-256 certificates, and 73
passing adversarial tests.
1 Introduction
List coloring, introduced independently by Vizing [9] and Erdős, Rubin, and Taylor [7], assigns
each vertex v ∈ V (G) a list L(v) of admissible colors and seeks a proper coloring f with
f (v) ∈ L(v). Dvořák, Norin, and Postle [6] introduced flexible list coloring as a quantitative
relaxation of precoloring extension [2]: given a k-list assignment L and a request function
r : ˆV → ∪ v L(v) on a nonempty domain ˆV ⊆ V (G) with r(v) ∈ L(v), a graph G is (k, ϵ)-flexible
1
```

---

## Page 2

```text
if there exists a proper L-coloring f satisfying f (v) = r(v) for at least ϵ| ˆV | vertices v ∈ ˆV .
More generally, G is weighted (k, ϵ)-flexible [6, 3] if for every non-negative weight function
w : ˆV → R≥0, some proper L-coloring satisfies at least ϵ ∑ v∈ ˆV w(v) of the total request weight.
A graph G is d-degenerate [5] if it admits a degeneracy ordering v1, . . . , vn such that each
vi has at most d backward neighbors in {v1, . . . , vi−1}. Every d-degenerate graph is (d + 1)-
choosable, and Kd+1 with identical lists and identical requested color forces k ≥ d+1 and ϵ ≤ 1 d+1
(Lean T15). Following Dvořák–Norin–Postle [6], Kaul et al. [8] (who proved (d + 2, 2−(d+1))-
flexibility), and Cambie–Cames van Batenburg–Davies–Kang [4, 3], Adak et al. [1] recently
proved three major theorems:
• (d + 2, 1 (d+1)(d2+d+1) )-flexibility [1, Theorem 1], improving ϵ from inverse-exponential to
inverse-cubic;
• (2d, 1 d+1 )-flexibility [1, Theorem 2] and (⌊(d + 2)(2 − 1/e)⌋, 1 d+1 )-flexibility [1, Theorem 3],
strictly beating 2d for every d ≥ 9;
• a 7-vertex 2-degenerate gadget [1, Proposition 10] refuting (3, 1/3)-flexibility.
Advancing [1], we resolve four structural questions: (1) tightening the Claim 9 min-cut recur-
rence and logarithmic conversion to lower the sub-2d crossover threshold below d = 9 and strictly
beat min(2d, ⌊(d + 2)(2 − 1/e)⌋) across a majority of degeneracies; (2) generalizing the global
random palette-order argument to arbitrary list surplus s = k − (d + 1) and conflict chromatic
number χ(Hr) to break the Θ(1/d3) barrier to Ω(1/d2); (3) lifting the d = 2 mutual-exclusion
gadget to an explicit (2d + 3)-vertex d-degenerate family for every d ≥ 2; and (4) establishing
the exact d = 1 forest double-optimum and the asymptotic flow-framework barrier (2 − 1/e)d.
2 Main Results
2.1 Theorem 1: Sharpened Discrete Min-Cut Recurrence and Padé Shift
Recall the inductive probability-distribution framework of [1, Section 4]. Along a d-degeneracy
ordering v1, . . . , vn, let Gi := G[{v1, . . . , vi}] and Ci be the set of proper L-colorings of Gi. We
maintain a distribution on Ci satisfying:
• Property 3: For every c ∈ L(vi), Pr[f (vi) = c] ≤ 1 d+1 , with equality at c = r(vi).
• Property 4: For every c ∈ L(vi) \ {r(vi)} and every C ∈ Ci−1, Pr[f (vi) = c | C] ≤ 1 M .
By linearity of expectation, a distribution on Cn with Property 3 satisfies
E

∑
v∈ ˆV
w(v)1f (v)=r(v)

 = 1 d + 1 ∑
v∈ ˆV
w(v)
for every weight function w ≥ 0, immediately yielding weighted (k, 1 d+1 )-flexibility (Lean T14).
In [1, Claim 9], letting u1, . . . , um (m ≤ d) be the backward neighbors of vi in degeneracy
order (uj = vtj ), S ⊆ L(vi) with |S| ≤ d, Uj := (L(vi) \ S) \ {f (u1), . . . , f (uj )}, Xj := |Uj |,
and Yj := min(M, Xj ), Adak et al. bound |Uj−1 \ {r(uj )}| loosely by Xj−1, giving E[Yj ] ≥
(1 − 1 M )E[Yj−1] − 1 d+1 . Retaining the exact −1 when r(uj ) ∈ Uj−1 via our indicator identity
p − 1 M ≤ (1 − 1 M )p sharpens Claim 9 and eliminates the crude ln(1 + 1 M −1 ) ≤ 1 M −1 conversion.
Theorem 1 (Sharpened Discrete Min-Cut Recurrence and Padé Shift). Let d ≥ 1, M ≥ 2, and
k ≥ d + M be integers satisfying:
1. (List-Capacity Margin.) k ≥ d + M (which guarantees both Property 4 feasibility M d ≤
(d + 1)(k − 1) via Lean T19 and k − |S| − M ≥ 0 for every |S| ≤ d).
2
```

---

## Page 3

```text
2. (Exact Discrete Min-Cut Criterion.) For every integer S ∈ {1, . . . , d}, setting ℓ(S) :=
max(0, d + S + M − k),
(
d + 2 − 1 M )( 1 − ( 1 − 1 M )ℓ(S)) ≤ S, (1)
equivalently in exact cleared integers,
(
(d + 2)M − 1
)(
M ℓ(S) − (M − 1)ℓ(S)) ≤ S · M ℓ(S)+1. (2)
Then every d-degenerate graph is weighted (k, 1 d+1 )-flexible. Moreover:
(a) (Padé Log Shift.) For every M ≥ 2, − ln(1 − 1/M ) < 1 M −1/2−1/(6M ) < 1 M −1 (Lean T16,
C04), strictly tightening the exponential conversion denominator of [1] by a shift 1 2 − 1 6M ∈
[ 5 12 , 1 2 ).
(b) (Crossover Drop and Strict Improvement Density.) Criterion (2) (with k ≥ d + M ) lowers
the sub-2d crossover threshold for ϵ = 1 d+1 from d ≥ 9 [1] to d ≥ 8, certifying weighted
(15, 1/9)-flexibility at d = 8 with M = 3 (Lean T04, T17, C01). Across d ∈ [8, 100], (2)
strictly improves min(2d, ⌊(d + 2)(2 − 1/e)⌋) on 50 of 93 integers (53.8%), including
d ∈ {8, 10, 11, 13, 14, 16, 17, 19, 21, 22, 24, 25, . . . } (Lean T04, T20, C01–C05; Fig. 1).
Proof. As in [1, Section 4], extend r arbitrarily to V (G) \ ˆV with weight w(v) := 0 for all v /∈ ˆV ,
and let C0 consist of the unique empty coloring of G0 = ∅. At i = 1, giving r(v1) probability
1
d+1 and each other color probability d (d+1)(k−1) satisfies Property 4 because k ≥ d + M implies
M d ≤ (d + 1)(k − 1) (Lean T19). For i ≥ 2, because k ≥ d + M ensures |AC | ≥ k − d ≥ M
for every C ∈ Ci−1, [1, Claim 8 & Eq. (10)] guarantee a flow of value 1 in Hi (and hence a
distribution on Ci satisfying Properties 3 and 4) whenever for every S ⊆ L(vi) with 1 ≤ |S| ≤ d,
|S|
d + 1 ≥ 1 − E[Ym] M . (3)
We sharpen [1, Claim 9] for every j ∈ {1, . . . , m}, where uj = vtj (1 ≤ t1 < · · · < tm < i).
Fix any coloring C ∈ Ctj −1 (well-defined including at j = 1, where t1 − 1 ≥ 0) and set p :=
Pr[f (uj ) = r(uj ) | C] ∈ [0, 1]. Note that u1, . . . , uj−1 ∈ V (Gtj −1), so Uj−1, Xj−1, and Yj−1 are
deterministic given C.
• If Xj−1 > M , then Xj ≥ M , so Yj−1 − Yj = 0 ≤ Yj−1 M + (1 − 1 M )p.
• If Xj−1 ≤ M (so Yj−1 = Xj−1) and r(uj ) /∈ Uj−1, then every color in Uj−1 is non-requested
at uj , so Property 4 gives E[Yj−1 − Yj | C] ≤ Yj−1 M ≤ Yj−1 M + (1 − 1 M )p.
• If Xj−1 ≤ M and r(uj ) ∈ Uj−1, then |Uj−1 \ {r(uj )}| = Yj−1 − 1 exactly. Applying
Property 4 to the Yj−1 − 1 non-requested colors yields
E[Yj−1 − Yj | C] ≤ Yj−1 − 1 M + p = Yj−1 M + ( p − 1 M ) ≤ Yj−1 M + ( 1 − 1 M ) p,
where p − 1 M ≤ (1 − 1 M )p holds identically for all p ∈ [0, 1] (proved in cleared integers in
Lean T01).
In all three cases, taking expectation over C ∈ Ctj −1 and applying Property 3 (E[p] = 1 d+1 ) gives
E[Yj ] ≥
(
1 − 1 M ) E[Yj−1] − ( 1 − 1 M ) 1 d + 1 . (4)
3
```

---

## Page 4

```text
Figure 1: Theorem 1 (Exact Discrete Min-Cut Gains). (a) Exact list-size ceiling k for
weighted (k, 1 d+1 )-flexibility vs. Adak et al. Theorems 2 and 3, highlighting the sub-2d crossover
drop from d = 9 to d = 8 (k = 15 < 16). (b) Cumulative strict-improvement frequency over
min(2d, ⌊(d + 2)(2 − 1/e)⌋), staying above 50% across d ∈ [8, 100] (50/93 = 53.8%).
If m ≤ k − |S| − M , then Xm ≥ k − m − |S| ≥ M , so Ym = M and (3) holds trivially. Otherwise,
j0 := k − |S| − M ≥ 0 (by hypothesis k ≥ d + M ≥ |S| + M !), Yj0 = M (with X0 = k − |S| ≥ M
if j0 = 0), and applying (4) at most ℓ = d − k + |S| + M times using the exact geometric
telescoping identity ∑ℓ−1 r=0(1 − 1 M )r = M (1 − (1 − 1 M )ℓ) (Lean T02–T03) yields
E[Ym] ≥ M
(
1 − 1 M )ℓ − M − 1 d + 1 ( 1 − ( 1 − 1 M )ℓ) .
Dividing by M and subtracting from 1 gives
1 − E[Ym] M ≤ ( 1 + 1 − 1/M d + 1 )( 1 − ( 1 − 1 M )ℓ) = d + 2 − 1/M d + 1 ( 1 − ( 1 − 1 M )ℓ) ,
so (1) implies (3) for all |S| ∈ {1, . . . , d}.
For part (a), set x := 1/M ∈ (0, 1/2] and define g(x) := x 1−x/2−x2/6 + ln(1 − x). Clearly
g(0) = 0, and differentiating on (0, 1/2] yields
g′(x) = 1 + x2/6 (1 − x/2 − x2/6)2 − 1 1 − x = x2(9 − 12x − x2) 36(1 − x)(1 − x/2 − x2/6)2 .
For every x ∈ (0, 1/2], 9 − 12x − x2 ≥ 9 − 6 − 1/4 = 11/4 > 0, while both denominator factors
are strictly positive (1 − x ≥ 1/2 and 1 − x/2 − x2/6 ≥ 17/24). Hence g′(x) > 0 on (0, 1/2],
proving g(1/M ) > g(0) = 0, i.e., − ln(1 − 1/M ) < (M − 1/2 − 1/(6M ))−1 for every M ≥ 2
(denominator dominance over (M − 1)−1 is verified in Lean T16, with exact rational Taylor
checks in C04). Part (b) follows by exact integer evaluation of (2) with k ≥ d + M (Lean T04,
T17, T20; certificates C01–C05, C15).
2.2 Theorem 2: Generalized s-Rank Global Palette-Order Flexibility and
Ω(1/d2) Jump
Adak et al. [1, Theorem 1] proved (d + 2, 1 (d+1)(d2+d+1) )-flexibility by coloring a single indepen-
dent set of ˆV with a uniformly random global color ordering. We generalize their argument
4
```

---

## Page 5

```text
simultaneously to arbitrary list surplus s ≥ 1 (k = d + 1 + s) and monochromatic conflict
chromatic number χ(Hr)—directly resolving the Θ(1/d3) vs. Ω(1/d2) open question for every
bounded-conflict request assignment!
Theorem 2 (Generalized s-Rank Palette-Order Flexibility and Ω(1/d2) Conflict Bound). Let G
be a d-degenerate graph (d ≥ 1), s ≥ 1 an integer, L a (d+1+s)-list assignment, r : ˆV → ∪ v L(v)
a request function, and w : ˆV → R≥0 any weight function. (For d = 0, G is edgeless and trivially
weighted (k, 1)-flexible for all k ≥ 1.) Define the monochromatic conflict subgraph
Hr :=
( ˆV , {uv ∈ E(G[ ˆV ]) : r(u) = r(v)} ) .
Then there exists a proper L-coloring f of G satisfying at least a fraction
ϵ(d, s, Hr) := s χ(Hr) ( 1 + d(d + s) ) (5)
of the total request weight ∑ v∈ ˆV w(v). In particular:
1. Since Hr ⊆ G is d-degenerate, χ(Hr) ≤ d + 1, giving unconditional weighted
(
d + 1 +
s, s (d+1)(1+d(d+s)) ) -flexibility (recovering Adak et al. [1, Theorem 1] at s = 1, Lean T08).
2. Whenever χ(Hr) = O(1) (in particular, for every proper request assignment where χ(Hr) =
1, or bipartite monochromatic conflicts where χ(Hr) ≤ 2), list size k = d+2 (s = 1) already
achieves weighted Ω(1/d2)-flexibility: ϵ ≥ 1 χ(Hr )(d2+d+1) (Fig. 2, certificates C06–C08).
Proof. Fix a d-degeneracy ordering v1, . . . , vn of G, and partition ˆV into χ(Hr) independent
sets of Hr; by averaging, pick a color class I ⊆ ˆV of Hr carrying weight ∑ v∈I w(v) ≥ 1
χ(Hr )
∑
v∈ ˆV w(v). Crucially, because I is independent in Hr, NO two adjacent vertices in I
share the same requested color!
Sample a uniformly random linear ordering π of the full palette P = ∪ v∈V L(v). For each
vertex v ∈ I, let N −(v) be its backward neighbors in G (|N −(v)| ≤ d), and define the active
conflict-color union
Wv := {r(v)} ∪
∪
u∈N −(v) : r(v)∈L(u)
(
L(u) \ {r(v)}
)
.
Every backward neighbor u ∈ N −(v) with r(v) ∈ L(u) satisfies |L(u) \ {r(v)}| = (d + 1 + s) − 1 =
d + s, whereas any backward neighbor with r(v) /∈ L(u) can never have r(v) forbid a color of
L(u). Hence |Wv| ≤ 1 + d(d + s) unconditionally (Lean T07).
Define the precolored subset Iπ ⊆ I as the set of vertices v ∈ I such that at most s − 1
colors of Wv strictly precede r(v) under π. Assign f (v) := r(v) for every v ∈ Iπ (which is
proper because Iπ ⊆ I has no monochromatic edges), and then color V (G) \ Iπ greedily in the
degeneracy order v1, . . . , vn, choosing at each u /∈ Iπ any color in L(u) not already used by its
backward neighbors or by its precolored forward neighbors in N +(u) ∩ Iπ. For any u /∈ Iπ and
any precolored forward neighbor v ∈ N +(u) ∩ Iπ with r(v) ∈ L(u), we have L(u) ⊆ Wv. By our
Subset Rank-Preservation Lemma (Lean T05), the number of colors in L(u) strictly preceding
r(v) under π is at most the number of colors in Wv strictly preceding r(v), which is at most s−1.
Consequently, every precolored forward neighbor v ∈ N +(u) ∩ Iπ whose requested color lies in
L(u) occupies one of the same π-first s colors of L(u). Thus all precolored forward neighbors of
u collectively forbid at most s colors of L(u). Together with at most d backward neighbors, at
most d + s colors of L(u) are forbidden, leaving at least (d + 1 + s) − d − s = 1 available color
for u (Lean T06), so the greedy extension always succeeds.
Finally, since π induces a uniformly random ordering on Wv, the probability that r(v) ranks
among the first s elements of Wv is min(1, s/|Wv|) ≥ s 1+d(d+s) ! Taking expectation over π yields
a proper L-coloring satisfying weight at least s 1+d(d+s) ∑ v∈I w(v) ≥ s χ(Hr )(1+d(d+s)) ∑ v∈ ˆV w(v).
5
```

---

## Page 6

```text
Figure 2: Theorem 2 (Ω(1/d2) Bounded-Conflict Jump and s-Rank Scaling). Com-
parison of weighted satisfaction ratios ϵ on log scale: proper requests (χ(Hr) = 1, green) and
bipartite conflicts (χ(Hr) = 2, blue) break Adak et al.’s Θ(1/d3) curve (orange) by a full factor
of d + 1 at k = d + 2, while surplus s = 3 (k = d + 4, purple) scales linearly in s.
2.3 Theorem 3: Universal All-d 4-Request Mutual-Exclusion Family Gd
Adak et al. [1, Proposition 10] exhibited a single 7-vertex 2-degenerate graph with 3-lists and 4
requests admitting at most 1 satisfied request, refuting (3, 1/3)-flexibility. We lift this construc-
tion to an explicit (2d + 3)-vertex d-degenerate family Gd for every integer d ≥ 2.
Theorem 3 (Universal All-d Mutual-Exclusion Family Gd). For every integer d ≥ 2, let Gd
be the graph on 2d + 3 vertices partitioned as {v1} ∪ A ∪ {v4} ∪ B ∪ {v7} with |A| = |B| = d
(A = {a1, . . . , ad}, B = {b1, . . . , bd}) and edges:
• A ∼= Kd and B ∼= Kd;
• v1 is adjacent to all of A ∪ B;
• v4 is adjacent to all of A ∪ (B \ {bd});
• v7 is adjacent to all of B.
Let the palette be {a, b, c, dcol} ∪ E with |E| = d − 2 (total size d + 2), assign (d + 1)-lists
L(v1) = {a, b, c} ∪ E, L(ai) = L(v7) = {a, b, dcol} ∪ E, L(v4) = L(bj ) = {a, c, dcol} ∪ E, and
place 4 requests r(v1) = a, r(v4) = dcol, r(bd) = a, r(v7) = dcol. Then for every d ≥ 2:
1. Gd is d-degenerate (verified universally in Lean T09, C12).
2. Every proper L-coloring of Gd satisfies at most 1 of the 4 requests (and 1 is achiev-
able), proving that no universal (d + 1, ϵ)-flexibility can hold for any ϵ > 1/4 (Fig. 3,
certificates C09–C11).
Proof. Part 1: In the ordering (v1, a1, . . . , ad, v4, b1, . . . , bd−1, bd, v7), the backward degrees are
0, i (1 ≤ i ≤ d), d, j + 1 (1 ≤ j ≤ d − 1), d, and d, all at most d (Lean T09).
Part 2: We rule out all
(4
2
)
= 6 pairs of simultaneous requests using our constructive
Pigeonhole Clique Impossibility Theorem (no Km+1 can be properly colored with m colors,
Lean T10, T12):
6
```

---

## Page 7

```text
1. {v1 = a, bd = a}: impossible because v1bd ∈ E(Gd).
2. {v1 = a, v4 = dcol}: every ai ∈ A loses both a and dcol, leaving only (d + 1) − 2 = d − 1
colors {b} ∪ E for the clique A ∼= Kd, impossible by T10.
3. {v1 = a, v7 = dcol}: every bj ∈ B loses both a and dcol, leaving only d − 1 colors {c} ∪ E
for B ∼= Kd, impossible by T10.
4. {v4 = dcol, bd = a}: every vertex of the (d − 1)-clique B′ := B \ {bd} loses both a and dcol,
leaving exactly d − 1 colors {c} ∪ E; hence B′ must use all of {c} ∪ E, so B = B′ ∪ {bd}
uses all d colors {a, c} ∪ E, forcing v1 to take its unique remaining color b! Then every
ai ∈ A loses b (from v1) and dcol (from v4), leaving only d − 1 colors {a} ∪ E for A ∼= Kd,
impossible by T10.
5. {v4 = dcol, v7 = dcol}: every vertex of B ∼= Kd loses dcol (from v7), leaving exactly d colors
{a, c} ∪ E, so B uses all of {a, c} ∪ E, forcing v1 = b! As in case 4, A ∼= Kd is left with
only d − 1 colors {a} ∪ E, impossible by T10.
6. {bd = a, v7 = dcol}: B′ ∼= Kd−1 loses a and dcol, forcing B′ to use all of {c} ∪ E, hence B
uses {a, c} ∪ E and forces v1 = b. Meanwhile v4 is adjacent to all of B′, losing {c} ∪ E and
leaving v4 ∈ {a, dcol}, while every ai ∈ A loses b from v1, leaving L(ai) \ {b} = {a, dcol} ∪ E.
Thus the (d + 1)-clique A ∪ {v4} ∼= Kd+1 has union of available colors {a, dcol} ∪ E of size
d < d + 1, impossible by T10.
At d = 2, G2 reproduces [1, Proposition 10] (proved directly without brute force in Lean T11)
and gives 1/4 < 1/3, refuting (3, 1/3)-flexibility. Moreover, 1 satisfied request is achievable for
every d ≥ 2 via the explicit proper L-coloring f (v1) = a, f (v4) = c, f (A) = {b, dcol} ∪ E (d
distinct colors), f (B \ {bd}) = {dcol} ∪ E (d − 1 distinct colors), f (bd) = c, and f (v7) = b,
which satisfies every list and adjacency constraint and grants r(v1) = a. For d ∈ {2, 3, 4}, exact
backtracking confirms max sat(Gd) = 1 (C09–C11).
Remark 1 (Honest Status at k = d + 1 for d ≥ 3). Because 1/4 ≥ 1/(d + 1) for all d ≥ 3,
Gd rules out (d + 1, ϵ)-flexibility for every ϵ > 1/4 uniformly for all d ≥ 2, while whether
(d + 1, 1 d+1 )-flexibility fails for d ≥ 3 remains open.
2.4 Theorem 4: Sharp Forest Double-Optimum and Claim 9 Criterion
Asymptotics
Theorem 4 (Sharp Forest Double-Optimum and Claim 9 Asymptotic Limit). 1. (Exact
d = 1 Double-Optimum.) Every 1-degenerate graph (forest) G is weighted (2, 1/2)-
flexible, simultaneously attaining the extremal limits k = d + 1 = 2 and ϵ = 1 d+1 = 1 2 , via
a linear-time constructive pair (C1, C2) of proper L-colorings with L(v) = {C1(v), C2(v)}
for all v ∈ V (G) (T13–T14, C13–C14).
2. (Exact Asymptotic Limit of the Claim 9 Criterion.) For every d ≥ 1, let k∗(d) denote the
minimum integer k for which there exists M ≥ 2 with k ≥ d + M satisfying Criterion (1).
Then
k∗(d) =
(
2 − 1 e ) d + O(1), lim d→∞ k∗(d) d = 2 − 1 e ≈ 1.63212 (C16).
Thus, improving the leading constant below 2 − 1/e requires strengthening the suﬀicient
Claim 9 min-cut criterion (1) itself.
7
```

---

## Page 8

```text
Figure 3: Theorems 3 and 4 (Universal Family Gd and Minimal-List Landscape).
(a) Our 9-vertex 3-degenerate graph G3 (4-lists, 4 red request vertices) satisfying at most 1
request. (b) Extremal flexibility landscape at minimal list size k = d + 1: Theorem 4 achieves
(2, 1/2) at d = 1, Theorem 3 enforces ϵ ≤ 1/4 for all d ≥ 2 (refuting (3, 1/3) at d = 2).
Proof. Part 1: Root each tree component of G and color in BFS order. For a root r0 with
L(r0) = {c1, c2}, set C1(r0) = c1, C2(r0) = c2. For any non-root v with parent u already assigned
u1 ̸= u2 and L(v) = {c1, c2} (c1 ̸= c2), if c1 ̸= u1 and c2 ̸= u2 set (C1(v), C2(v)) = (c1, c2);
otherwise set (C1(v), C2(v)) = (c2, c1) (if c1 = u1 then c2 ̸= u1 and c1 ̸= u2; if c2 = u2 then
c2 ̸= u1 and c1 ̸= u2; formally proved in Lean T13). Because r(v) ∈ {C1(v), C2(v)} for every
v ∈ ˆV , ∑ v∈ ˆV w(v)(1C1(v)=r(v) + 1C2(v)=r(v)) = ∑ v∈ ˆV w(v), so max(W (C1), W (C2)) ≥ 1 2 Wtot
(Lean T14).
Part 2: Upper bound: Adak et al. [1, Theorem 3] guarantees k∗(d) ≤ ⌊(d + 2)(2 − 1/e)⌋ =
(2 − 1/e)d + O(1). Lower bound (for all d ≥ 4): let k = k∗(d) and M ≥ 2 satisfy k ≥ d + M
and (1) for all S ∈ {1, . . . , d}. If M ≥ d, then k ≥ d + M ≥ 2d > (2 − 1/e)d. Otherwise
2 ≤ M ≤ d − 1. Set ℓ∗ := ⌊M ln((d + 1)/M )⌋ and S∗ := k − d − M + ℓ∗. Note first that
ℓ∗ ≥ 1: indeed, for 2 ≤ M ≤ d − 1 and d ≥ 4, M ln((d + 1)/M ) is concave on [2, d − 1], taking
values 2 ln((d + 1)/2) ≥ 2 ln(5/2) > 1 at M = 2 and (d − 1) ln(1 + 2 d−1 ) > (d − 1) · 2/(d−1) 1+1/(d−1) =
2(d−1)
d > 1 at M = d − 1. Since k ≥ d + M , this forces S∗ ≥ ℓ∗ ≥ 1. If S∗ > d, then
k ≥ 2d + 1 + M − ℓ∗ ≥ 2d + 1 − M (ln((d + 1)/M ) − 1) ≥ 2d + 1 − (d + 1)/e2 > (2 − 1/e)d
(using maxx>0 x(ln(a/x) − 1) = a/e2). Finally, when 1 ≤ S∗ ≤ d, applying (1) at S = S∗
together with 1 − 1/M < e−1/M and writing ℓ∗ = M ln((d + 1)/M ) − θ (θ ∈ [0, 1)) gives
e−ℓ∗/M ≤ e1/M M d+1 ≤ (1 + 2 M ) M d+1 = M +2 d+1 , hence
k ≥ d+M +
(
d + 2 − 1 M )( 1 − e−ℓ∗/M ) −ℓ∗ > d+M +(d+1) ( 1 − M + 2 d + 1 ) −M ln ( d + 1 M ) ,
which simplifies to k ≥ 2d−1−M ln((d+1)/M ) ≥ (2−1/e)d−2 because maxx>0 x ln((d+1)/x) =
(d + 1)/e. Combining upper and lower bounds yields k∗(d) = (2 − 1/e)d + O(1).
3 Formal Verification Boundary and Reproducibility
Table 1 records exact SHA-256 digests for the suite DEGENERATE-FLEXIBLE-COLORING-CERT-1.0.
• Lean 4.36.0 Constructive Suite (T01–T20): Builds cleanly via lake build and strict
compiler checks (lean warnings-as-errors) with 0 sorry, 0 grind, and 0 custom axioms.
Six theorems (T03, T04, T08, T13, T17, T20) use no axioms; eleven (T01, T02, T05–T07, T10,
8
```

---

## Page 9

```text
Table 1: Cryptographic SHA-256 inventory for DEGENERATE-FLEXIBLE-COLORING-CERT-1.0 (repos-
itory: https://github.com/arr-research/arr-research.github.io).
Artifact Exact SHA-256 Digest
DegenerateFlexibleColoringCert.lean e2a524e03563e347209335007b1911b4ec0ee20a38cfde422b3e8f6440fea6d3
degenerate_flexible_coloring_verifier.py 36c284d5dd53663a6f12349a521cb7aaf74a44067ee4c4fb2862eaecc5b10100
certificates/MANIFEST.json (16 certs) bd51374bc2f403654ce11fc74c4eb061b2e315a240ca684dbd2d6eaf47a75d11
T14–T16, T18, T19) use propext and Quot.sound; and three (T09, T11, T12) additionally
use Classical.choice via omega/by_cases. Lean mechanizes the indicator refinement
(T01), geometric recurrence (T02–T03), exact discrete certifications beating [1] at d ∈
{8, 10, 11, 13, 14, 16, 17, 19, 21, 22, 24, 25} (T04, T17, T20), the subset rank-preservation and
s-rank greedy color-availability lemmas (T05–T08), universal Gd degeneracy, pigeonhole
clique impossibility, and direct G2 proof (T09–T12), forest pair extension (T13), weighted
averaging (T14), and Padé denominator strictness (T16).
• Analytical vs. Computational Scope: The max-flow/min-cut existence reduction [1,
Claim 8] in Theorem 1, the random-ordering expectation in Theorem 2, and the calculus
optimization in Theorem 4(2) are proved analytically in Section 2; our AST-pure zero-
float Python suite (73/73 tests, 16 SHA-256 certificates C01–C16) certifies exact discrete
bounds across d ∈ [1, 100], rational Taylor-tail Padé bounds, exhaustive backtracking on
G2, G3, G4, and constructive forest weighted (2, 1/2)-colorings.
AI Assistance and Conflict-of-Interest Disclosure. The author (Lluis Eriksson, founder
and operator of AIRR.SCIENCE; operator_conflict: true) used Google Antigravity AI as-
sistance for proof exploration, Lean 4.36.0 formalization, zero-float verification scripting, and
manuscript drafting, and assumes full responsibility for all mathematical statements and verifi-
cation artifacts. Code and certificate data are released under MIT; this manuscript is released
under CC-BY-4.0.
References
[1] Rajat Adak, L. Sunil Chandran, Shiwali Gupta, Tomáš Kaiser, Subrahmanyam Kalyana-
sundaram, Rogers Mathew, Saraswati Girish Nanoti, Suraj Kumar Sahoo, Umesh Shankar,
and Joel M. Thomas. List coloring degenerate graphs with requests. arXiv preprint
arXiv:2611.34348v1, 2026.
[2] Miklós Biró, Mihály Hujter, and Zsolt Tuza. Precoloring extension. I. interval graphs. Dis-
crete Mathematics, 100(1–3):267–279, 1992.
[3] Stijn Cambie and Wouter Cames van Batenburg. Fractional list packing for layered graphs.
Journal of Graph Theory, 113:19–37, 2026.
[4] Stijn Cambie, Wouter Cames van Batenburg, Ewan Davies, and Ross J. Kang. Packing
list-colorings. Random Structures & Algorithms, 64(1):62–93, 2024.
[5] Reinhard Diestel. Graph Theory. Springer-Verlag, Heidelberg, 2005.
[6] Zdeněk Dvořák, Sergey Norin, and Luke Postle. List coloring with requests. Journal of
Graph Theory, 92(3):191–206, 2019.
[7] Paul Erdős, Arthur L. Rubin, and Herbert Taylor. Choosability in graphs. Congressus
Numerantium, 26:125–157, 1979.
9
```

---

## Page 10

```text
[8] Hemanshu Kaul, Rogers Mathew, Jeffrey A. Mudrock, and Michael J. Pelsmajer. Flexi-
ble list colorings: Maximizing the number of requests satisfied. Journal of Graph Theory,
106(4):887–906, 2024.
[9] Vadim G. Vizing. Vertex colorings with given colors. Diskretnyi Analiz, 29:3–10, 1976.
10
```
