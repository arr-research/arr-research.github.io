# Major-revision ledger

## Reviewer requests implemented

| Review point | Revision |
|---|---|
| Non-rejection could be misread as a positive gap certificate | Title changed from *Inference* to *Falsification*; the abstract, first page, Wishart section, limitations, and conclusion now state the one-sided direction explicitly. |
| Endpoint atom may conflict with a theoretically unique vacuum | The hidden atom is generalized to every `x_* in [0,1]`; a corollary puts it at `x_*=exp(-g)<1` and proves arbitrarily small strictly positive gaps in every noisy finite window. |
| Gaussian lower bound used only a zero-gap endpoint | The Le Cam theorem now uses `phi_N(x_*)`, covers every `x_*>theta`, and gives positive-gap alternatives tending to zero with a uniform fixed-window continuity argument. |
| Relationship to the earlier technical manuscript was unclear | The novelty section identifies *Noisy Euclidean Correlators Do Not Certify a Spectral Gap Without Visibility* as an unpublished draft replaced by this manuscript; it was never submitted and must not be counted separately. |
| Wishart overlap with the reflection-positive paper was implicit | A dedicated paragraph cites *Reflection Positivity and Exact Gap Certificates from Forgotten Quantum Order*, identifies the shared Loewner device, and separates the present identifiability and power contributions. |

## Additional strengthening beyond the review

- Sharpened the Chebyshev population bound from
  `theta alpha_N^2-delta gamma` to
  `theta alpha_N^2(1-gamma)-delta gamma`.
- Proved this sharpened visibility envelope is attained exactly by
  `(1-gamma) delta_0 + gamma delta_(theta+delta)`.
- Added a distribution-free bounded-readout theorem:
  paired differences remove an unknown mean, the exact statistic range gives a
  Hoeffding test, and a finite filter bank can be searched without splitting.
- Added an explicit power bound and a rational calibration fixture for the
  bounded test.
- Extended the standard-library replay to certify the near-critical Gaussian
  fixture, sharp envelope, Wishart threshold, and bounded finite-bank threshold.

## Second-review corrections and further strengthening

- Removed the visible `fixed commit fixed Lean source` marker. The PDF now
  prints the full immutable Lean commit, exact source path, axiom-audit path,
  and PR URL.
- Replaced the mutable verification link by the exact public repository commit
  `25f068c61905adb039f3b46f53ef23f5be9cc507` and its archived paths.
- Replaced the unqualified companion citation by the canonical companion-PDF
  SHA-256 while moderation is pending.
- Made `distribution-free within the bounded-iid model` the standing qualifier
  for the iid Hoeffding branch.
- Added a new theorem for a single strictly stationary bounded beta-mixing
  trajectory. It proves an explicit lag-covariance bias, Berbee coupling error,
  finite-bank level, power inequality, and elapsed chain horizon.
- Added the geometric-mixing corollary and a certified calibration with
  `beta_mix(q) <= 2^(-q)`: 68,527 paired blocks, lag 23, and a trajectory horizon
  of 3,152,220 steps for the displayed rational fixture.
- Upgraded the standard-library replay to schema v3, checking the near-critical
  atom and every dependent-data constant without heavy computation.

## Final pre-submission correction

- Converted the editorial status from replacement to **NEW SUBMISSION** after
  the author confirmed that no earlier version was uploaded.  No cancellation
  or replacement action is required.
- The PDF now calls the former title an unpublished draft, so it cannot be
  mistaken for a separate public paper or an ai.viXra replacement target.
- Printed the complete immutable GitHub URL for the exact/Krylov/ANNNI
  artifacts and the complete Colab entry-point URL directly in the PDF.
- Replaced the unverified editorial label `submitted manuscript` for the
  reflection-positive companion by the neutral `companion manuscript`; the
  canonical PDF hash remains until a public identifier can be verified.

## Scope retained

- No thermodynamic or Yang-Mills mass-gap claim.
- No globally minimax rate when the filter and covariance conditioning vary.
- No claim for arbitrary MCMC output, unknown burn-in, or a mixing rate inferred
  from the tested trajectory; the dependent theorem requires stationarity and
  an independently certified beta-mixing envelope.
- No claim that separated-mass visibility is the unique or globally weakest
  identifiability hypothesis; exact necessity is asserted only for uniform sign
  detection in the declared normalized scalar polynomial-localizer class.

## Third-review scientific upgrade

- Replaced the first-kind uniform stop-band construction by the exact
  fourth-kind weighted-localizer solution.  A weighted alternation theorem now
  proves
  `inf max sqrt(theta-x)|r(x)| = sqrt(theta)/W_N(y_delta)`.
- Proved an exact worst-case visibility theorem, attained by a two-atom
  measure.  The sign threshold is necessary and sufficient for uniform
  detection within the declared normalized scalar polynomial-localizer class.
- Added the exact hidden-atom Gaussian likelihood: its whitened covariance has
  one eigenvalue `1+w(beta-1)` and `d-1` eigenvalues `1-w`.
- Derived the LAN central sequence, Fisher information, sharp local power
  envelope, and the powerless/local/consistent trichotomy at the
  `w sqrt(n)` scale.  The theorem is explicitly fixed-window and fixed-path.
- Added a closed depth--sample resource frontier with a tunable retained-margin
  fraction.  It is labeled achievable, not jointly minimax when degree and
  conditioning vary.
- In the rational degree-two fixture, the weighted loss improves from `1/98`
  to `1/722`, the margin from `41/980` to `353/7220`, and the uniform sign
  threshold drops from degree two to degree one.  Sufficient counts improve to
  265,339 Gaussian sketches, 94,340 raw bounded observations, and 100,354
  retained beta-mixing readouts over 2,308,120 chain steps.
- Added an independent standard-library verifier, a two-panel boundary figure,
  and scoped citations distinguishing classical Chebyshev alternation and LAN
  from the paper's spectral-gap specialization.

## Final editorial correction

- Corrected the cross-reference in the proof of Corollary 6.4 from the
  counter-generated “Theorem 6.3” to the exact designation “Proposition 6.3”.
  No formula, proof step, numerical value, page count, or submission metadata
  changed.
