# Reproduce the scientific evidence

Read paper.pdf Sections 6 and 8 and the preserved reviewed-input/lean-verification.json. The source is https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME at cd62e1225e59335df974949d5c58a455cb790192 (tag c4-v1.0), using Lean 4.29.0-rc6 and the pinned Mathlib revision 07642720480157414db592fa85b626dafb71355b.

From that exact source checkout, run `lake exe cache get`, `lake build AmosClosure` and `lake env lean AmosClosure/Oracle.lean`. These are the documented full formal checks; no new Lean execution is claimed by this September 14 packaging step.

The supplied strict numerical companion needs python-flint and mpmath. Run `python c4_amos_real_arb_strict.py` from this directory. Every FAIL or UNDECIDED result and every disagreement causes a nonzero exit. The unchanged historical companion and its provenance remain alongside it.

To compile this AIRR manuscript, run `tectonic -X compile paper.tex` in a separate scratch directory containing paper.tex. Recompilation may change PDF metadata bytes; the exact reviewed paper.pdf remains canonical for the preserved reports.
