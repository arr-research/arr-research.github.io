# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("ARR_SESSION_SECRET", "test-import-secret-" * 4)

from werkzeug.security import generate_password_hash

from services.intake.app import create_app, get_db, init_db, iso, model_review_template, now, totp


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
        self.client.get("/submit")
        with self.client.session_transaction() as session:
            token = session["csrf_token"]
        data = {
            "csrf_token": token,
            "display_name": "Direct Author",
            "email": "direct-author@example.org",
            "title": "A rigorous test manuscript",
            "authors": "Author Example",
            "abstract": "A" * 120,
            "adult": "on",
            "terms": "on",
            "privacy": "on",
            "authority": "on",
            "ai_review_opt_in": "on",
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
            self.assertEqual(row["terms_version"], "ARR-DEPOSIT-1.3")
            self.assertEqual(row["privacy_version"], "ARR-PRIVACY-1.2")
            self.assertTrue((Path(self.app.config["QUARANTINE"]) / row["stored_name"]).exists())
            submitter = get_db().execute("SELECT * FROM users WHERE id=?", (row["user_id"],)).fetchone()
            self.assertEqual(submitter["email"], "direct-author@example.org")
            self.assertEqual(submitter["active"], 0)
            return row["id"]

    def add_model_review(self, submission_id: str, number: int, *, recommendation: str = "accept", material: bool = False) -> None:
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            value = model_review_template(row)
        value.update(
            {
                "provider": f"Provider {number}",
                "model_id": f"frontier-model-{number}",
                "assessed_at": f"2026-08-30T12:0{number}:00+00:00",
                "recommendation": recommendation,
                "millennium_score": 4.0 if recommendation == "accept" else 2.0,
                "overall_stars": 4 if recommendation == "accept" else 2,
                "summary": "This exact manuscript was inspected adversarially and the structured recommendation records the resulting evidence.",
                "strengths": ["The principal statement is precise and independently inspectable."],
                "weaknesses": ["The exposition could make one dependency more explicit."],
                "unresolved_material_objections": ["A main lemma appears unsupported by the stated assumptions."] if material else [],
            }
        )
        for criterion in value["criteria"].values():
            criterion["basis"] = "The exact manuscript supplies enough claim-linked evidence for this criterion."
        token = self.login_session("operator@example.org")
        response = self.client.post(
            f"/admin/submission/{submission_id}/model-review",
            data={"csrf_token": token, "response_json": json.dumps(value)},
        )
        self.assertEqual(response.status_code, 302)

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
            "/login?next=https://attacker.example/steal",
            data={"csrf_token": csrf, "email": "operator@example.org", "password": "operator-password-123", "totp": totp("JBSWY3DPEHPK3PXP")},
        )
        self.assertEqual(good.status_code, 302)
        self.assertEqual(good.headers["Location"], "/")

    def test_direct_form_requires_no_invitation_or_author_login(self) -> None:
        response = self.client.get("/submit")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"No invitation or account is required", response.data)
        self.assertNotIn(b"password", response.data.lower())

    def test_readiness_fails_closed_without_scanner_and_smtp(self) -> None:
        with patch("services.intake.app.shutil.which", return_value=None):
            response = self.client.get("/readyz")
        self.assertEqual(response.status_code, 503)
        self.assertFalse(response.json["ready"])
        self.assertFalse(response.json["checks"]["malware_scanner"])
        self.assertFalse(response.json["checks"]["operator_email_notification"])

    def test_bot_trap_discards_payload_without_creating_a_case(self) -> None:
        self.client.get("/submit")
        with self.client.session_transaction() as session:
            token = session["csrf_token"]
        response = self.client.post(
            "/submit",
            data={"csrf_token": token, "website": "https://spam.example", "email": "bot@example.org"},
        )
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            count = get_db().execute("SELECT COUNT(*) FROM submissions").fetchone()[0]
        self.assertEqual(count, 0)

    def test_upload_stays_private_and_requires_manual_acceptance(self) -> None:
        submission_id = self.upload()
        token = self.login_session("operator@example.org")
        for number in range(1, 4):
            self.add_model_review(submission_id, number)
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
        for number in range(1, 4):
            self.add_model_review(submission_id, number)
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

    def test_material_model_objection_blocks_acceptance(self) -> None:
        submission_id = self.upload()
        self.add_model_review(submission_id, 1)
        self.add_model_review(submission_id, 2)
        self.add_model_review(submission_id, 3, recommendation="reject", material=True)
        token = self.login_session("operator@example.org")
        response = self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "accept", "reason": "attempted-acceptance"},
        )
        self.assertEqual(response.status_code, 409)
        with self.app.app_context():
            row = get_db().execute("SELECT status FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual(row["status"], "eligible")

    def test_missing_scanner_fails_closed(self) -> None:
        self.client.get("/submit")
        with self.client.session_transaction() as session:
            token = session["csrf_token"]
        with patch("services.intake.app.shutil.which", return_value=None):
            response = self.client.post(
                "/submit",
                data={
                    "csrf_token": token,
                    "display_name": "Scanner Author",
                    "email": "scanner-author@example.org",
                    "title": "Scanner failure test",
                    "authors": "Author Example",
                    "abstract": "B" * 120,
                    "adult": "on",
                    "terms": "on",
                    "privacy": "on",
                    "authority": "on",
                    "ai_review_opt_in": "on",
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

    def test_operator_email_has_protected_link_and_no_manuscript(self) -> None:
        sent = []

        class FakeSMTP:
            def __init__(self, *_args, **_kwargs):
                pass

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def starttls(self, **_kwargs):
                return None

            def login(self, *_args):
                return None

            def send_message(self, message):
                sent.append(message)

        self.app.config.update(
            SMTP_HOST="smtp.example.org",
            SMTP_FROM="arr@example.org",
            SMTP_USERNAME="arr-user",
            SMTP_PASSWORD="secret",
            PUBLIC_ORIGIN="https://intake.example.org",
        )
        with patch("services.intake.app.smtplib.SMTP", FakeSMTP):
            submission_id = self.upload()

        self.assertEqual(len(sent), 1)
        body = sent[0].get_content()
        self.assertIn(f"https://intake.example.org/admin/submission/{submission_id}", body)
        self.assertNotIn("A" * 80, body)
        self.assertNotIn("%PDF", body)
        self.assertNotIn("attachment", str(sent[0].get_content_disposition()))

    def test_declined_pdf_is_erased_on_schedule(self) -> None:
        submission_id = self.upload()
        self.add_model_review(submission_id, 1)
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
            db = get_db()
            row = db.execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual(row["abstract"], "[deleted under retention policy]")
            self.assertEqual(db.execute("SELECT COUNT(*) FROM model_reviews WHERE submission_id=?", (submission_id,)).fetchone()[0], 0)

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
