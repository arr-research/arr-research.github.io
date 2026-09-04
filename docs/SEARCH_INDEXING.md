# ARR search discovery

ARR remains the primary catalogue. GitHub Releases retain the immutable artifacts;
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
python scripts/build_site.py --canonical-url https://arr-research.github.io --repository arr-research/arr-research.github.io --fetch-remote-pdfs
python scripts/check_site_indexing.py --canonical-url https://arr-research.github.io
python -m unittest discover -s tests -v
```

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
   `https://arr-research.github.io/`.
2. Choose the HTML tag verification method. Copy only the `content` value of
   Google's `google-site-verification` meta tag into the GitHub Actions repository
   variable **ARR_GOOGLE_SITE_VERIFICATION**. It is a public verification token,
   not a Google password or access token. Do not invent a value.
3. Run **Publish ARR catalogue**. Its build writes the escaped verification tag
   to the homepage. Confirm the tag is present in the deployed HTML source, then
   click **Verify** in Search Console. Keep the variable after verification.
4. Submit `https://arr-research.github.io/sitemap.xml` using the Sitemaps report.
5. Inspect several current and permanent-version URLs. Record Google's reported
   canonical, last crawl, fetch result, indexing status, and exclusion reason.
   Use the live URL test and request indexing for representative corrected pages.

Verification, sitemap submission and index requests must be confirmed in the
operator's Search Console session. A successful build or a DOI does not establish
that these account-level steps happened or that Google indexed the pages.

## Bibliographic checks and external archives

Before a deposit or correction, compare the **entire author-written abstract**,
title, actual authors, cited publication date and exact PDF version with the
registry metadata. Preserving the full registry abstract in HTML does not itself
prove that its text matches the manuscript. The PDF should contain searchable
text, the title and authors on its first page, and a References/Bibliography
section. Scholar documents a 5 MB limit. Do not rewrite immutable manuscripts or
their hashes just to alter search metadata; use ARR's correction/version workflow
when bibliographic or manuscript changes are needed.

The metadata field `date` remains the cited publication date. For an actual ARR
release, `citation_online_date` uses the release timestamp instead of falsely
repeating the manuscript date. Historical source dates and ARR version identifiers
retain their existing provenance.

For Zenodo, first identify the selected ARR IDs and exact versions. Make one
record per work with its PDF and verification certificates, cite the ARR page,
preserve authorship and licensing, and reuse an existing DOI when the publication
already has one. After a DOI is actually assigned, put its bare value (such as
`10.5281/zenodo.RECORD_NUMBER`) in that version's metadata `doi` field. ARR emits a
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
