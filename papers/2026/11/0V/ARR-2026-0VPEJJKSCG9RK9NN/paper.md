# 7.5x Sharper Non-Scalar Border-Rank Constant (4 q_ns), Exact Single-Gate Border-Rank Tightness via Strassen's Equation, and Sharp Bilinear/PIT Verification Bounds

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-0VPEJJKSCG9RK9NN` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/matrix-verification-sharp-constant-and-nonscalar (`v1.0.0`)  
**Canonical PDF SHA-256:** `f7e7ba12019036f842390a4e7867ff27843250e64625787bafb767303b59870d`

## Abstract

Chen Xiangle (arXiv:2611.34814v1, Theorem 1) recently proved that any deterministic real arithmetic decision tree of cost s verifying a bilinear map T : R^p x R^q -> R^m yields the border-rank upper bound brank_R(T) <= 30s, implying that deterministic verification and computation of n x n matrix products share the same arithmetic exponent omega_v = omega_C. Here we sharpen both the quantitative constant and the algebraic complexity model of Chen's framework, and establish exact tightness, finite-size, and field-dependence boundaries. First (Theorem 1), by initializing the Baur-Strassen reverse pass directly via bar{z}_j += 2 z_j (making all equality/inequality tests and all linear gates completely free), exploiting implicit differentiation for unsplit division gates, constructing an exact 4-term Walsh-Hadamard polarization identity for the 3x3x3 single-gate forward-reverse tensor G_3, and applying double-limit diagonalization to the border-rank-2 squaring tensor G_sq, we collapse Chen's 30s bound to the Ostrowski-Strassen non-scalar inequality brank_C(T) <= brank_R(T) <= 4(q_mul + q_div) + 2 q_sq <= 4 q_ns <= 4s, achieving a universal 7.5x reduction (15x on squaring circuits, 35.4x on Strassen 2x2 verifiers). Using Strassen's commutator equation on A = J_3 - I_3, we prove brank_C(G_3) = rank_R(G_3) = 4 and brank_C(G_sq) = 2 < 3 = rank_R(G_sq), establishing unconditional border-rank tightness for gate-by-gate tensor decompositions. Second (Theorem 2), we derive sharper finite-size non-scalar verification lower bounds q_ns(M_n) >= ceil(brank_C(M_n)/4) (lowering the conditional omega_C = 9/4 Freivalds crossover dimension by 50625/16 approx 3164x, from 12,960,000 to 4096) and halve the mixed-derivative error constant of Chen's Lemma 3 from 2 tau to tau via symmetric diagonal polarization along the exact Pareto frontier (delta^theta, O(delta^{(1-theta)/2})). Third (Theorem 3), we prove that Chen's dense quadratic PIT upper bound S^{omega_C/2 + o(1)} is attained uniquely at the square aspect ratio d = 2K (alpha = 1) with strict rectangular exponent savings |alpha-1|(omega_C-2)/(2(1+alpha)) for all alpha != 1, prove that Chen's univariate sum-of-squares reduction (Proposition 5(ii)) and real Gram reduction fail over every finite field F_p and over C, and tighten complex-to-real pair simulation constants via Gauss's 3-multiplication identity. All algebraic identities, commutator minors, dual-number executions, and finite-size tables are machine-verified by 20 constructive, dependency-free Lean 4.36.0 theorems (0 sorry, 0 Classical.choice), 16 zero-float SHA-256 rational certificates, and 56 adversarial tests.

## Full Extracted Text

--- Page 1 ---
7.5×Sharper Non-Scalar Border-Rank Constant (4q ns), Exact
Single-Gate Border-Rank Tightness via Strassen’s Equation, and
Sharp Bilinear/PIT Verification Bounds
Lluis Eriksson*
November 2026
Abstract
Chen Xiangle (arXiv:2611.34814v1, Theorem 1) recently proved that any deterministic
real arithmetic decision tree of cost s verifying a bilinear map T : Rp ×R q →R m yields
the border-rank upper bound rankR(T) ≤ 30s, implying that deterministic verification and
computation of n×n matrix products share the same arithmetic exponent ωv = ωC. Here
we sharpen both the quantitative constant and the algebraic complexity model of Chen’s
framework, and establish exact tightness, finite-size, and field-dependence boundaries. First
(Theorem 1), by initializing the Baur–Strassen reverse pass directly via ¯zj += 2zj (making all
equality/inequality tests and all linear gates completely free), exploiting implicit differentiation
for unsplit division gates, constructing an exact 4-term Walsh–Hadamard polarization
identity for the 3 × 3 × 3 single-gate forward–reverse tensor G3, and applying double-limit
diagonalization to the border-rank-2 squaring tensor Gsq, we collapse Chen’s 30 s bound to
the Ostrowski–Strassen non-scalar inequality rankC(T) ≤rank R(T) ≤ 4(q× + q÷) + 2qsq ≤
4qns ≤ 4s, achieving a universal 7 .5× reduction (15× on squaring circuits, 35 .4× on Strassen
2×2 verifiers). Using Strassen’s commutator equation on A = J3 −I3, we prove rankC(G3) =
rankR(G3) = 4 and rankC(Gsq) = 2 < 3 = rankR(Gsq), establishing unconditional border-
rank tightness for gate-by-gate tensor decompositions. Second (Theorem 2), we derive
sharper finite-size non-scalar verification lower bounds qns(Mn) ≥ ⌈rankC(Mn)/4⌉ (lowering
the conditional ωC = 9/4 Freivalds crossover dimension by 50625/16 ≈ 3164×, from 12,960,000
to 4096) and halve the mixed-derivative error constant of Chen’s Lemma 3 from 2 τ to τ
via symmetric diagonal polarization along the exact Pareto frontier ( δθ, O(δ(1−θ)/2)). Third
(Theorem 3), we prove that Chen’s dense quadratic PIT upper bound SωC/2+o(1) is attained
uniquely at the square aspect ratio d = 2K (α = 1) with strict rectangular exponent savings
|α− 1|(ωC −2)/(2(1+ α)) for all α̸ = 1, prove that Chen’s univariate sum-of-squares reduction
(Proposition 5(ii)) and real Gram reduction fail over every finite field Fp and over C, and
tighten complex-to-real pair simulation constants via Gauss’s 3-multiplication identity. All
algebraic identities, commutator minors, dual-number executions, and finite-size tables are
machine-verified by 20 constructive, dependency-free Lean 4.36.0 theorems ( 0 sorry, 0
Classical.choice), 16 zero-float SHA-256 rational certificates, and 56 adversarial tests.
1 Introduction
In a landmark recent preprint, Chen Xiangle [ 4] resolved the thirty-four-year-old problem of
B¨ urgisser, Karpinski, and Lickteig [3] on deterministic algebraic verification of matrix multi-
plication: if a deterministic real arithmetic decision tree of worst-case cost s decides whether
y=T(u, v) for a bilinear mapT:R p ×R q →R m, then the border rank ofTsatisfies
rankR(T)≤30s(1)
* Independent Researcher. Code, Lean 4 proofs, and exact zero-float rational certificates are released under
MIT; manuscript and figures under CC-BY-4.0.
1

--- Page 2 ---
(Chen [4, Theorem 1]), which combined with Bini’s interpolation lemma [ 2] ([4, Lemma 4]) yields
ωv =ω C ([4, Corollary 2]).
While (1) already settles the asymptotic exponent ωv = ωC, its proof leaves substantial slack
in three orthogonal directions:
1. Model and constant slack (30s vs.4 qns):In [ 4, Section 4.4], the constant 30 = 3 ×5×2
arises from three compounding overcounts: (i) every equality test zj = 0 is turned into a
subtraction, squaring, and addition inside P = P
j z2
j , and every division is split into a
reciprocal plus multiplication ( H≤ 2q + 3r≤ 3s); (ii) the forward–reverse Baur–Strassen
pass is bounded generically by 5 H gates; and (iii) every gate is charged 2 bilinear cross-
terms. As a consequence, (1) charges additions, subtractions, scalar multiplications, and
equality/inequality tests equally with non-scalar multiplications, and yields vacuous lower
boundss≥1 for 2×2, 3×3, and 4×4 matrix verification.
2. Tightness and finite-size quantitative boundaries:How small can the per-gate
constant in a Baur–Strassen dual-number extraction become, and is the resulting constant
provably optimal at the single-gate level? Furthermore, can Chen’s semialgebraic second-
derivative polarization ([ 4, Lemma 3]) be tightened, and what concrete finite- n lower
bounds follow for matrix multiplication and the conditional ωC = 9/4 separation against
Freivalds’ randomized algorithm [5]?
3. White-box PIT geometry and base-field obstructions:In [ 4, Section 6], Chen
shows that dense quadratic identity testing on S = 2Kd input slots runs in SωC/2+o(1)
time and gives a univariate sum-of-squares reduction ([ 4, Proposition 5(ii)]). What is the
exact complexity exponent as a function of the rectangular aspect ratio α = log2K(d), over
which base fields does the sum-of-squares reduction fail, and what is the sharp constant
for complex decision trees ([4, Section 7])?
We resolve all three questions completely in Theorems 1–3, with full constructive Lean 4.36.0
formalization and exact zero-float rational certification.
2 Main Results
Throughout, we follow Chen’s real arithmetic decision-tree model [ 4, Section 2]: on a fixed
accepting leaf O of positive Lebesgue measure for y = T(u, v), the path executes arithmetic gates
in {+,−,×,÷} (together with scalar multiplications by real constants and squaring gates w = u2
distinguished as a special case of multiplication) and equality/inequality branch tests. Denote
by q×, q÷, and qsq the numbers of non-scalar general multiplications ( u·v with neither operand
constant and u̸≡v ), non-scalar divisions (u/v with non-constant denominator v), and non-scalar
squarings (u2) executed along the selected accepting pathO, and setq ns :=q × +q ÷ +q sq. Let
qlin denote the number of additions, subtractions, scalar multiplications, and scalar divisions
(u/c for nonzero constants c), and let req, r̸= be the numbers of equality and strict inequality
tests, so total path length iss=q ns +q lin +r eq +r ̸=.
For a single non-scalar multiplication or division gate in the Baur–Strassen forward–reverse
circuit, define the symmetric 3×3×3 gate tensorG 3 ∈Q 3 ⊗Q 3 ⊗Q 3 by its three 3×3 slices
S1 =


0 0 0
0 0 1
0 1 0

, S 2 =


0 0 1
0 0 0
1 0 0

, S 3 =


0 1 0
1 0 0
0 0 0

,(2)
corresponding to the bilinear map ( x, y) 7→ (x2y3 + x3y2, x1y3 + x3y1, x1y2 + x2y1). For a single
squaring gate, define the 2×2×2 gate tensorG sq ∈Q 2 ⊗Q 2 ⊗Q 2 with slices
S(0)
sq =
0 0
0 1

, S (1)
sq =
0 1
1 0

,(3)
2

--- Page 3 ---
corresponding to (x, y)7→(x 2y2, x1y2 +x 2y1).
Theorem 1(7 .5× Non-Scalar Constant Collapse and Single-Gate Border-Rank Tightness).Let
T : Rp ×R q →R m be a bilinear map verified by a deterministic real arithmetic decision tree
whose full-dimensional accepting branch O executes q× general non-scalar multiplications, q÷
non-scalar divisions, qsq non-scalar squarings, qlin linear operations, and req + r̸= branch tests
(s=q ns +q lin +r eq +r ̸=).
(a) Sharp Ostrowski–Strassen non-scalar border-rank bound:Every perturbed implicit
derivative mapD 2
uvhwk (xk)in Chen [4, Section 4.4] satisfies the exact real rank bound
rankR
 
D2
uvhwk (xk)

≤4(q × +q ÷) + 3qsq,(4)
and passing to the double limit ( k→ ∞with diagonal border approximations εk → 0on
each squaring gate) yields
rankC(T)≤rank R(T)≤4(q × +q ÷) + 2qsq ≤4q ns ≤4s.(5)
In particular, all additions, subtractions, scalar multiplications, equality tests, and strict
inequality tests contribute zero to (5), strictly improving Chen’s bound30 s ([4, Theorem 1])
by a factor of at least15 /2 = 7 .5× universally whenever s≥ 1(and by15 × on pure
squaring circuits and495/14≈35.36×on a Strassen2×2matrix verifier).
(b) Unconditional single-gate border-rank tightness:Over both C and R, the forward–
reverse gate tensors(2)–(3)satisfy the exact equalities
rankC(G3) = rankR(G3) = rankC(G3) = rankR(G3) = 4,(6)
and over every fieldFwithchar(F)̸= 2,rank F(G3) = 4, while
rankC(Gsq) = rankR(Gsq) = 2<3 = rank C(Gsq) = rankR(Gsq).(7)
Consequently, the per-gate weights4(for multiplication/division) and2(for squaring)
in (5) are unconditionally optimal for every gate-by-gate tensor decomposition of the
Baur–Strassen derivative circuit.
Remark1 (Scope of gate-by-gate tightness).Theorem 1(b) proves that no decomposition acting
independently on each non-scalar gate tensor can reduce the coefficient 4 (for ×,÷) or 2 (for
squaring) even over C and even in border rank. Whether global cross-gate tensor sharing
across an entire forward–reverse DAG can lower the worst-case constant below 4 (analogous to
Strassen’s direct-sum non-additivity phenomenon, while never dropping below 1) remains an
interesting open problem.
Theorem 2(Finite-Size Verification Bounds and Semialgebraic Polarization).
(a) Finite-n deterministic non-scalar verification lower bounds:Every deterministic
real arithmetic decision tree verifying n×n matrix multiplication Mn (resp. rectangular
⟨n, m, p⟩) executes at least
qns(Mn)≥
lrankC(Mn)
4
m
(8)
non-scalar multiplications/divisions/squarings on a full-dimensional accepting branch.
Combining(8)withrank C(M2) = 7[6] andrank C(Mn)≥2n 2 −nfor alln≥2[8] yields
qns(M2)≥2, q ns(M3)≥4, q ns(M4)≥7,
qns(M8)≥30, q ns(Mn)≥
l2n2 −n
4
m
,
3

--- Page 4 ---
improving Chen’s Theorem 1 finite-n bounds by factors of2 × to7 .5×. Moreover, under
the conditional fixed-size border-rank lower bound rankC(Mn) ≥n 9/4 cited in Chen [ 4,
Section 6], our bound qns(Mn) ≥n 9/4/4surpasses the2 n2 non-scalar multiplications
of Chen’s two-trial binary Freivalds test (error ≤ 1/4, [ 4, Section 6]; n2 non-scalar
multiplications per trial since r∈ {0, 1}n makes Br and Cr addition-only) at dimension
n >84 = 4096, versus n >604 = 12,960,000under Chen’s30 s bound (and surpasses a single
binary trial’s n2 non-scalar multiplications at n >44 = 256versus30 4 = 810,000)—an
exact50625/16 = 3164.0625×reduction in crossover dimension.
(b) Symmetric diagonal polarization and exact Lemma 3 Pareto frontier:In Chen [ 4,
Lemma 3], let f : X→R m be a C2 semialgebraic map of bounded complexity on a box X⊂
RN with ∥f∥∞ ≤δ≤ 1. Replacing Chen’s asymmetric formula ∂i∂j = ∂2
(ei+ej )/
√
2 − 1
2 (∂2
i +
∂2
j )by symmetric diagonal polarization along the two unit directionsu ± := (ei ±e j)/
√
2,
∂i∂jf= 1
2

∂2
u+f−∂ 2
u−f

,(9)
halves the pointwise mixed-derivative error constant from2 τ to τ. Parameterizing the
second-derivative threshold asτ=δ θ for anyθ∈(0,1)traces the exact Pareto frontier
|∂i∂jf(x)| ≤δ θ outside a bad set of Lebesgue measureO

δ(1−θ)/2

,(10)
which reduces the direction count per individual pair( i, j)from3to2(and across all
pq mixed pairs uses2 pq directions versus pq + p + q). Equating the error and measure
exponents yields the unique balanced point θ = 1/3(error ≤δ 1/3, measure O(δ1/3)), while
at Chen’s benchmark θ = 1/2the error improves from2
√
δ to
√
δ at the same O(δ1/4)
measure.
Theorem 3(Rectangular Quadratic PIT, Field Obstructions, and Complex Trees).
(a) Unique square peak and strict rectangular speedup in dense quadratic PIT:For
Chen’s dense quadratic identity test [ 4, Section 6] on K pairs of d-variable linear forms
(c := 2K, total input slots S = cd), parameterize the aspect ratio by d = cα (α >0, so
S = c1+α). The block-matrix algorithm in [ 4, Section 6] runs in time SE(α)+o(1) with exact
exponent
E(α) =



α+ω C −1
1 +α , α≥1,
1 +α(ω C −1)
1 +α ,0< α≤1.
(11)
Whenever ωC > 2, Chen’s worst-case exponent ωC/2is attaineduniquelyat the square
aspect ratioα= 1(d= 2K), and for everyα̸= 1there is a strict rectangular speedup
ωC
2 −E(α) = |α−1|(ω C −2)
2(1 +α) >0.(12)
(b) Exact failure of sum-of-squares reductions over every Fp and C:Over every finite
prime field Fp (p prime) and over C, Chen’s univariate sum-of-squares PIT reduction
Q(t) = P
i((A(Bv) −Cv )i)2 ([4, Proposition 5(ii)]) fails: there exists a nonzero residual
matrix R = AB−C̸ = 0of size n×n (n = 2over C, F2, and all primes p≡ 1 ( mod 4);
n = 3over all primes p≡ 3 ( mod 4)) for which Q(t) ≡ 0identically as a formal polynomial.
By the same isotropic vectors, Chen’s d > cGram reduction RJR⊤ = 0 ⇐⇒HJH = 0
(H = R⊤R, [4, Section 6]) also fails over every Fp and over C (requiring the Hermitian
Gram matrixR ∗RoverC).
4

--- Page 5 ---
(c) Sharp complex-to-real pair simulation and direct complex constants:Simulating
an arbitrary complex equality-test decision tree ([ 4, Section 7]) by real pairs via Gauss’s
3-multiplication identity,
(a+bi)(c+di) = (ac−bd) +
 
(a+b)(c+d)−ac−bd

i,
and the3-squaring identity( a+bi)2 = (a2−b2)+
 
(a+b)2−a2−b2
i, yields the unconditional
complex border-rank bound
rankC(T)≤12q C
× + 6qC
sq + 24qC
÷,(13)
improving naive4-multiplication real-pair simulation (16 qC
×) by25%while charging zero
for all complex linear operations and equality tests. Furthermore, along any sequence
of regular values wk → 0of the holomorphic map F = ∇y
Pz2
j admitting uniformly
converging holomorphic local brancheshwk →T (for which D2hwk →T by Cauchy’s integral
formula), direct complex Baur–Strassen Walsh–Hadamard extraction yields rankC(T) ≤
4(qC
× + qC
÷) + 2qC
sq; whenever already rankC DyZ = m at y = T(x0), a generic constant
projection F = AZ requires only the forward pass and yields rankC(T) ≤ 2(qC
× + qC
÷) + qC
sq.
3 Proof of Theorem 1: Non-Scalar Collapse and Single-Gate
Tightness
3.1 Test-Free Reverse Mode and the Single-Gate TensorG 3
Following Chen [4, Sections 4.1–4.4], on the full-dimensional accepting branch O the verifier
tests equality polynomials/rational functions z1(x, y) = ··· = zr(x, y) = 0 and strict inequalities
gℓ(x, y) > 0. Setting P(x, y) = Pr
j=1 zj(x, y)2 and F(x, y) = ∇yP(x, y), for each selected
perturbation wk → 0 and point xk ∈int (X), h = hwk satisfies F(x, h(x)) = wk locally with
invertible Jacobian J = DyF(xk, h(xk)). For tangent directions a = (U, 0) and b = (0, V) with
L=Dh(x k), differentiating twice yields
D2h(xk)[a, b] =−J −1 Fαβ(U, V),(14)
where Fαβ(U, V) is the αβ-coefficient of F evaluated in the truncated dual-number ring R :=
R[α, β]/(α2, β2) at the affine input
(x, y) =
 
xk, h(xk)

+α(a, La) +β(b, Lb).
Every intermediate wire u carries a tuple u = u0 + u1α + u2β + u3αβ∈ R, where u0 ∈R is fixed
(independent ofU, V),u 1 is a fixed linear form inU, andu 2 is a fixed linear form inV.
Zero cost for tests and linear gates.Because F = ∇y
Pr
j=1 z2
j = 2 Pr
j=1 zj∇yzj, we donot
append squaring and summation gates to compute P before running reverse mode. Instead, we
run reverse-mode automatic differentiation directly on the forward DAG computing ( z1, . . . , zr)
by initializing the adjoints as
¯zj += 2z j (j= 1, . . . , r).(15)
In R, ¯zj,3 += 2zj,3 is purely linear in zj,3 and introduceszerobilinear products of U-forms
and V -forms. Strict inequality gates do not enter P on the open cell O, and every addition,
subtraction, or scalar multiplication w = λu + µv satisfies w3 = λu3 + µv3 and adjoint updates
¯u3 +=λ¯w3, ¯v3 +=µ¯w3, all purely linear in theαβ-slots (certified incert12).
5

--- Page 6 ---
General multiplication gate (w = u·v ).In the forward pass, w3 = (u0v3 + v0u3) + (u1v2 +
u2v1). In the reverse pass, ¯u+= ¯wvand ¯v+= ¯wu, giving
w3 =u 0v3 +v 0u3 + (u1v2 +u 2v1)| {z }
O1
,
¯u3 += ¯w0v3 +v 0 ¯w3 + ( ¯w1v2 + ¯w2v1)| {z }
O2
,
¯v3 += ¯w0u3 +u 0 ¯w3 + ( ¯w1u2 + ¯w2u1)| {z }
O3
.
The terms u0v3, v0u3,¯w0v3, v0 ¯w3,¯w0u3, u0 ¯w3 are fixed scalar multiples of existing αβ-slots;
hence theonlybilinear ( U, V) injection of the entire forward–reverse multiplication gate is
(O1, O2, O3) =G 3(x, y) atx= ( ¯w1, u1, v1) andy= ( ¯w2, u2, v2).
Unsplit division gate ( w = u/v, v0 ̸= 0).Differentiating the implicit identity wv = u in R
gives
w3 =v −1
0
 
u3 −w 0v3 −(w 1v2 +w 2v1)

.
In the reverse pass, set λ := ¯w/v(i.e., λv = ¯w), so ¯u+= λ and ¯v+= −λw. Expanding λv = ¯w
and−λwinRyields
λ3 =v −1
0
 
¯w3 −λ 0v3 −(λ 1v2 +λ 2v1)

,¯u 3 +=λ 3,
¯v3 +=−
 
λ0w3 +w 0λ3 + (λ1w2 +λ 2w1)

.
Setting x = (λ1, w1, v1) and y = (λ2, w2, v2), the three bilinear cross-terms ( w1v2 + w2v1, λ1v2 +
λ2v1, λ1w2 + λ2w1) areidenticalto G3(x, y) (verified end-to-end on a division verifier in cert04
and Lean Theorem 9)!
Exact4-term Walsh–Hadamard decomposition of G3.Define the four rank-1 products
P1 = (x1 +x 2 +x 3)(y1 +y 2 +y 3), P 2 = (x1 +x 2 −x 3)(y1 +y 2 −y 3),
P3 = (x1 −x 2 +x 3)(y1 −y 2 +y 3), P 4 = (−x1 +x 2 +x 3)(−y1 +y 2 +y 3).
Expanding directly (verified over Z in Lean Theorems 1–3 and over Q in cert01) yields the
exact identities
O1 = 1
4 (P1 −P 2 −P 3 +P 4), O 2 = 1
4 (P1 −P 2 +P 3 −P 4), O 3 = 1
4 (P1 +P 2 −P 3 −P 4).(16)
Thus every general multiplication gate and every unsplit division gate injects at most 4 rank-1
bilinear products into the linearαβ-propagation network.
Squaring gate (w = u2) and double-limit diagonalization.For w = u2, w3 = 2u0u3 +
2u1u2 and ¯u3 += 2( ¯w0u3 +u0 ¯w3 + ¯w1u2 + ¯w2u1), injecting Gsq(( ¯w1, u1), ( ¯w2, u2)) = (u1u2,¯w1u2 +
¯w2u1). Since Gsq has exact rank 3 (via u1u2, ¯w1u2, ¯w2u1), the linear dependence of D2h(xk) =
−J−1Fαβ on all gate injections immediately proves (4): rankR(D2hwk (xk)) ≤ 4(q× + q÷) + 3qsq.
To reach the border-rank bound (5), note that for everyε >0, the rank-2 bilinear map
Gsq,ε(x, y) =

(x2 +εx 1)(y2 +εy 1), ε−1
(x2 +εx 1)(y2 +εy 1)−x 2y2

(17)
converges to Gsq(x, y) as ε→ 0 with exact entrywise error O(ε) (Lean Theorem 8, cert03,
cert13). For each fixed k, the map sending the tuple of all gate injections to −J−1
k F(k)
αβ is linear
and hence continuous; replacing every squaring gate’s Gsq by Gsq,ε produces a bilinear map
B(k,ε) of exact real rank ≤ 4(q× + q÷) + 2qsq satisfying limε→0 B(k,ε) = D2hwk (xk). Choosing
εk > 0 so that ∥B(k,εk) −D 2hwk (xk)∥< 1/k yields B(k,εk) →T as k→ ∞, proving rankR(T) ≤
4(q× + q÷) + 2qsq ≤ 4qns ≤ 4s. The 7 .5× floor and 15 × squaring bound follow identically (Lean
Theorems 4–5,cert05–cert06).
6

--- Page 7 ---
Table 1: Exact comparison of Chen’s 30 s bound ([4, Theorem 1]) against our Ostrowski–Strassen
non-scalar bound (5) across representative verifier architectures (cert05–cert06,cert13).
Verifier architectures q ns Chen 30sExact (4) Border (5) Tightening
Pure non-scalar mul/div 100 100 3000 400 400 7.5×(15/2)
Pure squaring circuit 100 100 3000 300 200 15.0×
Strassen 2×2 (7×,22±,4 =) 33 7 990 28 28 35.4×(495/14)
Schoolbook 4×4 (64×,64±,16 =) 144 64 4320 256 256 16.9×(135/8)
Division-heavy (20×,30÷,10sq) 160 60 4800 230 220 21.8×(240/11)
Sign-test heavy (25×,5sq,50test) 100 30 3000 115 110 27.3×(300/11)
Squaring-polarized (2sq,6lin/test) 8 2 240 6 4 60.0×
3.2 Proof of Theorem 1(b): Single-Gate Border-Rank Tightness
Proof of(6)–(7). The upper bound rankR(G3) ≤ 4 is given by (16). For the lower bound over
C, observe first that G3 is 1-concise: stacking its three 3 × 3 slices (2) gives a 3 × 9 flattening
of rank 3. Take the slice combination A := S1 + S2 + S3 = J3 −I 3. Since det(A) = 2 ̸= 0, A
is invertible with A−1 = 1
2 (J3 − 2I3). Computing Mk := A−1Sk (k = 1, 2) gives the Strassen
commutator
[A−1S1, A−1S2] = 1
2


0−1 1
1 0−1
−1 1 0

,
whose top-left 2 × 2 minor equals 1 /4 ̸= 0, so rank([A−1S1, A−1S2]) = 2 (verified identically
in cert02 and Lean Theorem 7). By Strassen’s commutator equation [ 9, Theorem 2.4] (see
also [7, Proposition 3.8.1.1]), any tensor T∈C m ⊗C m ⊗C p with an invertible slice combination
Asatisfies
rankC(T)≥m+ 1
2 rank
 
[A−1Si, A−1Sj]

.
Applying this to G3 (m = 3) yields rankC(G3) ≥ 3 + 2/2 = 4. Combining with (16) proves
rankC(G3) = rankR(G3) = rankC(G3) = rankR(G3) = 4. Over any field F with char(F) ̸= 2, the
principal 2 ×2 minors of any nonzero slice combination aS1 + bS2 + cS3 are −c2,−b 2,−a 2, which
vanish simultaneously iff a = b = c = 0; hence spanF{S1, S2, S3} contains no rank-1 matrices
(Lean Theorem 6, cert14), so any 3 rank-1 matrices spanning a 3-dimensional space containing
span{S1, S2, S3}would coincide with it, a contradiction; thus rank F(G3) = 4.
For Gsq, the 2 × 4 flattening has rank 2, so rankC(Gsq) ≥ 2, matching (17). Conversely,
det(aS(0)
sq + bS(1)
sq ) = −b2 vanishes iff b = 0, so the 2-dimensional slice space span{S(0)
sq , S(1)
sq }
contains only a single rank-1 line ( span{S(0)
sq }) and cannot be spanned by 2 rank-1 matrices;
hence rankC(Gsq) = rankR(Gsq) = 3 (cert03).
4 Proof of Theorem 2: Finite-Size Lower Bounds and Polariza-
tion Frontier
Proof of Theorem 2. For part (a), Theorem 1(a) gives 4qns(Mn) ≥rank C(Mn), which for integers
qns is equivalent to qns(Mn) ≥ ⌈rankC(Mn)/4⌉ = ⌊(rankC(Mn) + 3)/4⌋ (Lean Theorem 12). Sub-
stituting Landsberg’s exact value rankC(M2) = 7 [6] and the Landsberg–Ottaviani lower bound
rankC(Mn) ≥ 2n2 −n for all n≥ 2 [8] yields the exact checkpoints in Table 2 (Lean Theorems 13
and 19, cert07, cert15). Under the conditional fixed-size lower bound rankC(Mn) ≥n 9/4 cited
in [4, Section 6], our non-scalar lower bound n9/4/4 exceeds the 2n2 non-scalar multiplications of
Chen’s two-trial binary Freivalds test (r∈ {0, 1}n makes Br and Cr addition-only, so each trial
costs n2 non-scalar multiplications for A(Br), and two trials cost 2 n2 for error ≤ 1/4) precisely
when n1/4 > 8, i.e., n >84 = 4096, whereas n9/4/30 > 2n2 requires n >604 = 12,960,000 (and
7

--- Page 8 ---
Figure 1:(a)Bound tightening factor 30 s/(4(q× + q÷) + 2qsq) over Chen [4, Theorem 1] across
six verifier architectures (cert06), showing the universal 7 .5× floor and up to 35 .4× collapse on
a Strassen 2 × 2 verifier.(b)Finite-size deterministic matrix-multiplication verification lower
bounds⌈rank C(Mn)/4⌉versus Chen’s⌈rank C(Mn)/30⌉(cert07).
Table 2: Concrete finite-size deterministic matrix-multiplication verification lower bounds
(cert07, cert15) comparing our Theorem 2(a) bound qns ≥ ⌈rankC/4⌉ with Chen’s s≥
⌈rankC/30⌉.
Matrix tensor rank C LB Source ChensLB Ourq ns LB Exact gain
M2 =⟨2,2,2⟩7 Landsberg [6] 1 2 2×
⟨2,3,2⟩6 Flattening max(nm, mp, np) 1 2 2×
M3 =⟨3,3,3⟩15 Landsberg–Ottaviani [8] 1 4 4×
⟨4,2,4⟩16 Flattening max(nm, mp, np) 1 4 4×
M4 =⟨4,4,4⟩28 Landsberg–Ottaviani [8] 1 7 7×
M8 =⟨8,8,8⟩120 Landsberg–Ottaviani [8] 4 30 7.5×(15/2)
M16 =⟨16,16,16⟩496 Landsberg–Ottaviani [8] 17 124 7.29×(124/17)
M64 =⟨64,64,64⟩8128 Landsberg–Ottaviani [8] 271 2032 7.50×(2032/271)
against a single binary trial’s n2 non-scalar multiplications, n >44 = 256 versus 304 = 810,000);
in all cases the dimension ratio is (15/2) 4 = 50625/16 = 3164.0625 (cert16).
For part (b), let u± = (ei ±ej)/
√
2 be unit vectors. Expanding ∂2
u±f = 1
2 (∂2
i f± 2∂i∂jf +∂2
j f)
and subtracting gives (9). On any line segment [ a, b] along a unit direction u where ϕ(t) :=
fr(x+tu) satisfies |ϕ| ≤δ≤1 and ϕ′′ > τ, Taylor’s theorem at the midpoint m = (a+b)/2 yields
ϕ(a)+ ϕ(b)−2ϕ(m) ≥ 1
4 τ(b−a )2, whence τ(b−a )2 ≤ 16δ (Lean Theorem 11) and b−a≤ 4
p
δ/τ .
Integrating over parallel lines for each fixed semialgebraic complexity bound (bounding the
number of monotone intervals by a constant depending only on the path complexity, as in [ 4,
Lemma 3]) and taking the union over the two unit directions u+, u− gives |∂2
u±fr| ≤τoutside a
bad set of measure O(
p
δ/τ ) (or O(δ/τ +
p
δ/τ ) if first derivatives are controlled simultaneously).
By (9), |∂i∂jfr| ≤1
2 (|∂2
u+fr| + |∂2
u−fr|) ≤τ (Lean Theorem 10, cert08), strictly halving Chen’s
2τ. Setting τ = δθ (θ∈ (0, 1)) gives δ/τ = δ1−θ = o(δ(1−θ)/2) as δ→ 0, yielding (10), whose
unique equal-exponent balance point satisfies θ = (1 −θ )/2 ⇐⇒θ = 1/3 while θ = 1/2 matches
Chen’sO(δ 1/4) measure with error≤
√
δ.
8

--- Page 9 ---
5 Proof of Theorem 3: Rectangular PIT, Field Obstructions,
and Complex Trees
Proof of Theorem 3. For part (a), let c = 2 K and d = cα, so S = cd = c1+α. In Chen [ 4,
Section 6], when d≥c (α≥ 1) the algorithm forms H = R⊤R∈R c×c in ⌈d/c⌉ square blocks
of size c and checks HJH = 0, taking ( d/c) cωC+o(1) = cα+ωC−1+o(1) = S(α+ωC−1)/(1+α)+o(1)
operations. When d≤c (0 < α≤ 1), blocking ( RJ)R⊤ along c takes ( c/d) dωC+o(1) =
c1+α(ωC−1)+o(1) = S(1+α(ωC−1))/(1+α)+o(1) operations, proving (11). Direct algebraic subtraction
yields
ωC
2 −E(α) =



(α−1)(ω C −2)
2(1 +α) , α≥1,
(1−α)(ω C −2)
2(1 +α) ,0< α≤1,
which equals (12) and is strictly positive iff α̸ = 1 and ωC > 2 (Lean Theorem 14, cert09,
Figure 2(a)).
For part (b), consider the univariate polynomial Q(t) = Pn
i=1((Rv(t))i)2 from Chen [ 4,
Proposition 5(ii)], where R = AB−C and v(t) = (1, t, . . . , tn−1)⊤. Choose R to have nonzero
first column u∈F n \ {0} and all remaining columns zero (realizable as AB−C by taking
A= 0, B= 0, C=−R). Then (Rv(t)) i =u i is constant, soQ(t) = Pn
i=1 u2
i ∈F[t].
OverC:u= (1, i) ⊤ satisfies 12 +i 2 = 0 (n= 2, Lean Theorem 17).
OverF 2:u= (1,1) ⊤ satisfies 12 + 12 = 0 (n= 2, Lean Theorem 15).
 Over any odd prime field Fp (p = 2k + 1): the two subsets {a2 : a∈F p} and {−1 −b 2 : b∈
Fp} each have cardinality k + 1. Since (k + 1) + (k + 1) > 2k + 1 = |Fp| (Lean Theorem 16),
by pigeonhole there exist a, b∈Fp with a2 + b2 + 1 ≡ 0 ( modp ) (explicitly certified for
all 16 primes p≤ 53 in cert10 and Lean Theorem 20). Setting u = (a, b,1)⊤ (n = 3, or
n= 2 whenp≡1 (mod 4) sob= 0 works) givesu̸= 0 andQ(t)≡0.
Finally, for Chen’s d > cGram reduction H = R⊤R ([4, Section 6]), taking R∈F d×2 with both
columns equal to ( u, 0, . . . ,0)⊤ gives H = R⊤R = 0 (so HJH = 0) while RJR⊤ = 2uu⊤ ̸= 0
over C and every odd prime field Fp; over F2, taking R∈F 4×2
2 with columns u1 = (1, 1, 0, 0)⊤
and u2 = (0, 0, 1, 1)⊤ gives H = R⊤R = 0 (hence HJH = 0) while RJR⊤ = u1u⊤
2 + u2u⊤
1 ̸= 0.
Over C, replacing R⊤R by the Hermitian Gram matrix H = R∗R restores ker(H) = kerR (so
RJR⊤ = 0 ⇐⇒HJH ⊤ = 0, i.e., HJ H = 0), whereas over Fp no positive-definite inner product
exists.
For part (c), represent each complex gate z = a+bi by the real pair (a, b). Complex additions,
subtractions, scalar multiplications, and equality tests ( a = 0, b= 0) translate exclusively into
real linear operations and real equality tests, which contribute 0 to Theorem 1(a). By Gauss’s
identity (Lean Theorem 18, cert11), each complex multiplication ( a + bi)(c + di) uses 3 real
non-scalar multiplications (ac, bd, (a + b)(c + d)), contributing 4 × 3 = 12 terms. Each complex
squaring (a + bi)2 = (a2 −b 2) + ((a + b)2 −a 2 −b 2)i uses 3 real squarings, contributing 2 × 3 = 6
border-rank terms. Each complex division ( a + bi)/(c + di) = ((ac + bd) + (bc−ad )i)/(c2 + d2)
uses 3 real multiplications (Gauss on (a+bi)(c−di )), 2 real squarings (c2, d2), and 2 real divisions
(dividing real and imaginary parts by c2 + d2), contributing 4(3) + 2(2) + 4(2) = 24 border-rank
terms, proving (13). Finally, when the complex equality system Z(x, y) = 0 admits a holomorphic
local regular-value map F = ∇y
Pz2
j with invertible DyF over C, applying the exact proof
of Theorem 1(a) over C[α, β]/(α2, β2) yields 4( qC
× + qC
÷) + 2qC
sq; if moreover rankC DyZ = m,
choosing a constant matrixA∈C m×r withA·D yZinvertible makesF=AZrequire only the
forward pass, where each multiplication/division injects a single cross-term u1v2 + u2v1 of rank
2 and each squaring injectsu 1u2 of rank 1, giving rank C(T)≤2(q C
× +q C
÷) +q C
sq.
9

--- Page 10 ---
Figure 2:(a)Dense quadratic PIT complexity exponent E(α) ((11), cert09) versus aspect
ratio α = log2K(d), demonstrating that Chen’s worst-case SωC/2 is attained uniquely at the
square aspect α = 1.(b)Exact Lemma 3 Pareto frontier (10) (cert08), showing the 2 ×
mixed-derivative error reduction from symmetric diagonal polarization.
6 Formal Verification and Reproducibility
Every algebraic identity, border-rank lower bound, dual-number circuit execution, and finite-size
table in this paper is independently certified by three zero-trust artifacts:
1. Constructive Lean 4.36.0 proof suite( lean/MatrixVerificationSharpConstant.
lean): 20 machine-checked theorems compiling under lean-DwarningAsError=true with
zero external dependencies, zero sorry, zero Classical.choice, and zero custom axioms,
covering the Walsh–Hadamard identities for G3 (Theorems 1–3), the 7 .5× and 15× non-
scalar bounds (Theorems 4–5), the rank-1 minor obstruction and Strassen commutator
border-rank-4 witness (Theorems 6–7), the Gsq border-rank-2 degeneration (Theorem 8),
implicit division cross-terms (Theorem 9), symmetric polarization and midpoint convexity
(Theorems 10–11), finite-n ceiling and Bl¨ aser/Landsberg–Ottaviani bounds (Theorems 12–
13, 19), rectangular PIT strictness (Theorem 14), characteristic-2, odd-prime pigeonhole,
and complex SoS failures (Theorems 15–17, 20), and Gauss’s 3-multiplication identity
(Theorem 18).
2. AST-audited zero-float rational verifier( verification/ script verify matrix
verification.py): Pure int/fractions.Fraction script generating 16 SHA-256-sealed
JSON certificates (cert01–cert16), including end-to-end exact dual-number executions
on a division-based verifier ( cert04), a Strassen 2 × 2 matrix verifier ( cert05), and a
squaring-polarized verifier (cert13).
3. Adversarial test suite( tests/test adversarial.py): 56 automated pytest checks
auditing zero-float AST compliance, SHA-256 manifest integrity, every certificate equation,
and Lean 4 axiom purity.
AI Disclosure.Google Antigravity assisted with the Walsh–Hadamard tensor decomposition,
Strassen commutator checks, exact dual-number rational verification, Lean 4 formalization, and
manuscript drafting. All mathematical proofs, certificates, and claims were audited and verified
by Lluis Eriksson.
10

--- Page 11 ---
References
[1] W. Baur and V. Strassen, “The complexity of partial derivatives,”Theoretical Computer
Science, vol. 22, no. 3, pp. 317–330, 1983.
[2] D. Bini, “Relations between exact and approximate bilinear algorithms. Applications,”
Calcolo, vol. 17, no. 1, pp. 87–97, 1980.
[3] P. B¨ urgisser, M. Karpinski, and T. Lickteig, “On randomized algebraic test complexity,”
Technical Report 8580-CS, University of Bonn, 1992.
[4] Chen Xiangle, “Deterministic Verification and Computation of Real Matrix Products Have
the Same Arithmetic Exponent,”arXiv:2611.34814v1, November 2026.
[5] R. Freivalds, “Fast probabilistic algorithms,” inMathematical Foundations of Computer
Science (MFCS 1979), LNCS 74, Springer, pp. 57–69, 1979.
[6] J. M. Landsberg, “The border rank of the multiplication of 2 ×2 matrices is seven,”Journal
of the American Mathematical Society, vol. 19, no. 2, pp. 447–459, 2006.
[7] J. M. Landsberg,Tensors: Geometry and Applications, Graduate Studies in Mathematics,
vol. 128, American Mathematical Society, 2012.
[8] J. M. Landsberg and G. Ottaviani, “New lower bounds for the border rank of matrix
multiplication,”Theory of Computing, vol. 11, no. 11, pp. 285–298, 2015.
[9] V. Strassen, “Rank and optimal computation of generic tensors,”Linear Algebra and its
Applications, vol. 52–53, pp. 645–685, 1983.
11
