# Scientific referee report

**Recommendation: accept. Score: 3.8/10. Overall stars: 4.**

This is a sound, specialized analytic contribution in its stated scope. The score uses the supplied non-percentage scale: 3 is acceptable substantive work and 4 is strong work. It does not suggest exceptional, field-shaping or historic novelty. I found no unresolved material objection to the exact manuscript reviewed. Acceptance here is a model recommendation for private preassessment, not a human editorial decision or permission to publish.

## Exact scope and reviewer identity

- Paper: ARR-2026-07EH3CZRD89YC8JN.
- Candidate: arr:version:f9a95623-ad1e-4174-9b32-dec9d2dcbe5d.
- Title: *Lossless Calibration Is Stored Memory: A Topological McMillan-Degree and Wigner–Smith Law for Passive Quantum Networks*.
- PDF SHA-256: `341c673d6613533931cbc0fc817cf946d178e390cde818221c19b33c304a4167`.
- Provider: OpenAI. Configured/exposed model identity: `gpt-6-astra`, effort high. No hidden serving metadata or independent execution-identity attestation is available to this reviewer.
- Prompt: ARR-PRIVATE-CANDIDATE-PREASSESS-1.0. Independence category: `involved_in_manuscript`. This is not independent human review or a claim of statistically independent model review.

The hash was verified before substantive reading. I read the text of all 16 PDF pages, checked the root source where needed, rendered all 16 pages, and inspected four contact sheets. I read the relevant companion theorem contained in the authorized input, not its historical reviews. I did not read coordinator documents, other versions of this manuscript, or previous assessment reports. A directory inventory exposed historical execution filenames; those execution files were not used as new evidence. The current manuscript itself describes historical corrections and a separately attributed referee replay. A primary-literature search for the cited routing manuscript incidentally returned AIRR catalogue snippets containing unrelated paper status and one unrelated score. No assessment was opened or intentionally retrieved, and those snippets did not inform this judgment. The primary routing PDF was then read directly for the pertinent results.

All scientific imports and executions used scratch copies with bytecode disabled. The supplied input was not edited. The accompanying evidence contains new executions, not copied claims of execution. The primary-runtime dependency information was obtained only to locate available Python/PDF tooling.

## Main scientific assessment

**Theorem 4.1 is correct under its stated hypotheses.** Boundary column unitarity identifies the lossless input space with the kernel of the complementary loss block. A strict all-direction stop makes that block full column rank at one point. A single fixed maximal minor can therefore be chosen nonzero there; no frequency-dependent row choice is needed. Its kernel contains every lossless calibration space, so the determinant has at least the corresponding nullity as local zero multiplicity. Summing at distinct nodes and applying the minor budget proves K <= n. This proof also covers rectangular protected outputs and different input subspaces at different nodes.

Lemma 3.1 and Appendix A correctly use a constant basis change and determinant multilinearity. The nullity lower bound concerns multiplicity, not the number of distinct roots. Lemma 3.2 and Appendix B correctly observe that a rank-one factor contributes a single scalar Blaschke coordinate to each exterior-power entry. The rank of the induced exterior projection is immaterial to that entrywise denominator count. The full product denominator has at most n factors, rather than rn. Cancellation cannot increase numerator degree. The alternative block-determinant proof is particularly useful: only the n state rows depend linearly on z. It supplies a direct route to the bound without treating the exterior-power mechanism as new mathematics.

The strict-stop hypothesis is substantive. Mere frequency dependence or nonzero loss somewhere is insufficient when a transparent input channel remains. My separate constant-transparent-channel example reproduces that obstruction. Theorem 4.1 is a selectivity result for the full-rank loss condition, not a general charge for collecting samples of transparent wiring.

**Theorem 5.1 and Corollary 5.2 are correct.** The elementary factor has the positive Poisson-kernel delay, the product rule gives a unitary conjugate sum, and trace integration gives the determinant winding. The stated sign is consistent with the analytic-disc convention. The mean-to-peak and largest-eigenvalue bounds follow immediately. The paper correctly distinguishes the dimensionless phase coordinate from a physical frequency variable. With its specified Cayley map and harmonic convention, the Jacobian is positive and the physical integral preserves the degree. A frequency-independent peak bound in seconds does not follow, and the paper does not claim one.

The oscillator interpretation is conditional on an annihilation-only minimal passive realization. That distinction is necessary: rational sample-delay coordinates and literal propagation delays are not interchangeable physical state counts. The explicit realization equations and the discussion of loss ports keep the claim within a defensible scope.

