# Spectral Sidon Sets in Matrix Algebras: Non-Commutative Packing Advantages, Hierarchical Hessenberg Decoding, and Arithmetic Obstructions

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-08GAV9156R811SFS | v1 | 2026-11-28
Spectral Sidon Sets in Matrix Algebras:
Non-Commutative Packing Advantages, Hierarchical
Hessenberg Decoding,
and Arithmetic Obstructions
Lluis Eriksson
Independent Researcher (lluiseriksson@gmail.com)
Public Repository: https://github.com/arr-research/arr-research.github.io
November 28, 2026
Abstract
A classical Sidon set (B2-sequence) in an abelian group has all pairwise sums distinct.
We initiate the study of Spectral Sidon Sets in matrix algebras: subsets A ⊆ Md(R) whose
pairwise sums A+B all have distinct characteristic polynomials χA+B (t) = det(tI −(A+B)).
While d = 1 recovers classical Sidon sets, passing to d ≥ 2 exposes a rich interaction between
non-commutativity, matrix invariant theory, algebraic number theory, and analytic number
theory.
Let σd(N ), σsym d (N ), and σcomm d (N ) denote the maximum sizes of strong Spectral Sidon
Sets in the integer box Md([0, N ]), the symmetric box Symd([0, N ]), and among all pairwise
commuting subsets of Md([0, N ]), respectively. We establish six foundational results:
1. Universal Commuting Ceiling (Wedderburn–Minkowski Packing): For every d ≥ 1
and every commuting subset A ⊆ Md([0, N ])—allowing arbitrary non-symmetric and
nilpotent Jordan structure—we prove |A| ≤
√
2(4dN + 1)d/2, yielding σcomm d (N ) =
Θd(N d/2).
2. Exact Optimal Exponent for Non-Commuting Integer Matrices: For every d ≥ 2,
we prove σd(N ) = Θd(N d(d+1)/4), strictly beating every commuting family by the
unbounded polynomial factor N d(d−1)/4. The matching lower bound is achieved con-
structively via a new Hierarchical Hessenberg Spectral Decoding Theorem, showing
that all
(d+1
2
)
full-scale upper-triangular and diagonal entries of an integer upper-
Hessenberg matrix with fixed subdiagonal are uniquely recovered from χS (t) alone by
stage-by-stage root isolation and lower-triangular residue peeling.
3. The Symmetric–Non-Symmetric Arithmetic Rift: In Sym2([0, N ]), the discriminant
(a − c)2 + 4b2 is forced to be a sum of two squares; Landau’s theorem (1908) yields
σsym 2 (N ) ≤ ( √ 30 √ 2 KLR + o(1)) N 3/2/(log N )1/4 = o(σ2(N )), proving that symmetry
strictly depresses asymptotic spectral packing capacity relative to M2([0, N ]). In the
equal-diagonal hyperbolic subspace, Erdős–Ford multiplication-table theory imposes
an intermediate (log N )−δ/2(log log N )−3/4 barrier.
4. Symmetric Jacobi-Band Breakthrough, Sharp Parity Barrier, and Spectral Energy: Us-
ing symmetric tridiagonal (Jacobi) matrices with separated diagonal bands and O(
√
N )
subdiagonals, matching-polynomial residue peeling proves σsym d (N ) = Ωd(N (3d−1)/4)
for every d ≥ 2, surpassing σcomm d (N ) by N (d−1)/4. At d = 2, exploiting equal-
trace parity X1 ≡ X2 (mod 2) pins down the exact sharp rectangular injectivity
threshold to u ≤
√
N (2u ≤ 2
√
N ), saturated by explicit integer symmetric col-
lisions at u =
√
N + O(1). Moreover, we bound the spectral additive energy as
Ω(N 9√log N ) ≤ Espec(Sym2([0, N ])) ≤ O(N 9 log N ) and show that uniform proba-
bilistic alteration yields only Ω(N/(log N )1/3), failing to beat even the commuting
barrier.
1
```

---

## Page 2

```text
5. Finite-Field Laws and Non-Commutative Witnesses: Over Fq , strong Spectral Sidon
Sets collapse to size 1 in characteristic 2, and every commuting subset of M2(Fq ) (q
odd) satisfies |A| ≤ q (matched up to constants by Ω(q) for every prime power q = pk
with p ≥ 5). We exhibit explicit machine-checked non-commutative witnesses strictly
breaking these ceilings in Sym2(Fq ) for q ∈ {5, 7, 11, 13} (achieving 6, 8, 12, 14) and in
Sym3(Fq ) for q ∈ {3, 5} (achieving 6 > 4 and 12 > 9 > 7).
6. Super-Exponential Galois-Torus Separation: Over Fp, split diagonalizable families
satisfy σsplit d (Fp) ≤ √ 2/d! pd/2 + Od(pd/2−1), whereas embedding the elliptic torus
Fpd ↪→ Md(Fp) via a normal-basis cyclic cone beats every split family for all even
d ≥ 8 by Ω(d−3/4(d/(2e))d/2) and for all d ≥ 25 (including every odd d ≥ 25) by
Ω(d1/4(d/(8e))d/2).
The algebraic, combinatorial, and finite-field cores (16 constructive theorems) are machine-
checked in Lean 4.36.0 (0 sorry, 0 grind, 0 custom axioms), accompanied by an exact-
arithmetic verification suite and empirical benchmarks. We conclude with four open conjec-
tures governing the symmetric exponent and finite-field limits.
1 Introduction
A subset A of an abelian group (G, +) is called a Sidon set (or B2-sequence) if every element
of G has at most one representation as a + b with a, b ∈ A up to order. Initiated by Sidon and
launched into extremal combinatorics by Singer [13], Erdős and Turán [3], Bose and Chowla [2],
and Ruzsa [11], Sidon sets in {0, 1, . . . , N } have exact asymptotic maximum size (1 + o(1))
√
N
(see [10, 14]). Non-abelian generalizations replacing addition with group multiplication were
investigated by Babai and Sós [1], where the target remains the group itself.
In matrix algebras Md(R), however, matrices are frequently observed only through their
similarity invariants—namely, their eigenvalue multisets or characteristic polynomials χX (t) =
det(tId − X). This motivates a fundamentally new extremal question that blends additive
combinatorics with non-commutative linear algebra and spectral geometry:
Definition 1.1 (Spectral Sidon Set). Let R be a commutative ring with unity, let d ≥ 1, and
let V ⊆ Md(R) be a subset of d × d matrices over R. A subset A ⊆ V is a strong Spectral Sidon
Set if the map
{A, B} ↦−→ χA+B (t) := det
(
tId − (A + B)
)
∈ R[t]
is injective on the set of unordered pairs {A, B} with A, B ∈ A (allowing A = B), i.e., χA+B =
χC+D implies {A, B} = {C, D}. It is a weak Spectral Sidon Set if this map is injective on
unordered pairs of distinct elements A ⁄= B in A.
When d = 1, χa+b(t) = t − (a + b) determines a + b uniquely, so Definition 1.1 collapses
identically to a classical Sidon set. For d ≥ 2, the problem takes on a striking new character.
Because χA+B (t) collapses the d2-dimensional space Md(R) onto the d-dimensional space of
monic degree-d polynomials, two matrices A + B and C + D can be spectrally indistinguishable
even when A + B ⁄= C + D. Yet over the integers [0, N ] := {0, 1, . . . , N }, the k-th coeﬀicient
ek(S) of χS (t) = td − e1(S)td−1 + · · · + (−1)ded(S) grows as Θd(N k), so the total number of
realizable characteristic polynomials scales as
d∏
k=1
Θd(N k) = Θd
(
N
d(d+1)
2
)
,
matching the Vandermonde Jacobian volume
∫
[0,2N ]d
∏
i<j |λi − λj | dλ ≍d N d(d+1)/2.
At first glance, one might suspect that a large Spectral Sidon Set can be obtained
simply by choosing commuting (e.g., diagonal) matrices whose eigenvalue vectors form a
2
```

---

## Page 3

```text
Table 1: Extremal landscape of strong Spectral Sidon Sets established in this paper.
Ambient Space Lower Bound Upper Bound Key Mechanism
Commuting ⊆ Md([0, N ]) Ωd(N d/2) Od(N d/2) Wedderburn–Minkowski (Thm. 2.1)
General Md([0, N ]) (d ≥ 2) Ωd(N d(d+1)/4) Od(N d(d+1)/4) Hessenberg peeling (Thm. 3.1)
Symmetric Sym2([0, N ]) Ω(N 5/4) O(N 3/2/(log N )1/4) Jacobi & Landau–Ram. (Thms. 4.1–4.2)
Hyperbolic Hhyp 2 ([0, N ]) Ω(N ) O ( N 3/2 (log N )δ/2 (log log N )3/4 ) c = 1 & Erdős–Ford (Thm. 4.1)
Symmetric Symd([0, N ]) (d ≥ 3) Ωd(N (3d−1)/4) Od(N d(d+1)/4) Jacobi matching peel (Thm. 4.2)
Md(F2m ) (strong) 1 1 Char.-2 collapse (Thm. 5.1)
Commuting ⊆ M2(Fq ) (q odd) Ω(q) (p ≥ 5) q (exact, all odd q) Elliptic slab & Schur (Thm. 5.1)
Sym2(Fq ) (q = 5, 7, 11, 13) 6, 8, 12, 14 ⌊(
√
8q2 + 1 − 1)/2⌋ Non-comm. witnesses > q (Thm. 5.1)
Split vs. Elliptic in Md(Fp) 1−o(1) d·2d/2 pd/2 (ell.) √ 2/d! pd/2 (split) Normal-basis cone, d ≥ 8 (Thm. 5.2)
d-dimensional Sidon set. Our first theorem shows that commutativity suffers a massive dimen-
sional bottleneck: every commuting subset of Md([0, N ])—even non-symmetric and arbitrarily
defective/nilpotent—has size at most Od(N d/2). In sharp contrast, non-commutativity unlocks
the full
(d+1
2
)
degrees of freedom of the characteristic polynomial! Our centerpiece result
(Theorem 3.1) proves that for every d ≥ 2,
σd(N ) = Θd
(
N
d(d+1)
4
)
,
strictly beating every commuting family by the unbounded polynomial factor N d(d−1)/4 (N 1/2
at d = 2, N 3/2 at d = 3, N 15/2 at d = 6). Even more surprisingly, imposing matrix symmetry
Symd([0, N ]) triggers a deep number-theoretic obstruction: at d = 2, Landau’s theorem on sums
of two squares forces σsym 2 (N )/σ2(N ) → 0, cleanly separating symmetric and non-symmetric
spectral packing. Table 1 summarizes the complete landscape proved in this paper.
Notation. For integers d ≥ 1 and N ≥ 1, let [0, N ] = {0, 1, . . . , N }, let Md([0, N ]) denote
the set of d × d matrices with entries in [0, N ], and let Symd([0, N ]) ⊆ Md([0, N ]) denote the
symmetric matrices. Write σd(N ), σsym d (N ), and σcomm d (N ) for the maximum cardinalities
of strong Spectral Sidon Sets in Md([0, N ]), in Symd([0, N ]), and among pairwise commuting
subsets of Md([0, N ]), respectively. Over a finite field Fq, write σd(Fq), σsym d (Fq), σsplit d (Fq), and
σell d (Fq) for the corresponding maxima over Md(Fq), Symd(Fq), simultaneously Fq-diagonalizable
subsets, and embeddings of the elliptic torus Fqd ↪→ Md(Fq). Throughout, asymptotic constants
in Od(·), Ωd(·), Θd(·) may depend on d but not on N or q.
2 Universal Commuting Ceilings and the Elementary Box Sidon
Lemma
We first establish a completely general upper bound on commuting Spectral Sidon Sets in
Md([0, N ]). If A ⊆ Symd([0, N ]) commutes, its elements are simultaneously orthogonally diag-
onalizable, so dimR spanR(A) ≤ d, and coordinate projection immediately bounds |A + A| ≤
(2N + 1)d. For non-symmetric commuting families, however, Schur’s classical theorem [12] al-
lows commutative subalgebras of Md(Q) to have dimension as large as ⌊d2/4⌋ + 1 via nilpotent
radicals (e.g., dim = 5 > 4 at d = 4). Remarkably, nilpotent blocks cannot assist spectral
packing at all: a discriminant-free 𝓁∞-packing argument in Minkowski space seals the Od(N d/2)
ceiling for every commuting subset of Md([0, N ]).
Theorem 2.1 (Universal Commuting Ceiling). Let d ≥ 1, N ≥ 1, and let A ⊆ Md([0, N ])
be any pairwise commuting family of integer matrices (not assumed symmetric, normal, or
diagonalizable).
3
```

---

## Page 4

```text
(a) If A is a strong Spectral Sidon Set, then
|A| ≤
√
2 (4dN + 1)d/2.
If A is a weak Spectral Sidon Set, then |A| ≤
√
2 (4dN + 1)d/2 + 1.
(b) If moreover every matrix in A is symmetric (or more generally, diagonalizable over C),
then |A| ≤
√
2 (2N + 1)d/2 (strong) and |A| ≤ √ 2 (2N + 1)d/2 + 1 (weak).
(c) These bounds are tight up to d-dependent constants: σcomm d (N ) = Θd(N d/2).
Proof. Part (a). Let R = Q[A] ⊆ Md(Q) be the commutative Q-subalgebra generated by A
and Id, and let N = Nil(R) be its nilradical. The quotient ¯R = R/N is a finite-dimensional
commutative reduced Q-algebra; by the Wedderburn–Artin theorem, there is a Q-algebra iso-
morphism
π = (π1, . . . , πm) : R −→ R/N ∼= L1 × L2 × · · · × Lm,
where each Lj /Q is a finite field extension of degree dj := [Lj : Q].
View V = Qd as a faithful R-module and choose a composition series 0 = V0 ⊂ V1 ⊂
· · · ⊂ Vt = V . Because N is nilpotent, it annihilates every simple R-module Vi/Vi−1, so each
composition factor is isomorphic as an R-module to one of the residue fields Lj(i). We claim
that every Lj (1 ≤ j ≤ m) occurs at least once among {Lj(1), . . . , Lj(t)}. Indeed, by idempotent
lifting modulo the nilpotent ideal N, the j-th primitive idempotent of ¯R lifts to an idempotent
ej = e2 j ∈ R with π(ej ) = (0, . . . , 1, . . . , 0). If Lj did not appear among the composition factors,
then ej would act as zero on every Vi/Vi−1, forcing et j = 0 on V ; since ej is idempotent, ej = 0
on V , contradicting the faithfulness of V (as ej /∈ N). Letting mj ≥ 1 be the multiplicity of Lj
in the composition series, we obtain both
m∑
j=1
dj ≤
m∑
j=1
mj dj = dimQ(V ) = d
and the exact characteristic-polynomial factorization for every X ∈ R:
χX (t) =
t∏
i=1
χX|Vi/Vi−1 (t) =
m∏
j=1
(
NLj [t]/Q[t]
(
t − πj (X)
))mj
.
In particular, χX (t) is completely determined by the tuple (π1(X), . . . , πm(X)) ∈ ∏m j=1 Lj .
Now let X ∈ A + A ⊆ Md([0, 2N ]). By Cayley–Hamilton, χX (X) = 0 where χX ∈ Z[t] is
monic; applying the ring homomorphism πj yields χX (πj (X)) = 0, so πj (X) lies in the ring of
integers OLj [9]. Furthermore, every complex embedding σ : Lj ↪→ C sends πj (X) to a root
of χX (t), i.e., an eigenvalue of X. Since every entry of X lies in [0, 2N ], Gershgorin’s circle
theorem [6] gives |λ| ≤ ‖X‖∞ ≤ 2dN for every eigenvalue λ of X, hence
‖πj (X)‖∞ := max σ:Lj ↪→C |σ(πj (X))| ≤ 2dN.
To count the set Sj := {α ∈ OLj : ‖α‖∞ ≤ 2dN } independently of the discriminant of Lj , let
r1 and 2r2 be the numbers of real and complex embeddings of Lj (r1 + 2r2 = dj ), and consider
the Minkowski embedding ιj : Lj ↪→ Rr1 × Cr2 ∼= Rdj equipped with the product sup-norm
‖z‖∞. For any two distinct elements α ⁄= β in OLj , their nonzero difference α − β ∈ OLj \ {0}
has rational integer norm |NLj /Q(α − β)| = ∏ σ |σ(α − β)| ≥ 1; since the maximum dominates
the geometric mean,
‖ιj (α) − ιj (β)‖∞ = ‖α − β‖∞ ≥ 1.
4
```

---

## Page 5

```text
Consequently, the open 𝓁∞-balls B∞(ιj (α), 1 2 ) := (− 1 2 , 1 2 )r1 × D(0, 1 2 )r2 + ιj (α) for α ∈ Sj are
pairwise disjoint and contained in B∞(0, 2dN + 1 2 ). Since Vol(B∞(0, ρ)) = (2ρ)r1 (πρ2)r2 =
2r1 πr2 ρdj , volume comparison yields
|Sj | ≤ Vol
(
B∞(0, 2dN + 1 2 ) )
Vol
(
B∞(0, 1 2 ) ) =
(
2dN + 1 2
1
2
)dj
= (4dN + 1)dj .
Multiplying over j = 1, . . . , m and using ∑m j=1 dj ≤ d, the total number of distinct characteristic
polynomials realized on A + A is at most ∏m j=1(4dN + 1)dj ≤ (4dN + 1)d. For a strong Spectral
Sidon Set of cardinality M = |A|, we have M 2 2 < (M +1 2 ) ≤ (4dN + 1)d, giving M ≤ √ 2(4dN +
1)d/2. For a weak Spectral Sidon Set, (M −1)2 2 < (M 2 ) ≤ (4dN +1)d gives M ≤ √ 2(4dN +1)d/2 +1.
Part (b). Any commuting family of diagonalizable matrices over C is simultaneously diag-
onalizable, so W := spanC(A) has dimension r ≤ d. Choosing r matrix coordinate positions
(i1, j1), . . . , (ir, jr) such that the coordinate projection W → Cr is injective, every element of
A + A ⊆ Md([0, 2N ]) is uniquely determined by its r entries in [0, 2N ], so |A + A| ≤ (2N + 1)r ≤
(2N + 1)d, yielding the tighter bounds.
Part (c). The matching lower bound σcomm d (N ) = Ωd(N d/2) follows for all N ≥ 8d from
Lemma 2.2 below applied to the d-dimensional integer diagonal box ∏d k=1 ([ 2k−1 4d N, 2k 4d N ] ∩ Z ) ,
where the d eigenvalues of A + B remain strictly ordered and hence uniquely determine the
diagonal matrix A + B.
To keep our lower-bound constructions completely self-contained, we record an elementary
multi-dimensional Sidon packing lemma proved directly from Erdős and Turán’s 1941 parabola
construction [3] without invoking finite-field Singer difference sets.
Lemma 2.2 (Elementary Box Sidon Lemma). Let D ≥ 1 and let B = ∏D j=1[0, Lj − 1] ⊂ ZD
be an integer box with side lengths Lj ≥ 1 and volume V = ∏D j=1 Lj ≥ 2. Then B contains a
classical Sidon set S ⊆ B (all sums x + y with x ≤ y distinct in ZD) of cardinality
|S| ≥ 2−(D+6)/2 √ V .
Proof. Define the mixed-radix injection Φ : B → [0, W − 1] with W := 2DV by
Φ(x1, . . . , xD) :=
D∑
j=1
xj
j−1∏
r=1
(2Lr).
Because xj + yj ≤ 2(Lj − 1) < 2Lj for every x, y ∈ B, addition in Φ(B) produces zero carries,
so Φ(x) + Φ(y) = Φ(x′) + Φ(y′) in Z if and only if x + y = x′ + y′ in ZD.
Let p be the smallest odd prime satisfying 2p2 ≥ W . Since W ≥ 4, Bertrand’s postulate
yields
√
W/2 ≤ p ≤ 2
√
W . Consider the Erdős–Turán set [3]
Ep :=
{
2pk + (k2 mod p) : 0 ≤ k ≤ p − 1 } ⊂ [0, 2p2 − 1].
We recall the two-line verification that Ep is a Sidon set in Z: if 2p(k1 + k2) + (k2 1 mod p) +
(k2 2 mod p) = 2p(k3 + k4) + (k2 3 mod p) + (k2 4 mod p), then since the remainder sums lie in
[0, 2p − 2] < 2p, both k1 + k2 = k3 + k4 in Z and k2 1 + k2 2 ≡ k2 3 + k2 4 (mod p); since p is odd, this
forces (k1 − k2)2 ≡ (k3 − k4)2 (mod p) and hence {k1, k2} = {k3, k4}.
Embed Ep into the cyclic group Z/(4p2)Z. Because Ep ⊂ [0, 2p2 − 1], no wraparound occurs
in Ep + Ep ⊂ [0, 4p2 − 2], so Ep is a Sidon set in Z/(4p2)Z, and so is every translate Ep + t
(mod 4p2). Averaging over all t ∈ Z/(4p2)Z,
1
4p2
4p2−1∑
t=0
⏐⏐(Ep + t) ∩ Φ(B) ⏐⏐ = |Ep| · |Φ(B)| 4p2 = V 4p ≥ V 8 √ 2DV = 2−(D+6)/2 √ V .
Choosing t∗ attaining at least the average and setting S := Φ−1((Ep + t∗) ∩ Φ(B)) yields a Sidon
set in B (since 2W ≤ 4p2 prevents wraparound on Φ(B)+Φ(B)) of size at least 2−(D+6)/2√ V .
5
```

---

## Page 6

```text
3 Exact Asymptotic Determination of σd(N ) via Hierarchical
Hessenberg Spectral Decoding
We now prove our main constructive theorem: over Md([0, N ]), non-commutativity achieves
the exact information-theoretic exponent d(d+1) 4 for every dimension d ≥ 2. The heart of the
proof is a surprising rigidity phenomenon for integer upper-Hessenberg matrices: fixing the
first subdiagonal to 1 and spacing the diagonal into d separated bands makes the characteristic
polynomial map χS (t) globally injective across all
(d+1
2
)
full-scale integer entries of S = A + A′.
Theorem 3.1 (Exact Optimal Exponent in Md([0, N ])). For every integer d ≥ 2,
σd(N ) = Θd
(
N
d(d+1)
4
)
.
In particular, σd(N )/σcomm d (N ) = Θd ( N d(d−1)/4) → ∞ as N → ∞.
The upper bound follows immediately from the coeﬀicient box: for any S ∈ Md([0, 2N ]),
each k-th principal minor sum ek(S) satisfies |ek(S)| ≤
(d
k
)
k! (2N )k, so the number of distinct
characteristic polynomials realized by Md([0, 2N ]) is at most
d∏
k=1
(
2
(d
k
)
k! (2N )k + 1
)
= Od
(
N
∑d
k=1 k
)
= Od
(
N
d(d+1)
2
)
,
whence
(σd(N )+1
2
)
≤ Od(N d(d+1)/2) and σd(N ) = Od(N d(d+1)/4).
For the matching lower bound, fix d ≥ 2, define the explicit constant
cd := 1 22d (4d)d−1 , (1)
and consider any N ≥ max(8d, ⌈2/cd⌉). Define the
(d+1
2
)
-dimensional upper-Hessenberg matrix
box Hd(N ) ⊂ Md([0, N ]) consisting of all matrices A = (aij ) such that:
• Fixed subdiagonal: ai+1,i = 1 for 1 ≤ i ≤ d − 1, and ai,j = 0 for all i ≥ j + 2;
• Separated diagonal bands: ak,k ∈
[ 2k−1
4d N, 2k 4d N ] ∩ Z for 1 ≤ k ≤ d;
• Full-scale upper triangle: ai,j ∈ [0, ⌊cdN ⌋] ∩ Z for all 1 ≤ i < j ≤ d.
Every sum S = A+A′ with A, A′ ∈ Hd(N ) is an upper-Hessenberg integer matrix with constant
subdiagonal si+1,i = 2, diagonal entries sk := sk,k ∈
[ 2k−1
2d N, 2k 2d N ] satisfying
min
i̸=j
|si − sj | ≥ N 2d , max i,j |si − sj | ≤ N, (2)
and upper-triangular entries ui,j := si,j ∈ [0, 2cdN ]. We prove that χS (t) uniquely determines
S via three clean lemmas.
Lemma 3.2 (Exact Hessenberg Interval-Cycle Expansion). Let S ∈ Md(Z) be upper-Hessenberg
with subdiagonal 2, diagonal (s1, . . . , sd), and upper-triangular entries {ui,j }1≤i<j≤d. Let Pd
denote the set of all partitions I = {[a1, b1], . . . , [ar, br]} of subsets of {1, . . . , d} into pairwise
disjoint contiguous intervals of length 𝓁α + 1 := bα − aα + 1 ≥ 2 (r = |I| ≥ 0). Then |Pd| = 2d−1
and
χS (t) =
d∏
m=1
(t − sm) −
∑
I∈Pd\{∅}
(−1)r−1
( r∏
α=1
2𝓁α uaα,bα
) ∏
m /∈∪ I
(t − sm). (3)
6
```

---

## Page 7

```text
Proof. Every permutation π ∈ Sd contributing a nonzero term sgn(π) ∏d i=1(tId − S)i,π(i) to
det(tId −S) satisfies π(i) ≥ i−1 for all i (since (tId −S)i,j = 0 whenever i ≥ j +2). Equivalently,
π−1(j) ≤ j + 1 for all j, so every cycle of π of length 𝓁 + 1 ≥ 2 must be a contiguous descending
cycle (b → b − 1 → · · · → a → b) with b − a = 𝓁 ≥ 1, using the single upper-triangular entry
(tId − S)a,b = −ua,b together with the 𝓁 subdiagonal entries (tId − S)r,r−1 = −2 (a < r ≤ b). Its
contribution to det(tId − S) is
sgn(cycle) · (−2)𝓁 · (−ua,b) = (−1)𝓁 · (−1)𝓁2𝓁 · (−ua,b) = −2𝓁ua,b.
Multiplying across r disjoint cycles yields (−1)r ∏r α=1(2𝓁α uaα,bα ) = −(−1)r−1 ∏r α=1(2𝓁α uaα,bα ),
proving (3). Finally, Pd is in exact bijection with subsets E ⊆ {1, . . . , d − 1} by taking
connected components of the graph on {1, . . . , d} with edge set E (discarding isolated ver-
tices), so |Pd| = 2d−1. (The cases d = 3, 4 are additionally checked identically in Lean 4 as
hessenberg_d3_cycle_expansion and hessenberg_d4_cycle_expansion.)
Lemma 3.3 (Stage-0 Root Isolation). For every S ∈ Hd(N ) + Hd(N ) with cd given by (1) and
N ≥ 8d, the polynomial χS (t) has d simple real roots λ1 < · · · < λd satisfying |λk − sk| < 1 2 for
every k ∈ {1, . . . , d}. In particular, sk = round(λk) is uniquely determined by χS (t).
Proof. Write χS (t) = B(t) − P (t), where B(t) = ∏d m=1(t − sm) and P (t) is the sum over
I ∈ Pd \ {∅} in (3). Fix k ∈ {1, . . . , d} and evaluate at t± := sk ± 1 2 . By (2) and N ≥ 8d, every
m ⁄= k satisfies
N
4d ≤ N 2d − 1 2 ≤ |t± − sm| ≤ N + 1 2 ≤ 2N,
whence |B(t±)| ≥ 1 2 ( N 4d )d−1 . On the other hand, for any nonempty I ∈ Pd with r ≥ 1 intervals
covering L := ∑r α=1(𝓁α +1) ≥ 2r vertices, we have ∑r α=1 𝓁α = L−r and d+r −L ≤ d−r ≤ d−1.
Since 2cd ≤ 1, the magnitude of the I-term at t± is bounded by
2L−r(2cdN )r(2N )d−L = 2d−r(2cd)rN d+r−L ≤ 2d−1(2cd)N d−1.
Summing over all |Pd \ {∅}| = 2d−1 − 1 < 2d−1 nonempty partitions and substituting (1) gives
|P (t±)| < 2d−1 · 2d−1(2cd)N d−1 = 22d−1cdN d−1 = 1 2 ( N 4d )d−1 ≤ |B(t±)|.
Hence sgn(χS (sk ± 1 2 )) = sgn(B(sk ± 1 2 )). Because B(sk − 1 2 ) and B(sk + 1 2 ) have opposite signs,
the Intermediate Value Theorem produces a real root λk ∈ (sk − 1 2 , sk + 1 2 ) for each k = 1, . . . , d.
Since these d intervals are disjoint and deg χS = d, they account for all roots of χS .
Lemma 3.4 (Superdiagonal-by-Superdiagonal Exact Residue Peeling). Under the hypotheses
of Lemma 3.3, every upper-triangular entry ui,j (1 ≤ i < j ≤ d) is uniquely recovered from
χS (t).
Proof. We proceed by strong induction on the superdiagonal distance 𝓁 = j −i ∈ {1, 2, . . . , d−1}.
Suppose that the diagonal (s1, . . . , sd) (recovered by Lemma 3.3) and all upper-triangular entries
ua,b with 1 ≤ b − a < 𝓁 have already been recovered exactly. Let S(𝓁−1) denote the upper-
Hessenberg matrix obtained from S by retaining all known entries with b − a < 𝓁 and zeroing all
entries with b − a ≥ 𝓁. By Lemma 3.2, the known residual polynomial P𝓁(t) := χS(ℓ−1) (t) − χS (t)
equals the sum of all terms in (3) whose partition I contains at least one interval of length
≥ 𝓁 + 1:
P𝓁(t) = 2𝓁
d−𝓁∑
a=1
ua,a+𝓁
∏
m /∈[a,a+𝓁]
(t − sm)
| {z }
Lℓ(t)
+ E𝓁(t), (4)
where every partition I contributing to the error polynomial E𝓁(t) satisfies one of two cases:
7
```

---

## Page 8

```text
• Case A (r = 1, single interval of length 𝓁′ + 1 ≥ 𝓁 + 2): Here L = 𝓁′ + 1 ≥ 𝓁 + 2. For any
i ∈ {1, . . . , d − 𝓁}, using |si − sm| ≤ N from (2), the term magnitude at t = si is at most
2𝓁′ (2cdN )N d−1−𝓁′ = 2𝓁′+1cdN d−𝓁′ ≤ 2dcdN d−𝓁−1.
• Case B (r ≥ 2 intervals, at least one of length ≥ 𝓁+1): Here L ≥ (𝓁+1)+2(r−1) = 𝓁+2r−1,
so d + r − L ≤ d − 𝓁 − r + 1 ≤ d − 𝓁 − 1. Since cd ≤ 1, the term magnitude at t = si is at
most
2L−r(2cdN )rN d−L = 2Lcr dN d+r−L ≤ 2dcdN d−𝓁−1.
Summing over at most |Pd \ {∅}| < 2d−1 partitions yields |E𝓁(si)| < 22d−1cdN d−𝓁−1 for every
i ∈ {1, . . . , d − 𝓁}.
We now recover ui,i+𝓁 sequentially for i = 1, 2, . . . , d − 𝓁. At t = si, the product∏
m /∈[a,a+𝓁](si − sm) vanishes whenever i /∈ [a, a + 𝓁], so the only surviving terms in L𝓁(si) satisfy
a ≤ i ≤ a + 𝓁—that is, a = i together with indices a ∈ {max(1, i − 𝓁), . . . , i − 1} whose values
ua,a+𝓁 have already been recovered exactly in earlier iterations of the i-loop! Subtracting those
exact known terms from P𝓁(si) leaves
Ri,𝓁 := P𝓁(si) − 2𝓁
i−1∑
a=max(1,i−𝓁)
ua,a+𝓁
∏
m /∈[a,a+𝓁]
(si − sm) = Di,𝓁 ui,i+𝓁 + E𝓁(si),
where Di,𝓁 := 2𝓁 ∏ m /∈[i,i+𝓁](si − sm). By (2), |Di,𝓁| ≥ 2𝓁 ( N 2d )d−𝓁−1 . Dividing |E𝓁(si)| by |Di,𝓁|,
all powers of N cancel identically:
⏐⏐⏐⏐ Ri,𝓁 Di,𝓁 − ui,i+𝓁 ⏐⏐⏐⏐ = |E𝓁(si)| |Di,𝓁| < 22d−1cdN d−𝓁−1 2𝓁(2d)−(d−𝓁−1)N d−𝓁−1 ≤ 22d−2(2d)d−2cd < 1 2 ,
by (1). Because ui,i+𝓁 is an integer, ui,i+𝓁 = round(Ri,𝓁/Di,𝓁) is recovered with zero error,
preventing any error propagation across i or 𝓁. Inducting over i = 1, . . . , d−𝓁 and 𝓁 = 1, . . . , d−1
recovers the entire matrix S uniquely.
Proof of Theorem 3.1. By Lemmas 3.3 and 3.4, the characteristic polynomial map S ↦→ χS (t) is
globally injective on Hd(N )+Hd(N ). The box Hd(N ) has dimension D = d(d+1) 2 and cardinality
|Hd(N )| =
d∏
k=1
Ωd(N ) ·
∏
1≤i<j≤d
(
⌊cdN ⌋ + 1
)
= Ωd
(
N
d(d+1)
2
)
.
Applying Lemma 2.2 to Hd(N ) yields a classical Sidon set A ⊆ Hd(N ) of size |A| =
Ωd(N d(d+1)/4). Because all pairwise matrix sums A + B (A ≤ B ∈ A) are distinct elements
of Hd(N ) + Hd(N ) and χ is injective on Hd(N ) + Hd(N ), A is a strong Spectral Sidon Set in
Md([0, N ]).
Remark 3.5 (Sharp Explicit Constants for Small d). At d = 2 and d = 3, Lean 4 directly
verifies tight elementary recovery bounds (Theorems hessenberg_d2_exact_recovery and
hessenberg_d3_exact_offdiag_recovery in SpectralSidonCore.lean) without asymptotic
slack: at d = 2, s1 − s2 ≥ N and 0 ≤ 8u < 2N + 1 suﬀice for exact recovery of (s1, s2, u), while
our verification script confirms 50/50 exact decoding across d ∈ {2, 3, 4, 5} at practical ratios
c2 = 0.05, c3 = 0.006, c4 = 5 × 10−4, c5 = 4 × 10−5.
8
```

---

## Page 9

```text
4 The Symmetric–Non-Symmetric Arithmetic Rift and Jacobi-
Band Breakthrough
A natural question is whether symmetric integer matrices Symd([0, N ]) can match the optimal
Θd(N d(d+1)/4) scaling of Theorem 3.1. At d = 2, we prove that the answer is emphatically no:
symmetry forces a deep arithmetic obstruction governed by Landau’s theorem on sums of two
squares, cleanly separating σsym 2 (N ) from σ2(N ).
Theorem 4.1 (Landau–Ramanujan Separation and Hyperbolic Ford Barrier). Let KLR =
1√
2
∏
p≡3 (mod 4)(1 − p−2)−1/2 ≈ 0.76422365 denote the Landau–Ramanujan constant, and let
δ = 1 − 1+log log 2 log 2 ≈ 0.08607133 denote the Erdős–Ford multiplication-table exponent.
(a) Every strong (or weak) Spectral Sidon Set A ⊆ Sym2([0, N ]) satisfies
σsym 2 (N ) ≤ (√ 30 √ 2 KLR + o(1) ) N 3/2 (log N )1/4 = o ( σ2(N ) ) .
(b) In the hyperbolic equal-diagonal subspace Hhyp 2 ([0, N ]) :=
{(a b
c a
)
: a, b, c ∈ [0, N ]
}
⊂
M2([0, N ]), the maximum Spectral Sidon size satisfies
Ω(N ) ≤ max
A⊆Hhyp 2 ([0,N ]) |A| = O
(
N 3/2
(log N )δ/2(log log N )3/4
)
= o
(
σ2(N )
)
.
Proof. Part (a). For any S =
(s1 u
u s2
)
∈ Sym2([0, 2N ]), the characteristic polynomial χS (t) =
t2 − T t + D is uniquely determined by the trace T = s1 + s2 ∈ [0, 4N ] and the discriminant
disc(S) := T 2 − 4D = (s1 − s2)2 + (2u)2,
where |s1 − s2| ≤ 2N , 0 ≤ u ≤ 2N , and s1 − s2 ≡ T (mod 2). Let B(X) denote the number
of positive integers n ≤ X representable as a sum of two squares, and let Bodd(X) denote the
number of odd positive integers n ≤ X representable as a sum of two squares. By Landau’s
theorem [7], B(X) = (KLR + o(1)) X√log X . Because multiplying by 2 preserves representability
as a sum of two squares (2(a2 + b2) = (a + b)2 + (a − b)2), every positive sum of two squares
factors uniquely as 2km with k ≥ 0 and m an odd sum of two squares; consequently, B(X) =∑
k≥0 Bodd(X/2k), which inverts cleanly to
Bodd(X) = B(X) − B(X/2) =
( 1
2 KLR + o(1)
) X√log X .
Splitting over the parity of T ∈ [0, 4N ]:
• For each even T (2N +1 values), disc(S)/4 = ((s1 −s2)/2)2 +u2 ∈ [0, N 2 +4N 2] = [0, 5N 2]
is a non-negative sum of two squares, giving at most B(5N 2) + 1 admissible discriminants.
• For each odd T (2N values), disc(S) = (s1 − s2)2 + (2u)2 ∈ [1, 4N 2 + 16N 2] = [1, 20N 2]
is an odd sum of two squares, giving at most Bodd(20N 2) admissible discriminants.
Summing over all T ∈ [0, 4N ] and using
√
log(cN 2) = ( √ 2 + o(1))√log N yields
#{χS : S ∈ Sym2([0, 2N ])} ≤ (2N + 1)
(
B(5N 2) + 1 ) + 2N Bodd(20N 2)
=
( 10KLR√
2 + 20KLR√ 2 + o(1) ) N 3 √log N
=
( 30KLR√
2 + o(1)
) N 3
√log N .
9
```

---

## Page 10

```text
Since 1 2 |A|2 < (|A|+1 2 ) ≤ #{χS } (and similarly 1 2 (|A| − 1)2 < (|A| 2 ) for weak sets), taking square
roots gives
σsym 2 (N ) ≤
(√
30
√
2 KLR + o(1)
) N 3/2
(log N )1/4 = o
(
σ2(N )
)
,
where the strict asymptotic separation follows from Theorem 3.1 (σ2(N ) = Θ(N 3/2)).
Part (b). For any S =
(s u
v s
)
∈ Hhyp 2 ([0, 2N ]), we have tr(S) = 2s ∈ [0, 4N ] (2N +1 values)
and det(S) = s2 − uv, where u, v ∈ [0, 2N ]. By Ford’s theorem on the multiplication table [4],
the number of distinct products uv with u, v ∈ [1, 2N ] is Θ
(
N 2(log N )−δ (log log N )−3/2) (plus
1 for uv = 0). Multiplying by 2N + 1 choices for s and taking square roots yields the stated
upper bound. Conversely, fixing c = 1 yields S = A + A′ =
(s u
2 s
)
, whose (tr(S), det(S)) =
(2s, s2 − 2u) uniquely determines (s, u) on the 2D box [0, N ]2; applying Lemma 2.2 yields an
explicit strong Spectral Sidon Set of size Ω(N ).
Despite the Landau–Ramanujan barrier at d = 2, symmetric non-commuting matrices still
strictly surpass every commuting family in every dimension d ≥ 2 by a polynomial factor
N (d−1)/4.
Theorem 4.2 (Symmetric Jacobi-Band Breakthrough, Sharp Parity Threshold, and Spectral
Energy).
(a) For every integer d ≥ 2,
σsym d (N ) = Ωd
(
N
3d−1
4
)
,
strictly surpassing the universal commuting ceiling σcomm d (N ) = Θd(N d/2) by N (d−1)/4.
(b) Exact Rectangular Parity Injectivity Threshold at d = 2: Consider integer symmetric
sum-matrices S =
(s1 u
u s2
)
∈ Sym2([0, 2N ]) with diagonal gap X = s1 − s2 ≥ N and
off-diagonal entry u ∈ [0, U ].
• If U ≤
√
N (i.e., 2u ≤ 2
√
N ), then χS (t) is globally injective on the entire rectangular
domain;
• Conversely, for every N ≥ 20 and any shift c ≥ 0, as soon as U ≥
√
N +3 (i.e., 2U ≥
2
√
N +6) and the diagonal domain contains the shifted integer pairs (c+4k2, c+1) and
(c + 4k2 + 1, c) for k = ⌈ √ (N + 1)/4⌉ (which have diagonal gap X ∈ [N, 2N ]), there
exist distinct integer symmetric matrices S1 ⁄= S2 in the domain with χS1 (t) = χS2 (t).
(c) Spectral Additive Energy and Uniform Alteration Limitation: Let Espec(Sym2([0, N ])) :=
#{(A1, A2, A3, A4) ∈ Sym2([0, N ])4 : χA1+A2 = χA3+A4 }. Then
Ω
(
N 9√ log N ) ≤ Espec ( Sym2([0, N ]) ) ≤ O ( N 9 log N ) ,
and the numbers of 3-element and 2-element spectral collisions are O(N 6 log N ) and
O(N 3 log N ), respectively. Consequently, uniform probabilistic alteration on Sym2([0, N ])
yields strong Spectral Sidon Sets of size Ω
(
N/(log N )1/3) —strictly below both the commut-
ing ceiling Θ(N ) and our structured Jacobi-band construction Ω(N 5/4).
Proof. Part (a). Set csym d := 2−d(4d)−(d−1)/2 and let N ≥ max(8d, ⌈4/(csym d )2⌉). Define the
(2d − 1)-dimensional symmetric tridiagonal (Jacobi) box Jd(N ) ⊂ Symd([0, N ]) consisting of
symmetric tridiagonal matrices A with diagonal ak,k ∈
[ 2k−1
4d N, 2k 4d N ] ∩ Z (1 ≤ k ≤ d) and
subdiagonal aj+1,j = aj,j+1 ∈ [0, ⌊csym d √ N ⌋] ∩ Z (1 ≤ j ≤ d − 1).
10
```

---

## Page 11

```text
For any S = A + A′ ∈ Jd(N ) + Jd(N ), write sk = Sk,k and wj := S2 j+1,j ∈ [0, 4(csym d )2N ].
By the classical matching-polynomial expansion of tridiagonal matrices [5],
χS (t) =
d∏
m=1
(t−sm) −
d−1∑
j=1
wj
∏
m /∈{j,j+1}
(t−sm) +
∑
M ∈M(Pd)
|M |≥2
(−1)|M |

