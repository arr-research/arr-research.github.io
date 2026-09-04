# SPDX-License-Identifier: AGPL-3.0-or-later
"""Check the built HTML/PDF contract before uploading the Pages artifact."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.meta: dict[str, list[str]] = {}
        self.links: list[str] = []
        self.canonical = ""
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "meta" and attrs.get("name"):
            self.meta.setdefault(attrs["name"], []).append(attrs.get("content", ""))
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href", "")


def site_file(root: Path, site_url: str, url: str) -> Path:
    prefix = site_url.rstrip("/") + "/"
    if not url.startswith(prefix):
        raise ValueError(f"URL is outside the site: {url}")
    relative = unquote(url[len(prefix):])
    if "?" in relative or "#" in relative:
        raise ValueError(f"Discovery URL contains a query or fragment: {url}")
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"URL escapes the site directory: {url}")
    return target / "index.html" if url.endswith("/") else target


def check_site(root: Path, site_url: str) -> tuple[list[str], int, int]:
    errors: list[str] = []
    article_count = pdf_count = 0
    sitemap_urls: set[str] = set()
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        tree = ET.parse(root / "sitemap.xml")
        maps = [tree]
        if tree.getroot().tag.endswith("sitemapindex"):
            maps = [ET.parse(site_file(root, site_url, loc.text)) for loc in tree.findall("s:sitemap/s:loc", namespace)]
        for tree in maps:
            sitemap_urls.update(loc.text for loc in tree.findall("s:url/s:loc", namespace))
        for url in sorted(sitemap_urls):
            if not site_file(root, site_url, url).is_file():
                errors.append(f"Sitemap target does not exist: {url}")
        robots = (root / "robots.txt").read_text(encoding="utf-8")
        if f"Sitemap: {site_url.rstrip('/')}/sitemap.xml" not in robots:
            errors.append("robots.txt does not advertise the canonical sitemap")
    except (OSError, ValueError, ET.ParseError) as error:
        errors.append(str(error))

    for path in sorted(root.rglob("*.html")):
        page = Page(path.read_text(encoding="utf-8"))
        if "citation_title" not in page.meta:
            continue
        article_count += 1
        label = path.relative_to(root).as_posix()
        if any(path.parent.glob("*.pdf")) and not page.meta.get("citation_pdf_url"):
            errors.append(f"{label}: local PDF has no citation_pdf_url")
        for field in ("citation_title", "citation_author", "citation_publication_date"):
            if not page.meta.get(field) or not all(page.meta[field]):
                errors.append(f"{label}: missing {field}")
        try:
            if site_file(root, site_url, page.canonical) != path.resolve():
                errors.append(f"{label}: canonical URL points at a different page")
            if page.canonical not in sitemap_urls:
                errors.append(f"{label}: canonical URL is missing from sitemap")
            for pdf in page.meta.get("citation_pdf_url", []):
                pdf_count += 1
                parsed, abstract = urlsplit(pdf), urlsplit(page.canonical)
                if (parsed.scheme, parsed.netloc) != (abstract.scheme, abstract.netloc) or parsed.path.rsplit("/", 1)[0] + "/" != abstract.path:
                    errors.append(f"{label}: PDF must be in the same directory as its abstract")
                if not parsed.path.endswith(".pdf") or parsed.query or parsed.fragment:
                    errors.append(f"{label}: PDF URL must end in .pdf")
                if pdf not in page.links and parsed.path not in page.links:
                    errors.append(f"{label}: missing a direct HTML link to its PDF")
                target = site_file(root, site_url, pdf)
                if not target.is_file():
                    errors.append(f"{label}: advertised PDF is missing")
                else:
                    with target.open("rb") as stream:
                        if stream.read(5) != b"%PDF-":
                            errors.append(f"{label}: advertised file is not a PDF")
        except ValueError as error:
            errors.append(f"{label}: {error}")
    if not article_count:
        errors.append("No scholarly article pages found")
    return errors, article_count, pdf_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("_site"))
    parser.add_argument("--canonical-url", required=True)
    args = parser.parse_args()
    errors, pages, pdfs = check_site(args.site_dir, args.canonical_url)
    for error in errors:
        print(error)
    print(f"Checked {pages} scholarly pages and {pdfs} same-directory PDF links; {len(errors)} error(s).")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
