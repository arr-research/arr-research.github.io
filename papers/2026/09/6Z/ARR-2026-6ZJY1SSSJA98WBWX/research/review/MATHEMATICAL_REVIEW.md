# Separate internal review: balanced inertia (5,5)

Reviewer: a separate research agent in the same model family as the constructor. Date: 6 September 2026. This is internal review, not independent human refereeing.

**Verdict: PASS within the scope below. No blocking mathematical error found.** The forward coefficient 113/152, its optimality in every fixed ambient dimension at least ten, and the four-point equality classification are supported by the analytic argument and independently reconstructed finite certificates.

Reviewed manuscript: `paper.md`, SHA-256 `a739718945c9d5ebb60e05766005d60e65ad34ac05cf423c55435e1496b05ae9`. The associated PDF supplied by the parent task has SHA-256 `9e38457c9c30445e41dfe2318985ab04c85c1e2b279d34a979d651c3bea9faf2`. This reviewer read the full mathematical source. PDF layout and source-to-PDF correspondence are reviewed separately by the parent task; this report does not substitute for that check.

## Independent reconstruction and exact checks

The review program imports none of the constructor's geometry, recursive Horn generator, optimizer, or verifier. It reconstructs the base cells through their explicit step-coordinate geometry and generates Horn triples by existence of semistandard lattice-word Littlewood–Richardson tableaux. The constructor instead uses recursive Horn inequalities. The LR characterization and Horn sufficiency are classical external input, properly attributed to [Fulton](https://arxiv.org/abs/math/9908012) and [Knutson–Tao](https://arxiv.org/abs/math/9807160); neither is claimed as a new result or proved by this finite run.

The independent reconstruction returns 11 base vertices, 30 base edges, 267 ordered cut-product vertices, and 139 sign classes. It produces exactly 191,353 Horn triples, with size counts 55, 1287, 12140, 46208, 71973, 46208, 12140, 1287, 55. The complete independently generated set equals the constructor's set.

Every primal spectrum is checked in both sign orientations, by direct indexed integer sums in the full unmerged Horn system. There are 53,387,487 inequality evaluations including repeated symmetric pairs and the midpoint. The distinct ordered conditions are the same 51,282,604 conditions quoted by the manuscript. Normalization, order, positivity and integer magnitude bounds are checked explicitly. All 139 dual certificates, containing 525 nonzero weighted terms, have admissible inequalities, nonnegative weights, the stated nonnegative residual coefficients, and objective exactly equal to the primal trace. No floating-point solver is used in this review.

The four zero-slack vertices are exactly (e,u), (u,e), (A,B), (B,A). The other 263 ordered vertices have minimum slack 7/80. Restricting to the manuscript's 32 cells gives 22 cells with no zero vertex, eight with one, and two with two. The review also checks redundant uniform-face cells; these introduce no additional candidate contact set. The only nontrivial candidate contact hulls are the two stated segments.

The midpoint witness has trace 69/40, distance 19/20 and positive stability gap 91/160, with every Horn inequality satisfied exactly. Its positive gap is a sufficient upper-cost certificate; the midpoint's exact optimal cost is not needed or asserted.

## Analytic argument inspected

1. **Normalization and quantifiers.** The conversion between a self-commutator factor and two positive matrices of common spectrum preserves the stated one-half normalization. The spectral lists have mass one after division by P, and the reference ceiling remains 3 on the compact closure. Exact inertia means both fifth coordinates are strictly positive. The limiting family is nonempty for every fixed d≥10.

2. **Finite coverage and convexity.** The step-coordinate cone has one apex and a product-simplex base. The active positive coefficients give face dimension p+q−2 on the base, yielding the displayed vertex and edge rules. Cutting product cells adds vertices only along their edges. U and D are affine on the stated cells. Convexity of the value is used only on the closed ordered spectral chamber, where finite-dimensional LP duality applies. Thus vertex upper bounds cover the full domain; this is not an assertion of convexity under arbitrary matrix mixing.

3. **All ambient dimensions.** A dimension-ten primal factor can be padded with zeros, yielding the required upper bound in every larger fixed dimension. The lower bound at the sharp pair is established separately. The argument does not assume general invariance of exact cost under zero padding.

4. **Tail obstruction.** The rank-two Horn triple ((1,3),(1,d−1),(2,d−1)) is admissible by its index sum and three rank-one tests. Applied to −F it gives s1+s3−s2−sd≥b2−a2. The min-max inequalities give s2≥b2 and si≥ai for the positive tail. Summing gives the claimed bound 3b2−a2+Σ(i≥4)ai. The assumptions ensure the positive tail and the two negative directions fit in the ambient space. At (A,B) the lower bound is exactly 127/80, matching the independent primal witness.

5. **Sharpness inside the stratum.** For 0<η<1/5 the displayed Bη is ordered, positive and normalized. Its two distance branches are 19/10−6η and 19/10+3η, so the stated minimum is correct. The lower and upper cost bounds tend to 127/80 in each fixed ambient dimension. Dividing by a distance tending to 19/10 proves the ratio tends to 113/152 without changing d.

6. **Complete equality classification.** On each cut cell the gap is concave and nonnegative. A zero can use only zero-gap vertices in a convex decomposition. The exact incidence check reduces the remaining possibilities to two segments. Padding preserves the midpoint's positive gap lower bound; concavity gives (91/80)min(t,1−t) on either segment. This excludes every interior point. The four endpoints are actual contacts by the one-spike formula and the sharp tail obstruction. None has exact inertia (5,5), proving strictness throughout that stratum.

The reverse coefficient 2 and its sharpness are explicitly imported from the predecessor. They are not presented as new in this manuscript. The prior theorem has the same normalization and applies to every fixed ambient zero count.

## Scope and reproducibility

Run `python review/independent_review.py` from the manuscript directory with NumPy installed. Its independent LR cache is tied to the review program's hash; absent a matching cache it reconstructs the tableaux. The machine-readable result is `review/independent_review.json` and includes source hashes, every certificate summary and cell incidence.

This review does not establish bibliographic priority, prove the imported Horn theorem, run a proof assistant, or resolve multiplicities six and above. The finite program count must not be interpreted as a polynomial total-time algorithm. Within those limits, the result is supported as a precise new evaluation and equality classification of the previously developed stability theory.
