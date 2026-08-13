# Independent audit: Gaussian spectral-gap boundary

Date: 2026-08-11

## Verdict

The proposed visibility-to-power inequality is correct under explicit
normalization and acquisition assumptions.  The hidden-atom argument becomes
a valid Le Cam lower bound only after choosing a null covariance that is
positive definite.  The strongest fixed-filter version should use the
compressed feature dimension `2c`, not the raw moment-feature dimension
`2(N+1)c`.

This is a mathematically coherent synthesis, but its novelty is the explicit
bridge and boundary theorem, not any of Le Cam, Gaussian singular-value
concentration, Hausdorff localization, or Chebyshev extremality separately.

## Population ratio

Let `0 < theta < 1`, `0 < delta <= 1-theta`, and let `nu_X` be a probability
spectral measure.  Thus in the multichannel form one needs `X >= 0`,
`tr(X)=1`, and an isometric normalization of the probe map.  Let

```
p(x) = T_N(2x/theta-1)/T_N(1+2delta/theta),
alpha_N = 1/T_N(1+2delta/theta),
a = theta alpha_N^2.
```

Split the interval into low, middle, and high parts and put

```
L = integral_low  (theta-x)p(x)^2 dnu_X,
M = integral_mid   (x-theta)p(x)^2 dnu_X,
H = integral_high (x-theta)p(x)^2 dnu_X,
m = M+H-L.
```

Then `L <= a`, `M >= 0`, and visibility gives `H >= delta gamma`, hence
`m >= mu := delta gamma-a`.  For the covariance of the stacked filtered
features and `C=diag(theta X,-X)`,

```
w = tr |K^(1/2) C K^(1/2)|
  <= tr(|C|K)
  = integral (theta+x)p(x)^2 dnu_X.
```

The trace-norm step follows by decomposing `C=C_+-C_-` and applying the
triangle inequality to the two positive congruences.  On the three regions,

```
low cost   <= 2a,
middle cost <= 2theta+delta,
high cost  <= R H,   R=(2theta+delta)/delta.
```

Since `H=m+L-M <= m+a`,

```
w <= (2+R)a+(2theta+delta)+R m = C0+R m.
```

The map `t -> t/(C0+Rt)` is increasing, so if `mu>0`,

```
m/w >= mu/(C0+Rmu) = r0.
```

No inequality direction is reversed in this chain.

### Sharper regional-envelope constant

The displayed bound is valid but not the strongest consequence of the same
three-region estimates.  Let `l,s,h` be the low, middle, and high masses.
Then `h>=gamma`, `l+s<=1-gamma`, and

```
m >= delta h-a l
  >= mu_star := delta gamma-a(1-gamma).
```

Writing the three denominator pieces as `D_L,D_M,D_H` gives

```
D_L <= 2a l,
D_M <= (2theta+delta)s,
D_H <= R H <= R(m+a l).
```

Consequently

```
w <= Rm+(2+R)a l+(2theta+delta)s
  <= Rm+C_star,
C_star=(1-gamma) max{(2+R)a,2theta+delta}.
```

Hence the stronger closed ratio is

```
r_star=mu_star/(C_star+R mu_star).
```

For `theta=1/2`, `delta=1/4`, `gamma=1/5`, `N=2`, this gives
`mu_star=41/980`, `C_star=1`, `r_star=41/1185`.  At significance `0.05`
and compressed dimension `d=2`, the strict threshold is
`235945.45179986526`, so `n>=235946` suffices.  This improves the original
regional estimate without adding a new assumption.

## Wishart algebra

For a real Gaussian feature vector of dimension `d`, put

```
eta=(sqrt(d)+sqrt(2 log(2/alpha_sig)))/sqrt(n).
```

The two-sided singular-value event has probability at least
`1-alpha_sig`.  The witness power condition is

```
delta_+(eta) < r0,
delta_+(eta)=((1+eta)/(1-eta))^2-1.
```

Solving it gives

```
eta < r0/(sqrt(1+r0)+1)^2,
n > (sqrt(d)+sqrt(2 log(2/alpha_sig)))^2
    (sqrt(1+r0)+1)^4/r0^2.
```

The strict sample inequality also implies `eta<1`.

## Dimension correction

If `p_N` is fixed before the data are inspected, each raw Gaussian moment
sketch can be linearly compressed to the stacked pair

```
(p_N(T)V, T^(1/2)p_N(T)V).
```

It is a Gaussian vector of dimension `2c`, and its sample covariance is
Wishart with the filtered covariance.  Therefore the theorem may use
`d=2c`, independent of `N`; in the scalar case `d=2`.  Using
`d=2(N+1)c` is valid but unnecessarily weak.

The raw dimension is appropriate if the filter or degree is selected
adaptively from the same data and the proof relies on one confidence band
that is simultaneous over all such linear compressions.  Otherwise selection
over several filters needs a simultaneous correction or sample splitting.

## Le Cam lower bound

Moment proximity alone is insufficient to prove proximity of Gaussian sample
laws when the base covariance is singular: adding an atom can open a new
support direction and make the laws mutually singular.  The lower theorem
must choose a gapped null with `K0 > 0`.  A continuous measure with positive
density on a compact subinterval of `(0,theta)` is an easy universal choice;
the feature functions are linearly independent there, so their Gram matrix is
positive definite.

For

```
Kw=K0+w(K1-K0),
E=K0^(-1/2)(K1-K0)K0^(-1/2),
```

if `w ||E||_op <= 1/2`, eigenvalue calculus gives

```
KL(N(0,Kw)^n || N(0,K0)^n) <= n w^2 ||E||_F^2/2,
TV <= w ||E||_F sqrt(n)/2.
```

Thus any level-`alpha_sig` test has power at most
`alpha_sig+w||E||_F sqrt(n)/2` at that hidden-atom alternative.  This is an
existential minimax obstruction over the model class, not a pointwise claim
at every gapped null.

## Required scope statements

- `T` is a positive contraction and `V` is normalized so that `nu_X` has
  total mass one.
- Visibility holds for the same direction `X` used by the witness.  A
  trace-averaged visibility premise permits the fixed choice `X=I/c`, not an
  arbitrary adaptive direction.
- The displayed concentration constants are for real, known-zero-mean
  Gaussian sketches.  Complex Gaussian sketches need their own stated tail
  convention.
- Use different notation for significance `alpha_sig` and Chebyshev leakage
  `alpha_N`.
- Chebyshev minimizes uniform stop-band leakage, not the complete statistical
  sample-size functional.  “Visibility-calibrated” is safer than
  “visibility-optimal” in the title.

## Strength relative to Paper 15

Without the quantitative Gaussian Le Cam statement, the paper is a direct
corollary-level synthesis and does not exceed Paper 15.  With the lower bound,
the compressed-dimension upper theorem, and a clean acquisition model, it is
autonomous and publishable, but remains less structurally strong than Paper
15's exact generic degree law.  It should be selected only if the programme
values a new statistical/physical axis more than a stronger exact algebraic
theorem.
