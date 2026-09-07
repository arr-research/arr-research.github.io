# Reading, discovery and citations

AIRR provides a static, crawlable catalogue and version-specific reference exports. A reader can find a paper, open its PDF, inspect its history and download a citation without an account. The dark, gold and serif visual identity is retained.

## Citation contract

Every source-backed version has four exports next to its permanent landing page:

```text
/papers/<id>/versions/<version>/citation.txt
/papers/<id>/versions/<version>/citation.bib
/papers/<id>/versions/<version>/citation.ris
/papers/<id>/versions/<version>/citation.csl.json
```

Technical notes use `/notes/`. The latest-record page exports the version currently displayed; each older landing page exports its own version. Exports use the metadata's title, author names and original publication date, never the build date or historical-import date. Registered DOI metadata is included only when present. No journal title or peer-review status is inferred. BibTeX uses `misc`, RIS uses `UNPB`, and CSL uses the generic `article` type with a manuscript/note genre, not `article-journal`. CSL author names are literal because the current schema does not distinguish given/family names reliably.

The displayed reference is a plain citation, not a claim to implement APA, Chicago or a publisher-specific style. Reference managers can import BibTeX, RIS or CSL JSON to apply their styles. The manuscript's historical ARR identifier remains intact.

## Reader behaviour

The title, authors, download links and full abstract are server-rendered HTML. Copy controls are progressively enhanced; exports and the selectable permalink remain usable without JavaScript. The optional PDF preview inserts a same-origin browser PDF iframe only when opened. Unsupported PDF viewers have a direct PDF link. No third-party viewer, new runtime dependency or analytics is added.

Versions, verification, model assessments and disclosures have direct anchors. Original provenance and activity definitions remain available in a native disclosure panel. Model scores and donation activity do not influence search relevance.

## Discovery

The home page prioritizes search, subject browsing and recent records. Subjects have static, paginated HTML pages (50 records per page) and sitemap entries. Case and whitespace variants share a group; this is not a curated scientific taxonomy. Other aliases require editorial review. Subject URLs use a readable stem plus a deterministic short hash to avoid collisions.

The search page supports subject, record status, publication year and relevance/date/title sorting. Empty queries browse the catalogue. Filters are reflected in the URL and restored by browser navigation. An obsolete subject/year returns no matches rather than silently dropping the filter. Existing scientific-notation matching is retained, including distinctions between SU(2) and SU(3). The original chronological HTML catalogue remains available without JavaScript.

## Validation and scope

`python -m unittest discover -s tests -v` and `node --test tests/search.test.cjs` cover exact-version citations, original dates, special characters, RIS injection, withdrawn/historical status, subject grouping, scientific relevance and intersecting filters. Build with the production canonical URL and run `scripts/check_site_indexing.py` to verify scholarly metadata, sitemaps and same-directory PDFs.

This feature does not register DOIs, certify Google Scholar inclusion, change paper bytes or assessment results, or enable the private submission service. DOI registration, preservation agreements, verified author identities and independent editorial participation are separate workstreams.

## Rollback

The starting main commit is `32f507861c3843f5b8403ff16b80a44c448070f7`. Revert the reader-experience change through a new commit/PR, preserving later deposits and operational changes. Do not reset or force-push main. Once citation URLs are in use, retain those routes and exports even if the visual design is reverted.
