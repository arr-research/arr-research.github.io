# What does a materials prediction target cost? Distinct labels and error certificates on a common test population

Lluis Eriksson. Working paper, version 1.

We reconstruct distinct cumulative training labels for two acquisition strategies across 150 property-seed pairs in a public materials regression benchmark. We derive conservative certificates for the error on any subset from the full-library MAE, RMSE and subset size, accounting for the rounding of the archived metrics. On arm-specific unmeasured materials we certify sixteen first-crossing cost advantages for cluster selection. On exactly the same never-acquired materials at every budget and for both arms, one ordering is certified. In that QM9 case the two strategies first reach the target with 100 and 561 distinct labels on a common test population of 122,398 molecules. The other 149 common-population comparisons remain unresolved.

## Model assessments and review context

OpenAI Codex (GPT-6 family, serving revision unverified) participated in the analysis and reviewed this exact PDF in the authoring context. The assessment is 3.80/10. Its full report SHA-256 is fd06ac9d356196b35bf19ddfa6164e398dc179c3777cb62adcc25be3857d7809. Independent peer review has not been established. The model reviewed the four rendered pages in the same Codex conversation that produced the analysis. No context-isolation controls were verified. The author administers AIRR. The original report and objections accompany the record.

## Reproduction

Run the Python reconstruction with NumPy and a new output ZIP path. The source and two input protocols are attached with the expected summary, complete paired output and double-build PDF proof. Upstream benchmark code and data belong to their respective creators. [Pinned programme source](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/e0c2c5225f4e1205ca577c03f48de3f709dbfa83/papers/acquisition-cost-certificates).
