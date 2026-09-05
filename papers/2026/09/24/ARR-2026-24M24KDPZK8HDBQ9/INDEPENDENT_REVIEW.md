# Independent internal review of the consolidated inertia manuscript

Reviewer: separate Codex subagent; 5 September 2026. This is internal mathematical review, not independent human refereeing. No publication was performed.

## Scope and conclusion

Read `outputs/cycle2/commutator/sharp_stability.md` in full and Sections 1–4 and 7 of `outputs/inertia_publication/paper.md`. Separately examined the proposed new balanced-inertia theorem for multiplicities (3,3), its parametric argument, its exact certificate, and its extremal family. No substantive mathematical objection was found within this bounded scope. The new result supplies the sharp two-sided inequality

\[
\frac{17}{36}D_*\leq\delta\leq D_*
\]

for inertia (3,3), in every fixed ambient dimension at least six. The right coefficient is the previously established optimal reverse coefficient; the newly checked contribution is 17/36 on the left.

The control script is `independent_balanced_review.py`, with output `independent_balanced_review_certificate.json`. It uses integer and rational arithmetic. It imports neither the author's active-set enumeration nor the recursive Horn generator.

## New balanced theorem: independent geometry

Write E(a)=2(1−a1), U(a)=||a−u||1, q(a)=E(a)−U(a), and u=(1/3,1/3,1/3). The ordered three-coordinate probability simplex has vertices e=(1,0,0), z=(1/2,1/2,0), and u. Cutting at a2=1/3 gives the two triangles conv{e,v,u} and conv{z,v,u}, where v=(2/3,1/3,0). On either triangle U is affine. Specifically it equals 2(a1−1/3) when a2≤1/3 and 2(1/3−a3) when a2≥1/3.

On each product of two triangles, D1=E(a)+U(b) and D2=U(a)+E(b) are affine. Their difference is q(a)−q(b). Cutting this product by that hyperplane therefore gives cells on which D*=min(D1,D2) is affine, including their boundaries. Each product has nine vertices and eighteen edges. A single halfspace cut introduces new vertices only where the cut meets original edges; original vertices on the cut are already included. This yields 22 distinct vertices globally: the sixteen ordered pairs from {e,v,z,u}, together with

- (w,v) and its interchange, where w=(2/3,1/6,1/6);
- (r,z) and its interchange, where r=(7/12,5/24,5/24);
- (t,z) and its interchange, where t=(7/12,1/3,1/12).

The script reconstructs all these intersections using exact rational interpolation and verifies equality with the author's complete vertex set. Thus the exhaustiveness of the proof can be presented geometrically and need not rest on numerical enumeration.

Ordered-chamber convexity of kappa and affinity of D* imply that kappa+(17/36)D* is convex on each cell. Every cell is compact and is the convex hull of its vertices. Bounding this convex function by two at all vertices proves the desired inequality throughout the cell; no concavity or global affinity of D* is being presumed.

## Independent Horn check

The script counts Littlewood–Richardson skew tableaux directly: rows weakly increase, columns strictly increase, and each prefix of the right-to-left, top-to-bottom reading word is a lattice word. It finds 21, 126, 228, 126 and 21 admissible triples of subset sizes one through five in dimension six, totaling 522. Some coefficients equal two; all positive coefficients are retained. It checks all 522 inequalities at each of the 22 rational common spectra, for 11,484 exact Horn inequalities in total. Every slack is nonnegative. Every common spectrum is ordered and nonnegative, has the declared trace, and satisfies trace+(17/36)D*≤2. These checks establish Horn feasibility of the supplied witnesses; sufficiency of the classical Horn theorem is an imported result, not something proved by the script.

The source SHA-256 of the checked author certificate is d776f3d728c51341ddb6060a5c1d9c89ddbe0c2e3869b15d54af4adbe11a98f9. The independent script source SHA-256 is 878d3fa2853b01eff03cb85404602d91a72f3298fa2b815f42d5e026a07902e7.

## Ambient dimension and optimality

For d≥6, zero-padding a six-dimensional realizing factor gives the same objective, so each vertex upper bound persists. Equivalently, kappa_d of the padded target is at most kappa_6. Equality under zero-padding for general targets is neither needed nor claimed. Convexity can then be applied directly in the d-dimensional ordered chamber, with a fixed block of zeros between the positive and negative lists.

At a=r and b=z, the elementary spectral lower bound is sum_j max(a_j,b_j)=31/24. The certified upper witness has that trace. Hence the cost equals 31/24 in every ambient dimension d≥6, D*=3/2, and the boundary ratio D*/delta equals 36/17.

