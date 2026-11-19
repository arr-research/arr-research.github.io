# SPDX-License-Identifier: AGPL-3.0-or-later
import hashlib
import json
import unittest
from unittest.mock import patch

from services.intake import programme_release_sync as sync


class PublicReadbackTests(unittest.TestCase):
    def setUp(self):
        paper = "ARR-2026-56MSF5D1YA8QDAXM"
        self.pdf = b"%PDF-1.5 fixture"
        self.sha = hashlib.sha256(self.pdf).hexdigest()
        report = {"paper_id": paper, "version": "v1", "version_id": "fixture-version",
                  "canonical_sha256": self.sha, "millennium_score": 4, "unresolved_material_objections": []}
        review = json.dumps(report).encode()
        item = self.item = {"paper": paper, "version": "v1", "month": "11",
                            "submission": "SUB-0000000000000001", "sha256": self.sha,
                            "report_sha256": hashlib.sha256(review).hexdigest()}
        tag = paper + "-v1"
        asset = "https://github.com/" + sync.REPO + "/releases/download/" + tag
        metadata = json.dumps({"id": paper, "version": "v1", "version_id": "fixture-version",
            "status": "working_paper", "source_of_truth": "paper.pdf", "authors": [{"name": "Test Author"}],
            "integrity": {"canonical_bytes": len(self.pdf), "canonical_sha256": self.sha},
            "licenses": {"manuscript": "CC-BY-4.0", "metadata": "CC0-1.0"}}).encode()
        src = "https://raw.githubusercontent.com/" + sync.REPO + "/" + tag + "/papers/2026/11/56/" + paper
        self.mirror = "https://airr.science/papers/" + paper + "/versions/v1/" + tag + ".pdf"
        self.report_url = src + "/screening/original/exact-pdf-assessment.json"
        self.receipt_url = src + "/authority/receipt.json"
        self.files = {
            self.mirror: self.pdf, self.report_url: review, asset + "/RECORD.json": metadata,
            src + "/metadata.json": metadata,
            self.receipt_url: json.dumps({"registration_number": item["submission"], "sha256": self.sha,
                                            "scan_status": "clean"}).encode(),
            "https://api.github.com/repos/" + sync.REPO + "/releases/tags/" + tag: json.dumps({
                "tag_name": tag, "html_url": sync.release_url(item), "draft": False, "prerelease": False,
                "published_at": "2026-11-19T03:27:43Z", "assets": [{"name": tag + ".pdf",
                "size": len(self.pdf), "browser_download_url": asset + "/" + tag + ".pdf",
                "digest": "sha256:" + self.sha}]}).encode()}

    def test_public_artifacts_must_match_together(self):
        def check():
            with patch.object(sync, "fetch", side_effect=lambda url, limit: self.files[url]):
                return sync.public_evidence(self.item, "Test Author", len(self.pdf))
        self.assertEqual(check(), "fixture-version")
        for url, data in [(self.mirror, b"%PDF-1.5 changed"),
                          (self.report_url, self.files[self.report_url] + b"\n"),
                          (self.receipt_url, self.files[self.receipt_url].replace(b"0001", b"0002"))]:
            with self.subTest(url=url), patch.dict(self.files, {url: data}), self.assertRaises(ValueError):
                check()

    def test_unknown_source_is_rejected(self):
        with self.assertRaises(ValueError):
            sync.allowed("https://example.org/")
