# A complete one-state error–delay law for asymmetric three-node routing

Lluis Eriksson — research manuscript, 5 September 2026.

This manuscript closes the positivity-active case left open in the local cycle-2 calculation. It supplies an explicit phase boundary, a two-branch exact minimax law, positive lower certificates and a two-port compiler. The results are new relative to that inspected local calculation. External priority is not established. A separate internal review is recorded alongside this manuscript; it is distinct from the deriving agent's replay and is not external refereeing.

## 1. Model and complete statement

Let S be an N by N rational-inner matrix on the unit disk, N>=2, of McMillan degree at most one. Fix one input unit vector. At each specified node the output phase is free, and the error from a target unit vector y is the chordal distance $\sqrt{1-|\langle y,f\rangle|^2}$. The peak constraint is the dimensionless angular trace delay

\[
D(S)=\sup_\phi\mathrm{tr}\left[-iS(e^{i\phi})^*\frac{dS(e^{i\phi})}{d\phi}\right]\leq T.
\]

The targets are e2 at $z=1$ and e1 at $z=e^{-ia},e^{ib}$, where $0<a,b<\pi$. Put $u=\cot(a/2)>0$ and $v=\cot(b/2)>0$. Denote the minimum worst-node squared error by $e_{\mathrm{opt}}(u,v,T)$. Reflection exchanges u and v and preserves the constraint, so in the formulas below arrange $u\geq v$. Reflect the final quadratic coordinate s back if the original $u<v$.

For $T\geq 1$ define

\[
p=\frac{T+T^{-1}}{2},\qquad q=\frac{T-T^{-1}}{2},
\]

\[
A(t)=\left(\sqrt{t^2+p^2}+q\right)^2,\qquad D(t)=(u+t)(v-t),\quad -u<t<v.
\]

There is a unique minimizer t_* of $F(t)=A(t)/D(t)$. It is zero for $u=v$ and lies in $((v-u)/2,0)$ for u>v. It is the unique root in that interval of

\[
2tD(t)=\sqrt{t^2+p^2}\left(\sqrt{t^2+p^2}+q\right)(v-u-2t).\tag{1}
\]

For $q^2>2v^2$ set

\[
w=\sqrt{q^2-v^2},
\]

\[
U_c(v,q)=v\frac{q^2+2pw}{q^2-2v^2}.\tag{2}
\]

**Theorem 1 (complete two-branch law).** For every u,v>0 and every port count N>=2,

\[
e_{\mathrm{opt}}=\frac{1}{2},\qquad 0\leq T<1;
\]

\[
e_{\mathrm{opt}}=\frac{1}{2+F(t_*)},\qquad T\geq1,\quad q^2\leq2v^2\ \mathrm{or}\ u\leq U_c(v,q);
\]

\[
e_{\mathrm{opt}}=\frac{1}{2}\left(1-\frac{L}{\sqrt{L^2+(u+v)^2}}\right),\qquad L=p+\sqrt{q^2-v^2},
\]

\[
T\geq1,\qquad q^2>2v^2,\qquad u>U_c(v,q).\tag{3}
\]

The second and third formulas coincide at the phase boundary. The minimum is attained by a two-port matrix of degree one and peak exactly T when $T\geq 1$. All three node errors are active. Extra ports cannot improve the value. For $T\geq 1$ the normalized denominator and the e2 intensity are unique, although scalar phases and unused output unitary choices are not.

If $u\leq 3v$, the second branch applies for every finite $T\geq 1$. If $u>3v$, there is exactly one finite transition $T_c>1$. In particular, increasing the cap can activate a global positivity constraint; it need not keep the old unconstrained lower certificate sharp.

For a finite radical description of the transition, put

\[
K=u^2-uv-v^2+1,
\]

\[
Q_c=\frac{2v^2\left[K+\sqrt{K^2-(u-3v)(u+v)(u^2+1)}\right]}{(u-3v)(u+v)},
\]

\[
T_c=\sqrt{Q_c+1}+\sqrt{Q_c}.\tag{4}
\]

Equation (4) is used only when $u>3v$. The positive sign selects the larger root and the unsquared equation (2); the other root does not describe the transition.

