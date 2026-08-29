# Independent hostile algebra and reproducibility audit V5

**Audited manuscript:** `work/neuron_paper_v2/src/main.tex`, SHA-256
`B22C2CEE2FC8BFA3699431AC83EB4440AFA38D120A6D147BB342264295B85523`
(53,122 bytes; observed 2026-08-29 12:22:41 Europe/Stockholm).

**Audited replay:** `work/neuron_paper_v2/repro/verify_saturation_law.py`,
SHA-256
`EAD8E380B681306A42829C0D0AD92C2E598E3385C827FC612B575678BB79FA65`
(21,720 bytes; observed 2026-08-29 12:21:05 Europe/Stockholm).

## Verdict

**PASS on the core mathematics; MINOR REVISION REQUIRED for proof exposition,
claim wording, and replay coverage wording.**

I found no incorrect coefficient in the all-`p` Gamma/polygamma identities,
the `r^6` jet, the refined large-`r` law, the spherical `q_X` bridge, the
finite-scale constants `C_h,D_g`, or the normalized empirical Loewner
implication. The finite-sample block theorem and the empty-slab lower bound
also survive independent re-derivation.

There are, however, four concrete corrections/clarifications before release:

1. a visible LaTeX source typo prints the word `quad` inside an equation;
2. “rotational symmetry and a fourth moment suffice” contradicts the stated
   sixth-moment hypothesis needed for the displayed `O(r^4)` proof;
3. `O_p` is used for “constant depending on the sensitivity power `p`,” but
   conventionally means stochastic boundedness in probability;
4. the replay's success banner/description can be read more broadly than the
   finite grid and three fixed empirical realizations it actually tests.

## 1. All-power Fourier and moment algebra

For

\[
 h_p(t)=\sigma'(t)^p=\frac{e^{pt}}{(1+e^t)^{2p}},\qquad p>0,
\]

the substitution `x=e^t` gives exactly

\[
 \widehat h_p(k)=\int_0^\infty
 \frac{x^{p+ik-1}}{(1+x)^{2p}}\,dx
 =B(p+ik,p-ik)
 =\frac{\Gamma(p+ik)\Gamma(p-ik)}{\Gamma(2p)}.
\]

If `L=log(hat h_p)`, then

\[
 L'(0)=0,\quad L''(0)=-2\psi_1(p),\quad
 L^{(4)}(0)=2\psi_3(p).
\]

Therefore

\[
 m_0=\frac{\Gamma(p)^2}{\Gamma(2p)},\qquad
 m_2=-\widehat h_p''(0)=2\psi_1(p)m_0,
\]

and

\[
 m_4=\widehat h_p^{(4)}(0)
 =m_0\{L^{(4)}(0)+3L''(0)^2\}
 =m_0\{2\psi_3(p)+12\psi_1(p)^2\}.
\]

**Assessment: correct.** The `p=1,2` table follows exactly. The proof would be
slightly more complete if it explicitly noted that `h_p(t)=O(e^{-p|t|})`, so
all Fourier differentiations used for moments are justified.

## 2. Small- and large-radius endpoint laws

### Small radius

After canceling `4^{-p}`, direct expansion gives

\[
 \operatorname{sech}^{2p}(t/2)
 =1-\frac p4t^2+\frac{p(1+3p)}{96}t^4
 -\frac{p(15p^2+15p+4)}{5760}t^6+O(t^8).
\]

Using the Gaussian moments through `E Z^8=105` in numerator and denominator
and dividing yields

\[
 \boxed{
 \kappa_p(r)=1+\frac p2r^2-\frac p8r^4
 +\frac{p(p+1)}{16}r^6+O(r^8).}
\]

All `p^2` terms do cancel from the fourth-order ratio coefficient.

**Assessment: correct.** For full rigor, the manuscript should add that every
real derivative of `sech^{2p}(t/2)` is bounded for fixed `p>0`; this supplies a
global Taylor remainder that may be integrated against the Gaussian. A local
power series alone does not automatically justify exchanging an `O(t^8)`
remainder with an unbounded Gaussian variable.

