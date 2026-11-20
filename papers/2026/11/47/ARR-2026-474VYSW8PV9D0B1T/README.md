# What can a platform-wide AI rollout establish about sales?

Lluis Eriksson. Working paper v1.

An exposure comparison can show differential growth while leaving the total change in sales unidentified. Under exact relative effects on log(1 + sales) we derive the break-even condition, its sharp support bound and a constructive three-sign example. For a historical-control comparison we derive an exact regression recalibration identity. Applying it to the sales marker in Figure III of NBER w36003 gives a necessary calibration increase of roughly 42% to erase the point estimate under a stated regression-weight condition. Neither calculation estimates the actual platform-wide gain.

## Model assessments and review context

OpenAI Codex participated in analysis, writing and the first review of the exact PDF. Its shared-context assessment is 3.90/10. Report SHA-256 9e0e4f035f4701634f30bf72a9539a50666722d8b5b99bc4b8cfa2b7e3c95f7e. The author administers AIRR. Independent peer review has not been documented. The original assessment, objections and declared review context accompany this record. The author administers AIRR.

## Reproduction

In Colab Linux run reproduce.py, reproduce-regression.py and reproduce-graph.py from reproduction/, retaining /content/archive.zip between scripts. The outputs are certificate.json, regression.json and graph.json. Compare regression shifts within 1e-12; the other JSON results matched exactly. [Pinned manuscript and analysis](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/3721178fcef4abab5249230706501e81232300fb/papers/ai-market-total-threshold).
