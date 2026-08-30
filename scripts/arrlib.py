# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import hashlib
import json
import re
import uuid
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"
TIMESTAMP_REGISTRY_PATH = ROOT / "registry" / "record-timestamps.json"
ID_PATTERN = re.compile(r"^ARR-(\d{4})-([0-9A-HJKMNP-TV-Z]{16})$")
UUID_PATTERN = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
RECORD_ID_PATTERN = re.compile(rf"^arr:record:{UUID_PATTERN}$")
VERSION_ID_PATTERN = re.compile(rf"^arr:version:{UUID_PATTERN}$")
VERSION_PATTERN = re.compile(r"^v[1-9]\d*$")
ALLOWED_STATUSES = {"accepted", "corrected", "withdrawn", "archived"}
ALLOWED_RECORD_TYPES = {"research_paper", "technical_note"}
ALLOWED_NOTE_KINDS = {
    "result",
    "proof",
    "formalization",
    "computational",
    "replication",
    "negative_result",
    "method",
    "data",
    "software",
    "protocol",
}
ALLOWED_SOURCE_FILES = {"paper.tex", "paper.md", "paper.pdf", "external_pdf"}
ALLOWED_CHECKS = {"pass", "partial", "not_assessed", "not_applicable"}
ALLOWED_LEAN_LEVELS = {"L0", "L1", "L2", "L3", "not_assessed", "not_applicable"}
CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


@dataclass(frozen=True)
class Paper:
    path: Path
    metadata: dict[str, Any]

    @property
    def id(self) -> str:
        return self.metadata["id"]

    @property
    def version(self) -> str:
        return self.metadata["version"]

    @property
    def record_type(self) -> str:
        # Schema 1.0 predates explicit record types and contains papers only.
        return self.metadata.get("record_type", "research_paper")

    @property
    def version_number(self) -> int:
        match = VERSION_PATTERN.fullmatch(self.version)
        return int(self.version[1:]) if match else 0

    @property
    def record_root(self) -> Path | None:
        for candidate in (self.path, *self.path.parents):
            if candidate.name == self.id:
                return candidate
        return None


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def crockford_prefix(value: uuid.UUID, length: int = 16) -> str:
    number = value.int
    encoded = []
    while number:
        number, remainder = divmod(number, 32)
        encoded.append(CROCKFORD[remainder])
    return "".join(reversed(encoded)).rjust(26, "0")[:length]


def discover_papers() -> list[Paper]:
    papers: list[Paper] = []
    for metadata_path in sorted(PAPERS_DIR.glob("**/metadata.json")):
        papers.append(Paper(metadata_path.parent, load_json(metadata_path)))
    return papers


def select_paper(papers: Iterable[Paper], paper_id: str, version: str | None = None) -> Paper:
    matches = [paper for paper in papers if paper.id == paper_id and (version is None or paper.version == version)]
    if not matches:
        requested = f" {version}" if version else ""
        raise ValueError(f"ARR record {paper_id}{requested} was not found")
    if version is not None and len(matches) != 1:
        raise ValueError(f"ARR record {paper_id} {version} is ambiguous")
    return max(matches, key=lambda paper: paper.version_number)


def group_paper_versions(papers: Iterable[Paper]) -> dict[str, list[Paper]]:
    groups: dict[str, list[Paper]] = {}
    for paper in papers:
        groups.setdefault(paper.id, []).append(paper)
    for versions in groups.values():
        versions.sort(key=lambda paper: paper.version_number)
    return groups


def parse_exact_timestamp(value: object) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include an explicit UTC offset")
    return parsed


