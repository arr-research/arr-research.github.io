# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_site
import check_site_indexing
import site_pdfs
import test_validation


PDF = b"%PDF-1.7\nexact version bytes\n%%EOF\n"
SITE = "https://example.test/preview"


class IndexingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paper = test_validation.PaperValidationTests.make_paper(self, self.root)
        self.paper.metadata["source_of_truth"] = "paper.pdf"
        self.paper.metadata["integrity"].update(
            canonical_sha256=hashlib.sha256(PDF).hexdigest(), canonical_bytes=len(PDF)
        )
        self.timestamp = {
            "publication_state": "published",
            "deposit_recorded_at": "2026-08-13T10:00:00+00:00",
            "published_at": "2026-08-14T10:00:00+00:00",
            "release_tag": f"{self.paper.id}-v1",
        }
        self.cache = self.root / "cache"

    def historical(self):
        self.paper.metadata["status"] = "archived"
        self.paper.metadata["source_of_truth"] = "external_pdf"
        self.paper.metadata["archival_source"] = {
            "mirror_pdf_url": "https://github.com/arr-research/arr-research.github.io/releases/download/bulk/old-v2.pdf"
        }

    def test_local_pdf_bytes_and_version_hash(self):
        (self.paper.path / "paper.pdf").write_bytes(PDF)
        self.assertEqual(site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache), PDF)
        (self.paper.path / "paper.pdf").write_bytes(PDF + b"changed")
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache)

    def test_tex_hash_is_not_compared_with_the_derived_pdf(self):
        (self.paper.path / "paper.pdf").write_bytes(PDF)
        self.paper.metadata["source_of_truth"] = "paper.tex"
        self.paper.metadata["integrity"]["canonical_sha256"] = "a" * 64
        self.assertEqual(site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache), PDF)
        self.paper.metadata["integrity"]["pdf_sha256"] = "b" * 64
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache)

    def test_pending_and_withdrawn_do_not_publish_local_pdf(self):
        (self.paper.path / "paper.pdf").write_bytes(PDF)
        self.assertIsNone(site_pdfs.published_pdf(self.paper, {"publication_state": "pending"}, cache_dir=self.cache))
        self.paper.metadata["status"] = "withdrawn"
        self.assertIsNone(site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache))

    def test_remote_pdf_is_hash_checked_and_cached_without_a_second_download(self):
        self.historical()
        with patch.object(site_pdfs, "urlopen", return_value=io.BytesIO(PDF)) as request:
            # A historical bulk release does not have a per-record release timestamp.
            result = site_pdfs.published_pdf(self.paper, {"publication_state": "pending"}, cache_dir=self.cache, fetch_remote=True)
            self.assertEqual(result, PDF)
            self.assertEqual(site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache), PDF)
            request.assert_called_once()

    def test_remote_offline_miss_does_not_fetch_or_advertise_a_file(self):
        self.historical()
        with patch.object(site_pdfs, "urlopen") as request:
            self.assertIsNone(site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache))
            request.assert_not_called()

    def test_remote_bad_content_fails_without_caching(self):
        self.historical()
        for data, message in [(b"<html>error</html>", "PDF header"), (PDF[:-1], "SHA-256"), (PDF + b"extra", "SHA-256")]:
            with self.subTest(data=data), patch.object(site_pdfs, "urlopen", return_value=io.BytesIO(data)):
                with self.assertRaisesRegex(ValueError, message):
                    site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache, fetch_remote=True)
                self.assertFalse(self.cache.exists())

    def test_cached_bytes_are_revalidated(self):
        self.historical()
        self.cache.mkdir()
        digest = self.paper.metadata["integrity"]["canonical_sha256"]
        (self.cache / f"{digest}.pdf").write_bytes(PDF + b"corruption")
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache)

    def test_remote_failure_and_wrong_size_are_errors(self):
        self.historical()
        with patch.object(site_pdfs, "urlopen", side_effect=OSError("unavailable")):
            with self.assertRaisesRegex(OSError, "unavailable"):
                site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache, fetch_remote=True)
        with self.assertRaisesRegex(ValueError, "byte count"):
            site_pdfs.verify_pdf(PDF, size=len(PDF) + 1)

    def test_remote_requires_a_release_url(self):
        self.historical()
        self.paper.metadata["archival_source"]["mirror_pdf_url"] = "http://localhost/private.pdf"
        with patch.object(site_pdfs, "urlopen") as request:
            with self.assertRaisesRegex(ValueError, "HTTPS GitHub Release"):
                site_pdfs.published_pdf(self.paper, self.timestamp, cache_dir=self.cache, fetch_remote=True)
            request.assert_not_called()

    def render(self, permanent=False, local=True, canonical=SITE):
        with patch.object(build_site, "ROOT", self.root):
            return build_site.build_paper_page(
                self.paper, self.timestamp, [], {self.paper.id: "papers"},
                [dict(self.timestamp, id=self.paper.id, version="v1")],
                {"v1": self.paper}, "v2", permanent, "/preview", canonical,
                "arr-research/arr-research.github.io", local_pdf=local,
            )

    def test_current_and_permanent_pages_link_to_their_own_version(self):
        for permanent in (False, True):
            with self.subTest(permanent=permanent):
                text = self.render(permanent)
                page = check_site_indexing.Page(text)
                suffix = "versions/v1/" if permanent else ""
                expected = f"{SITE}/papers/{self.paper.id}/{suffix}{self.paper.id}-v1.pdf"
                self.assertEqual(page.meta["citation_pdf_url"], [expected])
                self.assertIn(expected.removeprefix("https://example.test"), page.links)
                self.assertIn(self.paper.metadata["abstract"], text)
                self.assertLess(text.index('<section class="abstract">'), text.index('class="timestamp-panel"'))
                self.assertEqual(page.meta["citation_publication_date"], ["2026/08/13"])
                self.assertEqual(page.meta["citation_online_date"], ["2026/08/14"])

    def test_no_external_or_relative_pdf_citation_in_offline_preview(self):
        for local, canonical in [(False, SITE), (True, "")]:
            page = check_site_indexing.Page(self.render(local=local, canonical=canonical))
            self.assertNotIn("citation_pdf_url", page.meta)

    def test_doi_and_special_characters_are_preserved(self):
        self.paper.metadata["doi"] = "10.1234/example"
        self.paper.metadata["title"] = 'A < B & "C"'
        self.paper.metadata["authors"].append({"name": "Second Author"})
        text = self.render()
        page = check_site_indexing.Page(text)
        self.assertEqual(page.meta["citation_title"], ['A < B & "C"'])
        self.assertEqual(page.meta["citation_author"], ["Test Author", "Second Author"])
        self.assertEqual(page.meta["citation_doi"], ["10.1234/example"])
        structured = json.loads(text.split('<script type="application/ld+json">')[1].split("</script>")[0])
        self.assertIn("https://doi.org/10.1234/example", structured["identifier"])
        self.assertEqual(structured["encoding"]["contentUrl"], page.meta["citation_pdf_url"][0])

    def test_verification_token_is_optional_and_escaped_on_the_homepage(self):
        timestamps = {(self.paper.id, self.paper.version): self.timestamp}
        for token in ("", 'google-token"<&'):
            text = build_site.build_home([self.paper], timestamps, "/preview", SITE, google_site_verification=token)
            page = check_site_indexing.Page(text)
            self.assertEqual(page.meta.get("google-site-verification"), [token] if token else None)

    def test_site_checker_rejects_missing_and_cross_directory_pdfs(self):
        root = self.root / "site"
        page_dir = root / "papers" / self.paper.id
        page_dir.mkdir(parents=True)
        path = page_dir / "index.html"
        text = self.render()
        path.write_text(text, encoding="utf-8")
        canonical = f"{SITE}/papers/{self.paper.id}/"
        (root / "sitemap.xml").write_text(f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{canonical}</loc></url></urlset>')
        (root / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
        errors, _, _ = check_site_indexing.check_site(root, SITE)
        self.assertTrue(any("PDF is missing" in error for error in errors))
        (page_dir / f"{self.paper.id}-v1.pdf").write_bytes(PDF)
        self.assertEqual(check_site_indexing.check_site(root, SITE), ([], 1, 1))
        path.write_text(text.replace('name="citation_pdf_url"', 'name="unused"'), encoding="utf-8")
        errors, _, _ = check_site_indexing.check_site(root, SITE)
        self.assertTrue(any("no citation_pdf_url" in error for error in errors))
        path.write_text(text.replace(f'{canonical}{self.paper.id}-v1.pdf', 'https://github.com/other.pdf'), encoding="utf-8")
        errors, _, _ = check_site_indexing.check_site(root, SITE)
        self.assertTrue(any("same directory" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
