# Final literature and novelty audit V5

**Manuscript audited:** `work/neuron_paper_v2/src/main.tex`  
**Initial audited snapshot SHA-256:** `CA16E3B1ADE04C046E629E2477F48499C5A1F10ABF5A33739316DC85DEBFC000`  
**Audit date:** 2026-08-29  
**Scope:** priority wording and bibliographic metadata for Chardon Theorem 6, the two Chen--Mazumdar preprints, logistic-beta/generalized-logistic transforms, Lam v2/v3, the spherical Schwarzian bridge, the all-power laws, and the pointwise bilateral empirical theorem. `main.tex` was not edited.

## Verdict

**Conditional pass after two substantive citation/priority corrections and one precision correction.** The spherical coefficient bridge, finite-scale bridge, all-`p` strict ratio monotonicity and endpoint package, and the explicit block-resolved all-`p` empirical theorem remain defensibly novel under a bounded-search formulation. I found no primary source containing any of those packages in the manuscript's exact form.

The manuscript should **not** pass a final priority audit unchanged, for two reasons:

1. bilateral relative empirical-Hessian concentration is not new in itself. Ostrovskii--Bach (2021) already obtain a uniform two-sided constant-factor empirical-Hessian sandwich and explicitly verify their framework for Gaussian logistic regression; Fisher et al. (2023) also formulate fixed-point standardized-Hessian spectral concentration under a matrix-Bernstein condition. The new claim must be narrowed to the manuscript's explicit `(1\pm\varepsilon)`, pointwise, Gaussian logistic-sensitivity, all-`p`, block-resolved, saturation-scaled and angle-resolving form;
2. Lee et al. (2025) review the logistic-beta density and its digamma/trigamma moments, but are not the best source for the exact Gamma characteristic function used in Lemma `lem:moments`. The characteristic function and polygamma cumulants are explicit in earlier generalized-logistic literature, notably Ojo--Olapade (2004). That source must be cited, and the Fourier/moment identity must remain explicitly classical.

The Chardon comparison at line 630 should also replace `n\asymp rd` by the exact sufficient condition `n\gtrsim r(d+t)` (or quote the constants), because Theorem 6 itself is a sufficient uniform one-sided theorem, not a bilateral equivalence theorem.

## Mandatory corrections

| Location in current source | Current substance | Problem | Required correction |
|---|---|---|---|
| Abstract, lines 81--83 | “our additions are bilateral all-`p` empirical resolution” | Read literally, this can suggest that bilateral empirical-Hessian control itself is new. It is not; see Ostrovskii--Bach eq. (92), and the fixed-point spectral-concentration discussion in Fisher et al. | Narrow to: “our additions include an explicit pointwise, block-resolved `(1\pm\varepsilon)` theorem for the Gaussian logistic sensitivity family for every `p>0`, with saturation scaling, an eigenspace-angle bound, and a slab obstruction.” Cite the two antecedents in the related-work section. |
| Empirical-section introduction, lines 642--645 | Chardon has a one-sided theorem “at the same effective scale `n\asymp rd`” | Theorem 6 states the sufficient condition `n >= 1,200,000 B(d+t)` and probability `1-2e^{-t}`. `\asymp` is stronger than that theorem's literal statement. | Replace by “under the sufficient condition `n\gtrsim r(d+t)`” (with `B=r>=e`), or state the exact constants. Retain the pointwise-versus-uniform distinction. |
| Priority table and prose, lines 925--928 and 965--969 | The only empirical antecedents listed are Chen and Chardon; “The new empirical statement is the pointwise bilateral relative approximation...” | Missing a direct same-domain bilateral precedent. Ostrovskii--Bach obtain a **uniform** two-sided constant-factor sandwich in a Dikin ellipsoid and treat Gaussian logistic regression. | Add Ostrovskii--Bach, and preferably Fisher et al., to the table/prose. Say the new object is the **explicit `(1\pm\varepsilon)` block decomposition for the fixed Gaussian weighted Gram matrix, all `p>0`, with `O_p(r[d+\log(1/\delta)]/\varepsilon^2)`, radial eigenvalue/angle bounds and slab obstruction**. Do not claim first bilateral Hessian concentration. |
| Logistic-beta row and prose, lines 929--931 and 976--977 | Lee et al. alone support “The Gamma transform ... is a classical logistic-beta identity” | Lee et al. review the density and first two moments but do not state the manuscript's exact characteristic function. The formula is older and explicit in generalized-logistic literature. | Add Ojo--Olapade (2004), optionally also Barndorff-Nielsen--Kent--Sørensen (1982). Attribute the Gamma characteristic function and cumulants to that distribution literature; claim only the neural-geometric use, ratio monotonicity and endpoint package. |
| Chardon bibliography, lines 1116--1119 | `arXiv:2411.02137 (2024)` with unversioned URL | Theorem 6 was checked in v3, revised 2026-02-19. An unversioned citation may later point to a changed theorem. | Cite `arXiv:2411.02137v3`, “first posted 2024; v3 2026,” and use the v3 URL. |

