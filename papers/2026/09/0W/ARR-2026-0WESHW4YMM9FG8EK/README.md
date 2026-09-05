# Reproducing the quantum article

The article source is `quantum_weyl_trinomials.md`. Keep it beside `quantum_weyl_verify.py` and `composite_matrix_checks.py`.

Run `python quantum_weyl_verify.py` to regenerate the full exact finite certificate, or `python composite_matrix_checks.py` to run the direct composite-dimension checks separately. SymPy is the only dependency outside the Python standard library. The recorded Python and SymPy versions appear in `quantum_weyl_certificate.json`.

The full run checks 714,096 arbitrary-dimension label pairs, 1,948,590 prime-power noncommuting pairs, nineteen formal cyclic determinant products, the dyadic projector and positive-sum constructions, and seven direct composite-dimension matrices. It takes approximately nine seconds in the recorded environment. All rank and feasibility decisions are exact. Runtime measurements are descriptive and need not reproduce byte for byte.

The direct composite checker uses group closure and exact matrices without importing the main verifier. It was written by the same constructing agent. It is a separate computational method, not a separate agent review.

`revision_notes.md` identifies the preserved earlier edition, changes and review scope. `revision.diff` compares the earlier manuscript and verifier with this edition. `quantum_sources.md` records the bounded primary-source comparison. `checkpoint.json` records the source and evidence hashes and preservation checks.

The final universal delta and its thirteen-page PDF passed separate internal screening by another agent. `quantum_final_independent_review.md` and its JSON identify the exact reviewed hashes and limits. Its separate mathematical checker is `quantum_composite_review_checks.py`; run `python quantum_composite_review_checks.py --source-dir .` to reproduce it. The optional `--pdf PATH` argument also checks PDF markers and requires pypdf. This internal screening assigns no ARR score and is distinct from any subsequent external or user-commissioned evaluation.

`source_manifest.json` lists the portable package files and hashes. Python bytecode caches are excluded from that manifest.

The package does not require the earlier research workspace to run the verifier or follow the article proofs. No external publication action is performed by these files.


## Published assets and safe replay

ARR releases the canonical PDF separately from the source ZIP. Extract the sources and save the separate PDF in that directory as `paper.pdf` before checking the complete `MANIFEST.sha256`. The canonical PDF hash is also recorded in metadata.json. `paper.md` contains all machine-readable mathematics; ordinary extraction into `paper.txt` omits embedded formula images.

Verify the supplied hashes before running the scripts. Scientific replays write result JSON files, sometimes including runtime measurements, so run them in a working copy if you wish to preserve the deposited certificates and their hashes. A different elapsed time does not alter an exact mathematical result. The final, version-specific internal report is in `screening/final-internal-review.md`; the author-editor decision and pending subsequent Astra review are documented separately. `AUDIT_PROMPT_ASTRA.md` is ready for that future review and contains this PDF's exact identity.

For the final reviewer's portable extra check, run `python quantum_composite_review_checks.py --source-dir .`; optional `--pdf paper.pdf` checks PDF markers and requires pypdf. The earlier prime-power edition and its original internal review are preserved under evidence/cycle3/. checkpoint.json is a preparation snapshot with a separate final-review pointer.
