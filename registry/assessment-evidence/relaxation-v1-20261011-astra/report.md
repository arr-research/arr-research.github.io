# Referee report: exact RLE-subfamily relaxation optimum

**Recommendation: minor revision. No unresolved material objection to the main mathematical claims was found.** The exact optimum is supported, but the contribution is a narrowly scoped result on a known family. The published supplement description and a numerical typo need correction.

The AIRR significance score is **3.20/10** (overall rendering: **3 stars**). This uses AIRR's special comparison scale, where 3 denotes acceptable and substantive work; it is not a school mark or a correctness probability. The separate ordinary overall grade below is **7.5/10**.

## Artifact and reviewer disclosure

- Paper: *An exact relaxation optimum in a one-parameter family of four quantum measurement bases*, Lluis Eriksson, 11 October 2026, working manuscript v1.
- Record: `ARR-2026-3RH54K4NC58MRSX3`.
- Version identifier: `arr:version:5e3ad684-c532-4912-81ee-e14c628d57b4`.
- SHA-256 verified from the supplied PDF: `dc55322c19116a9a51ac89ce359717a782f126bcb1310960b99301ed0d09c313`.
- Assessment timestamp: 2026-10-11T14:02:04.459225+00:00.
- Requested provider/model/effort: **OpenAI / gpt-6-astra / xhigh**. These are the runtime-requested identifiers supplied for this review. No separate signed backend/configuration metadata was available to this reviewer, so exact routing and effort are not independently certified.
- Prior participation by this reviewer model: **unknown**. The manuscript declares substantial OpenAI Codex assistance but does not identify the prior exact model. I do not infer that model.

This review began in a fresh delegated conversation supplied with the scientific inputs and rubric. I did not consult other referee reports, prior scores, parent or sibling review folders, author development history, Codex chats, or saved user memories. The mandatory disk-storage instruction required reading `D:\LEEME.md`, an administrative filesystem/project index, before creating files; it was not used as scientific evidence. The workspace is shared, and I cannot technically guarantee workspace or memory isolation or statistical independence. Fresh context and withheld reports are procedural controls, not proof of independent model errors.

I read all seven PDF pages through `pypdf` extraction, saved as `pdf-extracted.txt`, and read the complete TeX source. I checked mathematical content rather than conducting a rendered-page typography audit. The supplied PDF hash matches the locked identifier. I read and executed the supplied `verify.py` and inspected `requirements.txt`. The source manuscript and supplied verifier were not modified. This report assesses the original artifact, not an amended paper.

## Overall assessment

The manuscript establishes a valid exact calculation for a constrained problem. Its strongest contribution is the complete spectrum for the specified branch of the RLE subfamily and the resulting unique optimum. The comparison with geometric distance is correct and concrete. The product-vector ceiling is a useful, clean complementary result, although its short trace argument is not evidence of a broad new technique.

No global optimality, resolution of the dimension-six MUB problem, advantage at fixed laboratory cost, or optimality under variable probabilities follows. The paper generally states these limitations accurately. The rate increase over the geometric optimizer is about **0.216%**, while the separate comparison with the sharp product-vector ceiling is exactly **9.5%**. Both figures concern the normalized event model.

## Findings by claim

### Section 2: dynamics, sharp exponent, and Gram correspondence

The Poisson-series expression is valid in this finite-dimensional setting. Each dephasing map is a Hilbert-Schmidt orthogonal projection, and their convex average is self-adjoint, positive semidefinite, trace preserving and unital. The traceless subspace is invariant. Consequently, its largest channel eigenvalue determines the slowest semigroup exponent.

The asserted sharpness for density matrices is sound. The channel preserves adjoints, so a real eigenvalue has a nonzero Hermitian eigenoperator after taking a nonzero Hermitian or anti-Hermitian part. Such an eigenoperator is traceless, and a sufficiently small real multiple added to `I/6` gives a valid state. There is no hidden infinite-dimensional regularity or ergodicity assumption.

