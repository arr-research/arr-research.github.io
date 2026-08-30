# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import json
import io
import tempfile
import unittest
import uuid
from pathlib import Path
from contextlib import redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from arrlib import (  # noqa: E402
    CROCKFORD,
    Paper,
    crockford_prefix,
    group_paper_versions,
    iter_package_files,
    select_paper,
    validate_collection,
    validate_paper,
    validate_record_timestamps,
)
import new_record  # noqa: E402
import new_version  # noqa: E402
import arrlib  # noqa: E402
import build_site  # noqa: E402
import submit_indexnow  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]


class PaperValidationTests(unittest.TestCase):
    def make_paper(self, root: Path) -> Paper:
        paper_dir = root / "2026" / "08" / "0J" / "ARR-2026-0J7S2PFT4V8B9T8N"
        paper_dir.mkdir(parents=True)
        metadata = {
            "schema_version": "1.1",
            "record_id": "arr:record:123e4567-e89b-42d3-a456-426614174000",
            "version_id": "arr:version:123e4567-e89b-42d3-a456-426614174001",
            "id": "ARR-2026-0J7S2PFT4V8B9T8N",
            "version": "v1",
            "record_type": "research_paper",
            "title": "A complete and testable research title",
            "abstract": "This abstract is deliberately long enough to state a question, method, result, scope, and limitation.",
            "authors": [{"name": "Test Author"}],
            "date": "2026-08-13",
            "status": "accepted",
            "licenses": {
                "manuscript": "CC-BY-4.0",
                "metadata": "CC0-1.0",
                "code": [{"path": "src/", "spdx": "Apache-2.0"}],
                "data": [],
            },
            "source_of_truth": "paper.tex",
            "deposit": {
                "depositor_name": "Test Author",
                "relationship": "author",
                "deposit_authorized": True,
                "third_party_material_disclosed": True,
                "terms_version": "ARR-DEPOSIT-0.1",
            },
            "integrity": {"algorithm": "sha256", "manifest": "MANIFEST.sha256"},
            "ai_assistance": {"used": False, "statement": "No AI assistance was used for this test record."},
            "screening": {
                "protocol": "ARR-SCREEN-1.0",
                "status": "not_assessed",
                "critical_objections_unresolved": 0,
                "human_signoff": True,
                "evaluators": [],
            },
            "verification": {
                "protocol": "ARR-VERIFY-1.0",
                "bibliography": "pass",
                "source_integrity": "pass",
                "reproducibility": "not_applicable",
                "lean4": "not_applicable",
            },
            "editorial": {
                "decision": "standard_acceptance",
                "signed_by": "Test Editor",
                "conflicts": [],
                "statement": "The test editor signed this exact version without a declared conflict.",
            },
        }
        provenance = {
            "schema_version": "1.0",
            "record_id": metadata["record_id"],
            "version_id": metadata["version_id"],
            "source_of_truth": metadata["source_of_truth"],
        }
        license_record = {
            "manuscript": {"spdx": "CC-BY-4.0"},
            "metadata": {"spdx": "CC0-1.0"},
            "code": [{"path": "src/", "spdx": "Apache-2.0"}],
            "data": [],
        }
        for name, content in {
            "metadata.json": json.dumps(metadata),
            "paper.tex": "\\documentclass{article}\\begin{document}Test\\end{document}",
            "paper.md": "# Test",
            "PROVENANCE.json": json.dumps(provenance),
            "LICENSES.json": json.dumps(license_record),
            "CITATION.cff": "cff-version: 1.2.0",
        }.items():
            (paper_dir / name).write_text(content, encoding="utf-8")
        (paper_dir / "LICENSES").mkdir()
        return Paper(paper_dir, metadata)

    def test_valid_complete_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            self.assertEqual(validate_paper(paper), [])

    def test_scholarly_discovery_metadata_is_complete(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            canonical = f"https://arr-research.github.io/papers/{paper.id}/"
            release = f"https://github.com/arr-research/arr-research.github.io/releases/tag/{paper.id}-{paper.version}"
            pdf = f"https://github.com/arr-research/arr-research.github.io/releases/download/{paper.id}-{paper.version}/{paper.id}-{paper.version}.pdf"
            head = build_site.scholarly_head(paper.metadata, canonical=canonical, release_url=release, pdf_url=pdf)
            self.assertIn('name="citation_title"', head)
            self.assertIn('name="citation_author"', head)
            self.assertIn('name="citation_pdf_url"', head)
            self.assertIn('name="DC.identifier"', head)
            self.assertIn('property="og:type" content="article"', head)
            self.assertIn('type="application/ld+json"', head)
            self.assertIn('"@type":"ScholarlyArticle"', head)
            self.assertIn('"contentUrl":', head)

    def test_indexnow_payload_is_host_scoped(self) -> None:
        urls = [
            "https://arr-research.github.io/",
            "https://arr-research.github.io/papers/ARR-2026-0J7S2PFT4V8B9T8N/",
        ]
        payload = submit_indexnow.make_payload(
            "https://arr-research.github.io/",
            "0123456789abcdef0123456789abcdef",
            urls,
        )
        self.assertEqual(payload["host"], "arr-research.github.io")
        self.assertEqual(payload["urlList"], urls)
        self.assertEqual(payload["keyLocation"], "https://arr-research.github.io/indexnow-key.txt")
        with self.assertRaises(ValueError):
            submit_indexnow.make_payload(
                "https://arr-research.github.io/",
                "0123456789abcdef0123456789abcdef",
                urls + ["https://example.com/foreign"],
            )

    def test_technical_note_requires_scope_and_limitations(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            paper.metadata["record_type"] = "technical_note"
            paper.metadata["technical_note"] = {
                "kind": "formalization",
                "maturity": "complete_in_scope",
                "scope_statement": "This note formalizes one stated lemma and no broader theorem.",
                "limitations": "The correspondence with the surrounding manuscript is not independently reviewed.",
            }
            self.assertEqual(validate_paper(paper), [])
            paper.metadata["technical_note"]["limitations"] = "Too short"
            errors = validate_paper(paper)
            self.assertTrue(any(error.startswith("technical_note.limitations:") for error in errors))

    def test_legacy_schema_is_an_implicit_research_paper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            paper.metadata["schema_version"] = "1.0"
            paper.metadata.pop("record_type")
            self.assertEqual(paper.record_type, "research_paper")
            self.assertEqual(validate_paper(paper), [])

    def test_exact_timestamp_registry_requires_offsets_and_matching_release(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root)
            registry_path = root / "record-timestamps.json"
            entry = {
                "id": paper.id,
                "version": paper.version,
                "deposit_recorded_at": "2026-08-13T10:15:20+02:00",
                "deposit_timestamp_basis": "first_repository_commit",
                "deposit_commit": "a" * 40,
                "publication_state": "published",
                "published_at": "2026-08-13T10:16:05+02:00",
                "publication_timestamp_basis": "github_release",
                "release_tag": f"{paper.id}-{paper.version}",
            }
            registry_path.write_text(json.dumps({"schema_version": "1.0", "records": [entry]}), encoding="utf-8")
            self.assertEqual(validate_record_timestamps([paper], registry_path), [])

            entry["published_at"] = "2026-08-13T10:16:05"
            registry_path.write_text(json.dumps({"schema_version": "1.0", "records": [entry]}), encoding="utf-8")
            errors = validate_record_timestamps([paper], registry_path)
            self.assertTrue(any("explicit UTC offset" in error for error in errors))

            entry = {
                "id": paper.id,
                "version": paper.version,
                "deposit_recorded_at": "2026-08-13T10:15:20+02:00",
                "deposit_timestamp_basis": "first_repository_commit",
                "deposit_commit": "a" * 40,
                "publication_state": "pending",
            }
            registry_path.write_text(json.dumps({"schema_version": "1.0", "records": [entry]}), encoding="utf-8")
            self.assertEqual(validate_record_timestamps([paper], registry_path), [])

    def test_missing_machine_readable_paper_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            (paper.path / "paper.md").unlink()
            errors = validate_paper(paper)
            self.assertTrue(any(error.startswith("paper.md:") for error in errors))

    def test_pdf_origin_requires_matching_hash_size_and_plain_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            (paper.path / "paper.tex").unlink()
            (paper.path / "paper.pdf").write_bytes(b"%PDF-1.4\nARR test\n%%EOF\n")
            (paper.path / "paper.txt").write_text("ARR test", encoding="utf-8")
            paper.metadata["source_of_truth"] = "paper.pdf"
            paper.metadata["integrity"].update(
                {
                    "canonical_sha256": "f5ac9f972d6bf70b08e82dfda026fb656f0cddc47f51d4ad93b9fddded2ed8f6",
                    "canonical_bytes": 24,
                }
            )
            provenance = json.loads((paper.path / "PROVENANCE.json").read_text(encoding="utf-8"))
            provenance["source_of_truth"] = "paper.pdf"
            (paper.path / "PROVENANCE.json").write_text(json.dumps(provenance), encoding="utf-8")
            errors = validate_paper(paper)
            self.assertTrue(any("canonical_sha256" in error for error in errors))

    def test_wrong_shard_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            wrong_path = paper.path.parents[1] / "ZZ" / paper.path.name
            wrong_path.parent.mkdir(parents=True)
            paper.path.rename(wrong_path)
            errors = validate_paper(Paper(wrong_path, paper.metadata))
            self.assertIn("path: shard must be 0J", errors)

    def test_screening_pass_requires_three_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            paper.metadata["screening"].update({"status": "pass", "completed_at": "2026-08-13"})
            errors = validate_paper(paper)
            self.assertTrue(any("three independent evaluators" in error for error in errors))

    def test_duplicate_version_id_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            clone = Paper(paper.path, dict(paper.metadata, version="v2"))
            failures = validate_collection([paper, clone])
            self.assertTrue(any("duplicate version_id" in error for errors in failures.values() for error in errors))

    def test_public_suffix_uses_crockford_alphabet(self) -> None:
        suffix = crockford_prefix(uuid.UUID("123e4567-e89b-42d3-a456-426614174000"))
        self.assertEqual(len(suffix), 16)
        self.assertTrue(set(suffix) <= set(CROCKFORD))

    def test_new_record_generates_a_valid_sharded_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temporary_root = Path(temporary)
            papers_dir = temporary_root / "papers"
            with (
                patch.object(new_record, "ROOT", temporary_root),
                patch.object(new_record, "PAPERS_DIR", papers_dir),
                patch.object(new_record, "TEMPLATE_DIR", ROOT / "templates" / "paper"),
                patch.object(sys, "argv", ["new_record.py", "--date", "2026-08-13", "--author", "Test Author"]),
            ):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(new_record.main(), 0)
            metadata_path = next(papers_dir.glob("**/metadata.json"))
            paper = Paper(metadata_path.parent, json.loads(metadata_path.read_text(encoding="utf-8")))
            self.assertEqual(validate_paper(paper), [])
            self.assertEqual(paper.record_type, "research_paper")

    def test_new_record_generates_a_technical_note_profile(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temporary_root = Path(temporary)
            papers_dir = temporary_root / "papers"
            with (
                patch.object(new_record, "ROOT", temporary_root),
                patch.object(new_record, "PAPERS_DIR", papers_dir),
                patch.object(new_record, "TEMPLATE_DIR", ROOT / "templates" / "paper"),
                patch.object(
                    sys,
                    "argv",
                    ["new_record.py", "--date", "2026-08-13", "--author", "Test Author", "--type", "technical-note"],
                ),
            ):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(new_record.main(), 0)
            metadata_path = next(papers_dir.glob("**/metadata.json"))
            paper = Paper(metadata_path.parent, json.loads(metadata_path.read_text(encoding="utf-8")))
            self.assertEqual(paper.record_type, "technical_note")
            self.assertEqual(validate_paper(paper), [])

    def test_new_version_preserves_identity_and_creates_version_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temporary_root = Path(temporary)
            first = self.make_paper(temporary_root)
            with (
                patch.object(arrlib, "PAPERS_DIR", temporary_root),
                patch.object(new_version, "PAPERS_DIR", temporary_root),
                patch.object(new_version, "ROOT", temporary_root),
                patch.object(
                    sys,
                    "argv",
                    [
                        "new_version.py",
                        first.id,
                        "--date",
                        "2026-08-14",
                        "--change-size",
                        "minor",
                        "--summary",
                        "Corrects notation and expands the replay instructions.",
                    ],
                ),
            ):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(new_version.main(), 0)

            metadata_path = first.path / "versions" / "v2" / "metadata.json"
            second = Paper(metadata_path.parent, json.loads(metadata_path.read_text(encoding="utf-8")))
            self.assertEqual(second.id, first.id)
            self.assertEqual(second.metadata["record_id"], first.metadata["record_id"])
            self.assertNotEqual(second.metadata["version_id"], first.metadata["version_id"])
            self.assertEqual(second.metadata["supersedes_version_id"], first.metadata["version_id"])
            self.assertEqual(second.metadata["revision"]["change_size"], "minor")
            self.assertEqual(second.path, first.path / "versions" / "v2")
            self.assertEqual(validate_collection([first, second]), {})
            self.assertIs(select_paper([first, second], first.id), second)
            self.assertEqual([item.version for item in group_paper_versions([second, first])[first.id]], ["v1", "v2"])
            self.assertFalse(any("versions" in path.relative_to(first.path).parts for path in iter_package_files(first.path)))

    def test_timestamp_registry_may_retain_release_only_older_versions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root)
            paper.metadata["version"] = "v2"
            entries = []
            for number in (1, 2):
                entries.append(
                    {
                        "id": paper.id,
                        "version": f"v{number}",
                        "deposit_recorded_at": f"2026-08-1{number}T10:15:20+02:00",
                        "deposit_timestamp_basis": "first_repository_commit",
                        "deposit_commit": str(number) * 40,
                        "publication_state": "published",
                        "published_at": f"2026-08-1{number}T10:16:05+02:00",
                        "publication_timestamp_basis": "github_release",
                        "release_tag": f"{paper.id}-v{number}",
                    }
                )
            registry_path = root / "record-timestamps.json"
            registry_path.write_text(json.dumps({"schema_version": "1.0", "records": entries}), encoding="utf-8")
            self.assertEqual(validate_record_timestamps([paper], registry_path), [])

    def test_technical_note_uses_its_own_public_route_and_scope_panel(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root)
            paper.metadata["record_type"] = "technical_note"
            paper.metadata["technical_note"] = {
                "kind": "computational",
                "maturity": "preliminary",
                "scope_statement": "This note reports one bounded computational observation and its replay files.",
                "limitations": "The observation has not been generalized beyond the declared parameter range.",
            }
            timestamp = {
                "deposit_recorded_at": "2026-08-13T10:15:20+02:00",
                "publication_state": "pending",
            }
            timestamps = {(paper.id, paper.version): timestamp}
            index = build_site.build_notes_index([paper], timestamps, "", "https://example.test")
            self.assertIn(f'/notes/{paper.id}/', index)
            self.assertIn("Technical note", index)
            with patch.object(build_site, "ROOT", root):
                page = build_site.build_paper_page(
                    paper,
                    timestamp,
                    [],
                    {paper.id: "notes"},
                    [dict(timestamp, id=paper.id, version=paper.version)],
                    {paper.version: paper},
                    paper.version,
                    False,
                    "",
                    "https://example.test",
                    "",
                )
            self.assertIn("Technical-note scope", page)
            self.assertIn("Preliminary", page)
            self.assertIn(f'https://example.test/notes/{paper.id}/', page)

    def test_public_submit_page_links_directly_to_private_receiver(self) -> None:
        page = build_site.build_submit("", "https://arr.example", "https://intake.example")
        self.assertIn('href="https://intake.example/submit"', page)
        self.assertIn("Paper index", page)
        self.assertIn("Submit privately", page)
        self.assertNotIn('class="submit-hero"', page)
        self.assertNotIn("Request an invitation", page)
        self.assertNotIn("mailto:lluiseriksson@gmail.com?subject=ARR%20invitation", page)

    def test_submit_ranking_pages_are_ordered_and_limited_to_fifty(self) -> None:
        papers = []
        metrics = {"views": {"available": False}, "papers": {}}
        for number in range(1, 52):
            paper_id = f"ARR-2026-{number:016X}"
            papers.append(
                SimpleNamespace(
                    id=paper_id,
                    version="v1",
                    record_type="research_paper",
                    metadata={
                        "id": paper_id,
                        "version": "v1",
                        "title": f"Ranked paper {number:02d}",
                        "authors": [{"name": "Test Author"}],
                    },
                )
            )
            metrics["papers"][paper_id] = {
                "pdf_downloads": number,
                "page_views": None,
                "unique_visitors": None,
            }

        first = build_site.build_submit("", "https://arr.example", "", papers, metrics, None, 1)
        second = build_site.build_submit("", "https://arr.example", "", papers, metrics, None, 2)

        self.assertEqual(first.count('class="ranked-paper"'), 50)
        self.assertIn("Ranked paper 51", first)
        self.assertNotIn("Ranked paper 01", first)
        self.assertIn('href="/submit/page/2/"', first)
        self.assertEqual(second.count('class="ranked-paper"'), 1)
        self.assertIn("Ranked paper 01", second)
        self.assertIn('href="/submit/"', second)

    def test_submit_ranking_prefers_page_views_when_available(self) -> None:
        def ranked_paper(suffix: str, title: str):
            paper_id = f"ARR-2026-{suffix}"
            return SimpleNamespace(
                id=paper_id,
                version="v1",
                record_type="research_paper",
                metadata={
                    "id": paper_id,
                    "version": "v1",
                    "title": title,
                    "authors": [{"name": "Test Author"}],
                },
            )

        download_leader = ranked_paper("0000000000000001", "Download leader")
        view_leader = ranked_paper("0000000000000002", "View leader")
        metrics = {
            "views": {"available": True},
            "papers": {
                download_leader.id: {"pdf_downloads": 100, "page_views": 2, "unique_visitors": 2},
                view_leader.id: {"pdf_downloads": 1, "page_views": 50, "unique_visitors": 30},
            },
        }

        page = build_site.build_submit("", "https://arr.example", "", [download_leader, view_leader], metrics)

        self.assertLess(page.index("View leader"), page.index("Download leader"))
        self.assertIn("50</strong><span>page views", page)


class RepositoryContractTests(unittest.TestCase):
    def test_all_json_schemas_parse(self) -> None:
        schemas = list((ROOT / "schema").glob("*.schema.json"))
        self.assertGreaterEqual(len(schemas), 3)
        for path in schemas:
            with self.subTest(path=path.name):
                value = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(value["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_template_contract_files_parse(self) -> None:
        for name in ("metadata.json", "PROVENANCE.json", "LICENSES.json"):
            with self.subTest(path=name):
                json.loads((ROOT / "templates" / "paper" / name).read_text(encoding="utf-8"))

    def test_platform_license_is_agpl(self) -> None:
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("GNU AFFERO GENERAL PUBLIC LICENSE", license_text)
        self.assertIn("Remote Network Interaction", license_text)


if __name__ == "__main__":
    unittest.main()
