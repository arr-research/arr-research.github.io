# Referee report: ARR-2026-3RH54K4NC58MRSX3, version v2

**Title:** An exact relaxation optimum in a one-parameter family of four quantum measurement bases
**Version identifier:** `arr:version:bc5c9f23-b39f-49a1-901c-16f499937caf`
**Assessed artifact (canonical PDF, SHA-256):** `3c60aee3179b0f8d9c7a07960b7b600cca8cac70b5898f710676d8d124ea25ae`
**Rubric / prompt version:** ARR-ASSESS-1.0
**Assessed at:** 2026-10-11T19:05:08+02:00

**Recommendation:** `minor_revision`. There are no unresolved material objections. This is a model recommendation, not human editorial acceptance.
**AIRR `millennium_score`:** 2.6 (`overall_stars` 3)
**Ordinary overall grade:** 6.0 / 10 (table in Section 9)

---

## 0. Reviewer, configuration, provenance and controls

- **Provider / model:** Anthropic, `claude-opus-5-5` (Claude Opus 5.5), running in the Claude Code / Claude Agent SDK harness. The operator requested the "max" effort configuration. I cannot independently inspect that runtime setting; the runtime model ID matches the request.
- **Independence:** `involved_in_manuscript`. This is the operator's declaration, and the manuscript itself states that Claude Opus 5.5 supplied advisory feedback on v1 that informed this revision. I have no memory of that participation and did not read any v1 report or grade. Missing memory does not establish independence, and I cannot verify context isolation.
- **Files read:**
  - the rubric (`airr-rubric.txt`);
  - `request.txt`, which the operator's resume message told me to re-read;
  - the eight scientific inputs: `paper.pdf`, `paper.tex`, `verify.py`, `verify_generic.py`, `requirements.txt`, `verification.json`, `generic-verification.json` and `exact-gram.json`.
- **Not opened:** `doi-correction-addendum.txt` (outside the permitted list) and the session logs (`claude-*.jsonl`, `claude-*stderr.txt`). I relied on the operator's description of the DOI change and verified it myself (below).
- **Not done:** no parent or sibling directories, memories, messages, git, publication, credentials, purchases or sub-agents.
- **Publication state:** per `request.txt`, a revised candidate not yet publicly released. I did not verify, and do not claim, any public upload.
- **Preliminary work (superseded artifact):** before the operator's pause I had read the then-current files and hashed the superseded PDF (`ce6f5c56ab5d…5f9b`) and source (`4efe8adc268e…cb94`). No assessment or grade was formed for that candidate. This report concerns only `3c60aee3…25ae`.
- **Hash checks on the corrected artifact:**
  - `paper.pdf` hashes to `3c60aee3179b0f8d9c7a07960b7b600cca8cac70b5898f710676d8d124ea25ae`, matching both `request.txt` and `airr-rubric.txt`. It has 8 pages; metadata shows MiKTeX pdfTeX-1.40.28, created 2026-10-11 18:29:06+02:00.
  - `paper.tex` hashes to `3e7a85407ba9364ef539506501e8ed222654078658021fad34d4b1f46bb8faec`.
  - **Proof that the DOI is the only source change:** substituting `10.1063/1.2748617` back to `10.1063/1.2749490` in the current source reproduces the superseded source hash `4efe8adc…` exactly.
- **PDF review method:** I viewed all 8 rendered pages and also extracted the text with pypdf 6.4.0 (`referee_work/pdf_extract/paper_extracted.txt`) to check strings. The PDF content matches the source, including the corrected DOI on p. 8.
- **Input integrity:** all ten input files were re-hashed at the end of the review and were unchanged. Author scripts were run only on copies in `referee_work/author_rerun/`.
- **Software:** `C:/Python312/python.exe`, Python 3.12.6, SymPy 1.14.0, NumPy 2.5.1, SciPy 1.18.0, mpmath 1.3.0, pypdf 6.4.0.

## 1. Claims under review

