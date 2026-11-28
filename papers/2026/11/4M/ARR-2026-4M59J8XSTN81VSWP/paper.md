# Exact-Z/Q Algebraic Verification-vs-Computation Equivalence, Border-Rank Witness Certificates, and Derandomized Matrix Product Complexity

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-4M59J8XSTN81VSWP | v1 | 2026-11-27
Exact-Z/Q Algebraic Verification-vs-Computation
Equivalence, Border-Rank Witness Certificates, and
Derandomized Matrix Product Complexity
Lluis Eriksson
Independent Researcher, AIRR.SCIENCE (lluiseriksson@gmail.com)
November 27, 2026
Abstract
Inspired by Xiangle Chen’s proof (arXiv:2611.34814v1) that deterministic exact real arith-
metic verification of AB = C requires Ω(nωC ) operations—matching the matrix multiplication
exponent via a decision-tree-to-border-rank reduction—we construct a fully machine-checked,
zero-float algebraic certification suite (MATVER-BORDERRANK-CERT-1.0) for bilinear tensor rank,
Z[ϵ] border-rank witnesses, asymptotic sum exponent bounds, and deterministic linear-probe de-
randomization barriers. All 20 core theorems are formalized constructively in Lean 4.36.0 (zero
sorry, zero Classical.choice, -DwarningAsError=true) and paired with an AST-audited
pure-Z/Q Python verifier emitting 16 SHA-256-indexed certificates (C01–C16). Specifically, we
verify: (i) Strassen’s exact 7-product ⟨2, 2, 2⟩ decomposition over Z across all 64 tensor entries
together with the integer power proof 7100 < 2281 certifying ω < 281/100; (ii) explicit Z[ϵ] polyno-
mial border-rank witnesses separating border rank from exact tensor rank for dual-number mul-
tiplication (Tdual, R = 2 < R = 3) and Schönhage’s direct-sum family ⟨m, 1, m⟩ ⊕ ⟨1, (m − 1)2, 1⟩
at m = 3 (R ≤ 10 < 13) and m = 4 (R ≤ 17 < 25), coupled with pure-integer τ -theorem
proofs certifying ω < 27/10 = 2.70 and ω < 51/20 = 2.55 without floating-point logarithms; (iii)
exact algebraic cost lower bounds from the decision-tree border-rank reduction RR(T ) ≤ c · s,
strictly separating the unconditional Ω(nωC ) theorem from the cited conditional ωC = 9/4 hy-
pothesis (where n9/4/n2 = 2k at n = 24k); and (iv) exact Freivalds error ceilings (2−30 < 10−9,
16−10 < 10−12) contrasted with constructive exact-Q Vandermonde nullspace witnesses proving
that any deterministic linear probe matrix R ∈ Qn×r with r < n admits a nonzero rank-1 error
matrix E = e1v⊤ ̸= 0 satisfying ER = 0 identically.
1 Introduction
Checking whether three n × n matrices satisfy AB = C admits a celebrated randomized O(n2)
algorithm due to Freivalds [4]: sampling r ∈ {0, 1}n uniformly and testing A(Br) = Cr catches
any nonzero error E := AB − C ̸= 0 with probability at least 1/2 per trial. Whether deterministic
verification can also beat fast matrix multiplication (O(nω+ε)) [8, 2] remained open in exact real
arithmetic until Xiangle Chen [3] proved that any deterministic exact real arithmetic decision tree
verifying AB = C requires Ω(nωC ) operations. More generally, Chen showed that a real arithmetic
decision tree of cost s deciding y = T (u, v) forces the bilinear tensor T to lie in the Zariski/Euclidean
closure of tensors of real rank O(s)—that is, RR(T ) = O(s).
Remarkably, Chen further noted that if one assumes the conditional hypothesis ωC = 9/4
together with a fixed-size border-rank lower bound cited from an unrefereed November 24, 2026
preprint, deterministic verification requires Ω(n9/4), strictly separating deterministic arithmetic
verification from Freivalds’ O(n2) randomized verification. Because border-rank arguments, ϵ-
cancellations, and asymptotic τ -theorem exponent derivations are notoriously delicate when checked
numerically, we build MATVER-BORDERRANK-CERT-1.0: a zero-float, Lean 4.36.0 and exact-Z/Q cer-
tification framework covering the exact algebraic machinery of tensor rank, border rank over Z[ϵ],
decision-tree cost reductions, and linear-probe derandomization barriers.
1
```

---

## Page 2

```text
2 Exact Tensor Rank and Z[ϵ] Border-Rank Witness Certificates
2.1 Strassen Exact Rank and Integer Exponent Ceilings
Let ⟨m, p, n⟩ denote the bilinear tensor of (m × p) × (p × n) matrix multiplication. Strassen’s
decomposition [8] proves R(⟨2, 2, 2⟩) ≤ 7. Theorem T01 in Lean 4.36.0 proves all four bilin-
ear coordinate identities over Z universally, and certificate C01 verifies all 43 = 64 entries of∑7
r=1 Ur,iVr,j Wr,k = ⟨2, 2, 2⟩i,j,k. Rather than approximating log2 7 in floating point, Lean T02
certifies the exact integer inequality
7100 < 2281 =⇒ ω ≤ log2 7 < 281 100 = 2.81, (1)
while certificates C02–C03 (Lean T03) record exact recursive Strassen counts (7k multiplications and
6(7k − 4k) additions) at n = 64 and n = 1024.
2.2 Exact Z[ϵ] Border-Rank Witnesses and Integer τ -Theorem Bounds
The border rank R(T ) of a bilinear tensor T is the smallest r such that ϵdT + O(ϵd+1) is a sum of r
rank-1 tensors over R[ϵ] for some integer d ≥ 0 [1, 5]. Unlike exact rank, border rank can be strictly
smaller than R(T ), which is precisely why Chen’s reduction [3] yields a border-rank (rather than
exact-rank) witness from a deterministic verification tree.
Theorem 2.1 (Dual-Number and Schönhage Direct-Sum Z[ϵ] Witnesses; Lean T04–T08).
1. For dual-number multiplication Tdual(a, b) = (a1b1, a1b2 + a2b1) (R = 3), the rank-2 family
M1 = (a1 + ϵa2)(b1 + ϵb2), M2 = a1b1 satisfies M1 − M2 = ϵ(a1b2 + a2b1) + ϵ2a2b2 identically
over Z[ϵ], certifying R(Tdual) ≤ 2 (C04, T04).
2. For every m, n ≥ 2, the Schönhage direct-sum tensor Tm,n := ⟨m, 1, n⟩ ⊕ ⟨1, (m − 1)(n − 1), 1⟩
[6] has exact border rank R(Tm,n) ≤ mn + 1 via the mn + 1 rank-1 products
Mi,j = (ui + ϵxi,j )(vj + ϵyi,j ) (0 ≤ i < m − 1, 0 ≤ j < n − 1),
Ri = ui
(
vn−1 − ϵ
n−2∑
j=0
yi,j
)
, Cj =
(
um−1 − ϵ
m−2∑
i=0
xi,j
)
vj ,
Plast = um−1vn−1, Ptot =
(m−1∑
i=0
ui
)(n−1∑
j=0
vj
)
.
Weighting the outer outputs by ϵ2 gives ϵ2uivj + O(ϵ3), while ∑ Mi,j + ∑ Ri + ∑ Cj + Plast −
Ptot = ϵ2 ∑ i,j xi,j yi,j holds identically with zero ϵ0, ϵ1, and ϵ3 terms (Lean T05; C05 for
m = n = 3 giving R ≤ 10 < 13, C06 for m = n = 4 giving R ≤ 17 < 25).
Theorem 2.2 (Zero-Float Integer Schönhage τ -Theorem Certificates; Lean T09–T10, C07–C08). By
Schönhage’s asymptotic sum inequality [6], R(⟨m, 1, m⟩ ⊕ ⟨1, (m − 1)2, 1⟩) ≤ m2 + 1 implies ω ≤ 3τ0
where (m2)τ0 + ((m − 1)2)τ0 = m2 + 1. Since f (τ ) = V τ 1 + V τ 2 is strictly increasing:
1. At m = 3 (V1 = 9, V2 = 4, r = 10), the exact integer inequalities 3610 < 99 · 510 and
1710 < 49 · 510 certify 99/10 + 49/10 > 36/5 + 17/5 = 53/5 > 10, hence τ0 < 9/10 and
ω < 27/10 = 2.70 (C07, T09).
2. At m = 4 (V1 = 16, V2 = 9, r = 17), the exact integer inequalities 21120 < 1617 · 2020 and
64720 < 917 · 10020 certify 1617/20 + 917/20 > 211/20 + 647/100 = 1702/100 > 17, hence
τ0 < 17/20 and ω < 51/20 = 2.55 (C08, T10).
2
```

---

## Page 3

```text
Figure 1: Left: Exact Z[ϵ] border-rank savings of Schönhage’s direct-sum family ⟨m, 1, m⟩ ⊕ ⟨1, (m−
1)2, 1⟩ versus trivial direct-sum rank (C05–C06). Right: Zero-float certified exponent progression
(ω < 2.81 → 2.70 → 2.55) compared against the cited conditional ωC = 9/4 benchmark and
Freivalds’ n2 randomized verification.
Figure 2: Left: Scaling of naive n3, Strassen nlog2 7, the cited conditional deterministic verification
lower bound n9/4, and 30-trial Freivalds randomized verification (k(6n2 − 2n) ops). Right: Exact
integer separation ratios n9/4/n2 = 2k at n = 24k (C10–C11).
3 Decision-Tree Reduction, Conditional n9/4 Separation, and
Linear-Probe Barriers
3.1 Exact Cost-to-Border-Rank Lower Bounds
Chen’s reduction [3] implies that any deterministic real arithmetic decision tree of cost s verifying
y = T (u, v) satisfies RR(T ) ≤ c · s for a universal constant c ≥ 1. Lean T11–T12 and certificate C09
formalize the exact integer ceiling s ≥ ⌈RR(T )/c⌉ and the asymptotic sandwich ωver = ωC.
Crucially, we maintain a strict logical boundary between the unconditional equivalence Ω(nωC )
and the conditional separation discussed in [3] under the unrefereed assumption ωC = 9/4. At
dyadic quartic dimensions n = 24k, n9/4 = 29k and n2 = 28k are exact integers whose separation
ratio is n9/4/n2 = 2k (Lean T13, C10–C11: 4× at n = 256 and 16× at n = 65536; Figure 2).
3
```

---

## Page 4

```text
Figure 3: Left: Exact Freivalds false-positive ceilings over F2 (2−k, C12) and Schwartz–Zippel
|S| = 16 (16−k, C13). Right: Guaranteed adversarial kernel dimension ≥ n − r for deterministic
linear probes with r < n (C14–C16).
3.2 Freivalds Error Amplification vs. Deterministic Linear-Probe Kernel Bar-
rier
For k independent Freivalds trials over F2 (or a finite set S ⊂ Q via Schwartz–Zippel [7]), the
false-positive probability is at most 2−k (or |S|−k), with exact arithmetic cost k(6n2 − 2n) that is
strictly sub-cubic whenever n ≥ 6k (Lean T14–T15; C12 certifies 2−30 = 1/1073741824 < 10−9, C13
certifies 16−10 = 1/1099511627776 < 10−12).
Why cannot one simply derandomize Freivalds by fixing r < n deterministic probe vectors
R ∈ Qn×r?
Theorem 3.1 (Constructive Deterministic Linear-Probe Kernel Barrier; Lean T16–T19, C14–C16).
For every deterministic linear probe matrix R ∈ Qn×r with r < n, dim ker(R⊤) ≥ n − r ≥ 1. For
any nonzero v ∈ ker(R⊤), the nonzero rank-1 adversarial error matrix E := e1v⊤ ̸= 0 satisfies
ER = 0 identically, so C := AB − E ̸= AB passes every deterministic linear check A(BR) = CR.
In particular, for the n × (n − 1) Vandermonde probe Ri,j = (i + 1)j , the alternating binomial vector
vi = (−1)n−1−i(n−1 i ) gives an explicit integer kernel witness (C14: v = (−1, 3, −3, 1) for 4 × 3, T17;
C15: v = (−1, 5, −10, 10, −5, 1) for 6 × 5, T18).
Figure 3 contrasts Freivalds’ exponential error decay against the linear-probe kernel dimension
lower bound n − r, illustrating why deterministic verification must abandon low-rank linear probing
and pay the full matrix-multiplication exponent Ω(nωC ).
4 Certificate Suite, Scope, and Verification Boundary
Table 1 lists all 16 SHA-256-indexed certificates (C01–C16) generated by our AST-audited zero-float
verifier and validated by 66 adversarial pytest checks alongside Lean 4.36.0 theorems T01–T20.
Verification Boundary and Attribution.
• Machine-checked in Lean 4.36.0 (T01–T20) and exact Z/Q (C01–C16): Strassen’s 7-
product identity, 7100 < 2281, exact Z[ϵ] border-rank witnesses for Tdual and Schönhage’s
direct-sum family, pure-integer τ -theorem inequalities for ω < 2.70 and ω < 2.55, decision-
tree cost lower-bound algebra, exact integer n9/4/n2 ratios, Freivalds exact op counts and
error bounds, and exact-Q linear-probe kernel witnesses. Every Lean theorem depends solely
on [propext, Quot.sound] or zero axioms (zero Classical.choice, zero sorry).
4
```

---

## Page 5

```text
Table 1: Complete summary of all 16 exact-Z/Q certificates (C01–C16) and matching Lean 4.36.0
theorems.
ID Target / Construction Exact Z/Q Certified Result Lean Ref.
C01 Strassen ⟨2, 2, 2⟩ exact tensor 64/64 entries exact, R ≤ 7, 7100 < 2281 ⇒ ω < 2.81 T01, T02
C02 Strassen recursive (n = 64) 117649 muls vs 262144 naive T03
C03 Strassen recursive (n = 1024) 282475249 muls vs 1073741824 naive T03
C04 Dual numbers Tdual Exact Z[ϵ] witness: R = 2 < R = 3 T04
C05 Schönhage ⟨3, 1, 3⟩ ⊕ ⟨1, 4, 1⟩ Exact Z[ϵ] witness: R ≤ 10 < 13 T05, T06
C06 Schönhage ⟨4, 1, 4⟩ ⊕ ⟨1, 9, 1⟩ Exact Z[ϵ] witness: R ≤ 17 < 25 T07, T08
C07 Schönhage τ -theorem (m = 3) 3610 < 99510, 1710 < 49510 ⇒ ω < 2.70 T09
C08 Schönhage τ -theorem (m = 4) 21120 < 16172020, 64720 < 91710020 ⇒ ω < 2.55 T10
C09 Decision-tree reduction (n = 16) R ≥ 512, c = 4 ⇒ deterministic s ≥ 128 T11, T12
C10 Conditional ωC = 9/4 (n = 256) Exact ratio n9/4/n2 = 4 (cited assumption) T13
C11 Conditional ωC = 9/4 (n = 65536) Exact ratio n9/4/n2 = 16 (cited assumption) T13
C12 Freivalds F2 (k = 30) Exact error ≤ 1/1073741824 < 10−9 T14, T15
C13 Freivalds Schwartz–Zippel (|S| = 16) Exact error ≤ 1/1099511627776 < 10−12 (k = 10) T15
C14 Linear-probe barrier (4 × 3) Exact Vandermonde kernel v = (−1, 3, −3, 1), ER = 0 T16, T17
C15 Linear-probe barrier (6 × 5) Exact kernel v = (−1, 5, −10, 10, −5, 1), ER = 0 T18, T19
C16 Linear-probe barrier (8 × 4) Exact 4-dim adversarial kernel, E ̸= 0, ER = 0 T19, T20
• Imported from cited literature (not re-proved inside Lean): Schönhage’s general
asymptotic sum inequality converting border rank of a direct sum into ω ≤ 3τ0 [6]; Chen’s
topological/algebraic theorem constructing a real border-rank-O(s) limit from a real arith-
metic decision tree of cost s [3]; and the conditional hypothesis ωC = 9/4 (cited explicitly as
an unrefereed external assumption in [3]).
Reproducibility and Disclosures. Code, Lean proofs, tests, and certificates are released under
MIT (manuscript CC-BY-4.0). AI-assisted research tooling (Google Antigravity) supported drafting
and formalization under human authorship and oversight by Lluis Eriksson; all formal claims are
independently verified by the Lean 4.36.0 kernel and zero-float pytest suite.
References
[1] Dario Bini, Milvio Capovani, Francesco Romani, and Grazia Lotti. o(n2.7799) complexity for
n × n approximate matrix multiplication. Information Processing Letters, 8(5):234–235, 1979.
[2] Peter Bürgisser, Michael Clausen, and Mohammad A. Shokrollahi. Algebraic Complexity Theory.
Springer, 1997.
[3] Xiangle Chen. Deterministic verification and computation of real matrix products have the same
arithmetic exponent. arXiv preprint arXiv:2611.34814v1, November 2026.
[4] Rūsiņš Freivalds. Fast probabilistic algorithms. Lecture Notes in Computer Science, 74:57–69,
1979.
[5] J. M. Landsberg. Tensors: Geometry and Applications. American Mathematical Society, 2012.
[6] Arnold Schönhage. Partial and total matrix multiplication. SIAM Journal on Computing,
10(3):434–455, 1981.
[7] J. T. Schwartz. Fast probabilistic algorithms for verification of polynomial identities. Journal
of the ACM, 27(4):701–717, 1980.
[8] Volker Strassen. Gaussian elimination is not optimal. Numerische Mathematik, 13(4):354–356,
1969.
5
```