For traceless `X`, summing `v_jk Tr(v_jk X)` over the six vectors of one basis gives exactly `E_j(X)`: the identity correction vanishes because the basis probabilities sum to `Tr X = 0`. Thus the frame operator is `4T` on the traceless space. Equality of nonzero spectra of the synthesis/analysis products then justifies equation (5). The complex traceless space has dimension 35; equivalently, its Hermitian real form has real dimension 35. The manuscript does not confuse these dimensions with the 24 Gram coordinates.

### Equations (6)–(11): bases, parameter branch, and generic overlaps

The original basis matrices agree with the attributed RLE parametrization. The factors on the left are diagonal phases. The central block matrices have orthogonal rows because the block phases sum to zero and both two-dimensional building blocks satisfy `FF*=HH*=2I`. The prefactor is correct.

For `u` in `[1/4,1]`, the square roots and phase branch are well defined, and

`1-q^2 = (1-u)(4u-1)/u`.

There is no singular endpoint: `u` stays positive. The chosen branch is sufficient for the theorem; the theorem does not require an unproved equivalence with every other phase branch.

The most important algebraic dependency is the claim that all three noncanonical overlap matrices have the stated blocks throughout the interval. An optimum-only calculation cannot verify that claim. I independently constructed all original matrices in the exact algebra generated over `Q(u)` by

`sqrt(1-u), sqrt(u), sqrt(4u-1), sqrt(3), i`,

using

`t = (1-i sqrt(3))(1-2u+i sqrt(1-u)sqrt(4u-1))/(2 sqrt(u))`.

The independently written script reduces these radicals algebraically and checks every entry of all three unitarity relations, every canonical flatness relation, and all 108 entries of `P12`, `P23`, and `P31`. Every identity passes. This verifies the link from the original bases to the polynomial Gram matrix, rather than merely diagonalizing an assumed Gram ansatz. The identities extend to the closed interval by continuity; the sole parameter denominator is nonzero there.

A useful short completion of the manuscript's omitted arithmetic is that the companion amplitude has modulus squared `36(1-2u)^2`, while each of the other four amplitudes has modulus squared `12(1-u)(4u-1)`. Dividing by 36 gives exactly `B` and `C`. For example, write `b=sqrt(u)` and `r=sqrt(1-q^2)`. Then `cos(theta_t-2pi/3)=-q` and `cos(theta_t)=q/2+sqrt(3)r/2`; substitution in the directly multiplied amplitudes yields these squares. Row normalization alone would not establish equality of the four remaining entries, but the actual equality is correct.

**Finding:** correct; add a little algebra or a generic original-matrix verifier for readability, not to repair a false theorem.

### Theorem 3.1: complete Gram spectrum

The proof's invariant sectors and multiplicities are correct. The canonical basis contributes one zero and five ones. The three remaining constant vectors account for three more zeros.

On the nine-dimensional antisymmetric sector, the off-diagonal blocks are `sI`, `sR`, and `-sR^2`. With `W=diag(I,I,R^2)`, the transformation is explicitly `W* G W`; it produces the signed scalar triangle tensor `I3`. The scalar matrix has eigenvalue `1-2s` on the vector `(1,-1,1)` and eigenvalue `1+s` on its two-dimensional orthogonal complement. Hence the multiplicities are three and six.

On the symmetric zero-sum sector, the all-ones contributions disappear and the same transformation gives the scalar matrix with diagonal one and off-diagonal `k`. Its constant-vector eigenvalue is `1+2k`, and the other two eigenvalues are `1-k`. The remaining coordinate sector has dimension two, giving multiplicities two and four. The total dimension is `4+5+3+6+2+4=24`.

Endpoint collisions cause no exception to the formula. At `u=1/4`, `s=1/2` and `k=1`: the Gram rank is 13 and the gap is `1/4`. At `u=1`, `s=-1` and `k=1`: the Gram rank is 10 and the gap is again `1/4`. The phrase that multiplicities add correctly handles these degeneracies.

**Finding:** correct over the complete stated closed interval.

### Theorem 4.1: unique sharp subfamily optimum

The lower bound on `h=max(0,-2s,s,2k,-k)` covers the whole interval with no missing boundary. On `[1/4,3/5]`, `s'=(4/3)(1-4u)<=0` and the endpoint value `13/75` is strictly greater than `2/25`. On `[3/5,7/10]`, the factorization of `-k-2/25` is nonnegative with equality only at `7/10`. On `[7/10,1]`, the factorization of `-2s-2/25` is likewise nonnegative with the same unique equality point.

