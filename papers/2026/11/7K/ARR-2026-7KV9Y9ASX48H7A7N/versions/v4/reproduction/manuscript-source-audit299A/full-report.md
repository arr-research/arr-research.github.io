# Full analytical integration audit — unit299 manuscript

Verdict: ACCEPT for the mathematical source integration and the declared source-package boundary at exact commit 6f9b27f59e3b105a872c773ed4d38d027536655b and PR245 body bound below. This is a new analytical integration verdict. It does not produce a PDF score, inherit an earlier score, certify a build, establish priority, or constitute human peer review.

No unresolved proof-invalidating mathematical or package-integrity objection was found. Every limitation and presentation observation identified during this review is retained below. The acceptance applies to this exact referent, not to the branch name, future edits, a future PDF, or a future publication record.

## 1. Exact referent and capture

Worktree: C:\Trabajo\the-eriksson-programme\prefix-rank290-20261113.
Branch: codex/tep-manuscript299-20261113.
Frozen commit: 6f9b27f59e3b105a872c773ed4d38d027536655b.
PR: https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/pull/245.
Captured base: dc792f12b1c8e0c448ddb0bfb21d1e70faec33c7.
Title: Consolidate exact critical moment budget into the transfer-kernel manuscript.

The complete PR body was independently read through the GitHub connector, then captured with:
gh pr view 245 --repo lluiseriksson/THE-ERIKSSON-PROGRAMME --json body,headRefOid,url,title,baseRefOid,files,state
The raw stdout bytes are pr245-body-capture.json. The capture timestamp is 2026-11-13T12:13:14.4652080Z. The decoded complete body, not an excerpt, was normalized by replacing CRLF and CR with LF, removing trailing LF characters, then appending exactly one LF. Encoding is UTF-8 without BOM.
Normalized full-body length: 1141 bytes.
Normalized full-body SHA-256: 13bc8bdcebbc9c4c06a9f0366f540c95d512d397b94ae35f1cb413bf68327e78.
The assignment delegated independent body capture to this auditor; no supplied body digest was silently treated as independently verified. The verdict repeats commit, capture method, normalization and hash. A separate final recapture checks stability.

Main manuscript: papers/marginal-transfer/manuscript299A.tex, 1261 lines, 56218 raw bytes.
Git blob and actual checkout independently extracted/hashed: both SHA-256 6b0c330c283e4f40d1711f4c2e358fdb3edf2ed73d70ac5fb87a55ca96514c64, matching the assigned UTF-8/LF digest.
SOURCE-INPUTS299.json: 35021 bytes, Git and checkout SHA-256 0352822a439320afaa4349446e4a889e4717e6d9e47c47ee527183081df7d078.
critical299-section.tex: 7601 bytes, both SHA-256 82e3cb8a3ff557356992da1952217b5ae06bef35c4852e53415e06a60245c098.
Predecessor manuscript298A.tex: 46979 bytes, both SHA-256 a01b9793fe66bd7b3e49c2ee62eb50bfc2f4d43d8bad7949aaaa637e3dfc7c28.
Accepted proof referent: 49705281f05ab18b71bd9ebc2da1985a0433340c, critical299A.txt raw SHA-256 00a0c712f9b929e3fb669356585c30f08bfd7a5218ea9d4a24121e5b26e00b03.
Registered judges: bed6289e75510ac633ca3255bd5c4708343ce784, judges299.txt raw SHA-256 d27ac6e5dc2b813643104b6d38f1de44b8ac5b47de784a1b264dfc8bb54e13c1.

