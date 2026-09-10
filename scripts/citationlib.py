# SPDX-License-Identifier: AGPL-3.0-or-later
"""Version-specific reference exports; no inferred journal, DOI or author names."""
from __future__ import annotations

import json
from urllib.parse import quote


def version_path(metadata: dict) -> str:
    route = "notes" if metadata.get("record_type") == "technical_note" else "papers"
    return f"/{route}/{quote(metadata['id'])}/versions/{quote(metadata['version'])}/"


def single_line(value: str) -> str:
    return " ".join(str(value).split())


def bib_escape(value: str) -> str:
    replacements = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
                    "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_",
                    "$": r"\$", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replacements.get(char, char) for char in single_line(value))


def citation_exports(metadata: dict, site_root: str) -> dict[str, str]:
    url = site_root.rstrip("/") + version_path(metadata)
    authors = [single_line(author["name"]) for author in metadata["authors"]]
    date = metadata["date"]
    title = single_line(metadata["title"])
    genre = "Archived manuscript" if metadata.get("archival_source") else "Research preprint"
    if metadata.get("record_type") == "technical_note":
        genre = "Technical note"
    note = f"{genre}; {metadata['id']} {metadata['version']}. Not peer reviewed by AIRR."
    if metadata.get("status") == "working_paper":
        note += " Working paper; not admitted to the AIRR accepted collection."
    elif metadata.get("status") == "withdrawn":
        note += " Withdrawn."
    elif metadata.get("status") == "archived":
        note += " Historical import; not assessed by AIRR."
    text = f"{'; '.join(authors)} ({date[:4]}). {title}. AIRR.SCIENCE, {metadata['id']}, {metadata['version']}. {url}"
    if metadata.get("doi"):
        text += f" DOI: {metadata['doi']}."
    if metadata.get("status") in {"working_paper", "withdrawn", "archived"}:
        text += " " + note

    fields = [
        ("author", " and ".join(bib_escape(author) for author in authors)),
        ("title", "{" + bib_escape(title) + "}"),
        ("year", date[:4]),
        ("howpublished", "AIRR.SCIENCE"),
        ("note", bib_escape(note)),
        ("url", url),
    ]
    if metadata.get("doi"):
        fields.append(("doi", bib_escape(metadata["doi"])))
    bib = f"@misc{{{metadata['id']}-{metadata['version']},\n" + ",\n".join(
        f"  {key} = {{{value}}}" for key, value in fields
    ) + "\n}\n"

    ris_fields = [("TY", "UNPB"), ("ID", f"{metadata['id']}-{metadata['version']}"),
                  ("TI", title), *[("AU", name) for name in authors],
                  ("PY", date[:4]), ("DA", date.replace("-", "/")),
                  ("PB", "AIRR.SCIENCE"), ("UR", url), ("N1", note),
                  ("AB", single_line(metadata["abstract"]))]
    if metadata.get("doi"):
        ris_fields.append(("DO", metadata["doi"]))
    ris = "\n".join(f"{key}  - {single_line(value)}" for key, value in ris_fields) + "\nER  - \n"
    csl = {
        "id": f"{metadata['id']}-{metadata['version']}", "type": "article",
        "title": title, "author": [{"literal": name} for name in authors],
        "issued": {"date-parts": [[int(part) for part in date.split("-")]]},
        "publisher": "AIRR.SCIENCE", "archive": "AIRR.SCIENCE",
        "archive_location": metadata["id"], "version": metadata["version"],
        "genre": genre, "URL": url, "note": note, "abstract": metadata["abstract"],
    }
    if metadata.get("doi"):
        csl["DOI"] = metadata["doi"]
    return {"txt": text + "\n", "bib": bib, "ris": ris,
            "csl.json": json.dumps([csl], ensure_ascii=False, indent=2) + "\n"}
