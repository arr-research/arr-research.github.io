# First exact-PDF scientific assessment

Artifact: Product Marginals and Density-Moment Thresholds for Ising Transfer Kernels, Lluis Eriksson, 13 November 2026, 13 pages.
Record ARR-2026-7KV9Y9ASX48H7A7N; version v2; version ID arr:version:84411507-f593-401a-8f5e-1fff17e28dcc.
PDF SHA-256: 3a379495c22afc732f17d6e855a9129a3c4173d9ccd28c1138c36e8c57df26c3; 360788 bytes.

## Decision and calibration

Millennium score: **5.00 / 10.00**. Public overall rating: **5 / 10, Very good**.
Recommendation: **minor_revision**, meaning suitable as a transparently labelled working paper with minor documentation improvements; this is not an editorial admission decision.

I found no mathematical error or unresolved objection that invalidates a main theorem in this exact manuscript. The proof chains for the code construction, stationary marginals, parity control, supercritical moment bound, and subcritical two-tilt construction withstand the analytical checks described below. The complementary strict moment regimes are the strongest part of the work. The finite code construction is also a useful synthesis, particularly its simultaneous statement about the weighting law and the actual Perron stationary law.

This is a notably good, inspectable finite-dimensional research paper, rather than a demonstrated field-shaping result. The ingredients are classical, external priority of the joint results remains unresolved, the critical exponent is excluded, and consequences for local Gibbs dynamics or physical mass gaps are absent. These limitations constrain significance and novelty; they do not constitute disproofs of the stated theorems. The overall score is a research judgment on the supplied high-ceiling scale, not the average of the five criterion stars, not a probability of truth, and not a school grade.

Criterion stars, on their separate 1-5 scale:

- Correctness confidence: **4/5**. Complete analytical scrutiny of the main chains found no invalid inference; the essential forward and reverse hypercontractive conventions were checked against a primary source. This is still one involved model assessment, without independent expert or formal verification.
- Rigor and completeness: **4/5**. Quantifiers, support zeros, rounding, sign normalization and finite spectral constants are handled explicitly. Completeness applies to the two strict regimes actually stated; the endpoint is expressly unresolved.
- Novelty relative to checked sources: **3/5**. The joint marginal/many-mode statement and the matching strict moment regimes are credible contribution candidates. The checked literature does not establish their priority; familiar coding, hypercontractive and matrix ingredients should not be counted as new results.
- Significance if correct: **3/5**. Useful separation of marginal information, density moments and normalized transfer spectra in a precise model class. Wider applications and sharp endpoint behavior are not established.
- Reproducibility/independent inspectability: **4/5**. Exact PDF, TeX, extraction, all page images and complete finite analytical proofs are available in the verified packet. No numerical or formal proof replay was performed. The paper's public source-package pointer could be more precise.

## Actual assessment context and limits

This was the first and only numerical assessment performed by this reviewer for these PDF bytes. No desired score, previous assessment scores, other agent reports or author rebuttals were used. No resampling was performed.

Provider/session: OpenAI/Codex. The exact served backend and reasoning setting are not exposed. The supplied context declares manuscript involvement by the model family, and technical workspace/memory isolation is not verified. I therefore use **involved_in_manuscript** and make no independent-review claim. The visible assignment was a fresh review task, but that is not proof of isolation. The author owns and administers AIRR. Working-paper deposit, editorial acceptance, model review and human peer review are separate.

Permitted local operations were reading, hashing and retention. No mathematical program, numerical test, Lean check, compiler, manuscript build, or scientific runtime was executed. Local file hashes are artifact checks, not scientific tests. The 13 supplied PNGs were inspected with the image viewer; I did not independently regenerate them from the PDF. Their provenance is supported by the supplied manifest and build report, not independently re-proved by this review.

The supplied input manifest itself hashes to 134f377bcec87e51a5a50944646621171ade891b695741e56a2721a54b649e18. All 24 listed files matched both byte lengths and SHA-256 values. The exact PDF length/hash above matched. A retained raw verification manifest records these checks.

Read scope: operator-context.txt, native-rubric.txt, response-schema.json and identifiers.json before assigning a score; the full exact manuscript TeX and extraction, with targeted rereads where tool output was shortened; all 13 page PNGs; the full supplied parity predecessor; the fusion/concentration, projective comparison and least-correlated-pair passages of the congruence predecessor; source294A.txt; and the provenance header/build metadata of report.json. The latter was not treated as scientific endorsement. Unrelated historical formalization details of the congruence predecessor were not audited. No author development workspace or omitted source audits were read. Global storage instructions and the PDF handling instructions were also read for operational compliance.

## Claim-by-claim scientific findings

### 1. Transfer and noise conventions (pp. 1-2, 6-7)