∏
j∈M
wj

 ∏
m /∈V (M )
(t−sm),
(5)
where M(Pd) is the set of matchings of the d-vertex path Pd (cardinality Fd+1 ≤ 2d−1).
Stage 0 (Root Isolation). Exactly as in Lemma 3.3, every nonempty matching M with
r = |M | ≥ 1 covers 2r vertices and contributes at t± = sk ± 1 2 at most (4(csym d )2N )r(2N )d−2r ≤
2d(csym d )2N d−1. Summing over < 2d−1 nonempty matchings gives |P (t±)| < 22d−1(csym d )2N d−1 = 1
2 (4d)−(d−1)N d−1 ≤ |B(t±)|, so sk = round(λk) is recovered uniquely for every k = 1, . . . , d.
Stage 1 (Telescoping Peeling for w1, . . . , wd−1). Let P (t) := ∏d m=1(t − sm) − χS (t) and
let E(t) be the sum over matchings M with |M | = r ≥ 2 in (5). At t = si (1 ≤ i ≤ d − 1),
every matching M with r ≥ 2 satisfies 4r(csym d )2rN d−r ≤ 16(csym d )4N d−2 (since 2csym d ≤ 1), so
|E(si)| < 2d+3(csym d )4N d−2. Evaluating P (si) sequentially for i = 1, . . . , d − 1: the linear sum∑d−1
j=1 wj
∏
m /∈{j,j+1}(si − sm) retains only j = i − 1 (already recovered exactly when i ≥ 2) and
j = i. Subtracting the j = i − 1 term and dividing by Di := ∏ m /∈{i,i+1}(si − sm) (which satisfies
|Di| ≥ (2d)−(d−2)N d−2) gives
|E(si)|
|Di| < 2d+3(2d)d−2(csym d )4 = 2d+3(2d)d−2 24d(4d)2d−2 < 1 2 .
Thus wi = round(. . . ) is recovered with zero error for every i = 1, . . . , d − 1; since Si+1,i ≥ 0,
taking Si+1,i = √wi recovers S uniquely. Because |Jd(N )| = Θd(N d ·N (d−1)/2) = Θd(N (3d−1)/2),
Lemma 2.2 yields a strong Spectral Sidon Set A ⊆ Jd(N ) of size Ωd(N (3d−1)/4).
Part (b). Suppose S =
(s1 u
u s2
)
and S′ =
(s′ 1 u′
u′ s′ 2
)
have equal trace T = s1 + s2 = s′ 1 + s′ 2
and equal discriminant X 2 + 4u2 = (X ′)2 + 4(u′)2, where X = s1 − s2 ≥ N , X ′ = s′ 1 − s′ 2 ≥ N ,
and 0 ≤ u, u′ ≤ √ N . Because s1 + s2 = s′ 1 + s′ 2, we have X ′ − X = 2(s′ 1 − s1) ≡ 0 (mod 2). If
X < X ′, then X ′ ≥ X + 2, so
(X ′)2 + 4(u′)2 ≥ (X + 2)2 = X 2 + 4X + 4 ≥ X 2 + 4N + 4 > X 2 + 4u2,
contradiction (and symmetrically if X ′ < X). Thus X = X ′, forcing u2 = (u′)2 and hence
(s1, s2, u) = (s′ 1, s′ 2, u′) (formalized in Lean 4 as sym2_even_parity_injectivity_threshold).
Conversely, for every integer k ≥ 1, the two distinct integer symmetric matrices
S1 =
(4k2 2k
2k 1
)
, S2 =
(4k2 + 1 0
0 0
)
have identical trace 4k2 + 1 and identical determinant 0 (formalized in Lean 4 as sym2_sharp_
rectangular_barrier_collision), with matching-parity diagonal gaps X1 = 4k2 − 1, X2 =
4k2 + 1, and off-diagonal entry u1 = 2k. Shifting both matrices by cI2 (c ≥ 0) preserves
χS1+cI2 (t) = χS2+cI2 (t), the diagonal gaps X1, X2, and u1 = 2k. Choosing k = ⌈
√
(N + 1)/4⌉
gives X1 ∈ [N, 2N − 2] for all N ≥ 20 and u1 = 2k ≤
√
N + 3 (so 2u1 ≤ 2
√
N + 6).
Part (c). Let V = Sym2([0, N ]), so |V| = (N + 1)3. For any (T, m) ∈ [0, 4N ] × [0, 20N 2], let
N (T, m) count ordered pairs (A1, A2) ∈ V 2 with tr(A1 + A2) = T and disc(A1 + A2) = m. Each
sum S = A1 + A2 ∈ Sym2([0, 2N ]) with (tr(S), disc(S)) = (T, m) satisfies (s1 − s2)2 + (2u)2 = m
(at most r2(m) choices for S, where r2(m) := #{(x, y) ∈ Z2 : x2 +y2 = m}), and each fixed S has
at most (N +1)3 representations S = A1 +A2 with A1, A2 ∈ V. Hence N (T, m) ≤ (N +1)3r2(m).
11
```

---

## Page 12

```text
By the classical Dirichlet–Ramanujan second-moment bound ∑ m≤X r2(m)2 = O(X log X),
Espec(V) =
4N∑
T =0
20N 2 ∑
m=0
N (T, m)2 ≤ (4N + 1)(N + 1)6
20N 2 ∑
m=0
r2(m)2 = O ( N 9 log N ) .
Conversely, by Cauchy–Schwarz and the characteristic-polynomial count #{χS : S ∈
Sym2([0, 2N ])} = O(N 3/√log N ) from Theorem 4.1(a),
Espec(V) =
∑
χ
N (χ)2 ≥ |V|4
#{χS } = (N + 1)12 O(N 3/√log N ) = Ω ( N 9√ log N ) .
There are two configurations of 3-element spectral collisions among distinct matrices A, B, C ∈
V:
(i) χA+B = χA+C (B ⁄= C): fixing A ∈ V ((N + 1)3 choices) and the shared trace TB = TC ∈
[0, 2N ] (2N + 1 choices), both A + B and A + C share trace TA + TB and discriminant
m ≤ 20N 2, giving at most r2(m) choices for B and r2(m) for C.
(ii) χ2A = χB+C (A, B, C distinct): fixing B ∈ V ((N + 1)3 choices), TA ∈ [0, 2N ] (2N + 1
choices), and m := disc(A) ∈ [0, 5N 2], there are at most r2(m) choices for A, while
S = B +C has fixed trace 2TA and discriminant disc(2A) = 4m, yielding at most r2(4m) =
r2(m) choices for S and hence for C = S − B.
Summing both cases over all parameters gives a combined 3-element collision bound
C3 ≤ 2(N + 1)3(2N + 1)
20N 2 ∑
m=0
r2(m)2 = O ( N 6 log N ) .
Similarly, for 2-element collisions χ2A = χ2B (A ⁄= B) or χ2A = χA+B (A ⁄= B), trace equality
forces TA = TB ∈ [0, 2N ] and discriminant equality forces disc(A) = disc(B) = m ≤ 5N 2
or disc(A + B) = 4disc(A) = 4m (noting r2(4m) = r2(m)), so fixing TA and m gives at most
r2(m)2 ordered pairs (A, B) in either case, whence C2 ≤ 2(2N +1) ∑5N 2 m=0 r2(m)2 = O(N 3 log N ).
Sampling each matrix in V independently with probability p = cN −2(log N )−1/3 gives E[|A0|] =
cN (log N )−1/3 while the expected total number of 4-, 3-, and 2-element collisions is
p4Espec(V) + p3C3 + p2C2 = O ( c4N (log N )−1/3) + O(c3) + O ( N −1(log N )1/3) ≤ 1 2 E[|A0|]
for suﬀiciently small c > 0 and large N . Deleting one element from each surviving collision
yields a strong Spectral Sidon Set of size Ω(N/(log N )1/3).
5 Finite-Field Spectral Sidon Sets: Characteristic-2 Collapse,
Commuting Ceilings, and Galois-Torus Hierarchies
Over a finite field Fq, every monic polynomial of degree d has qd possible coeﬀicient tuples, so
the absolute counting upper bound for any strong Spectral Sidon Set in Md(Fq) is
(|A| + 1
2
)
≤ qd =⇒ σd(Fq) ≤
⌊√
8qd + 1 − 1
2
⌋
= (
√
2 + o(1)) qd/2.
In stark contrast to the integer box (where non-commutativity changed the exponent of N ), over
Fq the exponent qd/2 is fixed by counting, while the leading constant exhibits a rich algebraic
hierarchy governed by characteristic, commutativity, and Galois group order.
12
```

---

## Page 13

```text
Figure 1: Asymptotic growth exponent α in |A| ≍ N α across matrix dimension d = 1, . . . , 6,
illustrating the unbounded polynomial gap N d(d−1)/4 between the universal commuting ceiling
d/2 (Theorem 2.1), the symmetric Jacobi-band lower bound (3d − 1)/4 (Theorem 4.2), and the
exact non-commuting optimum d(d + 1)/4 (Theorem 3.1).
Theorem 5.1 (Characteristic-2 Collapse, Exact d = 2 Commuting Ceiling, and Non-Commu-
tative Witnesses).
(a) Characteristic-2 Collapse: For every d ≥ 1 and every q = 2m, σd(Fq) = 1 (strong).
(b) Exact d = 2 Commuting Ceiling and Matching Lower Bound: For every odd prime power
q and every pairwise commuting subset A ⊆ M2(Fq) (split, elliptic, or Jordan),
|A| ≤ q (strong), |A| ≤ q + 1 (weak).
Conversely, for every prime power q = pk of characteristic p ≥ 5, the elliptic torus Fq2 ↪→
M2(Fq) contains a commuting strong Spectral Sidon Set of size at least ⌊(p−1)/4⌋ p q ≥ q 7 .
(c) Strict Non-Commutative Separation: For every q ∈ {5, 7, 11, 13}, there exist explicit
non-commuting strong Spectral Sidon Sets in Sym2(Fq) strictly exceeding the universal
commuting ceiling q:
σsym 2 (F5) = 6 > 5, σsym 2 (F7) ≥ 8 > 7,
σsym 2 (F11) ≥ 12 > 11, σsym 2 (F13) ≥ 14 > 13.
Moreover, in d = 3, explicit witnesses in Sym3(F3) and Sym3(F5) achieve σsym 3 (F3) = 6 > 4
(saturating the absolute counting ceiling and beating both split and elliptic ceilings by 50%)
and σsym 3 (F5) ≥ 12 > 9 > 7 (strictly beating both the split ceiling 7 and elliptic ceiling 9).
Proof. Part (a). In characteristic 2, A + A = 0 for every A ∈ Md(F2m ), so χA+A(t) = td for all
A ∈ A. Any two distinct elements A ⁄= B collide on their self-sums {A, A} and {B, B}.
Part (b). Every commutative subalgebra R = Fq[A] ⊆ M2(Fq) has dimFq (R) ≤ 2 over any
field Fq: if R ⊆ FqI2 then dimFq (R) = 1; otherwise R contains a non-scalar matrix M ∈ M2(Fq)
whose minimal polynomial has degree 2, so M is cyclic on F2 q and its centralizer in M2(Fq) equals
Fq[M ] of dimension 2. Up to GL2(Fq)-conjugacy, any 2-dimensional commutative subalgebra
of M2(Fq) falls into exactly one of three isomorphism classes:
13
```

---

## Page 14

```text
1. Split torus R ∼= Fq × Fq: χX (t) = (t − x)(t − y) is determined by the unordered pair
{x, y} ⊂ Fq, giving exactly
(q+1
2
)
= q(q+1) 2 distinct characteristic polynomials.
2. Elliptic torus R ∼= Fq2 : each z ∈ Fq has χz (t) = (t − z)2 (q polynomials), while each
z ∈ Fq2 \ Fq shares its irreducible characteristic polynomial (t − z)(t − zq) with its unique
Frobenius conjugate zq, giving q + q2−q 2 = q(q+1) 2 distinct characteristic polynomials.
3. Non-semisimple Jordan algebra R ∼= Fq[ε]/(ε2): every matrix is conjugate to
(a b
0 a
)
with
χ(t) = (t − a)2, giving only q ≤ q(q+1) 2 characteristic polynomials.
In all three cases, |{χA+B }| ≤ q(q+1) 2 . Thus m(m + 1) ≤ q(q + 1) forces m ≤ q (strong),
and m(m − 1) ≤ q(q + 1) forces m ≤ q + 1 (weak), both formally certified in Lean 4
(fq_d2_universal_commuting_ceiling). For the matching lower bound when q = pk with
p ≥ 5, embed Fq2 = Fq(√ε) ↪→ M2(Fq) (for a non-square ε ∈ F× q ), so Frobenius conjugation
sends (x, y) ↦→ (x, −y). Choose any surjective Fp-linear functional λ : Fq → Fp, and set
H := {y ∈ Fq : 1 ≤ λ(y) ≤ ⌊(p − 1)/4⌋} (viewing Fp = {0, . . . , p − 1}), which satisfies
(H + H) ∩ (−(H + H)) = ∅ and |H| = ⌊(p−1)/4⌋ p q ≥ q 7 for every prime p ≥ 5 (specifically 1/5
for p = 5, 1/7 for p = 7, 2/11 for p = 11, and at least p−4 4p ≥ 9 52 > 1 7 for all p ≥ 13). The
parabola P := {(x, x2) : x ∈ Fq} ⊂ F2 q is a classical Sidon set of size q (since q is odd), and so
is every translate P + v (v ∈ F2 q ). Averaging |(P + v) ∩ (Fq × H)| over v ∈ F2 q yields a translate
of size at least |P | · |H|/q = |H| ≥ q/7 whose pairwise sums never collide with their Frobenius
conjugates.
Part (c). For odd q, the linear bijection (t, x, y) ↦→
((t + x)/2 y/2
y/2 (t − x)/2
)
identifies
Sym2(Fq) with F3 q such that tr(A+B) = tA +tB and disc(A+B) = (xA +xB )2 +(yA +yB )2 ∈ Fq.
The four explicit witnesses
A5 = {(0, 1, 1), (0, 3, 0), (1, 2, 1), (2, 0, 0), (3, 2, 4), (4, 1, 4)} ⊂ F3 5,
A7 = {(0, 4, 1), (2, 3, 2), (3, 0, 5), (3, 2, 4), (4, 4, 0), (4, 5, 0), (5, 0, 2), (6, 0, 4)} ⊂ F3 7,
A11 = {(0, 0, 2), (0, 0, 10), (1, 7, 8), (2, 9, 8), (3, 0, 0), (4, 1, 0),
(6, 6, 0), (6, 10, 2), (7, 4, 6), (8, 3, 3), (9, 6, 7), (10, 3, 2)} ⊂ F3 11,
A13 = {(0, 12, 1), (1, 6, 3), (1, 11, 7), (3, 4, 2), (4, 0, 1), (4, 10, 3), (5, 8, 10),
(6, 4, 2), (6, 8, 7), (7, 6, 10), (8, 8, 0), (9, 2, 4), (10, 4, 2), (12, 3, 6)} ⊂ F3 13
are kernel-verified in Lean 4 (decide in SpectralSidonCore.lean) to generate 21/25, 36/49,
78/121, and 105/169 pairwise distinct characteristic polynomials, respectively. Similarly,
parametrizing Sym3(Fq) by upper-triangular 6-tuples (a, b, c, e, f, i) ↦→


