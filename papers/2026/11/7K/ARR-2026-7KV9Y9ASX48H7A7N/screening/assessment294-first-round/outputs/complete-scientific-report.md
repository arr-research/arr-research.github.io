# Complete scientific finding report: exact manuscript294A PDF

Reviewed artifact: *Product Marginals and Exponentially Slow Spectra of Positive Ising Transfer Kernels*, Lluis Eriksson, 13 November 2026, seven pages, 296958 bytes. SHA-256: `f6de607cb81d5f402735a21391b13e346bc85b12da44e07da0487edc7debf3df`.

Record identifiers supplied by the operator: ARR-2026-7KV9Y9ASX48H7A7N, v1, arr:version:250e87b3-dcd3-4b4d-bedc-6805a1049ba1. The operator calls these local draft identifiers, not evidence of a public record or native grant. This review confers neither AIRR acceptance nor human peer review.

## Verdict and complete score record

Recommendation: **minor_revision**. Millennium comparison score: **3.4 / 10.00**; nearest-whole-number overall rendering: **3 stars**. This means an acceptable, substantive contribution on the supplied comparison scale. It is not a probability, a school grade, a claim to a Millennium Problem solution, or an average of the criterion stars.

| Criterion | Stars, out of 5 | Basis |
| --- | ---: | --- |
| Correctness confidence | 4 | The analytical checks support every numbered result, including the finite bound, parameter specialization, stationary symmetry and parity ordering. Review is by an involved model, with no formal or independent certification. |
| Rigor | 4 | Main hypotheses, rounding, strictness and finite constants are explicit. A preliminary heat-bath sentence needs the L >= 2 qualifier and a fixed-rate convention. |
| Novelty | 2 | The joint conclusion is a plausible synthesis, but the components are classical and external priority is unestablished. |
| Significance | 3 | The construction is a useful obstruction to marginal-only gap certificates, with a substantial stationary-law strengthening, within a restrictive transfer setting. |
| Reproducibility | 4 | Exact inputs are identifiable, all packet hashes match, and complete proofs are available. This reviewer did not rebuild, rerender, execute mathematical tests, or verify the full production archive. |

**Unresolved material objections capable of invalidating a main claim: none identified in this review.** This is a bounded assessment, not proof that none exists. One minor potential error/domain ambiguity is preserved below. The native JSON is the complete, unaltered score response; no alternative rating was generated, compared or selected.

## Actual review scope and controls

The reviewer read the complete exact TeX and complete text extraction, visually inspected all seven supplied original page PNGs, and checked the canonical PDF and all 15 input-manifest members by byte length and SHA-256. The input manifest itself matches `384b764c1e9d283c5d6f395fed8a941e56452a3dcf5be0ab453da09fdaf39ad1`. The first combined text output was truncated; complete separate TeX and extraction reads followed. Another combined provenance/browser output was truncated; the complete builder and production manifest were reread separately. These truncations did not leave manuscript text unread.

The builder was inspected as text only. The production report and production manifest were read as provenance metadata. The outer input manifest has 15 entries: all were checked. The inner production manifest lists a larger build archive, including items not in this review packet. Reading that manifest is not verification of all those underlying files. No prior review contents, scores, rebuttals, desired grades, source-preparation audit, programme state/history or self-cited predecessor paper contents were opened. Filenames and hashes referring to earlier material occur in the supplied production manifest; they were not followed. The manuscript itself contains author statements about preparation and review, which were treated as research/provenance assertions rather than instructions or independent proof.

Conservative participation declaration: **involved_in_manuscript**, as explicitly supplied. Provider: OpenAI/Codex. Exact served backend identifier, version and reasoning effort are **not exposed**; native model_id is `not_exposed`. A fresh context was requested by the operator. This session does not independently attest spawn configuration, disabled saved memory, workspace isolation, blocked technical access, provider independence, or nonparticipation. No follow-up messages were received during scientific review. This reviewer is a distinct assigned review task, but role separation alone is not scientific or technical independence.

Tools were used for reading, displaying supplied images, checking hashes, primary-source browsing, and writing new output documents. No mathematical code, numerical spectral calculation, compiler, scientific runtime, formal prover, repository command, source mutation, publication or state change was performed. Outputs were created only in the new designated outputs folder. D:\LEEME.md was read before writing. This is the first and only numerical assessment performed by this review session; global first-ever status is an operator declaration, not independently established.

## Claim-by-claim findings

### 1. Transfer convention and product benchmark: pages 1-2, equations (1)-(4)

**Finding: supported.** At fixed beta > 0, q = exp(-2 beta) lies strictly between zero and one. Each two-state factor has positive eigenvalues 1+q and 1-q. Tensorization therefore makes M positive definite; congruence by the invertible diagonal square-root weight preserves positive definiteness. Strictly positive matrix entries give a unique positive Perron eigenvector and strict separation from every other eigenvalue. These are distinct uses of definiteness and entrywise positivity, and the text keeps them separate.

