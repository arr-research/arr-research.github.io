# What monthly photovoltaic summaries can identify about sensors and missing days

Lluis Eriksson. Working paper v1.

We audit eight monthly summaries from a rooftop photovoltaic system. The May and June implied capacity intervals are disjoint under common averaging, even after rounding. Two explicit daily records reproduce generation, theoretical yield, irradiation and performance ratio at the reported precision. One retains all dates and includes a June irradiation offset, and the other omits one irradiation reading. The May data also impose a sharp covariance constraint if performance ratio denotes a mean of daily ratios. We give the complete synthetic daily witnesses and distinguish them from measurements of the plant.

## Model assessments and review context

OpenAI Codex participated in analysis, writing and the first review of the exact PDF. Its shared-context assessment is 3.65/10. Report SHA-256 d9787ced8f80a7d906f8c9b7c3501cb9d52148cd43213e1d8a543ebdfcc8a4dc. The author administers AIRR. Independent peer review has not been documented. The original assessment, objections and declared review context accompany this record. The author administers AIRR.

## Reproduction

In Colab Linux run rounding.py and construct.py in reproduction/, retaining /content/archive.zip after each script. Compare the results against table-check.json and mechanisms.json. Rational daily entries appear as strings. [Pinned manuscript and analysis](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/e6019fe47d6d513034bfcf171a7369160cd8d763/audits/pv-monthly-identification).