a b c
b e f
c f i

, the explicit
witnesses
B3 = {(0, 0, 0, 2, 2, 1), (0, 0, 1, 0, 0, 0), (0, 2, 1, 0, 0, 2),
(1, 0, 0, 2, 0, 2), (2, 2, 0, 0, 0, 0), (2, 2, 0, 0, 1, 2)} ⊂ F6 3,
B5 = {(0, 0, 2, 3, 4, 2), (0, 0, 3, 1, 0, 0), (0, 3, 4, 1, 4, 1), (0, 4, 2, 0, 4, 0),
(1, 0, 2, 0, 1, 2), (1, 2, 3, 1, 3, 4), (2, 1, 1, 4, 0, 3), (2, 1, 4, 3, 3, 2),
(2, 2, 3, 1, 1, 0), (4, 0, 1, 4, 4, 3), (4, 1, 2, 1, 4, 3), (4, 4, 0, 1, 0, 1)} ⊂ F6 5
yield 21/27 and 78/125 pairwise distinct cubic characteristic polynomials, respectively
(both kernel-verified in Lean 4 as sym3_F3_noncomm_witness_size_6 and sym3_F5_noncomm_
witness_size_12). Since
(7
2
)
= 21 ≤ 25 < 28 =
(8
2
)
and
(7
2
)
= 21 ≤ 27 < 28 =
(8
2
)
,
σsym 2 (F5) = 6 and σsym 3 (F3) = 6 are exact.
14
```

---

## Page 15

```text
In higher dimensions d ≥ 3, even within the class of commutative subalgebras of Md(Fp),
a dramatic super-exponential separation emerges between split diagonal tori (governed by the
symmetric Weyl group Sd of order d!) and non-split elliptic Galois tori Fpd ↪→ Md(Fp) (governed
by the cyclic Frobenius group Gal(Fpd /Fp) ∼= Z/dZ of order only d).
Theorem 5.2 (Super-Exponential Split-vs.-Elliptic Galois Torus Separation). Let d ≥ 2 and
let p be an odd prime.
(a) Every simultaneously Fp-diagonalizable Spectral Sidon Set A ⊆ Md(Fp) satisfies
σsplit d (Fp) ≤
√
2
(p + d − 1
d
)
=
√
2
d! pd/2 + Od(pd/2−1).
(b) For every even dimension d = 2r ≥ 2 and every prime p ≥ 7, let p′ be the largest odd
prime satisfying p′ ≤ p−1 2 . Embedding Fpd ↪→ Md(Fp) via the regular representation yields
σell d (Fp) ≥ 1 −
(d
2
)
/p′
d (p′)d/2.
In particular, by the Prime Number Theorem (p′ = ( 1 2 − o(1))p as p → ∞),
lim inf
p→∞
σell d (Fp)
pd/2 ≥ 1 d · 2d/2 ,
which strictly exceeds the universal split-diagonal constant
√
2/d! for every even d ≥ 8
and diverges super-exponentially as Θ
(
d−3/4(d/(2e))d/2) by Stirling’s formula.
(c) All Dimensions (Including Odd d): For every integer d ≥ 2 (even or odd) and every
prime p ≥ 9, applying Lemma 2.2 to the axis-aligned sub-box B0 :=
[
⌊ p−1 4 ⌋ + 1, ⌊ p−1 2 ⌋ ] ×[
0, ⌊ p−1 4 ⌋ ]d−1 ⊂ K0 yields
lim inf
p→∞
σell d (Fp)
pd/2 ≥ 1 8 · 8d/2 ,
which strictly exceeds
√
2/d! for every d ≥ 25 (including all odd d ≥ 25) and diverges
super-exponentially as Θ
(
d1/4(d/(8e))d/2) .
Proof. Part (a). Every matrix in A + A splits completely over Fp; there are exactly
(p+d−1
d
)
monic degree-d polynomials with all d roots in Fp, giving
(|A|+1
2
)
≤
(p+d−1
d
)
.
Part (b). By the Normal Basis Theorem [8], Fpd admits an Fp-basis {e0, e1, . . . , ed−1} such
that the Frobenius automorphism ϕ(z) = zp acts by cyclic coordinate shift: ϕ(∑d−1 k=0 ckek) =∑d−1
k=0 ck−1 mod dek. Under the regular representation ρ : Fpd ↪→ Md(Fp), two elements z, w ∈ Fpd
have the same characteristic polynomial χρ(z)(t) = ∏d−1 j=0 (t − zpj ) if and only if w = ϕj (z) for
some j ∈ {0, . . . , d − 1}.
Identify [0, p′ − 1]d ⊆ [0, p−1 2 ]d ⊂ Fd p via the normal basis. Because 2(p′ − 1) ≤ p − 3 < p,
addition of any two vectors in [0, p′ − 1]d suffers zero wraparound modulo p. Partition the
tie-free subset U := {c ∈ [0, p′ − 1]d : ci ⁄= cj ∀i ⁄= j} into its d cyclic cones
Km :=
{
c ∈ [0, p′ − 1]d : cm > cj ∀j ⁄= m } (0 ≤ m ≤ d − 1).
Each Km is closed under addition inside [0, p − 1]d: if c, c′ ∈ Km, then (c + c′)m = cm + c′ m >
cj + c′ j = (c + c′)j for all j ⁄= m. Hence Km + Km contains at most one element from every
Frobenius orbit!
15
```

---

## Page 16

```text
Now let d = 2r be even, identify Fd p′ ∼= F(p′)r × F(p′)r , and take the classical parabola Sidon
set S0 := {(x, x2) : x ∈ F(p′)r } of size (p′)r = (p′)d/2 (since p′ is odd, (x1 + x2, x2 1 + x2 2) uniquely
determines {x1, x2}). Every translate Sv := S0 + v (mod p′) (v ∈ Fd p′ ) remains a Sidon set
in Fd p′ , and hence also in Zd (and Fd p) when lifted to [0, p′ − 1]d. Averaging over v ∈ Fd p′ , the
expected number of elements of Sv lying in U is |S0| · |U |/(p′)d ≥ (p′)d/2(1 − (d 2 ) /p′) by the union
bound over pairs i < j. Picking a translate Sv∗ achieving at least this average, the Pigeonhole
Principle over the d disjoint cones K0, . . . , Kd−1 yields some Km with
|Sv∗ ∩ Km| ≥ 1 −
(d
2
)
/p′
d (p′)d/2.
Because Sv∗ ∩ Km is a Sidon set in Fd p whose sumset lies inside the orbit-free cone Km +
Km, its image under ρ : Fpd ↪→ Md(Fp) is a strong Spectral Sidon Set! Finally, Lean 4
(elliptic_torus_beats_split_all_d_ge_8) proves by induction that d! > 2d22d for every
d ≥ 8, which is equivalent to 1 d·2d/2 > √ 2 d! , and Stirling’s formula d! ∼ √ 2πd(d/e)d gives the
ratio
√
d!√
2 d·2d/2 = Θ
(
d−3/4(d/(2e))d/2) .
Part (c). For arbitrary d ≥ 2 and prime p ≥ 9, every c ∈ B0 :=
[
⌊ p−1 4 ⌋ + 1, ⌊ p−1 2 ⌋ ] ×[
0, ⌊ p−1 4 ⌋ ]d−1 satisfies c0 > cj (j ≥ 1) and 2cm ≤ p − 1 < p, so B0 + B0 suffers zero wraparound
and is Frobenius-orbit-free. Since |B0| =
( p
4 + O(1)
)d = (1 − Od(1/p))4−dpd, Lemma 2.2
produces a Sidon set in B0 of size at least 2−(d+6)/2√ |B0| = (1 − Od(1/p)) 2−38−d/2pd/2. Its
ratio to
√
2/d! pd/2 is
√
d!
8
√
2 8d/2 = Θ
(
d1/4(d/(8e))d/2) , which exceeds 1 for all d ≥ 25 (as 25! ≈
1.55 × 1025 > 128 · 825 ≈ 4.84 × 1024 and the ratio increases strictly for d ≥ 8).
6 Empirical Discovery Benchmarks and Formal Verification In-
ventory
To test the finite-N onset of our asymptotic phase transitions, we ran randomized greedy
and simulated-annealing benchmarks across [0, N ] (N = 2, . . . , 15, d = 2) and across
Sym2(Fq), Sym3(Fq). As shown in Figure 2, the three-tier hierarchy predicted by Theo-
rems 2.1, 3.1, and 4.1 already manifests cleanly by N = 15: diagonal sets reach |A| = 16,
symmetric matrices Sym2([0, 15]) reach |A| = 48 (3.00× larger), and general non-symmetric
matrices M2([0, 15]) reach |A| = 65 (4.06× larger than diagonal and 1.35× larger than sym-
metric). Furthermore, our end-to-end constructive Hessenberg + Erdős–Turán Box Sidon
algorithm produces a zero-collision Spectral Sidon Set of size 27 (378 distinct characteristic
polynomials) in M2([0, 80]).
Demarcation of Formalized vs. Analytical Results. Rather than inflating a formal-
ization with routine arithmetic, our Lean 4.36.0 library (SpectralSidonCore.lean, compiled
with -DwarningAsError=true, 0 sorry, 0 grind, 0 custom axioms) formally verifies the ex-
act algebraic, combinatorial, and finite-field core of the paper: exact d = 2, 3 Hessenberg
recovery and d = 3, 4 cycle expansions, the exact even-parity d = 2 symmetric injectivity
threshold (u ≤
√
N ) and matching integer symmetric collision at u = 2k ≈
√
N , exact d = 3
symmetric Jacobi recovery, characteristic-2 collapse, the exact d = 2 finite-field commuting
ceiling (strong and weak), the inductive factorial dominance d! > 2d22d for all d ≥ 8, and
kernel-checked proofs of all six finite-field witnesses (Sym2(F5, F7, F11, F13) and Sym3(F3, F5)).
The Wedderburn–Minkowski packing theorem (Theorem 2.1), general-d IVT root isolation and
residue peeling (Theorems 3.1 and 4.2(a)), Landau–Ramanujan / Ford analytic ceilings (The-
orem 4.1), spectral energy alteration (Theorem 4.2(c)), and normal-basis Frobenius averaging
16
```

---

## Page 17

```text
Figure 2: (a) Empirical onset of the three-tier spectral packing separation in [0, N ] for d =
2: diagonal commuting sets vs. symmetric Sym2([0, N ]) vs. non-symmetric M2([0, N ]). (b)
Machine-checked non-commutative witnesses in Sym2(Fq) (q = 5, 7, 11, 13) and Sym3(Fq) (q =
3, 5) strictly exceeding the maximum commuting ceilings of Theorem 5.1.
Table 2: Cryptographic SHA-256 inventory of archived artifacts in the AIRR repository (https:
//github.com/arr-research/arr-research.github.io).
Artifact Path SHA-256 Digest
src/lean/SpectralSidonCore.lean 8c274e52b9d806c79f14bb32ff253689f373f5460562f819397dc8962c47c526
src/python/verify_spectral_sidon.py 3b8623d427d68f6a49492f511bcb93d63b1d490835f792a9c7ee956aa588ea0a
data/witnesses_and_benchmarks.json c5bac26f7a2e407648708ed447b7dec8d5604a0fe6c790d60bd00fa9f2d74998
(Theorem 5.2) are proved analytically above and cross-checked numerically across d ∈ {2, 3, 4, 5}
in verify_spectral_sidon.py. Table 2 records exact SHA-256 digests for full reproducibility.
7 Open Problems and Future Directions
The theory of Spectral Sidon Sets opens several genuinely challenging questions at the interface
of additive combinatorics, number theory, and matrix analysis:
Conjecture 7.1 (Symmetric d = 2 Optimal Exponent). Does σsym 2 (N ) = Θ ( N 3/2/(log N )1/4)
(or at least N 3/2−o(1)), closing the gap between our Ω(N 5/4) Jacobi lower bound and the Landau–
Ramanujan upper bound? By Theorem 4.2(b)–(c), any improvement beyond N 5/4 must aban-
don globally injective rectangular sub-boxes (u ≤
√
N ) and uniform probabilistic alteration,
likely requiring an algebraic or Gaussian-prime construction directly avoiding norm-circle colli-
sions.
Conjecture 7.2 (Higher-Dimensional Symmetric Exponent). For d ≥ 3, sums of
(d
2
)
≥ 3
squares suffer no Landau–Ramanujan logarithmic deficit (by Legendre’s three-square and La-
grange’s four-square theorems). Does σsym d (N ) = Θd(N d(d+1)/4) hold for all d ≥ 3, matching
the non-symmetric optimum of Theorem 3.1, or does symmetry impose a strict exponent drop
even in higher dimensions?
Conjecture 7.3 (Asymptotic Finite-Field Non-Commutative Constant). Theorem 5.1 proves
σsym 2 (Fq) > q for q ∈ {5, 7, 11, 13}. Does there exist an explicit infinite family achieving
lim inf q→∞ σsym 2 (Fq)/q > 1, and does limq→∞ σ2(Fq)/q equal √ 2?
17
```

---

## Page 18

```text
Conjecture 7.4 (Continuous Hermitian / Quantum Hamiltonian Packing). Let Hd(1) be the
unit operator-norm ball of d × d Hermitian matrices. What is the maximum cardinality of a
set {H1, . . . , HM } ⊂ Hd(1) whose pairwise sums Hi + Hj are pairwise ε-separated in optimal-
transport (Wasserstein-∞) spectral distance as ε → 0? (Intuitively, this measures the maximum
number of bounded Hamiltonians whose pairwise superpositions are tomographically unambigu-
ous at spectral resolution ε.)
AI Assistance and Licensing Disclosure. Authored by Lluis Eriksson with AI assistance
from Google Antigravity for proof exploration, Lean 4 formalization, Python verification, and
manuscript drafting. The author owns and administers AIRR.SCIENCE; this record is evalu-
ated by two distinct isolated frontier models under AIRR-FOUNDER-1.0. Manuscript licensed
under CC-BY-4.0; code and data under MIT.
References
[1] László Babai and Vera T. Sós. Sidon sets in groups and induced subgraphs of Cayley
graphs. European Journal of Combinatorics, 6(2):101–114, 1985.
[2] Raj Chandra Bose and Sarvadaman Chowla. Theorems in the additive theory of numbers.
Commentarii Mathematici Helvetici, 37:141–147, 1962.
[3] Paul Erdős and Paul Turán. On a problem of Sidon in additive number theory, and on
some related problems. Journal of the London Mathematical Society, 16(4):212–215, 1941.
[4] Kevin Ford. The distribution of integers with a divisor in a given interval. Annals of
Mathematics, 168(2):367–433, 2008.
[5] Christopher D. Godsil. Matchings and walks in graphs. Journal of Graph Theory, 5(3):285–
297, 1981.
[6] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge University Press, 2nd
edition, 2013.
[7] Edmund Landau. Über die Einteilung der positiven ganzen Zahlen in vier Klassen nach
der Mindestzahl der zu ihrer additiven Zusammensetzung erforderlichen Quadrate. Archiv
der Mathematik und Physik, 13:305–312, 1908.
[8] Rudolf Lidl and Harald Niederreiter. Finite Fields. Cambridge University Press, 2nd
edition, 1997.
[9] Jürgen Neukirch. Algebraic Number Theory. Springer, 1999.
[10] Kevin O’Bryant. A complete annotated bibliography of work related to Sidon sequences.
Electronic Journal of Combinatorics, DS11:1–39, 2004.
[11] Imre Z. Ruzsa. Solving a linear equation in a set of integers I. Acta Arithmetica, 65(3):259–
282, 1993.
[12] Issai Schur. Zur Theorie der vertauschbaren Matrizen. Journal für die reine und angewandte
Mathematik, 130:66–76, 1905.
[13] James Singer. A theorem in finite projective geometry and some applications to number
theory. Transactions of the American Mathematical Society, 43(3):377–385, 1938.
[14] Terence Tao and Van H. Vu. Additive Combinatorics. Cambridge University Press, 2006.
18
```
