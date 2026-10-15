# The arithmetic of sampling static quantum disorder: exact aliases, finite witnesses, and clock robustness

Lluis Eriksson · ARR-2026-7PEKNEDVH38HV8PX · v1 · Working paper.

Canonical PDF: paper.pdf, 10 pages. SHA-256: 66b83edcef934f296dcfc63e55f8463b3cbd9187b37afe06c4ab3a49cb5dcc33.

The paper proves exact finite static aliases for rationally independent sampling times, an explicit alias on an entire coarse grid, complete finite harmonic certificates outside the cut cone, and timing fragility and repairs. A bounded-time randomized protocol tolerates a specified independent additive clock error without a spectral-width assumption. The results concern memoryless single-use channels; they do not certify a quantum environment or solve an Erdős problem. No general priority certificate is claimed.

Reproduce in a disposable output directory with Python 3.12 and the versions in requirements.txt:

    python verify_sampling.py --out verification-rerun

All 31 assertion groups passed. Rational arithmetic certifies the 40,500-shot and 53,000-shot qutrit constants. Floating-point linear programming and random channel checks illustrate the analytic results; they do not prove exact interpolation or universal validity. The general proofs are in the manuscript, not a proof assistant.

reviews/original-9page preserves the first draft and original Astra report (ordinary 7.8/10, AIRR 4.7/10). These scores are not transferred to the amended paper. reviews/astra-addendum.txt identifies and assesses the exact amended PDF; reviews/response.txt and amendment.diff document changes. Context and model provenance are disclosed in reviews/operator-evidence.txt. The author is also AIRR operator. Publication is not human peer review or admission to the accepted collection. No Opus assessment of this manuscript is claimed.

The scoped inventory contains 719 OpenAI entries and 186 author records, plus the public repository catalogue. An inventory is not proof-level review of every source; access limitations and what was actually read are disclosed in audit-and-sources.txt. Private repository contents and credentials are excluded.
