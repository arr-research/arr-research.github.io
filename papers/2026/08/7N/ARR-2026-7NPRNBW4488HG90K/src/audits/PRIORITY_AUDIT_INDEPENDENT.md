# Independent priority and self-collision audit

**Proposed Paper 28:** *One-Spike Inverse Self-Commutators and Exact Three-versus-Four-Kick Curvature Synthesis*  
**Audit date:** 2026-08-24 (Europe/Stockholm)  
**Scope audited:** the exact one-spike inverse Hermitian self-commutator cost and optimizer rigidity/stability, together with the four-kick identity \(A_4(F)=16\kappa_d(F)\).  
**Status:** internal priority audit, not peer review and not a proof of global novelty.

## Bottom line

**Conditional GO.** The combined paper can support a defensible contribution, but only if its novelty statements are narrowed and its relationship to the author's own earlier records is explicit.

The strongest apparently new package is:

1. a dimension-free exact solution on the full one-spike cone, beyond the previously public dimensions three, four, and five;
2. rigidity of the squared singular-value multiset for **every** balanced optimum, not merely an optimal constructor or a minimum-rank statement;
3. sharp fixed-mass \(\ell^1\) stability, with its constants and equality families stated in the paper's spectral normalization; and
4. an all-target four-kick variational identity, including non-sign-paired targets, extending the already public sign-paired equality face.

The paper should **not** claim invention of weighted-shift self-commutator constructions, Horn feasibility, group-commutator/four-kick mechanisms, the low-dimensional inverse-cost formulas, the triangular-loop bridge in those dimensions, the sign-paired four-kick equality case, or general Gini/mean-deviation inequalities.

## Collision taxonomy

Here, an **exact collision** means that the same theorem, a literal special case, or essentially the same statement is already present in an earlier record. A **mechanism collision** means that the proof device or structural idea is known but the present sharp optimization statement was not located. An **adjacent result** addresses a nearby problem without supplying the audited theorem.

| Audited component | Exact collision | Mechanism collision | Adjacent results | Priority assessment and safe claim |
|---|---|---|---|---|
| \(\kappa_d(F)=\sum_j j b_j\) on the full one-spike cone | The local `work/one-spike-selfcommutator-rigidity` package contains the formula. Public author papers give its \(d=3,4,5\) slices. | Fan--Fong weighted shifts and Horn/Klyachko/Littlewood--Richardson spectral feasibility. | Weiss's unrestricted, generally non-Hermitian factorization problem; forward commutator inequalities. | Claim a **dimension-free extension and synthesis**, not a wholly new inverse-commutator program and not novelty in \(d\le5\). |
| Every optimum has squared singular values \(2\sum_{j=\ell}^n b_j\) and rank \(n\) | Present in the local one-spike package. No matching public external antecedent was located. Earlier public low-dimensional papers contain optimal constructors/rank information, which must be distinguished from every-optimizer rigidity. | Equality analysis in Horn inequalities and singular-value variational principles. | Equality cases for forward commutator bounds. | Defensible as **every-optimizer singular-spectrum rigidity in arbitrary dimension**, subject to an explicit self-development disclosure. |
| Sharp fixed-mass \(\ell^1\) stability | Present in the local one-spike package. No exact public spectral-normalization theorem was located. | The deficit is a Gini pairwise-dispersion functional; sharp Gini-mean-difference versus mean-absolute-deviation bounds are established literature. | Quantitative polygonal isoperimetry. | Claim the **exact constants and equality families for this ordered spectral simplex**, while citing the Gini/MAD literature and avoiding a claim that the underlying dispersion inequality is unprecedented. |
| Three-kick identity \(A_3=12\sqrt3\,\kappa_d\) | Public author papers already state this bridge in \(d=3,4,5\). | BCH/group-commutator synthesis and triangular-loop geometry. | Quantum simulation product formulas and non-Abelian/Zeno holonomy. | Present as a dimension-free consolidation/corollary of the inverse problem, not as a new low-dimensional bridge. |
| Four-kick identity \(A_4=16\kappa_d\) | The author's public matrix-isoperimetry paper already gives the exact sign-paired equality face, which implies this value there. | The author's operational-curvature paper already uses the balanced four-kick loop \((h,g,-h,-g)\); group-commutator product formulas are standard. | General polygonal isoperimetry. | Claim an **all-target variational identity extending the sign-paired case**, with particular emphasis on non-sign-paired targets. Do not call the four-kick mechanism itself new. |
| Universal ratio \(A_4/A_3=4/(3\sqrt3)\) | It follows immediately wherever the two exact identities hold; its low-dimensional content is already implicit in the author's earlier results. | Algebraic comparison of two loop normalizations. | None material. | State as a corollary of the all-dimensional identities; do not oversell it as an independent deep theorem. |

