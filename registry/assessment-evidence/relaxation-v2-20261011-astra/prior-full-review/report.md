# Scientific referee report: ARR-2026-3RH54K4NC58MRSX3, v2

**Recommendation: minor revision.** The principal mathematical claims withstand this audit. One sentence on page 2 should explicitly identify the centered frame operator and its normalization. This does not require changing the main theorem, its proof strategy or the optimum. There are **no unresolved material objections capable of invalidating a main claim**.

**AIRR significance score: 3.00/10 (3 overall stars). Ordinary overall grade: 7.8/10.** These are different scales, with reasons and ordinary component grades below. This is an advisory model recommendation, not human editorial acceptance.

## Exact artifact, configuration and provenance

- Title: *An exact relaxation optimum in a one-parameter family of four quantum measurement bases*.
- Version identifier: arr:version:bc5c9f23-b39f-49a1-901c-16f499937caf.
- Canonical PDF: eight pages; SHA-256 **3c60aee3179b0f8d9c7a07960b7b600cca8cac70b5898f710676d8d124ea25ae**.
- Source SHA-256: **3e7a85407ba9364ef539506501e8ed222654078658021fad34d4b1f46bb8faec**.
- Provider/model/configuration: **OpenAI gpt-6-astra, xhigh**, as assigned for this review. No contrary runtime identifier was supplied; this is not an independently signed runtime attestation.
- Assessment timestamp: **2026-10-11T16:45:50+00:00**.
- Independence declaration: **involved_in_manuscript**. The operator states that this model supplied v1 feedback used in the revision and that the generic verifier adapts the earlier Astra algebraic approach. A new conversation does not erase that involvement.
- Scientific input directory: D:\Temp\airr\2026-10-11_relaxation-v2\reviews\astra. All new files are in this directory or its child referee-work.

I hashed the corrected PDF before assessment, extracted and read all eight pages using pypdf, and read the complete corrected TeX source and both supplied scripts. This was a text-and-source mathematical audit, not a rendered-page visual quality audit. A preliminary read preceded the operator's DOI-only correction; the final extraction, reruns, hashes and findings concern only the corrected artifact identified above.

I consulted the assigned scientific packet, the review instructions/rubric/addendum, mandatory D: disk instructions, and independently obtained primary literature. I did not read other reviews, earlier grades, saved memories, superseded-inputs, or parent/sibling scientific directories. I cannot independently certify host-level context isolation or hidden runtime controls. The supplied JSON files are author-run records, not independent referee findings.

The paper is an unreleased revised candidate. I verified the supplied packet's contents and internal consistency, not a public upload, licensing action, historical v1 release state or independent human acceptance. The author's operation of AIRR and the model participation are disclosed and do not replace outside scientific scrutiny.

## Findings on the mathematical claims

### Measurement process and Gram correspondence: correct, with one sentence to repair

The Poisson expansion of exp[t(T-id)] correctly models rate-one events with four equally likely nonselective projective measurements. Each dephasing map is an orthogonal Hilbert–Schmidt projection, so T is self-adjoint and positive, with eigenvalues in [0,1]. The stated sharp exponential contraction on traceless operators follows. A Hermitian eigenoperator for the largest traceless eigenvalue exists, and a sufficiently small perturbation of I/6 produces a state attaining that exponent.

For the synthesis map W whose columns are the centered projectors v_jk, the identities are

\[
G=W^*W,\qquad WW^*=4T|_{\mathcal H_0}.
\]

These two operators have the same **nonzero** eigenvalues and multiplicities. Therefore gamma=1-lambda_max(G)/4 is correct. The full channel also contains its scalar stationary eigenvector, and its traceless nonzero eigenvalues are those of G divided by four.

**Required minor correction:** On PDF page 2, immediately before Eq. (5), the sentence “Its nonzero eigenvalues agree with those of G” follows the displayed full-channel formula and its verification-operator interpretation. If “Its” refers to that full channel, the statement is false. The intended earlier centered frame operator is clear from the preceding derivation and subsequent formulas, so this is a local antecedent/normalization defect rather than a failed theorem.

Replace that sentence with, for example:

> The centered frame operator \(4T|_{\mathcal H_0}\) and \(G\) have the same nonzero eigenvalues, including multiplicity.

At u=7/10 the distinction is concrete: lambda_max(G)=27/25, whereas the full channel has largest eigenvalue 1 and largest traceless eigenvalue 27/100. The direct 36-dimensional channel check confirms this.

### Original matrices, phase branch and new overlap derivation: correct

