Finite supplementary diagnostics for the entropy-budget manuscript.

Requires Python3, NumPy, SciPy and mpmath. Run geometry.py, renyi.py,
compound.py, minimax.py, bounds.py and independent_checks.py
from a writable copy of this folder. They perform deterministic finite
assertions and write their respective JSON results next to the script.
They do not access a network or a Windows-specific archival path.

geometry.py checks60 finite complex-subspace interlacing cases and36
finite branch-loss calculations. renyi.py checks72 tail cases,72 largest-
eigenvalue cases and72 recorded evaluations of the exact geometric power
sum (the latter are not independent equality assertions). compound.py
checks24 type-subspace information comparisons and72 compressed-noise
branch bounds. minimax.py checks144 noncommuting finite input cases with
exactly summed infinite thermal tails,54 thermal branch cases,96 spectral
tail cases and24 clipping cases. bounds.py checks240 scalar remainder and
clipping cases at220 decimal digits; the largest E=10^100 requires enough
precision to distinguish E-1. These are numerical diagnostics. They do not implement
a compound encoder or decoder, prove an infinite limit, establish coding
theorems, certify novelty, or constitute a ready Research Capsule.

independent_checks.py supplies the optical extension diagnostics:84 signal
bound cases,336 Gibbs-DPI cases,756 branch cases,2664 finite-rank detector
cases,15 thermal truncations and280 clipping cases (260-digit scalar work).
The signals array fields reverse_information, coherent_information and
EA_benchmark are NONNEGATIVE BOUND SLACKS, not the information values.
This exact portable audit script and its original output were copied
unchanged; its numerical diagnostics are not the analytical proof.

The scripts were separated from private preservation/network bookkeeping;
the supplied JSON files were produced by these exact portable copies.
Original working/audit packets and adverse outcomes are preserved privately.
The supplement manifest will bind the exact manuscript PDF and source.
