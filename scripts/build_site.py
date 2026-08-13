# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse
import html
import json
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

from arrlib import ROOT, discover_papers, validate_collection


SITE_DIR = ROOT / "site"
OUTPUT_DIR = ROOT / "_site"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the static ARR catalogue.")
    parser.add_argument("--base-path", default="", help="URL prefix, e.g. /arr-archive for GitHub project Pages")
    parser.add_argument("--canonical-url", default="", help="Public site root used in canonical links and sitemap")
    parser.add_argument("--repository", default="", help="GitHub OWNER/REPOSITORY")
    return parser.parse_args()


def clean_base_path(value: str) -> str:
    value = value.strip()
    if not value or value == "/":
        return ""
    return "/" + value.strip("/")


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def page_shell(*, title: str, description: str, content: str, base: str, canonical: str = "") -> str:
    canonical_tag = f'<link rel="canonical" href="{esc(canonical)}">' if canonical else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  {canonical_tag}
  <link rel="stylesheet" href="{base}/assets/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <a class="brand" href="{base}/">
      <span class="brand-mark" aria-hidden="true">A</span>
      <span><strong>ARR</strong><small>Archive for Rigorous Research</small></span>
    </a>
    <nav aria-label="Primary navigation">
      <a href="{base}/papers/">Papers</a>
      <a href="{base}/protocol/">Protocol</a>
      <a href="{base}/licensing/">Licensing</a>
      <a href="{base}/about/">About</a>
    </nav>
  </header>
  <main id="main">{content}</main>
  <footer>
    <p><strong>ARR</strong> is a curated archive with explicit evidence labels. Acceptance is not peer review and is not a guarantee of truth.</p>
    <p><a href="{base}/catalog.json">Machine-readable catalogue (CC0)</a> · <a href="{base}/catalog/index.json">Partition index</a> · <a href="{base}/protocol/">Verification protocol</a> · <a href="{base}/licensing/">Licensing</a> · <a href="https://github.com/arr-research/arr-research.github.io">Source (AGPL)</a></p>
  </footer>
</body>
</html>
"""


def status_badge(value: str) -> str:
    labels = {"accepted": "Accepted", "corrected": "Corrected", "withdrawn": "Withdrawn"}
    return f'<span class="badge badge-{esc(value)}">{esc(labels.get(value, value.title()))}</span>'


def verification_rows(metadata: dict) -> str:
    verification = metadata["verification"]
    labels = {
        "bibliography": "Bibliographic integrity",
        "source_integrity": "Source integrity",
        "reproducibility": "Reproducibility",
        "lean4": "Lean 4",
    }
    values = {
        "pass": "Pass",
        "partial": "Partial",
        "not_assessed": "Not assessed",
        "not_applicable": "Not applicable",
    }
    rows = []
    screening = metadata.get("screening", {})
    evaluator_count = len(screening.get("evaluators", []))
    screening_status = screening.get("status", "not_assessed")
    screening_label = {
        "pass": f"Pass · {evaluator_count} models",
        "fail": "Did not pass",
        "not_assessed": "Not assessed",
    }.get(screening_status, screening_status)
    screening_tone = "pass" if screening_status == "pass" else "neutral"
    rows.append(f'<div><dt>Frontier-model screening</dt><dd class="check-{screening_tone}">{esc(screening_label)}</dd></div>')
    for key in ("source_integrity", "bibliography", "reproducibility", "lean4"):
        value = verification[key]
        rendered = values.get(value, value)
        tone = "pass" if value in {"pass", "L2", "L3"} else "neutral"
        rows.append(f'<div><dt>{esc(labels[key])}</dt><dd class="check-{tone}">{esc(rendered)}</dd></div>')
    return "".join(rows)


def paper_card(metadata: dict, base: str) -> str:
    authors = ", ".join(author["name"] for author in metadata["authors"])
    return f"""
