# Version 0.6 release notes

This archive is the canonical, self-contained distribution of
*Cellulation-Independent Boundary Gauge Averaging and Sharp Class-Sector Gaps
in Two-Dimensional Yang--Mills*.

Version 0.6 responds to the three proof-interface objections in the independent
review of version 0.5. It does not enlarge the historical novelty claim.

## Strengthened finite-dimensional proof

- The boundary-conditioned amplitude now has an explicit conditional-Haar
  coordinate formula.
- A canonical-fibre lemma proves independence of the eliminated boundary edge
  and covers subdivision of that edge.
- The PL radial arc is inserted by a finite sequence consisting exactly of the
  two analytically invariant moves: edge subdivision and face subdivision.
- The disk identity now has a complete primal-tree/dual-cotree elimination
  schedule, including the choice of boundary edge, the Haar-preserving gauge
  coordinates, the leaf order, and the final convolution.

## Verification

- The numerical replay still terminates with `REPLAY: PASS`.
- The scalar gap target builds successfully in the exact pinned environment:
  2,817 jobs.
- The exact boundary-conditioned branch builds successfully: 3,097 jobs.
- The four new scalar endpoints use only `propext`, `Classical.choice`, and
  `Quot.sound`.
- The complete archive is covered by `MANIFEST.sha256`.

The compact-group and PL-topological extension remains a paper proof rather
than a monolithic Lean theorem; the release continues to state this boundary.
