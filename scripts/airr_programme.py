#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Scoped programme client. Initial host enrollment is separate; never prints secrets."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
from datetime import datetime, timezone

if __package__:
    from . import airr_submit as intake
else:
    import airr_submit as intake


def credential_path():
    if os.name == 'nt':
        return Path(os.environ['LOCALAPPDATA'])/'AIRR/programme-access/tep.dpapi'
    return Path.home()/'.local/state/airr/programme-access/tep.json'


def controller(path):
    value = intake.load_credential(path)
    if value.get('credential_kind') != 'programme-controller':
        raise intake.ClientError('Use the separate programme credential, not an ordinary intake grant.')
    return value


def fingerprint(path):
    value = controller(path)
    return {'controller_token_sha256': hashlib.sha256(value['agent_token'].encode('ascii')).hexdigest(),
            'credential': str(Path(path).resolve()), 'secret_exposed': False}


def initialize(path):
    if not Path(path).exists():
        intake.save_credential(path, {'credential_kind': 'programme-controller',
            'agent_token': secrets.token_urlsafe(32),
            'created_at': datetime.now(timezone.utc).isoformat()})
    return {**fingerprint(path), 'server_authorization_performed': False}


def read_job(path):
    path = Path(path)
    job = json.loads(path.read_text(encoding='utf-8-sig'))
    raw, digest = intake.exact_pdf(job['pdf'])
    if job['metadata']['sha256'] != digest or not re.fullmatch(r'[A-Za-z0-9._:-]{8,80}', job['idempotency_key']):
        raise intake.ClientError('Frozen PDF or idempotency key mismatch; preserve the job.')
    return path, job, raw, digest


def child_path(path):
    return Path(str(path)+'.programme-child.dpapi')


def grant(path, credential, name, version, binding_path=None, renew=False):
    path, job, _, digest = read_job(path)
    binding = json.loads(Path(binding_path).read_text(encoding='utf-8-sig')) if binding_path else None
    if binding is not None and (not isinstance(binding, dict) or binding.get('sha256') != digest):
        raise intake.ClientError('Revision binding must name the same exact PDF.')
    request = {'sha256': digest, 'kind': 'revision' if binding is not None else 'submission',
               'binding': binding, 'agent_name': name, 'agent_version': version}
    if job.get('programme_request', request) != request:
        raise intake.ClientError('Existing programme job identity changed; reconcile it, do not mint a duplicate.')
    job['programme_request'] = request
    intake.atomic_json(path, job)
    value = intake.call('POST', '/api/v1/programme-artifact-grants', controller(credential)['agent_token'],
                        {**request, **({'renew_expired_unused': True} if renew else {})})
    if (not re.fullmatch(r'AGT-[A-F0-9]{24}', value.get('request_id', ''))
            or not re.fullmatch(r'[A-Za-z0-9_-]{43}', value.get('agent_token', ''))):
        raise intake.ClientError('Unexpected grant response; keep the same job and reconcile.')
    if job.get('grant_id', value['request_id']) != value['request_id']:
        raise intake.ClientError('A different grant already owns this job; do not replace it.')
    value['programme_request'] = request
    intake.save_credential(child_path(path), value)
    return {'request_id': value['request_id'], 'expires_at': value.get('expires_at'),
            'kind': request['kind'], 'sha256': digest, 'secret_exposed': False}


def checked_receipt(value, job, digest, size):
    request = job.get('programme_request')
    if (not request or value.get('sha256') != digest or value.get('size_bytes') != size
            or not re.fullmatch(r'SUB-[A-F0-9]{16}', value.get('registration_number', ''))):
        raise intake.ClientError('Receipt does not identify the exact frozen job.')
    if request['kind'] == 'revision' and value.get('historical_revision') != request['binding']:
        raise intake.ClientError('Receipt does not match the frozen historical binding.')
    return value