### Large radius

The scaled integrals give

\[
 \alpha_p=\frac{\varphi(0)}r
 \left(m_0-\frac{m_2}{2r^2}+\frac{m_4}{8r^4}+O(r^{-6})\right),
\]

\[
 \beta_p=\frac{\varphi(0)}{r^3}
 \left(m_2-\frac{m_4}{2r^2}+O(r^{-4})\right).
\]

Consequently

\[
 \kappa_p(r)=\frac{m_0}{m_2}r^2+
 \frac{m_0}{m_2}
 \left(\frac{m_4}{2m_2}-\frac{m_2}{2m_0}\right)+O(r^{-2}).
\]

Substitution of the polygamma moments reduces this to

\[
 \boxed{
 \kappa_p(r)=\frac{r^2}{2\psi_1(p)}
 +1+\frac{\psi_3(p)}{4\psi_1(p)^2}+O(r^{-2}).}
\]

**Assessment: correct.** Exponential decay supplies the higher moments needed
for the remainder.

### Monotonicity

For `r_2>r_1` and `z>0`,

\[
 \partial_z\log\frac{h_p(r_2z)}{h_p(r_1z)}
 =-p\{r_2\tanh(r_2z/2)-r_1\tanh(r_1z/2)\}<0,
\]

because `a -> a tanh(az/2)` is strictly increasing. Thus the normalized law
of `|Z|` decreases strictly in monotone-likelihood-ratio order and its second
moment decreases. Hence `kappa_p` increases strictly for every `p>0`.

**Assessment: correct.** This is an analytic all-`p` theorem; it does not rely
on the replay grid.

## 3. Spherical `q_X` theorem

For an orthogonally invariant `X` with covariance `I_d`, write `X=R Theta`,
where `Theta` is uniform on `S^{d-1}` and independent of `R`. Then

\[
 \mathbb E Z^4=\frac{3\mathbb ER^4}{d(d+2)}=3q_X,qquad
 \mathbb E[Z^2(v^TX)^2]=\frac{\mathbb ER^4}{d(d+2)}=q_X.
\]

Taylor expansion, cancellation of odd terms, and division therefore give

\[
 \kappa_{p,X}(r)=1-q_X\frac{h_p''(0)}{h_p(0)}r^2+O(r^4)
 =1-q_XpSg(0)r^2+O(r^4).
\]

The last identity uses `g''(0)=0`. Combining it with