The input manifest distinguishes exact Git object bytes and actual checkout bytes. It does not silently normalize historical material. In particular, current CLAUDE.md is Git 23996 bytes / 443459690fceb9a52b47bf414eb404b7200c2f6806d1347336fd279303224fad versus checkout 24408 bytes / 618e5b2d6ee2ec6d88050870d27679fb64f76951d51323ea6b994b22d99cbcfe. The charter is Git 13573 bytes / 19e90b6aa2e70acb750a63e9a75383ee995a3c3b8e8e351e5e6091a69ffe2fc4 versus checkout 13831 bytes / fff6958f6457ec330e2b30a076c46105ba407da898f5a674576b8ba29948248f. These are recorded line-ending regimes, not hash mismatches hidden by normalization.

## 2. Actual scope and review context

I read the complete integrated manuscript, all 1261 lines, in bounded chunks, including its preamble, abstract, every theorem and proof, discussion, provenance and bibliography. I read the complete textual diff against manuscript298A, the full critical299A proof and unchanged G1-G7, package boundary, source-acceptance observation, retained interruption record, primary-reading notes, historical unit298 scientific report, importance assessment, schema-correction addendum and author response. I inspected the package inventory and verified all declared file bindings and tracking. The standalone new section occurs literally in the manuscript.

This is the same involved audit context that previously reviewed unit298 sources/integration and the resumed unit299 source. Prior assignments, source reasoning, primary-source readings and verdicts are retained context. This is not a blind review or a fresh independent source-theorem verdict. Nevertheless the integration and relevant mathematics were actively rechecked rather than inferred from an ACCEPT label. The exact current assignment is preserved verbatim in assignment-received.txt. No unsolicited inbound mathematical or operational notice arrived during this assignment. No other chat or agent was contacted.

The unit299 source's first attempt ended with a reported usage-limit interruption before a delivered verdict; its draft ACCEPT was not inherited. The operative resumed source report is full-report-resumed-final.md, raw SHA-256 1774c5cdf606820968a0ad258f32a0c4ad43a5179b60826068ea86e55d92a745. This history remains explicit in the package. No quota purchase, provider/account/model change or limit circumvention occurred in this integration audit.

The reviewer is an OpenAI/Codex model context. Exact served backend, reasoning setting, memory isolation and technical filesystem isolation are not independently verifiable. Same-provider and shared-filesystem limitations remain. No claim of independent human, provider-independent or formally verified review is made. Hash verification proves identity; static reference checks prove textual resolution; neither is a theorem-correctness certificate.

No local mathematical computation, numerical experiment, mathematical test suite, build, Lean/Lake, Colab or reviewed runtime was executed. Only reads, analytical reasoning, metadata/text comparisons, byte hashing, raw source copying and evidence writing were performed. A metadata helper is retained for reproducibility; it contains no mathematical computation. An initial tool orchestration syntax error happened before execution; it produced no source or evidence mutation and had no mathematical content. A console display using Select-Object on an ordered dictionary printed null summary fields, while the saved JSON was complete; rereading the saved file independently confirmed 172 entries and zero failures. Neither incident was presented as a mathematical result.

## 3. Whole-paper normalization and retained results

The paper consistently uses q=exp(-2 beta), M_beta(x,y)=q^{d(x,y)}, rho=tanh(beta), and P_rho=M_beta/(1+q)^L. With r=2^L mu,
A_mu=2^{-L}(1+q)^L T_r.
This is a scalar relation preserving normalized eigenvalue ratios. The uniform-measure L2 convention in density sections is consistent with the matrix eigenvalues. Perron stationary probabilities v_x^2 use Euclidean normalization in the initial code sections and are not confused with the weighting law mu or r u_L.

The first twelve numbered results are retained. Comparing the old and new source shows no altered theorem hypotheses or conclusion in them. The proof-local addition specifying a uniform sign x in {-1,1} makes the balanced-tilt convention explicit. Introductory and transition text now accurately says that the new final critical section resolves the previously open range. No old theorem is retroactively strengthened in the historical file.

