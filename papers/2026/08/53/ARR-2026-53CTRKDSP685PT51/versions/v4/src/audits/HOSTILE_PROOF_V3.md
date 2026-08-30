# Hostile proof audit of v3

## Verdict: FAIL (core matching-lower theorem passes; two claim-boundary defects block publication)

Audited source: `work/neuron_paper_v3/src/main.tex` as present on 2026-08-29. I did not edit the manuscript.

Executed checks:

- `repro/explicit_sample_constants.py`: PASS; it returns `C_1=22929`, `C_2=294162`, and the stated angle constants.
- `repro/verify_v3_additions.py`: PASS.
- `repro/verify_saturation_law.py`: PASS.
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`: PASS, 22 pages.

The numerical replays do not address the logical claim-boundary defects below.

## Blocking findings

### P0 — The claimed bottom-eigenspace lower bracket is neither proved nor implied by the stated spectral obstruction

Affected text:

- Immediately after Theorem `matchinglower`: “robust recovery of the ordinary bottom eigenspace is presently bracketed by a direct \(\Omega_p(rd/\log r)\) spectral obstruction and the \(O_p(rd)\) sufficient event above.”
- Limitations: “the present bottom-eigenspace bracket retains a logarithmic gap.”
- Figure 2 caption, which says that the common horizontal scale `n/(rd)` is predicted by Theorems `empirical` and `matchinglower` while displaying ordinary smallest-eigenvalue error and radial eigenspace angle.

There is no theorem or proof of an `Omega_p(rd/log r)` result in `main.tex`. More importantly, even the available logarithmic-slab construction proves only this type of statement:
\[
 \Pr\{\exists v\perp u:\ v^TCv<\beta/2\}\ge c.
\]
It follows that `lambda_min(Hhat)<beta/2`, i.e. ordinary spectral non-resolution. It does **not** by itself imply a lower bound on the angle of an arbitrarily tie-broken smallest eigenvector. Cross-block coupling and multiplicity/spacing of the low tangential modes still have to be controlled. A low tangential Rayleigh quotient is not an eigenspace-angle theorem.

Exact mandatory correction: choose one of the following.

1. **Safe minimal correction:** replace both bottom-eigenspace claims by:

   > A logarithmic-slab argument gives an `Omega_p(rd/log r)` obstruction to keeping every tangential Rayleigh quotient above the population radial scale. This is an ordinary spectral-resolution obstruction, not an eigenspace-angle lower bound. The present angle upper bound is `O_p(rd)` at fixed accuracy; no matching angle lower bound is claimed.

   In Figure 2, replace “the horizontal scale `n/(rd)` is predicted” with “the horizontal scale `n/(rd)` is the sufficient bilateral-Loewner scale; the smallest-eigenvalue and angle panels are diagnostics and no matching lower law is claimed for them.” Include the logarithmic-slab proposition and proof if the `Omega_p(rd/log r)` assertion is retained.

2. **Stronger correction:** add a genuine angle-lower theorem that controls `b`, the multiplicity of low tangential modes, and the selected empirical spectral projector. No such proof is currently present.

Until this is corrected, the target separation advertised in the paper is mathematically false at its most delicate boundary.

### P1 — `Theta_p(r/epsilon^2)` for the radial scalar is asserted without a lower proof

Affected text immediately after Theorem `matchinglower`:

> “the radial scalar entry has intrinsic constant-confidence complexity `Theta_p(r/epsilon^2)`”

The upper half follows from the scalar Bernstein term `e_R`. The current lower argument `eq:lower` proves `Omega_p(r log(1/delta))` only at fixed relative accuracy; it does not establish the `epsilon^{-2}` dependence. The matching-lower theorem obtains its `epsilon^{-2}` confidence term from a **tangential Gaussian off-diagonal entry**, so that theorem cannot be cited as a radial-scalar lower bound.

Exact mandatory correction: either weaken the sentence to the bounds actually proved in the paper, or add the following short argument.

Let `V=h_p(rZ)Z^2`, `beta=EV`, and `nu^2=Var(V)`. Scaled integration yields
\[
 \beta\asymp_p r^{-3},\qquad \nu^2\asymp_p r^{-5},\qquad
 \mathbb E(V-\beta)^4=O_p(r^{-9}).
\]
For `S_n=sum_i(V_i-beta)`,
\[
 \mathbb ES_n^2=n\nu^2,
 \quad
 \mathbb ES_n^4=n\mathbb E(V-\beta)^4+3n(n-1)\nu^4.
\]
Paley--Zygmund applied to `S_n^2` gives a constant lower probability for
\[
 |n^{-1}S_n|\ge\sqrt{\nu^2/(2n)}
 \asymp_p\beta\sqrt{r/n}
\]
when `n>=C_p r`; the existing empty-slab result covers `n<C_p r`. This proves the stated constant-confidence `Omega_p(r/epsilon^2)` for sufficiently small `epsilon`. State explicitly that the all-`epsilon`, high-confidence scalar lower tail is not proved unless an additional moderate-deviation argument is supplied.

## Mandatory proof clarification

### P1 — The high-confidence part of Theorem `matchinglower` suppresses the moment calculation and the small-`n` case

The theorem is valid, but lines 1010--1018 currently say only that the normalized second moment of
\[
 T=n^{-1}\sum_i A_i^2Y_{i1}^2
\]
“is bounded when `n` is at least order `r`.” For a theorem advertised as proof-complete, the missing calculation is essential. Insert
\[
 \mathbb ET=\rho=\frac{\gamma_0}{\alpha^2},
\]
\[
 \frac{\mathbb ET^2}{\rho^2}
 \le1+\frac{3\mathbb EA^4}{n\rho^2}
 =1+\frac{3\mathbb EW^4}{n\gamma_0^2}
 \le1+C_p\frac rn.                                           \tag{A}
\]
The last inequality follows from the finite-radius lower bracket for `gamma_0=E h_{2p}(rZ)` and the upper bracket for `E W^4=E h_{4p}(rZ)`. Paley--Zygmund then supplies an explicit `q_p>0` when `n>=a_p r`.

Also state the dichotomy explicitly: if `n<a_p r`, the empty-slab lower bound gives a fixed failure probability and is absorbed by choosing `delta_p`; if `n>=a_p r`, use (A) and the conditional Gaussian tail. Finally record that choosing `delta_p` small makes
\[
 \log(c'_p/\delta)\ge c\log(1/\delta),
\]
which is needed to pass from the displayed exponential lower tail to the theorem's stated logarithm.

This is a proof-completeness correction, not a counterexample to the theorem.

## Detailed audit of Theorem `matchinglower`

### Constant-confidence product term: PASS

Let `S_0=sum W_i^2`, `gamma_0=EW^2`, and `W<=H`.

1. The first Paley--Zygmund step is correct:
   \[
   \mathbb ES_0=n\gamma_0,
   \quad
   \mathbb ES_0^2
   =n\mathbb EW^4+n(n-1)\gamma_0^2
   \le nH^2\gamma_0+n^2\gamma_0^2.
   \]
   If `n gamma_0>=H^2`, this gives
   \[
   \Pr\{S_0\ge n\gamma_0/2\}\ge1/8.
   \]

2. Conditional on `W`, for `T_0=sum W_i^2Y_{i1}^2`,
   \[
   \mathbb E(T_0\mid W)=S_0,
   \quad
   \mathbb E(T_0^2\mid W)=S_0^2+2\sum_iW_i^4\le3S_0^2,
   \]
   so the second probability is at least `1/12`.

3. Conditional on `(W,Y_1)`, the `d-2` remaining coordinates are independent Gaussians of variance `T_0/n^2`. For `Q~chi^2_k`,
   \[
   \Pr\{Q\ge k/2\}\ge\frac{k}{4(k+2)}\ge1/12,
   \quad k=d-2\ge1.
   \]

4. The intersection probability `1/(8*12*12)=1/1152` and norm threshold
   \[
   \|C/\alpha-I\|_{op}
   \ge\sqrt{\frac{(d-2)\gamma_0}{8n\alpha^2}}
   \]
   are correct.

5. The finite-radius ratio
   \[
   \frac{\gamma_0}{\alpha^2}
   \ge\frac{m_0(2p)}{2\varphi(0)m_0(p)^2}r
   \]
   is correct: use the lower bracket for `gamma_0` and the upper bracket for `alpha`.

6. The explicit threshold coefficient is therefore correct. For `p=1`, it is `1/[96 phi(0)]`; for `p=2`, it is `9/[560 phi(0)]`.

7. The complementary condition `n gamma_0<H^2` indeed implies `n=O_p(r)`, because the same lower bracket gives `gamma_0>=c_p/r`; the empty-slab event then has a fixed positive probability. This should be written rather than left implicit.

### Confidence term: PASS after the proof clarification above

Conditional on the complete `(A_i,Y_{i1})` data, one off-diagonal entry is exactly `N(0,T/n)`. Conditioning only on `T` is also valid because the conditional characteristic function depends on the complete data only through `T`. On `{T>=rho/2}`,
\[
 \Pr\{|D_2|>\varepsilon\mid T\}
 \ge 2\Phi\!\left(-\varepsilon\sqrt{2n/\rho}\right)
 \ge c_0e^{-2n\varepsilon^2/\rho}.
\]
Together with (A), this yields `Omega_p(r epsilon^{-2} log(1/delta))`. Combining the dimension and confidence lower bounds by `max>=sum/2` is correct. The replacement of `d-2` by `d` costs only a factor three for `d>=3`.

### Scope: PASS with a wording qualification

The formal theorem correctly restricts to:

- fixed `p`;
- sufficiently large `r`;
- `d>=3`;
- `epsilon<=1/2`;
- `delta<=delta_p`;
- pointwise fixed-teacher bilateral relative Loewner loss.

The abstract's unqualified `Theta_p` formula should preferably say “for sufficiently large saturation and nontrivial confidence, in the range of Theorem `matchinglower`.” This is a precision correction, not a mathematical failure.

## Audit of the remaining theorem chain

### Explicit empirical upper theorem: PASS

- The scalar Bernstein, conditional weighted-chi-square net, radial Bernstein, and conditional Gaussian cross-block bounds are consistent.
- The failure count `9e^{-t}<delta` with `t=log(12/delta)` is conservative.
- Conjugation by `H^{-1/2}` gives exactly the bilateral relative Loewner bound.
- The eigengap, Schur-complement eigenvalue error, and angle bound have the correct sign and denominator.
- The logistic envelopes and `gamma_j` exponents are correct.
- The finite-radius choice of `R_p` implies the three population bounds used in the corollary, including `alpha-beta>=phi(0)m_0/(2r)`.
- The replayed sufficient constants agree with the source: `C_1=22929`, `C_2=294162`.

### Uniform shell theorem: PASS

- `||h_p'||_infinity<=p4^{-p}` is correct.
- The empirical-plus-population Lipschitz constant is bounded by the stated `A_{p,n,delta}`; `mu_{3,d}` is a valid Hölder upper bound for `E||X||^3`.
- The Gaussian norm event, shell covering number, pointwise union bound, and factor `128=64*2` from error `epsilon/8` and radius at most `2R` are consistent.
- `lambda_min G_p(w)>=phi(0)m_2(p)/(16R^3)` follows from `||w||<=2R`.
- The final conversion from operator Lipschitz error to relative quadratic-form error is conservative.

