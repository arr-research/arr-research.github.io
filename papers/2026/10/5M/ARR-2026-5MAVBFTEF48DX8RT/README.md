# A complete class of optimal quantum tests for unknown unitary dynamics

Lluis Eriksson · ARR-2026-5MAVBFTEF48DX8RT · v1 · Working paper.

Canonical manuscript: paper.pdf, 12 pages, SHA-256 15866420b1b97a9c5f9dc651caaf9d80f8c85b1286adceba97304af792cdd87b.

The complete-class theorem reduces physical positive testers to lotteries of explicit parallel Schur-Weyl tests, simultaneously over memoryless CPTP alternatives with two unknown fixed independent rotations. It gives exact finite-query minimax optimization, a universal two-query optimum, and the resource-constrained depolarizing optimum. It does not cover calibrated arbitrary channel discrimination or temporal memory. Related tools and constructions are explicitly attributed; exhaustive novelty is not certified.

Replay from a disposable copy:

    python verificacion/verify_minimax.py
    python verificacion/verify_physical.py
    python revision/check_independent.py

The first two need NumPy, SciPy, CVXPY and Clarabel; the reviewer script needs NumPy and SymPy. Original environment versions are recorded in verificacion/entorno-verificacion.json. These runs write results beside the programs. Preserved runs include 91 matrix cases, 12 causal optimizations, 75 circuit calculations and exact partition/reference comparisons. Two solver runs reported optimal_inaccurate, as retained in the data. The referee supplied separate checks on 34 channel cases and exact resource inequalities. General claims rest on the analytic proofs, not numerical sampling.

revision/informe-astra.txt and .json are the unchanged review of the original 11-page draft. revision/addendum-atribuciones-pdf.txt and .json bind that same judgment to this 12-page PDF. The only changes were explicit attribution to Chiribella-Ebler for Schmidt-rank truncation, Sedlak-Ziman for antisymmetric probes, and the assistance declaration. Proofs and equations are unchanged. Both original attribution observations were resolved. Scores remain 8.2/10 ordinary manuscript quality and 4.6/10 AIRR research importance: distinct scales, not a formula conversion. The structured public entry is a transcription of this one assessment.

The initial review was in a fresh separate context; the subsequent attribution addendum was coordinated with development. The final entry therefore conservatively declares shared context and manuscript involvement. Same provider as authorship assistance; no statistical independence, human peer review or formal verification is claimed. The author is AIRR operator. Working-paper publication is separate from AIRR acceptance.

Historical audit files are preserved as pre-publication snapshots. Their statements that deposition or review is pending describe their original date. Current release status is determined by metadata, the timestamp registry and the actual release. Corpus indexing is not proof-level reading of every listed paper. Private repository inventories are excluded. No new Opus report exists; the last attempt encountered a weekly limit until 17 October 2026 at 13:00 Europe/Stockholm.