def submit(path):
    path, job, raw, digest = read_job(path)
    receipt_path = Path(str(path)+'.receipt.json')
    if receipt_path.exists():
        return checked_receipt(json.loads(receipt_path.read_text()), job, digest, len(raw))
    child = intake.load_credential(child_path(path))
    request = job.get('programme_request')
    if not request or child.get('programme_request') != request or request['sha256'] != digest:
        raise intake.ClientError('Exact child grant and frozen programme job do not match.')
    if request['kind'] not in ('submission', 'revision'):
        raise intake.ClientError('Unsupported intake kind.')
    if job.get('grant_id', child['request_id']) != child['request_id']:
        raise intake.ClientError('A different grant already owns this job.')
    state = intake.call('GET', '/api/v1/agent-authorization', child['agent_token'])
    if state.get('state') != 'approved' or not state.get('intake_open'):
        raise intake.ClientError('The exact permission/intake is unavailable; preserve the job and receipt key.')
    job['grant_id'] = child['request_id']
    intake.atomic_json(path, job)
    boundary = 'airr-'+secrets.token_hex(24)
    body = (f'--{boundary}\r\nContent-Disposition: form-data; name="metadata"\r\nContent-Type: application/json\r\n\r\n'.encode()
            +json.dumps(job['metadata'], ensure_ascii=False).encode()
            +f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="manuscript"; filename="manuscript.pdf"\r\nContent-Type: application/pdf\r\n\r\n'.encode()
            +raw+f'\r\n--{boundary}--\r\n'.encode())
    endpoint = '/api/v1/revisions' if request['kind'] == 'revision' else '/api/v1/submissions'
    value = intake.call('POST', endpoint, child['agent_token'], body,
                        {'Content-Type': 'multipart/form-data; boundary='+boundary,
                         'Idempotency-Key': job['idempotency_key']})
    checked_receipt(value, job, digest, len(raw))
    intake.atomic_json(receipt_path, value)
    return value


def working_permission(path, credential):
    path, job, raw, digest = read_job(path)
    receipt = checked_receipt(json.loads(Path(str(path)+'.receipt.json').read_text()), job, digest, len(raw))
    request = {'submission_id': receipt['registration_number'], 'sha256': digest}
    value = intake.call('POST', '/api/v1/programme-working-paper-permissions',
                        controller(credential)['agent_token'], request)
    if (value.get('submission_id') != request['submission_id'] or value.get('sha256') != digest
            or value.get('publication_permission_recorded') is not True
            or value.get('public_status') != 'working_paper' or value.get('published') is not False):
        raise intake.ClientError('Unexpected permission response; no editorial acceptance/publication is inferred.')
    intake.atomic_json(Path(str(path)+'.working-permission.json'), value)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--credential', type=Path, default=credential_path())
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('initialize')
    commands.add_parser('fingerprint')
    prep = commands.add_parser('prepare')
    prep.add_argument('pdf', type=Path)
    prep.add_argument('metadata', type=Path)
    prep.add_argument('job', type=Path)
    issue = commands.add_parser('grant')
    issue.add_argument('job', type=Path)
    issue.add_argument('--agent-name', required=True)
    issue.add_argument('--agent-version', required=True)
    issue.add_argument('--binding', type=Path)
    issue.add_argument('--renew-expired-unused', action='store_true')
    for name in ('submit', 'working-permission'):
        commands.add_parser(name).add_argument('job', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'initialize':
            result = initialize(args.credential)
        elif args.command == 'fingerprint':
            result = fingerprint(args.credential)
        elif args.command == 'prepare':
            result = intake.prepare(args.pdf, args.metadata, args.job)
        elif args.command == 'grant':
            result = grant(args.job, args.credential, args.agent_name, args.agent_version,
                           args.binding, args.renew_expired_unused)
        elif args.command == 'submit':
            result = submit(args.job)
        else:
            result = working_permission(args.job, args.credential)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (intake.ClientError, OSError, ValueError, KeyError) as error:
        parser.exit(2, str(error)+'\n')


if __name__ == '__main__':
    main()