The main structural distinction is visible in the unique denominator $H(s)=s^2+2Bs+C$. In the inactive branch $B=qt_*/\sqrt{t_*^2+p^2}$ and the e1 residual quadratic is positive definite. At the boundary and throughout the active branch,

\[
B=-v,\qquad C=v^2+L^2,
\]

and both numerator intensities are rank-one quadratic forms. In the original ordering $u<v$ the corresponding pinned value is B=u. The conic feasibility reformulation by itself is a classical optimization technique, not the principal claim.

## 2. Exact quadratic reduction and the delay ellipse

A nonconstant degree-one rational-inner matrix has one rank-one Blaschke–Potapov factor. Its determinant zero alpha gives trace-delay peak $(1+|\alpha|)/(1-|\alpha|)\geq1$. Thus $T<1$ permits only constants, and a constant output has optimum squared error 1/2 for two orthogonal targets.

Use $s=\cot(\phi/2)$, so $z=(s+i)/(s-i)$, with $z=1$ represented by $s=\infty$. The column numerators are linear complex polynomials in s. Their squared moduli are nonnegative real quadratic forms. Normalize their sum to

\[
H(s)=s^2+2Bs+C,
\]

\[
M_{11}=1,\qquad M_{12}=M_{21}=B,\qquad M_{22}=C.
\]

The normalization is legitimate because the circle denominator is nonzero at $z=1$. Its circle intensity is proportional to $H(s)/(1+s^2)$, whose extreme-value ratio is $\lambda_{\max}(M)/\lambda_{\min}(M)$. The original angular peak cap is exactly

\[
B^2+\frac{[C-(1+2q^2)]^2}{4p^2}\leq q^2.\tag{5}
\]

This ellipse lies in the positive-definite region and is equivalent to $\lambda_{\max}(M)/\lambda_{\min}(M)\leq T^2$. It reduces to $M=I$ at $T=1$. For any real t its support is

\[
H(t)\leq A(t),\qquad B_t=\frac{qt}{\sqrt{t^2+p^2}},
\]

\[
C_t=1+2q^2+\frac{2p^2q}{\sqrt{t^2+p^2}}.\tag{6}
\]

Let Q be the e2 intensity and $P=H-Q$. Every router at squared error epsilon obeys

\[
Q(s)\geq0,\quad P(s)\geq0\quad (s\in\mathbb{R}\cup\{\infty\}),
\]

\[
\mathrm{lc}(Q)\geq1-\varepsilon,
\]

\[
Q(-u)\leq\varepsilon H(-u),\qquad Q(v)\leq\varepsilon H(v).\tag{7}
\]

Here evaluation at infinity is homogeneous: it means the leading coefficient of the quadratic form. For extra ports, P includes e1 and every remaining coordinate, so the repeated-node inequalities remain necessary. Conversely, any quadratic pair satisfying (5),(7) can be factored into two scalar linear complex polynomials and completed by Section 6; its actual repeated-node errors are Q/H. To make the general converse explicit, a nonnegative quadratic $R(s)=as^2+2bs+c$ with $a>0$ equals the squared modulus of $\sqrt{a}(s+b/a+i\sqrt{ac-b^2}/a)$. If $a=0$, positivity forces $b=0$ and the factor is the constant $\sqrt{c}$. Apply this separately to $Q$ and $P$, then use (22),(23). The degree is at most one and the cap is the one encoded by $M$. Hence the quadratic problem is exact for every ambient port count.

At fixed epsilon, (7) means $0\leq Q_{\mathrm{matrix}}\leq M$ plus three affine inequalities, and (5) is a second-order-cone constraint. A real symmetric matrix $M_{11}=a,\ M_{12}=M_{21}=b,\ M_{22}=c$ is PSD exactly when $\|(2b,a-c)\|\leq a+c$. Thus no frequency grid, port truncation or higher-degree positivity theorem is hidden in this finite representation. None of the proof below depends on the accuracy of a conic solver.

## 3. The inactive certificate and a simpler positivity test

For any quadratic R and -u<t<v, Lagrange interpolation gives

