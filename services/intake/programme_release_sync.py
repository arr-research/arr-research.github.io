# SPDX-License-Identifier: AGPL-3.0-or-later
"""Host-only readback of separately published sole-author programme working papers."""
import hashlib
import json
import re
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

import click
from werkzeug.exceptions import HTTPException

REPO = "arr-research/arr-research.github.io"
QUEUE = f"https://raw.githubusercontent.com/{REPO}/main/registry/programme-release-queue.json"
ALLOWED_HOSTS = {"api.github.com", "github.com", "raw.githubusercontent.com",
                 "release-assets.githubusercontent.com", "objects.githubusercontent.com", "airr.science"}
SHA = re.compile(r"[a-f0-9]{64}")
PAPER = re.compile(r"ARR-(20[0-9]{2})-([0-9A-HJKMNP-TV-Z]{16})")


def require(value, message):
    if not value:
        raise ValueError(message)


def allowed(url):
    parts = urlsplit(url)
    require(parts.scheme == "https" and parts.hostname in ALLOWED_HOSTS
            and parts.port in (443, None) and parts.username is None and parts.password is None,
            "Unexpected public evidence origin")


class OfficialRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        allowed(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url, limit):
    allowed(url)
    with build_opener(OfficialRedirects()).open(Request(url, headers={
            "User-Agent": "AIRR-programme-release-reconciliation"}), timeout=25) as response:
        require(response.status == 200, "Public evidence unavailable")
        data = response.read(limit + 1)
        require(0 < len(data) <= limit, "Unexpected evidence size")
        return data


def validate_entry(entry):
    fields = {"paper", "version", "submission", "sha256", "report_sha256", "month"}
    require(isinstance(entry, dict) and set(entry) == fields
            and all(isinstance(v, str) for v in entry.values()), "Malformed queue item")
    require(PAPER.fullmatch(entry["paper"]) and re.fullmatch(r"v[1-9][0-9]{0,4}", entry["version"])
            and re.fullmatch(r"SUB-[A-F0-9]{16}", entry["submission"])
            and re.fullmatch(r"0[1-9]|1[0-2]", entry["month"])
            and SHA.fullmatch(entry["sha256"]) and SHA.fullmatch(entry["report_sha256"]),
            "Invalid queue identity")


def release_url(entry):
    return f"https://github.com/{REPO}/releases/tag/{entry['paper']}-{entry['version']}"


def public_evidence(entry, author, byte_count):
    paper, version, sha = entry["paper"], entry["version"], entry["sha256"]
    year, identifier = PAPER.fullmatch(paper).groups()
    tag = f"{paper}-{version}"
    pdf = tag + ".pdf"
    base = f"https://github.com/{REPO}/releases/download/{tag}"
    release = json.loads(fetch(f"https://api.github.com/repos/{REPO}/releases/tags/{tag}", 256_000))
    require(release["html_url"] == release_url(entry) and release["tag_name"] == tag and
            release["draft"] is False and release["prerelease"] is False and release["published_at"],
            "Not a public final version release")
    assets = {a["name"]: a for a in release["assets"]}
    record = json.loads(fetch(base + "/RECORD.json", 128_000))
    require(record["id"] == paper and record["version"] == version
            and record["status"] == "working_paper" and record["source_of_truth"] == "paper.pdf"
            and [a["name"] for a in record["authors"]] == [author]
            and record["integrity"]["canonical_sha256"] == sha
            and record["integrity"]["canonical_bytes"] == byte_count
            and record["licenses"]["manuscript"] == "CC-BY-4.0"
            and record["licenses"]["metadata"] == "CC0-1.0", "Public record differs from native case")
    require(0 < byte_count <= 50 * 1024**2 and assets[pdf]["browser_download_url"] == base + "/" + pdf
            and assets[pdf]["digest"] == "sha256:" + sha and assets[pdf]["size"] == byte_count,
            "Official release PDF differs")
    leaf = f"papers/{year}/{entry['month']}/{identifier[:2]}/{paper}"
    raw = f"https://raw.githubusercontent.com/{REPO}/{tag}/{leaf}"
    # AIRR may materialize a historical version below versions/, or make it the
    # root record at its release tag. Select only a matching public version.
    candidates = [raw] if version == "v1" else [raw + "/versions/" + version, raw]
    from urllib.error import HTTPError
    for folder in candidates:
        try:
            at_tag = json.loads(fetch(folder + "/metadata.json", 128_000))
        except HTTPError as error:
            if error.code == 404: continue
            raise
        if at_tag == record: break
    else:
        raise ValueError("Exact release metadata missing from tagged tree")
    receipt = json.loads(fetch(folder + "/authority/receipt.json", 16_000))
    require(receipt["registration_number"] == entry["submission"] and receipt["sha256"] == sha
            and receipt["scan_status"] == "clean", "Receipt on tagged release differs")
    raw_report = fetch(folder + "/screening/original/exact-pdf-assessment.json", 512_000)
    require(hashlib.sha256(raw_report).hexdigest() == entry["report_sha256"], "Original report differs")
    report = json.loads(raw_report)
    require(report["paper_id"] == paper and report["version"] == version
            and report["version_id"] == record["version_id"] and report["canonical_sha256"] == sha
            and type(report["millennium_score"]) in (int, float) and 0 <= report["millennium_score"] <= 10
            and not report["unresolved_material_objections"], "Assessment does not clear this working paper")
    public_pdf = fetch(f"https://airr.science/papers/{paper}/versions/{version}/{pdf}", byte_count)
    require(len(public_pdf) == byte_count and hashlib.sha256(public_pdf).hexdigest() == sha,
            "AIRR PDF mirror differs")
    return record["version_id"]


