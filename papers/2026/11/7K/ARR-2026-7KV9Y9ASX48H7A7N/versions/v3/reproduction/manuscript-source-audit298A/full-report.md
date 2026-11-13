Hash context: frozen commit `45d91a667750b295ce096fd495863583ba56eced`; manuscript298A.tex Git-blob/LF SHA-256 `a01b9793fe66bd7b3e49c2ee62eb50bfc2f4d43d8bad7949aaaa637e3dfc7c28`; separately measured actual-checkout raw SHA-256 is the same.

# Integrated manuscript and package audit 298A

**Verdict: ACCEPT for the frozen integrated analytical manuscript, source-package boundary, and stated PR scope.** The two critical theorems accurately transcribe the accepted source; earlier theorem statements and proofs are preserved; all 111 declared package inputs match their raw hashes and byte lengths in both Git and the actual checkout and are tracked at the exact frozen SHA. No blocking objection was found. Two nonblocking editorial points and the remaining production/review limitations are listed explicitly below.

This is a new assignment to the same involved Codex/OpenAI auditor that completed the preceding source audit. It is not a new blind reviewer, independent human peer review, a formal verification, or a PDF assessment. Technical isolation and the exact served model/backend and reasoning settings are unverified. No score is created or inherited.

## Exact referent, PR capture and package identity

Worktree: `C:\Trabajo\the-eriksson-programme\prefix-rank290-20261113`.
Target commit: `45d91a667750b295ce096fd495863583ba56eced`.
Prior accepted mathematical source commit: `2d1d27c4ba5f677e7f51092c6479735ba9ba59fa`.
Manuscript Git blob: `70f9124e6b7b7da859886570f8c1e38e237d9cf8`.
Manuscript length: 46979 bytes, independently for Git blob/LF and actual checkout/LF.

PR: [242](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/pull/242).
Capture method actually executed: `gh pr view 242 --repo lluiseriksson/THE-ERIKSSON-PROGRAMME --json body,headRefOid,url,title`; stdout captured as raw bytes, then the JSON body decoded.
Body normalization: UTF-8 without BOM; CRLF and lone CR converted to LF; trailing LF characters removed, then exactly one LF appended. This realizes the assignment's UTF-8/LF, trailing-newlines-removed-plus-one-LF rule.
Normalized body: **808 bytes**, SHA-256 **`5c213f952c5c27fe7956af7f82fa152709f1f00f66367bff0ff8f693318bcf46`**.
Captured PR head: **`45d91a667750b295ce096fd495863583ba56eced`**.
The title is “Critical moment budgets: stability near one and balanced-tilt collapse”.

The independently captured body/head match the supplied frozen capture. Original provided capture files are preserved under `provided-pr-capture`; new raw snapshot, normalized body and capture metadata are also retained at the audit directory root. The original files under `evidencia-298` were not overwritten. No PR change or message was posted.

The PR body accurately describes the two new results, acknowledges the exact earlier source acceptance, and leaves optimal budgets, priority and exact-PDF work unresolved. Its statement that integrated review is pending reflects the frozen pre-verdict state, not an attempt to claim the present acceptance beforehand.

`SOURCE-INPUTS298.json`: 21795 bytes, Git/checkout raw SHA-256 `226ea6dbeab270ea99c12b4619e6447c8b3752bd3efb6f7a20ae26fc470c2e77`.
`PACKAGE-BOUNDARY298.txt`: 687 bytes, Git/checkout raw SHA-256 `e458acd716bf9ef157c5b812e4ee4ec5342101f27dae84e11719681d051e1bb3`.

## Complete manuscript reading and preservation

All 1052 lines were read in contiguous untruncated chunks: 1-240, 241-490, 491-745 and 746-1052. This includes the abstract, setup, every result and proof, all discussion, disclosures and bibliography. A complete textual comparison against manuscript297A.tex was also read. It contains the critical section insertion and limited abstract/discussion/provenance edits; no preceding theorem statement or proof was altered.

The original transfer convention remains coherent: q=exp(-2 beta), rho=tanh(beta), the product transfer kernel is normalized to P_rho, and A_mu is a positive scalar multiple of T_r for mu=2^(-L)r. Thus eigenvalue ratios in the code, parity and density sections concern the same transfer family. The later permission of zero densities retains the full ambient eigenvalue list and is explicitly distinguished from the strictly positive starting convention.

