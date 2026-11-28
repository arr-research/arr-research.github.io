# Schatten-q Crouzeix Constants and the Hilbert-Schmidt Phase Transition: Universal Conformal Majorization on M_2(C), Odd-Even Clifford Parity Staircases, and Double-Layer Trace Bounds

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR.SCIENCE · ARR-2026-0CWGGAA55A87XAZ9 v1 [Mathematics] 28 Nov 2026
Schatten-q Crouzeix Constants and the
Hilbert–Schmidt Phase Transition: Universal
Conformal Majorization on M2(C), Odd–Even
Clifford Parity Staircases, and Double-Layer Trace
Bounds
Lluis Eriksson∗
November 28, 2026
Abstract
For an n × n complex matrix A ∈ Mn(C) with numerical range W (A) and any exponent
q ∈ [1, ∞], we introduce the normalized Schatten-q Crouzeix constant
Ψq (A) := sup
p∈C[z]
∥p∥W (A) ≤1
‖p(A)‖q,norm, ‖X‖q,norm :=

 1
n
n∑
j=1
σj (X)q


1/q
,
normalized so that ‖I‖q,norm = 1 and Ψq (A) = 1 for every normal matrix, recovering the
classical Crouzeix constant at q = ∞. We establish four main structural laws governing this
functional calculus across dimensions and Schatten exponents:
1. Universal Linear/Disk Majorization and Clifford Parity Staircase (Theo-
rem 2.1): For every n ≥ 1 and A ∈ Mn(C), the singular values of A are weakly
majorized by s(n)w(A), where s(n) = (2, . . . , 2, [1], 0, . . . , 0) has ⌊n/2⌋ twos and (n mod 2)
ones. Consequently, for every unitarily invariant norm Φ, ‖A‖Φ ≤ ‖A(n) ext ‖Φ w(A), yield-
ing the exact odd–even parity staircase supA ‖A‖q,norm/w(A) =
( ⌊n/2⌋2q +(n mod 2)
n
)1/q
.
For q ∈ (1, ∞), equality at 21−1/q is rigidly characterized by unitary representations
of the Clifford algebra Cl2 (X 2 = Y 2 = I, XY + Y X = 0), forcing n even and
A ∼= w(A) ⨁n/2 j=1(2J2). Via Berger’s unitary 2-dilation, the identical majorization ex-
tends to all centered disk polynomials (p(0) = 0, w(A) ≤ 1).
2. Universal Ky Fan Dominance on M2(C) (Theorem 3.2): For every non-normal
2 × 2 matrix AR with elliptical numerical range ER of Joukowsky radius R = a +
b ∈ (1, ∞), the unique odd Riemann conformal map φR : ER → D with focus value
r(R) = φR(1) = θ2(R−4)/θ3(R−4) weakly majorizes f (AR) for every analytic function
f with ‖f ‖ER ≤ 1. Thus φR simultaneously maximizes every unitarily invariant norm
‖f (AR)‖Φ, yielding the exact closed form Ψq (AR) = θ2 (R−4 ) θ3 (R−4 ) ( Rq +R−q 2 )1/q .
3. Exact Hilbert–Schmidt Phase Transition at qc = 2 (Theorem 4.1): Across
M2(C), the nilpotent disk J2 (R → ∞, Ψq (J2) = 21−1/q ) is uniquely extremal for
all q ≥ 2 (Ψq (2) = 21−1/q , proved via an elementary Jacobi-product bound certifying
θ2(τ )2/θ3(τ )2 < 4√τ /(1 + τ )). In stark contrast, for every q ∈ [1, 2), the disk J2 strictly
fails to be extremal: an interior non-degenerate ellipse ER∗ (q) strictly beats 21−1/q , with
critical divergence R∗(q) = 4 1 4−2q (1 + o(1)) and exponentially flat excess as q ↑ 2−. At
the trace norm q = 1, Ψ1(J2) = 1 whereas Ψ1(AR) > 1 for every finite R ∈ (1, ∞),
peaking at Ψ1(2) ≈ 1.11557524 (R∗ ≈ 2.041101, c∗ ≈ 1.551169).
∗Independent researcher, AIRR.SCIENCE (editor@airr.science). Founder verification: AIRR-FOUNDER-1.0.
Manuscript licensed under CC-BY-4.0; code and formal proofs licensed under MIT.
1
```

---

## Page 2

```text
4. Universal n-Dimensional Double-Layer Trace Bound (Theorem 5.1): A self-
contained double-layer POVM trace identity proves ‖p(A)‖2 2,norm ≤ 4‖p‖2 W (A)+ 1 n ∑n j=1 |p(λj )|2 ≤
5‖p‖2 W (A) for all n ≥ 1 and all A ∈ Mn(C), strictly improving Crouzeix–Palencia’s 1+ √ 2
to
√
5 for all 1 ≤ q ≤ 2 (and to 2 whenever p|σ(A) = 0) and to 51/q (1 + √ 2)1−2/q for
q ∈ [2, ∞).
The exact denominator-cleared algebraic and polynomial inequalities underlying all four
theorems are formally certified in Lean 4.36.0 (13 public theorems, 1 public definition, 2
private helpers; zero sorry, zero custom axioms).
1 Introduction
For a complex matrix A ∈ Mn(C), its numerical range (field of values) and numerical radius are
W (A) :=
{
⟨Ax, x⟩ : x ∈ Cn, ‖x‖2 = 1 } , w(A) := sup
z∈W (A)
|z|.
By the Toeplitz–Hausdorff theorem, W (A) is a compact convex subset of C containing the
spectrum σ(A). In 2004, Crouzeix [3, 4] initiated the study of the optimal constant C such
that ‖p(A)‖∞ ≤ C‖p‖W (A) holds for all matrices A and polynomials p, where ‖p‖W (A) :=
supz∈W (A) |p(z)|. Crouzeix proved C ≤ 11.08 in general and C = 2 for n = 2 [3, 4], and
Crouzeix and Palencia [5] (see also [12]) later established the sharp general-dimension bound
C ≤ 1 +
√
2 using the double-layer potential on ∂W (A). In the operator norm (q = ∞), the
extremal geometry is universally believed to be governed by the 2 × 2 nilpotent Jordan block
J2 =
(0 1
0 0
)
, whose numerical range is the closed disk 1 2 D and for which p(z) = 2z achieves
‖p(J2)‖∞ = 2‖p‖W (J2).
What happens when the spectral operator norm ‖p(A)‖∞ is replaced by a normalized
Schatten-q norm
‖X‖q,norm :=
( 1
n tr
(
|X|q))1/q =   1 n n∑ j=1 σj (X)q   1/q (1 ≤ q < ∞), ‖X‖∞,norm := σ1(X),
(1)
where σ1(X) ≥ σ2(X) ≥ · · · ≥ σn(X) ≥ 0 denote the singular values of X ∈ Mn(C)? Because
‖I‖q,norm = 1, every normal matrix A satisfies ‖p(A)‖q,norm =
( 1
n
∑n
j=1 |p(λj )|q)1/q ≤ ‖p‖W (A)
with sharp constant 1 for every q ∈ [1, ∞]. For non-normal matrices, we define the normalized
Schatten-q Crouzeix constants
Ψq(A) := sup
p∈C[z]
∥p∥W (A)≤1
‖p(A)‖q,norm, Ψq(n) := sup
A∈Mn(C)
Ψq(A), Ψq := sup
n≥1
Ψq(n). (2)
Note that by Mergelyan’s theorem on the compact convex set W (A), the supremum in (2)
coincides with the supremum over all functions holomorphic on an open neighborhood of W (A),
and whenever σ(A) ⊂ W (A)◦ (as holds for every non-normal 2 × 2 matrix), it coincides with the
supremum over the full Hardy space H ∞(W (A)◦) of bounded holomorphic functions on W (A)◦.
Moreover, direct sums A ⊕ A leave both W (A) and ‖p(A)‖q,norm invariant, so Ψq(2m) ≥ Ψq(2)
for every m ≥ 1.
A naive expectation from the q = ∞ theory is that the nilpotent disk J2 should remain
extremal across all q ∈ [1, ∞], yielding Ψq(J2) = 21−1/q (since p(z) = 2z has singular values
(2, 0) on J2). In particular, at the normalized trace norm q = 1, one has Ψ1(J2) = 1, which might
suggest Ψ1(A) = 1 universally. We show that this intuition fails dramatically and uncovers a
rich phase diagram governed by conformal geometry, Clifford algebra rigidity, and double-layer
potential theory, summarized in Table 1.
2
```

---

## Page 3

```text
Regime / Setting Exact Constant or Bound Extremal Geometry Mechanism
Linear p(z) = z, ∀n ≥ 1
( ⌊n/2⌋2q +(n mod 2)
n
)1/q (⊕ 2J2 ) ⊕ [1]n mod 2 Weak majorization + Cl2 rigidity (Thm. 2.1)
Disk w(A) ≤ 1, p(0) = 0 Same odd–even staircase Same A(n) ext Berger C2 unitary 2-dilation (Thm. 2.1(c))
M2(C), ∀q ∈ [1, ∞] Ψq (AR) = θ2 (R−4 ) θ3 (R−4 ) ( Rq +R−q 2 )1/q Odd Riemann map φR : ER → D Universal Ky Fan dominance (Thm. 3.2)
M2(C), q ≥ qc = 2 Ψq (2) = 21−1/q Nilpotent disk J2 (R → ∞) Jacobi product bound θ2/θ3 (Thm. 4.1(a))
M2(C), 1 ≤ q < 2 Ψq (2) > 21−1/q ; Ψ1(2) ≈ 1.115575 Interior ellipse R∗(q) ∼ 4 1 4−2q Subcritical R−2q vs. R−4 competition (Thm. 4.1(b))
All n ≥ 1, 1 ≤ q ≤ 2 Ψq (n) ≤
√
5 ≈ 2.2361 (2 if p|σ = 0) Universal (all convex W (A)) Double-layer POVM trace bound (Thm. 5.1)
All n ≥ 1, 2 ≤ q < ∞ Ψq (n) ≤ 51/q (1 + √ 2)1−2/q Universal (all convex W (A)) Hölder interpolation with [5] (Thm. 5.1)
Table 1: Summary of the main theorems for normalized Schatten-q Crouzeix constants Ψq(A)
across dimensions n and exponents q ∈ [1, ∞].
Organization. Section 2 proves the universal singular-value weak majorization for w(A) ≤ 1,
establishes the exact odd–even parity staircase, classifies all even-dimensional extremizers via
Cl2, and extends the majorization to all centered disk polynomials. Section 3 proves universal
Ky Fan dominance of the Riemann conformal map φR on M2(C) via an elementary two-regime
Schwarz–Pick reduction. Section 4 proves the exact Hilbert–Schmidt critical phase transition
at qc = 2, deriving the Jacobi-product critical bound for q ≥ 2 and the critical divergence
law R∗(q) ∼ 41/(4−2q) for q ↑ 2−. Section 5 gives the self-contained double-layer POVM trace
proof of Ψ2 ≤
√
5. Section 6 records the Lean 4.36.0 formalization ledger and formulates the
Schatten-q Crouzeix Conjecture.
2 Universal Linear and Centered-Disk Majorization: The Odd–
Even Clifford Parity Staircase
For two non-increasing nonnegative vectors x, y ∈ Rn ≥0, we write x ≺w y (weak majorization) if∑k
j=1 xj ≤ ∑k j=1 yj for all 1 ≤ k ≤ n. By Ky Fan’s dominance theorem [7, 2], σ(A) ≺w σ(B)
holds if and only if ‖A‖Φ ≤ ‖B‖Φ for every unitarily invariant norm Φ on Mn(C). Define the
reference extremal matrix
A(n) ext :=



