# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader


BASE_URL = "https://www.ai.vixra.org"
AUTHOR_URL = f"{BASE_URL}/author/lluis_eriksson"
DEFAULT_OUTPUT = Path("registry/ai-vixra-import.json")
DEFAULT_DOWNLOAD_DIR = Path("tmp/pdfs/ai-vixra")
DEFAULT_MIRROR_TAG = "AIVIXRA-LATEST-2026-08-30"
VERSION_RE = re.compile(r"(?P<identifier>\d{4}\.\d{4})v(?P<version>[1-9]\d*)\.pdf$")
TIMESTAMP_RE = re.compile(r"(20\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory Lluis Eriksson's ai.vixra papers and exact version histories."
    )
    parser.add_argument("--author-url", default=AUTHOR_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--download", action="store_true", help="Download and verify every latest PDF.")
    parser.add_argument("--download-dir", type=Path, default=DEFAULT_DOWNLOAD_DIR)
    parser.add_argument("--mirror-tag", default=DEFAULT_MIRROR_TAG)
    parser.add_argument("--from-inventory", action="store_true", help="Reuse the existing inventory and only verify/download PDFs.")
    return parser.parse_args()


def get(session: requests.Session, url: str) -> requests.Response:
    response = session.get(url, timeout=30)
    response.raise_for_status()
    return response


def https_url(base: str, value: str) -> str:
    absolute = urljoin(base, value)
    parsed = urlparse(absolute)
    return parsed._replace(scheme="https").geturl()


def text_after_link(link) -> str:
    values: list[str] = []
    sibling = link.next_sibling
    while sibling is not None and getattr(sibling, "name", None) != "br":
        values.append(sibling.get_text(" ", strip=True) if hasattr(sibling, "get_text") else str(sibling))
        sibling = sibling.next_sibling
    return " ".join(values).strip()


def parse_record(session: requests.Session, abstract_url: str) -> dict:
    response = get(session, abstract_url)
    soup = BeautifulSoup(response.text, "html.parser")
    identifier_tag = soup.find("meta", attrs={"name": "citation_vixra_id"})
    title_tag = soup.find("meta", attrs={"name": "citation_title"})
    author_tags = soup.find_all("meta", attrs={"name": "citation_author"})
    if not identifier_tag or not title_tag:
        raise ValueError(f"Missing citation metadata at {abstract_url}")
    identifier = identifier_tag.get("content", "").strip()
    title = title_tag.get("content", "").strip()
    abstract_node = soup.select_one("#abstract p")
    abstract = abstract_node.get_text(" ", strip=True) if abstract_node else ""
    category_node = soup.select_one("#category h2")
    category = category_node.get_text(" ", strip=True) if category_node else "Unclassified"

    comments = ""
    for paragraph in soup.select("#flow > p"):
        bold = paragraph.find("b")
        if bold and bold.get_text(" ", strip=True).rstrip(":") == "Comments":
            comments = paragraph.get_text(" ", strip=True).removeprefix("Comments:").strip()
            break

    versions: list[dict] = []
    for link in soup.select('a[href*="/pdf/"]'):
        href = link.get("href", "")
        match = VERSION_RE.search(href)
        if not match or match.group("identifier") != identifier:
            continue
        timestamp_match = TIMESTAMP_RE.search(text_after_link(link))
        if not timestamp_match:
            continue
        submitted = datetime.strptime(timestamp_match.group(1), "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=timezone.utc
        )
        versions.append(
            {
                "version": f"v{int(match.group('version'))}",
                "submitted_at": submitted.isoformat(),
                "pdf_url": https_url(response.url, href),
            }
        )
    unique_versions = {item["version"]: item for item in versions}
    versions = sorted(unique_versions.values(), key=lambda item: int(item["version"][1:]))
    if not versions:
        raise ValueError(f"No version history found for {identifier}")

    return {
        "identifier": identifier,
        "abstract_url": https_url(response.url, response.url),
        "title": title,
        "authors": [tag.get("content", "").strip() for tag in author_tags if tag.get("content")],
        "category": category,
        "abstract": abstract,
        "comments": comments,
        "first_submitted_at": versions[0]["submitted_at"],
        "latest_version": versions[-1]["version"],
        "latest_submitted_at": versions[-1]["submitted_at"],
        "latest_pdf_url": versions[-1]["pdf_url"],
        "versions": versions,
    }


def download_latest(record: dict, download_dir: Path, mirror_tag: str) -> dict:
    selected = record["versions"][-1]
    payload = b""
    for candidate in reversed(record["versions"]):
        try:
            with requests.get(
                candidate["pdf_url"],
                timeout=90,
                headers={"User-Agent": "ARR archival importer/1.0 (+https://arr-research.github.io/)"},
            ) as response:
                response.raise_for_status()
                payload = response.content
            selected = candidate
            break
        except requests.RequestException:
            continue
    if not payload:
        raise ValueError(f"{record['identifier']}: no version PDF is retrievable")
    asset_name = f"ai-vixra-{record['identifier']}-{selected['version']}.pdf"
    target = download_dir / asset_name
    if not payload.startswith(b"%PDF-"):
        raise ValueError(f"{record['identifier']}: latest asset is not a PDF")
    target.write_bytes(payload)
    try:
        reader = PdfReader(target)
        pages = len(reader.pages)
        if pages < 1:
            raise ValueError("zero pages")
        text_chars = sum(len(page.extract_text() or "") for page in reader.pages)
    except Exception as error:  # noqa: BLE001 - malformed remote files must fail the import.
        target.unlink(missing_ok=True)
        raise ValueError(f"{record['identifier']}: unreadable PDF ({error})") from error
    digest = hashlib.sha256(payload).hexdigest()
    return {
        **record,
        "latest_asset": {
            "name": asset_name,
            "source_version": selected["version"],
            "bytes": len(payload),
            "pages": pages,
            "text_characters": text_chars,
            "sha256": digest,
            "mirror_release_url": f"https://github.com/arr-research/arr-research.github.io/releases/tag/{mirror_tag}",
            "mirror_pdf_url": f"https://github.com/arr-research/arr-research.github.io/releases/download/{mirror_tag}/{asset_name}",
        },
    }


def main() -> int:
    args = parse_args()
    author_response = None
    if args.from_inventory:
        prior = json.loads(args.output.read_text(encoding="utf-8"))
        records = prior["records"]
        abstract_urls = [record["abstract_url"] for record in records]
        source_url = prior["source"]
        errors: list[str] = []
    else:
      with requests.Session() as session:
        session.headers.update({"User-Agent": "ARR archival importer/1.0 (+https://arr-research.github.io/)"})
        author_response = get(session, args.author_url)
        author_soup = BeautifulSoup(author_response.text, "html.parser")
        abstract_urls: list[str] = []
        seen: set[str] = set()
        for link in author_soup.select('a[href^="/abs/"]'):
            url = https_url(author_response.url, link.get("href", ""))
            if url not in seen:
                seen.add(url)
                abstract_urls.append(url)

        records = []
        errors = []
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            future_urls = {executor.submit(parse_record, session, url): url for url in abstract_urls}
            for future in as_completed(future_urls):
                url = future_urls[future]
                try:
                    records.append(future.result())
                except Exception as error:  # noqa: BLE001 - inventory reports every remote failure.
                    errors.append(f"{url}: {error}")

      source_url = https_url(author_response.url, author_response.url)
    records.sort(key=lambda item: (item["first_submitted_at"], item["identifier"]), reverse=True)
    if errors:
        print("ai.vixra inventory failed:", file=sys.stderr)
        for error in sorted(errors):
            print(f"- {error}", file=sys.stderr)
        return 1
    if len(records) != len(abstract_urls):
        print(f"Expected {len(abstract_urls)} records but parsed {len(records)}", file=sys.stderr)
        return 1

    if args.download:
        args.download_dir.mkdir(parents=True, exist_ok=True)
        verified: list[dict] = []
        download_errors: list[str] = []
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {
                executor.submit(download_latest, record, args.download_dir, args.mirror_tag): record
                for record in records
            }
            for future in as_completed(futures):
                try:
                    verified.append(future.result())
                except Exception as error:  # noqa: BLE001 - report the complete failed set.
                    download_errors.append(str(error))
        if download_errors:
            print("Latest-PDF verification failed:", file=sys.stderr)
            for error in sorted(download_errors):
                print(f"- {error}", file=sys.stderr)
            return 1
        records = sorted(
            verified,
            key=lambda item: (item["first_submitted_at"], item["identifier"]),
            reverse=True,
        )
        manifest = "".join(
            f"{record['latest_asset']['sha256']}  {record['latest_asset']['name']}\n"
            for record in sorted(records, key=lambda item: item["latest_asset"]["name"])
        )
        (args.download_dir / "SHA256SUMS").write_text(manifest, encoding="utf-8")

    output = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": source_url,
        "source_timestamp_note": "ai.vixra displays no timezone; timestamps are preserved verbatim and normalized with +00:00 solely for deterministic ordering.",
        "author": "Lluis Eriksson",
        "record_count": len(records),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    version_count = sum(len(record["versions"]) for record in records)
    print(f"Inventoried {len(records)} papers and {version_count} ai.vixra versions at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
