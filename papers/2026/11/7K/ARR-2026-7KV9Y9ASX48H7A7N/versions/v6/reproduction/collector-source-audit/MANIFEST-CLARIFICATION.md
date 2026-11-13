# Separate factual clarification to the unchanged314 runner audit

The parent correction is confirmed from the actual SOURCE-INPUTS314.json. Of its940 entries, exactly one is `manuscript314A.tex`, with97173 raw bytes and SHA-256 `403e9a503aaf8ebffbdd97f8aa6267f6eec9e9e567c8eb625891ca9e13a310dc`. There is no `SOURCE-INPUTS314.json` entry: the manifest excludes itself, not the manuscript. The manifest's raw193716 bytes hash to `3f9a47ea0006c434ecb1f2b8a60dfcfd083c99b66e236c8ea8ce8378ac00d0cb` in both the prior exact-Git capture and current checkout.

The earlier sentence “it cannot include its own final binding and the final manuscript in the same self-referential fashion” was imprecise and could wrongly suggest that the manuscript is excluded. The exact factual statement is: **the940-entry manifest includes the final manuscript, and excludes the manifest file itself.** The earlier completed940 raw-blob checks included that manuscript entry; their result is unchanged.

The original report remains16051 raw bytes with SHA-256 `7e57ce3919ec1d9d2306439ddb086a5527c0c893ebe3cde4e078eeb1f4393219`. This separately retained clarification does not modify it or waive any source, engineering, CI, production or review gate.
