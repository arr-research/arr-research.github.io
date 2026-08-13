# Independent derivation audit: weighted localizers and the hidden-atom LAN boundary

## Scope

This note audits two additions to the manuscript.  Neither ordinary local
asymptotic normality nor Chebyshev polynomials of the fourth kind are claimed
as new.  The contribution is their exact specialization to finite-window
spectral-gap falsification.

## 1. Fourth-kind weighted minimax identity

Let `y=2x/theta-1`, `y_delta=1+2 delta/theta`, and let `W_N` be the
Chebyshev polynomial of the fourth kind,

`W_N(cos t)=sin((N+1/2)t)/sin(t/2)`.

For every polynomial `r` of degree at most `N` with
`r(theta+delta)=1`,

`max_[0,theta] sqrt(theta-x)|r(x)| >= sqrt(theta)/W_N(y_delta)`.

Equality is attained by

`q_N(x)=W_N(2x/theta-1)/W_N(y_delta)`.

Indeed,

`(theta-x)q_N(x)^2 = theta sin^2((N+1/2)t)/W_N(y_delta)^2`.

The right side alternates at `N+1` points.  A strictly better competitor
would make its difference from `q_N` alternate sign between those points and
also vanish at `theta+delta`, giving at least `N+1` roots to a polynomial of
degree at most `N`.  This is impossible.  The same argument gives uniqueness.

For `x>=theta+delta`, the hyperbolic identity

`W_N(cosh eta)=sinh((N+1/2)eta)/sinh(eta/2)`

shows that `q_N(x)>=1`.  Therefore the exact worst-case localizer over the
regional visibility class is

`theta(1-gamma)/W_N(y_delta)^2-delta gamma`.

It is attained by placing low-band mass at any weighted alternation point and
high-band mass at `theta+delta`.  Hence strict negativity is necessary and
sufficient for uniform detection within the declared degree-`N` polynomial
localizer class.

## 2. Strict improvement over the first-kind filter

For `eta>0`,

`W_N(cosh eta)=1+2 sum_(k=1)^N cosh(k eta)>cosh(N eta)=T_N(cosh eta)`

for every `N>=1`.  Thus the weighted loss

`theta/W_N(y_delta)^2`

is strictly smaller than the old first-kind envelope

`theta/T_N(y_delta)^2`.

At `theta=1/2`, `delta=1/4`, `gamma=1/5`, and `N=2`, the denominators are
`T_2(2)=7` and `W_2(2)=19`.  The certified margin improves from `41/980` to
`353/7220`.  The displayed sufficient resources consequently improve from
128,842 to 94,340 bounded raw observations and from a 3,152,220-step to a
2,308,120-step beta-mixing trajectory horizon.

## 3. Exact Gaussian geometry and LAN

With `a=K_0^(-1/2)v_*`, `beta=||a||^2`, and
`A=aa^T-I_d`, the eigenvalues of `A` are `beta-1` and `-1` with multiplicity
`d-1`.  The whitened alternative covariance has eigenvalues

`tau_w=1+w(beta-1)` and `rho_w=1-w`.

Consequently the one-sample relative entropy is exactly

`1/2[(d-1)(-w-log(1-w))+w(beta-1)-log(1+w(beta-1))]`.

For `w_n=h/sqrt(n)`, the log likelihood ratio has the LAN expansion

`h Delta_n-h^2 I/2+o_P(1)`,

where

`I=||A||_F^2/2=((beta-1)^2+d-1)/2`.

The level-`alpha` asymptotic power envelope is

`1-Phi(z_(1-alpha)-h sqrt(I))`.

Thus `w_n sqrt(n)` is the sharp simple-path boundary: vanishing gives
asymptotic power equal to size, finite nonzero limits give the displayed
nontrivial power, and divergence gives a consistent score test.  This is a
fixed-window, known-path statement.  It is not a composite scan result and it
does not supply a uniform rate when the degree or covariance conditioning also
changes.

## 4. Claims deliberately excluded

- No claim that fourth-kind Chebyshev polynomials are new.
- No minimax claim outside the normalized polynomial-localizer class.
- No composite-alt or unknown-location power envelope.
- No uniform LAN theorem over growing moment depth.
- No removal of Gaussianity from the LAN branch.