For uniform weights, A is 2^(-L) M. The largest tensor eigenvalue uses only 1+q factors and the next uses one 1-q factor. Their ratio is (1-q)/(1+q) = tanh(beta), including multiplicity of the second eigenvalue. The overall scalar cancels. The labelled marginal tuple really does discard conditionals, density bounds and operator entries; the subsequent impossibility statement is restricted accordingly.

**Boundary checks:** beta = 0 would destroy strict positive definiteness and the slow-mode conclusion, but it is explicitly excluded. Beta is fixed before L tends to infinity; no uniform-in-beta constants or zero-temperature limit are claimed. L is the Boolean dimension, not a spatial lattice dimension. The text makes no inference about a physical mass gap.

### 2. Lemma 2, simultaneous primal/dual conditions: pages 2-3

**Finding: supported.** For a uniform k by L binary matrix, each fixed nonzero message produces a uniform word, and each fixed nonzero dual candidate produces a uniform k-vector. The two union bounds require no independence between these failure events. Rank failure is included in the primal event because zero has weight below delta L when delta > 0. Thus avoidance ensures exactly dimension k, rather than merely dimension at most k.

The inclusive entropy sum bounds the strict primal failure event even when delta L is integral or nonintegral. With z = p/(1-p) < 1, the inequality z^j >= z^(pL) on the stated range gives the displayed entropy bound in the correct direction. The dual sum excludes zero and includes all nonzero words up to floor(alpha L). A dependence among the selected generator columns gives exactly a supported dual word. Absence of that word ensures full column rank and uniform projection of uniform messages. This proves exact labelled product marginals, not just unbiased coordinates.

Ceiling k = ceil(RL) adds a bounded exponent error. Both strict entropy inequalities make the two failure bounds vanish for all sufficiently large integers L, not merely a subsequence. R < 1 also eventually ensures k < L. No efficient code-search or deterministic encoding theorem is required. The code existence claim is self-contained and does not depend on an unverified predecessor.

### 3. Proposition 3, finite spectral estimate: pages 3-4, equations (9)-(11)

**Finding: supported.** Equal codeword mass a = (1-eta)/m + eta/2^L is at least 1/(2m), and the product component makes every mass strictly positive. The principal code block is a M_CC. Its off-diagonal row sum is at most s because differences of distinct codewords are nonzero codewords of weight at least d_C. Symmetry bounds its operator norm by the maximal absolute row sum, giving eigenvalues in [1-s,1+s].

The descending-order principal interlacing inequality is used correctly: lambda_m of the full matrix is at least the smallest eigenvalue of the m by m principal block. Hence every j <= m has lambda_j >= a(1-s). A coordinate Rayleigh vector separately gives lambda_1 >= a. These remain valid when s exceeds one; a negative lower bound does not invalidate interlacing.

The outside block is positive semidefinite with trace eta(1-m/2^L), so its norm is at most eta. The squared Frobenius norm of the cross block is bounded by the product of the two block masses since every kernel entry has magnitude at most one; that product is at most eta. The symmetric off-diagonal block matrix has norm equal to the rectangular cross-block norm. Thus the perturbation norm is at most sqrt(eta)+eta and lambda_1 <= a(1+s)+sqrt(eta)+eta.

Subtracting the lower eigenvalue bound gives a nonnegative upper estimate 2as+sqrt(eta)+eta for lambda_1-lambda_j; division using lambda_1 >= a produces the advertised 2s+2m(sqrt(eta)+eta). This subtraction argument avoids an invalid division of a possibly negative lower eigenvalue estimate. Perron simplicity yields strict positivity of every asserted deficit j >= 2. The full-code case has an empty outside block and poses no contradiction; the bound may simply be weak. All indices j <= m exist.

### 4. Theorem 1 parameter specialization: pages 2 and 4

**Finding: supported, including the constant 7.** The supplied R is positive and strictly below 1-h(1/4), and R log(2) <= beta/4. A positive alpha with h(alpha) < R/2 exists because entropy tends to zero at zero. These satisfy the stronger-than-needed dual inequality. Gamma = beta/2-R log(2) is positive, at least beta/4, and no greater than beta.

With m = 2^ceil(RL), eta = exp(-2 beta L)/m^2 lies in (0,1/4]. Ceiling control gives m <= 2 exp(R log(2)L). The primal contribution is at most 4 exp(-gamma L). The admixture contribution is exactly 2 exp(-beta L)+2 exp(-2 beta L)/m and is at most 3 exp(-beta L), hence at most 3 exp(-gamma L). Their sum is the asserted 7 exp(-gamma L). There is no hidden polynomial factor or dependence on the ambient matrix size in the block estimate.

