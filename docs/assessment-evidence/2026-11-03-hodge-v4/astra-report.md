# Assessment of the exact public v4 artifact

**Paper:** Coarse information and finite rank obstructions for flat lattice Hodge forms.  
**AIRR record:** ARR-2026-7EPM3V3DP796BBRR, v4.  
**Version identifier:** arr:version:06fc6b16-cadb-4184-8931-58a6893392d3.  
**Canonical PDF SHA-256:** e5e9ddcf044ddcfab0e4cae8e2c6ac1a3dca39ff21bf23b20989aaff4b220e05.  
**Extent inspected:** all 15 pages; pages 2–11 also rendered and visually inspected.  
**Recommendation:** minor_revision. **Millennium comparison score: 3.20/10; overall stars: 3.**  
**Independence:** unknown. Requested routing was OpenAI / gpt-6-astra / xhigh. Those are requested configuration labels, not authenticated observations of the served backend or reasoning setting. This is one model assessment, not human peer review or editorial acceptance.

The principal mathematical statements survive this assessment. I found no unresolved objection capable of invalidating a main theorem. The paper is a substantive but limited finite-lattice diagnostic, built from classical Fourier, dimension, trace and implicit-function arguments. Its most useful combination is the actual divergence-free construction with a directional mean of nonnegative derivative weights and local nonlinear observations. The score reflects that concrete contribution and careful hypothesis control, rather than progress toward a Millennium Problem. I recommend minor revisions for reproducibility navigation, terminology and version-specific publication context. A complete independent Lean reconstruction remains outside the checks actually performed.

## Claim-by-claim mathematical findings

### Sections 2–4: the operator, historical witness and real low-frequency band

The counting norm, forward curl and backward divergence have mutually compatible periodic conventions. For a field supported in component j, the unordered plaquettes contribute each transverse derivative once, and the backward j-difference contributes the remaining derivative after reindexing. Equation (2) has no missing factor of two. For general fields the mixed terms in curl and divergence cancel by periodic translation and commuting shifts; this yields the whole-space identity in Section 7. It is not necessary to identify the internal Euclidean coordinates with a matrix Lie algebra.

The two internal coordinates matter. A complex coefficient produces two real degrees of freedom in an actual real vector field, so the dimension 2(2R+1)^d is justified. This would require more care for a single real scalar Fourier field, but that is not the construction here. The condition 2R<n makes the centered frequencies distinct modulo n. The mass and derivative Gram calculations both diagonalize, proving the energy bound for every linear combination, not merely each generator. The n=1, R=0 case and d=1 case are consistent; the later transverse construction separately requires d≥2.

In Section 3 the constant-field calculation gives the necessary exponent σ≥(d−2)/2 when the block size is unbounded. It does not select equality or prove sufficiency, and the text correctly says so. The transverse character is independent of the line direction and sums to zero over the other block coordinate. Thus Q_l A=0, δA=0 and the energy quotient 4 sin²(π/l) are correct, including l=2 and the periodic wrap. The Poincare lower bound and the growing 2R-mode min–max cluster follow. The eigenvalue assertion is correctly limited to a self-adjoint linear repaired operator.

The changed-map identity λ_l+ε_l²+ν_l is exact. Full-space coercivity implies its necessary lower bound; the asserted equivalence is only on the witness line. The dimension-four leakage threshold follows from ε_l²=l²η_l². None of these observations establish full-space sufficiency. The historical square-wave appendix mentioned on page 3 was not separately inspected; it is not needed for the present Fourier proof.

### Sections 5–6: finite budget and quantifier order

For Theorem 5.1, the map (C,V) restricted to the constructed band has rank at most dim F+rank V. Its nonzero kernel vector annihilates both added terms. Consequently an arbitrary real-valued penalty with Φ(0)=0 is allowed, and neither symmetry nor positivity of V is needed. The stated use of codomain dimension is conservative; the argument can also use the effective restricted rank, but the paper does not mislabel that strengthening as its formal endpoint.

Proposition 5.2 independently intersects with ker P. This is the correct way to handle a restricted sector; failure on the full space alone would not suffice. The numerical illustration 2·3^4=162, b=π²/16<1 and 12+149=161 is correct.

In Theorem 6.1, c and the rank bound are fixed before the lattice size is chosen. The displayed finite choice of L ensures both no aliasing and b_R(n_L)<c. Arbitrary scaling or variation of C_L does not alter the kernel dimension. Constant/harmonic constraints have bounded rank at fixed d and N_c, but the entire divergence-free condition has growing codimension and is not justified by this theorem; Section 9 correctly supplies a separate construction for it. Replacing a sector by an unexamined quotient norm would be an unjustified extension, and the paper explicitly avoids it.

