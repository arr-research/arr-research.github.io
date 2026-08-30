# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from arrlib import discover_papers
from assessmentlib import ASSESSMENTS_PATH, load_assessment_registry, normalize_model_response, validate_assessment, validate_registry


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate and append one pasted frontier-model assessment.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", type=Path, help="JSON response file")
    source.add_argument("--stdin", action="store_true", help="Read the JSON response from standard input")
    source.add_argument("--clipboard", action="store_true", help="Read the JSON response from the desktop clipboard")
    parser.add_argument("--publish", action="store_true", help="Append the validated response to the public registry")
    return parser.parse_args()


def read_source(args: argparse.Namespace) -> str:
    if args.file:
        return args.file.read_text(encoding="utf-8")
    if args.stdin:
        return sys.stdin.read()
    try:
        import tkinter

        root = tkinter.Tk()
        root.withdraw()
        try:
            return root.clipboard_get()
        finally:
            root.destroy()
    except Exception as exc:  # pragma: no cover - depends on desktop clipboard
        raise RuntimeError(f"Could not read the desktop clipboard: {exc}") from exc


def main() -> int:
    args = parse_args()
    try:
        response = json.loads(read_source(args))
        assessment = normalize_model_response(response)
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    papers = discover_papers()
    errors = validate_assessment(assessment, papers)
    if errors:
        print("Assessment rejected:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    registry = load_assessment_registry()
    registry["assessments"].append(assessment)
    errors = validate_registry(registry, papers)
    if errors:
        print("Registry update rejected:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(json.dumps(assessment, ensure_ascii=False, indent=2))
    if not args.publish:
        print("Validated only. Re-run with --publish to append this response to the public registry.")
        return 0
    ASSESSMENTS_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Published {assessment['assessment_id']} to {ASSESSMENTS_PATH.relative_to(ASSESSMENTS_PATH.parents[1])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
