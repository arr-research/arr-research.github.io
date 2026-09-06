# Two-state exact routing: algebraic feasibility and sharp delay-two rigidity

Lluis Eriksson

ARR v1 - ARR-2026-03PY6WTF258KGSRN. 6 September 2026.

## Abstract

Consider lossless rational-inner matrices of McMillan degree at most two that route one input to one output ray at two prescribed boundary frequencies and to an orthogonal ray at a third frequency. We give an exact three-real-parameter description of every achievable determinant delay, independent of the number of ports. A global peak-delay cap is equivalent to positivity of one explicit quartic and one quadratic; the quartic admits a three-by-three positive-semidefinite certificate. The winding lower bound of two is attained exactly when the two repeated-target frequencies are symmetric about the exceptional frequency and their angular gaps are at least a right angle. We prove a quantitative positive gap outside this locus. For symmetric acute gaps we give a cubic-root construction with an exact quartic-square peak certificate, strictly improving the elementary double-pole construction. Its unrestricted optimality remains open. The results distinguish complete feasibility and sharp rigidity from an unproved numerical optimum.

## 1. Model and statements

Let $S$ be an $N\times N$ rational-inner matrix analytic in the unit disk, with $N\geq2$ and McMillan degree at most two. Fix one unit input vector and let $f$ denote its output column. At the three nodes require

\[
f(1)\in\mathbb C e_2,\qquad f(e^{-ia}),f(e^{ib})\in\mathbb C e_1,
\qquad 0<a,b<\pi.
\]

These are exact ray conditions: all three output vectors have norm one and their phases are free. The cost is the dimensionless angular trace-delay peak

\[
\mathcal T(S)=\max_\phi\operatorname{tr}\left[-iS(e^{i\phi})^*
\frac{dS(e^{i\phi})}{d\phi}\right].
\tag{1}
\]

Write $\mathcal T_2(a,b)$ for its minimum over exact routers of degree at most two. Set

\[
u=\cot(a/2),\quad v=\cot(b/2),\quad
m=\frac{v-u}{2},\quad d=\frac{u+v}{2}>0.
\tag{2}
\]

The coordinate $s=\cot(\phi/2)$ sends the nodes to $\infty,-u,v$; put $t=s-m$. The two finite nodes are $t=-d,d$. The angular factor $1+(t+m)^2$ will be retained throughout; translating $t$ does not preserve the original peak-delay cost.

**Theorem A (complete algebraic feasibility).** Choose real $V,Y,K$ and define

\[
A=Y^2-2V+2d^2,\quad B=Y^2K,\quad
C=V^2+Y^2K^2-d^4.
\tag{3}
\]

The admissible parameter set is exactly

\[
Y>0,\qquad V>K^2,\qquad
\begin{pmatrix}A&B\\B&C\end{pmatrix}\succeq0.
\tag{4}
\]

Every such triple is realized by a two-port exact router. Conversely, every exact router of degree at most two, in any number of ports, has the same trace-delay function as a triple satisfying (4). That function is

\[
\tau(t)=
\frac{Y[1+(t+m)^2](t^2+2Kt+V)}
{(t^2-V)^2+Y^2(t+K)^2},\qquad \tau(\infty)=Y.
\tag{5}
\]

Thus a cap $T$ is feasible if and only if there are parameters satisfying (4) for which the explicit quartic

\[
R_T(t)=T\bigl[(t^2-V)^2+Y^2(t+K)^2\bigr]
-Y[1+(t+m)^2](t^2+2Kt+V)
\tag{6}
\]

is nonnegative on the entire real line. Feasibility includes the point at infinity through the leading coefficient $T-Y$.

**Theorem B (sharp winding-bound rigidity).** The minimum exists, is finite, and is independent of $N\geq2$. Moreover,

\[
\mathcal T_2(a,b)=2
\quad\Longleftrightarrow\quad
a=b\geq\frac{\pi}{2}.
\tag{7}
\]

At every other fixed table the minimum is strictly greater than two.

Theorem C below gives an explicit positive gap in (7). Proposition D supplies a certified acute-gap construction. Neither Theorem A nor numerical optimization of its three parameters is asserted to give a closed formula for the general minimum.

## 2. Exact reduction to a quadratic spectral factor