<article class="paper-card">
  <div class="paper-meta">{status_badge(metadata['status'])}<span>{esc(metadata['id'])} · {esc(metadata['version'])}</span></div>
  <h3><a href="{base}/papers/{quote(metadata['id'])}/">{esc(metadata['title'])}</a></h3>
  <p class="authors">{esc(authors)}</p>
  <p>{esc(metadata['abstract'])}</p>
  <div class="paper-foot"><span>{esc(metadata['date'])}</span><span>Protocol {esc(metadata['verification']['protocol'])}</span></div>
</article>"""


def build_home(papers: list, base: str, canonical_url: str) -> str:
    accepted = sum(p.metadata["status"] != "withdrawn" for p in papers)
    lean_verified = sum(p.metadata["verification"]["lean4"] in {"L2", "L3"} for p in papers)
    recent = "".join(paper_card(p.metadata, base) for p in papers[:6])
    if not recent:
        recent = """
<section class="empty-state">
  <span>Prototype phase</span>
  <h2>The archive is being prepared.</h2>
  <p>No paper will appear here until its sources, provenance and verification record have completed the ARR acceptance workflow.</p>
</section>"""
    content = f"""
<section class="hero">
  <div class="eyebrow">Open · Curated · Reproducible</div>
  <h1>Research should arrive with its evidence.</h1>
  <p class="lede">ARR publishes source-first preprints with explicit, documented verification evidence. Every record keeps its manuscript, code, provenance, version, licenses and checks.</p>
  <div class="hero-actions"><a class="button" href="{base}/papers/">Browse papers</a><a class="text-link" href="{base}/protocol/">Read the protocol →</a></div>
</section>
<section class="stats" aria-label="Archive statistics">
  <div><strong>{accepted}</strong><span>public records</span></div>
  <div><strong>{lean_verified}</strong><span>Lean kernel verified</span></div>
  <div><strong>100%</strong><span>source-first</span></div>
</section>
<section class="principles">
  <div><span>01</span><h2>Inspectable by default</h2><p>Manuscripts, metadata and code remain readable as plain files—not trapped behind a PDF or proprietary interface.</p></div>
  <div><span>02</span><h2>Claims match checks</h2><p>ARR reports pass, partial and not-assessed results exactly as recorded. It does not turn screening into a claim of truth.</p></div>
  <div><span>03</span><h2>History remains visible</h2><p>Published versions are identified by hashes and releases. Corrections create a new record rather than silently rewriting the past.</p></div>
</section>
<section class="recent"><div class="section-heading"><div><span>Catalogue</span><h2>Latest accepted research</h2></div><a href="{base}/papers/">View all</a></div>{recent}</section>
"""
    canonical = f"{canonical_url}/" if canonical_url else ""
    return page_shell(title="ARR — Archive for Rigorous Research", description="A curated, source-first archive of screened research preprints.", content=content, base=base, canonical=canonical)


def build_papers_index(papers: list, base: str, canonical_url: str) -> str:
    cards = "".join(paper_card(p.metadata, base) for p in papers)
    if not cards:
        cards = '<section class="empty-state compact"><h2>No accepted papers yet.</h2><p>The public catalogue begins only after the first candidate completes the ARR workflow.</p></section>'
    content = f"""
<section class="page-intro"><span>Public catalogue</span><h1>Accepted papers</h1><p>Each record corresponds to an explicit version and provides machine-readable sources, provenance and verification status.</p></section>
<section class="catalogue">{cards}</section>
"""
    canonical = f"{canonical_url}/papers/" if canonical_url else ""
    return page_shell(title="Papers — ARR", description="Accepted ARR research papers.", content=content, base=base, canonical=canonical)


def build_paper_page(paper, base: str, canonical_url: str, repository: str) -> str:
    metadata = paper.metadata
    authors = ", ".join(author["name"] for author in metadata["authors"])
    relative_path = paper.path.relative_to(ROOT).as_posix()
    tag = f"{metadata['id']}-{metadata['version']}"
    release_url = metadata.get("release_url")
    if not release_url and repository:
        release_url = f"https://github.com/{repository}/releases/tag/{tag}"
    source_url = f"https://github.com/{repository}/tree/main/{relative_path}" if repository else ""
    links = []
    if release_url:
        links.append(f'<a class="button" href="{esc(release_url)}">Download release assets</a>')
    if source_url:
        links.append(f'<a class="button secondary" href="{esc(source_url)}">Browse plain sources</a>')
    if metadata.get("doi"):
        links.append(f'<a class="text-link" href="https://doi.org/{esc(metadata["doi"])}">DOI {esc(metadata["doi"])}</a>')
    keywords = "".join(f"<li>{esc(keyword)}</li>" for keyword in metadata.get("keywords", []))
    evaluators = "".join(
        f'<li><strong>{esc(item["model_id"])}</strong><span>{esc(item["provider"])} · pass' +
        (' · creation conflict declared' if item.get("involved_in_creation") else '') +
        '</span></li>'
        for item in metadata["screening"]["evaluators"]
    )
    content = f"""