I rechecked the retained chain of arguments for compatibility, rather than merely relying on unchanged bytes:
- The random-generator code union bound includes rank failure through a zero codeword. The inclusive entropy sums dominate the strict-weight event; the ceiling in dimension contributes only a bounded factor. Dual distance gives surjective labelled projections.
- The code concentration estimate uses a >=1/(2m), off-diagonal row norm s, outside PSD trace at most eta and cross Frobenius norm at most sqrt(eta). Interlacing and division by lambda1>=a give the displayed finite estimate even when its bound exceeds one. With the chosen constants, the two terms are bounded by 4 exp(-gamma L) and 3 exp(-gamma L). There is no missing dimension factor.
- Translation symmetry plus uniqueness of the positive Perron vector proves stationary marginal matching. It does not assume pi=mu.
- The parity complement blocks exhaust the character space. The constant determinant and monotonic upper-root-to-trace comparison identify the top two eigenvalues, including degeneracies. The transfer bound has no conflict with the heat-bath example.
- The marginal-certificate corollary is a factorization obstruction on a specified input tuple, not a claim that the product chain is slow or that all marginal functionals vanish.
- The bounded-density and supercritical finite-moment proofs retain the active-support treatment, nonnegative cross entries and exact two-dimensional compression. The reverse-Hypercontractive interpolation at p<1 uses Holder weights, not a triangle inequality. The strict moment condition is exactly Q>1+rho. Its exponent and final min{1/2,(2B)^(-2e)} are unchanged.
- The subcritical double-tilt proof has one-site norm kappa>1 and strictly smaller cross norm omega. Equality would force a shared top eigenvector of matrices whose difference is invertible. The rectangular Gram matrix adds zeros only; both genuine top eigenvalues transfer. All-L budgets and floor 1/B remain valid.
- The small critical budget estimate still correctly treats s>=2 and 1<s<2 separately. For s>=2, phi_s(t)>=|t-1|^s holds on both sides of one; for 1<s<2 the negative exponent in the integral remainder gives the stated weighted-square lower bound, including t=0 by continuity. Holder and Minkowski yield the printed d_s(B), which tends to zero at B=1.
- The balanced critical B>2 rate is preserved as a sufficient explicit rate. Its all-L constraint C d^4<=log(B-1) is possible because B>2, not at arbitrary smaller B. The new proof explicitly removes that budget-specific choice before reusing the family. No such all-L rate is silently transferred to equality or to an arbitrary prescribed floor.

The new exact-budget section follows these definitions rather than introducing a second incompatible operator or measure. Temporary notation S_L for the unnormalized sum in the new proof is explicitly defined there; the transformed actual operator is S_L/Z_L. The statement never confuses the ratio-preserving scalar normalization with convergence of actual eigenvalues.

## 4. Adversarial check of the integrated exact threshold

### 4.1 G1-G2: support, signs, multiplicities and exponents

For 0<rho<1, P_rho is PSD, invertible and strictly entrywise positive. On A={r>0}, T_r is strictly positive and has a simple positive Perron root and strictly positive Perron vector. Outside A there is a zero block. If lambda2=0, the two-sign bound is immediate, including one-point support. If lambda2>0, a real second eigenvector vanishes outside A and is orthogonal to the Perron vector. It must have both nonzero signs regardless of multiplicity of lambda2. The proof does not require base-measure mean zero.

Set p=1+rho=2s/(s+1). Then p/(2-p)=s and Q=P_sqrt(rho) maps Lp to L2 with norm one at equality of the classical noise threshold. For h supported on C, Holder on r^(p/2)|h|^p has exponents 2/(2-p) and 2/p. After raising to 2/p it yields
<h,T_r h> <= (E[r^s 1_C])^(1/s) ||h||2^2.
There is no counting-measure volume factor or unproved restriction of the noise operator.

Pairing the eigenrelation with f_+ gives lambda2||f_+||2^2 <= <f_+,T_r f_+>, since the subtracted cross term is nonnegative. Pairing with f_- gives the same bound. Divide only by the nonzero sign-part norms. The two disjoint regions therefore each carry moment mass at least lambda2^s. Zeros of f merely leave unused nonnegative mass. Adding proves exactly 2 lambda2^s <= E r^s.

