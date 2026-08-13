# ARR — Archive for Rigorous Research

ARR is a curated, source-first archive for research published with explicit, documented verification evidence.

This repository is the technical foundation for the archive. It keeps lightweight, inspectable sources in Git and publishes large generated artifacts—PDFs, complete source bundles, datasets, and build logs—as GitHub Release assets.

## Current status

ARR is in its public-infrastructure/private-intake prototype phase. No paper is considered published merely because it appears in a branch or pull request. A paper becomes an ARR publication only after the acceptance workflow completes and a versioned release is created. External submissions are not open.

## Local checks

```bash
python scripts/validate_papers.py
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

Create a concurrent-safe candidate identifier and sharded directory with:

```bash
python scripts/new_record.py --author "Author Name"
```

## Repository layout

```text
papers/                 Accepted paper sources, grouped by year and month
templates/paper/        Template for a new candidate
schema/                 Machine-readable metadata contract
scripts/                Validation, packaging and site generation
site/                   Static presentation assets
docs/                   Editorial and operational documentation
.github/workflows/       GitHub validation, Pages and Release automation
```

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the publication procedure.

## Scale and licensing

ARR separates private intake, the public metadata registry, and immutable artifact storage so that GitHub can be replaced or complemented without changing record identifiers. See [capacity and migration](docs/SCALE_READINESS.md), [state and evidence labels](docs/STATE_MODEL.md), and the [licensing policy](LICENSE_POLICY.md).

Platform software is `AGPL-3.0-or-later`; ARR-authored documentation is `CC-BY-4.0`; public catalogue metadata is `CC0-1.0`; deposited papers, code and data declare their own scoped licenses.
