# Phase calibration unlocks adaptive tests for renewed quantum noise

Lluis Eriksson · ARR-2026-33GYTDAT5C8THB3M · v1 · Working paper.

Canonical manuscript: paper.pdf, nine pages, SHA-256 6e613f81ad416894689d933bbaf09c8839f929ee320e71a391145b2f43875ab9.

The main theorem gives the exact all-causal minimax failure for an unknown common carrier as the optimized parallel permanent law, for all dimensions, query counts and Schur correlation matrices in the stated ordinary forward-query model. A fixed rational five-query qubit strategy beats every parallel strategy when the carrier is calibrated on a nonempty interval. It does not identify the calibrated causal optimum, prove minimality of five queries or improve the asymptotic failure exponent.

Replay from a disposable copy:

    python verify_exact.py
    python verify_circuit.py
    python review/verify_independent.py
    python review/verify_minimax.py

The first needs only Python 3.10+ standard library; the others need numpy and, for reviewer checks, sympy. All four passed from the delivered package. Exact Schur-complement positivity and causal constraints certify the matrices. Numerical circuit reconstructions and randomized diagnostics supplement the analytic arguments, rather than prove continuum claims. requirements.txt gives the verification dependencies. The discovery folder has optional cvxpy/CLARABEL search code, not needed for exact replay.

The manuscript and final exact-PDF review are fixed. review/final-manuscript-addendum.txt records 8.6/10 ordinary manuscript quality and 4.4/10 AIRR research importance, distinct judgments. The public structured record preserves the same score, time and involvement declaration. The earlier critical-review.txt audits the candidate without assigning a score. candidate.txt is retained solely as the scientific input needed to reproduce the review hashes; it is not a separate public version of the paper.

The reviewer used a separate, coordinated context of GPT-6 Astra, the same model/provider involved in development. It is not blind, human or statistically independent review. The author is AIRR operator. Working-paper publication does not satisfy the separate admission gate. Opus 5.5 was requested on 15 October but a weekly service limit prevented a report; see review/opus-availability.txt.

research-audit.txt and audit/ document the search as a pre-publication snapshot. Its sentence that no deposit had yet been made describes that earlier search closure; current publication state is determined by this record and the public timestamp registry. Catalog coverage is not proof-level reading of all indexed papers. No worldwide novelty certificate is claimed.
