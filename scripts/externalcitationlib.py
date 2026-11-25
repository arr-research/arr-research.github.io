# SPDX-License-Identifier: AGPL-3.0-or-later
"""Registry of documents outside AIRR whose reference lists cite an AIRR record.

An entry is added by hand only after the citing document's own reference list
has been read and matched to an exact AIRR record. Nothing here is harvested
from citation indexes, and a citation is never presented as an endorsement.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from arrlib import ROOT

REGISTRY_FILE = ROOT / "registry" / "external-citations.json"
POLICY = "AIRR-EXTERNAL-CITATIONS-1.1"
RELATIONSHIPS = {"independent"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ENTRY_ID = re.compile(r"^[a-z0-9][a-z0-9.\-]*$")
# An external reference record pins the outside document AIRR read. Its EXT- prefix keeps it
# apart from ARR- records, which only exist for work deposited with AIRR by its authors.
REFERENCE_ID = re.compile(r"^EXT-[A-Z0-9][A-Z0-9.\-]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CHECK_OUTCOMES = {"consistent", "discrepancy"}
# AIRR checks how its own record is cited. It does not rate a citing document unless its
# authors ask, and then the document is deposited as an ordinary AIRR record instead.
UNREQUESTED_JUDGEMENTS = {"rating", "score", "grade", "assessment", "review", "verdict"}


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _day(value: object) -> bool:
    return isinstance(value, str) and bool(DATE.match(value))


def _validate_reference_record(item: dict, where: str, seen: set[str]) -> tuple[list[str], set[str]]:
    """Check the pinned source versions; return the errors and the version labels that were pinned."""
    errors: list[str] = []
    record = item.get("reference_record")
    if not isinstance(record, dict):
        return [f"{where}: reference_record is required, so that the exact document checked is on record"], set()
    record_id = record.get("id")
    if not isinstance(record_id, str) or not REFERENCE_ID.match(record_id):
        errors.append(f"{where}: reference_record.id must look like EXT-SOURCE-IDENTIFIER, never ARR-")
    elif record_id in seen:
        errors.append(f"{where}: duplicate reference_record.id {record_id}")
    else:
        seen.add(record_id)
    licence = record.get("licence")
    if not isinstance(licence, dict) or not _text(licence.get("name")) or not _https(licence.get("url")):
        errors.append(f"{where}: reference_record.licence needs the source licence name and its https url")
    versions = record.get("versions")
    if not isinstance(versions, list) or not versions:
        return errors + [f"{where}: reference_record.versions must pin at least one source version"], set()
    pinned: set[str] = set()
    for version in versions:
        if not isinstance(version, dict) or not _text(version.get("version")):
            errors.append(f"{where}: every pinned source version needs a version label")
            continue
        label = version["version"]
        if label in pinned:
            errors.append(f"{where}: source version {label} is pinned twice")
        pinned.add(label)
        for field in ("date", "retrieved_on"):
            if not _day(version.get(field)):
                errors.append(f"{where}: source version {label}: {field} must be YYYY-MM-DD")
        for field in ("url", "pdf_url"):
            if not _https(version.get(field)):
                errors.append(f"{where}: source version {label}: {field} must be an https link")
        if not isinstance(version.get("pdf_sha256"), str) or not SHA256.match(version["pdf_sha256"]):
            errors.append(f"{where}: source version {label}: pdf_sha256 must be 64 lowercase hex digits")
        size = version.get("pdf_bytes")
        if not isinstance(size, int) or isinstance(size, bool) or size <= 0:
            errors.append(f"{where}: source version {label}: pdf_bytes must be a positive integer")
        if not isinstance(version.get("cites_airr"), bool):
            errors.append(f"{where}: source version {label}: cites_airr must say whether this version still cites AIRR")
    if item.get("source_version") not in pinned:
        errors.append(f"{where}: source_version {item.get('source_version')} is not pinned in reference_record.versions")
    return errors, pinned


def _numbered_statements_missing(paper, labels: list) -> list[str]:
    """Labels such as 'Theorem 2.2' that do not occur in the cited version's own text."""
    text_file = paper.path / "paper.txt"
    if not text_file.is_file():
        return []
    text = " ".join(text_file.read_text(encoding="utf-8", errors="replace").split())
    return [label for label in labels if isinstance(label, str) and not re.search(rf"(?<![\w.]){re.escape(label)}(?![\w]|\.\d)", text)]


def load_external_citations(path: Path | None = None) -> dict:
    path = path or REGISTRY_FILE
    if not path.is_file():
        return {"schema_version": 1, "policy": POLICY, "citations": []}
    return json.loads(path.read_text(encoding="utf-8"))


def _name_key(value: str) -> str:
    return re.sub(r"[^a-z]", "", value.lower())


def _https(value: object) -> bool:
    return isinstance(value, str) and value.startswith("https://") and " " not in value


