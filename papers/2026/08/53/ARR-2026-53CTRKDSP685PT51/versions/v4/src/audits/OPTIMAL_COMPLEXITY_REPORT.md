# Optimal complexity of the logistic-weighted Gaussian Gram matrix

## Executive verdict

Let
\[
 \widehat H=\frac1n\sum_{i=1}^n h_p(rZ_i)X_iX_i^\top,
 \qquad X_i=(Y_i,Z_i)\sim N(0,I_{d-1})\otimes N(0,1),
 \qquad h_p=\sigma'^p,
\]
and let
\[
 H=\mathbb E\widehat H=\operatorname{diag}(\alpha I_{d-1},\beta),
 \quad \alpha\asymp_p r^{-1},\quad \beta\asymp_p r^{-3}.
\]

There is not one sample complexity until the target is specified.

1. **Bilateral relative Loewner approximation.** For fixed `p`, the existing upper scale
   \[
   n=O_p\!\left(\frac{r[d+\log(1/\delta)]}{\varepsilon^2}\right)
   \]
   is optimal up to constants. In particular, the product `rd` is genuinely necessary; it is not merely an artifact of the net argument in the manuscript. A complete lower-bound proof is given below. It uses the exact conditional Gaussian law of an off-diagonal column of the tangential block. Thus the statements in the v2 abstract, finite-sample discussion, and limitations section that a matching product lower bound is open are no longer correct for **bilateral relative Loewner loss**.

2. **Radial scalar entry.** Estimating
   \(c_n=n^{-1}\sum_i h_p(rZ_i)Z_i^2\) relative to \(\beta\) has dimension-free intrinsic scale
   \[
   n=\Theta_p(r/\varepsilon^2)
   \]
   at constant confidence. The manuscript's empty-slab argument supplies the sharp fixed-accuracy confidence obstruction \(r\log(1/\delta)\). The upper scalar Bernstein bound gives \(r\log(1/\delta)/\varepsilon^2\). The full matrix lower bound below already proves the latter confidence scale for the full Loewner problem, but this report does not claim a new all-parameter, nonasymptotic lower-tail theorem for the scalar mean alone.

3. **Ordinary smallest eigenvalue / radial eigenspace.** These are weaker targets than relative approximation of all tangential directions. A separate truncation argument proves that, at constant probability, preventing a spurious tangential Rayleigh quotient below \(\beta/2\) requires
   \[
   n=\Omega_p\!\left(\frac{rd}{\log r}\right)
   \]
   for large `r`. The current manuscript gives the upper bound `O_p(rd)` through a stronger relative-Loewner event. The logarithmic gap is real in the present proof record. I do **not** claim that `rd` is optimal for the sole task of recovering the bottom eigenspace.

The attached referee text named in the task was not present at the supplied local path; the mathematical question was nevertheless fully specified in the task and the v2 source.

## 1. Exact reduction and moment ratios

Write `m=d-1`, `W=h_p(rZ)`, and
\[
 C=\frac1n\sum_{i=1}^nW_iY_iY_i^\top,\qquad
 b=\frac1n\sum_{i=1}^nW_iZ_iY_i,\qquad
 c=\frac1n\sum_{i=1}^nW_iZ_i^2.
\]
Then
\[
 \widehat H=\begin{pmatrix}C&b\\b^\top&c\end{pmatrix},
 \qquad H=\begin{pmatrix}\alpha I_m&0\\0&\beta\end{pmatrix}.
\]
Define
\[
 A=\frac W\alpha,\qquad
 \rho=\mathbb EA^2=\frac{\mathbb EW^2}{\alpha^2}.
\]
If
\[
 m_0(q)=\int_{\mathbb R}\sigma'(s)^q\,ds,
\]
then scaled integration gives
\[
 \alpha=\frac{\varphi(0)}r\int h_p(s)e^{-s^2/(2r^2)}ds,
 \quad
 \mathbb EW^2=\frac{\varphi(0)}r\int h_{2p}(s)e^{-s^2/(2r^2)}ds.
\]
Consequently
\[
 \frac\rho r\longrightarrow
 c_p:=\frac{m_0(2p)}{\varphi(0)m_0(p)^2}>0.                       \tag{1}
\]
For an explicit finite-radius version, if
\[
 r^2\ge \max\{m_2(p)/m_0(p),m_2(2p)/m_0(2p)\},
\]
the elementary brackets already proved in v2 imply
\[
 \frac{m_0(2p)}{2\varphi(0)m_0(p)^2}r
 \le \rho\le
 \frac{4m_0(2p)}{\varphi(0)m_0(p)^2}r.                         \tag{2}
\]

