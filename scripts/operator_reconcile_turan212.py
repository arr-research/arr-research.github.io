# SPDX-License-Identifier: AGPL-3.0-or-later
"""Existing AIRR host only: reconcile the verified historical Turan v1 entry.
Default is read-only. Never creates programme scope, grants, cases or permissions.
"""
import argparse,hashlib,json,os,sqlite3,stat,urllib.request
from pathlib import Path

def read_public(url,limit,headers=None):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AIRR-programme-integrity',**(headers or {})}),timeout=30) as response:
        raw=response.read(limit+1)
    if len(raw)>limit:raise RuntimeError('Oversized public artifact')
    return raw

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    if os.name!='posix':raise RuntimeError('Existing AIRR Linux host only')
    pid='ARR-2026-72G1SSCNNG8YDVC2'
    entry={'record_id':'arr:record:e2807396-56b0-479b-b60b-3229e1a6e6c8','version_id':'arr:version:85887c0e-1e00-489b-97f0-8b6e6a721191','version':'v1','canonical_sha256':'b6307a215b321c380f1f76b117e6cb6c660239c176b0b25c45fe2fe5a3c59d50','authors':['Lluis Eriksson']}
    root='https://raw.githubusercontent.com/arr-research/arr-research.github.io/8174a68cb296a9e85abcc8a3dee5c4468ee3dadf/'
    meta=json.loads(read_public(root+'papers/2026/07/72/'+pid+'/metadata.json',100000))
    if meta['id']!=pid or meta['authors']!=[{'name':'Lluis Eriksson','affiliation':'Independent researcher'}] or any(meta[k]!=entry[k] for k in ('record_id','version_id','version')) or meta['integrity']['canonical_sha256']!=entry['canonical_sha256']:
        raise RuntimeError('Immutable public metadata identity/author mismatch')
    pdf=read_public('https://api.github.com/repos/arr-research/arr-research.github.io/releases/assets/536420512',1000000,{'Accept':'application/octet-stream'})
    if len(pdf)!=305866 or hashlib.sha256(pdf).hexdigest()!=entry['canonical_sha256']:raise RuntimeError('Existing public v1 PDF bytes mismatch')
    p=Path('/srv/airr-private/historical-revisions/catalogue.json').resolve();raw=p.read_bytes();data=json.loads(raw)
    old=data.get(pid)
    if old==entry:
        print(json.dumps({'status':'already_reconciled','entry':entry,'mutated':False}));return
    if old is not None:raise RuntimeError('Unexpected existing entry; inspect it instead of overwriting')
    db=sqlite3.connect('/srv/airr-private/instance/intake.sqlite3',timeout=15)
    try:
        db.execute('BEGIN IMMEDIATE')
        active=db.execute("select count(*) from historical_revision_grants h join agent_grants g on h.grant_id=g.id where g.state='approved' and g.uses=0 and julianday(g.expires_at)>julianday('now')").fetchone()[0]
        if active:raise RuntimeError('Live unused historical grant; do not invalidate another job')
        result={'status':'verified_missing_historical_v1','old_sha256':hashlib.sha256(raw).hexdigest(),'active_unused_grants':active,'unrelated_entries_preserved':len(data),'entry':entry,'mutated':False,'creates_permission':False}
        if not args.apply:
            print(json.dumps(result));return
        if p.read_bytes()!=raw:raise RuntimeError('Concurrent catalogue change')
        backup=Path('/srv/airr-private/tep-catalogue-before208-turan-v1.json')
        with backup.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
        os.chmod(backup,0o600)
        original=dict(data);data[pid]=entry
        if any(data[k]!=v for k,v in original.items()):raise RuntimeError('Unrelated entry changed')
        new=(json.dumps(data,sort_keys=True,indent=2)+'\n').encode();tmp=p.with_name('catalogue.208-turan.tmp');st=p.stat()
        with tmp.open('xb') as f:f.write(new);f.flush();os.fsync(f.fileno())
        os.chmod(tmp,stat.S_IMODE(st.st_mode));os.chown(tmp,st.st_uid,st.st_gid);os.replace(tmp,p)
        if p.read_bytes()!=new:raise RuntimeError('Catalogue readback mismatch')
        db.commit();result.update(status='reconciled_verified_public_v1',new_sha256=hashlib.sha256(new).hexdigest(),mutated=True,backup=str(backup));print(json.dumps(result))
    finally:db.rollback();db.close()

if __name__=='__main__':main()
