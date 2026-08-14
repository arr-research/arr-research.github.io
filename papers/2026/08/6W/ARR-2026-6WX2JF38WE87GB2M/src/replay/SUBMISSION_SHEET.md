# Submission sheet

- **Record type:** research paper
- **Author:** Lluis Eriksson
- **Title:** Algebraic Query Support for Unitary Oracles: Exact Hilbert Laws, Harmonic Spectra, and General-Tester Bounds
- **Primary area:** Quantum Physics
- **Secondary area:** Mathematical Physics / Quantum Information
- **Status:** independent new work; not a replacement
- **Related ARR record:** ARR-2026-5KS70GV7KK9DYA69. That paper proves the $k=2$ fixed-trace defect and causal saturation for a specific tetrahedral 24-echo ensemble. This work generalizes the dimension law to all $k$ and arbitrary fixed-angle subsets, extends the cap to compact-orbit GEN testers, and adds branch-resolved sphere/circle spectra; it does not reuse the ensemble-specific attainment certificate.

## Abstract

The usual dimension bound for discrimination with k calls to a d-level
unitary oracle is the ambient symmetric-tensor count. We show that causal
forward-query support is instead the degree-k Hilbert function of the
projective oracle variety. For fixed-angle qubit rotations with unknown axis,
the exact rank is `(k+1)^2`, with separate traceless and central branches. A
constant-leverage orbit argument then refines the ultimate general-tester
success bound to `P_succ <= min(1,D_k/M)` for every uniform finite subset.
For rank-one selective-phase oracles in dimension `d`, the projective closure
is a transformed Segre variety and the exact support is
`binom(k+d-1,d-1)^2`, reducing the ambient growth exponent from `d^2-1` to
`2d-2`.
The continuous query frame is diagonalized exactly by spherical harmonics,
yielding closed spectra, purity, endpoint cascades, and a linear effective rank
inside quadratic algebraic support. Bell tightness is isolated to one query,
and no positive reweighting restores it at higher query number. A great-circle
restriction changes the quadratic rank law to `2k+1` and admits an exact
Fourier spectrum. The work refines a classical orbit-domination method; it
does not claim a new tester formalism or physical realizability of every
general process matrix.

## Suggested keywords

quantum query complexity; unitary channel discrimination; Hilbert function;
oracle varieties; Segre variety; SU(2) conjugacy class; general quantum testers

## Limitations

- The arbitrary-variety theorem is causal; the GEN extension needs a compact
  transitive orbit.
- Perfect-identification query counts are necessary, not sufficient.
- Controlled-U, U-dagger, postselection, and changed oracle models are not
  included.
- The exact verifier checks finite identities and is not machine-checked proof
  of the general theorems.
