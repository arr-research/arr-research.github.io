# Epoch AI FrontierMath Tier 4 v2 snapshot

Source: [Epoch AI native benchmark data](https://epoch.ai/data/benchmark_data.zip),
retrieved 12 September 2026. Attribution: Epoch AI, Capabilities & Benchmarking.
Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[Data usage](https://epoch.ai/benchmarks/use-this-data) and
[methodology](https://epoch.ai/benchmarks/about).

The CSV is unchanged. The JSON is an AIRR transformation: it selects the model
configuration, organization, mean accuracy, reported standard error, run ID and
dates from every CSV row and adds provenance metadata. No row is selected because
it has a higher score, and no reasoning tier is inferred. The native CSV digest is
recorded in the JSON and checked by the tests.

This is a fixed mathematical-capability input to AIRR-RATING-1.0, not a referee
reliability calibration. New source data requires a new file and an explicit
policy release. Builds do not fetch a live leaderboard.