**Proposition 6.1 is coefficient-sharp as claimed.** The Hadamard-conjugated delay bank has charge m at each of M roots, determinant z^(mM), a perfect stop, and constant trace mM. Its proper-delay eigenvalues are zero and M, so it does not saturate K/N=M/2. This lack of saturation is explicitly acknowledged. The example establishes existence for root-of-unity geometry; it does not solve arbitrary prescribed-node optimization.

**Theorem 7.1 is valid and appropriately limited.** Its reference and perturbed transfers are holomorphic on neighborhoods of the complete enclosed regions, the interiors are disjoint, and the contour margin is strict. Ordinary Rouché then preserves zeros, and the same rational-inner minor budget applies. The text correctly says that preserved complex zeros need not remain exact lossless real-frequency points. The enclosed-pole example illustrates why contour-only pole avoidance would fail. I checked this example numerically: on the radius-10 circle the perturbation maximum is 0.6875 and the reference minimum is 1.375; the reference pole is indeed enclosed. Proposition 7.2 correctly rules out degree bounds based only on a number of approximate samples with no separation assumptions.

**The six-port application is internally consistent.** Each arm has S simple boundary roots of B_g=1, and the three phase shifts make the root sets disjoint. U_rev U=z^2 I gives the stated calibration direction. The stop at -1 is strict for all three signal directions. The full determinant z^6 product_g B_g is a scalar inner function of degree 3S+6, with no inner-factor cancellation. The lower bound therefore gives 3S <= n_min <= 3S+6 for exactly the comparator class stated: matching calibration data plus a strict stop. It does not prove that the six-state excess is unavoidable. The det C factor z^3 counts additional zeros of this construction but is not imposed on arbitrary competitors, so it cannot simply be added to their universal lower bound.

The irreducibility reference is sufficiently mapped. In the supplied companion source, the pass-node lemma supplies S-1 nodes per group in the specified arc; their Fourier-transformed signatures are Vandermonde columns. The reducing-line argument has at most two orthogonality exceptions, so a scalar rational numerator with at least 3S-5 roots and degree at most S+4 vanishes for S>=5. The stop envelope is below one already at S=5 and decreases thereafter. This establishes the cited application without requiring full spark of the enlarged 3S-node set. Irreducibility is not needed for the present universal lower bound.

**The rate interpretation is a conditional corollary, not an additional universal quantum theorem.** The stationary filtering congruence is standard under the given model. For a lossless input v, w=Gv is normalized and G* w=v, including for rectangular G, so w*GJG*w=v*Jv. The norm bound at a stop follows from submultiplicativity. Auxiliary channels can add noise, and a growing delay scale does not by itself preserve a Markov approximation uniformly in S. These limitations appear explicitly. The paper does not establish device-level decoherence suppression, energy savings or a universal thermodynamic conversion from degree.

## Novelty and significance

