# Reproduction scope

The candidate manuscript Section 8 specifies THE-ERIKSSON-PROGRAMME at commit 3eb5cf9293d2b8cc6ece17f5e37d422726b9d27d (c5-v1.0.1), Lean 4.29.0-rc6 and pinned Mathlib 07642720480157414db592fa85b626dafb71355b. A full checkout is required: the preserved excerpts are not independently buildable.

From that pinned upstream checkout, the manuscript documents `lake exe cache get`, `lake build AmosClosure`, `lake env lean AmosClosure/Oracle.lean`, and `python scripts/c5_crossing_arb.py`. On Windows use core.autocrlf=false as described in the manuscript. Inspect each numerical verdict, including FAIL or UNDECIDED; the historical script may exit zero despite unsuccessful verdicts. No new execution of these commands is asserted by this publication.

The final paper.tex is supplied verbatim with its historical compilation log. To reproduce typography run `tectonic -X compile paper.tex` in a separate scratch directory. Recompilation can alter PDF metadata; preserved paper.pdf remains the exact artifact assessed. The revision.diff is a historical correction record, not a complete reconstruction recipe for final TeX.