\[
 \det L_g(0,\delta)=\frac{g'(0)^2Sg(0)}6\delta^2+O(\delta^3)
\]

produces the displayed bridge.

**Assessment: correct under the theorem's actual hypotheses:** `d>=2`, full
orthogonal invariance, covariance `I_d`, `E||X||^6<infinity`, and bounded
`h_p^{(4)}`. The sixth moment controls terms such as
`E[|Z|^4(v^TX)^2]` in the fourth-order remainder.

**Claim-consistency correction:** the prose immediately before the theorem
says that “rotational symmetry and a fourth moment suffice.” A fourth moment
defines `q_X` and the coefficient algebra, but the proof printed here uses a
sixth moment to obtain `O(r^4)`. Replace that sentence by “rotational symmetry
and suitable moments suffice,” or explicitly distinguish coefficient
identification from the stronger remainder.

## 4. Explicit `C_h` inequality

Set `a=h_p(0)>0`, `b=h_p''(0)`, and `M_4=||h_p^{(4)}||_infinity`. Gaussian
Taylor bounds give

\[
 \alpha=a+\frac b2r^2+R_\alpha,quad |R_\alpha|\le\frac{M_4}{8}r^4,
\]

\[
 \beta=a+\frac{3b}{2}r^2+R_\beta,quad
 |R_\beta|\le\frac{5M_4}{8}r^4.
\]

The stated `r_0` condition indeed implies `beta>=a/2`. With
`Q=1-(b/a)r^2`, exact subtraction gives

\[
 \alpha-Q\beta=R_\alpha+\frac{3b^2}{2a}r^4
 -\left(1-\frac ba r^2\right)R_\beta.
\]

Dividing by `beta>=a/2` yields exactly

\[
 C_h=\frac{3M_4}{2a}+3\left(\frac ba\right)^2
 +\frac{5|b|M_4}{4a^2}r_0^2.
\]

**Assessment: correct.** No missing factor was found.

For the logistic replay, the code uses

\[
 M_4^{\rm code}=4^{-p}
 \left(\frac p2+\frac{11p^2}{4}+3p^3+p^4\right).
\]

This is a valid conservative bound. One way to see it is to put
`f=sech^{2p}(t/2)` and `ell=log f`; the identity
`f^{(4)}/f=ell^{(4)}+4ell'ell'''+3ell''^2+6ell'^2ell''+ell'^4`, together with
`|tanh|,sech^2<=1`, gives a bound no larger than the code's polynomial.
The replay itself does not certify this supremum; the analytic bound should be
recorded in a comment or certificate if it is intended as an independently
auditable constant.

## 5. Explicit `D_g` inequality

Let `A=g'(0)>0`, `c=g'''(0)`, `d_4=g^{(4)}(0)`, and
`M_5=sup_{|x|<=delta_0}|g^{(5)}(x)|`. Since `g''(0)=0`,

\[
 g'(\delta)=A+\frac c2\delta^2+\frac{d_4}{6}\delta^3+R_1,
 \quad |R_1|\le\frac{M_5}{24}|\delta|^4,
\]

\[
 V:=\frac{g(\delta)-g(0)}\delta
 =A+\frac c6\delta^2+\frac{d_4}{24}\delta^3+R_2,
 \quad |R_2|\le\frac{M_5}{120}|\delta|^4.
\]

Using `det L=A g'(delta)-V^2` gives the leading term `Ac delta^2/6`
and the remainder bound

\[
 \frac{|Ad_4|}{12}|\delta|^3
 +\frac{7AM_5}{120}|\delta|^4+K^2|\delta|^4,
\]

where the printed `K` bounds `|V-A|/|delta|^2`. For
`|delta|<=delta_0`, this is exactly `D_g|delta|^3` with the manuscript's
`D_g`.

**Assessment: correct.** The logistic code's `M_5=1082` is safe: writing
`s=sigma(t)`, the fifth derivative is

\[
 -120s^6+360s^5-390s^4+180s^3-31s^2+s,
\]

whose coefficient `l^1` norm is `1082` on `0<=s<=1`.

**Required typesetting correction:** the source currently contains

```tex
... +R_1,quad
```

instead of `...+R_1,\quad`. The PDF visibly prints “quad” as mathematical
letters between the two Taylor expansions.

## 6. Direct finite bridge

Dividing the `C_h` estimate by `r^2`, the `D_g` estimate by `delta^2`, and
using

\[
 \frac ba=pSg(0),\qquad \frac{Ac}{6}=\frac{A^2Sg(0)}6
\]

gives

\[
 \left|\frac{\kappa_p(r)-1}{r^2}
 +\frac{6p}{A^2}\frac{\det L_g(0,\delta)}{\delta^2}\right|
 \le C_hr^2+\frac{6pD_g}{A^2}|\delta|.
\]

**Assessment: correct.** The signs agree: for the standard logistic,
`Ssigma=-1/2`, `A=1/4`, and
`det L_sigma(0,delta)~-delta^2/192`.

## 7. Empirical block theorem and normalized Loewner implication

The three block bounds are valid:

- `C`: condition on `Z_i`; the tangential `Y_i` remain independent standard
  Gaussian vectors. Scalar Bernstein controls the sample mean of `W`, and a
  `1/4`-net plus the weighted chi-square MGF gives the stated `e_T`.
- `c_n`: Bernstein for the bounded variable `WZ^2` gives `e_R`, with variance
  proxy `gamma_2`.
- `b_n`: conditionally Gaussian with covariance
  `(sum W_i^2Z_i^2/n^2)I_m`; one-sided Bernstein and the Gaussian norm tail
  give `q_n`.

The failure budget is also consistent: the listed events total at most
`9e^{-t}=3delta/4<delta` when `t=log(12/delta)`.

Let `Delta=hat H-H`. Conjugation gives a normalized block matrix whose
diagonal-block norms are at most `e_T/alpha` and `e_R/beta` and whose off-block
norm is at most `q_n/sqrt(alpha beta)`. Hence

\[
 \|H^{-1/2}\Delta H^{-1/2}\|_{op}
 \le \max\{e_T/\alpha,e_R/\beta\}
 +q_n/\sqrt{\alpha\beta}=\varepsilon_n.
\]

This is exactly equivalent to

\[
 (1-\varepsilon_n)H\preceq\widehat H
 \preceq(1+\varepsilon_n)H.
\]

The Schur-complement angle and eigenvalue estimates also have the correct gap
`G=alpha-beta-e_T-e_R` and no missing factor.

**Assessment: correct.** Note that the lower relative bound is noninformative
when `epsilon_n>=1`; the later corollary explicitly imposes a small target
epsilon when using it for resolution.

The logistic envelopes are correct:

\[
 H=4^{-p},\quad K_1\le e^{-2}/(p^2r^2),\quad
 K_2\le4e^{-2}/(p^2r^2),
\]

and variable substitution gives the printed `gamma_0,gamma_1,gamma_2`
bounds. Combining them with the finite-radius population lower bounds produces
the stated sufficient order `n >= C_p r[d+log(12/delta)]/epsilon^2` for fixed
`p`.

**Notation correction:** write `\lesssim_p`, “with a constant depending on
`p`,” or an explicit `C_p`, rather than `O_p`. In statistics, `O_p` normally
means bounded in probability, not dependence on the profile exponent. This
occurs in the abstract and in the angle display.

## 8. Empty-slab lower bound

Let `A={|Z|>a_p/r}`. Since
`P(A^c)<=2varphi(0)a_p/r<=1/2`,

\[
 P(A)^n\ge\exp[-4\varphi(0)a_pn/r].
\]

The tail-moment choice and `r^2>=m_4/m_2` imply

\[
 E[WZ^2\mid A]\le\frac{\varphi(0)m_2}{8r^3}
 \le\frac{\beta_p(r)}4.
\]

Conditional Markov then gives probability at least `1/2` that the empirical
radial Rayleigh quotient is below `beta/2`, and hence the smallest eigenvalue
is below `beta/2`. The printed probability and necessary
`Omega_p(r log(1/delta))` consequence follow.

**Assessment: correct.** The manuscript properly refuses to multiply this
obstruction by the separate rank condition `n>=d`.

## 9. Replay execution and actual coverage

I executed

```text
python repro/verify_saturation_law.py
```

successfully. It reported

```text
PASS: Loewner/Arb witness, spherical and quantitative bridges, all-p moments and endpoint laws, monotone anisotropy, empirical block bounds, and finite-r brackets
figure_sha256=093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97
certificate_sha256=a5442d5840a08ed1394e21f8f4d82f7947ba35ba7bd6cc5e9cf00d4df0c3618a
```

It also compiles under `pdflatex -halt-on-error`, producing 17 pages. The
typesetting typo noted above nevertheless remains visible in the PDF.

### What the script genuinely checks

- four floating-point evaluations of the closed logistic determinant;
- one 256-bit Arb-certified `2x2` matrix witness;
- `m_0,m_2,m_4` at five powers `p=0.5,1,1.7,2,3.25`;
- the Gaussian bridge at those five powers and three small radii;
- the fixed-radius spherical bridge in dimension five at three powers and
  three small radii;
- the `r^6` jet and refined large-`r` formula at one small and one large radius
  for five powers;
- positivity and grid monotonicity only for `p=1,2`, and only through the
  numerically declared range;
- the quantitative bridge for four powers and three `(r,delta)` pairs, only
  for the standard logistic activation;
- realized block and normalized-operator errors for three fixed random seeds;
- universal finite-radius brackets for `p=1,2` at four radii;
- deterministic regeneration of the figure and JSON certificate.

### What it does not certify

- the universal all-p monotonicity theorem (the proof does this);
- supremum definitions such as a general `M_4` or `M_5` by interval
  optimization;
- spherical laws beyond one fixed-radius example, or arbitrary radial
  mixtures;
- probability coverage of the empirical theorem over repeated samples;
- the empirical eigenspace-angle/eigenvalue bounds;
- the sufficient sample-size corollary or the empty-slab lower bound;
- universal Loewner negativity for all pairs (the analytic proof does this).

The manuscript mostly acknowledges that numerical checks are diagnostic.
Still, change “checks ... monotone anisotropy for several powers” to “checks
grid monotonicity for `p=1,2`,” and make the final PASS banner similarly
specific. A single realization lying inside a `1-delta` event is not a
calibration test of the claimed probability.

## 10. Final action list

Required before publication:

1. Replace `R_1,quad` by `R_1,\quad`.
2. Reconcile “a fourth moment suffice” with the theorem's sixth-moment
   assumption and `O(r^4)` remainder.
3. Replace ambiguous `O_p` notation by explicit dependence on `p`.
4. Narrow the replay wording to its actual finite grid/seeds.

Recommended proof-strengthening sentences:

1. State exponential decay/all-moment integrability when differentiating the
   Fourier transform and deriving the refined large-`r` remainder.
2. State bounded eighth derivative when integrating the small-`r` Taylor
   remainder.
3. Record the analytic derivations of the logistic `M_4` and `M_5` bounds used
   by the script.

Subject to these minor revisions, the manuscript's algebraic and empirical
theorems are internally consistent and the new replay completes successfully.

## Appendix A. Differential verification of the four requested fixes

This appendix supersedes the four-item action list in Section 10 for the
updated files identified below.

Verification snapshot (2026-08-29, Europe/Stockholm):

- `src/main.tex`: SHA-256
  `CA16E3B1ADE04C046E629E2477F48499C5A1F10ABF5A33739316DC85DEBFC000`;
- `repro/verify_saturation_law.py`: SHA-256
  `8D7442D5487864C55F953DEBAF2576A8D18C7C23D336C6B26809EE79DE1C2A8E`;
- `repro/README.md`: SHA-256
  `7D59630505E42525826C30C24730BE00DA7A3849FCC972C4B8B30C7A6530BC16`.

**Final differential verdict: PASS. All four V5 fixes are implemented.**

1. **Moment scope fixed.** The bridge introduction now says that suitable
   moments suffice and explicitly distinguishes the fourth moment, which
   identifies `q_X`, from the sixth moment, which controls the `O(r^4)`
   remainder. The theorem retains `E||X||^6<infinity`, so prose and proof now
   agree.
2. **Ambiguous `O_p` fixed.** The abstract uses the explicit sufficient
   condition `n >= C_p r[d+log(1/delta)]/epsilon^2`, and the angle corollary
   uses a named computable constant `C'_p`. No literal `O_p` remains in the
   manuscript, verifier, or replay README.
3. **Typesetting typo fixed.** The Taylor display now contains `R_1,\quad`.
   A fresh `pdflatex -halt-on-error` build succeeds and no literal “quad” is
   printed in that equation.
4. **Replay scope fixed consistently in all three files.** The manuscript says
   grid monotonicity for `p=1,2` and three declared fixed seeds; the README says
   finite grids for `p=1,2` and three fixed seeds; and the verifier's PASS line
   reports “all-p moment/endpoint test points,” “p=1,2 anisotropy grids,” and
   “three fixed-seed empirical block realizations.” It no longer implies a
   numerical proof of the universal theorem or a probability-calibration
   experiment.

The updated verifier executes successfully and reproduces:

```text
figure_sha256=093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97
certificate_sha256=a5442d5840a08ed1394e21f8f4d82f7947ba35ba7bd6cc5e9cf00d4df0c3618a
```

No residual blocker remains among the four requested V5 corrections.
