"""Standing scope, expiry, exhaustion, revocation and immutable instruction evidence."""
import json
from datetime import timedelta
from pathlib import Path
import unittest

import test_agent_intake as agent_tests
from services.intake.app import get_db, iso, now


class StandingAgentTests(unittest.TestCase):
    setUp = agent_tests.AgentIntakeTests.setUp
    tearDown = agent_tests.AgentIntakeTests.tearDown
    request_grant = agent_tests.AgentIntakeTests.request_grant
    begin_confirmation = agent_tests.AgentIntakeTests.begin_confirmation
    approve = agent_tests.AgentIntakeTests.approve
    upload = agent_tests.AgentIntakeTests.upload

    def evidence(self, grant, **changes):
        value = {'grant_id':grant['request_id'],'human_name':'Operator',
                 'human_instruction':'Enable a persistent ordinary-deposit delegation for this existing authorized research workflow.',
                 'source_reference':'Explicit controller instruction recorded in the current operator conversation.',
                 'recorded_at':iso(),'scope':['submission:create','submission:receipt']}
        value.update(changes)
        path = Path(self.temp.name)/'standing-evidence.json'
        path.write_text(json.dumps(value),encoding='utf-8')
        return path

    def record(self, path):
        return self.app.test_cli_runner().invoke(args=['record-standing-agent-delegation',str(path)])

    def status(self, grant):
        return self.client.get('/api/v1/agent-authorization',headers={'Authorization':'Bearer '+grant['agent_token']}).get_json()

    def test_expired_exhausted_grant_can_continue_only_after_recorded_instruction(self):
        grant=self.request_grant(); self.approve(grant)
        with self.app.app_context():
            get_db().execute('UPDATE agent_grants SET expires_at=?,uses=5 WHERE id=?',
                             (iso(now()-timedelta(days=1)),grant['request_id']))
            get_db().commit()
        self.assertEqual(self.upload(grant).status_code,403)
        result=self.record(self.evidence(grant))
        self.assertEqual(result.exit_code,0,result.output)
        status=self.status(grant)
        self.assertEqual(status['state'],'approved')
        self.assertIsNone(status['expires_at']); self.assertIsNone(status['uploads_remaining'])
        self.assertTrue(status['standing_delegation'])
        response=self.upload(grant)
        self.assertEqual(response.status_code,201,response.data)
        self.assertEqual(self.upload(grant).get_json()['registration_number'],response.get_json()['registration_number'])
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT uses FROM agent_grants WHERE id=?',(grant['request_id'],)).fetchone()[0],6)

    def test_workspace_revocation_remains_effective_after_original_expiry(self):
        grant=self.request_grant(); human,path,csrf=self.approve(grant)
        self.assertEqual(self.record(self.evidence(grant)).exit_code,0)
        with self.app.app_context():
            get_db().execute('UPDATE agent_grants SET expires_at=? WHERE id=?',
                             (iso(now()-timedelta(days=1)),grant['request_id']))
            get_db().commit()
        response=human.post(path,data={'csrf_token':csrf})
        self.assertIn(response.status_code,(302,303))
        self.assertEqual(self.status(grant)['state'],'revoked')
        self.assertEqual(self.upload(grant).status_code,403)
        self.assertNotEqual(self.record(self.evidence(grant)).exit_code,0)

    def test_scopes_actor_and_pending_grants_are_not_escalated(self):
        grant=self.request_grant()
        self.assertNotEqual(self.record(self.evidence(grant)).exit_code,0)
        self.approve(grant)
        self.assertNotEqual(self.record(self.evidence(grant,scope=['publication:create'])).exit_code,0)
        self.assertNotEqual(self.record(self.evidence(grant,human_name='Invented editor')).exit_code,0)
        self.assertFalse(self.status(grant)['standing_delegation'])

    def test_ordinary_limit_and_changed_terms_still_apply(self):
        grant=self.request_grant(); self.approve(grant)
        with self.app.app_context():
            get_db().execute('UPDATE agent_grants SET uses=5 WHERE id=?',(grant['request_id'],));get_db().commit()
        self.assertEqual(self.status(grant)['uploads_remaining'],0)
        self.assertEqual(self.upload(grant).status_code,403)
        self.assertEqual(self.record(self.evidence(grant)).exit_code,0)
        with self.app.app_context():
            get_db().execute("UPDATE agent_grants SET terms_version='obsolete' WHERE id=?",(grant['request_id'],));get_db().commit()
        self.assertEqual(self.upload(grant).status_code,403)

    def test_evidence_is_idempotent_and_immutable(self):
        grant=self.request_grant(); self.approve(grant); path=self.evidence(grant)
        self.assertEqual(self.record(path).exit_code,0)
        replay=self.record(path)
        self.assertEqual(replay.exit_code,0,replay.output)
        self.assertTrue(json.loads(replay.output)['reused'])
        other=self.record(self.evidence(grant,source_reference='A different purported instruction must not overwrite the first.'))
        self.assertNotEqual(other.exit_code,0)

    def test_historical_revision_grants_cannot_be_extended(self):
        grant=self.request_grant(); self.approve(grant)
        with self.app.app_context():
            actor=get_db().execute("SELECT id FROM users WHERE role='operator'").fetchone()[0]
            get_db().execute('INSERT INTO historical_revision_grants VALUES(?,?,?,?,?,?)',
                             (grant['request_id'],'{}','fixture','{}','fixture',actor))
            get_db().commit()
        self.assertNotEqual(self.record(self.evidence(grant)).exit_code,0)
        self.assertFalse(self.status(grant)['standing_delegation'])
        self.assertEqual(self.status(grant)['uploads_remaining'],1)


if __name__=='__main__':
    unittest.main()
