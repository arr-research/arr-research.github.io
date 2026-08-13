# Unified Grassmann transition and high-fidelity RDF replay

This archive accompanies:

Lluis Eriksson, *A Finite-Dimensional Nonanalytic Spectral Transition and
Exact High-Fidelity Rate--Distortion for Rank-r Born Prediction on Complex
Grassmannians*
(version dated August 13, 2026).

Requirements: Python 3.12, NumPy, SciPy, SymPy, and Matplotlib.

Run from this directory:

    python verify_grassmann_crossover.py
    python verify_grassmann_spectral_switch.py --d 5 --r 2
    python generate_d5r2_example.py
    python verify_high_fidelity_grassmann_rdf.py

On the frozen development machine all four commands complete in approximately
6.3 seconds total with one process each and no heavy computation.

The scripts check:

- exact quadratic, cubic, balanced-quartic, complement, and slope identities;
- bounded deterministic and Monte Carlo diagnostics for the canonical spectra;
- the exact d=5, r=2 Gauss--Jacobi comparator crossing and Figure 1;
- rational normalization, Selberg, complement-scaling, and high-rate identities
  through d=18, plus independent rank-two quadrature.

The JSON files are frozen outputs of these commands. Numerical diagnostics are
not used as substitutes for the analytic global-optimality, nonanalyticity, or
rate--distortion proofs.