The code existence proof uses an entropy union bound that includes rank failure. Its dual-distance condition implies surjective labelled projections. The finite block estimate uses principal interlacing, an outside trace bound and a cross Frobenius norm bound; it remains valid even when the small-size upper estimate exceeds one. The selected rate parameters give the stated 7 exp(-gamma L) bound for all sufficiently large dimensions. None of these steps is affected by the critical insertion.

The Perron stationary marginal assertion follows from code-translation symmetry and uniqueness of the positive normalized Perron vector. It is not incorrectly transferred to the new product-tilt examples. The certificate corollary compares the same input tuples and does not claim that the product chain itself is slow.

The parity control retains all complement-pair multiplicities, the determinant (1-t^2)rho^L, the identification of the top roots at s=0 and s=1, and the uniform ratio bound 2rho/(1+rho^2). The contrast with the heat-bath dynamics remains explicit. Its proof does not rely on the new construction.

The upper-density theorem, growth corollary, strict supercritical moment theorem and strict subcritical two-tilt theorem remain unchanged and consistent. Their proofs retain support handling, reverse-Hypercontractive sign-part estimates, finite-dimensional compression, and fixed-vs-dimension-dependent parameter distinctions. In particular, the positive lower density in the subcritical and critical examples does not contradict the upper-density theorem: neither example supplies a uniform upper density cap.

## Transcription of the two accepted critical proofs

The new small-budget theorem keeps precisely the accepted formula for d_s(B), including the separate 1<s<2 and s>=2 ranges, max with zero, nonnegative mean-one densities, and all L>=1. Its endpoint relation q-1=1/rho is unchanged. The perturbation estimate is for Q M_(r-1) Q, with Q=P_sqrt(rho), so it applies to the actual transfer spectrum through square AA*/A*A equivalence, including zero weights. The lambda_1>=1 and lambda_2<=rho+||r-1||_s bounds yield the claimed normalized gap without any Perron-law substitution.

Both scalar arguments are present, not merely cited. For s>=2 the two sides of t=1 are covered; for 1<s<2 the Taylor integral remains integrable at t=0 and the Holder product has the correct powers. The printed proof compresses some explanatory sentences from the accepted source but does not omit a needed hypothesis or change a constant. The source's explicit small-neighborhood conclusion follows because d_s(B) tends to zero at B=1 for each fixed rho.

The large-budget theorem retains every load-bearing quantity: n(delta), the one-bit H, kappa, the ordered square-root cross norm tau, the negative quadratic coefficient of log tau, bounded fourth-order remainder, the fixed d choice with C d^4<=log(B-1), delta_L=d L^(-1/3), exact a_L=kappa_L^(-L), Z_L and the density formula. The two time scales L delta_L^4 tending to zero and L delta_L^2 tending to infinity remain implicit in the displayed inequalities and are unchanged.

The all-L constraints are intact. The uniform floor comes from Z_L<=1+a_L<=B, not merely positivity. The block top eigenvalues equal one exactly; the cross norm is sqrt(a_L)tau_L^L. The rectangular Gram comparison correctly carries N positive eigenvalues and N extra zeros, so the top two labels match even for L=1. With lambda_1(F_L)>=1, the two variational bounds give gap<=2eta_L without requiring eta_L<1. Strict entrywise positivity establishes a positive gap at every finite L. No constant, exponent, square root, multiplicity or normalization was lost in transcription.

The full standalone `critical298-section.tex` is an exact textual substring of the integrated manuscript. The integrated file does not depend on an external input command for that section; this comparison is an additional source-integrity observation, not a TeX build or proof checker.

## Abstract, references, scope and literature discussion

The abstract now correctly distinguishes the two strict regimes from the critical budget-dependent results. It calls the critical decay stretched exponential, leaves the optimal budget unresolved and does not attach the marginal-matching claim to the tilt construction. The old blanket statement that the critical exponent is unresolved is replaced by the appropriate small/large-budget discussion. The new section explicitly leaves intermediate budgets open and makes no assertion at B=2.

A static text inventory found no duplicate labels, undefined internal references or undefined citation keys. The critical-small and critical-large labels are unique and the new discussion references the correct theorem. Source-level references were also read in their local contexts. This does not certify final typeset numbering, hyperlink rendering or layout: those require the pending TeX/PDF reproduction.

