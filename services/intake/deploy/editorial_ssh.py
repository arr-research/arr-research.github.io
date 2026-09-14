"""Forced SSH entry point for bounded founder editorial operations.

Install this file root-owned outside the service-writable tree. The entry point
drops to airr-intake before loading the application. No shell, paths, SQL, code,
environment variables, files or network destinations are accepted from clients.
"""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timezone

MAX_REQUEST = 400_000
OPERATIONS = {
    'inspect-case': (),
    'prepare-founder-round': ('authorization',),
    'record-assessment': ('report', 'runtime'),
    'record-external-founder-decision': ('evidence',),
    'record-external-founder-publication': ('evidence',),
    'mark-published': (),
}


def parse_request(raw, original_command):
    if original_command != 'airr-editorial-v1' or len(raw) > MAX_REQUEST:
        raise ValueError('Unsupported command or request size.')
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError('Duplicate JSON key.')
            out[key] = value
        return out
    request = json.loads(raw, object_pairs_hook=unique)
    if not isinstance(request, dict):
        raise ValueError('Object required.')
    operation = request.get('operation')
    if not isinstance(operation, str) or operation not in OPERATIONS:
        raise ValueError('Unsupported operation.')
    fields = {'operation', 'submission_id', 'manuscript_sha256'}
    fields.update(OPERATIONS[operation])
    if operation == 'mark-published':
        fields.add('release_url')
    if set(request) != fields:
        raise ValueError('Exact request schema required.')
    for key, pattern in [('submission_id', r'SUB-[A-F0-9]{16}'),
                         ('manuscript_sha256', r'[a-f0-9]{64}')]:
        if not isinstance(request[key], str) or not re.fullmatch(pattern, request[key]):
            raise ValueError('Invalid exact case binding.')
    if operation == 'mark-published':
        url = request['release_url']
        if not isinstance(url, str) or not re.fullmatch(
            r'https://github\.com/arr-research/arr-research\.github\.io/releases/tag/ARR-[0-9]{4}-[A-Z0-9]{16}-v[1-9][0-9]*', url):
            raise ValueError('AIRR immutable release URL required.')
    blobs = {}
    for field in OPERATIONS[operation]:
        text = request[field]
        if not isinstance(text, str):
            raise ValueError('Base64 evidence required.')
        blob = base64.b64decode(text, validate=True)
        limit = 128_000 if field in {'report', 'runtime', 'authorization'} else 20_000
        if len(blob) > limit:
            raise ValueError('Evidence too large.')
        value = json.loads(blob, object_pairs_hook=unique)
        if not isinstance(value, dict):
            raise ValueError('Structured evidence required.')
        # Runtime evidence has a report digest; all other files bind the case.
        if field != 'runtime':
            if value.get('submission_id') != request['submission_id'] or value.get('manuscript_sha256') != request['manuscript_sha256']:
                raise ValueError('Evidence does not bind the requested case/hash.')
        blobs[field] = blob
    return request, blobs


def case_guard(app, a, request):
    db = a.get_db()
    row = db.execute('SELECT * FROM submissions WHERE id=?', (request['submission_id'],)).fetchone()
    author = app.config.get('HISTORICAL_OPERATOR_AUTHOR')
    binding = db.execute('SELECT binding_json FROM historical_revisions WHERE submission_id=?', (request['submission_id'],)).fetchone()
    actor = db.execute("SELECT * FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL", (app.config['OPERATOR_EMAIL'],)).fetchone()
    if not author or not actor or actor['display_name'] != author or not row or row['authors'] != author or not binding:
        raise ValueError('Only configured sole-author historical cases are accessible.')
    if row['sha256'] != request['manuscript_sha256']:
        raise ValueError('Case hash mismatch.')
    pdf = Path(app.config['QUARANTINE']) / row['stored_name']
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != row['sha256']:
        raise ValueError('Stored PDF integrity mismatch.')
    return row, json.loads(binding['binding_json'])


def dispatch(app, a, request, blobs):
    with app.app_context():
        row, binding = case_guard(app, a, request)
        operation = request['operation']
        if operation == 'inspect-case':
            db = a.get_db()
            reports = db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id', (row['id'],)).fetchall()
            permission = db.execute('SELECT * FROM publication_permissions WHERE submission_id=?', (row['id'],)).fetchone()
            return {'checked_at': datetime.now(timezone.utc).isoformat(),
                    'submission': {k: row[k] for k in ['id','sha256','status','scan_status','decision_by','decided_at','public_release_url','public_released_at']},
                    'historical_binding': binding,
                    'pdf_sha256_verified': row['sha256'],
                    'reports': [{'id': r['id'], 'response_sha256': r['response_sha256'], 'response': json.loads(r['response_json'])} for r in reports],
                    'publication_permission': None if permission is None else {k: permission[k] for k in ['manuscript_sha256','license']},
                    'model_gate_ready': app.extensions['editorial']['can_accept'](row, reports)}
        if operation == 'mark-published':
            tag = f"{binding['paper_id']}-{binding['version']}"
            if request['release_url'].rsplit('/', 1)[-1] != tag:
                raise ValueError('Release must identify this historical version.')
            if row['public_release_url']:
                raise ValueError('Release already recorded; inspect before retrying.')
        with tempfile.TemporaryDirectory(prefix='airr-editorial-') as directory:
            files = []
            for field in OPERATIONS[operation]:
                path = Path(directory) / (field + '.json')
                path.write_bytes(blobs[field])
                path.chmod(0o600)
                files.append(str(path))
            args = [operation]
            if operation == 'prepare-founder-round':
                args.append(row['id'])
            args += files
            if operation == 'mark-published':
                args += [row['id'], request['release_url']]
            result = app.test_cli_runner().invoke(args=args)
            if result.exit_code:
                # No traceback, internal paths, secrets or supplied evidence in response.
                raise ValueError('Application rejected the operation; inspect the case before retrying.')
            try:
                output = json.loads(result.output)
            except ValueError:
                output = {'recorded': True, 'operation': operation, 'submission_id': row['id']}
            return output


def main():
    import pwd
    try:
        request, blobs = parse_request(sys.stdin.buffer.read(MAX_REQUEST + 1), os.environ.get('SSH_ORIGINAL_COMMAND'))
        if os.getuid() != 0:
            raise ValueError('Root-owned launcher required.')
        account = pwd.getpwnam('airr-intake')
        os.setgroups([])
        os.setgid(account.pw_gid)
        os.setuid(account.pw_uid)
        os.umask(0o077)
        # Deployment path is fixed and administrator-owned, never client input.
        sys.path.insert(0, '/opt/airr-intake/current')
        from services.intake import app as a
        print(json.dumps(dispatch(a.create_app(), a, request, blobs), ensure_ascii=False))
        return 0
    except Exception:
        print(json.dumps({'error': 'Request rejected; no automatic retry. Inspect case state before repeating a mutation.'}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
