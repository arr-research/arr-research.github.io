# Author response and visible scope clarification — v9

Exact assessed PDF: SHA256 e4bf6bfe658a59a9a0d61dc0f5e97d530dd6dd3504ba8d51052d37d747afd3e8, 51 pages. Source 28640cd82e5b2ae9a6da8c78ca772bc41134c0c6. This response accompanies the unchanged PDF; it is not a revised PDF or another assessment.

## Model assessments and review context

The first and only numerical assessment of these exact bytes is 5.40/10 on AIRR's Millennium scale, overall 5/10, with criterion ratings 4/4/3/3/4 out of 5 and recommendation minor_revision. The complete scientific report, native response, assignment, importance assessment and actual model/context disclosure accompany this response. Requested gpt-6-astra/high; served backend and effort are unverified. Same-provider involvement and shared filesystem prevent an independence claim. Historical scores visible in the manuscript are disclosed exposure and are not inherited. This is neither human peer review nor acceptance into AIRR's accepted collection. No review was repeated to improve the score.

## O3 — clarification of the abstract's scope

The finite-positive-ratio lower bound in Theorem 34 and the quadratic-order conclusion in Corollary 38 are asserted here **with a fixed positive density floor 0<b<1**, exactly as formally stated on pages 45 and 48. Read the corresponding abstract sentence on page 1 with this qualification. The public metadata abstract includes it explicitly. In the quadratic-order assertion, rho and b are fixed, the dimension limit is taken first, and only then C decreases to zero. The reviewer suggested a possible nonnegative extension; this release does not assert or rely on that extension. The unchanged PDF and the reviewer-identified front-matter omission remain visible.

## O1 — relation to existing results and priority limits

Historical priority remains unestablished. The source comparisons below report the bounded comparison made in the complete assessment; they are not an exhaustive search or a new originality certificate.

- Kirshner–Samorodnitsky, arXiv:1909.11929v1, Theorems 1.3 and 1.8 and Propositions 2.6–2.7, supply homogeneous and distribution-sensitive hypercontractive inputs. The present manuscript applies those results and derives its specific entropy expansion and degree/dimension consequences; it does not claim to invent the improved inequalities.
- Heilman–Mossel–Oleszkiewicz, introductory tail-space results and Theorems 1.2–1.4, concern same-exponent heat smoothing, Poincare estimates and special-valued tail functions. Volberg, arXiv:2208.00472v2, discusses Banach-valued Lp tail-space estimates and that literature. The present Theorem 28 instead asks when the endpoint norm of the high-degree Boolean noise operator from L2 to L^(1+1/rho) vanishes as the degree cutoff and dimension vary. The checked statements do not directly give its square-root degree/dimension threshold. This distinction is not proof that no prior result implies it.
- Alon–Andoni–Kaufman–Matulef–Rubinfeld–Xie, Fact 2.3 and Section 3.1, already provide the Fourier characterization of k-wise independence, erasure and positivity-repair methods. The present density construction uses a specialized one-sided odd truncation to control positivity simultaneously with the critical moment budget and spectrum. General erasure or positivity repair is not claimed as new.
- Miclo's hyperbounded Markov result and Wang's operator-tail criterion concern invariant Markov operators and operator norms. They are not identified here with the scalar density moment E r^s of the multiplicative congruence. Gross's additive Schrodinger framework is another important predecessor; a fixed positive density floor alone does not distinguish the examples by absence of inverse-density control. The operator/form correspondence has not been established.

Primary links checked in the assessment: https://arxiv.org/html/1909.11929v1 ; https://www.stevenheilman.org/~heilman/papers/hmo.pdf ; https://arxiv.org/html/2208.00472v2 ; https://www.cs.columbia.edu/~andoni/papers/kwise.pdf ; https://perso.math.univ-toulouse.fr/miclo/files/2012/04/hyperboundedness.pdf ; https://arxiv.org/html/1305.4460v6 ; https://arxiv.org/html/2412.20282v2 . See the full report for exact checked passages and access limitations. The requested more systematic literature positioning remains an editorial limitation of this PDF.

## O2 — reading map and preserved chronology

The report's presentation objection is retained. This supplementary map helps locate the final results without deleting any earlier evidence:

| Result | Location and dependency |
|---|---|
| Endpoint high-degree vanishing scale and marginal rigidity | Theorem 28, Lemma 29, Corollary 30; pages 36–40. Distribution-sensitive hypercontractivity and an entropy deficit enter here. |
| Positivity-preserving erasure and every sub-square-root density construction | Lemma 31 and Theorem 32; pages 40–43. The one-sided pointwise estimate is separate from the norm estimate. |
| Attained fixed-ratio profile | Theorem 33; pages 43–44. It is a constructed upper bound on the gap infimum, not its optimum. |
| Uniform fixed-positive-ratio lower bound | Theorem 34 and Lemmas 35–36; pages 44–47. Mean-one moment reserve and all three degree blocks, including their coupling, are required. |
| Quadratic small-ratio order | Corollary 38; page 48. Combines the universal lower bound and an attained upper profile, for fixed rho,b and dimension limit first. |

The preceding code, marginal, norm-budget and strict-tail results remain part of the grouped manuscript. The review history at the end is provenance, not an additional mathematical proof. This unchanged PDF has not undergone the requested structural shortening; that limitation remains openly recorded.

## O4 — effectiveness and significance

The entropy-deficit modulus, sufficiently large dimension and construction constants are existential or conservative. Neither the exact finite-C optimum nor the optimal small-C coefficient is determined. Exact Fourier zeros are essential to the stated rigidity results; no noisy-marginal stability theorem is supplied. These are results for finite Boolean global-weight transfer operators. They provide no calibrated finite-size certificate, local heat-bath mixing guarantee, fixed-range Gibbs theorem, physical or continuum spectral gap, or Yang–Mills resolution. Correctness, originality and practical significance are distinct; the assessment's limitations on novelty and broad impact remain in force.

## Disposition

No objection invalidating a formally stated main theorem was identified in this review. O3 is resolved at the public-claim level by the explicit fixed-floor qualification; the PDF's original omission remains preserved. O1, O2 and O4 are retained qualifications with the supplementary comparison, navigation and limits above, not represented as fully solved research or editorial issues. Publication is on the Working-paper route only.
