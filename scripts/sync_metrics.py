# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path


TAG_PATTERN = re.compile(r"^(ARR-[0-9]{4}-[0-9A-HJKMNP-TV-Z]{16})-(v[1-9][0-9]*)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a reproducible ARR activity-metrics snapshot.")
    parser.add_argument("--repository", required=True, help="GitHub OWNER/REPOSITORY")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--views-file",
        type=Path,
        help="Optional privacy-reviewed page-view export using the documented ARR interchange format.",
    )
    return parser.parse_args()


def fetch_releases(repository: str, token: str = "") -> list[dict]:
    releases: list[dict] = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repository}/releases?per_page=100&page={page}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "arr-metrics-sync/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:  # nosec B310 - fixed HTTPS GitHub API origin
                batch = json.load(response)
        except (urllib.error.URLError, TimeoutError) as error:
            raise RuntimeError(f"Could not read GitHub releases: {error}") from error
        if not isinstance(batch, list):
            raise RuntimeError("GitHub releases response was not an array")
        releases.extend(batch)
        if len(batch) < 100:
            return releases
        page += 1


def load_views(path: Path | None) -> tuple[dict, dict[str, dict[str, int | None]]]:
    if path is None:
        return (
            {
                "available": False,
                "definition": "Page views are not measured until ARR connects a privacy-reviewed, no-cookie analytics source.",
                "provider": "",
                "window_start": None,
                "window_end": None,
            },
            {},
        )
    value = json.loads(path.read_text(encoding="utf-8"))
    required = {"provider", "window_start", "window_end", "papers"}
    if not isinstance(value, dict) or not required.issubset(value):
        raise ValueError("views file must contain provider, window_start, window_end and papers")
    papers = value["papers"]
    if not isinstance(papers, dict):
        raise ValueError("views papers must be an object keyed by ARR id")
    normalized: dict[str, dict[str, int | None]] = {}
    for paper_id, metrics in papers.items():
        if not isinstance(metrics, dict):
            raise ValueError(f"views entry {paper_id} must be an object")
        page_views = metrics.get("page_views")
        visitors = metrics.get("unique_visitors")
        if not isinstance(page_views, int) or page_views < 0:
            raise ValueError(f"views entry {paper_id} has invalid page_views")
        if visitors is not None and (not isinstance(visitors, int) or visitors < 0):
            raise ValueError(f"views entry {paper_id} has invalid unique_visitors")
        normalized[paper_id] = {"page_views": page_views, "unique_visitors": visitors}
    return (
        {
            "available": True,
            "definition": "Privacy-reviewed page loads in the displayed measurement window; bots and blockers may affect counts.",
            "provider": str(value["provider"]),
            "window_start": value["window_start"],
            "window_end": value["window_end"],
        },
        normalized,
    )


def build_snapshot(repository: str, releases: list[dict], views_file: Path | None = None) -> dict:
    downloads: dict[str, int] = {}
    for release in releases:
        if release.get("draft"):
            continue
        tag = release.get("tag_name", "")
        match = TAG_PATTERN.fullmatch(tag) if isinstance(tag, str) else None
        if not match:
            continue
        paper_id = match.group(1)
        expected_pdf = f"{tag}.pdf"
        count = 0
        for asset in release.get("assets", []):
            if isinstance(asset, dict) and asset.get("name") == expected_pdf:
                value = asset.get("download_count", 0)
                if isinstance(value, int) and value >= 0:
                    count += value
        downloads[paper_id] = downloads.get(paper_id, 0) + count

    view_meta, views = load_views(views_file)
    paper_ids = sorted(set(downloads) | set(views))
    papers = {
        paper_id: {
            "pdf_downloads": downloads.get(paper_id, 0),
            "page_views": views.get(paper_id, {}).get("page_views"),
            "unique_visitors": views.get(paper_id, {}).get("unique_visitors"),
        }
        for paper_id in paper_ids
    }
    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "downloads": {
            "provider": "GitHub Releases",
            "definition": "Cumulative GitHub download_count for canonical PDF assets across all published versions; not unique and may include bots or repeat downloads.",
            "source_url": f"https://api.github.com/repos/{repository}/releases",
        },
        "views": view_meta,
        "papers": papers,
    }


def main() -> int:
    args = parse_args()
    releases = fetch_releases(args.repository, os.environ.get("GITHUB_TOKEN", ""))
    snapshot = build_snapshot(args.repository, releases, args.views_file)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote metrics for {len(snapshot['papers'])} ARR record(s) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