def validate_external_citations(registry: dict, versions: list) -> list[str]:
    """Return every reason the registry may not be published."""
    errors: list[str] = []
    if registry.get("schema_version") != 1 or registry.get("policy") != POLICY:
        errors.append(f"external-citations.json: expected schema_version 1 and policy {POLICY}")
    known = {(paper.id, paper.version): paper for paper in versions}
    seen: set[str] = set()
    seen_references: set[str] = set()
    for index, item in enumerate(registry.get("citations", [])):
        where = f"external-citations.json[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: entry must be an object")
            continue
        entry_id = item.get("id")
        if not isinstance(entry_id, str) or not ENTRY_ID.match(entry_id):
            errors.append(f"{where}: id must be a lowercase slug")
        elif entry_id in seen:
            errors.append(f"{where}: duplicate id {entry_id}")
        else:
            seen.add(entry_id)
        for field in ("identifier", "title", "venue"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{where}: {field} is required")
        for field in ("date", "verified_on"):
            if not isinstance(item.get(field), str) or not DATE.match(item[field]):
                errors.append(f"{where}: {field} must be YYYY-MM-DD")
        if not _https(item.get("url")):
            errors.append(f"{where}: url must be an https link to the citing document")
        for link in item.get("links", []):
            if not isinstance(link, dict) or not link.get("label") or not _https(link.get("url")):
                errors.append(f"{where}: every link needs a label and an https url")
        if item.get("relationship") not in RELATIONSHIPS:
            errors.append(f"{where}: relationship must be one of {sorted(RELATIONSHIPS)}")
        authors = item.get("authors")
        if not isinstance(authors, list) or not authors or not all(isinstance(a, dict) and a.get("name") for a in authors):
            errors.append(f"{where}: authors must be a non-empty list of named authors")
            authors = []
        citing = {_name_key(author["name"]) for author in authors}
        judged = sorted(UNREQUESTED_JUDGEMENTS & set(item))
        if judged:
            errors.append(f"{where}: {', '.join(judged)} is not allowed; AIRR does not assess a citing document its authors did not submit")
        reference_errors, pinned = _validate_reference_record(item, where, seen_references)
        errors.extend(reference_errors)
        for correction in item.get("corrections", []):
            if not isinstance(correction, dict) or not _day(correction.get("date")) or not _text(correction.get("note")):
                errors.append(f"{where}: every correction needs a YYYY-MM-DD date and a note")
        cites = item.get("cites")
        if not isinstance(cites, list) or not cites:
            errors.append(f"{where}: cites must name at least one AIRR record")
            continue
        for cited in cites:
            if not isinstance(cited, dict):
                errors.append(f"{where}: cites entries must be objects")
                continue
            key = (cited.get("paper_id"), cited.get("version"))
            paper = known.get(key)
            if paper is None:
                errors.append(f"{where}: cited record {key[0]} {key[1]} is not a published AIRR version")
                continue
            for field in ("reference", "location", "summary"):
                if not isinstance(cited.get(field), str) or not cited[field].strip():
                    errors.append(f"{where}: cites.{field} is required for {key[0]}")
            if cited["paper_id"] not in str(cited.get("reference", "")):
                errors.append(f"{where}: the reference as printed must contain {cited['paper_id']}")
            results = cited.get("results_cited", [])
            if not isinstance(results, list):
                errors.append(f"{where}: cites.results_cited must be a list")
                results = []
            # A numbered statement credited to a record must exist in that exact version.
            for label in _numbered_statements_missing(paper, results):
                errors.append(f"{where}: {label} is not a numbered statement of {key[0]} {key[1]}; check which AIRR record the citing paper means")
            if "use" in cited and not _text(cited["use"]):
                errors.append(f"{where}: cites.use must be one sentence when present for {key[0]}")
            check = cited.get("check")
            if not isinstance(check, dict):
                errors.append(f"{where}: cites.check is required for {key[0]}: compare the citation with the cited version before listing it")
            else:
                if check.get("outcome") not in CHECK_OUTCOMES:
                    errors.append(f"{where}: cites.check.outcome must be one of {sorted(CHECK_OUTCOMES)} for {key[0]}")
                if not _day(check.get("checked_on")):
                    errors.append(f"{where}: cites.check.checked_on must be YYYY-MM-DD for {key[0]}")
                for field in ("checked_by", "detail"):
                    if not _text(check.get(field)):
                        errors.append(f"{where}: cites.check.{field} is required for {key[0]}")
                if pinned and check.get("source_version") not in pinned:
                    errors.append(f"{where}: cites.check.source_version must be a pinned source version for {key[0]}")
            # An author citing their own record is a self-citation, which this registry does not list.
            own = {_name_key(author["name"]) for author in paper.metadata.get("authors", [])}
            if citing & own:
                errors.append(f"{where}: shares an author with {key[0]}; self-citations are not listed")
    return errors


def citations_by_paper(registry: dict) -> dict[str, list[tuple[dict, dict]]]:
    """Map each cited AIRR identifier to (citing document, citation detail) pairs, newest first."""
    result: dict[str, list[tuple[dict, dict]]] = {}
    for item in sorted(registry.get("citations", []), key=lambda entry: (entry["date"], entry["id"]), reverse=True):
        for cited in item["cites"]:
            result.setdefault(cited["paper_id"], []).append((item, cited))
    return result