<article class="paper-page">
  <div class="paper-meta">{status_badge(metadata['status'])}<span>{esc(metadata['id'])} · {esc(metadata['version'])} · {esc(metadata['date'])}</span></div>
  <h1>{esc(metadata['title'])}</h1>
  <p class="paper-authors">{esc(authors)}</p>
  <div class="download-row">{''.join(links)}</div>
  <section class="abstract"><span>Abstract</span><p>{esc(metadata['abstract'])}</p></section>
  <div class="paper-grid">
    <section><h2>Verification record</h2><dl class="checks">{verification_rows(metadata)}</dl><p class="protocol-note">Screened under <a href="{base}/protocol/">{esc(metadata['verification']['protocol'])}</a>. ARR screening is not peer review.</p></section>
    <aside><h2>Record</h2><dl class="record"><div><dt>Manuscript license</dt><dd>{esc(metadata['licenses']['manuscript'])}</dd></div><div><dt>Metadata license</dt><dd>{esc(metadata['licenses']['metadata'])}</dd></div><div><dt>Canonical source</dt><dd>{esc(metadata['source_of_truth'])}</dd></div><div><dt>Stable record</dt><dd>{esc(metadata['record_id'])}</dd></div><div><dt>Version identifier</dt><dd>{esc(metadata['version_id'])}</dd></div><div><dt>AI assistance</dt><dd>{'Declared' if metadata['ai_assistance']['used'] else 'Not used'}</dd></div></dl><ul class="keywords">{keywords}</ul></aside>
  </div>
  <section class="disclosure"><h2>AI assistance statement</h2><p>{esc(metadata['ai_assistance']['statement'])}</p></section>
  <section class="screening-record"><h2>Frontier-model screening</h2><p>Status: <strong>{esc(metadata['screening']['status'])}</strong>. Any listed reports correspond to this exact version under {esc(metadata['screening']['protocol'])}; no absent assessment is represented as a pass.</p><ul>{evaluators}</ul></section>
</article>
"""
    canonical = f"{canonical_url}/papers/{metadata['id']}/" if canonical_url else ""
    return page_shell(title=f"{metadata['title']} — ARR", description=metadata["abstract"], content=content, base=base, canonical=canonical)


def build_protocol(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>ARR-SCREEN-1.0</span><h1>A visible standard, not a black box.</h1><p>ARR guarantees that its stated process was applied to the identified version. It does not certify universal truth, novelty or importance.</p></section>
<section class="protocol-steps">
  <article><span>Gate 1</span><h2>Complete research object</h2><p>Required sources, metadata, provenance, licenses and stable identifiers must be present and internally consistent.</p></article>
  <article><span>Gate 2</span><h2>Technical verification</h2><p>Hashes, generated files, executable code, tests and formal proofs are checked where applicable. Failures remain visible until resolved.</p></article>
  <article><span>Gate 3</span><h2>Evidence-specific assessment</h2><p>Performed checks are reported independently. An AI-screened pass requires at least three declared, version-specific model reports; assessment is not silently inferred when absent.</p></article>
  <article><span>Gate 4</span><h2>Editorial sign-off</h2><p>No unresolved critical objection may be hidden. Acceptance is tied to stable identifiers, the exact SHA-256 manifest and versioned protocols.</p></article>
</section>
<section class="callout"><h2>Lean 4 verification levels</h2><p><strong>L0</strong> source supplied · <strong>L1</strong> clean build · <strong>L2</strong> kernel-checked, no unfinished proofs, axioms audited · <strong>L3</strong> correspondence between formalization and manuscript independently reviewed.</p></section>
"""
    canonical = f"{canonical_url}/protocol/" if canonical_url else ""
    return page_shell(title="Screening protocol — ARR", description="The documented ARR screening and verification protocol.", content=content, base=base, canonical=canonical)


