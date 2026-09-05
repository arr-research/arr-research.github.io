# Polynomial vertex reduction and optimal stability at balanced inertia (4,4)

Author: Lluis Eriksson. Final edition, 5 September 2026.

The canonical artifact is paper.pdf; paper.md is its complete typesetting source. Theorems A–B give the finite general reduction and the optimal 4/7 constant; Theorem C adds the full equality set and strictness on the exact (4,4) stratum. The earlier public inertia-ceiling article is a distinct antecedent cited in the manuscript.

From this directory, Python 3.12 or later:

```text
python verify_balanced_four.py
python independent_lr_geometry_review.py
python algorithm_certificate_replay.py
python verify_contacts.py
```

These checks use only the standard library. The first reconstructs the geometry and recursive Horn rows; the second reconstructs geometry and Horn rows by Littlewood–Richardson tableaux; the third replays the rational primal–dual certificates; the fourth checks the complete contact-set certificate and midpoint. Written arguments establish the universal geometry, convexity/concavity and ambient-dimension extension. Horn sufficiency is imported, not formalized.

Optional checked certificate construction:

```text
python -m pip install -r requirements.txt
python certified_constant.py --N 4 --ambient 8 --output regenerated_optimal_constant.json
```

NumPy/SciPy supply proposals; exact rational checks decide acceptance. A numerical failure stops the constructor instead of issuing an uncertified result. Use a separate output name to preserve the deposited original certificate. The finite count is polynomial in multiplicity, but neither the number of Horn constraints nor total running time is claimed polynomial.

screening/ contains the final version-specific internal assessment. Evidence inherited from the previous edition is labelled separately; no independent human refereeing, proof-assistant verification, exhaustive novelty review, or external model score is claimed. DEPOSIT_DECISION.json documents the author-directed deposit and editorial conflict.


## Published assets and safe replay

ARR releases the canonical PDF separately from the source ZIP. Extract the sources and save the separate PDF in that directory as `paper.pdf` before checking the complete `MANIFEST.sha256`. The canonical PDF hash is also recorded in metadata.json. `paper.md` contains all machine-readable mathematics; ordinary extraction into `paper.txt` omits embedded formula images.

Verify the supplied hashes before running the scripts. Scientific replays write result JSON files, sometimes including runtime measurements, so run them in a working copy if you wish to preserve the deposited certificates and their hashes. A different elapsed time does not alter an exact mathematical result. The final, version-specific internal report is in `screening/final-internal-review.md`; the author-editor decision and pending subsequent Astra review are documented separately. `AUDIT_PROMPT_ASTRA.md` is ready for that future review and contains this PDF's exact identity.

The root files review_pdf_correspondence.py, review_pdf_text.txt and write_review_final_delta.py preserve preparatory audit evidence cited by hash. They retain preparation-specific paths and are not required scientific replays. The five portable scientific replays are those documented above, together with review_final_delta_check.py (a second contact check using the separate LR construction).