We first prove Theorem A. The classical ingredients are rational-inner realization and Blaschke–Potapov factorization; their conventions are discussed in Section 8.

**Planarity and degree.** A common realization denominator of a degree-at-most-two matrix gives polynomial coordinate numerators of degree at most two for $f$. Every component orthogonal to $\operatorname{span}(e_1,e_2)$ vanishes at the three distinct nodes and therefore vanishes identically. After removal of common factors, the first two numerators form a primitive projective polynomial pair. The second numerator has the two repeated-target zeros, while the first has the exceptional zero and is nonzero at the other two nodes. Consequently their projective degree is exactly two. In particular, no degree-zero or degree-one router can solve the table, and every exact router under consideration uses exactly two states.

In the lower-half-plane coordinate $s=i(z+1)/(z-1)$, and then $t=s-m$, the routed column can therefore be written

\[
f(t)=\frac{1}{h(t)}\begin{pmatrix}p(t)\\q(t)\end{pmatrix},
\qquad q(t)=t^2-d^2,\qquad \deg p\leq1.
\tag{8}
\]

Multiplication of the column by a constant phase normalizes the leading coefficient of $h$ to one. A constant output phase normalizes that of $q$ to one. These normalizations are compatible because $f(\infty)$ has unit norm. The scalar denominator $h$ has both zeros in the upper half-plane, and

\[
|h(t)|^2=q(t)^2+|p(t)|^2\quad(t\in\mathbb R).
\tag{9}
\]

The cubic coefficient on the right is zero. Thus the real part of the linear coefficient of monic $h$ is zero, and we may write uniquely

\[
h(t)=t^2-V-iY(t+K),\qquad V,Y,K\in\mathbb R.
\tag{10}
\]

The upper-half-plane root condition is equivalent to $Y>0$ and $V>K^2$. Here is a direct proof. If the two roots are $r+i\eta_1$ and $-r+i\eta_2$, with positive $\eta_j$, comparison gives $Y=\eta_1+\eta_2$ and

\[
V-K^2=\eta_1\eta_2
\left(1+\frac{4r^2}{(\eta_1+\eta_2)^2}\right)>0.
\]

Conversely, the region $Y>0,V>K^2$ is connected. A root on the real axis would have to equal $-K$ and satisfy $V=K^2$, which is excluded. At $K=0$ both roots of $t^2-iYt-V$ lie in the upper half-plane. Continuity, including coincident roots, proves the converse throughout the region.

Subtracting $q^2$ from $|h|^2$ gives

\[
|p(t)|^2=At^2+2Bt+C,
\tag{11}
\]

with (3). A real quadratic is nonnegative exactly when its two-by-two coefficient matrix is positive semidefinite. Conversely, every such quadratic is the squared modulus of one complex linear polynomial: if $A>0$, take

\[
p(t)=\sqrt A\,t+\frac B{\sqrt A}
+i\sqrt{C-\frac{B^2}{A}};
\tag{12}
\]

if $A=0$, positivity forces $B=0$ and one takes $p=\sqrt C$. Since $h$ has no real zero, (9) makes $p(\pm d)\ne0$. Hence this reconstruction serves all three nodes and has no common numerator zero.

For a polynomial $g$ write $g^*(t)=\overline{g(\bar t)}$. An explicit square completion is

\[
S_2(t)=\frac1{h(t)}
\begin{pmatrix}p(t)&-q(t)\\q(t)&p^*(t)\end{pmatrix}.
\tag{13}
\]

Its columns are orthonormal on the real line and its determinant is $h^*/h$. It is analytic in the lower half-plane, regular at the boundary point corresponding to infinity, and has degree exactly two. An identity block embeds it in every larger port space.

**Pole exhaustion.** The primitive column in (8) has McMillan degree two: the quadratic denominator has no cancellation common to both numerators. In a minimal realization of any containing matrix, restricting the input to this column can only decrease each pole multiplicity. The column already has total pole multiplicity two, equal to the allowed matrix degree. Therefore those multiplicities agree at every pole, including a repeated pole. For a square rational-inner matrix, the determinant has precisely the same pole multiplicities as its McMillan pole data. This follows by taking determinants in a minimal Blaschke-Potapov product; see Alpay, Jorgensen and Lewkowicz, Theorem 3.1, with their exterior-disk convention converted to the interior convention used here. Hence the determinant is, up to a constant phase, $h^*/h$, as in (13), and the trace delays agree. Differentiating this quotient and using $dt/d\phi=-[1+(t+m)^2]/2$ gives exactly (5). Its denominator is strictly positive and its numerator is positive because $t^2+2Kt+V=(t+K)^2+V-K^2$. This proves Theorem A.

