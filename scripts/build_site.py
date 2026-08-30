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

from arrlib import (
    ROOT,
    discover_papers,
    group_paper_versions,
    load_record_timestamps,
    parse_exact_timestamp,
    validate_collection,
    validate_record_timestamps,
)


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


def exact_time(value: str) -> str:
    parsed = parse_exact_timestamp(value)
    offset = parsed.strftime("%z")
    zone = "UTC" if offset == "+0000" else f"UTC{offset[:3]}:{offset[3:]}"
    label = f"{parsed:%Y-%m-%d %H:%M:%S} {zone}"
    return f'<time datetime="{esc(value)}">{esc(label)}</time>'


def timestamp_panel(timestamp: dict) -> str:
    if timestamp["publication_state"] == "pending":
        publication = "<div><span>Publication</span><strong>Pending release</strong><small>The exact release timestamp will be appended after publication</small></div>"
    else:
        publication = f"<div><span>Published</span><strong>{exact_time(timestamp['published_at'])}</strong><small>GitHub release · tag {esc(timestamp['release_tag'])}</small></div>"
    return f"""
  <section class="timestamp-panel" aria-label="Record timestamps">
    <div><span>Deposit recorded</span><strong>{exact_time(timestamp['deposit_recorded_at'])}</strong><small>First repository commit · full Git SHA recorded</small></div>
    {publication}
  </section>"""


def chronology_time(timestamp: dict) -> str:
    return timestamp.get("published_at", timestamp["deposit_recorded_at"])


def page_shell(*, title: str, description: str, content: str, base: str, canonical: str = "", head_extra: str = "") -> str:
    canonical_tag = f'<link rel="canonical" href="{esc(canonical)}">' if canonical else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0b0f17">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  {canonical_tag}
  {head_extra}
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
      <a href="{base}/notes/">Technical notes</a>
      <a href="{base}/protocol/">Protocol</a>
      <a href="{base}/submit/">Submit</a>
      <a href="{base}/licensing/">Licensing</a>
      <a href="{base}/about/">About</a>
    </nav>
  </header>
  <main id="main">{content}</main>
  <footer>
    <p><strong>ARR</strong> is a curated archive of research papers and technical notes with explicit evidence labels. Acceptance is not peer review and is not a guarantee of truth.</p>
    <p><a href="{base}/catalog.json">Machine-readable catalogue (CC0)</a> · <a href="{base}/registry/record-timestamps.json">Exact record timestamps (CC0)</a> · <a href="{base}/catalog/index.json">Partition index</a> · <a href="{base}/protocol/">Verification protocol</a> · <a href="{base}/privacy/">Privacy</a> · <a href="{base}/terms/">Deposit terms</a> · <a href="{base}/contact/">Contact and complaints</a> · <a href="https://github.com/arr-research/arr-research.github.io">Source (AGPL)</a></p>
  </footer>
