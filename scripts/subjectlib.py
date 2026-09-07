# SPDX-License-Identifier: AGPL-3.0-or-later
"""Shared, offline subject vocabulary for discovery and private intake.

Discovery mappings never rewrite deposited metadata. Only explicit English
labels/AIRR aliases assign existing papers; translations assist human discovery.
"""
from functools import lru_cache
import json
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def normalize_subject(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


@lru_cache(maxsize=1)
def vocabulary() -> dict:
    source = json.loads((ROOT / "registry/euroscivoc.json").read_text(encoding="utf-8"))
    extensions = json.loads((ROOT / "registry/subject-extensions.json").read_text(encoding="utf-8"))
    terms = source["terms"] + extensions["terms"]
    by_id = {t["id"]: t for t in terms}
    if len(by_id) != len(terms):
        raise ValueError("Duplicate subject identifier")
    lookup = {}
    for term in terms:
        term["aliases"] = sorted(set(term["aliases"] + extensions["aliases"].get(term["id"], [])))
        chain = [term["id"]]
        parent = term["parent"]
        while parent:
            if parent not in by_id or parent in chain:
                raise ValueError(f"Broken subject hierarchy for {term['id']}")
            chain.append(parent)
            parent = by_id[parent]["parent"]
        term["ancestors"] = chain[1:]
        term["family"] = chain[-1]
        term["path"] = " › ".join(by_id[i]["label"] for i in reversed(chain))
        term["children"] = []
        # Curated aliases only for archival classification; source alternate
        # labels can be broad keywords and are used for browsing, not inference.
        aliases = extensions["aliases"].get(term["id"], []) if term["id"].startswith("eu-") else term["aliases"]
        for label in [term["label"], *aliases]:
            key = normalize_subject(label)
            lookup.setdefault(key, set()).add(term["id"])
    for term in terms:
        if term["parent"]:
            by_id[term["parent"]]["children"].append(term["id"])
    for term in terms:
        term["children"].sort(key=lambda i: by_id[i]["label"].casefold())
    family_order = ["Natural sciences", "Engineering and technology", "Medical and health sciences",
                    "Agricultural sciences", "Social sciences", "Humanities", "Interdisciplinary & emerging research"]
    roots = sorted((t for t in terms if not t["parent"]), key=lambda t: (family_order.index(t["label"]) if t["label"] in family_order else 99, t["label"]))
    return {"version": extensions["version"], "source_version": source["source_version"],
            "terms": terms, "by_id": by_id, "roots": roots,
            "lookup": {key: next(iter(ids)) for key, ids in lookup.items() if len(ids) == 1}}


def direct_subject_ids(labels: list[str]) -> list[str]:
    lookup = vocabulary()["lookup"]
    return sorted({lookup[normalize_subject(label)] for label in labels if normalize_subject(label) in lookup})


def record_subject_ids(metadata: dict) -> list[str]:
    data = vocabulary()
    direct = direct_subject_ids(metadata.get("subjects", []))
    return sorted({i for ident in direct for i in [ident, *data["by_id"][ident]["ancestors"]]})


def subject_counts(papers: list) -> dict[str, int]:
    members = {t["id"]: set() for t in vocabulary()["terms"]}
    for paper in papers:
        for ident in record_subject_ids(paper.metadata):
            members[ident].add((paper.id, paper.version))
    return {key: len(ids) for key, ids in members.items()}


def public_vocabulary(papers: list | None = None) -> dict:
    data = vocabulary()
    counts = subject_counts(papers or [])
    return {"version": data["version"], "source_version": data["source_version"],
            "source": "EuroSciVoc — Publications Office of the European Union; AIRR additions",
            "license": "CC-BY-4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
            "terms": [{k: t[k] for k in ("id", "label", "parent", "family", "path", "labels", "aliases")} |
                      {"count": counts[t["id"]]} for t in data["terms"]]}


def classification_options() -> list[dict]:
    data = vocabulary()
    return [{"label": root["label"], "terms": sorted(
        (t for t in data["terms"] if t["family"] == root["id"]), key=lambda t: t["path"])} for root in data["roots"]]


def validate_classification(primary: str, secondary: list[str], topic: str) -> dict:
    data = vocabulary()
    if primary not in data["by_id"]:
        raise ValueError("Choose a main subject from the catalogue, or Other or emerging research areas.")
    secondary = [s for s in secondary if s]
    if len(secondary) > 2 or len(set([primary, *secondary])) != 1 + len(secondary) or any(s not in data["by_id"] for s in secondary):
        raise ValueError("Choose up to two different additional subjects from the catalogue.")
    if len(topic) > 200:
        raise ValueError("Keep the specific or emerging topic to 200 characters.")
    if primary == "airr-other-or-emerging-research-areas" and not topic:
        raise ValueError("Describe the emerging research area so an editor can classify it.")
    return {"version": data["version"], "primary": {"id": primary, "label": data["by_id"][primary]["label"]},
            "secondary": [{"id": s, "label": data["by_id"][s]["label"]} for s in secondary], "topic": topic}


def classification_text(value: str) -> str:
    data = json.loads(value or "{}")
    if not data:
        return "Not supplied (earlier submission)"
    result = data["primary"]["label"]
    if data["secondary"]:
        result += " · Additional: " + ", ".join(t["label"] for t in data["secondary"])
    if data["topic"]:
        result += " · Specific topic: " + data["topic"]
    return result
