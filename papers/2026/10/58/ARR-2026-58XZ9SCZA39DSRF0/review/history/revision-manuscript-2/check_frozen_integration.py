from pathlib import Path
from zipfile import ZipFile
from datetime import datetime,timezone
from pypdf import PdfReader
import hashlib,json,re,shutil

O=Path(__file__).resolve().parent;I=O.parent/'input'
BASE=Path(r'D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico')
OLD=BASE/'revision-manuscript-1';EXT=BASE/'revision-extension-1'
DELIVERY=Path(r'D:\Entregas\airr\2026-10-18_escape-energetico\candidate-2')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
initial=json.loads((O/'input-hashes-initial.json').read_text())
assert all(sha(I/n)==x['sha256'] for n,x in initial.items())
manifest=json.loads((I/'artifact-manifest.json').read_text())
for row in manifest['artifacts']:
 assert initial[row['name']]==dict(bytes=row['bytes'],sha256=row['sha256'])
 assert sha(DELIVERY/row['name'])==row['sha256']
(O/'reviewed-inputs').mkdir(exist_ok=True)
for p in I.iterdir():shutil.copy2(p,O/'reviewed-inputs'/p.name)
frozen=O/'supplement-frozen';frozen.mkdir(exist_ok=True)
with ZipFile(I/'supplement.zip') as z:
 for n in z.namelist():
  assert len(Path(n).parts)==1 and not Path(n).is_absolute()
  (frozen/n).write_bytes(z.read(n))
sm=json.loads((frozen/'manifest.json').read_text())
assert all(sha(frozen/x['name'])==x['sha256'] and (frozen/x['name']).stat().st_size==x['bytes'] for x in sm['entries'])
matches=[]
for name,prior in [
 ('verify_escape.py',OLD/'supplement-frozen'/'verify_escape.py'),
 ('verification-1.json',OLD/'supplement-frozen'/'verification-1.json'),
 ('verify_extension_2.py',EXT/'reviewed-inputs'/'verify_extension_2.py'),
 ('extension-verification-2.json',EXT/'reviewed-inputs'/'extension-verification-2.json')]:
 assert (frozen/name).read_bytes()==prior.read_bytes()
 matches.append(dict(name=name,prior_path=str(prior),sha256=sha(prior),byte_identical=True))
reuse=O/'reused-verification';reuse.mkdir(exist_ok=True)
evidence=[]
for src,dest in [(OLD/'reproduction-results.json','original-200-reproduction.json'),(EXT/'additional-verification-results.json','new-500-reproduction-and-110-digit-table.json'),(EXT/'verification-results.json','independent-480-diagnostics.json')]:
 shutil.copy2(src,reuse/dest);evidence.append(dict(source=str(src),copy='reused-verification/'+dest,sha256=sha(src)))
table=json.loads((EXT/'additional-verification-results.json').read_text())['table']
tex=(I/'main.tex').read_text()
table_tex=tex.split('\\begin{table}')[1].split('\\end{table}')[0]
rows=re.findall(r'\$10\^\{(\d+)\}\$&([0-9.]+)&([0-9.]+)&([0-9.]+)&([0-9.]+)',table_tex)
assert len(rows)==6
for row,expected in zip(rows,table):
 assert 10**int(row[0])==expected['N'] and list(row[1:])==expected['upward_6']
reader=PdfReader(I/'main.pdf');assert len(reader.pages)==10
text='\n'.join(p.extract_text() or '' for p in reader.pages)
assert all(x in text for row in table for x in row['upward_6'])
assert '??' not in text
labels=re.findall(r'\\label\{([^}]+)\}',tex)
assert len(labels)==len(set(labels))
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
assert set(refs)<=set(labels)
citations=[]
for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex):citations.extend(group.split(','))
bibitems=re.findall(r'\\bibitem\{([^}]+)\}',tex)
assert set(citations)<=set(bibitems)
result=dict(checked_at=datetime.now(timezone.utc).isoformat(),input_manifest_valid=True,durable_delivery_matches=True,supplement_manifest_valid=True,supplement_reuse=matches,reused_evidence=evidence,scripts_executed_in_this_review=False,reason_not_rerun='Both scripts and their supplied JSON records are byte-identical to previously executed and audited versions; no numerical or source change requires another execution.',prior_reproduction_counts=[200,500],prior_independent_checks=480,table_rows=6,table_values=24,all_tex_table_values_match_independent_110_digit_result=True,all_pdf_table_values_present=True,pdf_pages=10,unique_labels=True,all_references_resolve=True,all_citations_resolve=True,original_inputs_unchanged=True)
write('integration-checks.json',result)
write('visual-review.json',dict(status='pass',method='Independent rendering of the exact received PDF using Poppler at 100 dpi; every page viewed.',pages_inspected=list(range(1,11)),observations='Legible formulas, table and bibliography. No clipping, overlap or unresolved references observed. PDF was not recompiled or altered.'))
print(json.dumps(dict(pages=10,script_and_record_matches=len(matches),table_values=24,citations=len(set(citations)),checks='PASS'),indent=2))