**A useful necessary inequality.** Every admissible triple satisfies $V\geq d^2$. Indeed

\[
AC-B^2=(V-d^2)
\left[Y^2(V+d^2-2K^2)-2(V^2-d^4)\right].
\tag{14}
\]

If $V<d^2$, then $V>K^2$ makes the bracket strictly positive, contradicting positive semidefiniteness. At $V=d^2$, (11) is the single square $Y^2(t+K)^2$. For $V>d^2$, (4) can equivalently be written

\[
Y>0,\qquad K^2<\frac{V+d^2}{2},\qquad
Y^2\geq\frac{2(V^2-d^4)}{V+d^2-2K^2}.
\tag{15}
\]

In (15), $A,C\geq0$ follow from the displayed bound, and stability follows from $K^2<(V+d^2)/2<V$. This alternative parametrization is useful for numerical searches without accepting points with negative residual power.

## 3. Finite exact certificates and attainment

Write $R_T(t)=\sum_{j=0}^4r_jt^j$. Its coefficients are

\[
r_4=T-Y,\qquad r_3=-2Y(K+m),
\]
\[
r_2=T(Y^2-2V)-Y(V+4mK+m^2+1),
\]
\[
r_1=2TY^2K-2Y[mV+K(m^2+1)],
\]
\[
r_0=T(V^2+Y^2K^2)-YV(m^2+1).
\tag{16}
\]

A univariate nonnegative quartic is a sum of squares of polynomials of degree at most two. Equivalently, for some real $\lambda$,

\[
G_\lambda=
\begin{pmatrix}
r_0&r_1/2&\lambda\\
r_1/2&r_2-2\lambda&r_3/2\\
\lambda&r_3/2&r_4
\end{pmatrix}\succeq0.
\tag{17}
\]

The identity is $R_T=(1,t,t^2)G_\lambda(1,t,t^2)^T$. The reverse implication follows by factoring a nonnegative real polynomial into real even-multiplicity roots and conjugate pairs, representing it as $|g(t)|^2$, and taking real and imaginary parts of $g$.

Equations (3), (4), and (16)–(17) give a finite exact feasibility certificate using two matrices of orders two and three and four auxiliary real variables $V,Y,K,\lambda$. The constraints are polynomial but are not jointly convex in these parameters. A floating-point feasible status or a frequency grid is not an exact certificate.

For rational $u,v$, feasibility is a first-order formula over the real algebraic numbers. Quantifier elimination therefore determines it exactly in principle. The finite minimum $\mathcal T_2$ is itself algebraic for such data: its feasible set of caps is a semialgebraic upper ray with an attained finite endpoint. This observation is an exact computability statement, not an efficient complexity bound or a practical general optimizer.

To see finite feasibility directly, set $V=d^2$, $K=0$, and $Y=2d$. Then $h=(t-id)^2$ and $p=2dt$ in (13). If

\[
P_0=\frac{1+m^2+d^2}{2d},
\]

its peak is

\[
\mathcal T_{\rm dbl}=2\left(P_0+\sqrt{P_0^2-1}\right).
\tag{18}
\]

Indeed the determinant has a double disk zero of modulus
$\sqrt{[m^2+(d-1)^2]/[m^2+(d+1)^2]}$; (18) is twice the peak of its Poisson kernel.

For completeness, attainment uses a compactness argument. Every degree-two inner determinant has two disk zeros $\alpha_1,\alpha_2$ and

\[
\tau(\phi)=\sum_{j=1}^2
\frac{1-|\alpha_j|^2}{|e^{i\phi}-\alpha_j|^2}.
\tag{19}
\]

A finite cap bounds each zero strictly away from the unit circle, because each nonnegative summand has peak $(1+|\alpha_j|)/(1-|\alpha_j|)$. In a Blaschke–Potapov representation, the two rank-one directions and the constant unitary matrix also range over compact spaces. The family under a fixed cap is compact and evaluation at the three nodes is continuous. Starting with (18), any minimizing sequence has a convergent exact degree-at-most-two subsequence. Its limit remains exact and hence has degree two. This proves attainment. Theorem A then proves that the attained minimum is the same in every port dimension.

