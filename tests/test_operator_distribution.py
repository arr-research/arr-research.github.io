import contextlib
import copy
import io
import json
from pathlib import Path
import runpy
import sys
import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import test_paper_keys as fixtures
from services.intake.app import get_db

class ExternalDistributionTests(unittest.TestCase):
 def setUp(self):
  self.fixture=fixtures.PaperKeyTests();self.fixture.setUp();self.app=self.fixture.app
  _,draft=self.fixture.create();self.case=self.fixture.send(draft,authors='External Author').location.rsplit('/',1)[-1]
  with self.app.app_context():
   db=get_db();self.sha=db.execute('SELECT sha256 FROM submissions WHERE id=?',(self.case,)).fetchone()[0]
   db.execute('DELETE FROM publication_permissions WHERE submission_id=?',(self.case,));db.commit()
  self.value=dict(submission_id=self.case,manuscript_sha256=self.sha,operator_name='Operator',license='LicenseRef-Author-Retained',rights_confirmed=True,instruction='The editor confirms direct author permission to host this exact PDF and publish its review with all manuscript rights retained.',source_reference='Actual editor confirmation received in the current publication chat.',recorded_at=datetime.now(timezone.utc).isoformat())
 def tearDown(self):self.fixture.tearDown()
 def invoke(self,apply=False):
  p=Path(self.fixture.temp.name)/'authorization.json';p.write_text(json.dumps(self.value),encoding='utf-8')
  with patch('services.intake.app.app',self.app),patch.object(sys,'argv',['operator_record_distribution_permission.py',str(p)]+(['--apply'] if apply else [])),contextlib.redirect_stdout(io.StringIO()) as out:
   runpy.run_path('scripts/operator_record_distribution_permission.py',run_name='__main__')
  return json.loads(out.getvalue())
 def test_exact_permission_is_atomic_idempotent_and_not_acceptance(self):
  self.assertFalse(self.invoke()['permission_recorded'])
  self.assertTrue(self.invoke(True)['permission_recorded'])
  self.assertTrue(self.invoke(True)['already_recorded'])
  with self.app.app_context():
   db=get_db();self.assertEqual(db.execute('SELECT COUNT(*) FROM publication_permissions WHERE submission_id=?',(self.case,)).fetchone()[0],1)
   self.assertEqual(db.execute("SELECT COUNT(*) FROM audit_log WHERE submission_id=? AND event='publication_permission_recorded'",(self.case,)).fetchone()[0],1)
   row=db.execute('SELECT * FROM submissions WHERE id=?',(self.case,)).fetchone();self.assertEqual(row['status'],'eligible');self.assertIsNone(row['public_release_url']);self.assertIsNone(row['decision_by'])
 def test_false_rights_changed_hash_license_operator_and_stale_evidence_fail(self):
  original=copy.deepcopy(self.value)
  for fields in ({'rights_confirmed':False},{'manuscript_sha256':'0'*64},{'license':'CC0-1.0'},{'operator_name':'Someone else'},{'recorded_at':'2000-01-01T00:00:00Z'}):
   self.value={**original,**fields}
   with self.assertRaises(SystemExit):self.invoke(True)
  with self.app.app_context():self.assertEqual(get_db().execute('SELECT COUNT(*) FROM publication_permissions WHERE submission_id=?',(self.case,)).fetchone()[0],0)