At that point `s=-1/25`, `k=-2/25`, and every term in the maximum is at most `2/25`. Thus the lower bound is attained and

`gamma = 1 - (1+2/25)/4 = 73/100`.

This is a global optimum on the specified one-parameter interval, even though it is not an unrestricted global optimum over basis choices. Equal weights and event rate one are essential to the numerical value, and are explicitly fixed.

**Finding:** correct, including uniqueness.

### Corollary 4.2: algebraic construction and channel spectrum

The specialized phases match `u=7/10`, and `A=3/25`, `B=4/25`, `C=9/50`. The nonzero channel eigenvalues and multiplicities are

| Eigenvalue | Multiplicity |
|---|---:|
| `21/100` | 2 |
| `24/100` | 6 |
| `1/4` | 5 |
| `27/100` | 7 |

Their total multiplicity is 20. There are consequently 15 zero eigenvalues on the 35-dimensional traceless space. On the full 36-dimensional space, one additionally has the scalar eigenvalue one. The author verifier checks the optimum directly in exact radicals, and my separate full-channel implementation agrees.

**Finding:** correct; no zero-eigenvalue counting error.

### Distance comparison and the numerical geometric optimizer

The normalization `1/30` is right: six unordered pairs are averaged and each individual dimension-six squared distance has defect normalization `1/5`. Expansion of the three noncanonical defects gives the quartic in equation (17). The nonzero derivative at `7/10` excludes distance maximality at this interior point. Both rational table entries and both exact differences are correct.

There is one minor numerical error. The unique real root of

`112u^3-192u^2+111u-22=0`

is

`u = 0.694552035120092...`,

not `0.6945524` to the displayed precision. At seven decimal places it is `0.6945520`. The associated gap is `0.7284249711786929...`, so the quoted `0.728425` is correct. The cubic is strictly increasing on the real line because its derivative `336u^2-384u+111` has negative discriminant and positive leading coefficient. Thus there is no root-selection ambiguity. This typo does not affect any exact statement or the conclusion of the table.

**Finding:** exact comparison correct; correct the displayed decimal.

### Proposition 5.1: arbitrary mixtures of product-vector bases

The local compression argument survives the strongest stated quantifier. It does not assume that a product-vector basis is a Cartesian product of two local bases. For every pure product projector,

`Q_V(Pi) = (rho_A-I2/2) tensor I3/3`,

whose squared Hilbert-Schmidt norm is `(1/2)(1/3)=1/6`. Summing over six projectors gives compressed superoperator trace one. Every probability mixture preserves this trace. The largest Rayleigh quotient of the compression on a three-dimensional space is at least `1/3`, and the largest eigenvalue on the full traceless space is at least that value. Invariance of `V` under `T` is not required. Therefore `gamma<=2/3`.

I also constructed a conditional orthonormal product basis in which the qutrit basis depends on the qubit label. Its compressed trace is one, as predicted. This directly probes the distinction emphasized in the proposition.

The proposed sharpness example consists of 12 equally weighted product bases, obtained independently from the three qubit Pauli bases and four qutrit MUBs. Its full channel has scalar eigenvalue one and traceless eigenvalues `1/3` with multiplicity 3, `1/4` with multiplicity 8, and `1/12` with multiplicity 24. I independently constructed these bases and verified this spectrum. The sharpness example does not claim to use four bases; the proposition allows any number, so there is no quantifier mismatch.

**Finding:** correct and sharp in its stated class. The relative improvement `(73/100)/(2/3)-1=19/200` is exactly 9.5%.

### Equation (19): unrestricted four-basis bound and its equality condition

For any four uniform dephasing projections on the traceless space, a unit vector in any one range has quadratic form at least one under their sum. This proves `lambda_max(T)>=1/4`, hence `gamma<=3/4`. Equality forces every other positive projection to annihilate every vector of each range, so the ranges must be mutually orthogonal. Their centered rank-one-projector overlaps are then zero, which is precisely pairwise mutual unbiasedness. Conversely, mutually unbiased bases attain the equality.

