# Novelty and priority audit V3: local order--anisotropy bridge

**Version audited.** `work/neuron_paper/src/main.tex`, SHA-256
`9C2686699E751A35DF257A04D8A90C089CDCE4B6CE414E2ABA44680E68233E0B`
(36,246 bytes; observed 2026-08-29 10:23:02 Europe/Stockholm).

**Verdict: PASS, with one mandatory positioning correction before publication.**

The bridge theorem is correct, and I found no source in the public
`lluiseriksson` corpus or in the directed primary-literature search that states
the manuscript's coefficient identity

\[
 \lim_{r\downarrow0}\frac{\kappa_p(r)-1}{r^2}
 =-pSg(0)
 =-\frac{6p}{g'(0)^2}
   \lim_{\delta\to0}\frac{\det L_g(0,\delta)}{\delta^2}.
\]

This is a genuinely distinct *cross-identification*: it equates the first
Gaussian radial--tangential anisotropy coefficient of a single-neuron
sensitivity matrix with the infinitesimal two-point Loewner defect. It is not,
however, a new Schwarzian/Loewner criterion, a new Gaussian Fisher
decomposition, or a generally new connection between Schwarzian geometry and
Fisher geometry. The theorem is an elegant, short Taylor argument; its novelty
is conceptual unification and the exact coefficient, not technical depth.

## 1. Independent correctness check

Write `h=h_p=(g')^p`. Bounded `h''''` and the Gaussian moments give

\[
 \alpha_p(r)=h(0)+\frac12h''(0)r^2+O(r^4),\qquad
 \beta_p(r)=h(0)+\frac32h''(0)r^2+O(r^4).
\]

Since `h(0)>0`, division gives

\[
 \kappa_p(r)=1-\frac{h''(0)}{h(0)}r^2+O(r^4).
\]

Moreover,

\[
 (\log h)''=p(\log g')'',\qquad
 \frac{h''(0)}{h(0)}=p\frac{g'''(0)}{g'(0)}=pSg(0),
\]

where the last equality uses `g''(0)=0`. Thus the first equality in the
theorem is exact.

For the adjacent pair `(0,delta)`, direct Taylor expansion gives

\[
 g'(0)g'(\delta)
 -\left(\frac{g(\delta)-g(0)}{\delta}\right)^2
 =\frac{g'(0)g'''(0)}6\delta^2+O(\delta^3)
 =\frac{g'(0)^2Sg(0)}6\delta^2+O(\delta^3).
\]

This proves the second equality and the stated sign consequences. The logistic
specializations `S sigma=-1/2`, coefficient `1/2` for `p=1`, and coefficient
`1` for `p=2` are also correct.

The regularity assumptions are sufficient. The `O(r^4)` remainder in `beta`
uses the finite sixth Gaussian moment after multiplying the Taylor remainder
by `Z^2`; bounded `h''''` supplies the domination.

## 2. What is old, and what remains new

| Component | Priority assessment | Evidence |
|---|---|---|
| `Sf>=0` iff order-two matrix monotonicity for increasing smooth `f` | Classical, not new | Kozlovski--Sands, Lemma 10, with `d=1`, states the fixed-order equivalence: [arXiv:0812.2646](https://arxiv.org/abs/0812.2646). |
| Negative Schwarzian, two-point coexpansion inequality, and serial closure | Classical, not new | Cook--Hammerlindl--Tucker define `chi_f`, prove the `C^3` equivalence with `Sf<=0`, and prove closure under composition: [arXiv:2303.12814](https://arxiv.org/abs/2303.12814). Their Lemma 11 and proof give `Sf(x)=6 lim U_f(x,y)` and `(x-y)^2U_f=chi_f-1`. |
| Adjacent Loewner determinant coefficient `g'(0)^2 Sg(0)/6` | Classical/algebraically immediate from the preceding facts; not a standalone novelty claim | The manuscript's exact identity `det L=D_f^2(chi_f-1)` combined with Cook's local formula yields this coefficient directly. The notation is different, but the content is already implicit. |
| Gaussian one-unit `h=phi'^2` Fisher matrix, radial--tangential split, and bias coupling | Prior art | Amari--Karakida--Oizumi give `G=E[phi'(u)^2 x*x*]` and the `A00`, `A0n`, `Ann` block decomposition in equations (49), (57)--(64): [PMLR 89](https://proceedings.mlr.press/v89/amari19a.html). |
| Bernoulli logistic radial/orthogonal Hessian eigenvalues and their large-signal orders | Prior art | Chen--Mazumdar explicitly use the population Hessian eigenvalues in the parameter direction and orthogonal space and prove the finite-sample consequences: [arXiv:2606.21683](https://arxiv.org/abs/2606.21683). Their follow-up proves the norm lower bound/rate `sqrt(R^3/n)`: [arXiv:2608.17260](https://arxiv.org/abs/2608.17260). |
| A Schwarzian--Fisher relation in broad information geometry | Existing adjacent work, newly important to cite | Lam develops the Schwarzian as score curvature on a manifold of densities and relates its mean to Fisher information: [arXiv:2602.07373](https://arxiv.org/abs/2602.07373). This paper does **not** study Loewner matrices, Gaussian single-neuron radial/tangential eigenvalues, or the bridge coefficient here. |
| `-pSg(0)` as the small-`r` coefficient of `E[(g'(rZ))^p]/E[Z^2(g'(rZ))^p]`, explicitly equated to the Loewner determinant coefficient | No direct precedent found; this is the defensible novelty | Directed searches across Schwarzian/Fisher, Schwarzian/Gaussian activation, radial--tangential Fisher, and exact expectation-ratio phrases found no primary source stating this identity. |

The novelty therefore survives only in the last row. That is enough for a
focused theorem/note when paired with the exact logistic global results and
reproducibility package, but it should not be advertised as discovering either
side of the bridge independently.

## 3. Delimitation of the named prior work

### Cook--Hammerlindl--Tucker: PASS

The current manuscript now accurately says that `chi_f<=1`, its Schwarzian
mechanism, and serial closure are theirs/classical. It also identifies the
algebraic relation `det L=D_f^2(chi_f-1)`. The residual claim---a strict closed
logistic determinant formula plus a certified matrix witness---is properly
separated. Do not strengthen this to say that the local Loewner coefficient is
new; Cook's local `U_f` identity already contains it after the displayed
algebraic conversion.

### Kozlovski--Sands: PASS

The manuscript correctly calls the order-two Schwarzian criterion classical
and cites Lemma 10. The serial chain rule is likewise not claimed as new.

### Amari--Karakida--Oizumi: PASS

Lines 291--293 and 592--596 correctly acknowledge the exact one-unit Gaussian
`phi'^2` decomposition, the radial--tangential split, and bias coupling. The
revised sentence at lines 588--590 now claims only profile-generic moment
brackets, closed leading constants, finite-radius bounds, and strict ratio
monotonicity for the squared-output profile. It no longer lists the profile or
its spectral reduction as new.

### Chen--Mazumdar: PASS

The manuscript now explicitly credits their Bernoulli radial/orthogonal
functions, the `r^-3` and `r^-1` eigenvalue orders, the corresponding
optimization penalty, and the minimax norm rate. Its residual Bernoulli claims
are exact leading constants, finite-radius brackets, strict monotonicity, and
the local Schwarzian/Loewner coefficient bridge. That boundary is defensible.

## 4. Newly located adjacent priority risk

Lam's 2026 preprint is close enough in vocabulary and organizing idea that a
referee searching “Schwarzian Fisher information” is likely to find it. It
states that the Schwarzian becomes a score curvature governing Fisher
information on density manifolds. It does not imply or state the manuscript's
single-neuron Gaussian anisotropy ratio or its equality with a Loewner defect,
so it does not defeat novelty.

**Mandatory correction:** cite Lam and add one boundary sentence: broad
Schwarzian--Fisher geometry is known; the present contribution is the local
coefficient identity for the Gaussian one-neuron radial/tangential matrix and
its equality with the two-point Loewner determinant defect. Correspondingly,
avoid any phrase implying this is the first Schwarzian--Fisher bridge in all
contexts.

## 5. Claims to retain, lower, or clarify

### Retain

- “Schwarzian bridge equating the local order defect with the leading radial--
  tangential anisotropy ... at a centered inflection.” This is precise.
- The bounded novelty statement at lines 573--575. It is appropriately limited
  to the exact coefficient identity and acknowledges search incompleteness.
- The exact logistic coefficients `1/2` and `1`, and their matching with the
  global small-radius expansions.

### Lower or clarify before publication

1. Add Lam and narrow “Schwarzian--Fisher bridge” priority to this Gaussian
   neuron/Loewner coefficient identity.
2. Prefer “determines the leading quadratic onset coefficient” to “determines
   the onset” for a general activation. When `Sg(0)=0`, the theorem only says
   the quadratic coefficient vanishes and does not determine the first
   nonzero higher-order term.
3. Describe the theorem as a new exact cross-identification, not a new
   Schwarzian criterion, a new Loewner expansion, or a new Fisher spectral
   decomposition.

## 6. Full-corpus check

The earlier sweep covered all 33 public repositories owned by
`lluiseriksson`, frozen at the commits recorded in
`work/neuron_paper/repo_synthesis.md`. A renewed targeted search for
`Schwarzian`, `kappa_p`, joint Schwarzian/anisotropy terms, and joint
Schwarzian/Fisher terms found no occurrence of this theorem or its coefficient
identity. Hits for “Loewner” in `finite-sample-spectral-certificates`,
`hausdorff-certificates`, and `physmath-lean-lemmas` concern PSD order or
confidence bands, not scalar activation Loewner matrices. Thus the bridge is
also new relative to the author's public corpus.

## 7. Publication decision

**PASS on mathematical correctness and bounded novelty.** The manuscript has
a defensible new result: the exact equality of two local coefficients from
matrix order and Gaussian neuron anisotropy. **Revise before upload** to make
the mandatory Lam positioning correction above. After that correction, the
priority boundary would be unusually clear: classical order theory on one
side, known Gaussian Fisher/Hessian decompositions on the other, and a new
coefficient-level bridge between them.

This audit is a bounded primary-source and corpus search, not an absolute
priority guarantee.
