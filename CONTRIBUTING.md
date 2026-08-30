# Contributing

ARR welcomes contributions to the **platform software, schemas, documentation and tests** through GitHub pull requests.

This repository is not a manuscript submission channel. Do not place unpublished papers, personal data, credentials, vulnerability details, or untrusted archives in an issue or pull request. ARR accepts free expressions of interest by email **without attachments**. A manuscript may enter only through a one-use invitation to the separately deployed private quarantine service after its production launch gate is signed.

For an invitation request, email `lluiseriksson@gmail.com` with the subject `ARR invitation` and include only your name, contact email, field and provisional title. Do not send the abstract or manuscript by ordinary email. The definitive [deposit terms](docs/DEPOSIT_TERMS.md), [privacy notice](docs/PRIVACY_NOTICE.md), [complaint procedure](docs/LEGAL_AND_COMPLAINTS.md) and [governance rules](docs/GOVERNANCE.md) apply.

Platform contributions are accepted under the license applying to the modified scope. By contributing software, you agree that your contribution may be distributed under `AGPL-3.0-or-later`. Documentation contributions are `CC-BY-4.0` unless stated otherwise.

Before opening a pull request:

```bash
python -m unittest discover -s tests -v
python scripts/validate_papers.py
python scripts/build_site.py
```

Keep changes reviewable, disclose generated or AI-assisted material, and do not weaken immutable-version, licensing, provenance or evidence-label requirements.
