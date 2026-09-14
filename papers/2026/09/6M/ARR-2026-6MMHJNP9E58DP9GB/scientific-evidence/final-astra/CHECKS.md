# Exact-PDF local scientific preassessment

UTC: 2026-09-14T17:21:16.012943+00:00

PDF SHA-256: `ba8900141816e9f257783a1fd90ea9c92a1f2fc94bb7b681731bb05704f73e44`

The exact hash matched before review. Read the manuscript and scientific code only; external assessments and scores were withheld.

The symbolic E2, C1-C6, bracket and small-parameter checks passed. The supplied 60-digit trajectory checks all passed for q=4,5,6,10,30,60 and the q=2,3 no-fold controls. An independently written integral quadrature reproduced kf=4.415714051354578486, 7.6135433940722125571, 19.373531911973125644 and 59.995291211432000003 for q=4,5,10,30. The first exploratory secant solve failed for the q=30 threshold; switching that solver to a bracketed bisection succeeded. This numerical solver issue is not a manuscript counterexample.

The analytic proof was checked beyond the code: boundary behavior, first-zero existence, the strict crossing and no-second-zero arguments, q=2,3, Fano identity and small-z bounds are coherent. The verdict is minor revision solely for review-status wording and the wrapper identity-number mismatch. No unresolved material mathematical objection was found. Universal correctness rests on the proof, not the finite sampled grids.

## Real logs

- C:\Users\lluis\Documents\Codex\2026-09-11\airr-continuidad\outputs\fable-c2c3-20260914\papers\B4_two_planes_fold\candidate-2\final-astra\independent_quadrature.log
- C:\Users\lluis\Documents\Codex\2026-09-11\airr-continuidad\outputs\fable-c2c3-20260914\papers\B4_two_planes_fold\candidate-2\final-astra\independent_quadrature_retry.log
- C:\Users\lluis\Documents\Codex\2026-09-11\airr-continuidad\outputs\fable-c2c3-20260914\papers\B4_two_planes_fold\candidate-2\final-astra\sym_reduction.py.log
- C:\Users\lluis\Documents\Codex\2026-09-11\airr-continuidad\outputs\fable-c2c3-20260914\papers\B4_two_planes_fold\candidate-2\final-astra\verify_lyapunov_60.py.log

Disclosure: Fresh delegated task context with other assessment reports withheld; the model family participated in manuscript revisions. No technical memory isolation or independent human review is claimed. Manuscript-contained historical review assertions were not treated as evidence. Local scientific preassessment only; no acceptance, deposit, publication, intake receipt or public authorization.
