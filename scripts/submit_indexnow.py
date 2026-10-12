# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
MANIFEST_NAME = "indexnow-manifest.json"
USER_AGENT = "AIRR-IndexNow/1.0 (+https://airr.science/)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Tell IndexNow which deployed AIRR pages changed.")
    parser.add_argument("--site-root", required=True, help="Canonical site root, for example https://airr.science/")
    parser.add_argument("--key-file", type=Path, help="UTF-8 IndexNow key file")
    parser.add_argument("--plan", type=Path, metavar="SITE_DIR", help="Before deployment: fingerprint the built site, write its manifest and report the pages that differ from the deployed one")
    parser.add_argument("--urls-json", help="JSON list of changed URLs from --plan; without it the whole sitemap is submitted")
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


class _IndexedText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag in {"script", "style"}:
            self._skip += 1
        elif tag == "meta" and attrs.get("name") == "description":
            self.parts.append(attrs.get("content") or "")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.parts.append(attrs.get("href") or "")

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def fingerprint(html: str) -> str:
    """Hash what a reader or search engine sees on a page.

    Download and view counters, dates and asset versions change on every scheduled
    build without the page saying anything new, so numbers and markup are left out.
    """
    parser = _IndexedText()
    parser.feed(html)
    text = re.sub(r"\s+", " ", re.sub(r"\d[\d.,:]*", "", " ".join(parser.parts))).strip()
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:20]


def local_sitemap_urls(site_dir: Path, site_root: str) -> list[str]:
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    prefix = site_root.rstrip("/") + "/"
    root = ET.parse(site_dir / "sitemap.xml").getroot()
    if not root.tag.endswith("sitemapindex"):
        return [location.text.strip() for location in root.findall("s:url/s:loc", namespace) if location.text]
    urls: list[str] = []
    for location in root.findall("s:sitemap/s:loc", namespace):
        child = ET.parse(site_dir / location.text.strip().removeprefix(prefix)).getroot()
        urls.extend(item.text.strip() for item in child.findall("s:url/s:loc", namespace) if item.text)
    return urls


def build_manifest(site_dir: Path, site_root: str) -> dict[str, str]:
    prefix = site_root.rstrip("/") + "/"
    manifest: dict[str, str] = {}
    for url in local_sitemap_urls(site_dir, site_root):
        if not url.startswith(prefix):
            raise ValueError(f"sitemap URL is outside {prefix}: {url}")
        relative = urllib.parse.unquote(url[len(prefix):])
        page = site_dir / relative / "index.html" if url.endswith("/") else site_dir / relative
        manifest[url] = fingerprint(page.read_text(encoding="utf-8"))
    return manifest


def changed_urls(current: dict[str, str], previous: object) -> list[str]:
    """Pages that are new or read differently; everything when the deployed state is unknown."""
    if not isinstance(previous, dict):
        return list(current)
    return [url for url, digest in current.items() if previous.get(url) != digest]


def plan(site_dir: Path, site_root: str, *, retries: int) -> tuple[list[str], int]:
    current = build_manifest(site_dir, site_root)
    (site_dir / MANIFEST_NAME).write_text(json.dumps(current, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    try:
        previous = json.loads(fetch(f"{site_root}/{MANIFEST_NAME}", retries=retries))
    except (urllib.error.URLError, TimeoutError, ValueError):
        # First deployment with a manifest, or the site is unreachable: fall back to the whole sitemap.
        previous = None
    return changed_urls(current, previous), len(current)


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
    if args.plan:
        urls, total = plan(args.plan, site_root, retries=1)
        print(f"IndexNow plan: {len(urls)} changed AIRR URL(s) of {total}")
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
                output.write(f"urls={json.dumps(urls)}\n")
        return 0
    if not args.key_file:
        raise ValueError("--key-file is required to submit")
    changed = json.loads(args.urls_json) if args.urls_json else None
    if changed == []:
        print("IndexNow: no AIRR page changed; nothing to submit")
        return 0
    key = args.key_file.read_text(encoding="utf-8").strip()
    public_key = fetch(f"{site_root}/indexnow-key.txt", retries=args.retries).decode("utf-8").strip()
    if public_key != key:
        raise ValueError("deployed IndexNow key does not match the repository key")
    urls = changed if changed is not None else sitemap_urls(f"{site_root}/sitemap.xml", retries=args.retries)
    payload = make_payload(site_root, key, urls)
    if args.dry_run:
        print(f"IndexNow dry run: {len(urls)} URL(s), key verified at {payload['keyLocation']}")
        return 0
    status = submit(args.endpoint, payload, retries=args.retries)
    if status not in {200, 202}:
        print(f"Unexpected IndexNow response: HTTP {status}", file=sys.stderr)
        return 1
    print(f"IndexNow accepted {len(urls)} AIRR URL(s): HTTP {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
