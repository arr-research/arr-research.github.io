# SPDX-License-Identifier: AGPL-3.0-or-later
import json
from pathlib import Path

from test_historical_revisions import HistoricalRevisionTests
from services.intake.app import get_db, iso


class ExternalWorkingPermissionTests(HistoricalRevisionTests):
    def prepared(self):
        case = self.send_revision(self.issue()).get_json()['registration_number']
        with self.app.app_context():
            get_db().execute("UPDATE users SET display_name='Operator Author' WHERE email='operator@example.org'")
            get_db().commit()
        return {'submission_id': case, 'manuscript_sha256': self.binding['sha256'], 'human_name': 'Operator Author',
                'human_instruction': 'Actual external author instruction: I authorize this exact Working paper under CC BY4.0 with CC0 metadata and confirm my rights and founder authorship.',
                'source_reference': 'Actual exact-artifact author reply fixture', 'recorded_at': iso(),
                'license': 'CC-BY-4.0', 'metadata_license': 'CC0-1.0', 'rights_confirmed': True, 'founder_authorship_confirmed': True}

    def invoke(self, evidence):
        path = Path(self.temp.name)/'working-permission.json'
        path.write_text(json.dumps(evidence))
        return self.app.test_cli_runner().invoke(args=['record-external-working-publication', str(path)])

    def test_actual_instruction_records_exact_permission_without_acceptance_or_review(self):
        evidence = self.prepared()
        result = self.invoke(evidence)
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertFalse(json.loads(result.output)['accepted'])
        self.assertFalse(json.loads(result.output)['published'])
        self.assertEqual(self.invoke(evidence).exit_code, 0)
        with self.app.app_context():
            db = get_db()
            self.assertEqual(db.execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0], 1)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM model_reviews').fetchone()[0], 0)
            row = db.execute('SELECT * FROM submissions WHERE id=?', (evidence['submission_id'],)).fetchone()
            self.assertEqual(row['status'], 'eligible')
            self.assertTrue(row['founder_authored'])
            self.assertIsNone(row['decision_by'])
            self.assertIsNone(row['public_released_at'])

    def test_missing_rights_changed_hash_stale_instruction_and_unreleasable_cases_fail(self):
        evidence = self.prepared()
        for changes in ({'rights_confirmed': False}, {'manuscript_sha256': '0'*64}, {'recorded_at': '2000-01-01T00:00:00Z'}, {'human_name': 'Other person'}, {'license': 'Other license'}):
            self.assertNotEqual(self.invoke({**evidence, **changes}).exit_code, 0)
        for status in ('declined', 'withdrawn', 'legal_hold', 'accepted_for_publication'):
            with self.app.app_context():
                get_db().execute('UPDATE submissions SET status=? WHERE id=?', (status, evidence['submission_id']))
                get_db().commit()
            self.assertNotEqual(self.invoke(evidence).exit_code, 0)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0], 0)
