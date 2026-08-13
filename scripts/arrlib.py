from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"
ID_PATTERN = re.compile(r"^ARR-(\d{4})-(\d{6})$")
VERSION_PATTERN = re.compile(r"^v[1-9]\d*$")
ALLOWED_STATUSES = {"accepted", "corrected", "withdrawn"}
ALLOWED_SOURCE_FILES = {"paper.tex", "paper.md"}
ALLOWED_CHECKS = {"pass", "partial", "not_applicable"}
ALLOWED_LEAN_LEVELS = {"L0", "L1", "L2", "L3", "not_applicable"}


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


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def discover_papers() -> list[Paper]:
    papers: list[Paper] = []
    for metadata_path in sorted(PAPERS_DIR.glob("**/metadata.json")):
        papers.append(Paper(metadata_path.parent, load_json(metadata_path)))
    return papers


def _required_string(metadata: dict[str, Any], field: str, errors: list[str]) -> None:
    value = metadata.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field}: a non-empty string is required")


def validate_paper(paper: Paper) -> list[str]:
    metadata = paper.metadata
    errors: list[str] = []

    for field in ("id", "version", "title", "abstract", "date", "status", "license", "source_of_truth"):
        _required_string(metadata, field, errors)

    paper_id = metadata.get("id", "")
    id_match = ID_PATTERN.match(paper_id) if isinstance(paper_id, str) else None
    if not id_match:
        errors.append("id: must match ARR-YYYY-NNNNNN")
    else:
        expected_year = id_match.group(1)
        try:
            relative_parts = paper.path.relative_to(PAPERS_DIR).parts
        except ValueError:
            relative_parts = ()
        if relative_parts and relative_parts[0] != expected_year:
            errors.append(f"path: paper year must be {expected_year}")

    version = metadata.get("version")
    if not isinstance(version, str) or not VERSION_PATTERN.match(version):
        errors.append("version: must match v1, v2, ...")

    if metadata.get("status") not in ALLOWED_STATUSES:
        errors.append(f"status: must be one of {sorted(ALLOWED_STATUSES)}")

    title = metadata.get("title")
    if isinstance(title, str) and len(title.strip()) < 10:
        errors.append("title: must contain at least 10 characters")

    abstract = metadata.get("abstract")
    if isinstance(abstract, str) and len(abstract.strip()) < 50:
        errors.append("abstract: must contain at least 50 characters")

    publication_date = metadata.get("date")
    if isinstance(publication_date, str):
        try:
            date.fromisoformat(publication_date)
        except ValueError:
            errors.append("date: must use YYYY-MM-DD")

    authors = metadata.get("authors")
    if not isinstance(authors, list) or not authors:
        errors.append("authors: at least one author is required")
    else:
        for index, author in enumerate(authors):
            if not isinstance(author, dict) or not isinstance(author.get("name"), str) or not author["name"].strip():
                errors.append(f"authors[{index}].name: a non-empty name is required")

    source = metadata.get("source_of_truth")
    if source not in ALLOWED_SOURCE_FILES:
        errors.append(f"source_of_truth: must be one of {sorted(ALLOWED_SOURCE_FILES)}")
    elif not (paper.path / source).is_file():
        errors.append(f"source_of_truth: {source} is missing")

    if not (paper.path / "paper.md").is_file():
        errors.append("paper.md: a machine-readable rendition is required")

    for filename in ("PROVENANCE.json", "CITATION.cff"):
        if not (paper.path / filename).is_file():
            errors.append(f"{filename}: required file is missing")

    if not (paper.path / "LICENSES").is_dir():
        errors.append("LICENSES: required directory is missing")

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
        if screening.get("status") != "pass":
            errors.append("screening.status: must be pass before publication")
        if screening.get("critical_objections_unresolved") != 0:
            errors.append("screening.critical_objections_unresolved: must be zero")
        if screening.get("human_signoff") is not True:
            errors.append("screening.human_signoff: must be true")
        evaluators = screening.get("evaluators")
        if not isinstance(evaluators, list) or len(evaluators) < 3:
            errors.append("screening.evaluators: at least three evaluators are required")
        else:
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
                if evaluator.get("outcome") != "pass":
                    errors.append(f"screening.evaluators[{index}].outcome: must be pass")
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

    folder_name = paper.path.name
    if isinstance(paper_id, str) and folder_name != paper_id:
        errors.append(f"path: directory must be named {paper_id}")

    return errors


def validate_collection(papers: Iterable[Paper]) -> dict[str, list[str]]:
    results: dict[str, list[str]] = {}
    seen: set[tuple[str, str]] = set()
    for paper in papers:
        key = (paper.id, paper.version)
        errors = validate_paper(paper)
        if key in seen:
            errors.append("duplicate id and version")
        seen.add(key)
        if errors:
            results[str(paper.path.relative_to(ROOT))] = errors
    return results


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def iter_package_files(path: Path) -> Iterable[Path]:
    ignored_parts = {".git", ".lake", "__pycache__"}
    generated_suffixes = {".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".pdf", ".toc"}
    for candidate in sorted(path.rglob("*")):
        if (
            candidate.is_file()
            and not ignored_parts.intersection(candidate.relative_to(path).parts)
            and candidate.suffix not in generated_suffixes
        ):
            yield candidate
