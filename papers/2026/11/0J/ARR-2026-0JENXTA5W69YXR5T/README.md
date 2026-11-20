# Instrument choice and geographic clustering in the Galician literacy panel

Lluis Eriksson. Working paper v1.

We reconstruct a four-census panel used to estimate how historic emigration affected literacy in Galicia. In the versioned replication package, the archived coefficient and its printed diagnostics use different sets of instruments. Holding 1,284 observations and the controls fixed, we compare the two specifications. Restricted wild bootstrap tests grouped by 47 judicial districts give p=0.1246 for the instrument used to estimate the coefficient and p=0.0282 for the two instruments used in the diagnostics. The sign of the estimated coefficient survives each single-municipality deletion. These results concern inference in one historical literacy equation.

## Model assessments and review context

OpenAI Codex participated in analysis, writing and the first review of the exact PDF. Its shared-context assessment is 3.80/10. Report SHA-256 4df0bb27b5b77ef1d3c4c22cfd665add846e02b703752ef4bb1be93a7a9cd8bf. The author administers AIRR. Independent peer review has not been documented. The original assessment, objections and declared review context accompany this record. The author administers AIRR.

## Reproduction

In Colab Linux run reproduce.py and reproduce-districts.py from reproduction/, saving /content/archive.zip after each script. Compare audit.json against the fields in results.json, and districts.json against the full archived results; absolute numeric tolerance 1e-8. [Pinned manuscript and analysis](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/eda4e65573bd6d9f95b736f6975171adc3db9a4a/audits/galicia-instrument-diagnostics).
