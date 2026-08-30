# Hostile proof audit V3

**Files audited:** `src/main.tex`, `repro/verify_saturation_law.py`  
**Focus:** Theorem `local order--anisotropy bridge`, equation `(bridge)`, and the three V2 blockers  
**Date:** 2026-08-29  
**Final verdict:** **REVISE**

The coefficient identity in `(bridge)` is correct, its assumptions are sufficient, and all three V2 blockers are fixed. One scope overstatement remains inside the bridge theorem. It has an explicit counterexample under the theorem's own hypotheses. No other blocking defect was found.

## Blocking finding

### [P1] “Every sufficiently close nontrivial Loewner pair” is false unless the pair is also localized near zero

Lines 377--378 conclude from `Sg(0)<0` that

> every sufficiently close nontrivial Loewner pair [is] indefinite.

Equation `(bridge)` and the proof establish the sign only for the anchored pair `L_g(0,delta)` as `delta -> 0`. The hypotheses do not require `Sg(x)<0` away from zero. Small separation `|x-y|` alone therefore cannot force a negative determinant everywhere.

An explicit counterexample satisfying every hypothesis is

\[
 g(x)=\int_0^x e^{\cos t}\,dt.
\]

Then `g'(x)=e^{cos x}>0`, `g''(0)=0`, and for every `p>0`,
`h_p(x)=e^{p cos x}` is smooth with bounded fourth derivative. Writing `q=log g'=cos x` gives

\[
 Sg(x)=q''(x)-\frac12q'(x)^2
      =-\cos x-\frac12\sin^2x.
\]

Thus `Sg(0)=-1<0`, but `Sg(pi)=1>0`. Consequently,

\[
 \det L_g(\pi,\pi+\delta)
 =\frac{g'(\pi)^2}{6}\,\delta^2+O(\delta^3)>0
\]

for all sufficiently small nonzero `delta`; with positive diagonal entries, these nearby Loewner matrices are positive definite rather than indefinite.

**Required correction:** replace the conclusion by

> `Sg(0)<0` makes `L_g(0,delta)` indefinite for every sufficiently small nonzero `delta`.

Alternatively, say “every nontrivial pair contained in a sufficiently small neighborhood of zero,” and add the short uniform argument: continuity gives `Sg<0` on a neighborhood of zero, while the adjacent-pair expansion is uniform on a compact sub-neighborhood. The current unlocalized wording is not implied by the theorem.

## Verification of equation `(bridge)`

No defect was found in the identity itself.

1. Since `h_p` has bounded fourth derivative, Taylor's theorem gives a global remainder bounded by `C|rZ|^4`. Gaussian fourth and sixth moments make this remainder integrable both in `alpha_p` and after multiplication by `Z^2` in `beta_p`. Thus Taylor expansion under expectation is justified.
2. Gaussian odd moments cancel the linear and cubic terms, and `E Z^2=1`, `E Z^4=3`, giving
   \[
   \alpha_p=h_p(0)+\tfrac12h_p''(0)r^2+O(r^4),\qquad
   \beta_p=h_p(0)+\tfrac32h_p''(0)r^2+O(r^4).
   \]
3. Because `h_p(0)>0`, division is legitimate and yields
   \[
   \kappa_p(r)=1-\frac{h_p''(0)}{h_p(0)}r^2+O(r^4).
   \]
4. From `log h_p=p log g'` and `g''(0)=0`,
   \[
   h_p''(0)/h_p(0)=p g'''(0)/g'(0)=pSg(0).
   \]
5. Direct adjacent-point expansion gives
   \[
   \det L_g(0,\delta)
   =\left(\frac{g'(0)g'''(0)}6-\frac{g''(0)^2}{4}\right)\delta^2+O(\delta^3)
   =\frac{g'(0)^2Sg(0)}6\delta^2+O(\delta^3).
   \]
   Therefore the coefficient and sign in `(bridge)` are exactly correct:
   \[
   \lim_{r\downarrow0}\frac{\kappa_p(r)-1}{r^2}
   =-pSg(0)
   =-\frac{6p}{g'(0)^2}
     \lim_{\delta\to0}\frac{\det L_g(0,\delta)}{\delta^2}.
   \]

The assumptions are stronger than necessary but coherent: `g'>0` makes real powers `(g')^p` well-defined and positive; the bounded fourth derivative of `h_p` supplies the needed global Gaussian domination; `g in C^5` is sufficient for the Loewner expansion.

## Verification of the three V2 blockers

All are closed.

1. **Dimension:** the abstract now explicitly assumes `d>=2` before calling `alpha/beta` the logistic spectral condition number.
2. **Transition-slab interpretation:** lines 407--412 now correctly state that both modes are supported by the near-boundary slab and that the radial mode alone pays the additional `Z^2` factor.
3. **Deterministic replay:** two consecutive executions produced identical artifacts:
   - figure SHA-256: `093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97` on both runs;
   - certificate SHA-256: `17c83799f6581b5b602e29960b8660c15a186f36d2aedc225eb5c4d3f6ac8bc7` on both runs.

The replay passed all declared checks, including the two logistic bridge coefficients, and the manuscript compiled successfully to an 11-page PDF without a LaTeX error.

After localizing the single overbroad sentence in Theorem `bridge`, the final mathematical verdict is **ACCEPT**.