## Self-collision audit

### 1. Exact local antecedent: one-spike package

The directory `work/one-spike-selfcommutator-rigidity` contains a theorem package whose `README.md`, `CLAIM_LEDGER.md`, `SUBMISSION_SHEET.md`, verifier, and stored results already state the exact cost, the singular spectrum and rank of every optimum, and the sharp trace-norm/\(\ell^1\) stability theorem. This is an **exact internal collision** with the central one-spike contribution of Paper 28.

The package appears to be an earlier development artifact rather than an indexed public paper: no public record with its exact title was located in the searches described below. Its `SUBMISSION_SHEET.md` is evidence of preparation for submission, not by itself evidence that a public deposit occurred. Before asserting a first public disclosure date, the author should check the relevant submission dashboard and confirmation email.

Recorded local hashes:

- `CLAIM_LEDGER.md`: `D001B593D76D06E422F6527D9DCBB2F1A1BCF33404CDFB1C7A7365F7AC60E75B`
- `README.md`: `D7D4B65F4625BD52608B0A502C1F1EC61F28A11DF84B53C4025AE846E2C9C56F`
- `SUBMISSION_SHEET.md`: `4B9DCFD3A5B90F6F14D4EA3E643732E4750D518464A189659938D163D7FE3F4E`
- `verify_one_spike.py`: `C15B3D9139C94D3E52A930AEB992C273E1F29D363B80731F87819A7F0A8D7196`

**Required treatment:** Paper 28 should be framed as the consolidated paper version of this line of work, not as an independent rediscovery. Preserve the local package and record its relationship in the final provenance metadata.

### 2. Strong local antecedent: general rank-adaptive bounds

The directory `work/general-selfcommutator-tax` contains a complete nine-page PDF/LaTeX/reproducibility package on sharp rank-adaptive bounds for inverse self-commutators. It gives all-dimensional bounds and equality classifications, includes the uniform one-spike upper extremizer, and uses the same Horn-certificate architecture. It explicitly leaves sharp stability open.

Relevant hashes recorded locally:

- `paper/Sharp_Rank_Adaptive_Bounds_for_Inverse_Self_Commutators.pdf`: `AF302CBAA12CCF9E5B73C35BBC8ECEED519110DB34641E116C42C0C44FE9E65D`
- `paper/rank_adaptive_selfcommutator_tax.tex`: `ED42F0DC63DF6B4B419852271545CEDC1580F9CD28A0E869FA8155448BF0CCC7`
- `output/release/Sharp_Rank_Adaptive_Bounds_Reproducibility.zip`: `80864B334B3CD371E23A523724D26DB6B8CC70ADB28AFE49761D878F508C2CB1`

This is a **mechanism and endpoint collision**, not an exact collision with the arbitrary one-spike formula, every-optimizer rigidity, or the sharp stability theorem. As with the one-spike package, a local submission sheet does not establish public availability; no exact-title public record was located.

### 3. Public low-dimensional antecedents by the same author

The following public records were located on ai.viXra:

