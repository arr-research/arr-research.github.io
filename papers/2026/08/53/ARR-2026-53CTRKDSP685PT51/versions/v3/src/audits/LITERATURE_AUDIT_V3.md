# Literature and priority audit V3

**Manuscript audited:** `work/neuron_paper/src/main.tex`, most recent version visible on 2026-08-29.

**Verdict:** **PASS WITH ONE MINOR PRIORITY-WORDING FIX RECOMMENDED.** The Cook (2023) and Amari--Karakida--Oizumi (2019) additions materially repair the earlier priority problem. The new local Schwarzian bridge is mathematically correct under its stated hypotheses, and I did not locate its explicit coefficient identity in the primary literature searched. The bibliography is now substantively accurate. The only remaining priority ambiguity is one sentence that lists the squared-output profile itself among the paper's contributions even though the manuscript correctly acknowledges earlier that Amari et al. already treated that branch.

## 1. The bridge identity: mathematical audit

The theorem defines, for `Z ~ N(0,1)`,

    alpha_p(r) = E[(g'(rZ))^p],
    beta_p(r)  = E[Z^2 (g'(rZ))^p],
    kappa_p(r) = alpha_p(r)/beta_p(r).

Put `h=(g')^p`. Bounded `h''''` gives a Gaussian-integrable fourth-order Taylor remainder, hence

    alpha_p(r) = h(0) + h''(0) r^2/2 + O(r^4),
    beta_p(r)  = h(0) + 3 h''(0) r^2/2 + O(r^4).

Therefore

    kappa_p(r) = 1 - [h''(0)/h(0)] r^2 + O(r^4).

At an inflection point, `g''(0)=0`. Since `log h = p log g'`,

    h''(0)/h(0) = p g'''(0)/g'(0) = p Sg(0).

Thus the stated coefficient

    lim_{r -> 0} [kappa_p(r)-1]/r^2 = -p Sg(0)

is exact. Combining it with

    det L_g(0,delta) = [g'(0)^2 Sg(0)/6] delta^2 + O(delta^3)

also gives the second equality in the theorem with the correct sign and factor `6p/g'(0)^2`.

The regularity assumptions are sufficient. `g in C^5`, `g'>0`, and the separate assumption that `(g')^p` is `C^4` with bounded fourth derivative justify all differentiations and the expectation remainder. The assertion `kappa_p(r)>1` for small positive `r` when `Sg(0)<0` follows immediately.

One proof-exposition refinement is advisable but not a mathematical defect: “every sufficiently close nontrivial Loewner pair” is stronger-sounding than the displayed adjacent pair `(0,delta)`. It is true because continuity makes `Sg<0` on a neighborhood and strict convexity of `(g')^{-1/2}` then gives the all-pair determinant sign there, but the proof should say this explicitly or narrow the phrase to `L_g(0,delta)`.

## 2. Explicit search for a prior occurrence of the bridge

I searched exact and conceptual combinations of the following:

- `E[h(rZ)] / E[Z^2 h(rZ)]`, `E[(g'(rZ))^p]`, and their small-`r` expansions;
- Schwarzian plus Fisher information, Hessian geometry, radial/tangential eigenvalues, anisotropy, Gaussian design, sigmoid activation, and condition number;
- the exact expressions `-p Sg(0)` and `h''(0)/h(0)` with Schwarzian terminology.

No primary source located states the displayed ratio coefficient or connects it to the adjacent two-point Loewner determinant. The nearest primary sources split cleanly into two non-overlapping sides:

1. **Cook, Hammerlindl and Tucker (2023)** define
   `chi_f(x,y)=f'(x)f'(y)((x-y)/(f(x)-f(y)))^2`, prove closure under composition, connect nonpositive Schwarzian to their two-point inequality, and explicitly discuss sigmoids and one-dimensional neural compositions. They do **not** introduce Gaussian radial/tangential sensitivity moments or the small-radius ratio coefficient. Primary source: [arXiv:2303.12814](https://arxiv.org/abs/2303.12814); journal DOI [10.1063/5.0162148](https://doi.org/10.1063/5.0162148).

2. **Amari, Karakida and Oizumi (2019)** derive the one-unit Gaussian Fisher matrix for the squared-derivative profile, including the tangential eigenvalue and the radial/bias block. They do **not** expand the radial/tangential ratio at zero and do not invoke the Schwarzian or Loewner matrices. Primary source: [PMLR 89, 694--702](https://proceedings.mlr.press/v89/amari19a.html).

3. **Kozlovski and Sands (2009)** give the classical fixed-order matrix-monotonicity/Schwarzian connection used on the order side. Their subject is interval dynamics and matrix monotonicity, not Gaussian Fisher/Hessian anisotropy. Primary source: [arXiv:0812.2646](https://arxiv.org/abs/0812.2646); journal DOI [10.4064/fm206-1-12](https://doi.org/10.4064/fm206-1-12).

4. **Chen and Mazumdar (2026)** analyze the Bernoulli logistic Gaussian-design radial and orthogonal Hessian functions and their large-signal statistical consequences, but do not state the small-signal Schwarzian coefficient identity. Primary sources: [arXiv:2606.21683](https://arxiv.org/abs/2606.21683) and [arXiv:2608.17260](https://arxiv.org/abs/2608.17260).

5. A potentially confusing 2026 Schwarzian search hit, **Lam, arXiv:2602.07373**, is now titled “Zero-energy scattering and the real Bers image on the line” and explicitly says version 3 corrects and supersedes versions 1--2. It studies the Bers/Schwarzian map and zero-energy scattering, not neural Gaussian moment ratios. It is not a priority conflict. Primary source: [arXiv:2602.07373v3](https://arxiv.org/abs/2602.07373).

The responsible conclusion is therefore: **no explicit antecedent was located, not an absolute claim of first discovery**. The manuscript already uses essentially this bounded formulation. Because the bridge is a short Gaussian Taylor identity once the two quantities are placed together, it should be presented as a new connection/lemma of moderate conceptual value, not as a standalone deep theorem breakthrough.

## 3. Cook and serial-chain priority

The current manuscript now handles this correctly:

- It writes the exact algebraic relation `det L_f = D_f^2 (chi_f-1)`.
- It expressly says the qualitative negative-Schwarzian obstruction is classical.
- It limits its claimed addition to the strict closed logistic determinant formula and a certified explicit `2 x 2` PSD witness.
- It calls the serial scalar-chain corollary a Loewner-order restatement of Cook's closure result.
- It excludes sums, skip connections, multivariate architectures, and coordinatewise order.

These are important and valid corrections. I found no primary source containing the manuscript's particular closed logistic determinant expression or its stated interval-certified numerical witness. The novelty claim is appropriately bounded.

## 4. Amari and Gaussian Fisher priority

The current text accurately concedes that Amari--Karakida--Oizumi already derived the one-unit Gaussian `phi'^2` decomposition, including the radial/tangential split and bias coupling. It also correctly concedes the Bernoulli exponents and associated estimation difficulty to the 2026 Gaussian-logistic literature.

The manuscript can validly claim the following narrower additions:

- a profile-generic moment theorem with finite-radius brackets;
- the closed logistic moment constants;
- strict global monotonicity of the two logistic ratios, if the proofs are otherwise sound;
- the Schwarzian bridge coefficient;
- the explicit connection between the small-signal Gaussian ratio and the local Loewner defect.

**Remaining wording issue:** in the relation-to-prior-work section, the sentence ending with “and the squared-output profile `h=sigma'^2`” reads as if the squared-output branch itself were new. That conflicts with the correct acknowledgement just above and with Amari et al. Replace that item by something narrower, for example “the closed squared-output constants and strict ratio monotonicity.” This is a positioning edit, not a theorem defect.

## 5. Bibliographic metadata and links

All 18 entries were rechecked against author, publisher, proceedings, journal, or current arXiv records. Titles, author lists, years, volumes, and page ranges in the current source are substantively correct.

Notable corrections now confirmed:

- **Hiai--Sano:** Journal of the Mathematical Society of Japan **64(2)** (2012), 343--364; [arXiv:1007.2478](https://arxiv.org/abs/1007.2478).
- **Heinavaara:** retaining “preprint (2019)” is accurate; the arXiv record still presents the 2019 preprint and no later journal metadata; [arXiv:1906.06155](https://arxiv.org/abs/1906.06155).
- **Kozlovski--Sands:** Fundamenta Mathematicae **206** (2009), 217--239. For maximum precision one may add issue 1 and DOI `10.4064/fm206-1-12`.
- **Cook--Hammerlindl--Tucker:** Chaos **33** (2023), article 123105 is correct. For maximum precision add issue 12 and DOI `10.1063/5.0162148`.
- **Maronese--Destri--Prati:** author spelling, 2022 journal year, volume 21, and article 128 are correct.
- **Liu--Cao--Li--Zikatanov:** the former preprint is now correctly cited as Journal of Machine Learning for Modeling and Computing **6(2)** (2025), 1--11; DOI [10.1615/JMachLearnModelComput.2024056966](https://doi.org/10.1615/JMachLearnModelComput.2024056966).
- **Vardi--Yehudai--Shamir:** NeurIPS 34 (2021), 28690--28700 is correct.
- **Braun--Quang--Imaizumi:** PMLR 258 (2025), 1216--1224 is correct.
- **Hsu--Mazumdar:** PMLR 247 (2024), 2418--2437 is correct; [official PMLR page](https://proceedings.mlr.press/v247/hsu24a.html).
- **Chen--Mazumdar:** both 2026 titles, author list, identifiers, and years match the current arXiv records as of 2026-08-29.
- **Chardon--Lerasle--Mourtada:** the corrected first initial `H.` is right (Hugo Chardon); the 2024 identifier and title remain current, with version 3 dated 2026-02-19.
- **Amari--Karakida--Oizumi:** PMLR 89 (2019), 694--702 and the title/author order are exact; [official PMLR page](https://proceedings.mlr.press/v89/amari19a.html).
- **Karakida--Akaho--Amari:** PMLR 89 (2019), 1032--1041 is correct.

The remaining references to Yehudai--Shamir, Diakonikolas et al., Wu, and Amari (1998) also match their linked primary records. Adding DOIs to journal entries would improve polish but is not needed for correctness because stable primary links are already supplied.

## 6. Final publication recommendation

From the literature and priority perspective, there is **no genuine blocker**. The current version no longer overclaims Cook's Schwarzian/composition mechanism or Amari's one-unit Fisher reduction. The new bridge equation is correct and was not found in the searched primary literature.

Before final publication, make the one small wording correction in the relation-to-prior-work paragraph so that the contribution is the **new constants/brackets/monotonicity for the squared-output profile**, not the already-known existence of that profile/decomposition. Optionally add Cook's issue/DOI and one sentence justifying the theorem's “every nearby pair” wording. With those refinements, the paper passes this hostile literature audit.
