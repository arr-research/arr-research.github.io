# Separate internal review — ternary low-rank Weyl probes

6 September 2026. Reviewer: a separate Codex research agent assigned to the passive-routing line, not the constructing quantum agent. This is an internal AI-assisted review within the same research cycle, not external refereeing or a formal proof-assistant certificate.

**Disposition: PASS within the stated scope.** I read the entire manuscript `ternary_low_rank.md`, including every proof, and found no substantive mathematical error. The reviewed source SHA-256 is `7ff52dd2210f7b63ab0060c8fa021d1e352a54fd6a91e3b851faaa171d107700`.

## Proof audit

The operational factorization in Lemma 1 has the correct direction of the positive squares and the correct dimension factor. Starting with a normalized POVM, the partial trace gives `sum B_j* B_j = d I`; the forward factors therefore require division by `sqrt(d)`. Starting with a sparse factorization instead gives `sum B_j* B_j = I`; Weyl twirling then requires the displayed POVM prefactor `1/d`. The support of `Tr(C W_g* W_h)` is a translated and phase-adjusted Weyl support and has the prescribed size. A separate exact rank-three probe in dimension nine, described below, directly checks both the twirl and all outcome supports.

Lemma 2's central subgroup count is valid in cyclic prime-power dimension. The minimal coordinate valuation can be put in one generator by swapping and applying an invertible determinant-one coordinate change. The two resulting central cyclic orders multiply to `d/q`; consequently the sector dimension is `q`, with no omitted multiplicity. The nonzero coefficient assumptions make the two-circle argument applicable. The kernel recurrence supplies nullity one on each singular block, and the strict rank threshold excludes these noncommuting trinomials even at the smallest allowed dimension nine.

Lemma 3 proves the shape of every individual square, not merely its rank. For commuting relative support, the character pair is injective because the two relative labels generate the group. At most two zeros and a group order divisible by three force group order exactly three below the threshold. Right multiplication by a supported Weyl preserves `CC*`; therefore the fixed commuting order-three algebra is obtained in the original output coordinates. This avoids an otherwise possible unsupported step from a rank theorem to a state classification.

The positive-sum range inclusion is used correctly. It confines every factor to the support of the target state. The small-line-union classification, private cells and support-contained-line test then prove the uniqueness claimed in Theorem A against all positive decompositions into the twelve projectors. Parallel pairs can be compressed into one three-sparse square, while crossing pairs and triangles cannot; the minimum square counts are therefore the stated one, two and three. The complex is a state complex with unique coefficients in each included face, not a classification by unordered spectrum alone.

Theorem B correctly distinguishes the existence of a two-list state at a given rank from the classification of all two-list states. Every relevant binomial square is a flat complement of one line projector. A rank-six-cell positive sum of such factors forces identical ranges and hence a single normalized complement state. Only the twelve parallel-edge midpoints permit two labels. The four-term construction has four distinct Weyl labels, rank `4d/9`, positive eigenvalue nine before normalization and trace `4d`; it therefore proves the asserted exact list value four after the three-list obstruction. The dimension-nine corollary separately excludes two labels at rank seven and does not claim exact values at ranks one or two.

The cutoff example has order nine, kills exactly two equal-dimensional eigenspaces and retains a nonzero `T^2` coefficient outside the order-three subgroup. The source correctly separates cyclic Weyl sparsity from tensor-qutrit sparsity and excludes dimension three from the commuting nine-cell theorem.

## Independent computational checks

I reran the constructor's `ternary_verify.py`: PASS, including 4,095 line subsets, matrix dimensions 9, 27 and 81, and 6,320 ordered distinct nonzero label pairs in dimension nine.

I also wrote `independent_ternary_review.py` without importing the constructor's verifier. It reconstructs the twelve lines as collinear triples rather than from normal-vector equations. It checks every nonempty line family, all 150 low-support cases, the absence of hidden lines, private-cell recovery and each spectrum formula using exact rational weights. It confirms twelve vertices, twelve parallel edges, fifty-four crossing edges and seventy-two triangles.

The separate matrix arithmetic uses rational coefficients in the field `Q(omega)`. It verifies the actual cyclic four-term matrices in dimensions nine and twenty-seven, their ranks, traces and the exact identity `(CC*)^2 = 9 CC*`. For the dimension-nine rank-three state supported on coordinates 0, 3 and 6, it constructs all 81 covariant measurement vectors, checks the full 27-by-27 POVM sum with prefactor `1/9`, and verifies that each outcome has exactly its three permitted channel labels. Finally it recomputes the central subgroup size by direct finite subgroup closure for all 5,616 noncommuting ordered pairs in dimension nine.

The separate verifier returns 6,309 checks with PASS. Its JSON records the source, constructor verifier, constructor certificate and independent verifier hashes. It checks finite geometric and representation content and selected operational realizations; the universal arbitrary-coefficient and arbitrary-dimension claims still depend on the proofs audited above.

## Limits

No worldwide priority assessment, complete literature audit, approximate-decoding stability theorem or higher-rank classification is certified by this review. The state count, factorization length and POVM outcome count remain correctly distinguished. The review does not assign a numerical paper rating or assert independent human approval.
