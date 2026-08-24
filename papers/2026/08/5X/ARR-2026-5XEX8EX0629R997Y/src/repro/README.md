# Replays

Run python run_all_replays.py from this directory. The combined report is
written to results.json.

The replay has three deliberately separated roles:

- verify_truncated_tjurina_floor.py checks the binomial optimization with
  exact integer arithmetic on the finite grid
  \(1\le d\le8,\ 1\le s\le20\), and checks selected local quotient matrices
  over two large prime fields.
- verify_plane_sharpness_exact.py computes exact Gröbner bases over
  \(\mathbb Q\) for the sharp plane family for \(1\le s\le12\).
- explore_monomial_defects.py records exploratory higher-dimensional
  Milnor/Tjurina fixtures. Its former naive defect-product pattern is not a
  theorem and is not claimed in the manuscript.

These finite computations do not prove the universal theorems. The
Euler-reduced dimension count and the prescribed-jet argument in
manuscript.tex carry those claims.