def build_about(base: str, canonical_url: str) -> str:
    content = """
<section class="page-intro"><span>About the archive</span><h1>Designed for inspection and independence.</h1><p>ARR is an open, curated archive for research published with the files and evidence needed to understand how each result was produced and checked.</p></section>
<section class="about-grid">
  <article><h2>What ARR is</h2><p>A versioned archive of source-first preprints, code, formalizations, data descriptions and explicit verification records.</p></article>
  <article><h2>What ARR is not</h2><p>ARR is not a journal, a replacement for expert peer review, a ranking of authors or a guarantee that a scientific claim is true.</p></article>
  <article><h2>Governance</h2><p>The prototype begins with a documented editorial process. Founder conflicts, authorship and future independent governance will be disclosed publicly.</p></article>
  <article><h2>Preservation</h2><p>Stable identifiers are independent of GitHub. Versioned releases distribute generated and large files; future object storage and independent preservation mirrors can replace any provider without changing citations.</p></article>
  <article><h2>Submissions</h2><p>External submissions are currently closed. GitHub issues and pull requests are not manuscript submission channels; ARR will announce intake only after privacy, security, moderation and deposit controls are operational.</p></article>
</section>
"""
    canonical = f"{canonical_url}/about/" if canonical_url else ""
    return page_shell(title="About — ARR", description="About the Archive for Rigorous Research.", content=content, base=base, canonical=canonical)