- Lluis Eriksson, *Sharp Costs and Exact Semigroups from Forgotten Quantum Order*, submitted 2026-08-10 19:10:19: <https://ai.vixra.org/abs/2608.0034>
- Lluis Eriksson, *The Exact Four-Level Inverse Commutator Cost: Horn-Littlewood-Richardson Facets, Rank Transitions, and Sharp Loop Synthesis*, submitted 2026-08-10 21:34:32: <https://ai.vixra.org/abs/2608.0031>
- Lluis Eriksson, *The Exact Five-Level Inverse Commutator Cost: Twelve Horn Chambers, Optimal Rank, and the Sharp 5/2 Resource Tax*, submitted 2026-08-11 12:20:40: <https://ai.vixra.org/abs/2608.0049>

These records already contain the exact inverse-cost formulas and singular constructions/optimal-rank results in dimensions three, four, and five, and the exact triangular-loop identity \(A_3=12\sqrt3\,\kappa\) in those dimensions. Consequently:

- the one-spike formula is not new without the qualifier **arbitrary dimension**;
- low-dimensional examples are prior results, not fresh evidence of novelty; and
- the triangular bridge should be described as a dimension-free consolidation or consequence.

### 4. Public kick/polygon antecedents by the same author

- Lluis Eriksson, *Operational Curvature of the Heisenberg Cut: Exact Diamond Readout, a Discrete Stokes Law, and Sharp Action Bounds for Dissipative Zeno Holonomy*, submitted 2026-08-10 15:20:28: <https://ai.vixra.org/abs/2608.0037>. This record already uses balanced three- and four-kick synthesis mechanisms. It is a mechanism collision with the kick synthesis part.
- Lluis Eriksson, *Matrix Isoperimetry and Diffusion from Forgotten Order in Block--Zeno Dynamics*, submitted 2026-08-10 16:16:46: <https://ai.vixra.org/abs/2608.0035>. Its polygonal inequality and equality classification give the exact four-edge value on sign-paired spectra. In the notation of Paper 28, that public equality face yields \(A_4=16\kappa\) when the target is sign-paired. The same source identifies nonpaired examples as strict for that general trace-norm bound and does not provide the proposed all-target formula.

Thus the defensible advance is **from the sign-paired equality face to every feasible target**, not from no known four-kick result to the proposed identity.

### 5. ARR archive and public GitHub search

The local checkout `work/arr-research.github.io` was fetched and checked against `origin/main` at commit `74016f0688ee8176243fd21728bd6d39ead3c22e`. Its 20 metadata records contain no title or text match for one-spike inverse self-commutators, the proposed rigidity theorem, or the all-target four-kick identity. History searches also produced no matching record.

Public repositories and public release assets under the GitHub account `lluiseriksson` were searched for exact and distinctive phrases including:

- `One-Spike Inverse Self-Commutators`
- `Exact Cost, Singular Rigidity`
- `A_4(F)`
- `four-kick curvature synthesis`
- `kappa_d(F)`
- `sum_j j b_j`

No public code or release collision was returned. This is negative search evidence only: it cannot exclude private repositories, deleted/renamed records, manually uploaded files, or material not indexed by GitHub search.

## External primary-literature audit

### Exact external collisions

No external primary source was located that states the full audited package: the exact arbitrary-dimensional one-spike Hermitian cost, singular-spectrum rigidity for every optimum, the stated sharp stability theorem, and the all-target identity \(A_4=16\kappa_d\).

This negative result must be reported as **“no matching antecedent was located in the search”**, never as proof that no antecedent exists.

### Mechanism collisions

1. **Hermitian self-commutator existence and weighted shifts.** Fan and Fong characterize compact Hermitian self-commutators and construct them using a weighted shift after arranging eigenvalues with nonnegative partial sums. This is a direct mechanism antecedent for the shift construction, but it does not solve the audited finite-dimensional norm minimization, optimizer rigidity, or stability problems.

2. **Hermitian spectral feasibility.** Horn's inequalities and their representation-theoretic completion by Klyachko and Knutson--Tao provide the established feasibility machinery behind spectra of sums/differences of Hermitian matrices. The paper's specialized optimization and equality extraction may be new, but the Horn/Littlewood--Richardson framework is not.