| ID | Claim (location) | Status |
|---|---|---|
| C1 | Dynamics: `e^{t(T-id)}` is CPTP and unital; `T` is self-adjoint and PSD; decay bound (3) with a sharp exponent; frame identity and `gamma = 1 - lambda_max(G)/4`, Eq. (5) (Sec. 2) | Verified; one ambiguous sentence (Section 3.1 below) |
| C2 | Eqs. (6)–(9) are RLE's construction; branch of relation `cos(theta_t+pi/3)=cos(2theta_x)/sin(theta_x)`; `|q|<=1 <=> 1/4<=u<=1` (Sec. 3) | Verified against RLE arXiv:1103.1025v1 |
| C3 | Overlap blocks (10)–(11) and the amplitude derivation on p. 4, for every u in [1/4,1] | Verified exactly (two independent implementations) |
| C4 | Theorem 3.1: complete Gram spectrum with multiplicities; rate formula (14) | Verified identically in u |
| C5 | Theorem 4.1: maximum 73/100, attained uniquely at u = 7/10 (equal probabilities, unit rate) | Verified |
| C6 | Corollary 4.2: explicit algebraic bases; channel spectrum (15) | Verified |
| C7 | Distance polynomial (17), Frobenius identity, (18), Table 1, RLE optimizer decimals | Verified; consistent with RLE closed forms |
| C8 | Proposition 5.1 (2/3 product-vector ceiling), 12-basis sharpness, bounds (19), MUB equality, compactness | Verified |

## 2. Overall assessment

The mathematics is correct. I attempted to break every main claim and could not.
- **Theorem 3.1** follows from a clean invariant-subspace argument whose eigenvectors are independent of u.
- **Theorem 4.1** is a short, correct piecewise argument.
- **Distance comparison:** it is exact and agrees with RLE's own published closed forms.
- **Section 5:** the bounds are correct.
- **Scope:** statements are careful and the abstract matches what is proved.
- **Reproducibility:** the bundle regenerates exactly.

The contribution is a narrow, explicit calculation on a known family using standard tools. Its significance is modest. The headline value 73/100 is a constrained optimum: with the same bases, re-weighting the measurement probabilities gives 25/34 (Section 4.2). That is not an error, because the paper fixes equal probabilities explicitly, but readers should be told.

## 3. Theorem and proof findings

### 3.1 Section 2: dynamics, gap, frame identity
- `E_j` is the pinching in basis j and an HS-orthogonal projection. `T` is self-adjoint, PSD and unital, with spectrum in [0,1]. The Poisson series gives a convex combination of CPTP unital maps. The decay bound (3) follows from self-adjointness on `H0`. Sharpness holds because `T` preserves Hermiticity, so the top eigenspace contains a Hermitian element. **Correct.**
- The identity `sum_k v_jk Tr(v_jk X) = E_j(X)` on `H0` is correct. The frame operator of `{v_jk}` is `4T|H0`, and `G` (= V*V) shares its nonzero eigenvalues. Since `lambda_max(G) >= 1 > 0`, Eq. (5) is correct.
- **Minor wording error (p. 2):** "With column vectorization … the full channel is ¼Σ|Π_jk)(Π_jk|. … *Its* nonzero eigenvalues agree with those of G, including multiplicity."
  - If "Its" refers to the full channel, as the syntax suggests, the statement is false. That channel has the extra eigenvalue 1 (on I), and its other nonzero eigenvalues are those of G divided by 4.
  - The statement is true for the frame operator `4T|H0` introduced two sentences earlier.
  - Eq. (5) is unaffected. *Required (minor):* reword.
- The column-vectorization formula `|Π) = b̄ ⊗ b` is correct.