The displayed matrices match the RLE construction and its one-parameter relation. The canonical basis is unbiased with each of the other three. The new derivation establishes B and all occurrences of C from the actual amplitudes, rather than deducing equality from row normalization.

I checked the three trigonometric identities, the phase factors in beta, delta and epsilon, and the five squared amplitudes by exact polynomial reduction under

\[
c^2+p^2=1,\qquad r^2+q^2=1,\qquad pq=1-2p^2.
\]

This independent calculation gives precisely 36A, 36B and 36C as appropriate, and verifies epsilon=conj(omega)conj(delta). The factors of 6 in the amplitudes and 36 in their probabilities are consistent. The alpha/beta exchange in the 31 block agrees with the published RLE placement.

The supplied generic verifier also passes after fresh execution: all original-matrix unitarity, canonical-unbiasedness and 108 noncanonical overlap-probability entries agree identically with the asserted blocks. I inspected its exact algebra and the transcription of its left diagonal phases. Its arithmetic is polynomial/rational reduction over Q(u), not a tolerance-based comparison.

The phase domain is correct. On the chosen interval, p is nonzero and the remaining radicals are real. In the algebraic implementation, possible denominators are powers of nonzero u and constants; no division by a radical that vanishes at an endpoint is required. Thus the identities extend to u=1/4 and u=1. Direct original-matrix evaluations at both endpoints also agree.

### Complete Gram spectrum, Theorem 3.1: correct

The plus/minus lines in each two-coordinate block are genuinely invariant for the full symmetric Gram matrix, including transposed off-diagonal blocks. The orientation of the cyclic permutation and of the conjugating matrix matters; I verified both sector conjugations with explicit symbolic 9-by-9 matrices.

The canonical block contributes 0 once and 1 five times. The antisymmetric sector contributes (1-2s) three times and (1+s) six times. The remaining symmetric sector contributes three basiswise constant null vectors, (1+2k) twice and (1-k) four times. These total 24 dimensions. The supplied characteristic-polynomial check reproduces the same spectrum over Q[u].

The endpoint degeneracies illustrate why the instruction to add coincident multiplicities is necessary. At u=1/4, the Gram rank is 13; at u=1 it is 10. The full channel spectra independently computed at those endpoints are

\[
u=\tfrac14:\{0^{(22)},(1/4)^{(5)},(3/8)^{(6)},(3/4)^{(2)},1\},
\]

\[
u=1:\{0^{(25)},(1/4)^{(5)},(3/4)^{(5)},1\}.
\]

Both give gamma=1/4. There is no overlooked stationary traceless mode or lost endpoint in the stated formula.

### Sharp optimum and explicit construction, Theorem 4.1 and Corollary 4.2: correct

The three intervals in the proof cover the entire closed domain. On the first interval, s'(u)=4(1-4u)/3 is nonpositive and s(3/5)=13/75>2/25. On the middle and last intervals the printed factorizations have the required signs, with equality only at 7/10. At that parameter the maximum of the five terms is indeed 2/25. This proves the **unique** maximum gamma=73/100 analytically; numerical sampling is not being used to establish optimality.

At the optimum, A=3/25, B=4/25, C=9/50, s=-1/25 and k=-2/25. The exact Gram rank is 20, so the traceless channel nullity is 35-20=15. Its remaining multiplicities sum to 20 and agree with Eq. (15). A separately assembled full channel has exactly the stated spectrum plus the scalar eigenvalue 1.

### Distance comparison and decimals: correct

The factor 1/30 correctly averages the dimension-six normalized squared chordal defect over six pairs. Each noncanonical pair contributes 6(A^2+B^2+4C^2)-1, giving Eq. (17). The spectral-moment relation

\[
\overline{D^2}=1-(\|G\|_F^2-20)/60
\]

also holds for arbitrary four bases because Tr G=20 and off-diagonal blocks are counted twice. It correctly distinguishes the second-moment objective from the largest-eigenvalue objective.

Both rational rows of Table 1, their distance difference 38513/750000000, the rate loss 29/20000 and the derivative -12/625 at 7/10 reproduce exactly.

Independently solving the stated cubic gives

- u_geo = 0.6945520351200921637448777526100098754...;
- gamma(u_geo) = 0.7284249711786930675328821296668640539...;
- relative rate gain = 0.216223891769980983007117729627... percent.

The published rounded values are correct. The cubic is strictly increasing because its derivative is 336(u-4/7)^2+9/7, so the unique real root is unambiguous. The derivative of the distance polynomial is -8/15 times that cubic.

### Product-vector ceiling and its sharpness: correct

