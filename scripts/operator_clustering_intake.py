"""One exact historical candidate via existing guarded authorization and API.

Decrypts to the existing host identity; never prints or exports a credential.
No access service, shell account, key, endpoint or policy is installed.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request
import uuid
import zipfile

PID = 'ARR-2026-31ED4MTKC18JPSDE'
SHA = '0701c2578111536ffed8eb97db5e95f69a5509e7337cbc9b9f1e0bc6755f0505'
ROOT = Path('/srv/airr-private/clustering-completion-20260914')
URL = 'https://github.com/arr-research/arr-research.github.io/releases/download/OPERATOR-TRANSFER-CLUSTERING-2026-09-14/clustering-20260914.zip.age'
CIPHER = 'de396acc9b6eda98faa7196e89697538f0fafa1fdd9e629b54d67248c09507d7'
PLAIN = '70f9db2e4372b37cba86779819edd00ba18e3511edee5fc669f371b224ac3e99'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    path = ROOT / name
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    path.chmod(0o600)
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['inspect', 'deposit', 'round'])
    parser.add_argument('--instruction')
    args = parser.parse_args()
    assert os.getuid() == 0
    os.umask(0o077)
    ROOT.mkdir(exist_ok=True, mode=0o700)
    encrypted = ROOT/'packet.zip.age'
    if not encrypted.exists():
        encrypted.write_bytes(urllib.request.urlopen(URL, timeout=45).read())
    assert digest(encrypted) == CIPHER
    plain = ROOT/'packet.zip'
    if not plain.exists():
        subprocess.run(['age', '-d', '-i', '/etc/ssh/ssh_host_ed25519_key', '-o', str(plain), str(encrypted)], check=True)
    assert digest(plain) == PLAIN
    packet = ROOT/'packet'
    packet.mkdir(exist_ok=True)
    with zipfile.ZipFile(plain) as z:
        for name in z.namelist():
            assert (packet/name).resolve().is_relative_to(packet.resolve())
        z.extractall(packet)
    for item in json.loads((packet/'MANIFEST.json').read_bytes()):
        assert digest(packet/item['path']) == item['sha256']
    job = json.loads((packet/'revision-job.json').read_bytes())
    binding = json.loads((packet/'binding.json').read_bytes())
    assert binding['paper_id'] == PID and binding['sha256'] == digest(packet/'paper.pdf') == SHA
    sys.path.insert(0, '/opt/airr-intake/current')
    from services.intake import app as a
    from services.intake.historical_revisions import catalogue, validate_binding
    app = a.create_app()
    def cli(*cmd):
        result = app.test_cli_runner().invoke(args=list(cmd))
        if result.exit_code:
            raise RuntimeError(result.output)
        return json.loads(result.output)
    with app.app_context():
        entries, catalogue_sha = catalogue(app)
        validate_binding(binding, entries, app.config['HISTORICAL_OPERATOR_AUTHOR'])
        db = a.get_db()
        existing = db.execute('SELECT submission_id FROM historical_revisions WHERE version_id=?', (binding['version_id'],)).fetchone()
        recent = db.execute("SELECT COUNT(*) FROM submissions WHERE owner_user_id=4 AND created_at>=?", (a.iso(a.now()-__import__('datetime').timedelta(hours=24)),)).fetchone()[0]
        if args.mode == 'inspect':
            value = {'checked_at':a.iso(), 'paper_id':PID, 'sha256':SHA, 'packet_verified':True, 'catalogue_binding_valid':True, 'owner_recent_24h_deposits':recent, 'existing_submission':existing[0] if existing else None, 'terms_version':a.TERMS_VERSION, 'privacy_version':a.PRIVACY_VERSION}
            save('inspection.json',value);print(json.dumps(value,indent=2));return
        assert args.instruction and len(args.instruction)>40
        if args.mode == 'deposit':
            if (ROOT/'receipt.json').exists():
                print((ROOT/'receipt.json').read_text());return
            assert not existing, 'Exact version already exists; retrieve its real receipt, do not redeposit.'
            assert recent < 10, 'Rolling deposit quota unavailable.'
            path = ROOT/'grant.json'
            if not path.exists():
                evidence = {'owner_user_id':4,'agent_name':'AIRR continuity coordinator','agent_version':'Codex desktop Clustering 2026-09-14','binding':binding,'author_instruction':args.instruction,'source_reference':'Current AIRR continuity conversation: next-paper instruction after verified diagonal Amos completion, with standing explicit exact-paper complete-cycle authorization.','recorded_at':a.iso(),'scope':['revision:create','submission:receipt'],'terms_version':a.TERMS_VERSION,'privacy_version':a.PRIVACY_VERSION,'operator_authorship_confirmed':True}
                save('grant.json', cli('authorize-historical-revision',str(save('historical-authorization.json',evidence))))
            grant = json.loads(path.read_bytes())
            boundary = 'AIRRClustering'+uuid.uuid4().hex
            body = (f'--{boundary}\r\nContent-Disposition: form-data; name="metadata"\r\nContent-Type: application/json\r\n\r\n'.encode()+json.dumps(job['metadata']).encode()+f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="manuscript"; filename="Clustering-v2.pdf"\r\nContent-Type: application/pdf\r\n\r\n'.encode()+(packet/'paper.pdf').read_bytes()+f'\r\n--{boundary}--\r\n'.encode())
            req = urllib.request.Request('https://submit.airr.science/api/v1/revisions',data=body,headers={'Authorization':'Bearer '+grant['agent_token'],'Idempotency-Key':job['idempotency_key'],'Content-Type':'multipart/form-data; boundary='+boundary})
            with urllib.request.urlopen(req,timeout=60) as response: raw=response.read()
            value=json.loads(raw);assert value['sha256']==SHA
            (ROOT/'receipt.json').write_bytes(raw)
            print(json.dumps(value,indent=2));return
        assert existing, 'Deposit required before a model round.'
        sid=existing[0]
        value={'submission_id':sid,'manuscript_sha256':SHA,'notice':'The author requested the complete scientific and editorial cycle for this exact Clustering PDF using identified Astra High and Sol Medium reviewers. Prior model involvement and service terms remain disclosed. No technical memory-isolation, training or retention guarantee is asserted; local preassessments remain distinct from intake reports.','author_instruction':args.instruction,'source_reference':'Explicit author instruction in current AIRR continuity conversation; recorded by authenticated Netcup operator.','authorization_recorded_at':a.iso(),'models':[{'provider':'OpenAI','model_id':'gpt-6-astra'},{'provider':'OpenAI','model_id':'gpt-5.6-sol'}],'founder_authorship_basis':'Lluis Eriksson is the sole author of the verified public historical parent and the corrected candidate and is AIRR founder-editor. This is external operator-recorded instruction, not a simulated author web signature.'}
        result=cli('prepare-founder-round',sid,str(save('round-authorization.json',value)))
        save('round-receipt.json',result)
        save('intake-review-template.json',a.model_review_template(db.execute('SELECT * FROM submissions WHERE id=?',(sid,)).fetchone()))
        print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
