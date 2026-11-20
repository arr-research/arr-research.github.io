# When four mean wind speeds reverse a turbine choice

Lluis Eriksson. Working paper v1.

We compare linearly interpolated, equally rated turbine power curves on a representative northern North Dakota resource at 80 m. Replacing 8,760 hourly speeds with four within-group means reverses 19 of 395 eligible pairwise rankings. The Fuhrlander FL 1500_70 and GE 1.5sle also reverse on a second, previously unevaluated Minnesota resource. Group means and supports yield sharp distributional bounds for the power difference. Mean speed and mean excesses above the differential curve's knots recover the hourly comparison exactly. These are common-inflow predictions rather than measurements of delivered power.

## Model assessments and review context

OpenAI Codex participated in analysis, writing and the first review of the exact PDF. Its shared-context assessment is 4.00/10. Report SHA-256 49630a41ed29d74b521731efa2c309e89e70141d20f332ade3e2f06a75c4bbb6. The author administers AIRR. Independent peer review has not been documented. The original assessment, objections and declared review context accompany this record. The author administers AIRR.

## Reproduction

In Colab Linux run python reproduce.py north-dakota nd.json and python reproduce.py minnesota mn.json in reproduction/. Compare with north-dakota.json and minnesota.json using an absolute tolerance of 1e-8 for numerical values. [Pinned manuscript and analysis](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/b5ddf35b470133d4853dca26a14b78b4d82c08a3/papers/wind-four-states).
