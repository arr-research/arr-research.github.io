# A sharp two-rate reset witness against static qutrit disorder

**Working paper.** Lluis Eriksson · ARR-2026-131G33B01486YA04 · v1 · 13 October 2026.

Canonical manuscript: paper.pdf, 10 pages, SHA-256 9bc3067af8f7a5a3135bf7bea2945bb6210e936b4aa36890d1f06f415f821e60. Editable source: qutrit-paper.tex. The text renditions are extracted from the PDF; consult the PDF for mathematical typography. Its preparation-time “research candidate, not deposited” line is retained to preserve the exact authorized bytes; the catalogue records the subsequent public deposit.

The paper proves a sharp two-rate witness against static qutrit Hamiltonian disorder, an exact selected-statistic approximation infimum of 1/45 with nonattainment, and a noisy population-calibration extension. The witness does not exclude classical time-dependent noise or establish a quantum environment. Experimental tolerances and sampling costs are stated explicitly in the manuscript. Global priority is not certified.

## Reproduce

Use Python 3.12 and the versions in requirements.txt. Run `python qutrit_verify.py` and `python robust_calibration_check.py` from this directory. The first yields 26 exact symbolic checks; the second tests 1000 random matrices in dimensions 2–6. The scripts overwrite their own JSON outputs, so use a copy if preserving the deposited outputs. Neither script accesses the network. The numerical test supplements the analytic proof and cannot establish it.

## Advisory reports

Both prior-draft reports are available in reviews/, together with the exact source they examined and the dated response. Astra's AIRR relevance score is 6.0/10; Opus's is 3.6/10. These unchanged scores apply to the preceding nine-page draft. No new score is assigned to the ten-page PDF. The author is also the AIRR operator; publication as a Working paper does not constitute human peer review or admission to the accepted collection.

Manuscript: CC BY 4.0. Metadata: CC0. Verifier code: Apache 2.0. Generated results: CC0. See LICENSES.json and PROVENANCE.json.
