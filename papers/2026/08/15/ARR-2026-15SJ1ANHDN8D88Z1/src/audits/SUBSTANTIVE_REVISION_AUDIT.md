# Substantive revision audit

This revision is not a repackaging of the 7.50 manuscript.  It preserves the
matroid-union theorem and replaces the weak correlation-only process example
by two input-dependent channel sections.

## Added results

1. Exact reduction of deterministic dephase--prepare channels to transcript
   partitions for arbitrary priors and list budgets, valid against entangled
   parallel probes.
2. Exact Bellman recursion for adaptive strategies with arbitrary retained
   quantum memory.
3. Closed laminar phase
   `P_parallel=min(1,ell(q+1)/M)` and
   `P_adaptive=min(1,ell*2^q/M)`, with exact perfect-list query thresholds.
4. Process-list translation of the known complete-UEB dense-coding spectrum
   law, an exact multitime Weyl wiring trichotomy, and a fixed-probe example
   where the coarse list-rank cap is strict.

## Priority corrections

- The one-guess UEB spectrum identity is credited to Feng, Duan, and Ji,
  *Physical Review A* 74, 012310 (2006), and is not claimed new.
- Adaptive channel advantages and membership-query learning are credited as
  established.  The laminar theorem is presented as an exact list/feedback
  phase in a specified family, not as a quantum advantage.
- The carrier-only `SER_0` resource class is not identified with all
  sequential strategies.

## Verification

- `verify_list_matroid_union.py`: exact core hierarchy and fixtures.
- `verify_exact_qubit_separation.py`: exact primal--dual counterexample.
- `verify_laminar_channel_phase.py`: 70 exact phase cases and arbitrary-prior
  partition fixture.
- `verify_multitime_ueb.py`: UEB spectrum, Weyl fibres, and fixed-probe
  primal--dual certificate.

All four replays pass with the Python standard library only.