The classical-source discussion preserves the distinction between a non-Markov transfer congruence in the uniform reference space and its Markov Perron transform in a different measure. The source correctly says inverse control is already available for both collapse families, so that cannot be used as a false distinction from Gross. No new novelty clearance is asserted.

Additional primary checks confirmed the relevant wording in [Miclo's Theorem 1 and Proposition 11](https://perso.math.univ-toulouse.fr/miclo/files/2012/04/hyperboundedness.pdf), [Wang's Theorem 1.1](https://arxiv.org/pdf/1305.4460v6), and the [Glueck v6 author abstract](https://arxiv.org/abs/1802.09422v6). The preceding completed source audit directly checked the MOS endpoint/tensorization statement and Gross Theorem 2.2. These checks support the limited comparison, not priority or an exhaustive exclusion of stronger implications.

The review disclosures correctly identify involved model assistance, unknown exact backend, lack of human peer review, no inherited PDF rating, and the author's relationship to AIRR. No older score has been promoted to this manuscript.

## Package boundary and all 111 entries

There are exactly **111 distinct declared paths**, totaling 807048 declared bytes. For **each** entry, I read the actual checkout file, extracted the exact frozen Git blob as a raw byte stream, recorded its blob ID and mode, and compared both byte lengths and both SHA-256 values with the manifest. Result: **111 matching, zero missing, zero mismatched, zero untracked at the frozen SHA**. These are raw comparisons, with no newline normalization. Details for every entry are retained in `package-111-checks.json`.

The manuscript, section source, boundary, manifest and package .gitattributes were checked separately and frozen as well. The package's `* -text` rule explains why raw historical mixed-line-ending files survive unchanged; equality was still tested rather than inferred from the rule.

The package retains the original 298 source audit report verbatim with its SHA-256 `ed00b8fe867b37b85386ba59ad53e424d4639186fc512673ec9284fe2760e155`, its assignment and scope limitations, and the accepted source/gates. The earlier spike source and the later two-tilt source are present in the declared subset. Historical assessment artifacts remain provenance records tied to their own earlier targets, not ratings of this version.

Original audit manifests name their original full captures, including external D: paths and subjects not redistributed in this subset. The package boundary explicitly discloses that distinction. Therefore those historical manifests are not falsely being represented as a self-contained inventory of only the present 111 files. The new SOURCE-INPUTS298 inventory provides the actual subset boundary. I certify byte identity and tracked inclusion here, not the truth of every claim in every historical report.

## Every objection and remaining limit

No blocking objection was found. The following are nonblocking editorial observations, not conditions silently added to acceptance:

1. Near lines 947-949, “the counterexample in Theorems ... have” has singular/plural disagreement. “the counterexamples in Theorems ... have” would read correctly. The theorem references and mathematical content are unambiguous.
2. The new large-tilt proof uses x_i in the sign-cube convention established in the preceding two-tilt proof, but does not repeat x_i in {-1,1} at its own definition of w_delta. Restating that convention would make this proof easier to read independently. The symmetric n(delta), Walsh one-bit H, preceding explicit relabelling and accepted source fix the intended convention; the proof is not being accepted with literal 0/1 coordinates in that formula.

The exact PDF has not been compiled, reproduced, rendered or reviewed in this audit. `SourceCommit` intentionally defaults to `SOURCE-NOT-BUILT`; final production must supply the actual reproduction source SHA so the displayed provenance and permanent-tree hyperlink resolve. This is a disclosed pending production task, not evidence of a presently verified final PDF.

No exact-budget boundary, claim at B=2, matching marginals for the tilt families, locality theorem, heat-bath conclusion, continuum/Yang-Mills claim or external priority is established. Public publication status and the exact deposited predecessor PDF were not independently reverified in this assignment. The complete proofs of every external bibliography item were not re-audited.

No score, formal proof, numerical verification, build/test result or human-peer-review status follows from this report. The preserved current-source acceptance and new manuscript acceptance are distinct referents. A later change to this manuscript or PR body is not covered automatically by this frozen verdict.

## Operational disposition

Only retained evidence under `D:\Datos\the-eriksson-programme\autonomia\evidencia-298\manuscript-source-audit298A` was written. No source, gate, branch, PR body or remote was modified. No inbound notice arrived while this new audit ran, and no other chat was contacted. No disposable clone was created and no cleanup is pending.

The source-manuscript and package review is complete at the stated SHA. Exact-PDF reproduction and review remain separate pending work, as disclosed in the assignment and frozen PR body.