### Gaussian and spherical population theorems: PASS

- The Gaussian `alpha/beta` reduction, finite-radius brackets, all-`p` moments, endpoint expansions, monotonicity argument, and finite-scale bridge remain consistent with the prior audits and verifier.
- In the global spherical theorem, the factors `E R`, `E R^{-1}`, `d-1`, and `c_d` follow from the exact radius/direction change of variables.
- For `d=2`, exponential localization controls the angular boundary singularity uniformly; the additional hypothesis is sufficient.
- The Gaussian, fixed-sphere, and Student values of `Q_R` are correct.
- The phase transition `r^{-(a+2)}`, `r^{-3}log r`, `r^{-3}` follows from the large-`q` integrand `q^{a-2}`.
- The Rademacher counterexample is correct for even `h`.

## Nonblocking editorial corrections

1. The phrase “explicit sufficient obstruction” in Theorem `matchinglower` is awkward: the inequality is a **sufficient condition for failure**, hence a **necessary sample-size lower bound**. Use one of those descriptions.
2. The explicit constants `C_1,C_2` are checked by a script, but the manuscript only sketches the deterministic majorization. For maximal proof completeness, include the `a_T,b_T,a_R,b_R,a_q,b_q` formulas in an appendix.
3. State that the theorem's lower constants depend on `p`; the notation already does this, but the abstract's `Theta_p` could be misread as uniform over `p`.