3. **Unrestricted Hilbert--Schmidt commutators.** Weiss studies commutators of Hilbert--Schmidt operators with generally unrestricted, non-Hermitian factors. This is an important neighboring inverse problem, but its optimum is not the Hermitian-factor optimum audited here.

4. **Product commutators.** Chen et al. treat group commutators and higher-order product formulas for quantum simulation. This collides with the use of a commutator loop as a synthesis mechanism, not with the precise fixed-target Hilbert--Schmidt polygon variational identity.

5. **Gini dispersion.** The proposed stability deficit is a pairwise-difference/Gini functional. Sharp comparisons between empirical Gini mean difference and mean absolute deviation exist. The paper must distinguish its ordered, nonnegative, fixed-mass spectral constants and equality cases from the general statistical inequality.

### Adjacent results

- Böttcher--Wenzel bounds concern how large a forward matrix commutator can be at fixed Frobenius norms. They do not determine the inverse Hermitian fixed-target cost.
- Polygonal isoperimetric stability concerns geometric polygons and supplies context for stability, not the matrix-valued fixed-target identity.
- Non-Abelian phases from quantum Zeno dynamics provide a physical holonomy setting, not the audited optimum.
- Classical trace-zero matrix-commutator existence theorems establish representability, not the Hermitian balanced minimum.

## Primary-source bibliography

The manuscript should cite the relevant items below directly rather than relying on surveys or secondary descriptions.

1. Peng Fan and Che-Kao Fong, “Which operators are the self-commutators of compact operators?”, *Proceedings of the American Mathematical Society* **80**(1), 58–60 (1980). DOI: <https://doi.org/10.1090/S0002-9939-1980-0574508-X>. Publisher PDF: <https://www.ams.org/journals/proc/1980-080-01/S0002-9939-1980-0574508-X/S0002-9939-1980-0574508-X.pdf>.
2. Gary Weiss, “Commutators of Hilbert–Schmidt operators II”, *Integral Equations and Operator Theory* **3**(4), 574–600 (1980). DOI: <https://doi.org/10.1007/BF01702316>.
3. Gary Weiss, “Commutators of Hilbert–Schmidt operators I”, *Integral Equations and Operator Theory* **9**(6), 877–892 (1986). DOI: <https://doi.org/10.1007/BF01202521>.
4. Alfred Horn, “Eigenvalues of sums of Hermitian matrices”, *Pacific Journal of Mathematics* **12**, 225–241 (1962). DOI: <https://doi.org/10.2140/pjm.1962.12.225>.
5. Alexander A. Klyachko, “Stable bundles, representation theory and Hermitian operators”, *Selecta Mathematica* **4**, 419–445 (1998). DOI: <https://doi.org/10.1007/s000290050037>.
6. Allen Knutson and Terence Tao, “The honeycomb model of \(GL_n(\mathbb C)\) tensor products I: Proof of the saturation conjecture”, *Journal of the American Mathematical Society* **12**, 1055–1090 (1999). DOI: <https://doi.org/10.1090/S0894-0347-99-00299-4>. Preprint: <https://arxiv.org/abs/math/9807160>.
7. Albrecht Böttcher and David Wenzel, “How big can the commutator of two matrices be and how big is it typically?”, *Linear Algebra and its Applications* **403**, 216–228 (2005). DOI: <https://doi.org/10.1016/j.laa.2005.02.012>.
8. Albrecht Böttcher and David Wenzel, “The Frobenius norm and the commutator”, *Linear Algebra and its Applications* **429**, 1864–1885 (2008). DOI: <https://doi.org/10.1016/j.laa.2008.05.020>.
9. Yu-An Chen et al., “Efficient Product Formulas for Commutators and Applications to Quantum Simulation”, *Physical Review Research* **4**, 013191 (2022). DOI: <https://doi.org/10.1103/PhysRevResearch.4.013191>. Preprint: <https://arxiv.org/abs/2111.12177>.
10. Daniel Burgarth et al., “Non-Abelian Phases from Quantum Zeno Dynamics”, *Physical Review A* **88**, 042107 (2013). DOI: <https://doi.org/10.1103/PhysRevA.88.042107>.
11. Pietro Cerone and Sever S. Dragomir, “Bounds for the Gini mean difference of an empirical distribution”, *Applied Mathematics Letters* **19**(3), 283–293 (2006). DOI: <https://doi.org/10.1016/j.aml.2005.05.009>.
12. Emanuel Indrei and Levon Nurbekyan, “On the stability of the polygonal isoperimetric inequality”, *Advances in Mathematics* **276**, 62–86 (2015). DOI: <https://doi.org/10.1016/j.aim.2015.02.013>.
13. A. A. Albert and Benjamin Muckenhoupt, “On matrices of trace zero”, *Michigan Mathematical Journal* **4**, 1–3 (1957). DOI: <https://doi.org/10.1307/mmj/1028990168>.
14. R. C. Thompson, “On matrix commutators”, *Journal of the Washington Academy of Sciences* **48**, 306–307 (1958). No DOI located in this audit.