The code dimension supplies exponentially many modes, m-1, and m < 2^L eventually ensures the claimed range. Perron strictness is compatible with arbitrarily small but positive deficits. The argument proves an upper bound on their deficits, not equal eigenvalues, a matching lower exponent or a count of metastable sets. The abstract accurately states the weaker conclusions actually proved.

### 5. Lemma 4 and Doob transform: pages 4-5

**Finding: supported; no identification of mu with pi is needed.** Translating by a codeword preserves the code, its complement, the mixture weights and Hamming distance. The induced permutation commutes with A. It takes the unit positive Perron vector to another unit positive Perron vector, so uniqueness makes the vector constant on code cosets. Squaring preserves that invariance.

For each coordinate set S of allowed size, every translation of the projected cube lifts to a codeword. Therefore the projected stationary measure is invariant under the full finite translation group, hence uniform. This is sufficient even though different code cosets may have different stationary masses. The proof has no hidden assumption that pi equals mu or that v is globally constant.

The row sums of P are one by Av = lambda_1 v. Detailed balance follows from symmetry and pi = v^2; unit Euclidean normalization makes pi a probability law. Explicitly P = diag(v)^(-1) A diag(v)/lambda_1, so the normalized spectrum is exactly preserved. Strict positivity gives irreducibility and uniqueness of the stationary measure. No single-site or spatial-locality property follows, and none is claimed.

### 6. Proposition 5, full parity spectrum and ordering: page 5

**Finding: supported for its explicit L >= 2 domain.** Summing over an omitted coordinate kills the full parity character, proving all proper marginals are uniform. The scalar suppressed in the transfer calculation is 2^(-L)(1+q)^L, common to every eigenvalue. D_t is invertible for |t|<1, so the stated similarity is valid. On the character basis, multiplication by full parity exchanges complementary subsets; the displayed nonsymmetric two by two block has the correct coefficients, trace and determinant. There are 2^(L-1) unordered pairs and two roots per pair, giving exactly 2^L eigenvalues with multiplicities.

The discriminant is nonnegative: it equals (rho^s-rho^(L-s))^2 + 4t^2 rho^L. Its determinant is positive and its trace positive, so both roots are positive. For 0<rho<1, the endpoint trace z_0 is largest, and z_1 is largest among proper pairs. The upper root increases with trace at fixed determinant. The lower root of the empty/full block is at most rho^L, while the upper root of a singleton pair is at least rho. Since L >= 2, these cannot compete in the wrong order. All other lower roots are bounded by their own upper roots. This establishes the second eigenvalue rather than merely a candidate mode.

The upper-root/trace function increases in trace; thus its ratio for z_1 and z_0 gives lambda_2/lambda_1 <= z_1/z_0, with the inequality in the printed direction. Writing b=rho^(L-2), the quotient rho(1+b)/(1+rho^2 b) increases in b in [0,1], so its maximum occurs at L=2 and equals tanh(2 beta). Letting |t| approach one at L=2 makes the determinant tend to zero and attains the bound as a supremum. It need not be attained within strictly positive weights.

**Analytical boundary checks:** at t=0 the blocks return the ordinary product spectrum; at L=2 the middle pair gives rho(1+|t|) and rho(1-|t|); a repeated middle root at t=0 is harmless. Negative t has the same spectrum because only t^2 enters the roots. Endpoint |t|=1 is excluded from the similarity argument and used only as a limit. These checks were symbolic inspection, not executed numerical experiments.

### 7. Preliminary heat-bath statement: page 5, before Proposition 5

**Minor potential error/domain ambiguity, retained as finding F1.** The sentence says the single-site heat-bath gap tends to zero at fixed size as |t| approaches one, but does not yet impose L >= 2. At L=1, the only heat-bath update redraws the whole one-spin law. A continuous-time update of fixed positive rate c has gap c for every |t|<1; the unit discrete-time update has gap one. Thus the unrestricted reading is false.

For L >= 2 the intended claim is correct and can be checked without the self-cited paper. Every spin has mean zero and variance one. Conditional expectation of spin i given the others is t times their parity product, so the conditional variance is 1-t^2. Under the usual continuous-time heat-bath generator with fixed finite rates c_i, the Dirichlet quotient of spin i is c_i(1-t^2); only the update at i contributes. Hence the gap is at most that expression and tends to zero. Fixed normalized random-scan probabilities give the corresponding discrete-time statement. Rates depending singularly on t would require separate qualification.

**Requested correction:** add “for L >= 2, with fixed finite positive site rates” and state the generator normalization, or supply a precise predecessor proposition reference. This correction does not change Theorem 1, Proposition 5, the many-mode conclusion, or the marginal-certificate corollary. It is not a material objection capable of invalidating a main claim.