</body>
</html>
"""


def status_badge(value: str) -> str:
    labels = {"accepted": "Accepted", "corrected": "Corrected", "withdrawn": "Withdrawn"}
    return f'<span class="badge badge-{esc(value)}">{esc(labels.get(value, value.title()))}</span>'


def record_type(metadata: dict) -> str:
    # Schema 1.0 contains research papers only; 1.1 makes the type explicit.
    return metadata.get("record_type", "research_paper")


def record_type_label(metadata: dict) -> str:
    return "Technical note" if record_type(metadata) == "technical_note" else "Research paper"


def record_route(metadata: dict) -> str:
    return "notes" if record_type(metadata) == "technical_note" else "papers"


def type_badge(metadata: dict) -> str:
    value = record_type(metadata)
    return f'<span class="badge badge-{esc(value.replace("_", "-"))}">{esc(record_type_label(metadata))}</span>'


def release_asset_url(release_url: str, filename: str) -> str:
    marker = "/releases/tag/"
    if marker not in release_url:
        return ""
    prefix, tag = release_url.split(marker, 1)
    return f"{prefix}/releases/download/{tag}/{quote(filename)}"


def scholarly_head(metadata: dict, *, canonical: str, release_url: str = "", pdf_url: str = "") -> str:
    """Emit discovery metadata for scholarly crawlers and general web/AI search."""
    authors = [author["name"] for author in metadata["authors"]]
    keywords = metadata.get("keywords", [])
    meta: list[tuple[str, object]] = [
        ("citation_title", metadata["title"]),
        *[("citation_author", author) for author in authors],
        ("citation_publication_date", metadata["date"]),
        ("citation_online_date", metadata["date"]),
        ("citation_abstract_html_url", canonical),
        ("citation_technical_report_institution", "ARR — Archive for Rigorous Research"),
        ("citation_technical_report_number", f"{metadata['id']} {metadata['version']}"),
        ("citation_language", "en"),
        ("DC.title", metadata["title"]),
        *[("DC.creator", author) for author in authors],
        ("DC.date", metadata["date"]),
        ("DC.identifier", canonical),
        ("DC.type", "Text"),
        ("DC.language", "en"),
        ("DC.rights", metadata["licenses"]["manuscript"]),
        ("DCTERMS.abstract", metadata["abstract"]),
    ]
    if keywords:
        meta.append(("citation_keywords", "; ".join(keywords)))
        meta.append(("DC.subject", "; ".join(keywords)))
    if pdf_url:
        meta.append(("citation_pdf_url", pdf_url))
    meta_tags = "\n  ".join(f'<meta name="{esc(name)}" content="{esc(value)}">' for name, value in meta)

    article_type = "TechArticle" if record_type(metadata) == "technical_note" else "ScholarlyArticle"
    structured: dict[str, object] = {
        "@context": "https://schema.org",
        "@type": article_type,
        "headline": metadata["title"],
        "name": metadata["title"],
        "description": metadata["abstract"],
        "abstract": metadata["abstract"],
        "author": [{"@type": "Person", "name": author} for author in authors],
        "datePublished": metadata["date"],
        "dateModified": metadata["date"],
        "inLanguage": "en",
        "keywords": keywords,
        "identifier": [metadata["id"], metadata["record_id"], metadata["version_id"]],
        "url": canonical,
        "version": metadata["version"],
        "isAccessibleForFree": True,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "publisher": {
            "@type": "Organization",
            "name": "ARR — Archive for Rigorous Research",
            "url": "https://arr-research.github.io/",
        },
    }
    if release_url:
        structured["sameAs"] = release_url
    if pdf_url:
        structured["encoding"] = {
            "@type": "MediaObject",
            "contentUrl": pdf_url,
            "encodingFormat": "application/pdf",
        }
    structured_json = json.dumps(structured, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    social_tags = "\n  ".join(
        [
            '<meta property="og:type" content="article">',
            f'<meta property="og:title" content="{esc(metadata["title"])}">',
            f'<meta property="og:description" content="{esc(metadata["abstract"])}">',
            f'<meta property="og:url" content="{esc(canonical)}">',
            f'<meta property="article:published_time" content="{esc(metadata["date"])}">',
            '<meta name="twitter:card" content="summary">',
            f'<meta name="twitter:title" content="{esc(metadata["title"])}">',
            f'<meta name="twitter:description" content="{esc(metadata["abstract"])}">',
        ]
    )
    return f'{meta_tags}\n  {social_tags}\n  <script type="application/ld+json">{structured_json}</script>'


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


def paper_card(metadata: dict, timestamp: dict, base: str) -> str:
    authors = ", ".join(author["name"] for author in metadata["authors"])
    chronology_label = "Published" if timestamp["publication_state"] == "published" else "Deposit recorded"
    return f"""
<article class="paper-card">
  <div class="paper-meta">{type_badge(metadata)}{status_badge(metadata['status'])}<span>{esc(metadata['id'])} · {esc(metadata['version'])}</span></div>
  <h3><a href="{base}/{record_route(metadata)}/{quote(metadata['id'])}/">{esc(metadata['title'])}</a></h3>
  <p class="authors">{esc(authors)}</p>
  <p>{esc(metadata['abstract'])}</p>
  <div class="paper-foot"><span>{chronology_label} {exact_time(chronology_time(timestamp))}</span><span>Protocol {esc(metadata['verification']['protocol'])}</span></div>
</article>"""


def build_home(papers: list, timestamps: dict, base: str, canonical_url: str) -> str:
    accepted_papers = sum(p.metadata["status"] != "withdrawn" and p.record_type == "research_paper" for p in papers)
    accepted_notes = sum(p.metadata["status"] != "withdrawn" and p.record_type == "technical_note" for p in papers)
    recent = "".join(paper_card(p.metadata, timestamps[(p.id, p.version)], base) for p in papers[:6])
    if not recent:
        recent = """
<section class="empty-state">
  <span>Prototype phase</span>
  <h2>The archive is being prepared.</h2>
  <p>No research record will appear here until its sources, provenance and verification record have completed the ARR acceptance workflow.</p>
</section>"""
    content = f"""
<section class="hero">
  <div class="eyebrow">Open · Curated · Reproducible</div>
  <h1>Research should arrive with its evidence.</h1>
  <p class="lede">ARR publishes inspectable research papers and technical notes with machine-readable renditions and explicit verification evidence. Every record keeps its manuscript, code, provenance, version, licenses and checks.</p>
  <div class="hero-actions"><a class="button" href="{base}/papers/">Browse papers</a><a class="button secondary" href="{base}/notes/">Browse technical notes</a><a class="text-link" href="{base}/protocol/">Read the protocol →</a></div>
</section>
<section class="stats" aria-label="Archive statistics">
  <div><strong>{accepted_papers}</strong><span>research papers</span></div>
  <div><strong>{accepted_notes}</strong><span>technical notes</span></div>
  <div><strong>100%</strong><span>machine-readable rendition</span></div>
</section>
<section class="principles">
  <div><span>01</span><h2>Inspectable by default</h2><p>Manuscripts, metadata and code remain readable as plain files—not trapped behind a PDF or proprietary interface.</p></div>
  <div><span>02</span><h2>Claims match checks</h2><p>ARR reports pass, partial and not-assessed results exactly as recorded. It does not turn screening into a claim of truth.</p></div>
  <div><span>03</span><h2>History remains visible</h2><p>Published versions are identified by hashes and releases. Corrections create a new immutable version rather than silently rewriting the past.</p></div>
