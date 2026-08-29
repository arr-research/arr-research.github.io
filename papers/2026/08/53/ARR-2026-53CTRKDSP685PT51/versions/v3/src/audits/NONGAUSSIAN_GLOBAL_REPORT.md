# Non-Gaussian global saturation laws

**Date:** 2026-08-29  
**Scope:** population sensitivity/Hessian asymptotics beyond Gaussian inputs; exact constants for spherical and elliptical laws; sharp limitations of isotropy; primary-literature priority audit through the date above.  
**Source-edit policy:** no manuscript source was edited.

## Executive result

There is no mathematical blocker. A proof-complete global extension exists and has a clean sharp condition.

Let

\[
H_h(r,u)=\mathbb E[h(r u^\top X)XX^\top],\qquad h\ge 0,
\]

and suppose that `X` is isotropic and spherically symmetric in `R^d`, `d>=2`. Write

\[
X=RU,\qquad R=\|X\|>0,\qquad U\sim\operatorname{Unif}(S^{d-1}),\qquad R\perp U,
\]

so isotropy is `E R^2=d`. If `E R^{-1}<infinity` and the sensitivity is localized (the condition below includes every logistic power `h_p=sigma'^p`, `p>0`), then

\[
H_h(r,u)=\alpha_h(r)(I-uu^\top)+\beta_h(r)uu^\top
\]

and, as `r->infinity`,

\[
\boxed{
\alpha_h(r)\sim
\frac{c_d\,\mathbb E R}{d-1}\frac{m_0(h)}r,
\qquad
\beta_h(r)\sim
c_d\,\mathbb E R^{-1}\frac{m_2(h)}{r^3}}
\]

with

\[
c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},\qquad
m_j(h)=\int_{\mathbb R}t^j h(t)\,dt.
\]

Consequently,

\[
\boxed{
\kappa_h(r)=\frac{\alpha_h(r)}{\beta_h(r)}
\sim Q_R\frac{m_0(h)}{m_2(h)}r^2,
\qquad
Q_R:=\frac{\mathbb E R}{(d-1)\mathbb E R^{-1}}.}
\]

The exponent two is universal over this spherical class, but its leading constant is not. The Gaussian identity `Q_R=1` is a special chi-radius cancellation. Isotropy alone is insufficient, and `E R^{-1}<infinity` is the exact radial threshold for the standard `r^{-3}` radial law in a broad regularly varying class.

For `h_p=sigma'^p`, the existing generalized-logistic moment calculation gives

\[
\frac{m_0(p)}{m_2(p)}=\frac1{2\psi_1(p)},
\]

hence

\[
\boxed{\kappa_p(r)\sim \frac{Q_R}{2\psi_1(p)}r^2.}
\]

This is the strongest proof-complete non-Gaussian next-paper theorem located in this audit.

## 1. The general transition-density theorem

The spherical result is a special case of a more local and more general principle.

### Theorem A (hyperplane transition-density law)

Fix `u in S^{d-1}` and suppose the law of `X` is invariant under every orthogonal transformation fixing `u`. Put `Z=u^T X`, and let `v` be any unit vector perpendicular to `u`. Assume:

1. `E||X||^2<infinity`;
2. `h>=0` and `h(t)<=C exp(-a|t|)` for some `a,C>0`;
3. near zero, `Z` has a density `f` continuous at zero;
4. near zero, the transverse-energy measure

   \[
   \mu_\perp(A):=\mathbb E[(v^\top X)^2\mathbf 1_{\{Z\in A\}}]
   \]

   has a density `a_perp` continuous at zero;
5. `f(0)>0` and `a_perp(0)>0`.

Then

\[
\alpha_h(r)\sim \frac{a_\perp(0)m_0(h)}r,
\qquad
\beta_h(r)\sim \frac{f(0)m_2(h)}{r^3},
\]

and

\[
\kappa_h(r)\sim
\frac{a_\perp(0)}{f(0)}\frac{m_0(h)}{m_2(h)}r^2.
\]

If the conditional transverse moment has a continuous version

