# Referee report: ARR-2026-3RH54K4NC58MRSX3, version v1

**Title:** *An exact relaxation optimum in a one-parameter family of four quantum measurement bases*
**Author:** Lluis Eriksson (manuscript declares substantial OpenAI Codex assistance; author operates AIRR)
**Version identifier:** `arr:version:5e3ad684-c532-4912-81ee-e14c628d57b4`

---

## 0. Identification, configuration and controls

| Item | Value |
|---|---|
| Canonical PDF SHA-256 (computed locally, matches request) | `dc55322c19116a9a51ac89ce359717a782f126bcb1310960b99301ed0d09c313` |
| paper.tex SHA-256 | `0fa91eb91c805573d176d14178ee482c844865ef04495885818688e9190f79dc` |
| verify.py SHA-256 (supplemental, **not** in published v1 per operator) | `a1a367b22897af98d830aa6d1872e976f3ef9282326804eceb820675a29bd52b` |
| requirements.txt SHA-256 (supplemental, **not** in published v1 per operator) | `25f9f1fb1988b230147a1d3092d34e09c069eb7a6c6d6df46b3973b9f2d36efc` (content: `sympy==1.14.0`) |
| Reviewer provider / model | Anthropic / `claude-opus-5-5` (the model ID is given in the runtime system information) |
| Effort setting | "max", as requested by the operator. I cannot independently confirm the platform's effort setting from inside the session. |
| Independence | `not_involved_in_manuscript` (operator's declaration). I have no record of taking part, but a fresh conversation does not prove statistical independence from the system that helped write the manuscript. |
| Assessment date | 2026-10-11 (local clock offset +02:00; the exact timestamp is in assessment.json) |
| Compute environment | Windows 11; Python 3.12.6; SymPy 1.14.0; NumPy 2.5.1; SciPy 1.18.0; mpmath 1.3.0; pypdf 6.4.0 |

**How the manuscript was read.** I read all 7 pages of `paper.pdf` directly as rendered page images. As a cross-check I extracted the text with pypdf (`outputs/paper_pdf_text.txt`), and it agrees with `paper.tex` in all equations, the table and the references. I read `paper.tex`, `verify.py`, `requirements.txt` and `airr-rubric.txt` in full.

**Controls.** I used only the four scientific inputs, the rubric, the operator's request and scope-addendum files in the assigned directory, and primary literature I obtained myself. I did **not** access the AIRR website: not the permanent version page, and not the self-citation [5]. This was to avoid exposure to any posted assessments. My statements about the v1 release contents therefore rely on the operator's declaration. I did not open parent or sibling directories, platform session logs, memory or other reviews. The original PDF and TeX were not modified (hashes re-checked after the work).

**Session note.** The tool session was interrupted once, during an *optional* exploratory global search (check 4, Section 6.2). On resumption the controller paused further unrestricted searches as out of scope, since the paper explicitly does not claim global optimality. That script had in fact run to completion and written its outputs before the interruption. Its results are reported below as limited exploratory context, unextended, and no grading conclusion depends on them.

---

## 1. Summary of the submission

Four orthonormal bases B0,…,B3 of C⁶ define the channel T = ¼ Σⱼ Eⱼ, where Eⱼ(X) = Σₖ Πⱼₖ X Πⱼₖ. This is the average of nonselective rank-one projective measurements. The generator L = T − id gives the semigroup of a rate-one Poisson process of randomly chosen measurements. The relaxation rate is γ = 1 − λmax(T|H₀), where H₀ is the traceless subspace, and γ = 1 − λmax(G)/4 for the 24×24 Gram matrix G of the traceless projectors vⱼₖ = Πⱼₖ − I/6.

For the one-parameter Raynal–Lü–Englert (RLE) family (canonical basis plus three Hadamard bases, parameter u = sin²θx ∈ [1/4, 1]) the paper claims:

* **Thm 3.1:** the complete Gram spectrum {0⁽⁴⁾, 1⁽⁵⁾, (1−2s)⁽³⁾, (1+s)⁽⁶⁾, (1+2k)⁽²⁾, (1−k)⁽⁴⁾}, with s = (1+4u−8u²)/3 and k = 8u²−10u+3.
* **Thm 4.1:** the maximum rate within the family is 73/100, attained uniquely at u = 7/10.
* **Cor 4.2:** the explicit algebraic construction at u = 7/10 and its channel spectrum.
* **Eqs. (16)–(18), Table 1:** the RLE mean squared distance is not maximized at u = 7/10, and an exact rational pair of parameters shows the two objectives reversed.
* **Prop 5.1:** γ ≤ 2/3 for any mixture of product-vector bases on C²⊗C³, and this ceiling is sharp.
* **Eq. (19):** 73/100 ≤ γ*₄(6) ≤ 3/4.

## 2. Overall assessment

The mathematics is **correct**. I re-derived every main claim independently. In particular, I tested the overlap structure (10)–(11), on which Theorem 3.1 depends, symbolically for **generic u from the original basis matrices**, and did not rely on the paper's ansatz. I also tested it numerically through the 36×36 superoperator, which involves no Gram matrix at all. I found no counterexample and no material objection.

The issues are (i) narrow scope and modest significance, (ii) a sketched and partly insufficient justification of (11), (iii) a 7th-digit numerical typo, and (iv) reproducibility statements that refer to a supplement which, per the operator, was not part of the published v1. **Recommendation: minor revision.**

---

## 3. Claim-by-claim findings

### 3.1 Section 2: framework (eqs. 1–5)

| Claim | Finding |
|---|---|
| e^{t(T−id)} = e^{−t} Σ tⁿTⁿ/n! is CPTP and unital | **Correct.** It is a convex combination of compositions of CPTP unital maps. Numerically, the series agrees with `expm` to 2.2e−16 (check 2). |
| Each Eⱼ is an HS-orthogonal projection; T is self-adjoint and PSD with spectrum in [0,1] | **Correct.** For rank-one Π, ΠXΠ = Tr(ΠX)Π, so Eⱼ = Σₖ \|Πⱼₖ)(Πⱼₖ\|. The Πⱼₖ are HS-orthonormal. |
| γ := 1 − λmax(T\|H₀); γ = 0 if a nonscalar fixed point exists | **Correct.** |
| Decay bound (3) in HS norm, and its sharpness | **Correct.** T preserves H₀, and T\|H₀ is self-adjoint. The top eigenspace contains a Hermitian traceless Y because T preserves Hermiticity, and I/6 + εY is a state. Numerically (u = 7/10): the worst ratio of the left side to the right side over 200 random states and 4 times was 0.980 ≤ 1, and the ratio is exactly 1.000 for the state built from the top eigenoperator (check 2). |
| Frame operator of {vⱼₖ} equals 4T\|H₀; nonzero spectra of the frame operator and G coincide; γ = 1 − λmax(G)/4 | **Correct.** One step is implicit. For X ∈ H₀, Tr(ΠⱼₖX) = Tr(vⱼₖX), and the I/6 component drops out because Σₖ vⱼₖ = 0. Numerically, γ from G and γ from the superoperator agree to 1.1e−15 on 3001 u-values (check 2). |

### 3.2 Section 3: identification with RLE, parametrization, overlap blocks (6)–(11)

* **Matrices (6)–(8) = RLE.** I compared them with the downloaded RLE paper ([arXiv:1103.1025](https://arxiv.org/abs/1103.1025), local copy `literature/rle_1103.1025.pdf`, SHA-256 `dea60071…228c`). RLE Eqs. (5)–(6) define M₁, M₂, M₃ with X = diag(x*, x), F₂, Z and T = [[1, ωt²], [1, −ωt²]]. The manuscript's U₁, U₂, U₃ are identical, with H ≡ RLE's T. RLE Eq. (7), equivalently (B33), is cos(θt + π/3) = cos(2θx)/sin θx, exactly as quoted. The two-parameter family genuinely has two free phases: RLE Fig. 2 shows the distance varying over (θx, θt), and relation (7) cuts out the single-parameter curves that contain the distance maximizer. The manuscript's description of RLE is accurate.
* **Branch (9).** |q| ≤ 1 ⇔ (4u−1)(u−1) ≤ 0 ⇔ 1/4 ≤ u ≤ 1, which is correct. With x = e^{iθx}, (9) chooses cos θx ≥ 0, u = sin²θx and sin(θt + π/3) ≥ 0. The branch contains RLE's marked distance maximizer (θx, θt) = (0.9852, 1.0094): there q = −0.467 with positive sine.
* **Derivation of A (text after (11)).** Correct: (1+√u q)² + u(1−q²) = 1 + u + 2√u q = 3(1−u), so |α|²/36 = (4/3)(1−u)².
* **Entries B and C (gap in exposition).** The paper asserts the remaining entries "by direct multiplication" and says they follow "either by the same multiplication or by row normalization." **Row normalization alone is insufficient.** It gives only that the four remaining entries of a row sum to 1 − A − B = 4C, not that each equals C. The claim itself is true:
  * RLE's published coefficients (Eqs. (8)–(12)) under relation (7) give |β|² = 36(1−2u)² and |γ|² = |δ|² = |ε|² = 12(1−u)(4u−1), which is 36C. I derived these by hand from RLE Eq. (11).
  * My symbolic computation from the matrices settles the point independently (next bullet).
* **Independent generic-u verification (check 1, exact SymPy).** I used p = √u, c = √(1−u), r = √(4u−1), so that √(1−q²) = c·r/p, and reduced modulo c² = 1 − p² and r² = 4p² − 1. From the **original** matrices (6)–(9), for all u ∈ [1/4, 1]:
  * U₁, U₂, U₃ are unitary;
  * |entries|² = 1/6, so P₀ⱼ = J/6;
  * P₁₂, P₂₃ and P₃₁ equal the ansatz (11) exactly, entrywise.

  The identities A + B + 4C = 1, s = A − B and k = 1 − 6C = A + B − 2C also hold. All passed, in 43 s.
* **Numerical confirmation (check 2).** Over 3001 grid points in [1/4, 1], endpoints included, max |P_direct − ansatz| = 1.4e−15. As a negative control, swapping A ↔ B gives mismatches of size |A − B| = |s|. This vanishes only at u = (1+√3)/4 ≈ 0.683, where s = 0, and is ≥ 2.9e−5 at every grid point in 0.3 < u < 0.95. So the test is not vacuous.

### 3.3 Theorem 3.1 (complete Gram spectrum): **correct**

My reconstruction, which agrees with the paper's proof and makes its implicit steps explicit:

1. The canonical basis decouples because P₀ⱼ = J/6. Its block Q = I − J/6 contributes 0⁽¹⁾ and 1⁽⁵⁾.
2. Index the six coordinates of bases 1–3 as C³ (block a) ⊗ C² (position σ). With the cyclic shift R:
   * P₁₂ = I₃⊗D + (J₃−I₃)⊗O;
   * P₂₃ = R⊗D + (J₃−R)⊗O;
   * P₃₁ = R²⊗D̃ + (J₃−R²)⊗O.

   Every 2×2 sub-block, and hence every transposed block, commutes with the swap. So C³⊗e₊ and C³⊗e₋ are invariant; the paper uses this tacitly.
3. **e₋ sector.** O → 0, D → s, D̃ → −s and J₆/6 → 0. The 9×9 block is [[I, sI, −sR], [sI, I, sR], [−sR², sR², I]]. Conjugating by W = diag(I, I, R²) gives N_s ⊗ I₃ with N_s = [[1, s, −s], [s, 1, s], [−s, s, 1]]. Its characteristic polynomial is (λ−1−s)²(λ−1+2s). Eigenvectors are (n₁f, n₂f, n₃R²f)⊗e₋, with n = (1, −1, 1) for 1 − 2s and n ∈ span{(1,1,0), (0,1,1)} for 1 + s. This gives (1−2s)⁽³⁾ and (1+s)⁽⁶⁾.
4. **e₊ sector.** The all-ones vector of each basis lies in ker G, because P is doubly stochastic and Σₖ vⱼₖ = 0: three zeros. On 1₃^⊥, the blocks minus J₆/6 act as kI, kR and kR², and k = A + B − 2C. The same conjugation gives K_k = [[1, k, k], [k, 1, k], [k, k, 1]] ⊗ I₂, hence (1+2k)⁽²⁾ and (1−k)⁽⁴⁾.
5. Dimension count: 6 + 9 + 3 + 6 = 24. All values are ≥ 0, as G ⪰ 0 requires: s ∈ [−1, 1/2] and k ∈ [−1/8, 1] on [1/4, 1]. The formula (14) follows because max{−2s, s} ≥ 0 and max{2k, −k} ≥ 0.

**Verification.**
* The author's verifier confirms the characteristic polynomial over Q[u] for the ansatz.
* Combined with check 1, this certifies Thm 3.1 for the original matrices.
* Directly, the 35-point spectrum of the superoperator T|H₀ matches the theorem to 1.6e−15 on 3001 u-values (check 2).

**Endpoints (check 2), not discussed in the paper.**
* **u = 1/4:** γ = 1/4; channel spectrum {0⁽²²⁾, ¼⁽⁵⁾, ⅜⁽⁶⁾, ¾⁽²⁾}.
* **u = 1:** γ = 1/4; spectrum {0⁽²⁵⁾, ¼⁽⁵⁾, ¾⁽⁵⁾}. Here bases 1, 2 and 3 **coincide as ray sets**, so the "four bases" degenerate to two distinct bases. This is RLE's distance-minimum point (θx, θt) = (π/2, 2π/3); RLE p. 6 and Eq. (23).

The formula remains valid there.

**Other branches (check 2).** I also tested the other branches of RLE relation (7): both signs of cos θx, both signs of sin(θt + π/3), and the sin θx < 0 loop, with u = sin²θx. All give exactly the spectrum of Theorem 3.1, with maximum deviation 1.3e−15. The theorem therefore covers RLE's whole one-parameter solution set, not only branch (9). This supports the paper's remark that equivalent branches are "not needed".

### 3.4 Theorem 4.1 (sharp subfamily optimum): **correct**

The three-interval proof is valid:
* **On [1/4, 3/5]:** s′ = (4/3)(1−4u) ≤ 0 and s(3/5) = 13/75 > 2/25.
* **On [3/5, 7/10]:** −k − 2/25 = −8(u − 11/20)(u − 7/10) ≥ 0.
* **On [7/10, 1]:** −2s − 2/25 = (16/3)(u − 7/10)(u + 1/5) ≥ 0.

Equality holds only at 7/10, where s = −1/25, k = −2/25 and γ = 1 − (27/25)/4 = 73/100.

**Independent exact check (check 5).** I did not reuse the paper's argument. Instead I computed the exact upper envelope h(u) = max{0, −2s, s, 2k, −k} on [1/4, 1]. The breakpoints are 4/7 ± 3√2/28, 1/2, 5/8, (1+√3)/4, 7/10 and 3/4, with active pieces 2k, s, s, −k, −k, −2s, −2s, −2s. The global minimum of h is 2/25, touched only at u = 7/10, by the −k and −2s pieces.

**Direct numerical check (check 2).** On the original matrices, the grid argmax is u = 0.7000 with γ = 0.7300000000. A bounded scalar optimization gives u* = 0.69999999615 with γ = 0.72999999885.

### 3.5 Corollary 4.2: **correct**

* x = (√30 + i√70)/10, q = −2√70/35 and e^{−iπ/3} = (1 − i√3)/2 agree with (9) at u = 7/10.
* (A, B, C) = (3/25, 4/25, 9/50).
* The channel spectrum on H₀ is {0⁽¹⁵⁾, (21/100)⁽²⁾, (24/100)⁽⁶⁾, (1/4)⁽⁵⁾, (27/100)⁽³⁺⁴⁼⁷⁾}, with trace 5 = 24·(5/6)/4. Rank 20 and nullity 15 are confirmed.

Evidence:
* The author's verifier computes the exact Gram eigenvalues from the algebraic bases: (25z − 27)⁷(25z − 24)⁶(25z − 21)², times z⁴(z − 1)⁵.
* My check 5 reproduces the merged multiplicities.
* Check 2 confirms them numerically through the superoperator.

### 3.6 Distance comparison, eqs. (16)–(18), Table 1 and the RLE maximizer: **correct, except one digit**

* (16) is RLE's ASD for k = 4 and d = 6 (RLE Eqs. (2)–(3)).
* (17) follows from the defect 6(A² + B² + 4C²) − 1 (check 5).
* As an independent cross-validation, RLE's published polynomial D₁₂² = (8/45)[5 − P(p, q)] (Eqs. (17)–(18)), with q = (1 − 2p²)/p, equals the manuscript's A, B, C-based D₁₂² identically (check 5). My matrices also reproduce RLE (17)–(18) to 1.7e−15 at 300 random points of the *two-parameter* family (check 3).
* D̄²(7/10) = 6239/6250 and dD̄²/du at 7/10 is −12/625.
* **Table 1** is exact. D̄²(139/200) = 748718513/750000000 and γ(139/200) = 14571/20000; the differences are 38513/750000000 and 29/20000.
* dD̄²/du = −(16/30)(112u³ − 192u² + 111u − 22). This cubic is RLE Eq. (20) with u = p². Its discriminant is −46656 < 0, so there is a unique real root.
* **Typo.** The root is **u = 0.6945520351…**, not "0.6945524" as printed. f(0.6945524) = +2.3e−6 ≠ 0; check 6, 30-digit mpmath. RLE's closed form (21), (3 + 16r − r²)/(28r) with r = (21√3 − 36)^{1/3}, agrees with the true root to working precision.
* D̄² at the root is 0.9982916927, matching RLE's 0.9983 and McNulty–Weigert's "D₄ = 0.9982917". RLE (22), (71 − 12(1−u)²)/70, agrees with (17) at the root. The second derivative there is −3.40, and D̄² is 29/40 at u = 1/4 and 1/2 at u = 1, so the root is the maximum on the interval.
* The rate at the root is 0.728424971, which the paper reports as "≈ 0.728425": correct. The typo does not affect any proof.

### 3.7 Proposition 5.1 (product-vector ceiling): **correct**

* Q_V(ρ_A ⊗ ρ_B) = (ρ_A − I/2) ⊗ I₃/3 with squared norm 1/6 for pure ρ_A. This uses the orthonormal basis σᵢ ⊗ I₃/√6 of V.
* The compressed trace on V is 6 · (1/6) = 1 for every product basis, hence for every mixture.
* Since V ⊂ H₀ and T is PSD, λmax(T|H₀) ≥ λmax(Q_V T Q_V) ≥ 1/3. This Rayleigh-quotient step is implicit in the paper.

The argument never uses a tensor-product structure of the basis, so non-tensor "nested" product bases are covered, as claimed.

**Spot checks (check 5).** I drew random tensor, qubit-split, qutrit-split and mixed product bases, from 1 to 8 bases with Dirichlet weights. The minimum λmax seen was 0.486, which is ≥ 1/3; random sampling is not expected to approach the bound.

**Sharpness.** The example is the uniform mixture over the **12** product bases {3 Pauli} ⊗ {4 qutrit MUBs}. Its exact spectrum on H₀ is (1/3)⁽³⁾, (1/4)⁽⁸⁾, (1/12)⁽²⁴⁾, matching the paper, so γ = 2/3. The paper's phrase "average independently" leaves the basis count (12) implicit.

**Additional referee observation (favourable to the paper).** Exactly **four** product bases also reach 2/3. Pair qubit bases along the four tetrahedral Bloch axes (Σᵢ nᵢnᵢᵀ = (4/3)I) one-to-one with the four qutrit MUBs. The spectrum is (1/3)⁽³⁾, (1/4)⁽¹⁶⁾, 0⁽¹⁶⁾, so γ = 2/3 (verified numerically, check 5). Hence "73/100 exceeds the product ceiling by 9.5%" (exactly 19/200) is also a like-for-like four-basis comparison.

### 3.8 Global bounds (19): **correct**

* The lower bound is the construction.
* For the upper bound: for a unit X in range(E₁|H₀), (X, 4T X) ≥ (X, E₁X) = 1, so γ ≤ 3/4.
* Equality forces the four traceless ranges to be mutually orthogonal, which is equivalent to pairwise unbiasedness.

By compactness of U(6)³ and continuity of λmax, the supremum is attained. Hence γ*₄(6) = 3/4 **iff** four MUBs exist in d = 6, which is a famous open problem. The paper correctly claims neither equality nor sharpening. Stating the "iff" and the compactness step explicitly would help.

### 3.9 Section 6 and disclosures: reproducibility statements

* The paper says "the accompanying `verify.py` …", "the supplementary `verification.json` records the actual run" and "the supplement contains source and environment requirements". According to the operator, `verify.py` and `requirements.txt` were **not** included in the published v1 release, and no `verification.json` was supplied to this review. For v1 as released, this statement is therefore inaccurate. I did not check the release independently.
* The description of the verifier is otherwise accurate, with one nuance. At the optimum the code compares exact eigenvalues and multiplicities (`eigenvals`) and records, rather than tests, the characteristic polynomial. This is equivalent in substance.
* The paper correctly states that the direct check from the original matrices is made at u = 7/10 only. Read alone, the verifier therefore does not certify (11) for generic u; my check 1 closes that gap.
* The AI-assistance and conflict-of-interest disclosures are clear and appropriate.

---

## 4. Reproduction results (actually executed)

| # | What | Script / output | Result |
|---|---|---|---|
| A | Author verifier, unmodified, run on a copy | `runs/author_verifier/` (`verify_stdout.txt`, `verification.json`, `exact-gram.json`) | **20/20 PASS**, 15 s, Python 3.12.6, SymPy 1.14.0 (matches the pin) |
| 1 | Generic-u symbolic check of unitarity, P₀ⱼ = J/6 and (10)–(11) from the original matrices | `scripts/check1_symbolic_overlaps.py` → `outputs/check1_*` | **All PASS** (43 s) |
| 2 | Numerics from the original matrices: 3001-point grid, direct 36×36 superoperator spectra, endpoints, all RLE branches, decay bound (3) and sharpness, Poisson series; negative control | `scripts/check2_numeric_original.py` → `outputs/check2_*` | Agreement ≤ 1.6e−15; argmax u = 0.7, γ = 0.73; endpoints γ = 1/4; degeneracy at u = 1; all branches identical; bound ratio ≤ 0.980; sharpness ratio 1.000 |
| 3 | Two-parameter RLE family: check against RLE (17)–(18); 361² γ-grid plus 40 Nelder–Mead refinements | `scripts/check3_two_parameter_family.py` → `outputs/check3_*` | RLE formula reproduced to 1.7e−15; ASD at RLE maximum 0.998292; **max γ found = 0.7300000000** at (θx, θt) = (−2.1504, 0.0251), which lies on relation (7) (residual 3e−14) with u = sin²θx = 0.7000 |
| 4 | *Optional, exploratory, outside the paper's claims:* unrestricted search over U(6)³ (log-sum-exp surrogate, analytic Riemannian gradient checked against finite differences: −1.2829092806 vs −1.2829092803) | `scripts/check4_global_search.py` → `outputs/check4_*` | Completed (171.8 s) although the tool call was interrupted; not extended. 60 Haar starts: best γ = 0.7299963, quartiles 0.7016/0.7040/0.7109, 3 runs > 0.729, **none > 0.73 + 1e−6**; 400 random perturbations of the u = 0.7 point: best 0.729942 < 0.73 |
| 5 | Exact algebra (Thm 4.1 envelope, (16)–(18), Table 1, RLE (20)–(22), RLE (17)–(18) identity, Cor 4.2 multiplicities, 19/200) plus Prop 5.1 spot checks and sharpness examples | `scripts/check5_exact_and_product.py` → `outputs/check5_*` | **All as claimed**, except the 7th digit of u ≈ 0.6945524 (see check 6); 12-basis and 4-basis product examples give γ = 2/3 |
| 6 | 30-digit root of the RLE cubic | `outputs/check6_rle_root_digits.txt` | u* = 0.694552035120…; γ(u*) = 0.728424971 |

Shared helpers are in `scripts/rlecommon.py`. The PDF text extraction is `outputs/paper_pdf_text.txt`.

One correction concerns my own tooling: the first run of check 5 displayed the Corollary 4.2 multiplicities with an overwritten dictionary key (27/100 shown as 4 rather than 3 + 4 = 7). I fixed the script and re-ran it; the saved output is the corrected one. The manuscript was not involved.

## 5. Counterexample attempts and stress tests

* **Ansatz versus matrices.** I tested generic u symbolically and 3001 grid points numerically. There is no discrepancy, and the negative control shows the test would detect a wrong pattern.
* **Endpoints.** Both endpoints are consistent with (13)–(14). At u = 1 the family degenerates to repeated bases. This is not an error, but it is worth stating.
* **Phase branches.** All four arcs and the sin θx < 0 loop give the same spectrum, so there is no branch-dependence counterexample.
* **Hidden assumptions checked.**
  * Self-adjointness of T, needed for (3).
  * Hermitian top eigenoperator, needed for sharpness.
  * λmax(G) > 0, true since tr G = 20.
  * Nonnegativity of all claimed eigenvalues on [1/4, 1].
  * Invariance of the e± sectors under transposed blocks.
  * Product-ness only of the basis vectors in Prop 5.1.
* **Product-basis ceiling.** No random mixture came near violating it. The bound is attained both by the paper's 12-basis example and by four product bases.
* **Uniform weights and unit rate** are explicit hypotheses of Thm 4.1. Nonuniform weights are out of scope and were not tested.

## 6. Context beyond the paper's claims (does not affect grading of correctness)

### 6.1 Two-parameter RLE family (check 3, completed)
The best γ over (θx, θt) that I found is 0.73 to 1e−15. It is attained on relation (7) at u = 0.7, with top Gram eigenvalue 1.08 of multiplicity 7, so the paper's subfamily optimum appears to be the optimum of the whole two-parameter family as well. This is numerical evidence only: grid plus local refinement, no certificate. The paper explicitly does not claim it.

### 6.2 Unrestricted four bases in C⁶ (check 4, completed but limited; further searches paused by the controller)
None of 60 random starts exceeded 0.73 + 1e−6. The best came within 4e−6 of 0.73, and perturbing the u = 7/10 configuration never increased γ. This weakly suggests that 73/100 may be close to, or equal to, γ*₄(6), in the same way that RLE's bases are numerically the global distance maximizers.

The limitations are significant: there are few restarts, the surrogate objective is smooth while λmax is nonsmooth (multiplicity 7), and there is no global certificate. I draw **no** conclusion about global optimality. I mention the run because the question, if settled, would be the natural route to real significance.

## 7. Novelty and literature

**Prior or standard (correctly attributed or acknowledged by the paper):**
* the RLE bases, relation (7) and the ASD objective (RLE 2011);
* the Gram and frame correspondence and Eⱼ as projections;
* MUBs ⇔ mutually orthogonal traceless ranges, and the 2-design and verification connection. Zhu–Hayashi's abstract states that optimal verification protocols correspond to 2-designs and, with minimal settings, to complete MUB sets.

**New, but narrow:**
* the closed-form spectrum of the measurement channel on the RLE family;
* its sharp optimization (73/100 at u = 7/10);
* the exact objective reversal;
* the elementary 2/3 product-vector ceiling. This is simple and plausibly folklore, but I did not find it stated.

**Sources consulted (actually read or fetched):**
* P. Raynal, X. Lü, B.-G. Englert, PRA 83, 062303 (2011), [arXiv:1103.1025](https://arxiv.org/abs/1103.1025). Full text read; local PDF in `literature/`.
* D. McNulty, S. Weigert, "Mutually Unbiased Bases in Composite Dimensions – A Review", [arXiv:2410.23997](https://arxiv.org/abs/2410.23997) (accepted in *Quantum*, 2026-03-17). Full text downloaded and keyword-searched (104 pp.). It reviews RLE's D₄ = 0.9982917 and the Bell-inequality optimizers, and has **no** mention of "spectral gap", "measurement channel", "frame operator", "operator norm" or "expander"; its "relaxation" hits are SDP relaxations.
* M. Prat Colomer, L. Mortimer, I. Frérot, M. Farkas, A. Acín, *Quantum* 6, 778 (2022), [arXiv:2203.09429](https://arxiv.org/abs/2203.09429), abstract read. Its Bell-inequality optimizers coincide numerically with RLE's bases; no spectral measure.
* H. Zhu, M. Hayashi, PRA 99, 052346 (2019), [arXiv:1901.09772](https://arxiv.org/abs/1901.09772). Abstract read; consistent with the paper's use of it.
* M. Ippoliti, *Quantum* 8, 1293 (2024), [arXiv:2305.10723](https://arxiv.org/abs/2305.10723). Abstract read; it is a generic classical-shadows citation, and the abstract does not discuss channel spectra.
* Search results seen but not studied: [arXiv:2302.07772](https://arxiv.org/abs/2302.07772) (quantum expanders), [arXiv:1811.08847](https://arxiv.org/abs/1811.08847) (spectral gap of random channels), [arXiv:2003.12570](https://arxiv.org/abs/2003.12570) (Pauli-channel generalization via MUMs), [arXiv:1006.0093](https://arxiv.org/abs/1006.0093) (MUBs and SDP).

**Search limits.** 7 web queries in standard mode, 4 abstract fetches and 2 full texts. I had no paywalled journals, no citation databases (Scholar or Web of Science), no exhaustive tracing of works citing RLE, and no theses. I did not access Butterley–Hall (Phys. Lett. A 369, 5 (2007)), Bengtsson et al. (JMP 48, 052106 (2007)) or Wootters–Fields (1989) directly; I know their content through RLE and the review. I cannot exclude an unindexed prior computation of this functional.

## 8. Significance and its limits

The result is an exact optimization of one spectral functional, the top eigenvalue of G, over a one-parameter family of known bases, using standard block-circulant diagonalization and quadratic inequalities.

An explanatory remark the paper misses: D̄² = 1 − (‖G‖_F² − 20)/60, with tr G = 20 fixed. The distance objective is therefore the second spectral moment of G, and the rate depends on its largest eigenvalue. That the two optimizers differ is then unsurprising, as the paper itself concedes.

The physical motivation, relaxation under randomly chosen nonselective measurements, is reasonable but modest. The paper does not connect γ to an operational task beyond the HS decay rate; possible links would be verification efficiency or a classical-shadow variance. The result's value would rise substantially if the authors established optimality over the two-parameter family, which my numerics suggest holds, or over all four-basis configurations, or proved a bound strictly below 3/4. Any proof of γ*₄(6) < 3/4 would rule out four MUBs in d = 6. As submitted, it is a correct, clean, narrowly scoped note.

## 9. Requested changes

### Required (minor)
1. **Justify (11) for generic u.** Show the multiplication, or cite RLE Eqs. (8)–(12) precisely, and give |β|² = 36(1−2u)² and |γ|² = |δ|² = |ε|² = 12(1−u)(4u−1). Remove or qualify "or by row normalization", which fixes only the sum of the four C-entries.
2. **Correct "u ≃ 0.6945524" to 0.6945520** (0.694552035…).
3. **Make Section 6 consistent with the published release.** Either attach `verify.py`, `requirements.txt` and `verification.json` to the record, or rephrase the statements about an "accompanying" supplement and a "supplementary verification.json".
4. **State the basis count (12) in the sharpness example of Prop 5.1.** Preferably also note that four product bases (tetrahedral qubit axes ⊗ the four qutrit MUBs) attain 2/3, so that the 73/100 comparison is at equal basis count.

### Optional
5. State that Theorem 3.1 holds on every branch of RLE relation (7), i.e. the whole RLE one-parameter family (verified numerically here), and mention the endpoint degeneracy at u = 1, where bases 1–3 coincide (γ(1/4) = γ(1) = 1/4).
6. Make explicit the frame-operator identity (it uses Σₖ vⱼₖ = 0), the e± invariance of the transposed blocks, the compression/Rayleigh step in Prop 5.1, and compactness in (19). Then state γ*₄(6) = 3/4 ⇔ four MUBs exist in d = 6.
7. Add D̄² = 1 − (‖G‖_F² − 20)/60 to clarify the relation between the two objectives.
8. Investigate, numerically or analytically, the two-parameter family and the unrestricted problem. My limited exploration found nothing above 73/100.
9. Broaden the references: Bengtsson et al. 2007 (origin of the distance), Butterley–Hall 2007, Prat Colomer et al. 2022, the McNulty–Weigert review, Huang–Kueng–Preskill 2020 for measurement-channel inversion in classical shadows, and quantum-expander and spectral-gap literature if the "mixing" language is kept.
10. Extend the supplementary verifier with a generic-u symbolic check of (11) from the original matrices, along the lines of check 1.

## 10. Ordinary 0–10 rubric (separate from the AIRR scale)

| Criterion | Score | Basis |
|---|---|---|
| Correctness | **9/10** | Every main claim verified independently, including generic u from the original matrices. Deductions only for the 7th-digit typo and the insufficient "row normalization" remark. |
| Originality | **4/10** | A new but narrow, technically routine optimization of a standard spectral functional on previously known bases. |
| Significance | **3/10** | Limited to one RLE subfamily; the questions that would matter (two-parameter or global optimum, a bound below 3/4) are not addressed. |
| Clarity | **8/10** | Concise, explicit phases and conventions, honest scoping. Some implicit steps, and the Section 6 supplement statements mismatch the v1 release. |

**Overall ordinary grade: 6/10, with uncertainty about ±1 (range 5–7).** The plain average of the four criteria is 6.0, and I judge that this reflects the paper well: correct and clear, but narrow. The uncertainty comes mainly from how one values an exact but narrow optimization, and from the limited literature search.

## 11. AIRR rubric mapping

* **Recommendation:** minor_revision. No unresolved objection capable of invalidating a main claim remains.
* **Criterion stars:**
  * correctness confidence 5;
  * rigor 4 (expository gaps only);
  * novelty 2;
  * significance 2;
  * reproducibility 4 (fully reproducible from the paper, and the verifier passes, but the v1 release lacks the supplement it describes and the verifier's direct check is at a single u).
* **AIRR millennium_score: 2.60, overall_stars 3.** This sits slightly below the 3.00 anchor ("acceptable and substantive"): the work is acceptable and correct, but its substance and significance are narrow. The score is a significance comparison on AIRR's special scale, not a correctness grade or a school mark. Correctness is rated separately, at 5 stars.

## 12. Files produced in this directory
* `assessment.json`: the AIRR JSON object.
* `report.md`: this report.
* `scripts/`: `check1_symbolic_overlaps.py`, `check2_numeric_original.py`, `check3_two_parameter_family.py`, `check4_global_search.py`, `check5_exact_and_product.py`, `rlecommon.py`.
* `outputs/`: JSON and text outputs of checks 1–6, the check 3 γ-grid (`.npy`), the check 4 per-run values (`.npy`), and the PDF text extraction.
* `runs/author_verifier/`: an unmodified copy of `verify.py` and `paper.tex` with its run outputs (`verify_stdout.txt`, `verification.json`, `exact-gram.json`). These were generated by my run, not supplied by the author.
* `literature/`: the RLE PDF, the McNulty–Weigert review PDF with its extracted text, and keyword contexts.
