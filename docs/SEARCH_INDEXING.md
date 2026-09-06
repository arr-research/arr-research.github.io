# AIRR.SCIENCE search discovery

AIRR.SCIENCE (Archive for Independent & Rigorous Research) is the primary catalogue.
The archive previously used the name ARR and `arr-research.github.io`. Existing
ARR record identifiers, hashes, manuscript titles and versions remain unchanged.
GitHub Releases retain the immutable artifacts;
the Pages build also serves exact PDF copies alongside the current abstract and
each available version abstract, for example:

```text
/papers/ARR-ID/ARR-ID-v2.pdf
/papers/ARR-ID/versions/v1/ARR-ID-v1.pdf
/papers/ARR-ID/versions/v2/ARR-ID-v2.pdf
```

Technical notes use `/notes/`. The current page copies only its current version.
Each page's `citation_pdf_url`, structured-data `contentUrl`, and direct download
link refer to its own copy. Releases and source bundles remain linked separately.
The complete registry abstract is visible immediately after the title and authors.

## Build and verify

```bash
python scripts/validate_papers.py
python scripts/build_site.py --canonical-url https://airr.science --repository arr-research/arr-research.github.io --fetch-remote-pdfs
python scripts/check_site_indexing.py --canonical-url https://airr.science
python -m unittest discover -s tests -v
```

The production Pages workflow reads its public URL and path from GitHub Pages,
so custom domains are reflected in canonical links, publisher structured data,
PDF citations, the sitemap and robots.txt. See [custom-domain operations](CUSTOM_DOMAIN.md).
The production Pages workflow enables remote PDF fetching. Local PDFs are copied
from their exact source snapshots. Historical public Release assets are downloaded
into `work/pdf-cache/` by recorded SHA-256 and checked for their PDF header, hash,
and byte count. Cache hits are checked again; invalid content or a failed download
stops the build before deployment. GitHub Actions caches verified historical files
to avoid repeatedly downloading the entire collection. No PDF binaries are added
to Git by this process. For TeX-origin records, `pdf_sha256`/`pdf_bytes` identify the
derived PDF when supplied; `canonical_sha256` can identify the TeX source instead.

Without `--fetch-remote-pdfs`, local checks can run offline. Missing historical
cache entries retain the external download button but omit `citation_pdf_url` and
the structured PDF encoding; no nonexistent local file is advertised. With no
`--canonical-url`, local links still work and absolute PDF citation tags are omitted.

Pending new publications and withdrawn records do not acquire new PDF copies.
Historical imports have an existing author-authorized public bulk release and are
eligible even though their per-record release timestamps are marked pending.
Source-only records receive no PDF citation until a PDF is supplied.

The build checker verifies that article canonicals and sitemap URLs resolve to
generated files, every advertised PDF exists alongside its abstract, and a direct
HTML download link is present. The sitemap includes paginated catalogue pages.
The existing IndexNow notification is for participating search engines; it is not
a Google Search Console or Google Scholar submission.

## Google Search Console