The lower bound `73/100` follows from the constructed example. No claim that this equals the unrestricted supremum is supported, and the manuscript does not make it.

**Finding:** correct; this is established background rather than a new unrestricted result.

## Computation and reproducibility

The executed environment was Python **3.12.6**, SymPy **1.14.0** and NumPy **2.5.1**. The author requirements specify SymPy 1.14.0, which matches the actual run.

The unchanged author verifier completed **20 exact checks**, including its generic polynomial-Gram characteristic polynomial, optimum-only original-basis construction, unitarity, rank, eigenvalues, interval identities, and exact distance comparison. Its outputs `verification.json` and `exact-gram.json` were generated during this review. They are evidence of this review-time execution, not evidence that these output files existed in the published release or that any earlier author run occurred exactly as described.

The independent script `independent_verify.py` does not import the author verifier. It completed **15 groups of checks**, including exact generic original-basis identities, numerical construction of the full `36 x 36` channel at **209** parameter values, an explicit 12-basis product construction, and a conditional product basis. The largest discrepancy between full-channel numerical eigenvalues and the claimed spectrum was **1.2212453270876722e-15**. Sampled parameters include both endpoints, points within `1e-12` of the endpoints, the optimum, and the rational comparison point. Numerical sampling supplements the generic exact argument; it is not the proof of uniqueness or of a continuum identity.

The author-supplied script checks the generic spectrum of a polynomial Gram ansatz, but links the original bases to that ansatz directly only at `u=7/10`. That is an important limitation of its test coverage. My generic check addresses it, and the manuscript's analytic multiplication statement is true. The limitation is therefore not an unresolved invalidator of Theorem 3.1.

The review request explicitly states that `verify.py` and `requirements.txt` were **not included in published v1**. Section 6 nevertheless describes an accompanying supplement and `verification.json`. This is an availability/provenance inconsistency in the release. The supplied source makes the result reproducible for this referee, but it must not be credited as a publicly packaged v1 supplement. I did not inspect other AIRR pages or reviews to reconstruct a release history.

Preserved evidence in this assigned directory:

- `assessment.json`: original AIRR JSON object.
- `report.md`: this report.
- `pdf-extracted.txt`: all seven canonical PDF pages as extracted text.
- `author-verifier-run.txt`, `verification.json`, `exact-gram.json`: actual author-code run and generated outputs.
- `independent_verify.py`, `independent-verifier-run.txt`, `independent-verification.json`: independent method, execution log and results.
- `rle-2011.pdf/.txt`, `zhu-hayashi-2019.pdf/.txt`, `roy-scott-2007.pdf/.txt`: retrieved primary literature and extracted text.
- `retrieve_primary_sources.py`: source-retrieval script.

No formal proof-assistant verification was performed. Exact symbolic arithmetic still depends on the mathematical transcription and implementation; separate analytic checks and a separate complex-number implementation reduce, but cannot eliminate, common errors.

## Novelty and literature

The bases, parameter relation and mean-distance objective are already in **Raynal, Lu and Englert (2011)**. I compared equations (5)–(11) and (19)–(22), including the single-parameter restriction and the geometric cubic. The new manuscript's attribution is accurate. Their overlap structure is already very explicit, so the present diagonalization is a short additional analysis rather than a new basis construction. [RLE primary paper](https://arxiv.org/pdf/1103.1025)

