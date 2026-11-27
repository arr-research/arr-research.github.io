# Optimal Collision-Variance Potentials, Minimal-Degree Newton-Binomial Filtering, and Exact Modular Coset-Halving Certificates for Deterministic Subexponential Discrete Logarithms

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-1VGQE23X9580FBXC` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/deterministic-dlp-optimal-collision-potentials-and-newton-filtering (`v1.0.0`)  
**Canonical PDF SHA-256:** `5b0f3bcad03717699049027323c2b76e93a8514d7588139c4c32bb3b1b35719c`

## Abstract

In a breakthrough of November 2026, Liu, Zhang, and Ren established the first deterministic subexponential-time algorithm for the discrete logarithm problem (DLP) in both prime-order elliptic curves E(F_p) and multiplicative prime fields F_p* (conditional on Cauchy-Hermite Boolean tensor contraction), combining Stage-I conditional-expectation derandomization of a collision-variance potential with fixed penalty lambda = 64 and thresholds B = 4096, A = 16, and Stage-II counterexample extraction via a degree-(4w + 2) nonnegative Newton-Binomial filter Q(X) coupled with Hermite normal form (HNF) modular coset halving. We establish three sharp theorems backed by 20 constructive Lean 4.36.0 theorems and 16 zero-float certificates. First, via two one-line perfect-square identities requiring zero calculus, we derive the exact global optimizer lambda* = c_0 / (sqrt(c_1)(1 - sqrt(c_1))) achieving maximum certified sumset density delta_max = (1 - sqrt(c_1))^2 / c_0, compressing the Stage-I threshold 64x (to A = 4, B = 64, lambda = 9, delta = 4987/9549 > 1/2, where LZR's fixed lambda = 64 collapses to 0.2876 < 1/2) and up to 146x-227x under the sharp binomial bound (1 + 1/(Bm))^m <= B/(B - 1). Second, we prove that LZR's extreme roots j = +/- w are strictly unreachable on [-w(M_lab - 1), w(M_lab - 1)] for all w >= 2, reducing the filter degree by 4 to 4w - 2 = 8m - 2 (saving 4 series terms and 4*ceil(log2(2w M_lab + 2)) bits in P_0), and prove unconditionally that 4w - 2 is the exact minimal degree among all real polynomials separating congruent from non-congruent integers. Third, we certify composite-modulus HNF coset halving, tighten LZR's Neumann M-matrix determinant bound via Fischer-Hadamard 0 < det(H_N) <= prod(w + 1 - D_ii) <= (w + 1)^N, and verify end-to-end deterministic zero-float DLP/ECDLP recovery on F_23*, F_47*, E(F_17), and E(F_23).

## Full Extracted Text

--- Page 1 ---
Optimal Collision-Variance Potentials,
Minimal-Degree Newton–Binomial
Filtering, and Exact Modular Coset-Halving
Certiﬁcates for
Deterministic Subexponential Discrete Logarithms
Lluis Eriksson∗
November 27, 2026
Abstract
In a breakthrough of November 2026, Liu, Zhang, and Ren [ 3] established the ﬁrst
deterministic subexponential-time algorithm for the discrete logarithm problem (DLP) in
both prime-order elliptic curves E(Fp) and multiplicative prime ﬁelds F∗
p (conditional on
the Cauchy–Hermite Boolean tensor contraction primitive), combining two core stages: (I)
conditional-expectation derandomization of a collision-variance potential Φ(S) = ( gordCS +
λ(WS − µ)2)/µ2 with ﬁxed penalty λ = 64 and thresholds n ≥ 4096m, µ ≥ 16gord, and
(II) counterexample extraction via a degree- (4w + 2) nonnegative Newton–Binomial ﬁl-
ter Q(X) = ∏w
j=−w(X − 1 − jMlab)2 coupled with Hermite normal form (HNF) modu-
lar coset halving. In this paper we analyze the exact ﬁnite-dimensional tightness of ev-
ery algebraic primitive in Stages I and II, proving three sharp theorems backed by 20
constructive Lean 4.36.0 theorems and 16 zero-ﬂoat certiﬁcates. First, via two one-line
perfect-square identities requiring zero calculus, we prove the exact closed-form optimal
penalty λ∗ = c0/(√c1(1 − √c1)) maximizing the certiﬁed Cauchy–Schwarz sumset den-
sity at δmax(c0, c1) = (1 − √c1)2/c0. Replacing LZR’s ﬁxed (λ, A, B) = (64 , 16, 4096) by
(9, 4, 64) reduces the block threshold by 64× (and A by 4×) while preserving universal
covering δ ≥ 4987/9549 > 0.5222 > 1/2 (D + D = G), whereas LZR’s ﬁxed λ = 64
collapses to 5099/17728 ≈ 0.2876 < 1/2 and fails; combining λ∗ with the sharp bino-
mial bound (1 + 1 /(Bm))m ≤ B/(B − 1) compresses the Stage-I threshold up to 146×
at A = 4 (B = 28 ) and 227× at A = 16 (B = 18 ). Second, we prove that the two
extreme roots j = ±w in LZR’s ﬁlter polynomial are strictly unreachable by any label
diﬀerence d ∈ [−w(Mlab − 1), w(Mlab − 1)] for every w ≥ 2, yielding the strictly smaller
ﬁlter Q∗(X) = ∏w−1
j=−(w−1)(X − 1 − jMlab)2 of degree 4w − 2 = 8 m − 2 (saving 4 series
terms and 4⌈log2(2wMlab + 2) ⌉ modulus precision bits in P0), and prove unconditionally
that 4w − 2 is the exact minimal degree among all real polynomials separating congruent
from non-congruent integers on [−w(Mlab − 1), w(Mlab − 1)]. Third, we certify modular
HNF coset halving, Fischer–Hadamard sharpening of LZR’s Neumann-series M-matrix de-
terminant bound 0 < det(HN ) ≤ ∏
i(w + 1 −Dii) ≤ (w + 1)N , and end-to-end deterministic
zero-ﬂoat Stage I + Stage II DLP recovery on concrete composite-order F∗
p and prime-order
E(Fp) groups.
∗Independent Researcher. Research, constructive formal veriﬁcation in Lean 4.36.0, zero-ﬂoat
exact rational and elliptic-curve certiﬁcate veriﬁcation, adversarial testing, and manuscript typeset-
ting were conducted with transparent assistance from Google Antigravity. Code is released un-
der MIT; manuscript and ﬁgures under CC-BY-4.0. Repository: https://github.com/lluiseriksson/
deterministic-dlp-optimal-collision-potentials-and-newton-filtering (v1.0.0).
1
AIRR:ARR-2026-1VGQE23X9580FBXC v1  [Computer and informatio...]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
1 Introduction
For a ﬁnite cyclic group G = ⟨P⟩ of order Mlab = gord (either a prime-order elliptic curve
E(Fp) with Mlab = r, or F∗
p with Mlab = p − 1), the discrete logarithm problem (DLP) asks
for the unique x ∈ {0, . . . , Mlab − 1} with [x]P = Q. Whereas generic algorithms face Shoup’s
Ω(√Mlab) lower bound [ 5, 4], Liu, Zhang, and Ren [ 3] (November 23, 2026) achieved worst-case
deterministic subexponential time 2O(b/
√
log log b) = po(1) (b = ⌈log2 p⌉) with zero randomness
and zero unproven number-theoretic heuristics (assuming the Cauchy–Hermite Boolean tensor
contraction primitive).
Because [ 3] aims primarily at the asymptotic 2O(b/
√
log log b) exponent, three fundamental
algebraic components of its pipeline are left unoptimized:
1. Stage-I collision-variance potential: Lemma 3.2 of [ 3] ﬁxes the weight-variance penalty
at λ = 64 and requires qblk ≥ 4096m and µ ≥ 16gord to guarantee sumset density
δ = |D|/gord > 7/8, even though universal 2m-sumset covering D + D = G only requires
δ > 1/2.
2. Stage-II Newton–Binomial ﬁlter degree: Eq. (4.3) of [ 3] constructs the nonnegative
ﬁlter Q(X) = ∏w
j=−w(X − 1 − jMlab)2 of degree 4w + 2 = 8 m + 2 , propagating 4w + 3
truncated power-series coordinates through every tensor contraction at modulus precision
P0 = 2 + 4 mk + dﬁlt⌈log2(2wMlab + 2)⌉.
3. Modular coset halving and M-matrix nullity: Section 4.3 and Remark 3.4 of [ 3]
establish composite-modulus HNF coset halving ( |A′| = |A|g∗/Mlab ≤ | A|/2) and an
optional Neumann-series determinant bound 0 < det(HN ) ≤ (w + 1)N without tightening
diagonal self-decompositions or executing end-to-end zero-ﬂoat certiﬁcation.
We establish three sharp, self-contained structural theorems resolving all three questions:
• Theorem 1 (Exact Potential Optimizer & 64×–227× Threshold Compression):
Derives the exact global optimizer λ∗ = c0/(√c1(1 − √c1)) and δmax = (1 − √c1)2/c0
purely algebraically, showing why ﬁxed λ = 64 fails at B = 64 while λ = 9 certiﬁes
D + D = G (64×–227× lower B).
• Theorem 2 (Exact Minimal Filter Degree 4w−2): Proves that LZR’s j = ±w roots
are strictly unreachable for all w ≥ 2, cuts the ﬁlter degree by 4 to 4w − 2 = 8 m − 2
(saving 4⌈log2(2wMlab + 2) ⌉ precision bits in P0), and proves 4w − 2 is strictly minimal
even under integer-only nonnegativity.
• Theorem 3 (HNF Halving, M-Matrix Bounds, and End-to-End DLP): Sharpens
Remark 3.4 via det(HN ) ≤ ∏
i(w+1−Dii) and certiﬁes full deterministic zero-ﬂoat Stage I
+ Stage II discrete logarithm recovery on F∗
23, F∗
47, E(F17), and E(F23).
2 Optimal Collision-Variance Potential and Stage-I Compres-
sion
In Stage I of [ 3], a seed S deﬁnes m aﬃne-interval factor-base blocks F1(S), . . . , Fm(S) ⊆ Ω
(|Ω| = n, with n = gord − 1 on E(Fp) and n = gord = p − 1 on F∗
p), sumset multiplicity dS(g) =
|{(A1, . . . , Am) ∈ ∏
i Fi(S) : ∑
i Ai = g}|, total product weight WS = ∏
i |Fi(S)| = ∑
g dS(g)
with expectation µ = qm
blk, and collision energy CS = ∑
g dS(g)2. For any penalty weight λ > 0,
deﬁne the generalized collision-variance potential
Φλ(S) := gord CS + λ(WS − µ)2
µ2 . (1)
2

--- Page 3 ---
Write A := µ/gord and B := qblk/m. By pairwise nonpositive covariance within parity classes
and block independence [ 3, Lemma 3.2],
Var(WS)
µ2 ≤
(
1 + 1
qblk
)m
− 1, gord E[CS]
µ2 ≤ 1
A + gord
n
(
1 + 1
qblk
)m
.
Setting c1 ≥ (1+1 /(Bm))m−1 and c0 := 1
A + gord
n (1+ c1) yields E[Φλ(S)] ≤ c0 +λc1; conditional-
expectation bit ﬁxing deterministically produces a seed S with Φλ(S) ≤ c0 + λc1.
Theorem 1 (Exact Potential Optimizer and 64×–227× Stage-I Threshold Compression) . Let
c0 ≥ 1 and 0 < c 1 < 1, and write s := √c1 ∈ (0, 1) and D := supp( dS) = F1(S) + · · · + Fm(S)
with density δ := |D|/gord.
(a) Exact non-calculus Cauchy–Schwarz density bound and global optimizer: For any λ >
c0/(1 − c1) and any seed S satisfying Φλ(S) ≤ a := c0 + λc1,
δ ≥ δ(λ) := 1
c0 + λc1
− 1
λ, (2)
achieved by the one-line algebraic square identity aλ(1−t)2−(λ−a)(a−λt2) = ( λt−a)2 ≥ 0
with signed deviation t := 1 −WS/µ (Lean thm01–thm02). Maximizing δ(λ) over all λ > 0
satisﬁes the exact square identity
(1 − s)2
c0
−
( 1
c0 + λs2 − 1
λ
)
=
(
λs(1 − s) − c0
)2
c0 λ (c0 + λs2) ≥ 0, (3)
so δ(λ) attains its unique global maximum δmax(c0, c1) = (1 −√c1)2/c0 at λ∗ = c0/(√c1(1−√c1)) (Lean thm03–thm04, Certiﬁcate cert03).
(b) 64×–227× Stage-I threshold compression for D + D = G: Universal 2m-sumset covering
D + D = G holds whenever δ > 1/2 (Lean thm08), which is feasible if and only if√
c0/2 + √c1 < 1. In the LZR regime gord ≥ 64 (gord/n ≤ 64/63):
• Under LZR’s conservative variance bound c1 = 2 /B at (A, B) = (4 , 64) (64× lower
B and 4× lower A than LZR’s (16, 4096)), LZR’s ﬁxed λ = 64 collapses to δ(64) =
5099/17728 ≈ 0.2876 < 1/2 (failing), whereas our optimal integer λ = 9 certiﬁes
δ(9) = 4987 /9549 > 0.5222 > 1/2 (Lean thm06, Certiﬁcates cert01–cert02).
• Replacing (1+1 /(Bm))m−1 ≤ 2/B by the sharp rational inequality (1+1 /(Bm))m ≤
B/(B − 1) (valid for all B ≥ 2, m ≥ 1; Certiﬁcate cert13) gives c1 = 1 /(B − 1) and
certiﬁes δ(9) = 57895 /111717 > 0.5182 > 1/2 already at (A, B) = (4 , 32) (128×
compression; Lean thm07).
• Across the exact (A, B) phase boundary (Certiﬁcate cert15), universal covering holds
down to Bmin(4) = 28 (146× reduction) and Bmin(16) = 18 (227× reduction).
Proof. For (a), Cauchy–Schwarz gives CS ≥ W2
S/|D|, so Φλ(S) ≤ a implies (1 − t)2/δ + λt2 ≤
a, where t := 1 − WS/µ (since WS ≥ 0, t ≤ 1, and a − λt2 ≥ W2
S/(µ2δ) > 0 whenever
WS > 0; in fact λ > a =⇒ λt2 ≤ a < λ =⇒ | t| < 1 = ⇒ WS > 0 automatically!).
Multiplying (1 − t)2/δ ≤ a − λt2 by aλδ > 0 and applying the exact identity aλ(1 − t)2 =
(λ − a)(a − λt2) + ( λt − a)2 ≥ (λ − a)(a − λt2) (Lean thm01–thm02) cancels a − λt2 > 0 to
yield δ ≥ (λ − a)/(aλ) = 1 /a − 1/λ. Expanding the numerator of ( 3) directly over Z[c0, s, λ]
(Lean thm03–thm04) proves δ(λ) ≤ (1 − s)2/c0 with equality iﬀ λ = c0/(s(1 − s)).
For (b), (1 + 1 /(Bm))m ≤ e1/B ≤ 1/(1 − 1/B) = B/(B − 1) holds for all B ≥ 2, m ≥ 1
because e−x ≥ 1−x on [0, 1). Substituting c0 = 1 /4+(64 /63)(33/32) = 109 /84, c1 = 1 /32 gives
δ(64) = 84 /277 − 1/64 = 5099 /17728 < 1/2 and δ(9) = 672 /1061 − 1/9 = 4987 /9549 > 1/2
3

--- Page 4 ---
Figure 1: Exact potential optimization and Stage-I threshold compression (Theo-
rem 1). (a) Certiﬁed sumset density δ(λ) at (A, B) = (4 , 64): optimal integer λ = 9 certiﬁes
δ = 4987 /9549 > 0.5222 > 1/2 (D + D = G), whereas LZR’s ﬁxed λ = 64 collapses to
≈ 0.2876 < 1/2 (Certiﬁcate cert02). (b) Minimal threshold Bmin(A) across A ∈ {2, 3, 4, 8, 16}
under conservative 2/B vs. sharp 1/(B − 1) variance bounds, achieving 64×–227× threshold
compression relative to LZR-2026’s (16, 4096) (Certiﬁcate cert15).
(Lean thm06); substituting c0 = 1 /4 + (64 /63)(32/31) = 10145 /7812, c1 = 1 /31 gives δ(9) =
7812/12413 − 1/9 = 57895 /111717 > 1/2 (Lean thm07). Because |D| > gord/2, for every X ∈ G
we have |D| + |X − D| = 2 |D| > g ord (Lean thm08), forcing D ∩ (X − D) ̸= ∅ and hence
X ∈ D + D.
3 Strict Degree- (4w − 2) Minimality of Nonnegative Newton–
Binomial Filters
In Stage II of [ 3], every w-term block-respecting tuple ( w = 2 m ≥ 4) maps to a lifted candidate
label sum Λy(X) ∈ [0, w(Mlab − 1)] for y ∈ { 0, . . . , Mlab − 1}N , so every ﬁxed-shift diﬀerence
d := Λ y(Y ) − Λy(X) belongs to the exact integer domain
Iw,Mlab :=
[
−w(Mlab − 1), w (Mlab − 1)
]
∩ Z. (4)
To extract a pair violating d ≡ 1 (mod Mlab) without modular cancellation, [ 3, Eq. (4.3)] uses
Q(X) = ∏w
j=−w(X − 1 − jMlab)2 of degree 4w + 2 = 8 m + 2. We prove that the two extreme
roots j = ±w never enter Iw,Mlab , and that removing them achieves the exact unconditional
minimal degree even among polynomials restricted only to integer nonnegativity.
Theorem 2 (Minimal-Degree (4w − 2) Nonnegative Newton–Binomial Filter) . Let w ≥ 2 and
Mlab ≥ w + 2.
(a) Strict unreachability of LZR’s extreme roots j = ±w: For every w ≥ 2 and Mlab ≥ 1,
1 + wMlab > w (Mlab − 1), 1 − wMlab < −w(Mlab − 1) (5)
(Lean thm09–thm10), whereas all 2w − 1 roots rj := 1 + jMlab (j ∈ {− (w − 1), . . . , w −
1}) lie strictly inside the interior (−w(Mlab − 1), w(Mlab − 1)) whenever Mlab ≥ w + 2 .
Consequently, the reduced nonnegative ﬁlter polynomial
Q∗(X) :=
w−1∏
j=−(w−1)
(X − 1 − jMlab)2 ∈ Z[X], deg(Q∗) = 4 w − 2 = 8 m − 2, (6)
4

--- Page 5 ---
satisﬁes Q∗(d) ≥ 0 for all d ∈ I w,Mlab with Q∗(d) = 0 ⇐ ⇒ d ≡ 1 (mod Mlab), expands
identically in the integer Newton–Binomial basis Q∗(X) = ∑4w−2
j=0 cj
(X
j
)
(cj ∈ Z, c4w−2 =
(4w − 2)!), and reduces the ring series length ℓ by 4 and the precision budget P0 by exactly
4⌈log2(2wMlab + 2)⌉ bits (Lean thm11, thm13, thm20; Certiﬁcates cert05–cert07).
(b) Unconditional integer-nonnegativity degree lower bound: Let P ∈ R[X] be any nonzero
real polynomial that separates congruent from non-congruent integers on Iw,Mlab without
sign cancellation—meaning P(d) = 0 for every d ∈ I w,Mlab with d ≡ 1 (mod Mlab) and
P(d) > 0 for every d ∈ I w,Mlab with d ̸≡ 1 (mod Mlab) (with no requirement on non-
integer real values!). Then
deg(P) ≥ 2(2w − 1) = 4 w − 2 = 8 m − 2. (7)
Proof. For (a), w(Mlab − 1) = wMlab − w < 1 + wMlab for all w ≥ 1, and w(Mlab − 1) + 1 =
wMlab − (w − 1) < wM lab for all w ≥ 2 (Lean thm09–thm10), proving ( 5). For |j| ≤ w − 1 and
Mlab ≥ w + 2 , rw−1 + 1 = ( w − 1)Mlab + 2 ≤ wMlab − w = w(Mlab − 1) and r−(w−1) − 1 =
−(w − 1)Mlab ≥ − w(Mlab − 1) (since Mlab ≥ w), so every open interval (rj − 1, rj + 1) lies
inside [−w(Mlab − 1), w(Mlab − 1)] and both integer endpoints rj ± 1 belong to Iw,Mlab with
rj ± 1 ̸≡ 1 (mod Mlab) (as Mlab ≥ 3). Since Q∗(d) is a product of integer squares vanishing iﬀ
d ∈ { rj : |j| ≤ w − 1} (Lean thm13), Q∗ separates congruent from non-congruent diﬀerences
identically on Iw,Mlab with degree 2(2w − 1) = 4 w − 2 = 4 w + 2 − 4 (Lean thm11), saving
4⌈log2(2wMlab + 2)⌉ bits in P0 (Lean thm20).
For (b), because Mlab ≥ w + 2 ≥ 4 ≥ 3, we have rj + 1 < rj+1 − 1 for every j (Lean thm12),
so the 2w − 1 open intervals Ij := ( rj − 1, rj + 1) (|j| ≤ w − 1) are strictly pairwise disjoint. Fix
any j ∈ {−(w −1), . . . , w −1}. By hypothesis, P(rj −1) > 0, P(rj) = 0 , and P(rj + 1) > 0. Let
mj ≥ 1 be the multiplicity of the root rj of P. If mj is even, then mj ≥ 2, so Ij already contains
at least 2 real roots of P counted with multiplicity. If mj is odd, then P changes sign at rj, so
there exists ϵ ∈ (0, 1) such that either P(rj − ϵ) < 0 or P(rj + ϵ) < 0; since P(rj ± 1) > 0, the
Intermediate Value Theorem produces at least one additional real root r′
j ∈ Ij \ {rj}, giving at
least mj + 1 ≥ 2 real roots (with multiplicity) inside Ij. Summing over the 2w − 1 pairwise
disjoint intervals Ij yields at least 2(2w − 1) = 4 w − 2 real roots counted with multiplicity,
proving deg(P) ≥ 4w − 2 (Certiﬁcate cert08).
4 Modular Coset Halving, M-Matrix Bounds, and End-to-End
DLP Certiﬁcates
Once ZQ∗ = ∑
(X,Y ) Q∗(Λy(Y ) − Λy(X)) > 0 witnesses a candidate failure (soundness of ﬁxed-
shift relations is formalized by constructive telescoping induction in Lean thm14 and Certiﬁ-
cate cert14), Stage II extracts a violating pair (X∗, Y ∗) and intersects the current aﬃne solu-
tion coset A = ( x0 + Λ lat)/MlabZN with (cnt(Y ∗) − cnt(X∗))⊤x ≡ 1 (mod Mlab) via column
Hermite normal form (HNF) [ 2, 3]. Meanwhile, decomposing [w + 1]Aj = ∑N
i=1 DijAi produces
the column-diagonally-dominant M-matrix HN = ( w + 1) I − Dmult (Dmult ≥ 0, column sums
w) of [ 3, Remark 3.4].
Theorem 3 (Modular Coset Halving, Fischer–Hadamard M-Matrix Bounds, and DLP Recov-
ery).
(a) Exact composite-modulus coset halving: Whenever a congruence a⊤x ≡ c0 (mod Mlab)
has nonempty intersection A′ ⊆ A and is violated by x0 (r0 := ( c0 − a⊤x0) mod Mlab ∈
{1, . . . , Mlab−1}), g∗ := gcd( a⊤b1, . . . , a⊤bN , Mlab) divides both r0 and Mlab, forcing 2g∗ ≤
Mlab and |A′| = |A| · g∗/Mlab ≤ |A|/2 (Lean thm15); consequently, Stage II terminates in
at most ⌊log2 |A0|⌋ ≤ ⌊ N log2 Mlab⌋ cuts (Lean thm16, Certiﬁcate cert09).
5

--- Page 6 ---
Figure 2: Strict degree- (4w − 2) ﬁlter minimality and P0 bit savings (Theorem 2).
(a) Minimal ﬁlter Q∗(X) (deg = 6 at w = 2 , Mlab = 5 ) vs. degree- 5 drop violating integer
nonnegativity at d = 0 , highlighting the 2w − 1 = 3 reachable roots vs. LZR’s unreachable
extreme roots j = ±w (−9, +11; Certiﬁcates cert05, cert08). (b) Conservative modulus
precision savings 4(b + ⌈log2(2w)⌉ + 1) bits in P0 across cryptographic bit-lengths b = 64 –2048
(Certiﬁcate cert07).
(b) Fischer–Hadamard sharpening of the Neumann M-matrix determinant bound: For any
nonnegative N × N integer matrix Dmult with every column sum equal to w ≥ 1, the
M-matrix HN = ( w + 1) I − Dmult has strict column diagonal dominance margin ≥ 1
(Lean thm17), entrywise nonnegative inverse H−1
N = 1
w+1
∑
k≥0( 1
w+1 Dmult)k ≥ 0, and
determinant obeying the tightened hierarchy
0 < det(HN ) ≤
N∏
i=1
(w + 1 − Dii) ≤ (w + 1)N , (8)
strictly tightening LZR’s (w + 1)N bound whenever any diagonal self-multiplicity Dii ≥ 1
(Lean thm18–thm19, Certiﬁcate cert10). In any prime-order group of order r, the Fr-
nullity satisﬁes
dimFr ker(H⊤
N ) ≤ νr(det HN ) ≤
⌊ N∑
i=1
logr(w + 1 − Dii)
⌋
.
(c) End-to-end zero-ﬂoat deterministic DLP and ECDLP certiﬁcates: Executing the determin-
istic Stage I + Stage II pipeline with zero randomness recovers exact discrete logarithms
across both composite-order multiplicative groups via conditional-expectation factor bases,
Proposition 3.3 primitive roots, minimal degree- (4w −2) ﬁlter Q∗, and exact HNF halving
(F∗
23 with Mlab = 22 , 7 cuts; F∗
47 with Mlab = 46 , 11 cuts; Certiﬁcates cert04, cert11) and
prime-order elliptic curves via deterministic aﬃne-interval factor bases and initial consis-
tency congruences ( E(F17) : y2 = x3 + 2x+ 2 of order 19; E(F23) : y2 = x3 +x+ 4 of order
29, where Eq. (4.1) already pins |A| = 1 with 0 extra Stage-II cuts; Certiﬁcate cert12).
Proof. For (a), writing Mlab = g∗qM and r0 = g∗qr, 0 < r 0 < M lab forces 1 ≤ qr < q M , hence
qM ≥ 2 and 2g∗ ≤ Mlab (Lean thm15). Induction on K yields 2K|AK| ≤ | A0| (Lean thm16).
For (b), HN is a strictly column-diagonally-dominant nonsingular M-matrix (so H−1
N ≥ 0 by
the Neumann series; Berman–Plemmons [ 1]). By Koteljanskii’s inequality for M-matrices (a
specialization of Fischer’s inequality for HN with nonpositive oﬀ-diagonals and positive principal
minors), det(HN ) ≤ det(HN [S]) det(HN [Sc]) for every partition, and induction on N yields
6

--- Page 7 ---
Table 1: Stage-I collision-variance potential comparison (Certiﬁcates cert01 and cert15): LZR-
2026 baseline vs. optimal penalty λ∗ across conservative ( 2/B) and sharp ( 1/(B − 1)) variance
bounds.
Conﬁguration A B Variance bound λ E[Φλ] ub δ = |D|/gord lb D + D = G
LZR-2026 baseline 16 4096 2/B 64 373 /336 0.8851 Yes (> 7/8)
LZR ﬁxed λ (64× lower B) 4 64 2/B 64 277 /84 0.2876 No (< 1/2)
Optimal λ (64× lower B) 4 64 2/B 9 1061 /672 0.5222 Yes (> 1/2)
Sharp binom (128× lower B) 4 32 1 /(B − 1) 9 12413 /7812 0 .5182 Yes (> 1/2)
Phase boundary ( A = 4 ) 4 28 1 /(B − 1) λ∗ — > 0.500 Yes (146×)
Phase boundary ( A = 16 ) 16 18 1 /(B − 1) λ∗ — > 0.500 Yes (227×)
Figure 3: Composite-modulus HNF coset halving and Neumann M-matrix certiﬁ-
cates (Theorem 3). (a) Actual HNF coset cuts vs. theoretical halving bound ⌊N log2 Mlab⌋
across composite moduli Mlab ∈ { 12, 22, 30, 46, 60} (Certiﬁcate cert09). (b) Exact Bareiss
determinant det(HN ) vs. our tightened Fischer–Hadamard bound ∏
i(w + 1 − Dii) vs. LZR’s
(w + 1)N bound across N ∈ {4, 5, 6} (Certiﬁcate cert10).
0 < det(HN ) ≤ ∏N
i=1(HN )ii = ∏N
i=1(w + 1 − Dii) ≤ (w + 1)N (formalized in the 2 × 2 base case
in Lean thm18 and veriﬁed via exact Bareiss determinants and entrywise nonnegative adjugates
for N ∈ { 4, 5, 6} in Certiﬁcate cert10). Since rdimFr ker(H⊤
N ) | det(HN ) via Smith normal form
over Z, Lean thm19 yields the tightened nullity bound immediately. Part (c) is directly certiﬁed
by exact integer executions in Certiﬁcates cert04 and cert11–cert12.
5 Formal Veriﬁcation Architecture and Scope
• Layer 1 — Lean 4.36.0 Kernel (lean/DeterministicDlpTheory.lean): Twenty con-
structive theorems compiled under -DwarningAsError=true, with zero external imports,
zero sorry, zero grind, zero Classical.choice, and zero custom axioms (audited via
#print axioms). Layer 1 formalizes both exact potential-optimization square identi-
ties ( thm01–thm04), exact LZR baseline and 64×/128× threshold compression arithmetic
(thm05–thm07), pigeonhole sumset covering ( thm08), strict unreachability of LZR’s ex-
treme roots j = ±w, degree-4 savings, pairwise interval disjointness, factor nonnegativ-
ity, and constructive ﬁxed-shift telescoping soundness ( thm09–thm14), composite-modulus
coset halving and termination induction ( thm15–thm16), M-matrix dominance margins,
2 × 2 Fischer determinant bounds, prime-order nullity bounds, and P0 precision bit sav-
ings ( thm17–thm20). The Intermediate Value Theorem step of Theorem 2(b), general-
7

--- Page 8 ---
N Koteljanskii–Fischer M-matrix inequality, and Cauchy–Hermite contraction black box
of [ 3] are proved/cited in Sections 3–4 and checked on concrete ﬁnite instances in Layer 2.
• Layer 2 — Zero-Float Python Veriﬁer (verification/verify_deterministic_dlp.
py): An AST-audited pure standard-library veriﬁer using strictly int and Fraction (zero
ﬂoats, zero numeric /, zero **, zero limit_denominator), emitting 16 SHA-256 certiﬁ-
cates in certificates/MANIFEST.json and validated by 56 adversarial pytest checks in
tests/test_adversarial.py. Layer 2 veriﬁes the full (A, B, λ) phase boundary, runs
exact deterministic Stage I conditional-expectation seed selection on F∗
23 and F∗
47, exhaus-
tively veriﬁes Q∗ separation and truncated Newton–Binomial power-series contraction,
certiﬁes Bareiss M-matrix determinants and entrywise nonnegative adjugates, and exe-
cutes end-to-end deterministic DLP/ECDLP recovery on F∗
23, F∗
47, E(F17), and E(F23).
References
[1] A. Berman and R. J. Plemmons, Nonnegative Matrices in the Mathematical Sciences , Clas-
sics in Applied Mathematics, Vol. 9, SIAM, Philadelphia, 1994.
[2] R. Kannan and A. Bachem, Polynomial algorithms for computing the Smith and Hermite
normal forms of an integer matrix , SIAM J. Comput. 8 (1979), no. 4, 499–507.
[3] S. Liu, B. Zhang, and K. Ren, A deterministic subexponential-time algorithm for the dis-
crete logarithm problem , Cryptology ePrint Archive, Paper 2026/3020, November 23, 2026.
[4] J. M. Pollard, Monte Carlo methods for index computation ( mod p), Math. Comp. 32
(1978), no. 143, 918–924.
[5] V. Shoup, Lower bounds for discrete logarithms and related problems , in Advances in Cryp-
tology — EUROCRYPT ’97 , LNCS 1233, Springer, 1997, pp. 256–266.
8
