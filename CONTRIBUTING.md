# Contributing

AIRR welcomes contributions to the **platform software, schemas, documentation and tests** through GitHub pull requests.

This repository is not a manuscript submission channel. Do not place unpublished papers, private contact details, credentials, vulnerability details, or untrusted archives in an issue or pull request. AIRR's currently fee-free pilot is open through a separate private receiver. An alias/password workspace is required; an invitation, author email and legal name are not.

Use the private form linked from [AIRR's Submit page](https://airr.science/submit/). Do not send an abstract or manuscript by ordinary email. The definitive [deposit terms](docs/DEPOSIT_TERMS.md), [privacy notice](docs/PRIVACY_NOTICE.md), [complaint procedure](docs/LEGAL_AND_COMPLAINTS.md) and [governance rules](docs/GOVERNANCE.md) apply.

Platform contributions are accepted under the license applying to the modified scope. By contributing software, you agree that your contribution may be distributed under `AGPL-3.0-or-later`. Documentation contributions are `CC-BY-4.0` unless stated otherwise.

Before opening a pull request:

```bash
python -m unittest discover -s tests -v
node --test tests/search.test.cjs
python scripts/validate_papers.py
python scripts/build_site.py
```

Keep changes reviewable, disclose generated or AI-assisted material, and do not weaken immutable-version, licensing, provenance or evidence-label requirements.
