# Reading, discovery and citations

AIRR provides a static, crawlable catalogue and version-specific reference exports. A reader can find a paper, open its PDF, inspect its history and download a citation without an account. The gold and serif identity is kept.

## Reading defaults (2026-09-19)

These choices follow the reading and credibility evidence summarised in the September 2026 audit.

- **Colour theme.** Pages use dark text on light paper by default. Positive polarity reads better for younger and older adults (Piepenbrock et al., *Ergonomics* 2013; *Human Factors* 2014). Readers whose system asks for dark mode get the original dark palette through `prefers-color-scheme`. Nothing is stored in the browser.
  - Both palettes are CSS variables in `site/style.css`.
  - `tests/test_theme.py` requires WCAG AA contrast (4.5:1) for all reading text in both themes, and rejects fixed colours outside the palettes.
- **Mathematics.** Inline TeX in titles, abstracts, listings and search results is typeset with KaTeX 0.18.7. KaTeX is vendored under `site/vendor/katex/` (MIT) and served from AIRR, so no third-party request is made. It loads only on pages that contain TeX. Citation text, permalinks and exports stay verbatim.
  - Search-engine metadata uses the Unicode rendering in `scripts/texlib.py`.
- **Line length.** Listing summaries are capped at 75 characters per line, following WCAG 1.4.8 and Dyson & Haselgrove 2001.
- **Review status.** Badges read *Screened*, *Working paper* or *Historical import*. Hovering a badge explains it, and each record repeats the explanation under the title. Every explanation says the record is not peer reviewed (Wingen et al. 2022). The formal status value `accepted` and the policies that define it are unchanged.
- **Scores.** Model scores and stars appear only in the record's screening section and on `/assessments/`, never in listings. This avoids false precision next to titles (Leiden Manifesto, principle 8).
- **Activity.** The author ranking appears only when at least three author profiles exist.

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

The compact home page places the introduction beside search on desktop and stacks them on mobile. Subject links use a compact row that wraps on desktop and scrolls horizontally on mobile; the latest papers precede archive statistics and the detailed admission strip. A short admission explanation remains beside the catalogue. This layout keeps the existing search form, paper records and discovery metadata.

The search page supports subject, record status, publication year and relevance/date/title sorting. Empty queries browse the catalogue. Filters are reflected in the URL and restored by browser navigation. An obsolete subject/year returns no matches rather than silently dropping the filter. Existing scientific-notation matching is retained, including distinctions between SU(2) and SU(3). The original chronological HTML catalogue remains available without JavaScript.

Paper lists share a full-width row layout across home, catalogue, subjects, author profiles and search. Titles and summaries use the available row width. Record identity and date share a wrapping header; authors and the version-specific citation link share a byline. Wide-screen summaries use two lines and smaller screens use three; complete abstracts remain on each paper page. The manuscript-reading column keeps its separate readable width.

## Validation and scope

`python -m unittest discover -s tests -v` and `node --test tests/search.test.cjs` cover exact-version citations, original dates, special characters, RIS injection, withdrawn/historical status, subject grouping, scientific relevance and intersecting filters. Build with the production canonical URL and run `scripts/check_site_indexing.py` to verify scholarly metadata, sitemaps and same-directory PDFs.

This feature does not register DOIs, certify Google Scholar inclusion, change paper bytes or assessment results, or enable the private submission service. DOI registration, preservation agreements, verified author identities and independent editorial participation are separate workstreams.

## Rollback

The starting main commit is `32f507861c3843f5b8403ff16b80a44c448070f7`. Revert the reader-experience change through a new commit/PR, preserving later deposits and operational changes. Do not reset or force-push main. Once citation URLs are in use, retain those routes and exports even if the visual design is reverted.

For the subsequent compact-homepage adjustment alone, the baseline is `cee7b0bb9d7c9489a8a47d70683e89d21b588baa`. Revert only that adjustment's commit; all citation and reading features remain available.

The full-width paper-list adjustment starts from `b8ecb838c8a46ff1cd49b50abc051d85b5cf07fb` and can be reverted separately from the compact homepage.