For exact inertia (3,3), keep a=r and take b_eta=(1/2−eta/2,1/2−eta/2,eta), with 0<eta<5/24. Both lists are strictly positive and ordered. The two orientations have distances 3/2−2eta and 3/2+eta, so D*=3/2−2eta. The elementary lower bound gives kappa_d≥31/24−eta/2. The already established sharp inequality gives kappa_d≤31/24+(17/18)eta. Thus kappa_d tends to 31/24 by an explicit sandwich, and D*/delta tends to 36/17 for each fixed number of ambient zeros. This avoids any separate continuity assumption in the new sharpness argument.

## Recommended corrections and clarifications in the integration

1. **State continuity at boundaries explicitly.** Several older sharpness arguments invoke fixed-dimensional continuity, which is valid but should not be attributed to convexity alone. The Horn epigraph is a projection of a finite polyhedron; the cost is finite on the entire trace-zero ordered chamber. Consequently it is polyhedral there, expressible as a finite maximum of linear forms on its domain, and is continuous in the relative topology, including boundary spectra. This short lemma covers the older perturbation arguments without assuming general zero-padding invariance.

2. **Use one normalization in the explicit strict gap.** In old Section 4 the lists were normalized by setting P=1, but the subsequent phrase “in original scaling” writes mn*a_m*b_n/P. If the symbols remain normalized, the displayed gap must be P*mn*a_m*b_n*(H−c_mn). The former expression is correct only if a_m and b_n are redefined as unnormalized magnitudes. State the convention rather than asking the reader to infer it.

3. **Update the scope of the balanced open problem.** After adding the (3,3) theorem, do not say that the balanced forward coefficient is wholly undetermined. The coefficient is now sharp at N=3; N=2 follows from the prior four-level formula, if it is included with attribution. General balanced N≥4 remains open here. The new certificate proves a stability constant, not a general six-dimensional cost formula.

4. **Distinguish exact cost from witness cost in the vertex table.** Upper witnesses alone suffice at the 22 vertices. Only the extremizing row needs an independently matching lower bound for sharpness. Label the table column “certified trace upper bound” unless exact optimality is separately justified in that row.

5. **Attach replay files to the review delivery.** The new finite proof should have its exact rational witness data and both verifier scripts available with the PDF. State that the geometric enumeration proves coverage and the exact arithmetic establishes the finite certificates; floating-point exploration is not part of the proof.

No further changes to the reviewed algebraic unbalanced constants, interpolation sharpness, rank-only threshold, or the ambient-independent 4/3 transportation separation benchmark are requested by this review.

## Final integration review

Read the complete consolidated manuscript `outputs/inertia_revision3/paper.md`, then read the small subsequent edits to the affected passages. The final reviewed source SHA-256 is **385812881d978c6c0e9c67c66ef4783e9df38fe4f4f0153b2e871ff46cd9f061**. No replay or literature search was repeated for this integration review.

The theorem statements agree with their proofs. The 13 symmetry-reduced rows of Table 1 correctly represent the 22 ordered vertices, with the declared common spectra, distances and trace upper bounds. Internal theorem, section and bibliographic references are coherent. The scope section correctly leaves the balanced forward coefficient for N≥4 open, attributes the four- and five-level formulas to their antecedents, and distinguishes the new finite stability proof from a general six-dimensional cost formula.

All earlier recommendations were incorporated. This final pass additionally requested explicit hypotheses and normalization in four places, now corrected:

- The moment-to-deficit step in Section 5.1 states m≤n, which is needed to identify H=(n+1)/2. The preceding Horn and elementary lower bounds remain valid for arbitrary sign multiplicities.
- Section 5.4 explicitly sets P=1, handles m>n by sign reversal, restricts the upper-coefficient construction to 2≤m≤n, and specifies 0<eta<1 for the opposite-boundary perturbation.
- Boundary arguments retain the reference H of the fixed-inertia stratum. Section 5.5 explicitly sets P=1 and keeps H=2 on the closed domain even when actual inertia drops. Thus its extended deficit is 2−kappa_d, as required by the vertex argument.
- The transportation separation benchmark in Section 6 is explicitly described as a normalized matrix cost.

These edits resolve the possible ambiguities without changing the proved constants or rational certificates. **No outstanding mathematical or integration objection remains in this bounded internal review.** This conclusion is tied to the source hash above; it does not certify external priority, formal proof-assistant verification, or PDF typesetting.
