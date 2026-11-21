# How many spectral shapes does the VLA correction table for 3C 138 require?

Lluis Eriksson. Working paper v1.

We quantify the representation error of the VLA table of monthly scaling factors for 3C 138 from February 2021 through December 2024. Across 47 dates and eight bands, the smallest worst relative error achievable by a fixed band profile and free monthly amplitudes is 28.94%. Four table entries furnish the matching lower bound. For contiguous periods with independently fitted profiles, 24, 14, six and three profiles are necessary and sufficient at tolerances of 1%, 2%, 5% and 10%, respectively. We supply the dated partitions, numerical factors and independent optimization checks. The bounds apply to the published table rather than to the true flux density of a target.

## Model assessments and review context

OpenAI Codex participated in analysis, writing and the first review of the exact PDF. Its shared-context assessment is 3.90/10. Report SHA-256 fab627702d11e5811033dfd16090cd19ad9b87b3e7c860680512e0b00b0ae42b. The author administers AIRR. Independent peer review has not been documented. The original assessment, objections and declared review context accompany this record. The author administers AIRR.

## Reproduction

In Colab Linux run static-shape.py and epochs.py in reproduction/, retaining /content/archive.zip after each script. Compare the achieved errors and segment counts to certificado.json and epocas.json. The reference runs agreed within 1e-8. [Pinned manuscript and analysis](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/2866945524b0ebd3697f6169d17112c1899e0c8a/audits/3c138-calibration-epochs).
