# SPDX-License-Identifier: AGPL-3.0-or-later
"""Resolve exact published PDFs for same-directory copies in the Pages artifact."""
from __future__ import annotations

import hashlib
import re
import time
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


def verify_pdf(data: bytes, *, sha256: str | None = None, size: int | None = None) -> None:
    if not data.startswith(b"%PDF-"):
        raise ValueError("file does not have a PDF header")
    if sha256 and hashlib.sha256(data).hexdigest() != sha256:
        raise ValueError("PDF SHA-256 does not match the recorded version")
    if size is not None and len(data) != size:
        raise ValueError("PDF byte count does not match the recorded version")


def published_pdf(paper, timestamp: dict, *, cache_dir: Path, fetch_remote: bool = False) -> bytes | None:
    """Return validated bytes, or None for pending/withdrawn records or offline misses.

    Historical imports already have an author-authorized public bulk release even
    though their individual timestamp-registry entries are marked pending.
    """
    metadata = paper.metadata
    archival = metadata.get("archival_source")
    if metadata["status"] == "withdrawn":
        return None
    if not archival and timestamp.get("publication_state") != "published":
        return None
    integrity = metadata["integrity"]
    if metadata["source_of_truth"] in {"paper.pdf", "external_pdf"}:
        digest = integrity.get("canonical_sha256")
        size = integrity.get("canonical_bytes")
    else:
        # In TeX-origin records canonical_sha256 can identify the TeX source.
        digest = integrity.get("pdf_sha256")
        size = integrity.get("pdf_bytes")
    local = paper.path / "paper.pdf"
    if local.is_file():
        data = local.read_bytes()
        verify_pdf(data, sha256=digest, size=size)
        return data
    if not archival:
        # Source-only records have no PDF asset until one is supplied.
        return None

    if not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest):
        raise ValueError("remote PDF requires a recorded SHA-256")
    if not isinstance(size, int) or not 0 < size <= 100_000_000:
        raise ValueError("remote PDF requires a byte count between 1 and 100 MB")
    cached = cache_dir / f"{digest}.pdf"
    if cached.is_file():
        data = cached.read_bytes()
        verify_pdf(data, sha256=digest, size=size)
        return data
    if not fetch_remote:
        return None

    url = archival["mirror_pdf_url"]
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc != "github.com" or not re.fullmatch(
        r"/[^/]+/[^/]+/releases/download/[^/]+/[^/]+\.pdf", parsed.path
    ) or parsed.query or parsed.fragment:
        raise ValueError("remote PDF must be a public HTTPS GitHub Release PDF")
    request = Request(url, headers={"User-Agent": "ARR-Pages-PDF-Mirror/1.0"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                data = response.read(size + 1)
            break
        except OSError:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)
    verify_pdf(data, sha256=digest, size=size)
    cache_dir.mkdir(parents=True, exist_ok=True)
    # Only verified bytes enter the persistent cache.
    cached.write_bytes(data)
    return data