The unit vector sqrt(r) has Rayleigh quotient <r,P_rho r> >=(Er)^2=1 by the nonnegative Walsh spectrum. Thus lambda1>=1 and lambda2/lambda1<=B/2^(1/s). This verifies the normalized-gap statement, not merely an additive spectral gap or a top-eigenvalue norm bound.

### 4.2 G3: scope of sharpness and quantifiers

The exactness claim concerns the budget B*=2^(1/s), with fixed rho and critical s, across all dimensions L>=1. It does not assert the lower bound 1-B/B* is the optimal gap value. At B=1, strict Jensen gives r=1 and actual gap 1-rho; this is stated separately. The admissible regime is B>=1; the theorem's classification explicitly uses 1<=B<B*.

The fixed-floor statement fixes any b in (0,1) before choosing a finite prefix. It does not assert a uniform construction simultaneously over b approaching one, or allow b=1. Every individual finite gap is strictly positive, while the infimum across dimensions is zero at and above B*. There is no assertion of an attained zero gap in finite dimension. At larger budgets the same boundary sequence remains admissible.

### 4.3 G4: balanced family, Taylor coefficients and actual spectrum

The one-site H is Q_1 M_w Q_1 in the orthonormal basis (1,x), with w=(1+delta x)/n and n^s=((1+delta)^s+(1-delta)^s)/2. Hence E w^s=1, E w=m=1/n. H is positive definite for |delta|<1, and its displayed kappa is its genuine top eigenvalue.

Tau=||D^(1/2)H^(1/2)|| satisfies tau^2=lambda1(D^(1/2) H D^(1/2)); the latter is n^(-1)[[1,rho delta],[rho delta,rho^2]]. This gives the displayed square-root expression with rho^2 rather than rho. Even analytic logarithms and a fixed small compact delta interval justify O(delta^4) remainders. At criticality:
log n=(s-1)delta^2/2+O(delta^4);
log kappa=[rho/(1-rho)-(s-1)/2]delta^2+O(delta^4)=O(delta^4);
log tau=(1/2)[rho^2/(1-rho^2)-(s-1)/2]delta^2+O(delta^4)
=-rho delta^2/[2(1-rho^2)]+O(delta^4).

The new manuscript explicitly brackets the whole coefficient, removing the nonblocking ambiguity in the source candidate's explanatory prose. The correct displayed coefficient was already present in the source. The half factor has not been lost in integration.

For delta_L=d L^(-1/3), L delta_L^4 tends to zero while L delta_L^2 tends to infinity. Thus a_L=kappa^(-L) tends to one, m^L tends to zero, Z_L=1+a_Lm^L tends to one and eta_L=sqrt(a_L)tau^L tends to zero. Fixed d is chosen sufficiently small and positive independently of L; no B>2 constraint is used here.

The sum S_L=P_rho+a_L H^tensor L has two diagonal Gram blocks of top eigenvalue exactly one. Their off-diagonal norm is eta_L, by tensorization and the square-root norm identity. Weyl/min-max gives lambda1<=1+eta and lambda2>=1-eta; PSD order gives lambda1>=1. Rectangular Gram zeros do not displace the top two genuine eigenvalues once 1-eta>0. Dividing by Z_L tending to one gives both top actual eigenvalues tending to one. For the final spectral identity, the square matrices X=M_sqrt(r)Q satisfy X*X=QM_rQ and XX*=T_r, preserving all eigenvalues including multiplicities and zeros. The proof has not inferred actual eigenvalue convergence from a ratio alone.

### 4.4 G5: exact limiting moment