def load_record_timestamps(path: Path = TIMESTAMP_REGISTRY_PATH) -> dict[tuple[str, str], dict[str, Any]]:
    registry = load_json(path)
    if registry.get("schema_version") != "1.0" or not isinstance(registry.get("records"), list):
        raise ValueError("timestamp registry must contain schema_version 1.0 and a records array")
    records: dict[tuple[str, str], dict[str, Any]] = {}
    for index, item in enumerate(registry["records"]):
        if not isinstance(item, dict):
            raise ValueError(f"timestamp registry record {index} must be an object")
        key = (item.get("id"), item.get("version"))
        if not all(isinstance(value, str) and value for value in key):
            raise ValueError(f"timestamp registry record {index} requires id and version")
        if key in records:
            raise ValueError(f"duplicate timestamp registry entry for {key[0]} {key[1]}")
        records[key] = item
    return records


def validate_record_timestamps(papers: Iterable[Paper], path: Path = TIMESTAMP_REGISTRY_PATH) -> list[str]:
    papers = list(papers)
    try:
        records = load_record_timestamps(path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [f"registry/record-timestamps.json: {error}"]

    errors: list[str] = []
    expected = {(paper.id, paper.version) for paper in papers}
    actual = set(records)
    for paper_id, version in sorted(expected - actual):
        errors.append(f"timestamp registry: missing {paper_id} {version}")
    maximum_versions: dict[str, int] = {}
    for paper in papers:
        maximum_versions[paper.id] = max(maximum_versions.get(paper.id, 0), paper.version_number)
    for paper_id, version in sorted(actual - expected):
        match = VERSION_PATTERN.fullmatch(version)
        historical_number = int(version[1:]) if match else 0
        if paper_id not in maximum_versions or historical_number < 1 or historical_number >= maximum_versions[paper_id]:
            errors.append(f"timestamp registry: orphaned {paper_id} {version}")

    for key in sorted(actual):
        item = records[key]
        prefix = f"timestamp registry {key[0]} {key[1]}"
        try:
            deposited = parse_exact_timestamp(item.get("deposit_recorded_at"))
        except ValueError as error:
            errors.append(f"{prefix}: {error}")
            deposited = None
        if item.get("deposit_timestamp_basis") != "first_repository_commit":
            errors.append(f"{prefix}: deposit timestamp basis must be first_repository_commit")
        commit = item.get("deposit_commit")
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
            errors.append(f"{prefix}: deposit_commit must be a full Git SHA")
        publication_state = item.get("publication_state")
        if publication_state not in {"pending", "published"}:
            errors.append(f"{prefix}: publication_state must be pending or published")
        elif publication_state == "published":
            try:
                published = parse_exact_timestamp(item.get("published_at"))
                if deposited is not None and published < deposited:
                    errors.append(f"{prefix}: published_at precedes deposit_recorded_at")
            except ValueError as error:
                errors.append(f"{prefix}: {error}")
            if item.get("publication_timestamp_basis") != "github_release":
                errors.append(f"{prefix}: publication timestamp basis must be github_release")
            if item.get("release_tag") != f"{key[0]}-{key[1]}":
                errors.append(f"{prefix}: release_tag does not match the record and version")
        elif any(field in item for field in ("published_at", "publication_timestamp_basis", "release_tag")):
            errors.append(f"{prefix}: pending records cannot claim release publication fields")
    return errors


def _required_string(metadata: dict[str, Any], field: str, errors: list[str]) -> None:
    value = metadata.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field}: a non-empty string is required")


