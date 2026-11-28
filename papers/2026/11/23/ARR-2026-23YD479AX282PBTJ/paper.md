# Sharp Non-Asymptotic Sphere-Packing Bounds for (1,1)-Criss-Cross Deletion Codes via Deleted-Slice Run-Tiering and Exact Indel-Pair Deduplication

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-23YD479AX282PBTJ | v1 | 2026-11-27
Sharp Non-Asymptotic Sphere-Packing Bounds for
(1, 1)-Criss-Cross Deletion Codes via Deleted-Slice
Run-Tiering and Exact Indel-Pair Deduplication
Lluis Eriksson
Independent Researcher (lluiseriksson@gmail.com)
Public Repository: https://github.com/arr-research/arr-research.github.io
November 27, 2026
Abstract
Li, Sun, and Ge (arXiv:2611.34447v1) proved that any q-ary (1, 1)-criss-cross deletion-
correcting code C ⊆ Σn×n q has redundancy rC ≥ 2n − 1 + 2 logq n − logq (1 + εLSG q,n ), es-
tablishing the strict finite-length threshold rC > 2n + 2 logq n − 2 only for n ≥ 27 in the
binary case q = 2 (and n ≥ 15, 11, 9, 7 for q = 3, 4, 5, 8). We prove four original combina-
torial theorems that strictly sharpen both the finite-length thresholds and the domain of
applicability: (1) an Exact Levenshtein Diagonal-and-Swap Deduplicated Indel-Pair Bound
Pindel(q, L) ≤ qL−1(L2(q −1)2 +2q −1) for all q ≥ 2, L ≥ 2, achieving exact equality at L = 2
and beating Li–Sun–Ge Lemma 6 by a factor approaching q2/(q − 1)2 (4× in binary); (2) a
Three-Tier Deleted-Slice Run-Decomposed Sphere-Packing Theorem that partitions code-
words into C1 ⊔ C2a ⊔ C2b according to |D1,1(X) ∩ Bm−1,n−1| ≥ s and proves via all three
cases of Li–Sun–Ge’s bad-subarray characterization that every X ∈ C2b has a deleted-column
slice X (−j) with ρrow(X (−j)) ≤ s + 1 or a deleted-row slice X (−i) with ρcol(X (−i)) ≤ s + 1,
slashing ε2,n by 53.3× at n = 18 and 90.2× at n = 27 and lowering the strict redundancy
threshold from n ≥ 27 → n ≥ 18 (q = 2), 15 → 11 (q = 3), 11 → 9 (q = 4), and 9 → 8
(q = 5); (3) a Rectangular m × n Sphere-Packing Converse and Exact Parity-Completion
Bijection Theorem extending both the three-tier converse and exact (m + n − 1)-symbol
parity completion to arbitrary rectangular arrays m, n ≥ 3; and (4) an Exact Small-Array
Optimal Binary Capacity Theorem proving |C ∗(2, 2, 2)| = |C ∗(2, 2, 3)| = 2 via exhaustive
conflict-graph maximum independent set certification. All 20 core structural theorems are
constructively formalized in Lean 4.36.0 (0 sorry, 0 grind, 0 Classical.choice), paired
with a zero-float exact-Q verifier, 16 canonical SHA-256 certificates, and 66 passing tests
(including explicit adversarial stress tests on Toeplitz and run-collapse arrays).
1 Introduction
Two-dimensional (1, 1)-criss-cross deletion channels—motivated by DNA-based storage and race-
track memories—delete one arbitrary row and one arbitrary column from an m × n q-ary array
X ∈ Σm×n q , producing a subarray in Σ(m−1)×(n−1) q [1, 4, 3]. Denote by ∆r,c(X) the (m−1)×(n−1)
array obtained by deleting row r and column c, and by D1,1(X) := {∆r,c(X) : r ∈ [1 : m], c ∈
[1 : n]} its (1, 1)-criss-cross deletion ball. A code C ⊆ Σm×n q corrects a (1, 1)-criss-cross dele-
tion if and only if the balls {D1,1(X) : X ∈ C} are pairwise disjoint. Its redundancy is
rC := mn − logq |C|.
Li, Sun, and Ge [3] derived the leading asymptotic converse rC ≥ 2n − 1 + 2 logq n − oq(1) for
square n×n arrays by splitting C into two tiers: “good” codewords C1 with |D1,1(X)| = n2, and
“bad” codewords C2 with |D1,1(X)| < n2, each of which places at least ONE bad subarray into
Bn−1 (bounded conservatively via |C2| ≤ |Bn−1| using a loose single-indel pair bound qL+1L2
1
```

---

## Page 2

```text
in their Lemma 6). Their non-asymptotic overhead term
εLSG q,n := 2(n − 2)(n − 1)3(n + 1) qn−2 (1)
crosses below 1—needed to obtain the strict finite-length redundancy bound rC > 2n+2 logq n−2
(from rC ≥ 2n − 1 + 2 logq n − logq(1 + ε) with logq(1 + ε) < 1)—only at n ≥ 27 for q = 2,
leaving a wide binary gap n ∈ [18, 26] unresolved and restricting analysis to square arrays.
We eliminate BOTH sources of looseness rigorously: (i) we replace the loose qL+1L2 single-
indel pair count with an exact diagonal-and-swap deduplicated Levenshtein bound (Theorem 1),
and (ii) we refine C2 = C2a ⊔ C2b by counting bad subarrays per codeword (|D1,1(X) ∩
Bm−1,n−1| ≥ s) and proving an exact, counterexample-proof inclusion of C2b into the deleted-
slice low-run family Lexact q,m,n(sr, sc) (Theorem 2).
2 Main Original Theorems
2.1 Theorem 1: Exact Levenshtein Diagonal-and-Swap Deduplicated Indel-
Pair Bound
For alphabet size q ≥ 2 and length L ≥ 2, let Pindel(q, L) := |{(u, v) ∈ ΣL q ×ΣL q : D1(u)∩D1(v) ̸=
∅}| be the number of ordered pairs of length-L q-ary words sharing at least one common length-
(L − 1) subsequence.
Theorem 1 (Exact Deduplicated Single-Indel Confusable Pair Bound). For every q ≥ 2 and
every L ≥ 2,
Pindel(q, L) ≤ qL−1( L2(q − 1)2 + 2q − 1 ) < qL+1L2. (2)
Exact equality Pindel(q, 2) = q(4q2 − 6q + 3) holds for every q ≥ 2. As L → ∞, (2) strictly beats
Li–Sun–Ge Lemma 6 (qL+1L2) by the asymptotic factor q2/(q − 1)2 (4× in binary, > 3× for
all L ≥ 4).
Proof. Every ordered confusable pair (u, v) shares a common subsequence w ∈ ΣL−1 q , so (u, v) ∈
I1(w) × I1(w), where I1(w) is Levenshtein’s single-insertion ball of exact uniform cardinality
|I1(w)| = L(q−1)+1 for every w ∈ ΣL−1 q [2]. Summing |I1(w)|2 over all qL−1 words w overcounts
two universal collision families:
1. Diagonal pairs (u, u): Each word u ∈ ΣL q is counted ρ(u) = |D1(u)| times across w ∈
D1(u) rather than once, giving exact excess ∑ u∈ΣLq (ρ(u) − 1) = qL−1(L − 1)(q − 1) since
E[ρ(u)] = 1 + (L − 1)(q − 1)/q.
2. Adjacent-transposition pairs (u, v): For each w ∈ ΣL−1 q , each index i ∈ [1 : L − 1], and
each a ∈ Σq \ {wi}, inserting a immediately before wi gives u and immediately after wi
gives v ̸= u; the ordered pair (u, v) ALSO shares the distinct common subsequence w′
obtained by replacing wi with a. Summing over all w, i, a yields at least qL−1(L − 1)(q − 1)
duplicate off-diagonal ordered pairs.
Subtracting both exact overcounts yields the constructive algebraic identity (mechanized in
Lean 4.36.0 T05–T08):
qL−1
(
(L(q − 1) + 1)2 − 2(L − 1)(q − 1) ) = qL−1( L2(q − 1)2 + 2q − 1 ) .
At L = 2, no two distinct words share more than two length-1 subsequences, giving exact
equality Pindel(q, 2) = q(4q2 − 6q + 3) (certified for q = 2, 3, 4 in C01–C04).
2
```

---

## Page 3

```text
2.2 Theorem 2: Three-Tier Deleted-Slice Run-Decomposed Sphere-Packing
Bound
Following Li, Sun, and Ge [3, Definition 2] generalized directly to rectangular arrays:
Definition 1 (Bad Subarray Space Bm−1,n−1). An (m − 1) × (n − 1) array Y ∈ Σ(m−1)×(n−1) q is
bad (Y ∈ Bm−1,n−1) if two adjacent rows of Y have intersecting single-deletion balls (D1(Yi) ∩
D1(Yi+1) ̸= ∅), OR two adjacent columns of Y have intersecting single-deletion balls (D1(Y j ) ∩
D1(Y j+1) ̸= ∅).
Note that equal adjacent rows (or columns) automatically satisfy D1(Yi) ∩ D1(Yi+1) =
D1(Yi) ̸= ∅, so they are already included in Bm−1,n−1. Applying Theorem 1 to each of the
m − 2 adjacent row pairs of length n − 1 and n − 2 adjacent column pairs of length m − 1 yields
immediately:
|Bm−1,n−1|
q(m−1)(n−1) ≤ (m − 2) (n − 1)2(q − 1)2 + 2q − 1 qn + (n − 2) (m − 1)2(q − 1)2 + 2q − 1 qm . (3)
For any matrix X ∈ Σm×n q , let X (−j) ∈ Σm×(n−1) q denote X with column j deleted, and
X (−i) ∈ Σ(m−1)×n q denote X with row i deleted. Write ρrow(M ) for the number of maximal
constant runs in the sequence of rows of M , and ρcol(M ) for the number of maximal constant
runs in the sequence of columns of M .
Lemma 1 (Deleted-Slice Bad-Ball Lower Bound). Let X ∈ Σm×n q (m, n ≥ 3) satisfy
|D1,1(X)| < mn. Then at least one of the following holds:
1. There exists a column j ∈ [1 : n] such that |D1,1(X) ∩ Bm−1,n−1| ≥ ρrow(X (−j)) − 2, or
2. There exists a row i ∈ [1 : m] such that |D1,1(X) ∩ Bm−1,n−1| ≥ ρcol(X (−i)) − 2.
Proof. Since |D1,1(X)| < mn, there exist distinct deletion patterns (i1, j1) ̸= (i2, j2) with
∆i1,j1 (X) = ∆i2,j2 (X). We check all three exhaustive cases (refining [3, Lemma 5]):
• Case 1 (i1 = i2 = i, j1 < j2): Deleting column j1 or column j2 from the (m − 1) × n
matrix X (−i) yields the same sequence of columns, so columns j1, j1 +1, . . . , j2 of X (−i) are
identical. Hence for every k ∈ [1 : n]\{j1, j1+1}, ∆i,k(X) retains the two identical adjacent
columns j1 and j1 + 1, so ∆i,k(X) ∈ Bm−1,n−1. The full set {∆i,k(X) : k ∈ [1 : n]} is the
single-deletion ball of the column sequence of X (−i), whose exact cardinality is ρcol(X (−i))
(since deleting two adjacent identical columns yields identical outputs, Lean T04). Because
j1 and j1 +1 belong to the same column run, excluding {j1, j1 +1} omits at most 1 distinct
array, giving |D1,1(X) ∩ Bm−1,n−1| ≥ ρcol(X (−i)) − 1 ≥ ρcol(X (−i)) − 2.
• Case 2 (j1 = j2 = j, i1 < i2): By transposition, |D1,1(X)∩Bm−1,n−1| ≥ ρrow(X (−j))−1 ≥
ρrow(X (−j)) − 2.
• Case 3 (i1 ̸= i2 and j1 ̸= j2; WLOG i1 < i2): Comparing row i1 of ∆i1,j1 (X) = ∆i2,j2 (X)
yields ∆j1 (Xi1+1) = ∆j2 (Xi1 ). Thus in the m × (n − 1) slice X (−j1), rows i1 and i1 + 1
are ∆j1 (Xi1 ) and ∆j1 (Xi1+1) = ∆j2 (Xi1 ), which BOTH share the common length-(n − 2)
subsequence obtained by deleting coordinates j1 and j2 from Xi1 ! Consequently, for
EVERY k ∈ [1 : m] \ {i1, i1 + 1}, deleting row k from X (−j1) keeps rows i1 and i1 + 1
adjacent, so ∆k,j1 (X) ∈ Bm−1,n−1. The full set {∆k,j1 (X) : k ∈ [1 : m]} has exact
cardinality ρrow(X (−j1)), and excluding two indices {i1, i1 + 1} omits at most 2 maximal
row runs (Lean T15), giving |D1,1(X) ∩ Bm−1,n−1| ≥ ρrow(X (−j1)) − 2.
3
```

---

## Page 4

```text
Notice why Lemma 1 is immune to column-projection run-collapse: the run count is evalu-
ated directly on the deleted slice X (−j) or X (−i) (NOT on the full array X). For any threshold
s ∈ {1, . . . , min(m, n) − 2}, define the exact deleted-slice low-run family
Lexact q,m,n(s) := { X ∈ Σm×n q : ( ∃j ∈ [1 : n], ρrow(X (−j)) ≤ s + 1 )
∨
(
∃i ∈ [1 : m], ρcol(X (−i)) ≤ s + 1 )} .
Counting the deleted column j (n positions, qm column vectors) plus the remaining m × (n − 1)
slice with ≤ s + 1 row runs (and symmetrically for deleted rows) gives the exact upper bound
|Lexact q,m,n(s)| ≤ nqm
min(m,s+1)∑
r=1
(m − 1
r − 1
)
qn−1(qn−1 − 1)r−1
+ mqn
min(n,s+1)∑
r=1
(n − 1
r − 1
)
qm−1(qm−1 − 1)r−1. (4)
Theorem 2 (Three-Tier Deleted-Slice Sphere-Packing Bound). For every q ≥ 2, m, n ≥ 3, and
tier threshold s ∈ {1, . . . , min(m, n) − 2}, every q-ary (1, 1)-criss-cross deletion-correcting code
C ⊆ Σm×n q satisfies
|C| ≤ q(m−1)(n−1)
mn
(
1 + εsharp q,m,n(s) ) , (5)
where, denoting Q := q(m−1)(n−1) and using (3) and (4),
εsharp q,m,n(s) := mn − s s |Bm−1,n−1| Q + (mn − 1) |Lexact q,m,n(s)| Q . (6)
In the square case m = n, optimizing s ∈ {1, . . . , n − 2} yields εsharp q,n < 1 and hence rC >
2n + 2 logq n − 2 strictly from:
n ≥ 18 (q = 2), n ≥ 11 (q = 3), n ≥ 9 (q = 4), n ≥ 8 (q = 5), n ≥ 7 (q = 8),
slashing Li–Sun–Ge’s thresholds (27, 15, 11, 9) to (18, 11, 9, 8) and tightening ε2,n by 53.3× at
n = 18 and 90.2× at n = 27 (and tightening ε8,7 by 2.6× at q = 8, n = 7).
Proof. Partition C = C1 ⊔ C2a ⊔ C2b where C1 = {X ∈ C : |D1,1(X)| = mn}, C2a = {X ∈
C \ C1 : |D1,1(X) ∩ Bm−1,n−1| ≥ s}, and C2b = {X ∈ C \ C1 : |D1,1(X) ∩ Bm−1,n−1| ≤ s − 1}.
Pairwise ball disjointness yields mn|C1| + s|C2a| + |C2b| ≤ Q and s|C2a| ≤ |Bm−1,n−1|. By
Lemma 1, every X ∈ C2b belongs to Lexact q,m,n(s), so |C2b| ≤ |Lexact q,m,n(s)|. Applying the constructive
integer packing identity
mn · s · (|C1| + |C2a| + |C2b|) ≤ sQ + (mn − s)|Bm−1,n−1| + (mn − 1)s|Lexact q,m,n(s)|
(proved in Lean 4.36.0 T09–T10) and dividing by mns yields (5)–(6). Whenever εsharp q,m,n(s) < 1,
we have 1 + ε < 2 ≤ q (Lean T14), whence logq(1 + ε) < 1 and rC > m + n − 2 + logq(mn)
(giving rC > 2n + 2 logq n − 2 for m = n).
2.3 Theorem 3: Rectangular m × n Converse and Exact Parity-Completion
Bijection
Theorem 3 (Rectangular (1, 1)-Criss-Cross Converse and Parity Bijection). For every q ≥ 2
and arbitrary rectangular dimensions m, n ≥ 3:
4
```

---

## Page 5

```text
Figure 1: Left: Binary (q = 2) sphere-packing overhead εLSG 2,n vs. our Theorem 2 εsharp 2,n , slashing
the ε < 1 crossing from n = 27 down to n = 18 (53.3× reduction at n = 18, 90.2× at n = 27).
Right: Strict non-asymptotic threshold reduction nLSG 0 (q) → nsharp 0 (q) across q ∈ {2, 3, 4, 5, 8}
(C05–C12).
1. Whenever εsharp q,m,n(s) < 1 in (6) (certified e.g. for (q, m, n) = (2, 18, 22) with s = 14, ε ≈
0.6596 in C13 and (3, 11, 15) with s = 6, ε ≈ 0.7798 in C14), every (1, 1)-criss-cross deletion
code C ⊆ Σm×n q satisfies rC > m + n + logq(mn) − 2.
2. Defining Pq,m,n := {X ∈ Σm×n q : ∑ j Xi,j ≡ 0 (mod q) ∀i, ∑ i Xi,j ≡ 0 (mod q) ∀j}, for
every fixed deleted row-column pair (r, c), ∆r,c : Pq,m,n → Σ(m−1)×(n−1) q is a bijection of
exact redundancy m + n − 1 symbols (Lean T11–T13, exhaustively verified on 3 × 4 binary
arrays in C15).
2.4 Theorem 4: Exact Small-Array Optimal Binary Capacities
Theorem 4 (Exact Small-Array Optimal Capacities). For binary (1, 1)-criss-cross deletion
codes on small arrays, exact maximum independent set computation on the (1, 1)-deletion conflict
graph establishes:
|C∗(2, 2, 2)| = 2 (saturating |D1,1| ∈ {1, 2}, target space 21 = 2),
|C∗(2, 2, 3)| = 2 (strictly below target space 22 = 4),
proving that on 2 × 3 arrays, non-uniform ball overlap already caps optimal binary code size at
half the naive target-space volume (C16, Figure 3).
3 Exact-Q Verification, Lean 4.36.0 Formalization, and Verifica-
tion Boundary
Verification Boundary.
1. Formally Proved in Lean 4.36.0 (lean/CrissCrossDeletionCert.lean, 20 theorems
T01–T20, compiled with -DwarningAsError=true and lake build, 0 sorry, 0 grind, 0
Classical.choice): Constructive List Nat induction proving run-monotonicity under
single deletions (T01), exact length and adjacent-duplicate lemmas (T02–T04), the Leven-
shtein deduplication identity and universal strict improvement over Li–Sun–Ge Lemma 6
for all q, L ≥ 2 (T05–T08), the three-tier master packing inequality (T09–T10), rectangular
5
```

---

## Page 6

```text
Figure 2: Left: Theorem 1 exact Levenshtein diagonal+swap deduplicated bound vs. brute-force
Pindel(2, L) and Li–Sun–Ge Lemma 6 (2L+1L2), demonstrating exact equality at L = 2 and ≈ 4×
tightening for L ≥ 4 (C01–C04). Right: Linear growth of the tightening ratio εLSG q,n /εsharp q,n with
n, reaching 90.2× (q = 2) at n = 27.
Figure 3: Left: Theorem 3 rectangular binary validity landscape log10 εsharp 2,m,n across (m, n) ∈
[14, 23]2 (green region certifies εsharp 2,m,n < 1, where Li–Sun–Ge Theorem 1 does not apply). Right:
Theorem 4 exact conflict-graph MIS binary capacities for 2 × 2 and 2 × 3 arrays (C16).
parity redundancy and (tr, tc) symbol-loss identities (T11–T13), the ε < 1 crossing crite-
rion (T14), the exact two-index run-exclusion step r − 2 ≤ s − 1 ⇒ r ≤ s + 1 (T15), and
zero-axiom finite threshold certifications (T16–T20).
2. Verified by Zero-Float Exact-Q Computation (src/crisscross_deletion_verifier.py,
66 passing pytest tests with AST zero-float purity audit): Exact rational evaluation
of (6) and (1), brute-force Pindel(q, L) checks, explicit adversarial verification of Lemma 1
on both Toeplitz (3 × 3, q = 5) and column-projection run-collapse (6 × 6, q = 9) arrays,
exhaustive 3 × 4 parity bijection, and exact conflict-graph MIS for 2 × 2 and 2 × 3.
3. Outside Scope: Multi-deletion (tr, tc) codes with tr + tc > 2 (beyond the exact symbol-loss
identity T12), explicit code constructions matching the converse at n ∈ [18, 26], and exact
MIS capacities for arrays of size ≥ 3 × 3.
6
```

---

## Page 7

```text
Cert ID Scope / Parameters Li–Sun–Ge [3] Our Certified Result (Eq. 6)
C01–C04 Pindel(q, L), (2, 2), (2, 4), (2, 5), (3, 3) 32, 512, 1600, 729 Exact 14, 142, 414, 363 ≤ Thm. 1 (14, 152, 448, 369)
C05–C08 Binary q = 2, n ∈ {18, 20, 23, 26} εLSG > 1 (fails) εsharp = 0.856, 0.321, 0.069, 0.014 < 1 (53.3×–86.1×)
C09 Binary q = 2, n = 27 (s = 22) εLSG = 0.733 εsharp = 0.00813 (90.2× sharper)
C10–C12 q = 3 (11), q = 4 (9), q = 5 (8) εLSG > 1 (fails) εsharp = 0.789, 0.599, 0.495 < 1 (4.8×–13.9×)
C13–C14 Rectangular (2, 18, 22), (3, 11, 15) Not covered εsharp < 1 certified exactly
C15 Parity bijection (2, 3, 4) Square only Exact 64 ↔ 64 bijection, r = m + n − 1 = 6
C16 Small binary 2 × 2, 2 × 3 Asymptotic only Exact MIS |C∗(2, 2, 2)| = 2, |C∗(2, 2, 3)| = 2
Table 1: Summary of the 16 canonical exact-Q certificates (CRISSCROSS-DELETION-CERT-1.0),
matching Eq. (6) identically.
Artifact Provenance and Cryptographic Digests. All artifacts are archived in the public
AIRR repository https://github.com/arr-research/arr-research.github.io under MIT
(code/data) and CC-BY-4.0 (manuscript) licenses:
• lean/CrissCrossDeletionCert.lean
SHA-256: 3f3bd33204842f188f37a32de4b0ca84d76838694f39a8fcbb31c0c566889f23
• src/crisscross_deletion_verifier.py
SHA-256: 69d97061014e15050cff3d8829977eec6181679689db624b3d1e2c9fe62575e0
• certificates/MANIFEST.json
SHA-256: aa390fe3eda89d7f78237b2321520dddcfd4d9d78a344e7b490d42ef19f553cc
AI Disclosure and Conflict Statement. This work was produced by Lluis Eriksson with
computational, formalization, and manuscript assistance from Google Antigravity autonomous
research agents. As founder/operator of AIRR.SCIENCE, the author discloses an operator
conflict (operator_conflict: true); all screening was performed by isolated PDF-only eval-
uators.
References
[1] Rawad Bitar, Lorenz Welter, Ilia Smagloy, Antonia Wachter-Zeh, and Eitan Yaakobi. Criss-
cross insertion and deletion correcting codes. IEEE Transactions on Information Theory,
67(12):7999–8015, 2021.
[2] Vladimir I. Levenshtein. Binary codes capable of correcting deletions, insertions, and rever-
sals. Soviet Physics Doklady, 10(8):707–710, 1966.
[3] Zhiqiang Li, Yubo Sun, and Gennian Ge. Optimal (1, 1)-criss-cross deletion-correcting codes
with linear-time encoder and decoder, November 2026. arXiv:2611.34447v1.
[4] Yubo Sun and Gennian Ge. Criss-cross deletion correcting codes: Optimal constructions
with eﬀicient decoders. IEEE Transactions on Information Theory, 72(7):4648–4660, 2026.
7
```
