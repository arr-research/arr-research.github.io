# Exact-Z/Q Strassen Spectral Interpolation, Flattening-Rank Interval Bounds, and Border-Rank Separation Certificates for the Asymptotic Spectrum of Tensors

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-3777A0KH3T81X8ZP | v1 | 2026-11-27
Exact-Z/Q Strassen Spectral Interpolation,
Flattening-Rank Interval Bounds, and Border-Rank
Separation Certificates for the Asymptotic Spectrum of
Tensors
Lluis Eriksson
Independent Researcher, AIRR.SCIENCE (lluiseriksson@gmail.com)
November 27, 2026
Abstract
Motivated by the landmark proof by Vrana and Zuiddam (arXiv:2611.34664v1) that
Strassen’s asymptotic spectrum ∆(Tk) of complex order-k tensors (k ≥ 3) is path-connected—
connecting every spectral point to every “one leg versus the rest” flattening rank so that
the evaluation at any fixed tensor is a closed interval—we construct a machine-checked,
zero-float verification and witness suite (TENSOR-SPECTRUM-CONN-CERT-1.0). All 20 core
theorems are proved constructively in Lean 4.36.0 (zero sorry, zero Classical.choice,
-DwarningAsError=true) and paired with an AST-audited pure-Z/Q Python verifier (exact
rational Gaussian elimination over Q) emitting 16 SHA-256-indexed certificates (C01–C16)
checked by 62 adversarial tests. Specifically, we prove and certify: (i) exact 3-mode flat-
tening ranks and Strassen semiring homomorphism laws (Kronecker multiplicativity and
direct-sum additivity) across matrix multiplication ⟨a, b, c⟩, W3, and Coppersmith–Winograd
CWq tensors (C01–C04, C11–C12); (ii) root-free integer-power spectral interval sandwiches
mD ≤ rn1 1 rn2 2 rn3 3 ≤ M D (D = n1 + n2 + n3), strict monotonicity along simplex edges, and
balanced volume-square identities ζ(1/3,1/3,1/3)(⟨a, b, c⟩)3 = (abc)2 (C05–C09, C15–C16); (iii) an
exhaustive 8-entry Z[ε] border-rank-2 witness for W3 together with the root-free cube separation
(2h(1/3))3 = 27/4 < 8 = rkj (W3)3 and exponential tensor-power amplification 27k < 32k (C10,
T11–T13); and (iv) exact graph asymptotic spectrum sandwiches for C5 (4 < 5 < 25/4 with
explicit size-5 strong-square independent set) and C7 via a root-free Chebyshev bracket on
p(t) = 8t3 − 4t2 − 4t + 1 certifying ϑ(C7) ∈ (63/19, 637/191) ⊂ (3, 7/2) (C13–C14, T15–T19).
1 Introduction
Volker Strassen introduced the asymptotic spectrum ∆(Tk) of order-k tensors [4]—the compact
Hausdorff space of monotone semiring homomorphisms ϕ : (Tk, ⊕, ⊗, ≤) → R≥0—to characterize
asymptotic tensor rank, subrank, and matrix multiplication complexity. Whether ∆(Tk) is con-
nected remained open for nearly four decades (known previously only on restricted families [1])
until Vrana and Zuiddam [5] proved that ∆(Tk) is path-connected for every k ≥ 3 by constructing
a general interpolation method connecting every spectral point to every one-leg-vs-rest flattening
rank rkj , and extending the same framework to graphs and Shannon capacity.
Here we build TENSOR-SPECTRUM-CONN-CERT-1.0 to provide an exact-Z/Q, zero-float verifica-
tion baseline certifying flattening-rank semiring homomorphisms, root-free simplex interpolation in-
tervals, W -state border-rank and quantum-functional interval separation, and Chebyshev-bracketed
Lovász-theta graph capacity sandwiches.
2 Flattening Ranks and Root-Free Strassen Spectral Interpolation
For an order-3 tensor T ∈ Qd1×d2×d3 , its three one-leg-vs-rest flattening ranks rj := rkj (T ) ∈ Z≥1
(j ∈ {1, 2, 3}) define extreme points of ∆(T3) that are additive under direct sum ⊕ and multiplicative
1
```

---

## Page 2

```text
Figure 1: Left: Strict monotone Strassen geometric interpolation paths along simplex edges of
⟨2, 3, 5⟩ (flattening ranks 6, 15, 10), marking exact rational certificates C05–C09. Right: Flattening-
rank subintervals [rmin, rmax] across benchmark tensors alongside the strictly non-degenerate W3
spectral gap [(27/4)1/3, 2] (C10). Note that equal flattening ranks for ⟨2, 2, 2⟩ (4) and CW3 (5)
collapse only the flattening-rank subinterval, not the full spectrum ∆(T3) (where maxϕ ϕ(⟨2, 2, 2⟩) =
2ω and CW3 has asymptotic subrank strictly below 5).
under Kronecker product ⊗ (verified by exact-Q Gaussian elimination in C01–C04 and C11–C12;
Lean T07–T08, T14). For rational weights θ = (n1/D, n2/D, n3/D) ∈ ∆2 ∩ Q3 (n1, n2, n3 ∈ Z≥0,
D = n1 + n2 + n3 ≥ 1), the Strassen geometric interpolation functional ζθ(T ) := rn1/D 1 rn2/D 2 rn3/D 3
satisfies exact root-free integer laws:
Theorem 2.1 (Root-Free Spectral Interval Sandwich and Edge Monotonicity; Lean T01–T06,
T09–T10). Let r1, r2, r3 ∈ Z≥1 with m = min(r1, r2, r3) and M = max(r1, r2, r3), and let n1, n2, n3 ∈
Z≥0 with D = n1 + n2 + n3 ≥ 1.
1. Interval Sandwich (T01–T02): mD ≤ rn1 1 rn2 2 rn3 3 ≤ M D, with collapse to rD whenever
r1 = r2 = r3 = r (T03, C01, C16).
2. Strict Simplex-Edge Monotonicity (T04): Whenever 0 < r1 < r2 and t ∈ Z≥0 satisfies
0 ≤ t < D, rD−t 1 rt 2 < rD−(t+1) 1 rt+1 2 , certifying strict monotonicity along the rational edge
connecting r1 to r2 (C05–C06, C08–C09).
3. Rectangular Matrix Multiplication Volume Square (T05): For ⟨a, b, c⟩ with flattening
ranks (ab, bc, ca), (ab)(bc)(ca) = (abc)2 identically; hence ζ(1/3,1/3,1/3)(⟨a, b, c⟩)3 = (abc)2 (e.g.
900 = 302 ∈ [216, 3375] for ⟨2, 3, 5⟩ in C07, T09; 1296 = 362 ∈ [64, 46656] for ⟨1, 4, 9⟩ in C15,
T10; Figure 1).
4. Kronecker Multiplicativity (T06): ζθ(T ⊗ S)D = ζθ(T )Dζθ(S)D identically for all
flattening-rank triples.
3 W -State Border-Rank Witness and Non-Degenerate Spectral In-
terval
For the 3-qubit W -state tensor W3 = |100⟩ + |010⟩ + |001⟩ ∈ Q2×2×2, all three flattening ranks
coincide (rk1 = rk2 = rk3 = 2), yet ∆(T3) evaluated at W3 is a strictly non-degenerate closed
interval containing [(27/4)1/3, 2]:
2
```

---

## Page 3

```text
Figure 2: Left: Root-free exact-Q cubed spectral landmarks of W3 (C10, Lean T12), certifying the
strict gap 27/4 < 8 separating the subrank upper functional from the flattening rank 2. Right:
Exponential amplification (32/27)k across tensor powers W ⊗k 3 (Lean T13).
Theorem 3.1 (W3 Border-Rank-2 Witness and Strict Cube Separation; Lean T11–T13, C10). 1.
Over Z[ε], (e0 + εe1)⊗3 − e⊗3 0 = εW3 + ε2(e0e1e1 + e1e0e1 + e1e1e0) + ε3e⊗3 1 holds across all 8
entries (C10, sum identity Lean T11), certifying R(W3) ≤ 2 (and = 2 since rkj (W3) = 2).
2. The Strassen binary-entropy upper functional value 2h(1/3) = 3/22/3 satisfies (2h(1/3))3 =
27/4 < 8 = rkj (W3)3 (cleared denominator: 27 < 32, exact gap 5/4; Lean T12), and tensor
powers amplify this separation exponentially via 27k < 32k for every k ≥ 1 (Lean T13;
Figure 2).
4 Graph Asymptotic Spectrum: C5 and Chebyshev-Bracketed C7
Sandwiches
In the graph asymptotic spectrum (where Vrana and Zuiddam’s interpolation recovers Lovász-theta
paths [5, 3]), every spectral point ϕ(G) lies in [Θ(G), χf (G)] with α(G) ≤ Θ(G) ≤ ϑ(G) ≤ χf (G).
We certify both C5 and C7 with zero floating-point arithmetic:
Theorem 4.1 (Root-Free C5 and Chebyshev C7 Lovász Sandwiches; Lean T15–T19, C13–C14). 1.
For C5, the 5-vertex independent set {(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)} ⊂ V (C⊠2 5 ) (C13) cer-
tifies Θ(C5)2 ≥ 5 = ϑ(C5)2, and 16 < 20 < 25 certifies α(C5) = 2 < √ 5 < 5/2 = χf (C5)
(Lean T15).
2. For C7, classical cyclotomic theory identifies c = cos(π/7) as the largest real root of p(t) =
8t3 − 4t2 − 4t + 1. Exact rational evaluation gives p(9/10) = −1/125 < 0 < 9521/125000 =
p(91/100) (Lean T16) and p′(t) = 24t2 − 8t − 4 > 0 for all t ≥ 9/10 (Lean T17), pinning
c ∈ (9/10, 91/100) uniquely via the Intermediate Value Theorem. Since f (t) = 7t/(1 + t) is
strictly increasing on t > 0 (Lean T19), ϑ(C7) = 7c/(1+c) satisfies the exact rational sandwich
(Lean T18; Figure 3):
3 = α(C7) < 63 19 < ϑ(C7) < 637 191 < 7 2 = χf (C7). (1)
3
```

---

## Page 4

```text
Figure 3: Left: Root-free Chebyshev minimal polynomial p(t) = 8t3 − 4t2 − 4t + 1 bracketing
cos(π/7) ∈ (9/10, 91/100) with certified derivative positivity (C14, Lean T16–T17). Right: Exact
graph asymptotic spectrum sandwiches [α(G), χf (G)] for C5 (C13) and C7 (C14).
5 Certificate Suite, Scope, and Verification Boundary
Table 1 summarizes all 16 SHA-256-indexed rational certificates (C01–C16) produced by TENSOR-
SPECTRUM-CONN-CERT-1.0, audited by 62 adversarial pytest checks and 20 constructive Lean 4.36.0
theorems.
Verification Boundary and Attribution.
• Machine-checked in Lean 4.36.0 (T01–T20) and exact Z/Q (C01–C16): All root-free
power-law spectral interval sandwiches, simplex-edge strict monotonicity, balanced volume-
square identities, Kronecker multiplicativity, exact Q-Gaussian-elimination flattening ranks
for ⟨a, b, c⟩, W3, CW2, CW3, the 8-entry Z[ε] border-rank-2 witness and 27/4 < 8 (27k < 32k)
spectral gap for W3, the C5 strong-square witness and sandwich, and the C7 Chebyshev
minimal-polynomial root bracket and Lovász-theta sandwich. Every Lean theorem depends
solely on [propext, Quot.sound] or zero axioms (zero Classical.choice, zero sorry).
• Imported from cited literature (not re-proved inside Lean): Vrana and Zuiddam’s
general path-connectedness theorem for ∆(Tk) (k ≥ 3) via symmetric-group representation-
theoretic “method of types” and cover-property interpolation [5], Strassen’s general duality
theorem [4], and Lovász’s semidefinite characterization ϑ(C2m+1) = (2m+1) cos(π/(2m+1)) 1+cos(π/(2m+1)) [3].
Reproducibility, Archived Artifact Hashes, and Disclosures. All verification artifacts are
archived directly inside this AIRR record under MIT (manuscript CC-BY-4.0):
• src/lean/TensorAsymptoticSpectrumCert.lean (20 constructive Lean 4.36.0 theorems
T01–T20):
SHA-256: 3f33a795154fc72a9dbbcc1923bab0cdcf104d8f03fc1659a69cf2f732168064
• src/python/tensor_asymptotic_spectrum_verifier.py (exact Z/Q zero-float engine):
SHA-256: 974e6ec2d3ffb9631cc69875b7f2fa923060fc5b365efbae39478ee792d3cec2
• data/certificates/MANIFEST.json (indexing all 16 exact-Z/Q JSON certificates C01–C16):
SHA-256: a66d30eae0f8633b4b38f75dc8f2c4043c6da56c91909bb5f2ff7e8e489c46cb
AI-assisted research tooling (Google Antigravity) supported drafting and formalization under human
authorship and oversight by Lluis Eriksson; every formal claim is independently checked by the
Lean 4.36.0 kernel and zero-float pytest suite.
4
```

---

## Page 5

```text
Table 1: Complete summary of all 16 exact-Z/Q certificates (C01–C16) and matching Lean 4.36.0
theorems.
ID Tensor / Graph Object Exact Rational / Certified Output (Zero Float) Lean Ref.
C01 ⟨2, 2, 2⟩ matmul Exact flattening ranks (4, 4, 4); flattening subinterval [4, 4] T03, T05
C02 ⟨2, 3, 4⟩ rectangular Exact flattening ranks (6, 12, 8); interval [6, 12] T01--T02
C03 W3 ⊗ W3 Kronecker Product ranks (4, 4, 4) = (2, 2, 2)2 (exact multiplicativity) T06--T07
C04 W3 ⊕ ⟨1, 2, 3⟩ Direct-sum ranks (4, 8, 5) = (2, 2, 2) + (2, 6, 3) (exact) T08
C05 ⟨2, 3, 5⟩ vertex e1 Weight (1, 0, 0): attains exact minimum flattening rank 6 T01, T09
C06 ⟨2, 3, 5⟩ vertex e2 Weight (0, 1, 0): attains exact maximum flattening rank 15 T02, T09
C07 ⟨2, 3, 5⟩ midpoint Weight (1/3, 1/3, 1/3): ζ 3 = 900 = 302 ∈ [216, 3375] T05, T09
C08 ⟨2, 3, 5⟩ edge (3/4, 1/4, 0) ζ 4 = 3240 ∈ [1296, 50625] (monotone path point) T04, T09
C09 ⟨2, 3, 5⟩ edge (1/4, 3/4, 0) ζ 4 = 20250 > 3240 (strict simplex-edge increase) T04, T09
C10 W3 ∈ Q2×2×2 Z[ε] border rank 2 (8 entries); (2h(1/3))3 = 27/4 < 8 T11--T13
C11 CW2 (dim 4) Exact flattening ranks (4, 4, 4) over Q [2] T14
C12 CW3 (dim 5) Exact flattening ranks (5, 5, 5) over Q [2] T14
C13 Graph C5 Shannon cap. Size-5 indep. set in C⊠2 5 ; 4 < ϑ2 = 5 < 25/4 T15
C14 Graph C7 Chebyshev p(9/10) = −1/125 < 0 < p(91/100); ϑ ∈ (63/19, 637/191) T16--T19
C15 ⟨1, 4, 9⟩ balanced Flattening (4, 36, 9); ζ 3 = 1296 = 362 ∈ [64, 46656] T05, T10
C16 ⟨3, 3, 3⟩ symmetric Flattening (9, 9, 9); equal flattening subinterval [9, 9] T03, T20
References
[1] Matthias Christandl, Péter Vrana, and Jeroen Zuiddam. Universal points in the asymptotic
spectrum of tensors. Journal of the American Mathematical Society, 36(1):31–79, 2023.
[2] Don Coppersmith and Shmuel Winograd. Matrix multiplication via arithmetic progressions.
Journal of Symbolic Computation, 9(3):251–280, 1990.
[3] László Lovász. On the Shannon capacity of a graph. IEEE Transactions on Information Theory,
25(1):1–7, 1979.
[4] Volker Strassen. The asymptotic spectrum of tensors. Journal für die reine und angewandte
Mathematik, 384:102–152, 1988.
[5] Péter Vrana and Jeroen Zuiddam. The asymptotic spectrum of tensors is connected.
arXiv:2611.34664v1 [cs.CC / math.AG / quant-ph], 2026.
5
```
