"""Versioned, exact-PDF permissions granted at submission, never backfilled."""
import hashlib
import json

VERSION = 'AIRR-SEND-1.0'
PROVIDERS = ('OpenAI', 'Anthropic', 'Google', 'OpenRouter')
NOTICE = ("AIRR may send this manuscript to OpenAI, Anthropic, Google or OpenRouter "
          "for AI assessment and originality checking, using models selected by the editor. "
          "OpenRouter may route it to the named providers only. AIRR must use services with "
          "no model-training use and appropriate confidentiality and transfer safeguards; "
          "retention and processing location depend on the selected service, including possible "
          "processing outside the EEA. No zero-retention guarantee is made. The editor records "
          "the actual provider, model and service controls in your case. Your PDF, author credit, "
          "metadata, assessments and editorial decisions may be published worldwide after checks, "
          "as a Working paper or Accepted record under the selected manuscript license. "
          "Metadata is CC0. Third-party material retains its own rights. Submission does not "
          "guarantee acceptance or publication. Check decisions and requests with your secret key; "
          "no email or further permission click is required within this scope.")
LICENSES = {'CC-BY-4.0', 'CC-BY-SA-4.0', 'CC0-1.0'}


def policy():
    value = dict(version=VERSION, providers=list(PROVIDERS), notice=NOTICE)
    value['hash'] = hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()
    return value


def migrate(db):
    db.execute("""CREATE TABLE IF NOT EXISTS submission_permissions (
        submission_id TEXT PRIMARY KEY REFERENCES submissions(id),
        manuscript_sha256 TEXT NOT NULL, actor_user_id INTEGER NOT NULL REFERENCES users(id),
        policy_json TEXT NOT NULL, license TEXT NOT NULL, authorized_at TEXT NOT NULL)""")


def validate_agreement(form):
    value = policy()
    if not form.get('agreement') or form.get('permission_policy') != value['hash']:
        raise ValueError('Read and accept the current submission permissions before sending.')
    license_id = form.get('publication_license')
    if license_id not in LICENSES:
        raise ValueError('Choose a manuscript publication license before sending.')
    return dict(policy=value, license=license_id)


def record(db, case_id, actor, permission, timestamp):
    checksum = db.execute('SELECT sha256 FROM submissions WHERE id=?', (case_id,)).fetchone()[0]
    db.execute('INSERT INTO submission_permissions VALUES(?,?,?,?,?,?)',
               (case_id, checksum, actor, json.dumps(permission['policy'], sort_keys=True), permission['license'], timestamp))
    db.execute('INSERT INTO publication_permissions VALUES(?,?,?,?)',
               (case_id, checksum, permission['license'], timestamp))
    db.execute('INSERT INTO audit_log(occurred_at,actor_user_id,event,submission_id,detail_json) VALUES(?,?,?,?,?)',
               (timestamp, actor, 'submission_permissions_granted', case_id,
                json.dumps(dict(policy=permission['policy'], license=permission['license'], sha256=checksum))))


def get(db, row):
    saved = db.execute('SELECT * FROM submission_permissions WHERE submission_id=? AND manuscript_sha256=?',
                       (row['id'], row['sha256'])).fetchone()
    return saved


def permits(saved, providers):
    allowed = {name.casefold() for name in json.loads(saved['policy_json'])['providers']}
    return all(item['provider'].strip().casefold() in allowed for item in providers)
