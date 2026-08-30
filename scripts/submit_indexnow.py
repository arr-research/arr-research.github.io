# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
USER_AGENT = "ARR-IndexNow/1.0 (+https://arr-research.github.io/)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Submit the deployed ARR sitemap to IndexNow.")
    parser.add_argument("--site-root", required=True, help="Canonical site root, for example https://arr-research.github.io/")
    parser.add_argument("--key-file", required=True, type=Path, help="UTF-8 IndexNow key file")
    parser.add_argument("--endpoint", default=INDEXNOW_ENDPOINT, help="IndexNow endpoint")
    parser.add_argument("--retries", type=int, default=4, help="Retries for transient deployment/API failures")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print without sending")
    return parser.parse_args()


def fetch(url: str, *, retries: int) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries:
                raise
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def sitemap_urls(sitemap_url: str, *, retries: int) -> list[str]:
    root = ET.fromstring(fetch(sitemap_url, retries=retries))
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    if root.tag.endswith("sitemapindex"):
        urls: list[str] = []
        for location in root.findall("s:sitemap/s:loc", namespace):
            if location.text:
                urls.extend(sitemap_urls(location.text.strip(), retries=retries))
        return urls
    return [location.text.strip() for location in root.findall("s:url/s:loc", namespace) if location.text]


def make_payload(site_root: str, key: str, urls: list[str]) -> dict[str, object]:
    site_root = site_root.rstrip("/")
    parsed = urllib.parse.urlparse(site_root)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("site root must be an absolute HTTPS URL")
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key):
        raise ValueError("IndexNow key must contain 8-128 letters, digits, or dashes")
    foreign = [url for url in urls if urllib.parse.urlparse(url).netloc != parsed.netloc]
    if foreign:
        raise ValueError(f"sitemap contains {len(foreign)} URL(s) outside {parsed.netloc}")
    if len(urls) > 10_000:
        raise ValueError("IndexNow accepts at most 10,000 URLs per request")
    return {
        "host": parsed.netloc,
        "key": key,
        "keyLocation": f"{site_root}/indexnow-key.txt",
        "urlList": urls,
    }


def submit(endpoint: str, payload: dict[str, object], *, retries: int) -> int:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": USER_AGENT},
        method="POST",
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.status
        except urllib.error.HTTPError as error:
            if error.code in {200, 202}:
                return error.code
            if error.code not in {429, 500, 502, 503, 504} or attempt == retries:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries:
                raise
        time.sleep(2**attempt)
    raise AssertionError("unreachable")


def main() -> int:
    args = parse_args()
    site_root = args.site_root.rstrip("/")
    key = args.key_file.read_text(encoding="utf-8").strip()
    public_key = fetch(f"{site_root}/indexnow-key.txt", retries=args.retries).decode("utf-8").strip()
    if public_key != key:
        raise ValueError("deployed IndexNow key does not match the repository key")
    urls = sitemap_urls(f"{site_root}/sitemap.xml", retries=args.retries)
    payload = make_payload(site_root, key, urls)
    if args.dry_run:
        print(f"IndexNow dry run: {len(urls)} URL(s), key verified at {payload['keyLocation']}")
        return 0
    status = submit(args.endpoint, payload, retries=args.retries)
    if status not in {200, 202}:
        print(f"Unexpected IndexNow response: HTTP {status}", file=sys.stderr)
        return 1
    print(f"IndexNow accepted {len(urls)} ARR URL(s): HTTP {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