The one-bit kernel has eigenvalues 1+q and 1-q, with q=exp(-2 beta) in (0,1). Thus positive definiteness, tensorization and the product ratio rho=tanh(beta) are consistent. The conversion
A_mu = 2^{-L}(1+exp(-2 beta))^L T_r
for mu=2^{-L}r is correct. A common scalar affects neither eigenvalue ratios nor the gap under review.

Entrywise positivity is not being confused with positive semidefiniteness: both hold for strictly positive weights here, while zero weights leave a positive definite principal block on their nonempty support and zero eigenvalues outside. The use of the second largest eigenvalue, rather than an absolute-value convention for negative modes, is valid for these positive semidefinite operators. L>=1 ensures the ambient matrix has at least two eigenvalue slots even for one-point support.

### 2. Coding existence and finite concentration (Lemma 2, Proposition 3, Theorem 1; pp. 2-4)

The random-generator argument accounts for rank failure: a nonzero message producing zero is among the forbidden low-weight events. The dual event uses uniformity of Gw for each fixed nonzero w, and no independence between these events is required for the union bound. The inclusive binomial entropy bounds dominate the strict primal failure event. Floors and ceilings cause no omitted integral boundary case.

The strict entropy inequalities and k=ceil(RL) make both exponents negative for all sufficiently large L. Their eventual gate is an actual existence condition at each such L, not a claim only along a subsequence. Dual-distance exclusion makes every indicated column set independent; therefore the corresponding coordinate projection of the code is onto, giving uniform labelled marginals.

For the positive admixture, the code block is exactly a M_CC with a>=(2m)^{-1}. Its off-diagonal norm is bounded by s=(m-1)exp(-2 beta d_C). Interlacing supplies a lower bound for all first m eigenvalues, while the outside block has norm at most its trace, at most eta. The Frobenius estimate for the cross block is at most sqrt(eta); the norm of the symmetric off-diagonal dilation is that norm, not twice it. These facts yield the displayed finite bound 2s+2m(sqrt(eta)+eta). Its validity does not require 1-s>0 or a useful upper bound below one at small L.

The selected R is positive, strictly below 1-h(1/4), and satisfies R log 2<=beta/4. The rate gamma=beta/2-R log 2 is therefore at least beta/4. The ceiling costs at most a factor two in m. With eta=exp(-2 beta L)/m^2, the two contributions are bounded by 4 exp(-gamma L) and 3 exp(-gamma L), respectively. The constant seven and every asserted eigenvalue index are justified. There are m-1 nonleading slow modes; coincidence of their eigenvalues is neither needed nor claimed.

### 3. Perron stationary marginals and information obstruction (Lemma 4, Corollary 6; pp. 5-6)

Code translations preserve both the weight and Hamming kernel. Uniqueness of the normalized positive Perron vector makes it invariant under those translations. Surjective coordinate projections then force the same product marginals for its square. This establishes the actual stationary law assertion without making the generally false identification pi=mu.

The Doob formula has row sums one, the displayed detailed-balance identity holds, and diagonal similarity gives precisely the normalized transfer spectrum. The certificate corollary follows from equality of the literal input tuples at fixed L and beta. Its scope is correctly limited: no assertion that every marginal functional vanishes, no assertion that the uniform chain is slow, and no prohibition against certificates using additional structural information.

### 4. Parity negative control (Proposition 5; pp. 5-6)

Similarity to P_beta D_t^2 is legal because |t|<1. Multiplication by full parity exchanges complementary characters, and the stated nonsymmetric coefficient blocks have the correct ordering, trace and common determinant. Complement pairs exhaust the spectrum with multiplicity.

The largest upper root belongs to the empty/full pair. The largest proper upper root is at s=1; the lower root of the empty/full pair is at most rho^L and cannot overtake it. This remains valid for L=2 and t=0, including repeated eigenvalues. The root-to-trace monotonicity gives the ratio bound, and maximizing rho(1+b)/(1+rho^2 b) for b=rho^{L-2}<=1 gives tanh(2 beta). L=2 and t approaching one prove sharpness as a supremum.

The supplied parity predecessor's actual conditional heat-bath block calculation supports the comparison being made. It is a different operator, with different gap normalization. The current manuscript properly refuses to infer transfer slowdown from heat-bath slowdown.

### 5. Density cap and the sign-part argument (Theorem 7, Corollary 8; pp. 7-8)

The test vector sqrt(r) has unit L2(u_L) norm. Its Rayleigh quotient is <r,P_rho r>>=1 by Walsh expansion. The cap supplies lambda_1<=B. For nonzero lambda_2, an eigenvector is supported where r>0, and orthogonality to the positive Perron vector forces both signs.

After normalizing the two sign parts separately, positivity gives lambda_2 h_+<=T_r h_+ and the analogous negative-part inequality. These hold even off their sign supports. Multiplication by sqrt(r) is legitimate with zeros; no division by r is used.

