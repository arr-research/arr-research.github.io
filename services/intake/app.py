# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import base64
import functools
import getpass
import hashlib
import hmac
import json
import os
import secrets
import shutil
import sqlite3
import smtplib
import ssl
# Scanner commands are fixed by the operator, use shell=False and never include an
# uploaded filename. See the guarded call in scan_file.
import subprocess  # nosec B404
import time
from datetime import UTC, datetime, timedelta
from email.message import EmailMessage
from email.utils import parseaddr
from pathlib import Path

import click
from flask import (
    Flask,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
)
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import check_password_hash, generate_password_hash


TERMS_VERSION = "ARR-DEPOSIT-1.2"
PRIVACY_VERSION = "ARR-PRIVACY-1.1"
MAX_PDF_BYTES = 25 * 1024 * 1024
ALLOWED_STATES = {
    "quarantined",
    "eligible",
    "under_assessment",
    "changes_requested",
    "awaiting_independent_decision",
    "accepted_for_publication",
    "declined",
    "withdrawn",
    "removed",
    "legal_hold",
}


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  email TEXT NOT NULL UNIQUE COLLATE NOCASE,
  display_name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK(role IN ('depositor','operator','independent_editor')),
  totp_secret TEXT,
  active INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS submissions (
  id TEXT PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  title TEXT NOT NULL,
  authors TEXT NOT NULL,
  abstract TEXT NOT NULL,
  original_filename TEXT NOT NULL,
  stored_name TEXT NOT NULL UNIQUE,
  sha256 TEXT NOT NULL,
  size_bytes INTEGER NOT NULL,
  scan_status TEXT NOT NULL CHECK(scan_status IN ('pending','clean','infected','error')),
  scan_detail TEXT NOT NULL,
  status TEXT NOT NULL,
  operator_conflict INTEGER NOT NULL DEFAULT 0,
  ai_review_opt_in INTEGER NOT NULL DEFAULT 0,
  terms_version TEXT NOT NULL,
  privacy_version TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  decided_at TEXT,
  decision_by INTEGER REFERENCES users(id),
  decision_reason TEXT,
  decision_note TEXT,
  delete_after TEXT,
  public_release_url TEXT,
  public_released_at TEXT,
  held_status TEXT
);
CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY,
  occurred_at TEXT NOT NULL,
  actor_user_id INTEGER REFERENCES users(id),
  event TEXT NOT NULL,
  submission_id TEXT,
  detail_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS rate_events (
  id INTEGER PRIMARY KEY,
  bucket TEXT NOT NULL,
  subject_hash TEXT NOT NULL,
  occurred_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_rate_events ON rate_events(bucket, subject_hash, occurred_at);
CREATE INDEX IF NOT EXISTS idx_submission_status ON submissions(status, created_at);
"""


def now() -> datetime:
    return datetime.now(UTC)


def iso(value: datetime | None = None) -> str:
    return (value or now()).replace(microsecond=0).isoformat()


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    default_instance = Path(os.environ.get("ARR_INTAKE_INSTANCE", app.instance_path)).resolve()
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("ARR_SESSION_SECRET"),
        DATABASE=str(default_instance / "intake.sqlite3"),
        QUARANTINE=str(default_instance / "quarantine"),
        MAX_CONTENT_LENGTH=MAX_PDF_BYTES + 64 * 1024,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Strict",
        SESSION_COOKIE_SECURE=os.environ.get("ARR_COOKIE_SECURE", "1") != "0",
        PERMANENT_SESSION_LIFETIME=timedelta(hours=8),
        OPERATOR_EMAIL=os.environ.get("ARR_OPERATOR_EMAIL", "lluiseriksson@gmail.com").lower(),
        PUBLIC_ORIGIN=os.environ.get("ARR_INTAKE_ORIGIN", "http://127.0.0.1:5000").rstrip("/"),
        SCANNER=os.environ.get("ARR_SCANNER", ""),
        SMTP_HOST=os.environ.get("ARR_SMTP_HOST", ""),
        SMTP_PORT=int(os.environ.get("ARR_SMTP_PORT", "587")),
        SMTP_USERNAME=os.environ.get("ARR_SMTP_USERNAME", ""),
        SMTP_PASSWORD=os.environ.get("ARR_SMTP_PASSWORD", ""),
        SMTP_FROM=os.environ.get("ARR_SMTP_FROM", ""),
        SMTP_SSL=os.environ.get("ARR_SMTP_SSL", "0") == "1",
        SMTP_STARTTLS=os.environ.get("ARR_SMTP_STARTTLS", "1") == "1",
        TESTING=False,
    )
    if test_config:
        app.config.update(test_config)
    if not app.config["SECRET_KEY"]:
        raise RuntimeError("ARR_SESSION_SECRET must be a persistent random value")

    Path(app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)
    Path(app.config["QUARANTINE"]).mkdir(parents=True, exist_ok=True)
    if os.name != "nt":
        os.chmod(Path(app.config["DATABASE"]).parent, 0o700)
        os.chmod(Path(app.config["QUARANTINE"]), 0o700)
    if os.environ.get("ARR_BEHIND_PROXY") == "1":
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)  # type: ignore[method-assign]

    app.teardown_appcontext(close_db)
    app.before_request(load_user)
    register_routes(app)
    register_commands(app)

    @app.after_request
    def security_headers(response):
        response.headers["Cache-Control"] = "no-store"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; img-src 'self'; style-src 'self' 'unsafe-inline'; "
            "form-action 'self'; frame-ancestors 'none'; base-uri 'none'"
        )
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        if request.is_secure:
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response

    return app


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(g.app_config_database if hasattr(g, "app_config_database") else current_app_config("DATABASE"))
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def current_app_config(name: str):
    from flask import current_app

    return current_app.config[name]


def close_db(_error=None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()
    db.executescript(SCHEMA)
    db.commit()


def audit(event: str, submission_id: str | None = None, **detail) -> None:
    actor = g.user["id"] if getattr(g, "user", None) else None
    db = get_db()
    db.execute(
        "INSERT INTO audit_log(occurred_at,actor_user_id,event,submission_id,detail_json) VALUES(?,?,?,?,?)",
        (iso(), actor, event, submission_id, json.dumps(detail, sort_keys=True)),
    )
    db.commit()


def load_user() -> None:
    user_id = session.get("user_id")
    g.user = get_db().execute("SELECT * FROM users WHERE id=? AND active=1", (user_id,)).fetchone() if user_id else None


def login_required(view):
    @functools.wraps(view)
    def wrapped(**kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return view(**kwargs)

    return wrapped


def editor_required(view):
    @functools.wraps(view)
    @login_required
    def wrapped(**kwargs):
        if g.user["role"] not in {"operator", "independent_editor"}:
            abort(403)
        return view(**kwargs)

    return wrapped


def csrf_token() -> str:
    token = session.get("csrf_token")
    if not token:
        token = secrets.token_urlsafe(32)
        session["csrf_token"] = token
    return token


def require_csrf() -> None:
    supplied = request.form.get("csrf_token", "")
    expected = session.get("csrf_token", "")
    if not expected or not hmac.compare_digest(supplied, expected):
        abort(400, "Invalid form token")


def rate_subject(raw: str | None = None) -> str:
    raw = raw if raw is not None else (request.remote_addr or "unknown")
    key = str(current_app_config("SECRET_KEY")).encode()
    return hmac.new(key, raw.encode(), hashlib.sha256).hexdigest()


def enforce_rate(bucket: str, maximum: int, window_seconds: int, raw_subject: str | None = None) -> None:
    db = get_db()
    cutoff = int(time.time()) - window_seconds
    subject = rate_subject(raw_subject)
    db.execute("DELETE FROM rate_events WHERE occurred_at < ?", (cutoff - 86400,))
    count = db.execute(
        "SELECT COUNT(*) FROM rate_events WHERE bucket=? AND subject_hash=? AND occurred_at>=?",
        (bucket, subject, cutoff),
    ).fetchone()[0]
    if count >= maximum:
        db.commit()
        abort(429)
    db.execute(
        "INSERT INTO rate_events(bucket,subject_hash,occurred_at) VALUES(?,?,?)",
        (bucket, subject, int(time.time())),
    )
    db.commit()


def totp(secret: str, at: int | None = None) -> str:
    counter = int((at or int(time.time())) / 30)
    key = base64.b32decode(secret.upper() + "=" * ((8 - len(secret) % 8) % 8))
    digest = hmac.new(key, counter.to_bytes(8, "big"), hashlib.sha1).digest()
    offset = digest[-1] & 0x0F
    code = (int.from_bytes(digest[offset : offset + 4], "big") & 0x7FFFFFFF) % 1_000_000
    return f"{code:06d}"


def verify_totp(secret: str, candidate: str) -> bool:
    if not candidate.isdigit() or len(candidate) != 6:
        return False
    current = int(time.time())
    return any(hmac.compare_digest(totp(secret, current + step * 30), candidate) for step in (-1, 0, 1))


def scanner_command(path: Path) -> list[str] | None:
    configured = current_app_config("SCANNER")
    if configured:
        configured_path = Path(configured)
        executable = str(configured_path) if configured_path.is_absolute() and configured_path.is_file() else shutil.which(configured)
        return [executable, str(path)] if executable else None
    if shutil.which("clamdscan"):
        return ["clamdscan", "--fdpass", "--no-summary", str(path)]
    if shutil.which("clamscan"):
        return ["clamscan", "--no-summary", str(path)]
    return None


def scan_file(path: Path) -> tuple[str, str]:
    command = scanner_command(path)
    if command is None:
        return "error", "No approved malware scanner is available; file remains quarantined."
    try:
        # command contains an operator-selected executable and our random server path;
        # no shell, uploaded filename or depositor-controlled argument is involved.
        result = subprocess.run(command, capture_output=True, text=True, timeout=120, check=False)  # nosec B603
    except (OSError, subprocess.TimeoutExpired):
        return "error", "Malware scanner failed or timed out; file remains quarantined."
    if result.returncode == 0:
        return "clean", "Approved scanner reported clean."
    if result.returncode == 1:
        return "infected", "Approved scanner detected malware; uploaded bytes were erased."
    return "error", "Malware scanner returned an operational error; file remains quarantined."


def scan_submission(row: sqlite3.Row) -> tuple[str, str]:
    path = Path(current_app_config("QUARANTINE")) / row["stored_name"]
    status, detail = scan_file(path)
    db = get_db()
    new_state = "eligible" if status == "clean" else ("removed" if status == "infected" else "quarantined")
    delete_after = iso(now()) if status == "infected" else None
    db.execute(
        "UPDATE submissions SET scan_status=?,scan_detail=?,status=?,updated_at=?,delete_after=? WHERE id=?",
        (status, detail, new_state, iso(), delete_after, row["id"]),
    )
    db.commit()
    if status == "infected":
        path.unlink(missing_ok=True)
    audit("scan_completed", row["id"], result=status)
    return status, detail


def valid_email(value: str) -> bool:
    parsed_name, parsed_address = parseaddr(value)
    return not parsed_name and parsed_address == value and 3 <= len(value) <= 254 and "@" in value


def find_or_create_submitter(email: str, display_name: str) -> sqlite3.Row:
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if user:
        return user
    try:
        db.execute(
            "INSERT INTO users(email,display_name,password_hash,role,active,created_at) VALUES(?,?,?,?,0,?)",
            (email, display_name[:200], generate_password_hash(secrets.token_urlsafe(48)), "depositor", iso()),
        )
        db.commit()
    except sqlite3.IntegrityError:
        db.rollback()
    return db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()


def notify_operator(submission_id: str, title: str, submitter_email: str, scan_status: str) -> bool:
    host = str(current_app_config("SMTP_HOST"))
    sender = str(current_app_config("SMTP_FROM"))
    if not host or not sender:
        audit("operator_notification_skipped", submission_id, reason="smtp_not_configured")
        return False
    message = EmailMessage()
    safe_title = title.replace("\r", " ").replace("\n", " ")
    message["Subject"] = f"[ARR private submission] {submission_id}: {safe_title[:120]}"
    message["From"] = sender
    message["To"] = current_app_config("OPERATOR_EMAIL")
    message["Reply-To"] = submitter_email
    message.set_content(
        "A new manuscript was submitted to ARR's private quarantine.\n\n"
        f"Case: {submission_id}\n"
        f"Title: {title}\n"
        f"Scanner status: {scan_status}\n"
        f"Review after signing in: {current_app_config('PUBLIC_ORIGIN')}/admin/submission/{submission_id}\n\n"
        "The manuscript is not attached to this email and has not been published."
    )
    try:
        if current_app_config("SMTP_SSL"):
            client = smtplib.SMTP_SSL(host, current_app_config("SMTP_PORT"), timeout=15, context=ssl.create_default_context())
        else:
            client = smtplib.SMTP(host, current_app_config("SMTP_PORT"), timeout=15)
        with client:
            if current_app_config("SMTP_STARTTLS") and not current_app_config("SMTP_SSL"):
                client.starttls(context=ssl.create_default_context())
            username = str(current_app_config("SMTP_USERNAME"))
            if username:
                client.login(username, str(current_app_config("SMTP_PASSWORD")))
            client.send_message(message)
    except (OSError, smtplib.SMTPException):
        audit("operator_notification_failed", submission_id, reason="smtp_delivery_error")
        return False
    audit("operator_notification_sent", submission_id, recipient="operator")
    return True


def register_routes(app: Flask) -> None:
    app.jinja_env.globals["csrf_token"] = csrf_token

    @app.get("/healthz")
    def healthz():
        get_db().execute("SELECT 1").fetchone()
        return {
            "status": "ok",
            "intake": "direct-private-submission",
            "operator_email_notification": bool(current_app_config("SMTP_HOST") and current_app_config("SMTP_FROM")),
        }

    @app.get("/readyz")
    def readyz():
        checks = {
            "database": bool(get_db().execute("SELECT 1").fetchone()),
            "https_origin": str(current_app_config("PUBLIC_ORIGIN")).startswith("https://"),
            "secure_cookie": bool(current_app_config("SESSION_COOKIE_SECURE")),
            "malware_scanner": scanner_command(Path(current_app_config("QUARANTINE")) / "readiness-probe.pdf") is not None,
            "operator_email_notification": bool(current_app_config("SMTP_HOST") and current_app_config("SMTP_FROM")),
        }
        return ({"ready": all(checks.values()), "checks": checks}, 200 if all(checks.values()) else 503)

    @app.route("/login", methods=("GET", "POST"))
    def login():
        if request.method == "POST":
            require_csrf()
            enforce_rate("login", 8, 15 * 60)
            email = request.form.get("email", "").strip().lower()
            user = get_db().execute("SELECT * FROM users WHERE email=? AND active=1", (email,)).fetchone()
            valid = bool(user and check_password_hash(user["password_hash"], request.form.get("password", "")))
            if valid and user["role"] in {"operator", "independent_editor"}:
                valid = bool(user["totp_secret"] and verify_totp(user["totp_secret"], request.form.get("totp", "")))
            if not valid:
                flash("Invalid credentials or one-time code.", "error")
            else:
                session.clear()
                session["user_id"] = user["id"]
                session.permanent = True
                audit("login")
                return redirect(url_for("dashboard"))
        return render_template("login.html")

    @app.post("/logout")
    @login_required
    def logout():
        require_csrf()
        audit("logout")
        session.clear()
        return redirect(url_for("login"))

    @app.get("/")
    @login_required
    def dashboard():
        if g.user["role"] in {"operator", "independent_editor"}:
            rows = get_db().execute(
                "SELECT s.*,u.email,u.display_name FROM submissions s JOIN users u ON u.id=s.user_id ORDER BY s.created_at DESC"
            ).fetchall()
            return render_template("admin.html", submissions=rows)
        rows = get_db().execute("SELECT * FROM submissions WHERE user_id=? ORDER BY created_at DESC", (g.user["id"],)).fetchall()
        return render_template("dashboard.html", submissions=rows)

    @app.route("/submit", methods=("GET", "POST"))
    def submit():
        if request.method == "POST":
            require_csrf()
            enforce_rate("submit", 3, 24 * 60 * 60)
            if request.form.get("website"):
                flash("Submission received for processing.", "success")
                return redirect(url_for("submit"))
            upload = request.files.get("manuscript")
            display_name = request.form.get("display_name", "").strip()
            email = request.form.get("email", "").strip().lower()
            title = request.form.get("title", "").strip()
            authors = request.form.get("authors", "").strip()
            abstract = request.form.get("abstract", "").strip()
            agreed = all(request.form.get(field) for field in ("adult", "terms", "privacy", "authority"))
            if not upload or len(display_name) < 2 or not valid_email(email) or not title or not authors or len(abstract) < 80 or not agreed:
                flash("Complete all fields and attestations.", "error")
                return render_template("submit.html", terms=TERMS_VERSION, privacy=PRIVACY_VERSION)
            enforce_rate("submit-email", 3, 24 * 60 * 60, email)
            original = Path(upload.filename or "manuscript.pdf").name[:200]
            submission_id = "SUB-" + secrets.token_hex(8).upper()
            stored = secrets.token_hex(24) + ".pdf"
            target = Path(current_app_config("QUARANTINE")) / stored
            digest = hashlib.sha256()
            size = 0
            with target.open("xb") as handle:
                first = upload.stream.read(5)
                if first != b"%PDF-":
                    handle.close()
                    target.unlink(missing_ok=True)
                    flash("Only a genuine PDF beginning with the PDF signature is accepted.", "error")
                    return render_template("submit.html", terms=TERMS_VERSION, privacy=PRIVACY_VERSION)
                handle.write(first)
                digest.update(first)
                size += len(first)
                while chunk := upload.stream.read(1024 * 1024):
                    size += len(chunk)
                    if size > MAX_PDF_BYTES:
                        handle.close()
                        target.unlink(missing_ok=True)
                        abort(413)
                    handle.write(chunk)
                    digest.update(chunk)
            if os.name != "nt":
                os.chmod(target, 0o600)
            submitter = find_or_create_submitter(email, display_name)
            conflict = int(email == current_app_config("OPERATOR_EMAIL") or bool(request.form.get("operator_conflict")))
            db = get_db()
            db.execute(
                """INSERT INTO submissions(
                   id,user_id,title,authors,abstract,original_filename,stored_name,sha256,size_bytes,
                   scan_status,scan_detail,status,operator_conflict,ai_review_opt_in,terms_version,
                   privacy_version,created_at,updated_at)
                   VALUES(?,?,?,?,?,?,?,?,?,'pending','Awaiting approved scanner.','quarantined',?,?,?,?,?,?)""",
                (
                    submission_id,
                    submitter["id"],
                    title[:500],
                    authors[:1000],
                    abstract[:5000],
                    original,
                    stored,
                    digest.hexdigest(),
                    size,
                    conflict,
                    int(bool(request.form.get("ai_review_opt_in"))),
                    TERMS_VERSION,
                    PRIVACY_VERSION,
                    iso(),
                    iso(),
                ),
            )
            db.commit()
            audit("submission_received", submission_id, sha256=digest.hexdigest(), size_bytes=size)
            row = db.execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            scan_file_status, _ = scan_submission(row)
            notify_operator(submission_id, title, email, scan_file_status)
            flash(
                f"Private submission {submission_id} received. Keep this case identifier. Uploading has not published the manuscript.",
                "success" if scan_file_status == "clean" else "warning",
            )
            return redirect(url_for("submit"))
        return render_template("submit.html", terms=TERMS_VERSION, privacy=PRIVACY_VERSION)

    @app.get("/admin/submission/<submission_id>")
    @editor_required
    def submission_detail(submission_id: str):
        row = get_db().execute(
            "SELECT s.*,u.email,u.display_name FROM submissions s JOIN users u ON u.id=s.user_id WHERE s.id=?",
            (submission_id,),
        ).fetchone()
        if not row:
            abort(404)
        return render_template("submission.html", submission=row, states=ALLOWED_STATES)

    @app.get("/admin/submission/<submission_id>/file")
    @editor_required
    def submission_file(submission_id: str):
        row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
        if not row or row["scan_status"] != "clean" or row["status"] in {"removed", "withdrawn"}:
            abort(404)
        audit("manuscript_downloaded", submission_id)
        return send_file(
            Path(current_app_config("QUARANTINE")) / row["stored_name"],
            mimetype="application/pdf",
            as_attachment=True,
            download_name=f"{submission_id}.pdf",
            conditional=False,
        )

    @app.post("/admin/submission/<submission_id>/decision")
    @editor_required
    def decision(submission_id: str):
        require_csrf()
        row = get_db().execute(
            "SELECT s.*,u.email FROM submissions s JOIN users u ON u.id=s.user_id WHERE s.id=?",
            (submission_id,),
        ).fetchone()
        if not row:
            abort(404)
        if row["user_id"] == g.user["id"]:
            abort(403, "An editor cannot decide their own submission")
        if row["status"] in {"accepted_for_publication", "declined", "withdrawn", "removed", "legal_hold"}:
            abort(409, "This state requires the correction, appeal, takedown or legal-hold workflow")
        if row["status"] == "awaiting_independent_decision" and g.user["role"] != "independent_editor":
            abort(403, "Only an independent editor may complete this conflicted decision")
        action = request.form.get("action")
        reason = request.form.get("reason", "").strip()[:200]
        note = request.form.get("note", "").strip()[:2000]
        if action not in {"accept", "decline", "request_changes"} or not reason:
            abort(400)
        if action == "accept" and row["scan_status"] != "clean":
            abort(409, "A quarantined or unscanned file cannot be accepted")
        if action == "accept" and row["operator_conflict"] and g.user["role"] != "independent_editor":
            new_status = "awaiting_independent_decision"
        elif action == "accept":
            new_status = "accepted_for_publication"
        elif action == "decline":
            new_status = "declined"
        else:
            new_status = "changes_requested"
        delete_after = iso(now() + timedelta(days=30)) if new_status == "declined" else None
        db = get_db()
        db.execute(
            """UPDATE submissions SET status=?,updated_at=?,decided_at=?,decision_by=?,
               decision_reason=?,decision_note=?,delete_after=? WHERE id=?""",
            (new_status, iso(), iso(), g.user["id"], reason, note, delete_after, submission_id),
        )
        db.commit()
        audit("editorial_decision", submission_id, action=action, resulting_status=new_status, reason=reason)
        flash(f"Decision recorded: {new_status.replace('_', ' ')}.", "success")
        return redirect(url_for("submission_detail", submission_id=submission_id))

    @app.post("/submission/<submission_id>/withdraw")
    @login_required
    def withdraw(submission_id: str):
        require_csrf()
        row = get_db().execute("SELECT * FROM submissions WHERE id=? AND user_id=?", (submission_id, g.user["id"])).fetchone()
        if not row or row["status"] == "accepted_for_publication":
            abort(404)
        db = get_db()
        db.execute(
            "UPDATE submissions SET status='withdrawn',updated_at=?,delete_after=? WHERE id=?",
            (iso(), iso(now() + timedelta(days=7)), submission_id),
        )
        db.commit()
        audit("submission_withdrawn", submission_id)
        return redirect(url_for("dashboard"))


def register_commands(app: Flask) -> None:
    @app.cli.command("init-db")
    def init_db_command():
        init_db()
        click.echo("Private intake database initialized.")

    @app.cli.command("create-operator")
    @click.option("--email", prompt=True, default="lluiseriksson@gmail.com")
    @click.option("--name", prompt=True, default="Lluis Eriksson")
    def create_operator(email: str, name: str):
        password = getpass.getpass("Password (minimum 12 characters): ")
        if len(password) < 12:
            raise click.ClickException("Password is too short")
        secret = base64.b32encode(secrets.token_bytes(20)).decode().rstrip("=")
        db = get_db()
        db.execute(
            """INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at)
               VALUES(?,?,?,?,?,?) ON CONFLICT(email) DO UPDATE SET
               display_name=excluded.display_name,password_hash=excluded.password_hash,
               role='operator',totp_secret=excluded.totp_secret,active=1""",
            (email.strip().lower(), name.strip(), generate_password_hash(password), "operator", secret, iso()),
        )
        db.commit()
        click.echo(f"Operator created. Add this TOTP secret now (shown once): {secret}")

    @app.cli.command("create-editor")
    @click.argument("email")
    @click.option("--name", prompt=True)
    def create_editor(email: str, name: str):
        password = getpass.getpass("Temporary password (minimum 12 characters): ")
        if len(password) < 12:
            raise click.ClickException("Password is too short")
        secret = base64.b32encode(secrets.token_bytes(20)).decode().rstrip("=")
        db = get_db()
        db.execute(
            "INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at) VALUES(?,?,?,?,?,?)",
            (email.strip().lower(), name.strip(), generate_password_hash(password), "independent_editor", secret, iso()),
        )
        db.commit()
        click.echo(f"Independent editor created. Deliver this TOTP secret securely: {secret}")

    @app.cli.command("scan-pending")
    def scan_pending():
        rows = get_db().execute("SELECT * FROM submissions WHERE scan_status IN ('pending','error')").fetchall()
        for row in rows:
            status, _ = scan_submission(row)
            click.echo(f"{row['id']}: {status}")

    @app.cli.command("mark-published")
    @click.argument("submission_id")
    @click.argument("release_url")
    def mark_published(submission_id: str, release_url: str):
        """Record a separately verified public release and start private-copy erasure."""
        if not release_url.startswith("https://"):
            raise click.ClickException("The immutable public release URL must use HTTPS")
        row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
        if not row or row["status"] != "accepted_for_publication":
            raise click.ClickException("Only a finally accepted submission can be marked published")
        get_db().execute(
            """UPDATE submissions SET public_release_url=?,public_released_at=?,updated_at=?,
               delete_after=? WHERE id=?""",
            (release_url, iso(), iso(), iso(now() + timedelta(days=30)), submission_id),
        )
        get_db().execute(
            "INSERT INTO audit_log(occurred_at,event,submission_id,detail_json) VALUES(?,?,?,?)",
            (iso(), "public_release_verified", submission_id, json.dumps({"release_url": release_url})),
        )
        get_db().commit()
        click.echo(f"{submission_id}: private working copy scheduled for erasure in 30 days")

    @app.cli.command("legal-hold")
    @click.argument("submission_id")
    @click.option("--reason", prompt=True)
    def legal_hold(submission_id: str, reason: str):
        row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
        if not row or row["status"] == "legal_hold":
            raise click.ClickException("Case not found or already held")
        get_db().execute(
            "UPDATE submissions SET held_status=status,status='legal_hold',updated_at=? WHERE id=?",
            (iso(), submission_id),
        )
        get_db().execute(
            "INSERT INTO audit_log(occurred_at,event,submission_id,detail_json) VALUES(?,?,?,?)",
            (iso(), "legal_hold_applied", submission_id, json.dumps({"reason": reason[:500]})),
        )
        get_db().commit()
        click.echo(f"{submission_id}: legal hold applied; review within 90 days")

    @app.cli.command("release-legal-hold")
    @click.argument("submission_id")
    @click.option("--reason", prompt=True)
    def release_legal_hold(submission_id: str, reason: str):
        row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
        if not row or row["status"] != "legal_hold" or not row["held_status"]:
            raise click.ClickException("Case is not under a reversible legal hold")
        get_db().execute(
            "UPDATE submissions SET status=held_status,held_status=NULL,updated_at=? WHERE id=?",
            (iso(), submission_id),
        )
        get_db().execute(
            "INSERT INTO audit_log(occurred_at,event,submission_id,detail_json) VALUES(?,?,?,?)",
            (iso(), "legal_hold_released", submission_id, json.dumps({"reason": reason[:500]})),
        )
        get_db().commit()
        click.echo(f"{submission_id}: legal hold released")

    @app.cli.command("retention-sweep")
    def retention_sweep():
        rows = get_db().execute(
            "SELECT * FROM submissions WHERE delete_after IS NOT NULL AND delete_after<=? AND status!='legal_hold'",
            (iso(),),
        ).fetchall()
        db = get_db()
        for row in rows:
            (Path(current_app_config("QUARANTINE")) / row["stored_name"]).unlink(missing_ok=True)
            db.execute(
                """UPDATE submissions SET original_filename='[deleted]',stored_name='deleted-'||id,
                   abstract='[deleted under retention policy]',updated_at=?,delete_after=NULL WHERE id=?""",
                (iso(), row["id"]),
            )
            db.execute(
                "INSERT INTO audit_log(occurred_at,event,submission_id,detail_json) VALUES(?,?,?,?)",
                (iso(), "retention_erasure", row["id"], "{}"),
            )
            click.echo(f"{row['id']}: manuscript erased")
        cutoff = int(time.time()) - 90 * 86400
        db.execute("DELETE FROM rate_events WHERE occurred_at<?", (cutoff,))
        audit_cutoff = iso(now() - timedelta(days=365))
        db.execute(
            "DELETE FROM audit_log WHERE occurred_at<? AND event NOT IN ('editorial_decision','retention_erasure','public_release_verified')",
            (audit_cutoff,),
        )
        account_cutoff = iso(now() - timedelta(days=180))
        inactive = db.execute(
            """SELECT u.id FROM users u WHERE u.role='depositor' AND u.created_at<?
               AND u.email NOT LIKE 'erased-user-%@invalid.local'
               AND NOT EXISTS(SELECT 1 FROM submissions s WHERE s.user_id=u.id AND
               (s.updated_at>=? OR s.status NOT IN ('declined','withdrawn','removed','accepted_for_publication')))""",
            (account_cutoff, account_cutoff),
        ).fetchall()
        for user in inactive:
            db.execute(
                "UPDATE users SET email=?,display_name='[erased contact]',password_hash=?,active=0 WHERE id=?",
                (f"erased-user-{user['id']}@invalid.local", generate_password_hash(secrets.token_urlsafe(32)), user["id"]),
            )
        db.commit()


app = create_app()