</section>
<section class="recent"><div class="section-heading"><div><span>Catalogue</span><h2>Latest accepted research</h2></div><a href="{base}/papers/">View papers</a></div>{recent}</section>
"""
    canonical = f"{canonical_url}/" if canonical_url else ""
    return page_shell(title="ARR — Archive for Rigorous Research", description="A curated, machine-readable archive of research preprints with explicit evidence labels.", content=content, base=base, canonical=canonical)


def build_papers_index(papers: list, timestamps: dict, base: str, canonical_url: str) -> str:
    research_papers = [paper for paper in papers if paper.record_type == "research_paper"]
    cards = "".join(paper_card(p.metadata, timestamps[(p.id, p.version)], base) for p in research_papers)
    if not cards:
        cards = '<section class="empty-state compact"><h2>No accepted papers yet.</h2><p>The public catalogue begins only after the first candidate completes the ARR workflow.</p></section>'
    content = f"""
<section class="page-intro"><span>Public catalogue</span><h1>Accepted papers</h1><p>Each record corresponds to an explicit version and provides machine-readable sources, provenance and verification status.</p></section>
<section class="catalogue">{cards}</section>
"""
    canonical = f"{canonical_url}/papers/" if canonical_url else ""
    return page_shell(title="Papers — ARR", description="Accepted ARR research papers.", content=content, base=base, canonical=canonical)


def build_notes_index(papers: list, timestamps: dict, base: str, canonical_url: str) -> str:
    notes = [paper for paper in papers if paper.record_type == "technical_note"]
    cards = "".join(paper_card(note.metadata, timestamps[(note.id, note.version)], base) for note in notes)
    if not cards:
        cards = '<section class="empty-state compact"><h2>No technical notes yet.</h2><p>This collection begins when the first concise, rigorous and machine-readable technical contribution completes the ARR workflow.</p></section>'
    content = f"""
<section class="page-intro"><span>ARR Technical Notes</span><h1>Technical notes</h1><p>Concise research communications with a precise contribution, explicit scope and limitations, machine-readable sources, provenance and evidence-specific verification labels.</p></section>
<section class="catalogue">{cards}</section>
"""
    canonical = f"{canonical_url}/notes/" if canonical_url else ""
    return page_shell(title="Technical notes — ARR", description="Rigorous, machine-readable ARR technical notes.", content=content, base=base, canonical=canonical)


def build_paper_page(
    paper,
    timestamp: dict,
    incoming_relations: list[dict],
    record_routes: dict[str, str],
    version_timestamps: list[dict],
    source_versions: dict[str, object],
    latest_version: str,
    permanent_version_page: bool,
    base: str,
    canonical_url: str,
    repository: str,
) -> str:
    metadata = paper.metadata
    authors = ", ".join(author["name"] for author in metadata["authors"])
    relative_path = paper.path.relative_to(ROOT).as_posix()
    tag = f"{metadata['id']}-{metadata['version']}"
    release_url = metadata.get("release_url")
    if not release_url and repository:
        release_url = f"https://github.com/{repository}/releases/tag/{tag}"
    source_url = f"https://github.com/{repository}/tree/main/{relative_path}" if repository else ""
    pdf_url = ""
    if release_url and (paper.path / "paper.pdf").is_file():
        pdf_url = release_asset_url(release_url, f"{tag}.pdf")
    links = []
    if pdf_url:
        links.append(f'<a class="button" href="{esc(pdf_url)}">Download canonical PDF</a>')
    if release_url:
        links.append(f'<a class="button secondary" href="{esc(release_url)}">Download release assets</a>')
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
    relationships = list(metadata.get("related_records", [])) + incoming_relations
    related_records = "".join(
        f'<li><a href="{base}/{record_routes.get(item["id"], "papers")}/{quote(item["id"])}/"><strong>{esc(item["id"])}</strong></a><span>{esc(item["relationship"].replace("_", " ").title())} · {esc(item["note"])}</span></li>'
        for item in relationships
    )
    related_section = (
        f'<section class="related-records"><h2>Related ARR records</h2><ul>{related_records}</ul></section>'
        if related_records
        else ""
    )
    route = record_route(metadata)
    root_url = f"{base}/{route}/{quote(metadata['id'])}/"
    history_items = []
    for entry in sorted(version_timestamps, key=lambda item: int(item["version"][1:]), reverse=True):
        version = entry["version"]
        source_available = version in source_versions
        if version == latest_version:
            target = root_url
        elif source_available:
            target = f"{root_url}versions/{quote(version)}/"
        elif entry.get("publication_state") == "published" and repository:
            target = f"https://github.com/{repository}/releases/tag/{quote(entry['release_tag'])}"
        else:
            target = ""
        label = f'<a href="{esc(target)}"><strong>{esc(version)}</strong></a>' if target else f"<strong>{esc(version)}</strong>"
        source_note = "source snapshot available" if source_available else "release archive"
        source_record = source_versions.get(version)
        revision = source_record.metadata.get("revision") if source_record is not None else None
        if isinstance(revision, dict):
            source_note = f"{revision['change_size']} revision · {source_note}"
        current = " · viewing" if version == metadata["version"] else ""
        history_items.append(
            f'<li>{label}<span>{exact_time(chronology_time(entry))} · {esc(source_note + current)}</span></li>'
        )
    version_history = (
        '<section class="version-history"><h2>Version history</h2><p>The ARR identifier remains stable. Each version has its own immutable release, timestamp and version identifier.</p><ul>'
        + "".join(history_items)
        + "</ul></section>"
    )
    revision = metadata.get("revision")
    revision_section = ""
    if isinstance(revision, dict):
        revision_section = (
            f'<section class="revision-note"><h2>Revision statement</h2><p><strong>{esc(revision["change_size"].title())} revision.</strong> {esc(revision["summary"])}</p></section>'
        )
    version_notice = ""
    if permanent_version_page:
        latest_link = f'<a href="{root_url}">{esc(latest_version)}</a>'
        version_notice = (
            f'<aside class="version-notice">Permanent snapshot for <strong>{esc(metadata["version"])}</strong>. '
            f'The current record page points to {latest_link}.</aside>'
        )
    summary_label = "Summary" if paper.record_type == "technical_note" else "Abstract"
    note_profile = metadata.get("technical_note", {})
    note_section = ""
    if paper.record_type == "technical_note":
        note_section = f"""
  <section class="note-scope"><h2>Technical-note scope</h2><dl class="record"><div><dt>Kind</dt><dd>{esc(note_profile['kind'].replace('_', ' ').title())}</dd></div><div><dt>Maturity</dt><dd>{esc(note_profile['maturity'].replace('_', ' ').title())}</dd></div></dl><h3>Contribution boundary</h3><p>{esc(note_profile['scope_statement'])}</p><h3>Limitations</h3><p>{esc(note_profile['limitations'])}</p></section>
