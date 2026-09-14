# B4: provenance and numerical-check clarification

This author-side note accompanies the unchanged 11-page PDF with SHA-256 `ba8900141816e9f257783a1fd90ea9c92a1f2fc94bb7b681731bb05704f73e44`. It was prepared with Codex assistance after the preserved Astra local assessment. The assessment's native minor-revision recommendation remains unchanged; this note is not an editorial adjudication, intake report or acceptance.

## Historical status claims

The Introduction's Status paragraph describes the review history reported in the author's original Fable package. Its claims about independent scripts, a gap-free adversarial review and literature searches are author-supplied historical statements, not independently authenticated serving-identity or review receipts. The provenance qualifications in Section 9 and the AI-assistance statement apply to that paragraph too. Those historical statements do not establish correctness, independence, priority or acceptance of the present exact PDF. Current assessments must instead be identified by their separate dated reports, exact-PDF hashes and bounded checks. A prior reviewer finding no gap is not a proof or an exhaustive novelty certificate.

## What the 60-digit wrapper checks

In Section 7, the sentence identifying the numerical Poisson check as equation (3.4) should identify equation (3.2): the implementation compares κH_q with 4(E[J] − Var[J]). Specifically, `verify_lyapunov_60.py` computes E[J] = S1/S0 and Var[J] = S2/S0 − E[J]² and compares those quantities with the independently evaluated state function. It does not numerically replay the separate factorial-moment identity numbered (3.4). That identity remains an analytic assertion with its displayed derivation; no additional numerical run of it is claimed. This is a correction to the description of a check, and changes neither the proof nor the preserved numerical outputs.

## Scope

No PDF, source, code, log or native assessment has been overwritten. The theorem is analytic; neither the sampled trajectory controls nor the historically reported certificate sweep prove unsampled cases. This note is intended to be included with the exact manuscript and reports after the genuine deposit and separate editorial/publication gates are completed.