For each fixed t strictly between zero and s, the even analytic single-site expansion is
log E w_delta^t = [t(t-1)/2 - t(s-1)/2]delta^2+O(delta^4)
= t(t-s)delta^2/2+O(delta^4).
The quadratic coefficient is negative. Therefore E R_L^t tends to zero, while E R_L^s=1 exactly. Remainder constants need not be uniform in t near the endpoints, and the manuscript makes no such claim.

For theta=min(1,s/2), both theta and s-theta are strictly interior. The global inequality
0 <= (1+y)^s-1-y^s <= s 2^(s-1)(y^theta+y^(s-theta))
holds for all y>=0. On [0,1], the mean-value bound is s2^(s-1)y and y<=y^theta. On [1,infinity), factor y^s and use the same bound at 1/y, giving y^(s-1)<=y^(s-theta). Convex superadditivity yields the lower bound. This works for both 1<s<2 and s>=2, including s=2.

Substitution y=a_L R_L keeps both amplitude powers; they remain bounded and tend to one. Both interior moment error terms vanish. Thus E(1+a_LR_L)^s=1+a_L^s+o(1) tends to two. Division by Z_L^s tending to one yields E r_L^s tending to two and B_L tending to B*. This is a true moment limit, not the weaker triangle bound 1+a_L.

### 4.5 G6: equality, perturbation and all-dimension floor

R_L is nonconstant for every L>=1 because d>0, and a_L>0, so B_L>1 by strict Jensen. If B_L<=B*, epsilon_L=0. Otherwise epsilon_L=(B_L-B*)/(B_L-1), with a strictly positive denominator and 0<epsilon_L<1. As B_L tends to B*>1, epsilon_L tends to zero, regardless of which side of B* occurs in any finite dimension.

The convex mixture rtilde=(1-epsilon)r+epsilon is positive and normalized. Minkowski gives its Ls norm at most (1-epsilon)B_L+epsilon<=B* exactly; equality of that upper bound does not need to be equality of the actual norm. The phrase “including equality” means admissibility under the boundary constraint, not exact norm equality in every dimension.

At the dual endpoint q=2s/(s-1), q-1=1/rho, so Q:L2->Lq has norm one. Holder with 1/s+2/q=1 gives ||QM_hQ||<=||h||s for signed h. Consequently the transformed perturbation is at most epsilon_L(1+B_L), which vanishes. No square-root multiplier continuity estimate, pointwise upper bound or inverse-density estimate is used. Weyl and the square-matrix spectral identity preserve convergence of both top actual eigenvalues to one. Their ratio therefore tends to one.

Both r_L and the constant density one are at least 1/Z_L because Z_L>1. Since Z_L tends to one, any fixed b<1 is eventually below that floor. Replacing only finitely many initial densities by one enforces the norm, normalization, strict positivity and floor for every L>=1 without changing the asymptotic gap. This is the permitted all-dimension completion. No convergence rate at equality follows or is claimed.

## 5. Integration, references and literature

The abstract accurately separates code/marginal results, strict exponent regimes, exact critical budget, arbitrary fixed floor below one, and the retained explicit B>2 rate. It does not suggest that the tilt family has the code construction's marginal matching. The title remains appropriate. The transitions distinguish the retained partial quantitative results from the newly complete critical budget classification. The new theorem is a combination and sharpening of earlier sections, not an assertion of newly discovered hypercontractivity.

A static source inventory finds 34 labels, no duplicate labels and no unresolved ref/eqref targets. All citation keys resolve to one of the eleven bibliography entries. The new section's standalone source is literally included as text in the integrated manuscript. These are static source facts; no TeX compilation or pagination is inferred.

The plural “counterexamples ... have” is corrected. The long evidence path uses the TeX path command, available through the loaded hyperref/url support, and has a plausible breakable representation. Actual PDF line breaks still require document production and visual review. The explicit sign-x convention avoids the 0/1 versus +/-1 ambiguity.

