# Two-state exact routing: algebraic feasibility and sharp delay-two rigidity

Lluis Eriksson. ARR-2026-03PY6WTF258KGSRN v1. The canonical article is paper.pdf; paper.md contains all formulas. paper.txt is extracted prose and is not a complete mathematical transcription of image equations.

## Reproduce

Install Python, NumPy and SymPy with `python -m pip install -r requirements.txt`. Run `python replay.py --fresh-lr --report ../my-replay.json`. Both scientific checkers run in a disposable copy. The flag forces independent LR reconstruction in the commutator paper; otherwise a matching cache may be reused. In the other papers it has no effect. SciPy is only needed to rerun exploratory proposals.

research/ preserves the scientific programs and certificates. Historical internal reports retain their original hashes and scope; screening/history/ contains the completed extra-high audit and its accepted delta. The new source differs from that accepted source only in publication labels and authorization wording, shown in screening/publication-only.diff. The networks checker's expected source hash was updated for these labels; mathematical checks are unchanged. FINAL_REPLAY.json records the publication-package execution; the final exact-artifact AI check is in screening/.

The producing and reviewing model family is GPT-6 Astra. This is internal AI screening, not independent human peer review. The author-operator conflict and delegated publication decision are explicit in DEPOSIT_DECISION.json. Historical numerical grades are not silently imported as assessments of these new PDF bytes.

Source releases omit the PDF by archive convention: download the separate PDF asset as paper.pdf before checking every line of MANIFEST.sha256. The typesetter requires ReportLab, Matplotlib and Pillow. Each original scientific result, its hypotheses and its remaining open problems are stated in the article.
