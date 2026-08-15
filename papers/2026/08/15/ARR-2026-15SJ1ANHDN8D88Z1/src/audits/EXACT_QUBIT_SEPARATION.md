# Exact qubit separation for the support threshold

Consider the equiprobable pure qubit states with Bloch vectors

\[
n_1=(0,0,1),\qquad n_2=(4/5,0,3/5),\qquad
n_3=(0,4/5,3/5).
\]

Every pair of state vectors is linearly independent, so the support matroid is
`U_(2,3)` and its two-fold union is free.  The support bound therefore permits
perfect two-list success.  The true optimum is nevertheless

\[
P_{\rm list}^{\star}=\frac{2+1/\sqrt 3}{3}<1.
\]

## Dual certificate

Reporting a two-element list is equivalent to omitting one label.  If `F_i`
is the effect that omits label `i`, the exclusion error is

\[
P_{\rm err}=\frac13\sum_i\operatorname{Tr}(F_i\rho_i),
\qquad F_i\succeq0,\quad \sum_iF_i=I.
\]

The SDP dual maximizes `Tr Y` subject to `Y <= rho_i/3`.  Write

\[
Y=y_0I+y\cdot\sigma,
\qquad \frac{\rho_i}{3}=\frac16(I+n_i\cdot\sigma).
\]

The three matrix inequalities are equivalent to

\[
y_0\leq \frac16-\left\lVert\frac{n_i}{6}-y\right\rVert
\quad(i=1,2,3).
\]

Thus the dual is the smallest-enclosing-ball problem for the three points
`n_i/6`.  Their triangle is acute.  Its circumcenter and radius before the
factor `1/6` are

\[
u=(1/3,1/3,2/3),\qquad R=1/\sqrt3.
\]

Taking

\[
y=u/6,\qquad y_0=(1-R)/6
\]

gives the feasible dual operator

\[
Y_\star=\frac16\bigl((1-R)I+u\cdot\sigma\bigr),
\qquad \operatorname{Tr}Y_\star=\frac{1-R}{3}.
\]

## Primal attainment

Put

\[
m_i=\frac{u-n_i}{R},\qquad
(w_1,w_2,w_3)=\left(\frac13,\frac56,\frac56\right),
\]

and define

\[
F_i=\frac{w_i}{2}(I+m_i\cdot\sigma).
\]

The barycentric identity

\[
u=\frac16n_1+\frac5{12}n_2+\frac5{12}n_3
\]

implies `sum_i w_i=2` and `sum_i w_i m_i=0`; hence
`sum_i F_i=I`.  Moreover, `F_i` is supported in the kernel of
`rho_i/3-Y_star`, so complementary slackness holds.  Therefore

\[
P_{\rm err}^{\star}=\frac{1-R}{3},\qquad
P_{\rm list}^{\star}=1-P_{\rm err}^{\star}
=\frac{2+1/\sqrt3}{3}.
\]

This is a quantitative separation between disappearance of the union-matroid
support obstruction and physical attainability.  It is not a general formula
for quantum list discrimination.