The ordinary hypercontractive exponent q_*=1+rho^{-2} is correct. For the reverse bilinear estimate, p_*=1-rho and its negative conjugate satisfy the stated time threshold exactly. The uniform Boolean semigroup normalization is essential: the factor one-half in its reverse inequality is supported by equations (1.1)-(1.2) of Mossel, Oleszkiewicz and Sen. Regularizing the input functions before passage to zero is sufficient and avoids taking a negative moment of a function with zeros.

The interpolation below exponent one is an application of ordinary Holder to positive powers with valid conjugate weights; it does not presume a triangle inequality for a quasi-norm. Its exponent simplifies to e_rho=(1+rho^2)/(1-rho)^2 as claimed.

The compression need not be an invariant subspace. It still has the coefficient vector of the actual eigenvector as an eigenvector. For sign masses a,b with a^2+b^2=1 and cross entry D, its other eigenvalue is lambda_2+D/(ab). The variational principle therefore gives lambda_1-lambda_2>=2D without losing a factor for a very small sign mass. The final constant B^{-1}(2B)^{-2e_rho} is valid (and conservative). The alternate lambda_2<lambda_1/2 case and singleton support are covered. Rearranging the bound gives Corollary 8's necessary density growth; no converse is claimed.

### 6. Supercritical moments (Theorem 9; pp. 8-9)

The thresholds of both forward inequalities are correct for A=1+rho and t=1+1/rho. The exponent Q=st/(s+t) exceeds A exactly when s>(1+rho)/(1-rho). Likewise A_0=2s/(s+1)>A. Holder multiplication by sqrt(r), probability-space norm monotonicity and the square-root noise identity yield 1<=lambda_1<=B.

For each sign part, the eigenvector inequality and Holder yield ||f||_Q<=(B/lambda_2)||f||_A, while the quadratic form gives ||f||_A>=sqrt(lambda_2). Interpolating between p=1-rho and Q gives exactly
e=2 rho s / ((1-rho)(s(1-rho)-1-rho)).
Applying the reverse bilinear inequality and the same compression argument gives the asserted min{1/2,(2B)^{-2e}}. There is no lower-density assumption hidden in the proof.

This argument fails to supply a bound at Q=A: its interpolation exponent diverges. That explains why the proof establishes only the strict supercritical regime; it does not show the endpoint assertion is false.

### 7. Subcritical two-tilt construction (Theorem 10; pp. 9-10)

For fixed small positive delta<1, the one-bit normalization n>1, Ls norm one, and mean m=1/n are consistent. Tensorization and Minkowski, which is used only at s>1, yield the advertised density moment bound. Z_L<=1+2 epsilon=B gives the pointwise floor 1/B. This holds for every L>=1 and every fixed B>1.

The AA* versus A*A step moves the density into a linear expression; it is not an unjustified replacement of sqrt(r) by a sum of square roots. The matrices H_+ and H_- are positive definite, conjugate and have the stated simple top eigenvalue. The local derivative calculation gives (log kappa)''(0)=2rho/(1-rho)-(s-1)>0 exactly in the strict subcritical range. Choosing one sufficiently small delta independently of L is therefore justified.

The norm omega is strictly below kappa. Equality would require a common top eigenvector of the two one-bit matrices, impossible because their difference is invertible. Tensor square roots and operator norms then give the cross Gram block norm omega^L. In the doubled Gram matrix, the diagonal part has two leading eigenvalues kappa^L, and the perturbation has norm omega^L. The extra zero eigenvalues of C*C do not alter its first two eigenvalues relative to CC*, since the latter is positive definite of dimension at least two. This is the crucial second-mode argument; one-channel top-norm growth alone would not suffice.

Adding positive semidefinite P_rho of norm one and dividing by the positive Perron lower bound epsilon kappa^L produces exactly
2(omega/kappa)^L + epsilon^{-1}kappa^{-L}.
The normalization Z_L cancels. Both bases are below one, even if omega itself exceeds one. Strict positive finite-size gaps and exponential collapse are compatible. No claim of product marginal matching for this tilted family is made.

## Primary-source comparison actually performed

These were targeted statement/convention checks, not exhaustive audits of every cited paper.