### Sections 7–8: derivative repairs and nonlinear hypotheses

The repair G*WG has the stated quadratic form. An upper bound w≤M suffices for the Section 7 upper estimate even for signed weights; M≥0 permits multiplication of the band bound by 1+M. This signed-weight observation is not silently carried into the positive-trace result of Section 9.

Theorem 7.1 is valid for the stated arbitrary energy q with an upper bound on S, because the shrinking ray remains in S. Differentiability at zero produces C(tv)=o(t) on an actual derivative-kernel direction. The local quadratic upper bound on Φ then makes its contribution o(t²), even when its finite constant K is negative. No uniform derivative remainder or neighborhood across lattice sizes is needed. Φ(0)=0 need not be separately assumed: the upper estimate already gives Φ(0)≤0, and the contradiction argument uses the upper estimate only.

Theorem 8.1 correctly pays the additional constraint dimension and requires DP(0) to be onto. The implicit function theorem produces an exact level-set curve with tangent v. Because that curve can leave S, the quadratic energy assumption is essential to the proof: the cross and remainder terms are o(t²). Mere differentiability of C at zero is enough along the curve. The finite-dimensional linear operator T is automatically bounded; symmetry is not needed for this expansion.

I checked the three scope counterexamples on pages 7–8. The norm-power observation and penalty are C1 with vanishing first derivatives but compose to a quadratic form. The curved quadratic sector has no nonzero exactly unseen vector in S while still having vanishing Rayleigh quotients along its exact curve. The C1 nonquadratic energy example genuinely has a positive local sector estimate despite zero energy on S. The singular constraint P(x)=||x||² has only the zero point in its zero fiber and demonstrates why a derivative-rank bound cannot replace regularity. These are valid delimiters, not counterexamples to the actual theorem.

Proposition 8.2 has the right order: choose a large lattice first, then shrink its own curve. The hypotheses allow lattice-dependent penalty constants, inverse derivatives and radii. The condition M_L/n_L²→0 is sufficient for its threshold to vanish.

### Section 9: actual divergence-free mean-weight obstruction

This is the paper's strongest concrete addition. The j-component fields varying only in x_i, with i≠j, belong to ker δ exactly. For 1≤s≤R<n, the two internal quadratures give an orthonormal real family of size 2R. At even n, including the Nyquist frequency does not collapse the two internal coordinates. Frequencies s and n−s are not accidentally identified as real scalar sine/cosine pairs.

Each basis field has a spatially constant squared derivative magnitude and only one nonzero derivative direction. Its repair energy therefore depends exactly on the directional mean b_ij(n), regardless of maxima elsewhere. This yields the displayed trace of the compression. The weighted operator need not preserve the strip; the proof uses compression and diagonal sums, not spectral invariance.

On ker DC_n(0)∩ker δ, the local estimate gives c||v||²≤Q_n(v) after division by t². Rank-nullity supplies at least 2R−dim F_n such directions in the strip. Nonnegativity supplies the remaining nonnegative diagonal terms. This proves (10), including its constants; the last inequality follows from the deliberately coarse bound Σ_{s=1}^R s²≤R³. R=0 is harmless. Choosing each fixed R before taking n→∞ establishes dim F_n→∞. It does not establish positive density per lattice volume, and the manuscript expressly makes no such claim.

The single-site weight n^(d+1) has directional mean n, so it satisfies the subquadratic mean assumption while violating a subquadratic pointwise maximum assumption. The example is sound. Nonnegativity is material to the argument: for a generic signed two-dimensional quadratic form diag(1,−100), observing the second coordinate and adding 101 times its square makes the total coercive, but c(dim E−dim F)≤tr Q fails. This falsifies an unqualified signed-trace extension, which the paper does not claim.

The quadratic-weight boundary construction is valid on the full cochain space. A translation-path argument gives ||A−lift μ(A)||²≤dn²||GA||²; the constant is intentionally loose. Weights 2dn² and the penalty 2n^d||μ||² then suffice. The fixed output dimension is d(N_c²−1), and the varying quadratic penalty constant is permitted by Theorem 9.1. This demonstrates a scale boundary for unrestricted allowance of quadratic means, not an optimal constant or a characterization of all spatial weight patterns.

The penalty counterexamples on pages 10–11 are correct. A C2 observation and a differentiable, nonnegative penalty vanishing at zero yield the stated alternative o(t²) composition on derivative-kernel rays; that analytic observation is not presented as a formalized physical application. One sentence merits clarification: “even when Q_n=0” is an abstract zero-background illustration. For the actual Q_n defined in Section 9 with n>1 and nonnegative weights, Q_n cannot be the zero form because it contains K_0,n. The counterexample already works with admissible w=0, hence Q_n=K_0,n. This is a minor notation/scope issue, not a failure of the obstruction or counterexample.

