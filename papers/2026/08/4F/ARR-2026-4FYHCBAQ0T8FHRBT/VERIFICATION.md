# Verification report

Record: `ARR-2026-4FYHCBAQ0T8FHRBT v1`

Canonical source SHA-256:
`d5f0bfaaa28e066c3d99fad9581b083ebb4ea16697931a1975089655b613c40c`

## Mathematical audit

The final referee task reconstructed the universal lower bound, the
strong-Lefschetz equality family, the prescribed-list theorem in every
dimension (d\ge1), the separator degree (E-1), first-jet degree (E),
incidence codimensions, exact reduced support, absorption, dual multiplicity,
the complete plane spectrum, and the sharp threefold endpoint. It reported no
remaining P0, P1, or P2 mathematical objection.

Primary-source checks included Greuel--Lossen--Shustin Corollary 2.24 for
contact ((\tau+1))-determinacy, Parusiński for dual multiplicity, Wahl
Example 4.7 for the classical three-variable number, Stanley for strong
Lefschetz, and Canino--Gimigliano--Idà for the plane spectrum. Bibliographic
coverage remains selective rather than exhaustive.

## Exact replays

Command:

    python src/repro/run_all_replays.py

Final status: `pass`.

- exact binomial identity and maximizing truncation: (1\le s\le50);
- exact rational Lefschetz ranks: (1\le s\le8);
- direct Tjurina quotient fixtures over two primes: (2\le s\le7);
- simplex-lattice evaluation ranks: dimensions 1 through 4 on the documented
  finite grid;
- all integer decompositions in the documented surface-spectrum grid.

The replay results are deterministic and hash-bound in
`src/repro/results.json`. They certify fixtures only, not the universal
proofs.

## LaTeX and visual QA

MiKTeX pdfTeX 1.40.28 compiled `paper.tex` twice with
`-interaction=nonstopmode -halt-on-error`.

- pages: 8;
- page size: A4;
- LaTeX errors: 0;
- undefined citations/references: 0;
- overfull boxes: 0;
- underfull boxes: 2, both harmless bibliography line breaks.

All eight pages were rendered at 150 dpi and visually inspected. No clipping,
collision, missing glyph, or malformed formula was observed.

## Limits

No Lean proof, formal verification, human peer review, independent
reproduction, exhaustive novelty search, or optimality of the degree
threshold is claimed.