### 3.2 Bases, parametrization, branch and endpoints (Eqs. 6–9)
- **Matches RLE:** the displayed `F, Z, X, H` and `U_1, U_2, U_3` coincide with RLE arXiv v1 Eq. (5) (with their `T` = this paper's `H`) and Eq. (6). The relation is RLE Eq. (7). The phrase "[3, Eqs. (5)–(7)]" is accurate for arXiv v1 numbering; I did not access the published PRA version.
- **Parametrization:** `x = sqrt(1-u) + i sqrt(u)` gives `sin^2(theta_x) = u` and `cos(2theta_x)/sin(theta_x) = q`. The definition `t = e^{-i pi/3}(q + i sqrt(1-q^2))` gives `cos(theta_t + pi/3) = q`. `|q| <= 1` is equivalent to `(4u-1)(1-u) >= 0`, i.e. `1/4 <= u <= 1`. **Correct.**
- **Branches:** the paper treats one arc of RLE's relation, which has eight arcs on the torus (RLE Fig. 2). I evaluated all eight arcs at 301 values of u each, 2,408 evaluations in total.
  - Each arc reproduces the Theorem 3.1 spectrum pointwise in `u = sin^2(theta_x)`, with maximum deviation 6.2e-15.
  - Each arc gives exactly γ = 0.73 at sin²θₓ = 7/10.
  - The branch restriction therefore loses nothing. The paper's statement "Equivalent phase branches are not needed for the theorem" is accurate, but a one-line symmetry argument would let the abstract's "the one-parameter subfamily introduced by RLE" be read literally. *Optional.*

### 3.3 Overlap blocks and amplitude derivation (Eqs. 10–11, p. 4)
- **Definitions:** `A + B + 4C = 1` holds. `s = A - B` and `k = 1 - 6C` match Eq. (12).
- **Generic u, all 108 off-diagonal probability entries and all unitarity/unbiasedness entries:** verified exactly from the displayed matrices, for every u in [1/4,1], by:
  - the author's `verify_generic.py` (rerun, 10/10 PASS);
  - my own `check_exact.py`, written independently. It uses real symbols `a=sqrt(1-u)`, `b=sqrt(u)`, `c=sqrt(4u-1)`, reduces modulo `a^2-(1-u)`, `b^2-u`, `c^2-(4u-1)`, and implements conjugation as `i -> -i`.
- **Endpoints:** only powers of u occur in denominators, so formal identities specialize correctly at u = 1/4 (c = 0) and u = 1 (a = 0). Conjugation is legitimate because a, b, c are real exactly on [1/4,1]. The paper's endpoint argument is therefore sound.
- **Amplitudes:** each displayed identity on p. 4 was checked exactly:
  - `|α|²/36 = A`;
  - `ω t̄ = -q + i sqrt(1-q²)`;
  - `Re t = (q + √3 r)/2`;
  - `cos(θ_t - 2π/3) = -q`;
  - `cos(θ_t + 2π/3) = (q - √3 r)/2`;
  - `|η|² = 12(1-u)(4u-1)`;
  - `u(1-q²) = (1-u)(4u-1)`.
- **Consistency with RLE:** the amplitude formulas match RLE Eq. (11) with `cos(theta_x) = sqrt(1-u) >= 0` on this branch. The block patterns match RLE Eqs. (8)–(10): `a1` and `b2 = ǎ1` give D, and `c3` carries the α/β interchange, giving D̃. RLE note that `ε = ω* δ*` on relation (7), which is consistent with the manuscript's δ and ε.
- **Second independent check:** a separate 50-digit mpmath rebuild (`check_numeric.py`) at the endpoints, the optimum, 139/200, u*, five other rationals and 12 random u gave:
  - unitarity, unbiasedness and block-ansatz deviations of at most 5.4e-51;
  - the same results on the alternative t-branch.

### 3.4 Theorem 3.1 (complete Gram spectrum)
- **Proof logic:** each step checks out.
  - The 2×2 blocks D, D̃ and CJ₂ and their transposes preserve the `e_±` lines.
  - On `C³⊗e_-`, Q acts as the identity and the three overlap blocks act as `sI, sR, -sR²`.
  - Conjugating by `diag(I, I, R²)` gives `[[1,s,-s],[s,1,s],[-s,s,1]] ⊗ I₃`. This is a frustrated-triangle matrix with eigenvalues `1+s` (twice) and `1-2s` (once).
  - On the symmetric sector, the constants are null vectors, using double stochasticity.
  - On the complement, `A + B - 2C = k` gives `[[1,k,k],[k,1,k],[k,k,1]]` on two copies.
  - The canonical block decouples because `P_0j = J/6`.
  - The dimension count 6 + 9 + 3 + 6 = 24 is correct.
- **Independent verification:** I built the proof's 24 explicit eigenvectors. They do not depend on u. I verified symbolically that `G(u) v = λ(u) v` holds identically in u for each, and that the 24 vectors are linearly independent (nonzero determinant). Hence the spectrum and multiplicities in (13) hold for **every** u, including where eigenvalues coincide.
- **Further checks:**
  - the author's characteristic-polynomial check over Q[u], rerun and passing;
  - a direct 35×35 channel matrix on an orthonormal Hermitian basis of `H0`, computed without using the Gram correspondence, which matches `{0^(35-rank)} ∪ nonzero(G)/4` to within 7.8e-16.
- **Endpoint behavior:** rank drops occur only at the endpoints (`1+s = 0` at u = 1, `1-2s = 0` at u = 1/4, `1-k = 0` at both). The phrase "multiplicities add" covers this. γ(1/4) = γ(1) = 1/4.

### 3.5 Theorem 4.1 (sharp subfamily optimum)
- **Interval-by-interval checks:**
  - `s' = (4-16u)/3 <= 0` on [1/4, 3/5], and `s(3/5) = 13/75 > 2/25`.
  - `-k - 2/25 = -8(u-11/20)(u-7/10)` is at least 0 on [3/5, 7/10], with equality only at 7/10.
  - `-2s - 2/25 = (16/3)(u-7/10)(u+1/5)` is at least 0 on [7/10, 1], with equality only at 7/10.
  - At 7/10, s = -1/25, k = -2/25 and h = 2/25, so γ = 73/100.
- **Independent semialgebraic check:** intersecting the five sets `{u: f(u) <= 2/25}` for `f ∈ {0, -2s, s, 2k, -k}` with [1/4,1] gives exactly {7/10}. Hence h(u) > 2/25 for every u ≠ 7/10, and the maximizer is unique. **Correct.**
- **Quantifiers:** uniqueness is in the parameter u on branch (9). On RLE's full relation the value is attained once on each of the eight arcs (Section 3.2), analogous to RLE's "eight optimal pairs" for the distance.

### 3.6 Corollary 4.2
- `x`, `q`, `t` equal the u = 7/10 parameters, and (A, B, C) = (3/25, 4/25, 9/50).
- The exact Gram spectrum is `{0⁴, 1⁵, (21/25)², (24/25)⁶, (27/25)⁷}`, with rank 20 and channel nullity 15. The channel spectrum is exactly Eq. (15).
- Confirmed by my exact check and by the author's direct-basis check (rerun).

### 3.7 Distance comparison (Eqs. 16–18, Table 1, decimals)
- **Definition (16):** RLE Eq. (2) gives `D²_ab = 1 - (1/(d-1)) Σ(|⟨a_i|b_j⟩|² - 1/d)²`, and RLE Eq. (3) averages over pairs. For d = 6 and k = 4 this is exactly (16).
- **Polynomial (17):** follows from the per-pair defect `6(A²+B²+4C²) - 1`. It also agrees **symbolically** with RLE's own per-pair formula, Eqs. (17)–(18), `D²_12 = (8/45)[5 - P(p,q)]` on relation (7). The mean is `(1 + D²_12)/2` because the three canonical pairs have distance 1.
- **Frobenius identity:** `Tr G = 20` and `D̄² = 1 - (||G||_F² - 20)/60` hold, checked symbolically on the family.
- **Eq. (18):** `D̄²(7/10) = 6239/6250` and `dD̄²/du(7/10) = -12/625`.
- **Table 1:** `D̄²(139/200) = 748718513/750000000`, `γ(139/200) = 14571/20000`, and the differences 38513/750000000 and 29/20000 are all exact.
- **RLE optimizer:**
  - `dD̄²/du = -(8/15)(112u³ - 192u² + 111u - 22)`.
  - The cubic has discriminant -46656 < 0, so it has exactly one real root, `u* = 0.694552035120092163744877752610…`. This matches the quoted 0.694552035120092, and u* is the maximizer on [1/4,1].
  - RLE Eqs. (20)–(21): their closed form `(3 + 16r - r²)/(28r)` with `r = (21√3 - 36)^{1/3}` equals u* to 40 digits.
  - RLE Eq. (22): `D̄²_max = (71 - 12cos⁴θ)/70 = 0.99829169270012…` equals (17) at u*.
- **Decimals:** `γ(u*) = 0.7284249711786930…`, quoted as ≈ 0.728425. The relative gain of 73/100 over it is 0.21622%, quoted as ≈ 0.2162%. The absolute gain is 0.0015750. **All correct.**

### 3.8 Proposition 5.1 (product-vector ceiling) and sharpness example
- **Proof:**
  - For a pure product projector, `Q_V Π = (ρ_A - I/2) ⊗ I₃/3` with `||Q_V Π||² = 1/6`.
  - Each basis therefore contributes compressed trace 1 on the three-dimensional subspace V, and so does any probability mixture.
  - The largest Rayleigh quotient on V is at least 1/3, hence γ ≤ 2/3.
  - No invariance of V is needed. Only the product form of each vector is used, so non-tensor product bases are covered. **Correct.**
- **Numerics:**
  - compressed-trace identity confirmed to 1e-15;
  - 3,000 random mixtures of up to 12 product bases (tensor, qubit-first, qutrit-first and genuinely nested orthogonal product bases, with Dirichlet weights) gave max γ = 0.5345;
  - an adversarial Nelder–Mead search over 4 non-tensor product bases (6 restarts) gave max γ = 0.5835.
  - No counterexample was found.
- **Sharpness example:** 3 Pauli bases × 4 qutrit MUBs gives traceless spectrum `{1/3 (×3), 1/4 (×8), 1/12 (×24)}` and γ = 2/3 exactly, as stated.
- **Margin:** `(73/100)/(2/3) = 219/200`, i.e. exactly 9.5% larger.

### 3.9 Unrestricted bounds (19), equality case, compactness
- **Bounds:** the lower bound comes from the construction. For the upper bound, each `E_j|H0` is a rank-5 projection and the other terms are PSD, so `λ_max(4T|H0) >= 1` and γ ≤ 3/4.
- **Equality case:** equality forces the traceless ranges to be mutually orthogonal, which is equivalent to all off-diagonal G blocks vanishing, i.e. to MUBs. Four MUBs attain equality.
- **Compactness:** the supremum over `U(6)⁴` is attained because `λ_max` is continuous. So `γ*₄(6) = 3/4` if and only if four MUBs exist in d = 6. **Correct.**
- **Validation:**
  - four MUBs in d = 5 give γ = 0.75 exactly;
  - 2,000 Haar-random quadruples in d = 6 give max γ = 0.5104.
- **Prior art:** this bound and its equality case are, under the vectorization identity, the "parsimonious strategy" statement of Zhu–Hayashi (`β(Ω) >= 1/g` for g tests, with equality for MUB-type tests) (Section 6). The paper attributes it loosely as a "standard projection connection".

### 3.10 Abstract versus proved results; scope
Every abstract sentence is supported by a proved statement. The qualifiers "within this subfamily", "equal measurement probabilities" and "unit total event rate" are present. The text explicitly disclaims global four-basis optimality, optimality over the two-parameter family and any new MUB construction. I found no overclaim in the PDF.

## 4. Stress tests beyond the paper's claims (numerical context, not proofs)

### 4.1 Two-parameter RLE family
- **Method:** a bounded scan of Eqs. (6)–(8) with free `|x| = |t| = 1`: a 240×240 grid, then Nelder–Mead refinement from the 12 best grid points.
- **Result:** the refinement converged to γ = 0.7300000000 at sin²θₓ = 0.70000000. That point satisfies relation (7) to 4.5e-15.
- **Interpretation:** no point of the two-parameter family exceeding 73/100 was found. This suggests, but does not prove, that the subfamily optimum is also the two-parameter optimum.

### 4.2 Equal probabilities are binding
- **Structural reason:** the canonical basis is unbiased to U₁–U₃, so its traceless range is orthogonal to theirs. Hence `T|H0 = p₀E₀ ⊕ Σ_{j≥1} p_j E_j`, and with `p₁ = p₂ = p₃ = p`, `λ_max = max{p₀, p(1 + h'(u))}` with `h' = max{-2s, s, 2k, -k}`.
- **Exact result:** at u = 7/10, weights (27, 25, 25, 25)/102 give `λ_max = 9/34`, so **γ = 25/34 ≈ 0.73529 > 73/100**. Under equal weights the canonical basis is under-used: its eigenvalue is 1/4, below the binding 27/100.
- **Numerical probe:** arbitrary simplex weights on a 151-point u-grid found nothing better (best 0.73529412 at u = 0.70 with these weights).
- **Why it matters:** this does not contradict Theorem 4.1, which fixes equal probabilities. But it shows the equal-weight constraint changes the optimum value, which is relevant to how "the largest relaxation rate within this subfamily" should be read.

## 5. Reproducibility audit
- **Reruns:** I ran copies of the author's scripts in `referee_work/author_rerun/`.
  - `verify.py`: 20/20 PASS in about 7 s.
  - `verify_generic.py`: 10/10 PASS in about 5 s.
- **Comparison with dated records:** my regenerated `verification.json` and `generic-verification.json` equal the author's dated records in every field except `generated_utc` and `seconds`. `exact-gram.json` is byte-identical. The author records (generated 16:29:49Z and 16:29:57Z) reference the *current* `paper.tex` hash `3e7a8540…`, so they were regenerated after the DOI correction.
- **Coverage:**
  - `verify.py` checks the characteristic polynomial of the *ansatz* Gram matrix over Q[u], and the direct basis construction only at u = 7/10.
  - `verify_generic.py` closes the gap: original matrices → ansatz for symbolic u.
  - Together they cover Theorems 3.1 and 4.1. My independent checks cover the same ground by different routes.
- **Inaccuracy:** the docstring of `verify_generic.py` (line 5) says "numerical checks form a 36x36 channel", but the script contains no numerical or channel computation. The PDF's Section 6 description ("Neither script relies on floating-point tolerances") is accurate. *Required (minor, bundle):* correct the docstring or add the advertised check.
- **Scope of the scripts:** they hash `paper.tex`, not `paper.pdf`. I established the PDF–source correspondence by reading and extracting the PDF.

## 6. Literature, attribution and novelty

**Sources obtained independently (stored in `referee_work/literature/` with SHA-256 in `MANIFEST.txt`):**
- RLE, arXiv:1103.1025v1 PDF (10 pages; SHA-256 `dea60071…228c`), read in full via text extraction.
- Crossref metadata for:
  - 10.1063/1.2748617 (Roy & Scott, J. Math. Phys. 48, 072110 (2007)): confirms the **corrected DOI**;
  - 10.1063/1.2749490 (the old DOI): resolves to an unrelated J. Appl. Phys. 101, 123525 paper on skutterudites, confirming the old DOI was wrong;
  - 10.1103/PhysRevA.83.062303 (RLE);
  - 10.1016/0003-4916(89)90322-9 (Wootters–Fields);
  - 10.22331/q-2024-03-21-1293 (Ippoliti).
- Zhu & Hayashi, PRA 99, 052346 (2019), arXiv:1901.09772: bibliographic data confirmed via search listings (the Crossref request timed out). Content was spot-checked through a fetch-tool summary of the ar5iv rendering, which returned quoted sentences; I did not read the full PDF. The quoted text contains the g-test parsimony statement ("parsimonious if β(Ω)=1/g") and only one d = 6 remark (a 2-design from eight bases). The summary reported no treatment of d = 6 with four settings or of RLE bases.
- The self-citation [6] (AIRR) was not checked. I avoided the AIRR site to stay clear of review content.

**Attribution findings:**
- The RLE matrices, relation, amplitude formulas, cyclic block structure, distance definition, cubic and optimizer all match RLE as cited, with arXiv v1 equation numbers.
- RLE note that the ASD maximum 0.9983 was first found numerically by Butterley & Hall (Phys. Lett. A 369, 5 (2007)). The distance itself is from Bengtsson et al. (J. Math. Phys. 48, 052106 (2007)). Citing both is optional.

**Novelty:**
- **Standard or prior:**
  - the operator/Gram frame correspondence (Roy–Scott; standard frame theory);
  - the measurement channel as a verification operator: under vectorization `γ` is exactly the Zhu–Hayashi spectral gap `ν` for verifying the 6×6 maximally entangled state with these four test bases;
  - the bound ν ≤ 1 - 1/g with its MUB equality case (Zhu–Hayashi's parsimonious strategies);
  - the local Pauli/MUB constructions (Wootters–Fields);
  - the two-parameter family, subfamily relation and distance objective (RLE).
- **Plausibly new:** the closed-form 24-eigenvalue spectrum of the RLE subfamily, its sharp equal-probability relaxation optimum 73/100 at u = 7/10, the exact rational objective reversal, and the elementary 2/3 product-vector ceiling.
- **Search:** focused web searches found no prior computation of the relaxation, verification gap or frame λ_max for the RLE family. Queries covered RLE follow-ups, spectral gaps of averaged dephasing or measurement channels, quantum expanders, frame operators of MUB-like sets, verification of maximally entangled states with few settings, and "completeness stability".
- **Search limits:** the search was focused, not exhaustive. Direct arxiv.org access was intermittent from this machine. The published PRA versions were not accessed.

## 7. Required and optional changes

**Required (minor; none affects the correctness of any stated result):**
- **R1. p. 2 wording.** Replace "Its nonzero eigenvalues agree with those of G" with an explicit statement. The frame operator `4T|H0` and G share nonzero eigenvalues with multiplicity. Equivalently, the full channel has nonzero spectrum `{1} ∪ {λ/4 : λ ∈ spec(G)∖{0}}`.
- **R2. Bundle documentation.** Correct the `verify_generic.py` docstring claim of "numerical checks form a 36x36 channel", or add that check. This is a factual inaccuracy in the reproducibility material, not in the PDF.

**Strongly recommended:**
- **S1. Equal probabilities.** Add a remark that the equal-probability constraint is binding. Weights (27,25,25,25)/102 on the same bases give exactly 25/34 at u = 7/10. Alternatively, treat weighted optimization briefly. This directly affects how the headline number is read.
- **S2. Verification equivalence.** State explicitly that γ equals the Zhu–Hayashi verification spectral gap for the maximally entangled state with these test bases, and credit bound (19) and its equality case to their g-setting result. This both sharpens prior-art attribution and gives the result a concrete application.

**Optional:**
- **O1.** Add a symmetry argument, or at least a sentence, noting that all arcs of RLE relation (7) give the same spectrum as a function of u = sin²θₓ (Section 3.2).
- **O2.** Report, clearly labeled as numerical evidence, that a scan of the two-parameter family found no rate above 73/100 (Section 4.1). Alternatively, pose this as an open problem.
- **O3.** Cite Butterley–Hall (2007) and Bengtsson et al. (2007) for the ASD history and definition. Optionally mention quantum-expander terminology (second-largest eigenvalue of a unital channel).
- **O4.** State that RLE equation numbers follow arXiv:1103.1025v1, or check them against the PRA version.
- **O5.** Write out the 2×2-block placement in (11) from the cyclic RLE products (or one representative computation) instead of only "direct multiplication".
- **O6.** Consider moving the long AI-assistance and provenance text to an end note. This is editorial; the disclosures themselves are appropriate.

**Is any change still required before this narrow working paper is scientifically satisfactory?** No change is required for the correctness of any stated theorem, proposition or numerical claim; all were verified.
- **R1 and R2** are small precision and documentation corrections that I consider necessary before the bundle is released. That is the reason for `minor_revision` rather than `accept`.
- **S1** is the most consequential content addition. It does not contradict any claim, but without it a reader may overrate the headline value.

## 8. AIRR grading (as in `assessment.json`)

| Field | Value | Basis |
|---|---|---|
| correctness_confidence | 5/5 | All claims verified independently, symbolically and identically in u where relevant |
| rigor | 4/5 | Complete proofs; minor wording error p. 2; block placement delegated to "direct multiplication" plus supplement |
| novelty | 2/5 | Narrow calculation on a known family with standard tools; bound (19) is prior art (Zhu–Hayashi) |
| significance | 2/5 | 1-D optimization; 0.216% over the RLE distance optimizer; equal-weight optimum exceeded by 25/34 with reweighting |
| reproducibility | 5/5 | Exact, pinned, regenerates field-for-field; one docstring overclaim |
| millennium_score | 2.6 (stars 3) | Correct and acceptable, but somewhat less substantive than the 3.00 "acceptable and substantive" anchor |
| recommendation | minor_revision | No material objections; R1–R2 required minor fixes |

## 9. Ordinary 0–10 grading (separate from the AIRR scale)

| Criterion | Grade (0–10) | Justification |
|---|---|---|
| Correctness | 9.5 | Every theorem, corollary, identity, table entry and decimal was verified, several by two independent routes. 0.5 deducted for the p. 2 sentence that is false under its most natural reading. |
| Originality | 4.0 | The spectrum and sharp optimum on the RLE subfamily appear new, but they are a direct application of the standard frame/Gram method to a published family. The bounds are known or elementary. |
| Significance | 3.5 | A clean exact example of geometric versus dynamical optimizers. The gains are small, the global and two-parameter questions are untouched, and the equal-weight constraint is binding (25/34). |
| Clarity | 8.0 | Well organized, with explicit scope and quantifiers, a readable proof of Theorem 3.1 and a transparent reproducibility section. Small deductions for the ambiguous p. 2 sentence, the partly delegated block derivation and lengthy process disclosures. |
| **Overall** | **6.0** | A correct, carefully scoped and exemplary-reproducible note of modest originality and significance. It would merit publication as a short note in a specialized venue after minor revision; it is not a substantial advance. |

## 10. Referee artifacts (all in `referee_work/`; SHA-256 for every file in `referee_work/MANIFEST.txt`)

| File | Purpose | Result |
|---|---|---|
| `author_rerun/` (copies) + `logs/author_verify_rerun.log`, `logs/author_verify_generic_rerun.log` | Rerun of the author verifiers on copies | 20/20 and 10/10 PASS |
| `logs/compare_outputs.py`, `.log` | Field-by-field comparison with the dated author records | Identical except timestamps; `exact-gram.json` byte-identical |
| `independent/check_numeric.py` (`df5e17790a108edbada8dcac8dee56c26d87e371e45d11aa0f3aa105ad637247`) + log | 50-digit rebuild from the displayed equations; direct 35×35 channel; both t-branches | Max deviation 5.4e-51 (exact-arithmetic level), 2.7e-15 (spectra) |
| `independent/check_exact.py` (`0c68d994bf8caf7fd46656d2b9917365740fff1acc18a96edb4520ed42ce9837`) + log | Generic-u exact identities, proof eigenvectors, semialgebraic optimum, distance and decimals, Cor. 4.2 | 49/49 PASS |
| `independent/check_bounds.py` (`47a4c96d1765bf31739d3e86737b5756d3fc5f73d0f1032f3d8f700d0a836017`) + log | Prop. 5.1 falsification, 12-basis example, 3/4 bound, two-parameter scan | No counterexample; scan max 0.73 at u = 0.7 |
| `independent/check_rle_crosscheck.py` (`a2b455445f06e276771facdf2eff0b3a237b1e82e8331bb1dfda01af9c84ae97`) + log | RLE closed forms (21)–(22), per-pair formula (17)–(18), branch arcs | Agreement to 1e-40 or symbolic |
| `independent/check_branches.py` (`58067779af74b720793f12dbbd4761161a1bcb35cfff232879b5dd53bee227ca`) + log | All eight arcs of relation (7) against Theorem 3.1 | Max deviation 6.2e-15; γ(7/10) = 0.73 on all arcs |
| `independent/check_weights.py` (`d3a287d81f8f94095e14a3dc2b769188c30f7f41525aa4a92265ee58ddf06fdb`) + log | Scope probe: unequal probabilities | 25/34 exactly with (27,25,25,25)/102 |
| `pdf_extract/extract.py`, `paper_extracted.txt` | pypdf text extraction and string checks of the canonical PDF | Hash, 8 pages, corrected DOI present |
| `literature/` | RLE arXiv v1 PDF and text, Crossref metadata | See Section 6 |

**Limits of this review:**
- The numerical scans (two-parameter family, weights, product bases, Haar sampling) are bounded falsification and context checks, not proofs. In particular, they cannot establish any global optimum.
- The literature search was focused and not exhaustive.
- The published versions of RLE and Zhu–Hayashi were not accessed (arXiv v1 and ar5iv only).
- I did not verify the operator's runtime "max" configuration or any context isolation.