For a product projector, the projected vector in V is (rho_A-I_2/2) tensor I_3/3 and has squared Hilbert–Schmidt norm 1/6. Summing six projectors gives compressed trace one. Positivity on the three-dimensional V gives a Rayleigh quotient at least 1/3; maximizing over the entire traceless space proves gamma<=2/3. This uses compression, not an unjustified invariance assumption, and works for arbitrary probability mixtures of complete product-vector bases.

As a separate check, I constructed a non-Cartesian product basis that uses different qubit Pauli eigenbases conditional on the three computational qutrit states. Its compressed trace is one even though V is not invariant; the norm of the off-subspace part is approximately 0.8164965809. This tests precisely the distinction addressed by the revised proof.

I also assembled all twelve tensor-product bases from the three Pauli bases and the four qutrit bases given by Z, X, XZ and XZ^2. Their uniformly averaged full-channel spectrum is

\[
\{1,\ (1/3)^{(3)},\ (1/4)^{(8)},\ (1/12)^{(24)}\}.
\]

Thus the twelve-basis example really attains gamma=2/3. The exact relative improvement (73/100)/(2/3)-1 is 9.5 percent. It is a comparison at fixed total event rate; no implementation-cost advantage follows.

### Unrestricted four-basis bound and equality: correct

A nonzero vector in one traceless dephasing range yields lambda_max(sum_j E_j)>=1. If equality holds, positivity forces every other projection to annihilate that range, giving pairwise orthogonality of all four traceless ranges. This is equivalent to mutual unbiasedness; the converse follows immediately. Continuity on compact U(6)^4 ensures attainment, so the stated equivalence between the unrestricted value 3/4 and existence of four MUB is valid.

The explicit construction supplies the lower bound 73/100. Neither this argument nor the new checks determine the unrestricted maximum or the full two-parameter optimum. The abstract, theorem quantifiers and limitations maintain the proper scope.

## Computations actually performed and their limits

I copied paper.tex, verify.py, verify_generic.py and requirements.txt into referee-work and ran the scripts there. The author originals and dated JSON outputs were preserved.

| Check | Actual result |
|---|---|
| Supplied verify.py, fresh run | All 20 exact checks pass |
| Supplied verify_generic.py, fresh run | All 10 exact check groups pass |
| New independent_audit.py | All 26 reported groups pass |
| Original matrices and full 36-by-36 channels | 305 parameter values, including both endpoints, 7/10, 139/200 and the geometric optimizer |
| Largest full-channel spectral discrepancy | 1.78e-15 |
| Largest Gram spectral discrepancy | 4.22e-15 |
| Largest original overlap-probability discrepancy | 9.99e-16 |
| Largest distance discrepancy | 1.05e-14 |
| Twelve-basis product-spectrum discrepancy | 3.89e-16 |
| Author inputs after checks | All eight SHA-256 hashes unchanged |

Environment: Python 3.12.6, SymPy 1.14.0, NumPy 2.5.1. The author scripts require only SymPy; NumPy is used only for my supplementary numerical checks. The generic exact checks and the analytic proofs carry the all-parameter assertions. Finite numerical sampling is supporting consistency evidence, not a proof of any global optimum.

The preserved independent script does not import either author verifier. Its exact amplitude checks use a different polynomial-ideal formulation, and its numerical check forms projectors and the full channel explicitly. This implementation separation does not erase the model's declared previous involvement. None of the checks is a proof-assistant certificate.

The retained initial independent-script log contains a failed comparison caused by a SymPy characteristic-polynomial generator dropping an assumption on my test symbol. After changing that test symbol, the entire script passes. This was a referee-test implementation issue, not evidence against the paper.

Saved reproducibility materials include the input hash manifest, all copied scripts, fresh verifier outputs and logs, independent_audit.py, independent-verification.json, independent-run.log, the PDF text extraction and primary-source retrieval notes. The supplied and freshly generated exact Gram matrices are identical. Author and rerun check lists and source hashes also agree.

## Primary literature and novelty assessment

I used primary sources to distinguish the new calculation from established construction and methods.

