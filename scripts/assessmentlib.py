# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import hashlib
import json
import re
import uuid
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from statistics import median
from typing import Any, Iterable

from arrlib import Paper, parse_exact_timestamp, select_paper


ROOT = Path(__file__).resolve().parents[1]
ASSESSMENTS_PATH = ROOT / "registry" / "model-assessments.json"
HIGHLIGHTS_PATH = ROOT / "registry" / "editorial-highlights.json"
PROMPT_VERSION = "ARR-ASSESS-1.0"
CRITERIA = ("correctness_confidence", "rigor", "novelty", "significance", "reproducibility")
RECOMMENDATIONS = {"accept", "minor_revision", "major_revision", "reject"}
INDEPENDENCE = {"not_involved_in_manuscript", "involved_in_manuscript", "unknown"}
ASSESSMENT_ID = re.compile(r"^arr:assessment:[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def source_hash(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def load_assessment_registry(path: Path = ASSESSMENTS_PATH) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != "1.0" or value.get("protocol") != PROMPT_VERSION or value.get("license") != "CC-BY-4.0" or not isinstance(value.get("assessments"), list):
        raise ValueError(f"{path}: invalid assessment registry envelope")
    return value


def load_highlight_registry(path: Path = HIGHLIGHTS_PATH) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != "1.0" or value.get("license") != "CC-BY-4.0" or not isinstance(value.get("highlights"), list):
        raise ValueError(f"{path}: invalid editorial-highlight registry envelope")
    return value


def expected_stars(score: float) -> int:
    return max(1, min(10, int(Decimal(str(score)) + Decimal("0.5"))))


def tier_label(stars: int) -> str:
    return {
        1: "Critical concerns",
        2: "Substantial revision needed",
        3: "Acceptable",
        4: "Strong",
        5: "Very good",
        6: "Excellent",
        7: "Exceptional",
        8: "Potentially field-shaping",
        9: "Potentially historic",
        10: "Millennium-resolution benchmark",
    }[stars]


def _text_list(value: object, field: str, errors: list[str]) -> None:
    if not isinstance(value, list) or len(value) > 12:
        errors.append(f"{field}: must be an array of at most 12 findings")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not 8 <= len(item.strip()) <= 800:
            errors.append(f"{field}[{index}]: must contain 8..800 characters")


def validate_assessment(value: object, papers: Iterable[Paper]) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, dict):
        return ["assessment: expected one JSON object"]
    required = {
        "assessment_id", "paper_id", "version", "version_id", "canonical_sha256", "provider", "model_id",
        "assessed_at", "prompt_version", "independence", "recommendation", "millennium_score", "overall_stars",
        "criteria", "summary", "strengths", "weaknesses", "potential_errors", "strong_novelty_candidates",
        "unresolved_material_objections", "source_response_sha256",
    }
    unknown = set(value) - required
    missing = required - set(value)
    if unknown:
        errors.append(f"assessment: unknown fields: {', '.join(sorted(unknown))}")
    if missing:
        errors.append(f"assessment: missing fields: {', '.join(sorted(missing))}")
        return errors
    if not isinstance(value["assessment_id"], str) or not ASSESSMENT_ID.fullmatch(value["assessment_id"]):
        errors.append("assessment_id: must be an ARR UUIDv4 assessment identifier")
    try:
        paper = select_paper(papers, value["paper_id"], value["version"])
    except (KeyError, ValueError) as exc:
        errors.append(f"paper: {exc}")
        paper = None
    if paper is not None:
        if value["version_id"] != paper.metadata.get("version_id"):
            errors.append("version_id: does not match the selected ARR version")
        if value["canonical_sha256"] != paper.metadata.get("integrity", {}).get("canonical_sha256"):
            errors.append("canonical_sha256: does not match the selected canonical artifact")
    for field, maximum in (("provider", 100), ("model_id", 160)):
        if not isinstance(value[field], str) or not 2 <= len(value[field].strip()) <= maximum:
            errors.append(f"{field}: invalid length")
    try:
        parse_exact_timestamp(value["assessed_at"])
    except (TypeError, ValueError):
        errors.append("assessed_at: must be an offset-aware ISO-8601 timestamp")
    if value["prompt_version"] != PROMPT_VERSION:
        errors.append(f"prompt_version: must be {PROMPT_VERSION}")
    if value["independence"] not in INDEPENDENCE:
        errors.append("independence: invalid value")
    if value["recommendation"] not in RECOMMENDATIONS:
        errors.append("recommendation: invalid value")
    score = value["millennium_score"]
    try:
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise InvalidOperation
        decimal_score = Decimal(str(score))
        if not Decimal("0") <= decimal_score <= Decimal("10") or decimal_score.as_tuple().exponent < -2:
            raise InvalidOperation
    except (InvalidOperation, ValueError):
        errors.append("millennium_score: must be 0.00..10.00 with at most two decimals")
    else:
        if not isinstance(value["overall_stars"], int) or value["overall_stars"] != expected_stars(float(decimal_score)):
            errors.append("overall_stars: must be the nearest whole-star rendering of millennium_score (minimum 1)")
    criteria = value["criteria"]
    if not isinstance(criteria, dict) or set(criteria) != set(CRITERIA):
        errors.append(f"criteria: must contain exactly {', '.join(CRITERIA)}")
    else:
        for name in CRITERIA:
            criterion = criteria[name]
            if not isinstance(criterion, dict) or set(criterion) != {"stars", "basis"}:
                errors.append(f"criteria.{name}: must contain stars and basis")
                continue
            if not isinstance(criterion["stars"], int) or not 1 <= criterion["stars"] <= 5:
                errors.append(f"criteria.{name}.stars: must be 1..5")
            if not isinstance(criterion["basis"], str) or not 15 <= len(criterion["basis"].strip()) <= 600:
                errors.append(f"criteria.{name}.basis: must contain 15..600 characters")
    if not isinstance(value["summary"], str) or not 40 <= len(value["summary"].strip()) <= 1600:
        errors.append("summary: must contain 40..1600 characters")
    for field in ("strengths", "weaknesses", "potential_errors", "strong_novelty_candidates", "unresolved_material_objections"):
        _text_list(value[field], field, errors)
    material = value["unresolved_material_objections"]
    if isinstance(material, list) and material and value["recommendation"] in {"accept", "minor_revision"}:
        errors.append("recommendation: unresolved material objections require major_revision or reject")
    if value["recommendation"] == "accept" and (float(score) < 3 or value["overall_stars"] < 3):
        errors.append("recommendation: accept requires the public acceptable floor of 3.00 / three stars")
    if not isinstance(value["source_response_sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", value["source_response_sha256"]):
        errors.append("source_response_sha256: must be a lowercase SHA-256 digest")
    else:
        original_response = {key: item for key, item in value.items() if key not in {"assessment_id", "source_response_sha256"}}
        if source_hash(original_response) != value["source_response_sha256"]:
            errors.append("source_response_sha256: does not match the structured model response")
    return errors


def normalize_model_response(value: object) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("Expected one JSON object")
    forbidden = {"assessment_id", "source_response_sha256"} & set(value)
    if forbidden:
        raise ValueError("The model response must not set operator-controlled fields: " + ", ".join(sorted(forbidden)))
    normalized = dict(value)
    normalized["assessment_id"] = f"arr:assessment:{uuid.uuid4()}"
    normalized["source_response_sha256"] = source_hash(value)
    return normalized


def validate_registry(registry: object, papers: Iterable[Paper]) -> list[str]:
    if not isinstance(registry, dict) or registry.get("schema_version") != "1.0" or registry.get("protocol") != PROMPT_VERSION or registry.get("license") != "CC-BY-4.0" or not isinstance(registry.get("assessments"), list):
        return ["assessment registry: invalid envelope"]
    errors: list[str] = []
    ids: set[str] = set()
    hashes: set[str] = set()
    for index, item in enumerate(registry["assessments"]):
        for error in validate_assessment(item, papers):
            errors.append(f"assessments[{index}].{error}")
        if isinstance(item, dict):
            assessment_id = item.get("assessment_id")
            response_hash = item.get("source_response_sha256")
            if assessment_id in ids:
                errors.append(f"assessments[{index}].assessment_id: duplicate")
            if response_hash in hashes:
                errors.append(f"assessments[{index}].source_response_sha256: duplicate response")
            ids.add(assessment_id)
            hashes.add(response_hash)
    return errors


def assessments_for(assessments: Iterable[dict[str, Any]], paper: Paper) -> list[dict[str, Any]]:
    return sorted(
        [item for item in assessments if item["paper_id"] == paper.id and item["version_id"] == paper.metadata["version_id"]],
        key=lambda item: parse_exact_timestamp(item["assessed_at"]),
        reverse=True,
    )


def aggregate_assessments(items: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    eligible = [item for item in items if item["independence"] == "not_involved_in_manuscript"]
    if not eligible:
        return None
    scores = [float(item["millennium_score"]) for item in eligible]
    score = float(median(scores))
    return {
        "count": len(eligible),
        "score": score,
        "stars": expected_stars(score),
        "tier": tier_label(expected_stars(score)),
        "minimum": min(scores),
        "maximum": max(scores),
    }


def validate_highlights(registry: object, papers: Iterable[Paper]) -> list[str]:
    if not isinstance(registry, dict) or registry.get("schema_version") != "1.0" or registry.get("license") != "CC-BY-4.0" or not isinstance(registry.get("highlights"), list):
        return ["editorial highlight registry: invalid envelope"]
    errors: list[str] = []
    seen: set[tuple[str, str]] = set()
    paper_list = list(papers)
    required = {"paper_id", "version", "headline", "why_it_matters", "strengths", "caveats", "signed_by", "updated_at"}
    for index, item in enumerate(registry["highlights"]):
        prefix = f"highlights[{index}]"
        if not isinstance(item, dict) or set(item) != required:
            errors.append(f"{prefix}: fields do not match the highlight schema")
            continue
        try:
            select_paper(paper_list, item["paper_id"], item["version"])
        except (KeyError, ValueError) as exc:
            errors.append(f"{prefix}.paper: {exc}")
        key = (item["paper_id"], item["version"])
        if key in seen:
            errors.append(f"{prefix}: duplicate paper version")
        seen.add(key)
        for field, low, high in (("headline", 10, 180), ("why_it_matters", 40, 1600), ("signed_by", 2, 120)):
            if not isinstance(item[field], str) or not low <= len(item[field].strip()) <= high:
                errors.append(f"{prefix}.{field}: invalid length")
        for field, minimum in (("strengths", 1), ("caveats", 0)):
            values = item[field]
            if not isinstance(values, list) or not minimum <= len(values) <= 8 or any(not isinstance(v, str) or not 8 <= len(v.strip()) <= 500 for v in values):
                errors.append(f"{prefix}.{field}: invalid findings")
        try:
            parse_exact_timestamp(item["updated_at"])
        except (TypeError, ValueError):
            errors.append(f"{prefix}.updated_at: invalid timestamp")
    return errors