"""
    content = f"""
<article class="paper-page">
  {version_notice}
  <div class="paper-meta">{type_badge(metadata)}{status_badge(metadata['status'])}<span>{esc(metadata['id'])} · {esc(metadata['version'])} · {esc(metadata['date'])}</span></div>
  <h1>{esc(metadata['title'])}</h1>
  <p class="paper-authors">{esc(authors)}</p>
  {timestamp_panel(timestamp)}
  <div class="download-row">{''.join(links)}</div>
  <section class="abstract"><span>{summary_label}</span><p>{esc(metadata['abstract'])}</p></section>
  <div class="paper-grid">
    <section><h2>Verification record</h2><dl class="checks">{verification_rows(metadata)}</dl><p class="protocol-note">Recorded under <a href="{base}/protocol/">{esc(metadata['verification']['protocol'])}</a>. ARR verification and screening are not peer review.</p></section>
    <aside><h2>Record</h2><dl class="record"><div><dt>Record type</dt><dd>{esc(record_type_label(metadata))}</dd></div><div><dt>Manuscript license</dt><dd>{esc(metadata['licenses']['manuscript'])}</dd></div><div><dt>Metadata license</dt><dd>{esc(metadata['licenses']['metadata'])}</dd></div><div><dt>Canonical source</dt><dd>{esc(metadata['source_of_truth'])}</dd></div><div><dt>Canonical SHA-256</dt><dd><code>{esc(metadata['integrity'].get('canonical_sha256', 'recorded in release manifest'))}</code></dd></div><div><dt>Stable record</dt><dd>{esc(metadata['record_id'])}</dd></div><div><dt>Version identifier</dt><dd>{esc(metadata['version_id'])}</dd></div><div><dt>AI assistance</dt><dd>{'Declared' if metadata['ai_assistance']['used'] else 'Not used'}</dd></div></dl><ul class="keywords">{keywords}</ul></aside>
  </div>
  {revision_section}
  {version_history}
  {note_section}
  {related_section}
  <section class="disclosure"><h2>AI assistance statement</h2><p>{esc(metadata['ai_assistance']['statement'])}</p></section>
  <section class="screening-record"><h2>Frontier-model screening</h2><p>Status: <strong>{esc(metadata['screening']['status'])}</strong>. Any listed reports correspond to this exact version under {esc(metadata['screening']['protocol'])}; no absent assessment is represented as a pass.</p><ul>{evaluators}</ul></section>
  <section class="disclosure"><h2>Editorial disclosure</h2><p>{esc(metadata['editorial']['statement'])}</p></section>