⨁n/2
j=1(2J2), n even, (⨁(n−1)/2
j=1 (2J2)
)
⊕ [1], n odd,
(3)
whose singular value vector is s(n) := (2, . . . , 2| {z }
⌊n/2⌋
, 1|{z}
n odd
, 0, . . . , 0| {z }
⌊n/2⌋
) and whose numerical range is D
for every n ≥ 2 (and {1} for n = 1), so w(A(n) ext) = 1.
Theorem 2.1 (Universal Linear/Disk Majorization and Clifford Parity Staircase). Let n ≥ 1.
(a) Universal weak majorization and odd–even staircase: For every A ∈ Mn(C),
σ(A) ≺w s(n) w(A). Consequently, for every unitarily invariant norm Φ on Mn(C),
‖A‖Φ ≤
‖‖A(n) ext ‖‖ Φ w(A), (4)
with equality at A = A(n) ext. In particular, for every q ∈ [1, ∞),
sup
A∈Mn(C)\{0}
‖A‖q,norm
w(A) =
( ⌊n/2⌋ · 2q + (n mod 2)
n
)1/q
, (5)
which equals 21−1/q for every even n and is strictly smaller than 21−1/q for every odd n
whenever q ∈ (1, ∞).
3
```

---

## Page 4

```text
(b) Clifford Cl2 rigidity of equality: Let q ∈ (1, ∞) and A ∈ Mn(C)\{0}. Then ‖A‖q,norm =
21−1/q w(A) holds if and only if n is even and A/w(A) = X + iY where X, Y ∈ Mn(C) are
Hermitian matrices generating a unitary representation of the Clifford algebra Cl2:
X 2 = Y 2 = I, XY + Y X = 0, (6)
equivalently, A is unitarily similar to w(A) ⨁n/2 j=1(2J2).
(c) Centered disk functional calculus: For every A ∈ Mn(C) with w(A) ≤ 1, every
polynomial p ∈ C[z] satisfying ‖p‖D ≤ 1 and p(0) = 0, and every unitarily invariant norm
Φ on Mn(C),
‖p(A)‖Φ ≤
‖‖A(n) ext ‖‖ Φ. (7)
Proof. Proof of (a). Without loss of generality assume w(A) = 1. First, the classical inequality
‖A‖∞ ≤ 2w(A) gives σ1(A) ≤ 2. Second, write the polar decomposition A = U |A| with U ∈
Mn(C) unitary and |A| = (A∗A)1/2 ≽ 0. Diagonalizing U = ∑n j=1 eiθj vj v∗ j in an orthonormal
eigenbasis {v1, . . . , vn} of Cn yields the normalized trace-norm bound
n∑
j=1
σj (A) = tr(|A|) = tr(U ∗A) =
n∑
j=1
e−iθj ⟨Avj , vj ⟩ ≤
n∑
j=1
⏐⏐⟨Avj , vj ⟩ ⏐⏐ ≤ n w(A) = n. (8)
Therefore, for every 1 ≤ k ≤ n, combining σj (A) ≤ 2 with ∑n j=1 σj (A) ≤ n gives
k∑
j=1
σj (A) ≤ min(2k, n) =
k∑
j=1
s(n) j ,
where the exact identity ∑k j=1 s(n) j = min(2k, n) is verified in Lean 4 as extremal_prefix_sum_
eq_min. Thus σ(A) ≺w s(n), and Ky Fan’s dominance theorem [7, 2] implies (4) and (5). For
odd n = 2m + 1 and any q > 1, m · 2q + 1 < m · 2q + 2q−1 = (2m + 1)2q−1 because 2q−1 > 1
(certified for integer q ≥ 2 as odd_schatten_parity_strict), proving the strict parity deficit.
Proof of (b). Normalize w(A) = 1 and fix q ∈ (1, ∞). Since 0 ≤ σj (A) ≤ 2 and q > 1, we
have σj (A)q ≤ 2q−1σj (A), with equality if and only if σj (A) ∈ {0, 2}. Summing over j = 1, . . . , n
and applying (8) gives
n∑
j=1
σj (A)q ≤ 2q−1
n∑
j=1
σj (A) ≤ n 2q−1.
Equality holds if and only if σj (A) ∈ {0, 2} for every j and ∑n j=1 σj (A) = n, which forces
n = 2m even with exactly m singular values equal to 2 and m equal to 0. In particular, ‖A‖2 F =∑n
j=1 σj (A)2 = 4m = 2n. Decomposing A = X + iY into its Hermitian and skew-Hermitian
parts (X = 1 2 (A + A∗), Y = 1 2i (A − A∗)), we have ‖X‖∞ ≤ w(A) = 1, ‖Y ‖∞ ≤ w(A) = 1, and
tr(X 2) + tr(Y 2) = ‖A‖2 F = 2n.
Since tr(X 2) ≤ n‖X‖2 ∞ ≤ n and tr(Y 2) ≤ n‖Y ‖2 ∞ ≤ n, equality forces all eigenvalues of X and
Y to lie in {−1, +1}, i.e., X 2 = Y 2 = I. Moreover, w(A) = 1 implies ‖ cos θ X + sin θ Y ‖∞ ≤ 1
for every θ ∈ R, so
I ≽ (cos θ X+sin θ Y )2 = cos2 θ X 2+sin2 θ Y 2+cos θ sin θ (XY +Y X) = I+ 1 2 sin(2θ) (XY +Y X).
As sin(2θ) takes both positive and negative signs, XY + Y X = 0, proving (6).
Conversely, suppose X, Y are Hermitian satisfying (6). Then Y XY −1 = −X, so tr(X) =
− tr(X) = 0; hence n = 2m is even and X has m eigenvalues +1 and m eigenvalues −1. In
4
```

---

## Page 5

```text
an orthonormal eigenbasis where X = Im ⊕ (−Im), the relations XY + Y X = 0, Y = Y ∗, and
Y 2 = I force Y =
( 0 V
V ∗ 0
)
with V ∈ Mm(C) unitary. Conjugating by Im ⊕ V maps X + iY
unitarily to ⨁m j=1 B where B = (1 i i −1 ) . Direct computation (certified in Lean 4 as clifford_
cl2_nilpotent_check) shows B2 = 0 and ‖B‖2 F = 4, so B is rank-1 nilpotent with norm 2 and
hence unitarily similar to 2J2. Thus A ∼= ⨁m j=1(2J2), which achieves ‖A‖q,norm = 21−1/q.
Proof of (c). Fix A ∈ Mn(C) with w(A) ≤ 1 and a polynomial p ∈ C[z] with ‖p‖D ≤ 1 and
p(0) = 0. For any ρ ∈ (0, 1), set Aρ := ρA; then w(Aρ) ≤ ρ < 1, so σ(Aρ) ⊂ D strictly. Since
p(0) = 0 and ‖p‖D ≤ 1, the Schwarz lemma gives q(z) := p(z)/z ∈ C[z] with ‖q‖D ≤ 1; applying
Carathéodory’s theorem [8] to q yields finite Blaschke products ~Bk converging to q uniformly
on compact subsets of D, and setting Bk(z) := z ~Bk(z) yields finite Blaschke products with
Bk(0) = 0 converging to p uniformly on compact subsets of D (hence in C∞ on a neighborhood
of σ(Aρ), so Bk(Aρ) → p(Aρ)). By Berger’s unitary 2-dilation theorem [1, 11, 14], w(Aρ) ≤ 1
implies the existence of a Hilbert space K ⊇ Cn and a unitary operator U ∈ B(K) such that
Aj ρ = 2PCn U j |Cn for all j ≥ 1. For each finite Blaschke product Bk with Bk(0) = 0 and
every m ≥ 1, the Maclaurin series Bk(z)m = ∑∞ j=m cm,j zj converges absolutely on D with zero
constant term, whence
Bk(Aρ)m =
∞∑
j=m
cm,j Aj ρ = 2PCn