## 4. Rigidity at the winding bound

The mean of (19) is two, so $\mathcal T_2\geq2$. If the peak equals two, its continuous nonnegative delay must be identically two. The Fourier expansion of (19) gives

\[
\alpha_1+\alpha_2=0,\qquad
\alpha_1^2+\alpha_2^2=0,
\]

and therefore both zeros vanish. The denominator of the routed column is consequently constant in the disk coordinate. Its second polynomial component must be

\[
q_z(z)=c_0(z-e^{-ia})(z-e^{ib}).
\tag{20}
\]

Since $|q_z(1)|=1$ and $|q_z|\leq1$ on the circle, its modulus must have a global maximum at $z=1$. Put

\[
\alpha=\frac{a+b}{2},\qquad \beta=\frac{b-a}{2}.
\]

Direct multiplication gives

\[
|(e^{i\phi}-e^{-ia})(e^{i\phi}-e^{ib})|
=2|\cos(\phi-\beta)-\cos\alpha|.
\tag{21}
\]

Its maximum is $2(1+|\cos\alpha|)$, whereas its value at zero is
$2(\cos\beta-\cos\alpha)>0$. Equality of these two quantities holds exactly when $\beta=0$ and $\cos\alpha\leq0$, namely $a=b\geq\pi/2$.

Conversely, in this symmetric range $m=0$ and $0<d\leq1$. Choose

\[
V=1,\quad Y=2,\quad K=0,\quad
h=(t-i)^2,\quad q=t^2-d^2,
\]
\[
p(t)=\sqrt{2+2d^2}\,t+i\sqrt{1-d^4}.
\tag{22}
\]

Then $|h|^2=q^2+|p|^2$ and (5) is identically two. This is a two-port exact router. The preceding attainment argument turns the obstruction outside this range into strict inequality for the minimum, and proves Theorem B.

The full complex linear factor in (22) matters. Restricting every router to a balanced pair built from a single scalar Blaschke product would discard part of this attainment region.

## 5. A quantitative gap outside the attainment locus

Define the normalized numerator overshoot

\[
M(a,b)=\frac{1+|\cos\alpha|}{\cos\beta-\cos\alpha}\geq1,
\qquad \eta=\frac{M-1}{M+1}\in[0,1).
\tag{23}
\]

**Theorem C (explicit winding gap).** For every table in the model,

\[
\mathcal T_2(a,b)\geq
2+\frac{\sqrt{9+8\eta}-3}{2}.
\tag{24}
\]

The added term is positive exactly outside $a=b\geq\pi/2$. Its numerical constant is not asserted to be optimal.

**Proof.** Consider any exact router with peak $2+\varepsilon$. The nonnegative function $2+\varepsilon-\tau$ has mean $\varepsilon$. Each of its nonconstant Fourier coefficients consequently has modulus at most $\varepsilon$. From (19),

\[
|\alpha_1+\alpha_2|\leq\varepsilon,\qquad
|\alpha_1^2+\alpha_2^2|\leq\varepsilon.
\]

It follows that

\[
|\alpha_1\alpha_2|\leq\frac{\varepsilon^2+\varepsilon}{2}.
\]

Normalize the stable disk denominator to
$h_z(z)=(1-\bar\alpha_1z)(1-\bar\alpha_2z)$. Uniformly on the circle,

\[
|h_z(z)-1|\leq r,
\qquad r=\frac{\varepsilon^2+3\varepsilon}{2}.
\tag{25}
\]

The normalized maximum of the numerator in (20) is $M$. Exact service at 1 and the contractive component bound imply

\[
M\leq\frac{\max_{|z|=1}|h_z(z)|}{|h_z(1)|}.
\]

If $r<1$, this is at most $(1+r)/(1-r)$, so $r\geq\eta$. If $r\geq1$, the same conclusion is automatic because $\eta<1$. Solving $\varepsilon^2+3\varepsilon\geq2\eta$ proves (24).

There is also a useful geometric lower bound