We shall also need a kurtosis ratio. For `G~N(0,1)` independent of `A`, put `B=A^2G^2`. Then
\[
 \mathbb EB=\rho,\qquad
 \tau:=\frac{\mathbb EB^2}{\rho^2}
 =\frac{3\mathbb EW^4}{(\mathbb EW^2)^2}.
\]
The same brackets show, for all sufficiently large `r`,
\[
 \tau\le C_p^{(4)}r,
 \qquad
 C_p^{(4)}=\frac{12m_0(4p)}{\varphi(0)m_0(2p)^2}.              \tag{3}
\]

Equations (1)--(3) display the heteroscedastic effective sample size exactly: the normalized tangential observation has second moment of order `r`, not order one.

## 2. Matching lower bound for bilateral relative Loewner approximation

### Theorem 1 (product and confidence lower bounds)

Fix `p>0`. There are constants `R_p<infinity`, `c_p^*>0`, and `delta_p>0` such that, for all `r>=R_p`, `d>=3`, `0<epsilon<=1/2`, and `0<delta<=delta_p`,
\[
 \Pr\{(1-\varepsilon)H\preceq\widehat H\preceq(1+\varepsilon)H\}
 \ge1-\delta
\]
implies
\[
 n\ge c_p^*\frac{r[d+\log(1/\delta)]}{\varepsilon^2}.          \tag{4}
\]
For a fixed confidence smaller than a `p`-dependent numerical constant, the same argument gives
\[
 n=\Omega_p(rd/\varepsilon^2).                                 \tag{5}
\]

### Proof

Relative Loewner approximation of the full matrix implies its restriction to the tangential subspace:
\[
 \left\|M-I_m\right\|_{\rm op}\le\varepsilon,
 \qquad M:=\frac C\alpha=\frac1n\sum_{i=1}^nA_iY_iY_i^\top.  \tag{6}
\]
Fix the first coordinate in the tangential space and project the first column of `M-I` onto the remaining `k=m-1=d-2` coordinates:
\[
 D_j=e_j^\top(M-I)e_1
 =\frac1n\sum_{i=1}^nA_iY_{i1}Y_{ij},\qquad j=2,\ldots,m.
\]
Conditional on `(A_i,Y_{i1})_{i<=n}`, the vector `D=(D_2,...,D_m)` is exactly Gaussian,
\[
 D\mid(A,Y_1)\sim N(0,S I_k),
 \qquad
 S=\frac1{n^2}\sum_{i=1}^nA_i^2Y_{i1}^2.                     \tag{7}
\]
Put
\[
 T=\frac1n\sum_{i=1}^nA_i^2Y_{i1}^2,
\]
so `S=T/n`, `ET=rho`, and
\[
 \mathbb ET^2\le \rho^2(1+\tau/n).
\]
Paley--Zygmund therefore yields
\[
 \Pr\{T\ge\rho/2\}\ge\frac1{4(1+\tau/n)}.                 \tag{8}
\]
If `n>=a r` for any fixed `a>0`, (3) makes the right side a positive constant depending only on `(p,a)`.

Independently, if `Q~chi^2_k`, a second Paley--Zygmund application gives
\[
 \Pr\{Q\ge k/2\}\ge\frac{k}{4(k+2)}\ge\frac1{12}.          \tag{9}
\]
Combining (7)--(9), with probability at least a positive constant `q_{p,a}`,
\[
 \|M-I_m\|_{\rm op}\ge\|D\|_2
 \ge\sqrt{\frac{\rho(d-2)}{4n}}.                            \tag{10}
\]
Thus, whenever `delta<q_{p,a}`, (6) forces
\[
 n\ge\frac{\rho(d-2)}{4\varepsilon^2}
 \gtrsim_p\frac{rd}{\varepsilon^2}.                          \tag{11}
\]

It remains only to justify the harmless condition `n>=a r`. The empty-transition-slab lower bound already proved in v2 says
\[
 \Pr\{\lambda_{\min}(\widehat H)<\beta/2\}
 \ge\frac12e^{-C_p n/r}.                                     \tag{12}
\]
For `epsilon<=1/2`, the event in (12) contradicts the lower Loewner inequality. Hence success probability `1-delta` itself forces
\[
 n\ge C_p^{-1}r\log(1/(2\delta)).                             \tag{13}
\]
Choosing `delta_p` small enough makes (13) imply `n>=a r`; no circular assumption is being made.