\[
\mathrm{lc}(R)=\frac{R(-u)}{(u+v)(u+t)}+\frac{R(v)}{(u+v)(v-t)}-\frac{R(t)}{D(t)}.\tag{8}
\]

Applied to Q and H, (7),(8),(6) give $\varepsilon\geq1/(2+F(t))$. Maximizing this lower bound amounts to minimizing F. Since A''>0, D''=-2 and

\[
(A^{\prime} D-AD^{\prime})^{\prime}=A^{\prime\prime} D+2A>0,
\]

there is exactly one stationary point; endpoint divergence and the signs at (v-u)/2 and zero prove its asserted location.

Write $F=F(t_*)$, $e=1/(2+F)$, $k=1-e$, and use the support denominator (6) at t=t_*. Stationarity implies the polynomial identity

\[
H(s)=(1+F)(s-t)^2+F(u+s)(v-s).\tag{9}
\]

Consequently $Q(s)=k(s-t)^2$ has all three active node errors. The residual $P=H-Q$ has leading coefficient $e>0$. Expressing the coefficient of s in (9) gives

\[
B=-(1+F)t+\frac{F(v-u)}{2},
\]

\[
\det(P_{\mathrm{matrix}})=\frac{F(u-B)(B+v)}{F+2}.\tag{10}
\]

For $u>v$ the support coefficient obeys $(v-u)/2<B\leq0$; for $u=v$ one has $B=0=(v-u)/2$. Hence $u-B>0$, and global residual positivity is equivalent simply to

\[
B\geq-v.\tag{11}
\]

When strict, P is positive definite. When equality holds, P has rank one. If (11) fails, equality in (8) would force this unique nonnegative Q and unique support denominator, whose residual violates positivity; the old lower certificate is then strictly below the optimum. This is the same criterion as $t_*^2(1+F)\leq p^2$ in the earlier calculation, now factored into the two endpoint factors in (10).

## 4. Deriving and classifying the transition

If $u\leq 3v$, then (v-u)/2>=-v and B>(v-u)/2 for finite T, except for the harmless symmetric equality at zero. Thus (11) holds strictly at every finite cap.

Suppose $q>v$ and put $w=\sqrt{q^2-v^2}$. The support coefficient B_t is strictly increasing in t, and $B_t=-v$ precisely at

\[
\tau=-\frac{pv}{w}.\tag{12}
\]

At this support point the denominator is

\[
H_0(s)=(s-v)^2+L^2,\qquad L=p+w.\tag{13}
\]

To determine on which side the minimizer lies, set $N=A^{\prime} D-AD^{\prime}$. At t=tau a direct substitution gives

\[
N(\tau)=\frac{L^2}{w^2}\left[(q^2-2v^2)u-v(q^2+2pw)\right].\tag{14}
\]

The formula is used for a root comparison only when $\tau$ lies in $(-u,v)$. If $\tau\leq -u$, then $t_*>\tau$ and the inactive criterion holds immediately. When $q\leq v$, $B_t\geq-q\geq-v$ also settles the issue immediately; at $q=0$ one has $B_t=0>-v$. For $v<q\leq\sqrt{2}\,v$, the expression in brackets in (14) is negative for every $u>0$, so $t_*\geq \tau$ whenever the comparison is needed. For $q>\sqrt{2}\,v$ it changes sign exactly at $u=U_c(v,q)$.

At $u=U_c$, the identities in the next section with $\sqrt{x}=v/w$ show tau in $((v-u)/2,0)$, so it is indeed the unique stationary point. For $u>U_c$ it stays inside (-u,v), (14)>0 and monotonicity of N gives $t_*<\tau$, equivalently $B_*<-v$. For $u<U_c$, either tau is left of the node interval or (14)<0, giving the inactive criterion. This proves that the branch test in (3) is exactly the old positivity test, including all cases where the square root or denominator in (2) would otherwise be undefined.

There is one transition precisely when $u>3v$. Indeed, writing $w>v$ and $p=\sqrt{w^2+v^2+1}$,

\[
\frac{U_c}{v}=\frac{2\left[1+\sqrt{1+(v^2+1)/w^2}\right]}{1-v^2/w^2}-1.\tag{15}
\]