\[
\tau(z)=\mathbb E[(v^\top X)^2\mid Z=z],
\]

then `a_perp(0)=tau(0)f(0)`, so the density of the score at the decision boundary cancels from the ratio:

\[
\kappa_h(r)\sim \tau(0)\frac{m_0(h)}{m_2(h)}r^2.
\]

This gives the requested exact condition in terms of the longitudinal marginal and transverse moments: the radial constant uses the ordinary hyperplane density `f(0)`, while the tangential constant uses its transverse-energy-weighted analogue `a_perp(0)`.

#### Proof

Axial invariance forces the two-eigenspace decomposition and gives

\[
\alpha_h(r)=\int h(rz)a_\perp(z)\,dz,
\qquad
\beta_h(r)=\int z^2h(rz)f(z)\,dz.
\]

After `t=rz`,

\[
r\alpha_h(r)=\int h(t)a_\perp(t/r)\,dt,
\qquad
r^3\beta_h(r)=\int t^2h(t)f(t/r)\,dt.
\]

On a fixed neighborhood of zero, continuity and local boundedness permit dominated convergence. Outside that neighborhood, exponential localization of `h` and the finite second moment make the two contributions, even after multiplication by `r` or `r^3`, exponentially small. This proves both limits. The ratio follows because both limiting constants are positive.

### Quantitative refinement

If, near zero,

\[
|a_\perp(z)-a_\perp(0)|\le L_a|z|^\gamma,
\qquad
|f(z)-f(0)|\le L_f|z|^\gamma,
\]

for `0<gamma<=1`, then the same proof gives

\[
\alpha_h(r)=\frac{a_\perp(0)m_0}{r}+O(r^{-1-\gamma}),
\qquad
\beta_h(r)=\frac{f(0)m_2}{r^3}+O(r^{-3-\gamma}),
\]

where the constants use `int |t|^gamma h(t)dt` and `int |t|^{2+gamma}h(t)dt`. Thus a finite-radius non-Gaussian theorem is available under Hölder regularity at the transition hyperplane.

## 2. Exact spherical theorem and proof

The transition-density theorem is conceptually transparent, but the radial representation gives a stronger result that does not require `X` to have a full-dimensional density.

### Theorem B (global spherical saturation with radial constants)

Let `d>=2`, let `X=RU` be isotropic and spherically symmetric with `R>0` almost surely, and assume

\[
\mathbb E R^2=d,\qquad \mathbb E R^{-1}<\infty.
\]

Let `h:R->[0,infinity)` have `0<m_0,m_2<infinity`. Define

\[
M_{d,h}:=\sup_{q>0}\int_{-q}^{q}
t^2h(t)\left(1-\frac{t^2}{q^2}\right)^{(d-3)/2}dt.
\]

Assume `M_{d,h}<infinity`. This condition is automatic for `d>=3`, since then `M_{d,h}<=m_2`; for `d=2` it holds whenever `h(t)<=C exp(-a|t|)`, hence for every logistic power. Then the boxed asymptotics in the executive result hold.

#### Exact one-dimensional identities

Let `T=u^T U`. Its density is

\[
p_T(t)=c_d(1-t^2)^{(d-3)/2}\mathbf 1_{(-1,1)}(t).
\]

Conditional on `T=t`, every unit transverse coordinate has second moment `(1-t^2)/(d-1)`. Therefore, exactly for every `r>0`,

\[
r\alpha_h(r)=\frac{c_d}{d-1}\mathbb E\left[
R\int_{|s|<rR}h(s)
\left(1-\frac{s^2}{r^2R^2}\right)^{(d-1)/2}ds\right],
\tag{S1}
\]

and

\[
r^3\beta_h(r)=c_d\mathbb E\left[
R^{-1}\int_{|s|<rR}s^2h(s)
\left(1-\frac{s^2}{r^2R^2}\right)^{(d-3)/2}ds\right].
\tag{S2}
\]