1. Open [Search Console](https://search.google.com/search-console/) using the
   operator's Google account. Add the **URL-prefix** property
   `https://airr.science/`. Keep the existing `https://arr-research.github.io/`
   property to monitor the old URLs during migration.
2. Choose the HTML tag verification method. Copy only the `content` value of
   Google's `google-site-verification` meta tag into the GitHub Actions repository
   variable **ARR_GOOGLE_SITE_VERIFICATION_AIRR**. Keep the previous
   **ARR_GOOGLE_SITE_VERIFICATION** variable intact. The workflow passes both
   values, one per line, and the homepage emits separate escaped tags so old
   ownership verification is preserved. These are public verification tokens,
   not Google passwords or access tokens. Do not invent values.
3. Run **Publish AIRR catalogue**. Its build writes the escaped verification tag
   to the homepage. Confirm the tag is present in the deployed HTML source, then
   click **Verify** in Search Console. Keep the variable after verification.
4. Submit `https://airr.science/sitemap.xml` using the Sitemaps report.
5. Open the old property's Settings > Change of address, choose the verified
   `https://airr.science/` property, run Google's checks and submit the move.
   Keep the old property and the path-preserving permanent redirects; do not use
   URL removals to perform a migration. Record the actual confirmation separately.
6. Inspect several current and permanent-version URLs. Record Google's reported
   canonical, last crawl, fetch result, indexing status, and exclusion reason.
   Use the live URL test and request indexing for representative corrected pages.

Verification, sitemap submission and index requests must be confirmed in the
operator's Search Console session. A successful build or a DOI does not establish
that these account-level steps happened or that Google indexed the pages.

## Search-result name

The homepage declares a `WebSite` with preferred name `AIRR.SCIENCE`, alternate
names `AIRR`, the expanded archive name and `airr.science`, and the configured
canonical root. Open Graph site name, page titles, the visible homepage, publisher
metadata and the LLM guides use the new identity. No legal registration status
is implied by the public archive name.

Google chooses the displayed name and must recrawl the site after a change.
Verification and sitemap acceptance do not guarantee indexing, a chosen display
name or an immediate replacement of old search results. See Google's
[site-name guidance](https://developers.google.com/search/docs/appearance/site-names)
and [domain-migration guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).

## Site icon

The shared page header links to AIRR's gold A and three-node mark on black in SVG, 96-pixel PNG,
multi-size ICO (16, 32 and 48 pixels), and a 180-pixel Apple touch icon. The build
copies these assets from `site/` to the public root and respects `--base-path`.
The SVG is a self-contained wrapper around a PNG rendition of the mark.
The header displays the approved transparent AIRR.SCIENCE logo (`site/airr-logo.png`),
with the subtitle "Archive for Independent & Rigorous Research" and an accessible
home-link label. The compact 1859-by-336 PNG is shown at its natural aspect ratio
and scales to fit narrow screens. The previous `assets/arr-logo.png` URL remains
available for cached pages.
Keep their URLs stable. The 96-pixel PNG provides a square raster image above
Google's recommended 48-pixel size, and `robots.txt` permits image crawling.

After deployment, confirm that the homepage links and icon files return HTTP 200.
The operator can request a homepage recrawl in Search Console. Google may take
days to weeks to process the icon and does not guarantee its display; IndexNow
does not request a Google recrawl. See
[Google's favicon guidance](https://developers.google.com/search/docs/appearance/favicon-in-search).

## Bibliographic checks and external archives

Before a deposit or correction, compare the **entire author-written abstract**,
title, actual authors, cited publication date and exact PDF version with the
registry metadata. Preserving the full registry abstract in HTML does not itself
prove that its text matches the manuscript. The PDF should contain searchable
text, the title and authors on its first page, and a References/Bibliography
section. Scholar documents a 5 MB limit. Do not rewrite immutable manuscripts or
their hashes just to alter search metadata; use AIRR's correction/version workflow
when bibliographic or manuscript changes are needed.

The metadata field `date` remains the cited publication date. For an actual AIRR
release, `citation_online_date` uses the release timestamp instead of falsely
repeating the manuscript date. Historical source dates and AIRR version identifiers
retain their existing provenance.

For Zenodo, first identify the selected AIRR IDs and exact versions. Make one
record per work with its PDF and verification certificates, cite the AIRR page,
preserve authorship and licensing, and reuse an existing DOI when the publication
already has one. After a DOI is actually assigned, put its bare value (such as
`10.5281/zenodo.RECORD_NUMBER`) in that version's metadata `doi` field. AIRR emits a
visible DOI link, `citation_doi`, a Dublin Core identifier and a JSON-LD identifier.
Neither a DOI nor a deposit is created by this site build. arXiv submissions remain
a separate author-account workflow.

## Initial bibliographic spot check, 2026-09-05

The following is an open editorial follow-up, not a claim of full Scholar
compliance. No manuscript or immutable source metadata was changed by the site
repair.

| Record and version | PDF comparison | Follow-up |
| --- | --- | --- |
| `ARR-2026-5QQF95VHTC9GABH8 v1` (norm-optimal self-commutator rank) | First-page title, Lluis Eriksson and 30 August 2026 agree. The registry abstract is a shorter reformulation with additional scope wording. | Reconcile the public abstract with the complete author-written manuscript abstract through a documented bibliographic correction. |
| `ARR-2026-7H9FAPTBZA897AMJ v2` (Haar two-plane phase diagram) | Lluis Eriksson and 14 August 2026 agree. The PDF's subtitle additionally includes “sharp thermodynamic contact asymptotics”; its abstract and the registry abstract differ in wording. | Reconcile the citation title/subtitle and the complete abstract with the exact PDF. |

Both inspected first pages have searchable text. The full build checks file
identity and links across the catalogue; it does not adjudicate scientific claims
or automatically certify author-written abstracts. The operator's eight selected
Zenodo deposits have not been identified or created by this change.

## Primary documentation

- [Google Scholar inclusion guidelines](https://scholar.google.com/intl/en/scholar/inclusion.html)
- [Verify site ownership](https://support.google.com/webmasters/answer/9008080)
- [Ask Google to recrawl](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
- [Zenodo DOI guidance](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/)
