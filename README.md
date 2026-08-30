# ARR — Archive for Rigorous Research

ARR is a curated, versioned archive for research papers and technical notes published with canonical artifacts, machine-readable renditions, and explicit verification evidence.

This repository is the technical foundation for the archive. It keeps lightweight, inspectable sources in Git and publishes large generated artifacts—PDFs, complete source bundles, datasets, and build logs—as GitHub Release assets.

## Current status

ARR operates a public archive and is building a **free, invitation-only intake pilot**. Expressions of interest are accepted without attachments; live upload invitations remain gated by the signed production checklist. No record is considered published merely because it appears in a branch, pull request or private intake. A research paper or technical note becomes an ARR publication only after a human acceptance workflow completes and a versioned release is created.

## Local checks

```bash
python scripts/validate_papers.py
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

Create a concurrent-safe candidate identifier and sharded directory with:

```bash
python scripts/new_record.py --author "Author Name" --type research-paper
python scripts/new_record.py --author "Author Name" --type technical-note
```

Create the next version of an existing record without changing its ARR identifier:

```bash
python scripts/new_version.py ARR-2026-XXXXXXXXXXXXXXXX --change-size minor --summary "Corrects notation and expands the reproducibility instructions."
python scripts/new_version.py ARR-2026-XXXXXXXXXXXXXXXX --change-size major --summary "Replaces the main argument and adds new principal results."
```

## Repository layout

```text
papers/                 Accepted record sources, grouped by year and month (legacy path name)
papers/.../versions/vN/ Immutable source snapshots for later versions
templates/paper/        Shared template for new paper and technical-note candidates
schema/                 Machine-readable metadata contract
scripts/                Validation, packaging and site generation
site/                   Static presentation assets
docs/                   Editorial and operational documentation
.github/workflows/       GitHub validation, Pages and Release automation
```

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the publication procedure.
Copy-ready agent instructions are in [docs/AGENT_DEPOSIT_PROMPTS.es.md](docs/AGENT_DEPOSIT_PROMPTS.es.md).

## Scale and licensing

ARR separates private intake, the public metadata registry, and immutable artifact storage so that GitHub can be replaced or complemented without changing record identifiers. See [capacity and migration](docs/SCALE_READINESS.md), [state and evidence labels](docs/STATE_MODEL.md), and the [licensing policy](LICENSE_POLICY.md).

The private intake service is in [`services/intake/`](services/intake/). Submission, assessment, publication and withdrawal cost EUR 0.00 under [`ARR-DEPOSIT-1.0`](docs/DEPOSIT_TERMS.md). The operator is Lluis Eriksson, founder, registry operator, responsible editor and GDPR controller. See [privacy](docs/PRIVACY_NOTICE.md), [complaints/contact](docs/LEGAL_AND_COMPLAINTS.md), [retention](docs/RETENTION_SCHEDULE.md), [governance](docs/GOVERNANCE.md) and the [production launch gate](docs/INTAKE_OPERATIONS.md).

Platform software is `AGPL-3.0-or-later`; ARR-authored documentation is `CC-BY-4.0`; public catalogue metadata is `CC0-1.0`; deposited papers, code and data declare their own scoped licenses.
