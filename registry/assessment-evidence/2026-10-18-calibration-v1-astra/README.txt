Exact-version model assessment evidence — 18 October 2026

Canonical paper: ARR-2026-0S8D4XJMZS9PDV1Z v1.
The model response and full report are retained unchanged. Score 3.40/10;
recommendation accept; no unresolved material objections. This is one
named-model assessment, not editorial acceptance or human peer review.
The publication status remains Working paper. Evidence is limited.

Context: a new agent was requested without inherited turns, but the
filesystem was shared and memory isolation was not independently verified.
The reviewer accidentally encountered an earlier report on a predecessor's
public primary-paper page. The registry therefore records shared context,
not fresh_blind. See operator-evidence.json and the full report.

The seven scientific input files are already-public author material.
The original certificate verifier needs only Python standard library:
  cd input/certificate
  python verify.py
The separately written referee audit uses numpy and scipy:
  python output/independent-audit.py
It reads the preserved published and replayed verification reports and
overwrites output/independent-checks.json. Exact rational checks control;
floating-point circuit reconstruction is a diagnostic, not an experiment.

No private authentication, session transcript, or third-party full text
is included. This report applies only to the exact v1 PDF, not later
scientific extensions or the separate local-signal manuscript.