1. **Raynal, Lü and Englert (2011).** I downloaded the primary arXiv PDF and inspected the construction, cyclic overlaps, amplitude formulas, parameter relation and distance optimization, especially Eqs. (5)-(12) and (17)-(22). They supply the bases and geometric objective used here. Their specific polynomial distance optimizer agrees with the corrected manuscript. The submitted spectral optimum is not a new four-basis construction. [Primary paper](https://arxiv.org/abs/1103.1025).

2. **Roy and Scott (2007).** I verified the corrected DOI against the primary arXiv record and inspected the HTML discussion of centered operator frames and the POVM frame superoperator, including the material around Eqs. (57) and (60)-(63). This is prior framework, not new machinery of the present manuscript. The correct DOI is 10.1063/1.2748617. [Primary paper and DOI record](https://arxiv.org/abs/quant-ph/0703025); [operator-frame text](https://arxiv.org/html/quant-ph/0703025v2).

3. **Zhu and Hayashi (2019).** I downloaded the primary PDF and inspected the corresponding HTML. Lemma 3 and Propositions 1-2 give the projection bound, MUB equality condition and restricted-setting spectral optimization in verification language; Eqs. (43)-(44) display the relevant operator. Up to tensor-factor ordering, this is the vectorized measurement-channel matrix used here. Their discussion also gives the prime-dimensional bases used in the sharpness test. These connections are appropriately cited as prior work. [Primary paper](https://arxiv.org/abs/1901.09772); [relevant full text](https://arxiv.org/html/1901.09772v2).

4. **Ippoliti (2024).** I checked the primary arXiv abstract and publication metadata. It supports the general contextual connection to randomized entangled measurements; I did not obtain its full PDF and do not treat it as verification of a theorem in this paper. [Primary record](https://arxiv.org/abs/2305.10723).

Direct PDF retrieval of Roy-Scott and Ippoliti timed out; Roy-Scott's relevant HTML was available. I did not independently obtain the full Wootters-Fields article or audit the separately cited Eriksson block-diffusion manuscript. No present proof depends on the latter, and the local MUB sharpness construction was checked directly.

Focused searches using RLE/spectral-gap terms and the exact 73/100 constant did not identify a prior occurrence of this particular optimum. Search coverage was limited and some returned hits were irrelevant. This does not certify priority. I found no reason in the sources inspected to deny the plausibility of the narrow novelty claim: the explicit polynomial spectrum and its exact unique optimum on this already known subfamily.

The product ceiling is an elementary useful comparison, and the projector upper bound/equality case are standard. The new result remains a specialized exact calculation. The roughly 0.2162-percent rate increase over the geometric optimizer is mathematically clean but, by itself, does not establish a broadly important operational advance.

## Required and optional changes

**Required for a clean final scientific text:** Replace the ambiguous nonzero-spectrum sentence on page 2 by the explicit centered-frame statement given above. This is the sole required scientific-text correction identified in this audit. The underlying mathematics is satisfactory for the paper's narrow working-paper scope; no additional main theorem, global optimization, numerical experiment or proof-assistant formalization is required for that scope.

**Optional improvements:**

- Correct the header of verify_generic.py, which says numerical checks form a 36-by-36 channel although that supplied file performs only exact generic checks. The manuscript's own description of its exact checks is accurate.
- In the verification connection, cite Zhu-Hayashi's Lemma 3 and Propositions 1-2 explicitly to make the inherited bound and equality criterion easier to locate.
- Add endpoint ranks or a brief endpoint note if desired; the existing coincident-multiplicity convention already makes the spectrum correct.

The release text uses completed-publication language about the v2 bundle. In this review it is understood prospectively: the candidate packet contains the files, but public release is still pending. That operational condition should be fulfilled or the wording made prospective; it is not a mathematical objection. No historical v1 file availability was independently certified here.

## Ordinary grading, separate from AIRR

These ordinary grades assess this particular manuscript as a specialized mathematical working paper, not as a proposed breakthrough.

| Criterion | Ordinary grade /10 | Basis |
|---|---:|---|
| Correctness | 9.2 | Main claims survive exact, analytic and direct-channel checks; one localized antecedent/normalization sentence needs correction |
| Originality | 6.0 | Plausibly new explicit spectrum and optimum, built on an existing RLE family and established methods; priority search limited |
| Significance | 5.5 | Useful exact objective-comparison example and product-class benchmark; narrow family and no demonstrated implementation benefit |
| Clarity | 8.4 | Explicit phases, multiplicities, proofs and limitations are readable; page-2 wording and a code-header mismatch remain |

**Overall ordinary grade: 7.8/10**, using weights 40% correctness, 20% originality, 15% significance and 25% clarity (weighted value 7.805). This rewards the reliable mathematical core while retaining a substantial discount for limited breadth and modest novelty.

**AIRR millennium_score: 3.00/10**, rendered as **3 overall stars**. Under AIRR's supplied significance scale, this denotes acceptable and substantive work. It is not the ordinary grade above, a probability of correctness, or a claim of proximity to a Millennium Prize result.

My final recommendation is **minor_revision**, with **no unresolved material objections**. The mathematical results appear sound within the explicitly stated admissible family; the required correction is local and readily specified. The final editorial and release decisions remain human decisions.

