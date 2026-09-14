# Exact-candidate local checks: B3

PDF SHA256: `810df760794f04ec3d423f157d6c6e4a30f9651545d636994fc5ce35eebdb654`

Recommendation: minor_revision. Overall: 4/10 (strong); Millennium score: 4/10.

## Checked

- PDF SHA256 matched; 14 pages extracted; proof page 4 and normalization/Bessel page 7 visually inspected.
- Sections 3-8 main mathematical derivations independently followed, including denominator positivity, first-zero argument, stationary-point classification, Danskin derivative, scaling and exceptional q=1,2 Riccati identities.
- sym_riccati.py passed: exact rational consequences and explicitly finite Taylor matches.
- candidate_checks.py passed: eight exact correction identities; 18 Beta cases and six q values at 900 grid points each, 45-digit arithmetic.
- Fresh independent.py: exact transversality and tangency derivative; five Beta-density quadrature checks at 100 digits; maximum relative discrepancy about 1.73e-27.
- Primary DLMF equations, Fatkullin-Slastikov theorem and Sra-Karp monotonicity/bounds inspected.

## Not checked

- Historical 744-case grid and all manuscript/reviewer scripts were not rerun.
- No complete independent verification of cited private AIRR antecedent papers or their report-attribution history; their rate-distortion consequences are assessed as stated conditional imports.
- No exhaustive novelty search; no theorem proving the oriented-two-plane Delta sign pattern.

## Minor issues

- Related-work discussion omits Sra and Karp (2013), whose general Kummer-ratio monotonicity and inverse bounds are especially close background. A 2024 integrable-bounds paper was located but full text access failed, so that comparison remains incomplete.
- The hypothetical tangency at m_f=1/2 can actually be excluded: D=0,D'=0 there imply D''=16(c+1)(1-2mu)>0, incompatible with D<0 immediately to the left. This sharpens, rather than invalidates, Theorem 4.1.
- Numerical coverage is bounded; no finite grid certifies all parameters or zero counts.

## Potential errors

- Nonmaterial domain typo in Theorem 4.1 proof: [m_f,infinity) should be [m_f,1).
- Subdifferential formulas at the boundary lambda=0 should be read for positive lambda or with the appropriate one-sided convention.

## Execution and independence

Fresh delegated task context; other model reports, prior scores, source diffs, provenance files and editorial registries withheld. The configured model family participated in revision assistance. The candidate itself describes prior review findings, which were visible and were not treated as evidence. No technical claim that model memory is disabled.

All executed supplied scripts inspected first and run from a separate workcopy; no pickle loading. The independent reviewer harness initially used beta(a,c) instead of beta(a,c-a), causing two failed harness attempts; corrected normalization passed. Those failures are retained and are not manuscript failures.

Local preassessment only. No SID/intake assessment, human acceptance, private deposit or public permission is created by this report.

## Primary sources

- [NIST DLMF Kummer equation](https://dlmf.nist.gov/13.2#E1)
- [NIST DLMF integral representation](https://dlmf.nist.gov/13.4#E1)
- [NIST DLMF Kummer-Bessel relation](https://dlmf.nist.gov/13.6#E9)
- [NIST DLMF large-argument expansion](https://dlmf.nist.gov/13.7#E1)
- [Fatkullin and Slastikov, Critical points of the Onsager functional on a sphere (Theorem 3, Section 3.1)](https://www.math.cmu.edu/CNA/Publications/publications2005/005abs/05-CNA-005.pdf)
- [Sra and Karp, The multivariate Watson distribution (Theorem 3.1 and Appendix A)](https://optml.mit.edu/papers/2013_sra_karp_jmva.pdf)

## Actual logs

- `sym_riccati.log`: SHA256 `559aeeb206b8da6a64c8833c9a84c35e63b475e3610785e55dd096b92df9509c`
- `candidate_checks.log`: SHA256 `43a082d1419aa05372b8d7d39f21f62444483ef5c680fd6608f72ce99134173a`
- `independent.log`: SHA256 `337074131107b40ca63b2d71da9c91f192f62f1f123af5d8be1a86ed873ba1fb`
- `independent-attempt1.log`: SHA256 `c9a9df88aaf92617a3a587ad74b41212eb9bc98f4f18cdaea22719b3e6619f19`
- `independent-attempt2.log`: SHA256 `3b6a671a5809eb6be35f3c1b27537741a3aca8e930e6827c72351ed190710396`
- `independent.py`: SHA256 `f3a63ea58737cc6c4e75980396c8f8eb9bca3cd977efffdaaaf464465c29d7de`
