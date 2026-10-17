"""Portable, read-only revision audit.

Usage: python revision_audit.py BASELINE_PACKET REVISED_PACKET OUTPUT_DIRECTORY
Run the two supplied verifiers in a writable copy separately.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, difflib, hashlib, json, re
from pypdf import PdfReader

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('baseline',type=Path)
ap.add_argument('revised',type=Path)
ap.add_argument('output',type=Path)
args=ap.parse_args()
args.output.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
oldman=json.loads((args.baseline/'manifest-sha256.json').read_text(encoding='utf-8'))
newman=json.loads((args.revised/'manifest-sha256.json').read_text(encoding='utf-8'))
oldchecks={k:sha(args.baseline/k)==v for k,v in oldman.items()}
newchecks={k:sha(args.revised/k)==v for k,v in newman.items()}
assert all(oldchecks.values()) and all(newchecks.values())
oldtex=(args.baseline/'main.tex').read_text(encoding='utf-8')
newtex=(args.revised/'main.tex').read_text(encoding='utf-8')
diff=''.join(difflib.unified_diff(oldtex.splitlines(keepends=True),newtex.splitlines(keepends=True),fromfile='baseline/main.tex',tofile='revised/main.tex'))
(args.output/'manuscript-diff.txt').write_text(diff,encoding='utf-8')
def statements(tex):
    matches=re.findall(r'\\begin\{(theorem|lemma|proposition|corollary)\}(.*?)\\end\{\1\}',tex,re.S)
    return [(kind,re.sub(r'\s+',' ',text).strip()) for kind,text in matches]
oldst,newst=statements(oldtex),statements(newtex)
assert len(oldst)==7 and oldst==newst
env=lambda s,name:re.search(r'\\begin\{'+name+r'\}(.*?)\\end\{'+name+r'\}',s,re.S).group(1)
assert env(oldtex,'abstract')==env(newtex,'abstract')
assert env(oldtex,'thebibliography')==env(newtex,'thebibliography')
changed=sorted(k for k in oldman.keys() & newman.keys() if oldman[k]!=newman[k])
added=sorted(newman.keys()-oldman.keys()); removed=sorted(oldman.keys()-newman.keys())
assert newman['main.pdf']==newman['paper.pdf']
assert newman['verify_weighted_gap.py']==oldman['verify_weighted_gap.py']
assert newman['weighted-diagnostics.json']==oldman['weighted-diagnostics.json']
newpdf=PdfReader(args.revised/'main.pdf')
assert len(newpdf.pages)==10
newtext='\n\n'.join(p.extract_text() for p in newpdf.pages)
(args.output/'revised-pdf-text.txt').write_text(newtext,encoding='utf-8')
first=newpdf.pages[0].extract_text(); second=newpdf.pages[1].extract_text()
assert 'Theorem 1.' not in first and 'Theorem 1.' in second
reproduced={name:sha(args.output/'verification'/name)==newman[name]
            for name in ['position-diagnostics.json','weighted-diagnostics.json']}
assert all(reproduced.values())
audit={
    'checked_at':datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'status':'PASS','baseline_manifest_entries':len(oldman),'revised_manifest_entries':len(newman),
    'baseline_manifest_matches':oldchecks,'revised_manifest_matches':newchecks,
    'changed_files':changed,'added_files':added,'removed_files':removed,
    'numbered_statements_checked':len(oldst),'numbered_statements_unchanged':True,
    'abstract_unchanged':True,'bibliography_unchanged':True,'weighted_verifier_byte_unchanged':True,
    'pdf_pages':len(newpdf.pages),'main_theorem_begins_on_page':2,
    'reproduced_diagnostics_byte_identical':reproduced,
    'revised_hashes_sha256':newman,
    'pdf_text_extraction_is_not_visual_verification':True,
    'no_packet_files_modified':True
}
(args.output/'revision-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:audit[k] for k in ['status','baseline_manifest_entries','revised_manifest_entries','changed_files','added_files','numbered_statements_checked','numbered_statements_unchanged','abstract_unchanged','bibliography_unchanged','pdf_pages','reproduced_diagnostics_byte_identical']},indent=2))
