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
POLICY = "AIRR-EXTERNAL-CITATIONS-1.0"
RELATIONSHIPS = {"independent"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ENTRY_ID = re.compile(r"^[a-z0-9][a-z0-9.\-]*$")


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
            if not isinstance(cited.get("results_cited", []), list):
                errors.append(f"{where}: cites.results_cited must be a list")
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