## Mandatory changes before release

1. **Add a self-prior-art subsection.** Cite the public \(d=3,4,5\) inverse-cost papers, the operational-curvature record, and the matrix-isoperimetry record. State exactly which slices or mechanisms they already contain.
2. **Disclose consolidation of the local theorem package.** Treat `work/one-spike-selfcommutator-rigidity` as provenance for the present paper and check whether its prepared viXra submission was ever made public.
3. **Qualify the four-kick claim.** Replace any unqualified “new exact four-kick identity” with “an all-target identity extending the previously established sign-paired equality case.”
4. **Qualify the inverse-cost claim.** Use “dimension-free one-spike formula” or “arbitrary-dimensional solution on the one-spike cone,” not a claim that the low-dimensional formulas or weighted-shift solution mechanism are new.
5. **Cite Gini/MAD results in the stability section.** Explain what is special about the spectral ordering, fixed mass, constants, and equality families here.
6. **Separate theorem depth.** Present the universal ratio as a corollary, and distinguish the elementary kick-to-commutator algebra from the harder inverse spectral optimization and rigidity theorem.
7. **Avoid exhaustive-priority language.** Use “we did not locate” or “to our knowledge after the searches described,” with a dated search statement. Do not use “first,” “unique,” “unprecedented,” or “no prior result” without a materially broader expert literature review.
8. **Keep public and local chronology separate.** Local timestamps and draft hashes establish internal development chronology, not public priority.

## Recommended conservative novelty statement

> Building on our earlier dimension-three, dimension-four, and dimension-five inverse-commutator formulas and their triangular-loop corollaries, and on our previously established sign-paired matrix-polygon equality face, we give a dimension-free solution on the full one-spike cone. The contributions isolated here are the closed one-spike formula in arbitrary dimension, rigidity of the singular spectrum of every optimum, sharp fixed-mass stability with explicit equality families, and an all-target four-kick variational identity extending the known sign-paired case. We do not claim novelty for weighted-shift self-commutator constructions, Horn feasibility, group-commutator loops, or general Gini/mean-deviation inequalities.

An even more conservative abstract sentence is:

> We extend the author's earlier low-dimensional formulas and sign-paired polygon equality cases to an arbitrary-dimensional one-spike theorem with every-optimizer rigidity and to an all-target four-kick variational identity.

## Residual uncertainty

This audit searched the local ARR checkout and its fetched history, the local work packages supplied in the workspace, public repositories and releases under `lluiseriksson`, public ai.viXra records located by title/author/category search, and targeted primary-literature queries. It did not establish the state of private repositories, unindexed manuscripts, subscription-only full-text databases beyond accessible metadata, conference proceedings not surfaced by the searches, or submission dashboards. Therefore the audit supports conservative wording and a release decision; it is not a legal priority opinion or an exhaustive novelty certification.