- [Mossel, Oleszkiewicz and Sen, arXiv:1108.1210v5](https://arxiv.org/pdf/1108.1210): checked the uniform Boolean forward and reverse inequalities (1.1)-(1.2), negative exponent allowance and tensorization discussion. They support the imported estimates, not the manuscript's full transfer-gap conclusions.
- [Brehm and Resch, ITCS 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.28/LIPIcs.ITCS.2026.28.html): checked the stated fast primal/dual code result, including its rate-one-half setting. It establishes stronger algorithmic coding achievements. It is not a substitute for every parameter of the manuscript's separate entropy proof.
- [Alon, Goldreich and Mansour](https://www.wisdom.weizmann.ac.il/~oded/PSX/agm.pdf): checked the limited-independence setup and scope. Its use as background is justified; it is not direct priority evidence for the dual-distance equivalence or the transfer theorem.
- [Miclo](https://perso.math.univ-toulouse.fr/miclo/files/2012/04/hyperboundedness.pdf): checked Theorem 1 and Proposition 11. Qualitative hyperboundedness of ergodic reversible Markov operators and the obstruction to a general quantitative second-eigenvalue bound are described accurately.
- [Wang, arXiv:1305.4460v6](https://arxiv.org/html/1305.4460v6): checked Theorem 1.1 and the Markov/invariant-measure setting. A family-uniform bound for the current congruences does not follow merely by naming that criterion.
- [Gross, arXiv:2412.20282v2](https://arxiv.org/html/2412.20282v2): checked the Riemannian operator setup and Theorem 2.2, including dimension-independent gap dependence and moments of exp(V), exp(-V). The manuscript correctly acknowledges this quantitative result. No identification of that additive perturbation with the logarithm of the present discrete congruence was established by this review.
- [Gluck, arXiv:1802.09422v6](https://arxiv.org/pdf/1802.09422v6): checked the essential-spectral-radius scope, differing spectral-gap definition and stated uniform essential-radius discussion. Those conclusions alone do not locate the second eigenvalue of an arbitrary finite matrix.

A brief broader search for combinations of noise operator, density, spectral gap, transfer perturbation, hypercontractivity, linear codes and Perron marginals produced no directly matching theorem inspected here. Search non-detection is not affirmative novelty evidence. Nonprimary search hits were not relied on. Aida's original theorem and a complete survey of discrete Feynman-Kac/positive-kernel perturbations were not checked. No claim of exhaustive originality clearance is warranted.

The supplied congruence predecessor already establishes antipodal concentration as a transfer obstruction, but not the present linear-order labelled marginals or exponential multiplicity. The supplied parity predecessor establishes the marginal obstruction for heat-bath dynamics, but the current parity calculation proves why that alone cannot imply the present transfer result. This is a substantive synthesis, not simply a change in the name of the operator. The strict moment dichotomy is the more distinctive candidate beyond those supplied predecessors.

## Objections, requested revisions and remaining limits

No unresolved material mathematical objection was found. No specific potential theorem-invalidating error is alleged.

The following are retained rather than silently omitted:

1. **Documentation revision, minor:** pp. 11-12 refer to retained analytical sources, a source package and a comparison recording incomplete Aida access, but provide no precise citation/location for each such item in the bibliography. Supply a permanent, version-bound source-package citation and identify the superseded two-point-spike supplement, or remove that historical sentence. The provided assessment packet did not contain the spike proof. The main Theorems 9-10 do not depend on it.
2. **Attribution improvement, minor:** a direct primary citation for the classical dual-distance/orthogonal-array equivalence would improve historical attribution. The current AGM caveat is honest, and Lemma 2 proves the needed fact, so this is not a proof gap.
3. **Novelty uncertainty, material to valuation but not validity:** the joint conclusions were not located in the sources inspected, but priority and possible deduction from stronger general perturbation results remain unestablished. A qualified external expert comparison is needed before making stronger originality or impact claims. The manuscript already avoids them.
4. **Critical endpoint, acknowledged scope limit:** neither theorem resolves s=s_c. The endpoint has bounded top norm by classical hypercontractivity, but that observation alone does not settle a normalized second-eigenvalue gap. Do not advertise a complete closed-endpoint classification.
5. **Uniformity limits, acknowledged:** beta/rho, s and B are fixed before L. There is no uniform collapse rate as s approaches s_c or B approaches one, and no gap bound uniform as rho approaches one. At B=1 the constant density case is separate and consistent.
6. **Application limits, acknowledged:** global weights and full-configuration Doob transitions are allowed. No fixed-range Gibbs, local heat-bath, entropy tensorization, spatial mixing, continuum field theory or Millennium-problem conclusion follows.
7. **Verification limit:** this is a single involved model's analytical assessment. Artifact integrity, supplied build provenance and legible renders do not constitute independent proof verification.

All 13 supplied pages are legible, consistently numbered and free of observed clipping, overlapping formulas, missing glyphs or placeholder source-commit text. Page 13 is a short reference continuation, which is harmless. The TeX/extraction scientific content agrees with the visible pages at the inspected formulas; extraction artifacts were resolved against the renders and TeX. The full PDF was not rebuilt during this review.

The recommendation and score above apply only to the exact bound PDF and retain all the qualifications and objections in this report.