### 8. Corollary 6, certification limitation: page 6

**Finding: supported.** A function factoring through the specified tuple must have the same value on the uniform law and on the constructed weight at the same L and beta, because both marginal tuples agree exactly. A valid lower bound for every strictly positive weight must be no larger than the actual constructed gap, which is bounded above by the theorem. The argument still works if either marginal tuple alone is retained.

No regularity, computability, continuity or sign hypothesis on F is needed. The corollary only restricts its value at the product marginal input for sufficiently large L; it does not make every such functional zero, make the product chain slow, or exclude a certificate using additional information. Restriction to a smaller class of weights with uniform density or local Gibbs bounds would break the universal premise; the manuscript expressly acknowledges this. There is no unsupported finite-size or universal dynamical impossibility claim.

## Citations, originality and importance

Two external primary sources were actually opened. The [Brehm–Resch publisher page](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.28) verifies the author/title/ITCS 2026/volume/article metadata and describes codes with good primal and dual parameters and linear-time encoding. This supports the manuscript's statement that stronger algorithmic work exists. The full 19-page proof was not audited.

The [Alon–Goldreich–Mansour author manuscript](https://www.wisdom.weizmann.ac.il/~oded/PSX/agm.pdf) was opened and its returned introduction/formal-setting material inspected. It supports the use of k-wise independence as exact uniform restrictions on selected coordinates and its distinction from approximate independence. It does not, in the inspected passages, directly document the historical code-dual-distance/orthogonal-array equivalence. Its posted preprint date differs from the journal year, which is not itself a bibliographic error. The final journal metadata and full proof were not independently checked.

**Attribution improvement F2:** add a direct primary reference for the code-projection/dual-distance equivalence or explicitly characterize [1] as general limited-independence background. The equivalence is proved here, so this is attribution, not a logical gap.

The two self-cited AIRR predecessors were not opened because this review was restricted from reading programme history. Accordingly their public availability, exact versions, full theorems, historical priority and editorial status are not certified. Their narrowly described mechanisms are analytically plausible independently of those documents: an equally weighted antipodal pair has a two by two transfer block with diagonal one and off-diagonal q^L, with ratio (1-q^L)/(1+q^L); an arbitrarily small positive admixture preserves the limiting effect. Such a pair has correlated two-coordinate marginals. The parity heat-bath mechanism is checked above. These observations verify the mathematical comparison, not the predecessor records.

The primary-source check was targeted and small, not a systematic originality search. The statement that the authors' own search did not find the joint result cannot be independently verified from this packet. The manuscript appropriately disclaims established priority. No external evidence of field-shaping, historic, Millennium-level or unusually broad impact was found or is asserted. The joint stationary and weight marginal equality plus many slow modes is the strongest plausible novelty candidate; the sharp parity control is an additional candidate. Neither has verified historical priority.

## Presentation and provenance findings

All seven actual page images were viewed. Equations, theorem labels, proof endings, page numbers, source identifier and references are readable. No clipped formulas, black-square glyph failures, unresolved reference markers or overlapping text were observed. Text-extraction artifacts in matrices and radicals were resolved against the TeX and page images. The last page has ample whitespace, which is not a scientific or reproduction defect.

The production report records two fresh source builds with the same PDF hash and size, no reported overfull lines, seven rendered pages, and successful command exits. The supplied builder describes a corresponding process and source-hash checks. Those are inspected records, not executions or full independent replications performed here. The reviewer did not verify the remote Git commit, clone PDFs, native logs, build exits, source-capture history or internal manifest members absent from this packet. The exact local PDF, extraction, source and page-image hashes do match the outer packet manifest.

The TeX contains a default SourceCommit placeholder that the builder replaces through a compiler definition. The PDF/extraction display the supplied commit f4d66763d3fe3eccfc9e5eafba37d17dbe519f6b; no unresolved placeholder appears in the viewed artifact. This supports consistency with the reported procedure, not a cryptographic proof of the historical build environment. No separate scientific dataset or computational certificate is used as a theorem premise. Analytical self-containment is a strength; document byte reproducibility is not mathematical proof.

## Complete disposition

F1 is the sole identified potential mathematical error and is a minor domain qualifier in a preliminary comparison sentence. F2 is an attribution improvement. No numerical claim was silently omitted, no criterion score was replaced, and no objection was suppressed for a desired outcome. The remaining limitations are external priority, modest scope, nonconstructive parameter choices and involved model review with unverified isolation. They affect the interpretation and score, not the established internal proof chain as inspected.

Recommended revisions are confined to the heat-bath domain/rate clarification and more precise attribution. No new numerical experiment, formal proof, compilation or broader physics claim is needed to address these observations. This report and the native JSON assess only the canonical hash stated above.