**Zhu and Hayashi (2019)** give the uniform-projector spectral bound and its orthogonality equality condition in Lemma 3, and connect the corresponding orthogonal ranges to MUBs in Propositions 1–2. Under vectorization, their conjugate-basis verification operator is the same matrix as this measurement superoperator. This makes the general spectral objective and unrestricted bound established background. I did not find the specific RLE `73/100` optimization in that work. [Zhu–Hayashi primary paper](https://arxiv.org/pdf/1901.09772)

**Roy and Scott (2007)** explicitly use centered projectors and tight operator frames on the traceless Hilbert-Schmidt space, notably equations (5.2)–(5.6), and discuss weighted unions of orthonormal bases. This is a useful more direct citation for the framework. It does not establish the narrow RLE optimum reviewed here. [Roy–Scott primary paper](https://arxiv.org/pdf/quant-ph/0703025)

**Ippoliti (2024)** treats measurement-channel eigenvalues in locally entangled classical-shadow constructions. This supports the manuscript's general context, but the objective and ensembles differ; it is not a direct predecessor of the exact optimization under review. I consulted the article's channel discussion and Section 2.2. [Ippoliti primary article](https://arxiv.org/html/2305.10723v2)

For **Wootters and Fields (1989)** I consulted the publisher's abstract and bibliographic record, not the full paywalled article. Its explicit prime-power MUB construction supports the standard local constructions cited by the manuscript; the concrete qubit/qutrit example was also reconstructed directly here. [Publisher record](https://www.sciencedirect.com/science/article/pii/0003491689903229)

The author's separately cited diffusion manuscript is used only for motivation and is not a theorem dependency. I did not inspect that author's prior manuscript or development history. No correctness conclusion here relies on it.

Focused searches included the exact RLE title with relaxation/spectral terms, combinations of Raynal/Englert with spectral gap, and the distinctive values `73/100` and `0.73` with mutually unbiased bases. Broader measurement-channel/dephasing searches and primary-domain searches were also tried. Many results were irrelevant. No earlier identical optimization was identified in the primary papers examined, but this is **not an exhaustive priority certificate**, a systematic citation-network audit, or evidence that no equivalent optimization exists under different terminology.

The plausible new contribution is therefore the explicit signed-block spectrum and its exact minimax optimizer, with the rational distance/rate reversal as a compact illustration. I assign only moderate novelty confidence. The product-vector ceiling is valid, but its simplicity and relation to familiar local-purity/frame constraints warrant caution about claiming it as a strong independent novelty result.

## Required minor changes and optional improvements

Required before accepting the paper as a complete reproducible release:

1. Correct Section 6's availability wording or issue a properly versioned public supplement containing the actual source, requirements, and clearly dated run output. Preserve the distinction between what accompanied v1 and what was supplied later for review. This is a release correction, not a demand to alter the valid mathematics.
2. Replace `0.6945524` by `0.6945520` at seven decimal places, or give the more accurate root above.

Optional improvements:

1. Add the short `B,C` overlap derivation, or include generic original-matrix verification in the supplement. This would remove the largest avoidable verification burden.
2. Cite Roy–Scott for the centered operator-frame formalism and make the exact vectorization connection to Zhu–Hayashi explicit.
3. Explain the small improvement over the geometric optimizer alongside the separate 9.5% product-class comparison, so readers can assess its practical scale.
4. Consider unequal probabilities or the full two-parameter RLE family as further work. These are possible extensions, not missing assumptions or requirements for the stated theorem.

There are **no unresolved material objections** capable of invalidating the main results in this exact version. The listed adverse findings remain relevant to accuracy, release quality and significance.

## Separate ordinary 0–10 grading

| Criterion | Ordinary grade | Basis |
|---|---:|---|
| Mathematical correctness | **9.5/10** | All substantive claims withstand analytic reconstruction and direct checks; one harmless decimal error remains. |
| Originality | **6.0/10** | A plausible new exact optimization within a known explicit family; construction and general method are prior work. Priority remains incompletely searched. |
| Scientific significance | **4.5/10** | Useful specialized example and bound, with limited breadth and no demonstrated implementation gain or unrestricted optimality. |
| Clarity and exposition | **8.5/10** | Clear scope and concise proofs; overlap details and supplement provenance need improvement. |

An ordinary overall grade of **7.5/10** results, rounded from 7.475, using weights 40% correctness, 25% originality, 20% significance and 15% clarity. These are qualitative referee judgments, not calibrated measurements. A reasonable uncertainty is about half a point overall, with larger uncertainty in originality and significance than in the checked algebra. The score would change if an earlier identical result were found; successful symbolic checks do not themselves establish novelty.

This grade is fully separate from the AIRR significance score **3.20/10**. The recommendation is **minor revision**, appropriate for a short specialized mathematical/quantum-information note, without an implication of acceptance at any particular journal.