## Result-by-result audit

### 1. Chardon, Lerasle and Mourtada, Theorem 6

Primary source: [arXiv:2411.02137v3](https://arxiv.org/abs/2411.02137v3), [HTML, Theorem 6](https://arxiv.org/html/2411.02137v3).

Metadata verified:

- Hugo Chardon, Matthieu Lerasle, Jaouad Mourtada;
- *Finite-sample performance of the maximum likelihood estimator in logistic regression*;
- v1: 2024-11-04; v3: 2026-02-19.

Theorem 6 says: for `X~N(0,I_d)`, `d>=2`, `B=||theta*||>=e`, if

`n >= 1,200,000 B(d+t)`, 

then with probability at least `1-2e^{-t}`,

`Hhat_n(theta) >= (1/1000) H`

uniformly over the stated `H`-ellipsoid around `theta*`. The manuscript's descriptions “uniform” and “one-sided” are exact, and the distinction from a pointwise theorem is valid. The safe scale wording is `n\gtrsim r(d+t)`, not `n\asymp rd` when Theorem 6 alone is the cited support.

Chardon et al. call their Gaussian theorem an “optimal uniform lower bound.” This does not make it a two-sided relative approximation and does not supply the manuscript's explicit tangential/radial/cross block errors or eigenspace angle.

### 2. Chen and Mazumdar: population Hessian and minimax estimation

Primary sources:

- Junren Chen and Arya Mazumdar, [*Finite-Sample Performance of Gradient Descent in Logistic Regression with Gaussian Design*](https://arxiv.org/abs/2606.21683), arXiv:2606.21683v1, submitted 2026-06-19;
- Junren Chen and Arya Mazumdar, [*Minimax Optimal Estimator and Improved Error Rate for the MLE in Logistic Regression with Gaussian Design*](https://arxiv.org/abs/2608.17260), arXiv:2608.17260v1, submitted 2026-08-18.

The titles, authors, years and arXiv identifiers in the current bibliography are exact.

In arXiv:2606.21683, Lemma 15 defines

- `m(tau)=E[sigma'(tau g)]`, the tangential eigenvalue;
- `q'(tau)=E[sigma'(tau g)g^2]`, the radial eigenvalue;

and proves their orders `(1+tau)^{-1}` and `(1+tau)^{-3}`. Lemma 16 further proves `m(tau)>q'(tau)` for every `tau>0`. Therefore:

- the manuscript correctly disclaims novelty of the `p=1` two-eigenspace functions and saturation exponents;
- it should also avoid implying novelty of the mere `p=1` ordering `alpha_1>beta_1`;
- Chen does **not** prove strict monotonicity of the ratio `alpha_1/beta_1`, the exact leading constants, the endpoint series, or any all-`p` statement found here.

The 2026-08-18 follow-up proves the norm-estimation lower bound `Omega(sqrt(R^3/n))` and the overall minimax rate `Theta(sqrt(Rd/n)+sqrt(R^3/n))`. The manuscript's summary is accurate and does not confuse that statistical minimax theorem with weighted-Gram concentration.

### 3. Logistic-beta transform and the all-`p` laws

Primary sources:

- C.J. Lee, A. Zito, H. Sang and D.B. Dunson, [*Logistic-beta processes for dependent random probabilities with beta marginals*](https://arxiv.org/abs/2402.07048v3), Bayesian Analysis 20(4) (2025), 1345--1369, [DOI 10.1214/25-BA1541](https://doi.org/10.1214/25-BA1541);
- M.O. Ojo and A.K. Olapade, [*On a Six-Parameter Generalized Logistic Distribution*](https://imi.pmf.kg.ac.rs/kjm/pub/12616736649184_5.pdf), Kragujevac Journal of Mathematics 26 (2004), 31--38;
- O. Barndorff-Nielsen, J. Kent and M. Sørensen, [*Normal variance-mean mixtures and z distributions*](https://doi.org/10.2307/1402598), International Statistical Review 50(2) (1982), 145--159.

Lee et al. correctly support the claim that the logit-Beta/type-IV generalized-logistic/Fisher-z density is classical. Their §2.1 gives density proportional to `sigma(eta)^a sigma(-eta)^b` and gives digamma/trigamma first moments. Their article does **not** state the exact characteristic function used in the manuscript.

Ojo--Olapade, equations (2.3)--(2.5), explicitly give the moment generating function, characteristic function

`lambda^(it) beta^(-it) Gamma(p+it) Gamma(q-it)/(Gamma(p)Gamma(q))`,

and Gamma/polygamma cumulants. Setting `lambda=beta=1` and `q=p`, then undoing the density normalization, yields exactly the manuscript's Fourier transform

`Gamma(p+ik)Gamma(p-ik)/Gamma(2p)`.

Accordingly, the Fourier transform and `m_0,m_2,m_4` special-function formulas are not independently novel. The following package still has a defensible bounded novelty claim because no direct antecedent was located:

- application of those moments to Gaussian one-neuron radial/tangential anisotropy for every real `p>0`;
- strict global monotonicity of `kappa_p(r)` for every `p>0`;
- the exact small-`r` ratio expansion through `r^6` and refined large-`r` ratio expansion;
- the common theorem linking these results to the Schwarzian coefficient and empirical resolution.

Safe wording is: “The generalized-logistic Gamma transform and its polygamma cumulants are classical; we use them to derive the all-power neuronal anisotropy, its strict ratio monotonicity and endpoint laws.”

### 4. Lam v2 and v3

Primary sources:

- Hy P.G. Lam, [*The Real Bers Embedding on the Line: Fisher--Rao Linearization, Schwarzian Curvature, and Scattering Coordinates*](https://arxiv.org/abs/2602.07373v2), arXiv:2602.07373v2, revised 2026-02-26;
- Hy P.G. Lam, [*Zero-Energy Scattering and the Real Bers Image on the Line*](https://arxiv.org/abs/2602.07373v3), arXiv:2602.07373v3, 2026-08-26.

The current titles, version numbers and chronology are accurate. The arXiv v3 record says it corrects and supersedes v1--v2 and changes the title. v2 develops `L^p` Fisher--Rao geometry of density manifolds and relates Fisher information to Schwarzian/score curvature. v3 removes that Fisher--Rao architecture and focuses on the corrected real Bers/scattering result.

Neither version contains Gaussian one-neuron Hessian eigenvalues, radial/tangential anisotropy, a Löwner determinant, the coefficient `-q_X p Sg(0)`, or the manuscript's empirical theorem. The statement that Lam's `L^p` parameter is unrelated to the sensitivity exponent in `h_p=(g')^p` is correct. The manuscript's bounded wording—no claim to the first general Fisher--Schwarzian relation—is exactly the right boundary.

### 5. Spherical and finite-scale Schwarzian bridges

Claim audited:

`lim_{r->0}(kappa_{p,X}(r)-1)/r^2 = -q_X p Sg(0)`

and its equality, up to the stated constant, with

`lim_{delta->0} det L_g(0,delta)/delta^2`.

Searches across primary sources on matrix monotonicity/Löwner matrices, Schwarzian derivative, Fisher geometry, single-neuron Gaussian/spherical Fisher information, and rotational fourth moments did not locate this coefficient-level cross-identification. Kozlovski--Sands and Cook--Hammerlindl--Tucker cover the Schwarzian/order side; Amari--Karakida--Oizumi cover the one-unit Gaussian Fisher decomposition; Lam v2 is a different Fisher--Schwarzian adjacency. None contains this bridge.

The finite-scale inequality with derivative suprema and input moments was likewise not located. Because the identity follows from a short Taylor/fourth-moment calculation, an absolute “first ever” claim would still be inappropriate. The manuscript's existing sentence—“In the primary sources we located, we did not find ... This is a bounded novelty statement”—is priority-safe and should be retained.

### 6. Bilateral pointwise empirical theorem

Direct antecedents:

1. Dmitrii M. Ostrovskii and Francis Bach, [*Finite-sample analysis of M-estimators using self-concordance*](https://arxiv.org/abs/1810.06838v2), Electronic Journal of Statistics 15(1) (2021), 326--391, [DOI 10.1214/20-EJS1780](https://doi.org/10.1214/20-EJS1780). Their analysis explicitly treats logistic regression with Gaussian design. In the proof of Theorem 4.1, equation (92), they obtain with high probability, uniformly on a Dikin ellipsoid,

   `0.09 H(theta*) <= H_n(theta) <= 32 H(theta*)`.

   This is a two-sided relative constant-factor empirical-Hessian sandwich and is a direct same-domain priority antecedent.

2. Jillian Fisher, Lang Liu, Krishna Pillutla, Yejin Choi and Zaid Harchaoui, [*Influence Diagnostics under Self-concordance*](https://proceedings.mlr.press/v206/fisher23a.html), PMLR 206 (AISTATS 2023), 10028--10076. They formulate a matrix-Bernstein condition for the standardized Hessian and explicitly state fixed-point spectral concentration of the form `(1/2)H(theta) <= H_n(theta) <= 2H(theta)` for sufficiently large `n`. Their concrete logistic example assumes bounded covariates, so this is a conceptual/generic antecedent rather than a Gaussian-saturation theorem.

These sources invalidate only a broad “first bilateral concentration” reading. I found no source giving the exact theorem proved in the manuscript:

- a fixed Gaussian teacher and a general bounded profile, specialized to every `h_p=sigma'^p`, `p>0`;
- explicit separate errors `e_T,e_R,q_n` for tangential, radial and cross blocks;
- a tunable `(1\pm\varepsilon_n)` Löwner sandwich rather than a universal constant-factor sandwich;
- the saturation-aware sufficient scaling `n=O_p(r[d+log(1/delta)]/epsilon^2)`;
- an empirical radial eigendirection-angle bound;
- the matching-in-`r` empty-transition-slab obstruction `Omega_p(r log(1/delta))` together with the explicit disclaimer that an `Omega(rd)` product lower bound is open.

Thus the theorem remains publishably differentiated once the antecedents are cited and the novelty sentence is made compound and precise.

## Recommended replacement priority paragraph

The following wording is supported by the audited sources:

> Prior self-concordant M-estimation analyses give bilateral constant-factor empirical-Hessian sandwiches, including a uniform result for Gaussian logistic regression, while Chardon, Lerasle and Mourtada prove an optimal uniform one-sided lower bound for the Bernoulli Hessian under the sufficient condition `n\gtrsim r(d+t)`. We do not claim the first bilateral Hessian concentration or the first finite-sample lower bound. Our empirical contribution is an explicit pointwise `(1\pm\varepsilon)` theorem for the Gaussian sensitivity family `h_p=sigma'^p` for every `p>0`, with separate radial, tangential and cross errors, saturation scaling `n=O_p(r[d+log(1/delta)]/epsilon^2)`, a radial-eigenspace angle bound, and a transition-slab obstruction.

For the population result:

> Chen and Mazumdar identify the `p=1` radial and tangential Hessian functions, prove their `r^{-3}` and `r^{-1}` orders, and prove tangential curvature exceeds radial curvature for every nonzero signal. The generalized-logistic Gamma transform and its polygamma cumulants are classical. Our contribution is the all-`p` neural-geometric package: strict monotonicity of the anisotropy ratio for every real `p>0`, exact endpoint laws, and its spherical coefficient identity with the local Löwner/Schwarzian defect.

## Bibliographic metadata audit

### Correct as written

- Chen--Mazumdar, arXiv:2606.21683 (2026): title/authors/year/identifier correct.
- Chen--Mazumdar, arXiv:2608.17260 (2026): title/authors/year/identifier correct.
- Lam v2 and v3: titles, version labels and year correct. “H.P.G. Lam” matches the author form printed in the papers; arXiv displays “Hy Lam.”
- Amari--Karakida--Oizumi, PMLR 89 (2019), 694--702: correct.

### Precision fixes recommended or required

- **Chardon et al.:** use `arXiv:2411.02137v3 (first posted 2024; v3 2026)` and the versioned URL because the exact theorem was audited in v3.
- **Lee et al.:** add issue number: *Bayesian Analysis* **20(4)** (2025), 1345--1369. The DOI is correct.
- **Cook et al.:** optional precision improvement: *Chaos* **33(12)** (2023), 123105, DOI [10.1063/5.0162148](https://doi.org/10.1063/5.0162148). Current title, authors, volume, year and article number are correct.
- **Add Ojo--Olapade:** M.O. Ojo and A.K. Olapade, *On a Six-Parameter Generalized Logistic Distribution*, *Kragujevac Journal of Mathematics* **26** (2004), 31--38, [primary PDF](https://imi.pmf.kg.ac.rs/kjm/pub/12616736649184_5.pdf).
- **Add Ostrovskii--Bach:** D.M. Ostrovskii and F. Bach, *Finite-sample analysis of M-estimators using self-concordance*, *Electronic Journal of Statistics* **15(1)** (2021), 326--391, DOI [10.1214/20-EJS1780](https://doi.org/10.1214/20-EJS1780), [arXiv v2](https://arxiv.org/abs/1810.06838v2).
- **Preferably add Fisher et al.:** J. Fisher, L. Liu, K. Pillutla, Y. Choi and Z. Harchaoui, *Influence Diagnostics under Self-concordance*, PMLR **206** (2023), 10028--10076, [official PMLR page](https://proceedings.mlr.press/v206/fisher23a.html).
- **Optional historical logistic-beta source:** O. Barndorff-Nielsen, J. Kent and M. Sørensen, *Normal variance-mean mixtures and z distributions*, *International Statistical Review* **50(2)** (1982), 145--159, DOI [10.2307/1402598](https://doi.org/10.2307/1402598).

## Search boundary and final priority assessment

The audit used exact-title, formula and concept searches through arXiv and official proceedings/journal records, then inspected the primary PDFs/HTML for theorem statements and formulas. It targeted the combinations “Schwarzian + Fisher,” “Löwner determinant + sigmoid/logistic,” “Gaussian logistic weighted Hessian/Gram + relative concentration,” “logistic derivative power `p` + trigamma/polygamma,” and “spherical fourth moment + one-neuron anisotropy.” Negative search results are not proof of global absence, hence all novelty conclusions are bounded.

**Final assessment after mandatory corrections:**

- spherical coefficient bridge: **priority-safe, bounded novelty**;
- finite-scale bridge: **priority-safe, bounded novelty**;
- all-`p` Gamma transform/moments: **classical ingredients, must not be claimed new**;
- all-`p` strict anisotropy-ratio monotonicity and endpoint package: **no direct antecedent located; priority-safe when separated from the classical transform and Chen's `p=1` ordering**;
- pointwise bilateral empirical theorem: **new exact package appears defensible, but not the first bilateral empirical-Hessian concentration**;
- Chardon/Chen/Lam comparisons: **accurate after the scale/version precision fixes above**.

**Publication verdict:** **PASS WITH MANDATORY PRIOR-WORK REVISION.** The missing Ostrovskii--Bach antecedent and the source-inexact attribution of the Gamma characteristic function must be fixed before publication. No theorem needs to be removed; the contribution claims need narrowing and better sourcing.

## Differential close-out after author corrections

**Corrected source snapshot SHA-256:** `014C8448C64F622A6C5A20BF12635D1FA4C7793CEE8F4147E0005B3D29AB258D`  
**Differential review date:** 2026-08-29

The corrected `main.tex` resolves every mandatory literature/priority objection above:

- the abstract now describes the empirical contribution as an explicit pointwise, block-resolved `(1\pm\varepsilon)` theorem for all logistic powers, with saturation scaling, angle control and a slab obstruction, while acknowledging prior one-sided and bilateral constant-factor Hessian results;
- the empirical introduction and priority discussion now cite Ostrovskii--Bach equation (92) and Fisher et al., explicitly disclaim the first bilateral concentration, and distinguish the new theorem by tunable precision, all powers, block errors, angle and slab obstruction;
- the Chardon comparison now states the sufficient condition `n\gtrsim r(d+t)`, and the bibliography pins the cited result to arXiv:2411.02137v3 with its 2024/2026 chronology;
- the Chen comparison now acknowledges the previously proved `p=1` tangential-over-radial ordering in addition to the two population exponents;
- the Gamma transform is now attributed before the lemma to Ojo--Olapade equations (2.3)--(2.5), and the priority table/prose clearly separate the classical generalized-logistic transform and cumulants from the neural-geometric all-`p` contribution;
- Lee et al. now have the correct issue metadata, and the new Ostrovskii--Bach, Fisher et al. and Ojo--Olapade entries have correct titles, authors, venues, years, pages and direct primary-source links.

The remaining bounded novelty language for the spherical/finite-scale bridges, global all-`p` ratio monotonicity and endpoint laws is appropriately qualified. No direct antecedent found in this audit requires further narrowing.

**FINAL DIFFERENTIAL VERDICT: PASS. No literature, priority-wording, or bibliography blocker remains for publication.** This verdict is limited to the requested novelty/reference audit; it does not replace the separate proof, numerical-replay, source-build or publication-integrity audits.
