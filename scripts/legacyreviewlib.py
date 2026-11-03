# SPDX-License-Identifier: AGPL-3.0-or-later
"""Preserve historical reports without inventing modern assessment responses."""
from __future__ import annotations

import hashlib
import json
import math
from datetime import date
from pathlib import Path

from arrlib import ROOT, parse_exact_timestamp
from assessmentlib import assessment_artifact_sha256

PRESERVED_REVIEWS_PATH = ROOT / "registry" / "preserved-model-reviews.json"


def load_preserved_reviews() -> dict:
    return json.loads(PRESERVED_REVIEWS_PATH.read_text(encoding="utf-8"))


def read_preserved_review(record: dict, paper) -> dict:
    """Validate exact version, all original bytes and the sealed receipt binding."""
    required = {"record_id", "paper_id", "version_id", "canonical_sha256", "recorded_at", "sources"}
    if not isinstance(record, dict) or set(record) != required:
        raise ValueError("invalid preserved-review fields")
    if not isinstance(record["record_id"], str) or not record["record_id"].startswith("arr:preserved-review:"):
        raise ValueError("invalid preserved-review identifier")
    if (record["paper_id"] != paper.id or record["version_id"] != paper.metadata["version_id"]
            or record["canonical_sha256"] != assessment_artifact_sha256(paper)):
        raise ValueError("preserved review must match the exact version and PDF")
    parse_exact_timestamp(record["recorded_at"])
    sources = record["sources"]
    if not isinstance(sources, dict) or set(sources) != {"verdict", "report", "receipt"}:
        raise ValueError("verdict, full report and sealed receipt are required")
    payload = {}
    for role, source in sources.items():
        if not isinstance(source, dict) or set(source) != {"path", "sha256"}:
            raise ValueError("invalid preserved source binding")
        relative = Path(source["path"])
        resolved = (ROOT / relative).resolve()
        if (relative.is_absolute() or ".." in relative.parts
                or not resolved.is_relative_to((paper.path / "review").resolve())):
            raise ValueError("preserved source must belong to this version's review directory")
        raw = resolved.read_bytes()
        if hashlib.sha256(raw).hexdigest() != source["sha256"]:
            raise ValueError("preserved source bytes do not match their digest")
        payload[role] = raw
    native = json.loads(payload["verdict"])
    receipt = json.loads(payload["receipt"])
    if not isinstance(native, dict) or not isinstance(receipt, dict) or not payload["report"].strip():
        raise ValueError("native verdict, sealed receipt and full report are required")
    if native.get("kind") != "private_full_exact_version_scientific_review":
        raise ValueError("unsupported historical verdict format")
    if (native["artifact"]["pdf_sha256"] != record["canonical_sha256"]
            or receipt["pdf_sha256"] != record["canonical_sha256"]
            or receipt["review_id"] != native["review_id"]
            or receipt["status"] != "SEALED"
            or receipt["verdict_sha256"] != sources["verdict"]["sha256"]
            or receipt["report_sha256"] != sources["report"]["sha256"]):
        raise ValueError("sealed receipt does not bind the original report, verdict and exact PDF")
    date.fromisoformat(native["date"])  # Preserve day precision; never invent a review time.
    for field in ("importance_airr", "technical_quality"):
        score = native[field]["score"]
        if (isinstance(score, bool) or not isinstance(score, (int, float))
                or not math.isfinite(score) or not 0 <= score <= 10
                or native[field]["scale"] != "0..10"):
            raise ValueError("invalid native score or scale")
        if not isinstance(native[field].get("basis"), str):
            raise ValueError("native score basis must be retained")
    if native["importance_airr"]["rubric_url"] != "https://airr.science/assessments/#scale":
        raise ValueError("native importance scale is not explicitly identified")
    if not isinstance(native.get("provenance"), dict) or not isinstance(native.get("scope_limits"), list):
        raise ValueError("native provenance and scope limits must be retained")
    if native.get("recommendation") not in {"accept", "minor_revision", "major_revision", "reject"}:
        raise ValueError("invalid native model recommendation")
    for field in ("scope_limits", "material_objections", "required_corrections"):
        if not isinstance(native.get(field), list) or any(not isinstance(x, str) for x in native[field]):
            raise ValueError("native scope, objections and corrections must be retained")
    if (not isinstance(native.get("optional_comments"), list)
            or any(not isinstance(c, dict) or any(not isinstance(c.get(k), str) for k in ("id", "location", "comment"))
                   for c in native["optional_comments"])):
        raise ValueError("invalid native comments")
    return native


def validate_preserved_reviews(registry: object, papers) -> list[str]:
    if (not isinstance(registry, dict) or set(registry) != {"schema_version", "license", "mode", "reviews"}
            or registry.get("schema_version") != "1.0" or registry.get("license") != "CC-BY-4.0"
            or registry.get("mode") != "historical_evidence_only" or not isinstance(registry.get("reviews"), list)):
        return ["preserved model reviews: invalid historical-evidence registry"]
    papers = list(papers)
    errors, seen_ids, seen_sources = [], set(), set()
    for index, record in enumerate(registry["reviews"]):
        try:
            paper = next(p for p in papers if p.id == record["paper_id"] and p.metadata["version_id"] == record["version_id"])
            read_preserved_review(record, paper)
            digest = record["sources"]["verdict"]["sha256"]
            if record["record_id"] in seen_ids or digest in seen_sources:
                raise ValueError("duplicate preserved report")
            seen_ids.add(record["record_id"])
            seen_sources.add(digest)
        except (OSError, ValueError, KeyError, TypeError, StopIteration) as error:
            errors.append(f"preserved model reviews[{index}]: {error}")
    return errors