For the confidence term, retain only `D_2`. On `{T>=rho/2}`, (7) and the elementary Gaussian lower-tail inequality
\[
 2\Phi(-x)\ge c_0e^{-x^2},\qquad x\ge0,                      \tag{14}
\]
give
\[
 \Pr\{|D_2|>\varepsilon\}
 \ge c_{p,a}\exp\left(-\frac{2n\varepsilon^2}{\rho}\right).\tag{15}
\]
Therefore failure probability at most `delta` requires
\[
 n\ge\frac\rho{2\varepsilon^2}\log(c_{p,a}/\delta)
 \gtrsim_p\frac r{\varepsilon^2}\log(1/\delta).             \tag{16}
\]
The maximum of (11) and (16) is at least half their sum, which proves (4). `square`

### Why this closes the v2 "open product" claim

The proof is self-contained and attacks the actual bilateral relative loss. It does not infer a product lower bound by multiplying the rank obstruction `n>=d` and the empty-slab obstruction `n>=r log(1/delta)`. Instead, the product appears in one random object: the conditional Gaussian column (7) has `d-2` coordinates and variance `rho/n asymptotic c_p r/n` per coordinate. This is precisely the heteroscedastic design mechanism requested by the referee.

The argument is pointwise at a fixed teacher and uses no labels or alternative parameter distributions. It is therefore a lower bound for the oracle empirical Gram matrix itself, not a minimax estimation lower bound.

### Constant audit via three elementary events

There is a slightly more explicit equivalent route to (10). Let `S_0=sum_i W_i^2`. Since `W<=H`,
\[
 \mathbb ES_0=n\gamma_0,
 \qquad
 \mathbb ES_0^2
 \le nH^2\gamma_0+n^2\gamma_0^2.
\]
Thus, if `n gamma_0>=H^2`,
\[
 \Pr\{S_0\ge n\gamma_0/2\}\ge1/8.                         \tag{17a}
\]
Conditional on the weights, `T_0=sum_iW_i^2Y_{i1}^2` has
\[
 \mathbb E(T_0\mid W)=S_0,
 \qquad
 \mathbb E(T_0^2\mid W)=S_0^2+2\sum_iW_i^4\le3S_0^2,
\]
so
\[
 \Pr\{T_0\ge S_0/2\mid W\}\ge1/12.                         \tag{17b}
\]
Finally, conditional on `(W,Y_1)`, the squared norm of the remaining off-diagonal column divided by `T_0/n^2` is `chi^2_{d-2}`, and
\[
 \Pr\{\chi^2_{d-2}\ge(d-2)/2\}\ge1/12.                     \tag{17c}
\]
The three events therefore intersect with probability at least `1/1152`, and on their intersection
\[
 \|C/\alpha-I\|_{\rm op}
 \ge\sqrt{\frac{(d-2)\gamma_0}{8n\alpha^2}}.                \tag{17d}
\]
The lower moment bracket gives directly
\[
 \frac{\gamma_0}{\alpha^2}
 \ge \frac{m_0(2p)}{2\varphi(0)m_0(p)^2}r.                  \tag{17e}
\]
This audits the numerical probability and the factor `1/8` in the threshold. The complementary case `n gamma_0<H^2` is `n=O_p(r)` and is covered by the empty-slab obstruction after choosing the fixed failure-probability constant consistently. The `T`/`tau` proof above is preferable for (15), because it retains the random variance needed for the confidence lower tail; (17a)--(17e) are preferable if only the constant-confidence product is wanted.

## 3. A direct smallest-generalized-eigenvalue obstruction

The preceding proof detects bilateral operator error. For completeness, a separate truncation gives a one-sided failure at constant accuracy and also explains the effective sample interpretation.

Choose a constant `a_p` so that
\[
 \int_{|s|>a_p}h_p(s)ds\le m_0(p)/32.                         \tag{17}
\]
Call an observation active when `|rZ_i|<=a_p`, and let `K` be the active count. Its probability satisfies
\[
 q_r\le2\varphi(0)a_p/r.
\]
If
\[
 n\le\frac{(d-1)r}{8\varphi(0)a_p},                          \tag{18}
\]
then `EK<=(d-1)/4`, hence `P(K<d-1)>=3/4`. On this event choose a unit tangential vector `v` orthogonal to all active `Y_i`. Conditional on the active observations, `v` is independent of the inactive tangential Gaussians. The expected inactive Rayleigh quotient is at most `E[W 1{|rZ|>a_p}]`, which, by (17) and the finite-radius lower bound on `alpha`, is at most `alpha/16`. Markov's inequality then gives, jointly with probability at least `5/8`,
\[
 v^TCv<\alpha/2.                                              \tag{19}
\]
Thus the smallest generalized eigenvalue of
`H^{-1/2} Hhat H^{-1/2}` is below `1/2`. This is an independent, genuinely one-sided `Omega_p(rd)` obstruction for constant relative accuracy.