def install(app, a, current):
    def check_native(db, item):
        row = db.execute("""SELECT s.*, p.id AS programme_key, c.artifact_json AS exact_artifact
          FROM submissions s JOIN agent_submissions m ON m.submission_id=s.id
          JOIN programme_artifact_grants c ON c.grant_id=m.grant_id
          JOIN programme_delegations p ON p.id=c.programme_id AND s.user_id=p.owner_user_id
          WHERE s.id=?""", (item["submission"],)).fetchone()
        require(row is not None and row["sha256"] == item["sha256"], "Programme receipt mismatch")
        if row["public_release_url"]:
            require(row["public_release_url"] == release_url(item), "Conflicting prior public release")
            return None
        programme = db.execute("SELECT * FROM programme_delegations WHERE id=?", (row["programme_key"],)).fetchone()
        authority = current(app, a, programme)
        require(authority["author"] == row["authors"] and row["operator_conflict"]
                and row["publication_mode"] == "standard" and authority["publication_status"] == "working_paper"
                and authority["pdf_license"] == "CC-BY-4.0" and authority["metadata_license"] == "CC0-1.0"
                and row["status"] in {"eligible", "under_assessment", "changes_requested", "awaiting_independent_decision"}
                and row["scan_status"] == "clean", "Current working-paper authority required")
        artifact = json.loads(row["exact_artifact"])
        require(artifact["sha256"] == row["sha256"], "Child grant differs")
        expected_id = None
        if artifact["kind"] == "revision":
            binding = artifact["binding"]
            require(binding["paper_id"] == item["paper"] and binding["version"] == item["version"]
                    and item["paper"] in authority["paper_ids"], "Historical version authority differs")
            expected_id = binding["version_id"]
        else:
            require(artifact["kind"] == "submission" and authority["allow_new_submissions"]
                    and item["version"] == "v1", "New-submission scope differs")
        permission = db.execute("SELECT * FROM publication_permissions WHERE submission_id=?", (row["id"],)).fetchone()
        require(permission and permission["manuscript_sha256"] == row["sha256"]
                and permission["license"] == "CC-BY-4.0", "Existing exact distribution permission required")
        return row["authors"], row["size_bytes"], expected_id

    @app.cli.command("reconcile-programme-publications")
    def reconcile():
        """Check the public queue and record verified releases using the native operator command."""
        queue = json.loads(fetch(QUEUE, 1024 * 1024))
        require(isinstance(queue, list), "Expected release queue")
        db = a.get_db()
        failed = 0
        for item in queue:
            try:
                validate_entry(item)
                native = check_native(db, item)
                if native is None: continue
                author, size, expected_id = native
                version_id = public_evidence(item, author, size)
                require(expected_id is None or expected_id == version_id, "Historical version ID differs")
                db.execute("BEGIN IMMEDIATE")
                latest = check_native(db, item)
                if latest is None:
                    db.rollback()
                    continue
                require(latest == native, "Native case changed during public readback")
                click.get_current_context().invoke(app.cli.commands["mark-published"],
                    submission_id=item["submission"], release_url=release_url(item))
            except (HTTPException, OSError, KeyError, TypeError, ValueError, click.ClickException) as error:
                db.rollback()
                failed += 1
                click.echo(f"Release deferred ({type(error).__name__}).", err=True)
        if failed:
            raise click.ClickException(f"{failed} release(s) deferred; other items were processed.")
