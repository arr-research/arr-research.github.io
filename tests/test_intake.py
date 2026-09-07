# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import io
import hashlib
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

    def upload(self, *, conflict: bool = False, fields: dict | None = None, expected_status: int = 302) -> str:
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
            "primary_subject": "airr-quantum-information",
            "adult": "on",
            "terms": "on",
            "privacy": "on",
            "authority": "on",
            "ai_review_opt_in": "on",
            "manuscript": (io.BytesIO(b"%PDF-1.7\nminimal test bytes"), "paper.pdf"),
        }
        if conflict:
            data["operator_conflict"] = "on"
        data.update(fields or {})
        with patch("services.intake.app.scan_file", return_value=("clean", "Approved scanner reported clean.")):
            response = self.client.post("/submit", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, expected_status)
        if expected_status != 302:
            with self.app.app_context():
                self.assertEqual(get_db().execute("SELECT COUNT(*) FROM submissions").fetchone()[0], 0)
            self.assertEqual(list(Path(self.app.config["QUARANTINE"]).glob("*.pdf")), [])
            return ""
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions ORDER BY created_at DESC LIMIT 1").fetchone()
            self.assertEqual(row["scan_status"], "clean")
            self.assertEqual(row["status"], "eligible")
            self.assertEqual(row["terms_version"], "ARR-DEPOSIT-1.6")
            self.assertEqual(row["privacy_version"], "ARR-PRIVACY-1.4")
            self.assertTrue((Path(self.app.config["QUARANTINE"]) / row["stored_name"]).exists())
            submitter = get_db().execute("SELECT * FROM users WHERE id=?", (row["user_id"],)).fetchone()
            self.assertEqual(submitter["email"], "direct-author@example.org")
            self.assertEqual(submitter["active"], 0)
            get_db().execute('INSERT INTO case_editors VALUES(?,?,?,?)', (row['id'], self.user_id('independent@example.org'), self.user_id('operator@example.org'), iso()))
            get_db().commit()
            return row["id"]

    def add_model_review(self, submission_id: str, number: int, *, recommendation: str = "accept", material: bool = False) -> None:
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            value = model_review_template(row)
            # Fixture: the named plan was authorized before this report was made.
            get_db().execute('INSERT INTO assessment_plans(submission_id,manuscript_sha256,providers_json,notice,created_by,created_at,authorized_at) VALUES(?,?,?,?,?,?,?)',
                             (submission_id, row['sha256'], json.dumps([{'provider': f'Provider {number}', 'model_id': f'frontier-model-{number}'}]),
                              'Test fixture: author confirmed the provider-specific confidentiality notice before any transfer.', self.user_id('operator@example.org'), iso(), iso()))
            get_db().commit()
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

    def test_subjects_are_saved_on_receipt_and_editor_page(self):
        submission_id = self.upload(fields={
            "secondary_subject": ["airr-number-theory", "airr-ai-agents-and-multi-agent-systems"],
            "specific_topic": "<script>not markup</script>",
        })
        with self.app.app_context():
            row = get_db().execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            saved = json.loads(row["classification_json"])
            self.assertEqual(saved["primary"]["label"], "Quantum information")
            self.assertEqual(len(saved["secondary"]), 2)
        receipt = self.client.get("/receipt")
        self.assertIn(b"Number theory", receipt.data)
        self.assertIn(b"&lt;script&gt;not markup", receipt.data)
        self.assertIn(b"Quantum information", self.client.get("/receipt/download").data)
        self.login_session("operator@example.org")
        detail = self.client.get(f"/admin/submission/{submission_id}")
        self.assertIn(b"AI agents and multi-agent systems", detail.data)
        self.assertNotIn(b"<script>not markup</script>", detail.data)

    def test_forged_subject_does_not_store_a_case_or_file(self):
        self.upload(fields={"primary_subject": "not-a-subject"}, expected_status=400)

    def test_duplicate_subject_does_not_store_a_case(self):
        self.upload(fields={"secondary_subject": ["airr-quantum-information"]}, expected_status=400)

    def test_form_preserves_valid_selection_after_error_and_query_prefill(self):
        selected = "airr-number-theory"
        page = self.client.get("/submit?subject=" + selected)
        self.assertIn(f'value="{selected}" selected'.encode(), page.data)
        self.client.get("/submit")
        with self.client.session_transaction() as session:
            token = session["csrf_token"]
        page = self.client.post("/submit", data={"csrf_token": token, "primary_subject": selected,
            "secondary_subject": ["airr-quantum-information"], "title": "Still here"})
        self.assertIn(f'value="{selected}" selected'.encode(), page.data)
        self.assertIn(b'value="airr-quantum-information" selected', page.data)
        self.assertIn(b'Still here', page.data)

    def test_old_database_migration_is_idempotent_and_keeps_cases(self):
        submission_id = self.upload()
        with self.app.app_context():
            db = get_db()
            db.execute("ALTER TABLE submissions DROP COLUMN classification_json")
            db.commit()
            init_db()
            init_db()
            row = db.execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual(row["title"], "A rigorous test manuscript")
            self.assertEqual(row["classification_json"], "{}")
        self.assertIn(b"earlier submission", self.client.get("/receipt").data)

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

    def test_receipt_confirms_persisted_bytes_and_pending_approval(self) -> None:
        submission_id = self.upload()
        receipt = self.client.get("/receipt")
        self.assertEqual(receipt.status_code, 200)
        self.assertIn(submission_id.encode(), receipt.data)
        self.assertIn(b"Pending approval", receipt.data)
        self.assertIn(b"does not mean", receipt.data)
        self.assertIn(b"Download your receipt", receipt.data)
        self.assertEqual(receipt.headers["Cache-Control"], "no-store")
        self.assertIn("noindex", receipt.headers["X-Robots-Tag"])
        saved = self.client.get("/receipt/download")
        self.assertEqual(saved.status_code, 200)
        self.assertIn("attachment", saved.headers["Content-Disposition"])
        self.assertIn(submission_id.encode(), saved.data)
        expected_hash = hashlib.sha256(b"%PDF-1.7\nminimal test bytes").hexdigest()
        self.assertIn(expected_hash.encode(), saved.data)
        self.assertIn(b"not approval or publication", saved.data)
        with self.app.app_context():
            row = get_db().execute("SELECT status,public_release_url FROM submissions WHERE id=?", (submission_id,)).fetchone()
            self.assertEqual(row["status"], "eligible")
            self.assertIsNone(row["public_release_url"])

    def test_receipt_number_does_not_authorize_another_browser(self) -> None:
        submission_id = self.upload()
        other = self.app.test_client()
        for path in ("/receipt", "/receipt/download", f"/receipt?submission_id={submission_id}"):
            self.assertEqual(other.get(path).status_code, 404)
        self.assertEqual(other.get(f"/admin/submission/{submission_id}/file").status_code, 302)

    def test_receipt_donation_is_optional_and_does_not_send_paper_data(self) -> None:
        submission_id = self.upload()
        response = self.client.get("/receipt")
        self.assertIn(f"AIRR submission {submission_id}".encode(), response.data)
        self.assertIn(b"does not affect", self.client.get("/submit").data)
        self.assertIn(b"cannot affect approval, review speed, scores or ranking", response.data)
        self.assertIn(b'https://www.paypal.com/donate/?hosted_button_id=BCYAHWZCKGF5Q', response.data)
        self.assertNotIn(b"paypalobjects", response.data)
        self.assertNotIn(b"donate/sdk", response.data)
        self.assertNotIn(b"business=", response.data)
        self.assertIn(b"Sharing it with PayPal is your choice", response.data)
        # The only registration reference is displayed for optional manual copy.
        self.assertNotIn(b"hosted_button_id=BCYAHWZCKGF5Q&", response.data)

    def test_receipt_escapes_manuscript_title_and_hides_donation_when_disabled(self) -> None:
        submission_id = self.upload()
        with self.app.app_context():
            db = get_db()
            db.execute("UPDATE submissions SET title=? WHERE id=?", ('<script>alert("bad")</script>', submission_id))
            db.commit()
        donation_config = Path(self.temp.name) / "donations.json"
        donation_config.write_text('{"paypal_business":"","paypal_hosted_button_id":""}', encoding="utf-8")
        self.app.config["DONATIONS_CONFIG"] = str(donation_config)
        response = self.client.get("/receipt")
        self.assertIn(b"&lt;script&gt;", response.data)
        self.assertNotIn(b'<script>alert', response.data)
        self.assertNotIn(b"Donate with PayPal", response.data)

    def test_receipt_keeps_security_rejection_distinct_from_editorial_review(self) -> None:
        submission_id = self.upload()
        with self.app.app_context():
            db = get_db()
            row = db.execute("SELECT * FROM submissions WHERE id=?", (submission_id,)).fetchone()
            (Path(self.app.config["QUARANTINE"]) / row["stored_name"]).unlink()
            db.execute("UPDATE submissions SET scan_status='infected',status='removed' WHERE id=?", (submission_id,))
            db.commit()
        response = self.client.get("/receipt")
        self.assertIn(b"File rejected by safety checks", response.data)
        self.assertNotIn(b"Pending approval", response.data)
        self.assertNotIn(b"Donate with PayPal", response.data)

    def test_receipt_shows_a_later_recorded_editorial_decision(self) -> None:
        submission_id = self.upload()
        with self.app.app_context():
            db = get_db()
            db.execute("UPDATE submissions SET status='changes_requested' WHERE id=?", (submission_id,))
            db.commit()
        response = self.client.get("/receipt")
        self.assertIn(b"Changes requested", response.data)
        self.assertNotIn(b"Pending approval", response.data)

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

    def test_acceptance_requires_a_recorded_frontier_audit(self) -> None:
        submission_id = self.upload()
        token = self.login_session("operator@example.org")
        response = self.client.post(
            f"/admin/submission/{submission_id}/decision",
            data={"csrf_token": token, "action": "accept", "reason": "missing-audit"},
        )
        self.assertEqual(response.status_code, 409)

    def test_upload_stays_private_and_requires_manual_acceptance(self) -> None:
        submission_id = self.upload()
        token = self.login_session("operator@example.org")
        self.add_model_review(submission_id, 1)
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
        self.add_model_review(submission_id, 1)
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
        self.add_model_review(submission_id, 1, recommendation="reject", material=True)
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
                    "primary_subject": "airr-quantum-information",
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
            self.assertEqual(row["classification_json"], "{}")
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