## Final decision

**FAIL as presently written.** The matching product theorem itself passes, and no counterexample was found to it. Publication is blocked by the unsupported and logically overextended bottom-eigenspace bracket and by the unproved radial-scalar `epsilon^{-2}` lower claim. After either proving or weakening those two statements, and inserting calculation (A), the mathematical verdict becomes **PASS**.

---

## Final re-audit after mandatory corrections (2026-08-29)

### Final verdict: PASS

I re-read the revised finite-sample section, Figure 2 caption, and limitations, and recompiled the manuscript twice. All three blocking corrections from this report are correctly implemented:

1. **Bottom eigenspace:** the unsupported `Omega_p(rd/log r)` bracket and every implied angle-lower claim have been removed. The manuscript now states only the proved `O_p(rd)` sufficient angle event and explicitly says that no matching lower threshold for the ordinary bottom eigenspace is proved. Figure 2 now identifies `n/(rd)` as the sharp scale only for full bilateral relative Loewner loss and labels the ordinary-eigenvalue and angle panels as diagnostics.

2. **Radial scalar:** the unproved `Theta_p(r/epsilon^2)` assertion has been replaced by exactly the proved boundary: scalar Bernstein gives the constant-confidence upper `O_p(r/epsilon^2)`, while the empty-slab theorem gives the fixed-accuracy lower `Omega_p(r)`. No all-`epsilon` scalar lower is claimed.

3. **High-confidence lower proof:** the manuscript now includes
   \[
   \frac{\mathbb ET^2}{\rho^2}
   \le1+\frac{3\mathbb EW^4}{n(\mathbb EW^2)^2}
   \le1+C_p\frac rn,
   \]
   invokes Paley--Zygmund for `n>=a_p r`, and explicitly routes `n<a_p r` through the slab event after fixing `delta_p`. This supplies the missing proof bridge to the conditional Gaussian lower tail.

The revised text preserves the correct separation among bilateral relative Loewner loss, the radial scalar entry, ordinary eigenvalue diagnostics, and eigenspace-angle recovery. No new counterexample, constant error, probability-count error, or scope overclaim was found.

Final build: `pdflatex -interaction=nonstopmode -halt-on-error main.tex` succeeds; a second pass reports no undefined references. The standalone verifier status remains PASS.

**Publication-blocking mathematical objections: none. Final decision: PASS.**
