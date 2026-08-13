# Claim ledger

## Headline claims

| Claim | Status | Proof / replay | Scope gate |
|---|---|---|---|
| Block Hankel Ritz values increase to the visible transfer edge | proved | Proposition 2.1 | visible cyclic subspace only |
| Flat rank stabilization recovers the complete visible spectrum | proved | Theorem 3.1; exact rational fixture | exact arithmetic terminal branch |
| Every positive finite moment-error ball contains models with arbitrarily small strictly positive gap | proved | Theorem 4.1 and near-critical corollary; endpoint Lean core | edges remain strictly below one; no extra zero mode needed |
| A near-critical atom has an exact rank-one-spike likelihood and a sharp `w sqrt(n)` LAN power phase | proved | Theorems 5.1--5.2; exact KL/LR, central sequence, independent fixture | fixed nonsingular Gaussian covariance, degree, and known atom path |
| Visibility plus fourth-kind Chebyshev filtering yields the exact worst-case localizer margin `delta gamma-e_N(1-gamma)` | proved | Theorem 6.2; two-atom extremizer; rational replay | declared `(delta,gamma)` premise and normalized scalar polynomial localizers |
| The fourth-kind filter is the exact weighted-localizer minimizer | proved | Proposition 6.3; weighted alternation; independent random-competitor audit | degree-N real polynomials normalized at `theta+delta` |
| The exact population threshold gives a closed depth--sample law | proved | Corollary 7.2; Wishart theorem; rational certificate | achievable law, not joint global minimax |
| The two-coordinate Wishart feasibility test has finite-sample level at most alpha | proved | Theorem 7.1; Gaussian singular-value band | iid exactly Gaussian, known-zero-mean, precommitted filter |
| Visibility gives the explicit Wishart sufficient sample bound | proved | Theorem 7.1; rational certificate | sufficient, not globally minimax |
| Bounded iid readouts admit a non-Gaussian unknown-mean finite-bank test | proved | paired-difference Hoeffding theorem; exact range; replay | iid and known coordinate bounds; not MCMC |
| A stationary bounded beta-mixing trajectory admits an explicit finite-bank test | proved | Berbee block coupling, lag-covariance lemma, Hoeffding theorem, geometric-mixing corollary, replay | stationarity, known coordinate bounds, and an externally certified mixing envelope; no burn-in claim |
| The ANNNI X probe is parity-blind while the (X,Z) block detects the edge | verified finite volume | exact sparse records through L=16 | no thermodynamic extrapolation |

## Priority boundary

- Classical and not claimed: Rayleigh-Ritz, Krylov termination, truncated
  moments, Chebyshev polynomials/alternation, Gaussian KL/Pinsker/LAN, Gaussian singular-value
  concentration, and symmetry selection rules.
- Contribution claimed: the assembled impossible/terminal/visibility-restored
  finite-sample falsification boundary, the exact hidden-atom Gaussian
  specialization, the exact weighted visibility minimax, the explicit two-coordinate
  visibility-to-Wishart theorem, the bounded unknown-mean filter-bank test, and
  the explicit dependence penalty for one stationary beta-mixing trajectory.
- Nearby work explicitly distinguished: lattice GEVP and moment methods,
  sparse Hausdorff recovery with minimum weight and separation, mixed-measure
  moment recovery, and Euclidean-correlator SDP bootstrap.

## Claims explicitly not made

- no globally minimax joint rate when filter depth and conditioning vary;
- no composite unknown-atom scan or growing-degree LAN theorem;
- no theorem for arbitrary MCMC output or data-driven burn-in/mixing estimation;
  the dependent theorem requires stationary bounded beta-mixing output with a
  certified envelope;
- no thermodynamic or four-dimensional Yang-Mills mass gap;
- no claim that the visibility premise is unique or weakest;
- no claim that the ANNNI numerics are a Wishart experiment.

## Audit record

- `verification/finite_window_gap_certificates/verify_all.py`: PASS, 2.4 s.
- `verification/statistical_gap_boundary/certify_statistical_boundary.py`: PASS,
  under one second, schema v4; includes the exact weighted margin, LAN, and beta-mixing fixtures.
- `verification/statistical_gap_boundary/verify_weighted_boundary.py`: PASS;
  exact identities plus 2,000 deterministic random-competitor checks over degrees 1--8.
- Independent adversarial proof review: PASS after adding the nonsingularity
  gate, fixing the experiment dimension, and removing a global-minimax claim.
- LaTeX: consecutive terminal builds completed with no undefined references,
  LaTeX warnings, or overfull boxes.
- Visual PDF QA: all 23 pages and all four figures inspected after the terminal
  build; no clipping, overlap, broken glyphs, or unreadable table was found.
