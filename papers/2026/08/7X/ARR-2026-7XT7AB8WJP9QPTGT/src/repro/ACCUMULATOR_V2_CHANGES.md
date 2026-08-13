# Accumulator v2 and centred-binary64 export v2

After extracting `riemann-prime-resolvent-3d997887-source.zip`, overwrite the
three corresponding files with those under `patched-source/` and copy the
regression test into `tests/`.

The corrected files make six fail-closed changes:

1. accumulate python-flint matrices through `full_bands[index]`, because
   augmented assignment on the loop variable only rebinds that variable;
2. widen each stored entry radius by the Arb radius, the binary64-centre ulp,
   and outward rounding at both arithmetic conversions;
3. mark generated proof objects as format 3 with accumulator version 2 and
   float-export version 2;
4. export the rational smooth remainder upward by construction;
5. retain positive other-tail divisions and row/column sums in outward-rounded
   arithmetic;
6. reject malformed, nonfinite, negative-radius, or nonpositive-trace explicit
   bands before Schur adjudication.

The focused tests cover the original zero-band regression, midpoint-export
containment, interval sum consistency, and cache-loader rejection.
