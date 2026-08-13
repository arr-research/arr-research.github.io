# Paper 16 research memo

## Working title

The Finite-Sample Boundary of Spectral-Gap Inference: Hidden Atoms, Honest Wishart Tests, and Visibility-Optimal Filters

## Core statistical experiment

Let mu be a probability measure on [0,1]. For N >= 0 define the 2N+2 feature functions

    f_i(x) = x^i,        g_i(x) = x^(i+1/2),    0 <= i <= N.

Their Gram covariance K_mu has principal blocks

    H_N = [m_(i+j)],     G_N = [m_(i+j+1)].

Independent observations z_1,...,z_n ~ N(0,K_mu) are Gaussian Euclidean sketches. The null edge hypothesis is supp(mu) subset [0,theta]. It implies theta H_N-G_N >= 0.

## New theorem package

### 1. Finite-window Le Cam obstruction

Choose a gapped mu_0 supported by 2N+2 distinct points in (0,theta), so K_0 is positive definite. Let

    mu_w = (1-w)mu_0 + w delta_1,
    K_w  = (1-w)K_0 + w vv^T,
    A    = K_0^(-1/2) vv^T K_0^(-1/2) - I.

If w ||A||_op <= 1/2, then

    KL(N(0,K_w)^n || N(0,K_0)^n) <= n w^2 ||A||_F^2 / 2,
    TV <= w ||A||_F sqrt(n) / 2.

Hence every level-alpha gap test has power at most alpha + w ||A||_F sqrt(n)/2 against a zero-gap hidden atom of weight w. No finite-window procedure is uniformly powerful without a visibility floor. The result concerns distributions of the observed sketches, not only closeness of noiseless moments.

### 2. Exact finite-sample level

For an adaptively chosen degree-N filter, use the full raw sketch with d=2N+2. For a Chebyshev filter fixed before seeing the data, first compress every raw sketch to the two coordinates (p_N(T)V,T^(1/2)p_N(T)V), so d=2. In either regime, for S=n^(-1) sum z_r z_r^T and

    eta=(sqrt(d)+sqrt(2 log(2/alpha)))/sqrt(n) < 1,
    a=(1+eta)^(-2), b=(1-eta)^(-2),

the simultaneous band aS <= K <= bS covers K with probability at least 1-alpha. Reject theta only when no K in this band has theta H_N(K)-G_N(K) >= 0. This test has type-I error at most alpha with arbitrary adaptive witness optimization and no sample split.

### 3. Visibility-conditioned explicit power

Assume mu([theta+delta,1]) >= gamma. Let

    p_N(x)=T_N(2x/theta-1)/T_N(1+2delta/theta),
    q=1/T_N(1+2delta/theta),
    A0=theta q^2,
    mu0=delta gamma-A0(1-gamma) > 0,
    r0=mu0/(1+theta).

For the rank-one polynomial witness X, its population negativity-to-uncertainty ratio obeys r_X >= r0. Therefore rejection has probability at least 1-alpha whenever

    n > (sqrt(d)+sqrt(2 log(2/alpha)))^2
        * (sqrt(1+r0)+1)^4 / r0^2.

The proof uses the two-block covariance geometry, avoiding any monomial coefficient-norm penalty. The fixed-filter theorem has d=2 (or d=2c for c channels); the simultaneous adaptive theorem pays d=2(N+1) (or d=2c(N+1)).

## Ratio proof ledger (integer-time filter-first design)

Write p=p_N, u=p(T)V, v=Tp(T)V, and observe the 2D Gaussian sketch with covariance K=[[P,X],[X,R2]]. The null functional is theta P-X. Put m=X-theta P and C=[[theta,-1/2],[-1/2,0]]. Then

    w=||K^(1/2) C K^(1/2)||_1 <= theta P+sqrt(P R2) <= (1+theta)P.

Let l,s,h be the masses of the low, middle, and high regions. On low, |p|<=q; on middle, 0<p<=1; on high, p>=1. Hence m>=delta h-A0 l>=mu0. If H is the high positive contribution, H<=m+A0 l and P_high<=H/delta. Therefore

    P <= l q^2+s+(m+A0 l)/delta
      <= 1-gamma+(m+A0(1-gamma))/delta.

The ratio m/[(1+theta)P] is increasing in m. At m=mu0 the bracket bounding P equals one, so m/w>=mu0/(1+theta)=r0.

## Scope and forbidden claims

- The theorem rejects an overstated visible gap; it does not prove a positive Yang-Mills mass gap.
- Gaussian primitive sketches and known zero mean are assumptions, not universal noise robustness.
- Visibility gamma is external information; it cannot be estimated from the same finite noisy window without circularity.
- Chebyshev is minimax for uniform stop-band leakage, not necessarily for the full statistical sample-size functional.
- The lower and upper theorems establish a sharp logical boundary, not a universal constant-optimal minimax rate over growing moment depth.

## Priority boundary

Classical ingredients include Le Cam/Pinsker testing bounds, Gaussian singular-value concentration, Hausdorff localizers, and Chebyshev extremality. The claimed novelty is their exact conjunction for finite-sample Euclidean spectral-edge inference, including the explicit visibility-to-sample-complexity bridge and the no-split adaptive test.
