# Higher-Dimensional Hadwiger Covering Beyond Three Dimensions: Exact Illumination and Continuum Covering of the Self-Dual 4D 24-Cell, 4D Regular Polytope Radii, Factor-d Helly Collapse, and the Measure-1 Double-Shadow Obstruction

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6HQYSAJ2JN8KY9WX` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/paper133-hadwiger-4d-polytopes-and-shadow-peeling (`v1.0.0`)  
**Canonical PDF SHA-256:** `287cf1204dbdfbbdcf2b43bc28e0578e226d1cccbbc34b7a233422680c361fea`

## Abstract

Following Aiger, Har-Peled, and Zuzic's November 2026 resolution of Hadwiger's covering conjecture in R^3 (c(K) <= 8), Hadwiger's conjecture remains open in all dimensions d >= 4 (in particular c(K) <= 16 in R^4). We establish a machine-checked higher-dimensional analysis backed by 20 constructive Lean 4.36.0 theorems (zero sorry, zero Classical.choice, zero warnings) and an AST-audited zero-float exact-rational verifier emitting 16 SHA-256 certificates and passing 56 adversarial tests. First, we prove that the self-dual 4D 24-cell P_24 (F_4) has exact illumination number c(P_24) = 8: its 15-regular distance-2 graph G_2(P_24) has exact independence number alpha = 3 (forcing c >= 8), matched by a centrally symmetric 4-pair integer illumination certificate +/- (2,0,-1,-1), +/- (0,2,-1,1), +/- (0,1,2,-1), +/- (1,0,1,2) illuminating all 24 vertices and hence all of partial P_24. Second, we prove exact continuum 8-homothet covering bounds 3/4 <= lambda_8(P_24) <= 8/9: the lower bound via a one-line 4-vector LP dual identity canceling the center identically, and the continuum upper bound over all of P_24 subset R^4 via 576 exact rational Voronoi-cell LP dual certificates (denominators in {1,2,3}, kernel-checked in Lean 4). Third, we certify exact minimal-cardinality covering ratios for the core 4D regular polytopes (Delta_d: d/(d+1); beta_d: (d-1)/d; C_d: 1/2 closed and 2/3 open-interior). Fourth, we prove two exact structural obstructions to extending 3D shadow peeling into d >= 4: a factor-d collapse of the universal 1-homothet S-diameter covering threshold from 2 to 2/d (1/2 in R^4) on -(delta/2)*Delta_d, and a universal measure-1 double-shadow obstruction showing that for every direction pair (w_1, w_2) in S^3 x S^3, Sigma(C_4, w_1) cap Sigma(C_4, w_2) retains at least 4 complete 2-dimensional square faces (requiring k_min(d) = 1 + ceil(log_2 d) pairs on C_d, achieved by Hadamard H_4 at d = 4), alongside the exact Wallis recurrence (d*kappa_d)*((d+1)*kappa_{d+1}) = 2(d+1)/pi for the John mean-width bound.

## Full Extracted Text

--- Page 1 ---
Higher-Dimensional Hadwiger Covering Beyond
Three Dimensions:
Exact Illumination and Continuum Covering of the
Self-Dual 4D 24-Cell,
4D Regular Polytope Radii, F actor-d Helly Collapse,
and
the Measure-1 Double-Shadow Obstruction
Lluis Eriksson
Independent Researcher
github.com/lluiseriksson/paper133-hadwiger-4d-polytopes-and-shadow-peeling
November 27, 2026
Abstract
In a landmark breakthrough, Aiger, Har-Peled, and Žužić [ 1] settled Hadwiger’s seven-
decade-old covering conjecture in three dimensions ( c(K) ≤ 8 for every convex body K ⊂ R3)
by combining a 2-direction orthogonal shadow-peeling step with John’s position mean-width
bound (8
∫
S2 hS d˜σ < 12) and a 1D-arc Helly chord-telescoping lemma. Hadwiger’s conjecture
remains wide open in all dimensions d ≥ 4 (in particular c(K) ≤ 24 = 16 in R4).
W e establish a complete, machine-checked higher-dimensional analysis ( d ≥ 4, with spe-
cial emphasis on the unique four-dimensional geometry of R4), backed by 20 constructive
Lean 4.36.0 theorems (zero sorry, zero Classical.choice, zero external imports) and an
AST-audited zero-float exact-rational verifier generating 16 SHA-256 certificates and passing
56 adversarial tests:
1. Exact Illumination Number of the Self-Dual 4D 24-Cell ( P24, F4): c(P24) = 8 .
Unlike the 3D Platonic solids,R4 admits the self-dual 24-cell P24 (24 vertices, 24 octahedral
facets). W e prove exhaustively in Lean 4 that its 15-regular distance-2 graph G2(P24) has
exact independence number α(G2(P24)) = 3 (forcing c(P24) ≥ 24/3 = 8 ), and construct
a centrally symmetric 4-pair integer illumination certificate ±(2, 0, −1, −1), ±(0, 2, −1, 1),
±(0, 1, 2, −1), ±(1, 0, 1, 2) illuminating all 24 vertices (3 disjoint vertices per direction) and
hence all of ∂P24.
2. Exact Continuum 8-Homothet Covering Bounds 3
4 ≤ λ8(P24) ≤ 8
9 . W e prove
λ8(P24) ≥ 3
4 via a one-line 4-vector LP dual identity canceling the translation center
identically , and prove λ8(P24) ≤ 8
9 unconditionally over the entire continuum P24 ⊂ R4
(zero sampling) via 576 exact rational V oronoi-cell LP dual certificates (denominators in
{1, 2, 3}, hence in 1
6 Z≥0, kernel-checked in Lean 4 thm14–thm15).
3. Exact Covering Radii of the Core 4D Regular Polytopes. W e certify the ex-
act optimal minimal-cardinality covering ratios for the 5-cell ∆4 (c = 5 , λ5 = 4
5 , and
λd+1(∆d) = d
d+1 for all d ≥ 2), the 16-cell β4 (c = 8 , λ8 = 3
4 , and exact λ2d(βd) = d−1
d
for all d ≥ 2), the 24-cell P24 (c = 8 , λ8 ∈ [3
4 , 8
9 ]), and the 8-cell C4 (c = 16 , exact closed
minimum λ16 = 1
2 , with explicit open-interior cover at λ = 2
3 ).
4. T wo Exact Structural Obstructions to Extending 3D Shadow Peeling intod ≥ 4.
First, we prove an exact factor-d collapse of the universal 1-homothet S-diameter covering
threshold from 2 (for 1D shadow curves in R3) to 2/d (1/2 in R4) on the inverted d-simplex
−δ
2 ∆d. Second, we prove a Universal Measure-1 Non-Smooth Double-Shadow
1
AIRR:ARR-2026-6HQYSAJ2JN8KY9WX v1  [Mathematical physics]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
Obstruction: for every pair of directions (w1, w2) ∈ S3 × S3 without exception, the
double-shadow boundary Σ(C4, w1) ∩ Σ(C4, w2) retains at least 4 complete 2-dimensional
square faces (requiring kmin(d) = 1 + ⌈log2 d⌉ pairs on Cd, with k = 3 achieved via
Hadamard H4 in R4), alongside the exact W allis recurrence (dκd)((d + 1)κd+1) = 2(d+1)
π
for the John mean-width constant.
1 Introduction
F or a convex body K ⊂ Rd, the Hadwiger covering number c(K) is the minimum number of
smaller positive homothetic copies λK + vi (λ ∈ (0, 1), vi ∈ Rd) whose union covers K [7, 6]. By
Boltyanski’s theorem [4], c(K) equals the illumination number: the minimum number of nonzero
directions d1, . . . , dm ∈ Rd \ {0} such that for every boundary point x ∈ ∂K, some open ray
{x + tdi : t > 0} meets int(K). Hadwiger’s conjecture asserts c(K) ≤ 2d, with equality attained
by parallelotopes ( c([0, 1]d) = 2 d). After Levi [ 11] settled d = 2 and Lassak [ 10] settled centrally
symmetric bodies in d = 3 , Aiger, Har-Peled, and Žužić [ 1] resolved d = 3 unconditionally in
November 2026; in higher dimensions d ≥ 4, the conjecture remains open (the best general
asymptotic bounds remain exponential with base < 2 [12, 8, 3]).
The breakthrough of [ 1] hinges on three tightly interlocking three-dimensional phenomena:
(i) two antipodal directions ±w∗ illuminate ∂K \ Σ(K, w∗), leaving a 1-dimensional shadow
curve Σ(K, w∗); (ii) in John’s position [ 9] for S = 1
2 (K − K), the spherical mean width satisfies
8
∫
S2 hS d˜σ ≤ 8 · 3
2 = 12 with equality only for cubes; and (iii) any contiguous 1D arc of S-length
< 2 is covered by a single smaller homothet via Helly’s theorem in R3 and linear ordering of 4
points along the curve.
This paper investigates what survives and what breaks down when moving from d = 3 to
d ≥ 4—focusing both on exact quantitative obstructions to higher-dimensional shadow peeling
and on exact, machine-checked illumination and continuum covering theorems for the core four-
dimensional regular polytopes [ 5], highlighted by the self-dual 24-cell P24 (which has no three-
dimensional analogue).
2 Exact Illumination Number of the Self-Dual 4D 24-Cell: c(P24) =
8
In dual Hurwitz coordinates (scaled by 2 so every coordinate is an integer), we represent the
self-dual 4D 24-cell as
P24 =
{
x ∈ R4 : |xi| + |xj| ≤ 1 ∀ 1 ≤ i < j ≤ 4
}
, ∥x∥24 = max
1≤i<j≤4
(|xi| + |xj|). (1)
Its 24 vertices consist of the 8 axis vertices ±ei (i = 1 , 2, 3, 4) and the 16 half-integer vertices
(±1
2 , ±1
2 , ±1
2 , ±1
2 ) (so every vertex satisfies ∥v∥2 = 1 and ∥v∥24 = 1 , and lies on exactly 6 of the
24 octahedral facets f · x = 1 , where f ∈ F24 runs over the 24 permutations of (±1, ±1, 0, 0)).
Define the distance-2 incompatibility graph G2(P24) on V (P24) by joining u ∼ w whenever
∥u−w∥24 = 2 . By the triangle inequality , if two verticesu, w belong to a single homothet c+λP24,
then 2 = ∥u − w∥24 ≤ ∥ u − c∥24 + ∥w − c∥24 ≤ 2λ, forcing λ ≥ 1. Hence any smaller homothet
(λ < 1) can contain only an independent set of G2(P24).
Theorem 2.1 (Exact Illumination Number of the 4D 24-Cell) . The Hadwiger covering / il lumi-
nation number of the self-dual 4D 24-cel l is exactly c(P24) = 8 :
1. Sharp Lower Bound c(P24) ≥ 8 (Lean thm06–thm09, Cert. C01): The graph G2(P24) is
15-regular (180 edges), and exhaustive kernel search proves its exact independence number is
α(G2(P24)) = 3 (no 4 vertices are pairwise at ∥ · ∥ 24-distance < 2). Therefore any m ≤ 7
smal ler homothets cover at most 3m ≤ 21 < 24 vertices, forcing c(P24) ≥ 8.
2

--- Page 3 ---
2. Exact Central ly Symmetric 8-Direction Upper Boundc(P24) ≤ 8 (Lean thm10–thm11,
Certs. C02, C04): The four antipodal integer direction pairs
±(2, 0, −1, −1), ±(0, 2, −1, 1), ±(0, 1, 2, −1), ±(1, 0, 1, 2) (2)
partition the 24 vertices into 8 disjoint co-il luminable triples (3 vertices per direction), with
strict inward margin f ·dk ≤ −1 on al l 6 active facets of each vertex. By Boltyanski’s vertex-to-
boundary equivalence for bounded polytopes (every boundary point x ∈ ∂P24 lies on a minimal
face containing a vertex v with active facet set F(x) ⊆ F(v), Lean thm11), these 8 directions
il luminate al l of ∂P24.
3 Exact Continuum 8-Homothet Covering Bounds: 3
4 ≤ λ8(P24) ≤
8
9
Boltyanski’s theorem guarantees that 8 directions imply some λ < 1 covers P24, without giving
an explicit optimal value. Using self-duality of P24 and exact linear programming duality over Q,
we certify explicit continuum bounds directly on all of P24 ⊂ R4.
Theorem 3.1 (Exact Continuum Covering Ratio of the 4D 24-Cell) . Let λ8(P24) := inf {λ > 0 :
∃ c1, . . . , c8 ∈ R4 with P24 ⊆ ∪8
k=1(ck + λP24)}. Then
3
4 ≤ λ8(P24) ≤ 8
9. (3)
Proof. Lower bound λ8(P24) ≥ 3
4 (Lean thm12, Cert. C03): F or any two distinct vertices
u, w ∈ V (P24), either ∥u − w∥24 = 2 (adjacent in G2(P24)) or ∥u − w∥24 = ∥u − w∥2 = 1 (an edge
of P24). Hence every independent triple of G2(P24) consists of three pairwise adjacent vertices
forming a triangular 2-face ofP24, and all 96 such triples form a single orbit under theF4 symmetry
group of P24 (verified exhaustively in Certs. C01, C04). In any 8-homothet cover of P24 with λ < 1,
since α(G2(P24)) = 3 and |V (P24)| = 24 , every homothet must cover one such triangular 2-face,
and at least one homothet c + λP24 must also cover the origin 0 ∈ P24. By F4-transitivity on
triangular 2-faces, assume it covers u0 = (1 , 0, 0, 0), u1 = ( 1
2 , 1
2 , 1
2 , 1
2 ), u2 = ( 1
2 , 1
2 , 1
2 , −1
2 ), and
u3 = (0 , 0, 0, 0). Evaluating the four facet inequalities fr · (ur − c) ≤ λ for
f0 = (1 , 0, −1, 0), f 1 = (0 , 0, 1, 1), f 2 = (0 , 1, 0, −1), f 3 = ( −1, −1, 0, 0), (4)
observe that f0 + f1 + f2 + f3 = (0 , 0, 0, 0), so summing the four inequalities cancels c identically:
4λ ≥
3∑
r=0
fr · (ur − c) = 1 + 1 + 1 + 0 − 0 = 3 = ⇒ λ ≥ 3
4. (5)
Continuum upper bound λ8(P24) ≤ 8
9 (Lean thm13–thm15, Certs. C05–C08): Because
all 24 vertices vi ∈ V (P24) lie on the unit 3-sphere S3, the 24 closed V oronoi cells
Vor(vi) :=
{
x ∈ P24 : ⟨x, vi⟩ ≥ ⟨ x, vj⟩ ∀ j ∈ {0, . . . , 23}
}
(6)
form an exact gapless partition P24 = ∪23
i=0 Vor(vi) (every x ∈ P24 maximizes the finite set
{⟨x, vi⟩}). Define the 8 centrally symmetric translation centers ck := −1
9 dk (∥ck∥24 = 1
3 ), where
dk are the 8 illumination directions of Theorem 2.1, and let k(i) ∈ { 0, . . . , 7} be the unique
direction assigned to vertex vi. T o proveVor(vi) ⊆ ck(i) + 8
9 P24 for every x ∈ Vor(vi), it suﬀices by
LP weak duality (Lean thm13) to exhibit, for each of the 24 ×24 = 576 pairs (vi, fj), nonnegative
rational multipliers ur ≥ 0 (r = 0 ..23) and wℓ ≥ 0 (ℓ ̸= i) such that
23∑
r=0
urfr +
∑
ℓ̸=i
wℓ(vℓ − vi) = fj and
23∑
r=0
ur + fj · dk(i)
9 ≤ 8
9. (7)
3

--- Page 4 ---
Figure 1: (a) Orthonormal 2D projection of the 4D 24-cell P24 displaying the exact 8×3 centrally
symmetric illumination partition into 8 disjoint triangular triples (Theorem2.1). (b) Distribution
of certified exact rational V oronoi dual upper bounds λ(vi, fj) across all 576 (V oronoi cell, facet)
pairs: every pair satisfies λ ≤ 8/9 with maximum denominator 3 (Theorem 3.1).
All 576 exact rational dual certificates—remarkably having every individual multiplier denomi-
nator in {1, 2, 3} (hence all multipliers in 1
6 Z≥0, max denominator 3)—are stored in scripts/
exact_4d_witnesses.json and checked exhaustively inside the Lean 4 kernel ( thm14–thm15)
and Certificates C05–C08. Hence P24 ⊆ ∪7
k=0(ck + 8
9 P24) holds unconditionally over the entire
continuum.
4 Complete 4D Regular Polytope Classification and Universal
d-Dimensional Radii
Combining Theorems 2.1–3.1 with exact universal theorems for thed-simplex ∆d, d-cross-polytope
βd, and d-cube Cd yields a complete machine-checked classification of the four core regular 4-
polytopes (T able 1 and Figure 2).
Theorem 4.1 (Exact Optimal Minimal-Cardinality Covering Ratios of ∆d, βd, and Cd). F or
every integer dimension d ≥ 2:
1. d-Simplex ∆d (Lean thm02, Certs. C09–C10): c(∆d) = d + 1 with exact optimal covering
ratio λd+1(∆d) = d
d+1 (λ5(∆4) = 4
5 ).
2. d-Cross-Polytope βd (Lean thm03–thm04, Certs. C09, C11): c(βd) = 2 d (c(β4) = 8 ) with
exact optimal 2d-homothet covering ratio λ2d(βd) = d−1
d (λ8(β4) = 3
4 ).
3. d-Cube Cd (Lean thm05, Cert. C12): c(Cd) = 2 d (c(C4) = 16 ), with exact closed min-
imal covering ratio λ2d (Cd) = 1
2 (attained by 2d closed half-cubes (±1
2 )d + 1
2 Cd), while the
same centers (±1
2 )d at λ = 2
3 yield an explicit rational strict open-interior cover Cd ⊆∪
s∈{±1}d int
(1
2 s + 2
3 Cd
)
.
Proof. (1) W rite ∆d = {x ∈ Rd
≥0 : ∑d
i=1 xi ≤ 1}. No smaller homothet ( λ < 1) can contain two
distinct vertices of ∆d (their difference has difference-body norm 2), so c(∆d) ≥ d + 1. F or the
upper bound λd+1(∆d) ≤ d
d+1 , consider the d + 1 translates d
d+1 ∆d (shift 0) and 1
d+1 ek + d
d+1 ∆d
(k = 1 , . . . , d). F or any x ∈ ∆d, either xk ≥ 1
d+1 for some k—in which case x − 1
d+1 ek ∈ Rd
≥0
has coordinate sum ≤ 1 − 1
d+1 = d
d+1 —or maxi xi < 1
d+1 , forcing ∑d
i=1 xi ≤ d maxi xi < d
d+1 so
4

--- Page 5 ---
T able 1: Exact machine-checked covering classification of the four core regular 4-polytopes (all
satisfying c(P) ≤ 24 = 16 , Lean thm02–thm15, thm19–thm20, Certs. C01–C12, C16).
4D Polytope |V | | F | Exact c(P ) |V |/c Certified λc(P ) Certificates
5-cell (∆4) 5 5 5 1 4/5 (exact) C09–C10, thm02
16-cell (β4) 8 16 8 1 3/4 (exact) C09, C11, thm04
24-cell (P24, F4) 24 24 8 3 [3/4, 8/9] C01–C08, thm06–thm15
8-cell (C4) 16 8 16 1 1 /2 closed (2/3 open) C12, thm05
Figure 2: (a) Exact illumination number c(P) versus vertex count |V (P)| across the four core
regular 4-polytopes, highlighting the 24-cell’s 3× vertex-to-illumination compression ( 24 → 8,
half the 4D Hadwiger budget 16). (b) Certified minimal-cardinality homothety covering ratios
λc(P).
x ∈ d
d+1 ∆d (Lean thm02 for arbitrary rational scale M ≥ 1). F or the lower bound, in any (d + 1)-
homothet cover with λ < 1, each homothet covers one vertex, so the centroid g = ( 1
d+1 , . . . , 1
d+1 )
must share a homothet v + λ∆d with some vertex: if it shares with 0, then vi ≤ 0 for all i and∑d
i=1(gi − vi) ≤ λ forces λ ≥ d
d+1 ; if it shares with ek, then vi ≤ 0 (i ̸= k), vk ≤ 1
d+1 , and
1 − ∑d
i=1 vi ≤ λ again forces λ ≥ 1 − 1
d+1 = d
d+1 (Lean thm02).
(2) F or βd = {x ∈ Rd : ∥x∥1 ≤ 1}, every pair of distinct vertices ±ei satisfies ∥u − w∥1 = 2 ,
so by the triangle inequality any homothet covering two vertices requires λ ≥ 1 (Lean thm03),
hence c(βd) ≥ 2d. F or the upper bound, take the 2d translates ±1
d ei + d−1
d βd. Given x ∈ βd with
s = ∥x∥1 ≤ 1, choose i attaining m = |xi| = max j |xj| (so s ≤ dm) and σ = sgn( xi) ∈ {± 1}
(taking +1 if xi = 0 ). Then ∥x − σ
d ei∥1 = |m − 1
d | + (s − m): if m ≥ 1
d , this equals s − 1
d ≤ d−1
d ; if
m < 1
d , since d ≥ 2 we have 1
d + s−2m ≤ 1
d + (d−2)m ≤ d−1
d (Lean thm04 over arbitrary rational
scale M ≥ 1). F or the lower bound, the facet centroid g = ( 1
d , . . . , 1
d ) satisfies ∥g − (±ek)∥1 ≥
(1 − 1
d ) + ( d − 1)1
d = 2 d−1
d for every vertex; since g must share a homothet with one of the 2d
vertices, the triangle inequality forces 2λ ≥ 2d−1
d , i.e. λ ≥ d−1
d .
(3) F or Cd = [ −1, 1]d, distinct vertices in {±1}d lie at ℓ∞-distance 2, forcing c(Cd) ≥ 2d.
V olume monotonicity gives2dλd vol(Cd) ≥ vol(Cd), so λ ≥ 1
2 , attained by the 2d closed half-cubes
1
2 s + 1
2 Cd (s ∈ {± 1}d). Moreover, for every x ∈ [−1, 1]d, choosing sm = +1 if xm ≥ 0 and −1
otherwise gives |xm − 1
2 sm| ≤ 1
2 < 2
3 for every coordinate m, proving Cd ⊆ ∪
s∈{±1}d int
(1
2 s+ 2
3 Cd
)
(Lean thm05, Cert. C12).
5

--- Page 6 ---
5 T wo Exact Obstructions to Extending 3D Shadow Peeling into
d ≥ 4
Why cannot Aiger, Har-Peled, and Žužić’s 3D proof [ 1] be extended verbatim to d ≥ 4? W e
identify and formalize two sharp, quantitative geometric obstructions.
Theorem 5.1 (F actor-d Collapse of the Non-1D Helly–Minkowski Covering Threshold) . In R3,
Lemma 3.4 of [ 1] covers any 1D boundary curve of S-length < 2 by a single smal ler homothet
λ0K + v (λ0 < 1) by exploiting linear ordering of 4 points along the curve. In Rd (d ≥ 4),
the shadow boundary Σ(K, w) is (d − 2)-dimensional ( d − 2 ≥ 2) and lacks a linear order. F or
K = ∆ d with halved difference body S = 1
2 (∆d − ∆d), the inverted simplex A = −δ
2 ∆d has S-
diameter diamS(A) = δ, yet any positive homothet v+λ∆d ⊇ A must satisfy λ ≥ d
2 δ (Lean thm01,
Cert. C09). Thus the universal 1-homothet S-diameter covering threshold col lapses by an exact
factor of d, from 2 to 2
d ( 1
2 in d = 4 ).
Proof. Since S = 1
2 (∆d − ∆d), every pair of points a, b ∈ ∆d satisfies 1
2 (a − b) ∈ S, so ∥a −
b∥S ≤ 2, with equality on distinct vertices (since ei − 0 ∈ ∂(2S)); hence diamS(∆d) = 2 and
diamS(A) = δ
2 diamS(∆d) = δ. Now suppose A ⊆ v + λ∆d. Because each vertex −δ
2 ei ∈ A
satisfies (−δ
2 ei − v)i ≥ 0, we have vi ≤ − δ
2 for every i = 1 , . . . , d. Because 0 ∈ A satisfies∑d
i=1(0 − vi) ≤ λ, summing −vi ≥ δ
2 over i = 1 , . . . , d yields λ ≥ ∑d
i=1(−vi) ≥ d
2 δ (formalized
for arbitrary dimension d in Lean thm01 and checked for d = 2 ..12 in Cert. C09). Hence λ < 1
requires δ < 2
d .
Theorem 5.2 (Universal Measure-1 Non-Smooth Double-Shadow Obstruction and John Mean
Width). Consider attempting to iterate shadow peeling in Rd (d ≥ 4) using k antipodal pairs
{±w1, . . . , ±wk} to reduce ∂K to a 1D curve.
1. Universal 4D Measure-1 Obstruction (Lean thm16, Cert. C13): F or every pair of
directions (w1, w2) ∈ S3 × S3 without exception, the double-shadow intersection Σ(C4, w1) ∩
Σ(C4, w2) on the 4-cube C4 = [ −1, 1]4 contains at least 4 complete 2-dimensional square
faces (total 2D area ≥ 16).
2. General d-Cube Pigeonhole Bound and Hadamard H4 Elimination (Lean thm17 for
d = 4 / H4, Cert. C14): On Cd, k antipodal pairs leave complete (d−2)-faces unil luminated
whenever d > 2k−1; eliminating al l (d − 2)-faces requires kmin(d) = 1 + ⌈log2 d⌉ pairs (2kmin
directions). At d = 4 , k = 3 pairs (6 directions from the first three rows of the Hadamard
matrix H4) separate al l 4 coordinate sign signatures and eliminate al l 2-faces.
3. Higher-Dimensional John Mean-Width Recurrence (Lean thm18 for d = 2 , 3 arith-
metic, Cert. C15): Let ωd := vol d(Bd
2 ) and κd :=
∫
Sd−1 |u1| d˜σ(u) = 2ωd−1
d ωd
. Placing the
symmetric body S = 1
2 (K − K) in maximal-volume-el lipsoid John ’s position (Bd
2 ⊆ S) gives
spherical mean width
∫
Sd−1 hS d˜σ ≤ dκd = 2ωd−1
ωd
(attained by [−1, 1]d), obeying the exact
W al lis recurrence(dκd)((d + 1)κd+1) = 2(d+1)
π for al l d ≥ 2 (recovering 3κ3 = 3
2 and 8 · 3
2 = 12
in [ 1], and yielding 4κ4 = 16
3π in R4).
Proof. (1) A (d − 2)-face Fij(si, sj) = {x ∈ Cd : xi = si, x j = sj} (si, sj ∈ {± 1}) has outward
normal cone NCd (Fij) = {asiei + bsjej : a, b ≥ 0}\{ 0}, which meets w⊥ (putting Fij ⊆ Σ(Cd, w))
if and only if sisjwiwj ≤ 0: indeed, if wi = wj = 0 then siei + sjej ∈ NCd (Fij) ∩ w⊥; if exactly
one of wi, wj vanishes, the corresponding axis normal siei or sjej lies in NCd (Fij) ∩ w⊥; and if
wi, wj ̸= 0 with sisjwiwj < 0, then |wj|siei + |wi|sjej ∈ NCd (Fij) ∩ w⊥. F or any w1, w2 ∈ S3,
choose sign completions σr,i ∈ {±1} with σr,i = sgn( wr,i) whenever wr,i ̸= 0 (and +1 if wr,i = 0 ).
Setting εi := σ1,iσ2,i ∈ {± 1}, let a ∈ { 0, . . . , 4} be the count of +1 entries. By pigeonhole
(Lean thm16),
(a
2
)
+
(4−a
2
)
≥ 2 coordinate pairs (i, j) satisfy εiεj = +1 , i.e. σ1,iσ1,j = σ2,iσ2,j.
F or each such pair, both antipodal 2-faces with sisj = −σ1,iσ1,j satisfy sisjwr,iwr,j ≤ 0 for both
6

--- Page 7 ---
Figure 3: (a) Exact factor-d collapse of the universal non-1D S-diameter threshold 2/d relative to
the 3D 1D-arc threshold 2 (Theorem 5.1), alongside optimal simplex and cross-polytope covering
ratios. (b) Minimum shadow-peeling direction pairs kmin(d) = 1 + ⌈log2 d⌉ required to eliminate
(d − 2)-faces on Cd (showing k = 2 fails everywhere in 4D while k = 3 succeeds via H4) and the
exact John mean-width constant dκd (Theorem 5.2).
r = 1 , 2, leaving at least 2 ×2 = 4 complete square faces (area ≥ 16; verified across all 802 = 6400
nonzero direction patterns in {−1, 0, 1}4 \ {0} in Cert. C13).
(2) With k directions w1, . . . , wk ∈ Rd \ {0} and sign completions σr,i ∈ {± 1}, assign to
each coordinate i ∈ { 1, . . . , d} the relative sign signature τi := ( σ1,iσ2,i, . . . , σ1,iσk,i) ∈ {± 1}k−1.
Whenever d > 2k−1, by the pigeonhole principle two distinct coordinates i ̸= j share τi = τj,
hence σr,iσr,j = σ1,iσ1,j for all r = 1 , . . . , k , preserving both (d − 2)-faces with sisj = −σ1,iσ1,j
across all k pairs. Conversely , when 2k−1 ≥ d (i.e. k ≥ 1 + ⌈log2 d⌉), choosing d distinct columns
from {±1}k−1 with all coordinates nonzero (e.g. rows (1, 1, 1, 1), (1, 1, −1, −1), (1, −1, 1, −1) of
H4 at d = 4 ) ensures that for every pair (i, j) some r flips σr,iσr,j, eliminating every (d − 2)-face
(Lean thm17, Cert. C13–C14).
(3) When the symmetric body S is in maximal-volume-ellipsoid John’s position ( Bd
2 ⊆ S
with contact decomposition ∑ciui ⊗ ui = Id, ui ∈ ∂S ∩ Sd−1), Barthe’s reverse Brascamp–Lieb
inequality [ 2] (see also [ 1]) bounds its spherical mean width by that of the circumscribed cube
[−1, 1]d:
∫
Sd−1 hS d˜σ ≤
∫
Sd−1 ∥u∥1 d˜σ(u) = dκd. Projecting the upper and lower hemispheres of
Sd−1 orthogonally onto {u1 = 0 } gives
∫
Sd−1 |u1| dσ(u) = 2 ωd−1, while Area(Sd−1) = dωd, hence
dκd = 2ωd−1
ωd
. Substituting the exact unit-ball recurrence ωd+1 = 2π
d+1 ωd−1 immediately gives
(dκd)((d + 1) κd+1) = 4ωd−1
ωd+1
= 2(d+1)
π for all d ≥ 2 (checked for d = 2 ..10 in Cert. C15 and at
d = 2 , 3 in Lean thm18).
6 F ormal V erification Architecture and Reproducibility
All results are independently verified across three layers:
1. Constructive Lean 4.36.0 F ormalization:20 theorems (thm01–thm20) in lean/HadwigerFourDim.lean
compiling under lean -DwarningAsError=true with zero external imports, zero sorry, zero
grind, and zero Classical.choice, including kernel verification of α(G2(P24)) = 3 , the
8-direction symmetric illumination certificate, the 4-vector lower-bound dual, and all 576
V oronoi-cell LP duals.
2. AST-Audited Zero-Float Python V erifier: Pure standard-library code ( int, Fraction)
in verification/verify_hadwiger_4d.py, self-auditing its AST and emitting 16 canonical
SHA-256 certificates ( C01–C16) across four modes (manifest digest 451382269eb84d99...).
7

--- Page 8 ---
3. Adversarial T est Suite:56 pytest checks intests/test_adversarial.py covering positive
verification and live adversarial tampering across all four modes.
AI Assistance Disclosure. Portions of the exact LP dual extraction, Lean 4 formalization,
zero-float verification tooling, and manuscript preparation were developed using Google Anti-
gravity . All theorems, formal proofs, exact rational certificates, and adversarial tests were in-
dependently audited and verified, and the author takes full responsibility for all mathematical
content.
References
[1] Dror Aiger, Sariel Har-Peled, and Goran Žužić. Hadwiger’s covering conjecture in three
dimensions. arXiv preprint arXiv:2611.32334v2 , November 2026.
[2] F ranck Barthe. On a reverse form of the Brascamp–Lieb inequality . Inventiones Mathemat-
icae, 134(2):335–361, 1998.
[3] Károly Bezdek and Muhammad A. Khan. The illumination conjecture for convex polytopes.
Discrete & Computational Geometry , 48:1–20, 2012.
[4] V. G. Boltyanski. The problem of illuminating the boundary of a convex body .Izv. Moldavsk.
Fil. Akad. Nauk SSSR , 76:77–84, 1960.
[5] H. S. M. Coxeter. Regular Polytopes. Dover Publications, 3rd edition, 1973.
[6] I. T s. Gohberg and A. S. Markus. A certain problem about the covering of convex sets with
homothetic ones. Izv. Moldavsk. Fil. Akad. Nauk SSSR , 10(76):87–90, 1960.
[7] Hugo Hadwiger. Ungelöste Probleme Nr. 20. Elemente der Mathematik , 12:121, 1957.
[8] Han Huang, Boaz A. Slomka, T omasz Tkocz, and Beatrice-Helen V ritsiou. Improved bounds
for Hadwiger’s covering problem via thin-shell estimates. Journal of the European Mathe-
matical Society, 24(4):1431–1448, 2022.
[9] F ritz John. Extremum problems with inequalities as subsidiary conditions. Studies and
Essays Presented to R. Courant on his 60th Birthday , pages 187–204, 1948.
[10] Marek Lassak. Solution of Hadwiger’s covering problem for centrally symmetric convex
bodies in E3. Journal of the London Mathematical Society , 30:501–511, 1984.
[11] F riedrich W. Levi. Überdeckung eines Eibereiches durch Parallelverschiebungen seines offe-
nen Kerns. Archiv der Mathematik, 6:369–370, 1955.
[12] C. A. Rogers and Chuanming Zong. Covering convex bodies by translates of convex bodies.
Mathematika, 44(1):215–218, 1997.
8
