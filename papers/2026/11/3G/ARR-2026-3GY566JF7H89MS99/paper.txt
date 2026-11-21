     How many spectral shapes does the VLA correction table for
                          3C 138 require?
                                                 Lluis Eriksson
                                                 November 2026


                                                     Abstract
          During its radio outburst, 3C 138 changed brightness differently at different frequencies. We ask how
      well a time-dependent amplitude and a fixed frequency profile can represent the public VLA correction
      factors. For 47 monthly entries in eight bands, the smallest possible worst relative error of this repre-
      sentation is 28.94%. Four entries give the lower bound and a factorization of the full table attains it
      numerically. With one amplitude per month and separate frequency profiles on contiguous periods, six
      profiles are necessary and sufficient for a 5% tolerance. We give the break dates and the band and month
      factors. These are bounds for representing a particular table, rather than estimates of the uncertainty in
      astronomical flux measurements.


1    A question about calibrating a variable source
The NRAO recommends accounting for the flare of the flux calibrator 3C 138 and provides a table of time-
and band-dependent scaling factors [1]. Multiwavelength observations document spectral hardening during
the outburst [2]. Consider a reduction that stores one reference value per band and updates a single amplitude
each month. Could those choices, optimized after seeing the entire table, approximate every published factor
to within a specified tolerance? This matters when deciding whether archived reduction metadata with a
single time-dependent scale can encode the published calibration.
    We use the CSV linked by the VLA Observing Guide [1], filename ending in 2025-03-06.csv. It contains
47 monthly rows from February 2021 through December 2024 and eight labeled columns L, S, C, X, U, K,
A, Q. We retain the column names as supplied. Each of the 376 entries is positive. Our unit of analysis is
the tabulated factor. No raw visibility data or target measurements enter the calculation.


2    A check using four entries
Write Fib for a published factor and model it as ai sb , with positive monthly amplitudes and band factors. In
log space set t = maxib | log(ai sb /Fib )|. The alternating sum of the four model logs on any rectangle of months
and bands vanishes. Consequently the corresponding data log cross-ratio has absolute value at most 4t. For
L and Q the February 2021 row gives (1.013134, 1.132233) and the December 2024 row (1.009391, 3.714359).
These entries alone require exp(t) ≥ 1.347066 to displayed precision.
    Log-Chebyshev rank-one approximation is an established problem [3]. Here a matching upper bound
comes from fitting all entries by linear programming in the log factors and checking the residuals. To express
the answer as an ordinary relative error e = max |ai sb /Fib − 1|, the smallest feasible interval of log residuals
has width 2t∗ . Centering the multiplicative scale so that its endpoint ratios are 1 − e and 1 + e gives
e∗ = tanh(t∗ ). Both bounds agree numerically within 10−8 in log units.




                                                          1
3    The minimum number of contiguous periods
Allow a distinct band profile on each contiguous period, with a free amplitude in every month. For a
proposed ordinary error ϵ, put t = atanh(ϵ) and Lib = log Fib . Eliminating monthly log amplitudes gives the
constraints
                         vj − vk ≤ 2t + min (Lij − Lik )          for every pair j, k.
                                         i in period

Indeed the allowed intervals for the monthly amplitude overlap exactly when all these inequalities hold.
The band constraints are feasible precisely when their difference graph has no negative cycle. Shortest-path
distances yield band offsets; the midpoint of each month’s allowed interval yields its amplitude. A common
rescaling converts the log-error witness to the desired ordinary relative-error convention.
    Feasibility passes to every shorter interval. Thus selecting the longest feasible initial period is optimal:
in any optimal partition, extend its first period to this endpoint, discarding covered periods and shortening
the next one if necessary. Repeat on the suffix. We also computed the minimum by dynamic programming
over all intervals, checked the supplied factors at every entry, and checked each greedy endpoint and its
one-month extension (when available) by a separate linear program.

                   Months and bands              Minimum worst relative error, one profile
                   All months, L through Q                        28.94%
                   2024 only, L through Q                         11.22%
                   All months, L through X                         5.72%
                   All months, K, A and Q                         11.86%

                   Allowed relative error (all months and bands)      1%    2%    5%    10%
                   Minimum number of contiguous profiles              24    14      6      3

At 5%, one optimal partition starts in February 2021, March 2022, March 2023, October 2023, April 2024
and September 2024. These dates depend on the tolerance and on the chosen table. They do not locate
physical changes in the emission mechanism. The CSV stops in 2024; applying its final factors to later
observations would require further evidence. Measurement error, spatially resolved structure, and errors in
calibrated target fluxes are outside the bounds proved here.

Reproduction and review context. The accompanying scripts static-shape.py and epochs.py ver-
ify the CSV checksum and return lower-bound entries, constructive factors, and numerical checks. Model
assessments and review context: AI assisted with the analysis and writing. A subsequent assessment refers
to the identified PDF in its separate review record.

References. [1] NRAO, VLA Observing Guide, Calibration, linked monthly scaling-factor table for 3C 138.
   [2] T. V. Mufakharov et al., A broadband outburst of the compact steep-spectrum quasar 3C 138 in 2024–
2026, MNRAS, doi:10.1093/mnras/stag2220.
   [3] N. Krivulin, Rank-one approximation of positive matrices based on methods of tropical mathematics
(2018).




                                                       2
