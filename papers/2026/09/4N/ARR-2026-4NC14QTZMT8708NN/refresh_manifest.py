"""Refresh package-local diff and hashes; no network or publication operation."""
from pathlib import Path
import difflib
import hashlib
import json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    changes=[]
    for name in ['active_delay.md','verify_active_delay.py']:
        old=HERE/'evidence'/'cycle3'/name
        new=HERE/name
        changes.extend(difflib.unified_diff(
            old.read_text(encoding='utf-8').splitlines(keepends=True),
            new.read_text(encoding='utf-8').splitlines(keepends=True),
            fromfile='evidence/cycle3/'+name,tofile=name))
    (HERE/'changes_from_cycle3.diff').write_text(''.join(changes),encoding='utf-8')
    reviewed={'evidence/cycle3/active_delay.md':
              '690c4ce5b76f5d05a29e4f93ce6409e8f142187c1e5699c5713f1d1b7c4209ea',
              'evidence/cycle3/verify_active_delay.py':
              'd7c4293aba1fb98a526c2a569e45ff61249dc92cf4506ea79348578ecc7dd398'}
    for name,digest in reviewed.items():
        if sha(HERE/name)!=digest:
            raise AssertionError('Frozen reviewed source changed: '+name)
    files={p.relative_to(HERE).as_posix():sha(p) for p in sorted(HERE.rglob('*'))
           if p.is_file() and p.name!='source_manifest.json' and '__pycache__' not in p.parts}
    manifest={'package':'Complete one-state error-delay law',
              'author':'Lluis Eriksson','arr_identifier':'ARR-2026-4NC14QTZMT8708NN',
              'intended_version':1,'publication_performed_by_this_package':False,
              'reviewed_historical_source_hashes':reviewed,
              'evidence_policy':'Frozen historical paths are provenance labels; use package-relative evidence paths.',
              'review_scope':'Earlier review is tied to original hashes; inverse review is a separate record.',
              'review_limit':'Same-family internal agent review is not external or human refereeing; no ARR score asserted.',
              'files_sha256':files}
    (HERE/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','files_hashed':len(files),'frozen_source_hashes_verified':len(reviewed)}))

if __name__=='__main__':main()