It does **not** say that the ordinary smallest eigenvalue of `Hhat` is below `beta/2`, because `alpha/2` is much larger than `beta` in saturation.

## 4. Radial scalar: dimension-free complexity

Let
\[
 V=h_p(rZ)Z^2,\qquad \mathbb EV=\beta,
 \qquad \nu^2=\operatorname{Var}(V).
\]
Scaled integration gives, as `r->infinity`,
\[
 \beta\sim\frac{\varphi(0)m_2(p)}{r^3},\qquad
 \nu^2\sim\frac{\varphi(0)m_4(2p)}{r^5}.                    \tag{20}
\]
Hence
\[
 \frac{\nu^2}{\beta^2}\asymp_p r.                           \tag{21}
\]
Moreover, with `mu_4=E(V-beta)^4`, the eighth scaled moment gives
\[
 \frac{\mu_4}{\nu^4}=O_p(r).                                \tag{22}
\]
For `S_n=sum_i(V_i-beta)`,
\[
 \mathbb ES_n^2=n\nu^2,
 \qquad
 \mathbb ES_n^4=n\mu_4+3n(n-1)\nu^4.
\]
Applying Paley--Zygmund to `S_n^2`, (22) shows that for `n>=C_p r`, with probability at least a `p`-dependent constant,
\[
 \left|\frac1n\sum_iV_i-\beta\right|
 \ge \sqrt{\frac{\nu^2}{2n}}
 \asymp_p\beta\sqrt{\frac rn}.                              \tag{23}
\]
Together with the empty-slab obstruction for `n<C_p r`, this proves the constant-confidence necessity
\[
 n=\Omega_p(r/\varepsilon^2)                                 \tag{24}
\]
for sufficiently small fixed `epsilon`, matching the scalar part of the manuscript's Bernstein upper bound.

No dimension factor belongs to the radial entry alone. The factor `d` in Theorem 1 comes from simultaneously controlling the tangential covariance, not from estimating `beta`.

For confidence dependence, v2 already proves `Omega_p(r log(1/delta))` at fixed relative accuracy from an empty slab. A sharp all-`epsilon`, all-`delta` scalar lower tail would require a separate binomial/moderate-deviation lemma for the localized nonnegative summands. It is unnecessary for the full matrix conclusion because (15) proves the sharp `r epsilon^{-2} log(1/delta)` term there.

## 5. Ordinary smallest eigenvalue and bottom eigenspace

The ordinary bottom eigenvalue is `beta`, not `alpha`. Therefore the constant-slab proof (19) is insufficient. Enlarging the slab to logarithmic width yields a rigorous different obstruction.

### Proposition 2 (spurious tangential mode below the radial scale)

Fix `p>0` and put
\[
 t_r=\frac4p\log r.
\]
For all sufficiently large `r`, if
\[
 n\le c_p\frac{r(d-1)}{\log r},                              \tag{25}
\]
then with probability bounded below by a positive universal constant,
\[
 \lambda_{\min}(\widehat H)\le\lambda_{\min}(C)<\beta/2.  \tag{26}
\]

### Proof

Call an observation active when `|rZ_i|<=t_r`. Since
\[
 q_r\le2\varphi(0)t_r/r=\frac{8\varphi(0)}p\frac{\log r}{r},
\]
a sufficiently small constant in (25) makes the expected active count at most `(d-1)/4`; Markov gives `P(K<d-1)>=3/4`. On that event take a unit tangential `v` orthogonal to all active `Y_i`.

For every inactive sample,
\[
 W_i=h_p(rZ_i)\le e^{-p|rZ_i|}\le e^{-pt_r}=r^{-4}.           \tag{27}
\]
Conditional on the active data and the inactive `Z_i`, the inactive projections `v^TY_i` are independent standard Gaussians. Markov's inequality for their chi-square sum gives conditional probability at least `1/2` that
\[
 v^TCv\le r^{-4}\frac1n\sum_{i\notin A}(v^TY_i)^2\le2r^{-4}.\tag{28}
\]
On the other hand, the v2 finite-radius bracket gives
\[
 \beta\ge\frac{\varphi(0)m_2(p)}{2r^3}                      \tag{29}
\]
for large `r`. Equations (28)--(29) imply `v^TCv<beta/2` once `r>=8/[varphi(0)m_2(p)]`. The Rayleigh principle proves (26). `square`

This proposition establishes a necessary `rd/log r` scale for avoiding an ordinary tangential eigenvalue below the population radial eigenvalue. It also shows why rank alone is a very weak obstruction.

