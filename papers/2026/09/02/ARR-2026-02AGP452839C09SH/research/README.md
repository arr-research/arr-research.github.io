# Ternary Weyl research package

Author: Lluis Eriksson. Date: 6 September 2026.

This is a new internal research result, not a publication update. The earlier ARR paper and its archived evidence have been left unchanged.

- `ternary_low_rank.md`: self-contained manuscript, including all universal proofs.
- `ternary_verify.py`: standard-library exact replay; run with Python 3.10 or later.
- `ternary_certificate.json`: generated finite certificate, with manuscript and verifier hashes.
- `sources_and_scope.md`: inspected antecedents, literature and rejected overclaims.
- `reading_ledger.json`: machine-readable version and reading scope.

Run `python ternary_verify.py`. The recorded replay completed with PASS in approximately 1.5 seconds on Python 3.12. It tests all 4,095 nonempty affine-line subsets, exact matrices in dimensions 9, 27 and 81, and 6,320 ordered label pairs in dimension nine. It has no third-party dependency and uses no numerical rank threshold.

The main theorem classifies the entire exact three-list stratum below rank 7d/9 for d=3^k, k>=2. It gives 150 disjoint simplex interiors, their spectra and unique line decompositions, the exact minimum number of three-sparse squares, and the twelve states allowing only two labels. It also proves an infinite four-label family of rank 4d/9 and a three-label family of rank 5d/9.

The construction replay is not an independent review. Separate review, once performed, belongs in its own report with the reviewed manuscript hash. The PDF is to be produced from the reviewed source by the parent task. No external submission, new ARR record, message to a third party, or publication was performed by this constructing agent.
