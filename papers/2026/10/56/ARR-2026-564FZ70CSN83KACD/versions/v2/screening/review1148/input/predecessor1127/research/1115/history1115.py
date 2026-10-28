from pathlib import Path
import json,hashlib,difflib,shutil
P=Path(__file__).parent;src=Path(r'C:\Trabajo\airr\2026-10-27_fixed1110');h=P/'input-history1110';h.mkdir(exist_ok=True)
for name in ['first-check1110.py.txt','first-control1110.json.txt','INCIDENTS1110.json','DEPENDENCIES1110.json']:shutil.copyfile(src/name,h/name)
first=(src/'first-check1110.py.txt').read_text();final=(src/'check1110.py').read_text()
diff=''.join(difflib.unified_diff(first.splitlines(True),final.splitlines(True),fromfile='sealedfirstscript',tofile='sealedfinalscript'))
(P/'HISTORY_DIFF1115.txt').write_text(diff,encoding='utf-8')
a=(src/'first-control1110.json.txt').read_bytes();b=(src/'CONTROL1110.json').read_bytes()
out=dict(first_control_equals_final=a==b,both_parse_as_JSON=True,first_control_sha256=hashlib.sha256(a).hexdigest(),first_control_tail_repr=repr(a[-15:]),script_only_difference='Unused except_placeholder=0 removed; serializednewlinealreadycorrect inbothsealedscriptversions',finding='The sealed historical script/output do NOT retain the claimed literal-backslash-n malformed version. They retain a corrected parseable duplicate and an incident narrative. Raw malformedbytes cannot be attested from theseinputs.',mathematical_parameters_changed=False)
assert a==b and len(json.loads(a)['cases'])==9
(P/'HISTORY1115.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(out['finding'])
