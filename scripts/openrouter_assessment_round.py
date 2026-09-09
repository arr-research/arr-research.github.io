# SPDX-License-Identifier: AGPL-3.0-or-later
"""Plan and run sealed AIRR public-assessment rounds through OpenRouter.

The API key is read only from OPENROUTER_API_KEY. Plans and raw responses live
under work/, which is ignored by Git. This script never edits the public registry.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from arrlib import discover_papers, select_paper
from assessmentlib import normalize_model_response, validate_assessment
from prepare_model_assessment import build_prompt


ROOT = Path(__file__).resolve().parents[1]
RUNS_ROOT = ROOT / "work" / "openrouter-assessment-rounds"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_URL = "https://openrouter.ai/api/v1/models"
SITE_URL = "https://airr.science"
OPERATOR_FIELDS = {"assessment_id", "source_response_sha256", "runtime_provenance"}


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def model_response_schema() -> dict[str, Any]:
    schema = json.loads((ROOT / "schema" / "model-assessment.schema.json").read_text(encoding="utf-8"))
    schema.pop("$id", None)
    schema["title"] = "AIRR model-authored assessment response"
    schema["required"] = [field for field in schema["required"] if field not in OPERATOR_FIELDS]
    for field in OPERATOR_FIELDS:
        schema["properties"].pop(field, None)
    # Some upstream structured-output validators reject JSON Schema's
    # ``multipleOf`` keyword for numbers. AIRR applies the stricter two-decimal
    # check locally before an assessment can be imported.
    def remove_multiple_of(value: object) -> None:
        if isinstance(value, dict):
            value.pop("multipleOf", None)
            for child in value.values():
                remove_multiple_of(child)
        elif isinstance(value, list):
            for child in value:
                remove_multiple_of(child)

    remove_multiple_of(schema)
    return schema


def get_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "AIRR-assessment-runner/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read())


def available_models() -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in get_json(MODEL_URL).get("data", [])}


def round_dir(round_id: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{2,80}", round_id):
        raise ValueError("round id must use 3..81 letters, numbers, dots, underscores or hyphens")
    return RUNS_ROOT / round_id


def create_plan(args: argparse.Namespace) -> int:
    if len(set(args.models)) != len(args.models) or len(args.models) < 2:
        raise ValueError("choose at least two distinct exact model slugs")
    catalog = available_models()
    missing = [model for model in args.models if model not in catalog]
    if missing:
        raise ValueError("models absent from the current OpenRouter catalog: " + ", ".join(missing))
    efforts: dict[str, str] = {}
    for entry in args.efforts:
        if "=" not in entry:
            raise ValueError("effort must use MODEL=LEVEL")
        model, effort = entry.rsplit("=", 1)
        if model not in args.models or effort not in {"none", "minimal", "low", "medium", "high", "xhigh", "max"}:
            raise ValueError(f"invalid model effort: {entry}")
        efforts[model] = effort
    papers = discover_papers()
    selected = [select_paper(papers, paper_id, args.version) for paper_id in args.papers]
    requests: list[dict[str, Any]] = []
    for paper in selected:
        prompt = build_prompt(paper)
        pdf_url = f"{SITE_URL}/papers/{paper.id}/{paper.id}-{paper.version}.pdf"
        for model in args.models:
            inputs = catalog[model].get("architecture", {}).get("input_modalities", [])
            requests.append({
                "paper_id": paper.id,
                "version": paper.version,
                "version_id": paper.metadata["version_id"],
                "canonical_sha256": paper.metadata["integrity"]["canonical_sha256"],
                "pdf_url": pdf_url,
                "model": model,
                "model_canonical_slug": catalog[model].get("canonical_slug"),
                "reasoning_effort": efforts.get(model, "high"),
                "pdf_engine": "native" if "file" in inputs else "mistral-ocr",
                "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            })
    plan = {
        "schema_version": "1.0",
        "protocol": "ARR-ASSESS-1.0",
        "round_id": args.round_id,
        "created_at": utc_now(),
        "selection_rule": "Every valid result from every predeclared paper/model pair is retained; no score-based resampling or cherry-picking.",
        "independence_declaration": args.independence_declaration,
        "transport": {
            "service": "OpenRouter",
            "endpoint": API_URL,
            "pdf_engine": "native where supported; otherwise mistral-ocr",
            "structured_output": True,
            "provider_data_collection": "deny",
            "zero_data_retention": False,
            "require_parameters": False,
            "model_fallbacks": False,
            "same_model_endpoint_fallbacks": True,
        },
        "requests": requests,
    }
    target = round_dir(args.round_id)
    target.mkdir(parents=True, exist_ok=False)
    (target / "manifest.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (target / "manifest.sha256").write_text(digest(plan) + "  manifest.json\n", encoding="ascii")
    print(f"Sealed {len(requests)} requests in {target}")
    return 0


def load_sealed(round_id: str) -> tuple[Path, dict[str, Any]]:
    target = round_dir(round_id)
    plan = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
    expected = (target / "manifest.sha256").read_text(encoding="ascii").split()[0]
    if digest(plan) != expected:
        raise ValueError("manifest seal does not match; refuse to run a modified round")
    return target, plan


def request_body(item: dict[str, Any], independence: str) -> dict[str, Any]:
    paper = select_paper(discover_papers(), item["paper_id"], item["version"])
    prompt = build_prompt(paper)
    if hashlib.sha256(prompt.encode("utf-8")).hexdigest() != item["prompt_sha256"]:
        raise ValueError(f"prompt changed after sealing for {item['paper_id']}")
    identity = (
        f"\n\nRuntime instructions: this request is routed by OpenRouter to the exact model slug "
        f"`{item['model']}`. Set `provider` to `OpenRouter` and `model_id` to exactly "
        f"`{item['model']}`. Set `independence` to `{independence}`. "
        "OUTPUT LIMITS ARE STRICT: each criterion basis must be at most 500 characters; "
        "the summary at most 1200 characters; each list item at most 600 characters; "
        "use at most 8 items per list. Return the final JSON before the output limit."
    )
    reasoning = {"effort": item["reasoning_effort"], "exclude": True}
    return {
        "model": item["model"],
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt + identity},
            {"type": "file", "file": {"filename": f"{item['paper_id']}-{item['version']}.pdf", "file_data": item["pdf_url"]}},
        ]}],
        "response_format": {"type": "json_schema", "json_schema": {"name": "airr_assessment", "strict": True, "schema": model_response_schema()}},
        "plugins": [{"id": "file-parser", "pdf": {"engine": item["pdf_engine"]}}],
        "provider": {"allow_fallbacks": True, "require_parameters": False, "data_collection": "deny"},
        "reasoning": reasoning,
        "max_completion_tokens": 48000,
        "stream": False,
    }


def call_openrouter(body: dict[str, Any], api_key: str) -> tuple[int, dict[str, str], dict[str, Any]]:
    request = urllib.request.Request(API_URL, data=canonical_bytes(body), method="POST", headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": SITE_URL,
        "X-Title": "AIRR independent model assessments",
        "X-OpenRouter-Metadata": "enabled",
    })
    try:
        with urllib.request.urlopen(request, timeout=900) as response:
            return response.status, dict(response.headers.items()), json.loads(response.read())
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"error": {"message": raw.decode("utf-8", errors="replace")}}
        return exc.code, dict(exc.headers.items()), payload


def parse_content(response: dict[str, Any]) -> dict[str, Any]:
    content = response["choices"][0]["message"]["content"]
    if isinstance(content, dict):
        return content
    if isinstance(content, list):
        content = "".join(part.get("text", "") for part in content if isinstance(part, dict) and part.get("type") in {"text", "output_text"})
    if not isinstance(content, str):
        raise ValueError("response content is neither a JSON string nor an object")
    return json.loads(content)


def run_plan(args: argparse.Namespace) -> int:
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is not set")
    target, plan = load_sealed(args.round_id)
    outcomes = target / "outcomes"
    outcomes.mkdir(exist_ok=True)
    papers = discover_papers()
    failures = 0
    attempted = 0
    for index, item in enumerate(plan["requests"], start=1):
        stem = f"{index:02d}-{item['paper_id']}-{safe_name(item['model'])}"
        audit_path = outcomes / f"{stem}.response.json"
        result_path = outcomes / f"{stem}.assessment.json"
        if audit_path.exists() and not args.retry_failed:
            print(f"SKIP {stem}: outcome already recorded")
            continue
        if attempted >= args.max_requests:
            print(f"STOP: per-run safety limit of {args.max_requests} request(s) reached")
            break
        attempted += 1
        body = request_body(item, plan["independence_declaration"])
        request_hash = digest(body)
        status, headers, response = call_openrouter(body, api_key)
        audit = {
            "recorded_at": utc_now(), "request_sha256": request_hash, "http_status": status,
            "generation_id": headers.get("X-Generation-Id") or response.get("id"),
            "requested_model": item["model"], "response": response,
        }
        audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        try:
            if status != 200:
                raise ValueError(f"OpenRouter returned HTTP {status}")
            model_response = parse_content(response)
            if model_response.get("provider") != "OpenRouter" or model_response.get("model_id") != item["model"]:
                raise ValueError("model response did not preserve the instructed runtime identity")
            normalized = normalize_model_response(model_response)
            errors = validate_assessment(normalized, papers)
            if errors:
                raise ValueError("; ".join(errors))
            result_path.write_text(json.dumps(model_response, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"OK   {stem}: {model_response['millennium_score']:.2f}")
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            failures += 1
            (outcomes / f"{stem}.error.txt").write_text(str(exc) + "\n", encoding="utf-8")
            print(f"FAIL {stem}: {exc}", file=sys.stderr)
            print("STOP: fix and review this failure before spending on another request", file=sys.stderr)
            return 1
    return 1 if failures else 0


def status(args: argparse.Namespace) -> int:
    target, plan = load_sealed(args.round_id)
    outcomes = target / "outcomes"
    print(f"Round {args.round_id}: {len(plan['requests'])} sealed requests")
    for index, item in enumerate(plan["requests"], start=1):
        stem = f"{index:02d}-{item['paper_id']}-{safe_name(item['model'])}"
        state = "valid" if (outcomes / f"{stem}.assessment.json").exists() else "failed" if (outcomes / f"{stem}.error.txt").exists() else "pending"
        print(f"{state:7} {item['paper_id']} {item['model']}")
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Run sealed AIRR assessments through OpenRouter without auto-publication.")
    commands = root.add_subparsers(dest="command", required=True)
    plan = commands.add_parser("plan", help="Seal papers, exact hashes and models before seeing results")
    plan.add_argument("--round-id", required=True)
    plan.add_argument("--paper", dest="papers", action="append", required=True)
    plan.add_argument("--model", dest="models", action="append", required=True)
    plan.add_argument("--effort", dest="efforts", action="append", default=[], help="Per-model reasoning level as MODEL=LEVEL")
    plan.add_argument("--version")
    plan.add_argument("--independence-declaration", choices=("not_involved_in_manuscript", "involved_in_manuscript", "unknown"), default="not_involved_in_manuscript")
    plan.set_defaults(func=create_plan)
    run = commands.add_parser("run", help="Execute every pending request in a sealed round")
    run.add_argument("--round-id", required=True)
    run.add_argument("--retry-failed", action="store_true", help="Retry only for transport or schema failure; never for an unfavorable score")
    run.add_argument("--max-requests", type=int, default=1, choices=range(1, 9), help="Safety cap per invocation; defaults to one paid request")
    run.set_defaults(func=run_plan)
    show = commands.add_parser("status", help="Show pending, valid and failed outcomes")
    show.add_argument("--round-id", required=True)
    show.set_defaults(func=status)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError, urllib.error.URLError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
