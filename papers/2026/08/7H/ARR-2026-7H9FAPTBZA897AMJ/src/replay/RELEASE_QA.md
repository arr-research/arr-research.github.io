# Unified Paper 12 release QA

Status: GO for ARR deposit as the definitive version superseding the all-field draft.

## Canonical artifact

- Title: Complete Rate--Distortion Phase Diagram of Haar Oriented Two-Planes: One-Change Hypergeometric Coefficients, Unique Coexistence, and No Reentrance
- Author: Lluis Eriksson
- PDF: `work/twelfth_paper/output/pdf/Eriksson_Complete_Rate_Distortion_Haar_Oriented_Two_Planes_UNIFIED_v1.pdf`
- SHA-256: `f8bd2e9ed5f8b166e014dd7b51578adc572dd603b37a82c1fde837b7d89488be`
- Bytes: `441916`
- Pages: 16 A4
- Figures: 1 vector figure

## Revision checks passed

- The title now leads with the complete phase-diagram result.
- The title page explicitly states that this version supersedes and absorbs the earlier all-field draft.
- The parity-window likelihood-ratio step is a standalone proved lemma.
- The two-derivative Gamma-tail estimate is a standalone proved lemma.
- The high-fidelity proof now cites Equation (21) with parentheses.
- The reproducibility section provides one replay command, a release seal, exact archive name, and archive SHA-256.
- The bounded one-command replay passes 6,783 coefficient signs, 297 exact tail bounds, global-phase identities, contact diagnostics, and figure generation.
- The manuscript now reports those exact replay counts and the scalar-contact range through `q=120`, so a reader can reconcile the frozen artifact without relying on an unquantified validation claim.
- `pdflatex`, `biber`, `pdflatex`, `pdflatex` completed successfully.
- No undefined references/citations, LaTeX/package warnings, or overfull/underfull boxes remain.
- PDF metadata identifies the final title and author.
- All 16 pages were rendered with Poppler and visually inspected at 120 dpi; the title page, central theorem, Gamma-tail lemma, replay seal, figure, and references were additionally inspected at full resolution.
- Canonical output PDF and `PAPER_12_FINAL.pdf` are byte-identical.

## Scope boundary

This is signed Pluecker-coordinate compression, not quantum rate--distortion or Born-probability prediction. The N-letter result is a mutual-information/capacity identity and strong converse, not an exact finite-codebook achievability theorem.