For every fixed `R>0`, the inner integrals converge to `m_0` and `m_2`. The integrand in (S1) is bounded by `R m_0`, which is integrable because isotropy implies `E R<infinity`. The integrand in (S2) is bounded by `R^{-1}M_{d,h}`, integrable by assumption. Dominated convergence proves the theorem.

For `d=2`, the only apparent difficulty is the arcsine boundary factor. If `h(t)<=C exp(-a|t|)`, split the defining integral at `|t|=q/2`. The interior is bounded by a constant multiple of `m_2`; the boundary is at most a constant times `q^3 exp(-aq/2)`. Hence `M_{2,h}<infinity`.

### Hyperplane constants for a spherical law

The same calculation identifies the quantities in Theorem A:

\[
f_Z(0)=c_d\mathbb E R^{-1},
\qquad
a_\perp(0)=\frac{c_d}{d-1}\mathbb E R,
\qquad
\tau(0)=Q_R.
\]

Thus `Q_R` is exactly the conditional transverse variance on the decision hyperplane.

## 3. Constants for canonical non-Gaussian inputs

For any isotropic spherical law with `R>0` a.s.,

\[
0<Q_R\le \frac d{d-1}.
\]

Indeed, `E R^{-1}>=1/E R` and `(E R)^2<=E R^2=d`. Equality holds precisely for fixed radius.

| Isotropic spherical input | Radius facts | `Q_R` | Logistic-power anisotropy |
|---|---|---:|---:|
| Gaussian `N(0,I_d)` | `R~chi_d` | `1` | `kappa_p(r)~r^2/[2 psi_1(p)]` |
| Uniform on `sqrt(d) S^{d-1}` | `R=sqrt(d)` | `d/(d-1)` | `kappa_p(r)~[d/(d-1)]r^2/[2 psi_1(p)]` |
| Isotropic multivariate Student `t_nu`, `nu>2` | `R=sqrt(nu-2) chi_d/chi_nu` | `(nu-2)/(nu-1)` | `kappa_p(r)~[(nu-2)/(nu-1)]r^2/[2 psi_1(p)]` |

The Student constant follows from the chi-moment identities

\[
\frac{\mathbb E\chi_d}{\mathbb E\chi_d^{-1}}=d-1,
\qquad
\frac{\mathbb E\chi_\nu^{-1}}{\mathbb E\chi_\nu}=\frac1{\nu-1}.
\]

For the two canonical observation powers:

\[
\kappa_1(r)\sim Q_R\frac{3}{\pi^2}r^2,
\qquad
\kappa_2(r)\sim Q_R\frac{3}{\pi^2-6}r^2.
\]

These examples make the result falsifiable and reproducible: Gaussian, fixed-sphere and Student inputs have the same exponent and three distinct leading constants.

## 4. Elliptical corollary

Let `X=A S`, where `S` is isotropic spherical and `A` is invertible. For a parameter `w`, set

\[
\rho=\|A^\top w\|,\qquad u=\frac{A^\top w}{\rho}.
\]

Then exactly

\[
H_{h,X}(w)=A\,H_{h,S}(\rho,u)\,A^\top.
\]

Therefore Theorem B transfers without loss in whitened coordinates, with saturation parameter `rho`. In Euclidean coordinates the eigenvectors need not be literally parallel and perpendicular to `w`; the radial/tangential statement is a generalized-eigenvalue statement relative to `AA^T`, or an ordinary eigenspace statement after whitening. This prevents an incorrect claim that arbitrary elliptical inputs retain the same Euclidean two-eigenvalue matrix.

## 5. Sharp failure modes

### 5.1 Isotropy alone is insufficient

Let `X` have independent Rademacher coordinates, so `X_j` is `+1` or `-1` with equal probability. This law is isotropic but not spherical. For `u=e_1` and any even profile `h`,

\[
H_h(r,e_1)=h(r)I_d.
\]

For logistic powers, both eigenvalues decay exponentially and `kappa=1`; none of the `r^{-1}`, `r^{-3}`, `r^2` laws holds. The obstruction is geometric: there is no score mass in an `O(1/r)` transition slab around `u^T X=0`.