Aida's author-hosted preprint is now cited with its date and a targeted setup/Theorem10 reading. This is consistent with the primary reading previously performed in this audit context and retained notes. The old incomplete-access statements remain historical records rather than being silently edited. Its additive Dirichlet-form framework, derivation/chain rule and ground-state/weak-Poincare inputs have not been identified with this multiplicative Boolean congruence.

The Biskup–Koenig comparison is apt: their Lemma4.5 uses the two sign regions, and Eq4.29 splits an additive potential budget, yielding a log-two cost. That is a close classical mechanism, not an exact statement of this cube theorem. The paper credits it and expressly does not use the difference of settings as evidence of novelty.

Primary material used in the retained context:
- Mossel–Oleszkiewicz–Sen, arXiv:1108.1210v5, introductory ordinary/reverse inequalities and tensorization, for exact Boolean endpoint normalization.
- Aida, author preprint dated 9 February 2001: https://www.ms.u-tokyo.ac.jp/~aida/paper/preprint/handai3.pdf ; setup, assumptions A1-A6, additive form and Theorem10.
- Biskup–Koenig, author manuscript dated 21 April 2015: https://www.wias-berlin.de/people/koenig/www/PPP4PAM-CMP-final.pdf ; setting, Proposition2.2, Section4.3, Lemma4.5 and Eq4.29.
- Targeted prior readings of Miclo Theorem1/Proposition11, Wang Theorem1.1, Gross Theorem2.2 and Gluck's essential-spectrum statements support the cautious discussion. The entire final articles and every possible stronger implication were not exhaustively reviewed.
These reads were performed in earlier assigned audits in this retained context, not newly repeated web research during the integration audit. No full third-party text is copied into the evidence. No originality claim is inferred from unsuccessful searches.

## 6. Package, source history and exact-PDF assessments

All 172 distinct entries of SOURCE-INPUTS299.json were verified against both exact frozen Git blob bytes and actual checkout bytes, including file length and raw SHA-256. All are tracked at the frozen commit. Zero mismatches. Additional subjects bring this audit's independently frozen input set to 181 paths, with separate Git and checkout copies. SOURCE-INPUTS299 is a support-input manifest, not a self-hashing manifest of the entire paper tree; the manuscript and manifest itself are bound separately above.

Both Git and PR metadata show 63 added files and no changed/deleted preexisting files in the PR. Fifty-nine additions are under evidence299. This preserves every earlier manuscript/source file. The package contains the complete retained unit299 source-audit history, including provisional draft files, the reported interruption, resumed reports, contexts, assignments, body captures, hashes and source copies. The operative resumed report is identified explicitly; a provisional filename final-state.json is not repurposed as a delivered verdict.

All 55 packaged files under source-audit299A and prior298-assessment were directly compared with their original D: counterparts: zero byte differences. Historical raw manifests retain their original absolute capture paths and line-ending regimes; PACKAGE-BOUNDARY299 explains this, and SOURCE-INPUTS299 binds the actual packaged relative bytes. No attempt was made to rewrite old paths or normalize original reports. The other new evidence files are the proof, judges, dated parent acceptance observation and unit298 author response.

The historical unit298 assessment explicitly belongs to the 15-page PDF SHA-256 55d07066bd947482fa2e41f312ca6da614f4ec142f8ee9348b85f5f9d2de31d1, source45d91a667750b295ce096fd495863583ba56eced. Its overall 4.00/10, importance3.50/10, criteria4/4/3/3/4 and minor_revision recommendation remain historical observations, not scores issued or endorsed for this manuscript. The schema-only correction changed its independence enum to unknown and retains the original response. It is not a second scientific vote. This review did not rescore that PDF.

O1-O6 from the historical report remain preserved. The new source addresses O2 bibliographically, O5 editorially, and supplies a separately audited mathematical extension resolving the budget part of O3. The retained rate is still not claimed optimal. O1 priority, O4 global/local relevance and O6 provenance limitations remain substantive scope limits. No changes to the old report, its actual PDF, or its grade were made.