def build_licensing(base: str, canonical_url: str) -> str:
    content = """
<section class="page-intro"><span>Open by scope</span><h1>Licenses follow the material.</h1><p>ARR does not apply one ambiguous license to software, papers, metadata and data. Every scope is declared explicitly and deposited records retain their own licensing information.</p></section>
<section class="about-grid">
  <article><h2>Platform software</h2><p><strong>AGPL-3.0-or-later.</strong> Modified network deployments must offer their corresponding source under the license terms.</p></article>
  <article><h2>Catalogue and schemas</h2><p><strong>CC0-1.0.</strong> Public metadata and machine contracts can be indexed, mirrored and implemented without permission friction.</p></article>
  <article><h2>ARR documentation</h2><p><strong>CC-BY-4.0.</strong> Policies, protocols and templates may be reused with attribution unless a file says otherwise.</p></article>
  <article><h2>Deposited research</h2><p>Each record declares separate manuscript, code and data licenses in <code>LICENSES.json</code>. Depositors retain copyright unless expressly transferred.</p></article>
  <article><h2>Name and endorsement</h2><p>Open licenses do not grant trademark rights or permission to imply that ARR endorses a modified archive, paper or service.</p></article>
</section>
"""
    canonical = f"{canonical_url}/licensing/" if canonical_url else ""
    return page_shell(title="Licensing — ARR", description="Licensing scopes for ARR software, metadata, documentation and deposited research.", content=content, base=base, canonical=canonical)


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def write_catalogue_exports(papers: list) -> None:
    catalogue = [paper.metadata for paper in papers]
    write(OUTPUT_DIR / "catalog.json", json.dumps(catalogue, ensure_ascii=False, indent=2) + "\n")
    write(OUTPUT_DIR / "catalog.ndjson", "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in catalogue))

    partitions: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for item in catalogue:
        _, year, suffix = item["id"].split("-", 2)
        partitions[(year, suffix[:2])].append(item)

    partition_index = []
    for (year, shard), records in sorted(partitions.items()):
        relative_path = f"catalog/{year}/{shard}.ndjson"
        write(OUTPUT_DIR / relative_path, "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records))
        partition_index.append({"year": year, "shard": shard, "records": len(records), "path": relative_path})
    write(
        OUTPUT_DIR / "catalog" / "index.json",
        json.dumps(
            {
                "schema_version": "1.0",
                "license": "CC0-1.0",
                "records": len(catalogue),
                "partitions": partition_index,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )


def write_sitemaps(papers: list, canonical_url: str) -> None:
    if not canonical_url:
        return
    urls = [f"{canonical_url}/", f"{canonical_url}/papers/", f"{canonical_url}/protocol/", f"{canonical_url}/licensing/", f"{canonical_url}/about/"]
    urls.extend(f"{canonical_url}/papers/{paper.id}/" for paper in papers)
    chunks = [urls[index : index + 10_000] for index in range(0, len(urls), 10_000)]
    if len(chunks) == 1:
        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{esc(url)}</loc></url>\n" for url in chunks[0]) + "</urlset>\n"
        write(OUTPUT_DIR / "sitemap.xml", sitemap)
        return

    sitemap_links = []
    for number, chunk in enumerate(chunks, start=1):
        filename = f"sitemaps/sitemap-{number:05d}.xml"
        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{esc(url)}</loc></url>\n" for url in chunk) + "</urlset>\n"
        write(OUTPUT_DIR / filename, sitemap)
        sitemap_links.append(f"  <sitemap><loc>{esc(canonical_url + '/' + filename)}</loc></sitemap>\n")
    index = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(sitemap_links) + "</sitemapindex>\n"
    write(OUTPUT_DIR / "sitemap.xml", index)


def main() -> int:
    args = parse_args()
    base = clean_base_path(args.base_path)
    canonical_url = args.canonical_url.rstrip("/")
    papers = discover_papers()
    failures = validate_collection(papers)
    if failures:
        print("Cannot build site: paper validation failed.", file=sys.stderr)
        for path, errors in failures.items():
            for error in errors:
                print(f"{path}: {error}", file=sys.stderr)
        return 1

    papers.sort(key=lambda paper: (paper.metadata["date"], paper.id), reverse=True)
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    (OUTPUT_DIR / "assets").mkdir(parents=True)
    (OUTPUT_DIR / "schema").mkdir(parents=True)
    shutil.copy2(SITE_DIR / "style.css", OUTPUT_DIR / "assets" / "style.css")
    shutil.copy2(ROOT / "schema" / "paper.schema.json", OUTPUT_DIR / "schema" / "paper.schema.json")
    shutil.copy2(ROOT / "schema" / "submission-receipt.schema.json", OUTPUT_DIR / "schema" / "submission-receipt.schema.json")
    shutil.copy2(ROOT / "schema" / "registry-event.schema.json", OUTPUT_DIR / "schema" / "registry-event.schema.json")

    write(OUTPUT_DIR / "index.html", build_home(papers, base, canonical_url))
    write(OUTPUT_DIR / "papers" / "index.html", build_papers_index(papers, base, canonical_url))
    write(OUTPUT_DIR / "protocol" / "index.html", build_protocol(base, canonical_url))
    write(OUTPUT_DIR / "licensing" / "index.html", build_licensing(base, canonical_url))
    write(OUTPUT_DIR / "about" / "index.html", build_about(base, canonical_url))
    for paper in papers:
        write(OUTPUT_DIR / "papers" / paper.id / "index.html", build_paper_page(paper, base, canonical_url, args.repository))

    write_catalogue_exports(papers)
    write(OUTPUT_DIR / "robots.txt", "User-agent: *\nAllow: /\n" + (f"Sitemap: {canonical_url}/sitemap.xml\n" if canonical_url else ""))
    write_sitemaps(papers, canonical_url)

    print(f"Built ARR site with {len(papers)} paper(s) at {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