As w increases from v to infinity the numerator decreases and the positive denominator increases. Thus U_c strictly decreases from infinity to 3v. Squaring its equality to u gives

\[
(u-3v)(u+v)Q^2-4v^2KQ+4v^4(u^2+1)=0,\qquad Q=q^2.\tag{16}
\]

with the retained condition $(u-v)Q-2uv^2>0$. At $Q=2v^2$ the polynomial is negative, while its leading coefficient is positive for $u>3v$; its larger root is the sole root above 2v² and is (4). The polynomial is also negative at $Q=2uv^2/(u-v)>2v^2$, so that larger root satisfies the retained positive sign. This proves the radicand and branch selection in (4).

## 5. A positive certificate for the active branch

Assume $q^2>2v^2$ and u>=U_c, allowing equality for the boundary. Define e by the last formula in (3), $k=1-e$, $x=e/k$, $m=(v-u)/2$ and $d=(u+v)/2$. Then

\[
0<x<1,\qquad L=\frac{d(1-x)}{\sqrt{x}},
\]

\[
t=m+dx=v-L\sqrt{x},\qquad r=m+\frac{d}{x}=v+\frac{L}{\sqrt{x}},
\]

\[
Q_0(s)=k(s-t)^2,\qquad P_0(s)=e(s-r)^2.\tag{17}
\]

Elementary expansion gives $Q_0+P_0=(s-v)^2+L^2$, so the denominator is exactly (13), on the cap ellipse. At the endpoints, (s-t)/(s-r) takes the values x and -x. It follows that $Q_0(-u)/H_0(-u)=Q_0(v)/H_0(v)=e$, while P_0/H_0 tends to e at infinity. Thus (17) is a globally feasible candidate using two ports.

The branch condition is equivalent to $\sqrt{x}\geq v/w$, or $t\leq \tau$. To see this, $d=L\sqrt{x}/(1-x)$ is strictly increasing in sqrt(x) in (0,1). At $\sqrt{x}=v/w$ it gives $u=U_c$; also $t\leq \tau$ is exactly $\sqrt{x}\geq v/w$ after using L=p+w. Notice $r>v>0$ and $\tau<0$.

Here is a lower certificate that proves optimality, without assuming a priori that the unknown optimizer has rank one. Put

\[
h=kr+et=v+\frac{L^2}{d}>0,
\]

\[
\nu=\frac{e(\tau-t)}{h-\tau}\geq0,\qquad\mu=1+\nu,
\]

\[
\lambda_- =\frac{v-t+\nu(r-t)}{u+v},\qquad\lambda_+=1-\lambda_-,
\]

\[
\lambda_0=\lambda_-(u+t)^2+\lambda_+(v-t)^2+\nu(r-t)^2.\tag{18}
\]

Both endpoint weights are strictly positive. The first is visibly positive. For the second, writing $x=e/k$ shows its positivity equivalent to $\nu<x/(1-x)$; substitution of nu reduces this to $2\tau<t+r$. But $t+r>2v>0>2\tau$. Therefore $\lambda_0>0$ and $\mu>0$. In the strict active phase $\nu>0$; at the boundary $\nu=0$.

For every quadratic R, direct matching of its three coefficients gives

\[
\lambda_0\mathrm{lc}(R)=\lambda_-R(-u)+\lambda_+R(v)+\nu R(r)-\mu R(t).\tag{19}
\]

The definition of nu gives the first-moment identity

\[
e[-u\lambda_-+v\lambda_+]+\nu r=(e+\nu)\tau.\tag{20}
\]

Define the constant

\[
\beta=e[\lambda_-u^2+\lambda_+v^2]+\nu r^2-(e+\nu)\tau^2.
\]

For every normalized H of leading coefficient one, (20) implies

\[
e[\lambda_-H(-u)+\lambda_+H(v)]+\nu H(r)=(e+\nu)H(\tau)+\beta,
\]

\[
(e+\nu)H(\tau)+\beta\leq(e+\nu)A(\tau)+\beta=\lambda_0 k.\tag{21}
\]

The last equality can be checked by substitution, or by applying (19) to Q_0: its two node inequalities, $Q_0(t)=0$, $P_0(r)=0$ and the support equality are all active.

