# Verification report

- Record: `ARR-2026-15SJ1ANHDN8D88Z1 v1`
- Protocol: `ARR-VERIFY-1.0`
- Canonical PDF SHA-256:
  `a955a5e4a05adbef081a8fbb0c8a76f46b2027eca35a0be0dbaf82a607fbb8a2`
- Canonical PDF size: `462877` bytes
- Canonical PDF geometry: 20 A4 pages

## Checks performed

1. Recomputed the canonical PDF SHA-256, byte count, page count, title,
   authorship metadata, and A4 page geometry.
2. Compiled the preserved LaTeX source with MiKTeX `pdflatex` and `bibtex`.
   The final log contained no unresolved citations or references, overfull or
   underfull boxes, or LaTeX/package warnings.  Consecutive final builds were
   byte-identical to the canonical PDF.
3. Rendered all 20 pages with Poppler and visually inspected them for clipping,
   overlap, broken equations, malformed tables, and missing text.  A literal
   `qquad` in the query-threshold equation was corrected before the final
   freeze and the affected page was rerendered.
4. Ran `verify_list_matroid_union.py`: **PASS**.  It checks 240 exhaustive
   union-rank cases, exact list/simplex fixtures, strict-flat and process-rank
   fixtures, and the retained correlation-only regression fixture.
5. Ran `verify_exact_qubit_separation.py`: **PASS**.  It replays the exact
   primal--dual value `(2+1/sqrt(3))/3` for the union-full counterexample.
6. Ran `verify_laminar_channel_phase.py`: **PASS**.  It checks 70 exact
   `(h,s,q)` phase cases and an arbitrary-prior transcript-partition fixture.
7. Ran `verify_multitime_ueb.py`: **PASS**.  It checks complete-UEB spectra,
   Weyl-history fibres for small exact instances, Schmidt-rank caps, and the
   fixed-probe list primal--dual value.
8. Rebuilt the supplied pre-deposit reproducibility archive twice and after a
   fresh extraction; its bytes and SHA-256 were identical.  The ARR release
   packages the preserved pure sources and replay scripts independently.
9. Performed a targeted primary-source priority audit.  In particular, the
   one-use complete-UEB success formula is explicitly credited to Feng, Duan,
   and Ji, *Physical Review A* 74, 012310 (2006).  This was not a complete ARR
   bibliography protocol or specialist novelty review.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial**.  The executable evidence checks exact finite
  fixtures and formula identities; it does not formally prove the universal
  analytic theorems.
- Bibliography: **partial**.  Targeted primary-source checks were performed,
  but no complete database or specialist audit is claimed.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific validation: **not assessed**.

ARR publication records technical preservation and the checks above.  It is
not an independent finding that every theorem or novelty claim is correct.
