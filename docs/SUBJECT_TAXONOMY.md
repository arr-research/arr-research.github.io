# AIRR research subjects

AIRR-SUBJECTS-1 (reviewed 2026-09-07) separates the fields an author can
choose from the subjects already represented in the archive. It contains 1,086
selectable fields: 1,030 active EuroSciVoc concepts and 56 AIRR additions.

## Coverage and sources

The six EuroSciVoc families cover natural sciences; engineering and technology;
medical and health sciences; agricultural sciences (including veterinary
research); social sciences; and humanities (including arts). AIRR adds an
interdisciplinary/emerging family and specialities for its mathematical work,
formal proofs, AI agents, AI safety and evaluation, and research methods.

- [EuroSciVoc, Publications Office of the European Union](https://op.europa.eu/en/web/eu-vocabularies/euroscivoc)
  provides the multilingual, hierarchical base. It extends the OECD Frascati
  research-field classification. This is a pinned **1.5.0** snapshot issued
  2025-06-25, not a claim to use the latest release. The EU catalogue currently
  also lists 1.6; upgrades require review rather than changing author choices
  through a live external dependency.
- [OECD Frascati Manual 2015, table 2.2](https://www.oecd.org/content/dam/oecd/en/publications/reports/2015/10/frascati-manual-2015_g1g57dcb/9789264239012-en.pdf)
  was consulted for the breadth of research families.
- [arXiv category taxonomy](https://arxiv.org/category_taxonomy) was consulted
  to check the need for mathematical, computing and physics specialities. AIRR
  does not claim an arXiv crosswalk or identical admission scope.

No finite taxonomy covers every future speciality. Authors may choose a broad
field, one main and up to two additional fields, and a specific/emerging topic
of up to 200 characters. The “Other or emerging research areas” choice requires
a description. Subject availability is distinct from reviewer availability and
editorial acceptance; the admission policy remains unchanged.

## Data, provenance and maintenance

`registry/euroscivoc.json` preserves source concept URIs, six-language preferred
labels, alternate labels, the exact download URL, source version and SHA-256.
Its English labels are initial-capitalised and surrounding whitespace is
trimmed. Deprecated concepts are excluded. The EU source is **CC BY 4.0**;
the [official dataset catalogue API](https://data.europa.eu/api/hub/search/datasets/euroscivoc-the-european-science-vocabulary)
lists that licence for the 1.5 distribution. Attribution, adaptation and licence
links are displayed in the directory and exported JSON. AIRR additions are also
made available under CC BY 4.0. No EU endorsement is implied.

`registry/subject-extensions.json` holds reviewed additions and explicit
aliases. IDs, not labels or positions, identify selections. New IDs must never
reuse an existing meaning. Source updates and local additions require a separate
review of removed IDs, changed parents, duplicate labels and translations.

To reproduce the base, install `rdflib` in a maintenance-only environment,
download the URL recorded in the base JSON, check its SHA-256 and run:

```console
python scripts/import_subject_vocabulary.py /path/to/EuroSciVoc.ttl --source-url SOURCE_URL
```

Neither the website build nor the intake runtime needs rdflib or network
access to the EU service. `scripts/subjectlib.py` is the shared loader.
`/assets/subjects.json` is the public machine-readable catalogue for authors and
agents. The private service serves the same vocabulary at
`/subject-catalogue.json`; that endpoint contains no submission data.

## Discovery and compatibility

The directory has expandable families, accent-insensitive search, translated
and alternate terms, a family filter and a “with papers only” filter. Search
results are paginated in batches of 48; native expandable sections remain usable
without JavaScript or if the searchable JSON cannot load. Empty fields are
visible but do not generate thousands of empty indexed landing pages.

Existing deposited metadata, PDFs, hashes and subject URLs are unchanged.
Explicit English labels and curated aliases classify existing records for
discovery. Source translations and broad alternate keywords help people find
fields but do not infer a paper's classification. Ambiguous labels are not
assigned silently. Every current deposited label has a reviewed mapping.

For example, “Quantum information theory” and “Quantum information” share the
new discovery field; “Physics — Quantum Physics” maps to “Quantum physics”.
The old deposited-label routes/filters remain available. Parent counts include
all classified descendants and deduplicate each current paper; a paper may
appear in several fields, so counts across fields are not additive. Historical
imports remain labelled. A previously unknown label still has its original
subject page and exact search filter; add a reviewed mapping before relying on
the new family directory for it.

## Private intake

The form supports the same catalogue with one required main subject, two
optional distinct additional subjects, a searchable native-select fallback and
an optional topic. A public “Use subject” link preserves the selected ID through
the public submission information page and into a configured private receiver.
When no receiver is configured, the page explicitly says uploads are closed and
no manuscript was registered.

Server validation checks IDs, duplicates, count limits and emerging-topic
requirements before storing files. SQLite stores a versioned classification
snapshot (IDs and labels), separate from the exact PDF. Receipts and the editor
view show it with HTML escaping; it is cleared by the existing retention sweep.
`flask --app services.intake.app init-db` adds the classification column
idempotently to an existing database. Old cases are labelled “not supplied”.

An editor reviews classification before any later public release. Carry the
reviewed canonical labels into public `subjects`, and the free topic into
appropriate public keywords only after review; verify the discovery mapping.
Private intake does not publish papers automatically or create public IDs.
This change does **not** deploy or enable the private receiver.

## Verification and rollback

Run Python repository/intake tests, both Node search suites, the static build
and `check_site_indexing.py`. Check desktop/mobile browsing, a translated query,
an empty field, an alias merge, filtered paper counts and form selection.
Taxonomy and UI changes are isolated in one PR and can be reverted without
changing research records. The additive database column is harmless if code is
rolled back; do not drop it or erase existing classifications during rollback.