The package's new evidence inventory consists only of json, md, sha256, tex and txt files. The inspected content and origins match the stated research/audit history; no third-party full text or protected credential material was identified. This is a bounded package-content finding, not a claim of a general-purpose secret-scanner or security audit.

The read-only whitespace observation with cr-at-eol returns exit2 for exactly two preserved original-report final blank lines:
- evidence299/prior298-assessment/full-scientific-report.txt:179;
- evidence299/prior298-assessment/schema-correction/schema-correction-addendum.txt:67.
The new section EOF is not among them. These are disclosed nonsemantic archival formatting observations, not mathematical failures or reasons to alter originals. The earlier CRLF diagnosis is supplied history; this audit independently verifies the current cr-at-eol observation, rather than inventing a replay of an unavailable prefreeze state.

## 7. Objections, limitations and attempted falsifiers

No material blocker survived the following attacks: missing factor of two or base-measure factor; zeros outside support; missing sign part under multiplicity; invalid endpoint strictness; lambda1 normalization; confusing positive gap optimality with budget sharpness; missing half factor in log tau; all-L B>2 assumptions imported into the boundary family; nonuniform Taylor remainders; cross moment exponents at endpoints; amplitude or Z normalization omitted; false actual-eigenvalue inference from Gram zeros; inability to approach B* from above; zero dilution denominator; small density floor only eventually; finite-dimensional zero gap claimed; mismatch of history hashes; inherited PDF grade; and novelty inferred from a source-setting difference.

Remaining limits and nonblocking observations:
1. External priority and the significance of this specialization remain unestablished. Classical mechanisms are credited; no exhaustive implication search or new novelty certificate exists.
2. The positive gap formula below B* is sufficient, not optimal. The equality construction has no claimed convergence rate. Fixed rho,s,b quantifiers do not give endpoint-uniform estimates as rho or b varies.
3. The tilt family is global and need not match marginals or arise from a fixed-range Gibbs model. There is no local-dynamics, continuum, Yang–Mills or physical mass-gap conclusion.
4. No new PDF exists within this audit's reviewed subject. Source acceptance does not establish successful compilation, page layout, reproduction, PDF byte identity, or a numerical scientific assessment. The SourceCommit fallback remains SOURCE-NOT-BUILT pending an explicit production invocation.
5. The path/plural edits are valid source edits, but the visual result of the path change is not yet inspected. The two historical EOF observations remain visible and intentional.
6. Review is involved, same-provider and technically unisolated/unattested. Prior accepted arguments and historical ratings were visible by design. No independent-human or blind-review claim is warranted.
7. Byte checks cover every manifest input; semantic full reading covers the current entire manuscript and specified relevant proofs/reports, not every unrelated historical document in all nested evidence directories. No broad independent audit of the repository's other research follows.

These limits are consistent with the exact current statements and do not block this source integration. There is no known-open mathematical defect requiring a carve-out in this verdict.

## 8. Deliverables and decision boundary

This directory contains the exact assignment, full report, context, gate table, original connector capture, raw GH capture, normalized complete body, initial/final snapshots, static observations, full 298-to299 textual diff, historical-byte comparison, input-manifest and separate frozen Git/checkout subject trees. The final raw-hashmanifest binds every stored file except itself and its detached digest, avoiding circular hashing. Its detached digest binds the manifest.

The worktree's tracked state remained frozen; only preexisting untracked _drafts/ and _tmp/ were listed, never read. No source, branch, PR, assessment or prior evidence was modified. No disposable clone/worktree was created; no cleanup is pending. Only new evidence in the assigned D: directory was written.

ACCEPT is restricted to commit6f9b27f59e3b105a872c773ed4d38d027536655b and PR245 full body normalized as specified, 1141 bytes, SHA-25613bc8bdcebbc9c4c06a9f0366f540c95d512d397b94ae35f1cb413bf68327e78. Exact PDF production/review remains separate. No numerical score is created by this report.
