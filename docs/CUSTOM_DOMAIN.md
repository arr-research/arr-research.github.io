# Custom domain: airr.science

The public catalogue remains hosted by GitHub Pages in
`arr-research/arr-research.github.io`. The purchased domain is `airr.science`,
with `www.airr.science` redirecting to the apex. Porkbun remains the DNS provider;
no paid web-hosting service or nameserver transfer is needed.

## Configure and verify

1. In the **organization** Settings > Pages, add `airr.science` as a verified
   domain. Create the TXT record `_github-pages-challenge-arr-research` using
   the exact value GitHub supplies. Confirm the DNS answer, finish verification
   in GitHub, and keep this record permanently.
2. In the **repository** Settings > Pages, set the custom domain to
   `airr.science` before pointing the domain's web records at GitHub.
3. Replace only Porkbun's parking records at the apex and `www` with the records
   below. Preserve unrelated TXT, mail, and other service records. Do not add
   wildcard records. Save the previous DNS values before changing them.

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | arr-research.github.io |

4. Run **Publish ARR catalogue**. The build gets `base_url` and `base_path`
   from `actions/configure-pages`, rather than inferring them from the repository
   name. All discovery URLs use HTTPS. This repository deploys through Actions,
   so a source `CNAME` file is neither required nor used by GitHub Pages.
5. Wait for GitHub's certificate to cover the apex and `www`; enable **Enforce
   HTTPS** once available. Do not report HTTPS as ready based only on successful
   DNS checks. Verify it with normal certificate validation.
6. Check the homepage, search, a current paper, an older version and their PDFs.
   Check that `www` and the former GitHub Pages address redirect to the correct
   new paths, retaining paper identifiers. Verify `robots.txt`, `sitemap.xml`,
   article canonical URLs, PDF citations and publisher URLs use `airr.science`.
7. Follow [Search Console operations](SEARCH_INDEXING.md#google-search-console)
   to establish the new property and monitor indexing. A deployment or IndexNow
   notification does not prove that Google has indexed the new domain.

## Rollback

If a rollback is necessary, first restore the saved Porkbun web records while
the custom domain is still assigned in GitHub. Then remove the repository's
custom domain and run **Publish ARR catalogue** again. Its configured URL will
return to `https://arr-research.github.io/`. Keep the organization verification
TXT record. Do not leave DNS pointing at GitHub after removing its domain claim.
Domain settings and DNS changes do not modify the immutable papers or their IDs.

## Primary documentation

- [GitHub: manage a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [GitHub: verify domain ownership](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [Porkbun: connect a domain to GitHub Pages](https://kb.porkbun.com/article/64-how-to-connect-your-domain-to-github-pages)
