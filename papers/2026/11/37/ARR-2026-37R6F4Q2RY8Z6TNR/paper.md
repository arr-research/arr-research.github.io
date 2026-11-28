# Universal Tree Collapse, Complete 13-Element Green's Eggbox Structure, and Exact Cycle-Escape Laws for 1-Joined Graph Adjacency Determinants

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-37R6F4Q2RY8Z6TNR | v1 | 2026-11-27
Universal Tree Collapse, Complete 13-Element
Green’s Eggbox Structure, and Exact Cycle-Escape
Laws for 1-Joined Graph Adjacency Determinants
Lluis Eriksson
Independent Researcher, AIRR.SCIENCE
lluiseriksson@gmail.com
November 27, 2026
Abstract
Pinzon, Pragel, Roberts, Marshall, and Strain (arXiv:2611.34794v1) showed that the
adjacency determinants of 1-joined labeled path graphs are governed by a finite 2 × 2 integer
transfer-matrix monoid M13 under π(G) = ϕ(G)E1, leaving open in Section 6 the extension
from paths to general trees. We resolve that open question completely and establish four
machine-checked structural theorems backed by 20 constructive Lean 4.36.0 proofs (0 sorry,
0 Classical.choice), 16 SHA-256 certificates (C01--C16), and 61 adversarial exact-integer
pytest checks. First, we formalize the complete 13-element monoid closure (169/169 prod-
ucts), its exact 4 idempotents {I2,E11,E22, 0}, its universal invariants det(π(G)) ∈ {0, +1}
and | det(A(G))| ≤ 1, its 3 J -cells and 6 H-cells (Z4, two Z2 groups, two nilpotent cells,
and Z1), and the exact 11/13 single-path deficit missing precisely {±E22}. Second, we prove
the Universal Tree Collapse and Surjectivity Theorem: because every finite forest admits
at most one perfect matching whose sign depends solely on |V | mod 4, every finite labeled
tree T (|V (T )| ≥ 2) maps directly into M13 (independently verified exhaustively across all
1,441 labeled trees on 2 ≤ n ≤ 6 vertices via Prüfer codes in C09); moreover, unlike sin-
gle paths, single labeled trees surject onto all 13 elements via explicit minimal witnesses
T6 ↦→ −E22 (C10) and T8 ↦→ +E22 (C11). Third, we establish the sharp boundary of finiteness
via the Exact Cycle-Escape Theorem: adjoining even a single cycle breaks M13 into an infinite
monoid, with closed-form Bareiss- and Lean-verified chain determinants det(A(≍k 1 C3)) = k+1
(unipotent Jordan growth, C12), det(A(≍k 1 C6)) = (−4)k (exponential growth, C13), and
det(A(≍k 1 K4)) = (−1)k(2k + 1) (C14). Fourth, we certify Pinzon et al.’s Section 5 chain
examples by direct fraction-free Bareiss elimination (C06--C08), flagging a minor path-count
slip in Example 5.1 (2 × 2025 = 4050, not 5050).
1 Introduction and Transfer-Matrix Framework
For a finite labeled graph G on vertex set V (G) = {1,...,n} (n ≥ 2) with adjacency matrix
A(G), denote |G| := det(A(G)) ∈ Z. The 1-join G ≍1 H connects the exit vertex n of G by a
single edge to the entry vertex 1 of H (shifting labels of H by |V (G)|). Following [5, 6], define
ϕ(G) :=
( |G| |G \ {n}|
|G \ {1}| |G \ {1,n}|
)
∈ M2(Z), E1 :=
(1 0
0 −1
)
, π(G) := ψ(ϕ(G)) := ϕ(G)E1.
(1)
By Hickey’s sandwich-semigroup isomorphism [3] and the 1-join determinant identity |G ≍1 H| =
|G||H| − |G \ {n}||H \ {1}| [5], ϕ(G ≍1 H) = ϕ(G)E1ϕ(H), and hence π(G ≍1 H) = π(G)π(H) is
an ordinary matrix-multiplication homomorphism whose (1, 1) entry recovers |G ≍1 H| identically
(Lean T01--T05).
Pinzon, Pragel, Roberts, Marshall, and Strain [6] showed that all relabeled paths Pn|σ map to
11 distinct matrices generating a 13-element finite monoid M13, characterized its cells via [4], and
1
```

---

## Page 2

```text
Figure 1: Left: Complete Green’s J /H-cell eggbox decomposition of M13 (C02--C03), high-
lighting the unique single-path-missing cell {±E22} (green). Right: Distinct transfer matrices
reached by single paths (11/13, C01), depth-2 path joins (13/13, C04--C05), single labeled trees
(13/13, C10--C11), and all 1,441 labeled trees on 2 ≤ n ≤ 6 vertices (C09).
posed in Section 6 the extension from paths to general trees. We resolve this problem completely
and establish the exact spectral dichotomy separating finite tree closure from unbounded cyclic
escape.
2 Complete 13-Element Monoid Structure and Green’s Eggbox
Theorem 2.1 (Closure, Idempotents, Universal Invariants, and Path Deficit; Lean T06--T12,
T20). Let M13 := {±I2, ±J, ±E11, ±E22, ±E12, ±E21, 0} ⊂ M2({−1, 0, 1}), where J =
( 0 −1
1 0
)
and Eij are standard matrix units. Then:
1. M13 has exact cardinality 13 and is multiplicatively closed across all 169 ordered pairs, with
Cayley-table rank distribution 16 rank-2, 96 rank-1, and 57 rank-0 products.
2. M13 contains precisely 4 idempotents {I2,E11,E22, 0}, partitioning into 3 Green’s J -classes
(sizes 4, 8, 1), 4 L-classes, 4 R-classes, and 6 H-classes: the rank-2 unit group {±I2, ±J} ∼=
Z4, a 2 × 2 rank-1 eggbox consisting of two group H-cells {±E11} ∼= Z2 and {±E22} ∼= Z2
plus two nilpotent cells {±E12} and {±E21} (X 2 = 0), and the rank-0 sink {0} ∼= Z1.
3. Every X ∈ M13 satisfies det(X) ∈ {0, +1} (never −1) and X11 ∈ {−1, 0, +1}.
4. The single-path image P11 = π(P) has cardinality 11 and misses precisely {±E22}, both of
which are attained at join-depth 2: E21(−E12) = −E22 (C04) and E21E12 = +E22 (C05).
3 Universal Tree Collapse and Single-Tree Surjectivity
We now completely answer Section 6 of [6] for arbitrary trees and forests.
Theorem 3.1 (Universal Tree Collapse and Surjectivity; Lean T13, Certs C09--C11). For every
finite labeled forest (in particular every finite labeled tree) T on n ≥ 2 vertices with arbitrary
distinct entry and exit vertices:
1. Universal Collapse: π(T ) ∈ M13. Consequently, for any finite 1-joined chain G = T1 ≍1
· · · ≍1 Tm of arbitrary labeled trees, π(G) ∈ M13 and |G| = det(A(G)) ∈ {−1, 0, +1}.
2
```

---

## Page 3

```text
2. Single-Tree Surjectivity: Unlike single paths (which reach only 11 of 13 elements), single
labeled trees surject onto all 13 elements of M13. Specifically, the 6-vertex tree T6 obtained
by attaching entry 0 and exit 5 as pendant leaves to vertex 1 of P4 = (1–2–3–4) satisfies
π(T6) = −E22 (C10), and the 8-vertex tree T8 attaching entry 0 and exit 7 to vertex 1 of
P6 = (1–2–3–4–5–6) satisfies π(T8) = +E22 (C11).
Proof. By Harary’s determinant expansion [2], every elementary spanning subgraph of a forest
F is cycle-free and therefore a perfect matching of F . Because a forest has at most one perfect
matching (a symmetric difference of two distinct perfect matchings would contain an alternating
even cycle), every forest F on m vertices satisfies |F | = 0 if m is odd, and |F | ∈ {0, (−1)m/2} if
m is even (each K2 factor contributes −1). Now let T be a labeled forest on n ≥ 2 vertices; the
induced subgraphs T , T \ {n}, T \ {1}, and T \ {1,n} are all forests of orders n, n − 1, n − 1, and
n − 2, respectively:
• If n is even, n−1 is odd so |T \{1}| = |T \{n}| = 0, while |T | ∈ {0,s} and |T \{1,n}| ∈ {0, −s}
where s = +1 for n ≡ 0 (mod 4) and s = −1 for n ≡ 2 (mod 4).
• If n is odd, n and n − 2 are odd so |T | = |T \ {1,n}| = 0, while |T \ {1}|, |T \ {n}| ∈ {0,s}
where s = +1 for n ≡ 1 (mod 4) and s = −1 for n ≡ 3 (mod 4).
In all 4 × 4 = 16 parity-matching configurations, Lean Theorem T13 verifies constructively that
ψ(ϕ(T )) = ϕ(T )E1 ∈ M13. By closure of M13 (T07), arbitrary 1-joined chains of trees remain
inside M13. For surjectivity, T6 has two leaves sharing neighbor 1 so it admits no perfect matching
(|T6| = 0), while deleting both leaves yields P4 (|P4| = +1), giving ϕ(T6) = diag(0, 1) and
π(T6) = diag(0, −1) = −E22; identically, deleting the two leaves of T8 yields P6 (|P6| = −1),
giving ϕ(T8) = diag(0, −1) and π(T8) = +E22. Certificate C09 independently audits all 1 + 3 +
16 + 125 + 1296 = 1,441 labeled trees on 2 ≤ n ≤ 6 vertices via Prüfer decoding and exact Bareiss
elimination [1], confirming 100% collapse into M13.
4 Exact Cycle-Escape Laws and Chain Audits
Theorem 3.1 raises a sharp converse question: what is the minimal structural perturbation that
escapes M13? Adding a single cycle immediately breaks finite closure and triggers unbounded
linear or exponential determinant growth.
Theorem 4.1 (Exact Cycle- and Clique-Escape Laws; Lean T17--T19, Certs C12--C14). For
every integer k ≥ 1:
1. Triangle C3 (Linear Unipotent Jordan Escape): With entry 0 and exit 2, π(C3) =( 2 1
−1 0
)
has trace 2, det = +1, and exact powers π(≍k 1 C3) = ( k+1 k −k 1−k ) , yielding det(A(≍k 1
C3)) = k + 1.
2. Adjacent 6-Cycle C6 (Exponential Escape): With adjacent entry 0 and exit 1, π(C6) =
diag(−4, −1), yielding π(≍k 1 C6) = diag((−4)k, (−1)k) and det(A(≍k 1 C6)) = (−4)k.
3. Clique K4 (Alternating Linear Escape): With entry 0 and exit 3, π(K4) =
( −3 −2
2 1
)
,
yielding π(≍k 1 K4) = (−1)k ( 2k+1 2k −2k 1−2k ) and det(A(≍k 1 K4)) = (−1)k(2k + 1).
Remark 4.2 (Chain Audits and Pinzon et al. Example 5.1 Erratum; Lean T14--T16, Certs
C06--C08, C15). We independently audited the chain applications of [6, Section 5] via both Lean 4
matrix powers and direct Bareiss elimination on explicitly constructed 1-joined graphs: (i) P5|(1)
generates Z4 with exact 4-periodic determinants 0, −1, 0, +1 (T14, C06); (ii) Example 5.2’s alter-
nating block G = P4|(12)(34) ≍1 P6|(12)(56) satisfies π(G) = −E11 and | ≍k 1 G| = (−1)k (T15,
C07); (iii) Example 5.1’s block G = P3|(23) ≍1 P5|(125) satisfies π(G) = (−E21)(E21) = 0 and
determinant 0 for all k ≥ 1 (T16, C08), while noting a minor typographical slip in [6, Example
3
```

---

## Page 4

```text
Figure 2: Left: Sharp spectral dichotomy between the universal tree collapse barrier | det | ≤ 1
(T13) and unbounded escape under C3 (k + 1, C12), K4 (2k + 1, C14), and C6 (4k, C13). Right:
Signed chain determinant trajectories contrasting 4-periodic Z4 (C06) and 2-periodic Z2 (C07)
monoid orbits against linear C3 escape.
Figure 3: Left: Exhaustive Prüfer-code audit (C09) verifying 100% collapse into M13 across
all 1 + 3 + 16 + 125 + 1296 = 1,441 labeled trees on 2 ≤ n ≤ 6 vertices. Right: Exact rank
distribution of the 13 × 13 = 169 Cayley-table products of M13 (16 rank-2, 96 rank-1, 57 rank-0).
5.1]: joining k = 2025 copies of a 2-path block contains 2 × 2025 = 4050 path graphs, not 5050;
(iv) the degenerate 2-vertex path satisfies ϕ(P2) = diag(−1, 1) and π(P2) = −I2 ∈ M13, matching
direct Bareiss determinants on three-graph sandwiches P4 ≍1 P2 ≍1 P4 (T20, C15).
5 Certificate Suite, Verification Boundary, and Reproducibility
Table 1 summarizes the 16 SHA-256 certificates generated by the AST-audited zero-float exact-
integer verifier src/path_join_monoid_verifier.py and validated by 61 adversarial pytest
checks alongside 20 constructive Lean 4.36.0 theorems.
Explicit Verification Boundary. Our machine-checked claims are partitioned into three dis-
joint verification layers:
1. Universally proved in Lean 4.36.0 (T01--T20, 0 sorry, 0 Classical.choice,
warnings-as-errors): 2 × 2 matrix associativity, identity, determinant multiplicativ-
4
```

---

## Page 5

```text
Table 1: Summary of the 16 canonical SHA-256 certificates (PATH-JOIN-MONOID-CERT-1.0).
IDs Mode Object / Scope Exact Certified Result
C01--C03 Monoid Paths n ≤ 8, M13, Green’s cells 11/13 paths; |M13| = 13; 4 idemp.; J = 3, H = 6
C04--C05 Depth-2 Join Bareiss π(G ≍1 H) = π(G)π(H) Realizes missing −E22 (10v) and +E22 (8v)
C06--C08 Chain Audits P5|(1), Ex. 5.2, Ex. 5.1 Z4 periodic; (−1)k ; 0 (erratum 4050 ̸= 5050)
C09 Tree Collapse All 1,441 labeled trees 2 ≤ n ≤ 6 100% Bareiss π(T ) ∈ M13 via Prüfer codes
C10--C11 Surjectivity Minimal trees T6 (6v), T8 (8v) Direct Bareiss π(T6) = −E22, π(T8) = +E22
C12--C14 Cycle Escape C3, C6 (adj.), K4 chains Bareiss + power: k + 1, (−4)k , (−1)k (2k + 1)
C15--C16 Boundary P2 sandwich; spectral dichotomy π(P2) = −I2; | det | ≤ 1 vs. k + 1 vs. 4k
ity, Hickey sandwich isomorphism ψ(x ◦ y) = ψ(x)ψ(y) preserving entry (1, 1), exact size 13
and 169-product closure of M13, exact 4-idempotent classification, universal det ∈ {0, +1}
and |X11| ≤ 1 barriers, exact 11/13 single-path deficit {±E22} and depth-2 realization, uni-
versal forest parity-matching collapse into M13 (T13), Z4 and alternating chain periodicities
(T14--T16), and exact closed-form matrix-power escape theorems for C3, C6, and K4 for all
k ≥ 0 (T17--T19).
2. Verified over explicit finite graph instances by the AST-audited zero-float Bareiss
verifier (C01--C16, 61 adversarial pytest checks): direct fraction-free integer adjacency
determinants confirming π(G ≍1 H) = π(G)π(H) on path joins, P2 sandwiches, chains up to
k = 6, all 1,441 Prüfer-decoded labeled trees on 2 ≤ n ≤ 6 vertices, single-tree surjectivity
witnesses T6,T8, and explicit C3,C6,K4 joined graphs.
3. Imported from cited literature: Harary’s determinant expansion [2] establishing that a
forest F has at most one perfect matching (yielding the parity-matching matrix precondition
consumed by Lean T13), and the general 1-join homomorphism ϕ(G ≍1 H) = ϕ(G)E1ϕ(H) [5,
6] for arbitrary finite graphs.
Archived Artifact Digests. The immutable source artifacts bundled with this record carry
the following exact SHA-256 digests:
• lean/PathJoinMonoidCert.lean:
SHA-256: f09087cac2f3522eb9f9ae60cd14f24dd4c9ad96d97d03730044c93f11e9612d
• src/path_join_monoid_verifier.py:
SHA-256: 02d8506d5b062eca35e955f603ac041293b883490368caf81a93a69ae4d739ca
• certificates/MANIFEST.json:
SHA-256: 156cb437a1ce3a3f4d0dd9f129c16a71014b30fca488ff98fec44c9b8321a8e2
AI Assistance Disclosure. This manuscript, the Lean 4.36.0 formalization, the fraction-free
Bareiss Python verifier, and the adversarial test suite were developed with assistance from Google
Antigravity; all 20 Lean theorems were independently verified by the Lean 4.36.0 kernel, and all
16 certificates were generated and audited deterministically without floating-point arithmetic.
References
[1] Erwin H. Bareiss. Sylvester’s identity and multistep integer-preserving Gaussian elimination.
Mathematics of Computation, 22(103):565–578, 1968.
[2] Frank Harary. The determinant of the adjacency matrix of a graph. SIAM Review, 4(3):202–
210, 1962.
[3] John B. Hickey. Semigroups under a sandwich operation. Proceedings of the Edinburgh
Mathematical Society, 26(3):371–382, 1983.
5
```

---

## Page 6

```text
[4] Mikhail Khovanov, Maithreya Sitaraman, and Daniel Tubbenhauer. Monoidal categories,
representation gap and cryptography. Transactions of the American Mathematical Society,
Series B, 11(10):329–395, 2024.
[5] Daniel Pinzon, Daniel Pragel, and Joshua Roberts. Algebraic structures on graphs joined by
edges, 2024.
[6] Daniel Pinzon, Daniel Pragel, Joshua Roberts, Zack Marshall, and Olivia Strain. Monoid rep-
resentation of the determinants of the adjacency matrices of 1-joined path graphs, November
2026. arXiv:2611.34794v1.
6
```