Thus “isotropic inputs” must never replace “spherically symmetric isotropic inputs” in the global theorem without explicit hyperplane-density hypotheses such as Theorem A.

### 5.2 The inverse-radius condition is essentially sharp

Consider a spherical law whose radius has a density

\[
f_R(\rho)\sim c\rho^{a-1}\qquad(\rho\downarrow0),
\]

with its tail adjusted so `E R^2=d`. If `0<a<1`, then `E R^{-1}=infinity`. For an exponentially localized profile,

\[
\alpha_h(r)\sim \frac{c_d E R}{d-1}\frac{m_0}{r},
\]

but

\[
\beta_h(r)\sim D_{a,d,h}\,r^{-(a+2)},
\]

where the explicit positive constant is

\[
D_{a,d,h}=c_dc\int_0^\infty q^{a+1}
\left[\int_{-1}^1t^2h(qt)(1-t^2)^{(d-3)/2}dt\right]dq.
\]

The integral is finite exactly because `a<1`: its large-`q` integrand is asymptotic to `m_2 q^{a-2}`. Consequently

\[
\kappa_h(r)\asymp r^{a+1},
\]

not `r^2`.

At the boundary `a=1`,

\[
\beta_h(r)\sim c_dc,m_2\,r^{-3}\log r,
\qquad
\kappa_h(r)\asymp\frac{r^2}{\log r}.
\]

For `a>1`, `E R^{-1}<infinity` and Theorem B applies. This is a sharp three-regime phase diagram, not merely a technical integrability caveat.

### 5.3 Sensitivity tails also matter

The transition-layer proof requires finite `m_0,m_2`, and the two-dimensional sphere-mixture proof needs the displayed kernel bound. Heavy-tailed sensitivities can receive leading mass from scores far outside `O(1/r)` and need not obey the same exponents. Every logistic derivative power is exponentially localized, so this limitation does not affect the target family.

## 6. Primary-literature priority audit

### Classical spherical/elliptical structure

