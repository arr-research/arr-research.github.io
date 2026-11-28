# Exact-Rational Fixed-Angle Equiangular Line Bounds, Odd-q Compression Barriers, and Semidefinite Dual Certificates in Dimensions 18-23

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-5F2W1TC6ZK93CSAG | v1 | 2026-11-27
Exact-Rational Fixed-Angle Equiangular Line Bounds,
Odd-q Compression Barriers, and Semidefinite Dual
Certificates in Dimensions 18–23
Lluis Eriksson
Independent Researcher, AIRR.SCIENCE (lluiseriksson@gmail.com)
November 27, 2026
Abstract
Motivated by the recent determination of the exact maximum sizes of real equiangular line
systems in dimensions 18, 19, 20 (N (18) = 57, N (19) = 72, N (20) = 90) and sharp fixed-angle
bounds at odd reciprocal cosines 1/q by Djaljapayan, Liao, and Yu (arXiv:2611.34855v1),
we construct a fully machine-checked, zero-float verification and dual-certificate framework
(EQUILINE-SDP-DUAL-CERT-1.0) spanning dimensions 18 ≤ d ≤ 23 and high-dimensional
fixed-angle regimes. Every algebraic inequality is formalized constructively in Lean 4.36.0 (20
theorems, zero sorry, zero Classical.choice, -DwarningAsError=true) and mirrored by
an AST-audited pure-Q Python verifier producing 16 SHA-256-indexed rational certificates
(C01–C16). Our contributions are fourfold: (i) an exact spectral and descendant strongly regular
graph (SRG) audit separating the non-integer relative-bound failure at d = 18 (432/7, floor 61)
and the arithmetically feasible yet non-existent descendant SRGs srg(75, 32, 10, 16) (d = 19) and
srg(95, 40, 12, 20) (d = 20) from the realized regular two-graphs at d = 21, 22, 23 culminating in
the McLaughlin saturation N (23) = 276; (ii) a constructive proof that α = 1/5 strictly domi-
nates every integer reciprocal cosine α = 1/a with a ≥ 7 across all d ≤ 23 via the uniform ceiling
N1/a(d) ≤ 42 < 57; (iii) explicit rational degree-4 Gegenbauer semidefinite programming (SDP)
dual certificates operating strictly beyond the Lemmens–Seidel relative-bound wall dα2 = 1,
certifying N1/3(18) ≤ 66, the exact integer ceiling N1/3(23) ≤ 100 (from G(23) 4 (1/3) = −1/99),
and N1/5(28) ≤ 294; and (iv) an exact equivalence characterizing the odd-q compression barrier
N1/q (d) ≤ d + e − 1 ⇐⇒ d2 + (e − 1)d < eq2, explicitly certified at q = 319 (d ≤ 898, e = 8) and
q = 5599 (d ≤ 27417, e = 24), together with exact Kronecker Seidel-block lifting and symmetric
conference-matrix saturation certificates (n = 2d at α = 1/
√
2d − 1).
1 Introduction
A system of n lines through the origin in Rd represented by unit vectors u1, . . . , un ∈ Sd−1 is
equiangular with common angle arccos(α) (α ∈ (0, 1)) if |⟨ui, uj ⟩| = α for all 1 ≤ i < j ≤ n. Let
N (d) denote the maximum cardinality of a real equiangular line system in Rd, and let Nα(d) denote
the maximum cardinality at prescribed cosine α. Classical theory [8, 4, 9] establishes the Gerzon
absolute bound N (d) ≤
(d+1
2
)
, the Lemmens–Seidel relative bound
Nα(d) ≤ d(1 − α2) 1 − dα2 whenever dα2 < 1, (1)
and Neumann’s integrality theorem: whenever Nα(d) > 2d, the reciprocal cosine a := 1/α must be
an odd integer.
Dimensions 18 ≤ d ≤ 23 occupy a celebrated transition window between the a = 3 regime
(saturated at d = 7–13 by N (d) = 28) and the Gerzon-tight McLaughlin configuration N (23) =
276 at a = 5 [6, 10]. While N (21) = 126, N (22) = 176, and N (23) = 276 saturate (1) as
regular two-graphs, closing the remaining open gaps at d = 18, 19, 20 required ruling out nonexistent
descendant strongly regular graphs [1, 2] and tightening upper bounds below the relative ceiling.
1
```

---

## Page 2

```text
In a breakthrough preprint, Djaljapayan, Liao, and Yu [5] resolve N (18) = 57, N (19) = 72, and
N (20) = 90 via paired lattice points in sections of rank-24 even unimodular lattices (the Leech lattice
and Golay code generalized Hamming weights), and further establish sharp fixed-angle bounds
N1/q(d) = d + 7 (odd q ≥ 319) and N1/q(d) = d + 23 (odd q ≥ 5599) on explicit dimension intervals
via repeated Seidel-block graphs, alongside a sharp quadratic-irrational family from symmetric
conference matrices.
When upper bounds rely on floating-point semidefinite programming (SDP) solvers or delicate
spectral integrality checks, rounding ambiguity can obscure whether a bound is genuinely rigorous.
Following the exact-rational dual-certificate methodology of [3, 10], we isolate the algebraic core
of fixed-angle equiangular bounds, regular two-graph spectra, degree-4/6 Gegenbauer SDP duals
beyond the dα2 = 1 wall, and odd-q compression barriers, formalizing every theorem constructively
in Lean 4.36.0 (T01–T20, zero Classical.choice) and auditing all 16 rational certificates (C01–C16)
in exact Q arithmetic with zero floating-point operations.
2 Exact Spectral Audit in Dimensions 18–23
2.1 Relative Bounds, Integrality Obstructions, and Descendant SRGs
Write the Gram matrix of n equiangular lines at cosine 1/a (a ∈ Z≥2) as G = In + 1 a S, where
S ∈ {0, ±1}n×n is the symmetric Seidel matrix with zero diagonal. Because rank(G) ≤ d and
G ⪰ 0, the smallest eigenvalue of S is at least −a with multiplicity at least n − d. Equality in (1)
holds if and only if S has exactly two distinct eigenvalues: −a (multiplicity n−d) and b := a(n−d)/d
(multiplicity d), which defines a regular two-graph [9].
Theorem 2.1 (Regular Two-Graph Square-Trace Identity; Lean T15). Let d, n, a, b ∈ Z satisfy the
zero-trace condition db = (n − d)a and the switching quadratic relation ab = n − 1. Then the Seidel
square-trace identity holds identically:
db2 + (n − d)a2 = n(n − 1). (2)
Proof. Substituting db = (n − d)a into db2 = (db)b and (n − d)a2 = ((n − d)a)a = (db)a, both terms
factor through ab = n − 1:
db2 + (n − d)a2 = (n − d)(ab) + d(ab) = n(ab) = n(n − 1).
Isolating a vertex x by Seidel switching transforms S into the n × n block matrix S′ = ( 0 1⊤ 1 S0 ) , where S0 = Jv − Iv − 2A is the Seidel matrix of the descendant graph on v = n − 1 vertices with
adjacency matrix A. Since S′ is orthogonally similar to S, it satisfies (S′)2 − (b − a)S′ − abIn = 0,
which decomposes into v = ab, S01 = (b − a)1 (hence v − 1 − 2k = b − a), and S2 0 − (b − a)S0 − abIv =
−Jv. Thus the descendant SRG(v, k, λ, µ) has exact parameters
v = n − 1, r = a − 1 2 , s = − b + 1 2 , k = v − 1 − (b − a) 2 , µ = k + rs, λ = µ + r + s. (3)
Applying our exact verifier across d ∈ {18, . . . , 23} at a = 5 (C01–C06, Lean T14, T16, T17)
reveals three sharp structural regimes (Figure 1):
1. Non-integer relative ceiling (d = 18, C01, T14): Equation (1) gives 432/7 ≈ 61.7143,
floor 61. Since 18 ∤ 5(61 − 18) = 215, no regular two-graph can attain n = 61; the sharp value
N (18) = 57 [5] lies 4 lines below the relative floor.
2. Arithmetically feasible yet nonexistent descendant SRGs (d = 19, 20, C02–C03, T16):
Equation (1) yields exact integers 76 (b = 15) and 96 (b = 19), passing k(k−λ−1) = µ(v−k−1)
for srg(75, 32, 10, 16) (672 = 672) and srg(95, 40, 12, 20) (1080 = 1080). Both SRGs were
proved nonexistent by Azarija and Marc [1, 2], and Djaljapayan–Liao–Yu [5] pin the sharp
gaps to 76 − 72 = 4 and 96 − 90 = 6.
2
```

---

## Page 3

```text
Figure 1: Left: Gerzon bound, Lemmens–Seidel relative bounds at α = 1/5 and α = 1/7 (≤ 42), and
sharp N (d) values across d = 18–23 (incorporating N (18) = 57, N (19) = 72, N (20) = 90 from [5]).
Right: Exact excess ⌊R1/5(d)⌋ − N (d) distinguishing the d = 18 integrality failure, the d = 19, 20
nonexistent SRGs, and the d = 21–23 regular two-graph saturations.
3. Realized regular two-graph saturations (d = 21, 22, 23, C04–C06, T17): The relative
ceilings 126, 176, and 276 are realized by srg(125, 52, 15, 26), srg(175, 72, 20, 36), and the
McLaughlin graph srg(275, 112, 30, 56), which simultaneously saturates the Gerzon bound(24
2
)
= 276.
Theorem 2.2 (Uniform Dominance of a = 5 over All a ≥ 7 for d ≤ 23; Lean T18, C07). For every
integer dimension 1 ≤ d ≤ 23 and every integer a ≥ 7, any system of N equiangular lines in Rd at
cosine 1/a satisfies N ≤ 42. Consequently, no odd reciprocal cosine a ≥ 7 can achieve N (d) ≥ 57
in dimensions 18 ≤ d ≤ 23.
Proof. Since a ≥ 7 and d ≤ 23, we have a2 ≥ 49 > d and 43 − d ≥ 20, whence
43(a2 − d) − d(a2 − 1) = (43 − d)a2 − 42d ≥ 20 · 49 − 42 · 23 = 980 − 966 = 14 > 0.
By the integer relative bound N (a2 − d) ≤ d(a2 − 1) (Lean T02), N < 43, so N ≤ 42.
3 Exact-Rational Gegenbauer SDP Dual Certificates Beyond dα2 =
1
When dα2 ≥ 1 (for instance α = 1/3 at d ≥ 9, or α = 1/5 at d ≥ 25), the denominator 1 − dα2 in
(1) becomes non-positive and the relative bound collapses. To certify finite upper bounds beyond
this wall without floating-point SDP error, we use the Delsarte–Goethals–Seidel polynomial method
[4, 10] with normalized even Gegenbauer (ultraspherical) polynomials on Sd−1:
G(d) 2 (t) = dt2 − 1 d − 1 , (4)
G(d) 4 (t) = (d + 2)(d + 4)t4 − 6(d + 2)t2 + 3 (d − 1)(d + 1) , (5)
G(d) 6 (t) = (d + 4)(d + 6)(d + 8)t6 − 15(d + 4)(d + 6)t4 + 45(d + 4)t2 − 15 (d − 1)(d + 1)(d + 3) . (6)
Each G(d) 2k is verified constructively to satisfy G(d) 2k (1) = 1 (Lean T06–T08) and positive-semidefinite
zonal kernel structure ∑N i,j=1 G(d) 2k (⟨ui, uj ⟩) ≥ 0 for all unit vectors u1, . . . , uN ∈ Sd−1 [4].
3
```

---

## Page 4

```text
Figure 2: Exact degree-4 Gegenbauer SDP dual ceilings operating strictly beyond the Lemmens–
Seidel relative wall d = a2, compared against the Gerzon bound (d+1 2 ) . Highlighted points mark
certified rational duals C08 (d = 18, α = 1/3 ⇒ N ≤ 66), C09 (d = 23, α = 1/3 ⇒ N ≤ 100 exact),
and C10 (d = 28, α = 1/5 ⇒ N ≤ 294).
Theorem 3.1 (Exact Gegenbauer SDP Dual Bound; Lean T09–T13). Let c2, c4, c6 ∈ Q≥0 and set
c0 := −(c2G(d) 2 (α) + c4G(d) 4 (α) + c6G(d) 6 (α)). If c0 > 0, then F (t) := c0 + c2G(d) 2 (t) + c4G(d) 4 (t) +
c6G(d) 6 (t) satisfies F (±α) = 0 and every equiangular line system of size N at cosine α in Rd obeys
N ≤ F (1) c0 = 1 + c2 + c4 + c6 c0 . (7)
In particular:
1. For (c2, c4, c6) = (1, 0, 0) with dα2 < 1, (7) recovers the Lemmens–Seidel bound (1) identically
(Lean T10, C11).
2. Beyond the relative wall at α = 1/3, pure G4 duals (0, 1, 0) certify N1/3(18) ≤ ⌊26560/397⌋ =
66 (C08, T11) and the exact integer ceiling N1/3(23) ≤ 100 from G(23) 4 (1/3) = −1/99 (C09,
T12).
3. Beyond the relative wall at α = 1/5, the pure G4 dual at d = 28 (dα2 = 28/25 > 1) yields
G(28) 4 (1/5) = −37/10875, certifying N1/5(28) ≤ ⌊10912/37⌋ = 294 strictly below the Gerzon
ceiling 406 (C10, T13).
Proof. Because each zonal kernel G(d) 2k (⟨ui, uj ⟩) is PSD and c2, c4, c6 ≥ 0, summing F (⟨ui, uj ⟩)
over all (i, j) ∈ [N ]2 gives N 2c0 ≤ ∑ i,j F (⟨ui, uj ⟩) = N F (1) + ∑ i̸=j F (±α) = N F (1). Dividing
by N c0 > 0 yields (7) (formalized in integer cross-multiplied form in Lean T09). Exact rational
evaluation of G(d) 4 (α) establishes the three beyond-wall certificates (T11–T13); see Figure 2.
4 Odd-q Compression Barriers, Kronecker Seidel Lifting, and Con-
ference Saturation
A central result of [5] (extending the fixed-angle theory of [7]) determines exact regimes where
N1/q(d) = d + 7 (for odd q ≥ 319) and N1/q(d) = d + 23 (for odd q ≥ 5599), alongside a sharp
quadratic-irrational conference-matrix family. We isolate and machine-check the exact integer bar-
riers governing both upper bounds and algebraic constructions.
4
```

---

## Page 5

```text
Figure 3: Left: Exact odd-q compression horizon dmax(q, e) from (8) for e = 8 (N1/q(d) ≤ d + 7)
and e = 24 (N1/q(d) ≤ d + 23), marking sharp boundary certificates C12 (q = 319, d ≤ 898) and
C13 (q = 5599, d ≤ 27417). Right: Exact relative-bound saturation n = 2d for the symmetric
conference-matrix family at α = 1/
√
2d − 1 (C15–C16).
Theorem 4.1 (Odd-q Compression Barrier Equivalence; Lean T03–T05, C12–C13). Let d ≥ 1,
e ≥ 1, and odd q ≥ 3 satisfy q2 > d. Then the Lemmens–Seidel relative bound strictly certifies
N1/q(d) ≤ d + e − 1 if and only if
d2 + (e − 1)d < eq2. (8)
In particular:
• At q = 319, e = 8: for every 1 ≤ d ≤ 898, d2 + 7d ≤ 812690 < 814088 = 8 · 3192, certifying
N1/319(d) ≤ d + 7 (C12, T04); at d = 899, the barrier reverses (814494 > 814088, relative floor
907 = d + 8).
• At q = 5599, e = 24: for every 1 ≤ d ≤ 27417, d2 + 23d < 24 · 55992, certifying N1/5599(d) ≤
d + 23 (C13, T05); at d = 27418, the barrier reverses (relative floor 27442 = d + 24).
Proof. Exact polynomial expansion (Lean T03) gives the identity
(d + e)(q2 − d) − d(q2 − 1) = eq2 − ( d2 + (e − 1)d ) .
Hence d(q2 − 1)/(q2 − d) < d + e if and only if (8) holds. Since N1/q(d) is an integer, this forces
N1/q(d) ≤ d + e − 1.
On the constructive side, repeated Seidel-block matrices of the form S = Ir ⊗ S0 + (Jr − Ir) ⊗ Jm
(where S0 is the Seidel matrix of a k-regular graph G0 on m vertices with all-ones eigenvalue
θ0 = m − 1 − 2k) produce an exact block-difference eigenvalue θ0 − m = −(2k + 1) of multiplicity
r −1 (Lean T19). Let µq := dim ker(S0 +(2k +1)Im) denote the multiplicity of −(2k +1) in Spec(S0)
(so µq = 0 whenever λmin(S0) > −(2k + 1)). Whenever λmin(S0) ≥ −(2k + 1), the resulting Gram
matrix G = Irm + 1 2k+1 S is positive semidefinite and realizes n = rm lines at cosine 1/(2k + 1) in
dimension d = n − (r − 1 + rµq). Certificate C14 records the algebraic specialization (m, k, r, µq) =
(320, 159, 8, 0), giving exact reciprocal cosine q = 319 and excess n − d = 7 (n = 2560, d = 2553).
Finally, for symmetric conference matrices of order n = 2d (d odd with 2d − 1 a sum of two squares
by Belevitch’s necessary condition, C⊤ = C, C2 = (2d − 1)I2d), Lean T20 and certificates C15–C16
verify the exact quadratic-irrational saturation identity ((2d − 1) − d)(2d) = d((2d − 1) − 1) at
α = 1/
√
2d − 1 (Figure 3).
5
```

---

## Page 6

```text
Table 1: Complete summary of the 16 exact-Q certificates (C01–C16) and matching Lean 4.36.0
theorems.
ID Regime / Target Exact Rational / Integer Output Lean Ref.
C01 d = 18, α = 1/5 relative gap 432/7 (floor 61), 18 ∤ 215, gap 4 vs N (18) = 57 T02, T14
C02 d = 19, n = 76, a = 5 two-graph b = 15, feasible srg(75, 32, 10, 16) (nonexistent) T15, T16
C03 d = 20, n = 96, a = 5 two-graph b = 19, feasible srg(95, 40, 12, 20) (nonexistent) T15, T16
C04 d = 21, n = 126, a = 5 two-graph b = 25, realized srg(125, 52, 15, 26) T15, T17
C05 d = 22, n = 176, a = 5 two-graph b = 35, realized srg(175, 72, 20, 36) T15, T17
C06 d = 23, n = 276, a = 5 McLaughlin b = 55, srg(275, 112, 30, 56), Gerzon tight (276) T01, T17
C07 d ≤ 23, all a ≥ 7 dominance Worst case 1104/26 (floor 42 < 57 ≤ N (18–23)) T18
C08 d = 18, α = 1/3 (G4 SDP dual) G4 = −397/26163 ⇒ 26560/397 (floor 66) T09, T11
C09 d = 23, α = 1/3 (G4 SDP dual) G4 = −1/99 ⇒ 100/1 (exact integer 100) T09, T12
C10 d = 28, α = 1/5 (G4 SDP dual) G4 = −37/10875 ⇒ 10912/37 (floor 294 < 406) T09, T13
C11 d = 20, α = 1/5 (G2 SDP dual) Pure G2 dual recovers 96/1 identically T06, T10
C12 Odd-q barrier q = 319, e = 8 d ≤ 898: 812690 < 814088 ⇒ N1/319(d) ≤ d + 7 T03, T04
C13 Odd-q barrier q = 5599, e = 24 d ≤ 27417: d2 + 23d < 24 · 55992 ⇒ N ≤ d + 23 T03, T05
C14 Kronecker Seidel block (q = 319) (m, k, r, µ) = (320, 159, 8, 0) ⇒ n = 2560, d = 2553 T19
C15 Conference family d = 19 n = 38, α2 = 1/37: exact relative saturation T20
C16 Conference family d = 23 n = 46, α2 = 1/45: exact relative saturation T20
5 Certificate Suite, Scope, and Verification Boundary
Table 1 summarizes all 16 SHA-256-indexed rational certificates (C01–C16) produced by our AST-
audited zero-float Python verifier (EQUILINE-SDP-DUAL-CERT-1.0) and validated by 72 adversarial
pytest checks plus 20 constructive Lean 4.36.0 theorems.
Verification Boundary and Attribution. We state our verification boundary explicitly to
avoid any ambiguity between machine-checked theorems and cited literature:
• Machine-checked in Lean 4.36.0 (T01–T20) and exact Q (C01–C16): All inte-
ger/rational relative bounds, odd-q compression equivalences, Gegenbauer unit normaliza-
tions (G2, G4, G6), integer cross-multiplied SDP dual bounds from PSD Gram hypotheses,
regular two-graph trace/square-trace and descendant SRG parameter equations, uniform
a ≥ 7 dominance for d ≤ 23, Kronecker block-mode eigenvalue identities, and symmetric
conference relative-bound saturation. Every Lean theorem depends solely on [propext,
Quot.sound] (zero Classical.choice, zero sorry).
• Imported from cited literature (not re-proved inside Lean): Positive-semidefiniteness
of zonal spherical harmonics G(d) 2k (⟨ui, uj ⟩) on Sd−1 [4]; graph-theoretic nonexistence of
srg(75, 32, 10, 16) and srg(95, 40, 12, 20) [1, 2]; the Leech-lattice paired-point constructions
and sharp proofs of N (18) = 57, N (19) = 72, N (20) = 90 and explicit G0 spectral realizations
in [5]; and existence of symmetric conference matrices of order 2d (which requires 2d − 1 to be
a sum of two squares, satisfied at 2d − 1 = 37 = 62 + 12 for d = 19 and 2d − 1 = 45 = 62 + 32
for d = 23).
Reproducibility and Disclosures. All code, Lean proofs, tests, and SHA-256 certificates are
released under MIT (manuscript CC-BY-4.0). AI-assisted research tooling (Google Antigravity)
was used in drafting and formalization under human authorship and oversight by Lluis Eriksson;
every mathematical claim is independently checked by the Lean 4.36.0 kernel and zero-float Python
test suite.
6
```

---

## Page 7

```text
References
[1] Jernej Azarija and Tilen Marc. There is no (75, 32, 10, 16) strongly regular graph. Linear
Algebra and its Applications, 557:62–83, 2018.
[2] Jernej Azarija and Tilen Marc. There is no (95, 40, 12, 20) strongly regular graph. Journal of
Combinatorial Designs, 28(4):294–306, 2020.
[3] Alexander Barg and Wei-Hsuan Yu. New bounds for equiangular lines. Contemporary Mathe-
matics, 625:111–121, 2014.
[4] P. Delsarte, J. M. Goethals, and J. J. Seidel. Spherical codes and designs. Geometriae Dedicata,
6(3):363–388, 1977.
[5] Valjakas Djaljapayan, Zhen-Qi Liao, and Wei-Hsuan Yu. Real equiangular lines in dimensions
18–20 and sharp fixed-angle bounds. arXiv preprint arXiv:2611.34855v1, November 2026.
[6] Gary Greaves, Jacobus H. Koolen, Akihiro Munemasa, and Ferenc Szöllősi. Equiangular lines
in Euclidean spaces. Journal of Combinatorial Theory, Series A, 138:208–235, 2016.
[7] Zilin Jiang, Jonathan Tidor, Yuan Yao, Shengtong Zhang, and Yufei Zhao. Equiangular lines
with a fixed angle. Annals of Mathematics, 194(3):729–743, 2021.
[8] P. W. H. Lemmens and J. J. Seidel. Equiangular lines. Journal of Algebra, 24(3):494–512,
1973.
[9] J. J. Seidel. A survey of two-graphs. Colloquio Internazionale sulle Teorie Combinatorie
(Roma, 1973), 1:481–511, 1976.
[10] Wei-Hsuan Yu. New bounds for equiangular lines and spherical two-distance sets. SIAM
Journal on Discrete Mathematics, 31(2):908–917, 2017.
7
```