The classical foundation is well documented. The square rank-one factorization and the warning about arbitrary mixed-pole product cancellation can be checked in [Alpay, Jorgensen and Lewkowicz, Theorem 3.1 and Eq. (3.5)](https://arxiv.org/pdf/1410.0283). The system-matrix identity used in the alternative proof is consistent with [Dopico, Quintana and Van Dooren, Section 1](https://arxiv.org/pdf/1903.05016). Neither foundation supports a claim that scalar zero budgets are new here, and the manuscript makes no such claim.

The cited [routing manuscript, Lemma 2.1 and Corollary 4.2](https://airr.science/papers/ARR-2026-52B6MSS1W197W9T2/versions/v1/ARR-2026-52B6MSS1W197W9T2-v1.pdf) already contains the compressed-minor mechanism and degree-to-integrated-delay conversion. Its routing data use one fixed input plane and prescribed output planes. The present protected-output formulation allows node-varying lossless input spaces, with one strict stop selecting a nonzero loss minor. That is a useful different proposition, but a relatively short application of shared machinery, not a new degree principle. The exact near-optimality bracket for the six-port construction is the strongest concrete consequence here. The manuscript neither establishes priority over the related paper nor computes optimal degree for arbitrary calibration data.

The physical realization conventions agree with the passive model and minimality discussion in [Gough and Zhang, Sections 3.1–3.3 and Theorem 3.5](https://arxiv.org/pdf/1311.1375). This supports the conditional mode-count reading, not an experimental validation of the proposed family. The originally accessed institutional PDF timed out during subsequent targeted retrieval; the arXiv primary manuscript supplied the relevant equations and theorem.

The result should be useful as a compact resource obstruction for exact passive interpolation. Its present significance is constrained by exact boundary equalities, finite rational models, and the lack of a real-axis noisy-data theorem. These are acknowledged boundaries rather than defects, but they limit the appropriate score.

## Actual reproduction and falsification evidence

The documented top-level replay was run from a scratch package with a new sibling output directory. Both generator and corrected validator exited zero. Actual versions were NumPy 2.5.1, SciPy 1.18.0 and Matplotlib 3.11.1. The replay records timestamps, commands, stdout/stderr, environment and hashes in `replay-1/RESULT.json`. The manuscript's six prescribed orders were regenerated; the maximum random-minor interpolation residual was 1.3465280673577658e-15 across 128 seeded trials covering ranks 1–6. This is numerical falsification evidence, not a formal polynomial certificate.

New checks in `scratch/independent_checks.py` go beyond replaying the supplied formulas:

| Check | Result |
|---|---|
| Full 6x6 matrix and analytic derivative, S=5,6,7,9,11,15,19 | Boundary unitarity, Hermiticity/positivity and trace formula passed; worst unitarity residual 1.05e-11 and relative trace discrepancy 1.08e-11. |
| Independent Möbius inversion for every arm | All 3S calibration vectors verified; worst direct vector residual 6.26e-12. Even order S=6 also passed. |
| Integrated trace from matrix derivative, with a peak-resolving change of variable | At S=19, 63.00000000007482 versus 63; no minimal realization was numerically computed. |
| Strict stop | Direct signal norms agreed with sin(exp(-0.45S)/2); S=19 gave 9.677254962797824e-5. |
| Perturbed roots via independent scalar inversion | Exactly one root in each of fifteen disjoint, pole-free reference discs. |
| Shifted 65,536-point contour grid | Maximum sampled ratio 0.0451165803161476, agreeing with the original 0.04511658024617411. This remains sampled evidence. |
| Saturation examples | m,M=(1,1),(2,3),(4,5), with the stated delay spectra. |
| Rectangular protected output and correlated positive J | Rate identity residual 4.75e-16. |
| Approximate-calibration counterexample | 1,000 distinct samples achieved signal magnitude at least 0.9999999956887755 with degree one. |
| Fixed-ledger adversarial mutations | Baseline accepted; eight malformed variants rejected with actual exception text retained. |

The eight negative cases cover duplicated orders, an empty root inventory, a false stop determinant, NaN delay, a Boolean count, a non-strict Rouché ratio, a forged peak and an invalid rank inventory. Rejection is the expected result of these negative tests, not an unreported failure. All five reviewer check groups passed; their stderr is empty. One bookkeeping caution about my own transparent-channel test is recorded: its 101-point closed angular grid repeats -pi/pi, so those entries are not 101 distinct boundary nodes. The counterexample is analytic and survives deletion of the repeated endpoint; the raw result is retained without relabelling it as a distinct-node campaign.

No continuous interval contour proof, independent state-space minimality computation, full public release gate, hardware experiment or quantum-master-equation simulation was performed. Those omissions are not used to refute analytic claims for which the manuscript supplies proofs. The historical three-ledger/32-mutation assertion was not independently authenticated in this review; it is not counted as my execution evidence.

## Minor suggestions and remaining limits

There are no required scientific corrections for this exact candidate. The following suggestions are optional:

1. A future current numerical overlay could evaluate the Poisson denominator as `(1-r)^2 + 4r sin(theta/2)^2` and numerator as `(1-r)(1+r)` to reduce cancellation. The present published-order replay passes, but the displayed formula is less stable as r approaches one. Preserve historical generator bytes when making such an overlay.
2. Move some operational history from Section 10 into the supplement while retaining clear evidence provenance. The scientific presentation is longer than its central theorem requires.
3. Keep the current restricted novelty language in any abstract, submission description or public summary. The strongest defensible claim is the protected signal/loss formulation and its application; the underlying minor and phase-volume laws are shared classical or related-work machinery.

The residual research questions are meaningful: a separated noisy-data theorem, certified analytic model-uncertainty margins, and whether the six extra states can be reduced while maintaining the specified directional data. None is needed for correctness of the claims presently made.

## Page coverage

Pages 1–3: abstract, contributions, disc/half-plane convention, passive realization and lossless-space definition. Pages 4–5: both degree proofs, calibration theorem and delay proof. Pages 6–7: corollaries, sharpness, Rouché assumptions and approximate-sample counterexample. Pages 8–9: companion mapping, six-port family, determinant, trace-delay law and Figure 1. Pages 10–12: rate interface, reproducibility, table, evidence qualifications and classical comparisons. Pages 13–14: routing overlap, limitations, conclusion and local multiplicity appendix. Pages 15–16: exterior-power conclusion, conditioning appendix and every reference entry. The render review found no material clipping or missing mathematical content.