Now let an arbitrary feasible router have squared error $\varepsilon<e$, with Q,P,H as in (7), and $W=\lambda_-H(-u)+\lambda_+H(v)>0$. Applying (19) to Q, using $Q(r)=H(r)-P(r)$, and then (7),(21), gives

\[
\lambda_0(1-\varepsilon)\leq\varepsilon W+\nu H(r)-\nu P(r)-\mu Q(t),
\]

\[
\varepsilon W+\nu H(r)-\nu P(r)-\mu Q(t)\leq\lambda_0(1-e)-(e-\varepsilon)W.
\]

Thus $(e-\varepsilon)(\lambda_0+W)\leq0$, a contradiction. This certificate covers complex numerator coefficients and every number of extra output coordinates. It proves the active part of Theorem 1. It also rules out an overlooked phase with an inactive node: all three weights are strictly positive.

For equality, the positive weights require all three node errors to be active and $Q(t)=0$, while ellipse support uniqueness fixes $H=H_0$. In the strict active phase $\nu>0$ also forces $P(r)=0$. The leading coefficient determines $Q=Q_0$. The same uniqueness follows at the boundary from $Q(t)=0$ and the active leading coefficient. Together with the earlier inactive certificate, this proves the uniqueness assertion in Theorem 1.

## 6. Operational lossless compiler with two ports

For $0\leq T<1$, use the constant matrix with entries $S_{11}=S_{21}=S_{22}=1/\sqrt{2}$ and $S_{12}=-1/\sqrt{2}$. It has degree zero, peak zero and squared node errors $1/2$. The degree-one sharp operation in (23) is not applied to this constant branch. The software returns this matrix directly with `completion_degree=0`.

Both nonconstant branches give $Q=k(s-t)^2$, $P=es^2+2js+\ell\geq0$ and $H=s^2+2Bs+C>0$. Put

\[
\eta=\sqrt{\frac{\ell}{e}-\left(\frac{j}{e}\right)^2}\geq0,
\]

\[
q_R(s)=\sqrt{k}(s-t),\qquad p_R(s)=\sqrt{e}\left(s+\frac{j}{e}+i\eta\right),
\]

\[
\Delta=\sqrt{C-B^2}>0.
\]

In the active phase $\eta=0$ and $p_R(s)=\sqrt{e}(s-r)$. Define linear polynomials

\[
q_z(z)=(z-1)q_R\left(\frac{i(z+1)}{z-1}\right),
\]

\[
p_z(z)=(z-1)p_R\left(\frac{i(z+1)}{z-1}\right),
\]

\[
h_z(z)=i(z+1)+(B-i\Delta)(z-1).\tag{22}
\]

On the circle, $|p_z|^2+|q_z|^2=|h_z|^2=4H(s)/(1+s^2)$. The constant and linear coefficients of h_z are $h_0=-B+i(1+\Delta)$ and $h_1=B+i(1-\Delta)$; they satisfy $|h_0|^2-|h_1|^2=4\Delta>0$. Thus h_z has no zero in the closed disk. This is the degree-one scalar spectral factor written explicitly.

For $f^\sharp(z)=z\overline{f(1/\overline{z})}$, set

\[
(S_2)_{11}=\frac{p_z}{h_z},\qquad (S_2)_{21}=\frac{q_z}{h_z},
\]

\[
(S_2)_{12}=-\frac{q_z^{\sharp}}{h_z},\qquad (S_2)_{22}=\frac{p_z^{\sharp}}{h_z}.\tag{23}
\]

The columns are orthonormal on the circle, S_2 is analytic in the disk, and $\det S_2=h_z^\sharp/h_z$ is a scalar Blaschke product of degree one, including a zero at zero if $h_1=0$. Its global peak is $(|h_0|+|h_1|)/(|h_0|-|h_1|)$, equal to $\sqrt{\lambda_{\max}(M)/\lambda_{\min}(M)}=T$. The determinant and the rank-one inner structure give McMillan degree exactly one. Also q_z and p_z have no common zero because Q vanishes at t while $P(t)=H(t)>0$. Constant changes of input/output bases and a block identity embed the solution in N ports, without extra states or peak delay.