∞∑
j=m
cm,j U j


⏐⏐⏐
Cn
= 2PCn Bk(U )m⏐⏐ Cn (∀ m ≥ 1).
Because Bk is unimodular on ∂D and U is unitary, Bk(U ) is unitary, so Bk(Aρ) admits a unitary
2-dilation. By the converse of Berger’s theorem [14], w(Bk(Aρ)) ≤ 1. Letting k → ∞ gives
w(p(Aρ)) ≤ 1, and letting ρ ↑ 1− gives w(p(A)) ≤ 1. Applying part (a) to p(A) yields (7).
3 Universal Ky Fan Dominance of the Riemann Conformal Map
on M2(C)
Every 2 × 2 complex matrix A ∈ M2(C) falls into one of three aﬀine-unitary equivalence classes:
1. A is normal (W (A) is a line segment or point), for which Ψq(A) = 1 for all q ∈ [1, ∞];
2. A has a repeated eigenvalue and is non-normal (A is aﬀinely and unitarily equivalent to J2,
W (J2) = 1 2 D);
3. A is non-normal with distinct eigenvalues, in which case A is aﬀinely and unitarily equivalent
to
AR :=
(1 c
0 −1
)
, c := R − R−1 > 0, R ∈ (1, ∞). (9)
By the elliptical range theorem [9], W (AR) is the closed filled ellipse ER with foci ±1, semi-
major axis a = 1 2 (R + R−1), semi-minor axis b = 1 2 (R − R−1) = c 2 , and Joukowsky radius
R = a + b ∈ (1, ∞) (so a − b = R−1 and a2 − b2 = 1). The normal limit corresponds to R ↓ 1+,
while the nilpotent disk limit corresponds to R → ∞ (via R−1AR → 2J2).
Let φR : E◦ R → D be the unique Riemann conformal bijection normalized by φR(0) = 0
and φ′ R(0) > 0. By reflection symmetry of ER across both coordinate axes, φR(−z) = −φR(z)
and φR(¯z) = φR(z), so φR(1) = −φR(−1) =: r(R) ∈ (0, 1). By Schwarz’s classical conformal
mapping formula for an ellipse [13, 10], φR(z) =
√
k sn
( 2K(k)
π arcsin z, k
)
where the elliptic
modulus k = k(τ ) corresponds to the nome τ := e−πK′/K = (a − b)4 = R−4. Evaluating at
z = 1 (arcsin 1 = π 2 , sn(K(k), k) = 1) and invoking Jacobi’s theta-function and triple-product
5
```

---

## Page 6

```text
representations [15] yields the exact closed form
r(R) =
√
k(R−4) = θ2(R−4) θ3(R−4) = 2R−1 ∑∞ n=0 R−4n(n+1) 1 + 2 ∑∞ n=1 R−4n2 = 2R−1 ∞∏ m=1 ( 1 + R−8m 1 + R−8m+4 )2 .
(10)
Because φR(1) = r(R) and φR(−1) = −r(R), the functional calculus yields
φR(AR) =
(r(R) c r(R)
0 −r(R)
)
,
whose singular values satisfy σ1σ2 = | det φR(AR)| = r(R)2 and σ2 1 + σ2 2 = r(R)2(2 + c2) =
r(R)2(R2 + R−2), hence
σ1
(
φR(AR)
)
= r(R) R, σ2
(
φR(AR)
)
= r(R) R . (11)
Lemma 3.1 (Strict Schwarz Focus Bound). For every R ∈ (1, ∞), a r(R) = 1 2 (R +R−1) r(R) >
1 strictly, and consequently λ(R) := r(R) R > a r(R) > 1.
Proof. Define f0(z) := z/a. On ER = {(x/a)2 + (y/b)2 ≤ 1} with 0 < b < a, we have
|z|2 = x2 + y2 ≤ a2 with equality only at z = ±a, so f0(E◦ R) is a proper open sub-ellipse
of D with f0(0) = 0. Therefore h := f0 ◦ φ−1 R : D → D is holomorphic, fixes 0, and is not
a rotation. By the strict Schwarz lemma, |h(w)| < |w| for all w ∈ D \ {0}. Evaluating at
w = r(R) = φR(1) ∈ (0, 1) gives 1 a = |f0(1)| = |h(r(R))| < r(R), hence a r(R) > 1. Since
R > 1 2 (R + R−1) = a, λ(R) = r(R)R > a r(R) > 1.
Theorem 3.2 (Universal Ky Fan Dominance of the Riemann Conformal Map on M2(C)). Let
R ∈ (1, ∞) and let AR be given by (9). For every f ∈ H ∞(E◦ R) with ‖f ‖ER ≤ 1, the singular
values of f (AR) are weakly majorized by those of φR(AR):
σ1
(
f (AR)
)
≤ r(R) R, σ1
(
f (AR)
)
+ σ2
(
f (AR)
)
≤ r(R)
(
R + R−1) . (12)
Consequently, φR simultaneously maximizes every unitarily invariant norm ‖f (AR)‖Φ over the
unit ball of H ∞(E◦ R) (and of C[z]). In particular, for every q ∈ [1, ∞],
Ψq(AR) = r(R)
( Rq + R−q
2
)1/q
= θ2(R−4) θ3(R−4) ( Rq + R−q 2 )1/q , (13)
with Ψ∞(AR) = r(R)R, Ψ1(AR) = a r(R) = w(φR(AR)), and Ψq(J2) = 21−1/q for the nilpotent
disk J2.
Proof. First handle the nilpotent disk J2 (W (J2) = 1 2 D): for any f ∈ H ∞( 1 2 D) with ‖f ‖ ≤ 1,
f (J2) =
(u γ
0 u
)
where u = f (0) ∈ D and |γ| = |f ′(0)| ≤ 2(1 − |u|2) by the Schwarz–Pick lemma
on 1 2 D. Letting x = |u| ∈ [0, 1], the singular values satisfy σ1σ2 = x2 and σ2 1 + σ2 2 = 2x2 + |γ|2 ≤
2x2 + 4(1 − x2)2. Hence
(σ1 + σ2)2 = 4x2 + |γ|2 ≤ 4x2 + 4(1 − x2)2 = 4(1 − x2 + x4) ≤ 4,
σ1 ≤ 1 2 ( σ1 + σ2 + √ (σ1 + σ2)2 − 4x2) ≤ 1 + (1 − x2) ≤ 2,
so σ(f (J2)) ≺w (2, 0) = σ(2J2), giving Ψq(J2) = 21−1/q for all q ∈ [1, ∞] (attained by f (z) = 2z).
Now fix R ∈ (1, ∞) and set r := r(R), ρ := 2r 1+r2 ∈ (0, 1), and λ := rR. By Lemma 3.1,
λ > ar > 1. For any f ∈ H ∞(E◦ R) with ‖f ‖ER ≤ 1, write u := f (1) ∈ D and v := f (−1) ∈ D,
so
f (AR) =
(u c 2 (u − v)
0 v
)
.
6
```

---

## Page 7

```text
If |u| = 1 or |v| = 1, the maximum modulus principle forces f to be constant (u = v ∈ ∂D), so
f (AR) = uI has σ1 = 1 < λ and σ1 + σ2 = 2 < 2ar, satisfying (12) strictly. Assume henceforth
that |u|, |v| < 1. Applying the Schwarz–Pick lemma to f ◦ φ−1 R : D → D at the points φR(1) = r
and φR(−1) = −r yields
⏐⏐⏐⏐ u − v 1 − ¯uv ⏐⏐⏐⏐ ≤ ⏐⏐⏐⏐ r − (−r) 1 − r(−r) ⏐⏐⏐⏐ = 2r 1 + r2 = ρ. (14)
Write x := |u| ∈ [0, 1), y := |v| ∈ [0, 1), and t := 2 Re(u¯v) ∈ [−2xy, 2xy], so |u − v|2 = x2 + y2 − t
and |1 − ¯uv|2 = 1 + x2y2 − t. Then (14) rearranges to (1 − ρ2)t ≥ x2 + y2 − ρ2(1 + x2y2).
Because S2 := σ2 1 + σ2 2 = x2 + y2 + c2 4 |u − v|2 is strictly decreasing in t while P := σ1σ2 = xy
is independent of t, both σ1 + σ2 = √S2 + 2P and σ1 = √ 1 2 (S2 + √ S2 2 − 4P 2) are maximized
for fixed (x, y) by taking t as small as permitted, i.e., t = max
(
−2xy, x2+y2−ρ2(1+x2y2) 1−ρ2 ) . This
partitions [0, 1]2 into two regimes along the hyperbola x + y = ρ(1 + xy):
• Regime A (x+y ≤ ρ(1+xy)): t = −2xy binds, giving |u−v|2 = (x+y)2. Setting s := x+y
and p := xy, AM–GM gives 2√p ≤ s ≤ ρ(1 + p) = 2r 1+r2 (1 + p), which forces √p ≤ r, i.e.,
p ≤ r2, and s ≤ 2r (since s 1+s2/4 ≤ s 1+p ≤ 2r 1+r2 ).
• Regime B (x+y ≥ ρ(1+xy)): the Schwarz–Pick constraint binds strictly, yielding (certified
in Lean 4 as schwarz_pick_regime_b_identity)
|u−v|2 = x2+y2− x2 + y2 − ρ2(1 + x2y2) 1 − ρ2 = ρ2 1 − ρ2 (1−x2)(1−y2) = 4r2 (1 − r2)2 (1−x2)(1−y2).
Write K := c2 4 · ρ2 1−ρ2 = c2r2 (1−r2)2 > 0, so S2 = x2 + y2 + K(1 − x2)(1 − y2).
Proof of the Ky Fan 2-norm bound σ1 + σ2 ≤ 2ar = r(R + R−1). In Regime A, (σ1 + σ2)2 =
(x + y)2(1 + c2/4) = a2s2 ≤ (2ar)2 immediately since s ≤ 2r. In Regime B, (σ1 + σ2)2 =
F (x, y) := s2 + K(1 − s2 + 2p + p2), which for fixed s = x + y ∈ [ρ, 2] is strictly increasing
in p = xy. Inside Regime B (p ≤ s ρ − 1) and [0, 1]2 (p ≤ s2/4), the maximal admissible p is
pmax(s) = min
( s2
4 , s ρ − 1 ) . Since
s2
4 −
( s
ρ − 1
)
= 1 4 (s − 2r) ( s − 2 r )
and 2r < 2 < 2/r:
• For s ∈ [ρ, 2r], pmax(s) = s ρ − 1 lies on the hyperbola boundary s = ρ(1 + p) of Regime A,
where F = a2s2 ≤ (2ar)2.
• For s ∈ [2r, 2], pmax(s) = s2/4 is attained at x = y = τ := s/2 ∈ [r, 1], giving F (τ, τ ) =
4τ 2 + K(1 − τ 2)2. This is a convex quadratic in w := τ 2 ∈ [r2, 1], so it attains its maximum
at one of the two endpoints: F (r, r) = 4r2 + c2r2 = (2ar)2 (certified as regime_b_kyfan2_
endpoint_identity) or F (1, 1) = 4 < (2ar)2 by Lemma 3.1.
Thus σ1 + σ2 ≤ 2ar = r(R + R−1) everywhere.
Proof of the Ky Fan 1-norm bound σ1 ≤ λ = rR. For any 2 × 2 matrix with σ2 1 + σ2 2 = S2
and σ1σ2 = P , we have σ1 ≤ λ if and only if both
(i) 2λ2 − S2 ≥ 0 and (ii) Q := λ4 − λ2S2 + P 2 ≥ 0. (15)
In Regime A, S2 = a2s2 − 2p is strictly increasing in s, so both 2λ2 − S2 and Q = λ4 − λ2(a2s2 −
2p) + p2 are minimized for fixed p ∈ [0, r2] at the upper boundary s = ρ(1 + p) (the hyperbola).
Along s = ρ(1 + p):
7
```

---

## Page 8

```text
• First, S2(p) := a2ρ2(1 + p)2 − 2p is convex in p ∈ [0, r2], so its maximum occurs at an
endpoint: at p = 0, S2(0) = a2ρ2 < λ2 < 2λ2 (since λ − aρ = r(λ2−1) R(1+r2) > 0); at p = r2,
S2(r2) = 4a2r2 − 2r2 = r2(R2 + R−2) < 2r2R2 = 2λ2. Hence (i) holds on Regime A.
• Second, QA(p) := λ4 − λ2a2ρ2(1 + p)2 + 2λ2p + p2 vanishes identically at p = r2 (since
ρ(1 + r2) = 2r gives λ4 − r2λ2(R2 + R−2) + r4 = 0), and admits the exact factorization
(certified in Lean 4 as hyperbola_quadratic_factorization):
QA(p) = (r2 − p)
( λ2(λ2 − a2ρ2)
r2 +
(
λ2a2ρ2 − 1 ) p ) . (16)
Because λ > 1, direct algebra (certified in Lean 4 as hyperbola_positivity_factors) gives
λ − aρ = r(λ2 − 1) R(1 + r2) > 0, λaρ − 1 = λ2 − 1 1 + r2 > 0,
so every factor in (16) is nonnegative on p ∈ [0, r2], proving (ii) on Regime A.
In Regime B, for each fixed x ∈ [0, 1], both 2λ2 − S2(x, y) and QB (x, y) := λ4 − λ2(x2 + y2 +
K(1 − x2)(1 − y2)) + x2y2 are aﬀine functions of y2 on the closed interval y2 ∈ [ymin(x)2, 1],
where ymin(x) := max
(
0, ρ−x 1−ρx ) . Hence both attain their minima at an endpoint:
• At y = 1: 2λ2 − (x2 + 1) ≥ 2(λ2 − 1) > 0, and QB (x, 1) = (λ2 − 1)(λ2 − x2) > 0 (certified
in Lean 4 as regime_b_upper_endpoint_factorization).
• For x ∈ [0, ρ], ymin(x) = ρ−x 1−ρx lies on the hyperbola boundary of Regime A, where both (i)
and (ii) were already proved.
• For x ∈ [ρ, 1], ymin(x) = 0; on y = 0, both 2λ2−S2(x, 0) and QB (x, 0) are aﬀine in x2 ∈ [ρ2, 1],
so their minima occur at x = 1 (where 2λ2 − 1 > 0 and QB (1, 0) = λ2(λ2 − 1) > 0) or at
x = ρ (the hyperbola endpoint (ρ, 0) of Regime A).
This establishes (15) across [0, 1]2, proving (12). Ky Fan’s dominance theorem and (11) then
yield (13) (with w(φR(AR)) = r
√
1 + c2/4 = ar = Ψ1(AR) since W (φR(AR)) is the ellipse with
foci ±r and minor axis cr).
Remark 3.3 (Contrast with the Numerical Radius on J2). Although Ψ1(AR) = w(φR(AR))
for every finite R, the numerical-radius Crouzeix constant sup∥f ∥W (A)≤1 w(f (A)) behaves very
differently from Ψ1(A): on the nilpotent disk J2, the non-centered Möbius map fa(z) = 2z+a 1+2¯az
gives w(fa(J2)) = |a| + (1 − |a|2) ≤ 5 4 (attained at |a| = 1 2 , cf. [6]), whereas ‖fa(J2)‖1,norm =√
1 − |a|2 + |a|4 ≤ 1, so Ψ1(J2) = 1 < Ψ1(2) < 5 4 .
4 The Exact Hilbert–Schmidt Critical Phase Transition at qc = 2
Theorem 3.2 reduces the global 2 × 2 constant Ψq(2) = supR∈[1,∞] Ψq(AR) to an explicit one-
dimensional variational problem over Joukowsky radii R ∈ [1, ∞]. Analyzing the competition
between the two singular values r(R)R and r(R)/R reveals a sharp critical phase transition at
the Hilbert–Schmidt exponent qc = 2 (Figure 1).
Theorem 4.1 (Exact Hilbert–Schmidt Phase Transition at qc = 2).
(a) Critical and supercritical regime (q ≥ 2): For every q ∈ [2, ∞] and every finite
R ∈ [1, ∞),
Ψq(AR) < 21−1/q = Ψq(J2). (17)
8
```

---

## Page 9

```text
In particular, Ψq(2) = 21−1/q for all q ≥ 2 (with Ψ2(2) = √ 2), attained uniquely in the
nilpotent disk limit R → ∞. At q = 2, (17) is equivalent to the sharp Jacobi theta inequality
θ2(τ )2
θ3(τ )2 < 4√τ 1 + τ ∀ τ ∈ (0, 1). (18)
(b) Subcritical regime (1 ≤ q < 2): For every q ∈ [1, 2), the nilpotent disk J2 strictly fails
to be extremal: as R → ∞,
Ψq(AR) = 21−1/q
(
1 + 1 q R−2q − 2R−4 + O ( R−4q + R−8)) > 21−1/q. (19)
Consequently, Ψq(2) > 21−1/q is attained at an interior non-degenerate ellipse ER∗(q) with
R∗(q) ∈ (1, ∞).
(c) Critical scaling law as q ↑ 2−: Every global maximizer R∗(q) of R ↦→ Ψq(AR) satisfies
R∗(q) = 4 1 4−2q ( 1 + o(1) ) , Ψq(2) − 21−1/q = 21−1/q 2 − q 2q 4− q 2−q ( 1 + o(1) ) (q ↑ 2−).
(20)
(d) Trace-norm extremal constant (q = 1): While Ψ1(J2) = 1, every finite ellipse
R ∈ (1, ∞) satisfies Ψ1(AR) > 1 strictly, attaining the exact elliptic trace-norm Crouzeix
constant
Ψ1(2) = max R>1
R + R−1
2
θ2(R−4)
θ3(R−4) ≈ 1.1155752422, (21)
at R∗ ≈ 2.04110102 (c∗ = R∗ − (R∗)−1 ≈ 1.55116936).
Proof. Proof of (a). For R = 1, Ψq(A1) = 1 < 21−1/q for all q > 1. Fix R ∈ (1, ∞) and set
t := R−2 ∈ (0, 1) and τ := R−4 = t2 ∈ (0, 1). From the Jacobi triple-product identity (10),
every factor satisfies 1+τ 2m 1+τ 2m−1 < 1, whence immediately
σ1
(
φR(AR)
)
= r(R)R = 2
∞∏
m=1
( 1 + τ 2m
1 + τ 2m−1
)2
< 2. (22)
This already proves (17) for q = ∞. At q = 2, since R2 + R−2 = t−1 + t = 1+t2 t , the inequality
Ψ2(AR) <
√
2 is equivalent to r(R)2(R2 + R−2) < 4, i.e., r(R)2 < 4t 1+t2 , which is precisely (18)
since √τ = t. To prove r(R)2 < 4t 1+t2 for all t ∈ (0, 1), split at t0 := 2 − √ 3 (the positive root
of 1 + t2 = 4t):
• Case 1 (t ∈ [2 −
√
3, 1)): Here 4t 1+t2 ≥ 1, whereas r(R) = φR(1) < 1, so r(R)2 < 1 ≤ 4t 1+t2
holds immediately.
• Case 2 (t ∈ (0, 2 −
√
3)): Here τ = t2 < (2 − √ 3)2 = 7 − 4 √ 3 < 1 10 (since 692 = 4761 <
4800 = 1600·3, certified in Lean 4 as critical_threshold_bound). Keeping only the m = 1
factor in (10) and dropping all m ≥ 2 factors (< 1) gives
r(R)2 < 4√τ ( 1 + τ 2
1 + τ
)4
= 4t 1 + τ · (1 + τ 2)4 (1 + τ )3 .
For every τ ∈ (0, 1/10], expanding gives (1+τ )3 −(1+τ 2)4 = τ (3−τ +τ 2 −6τ 3 −4τ 5 −τ 7) > 0
(formally certified over all rationals 0 < p/q ≤ 1/10 in Lean 4 as hilbert_schmidt_jacobi_
poly_bound). Hence (1 + τ 2)4 < (1 + τ )3 and r(R)2 < 4t 1+t2 , proving (18) and Ψ2(AR) < √ 2.
9
```

---

## Page 10

```text
Finally, for any q ∈ (2, ∞), combining σ2 < σ1 < 2 from (22) with σ2 1 + σ2 2 < 4 yields
Ψq(AR)q = σq 1 + σq 2 2 ≤ σq−2 1 · σ2 1 + σ2 2 2 < 2q−2 · 2 = 2q−1,
proving Ψq(AR) < 21−1/q for every q ≥ 2 and every finite R ∈ [1, ∞).
Proof of (b) and (c). Write Lq(R) := log Ψq (AR) 21−1/q . From (10) and (13), for all R > 1,
Lq(R) = 2
∞∑
m=1
(
log(1 + R−8m) − log(1 + R−8m+4) ) + 1 q log ( 1 + R−2q) . (23)
For R ≥ 2, the infinite sum satisfies 2 ∑∞ m=1(. . . ) = −2R−4 + O(R−8) and 1 q log(1 + R−2q) =
1
q R−2q + O(R−4q) uniformly in q ∈ [1, 2]. Exponentiating yields (19). When 1 ≤ q < 2, we have
2q < 4, so R−2q dominates 2R−4 for large R, giving Lq(R) > 0 for all suﬀiciently large R. Since
Lq(1) = − q−1 q log 2 ≤ 0, limR→∞ Lq(R) = 0, and Lq is continuous on [1, ∞), the supremum
supR≥1 Lq(R) > 0 is attained at an interior maximizer R∗(q) ∈ (1, ∞).
Now let ε := 2 − q ↓ 0+. We first show R∗(q) → ∞: fix any R1 > 1. On the compact interval
[1, R1], Lq(R) → L2(R) uniformly as q ↑ 2−, and by part (a) maxR∈[1,R1] L2(R) < 0 strictly;
hence Lq(R) < 0 throughout [1, R1] for all suﬀiciently small ε > 0. Since Lq(R∗(q)) > 0, we
must have R∗(q) > R1, so R∗(q) → ∞ as ε ↓ 0+. Differentiating (23) with respect to log R at
the interior critical point R = R∗(q) gives
0 = R dLq
dR
⏐⏐⏐
R=R∗
= 8R−4( 1 + O(R−4) ) − 2R−2q( 1 + O(R−2q) ) ,
where the uniform bounds follow from differentiating (23) termwise for R ≥ 2. Multiplying by
1
2 R2q yields
R∗(q)4−2q = R∗(q)2ε = 4 ( 1 + O(R∗(q)−2q + R∗(q)−4) ) .
In particular, for small ε, R∗(q) ≥ 3 1 2ε , so R∗(q)−2q + R∗(q)−4 = O(3−2/ε). Raising both sides
to the power 1 2ε yields
R∗(q) = 4 1 2ε ( 1 + O(3−2/ε) ) 1 2ε = 4 1 4−2q ( 1 + O ( ε−13−2/ε)) = 4 1 4−2q ( 1 + o(1) ) .
Substituting R∗(q)2ε = 4(1 + O(3−2/ε)) and R∗(q)−4 = 4−2/ε(1 + o(1)) into (23) gives
Lq
(
R∗(q) ) = R∗(q)−4
( R∗(q)2ε
q − 2
)
+ O(R∗(q)−4q + R∗(q)−8) = 2 − q 2q 4− q 2−q ( 1 + o(1) ) ,
which implies the second asymptotic in (20) upon exponentiating 21−1/qeLq (R∗(q)).
Proof of (d). By Lemma 3.1 and Theorem 3.2, Ψ1(AR) = a r(R) > 1 for every finite
R ∈ (1, ∞), whereas Ψ1(J2) = 1 and Ψ1(A1) = 1. Since R ↦→ Ψ1(AR) is continuous on
[1, ∞) with limR→∞ Ψ1(AR) = 1, it attains a global maximum strictly greater than 1 on (1, ∞);
numerical golden-section refinement of (10) (verified in verify_schatten_crouzeix.py, where
Ψ1(AR) is numerically observed to be unimodal on (1, ∞)) locates the maximum (21) at R∗ ≈
2.04110102.
Table 2 lists exact numerical values of R∗(q) (with c∗(q) = R∗(q) − R∗(q)−1), the critical
law 41/(4−2q), Ψq(2), and the excess over J2 across the transition, confirming how accurately
the critical scaling matches R∗(q) even far from qc = 2 (within 2.1% at q = 1, 0.38% at q = 1.5,
and 0.0008% at q = 1.8). Note also the dramatic essential-singularity flatness near qc = 2: at
q = 1.85, the excess over J2 has already decayed to 2.09 × 10−9, and by q = 1.95 the asymptotic
excess is 5.95 × 10−26.
10
```

---

## Page 11

```text
Figure 1: The exact Hilbert–Schmidt critical phase transition at qc = 2 (Theorem 4.1). (a) Nor-
malized ratio Ψq(AR)/21−1/q vs. Joukowsky radius R ∈ (1, ∞): for q ≥ 2 the curve stays strictly
below 1 and approaches 1 monotonically as R → ∞ (J2), whereas for every 1 ≤ q < 2 an interior
non-degenerate ellipse strictly exceeds 1, peaking at Ψ1(2) ≈ 1.1156 (R∗ ≈ 2.04). (b) Exact
extremal radius R∗(q) vs. the critical divergence law 41/(4−2q) as q ↑ 2−.
q R∗(q) 41/(4−2q) Ψq (2) 21−1/q (J2) Excess Ψq (2) − 21−1/q
1.00 2.041101 2.000000 1.11557524 1.00000000 +1.1558 × 10−1
1.25 2.555109 2.519842 1.18119746 1.14869835 +3.2499 × 10−2
1.50 4.015150 4.000000 1.26316253 1.25992105 +3.2415 × 10−3
1.70 10.080997 10.079368 1.33035753 1.33031206 +4.5470 × 10−5
1.75 16.000522 16.000000 1.34590606 1.34590019 +5.8672 × 10−6
1.80 32.000257 32.000000 1.36079029 1.36079000 +2.8839 × 10−7
1.85 101.604233 101.593667 1.37502654 1.37502653 +2.0931 × 10−9
2.00 ∞ (J2) ∞
√
2 ≈ 1.41421356 1.41421356 0
3.00 ∞ (J2) — 22/3 ≈ 1.58740105 1.58740105 0
∞ ∞ (J2) — 2.00000000 2.00000000 0
Table 2: Exact 2 × 2 extremal Joukowsky radius R∗(q), critical scaling prediction 41/(4−2q),
optimal constant Ψq(2), and excess over the nilpotent disk J2 across the phase transition at
qc = 2.
5 Universal n-Dimensional Double-Layer Trace Bounds
We now establish dimension-independent upper bounds on Ψq(n) valid for all n ≥ 1 and all
A ∈ Mn(C) that strictly improve upon the Crouzeix–Palencia spectral constant 1 +
√
2 ≈
2.414214 for every finite q ∈ [1, ∞). Remarkably, the Hilbert–Schmidt proof requires neither
the Crouzeix–Palencia recursion C2 ≤ 4 + 2C nor any upper bound on the Cauchy transform
g: completing the square in the trace absorbs the cross-term directly into Schur’s inequality!
Theorem 5.1 (Universal Double-Layer Trace Bound). For every n ≥ 1, every matrix A ∈
Mn(C) with eigenvalues λ1, . . . , λn ∈ W (A) (counted with algebraic multiplicity), and every
polynomial p ∈ C[z],
‖p(A)‖2 2,norm ≤ 4 ‖p‖2 W (A) + 1 n n∑ j=1 |p(λj )|2 ≤ 5 ‖p‖2 W (A). (24)
Consequently, for all n ≥ 1 and all A ∈ Mn(C):
11
```

---

## Page 12

```text
(a) For every q ∈ [1, 2], Ψq(n) ≤
√
5 ≈ 2.236068 < 1 +
√
2.
(b) Whenever p(λj ) = 0 for all j = 1, . . . , n (in particular, for every nilpotent matrix A and
every p with p(0) = 0), ‖p(A)‖2,norm ≤ 2 ‖p‖W (A).
(c) For every q ∈ [2, ∞), combining (24) with Crouzeix–Palencia’s ‖p(A)‖∞ ≤ (1+
√
2)‖p‖W (A) [5]
yields
Ψq(n) ≤ 51/q ( 1 + √ 2 )1−2/q < 1 + √ 2. (25)
Proof. Fix A ∈ Mn(C) and p ∈ C[z]. For any ε > 0, let Ωε := {z ∈ C : dist(z, W (A)) ≤ ε}
be the closed ε-parallel body of the compact convex set W (A). For every compact convex set
W (A) ⊂ C (including a point or line segment), Ωε is compact, convex, contains W (A) (hence
σ(A)) in its interior, and has a C1,1 boundary ∂Ωε (continuously differentiable with Lipschitz-
continuous unit tangent τ (ζ)) oriented counterclockwise by arclength ds, with outward unit
normal ν(ζ) = −iτ (ζ) (so dζ = τ (ζ) ds = iν(ζ) ds). Because W (A) ⊂ Ω◦ ε lies strictly on the
inward side of every supporting tangent line of ∂Ωε, we have Re
(
ν(ζ)(ζI − A)
)
≻ 0 for all
ζ ∈ ∂Ωε.
Define the Hermitian matrix-valued measure on ∂Ωε:
dµε(ζ) := 1 2πi ( (ζI − A)−1 dζ − (¯ζI − A∗)−1 d¯ζ )
= ds π (ζI − A)−1 Re ( ν(ζ)(ζI − A) ) (¯ζI − A∗)−1 ≻ 0.
By Cauchy’s integral formula,
∫
∂Ωε dµε(ζ) = I + I = 2I, so dνε := 1 2 dµε is a positive operator- valued probability measure on ∂Ωε. Define the double-layer operator and conjugate Cauchy
transform
Sε(p) :=
∫
∂Ωε
p(ζ) dµε(ζ) = p(A) + gε(A)∗, gε(A) := 1 2πi ∫ ∂Ωε p(ζ) (ζI − A)−1 dζ.
For any unit vectors x, y ∈ Cn, applying Cauchy–Schwarz to the positive semidefinite matrices
dνε(ζ) ≽ 0 gives
⏐⏐⟨Sε(p)x, y⟩ ⏐⏐ ≤ 2‖p‖Ωε
∫
∂Ωε
⏐⏐⟨dνε(ζ)x, y⟩ ⏐⏐
≤ 2‖p‖Ωε
(∫
∂Ωε
⟨dνεx, x⟩
)1/2(∫
∂Ωε
⟨dνεy, y⟩
)1/2
= 2‖p‖Ωε ,
whence ‖Sε(p)‖∞ ≤ 2‖p‖Ωε and therefore ‖Sε(p)‖2 2,norm ≤ ‖Sε(p)‖2 ∞ ≤ 4‖p‖2 Ωε .
Now expand ‖Sε(p)‖2 2,norm = 1 n tr ( Sε(p)∗Sε(p) ) using Sε(p) = p(A) + gε(A)∗ and cyclicity of
the trace:
‖p(A)‖2 2,norm + ‖gε(A)‖2 2,norm + 2 Re 1 n tr ( p(A) gε(A) ) = ‖Sε(p)‖2 2,norm ≤ 4 ‖p‖2 Ωε . (26)
Let U ∈ Mn(C) be a unitary matrix bringing A to upper-triangular Schur form U ∗AU = T
with diagonal entries λ1, . . . , λn [9]. Then for every ζ ∈ ∂Ωε, U ∗(ζI − A)−1U = (ζI − T )−1 is
upper-triangular with diagonal entries (ζ − λj )−1; integrating over ∂Ωε shows that U ∗gε(A)U
is upper-triangular with aligned diagonal entries wj := 1 2πi ∫ ∂Ωε p(ζ) ζ−λj dζ, and U ∗p(A)gε(A)U is
upper-triangular with diagonal entries zj wj , where zj := p(λj ). Consequently, tr(p(A) gε(A)) =∑n
j=1 zj wj , and Schur’s inequality yields ‖gε(A)‖2 2,norm ≥ 1 n ∑n j=1 |wj |2. Substituting into (26)
and completing the square termwise (certified in Lean 4 as complex_complete_square_nonneg):
|wj |2 + 2 Re(zj wj ) = ⏐⏐wj + zj ⏐⏐2 − |zj |2 ≥ −|zj |2 = −|p(λj )|2,
12
```

---

## Page 13

```text
Figure 2: (a) The exact odd–even Clifford Cl2 parity staircase of Theorem 2.1(a) for n =
1, . . . , 12. (b) Universal Schatten-q Crouzeix landscape comparing our 2 × 2 exact lower bound
Ψq(2) (Theorem 4.1), the nilpotent disk curve 21−1/q, our n-independent double-layer upper
bound (Theorem 5.1), and Crouzeix–Palencia’s spectral bound 1 +
√
2 [5].
Artifact Scope / Verification SHA-256 Digest (full)
src/lean/SchattenCrouzeixCore.lean 13 public thms, 1 def, 2 helpers (0 sorry) 4fe997a76bed97c609e20e618964c9e7
(LEAN_EXIT=0, LAKE_EXIT=0, 21,680 B) 9494c412ea60d67059353cb406aa9bb1
src/python/verify_schatten_crouzeix.py 600 maj. trials, 2,000 ellipses, 43 DL checks af5d3a9db179d7757f6d4fd0947f7844
(VERIFY_EXIT=0, 26,693 B, 3 figures) 1691b0241ddbfb6c751496c524476443
data/verification_summary.json Exact tables (Ψq (2), R∗(q), parity staircase) 9281af4a6f4e3923699b9080aff64adb
(11,794 B) 42ae08d5e2631927597020cd69973fb5
Table 3: Cryptographic SHA-256 verification ledger for Frontier F5 artifacts.
we obtain
‖p(A)‖2 2,norm ≤ 4 ‖p‖2 Ωε + 1 n n∑ j=1 |p(λj )|2.
Since p is continuous on C, ‖p‖Ωε → ‖p‖W (A) as ε ↓ 0+, yielding (24). Part (a) follows from
monotonicity of q ↦→ ‖X‖q,norm on [1, 2] and 5 < (1 +
√
2)2 (certified in Lean 4 as sqrt5_beats_
crouzeix_palencia); part (b) is immediate from (24); and part (c) follows from Hölder’s
inequality 1 n ∑ σq j ≤ σq−2 1 · 1 n ∑ σ2 j ≤ (1 + √ 2)q−2 · 5 ‖p‖q W (A).
6 Lean 4.36.0 Formal Certification, Reproducibility, and Open
Problems
The exact denominator-cleared integer/rational algebraic, majorization, polynomial, and completing-
the-square core of Theorems 2.1–5.1 is formally verified in standalone Lean 4.36.0 in src/lean/
SchattenCrouzeixCore.lean, with zero external dependencies, -DwarningAsError=true, zero
sorry, zero grind, and zero custom axioms (13 public theorems, 1 public definition extremal
PrefixSum, and 2 private helpers; 16 declarations total, building cleanly under both lean and
lake build). Table 3 records the verified artifact inventory and cryptographic SHA-256 di-
gests. All code, formal proofs, numerical verification scripts, and figure generators are publicly
archived at https://github.com/arr-research/arr-research.github.io.
13
```

---

## Page 14

```text
Figure 3: (a) Singular values (σ1(f (AR∗ )), σ2(f (AR∗ ))) of 4,000 valid Schwarz–Pick images at
the trace-norm extremal ellipse R∗ ≈ 2.0411, lying strictly inside the Ky Fan dominance wedge
of the odd Riemann conformal map φR∗ (AR∗ ) (Theorem 3.2). (b) Numerical verification of
the double-layer trace identity (26) across 43 non-normal instances in dimensions n = 2, 3, 4, 5
(maximum identity error 4.44 × 10−16).
Open Problems: The Schatten-q Crouzeix Conjecture. Theorems 4.1 and 5.1 bracket
the universal normalized Schatten-q Crouzeix constant Ψq = supn≥1 Ψq(n) tightly between
Ψq(2) and min
(√
5, 51/q(1 + √ 2)1−2/q) for all q ∈ [1, ∞) (Figure 2(b)). None of the randomized
and structured higher-dimensional tests (n = 3, 4, 5) in verify_schatten_crouzeix.py exceed
Ψq(2), motivating two sharp conjectures:
Conjecture 6.1 (Schatten-q Crouzeix Conjecture and Odd-Dimension Rigidity).
(a) Universal 2 × 2 Reduction: For every q ∈ [1, ∞], the global supremum over all finite
dimensions is already attained in dimension 2: Ψq = Ψq(2). In particular, Ψ2 =
√
2
(Hilbert–Schmidt Crouzeix Conjecture) and Ψ1 = maxR>1 R+R−1 2 θ2(R−4) θ3(R−4) ≈ 1.11557524
(Trace-Norm Crouzeix Conjecture).
(b) Odd-Dimension Gap: For every odd n = 2m + 1 and every q ∈ [2, ∞), does the strict
Clifford parity deficit of Theorem 2.1(a) persist across all polynomials, i.e., Ψq(2m + 1) =( m·2q +1
2m+1
)1/q < 21−1/q?
AI Assistance Disclosure. This research was directed, authored, and verified by Lluis Eriks-
son (editor@airr.science) with autonomous mathematical exploration, Lean 4 formalization,
numerical verification, and LaTeX typesetting assistance from Google Antigravity. All theo-
rems, proofs, Lean 4 kernel builds, and numerical checks were independently verified prior to
release.
References
[1] C. A. Berger. A strange dilation theorem. Notices of the American Mathematical Society,
12:590, 1965.
[2] R. Bhatia. Matrix Analysis, volume 169 of Graduate Texts in Mathematics. Springer-Verlag,
New York, 1997.
[3] M. Crouzeix. Bounds for analytical functions of matrices. Integral Equations and Operator
Theory, 48(4):461–477, 2004.
14
```

---

## Page 15

```text
[4] M. Crouzeix. Numerical range and functional calculus in Hilbert space. Journal of Func-
tional Analysis, 244(2):668–690, 2007.
[5] M. Crouzeix and C. Palencia. The numerical range is a (1+
√
2)-spectral set. SIAM Journal
on Matrix Analysis and Applications, 38(2):649–655, 2017.
[6] S. W. Drury. Symbolic generation of Schwarz lemmas for the numerical radius. Linear
Algebra and its Applications, 428(8–9):2061–2069, 2008.
[7] K. Fan. Maximum properties and inequalities for the eigenvalues of completely continuous
operators. Proceedings of the National Academy of Sciences of the United States of America,
37(11):760–766, 1951.
[8] J. B. Garnett. Bounded Analytic Functions, volume 236 of Graduate Texts in Mathematics.
Springer, New York, revised 1st edition, 2007.
[9] R. A. Horn and C. R. Johnson. Topics in Matrix Analysis. Cambridge University Press,
Cambridge, 1991.
[10] Z. Nehari. Conformal Mapping. McGraw-Hill, New York, 1952.
[11] C. Pearcy. An elementary proof of the power inequality for the numerical radius. Michigan
Mathematical Journal, 13(3):289–291, 1966.
[12] T. Ransford and F. L. Schwenninger. Remarks on the Crouzeix–Palencia proof that the nu-
merical range is a (1+
√
2)-spectral set. SIAM Journal on Matrix Analysis and Applications,
39(1):342–345, 2018.
[13] H. A. Schwarz. Ueber einige Abbildungsaufgaben. Journal für die reine und angewandte
Mathematik, 70:105–120, 1869.
[14] B. Sz.-Nagy, C. Foias, H. Bercovici, and L. Kérchy. Harmonic Analysis of Operators on
Hilbert Space. Universitext. Springer, New York, 2nd edition, 2010.
[15] E. T. Whittaker and G. N. Watson. A Course of Modern Analysis. Cambridge University
Press, Cambridge, 4th edition, 1927.
15
```