### Sections 10–11: sufficiency and scaling

Proposition 10.1 is the classical singular-Schur condition. Necessity follows from the zero fiber and the unbounded linear cross term on any null direction of A. Sufficiency follows by completing the square with A† and extending the inverse of C on (ker C)⊥. The two-dimensional example has exactly the claimed fiber value 1−2t+Φ(1). Kernel nonnegativity at the threshold is genuinely insufficient. There is no claim of a new general matrix theorem.

The inspected pinned PhysicalGaugeFixedPrecision source defines the unscaled K_0+aQ*Q−Σ shell and a fixed-volume theorem with the lower constant min(1,a)/C_P minus the perturbation budget. Setting Σ and its majorant to zero gives the specialization described in Section 11. The source does not supply a uniform C_P, so the present obstruction does not contradict that endpoint. Multiplication of K_0 by l² indeed changes the band threshold to 4π²dR²/(N′)². That escapes this proof's vanishing threshold but does not itself prove coercivity. The paper's exclusions of interacting Hessians, continuum limits, uniform localization and a Yang–Mills gap are appropriate.

## Formalization and reference checks actually performed

I retrieved and read 15 selected public Lean files at the paper's printed commits: the physical finite/uniform rank endpoints, the older dimension-four factorized-repair endpoint, whole-space Hodge identity, full-space tangent obstruction, regular-sector curve and energy obstruction, transverse character strip, positive compression trace, finite/asymptotic mean-weight endpoint, quadratic mean repair and torus mean comparison. Their explicit hypotheses and conclusions are consistent with the corresponding manuscript claims. In particular, the physical strip, its dimension and trace, and the derivative-kernel estimate are derived in these files rather than assumed as a certificate. The inspected older factorized theorem is explicitly four-dimensional, matching the manuscript's stated limitation.

This was source inspection, not elaboration or kernel checking. A literal search in the initially inspected Lean sources found no sorry, admit, custom axiom declaration or native_decide token; that is not a dependency-closure audit. The oracle source contains six #print axioms commands; I did not run them. I did not verify the reported fresh-clone executions, compiled object hash, raw oracle outputs, source-manifest agreement or mutation-validator executions. Matching source statements and visible proof bodies do not authenticate any of those computational claims. The paper generally distinguishes analytic statements, source-level specialization and formally claimed endpoints correctly. A complete rebuild and closure audit remain unperformed verification work, not a discovered mathematical counterexample.

