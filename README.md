# AIRR — Archive for Independent & Rigorous Research

AIRR is the hostile-audit research registry: new admissions must survive an operator-selected frontier-model audit of the exact hashed manuscript, with zero unresolved material objections and a final human decision. AIRR promises no fixed provider, model, report count or reasoning tier; it publishes exactly which models were used, their findings and any disagreement alongside canonical artifacts, machine-readable renditions and explicit verification evidence.

Passing that gate is meaningful positive evidence that a paper deserves serious attention. It is not a guarantee of truth, a proof certificate or a replacement for qualified domain-expert peer review; AIRR makes the hard filter inspectable instead of asking readers to trust a label.

This repository is the technical foundation for the archive. It keeps lightweight, inspectable sources in Git and publishes large generated artifacts—PDFs, complete source bundles, datasets, and build logs—as GitHub Release assets.

## Current status

AIRR operates the public archive at **[airr.science](https://airr.science/)**. The **currently fee-free private-submission pilot is open** following the recorded production checks and operator authorization on 8 September 2026. Authors [create a private workspace](https://submit.airr.science/account/register) with an alias and password; no invitation, author email or legal name is requested. Each account may submit up to 10 papers in any 24-hour period, shared with its delegated agents. The manuscript enters private quarantine and email carries only an operator notice, never the PDF. Sending a paper does not authorize external AI assessment or public release: those require separate confirmations. A research paper or technical note becomes an AIRR publication only after the editorial workflow and author permission complete and a versioned release is created. New installations remain closed until their own launch checks pass.

The current brand is **AIRR.SCIENCE — Archive for Independent & Rigorous Research**.
Existing `ARR-…` paper identifiers, policy identifiers and the GitHub repository
address remain stable so that citations and integrations keep working. See
[brand and compatibility](docs/BRAND_IDENTITY.md).

## Local checks

```bash
python scripts/validate_papers.py
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

Production builds also serve PDFs alongside each abstract for scholarly crawlers.
See [search indexing and Search Console setup](docs/SEARCH_INDEXING.md) for the
complete build check, PDF integrity rules, and DOI metadata workflow.

Create a concurrent-safe candidate identifier and sharded directory with:

```bash
python scripts/new_record.py --author "Author Name" --type research-paper
python scripts/new_record.py --author "Author Name" --type technical-note
```

Create the next version of an existing record without changing its AIRR identifier:

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

AIRR separates private intake, the public metadata registry, and immutable artifact storage so that GitHub can be replaced or complemented without changing record identifiers. See the [operational configuration and continuity guide](docs/CONFIGURACION_OPERATIVA.es.md), [capacity and migration](docs/SCALE_READINESS.md), [state and evidence labels](docs/STATE_MODEL.md), and the [licensing policy](LICENSE_POLICY.md).

The private intake service is in [`services/intake/`](services/intake/). AIRR does not currently charge for submission, assessment, publication or withdrawal under [`ARR-DEPOSIT-1.9`](docs/DEPOSIT_TERMS.md); any future fee would apply only after advance notice and new terms. New admissions require the version-locked frontier-model gate in [`ARR-ASSESS-1.0`](docs/MODEL_ASSESSMENT_POLICY.md), while legacy records remain honestly labelled `not_assessed`. The operator is Lluis Eriksson, founder, registry operator, responsible editor and GDPR controller. See [privacy](docs/PRIVACY_NOTICE.md), [complaints/contact](docs/LEGAL_AND_COMPLAINTS.md), [retention](docs/RETENTION_SCHEDULE.md), [governance](docs/GOVERNANCE.md) and the [production launch gate](docs/INTAKE_OPERATIONS.md).

Platform software is `AGPL-3.0-or-later`; AIRR-authored documentation is `CC-BY-4.0`; public catalogue metadata is `CC0-1.0`; deposited papers, code and data declare their own scoped licenses.

Historical reproduction environments are preserved with their papers. They are
not the production application's dependencies. Read the
[dependency security notice](docs/DEPENDENCY_SECURITY.md) before running them.

Public author profiles use stable identities from `registry/authors.json`. Paper and
author activity rankings are generated from reproducible provider snapshots under
[`ARR-METRICS-1.0`](docs/METRICS_POLICY.md); missing page-view measurement is never
represented as zero or simulated activity.