- S. Cambanis, S. Huang and G. Simons, [*On the theory of elliptically contoured distributions*](https://doi.org/10.1016/0047-259X(81)90082-8), Journal of Multivariate Analysis 11(3) (1981), 368--385. This is a primary source for the radius--direction stochastic representation and conditional structure of elliptical laws. It does not study neuronal Hessians or saturation.
- E. Liebscher, [*Constructing models for spherical and elliptical densities*](https://doi.org/10.1515/demo-2023-0111), Dependence Modeling 11(1) (2023), article 20230111. It develops spherical/elliptical density generators and lower-dimensional marginal densities. It does not contain the weighted Hessian asymptotics or the `E R/E R^{-1}` anisotropy constant.

These sources mean that the radius--direction decomposition and projection-density formulas are classical ingredients, not new contributions.

### Single-neuron and single-index work under symmetric designs

- G. Yehudai and O. Shamir, [*Learning a Single Neuron with Gradient Methods*](https://proceedings.mlr.press/v125/yehudai20a.html), PMLR 125 (2020), 3756--3786, uses spherically symmetric input assumptions in learnability/gradient arguments. It does not derive strong-signal radial/tangential Hessian constants.
- S. Goel, A. Gollakota, Z. Jin, S. Karmalkar and A. Klivans, [*Superpolynomial Lower Bounds for Learning One-Layer Neural Networks using Gradient Descent*](https://proceedings.mlr.press/v119/goel20a.html), PMLR 119 (2020), 3587--3596, constructs orthogonal families over all spherically symmetric distributions. Its result is a learning lower bound, not a saturation law.
- H. Eftekhari, M. Banerjee and Y. Ritov, [*Inference in High-dimensional Single-Index Models Under Symmetric Designs*](https://www.jmlr.org/papers/v22/19-744.html), JMLR 22(27) (2021), 1--63, exploits elliptical symmetry for proxy-linear inference. It does not compute the target Fisher/Hessian strong-signal asymptotics.

### Logistic/Fisher saturation literature

- S.-i. Amari, R. Karakida and M. Oizumi, [*Fisher Information and Natural Gradient Learning in Random Deep Networks*](https://proceedings.mlr.press/v89/amari19a.html), PMLR 89 (2019), gives the one-unit Gaussian `phi'^2` Fisher decomposition, not the non-Gaussian radial law.
- J. Chen and A. Mazumdar, [*Finite-Sample Performance of Gradient Descent in Logistic Regression with Gaussian Design*](https://arxiv.org/abs/2606.21683), arXiv:2606.21683v1 (2026), proves the Gaussian `p=1` radial/tangential orders and ordering, not spherical non-Gaussian constants.
- H. Chardon, M. Lerasle and J. Mourtada, [*Finite-sample performance of the maximum likelihood estimator in logistic regression*](https://arxiv.org/abs/2411.02137v3), arXiv:2411.02137v3 (2026). Their “regular design” conditions and Theorem 5 support the `B^{-1}`/`B^{-3}` reference geometry and empirical lower bounds beyond Gaussianity, up to logarithmic factors. Therefore the bare non-Gaussian exponents should **not** be advertised as wholly unprecedented. They do not give the exact spherical population constants, the radial inverse-moment criterion, the all-`p` formula, or the failure phase diagram above.

Searches of current primary literature combining logistic/sigmoid Hessians, spherical or elliptical designs, strong signal/saturation, radial--tangential Fisher eigenvalues, and inverse radial moments did not locate a source with

\[
Q_R=\frac{E R}{(d-1)E R^{-1}},
\]

the three explicit Gaussian/sphere/Student constants, or the `a<1`, `a=1`, `a>1` inverse-radius phase transition. This is a bounded novelty conclusion, not proof that no obscure antecedent exists.

## 7. Exact novelty boundary and recommended theorem programme

### Do not claim

- the radius--direction representation of spherical/elliptical distributions;
- the first use of spherical inputs in single-neuron theory;
- the first `r^{-1}`/`r^{-3}` comparison outside Gaussianity in any form, because Chardon et al.'s regular-design theory already uses that reference geometry;
- universality under isotropy alone.

### Defensible new package

Subject to another independent proof audit, the following compound claim is priority-safe:

> For every localized sensitivity profile, including all logistic powers, the global spherical saturation law has exact leading constants governed only by `E R` and `E R^{-1}`. The anisotropy factor is the conditional transverse variance on the transition hyperplane. Gaussian, fixed-sphere and isotropic Student designs yield distinct closed constants. The inverse-radius condition is sharp: regularly varying radial mass at the origin produces a phase transition from `r^2` to `r^2/log r` or `r^{a+1}` anisotropy.

### Recommended paper structure

1. Transition-density theorem for axially symmetric laws.
2. Exact spherical radius theorem with equations (S1)--(S2).
3. All-`p` logistic corollary and the three canonical constants.
4. Elliptical whitening/generalized-eigenvalue corollary.
5. Sharp counterexamples: isotropic Rademacher and inverse-radius phase transition.
6. Optional finite-radius Hölder remainder and numerical replay for Gaussian, sphere, Student, and a singular-at-zero radial law.

This programme is stronger than merely replacing the Gaussian density by a generic density at zero: it identifies the transverse conditional moment, produces exact distribution-sensitive constants, and states when and how the quadratic law fails.

## Final verdict

**PROOF-COMPLETE PROGRAMME AVAILABLE; NO GENUINE BLOCKER.** The global non-Gaussian theorem is valid for spherical isotropic inputs under the sharp negative-radius-moment condition and for more general axially symmetric inputs under explicit transition-density assumptions. The literature search found prior non-Gaussian exponent-scale and spherical-learning adjacencies, but no direct antecedent for the exact radial constants, all-power corollary, or sharp inverse-radius phase transition.

The principal publication risk is wording, not mathematics: present the result as an exact-constant and sharp-boundary refinement, not as the first appearance of non-Gaussian `r^{-1}`/`r^{-3}` scaling.