def validate_paper(paper: Paper) -> list[str]:
    metadata = paper.metadata
    errors: list[str] = []

    for field in (
        "schema_version",
        "record_id",
        "version_id",
        "id",
        "version",
        "title",
        "abstract",
        "date",
        "status",
        "source_of_truth",
    ):
        _required_string(metadata, field, errors)

    schema_version = metadata.get("schema_version")
    if schema_version not in {"1.0", "1.1", "1.2", "1.3"}:
        errors.append("schema_version: must be 1.0, 1.1, 1.2 or 1.3")

    explicit_record_type = metadata.get("record_type")
    record_type = explicit_record_type or "research_paper"
    if schema_version == "1.0" and explicit_record_type is not None:
        errors.append("record_type: schema 1.0 records must use the legacy implicit research_paper type")
    if schema_version in {"1.1", "1.2", "1.3"} and explicit_record_type not in ALLOWED_RECORD_TYPES:
        errors.append(f"record_type: must be one of {sorted(ALLOWED_RECORD_TYPES)}")
    if record_type not in ALLOWED_RECORD_TYPES:
        errors.append(f"record_type: must be one of {sorted(ALLOWED_RECORD_TYPES)}")

    note_profile = metadata.get("technical_note")
    if record_type == "technical_note":
        if schema_version not in {"1.1", "1.2"}:
            errors.append("technical_note: technical notes require schema_version 1.1 or 1.2")
        if not isinstance(note_profile, dict):
            errors.append("technical_note: an object is required for technical notes")
        else:
            if note_profile.get("kind") not in ALLOWED_NOTE_KINDS:
                errors.append(f"technical_note.kind: must be one of {sorted(ALLOWED_NOTE_KINDS)}")
            if note_profile.get("maturity") not in {"preliminary", "complete_in_scope"}:
                errors.append("technical_note.maturity: must be preliminary or complete_in_scope")
            for field in ("scope_statement", "limitations"):
                value = note_profile.get(field)
                if not isinstance(value, str) or len(value.strip()) < 30:
                    errors.append(f"technical_note.{field}: at least 30 characters are required")
    elif note_profile is not None:
        errors.append("technical_note: only technical_note records may declare this object")

    record_id = metadata.get("record_id")
    if not isinstance(record_id, str) or not RECORD_ID_PATTERN.match(record_id):
        errors.append("record_id: must be arr:record:<UUIDv4>")

    version_id = metadata.get("version_id")
    if not isinstance(version_id, str) or not VERSION_ID_PATTERN.match(version_id):
        errors.append("version_id: must be arr:version:<UUIDv4>")

    paper_id = metadata.get("id", "")
    id_match = ID_PATTERN.match(paper_id) if isinstance(paper_id, str) else None
    if not id_match:
        errors.append("id: must match ARR-YYYY-<16 Crockford Base32 characters>")
    else:
        expected_year = id_match.group(1)
        expected_shard = id_match.group(2)[:2]
        if isinstance(record_id, str) and RECORD_ID_PATTERN.match(record_id):
            expected_suffix = crockford_prefix(uuid.UUID(record_id.removeprefix("arr:record:")))
            if id_match.group(2) != expected_suffix:
                errors.append("id: suffix must be derived from record_id")
        record_root = paper.record_root
        if record_root is None:
            errors.append(f"path: no ancestor directory is named {paper_id}")
        elif len(record_root.parts) >= 4:
            actual_year, actual_month, actual_shard, actual_id = record_root.parts[-4:]
            if actual_year != expected_year:
                errors.append(f"path: paper year must be {expected_year}")
            if not re.match(r"^(0[1-9]|1[0-2])$", actual_month):
                errors.append("path: paper month must be 01 through 12")
            if actual_shard != expected_shard:
                errors.append(f"path: shard must be {expected_shard}")
            if actual_id != paper_id:
                errors.append(f"path: record directory must be named {paper_id}")

    version = metadata.get("version")
    if not isinstance(version, str) or not VERSION_PATTERN.match(version):
        errors.append("version: must match v1, v2, ...")
    elif paper.record_root is not None and paper.path != paper.record_root:
        expected_version_path = paper.record_root / "versions" / version
        if paper.path != expected_version_path:
            errors.append(f"path: version {version} must be stored at versions/{version}")

    revision = metadata.get("revision")
    if schema_version == "1.2" and isinstance(version, str) and VERSION_PATTERN.match(version) and int(version[1:]) > 1:
        if not isinstance(metadata.get("supersedes_version_id"), str):
            errors.append("supersedes_version_id: required for version 2 and later")
        if not isinstance(revision, dict):
            errors.append("revision: an object is required for version 2 and later")
        else:
            if revision.get("change_size") not in {"minor", "major"}:
                errors.append("revision.change_size: must be minor or major")
            summary = revision.get("summary")
            if not isinstance(summary, str) or len(summary.strip()) < 20:
                errors.append("revision.summary: at least 20 characters are required")
    elif revision is not None and not isinstance(revision, dict):
        errors.append("revision: must be an object")

    if metadata.get("status") not in ALLOWED_STATUSES:
        errors.append(f"status: must be one of {sorted(ALLOWED_STATUSES)}")
    if metadata.get("status") == "corrected" and not metadata.get("supersedes_version_id"):
        errors.append("supersedes_version_id: required for a corrected version")

    archival = metadata.get("archival_source")
    if metadata.get("status") == "archived":
        if schema_version != "1.3":
            errors.append("status: archived records require schema_version 1.3")
        if not isinstance(archival, dict):
            errors.append("archival_source: required for archived records")
        else:
            identifier = archival.get("identifier")
            if archival.get("archive") != "ai.vixra":
                errors.append("archival_source.archive: must be ai.vixra")
            if not isinstance(identifier, str) or not re.fullmatch(r"\d{4}\.\d{4}", identifier):
                errors.append("archival_source.identifier: invalid ai.vixra identifier")
            for field in ("abstract_url", "mirror_pdf_url", "mirror_release_url"):
                value = archival.get(field)
                if not isinstance(value, str) or not value.startswith("https://"):
                    errors.append(f"archival_source.{field}: an HTTPS URL is required")
            versions = archival.get("versions")
            if not isinstance(versions, list) or not versions:
                errors.append("archival_source.versions: a non-empty history is required")
            else:
                version_numbers: list[int] = []
                for index, source_version in enumerate(versions):
                    if not isinstance(source_version, dict):
                        errors.append(f"archival_source.versions[{index}]: an object is required")
                        continue
                    label = source_version.get("version")
                    match = VERSION_PATTERN.fullmatch(label) if isinstance(label, str) else None
                    if not match:
                        errors.append(f"archival_source.versions[{index}].version: invalid value")
                    else:
                        version_numbers.append(int(label[1:]))
                    try:
                        parse_exact_timestamp(source_version.get("submitted_at"))
                    except ValueError as error:
                        errors.append(f"archival_source.versions[{index}].submitted_at: {error}")
                    pdf_url = source_version.get("pdf_url")
                    if not isinstance(pdf_url, str) or not pdf_url.startswith("https://"):
                        errors.append(f"archival_source.versions[{index}].pdf_url: an HTTPS URL is required")
                if version_numbers != sorted(set(version_numbers)):
                    errors.append("archival_source.versions: versions must be unique and ascending")
                if versions[0].get("submitted_at") != archival.get("first_submitted_at"):
                    errors.append("archival_source.first_submitted_at: must equal the first version timestamp")
                if versions[-1].get("version") != archival.get("latest_declared_version"):
                    errors.append("archival_source.latest_declared_version: must equal the final declared version")
                if versions[-1].get("submitted_at") != archival.get("latest_submitted_at"):
                    errors.append("archival_source.latest_submitted_at: must equal the final version timestamp")
            for field in ("first_submitted_at", "latest_submitted_at"):
                try:
                    parse_exact_timestamp(archival.get(field))
                except ValueError as error:
                    errors.append(f"archival_source.{field}: {error}")
            if not isinstance(archival.get("source_file_available"), bool):
                errors.append("archival_source.source_file_available: a boolean is required")
    elif archival is not None:
        errors.append("archival_source: only archived records may declare an archival source")

    title = metadata.get("title")
    if isinstance(title, str) and len(title.strip()) < 10:
        errors.append("title: must contain at least 10 characters")

    abstract = metadata.get("abstract")
    if isinstance(abstract, str) and len(abstract.strip()) < 50:
        errors.append("abstract: must contain at least 50 characters")

    publication_date = metadata.get("date")
    if isinstance(publication_date, str):
        try:
            parsed_date = date.fromisoformat(publication_date)
            if id_match and str(parsed_date.year) != id_match.group(1):
                errors.append("date: year must match public id")
            if id_match and paper.record_root is not None and paper.record_root.parts[-3] != f"{parsed_date.month:02d}":
                errors.append("path: month must match publication date")
        except ValueError:
            errors.append("date: must use YYYY-MM-DD")

    authors = metadata.get("authors")
    if not isinstance(authors, list) or not authors:
        errors.append("authors: at least one author is required")
    else:
        for index, author in enumerate(authors):
            if not isinstance(author, dict) or not isinstance(author.get("name"), str) or not author["name"].strip():
                errors.append(f"authors[{index}].name: a non-empty name is required")

    related_records = metadata.get("related_records", [])
    if not isinstance(related_records, list):
        errors.append("related_records: an array is required")
    else:
        related_ids: set[str] = set()
        for index, relation in enumerate(related_records):
            if not isinstance(relation, dict):
                errors.append(f"related_records[{index}]: an object is required")
                continue
            related_id = relation.get("id")
            if not isinstance(related_id, str) or not ID_PATTERN.match(related_id):
                errors.append(f"related_records[{index}].id: invalid ARR identifier")
            elif related_id == paper_id:
                errors.append(f"related_records[{index}].id: a record cannot relate to itself")
            elif related_id in related_ids:
                errors.append(f"related_records[{index}].id: duplicate related record")
            else:
                related_ids.add(related_id)
            if relation.get("relationship") not in {"related_work", "supplement", "companion", "is_part_of", "extends", "is_extended_by"}:
                errors.append(f"related_records[{index}].relationship: invalid value")
            if not isinstance(relation.get("note"), str) or len(relation["note"].strip()) < 10:
                errors.append(f"related_records[{index}].note: a meaningful note is required")

    source = metadata.get("source_of_truth")
    if source not in ALLOWED_SOURCE_FILES:
        errors.append(f"source_of_truth: must be one of {sorted(ALLOWED_SOURCE_FILES)}")
    elif source != "external_pdf" and not (paper.path / source).is_file():
        errors.append(f"source_of_truth: {source} is missing")

    if not (paper.path / "paper.md").is_file():
        errors.append("paper.md: a machine-readable rendition is required")
    if source in {"paper.pdf", "external_pdf"} and not (paper.path / "paper.txt").is_file():
        errors.append("paper.txt: a plain-text rendition is required for PDF-origin records")

    for filename in ("PROVENANCE.json", "CITATION.cff", "LICENSES.json"):
        if not (paper.path / filename).is_file():
            errors.append(f"{filename}: required file is missing")

    if not (paper.path / "LICENSES").is_dir():
        errors.append("LICENSES: required directory is missing")

    licenses = metadata.get("licenses")
    if not isinstance(licenses, dict):
        errors.append("licenses: an object is required")
    else:
        if not isinstance(licenses.get("manuscript"), str) or not licenses["manuscript"].strip():
            errors.append("licenses.manuscript: an SPDX identifier is required")
        if licenses.get("metadata") != "CC0-1.0":
            errors.append("licenses.metadata: ARR catalogue metadata must be CC0-1.0")
        for category in ("code", "data"):
            entries = licenses.get(category)
            if not isinstance(entries, list):
                errors.append(f"licenses.{category}: an array is required")
            else:
                for index, entry in enumerate(entries):
                    if not isinstance(entry, dict):
                        errors.append(f"licenses.{category}[{index}]: an object is required")
                        continue
                    if not isinstance(entry.get("path"), str) or not entry["path"].strip():
                        errors.append(f"licenses.{category}[{index}].path: required")
                    if not isinstance(entry.get("spdx"), str) or not entry["spdx"].strip():
                        errors.append(f"licenses.{category}[{index}].spdx: required")

    licenses_path = paper.path / "LICENSES.json"
    if licenses_path.is_file():
        try:
            license_record = load_json(licenses_path)
            if isinstance(licenses, dict):
                for category in ("manuscript", "metadata"):
                    declared = license_record.get(category)
                    if not isinstance(declared, dict) or declared.get("spdx") != licenses.get(category):
                        errors.append(f"LICENSES.json: {category} must match metadata.json")
                for category in ("code", "data"):
                    metadata_pairs = {
                        (item.get("path"), item.get("spdx"))
                        for item in licenses.get(category, [])
                        if isinstance(item, dict)
                    }
                    record_pairs = {
                        (item.get("path"), item.get("spdx"))
                        for item in license_record.get(category, [])
                        if isinstance(item, dict)
                    }
                    if metadata_pairs != record_pairs:
                        errors.append(f"LICENSES.json: {category} entries must match metadata.json")
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"LICENSES.json: invalid JSON ({error})")

    code_suffixes = {".lean", ".py", ".r", ".jl", ".js", ".ts", ".rs", ".c", ".cc", ".cpp", ".h"}
    code_files = [path for path in (paper.path / "src").glob("**/*") if path.is_file() and path.suffix.lower() in code_suffixes]
    if code_files and isinstance(licenses, dict) and not licenses.get("code"):
        errors.append("licenses.code: code files exist but no scoped code license is declared")

    data_dir = paper.path / "data"
    data_files = [path for path in data_dir.glob("**/*") if path.is_file()] if data_dir.is_dir() else []
    if data_files and isinstance(licenses, dict) and not licenses.get("data"):
        errors.append("licenses.data: data files exist but no scoped data license is declared")

    provenance_path = paper.path / "PROVENANCE.json"
    if provenance_path.is_file():
        try:
            provenance = load_json(provenance_path)
            for field in ("record_id", "version_id", "source_of_truth"):
                if provenance.get(field) != metadata.get(field):
                    errors.append(f"PROVENANCE.json: {field} must match metadata.json")
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"PROVENANCE.json: invalid JSON ({error})")

    deposit = metadata.get("deposit")
    if not isinstance(deposit, dict):
        errors.append("deposit: an object is required")
    else:
        if deposit.get("relationship") not in {"author", "rights_holder", "authorized_agent"}:
            errors.append("deposit.relationship: invalid value")
        if deposit.get("deposit_authorized") is not True:
            errors.append("deposit.deposit_authorized: must be true")
        if not isinstance(deposit.get("third_party_material_disclosed"), bool):
            errors.append("deposit.third_party_material_disclosed: a boolean is required")
        if not isinstance(deposit.get("terms_version"), str) or not deposit["terms_version"].strip():
            errors.append("deposit.terms_version: required")

    integrity = metadata.get("integrity")
    if not isinstance(integrity, dict):
        errors.append("integrity: an object is required")
    else:
        if integrity.get("algorithm") != "sha256":
            errors.append("integrity.algorithm: must be sha256")
        if integrity.get("manifest") != "MANIFEST.sha256":
            errors.append("integrity.manifest: must be MANIFEST.sha256")
        if source == "paper.pdf" or metadata.get("status") == "archived":
            canonical_path = paper.path / "paper.pdf"
            canonical_hash = integrity.get("canonical_sha256")
            canonical_bytes = integrity.get("canonical_bytes")
            if not isinstance(canonical_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", canonical_hash):
                errors.append("integrity.canonical_sha256: required for PDF-origin records")
            elif source == "paper.pdf" and canonical_path.is_file() and sha256(canonical_path) != canonical_hash:
                errors.append("integrity.canonical_sha256: does not match paper.pdf")
            if not isinstance(canonical_bytes, int) or isinstance(canonical_bytes, bool) or canonical_bytes < 1:
                errors.append("integrity.canonical_bytes: required for PDF-origin records")
            elif source == "paper.pdf" and canonical_path.is_file() and canonical_path.stat().st_size != canonical_bytes:
                errors.append("integrity.canonical_bytes: does not match paper.pdf")

    ai = metadata.get("ai_assistance")
    if not isinstance(ai, dict):
        errors.append("ai_assistance: an object is required")
    else:
        if not isinstance(ai.get("used"), bool):
            errors.append("ai_assistance.used: a boolean is required")
        if not isinstance(ai.get("statement"), str) or len(ai["statement"].strip()) < 10:
            errors.append("ai_assistance.statement: a meaningful statement is required")

    screening = metadata.get("screening")
    if not isinstance(screening, dict):
        errors.append("screening: an object is required")
    else:
        screening_status = screening.get("status")
        if screening_status not in {"not_assessed", "pass", "fail"}:
            errors.append("screening.status: invalid value")
        unresolved = screening.get("critical_objections_unresolved")
        if not isinstance(unresolved, int) or isinstance(unresolved, bool) or unresolved < 0:
            errors.append("screening.critical_objections_unresolved: must be a non-negative integer")
        if screening.get("human_signoff") is not True:
            errors.append("screening.human_signoff: must be true")
        evaluators = screening.get("evaluators")
        if not isinstance(evaluators, list):
            errors.append("screening.evaluators: an array is required")
        else:
            if screening_status == "not_assessed" and evaluators:
                errors.append("screening.evaluators: must be empty when status is not_assessed")
            if screening_status == "pass":
                if not evaluators:
                    errors.append("screening.evaluators: a declared evaluator report is required for pass")
                if screening.get("critical_objections_unresolved") != 0:
                    errors.append("screening.critical_objections_unresolved: must be zero for pass")
                completed_at = screening.get("completed_at")
                if not isinstance(completed_at, str):
                    errors.append("screening.completed_at: required for pass")
                else:
                    try:
                        date.fromisoformat(completed_at)
                    except ValueError:
                        errors.append("screening.completed_at: must use YYYY-MM-DD")
            model_ids: set[str] = set()
            for index, evaluator in enumerate(evaluators):
                if not isinstance(evaluator, dict):
                    errors.append(f"screening.evaluators[{index}]: an object is required")
                    continue
                model_id = evaluator.get("model_id")
                if not isinstance(model_id, str) or not model_id.strip():
                    errors.append(f"screening.evaluators[{index}].model_id: required")
                elif model_id in model_ids:
                    errors.append(f"screening.evaluators[{index}].model_id: duplicate model")
                else:
                    model_ids.add(model_id)
                if evaluator.get("outcome") not in {"pass", "concerns", "fail"}:
                    errors.append(f"screening.evaluators[{index}].outcome: invalid value")
                if screening_status == "pass" and evaluator.get("outcome") != "pass":
                    errors.append(f"screening.evaluators[{index}].outcome: must be pass for screening pass")
                report = evaluator.get("report")
                if not isinstance(report, str) or not (paper.path / report).is_file():
                    errors.append(f"screening.evaluators[{index}].report: referenced report is missing")

    verification = metadata.get("verification")
    if not isinstance(verification, dict):
        errors.append("verification: an object is required")
    else:
        if not isinstance(verification.get("protocol"), str) or not verification["protocol"].strip():
            errors.append("verification.protocol: a protocol identifier is required")
        if verification.get("source_integrity") != "pass":
            errors.append("verification.source_integrity: must be pass before publication")
        for field in ("bibliography", "reproducibility"):
            if verification.get(field) not in ALLOWED_CHECKS:
                errors.append(f"verification.{field}: invalid value")
        if verification.get("lean4") not in ALLOWED_LEAN_LEVELS:
            errors.append("verification.lean4: invalid level")

    editorial = metadata.get("editorial")
    if not isinstance(editorial, dict):
        errors.append("editorial: an object is required")
    else:
        if editorial.get("decision") not in {"founder_pilot", "standard_acceptance", "correction", "withdrawal", "historical_import"}:
            errors.append("editorial.decision: invalid value")
        if not isinstance(editorial.get("signed_by"), str) or not editorial["signed_by"].strip():
            errors.append("editorial.signed_by: required")
        if not isinstance(editorial.get("conflicts"), list):
            errors.append("editorial.conflicts: an array is required")
        if not isinstance(editorial.get("statement"), str) or len(editorial["statement"].strip()) < 20:
            errors.append("editorial.statement: a meaningful statement is required")
        if metadata.get("status") == "archived" and editorial.get("decision") != "historical_import":
            errors.append("editorial.decision: archived records require historical_import")

    if metadata.get("status") == "archived" and isinstance(screening, dict) and screening.get("status") != "not_assessed":
        errors.append("screening.status: historical imports must remain not_assessed until a new ARR version is audited")

    return errors


def validate_collection(papers: Iterable[Paper]) -> dict[str, list[str]]:
    papers = list(papers)
    results: dict[str, list[str]] = {}
    seen_versions: set[tuple[str, str]] = set()
    seen_version_ids: set[str] = set()
    public_to_record: dict[str, str] = {}
    public_ids = {paper.id for paper in papers}
    for paper in papers:
        record_id = paper.metadata.get("record_id", "")
        version_id = paper.metadata.get("version_id", "")
        key = (record_id, paper.version)
        errors = validate_paper(paper)
        if key in seen_versions:
            errors.append("duplicate record_id and version")
        seen_versions.add(key)
        if version_id in seen_version_ids:
            errors.append("duplicate version_id")
        seen_version_ids.add(version_id)
        previous_record = public_to_record.setdefault(paper.id, record_id)
        if previous_record != record_id:
            errors.append("id: public identifier is assigned to multiple record_id values")
        for relation in paper.metadata.get("related_records", []):
            if isinstance(relation, dict) and relation.get("id") not in public_ids:
                errors.append(f"related_records: unknown target {relation.get('id')}")
        if errors:
            try:
                display_path = paper.path.relative_to(ROOT)
            except ValueError:
                display_path = paper.path
            results[str(display_path)] = errors

    for paper_id, versions in group_paper_versions(papers).items():
        record_ids = {paper.metadata.get("record_id") for paper in versions}
        record_types = {paper.record_type for paper in versions}
        if len(record_ids) > 1 or len(record_types) > 1:
            target = versions[-1]
            key = str(target.path.relative_to(ROOT)) if target.path.is_relative_to(ROOT) else str(target.path)
            if len(record_ids) > 1:
                results.setdefault(key, []).append("versions: all versions must share one record_id")
            if len(record_types) > 1:
                results.setdefault(key, []).append("versions: record_type cannot change between versions")
        numbers = [paper.version_number for paper in versions]
        if numbers and numbers != list(range(numbers[0], numbers[-1] + 1)):
            target = versions[-1]
            key = str(target.path.relative_to(ROOT)) if target.path.is_relative_to(ROOT) else str(target.path)
            results.setdefault(key, []).append(f"versions: source versions for {paper_id} must be consecutive")
        for previous, current in zip(versions, versions[1:]):
            expected_previous = previous.metadata.get("version_id")
            if current.metadata.get("supersedes_version_id") != expected_previous:
                key = str(current.path.relative_to(ROOT)) if current.path.is_relative_to(ROOT) else str(current.path)
                results.setdefault(key, []).append(
                    f"supersedes_version_id: {current.version} must reference {previous.version}"
                )
    return results


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def iter_package_files(path: Path) -> Iterable[Path]:
    # A root-held legacy version may contain later snapshots beneath versions/;
    # those must never leak into the immutable package for the selected version.
    ignored_parts = {".git", ".lake", "__pycache__", "versions"}
    generated_suffixes = {".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".pdf", ".toc"}
    for candidate in sorted(path.rglob("*")):
        if (
            candidate.is_file()
            and not ignored_parts.intersection(candidate.relative_to(path).parts)
            and candidate.suffix not in generated_suffixes
        ):
            yield candidate
