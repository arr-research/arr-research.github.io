# Audit of the beta-mixing trajectory theorem

## Model and convention

The full finite-filter readout process is strictly stationary and bounded:
`|Y_{s,k}^{(j)}| <= B_j`.  Its absolute-regularity coefficient is defined by

`beta_mix(q) = sup_t E sup_{A in F_{t+q}^infty} |P(A | F_{-infty}^t)-P(A)|`.

With this convention, Berbee coupling gives a future copy, independent of the
past and with the correct marginal law, whose mismatch probability is at most
`beta_mix(q)`.

## Lag-covariance penalty

For one filter let `Gamma_j(q)=Cov(Y_t^(j),Y_{t+q}^(j))`.  Coupling the future
coordinate to an independent copy yields entrywise

`|Gamma_j(q)_{ab}| <= 2 B_j^2 beta_mix(q)`.

For the localizer matrix

`C = [[theta,-1/2],[-1/2,0]]`,

the sum of absolute coefficients is `1+theta`.  Therefore the paired statistic
has bias at most

`b_j(q)=2(1+theta) B_j^2 beta_mix(q)`.

The null-safe test adds `b_j(q)`.  Under an alternative, the unknown lag bias
can act in the opposite direction and costs another `b_j(q)`.  The uniform
power separation is therefore `mu-2b_j(q)`, not `mu-b_j(q)`.

## Independent block coupling

The retained pairs use times

`t_r=1+2q(r-1)` and `t_r+q`.

Consecutive pair blocks are separated by `q` time steps.  Recursive Berbee
coupling constructs independent blocks with total mismatch probability bounded
by

`epsilon_{n,q}=(n-1) beta_mix(q)`.

On the coupling event, ordinary one-sided Hoeffding concentration applies with
the exact quadratic range `L_theta(B_j)` already proved for the iid theorem.
Adding the coupling failure probability proves the displayed level and power
bounds.

## Geometric envelope and fixture

If `beta_mix(q) <= c exp(-q/tau)`, choosing

`q_n=max(1,ceil(tau log(c(n-1)/epsilon)))`

gives `epsilon_{n,q_n} <= epsilon` and

`b_j(q_n) <= 2(1+theta)B_j^2 epsilon/(n-1)`.

For the manuscript fixture

- `theta=1/2`, `mu=41/980`, `M=3`, `B=1`;
- type-I and miss probabilities `0.05`;
- coupling budget `epsilon=0.01`;
- `beta_mix(q) <= 2^(-q)`;

the first sufficient integer count is `n=68,527` paired blocks.  The certified
lag is `q=23`, the retained readout count is `137,054`, and the elapsed chain
horizon is `3,152,220` steps.  These values are replayed by
`certify_statistical_boundary.py` under schema v3.

## Scope gates

The theorem does not estimate a mixing coefficient, certify stationarity,
remove burn-in, or cover arbitrary MCMC output.  The mixing envelope is an
external model premise.  The contribution is an explicit valid bridge from
that premise to a finite-sample spectral-edge falsifier.
