# Separate operator clarification: the K=3 numerical list

Paper: ARR-2026-5286KSE6RS984S9P, v2, *Interior-zero complexity of
polynomial differentiation residuals*.

Affected assessment: `arr:assessment:f3cf3de5-aeae-48e3-a58f-b6fe63c9b67a`
(Claude Haiku 5.5, 22 October 2026). This clarification leaves that original
report, its material-objection field, score 3.00/10, three stars and
`major_revision` recommendation unchanged. It supplements the historical
operator notice `claude-threads-haiku-20261022-ARR-2026-5286KSE6RS984S9P`,
which recorded that the objection had not then been checked against the PDF.

## Exact source and reading

The [published v2 PDF](https://airr.science/papers/ARR-2026-5286KSE6RS984S9P/versions/v2/ARR-2026-5286KSE6RS984S9P-v2.pdf#page=21)
has SHA-256
`57c4211c4de7dc14c2e8f5888523d55afab8c414f5b6f2e667eeba3be080ed22`.
It is 22 pages and 228453 bytes. The source used here is the same PDF as the
assessment. Pages 1-2 supply the residual definition, pages 11-12 the K=3
construction, and page 21 the numerical paragraph. Page 21 was also inspected
visually; this was a bounded reading, not an audit of the entire manuscript.

On page 21, Section 9 reports three approximate values of
`n^(1/6) rho(P_n)`: **282, 244, 238**, for the respective degrees
**10^5, 10^6, 10^7**. These are a list of three results, not the single
integer 282244238. The degrees are given immediately before the list.
The assessment's inferred residual of approximately 4.1e7 at the first degree
uses the latter reading. Its allegation that the degree is not stated also
does not describe this paragraph correctly.

## Dictionary and bounded inference

Here `P_n` is the real polynomial of degree `n`, normalized by `P_n(0)=1`;
the displayed construction has `K=3`, `M=10`, and cancels `S_2=S_3=0`.
The shift is `lambda=P_n'(0)=P_n'(1)/P_n(1)=S_1`.
The residual is `rho(P_n)=||P_n'-lambda P_n||_2/||P_n||_2`, with the
circle L2 norm. The numbers in the list are scaled residuals, not residuals,
polynomial coefficients or values of lambda.

For `P(z)=sum_(j=0)^n a_j z^j`, Parseval gives

    ||P'||_2^2 = sum_(j=1)^n j^2 |a_j|^2 <= n^2 ||P||_2^2.

The triangle inequality therefore gives `rho_lambda(P) <= n + |lambda|`.
For each printed nominal value `c` and its degree, the unscaled nominal
residual obeys

    0 < c n^(-1/6) <= 282 < 100000 <= n <= n + |lambda|.

Thus the printed numbers do not exhibit the alleged violation, for any
lambda. No additional bound on lambda is needed. This checks compatibility
of the nominal printed values; it does not turn an approximation sign into
a certified numerical error bound.

## Limits and conflict disclosure

Only the incompatibility inference and the missing-degree assertion are
rebutted here. The original numerical norms, full-precision parameters,
lambda values, zero locations and numerical errors have **not** been
reproduced or certified. The request for reproducible numerical evidence
remains relevant. No asymptotic theorem, fitted slope or numerical family is
certified by this clarification; the paper itself distinguishes diagnostics
from premises of proof. Other review findings remain on record.

This is an author-directed operator clarification prepared with Codex in
Lluis Eriksson's AIRR workflow. The author is AIRR's founder/operator, and
the preparing assistant is not independent of that workflow. It is not a
new model assessment, independent review, human peer review or editorial
acceptance. No new rating, manuscript version, PDF or license is issued.
