# Contributing

ARR welcomes contributions to the **platform software, schemas, documentation and tests** through GitHub pull requests.

This repository is not a manuscript submission channel. Do not place unpublished papers, personal data, credentials, vulnerability details, or untrusted archives in an issue or pull request. External research intake is closed until ARR publishes an approved deposit agreement, privacy notice, security contact and quarantine workflow.

Platform contributions are accepted under the license applying to the modified scope. By contributing software, you agree that your contribution may be distributed under `AGPL-3.0-or-later`. Documentation contributions are `CC-BY-4.0` unless stated otherwise.

Before opening a pull request:

```bash
python -m unittest discover -s tests -v
python scripts/validate_papers.py
python scripts/build_site.py
```

Keep changes reviewable, disclose generated or AI-assisted material, and do not weaken immutable-version, licensing, provenance or evidence-label requirements.
