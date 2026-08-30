# Final PDF and package QA

Original QA date: 24 August 2026 (Europe/Stockholm)  
Final rendered QA: 30 August 2026 (Europe/Stockholm)

Artifact: `output/pdf/One_Spike_Inverse_Selfcommutators_and_Exact_Switching.pdf`

## Mechanical checks

- Final PDF: 9 pages, 341,892 bytes.
- SHA-256: `0F45A998063E687CC689B8E43C2887194C0937C8587C34B783A1631F8974776D`.
- Metadata: title and author (`Lluis Eriksson`) match the manuscript; 44 link annotations are present.
- Extracted text contains all structural markers required by `package_release.py`.
- Final LaTeX and BibTeX logs contain no warnings, overfull or underfull boxes, missing characters, or unresolved references.

## Visual inspection

The final 30 August PDF was rendered with Poppler and all nine pages were
inspected at high detail after the last proof, provenance, and bibliography
edits. No clipping, overlap, broken glyphs, malformed formulas, bad margins,
or citation-layout defects were found. The compact bibliography occupies pages
8--9 without an orphaned reference; the whitespace following it is intentional
and acceptable.

## Scientific and reproducibility gates

- Independent mathematical re-audit: unconditional PASS.
- Independent priority/bibliography re-audit: unconditional PASS.
- Exact rational replay: PASS on 160 balanced-quadrilateral/flux fixtures,
  the corrected Gram certificate, the counterexample to the discarded step,
  and 15 one-spike/reflected/zero-padded constructors.
- Independent SymPy replay: PASS on exact matrices, singular spectra,
  stability, triangular and quadrilateral constructors.
- Both replay-result hashes were verified by the fail-closed runner.
- Python release and replay scripts compile without syntax errors.

Result: **PASS for local release packaging.**

This QA result is local. It is not peer review or formal proof certification.