The construction requires real arithmetic, square roots, and only in the inactive branch one isolated root of (1). For algebraic u,v,T the root is algebraic of degree at most four: square

\[
2tD-(t^2+p^2)D^{\prime}=q\sqrt{t^2+p^2}\,D^{\prime}
\]

and retain its unsquared sign and the unique interval $((v-u)/2,0)$. For $u=v$ use t=0; for $T=1$ the unsquared polynomial already reduces to degree two. There is no iterative SDP requirement and no frequency sampling in the certificate.

## 7. Exact examples, degenerations and asymptotics

**The formerly obstructed example.** For u=3, v=1/3, T=2 one has q²=9/16 and $q_c^2=(8+\sqrt{10})/27$. Therefore T_c is approximately 1.831848098864042, and the active branch applies at T=2. Its exact value is

\[
L=\frac{15+\sqrt{65}}{12},
\]

\[
e_{\mathrm{opt}}=\frac{1}{2}\left(1-\frac{L}{\sqrt{L^2+100/9}}\right)
\]

\[
e_{\mathrm{opt}}=0.250257935326986104116692073687\ldots.\tag{24}
\]

The old lower certificate is 0.25002997308687797..., strictly smaller. Thus merely continuing the inactive quartic formula gives an unattainable answer. The new denominator is B=-1/3, $C=(153+15\sqrt{65})/72$, and both power quadratics are perfect squares.

**A certificate with rational coefficients throughout.** Take

\[
T=2,\qquad v=\frac{9}{20},\qquad u=\frac{1399}{180},
\]

\[
B=-\frac{9}{20},\qquad C=\frac{29}{8},\qquad e=\frac{16}{41},\qquad k=\frac{25}{41},
\]

\[
t=-\frac{103}{100},\qquad r=\frac{221}{80},\qquad\tau=-\frac{15}{16}.
\]

Then $Q=k(s-t)^2$ and P=e(s-r)² have three errors e and peak T. All weights (18), the support direction, and every coefficient in the lower certificate are rational. This fixture certifies the positivity-active formula with exact rational arithmetic, independent of numerical optimization.

**A rational point on the transition.** With T=2, v=9/20 and u=165/28, the two formulas give e=9/25, t=tau=-15/16, B=-9/20, C=29/8 and $\nu=0$. The replay checks the equality branch separately.

**Degenerations.** At $u=v=c$ the law reduces to $e=c^2/(T^2+2c^2)$. At $T=1$, putting $R=\sqrt{(1+u^2)(1+v^2)}$ gives the all-gap expression $e=(R+uv-1)/(2(R+uv))$; in particular it is strictly below 1/2 for finite positive gaps. There is consequently a jump from the constant branch at the first nonzero cap. The ratio $u/v=3$ has no finite positivity transition. At fixed v, as u decreases to 3v from above,

\[
T_c\sim2\sqrt{\frac{v(1+5v^2)}{u-3v}}.\tag{25}
\]

At fixed u>0 and T>1, as v decreases to zero the active formula tends to $(1-T/\sqrt{T^2+u^2})/2$. This is a limit toward b=pi, not an extension of the stated open-angle hypotheses. As u tends to infinity at fixed v,T, $e_{\mathrm{opt}}$ tends to 1/2, consistently with collision of the exceptional node and one repeated-target node. None of these limits identifies a finite-cap zero-error router.

**High delay.** For every fixed u,v>0,

\[
\lim_{T\to\infty}T\sqrt{e_{\mathrm{opt}}}=\frac{u+v}{2}.\tag{26}
\]

For the inactive branch this follows from uniform $A(t)/T^2\to1$ on the compact interval between (v-u)/2 and zero, and the maximum $D((v-u)/2)=(u+v)^2/4$. The active branch has $L/T\to 1$ and yields the same limit directly. Therefore the leading asymptotic constant alone does not reveal the positivity transition.

More precisely, put $d=(u+v)/2$ and $m=(v-u)/2$. Let $e_L=1/(2+\min A/D)$, even where this lower bound is unattainable. Expansion of (1) gives $t_*=m+O(T^{-2})$, and hence

