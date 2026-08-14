# Final release QA

Date: 2026-08-14 (Europe/Stockholm)

## Canonical paper

- File: `output/pdf/Eriksson_Exact_Classical_Rate_Distortion_Phase_Lifted_Coherent_States_FINAL.pdf`
- SHA-256: `01678e31e1fc652a1d1b8c8b00023ad6bc192439bc27267a0abde4d4568ede51`
- Size: 374,586 bytes
- Format: PDF 1.5, A4
- Pages: 11
- Figures: 1 vector figure
- Author metadata: Lluis Eriksson
- Byte-identical to the final four-pass LaTeX/Biber build: yes

## Build and replay

- Build: `pdflatex`, `biber`, `pdflatex`, `pdflatex`; exit status 0.
- Final LaTeX/Biber scan: no errors, undefined references/citations, package warnings, or over/underfull boxes.
- `verify_coherent_orbit_rdf.py`: PASS; 728 dimension identities, 728 complement identities, and bounded diagnostics.
- `verify_slater_cartan_series.py`: PASS; 196 exact Weyl/hook/hypergeometric coefficient checks.
- No heavy local computation, branch-and-bound, pools, Colab session, or GitHub Action was used for release QA.

## Visual inspection

All 11 pages were rendered independently with Poppler at 130 dpi. The full contact sheet and selected full-resolution pages were inspected. No clipping, overlap, missing glyph, blank page, malformed equation, or illegible figure was found.

## Source package

- ZIP: `output/source/Eriksson_Coherent_Orbit_RDF_ARR_Source.zip`
- SHA-256: `6d2e9241e5d13c95439466cab5274060e9965220960a54a831096f280ecabb4e`
- Size: 378,412 bytes
- Internal manifest SHA-256: `605fa5a9abefb466b4a77563becc53a2e7026ab2731e8ebec9d3bfa0a2ba3406`
- Internal manifest verification: PASS

## Assessment boundary

The theorem package passed independent internal hostile proof and bibliography audits. This is not peer review, machine-checked proof certification, independent reproduction, or a guarantee of novelty. Those fields must remain `not_assessed` in ARR.