</article>
"""
    if canonical_url:
        root_canonical = f"{canonical_url}/{route}/{metadata['id']}/"
        canonical = f"{root_canonical}versions/{metadata['version']}/" if permanent_version_page else root_canonical
    else:
        canonical = ""
    return page_shell(
        title=f"{metadata['title']} — ARR",
        description=metadata["abstract"],
        content=content,
        base=base,
        canonical=canonical,
        head_extra=scholarly_head(metadata, canonical=canonical, release_url=release_url or "", pdf_url=pdf_url),
    )


def build_protocol(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>ARR-SCREEN-1.0</span><h1>A visible standard, not a black box.</h1><p>ARR guarantees that its stated process was applied to the identified version. It does not certify universal truth, novelty or importance.</p></section>
<section class="protocol-steps">
  <article><span>Gate 1</span><h2>Complete research object</h2><p>Required sources, metadata, provenance, licenses and stable identifiers must be present and internally consistent. Technical notes additionally declare their precise scope, maturity, kind and limitations.</p></article>
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
  <article><h2>What ARR is</h2><p>A versioned archive of research papers and concise technical notes, with canonical manuscripts, machine-readable renditions, code, formalizations, data descriptions and explicit verification records.</p></article>
  <article><h2>Two publication types</h2><p>Research papers present complete scholarly arguments at paper scale. Technical notes preserve narrower but rigorous results, proofs, formalizations, methods, replications, negative results, software or protocols. A note is different in scope, not exempt from evidence or integrity requirements.</p></article>
  <article><h2>What ARR is not</h2><p>ARR is not a journal, a replacement for expert peer review, a ranking of authors or a guarantee that a scientific claim is true.</p></article>
  <article><h2>Governance</h2><p>Lluis Eriksson is founder, registry operator, responsible editor and data controller. Every decision is human. His conflicted or author-owned work requires a disclosed independent editor before publication.</p></article>
  <article><h2>Preservation</h2><p>Stable identifiers are independent of GitHub. Versioned releases distribute generated and large files; future object storage and independent preservation mirrors can replace any provider without changing citations.</p></article>
  <article><h2>Submissions</h2><p>ARR does not currently charge a submission or publication fee. Expressions of interest are open without attachments; manuscript uploads are private, invitation-only and cannot begin until the production launch checklist is signed. GitHub and ordinary email are never manuscript channels.</p></article>
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


def policy_source(filename: str) -> str:
    return f"https://github.com/arr-research/arr-research.github.io/blob/main/docs/{filename}"


def build_submit(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>Currently no fee · invitation-only pilot</span><h1>Every paper enters privately and every decision is manual.</h1><p>ARR does not currently charge for submission, assessment, publication or withdrawal. Fees may be introduced for future submissions only after advance notice and updated terms. Uploading never publishes a manuscript.</p></section>
<section class="about-grid">
  <article><h2>1. Request an invitation</h2><p>Email <a href="mailto:lluiseriksson@gmail.com?subject=ARR%20invitation">lluiseriksson@gmail.com</a> with subject <code>ARR invitation</code>. Include only your name, email, field and provisional title. <strong>Do not attach a manuscript or abstract.</strong></p></article>
  <article><h2>2. Private quarantine</h2><p>After the production gate is complete, selected applicants receive a one-use, email-bound link. The PDF is authenticated, rate-limited, size/type checked, quarantined and unavailable to editors unless an approved malware scanner reports it clean.</p></article>
  <article><h2>3. Human decision</h2><p>Lluis Eriksson reviews ordinary cases one by one and records accept, decline or changes requested with a concise basis. No algorithm publishes or rejects a paper. A founder conflict requires an independent editor.</p></article>
  <article><h2>Current boundary</h2><p>Expressions of interest are open. Live upload credentials are not issued until legal review, a stable service address, named processors, HTTPS, ClamAV, backups, retention jobs and incident testing have been signed off. This protects authors from a premature opening.</p></article>
</section>
<section class="callout"><h2>Read before requesting access</h2><p><a href="{base}/terms/">Deposit terms</a> · <a href="{base}/privacy/">Privacy</a> · <a href="{base}/governance/">Governance</a> · <a href="{base}/contact/">Complaints and legal notices</a></p></section>
"""
    canonical = f"{canonical_url}/submit/" if canonical_url else ""
    return page_shell(title="Submit — ARR", description="Free invitation-only manuscript intake with private quarantine and manual editorial decisions.", content=content, base=base, canonical=canonical)