\[
e_L=\frac{d^2}{T^2}-\frac{2d^2(d^2+m^2)}{T^4}+O(T^{-6}).
\]

In the strict asymmetry regime $u>3v$, the active value instead satisfies

\[
e_{\mathrm{opt}}=\frac{d^2}{T^2}+\frac{2v^2d^2-3d^4}{T^4}+O(T^{-6}),
\]

\[
e_{\mathrm{opt}}-e_L=\frac{d^2(u-3v)^2}{4T^4}+O(T^{-6}).\tag{27}
\]

Thus the failure has a positive, explicit fourth-order size. These expansions hold for fixed positive u,v; they are not uniform through a node collision or simultaneous parameter scaling.

## 8. Antecedents, scope and verification status

The complete local cycle-2 manuscript `outputs/cycle2/passive/asymmetric_delay.md` and its independent review were read. They prove the inactive lower certificate and its exact residual-positivity criterion, including the all-T u=2,v=1 law and all-gap $T=1$ law, and explicitly leave the failed-positivity region open. The present additions relative to that corpus are the factorization (10), full branch classification (2)–(4), explicit active law and positive dual certificate, operational full-regime compiler and quantitative asymptotics. The underlying local passive predecessor is [Projective Memory and Resonant Bottlenecks in Passive Spectral Routing](https://arr-research.github.io/papers/ARR-2026-6M3VGTXZ6W8JW9C9/); its limitation and earlier comparison are recorded by cycle 2.

Classical structural ingredients remain classical. [Alpay, Jorgensen and Lewkowicz, *Characterizations of rectangular (para)-unitary rational functions*, arXiv:1410.0283v2](https://arxiv.org/html/1410.0283v2), Sections 2–3, provides degree-preserving completion and Blaschke–Potapov structure. Its outside-disk stability convention is reflected to the disk convention used here. The explicit spectral factor and two-port completion in Section 6 specialize this structure.

The magnitude-squared substitution, global nonnegative power polynomials and convex or quasiconvex filter design via spectral factorization have direct antecedents in [Wu, Boyd and Vandenberghe, *FIR Filter Design via Semidefinite Programming and Spectral Factorization*, CDC 1996](https://stanford.edu/~boyd/papers/pdf/magdes_cdc96.pdf), and its [1998 chapter version](https://web.stanford.edu/~boyd/papers/magdes.html). That framework already explains why an exact finite conic formulation should not itself be presented as a major new result. It does not by its statement supply the present degree-one, three-node, original-coordinate peak-delay phase boundary.

A current adjacent comparison is [Dong, Larsen, Lin and Sarkar, *Constrained Minimax Approximation for Quantum Signal Processing*, arXiv:2608.30937v1, submitted 31 August 2026](https://arxiv.org/html/2608.30937v1). It addresses bounded polynomial minimax approximation and the danger of inferring continuous feasibility from a frequency grid, with active constraints and degree-preserving completion. Its objects are parity-constrained QSP polynomials, not this rational-inner three-node peak-delay problem. [Zhang, Yang, Yang and Zhang, *A convex dual problem for the rational minimax approximation and Lawson's iteration*, arXiv:2308.06991](https://arxiv.org/abs/2308.06991), supplies an adjacent rational-minimax duality comparison; its abstract is a bounded comparison only here.

The external search is bounded, not an exhaustive priority review. No bibliographic-priority claim is made for (3), and no physical circuit-component synthesis, laboratory time calibration, loss model, nonorthogonal target, fixed output phase, $\mathrm{degree}\ \geq 2$ or arbitrary larger interpolation table is covered. Additional nodes require additional error checks. The state-memory identities from the older routing corpus are not new consequences claimed here.

The companion replay distinguishes universal symbolic identities, exact rational/radical certificates and high-precision numerical supplements. Numerical conic experiments were used only to suggest the active structure; inaccurate solver statuses and points with negative residual eigenvalues were not accepted as certificates. The analytic lower certificates and compiler establish the continuum claims. No Lean formalization, external refereeing or independent review by the deriving agent is claimed.

Lluis Eriksson directed the research programme. OpenAI Codex assisted with derivation, computation, source comparison and drafting.