\[
\mathcal T_2(a,b)\geq\max\left\{2,\frac\pi a,\frac\pi b\right\}.
\tag{26}
\]

Indeed the Wigner–Smith matrix of a disk-inner response is positive semidefinite by its Potapov factorization. The Fubini–Study speed of a unit output column is the standard deviation of that matrix in the input state, at most half its spectral range and therefore at most half its trace. Traversing between orthogonal rays over an angular interval of length $a$ or $b$ requires Fubini–Study length at least $\pi/2$. Integration proves (26). When $\pi/a>2$ or $\pi/b>2$, equality in the corresponding bound is impossible: it would force the analytic delay to be constant at its peak on a nonempty arc and hence everywhere, contradicting its mean two. This strictness also applies to the attained minimum.

## 6. A certified improvement for symmetric acute gaps

Assume now $a=b<\pi/2$, so $m=0$ and $d=u=v>1$. Write $w=d^2>1$.

**Proposition D (cubic-root upper bound).** Let $x>w$ be the unique root of

\[
x^3-(4w+1)x^2-(w^2+4w)x+w^2=0.
\tag{27}
\]

Set

\[
V=w,\quad K=0,\quad
Y=\frac{x-w}{\sqrt x},\qquad
T_* =\frac{(x+1)(x+w)}{2\sqrt x(x-w)}.
\tag{28}
\]

These parameters give an exact router whose global peak is $T_*<2d$. Therefore

\[
\mathcal T_2(a,a)\leq T_*<2\cot(a/2).
\tag{29}
\]

The two equal peaks occur at $t=\pm\sqrt x$. This proposition is an upper-bound theorem, not a classification of the unrestricted minimizers.

**Proof.** Substituting $x=w+z$ in the left side of (27) gives

\[
z^3-(w+1)z^2-6w(w+1)z-4w^2(w+1).
\]

Its coefficient signs have exactly one variation and its constant term is negative, so it has precisely one positive root. This proves the stipulated uniqueness. Put $r=x/w$. Equation (27) is equivalently

\[
w=\frac{r^2+4r-1}{r(r^2-4r-1)}.
\tag{30}
\]

On $2+\sqrt5<r\leq3+2\sqrt2$, the right side decreases from infinity to one, since its derivative is

\[
-\frac{(r-1)^2(r^2+10r+1)}{r^2(r^2-4r-1)^2}<0.
\]

Hence $w>1$ corresponds to the strict interior of this interval. In particular $T_*>Y>0$. Substitution in (6), followed by reduction using (27), gives the exact identity

\[
R_{T_*}(t)=(T_*-Y)(t^2-x)^2.
\tag{31}
\]

It proves the cap globally, and its real zeros prove actual attainment of that peak. The routing conditions follow from $V=w$, $K=0$, for which $|p|^2=Y^2t^2$ and stability holds.

Finally (30) gives

\[
4w-T_*^2=
-\frac{(r^2-6r+1)(r^3+6r^2+9r-4)}
{r(r^2-4r-1)(r^2+4r-1)}>0
\tag{32}
\]

on the stated interval. This proves the strict improvement in (29). The limit at $w=1$ is $T_*=Y=2$, consistently with (7).

**An exact fixture.** Take $w=11/5$, for which $r=5$ and $x=11$. Then

\[
Y=\frac{4\sqrt{11}}5,\qquad T_* =\frac9{\sqrt{11}},
\qquad
R_{T_*}(t)=\frac{(t^2-11)^2}{5\sqrt{11}}.
\tag{33}
\]

This reduces the elementary upper bound $2\sqrt{11/5}$ by about 8.52 percent and supplies an exact global positivity certificate, not a sampled frequency estimate. For $d=2$, the same construction gives $T_*=3.51741499359\ldots$, below the elementary bound four.

Exploratory optimization of the full three-parameter feasible set at seven symmetric acute tables returned values consistent with (28), with $V$ tending to $d^2$ and $K$ tending to zero. That observation motivated (27). It does not prove that nonsymmetric denominators or $V>d^2$ cannot improve (28). Resolving that exclusion is an explicit remaining problem.

## 7. Reproducible verification and limits

The companion exact verifier checks the general coefficient identities (3), (5), (14), and (16), the completion identity, the quartic Gram identity, the degree-two winding construction, and the parameterized certificate (31). Rational and radical fixtures cover both sides of the right-angle boundary, symmetric acute designs, and genuinely asymmetric tables. A separate exploration file records the numerical searches and is not used by the proof verifier.