It does not, by itself, prove a quantitative lower bound on the angle of one arbitrarily tie-broken smallest eigenvector: (26) proves spectral non-resolution, while a vector-angle statement must additionally control the cross block and the multiplicity/spacing of the low tangential modes. The manuscript's current sufficient event gives `O_p(rd)` for this stronger task. Closing
\[
 \Omega_p(rd/\log r)\quad\text{versus}\quad O_p(rd)          \tag{30}
\]
for bottom-eigenspace recovery remains a legitimate next problem. It must not be conflated with Theorem 1, which already closes the bilateral relative-Loewner complexity.

In the perturbative regime where the empirical tangential gap is already known to be healthy, the conditional law
\[
 b\mid Z\sim N\left(0,\frac{\sum_iW_i^2Z_i^2}{n^2}I_{d-1}\right)
\]
has typical size `sqrt(d/(n r^3))`; division by the population gap `alpha asymptotic r^{-1}` gives the angle scale
\[
 \sqrt{\frac d{nr}}.                                         \tag{31}
\]
This is a conditional perturbative scale, not a global sample threshold: before (31) is usable one must prevent the spurious low tangential modes described by Proposition 2.

## 6. Relation to primary literature

- Chardon, Lerasle and Mourtada, [*Finite-sample performance of the maximum likelihood estimator in logistic regression*](https://arxiv.org/abs/2411.02137), prove a sharp Gaussian **one-sided uniform empirical-Hessian lower bound** (their Theorem 6). Their sufficient scale `n` proportional to signal strength times dimension is consistent with the effective-transition-layer mechanism. It does not supply the pointwise bilateral lower bound proved here.
- Ostrovskii and Bach, [*Finite-sample analysis of M-estimators using self-concordance*](https://doi.org/10.1214/20-EJS1780), prove bilateral empirical-Hessian comparisons in their self-concordant analysis. This is relevant upper-bound context, not a lower-bound result for the present weighted oracle Gram matrix.
- Koltchinskii and Lounici, [*Concentration Inequalities and Moment Bounds for Sample Covariance Operators*](https://arxiv.org/abs/1405.2468), identify the sharp `sqrt(effective-rank/n)` covariance-deviation mechanism for Gaussian sample covariance. Their observations are Gaussian with a fixed covariance, whereas `sqrt(W)Y` here is a heteroscedastic Gaussian scale mixture. Their theorem therefore cannot simply be quoted to obtain Theorem 1; the conditional calculation (7) is the needed model-specific proof.
- Koltchinskii and Lounici, [*Asymptotics and Concentration Bounds for Bilinear Forms of Spectral Projectors of Sample Covariance*](https://arxiv.org/abs/1408.4643), treat spectral-projector fluctuations for Gaussian covariance models. Again, it is useful context for distinguishing covariance loss from eigenspace loss, but it does not close the heteroscedastic bottom-eigenspace gap (30).

All arguments above are independent of those papers and are included in full because none of the cited Gaussian-covariance theorems directly covers the dependence of the row scale `W=h_p(rZ)` on the radial coordinate of the same observation.

## 7. Required manuscript changes implied by this report

This report did not edit `main.tex`, as requested. A future revision should make the following mathematical changes.

1. Replace every statement that a matching product lower bound remains open by Theorem 1, explicitly limiting the claim to bilateral relative Loewner approximation.
2. Keep the rank and empty-slab bounds as useful elementary obstructions, but do not present them as the strongest known lower bound after Theorem 1.
3. Separate three targets in the abstract and limitations: full relative Loewner, radial scalar estimation, and bottom-eigenspace recovery.
4. Do not claim an optimal `rd` threshold for the bottom eigenvector. The rigorous present bracket is (30), while its perturbative angle scale is (31).
5. If the paper adds only one new theorem, Theorem 1 is proof-complete, matches the existing upper theorem, and resolves exactly the referee's optimal-complexity request.

## Final assessment

**The referee's product-complexity request is viable and can be answered completely for bilateral relative Loewner approximation:**
\[
 \boxed{n_{\rm Loewner}=\Theta_p\!\left(\frac{r[d+\log(1/\delta)]}{\varepsilon^2}\right)}.
\]

The answer is not additive `r+d`; the heteroscedastic second-moment ratio `rho asymptotic c_p r` multiplies the `d` tangential Gaussian coordinates. The same formula should not be exported unqualified to the radial scalar or the bottom eigenspace. For those targets the established scales are respectively `Theta_p(r/epsilon^2)` at constant confidence and the unresolved bracket `Omega_p(rd/log r)` versus `O_p(rd)` for robust bottom-mode resolution.
