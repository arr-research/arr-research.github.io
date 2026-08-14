# Release QA

**Date:** 2026-08-14 (Europe/Stockholm)  
**Decision:** GO for ARR preparation; not yet deposited.

## Canonical PDF

- Title: *Universal Semiclassical Coexistence in Classical Compression of
  Phase-Lifted Coherent States: Dimension-Normalized Contacts and a Matched
  High-Fidelity Boundary Layer*
- Author: Lluis Eriksson
- Pages: 13
- Page size: A4
- Figures: 1 vector figure
- Bytes: 468,754
- SHA-256: `3848730dfd1e4883f8b9de9a63c5ae0c123cf389569829d671503e5cbfe642a6`

## Checks performed

- Full `pdflatex`, `biber`, `pdflatex`, `pdflatex` build: PASS.
- Undefined citations or references: 0.
- LaTeX/Biber errors or warnings in final logs: 0.
- Overfull/underfull boxes in final log: 0.
- All 13 pages rendered with Poppler and visually inspected: PASS.
- Figure generator executed from the packaged release tree: PASS.
- Declared Python dependencies: NumPy 2.5.1, SciPy 1.18.0,
  Matplotlib 3.11.1.
- PDF metadata title and displayed title: matched.
- Author spelling: `Lluis Eriksson`.
- `verify_semiclassical_frontier.py`: PASS in under 5 seconds.
- `verify_semiclassical_coherent_rdf.py`: PASS in under 1 second.
- Release `MANIFEST.sha256`: PASS.
- Independent hostile mathematical audit after repairs: GO.
- Primary-literature/editorial audit after repairs: GO.

## Not assessed

- External peer review.
- Independent replication outside the supplied deterministic replay.
- Lean or other proof-assistant certification.
- Numerical interval certification.
- AI-content screening.
- Scientific correctness by ARR; ARR is an archive, not a peer-review claim.
