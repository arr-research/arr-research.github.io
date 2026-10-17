Supplement: Six-spin Lorentzian obstructions for clique blowups of independence-stable graphs
Author: Lluis Eriksson. Research draft, 17 October 2026.

Run: python -B verify_all.py
Python 3 with the SymPy and NetworkX versions recorded in requirements.txt.
The driver uses a temporary subdirectory, recomputes both complete datasets,
and compares every exact output field except elapsed time. It does not change
the baseline results. Scripts run separately write into _run by default;
AIRR_OUTPUT_DIR can select another output folder.

verify_stable_blowups.py screens every connected atlas graph of orders 3--7.
It checks the stability equivalence by independent edge deletions, enumerates
all bounded occupations for s=2,3 on each stable base, and checks the entire
minimum-pattern classification and the first four-profile block.
Result: 994 base graphs screened; 360 stable bases; 720 blowup cases.

construct_six_spin_examples.py builds four strictly positive rational targets
and calculates complete 4x4 Hessian restrictions by all occupation vectors.
The ordered-edge expression is in the manuscript. Exact congruence pivots,
all matrix entries and six target nodes are recorded in results/.
Finite search caps in this example script are practical caps only. The theorem
uses two unbounded searches whose termination is proved by successive limits.

ground_profiles.py and exact_inertia.py contain ordinary pure helper functions.
No external manuscript file, author-state file, model report or executable
download is needed to reproduce the calculations. The checks are exact
rational computations; they are not proof-assistant verification or human review.

Status: author computations. The separate source-level technical audit is complete.
An exact-version referee score has not yet been assigned to this manuscript.
The results of older manuscripts do not apply to this version.

Licensing: authored source code Apache-2.0; authored explanatory text CC BY 4.0;
factual metadata and computed datasets CC0-1.0. Third-party libraries retain
their own licenses and are not bundled.