The pinned [Mathlib implicit-function source](https://raw.githubusercontent.com/leanprover-community/mathlib4/07642720480157414db592fa85b626dafb71355b/Mathlib/Analysis/Calculus/Implicit.lean) has the cited exact level-set identity and derivative equal to the kernel inclusion. Its strict-derivative interface is compatible with the C1 hypothesis through the conversion explicitly used in RegularSectorCurve. This reference supports the formal dependency claimed; it does not mean this assessment built it.

The [CUNY Dodziuk record](https://academicworks.cuny.edu/gc_pubs/180/) confirms the cited historical publication, but I did not inspect its full proof. Publisher records confirm [Albert](https://epubs.siam.org/doi/10.1137/0117041) and [Carlson–Haynsworth–Markham](https://epubs.siam.org/doi/10.1137/0126013); the latter's abstract describes the generalized Schur complement. Their full texts were not inspected. Proposition 10.1 was checked directly here, so its correctness does not rely on an unexamined citation.

The introduction and relevant scaling passages of [Dimock v2](https://arxiv.org/pdf/1410.2798v2) support the manuscript's distinction between unit spacing/large volume and small-spacing tori, and its warning about constrained renormalization-group forms. The [Spielman author bibliography](https://cs-www.cs.yale.edu/homes/spielman/Research/List.html) confirms [7]'s bibliographic data; full-PDF retrieval failed, so I do not claim to have verified its detailed trace discussion. The author-hosted search excerpt of [Levin–Peres, Chapter 13](https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf) specifically exposes Section 13.4, “The Path Method,” and the comparison setting. Full-PDF retrieval failed; I checked the torus comparison independently and read the pinned TorusMeanPoincare proof. This was a targeted reference check, not an exhaustive priority search. Historical AIRR publication and previous-assessment assertions were not independently verified or used to grade the mathematics.

## Concrete falsifier attempts

The accompanying Python/NumPy/SciPy script uses seed 2631 and constructs the actual periodic differences, real cochains and weights. All assertions passed. These are finite floating-point diagnostics, not proofs:

| Check | Cases and result |
|---|---|
| Whole-space curl/divergence versus gradient energy | 10 cases spanning d=1–4 and including n=1 and n=2; largest relative discrepancy 2.11×10^-16. |
| Original block-kernel witness | 10 cases, l in {2,3,4,5,7}, N′ in {1,2}; block image/divergence vanish numerically and the exact trigonometric quotient agrees. |
| Actual transverse strip | 21 (d,n,R) cases, including R=0, R=n−1 and even n; correct rank, Gram matrix and zero divergence. Directional single-site spikes coexist with weights up to 10,000 in unrelated entries. Largest relative trace discrepancy 2.15×10^-16. |
| Positive-trace kernel inequality | Random observation restrictions in the nonzero strip cases; compressed positivity and kernel/trace comparison passed. |
| Nonsymmetric finite-rank repair | A 50-dimensional real band with seven observations and a nonsymmetric rank-nine repair has a 34-dimensional joint kernel; selected witness residuals 1.38×10^-15 and 3.02×10^-14, Rayleigh quotient 1.44836 below bound 3.89910. |
| Quadratic-weight boundary | Six small-torus spectra; the repair-plus-mean-penalty minimum is 2, hence exceeds the claimed lower bound 1. |
| Nonlinear and cross-coupling examples | Direct algebra checked; numerical spot checks agree with the vanishing curved-sector quotient, positive C1-energy sector quotient, norm-power composition and unbounded Schur fiber. |

No numerical test attempted to prove an asymptotic limit. The limits and all-scale quantifier orders were evaluated analytically as described above.

## Remaining issues and proportionate revisions

1. **Formal reproducibility navigation:** include stable clickable paths for the declaration map, exact map/package revision and each reproduction entrypoint. The PDF supplies source commits and generic filenames but does not itself identify the map revision by hash or print the endpoint mapping. The public sources I selected were accessible; the reported complete reconstruction evidence is still unverified by this assessment. This is a verification limitation, not evidence that the claims are false.
2. **Novelty and significance:** the individual mechanisms are classical and the main results are finite flat specializations. A closer comparison with established low-rank spectral approximation and observation-budget arguments would sharpen what is specific to the directional mean construction. No exhaustive priority claim can be validated from the present bibliography. The manuscript already avoids asserting one.
3. **Scope wording:** clarify the abstract zero-energy illustration Q_n=0 on page 11 as noted above. State explicitly that “output rank” in the displayed theorem is the codomain dimension, or give the readily available restricted-derivative-rank version separately. The existing dimension theorem is valid.
4. **Artifact status:** page 1 and page 14 call the file an undeposited v4 candidate and refer to v3 as current, whereas the assessment assignment locks it as public v4. A subsequent version or external metadata should reconcile these stale status statements without rewriting the artifact evaluated here. No previous report or score was inherited.
5. **Useful optional quantitative clarification:** inequality (10) can be optimized in R to give a lower growth scale of order n/sqrt(1+b_ij(n)) when the cutoff is chosen in range, rather than only divergence. This is a consequence to state carefully if desired, not a missing premise or a claimed positive-volume-density theorem.

**Unresolved material objections: none identified.** Remaining formal verification and priority-search limits are stated explicitly above. None has been converted into an allegation of an invalid main theorem without evidence.

## Criteria and score basis

| Criterion | Stars | Basis |
|---|---:|---|
| Correctness confidence | 4/5 | All displayed main proofs checked; actual divergence-free dimensions, trace and nonlinear limits withstand targeted falsifier attempts. Complete formal closure not checked. |
| Rigor | 4/5 | Quantifiers, counting norm, real dimension, local penalties and exact-sector curve are explicit; the analytic/formal distinction is mostly careful. |
| Novelty | 2/5 | Classical mechanisms with a useful concrete directional-mean and physical-space synthesis; broad priority or a new general spectral principle is not established. |
| Significance | 2/5 | A worthwhile obstruction to a narrowly specified repair route; no interacting, continuum or mass-gap consequence. |
| Reproducibility | 3/5 | Accessible pinned source statements and transparent analytic calculations, but no assessor-run Lean build, oracle/compiled hash validation or full dependency audit. |

The 3.20/10 comparison score means an acceptable, substantive finite-lattice contribution with modest novelty and scope. It is not a probability of correctness, a school grade or evidence of a Millennium solution. The related exact-schema JSON and separate controls record are authoritative for machine-readable metadata and disclosure of what was actually observed.
