# Statistical gap-boundary certificate

Run from this directory:

```powershell
python .\certify_statistical_boundary.py
python .\verify_weighted_boundary.py
```

The script uses only Python's standard library and finishes in under one
second. It certifies the rational near-critical Gaussian fixture, the exact
rank-one-spike KL/LAN identities, the fourth-kind weighted visibility minimax,
the filter-first Wishart threshold, and the bounded unknown-mean
finite-bank threshold. It also verifies the stationary beta-mixing calibration:
the coupling budget, lag bias, first sufficient paired-block count, retained
readouts, and total trajectory horizon. A successful replay prints `PASS` and
reproduces `statistical_boundary_certificate.json`.

The independent verifier checks the weighted alternation formula, exact
first-versus-fourth-kind rational fixture, exact covariance eigenvalues and KL,
and 2,000 deterministic random polynomial competitors over degrees 1--8.  It
reproduces `weighted_boundary_certificate.json`.  The phase-figure source is
`make_sharp_boundary_figure.py`.
