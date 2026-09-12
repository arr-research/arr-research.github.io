# SPDX-License-Identifier: AGPL-3.0-or-later
"""Versioned, provisional capability weighting; never an acceptance decision."""
from __future__ import annotations

import hashlib
import json
import math
import re
from datetime import datetime
from functools import lru_cache
from pathlib import Path

POLICY = "AIRR-RATING-1.0"
SNAPSHOT = Path(__file__).resolve().parents[1] / "registry/benchmarks/epoch-frontiermath-tier4-v2-20260912.json"


@lru_cache(maxsize=1)
def load_benchmark():
    raw = SNAPSHOT.read_bytes()
    data = json.loads(raw)
    if data["benchmark"] != "FrontierMath Tier 4 (v2)" or data["license"] != "CC-BY-4.0":
        raise ValueError("Unexpected benchmark snapshot")
    seen = set()
    for row in data["results"]:
        key = (row["organization"], row["model_version"])
        if key in seen:
            raise ValueError("Ambiguous benchmark configuration")
        seen.add(key)
        for k in ("accuracy", "standard_error"):
            value = row[k]
            if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or not 0 <= value <= 1:
                raise ValueError("Benchmark values must be finite proportions")
    return {**data, "snapshot_sha256": hashlib.sha256(raw).hexdigest()}


def identity(report):
    runtime = report.get("runtime_provenance")
    source = runtime or report
    return source["provider"].strip(), source["model_id"].strip()


def weight_for(report, benchmark, applicable=True):
    runtime = report.get("runtime_provenance")
    reason = "No evidenced exact benchmark configuration"
    if not applicable:
        return {"weight": 1.0, "matched": False, "reason": "Benchmark outside declared mathematical scope"}
    if runtime and re.fullmatch(r"[0-9a-f]{64}", str(runtime.get("evidence_sha256", ""))) and runtime.get("basis") in {"platform_runtime_metadata", "author_verified_ui", "operator_verified_ui"}:
        key = runtime["model_id"] + "_" + runtime["reasoning_effort"]
        hits = [r for r in benchmark["results"] if r["organization"] == runtime["provider"] and r["model_version"] == key]
        if len(hits) > 1:
            raise ValueError("Ambiguous benchmark mapping")
        if hits:
            row = hits[0]
            # One reported standard error is a cautious policy margin, not a paper CI.
            q = max(0.0, row["accuracy"] - row["standard_error"])
            return {"weight": 1.0 + 2.0*q, "matched": True, "reason": "Exact evidenced model and effort",
                    "benchmark_key": key, "accuracy": row["accuracy"], "standard_error": row["standard_error"], "run_id": row["run_id"]}
    return {"weight": 1.0, "matched": False, "reason": reason}


def aggregate_ratings(items, *, benchmark=None, applicable=True):
    reports = list(items)
    if not reports:
        return None
    locks = {(r["paper_id"], r["version_id"], r["canonical_sha256"]) for r in reports}
    if len(locks) != 1:
        raise ValueError("Ratings cannot pool paper versions or PDF hashes")
    latest = {}
    for report in reports:
        score = report["millennium_score"]
        if isinstance(score, bool) or not isinstance(score, (float,int)) or not math.isfinite(score) or not 0 <= score <= 10:
            raise ValueError("Invalid rating")
        at = datetime.fromisoformat(report["assessed_at"].replace("Z", "+00:00"))
        if at.utcoffset() is None:
            raise ValueError("Report date needs timezone")
        key = identity(report)  # repeated runs and effort settings of one model get one voice
        previous = latest.get(key)
        if previous and previous[0] == at and (previous[1].get("source_response_sha256") != report.get("source_response_sha256") or previous[1]["millennium_score"] != score):
            raise ValueError("Conflicting simultaneous reports require explicit adjudication")
        if previous is None or at > previous[0]:
            latest[key] = (at, report)
    selected = [r for _,r in sorted(latest.values(), key=lambda x:(x[0],identity(x[1])))]
    benchmark = load_benchmark() if benchmark is None else benchmark
    weighted = [{"assessment_id": r.get("assessment_id"), "model": identity(r), "score": float(r["millennium_score"]),
                 "involvement": r["independence"], **weight_for(r, benchmark, applicable)} for r in selected]
    total = sum(x["weight"] for x in weighted)
    score = sum(x["score"]*x["weight"] for x in weighted)/total
    raw_mean = sum(x["score"] for x in weighted)/len(weighted)
    providers = {identity(r)[0] for r in selected}
    blockers = [r.get("assessment_id") for r in reports if r["recommendation"] != "accept" or r["unresolved_material_objections"]]
    reasons = []
    if len(selected)<2: reasons.append("Only one distinct model")
    if len(providers)<2: reasons.append("One provider; shared blind spots possible")
    def isolated(r):
        c=r.get("review_context",{})
        return (c.get("mode")=="fresh_blind" and all(c.get(k) is True for k in ("history_isolated","memory_disabled","other_reports_withheld"))
                and c.get("basis") in {"platform_runtime_metadata","author_verified_ui","operator_verified_ui"}
                and bool(re.fullmatch(r"[0-9a-f]{64}",str(c.get("evidence_sha256","")))))
    if any(not isolated(r) for r in selected):reasons.append("Fresh blinded review context not documented for every model")
    if any(not x["matched"] for x in weighted):reasons.append("Benchmark match incomplete" if applicable else "Mathematical benchmark not applied to this subject")
    span = max(x["score"] for x in weighted)-min(x["score"] for x in weighted)
    if span>1.0:reasons.append("Review scores differ by more than one point")
    if blockers:reasons.append("Adverse reports or unresolved objections require editorial disposition")
    backing = "Limited" if reasons else "Broader model support"
    return {"policy": POLICY,"count":len(selected),"preserved_reports":len(reports),"score":score,"unweighted_mean":raw_mean,
            "minimum":min(x["score"] for x in weighted),"maximum":max(x["score"] for x in weighted),
            "weights":weighted,"benchmark_matches":sum(x["matched"] for x in weighted),
            "benchmark_snapshot":benchmark["snapshot_id"],"benchmark_snapshot_sha256":benchmark.get("snapshot_sha256"),
            "evidence_backing":backing,"evidence_reasons":reasons,"confidence_probability":None,
            "confidence_note":"Qualitative evidence description, not a calibrated probability or confidence interval. Model-only evidence never establishes high confidence.",
            "blocking_report_ids":blockers,"acceptance_determined":False}
