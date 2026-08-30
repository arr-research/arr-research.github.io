# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("ARR_SESSION_SECRET", "test-import-secret-" * 4)

from werkzeug.security import generate_password_hash

from services.intake.app import create_app, get_db, init_db, iso, now, totp


class IntakeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.app = create_app(
            {
                "TESTING": True,
                "SECRET_KEY": "test-secret-with-sufficient-entropy",
                "DATABASE": str(root / "intake.sqlite3"),
                "QUARANTINE": str(root / "quarantine"),
                "SESSION_COOKIE_SECURE": False,
                "OPERATOR_EMAIL": "operator@example.org",
            }
        )
        with self.app.app_context():
            init_db()
            db = get_db()
            db.execute(
                "INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at) VALUES(?,?,?,?,?,?)",
                ("author@example.org", "Author", generate_password_hash("author-password-123"), "depositor", None, iso()),
            )
            db.execute(
                "INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at) VALUES(?,?,?,?,?,?)",
                ("operator@example.org", "Operator", generate_password_hash("operator-password-123"), "operator", "JBSWY3DPEHPK3PXP", iso()),
            )
            db.execute(
                "INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at) VALUES(?,?,?,?,?,?)",
                ("independent@example.org", "Independent", generate_password_hash("independent-password-123"), "independent_editor", "JBSWY3DPEHPK3PXQ", iso()),
            )
            db.commit()
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def user_id(self, email: str) -> int:
        with self.app.app_context():
            return get_db().execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()[0]

    def login_session(self, email: str) -> str:
        token = "csrf-for-tests"
        with self.client.session_transaction() as session:
            session["user_id"] = self.user_id(email)
            session["csrf_token"] = token
        return token

    def upload(self, *, conflict: bool = False) -> str:
        token = self.login_session("author@example.org")
        data = {
            "csrf_token": token,
            "title": "A rigorous test manuscript",
            "authors": "Author Example",
            "abstract": "A" * 120,
            "terms": "on",
            "privacy": "on",
            "authority": "on",
            "manuscript": (io.BytesIO(b"%PDF-1.7\nminimal test bytes"), "paper.pdf"),
        }
        if conflict:
            data["operator_conflict"] = "on"
        with patch("services.intake.app.scan_file", return_value=("clean", "Approved scanner reported clean.")):
            response = self.client.post("/submit", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions ORDER BY created_at DESC LIMIT 1").fetchone()
            self.assertEqual(row["scan_status"], "clean")
            self.assertEqual(row["status"], "eligible")
            self.assertTrue((Path(self.app.config["QUARANTINE"]) / row["stored_name"]).exists())
            return row["id"]

    def test_editor_login_requires_valid_totp(self) -> None:
        self.client.get("/login")
        with self.client.session_transaction() as session:
            csrf = session["csrf_token"]
        bad = self.client.post(
            "/login",
            data={"csrf_token": csrf, "email": "operator@example.org", "password": "operator-password-123", "totp": "000000"},
        )
        self.assertEqual(bad.status_code, 200)
        good = self.client.post(
            "/login",
            data={"csrf_token": csrf, "email": "operator@example.org", "password": "operator-password-123", "totp": totp("JBSWY3DPEHPK3PXP")},
        )
        self.assertEqual(good.status_code, 302)

    def test_upload_stays_private_and_requires_manual_acceptance(self) -> None:
        submission_id = self.upload()
        token = self.login_session("operator@example.org")
        response = self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "accept", "reason": "scope-and-integrity-complete", "note": "Human review complete."},
        )
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual(row["status"], "accepted_for_publication")
        self.assertFalse(any(Path(self.temp.name).glob("papers/**")))
        blocked = self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "decline", "reason": "silent-rewrite-attempt"},
        )
        self.assertEqual(blocked.status_code, 409)

    def test_founder_conflict_requires_independent_editor(self) -> None:
        submission_id = self.upload(conflict=True)
        token = self.login_session("operator@example.org")
        self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "accept", "reason": "operator-provisional", "note": "Conflict disclosed."},
        )
        with self.app.app_context():
            status = get_db().execute("SELECT status FROM submissions WHERE id=?", (submission_id,)).fetchone()[0]
            self.assertEqual(status, "awaiting_independent_decision")
        token = self.login_session("independent@example.org")
        self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "accept", "reason": "independent-signoff", "note": "Independent review complete."},
        )
        with self.app.app_context():
            status = get_db().execute("SELECT status FROM submissions WHERE id=?", (submission_id,)).fetchone()[0]
            self.assertEqual(status, "accepted_for_publication")

    def test_missing_scanner_fails_closed(self) -> None:
        token = self.login_session("author@example.org")
        with patch("services.intake.app.shutil.which", return_value=None):
            response = self.client.post(
                "/submit",
                data={
                    "csrf_token": token,
                    "title": "Scanner failure test",
                    "authors": "Author Example",
                    "abstract": "B" * 120,
                    "terms": "on",
                    "privacy": "on",
                    "authority": "on",
                    "manuscript": (io.BytesIO(b"%PDF-1.7\nscanner failure"), "paper.pdf"),
                },
                content_type="multipart/form-data",
            )
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions ORDER BY created_at DESC LIMIT 1").fetchone()
            self.assertEqual((row["scan_status"], row["status"]), ("error", "quarantined"))
        token = self.login_session("operator@example.org")
        blocked = self.client.post(
            f"/admin/submission/{row['id']}/decision",
            data={"csrf_token": token, "action": "accept", "reason": "should-not-pass"},
        )
        self.assertEqual(blocked.status_code, 409)

    def test_declined_pdf_is_erased_on_schedule(self) -> None:
        submission_id = self.upload()
        token = self.login_session("operator@example.org")
        self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "decline", "reason": "out-of-scope", "note": "Outside current scope."},
        )
        with self.app.app_context():
            db = get_db()
            row = db.execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            path = Path(self.app.config["QUARANTINE"]) / row["stored_name"]
            db.execute("UPDATE submissions SET delete_after=? WHERE id=?", (iso(now()), submission_id))
            db.commit()
        result = self.app.test_cli_runner().invoke(args=["retention-sweep"])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertFalse(path.exists())
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual(row["abstract"], "[deleted under retention policy]")

    def test_legal_hold_pauses_and_restores_retention_state(self) -> None:
        submission_id = self.upload()
        applied = self.app.test_cli_runner().invoke(args=["legal-hold", submission_id, "--reason", "documented dispute"])
        self.assertEqual(applied.exit_code, 0, applied.output)
        with self.app.app_context():
            row = get_db().execute("SELECT status,held_status FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual((row["status"], row["held_status"]), ("legal_hold", "eligible"))
        released = self.app.test_cli_runner().invoke(args=["release-legal-hold", submission_id, "--reason", "dispute resolved"])
        self.assertEqual(released.exit_code, 0, released.output)
        with self.app.app_context():
            row = get_db().execute("SELECT status,held_status FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual((row["status"], row["held_status"]), ("eligible", None))


if __name__ == "__main__":
    unittest.main()