def build_privacy(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>ARR-PRIVACY-1.0 · effective 2026-08-30</span><h1>Privacy is separated from publication.</h1><p>The controller is Lluis Eriksson, a natural person in Stockholm, Sweden, acting as founder, registry operator and responsible editor. Contact: <a href="mailto:lluiseriksson@gmail.com?subject=ARR%20privacy">lluiseriksson@gmail.com</a>. No DPO is designated.</p></section>
<section class="about-grid">
  <article><h2>Private data</h2><p>ARR processes invitation/account details, submission metadata and PDF, declarations, decisions, correspondence and pseudonymized security events to administer the deposit agreement and protect the service. Accounts are restricted to adults in the pilot.</p></article>
  <article><h2>No automated editorial decision</h2><p>Format and malware controls may keep a file quarantined. Acceptance or rejection is human. Private manuscripts are never sent to an AI provider by default; a named-provider notice and reconfirmed optional consent are required first.</p></article>
  <article><h2>Retention</h2><p>Malware bytes are erased immediately, withdrawn PDFs after 7 days, declined PDFs after 30 days, and accepted private copies 30 days after verified public release. A minimal decision record is retained for three years, subject to narrowly reviewed legal hold.</p></article>
  <article><h2>Your rights</h2><p>Applicable rights include access, correction, erasure, restriction, portability and objection. You can complain to Sweden's IMY or another competent EEA authority. Requests receive proportionate identity verification.</p></article>
</section>
<section class="callout"><h2>Complete binding notice</h2><p><a href="{policy_source('PRIVACY_NOTICE.md')}">Read ARR-PRIVACY-1.0 in full</a>. The accepted version is recorded with each deposit.</p></section>
"""
    canonical = f"{canonical_url}/privacy/" if canonical_url else ""
    return page_shell(title="Privacy — ARR", description="ARR-PRIVACY-1.0 privacy notice for private manuscript intake.", content=content, base=base, canonical=canonical)


def build_terms(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>ARR-DEPOSIT-1.1 · effective 2026-08-30</span><h1>There is currently no ARR deposit fee.</h1><p>ARR does not currently charge for submission, assessment, publication or withdrawal. A future fee may apply only after advance notice and new terms, never retroactively or in exchange for acceptance. The operator is Lluis Eriksson in Stockholm, Sweden.</p></section>
<section class="about-grid">
  <article><h2>Authority and scope</h2><p>Adult depositors must be an author, rights holder or authorized agent and accurately disclose rights, authorship, AI assistance, interests, third-party material, provenance and licenses. The pilot accepts one PDF up to 25 MiB.</p></article>
  <article><h2>Private first</h2><p>An upload enters quarantine and carries no public license. ARR may decline, request changes, restrict or remove material. Submission creates no entitlement to a timetable, publication, preservation or endorsement.</p></article>
  <article><h2>Publication rights</h2><p>Copyright remains with its owner. A final accepted version receives explicit scoped licenses before public release. Public copies and open licenses may be irreversible; withdrawal cannot recall third-party copies.</p></article>
  <article><h2>Appeal and conflict</h2><p>A decline or restriction may be appealed once within 30 days. A conflicted founder approval is provisional and an unconflicted independent editor must sign before publication.</p></article>
</section>
<section class="callout"><h2>Complete binding terms</h2><p><a href="{policy_source('DEPOSIT_TERMS.md')}">Read ARR-DEPOSIT-1.1 in full</a>. Email and GitHub issues are not deposit channels.</p></section>
"""
    canonical = f"{canonical_url}/terms/" if canonical_url else ""
    return page_shell(title="Deposit terms — ARR", description="ARR-DEPOSIT-1.1 terms for the currently fee-free invitation-only pilot.", content=content, base=base, canonical=canonical)


def build_governance(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>Human gate · disclosed conflicts</span><h1>The founder cannot be his own final editor.</h1><p>Lluis Eriksson is founder, registry operator, responsible editor and data controller. ARR does not use the company title VD/CEO while no such legal office exists.</p></section>
<section class="about-grid"><article><h2>Ordinary external case</h2><p>The operator records the exact version, checks and reason, then manually chooses accept, decline or changes requested. Acceptance still requires a separate public-release workflow.</p></article><article><h2>Founder or editor conflict</h2><p>Authorship, recent collaboration, supervision, close relationships, financial interests or disputes trigger recusal. An operator accept becomes provisional until a named independent editor signs.</p></article><article><h2>Appeal</h2><p>The original decision-maker cannot be the sole appeal reviewer. An unavailable independent reviewer means the case remains private or is declined without implying low quality.</p></article><article><h2>Transparency</h2><p>Public records disclose relevant founder relationships. Once the pilot has activity, ARR will report aggregate decisions, appeals, conflicts and reversals without exposing private submissions.</p></article></section>
<section class="callout"><h2>Full governance rules</h2><p><a href="{policy_source('GOVERNANCE.md')}">Read the version-controlled policy</a>.</p></section>
"""
    canonical = f"{canonical_url}/governance/" if canonical_url else ""
    return page_shell(title="Governance — ARR", description="ARR governance, manual editorial gate and founder conflict controls.", content=content, base=base, canonical=canonical)


def build_contact(base: str, canonical_url: str) -> str:
    content = f"""
<section class="page-intro"><span>Responsible operator and redress</span><h1>One accountable human contact.</h1><p>ARR is a non-commercial project operated by Lluis Eriksson, a natural person in Stockholm, Sweden: founder, registry operator, responsible editor and GDPR data controller.</p></section>
<section class="about-grid"><article><h2>Contact</h2><p><a href="mailto:lluiseriksson@gmail.com">lluiseriksson@gmail.com</a>. Use subject <code>ARR invitation</code>, <code>ARR appeal</code>, <code>ARR privacy</code>, <code>ARR copyright</code>, <code>ARR illegal-content notice</code> or <code>ARR security</code>. Never email manuscript attachments or live malware.</p></article><article><h2>Appeal</h2><p>Appeal once within 30 days with the case, challenged decision, alleged error and remedy. ARR aims to acknowledge within 7 days and decide within 30 days through someone other than the sole original decision-maker.</p></article><article><h2>Rights/illegality notice</h2><p>Identify yourself, the exact URL/version or case, the material and legal basis, supporting facts and requested action. ARR records the case, may restrict urgently, gives reasons and permits a substantiated counter-notice.</p></article><article><h2>Privacy regulator</h2><p>You may complain to the <a href="https://www.imy.se/en/individuals/forms-and-e-services/file-a-gdpr-complaint/">Swedish Authority for Privacy Protection (IMY)</a> or another competent EEA authority.</p></article></section>
<section class="callout"><h2>Complete procedure</h2><p><a href="{policy_source('LEGAL_AND_COMPLAINTS.md')}">Read legal contact, notices and complaints in full</a>. A stable postal service address remains a launch condition for unrestricted public intake.</p></section>
"""
    canonical = f"{canonical_url}/contact/" if canonical_url else ""
    return page_shell(title="Contact and complaints — ARR", description="ARR operator, legal contact, editorial appeal and notice procedure.", content=content, base=base, canonical=canonical)


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def write_catalogue_exports(papers: list, groups: dict, timestamps: dict) -> None:
    catalogue = []
    for paper in papers:
        item = dict(paper.metadata)
        item.setdefault("record_type", paper.record_type)
        source_versions = {version.version for version in groups[paper.id]}
        history = [entry for (paper_id, _), entry in timestamps.items() if paper_id == paper.id]
        history.sort(key=lambda entry: int(entry["version"][1:]))
        item["latest_version"] = paper.version
        item["version_count"] = len(history)
        item["versions"] = [
            {
                "version": entry["version"],
                "publication_state": entry["publication_state"],
                "release_tag": entry.get("release_tag"),
                "source_snapshot_available": entry["version"] in source_versions,
            }
            for entry in history
        ]
        catalogue.append(item)
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
                "versions": sum(item["version_count"] for item in catalogue),
                "partitions": partition_index,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )


def write_sitemaps(papers: list, groups: dict, canonical_url: str) -> None:
    if not canonical_url:
        return
    latest_date = max(paper.metadata["date"] for paper in papers)
    urls = [
        (f"{canonical_url}/", latest_date),
        (f"{canonical_url}/papers/", latest_date),
        (f"{canonical_url}/notes/", latest_date),
        (f"{canonical_url}/protocol/", latest_date),
        (f"{canonical_url}/submit/", latest_date),
        (f"{canonical_url}/licensing/", latest_date),
        (f"{canonical_url}/about/", latest_date),
        (f"{canonical_url}/privacy/", latest_date),
        (f"{canonical_url}/terms/", latest_date),
        (f"{canonical_url}/governance/", latest_date),
        (f"{canonical_url}/contact/", latest_date),
    ]
    urls.extend((f"{canonical_url}/{record_route(paper.metadata)}/{paper.id}/", paper.metadata["date"]) for paper in papers)
    for paper in papers:
        route = record_route(paper.metadata)
        urls.extend(
            (f"{canonical_url}/{route}/{paper.id}/versions/{version.version}/", version.metadata["date"])
            for version in groups[paper.id]
        )
    chunks = [urls[index : index + 10_000] for index in range(0, len(urls), 10_000)]
    if len(chunks) == 1:
        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{esc(url)}</loc><lastmod>{esc(date)}</lastmod></url>\n" for url, date in chunks[0]) + "</urlset>\n"
        write(OUTPUT_DIR / "sitemap.xml", sitemap)
        return

    sitemap_links = []
    for number, chunk in enumerate(chunks, start=1):
        filename = f"sitemaps/sitemap-{number:05d}.xml"
        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{esc(url)}</loc><lastmod>{esc(date)}</lastmod></url>\n" for url, date in chunk) + "</urlset>\n"
        write(OUTPUT_DIR / filename, sitemap)
        sitemap_links.append(f"  <sitemap><loc>{esc(canonical_url + '/' + filename)}</loc></sitemap>\n")
    index = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(sitemap_links) + "</sitemapindex>\n"
    write(OUTPUT_DIR / "sitemap.xml", index)


def write_llm_guides(papers: list, canonical_url: str) -> None:
    if not canonical_url:
        return
    intro = [
        "# ARR — Archive for Rigorous Research",
        "",
        "> Public, versioned research records with explicit provenance, integrity hashes, licensing, evidence labels, and machine-readable renditions.",
        "",
        "ARR pages and metadata may be crawled, indexed, quoted, and linked subject to each record's declared licenses. Acceptance is not peer review and is not a guarantee of truth.",
        "",
        "## Machine-readable resources",
        "",
        f"- [Catalogue JSON]({canonical_url}/catalog.json)",
        f"- [Catalogue NDJSON]({canonical_url}/catalog.ndjson)",
        f"- [Partition index]({canonical_url}/catalog/index.json)",
        f"- [Sitemap]({canonical_url}/sitemap.xml)",
        f"- [Verification protocol]({canonical_url}/protocol/)",
        "",
        "## Current records",
        "",
    ]
    records = [
        f"- [{paper.metadata['title']}]({canonical_url}/{record_route(paper.metadata)}/{paper.id}/) — {paper.id} {paper.version}"
        for paper in papers
    ]
    write(OUTPUT_DIR / "llms.txt", "\n".join(intro + records) + "\n")

    full = intro.copy()
    for paper in papers:
        full.extend(
            [
                f"### {paper.metadata['title']}",
                "",
                f"- Identifier: {paper.id} {paper.version}",
                f"- Authors: {', '.join(author['name'] for author in paper.metadata['authors'])}",
                f"- Date: {paper.metadata['date']}",
                f"- URL: {canonical_url}/{record_route(paper.metadata)}/{paper.id}/",
                f"- Abstract: {paper.metadata['abstract']}",
                "",
            ]
        )
    write(OUTPUT_DIR / "llms-full.txt", "\n".join(full) + "\n")


def main() -> int:
    args = parse_args()
    base = clean_base_path(args.base_path)
    canonical_url = args.canonical_url.rstrip("/")
    all_versions = discover_papers()
    failures = validate_collection(all_versions)
    timestamp_errors = validate_record_timestamps(all_versions)
    if failures or timestamp_errors:
        print("Cannot build site: record validation failed.", file=sys.stderr)
        for path, errors in failures.items():
            for error in errors:
                print(f"{path}: {error}", file=sys.stderr)
        for error in timestamp_errors:
            print(error, file=sys.stderr)
        return 1

    timestamps = load_record_timestamps()
    groups = group_paper_versions(all_versions)
    papers = [versions[-1] for versions in groups.values()]
    papers.sort(key=lambda paper: (chronology_time(timestamps[(paper.id, paper.version)]), paper.id), reverse=True)
    record_routes = {paper.id: record_route(paper.metadata) for paper in papers}
    incoming_relations: dict[str, list[dict]] = defaultdict(list)
    for source in papers:
        for relation in source.metadata.get("related_records", []):
            incoming_relations[relation["id"]].append(
                {
                    "id": source.id,
                    "relationship": "referenced_by",
                    "note": f"Linked from {source.metadata['title']}.",
                }
            )
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    (OUTPUT_DIR / "assets").mkdir(parents=True)
    (OUTPUT_DIR / "schema").mkdir(parents=True)
    shutil.copy2(SITE_DIR / "style.css", OUTPUT_DIR / "assets" / "style.css")
    shutil.copy2(SITE_DIR / "indexnow-key.txt", OUTPUT_DIR / "indexnow-key.txt")
    shutil.copy2(ROOT / "schema" / "paper.schema.json", OUTPUT_DIR / "schema" / "paper.schema.json")
    shutil.copy2(ROOT / "schema" / "submission-receipt.schema.json", OUTPUT_DIR / "schema" / "submission-receipt.schema.json")
    shutil.copy2(ROOT / "schema" / "registry-event.schema.json", OUTPUT_DIR / "schema" / "registry-event.schema.json")
    shutil.copy2(ROOT / "schema" / "record-timestamps.schema.json", OUTPUT_DIR / "schema" / "record-timestamps.schema.json")
    (OUTPUT_DIR / "registry").mkdir(parents=True)
    shutil.copy2(ROOT / "registry" / "record-timestamps.json", OUTPUT_DIR / "registry" / "record-timestamps.json")

    write(OUTPUT_DIR / "index.html", build_home(papers, timestamps, base, canonical_url))
    write(OUTPUT_DIR / "papers" / "index.html", build_papers_index(papers, timestamps, base, canonical_url))
    write(OUTPUT_DIR / "notes" / "index.html", build_notes_index(papers, timestamps, base, canonical_url))
    write(OUTPUT_DIR / "protocol" / "index.html", build_protocol(base, canonical_url))
    write(OUTPUT_DIR / "submit" / "index.html", build_submit(base, canonical_url))
    write(OUTPUT_DIR / "licensing" / "index.html", build_licensing(base, canonical_url))
    write(OUTPUT_DIR / "about" / "index.html", build_about(base, canonical_url))
    write(OUTPUT_DIR / "privacy" / "index.html", build_privacy(base, canonical_url))
    write(OUTPUT_DIR / "terms" / "index.html", build_terms(base, canonical_url))
    write(OUTPUT_DIR / "governance" / "index.html", build_governance(base, canonical_url))
    write(OUTPUT_DIR / "contact" / "index.html", build_contact(base, canonical_url))
    for paper in papers:
        version_timestamps = [entry for (paper_id, _), entry in timestamps.items() if paper_id == paper.id]
        source_versions = {version.version: version for version in groups[paper.id]}
        write(
            OUTPUT_DIR / record_route(paper.metadata) / paper.id / "index.html",
            build_paper_page(
                paper,
                timestamps[(paper.id, paper.version)],
                incoming_relations.get(paper.id, []),
                record_routes,
                version_timestamps,
                source_versions,
                paper.version,
                False,
                base,
                canonical_url,
                args.repository,
            ),
        )
        for version in groups[paper.id]:
            write(
                OUTPUT_DIR / record_route(paper.metadata) / paper.id / "versions" / version.version / "index.html",
                build_paper_page(
                    version,
                    timestamps[(version.id, version.version)],
                    incoming_relations.get(paper.id, []),
                    record_routes,
                    version_timestamps,
                    source_versions,
                    paper.version,
                    True,
                    base,
                    canonical_url,
                    args.repository,
                ),
            )

    write_catalogue_exports(papers, groups, timestamps)
    write(
        OUTPUT_DIR / "robots.txt",
        "User-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: *\nAllow: /\n"
        + (f"Sitemap: {canonical_url}/sitemap.xml\n" if canonical_url else ""),
    )
    write_sitemaps(papers, groups, canonical_url)
    write_llm_guides(papers, canonical_url)

    paper_count = sum(paper.record_type == "research_paper" for paper in papers)
    note_count = sum(paper.record_type == "technical_note" for paper in papers)
    print(
        f"Built ARR site with {paper_count} paper(s), {note_count} technical note(s), "
        f"and {len(timestamps)} published/pending version(s) at {OUTPUT_DIR}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