The algebraic identities are universal symbolic checks. Exact fixtures test implementations and signs; they do not replace the universal arguments in Sections 2–6. The work is not a formal proof-assistant development, and internal review is separate from external refereeing. The companion review records its own scope and source hashes.

The model retains exactly two states, three nodes, orthogonal targets, free endpoint phases, and the angular trace-delay peak. It does not cover a physical time calibration, dissipation, fixed phases, arbitrary additional nodes, or higher-degree minimax laws. The global acute optimum and the general asymmetric minimum remain open despite the complete finite feasibility description.

## 8. Antecedents and contribution boundary

[Eriksson, *Projective Memory and Resonant Bottlenecks in Passive Spectral Routing*, ARR-2026-6M3VGTXZ6W8JW9C9](https://arr-research.github.io/papers/ARR-2026-6M3VGTXZ6W8JW9C9/) already proves the projective state law, two-state exact existence for this binary table, and compactness under a finite peak cap. Its proof supplies the three-node planarity argument and the compactness mechanism used here. Those state-count and compactness facts are not new claims.

[Eriksson, *A complete one-state error–delay law for asymmetric three-node routing*, ARR-2026-4NC14QTZMT8708NN](https://arr-research.github.io/papers/ARR-2026-4NC14QTZMT8708NN/) solves the degree-at-most-one positive-error problem and its inverse; it explicitly excludes degree two. The present note studies exact service after adding the second state. It neither alters that published law nor presents its one-state inverse as new.

[Alpay, Jorgensen and Lewkowicz, *Characterizations of rectangular (para)-unitary rational functions*, arXiv:1410.0283v2](https://arxiv.org/abs/1410.0283) supplies classical lossless realization, completion, and Potapov structure. [Bolotnikov, *Boundary interpolation by finite Blaschke products*, arXiv:1609.09843](https://arxiv.org/abs/1609.09843) is a direct antecedent for scalar boundary interpolation with degree restrictions; the present phase-free vector-routing constraints and global derivative cap form a different specification.

[Appaiah and Pal, *All-Pass Filter Design Using Blaschke Interpolation*, IEEE Signal Processing Letters 27 (2020), 226-230](https://doi.org/10.1109/LSP.2020.2965318) addresses exact scalar phase interpolation and the tuning or optimization of group delay at the interpolation nodes. This comparison is based on the [institutional abstract and metadata](https://dspace.library.iitb.ac.in/jspui/handle/100/34432); the full text was not available for this review.

[Bharath, Gaharwar, Appaiah and Pal, *Design of Discrete-time Matrix All-Pass Filters Using Subspace Nevanlinna Pick Interpolation*, Signal Processing 204 (2023), 108839](https://arxiv.org/abs/2210.14015) interpolates prescribed unitary matrices. Section 4.4 minimizes the sum of traces of the group-delay matrices at the specified nodes through a Pick-matrix formulation. Our constraints prescribe output rays of one column with free phases, fix the degree at two, and cap trace delay over the entire circle. These differences specify the problem addressed here; they do not constitute a proof of bibliographic priority.

[Kovalev and Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760](https://arxiv.org/abs/2007.09760) studies the joint minimum and maximum of a Blaschke derivative. Its winding average, Poisson expansion, and extremal derivative framework are directly relevant classical context. Their extremal problem does not impose the three routing conditions used here. The elementary two-Fourier-coefficient argument in Section 5 is included in full.

Global nonnegative power-polynomial design and spectral factorization have a further antecedent in [Wu, Boyd and Vandenberghe, *FIR Filter Design via Semidefinite Programming and Spectral Factorization*](https://web.stanford.edu/~boyd/papers/magdes.html). A small Gram matrix or a polynomial positivity conversion is not itself claimed as a new general method. The specific deductions here are the complete parameters (3)–(6), the sharp locus (7), the geometry-dependent gap (24), and the attainable cubic certificate (27)–(33).

This is a bounded source comparison. It does not establish worldwide bibliographic priority. Lluis Eriksson directed the research programme; OpenAI Codex assisted with derivation, computation, source comparison, and drafting. The author authorized publication of this version.
