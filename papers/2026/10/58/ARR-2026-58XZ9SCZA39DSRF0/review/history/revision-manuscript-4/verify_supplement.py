from pathlib import Path
import json,hashlib,subprocess,sys,shutil,datetime,re
out=Path(__file__).resolve().parent
base=out.parent.parent
supp=out/"supplement"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mf=json.loads((supp/"manifest.json").read_text(encoding="utf-8"))
for e in mf["entries"]:
 p=supp/e["name"]
 assert p.stat().st_size==e["bytes"] and sha(p)==e["sha256"],e["name"]
assert set(e["name"] for e in mf["entries"])==set(p.name for p in supp.iterdir() if p.name!="manifest.json")
assert all(p.suffix in [".json",".txt",".py"] for p in supp.iterdir())
old=base/"review-manuscript-3"/"output"
old5=base/"review-reduction-mixed-1"
reused=[]
for n in ["verify_escape.py","verification-1.json","verify_extension_2.py","extension-verification-2.json",
"verify_general_noise_2.py","general-noise-verification-2.json","verify_mismatch_1.py","mismatch-verification-1.json",
"verify_table_3.py","table-verification-3.json"]:
 p=old/"supplement"/n;assert sha(p)==sha(supp/n)
 reused.append(dict(file=n,sha256=sha(p),identical_evidence=str(p)))
for n in ["verify_reduction_seed_3.py","reduction-seed-verification-3.json",
"verify_mixed_correlated_4.py","mixed-correlated-verification-4.json"]:
 p=old5/"reviewed-inputs"/n;assert sha(p)==sha(supp/n)
 reused.append(dict(file=n,sha256=sha(p),identical_evidence=str(p)))
for source,target in [
(old/"supplement-verification.json","manuscript3-supplement-verification.json"),
(old/"verify_supplement.py","manuscript3-verify-supplement.py"),
(old5/"reproduction-check.json","dossiers5-6-reproduction-check.json"),
(old5/"independent-verification.json","dossiers5-7-independent-verification.json"),
(base/"review-ldoi-1"/"independent-verification.json","dossier8-independent-verification.json"),
(base/"review-ldoi-1"/"verify_ldoi_independent.py","dossier8-verify-independent.py")]:
 shutil.copy2(source,out/"reused-evidence"/target)
p=out/"reproduction"/"verify_diagonal_invariant_5";p.mkdir()
shutil.copy2(supp/"verify_diagonal_invariant_5.py",p/"verify_diagonal_invariant_5.py")
r=subprocess.run([sys.executable,"-B",str(p/"verify_diagonal_invariant_5.py")],cwd=p,text=True,capture_output=True)
(p/"stdout.txt").write_text(r.stdout,encoding="utf-8")
(p/"stderr.txt").write_text(r.stderr,encoding="utf-8")
assert r.returncode==0,r.stderr
fresh=json.loads((p/"diagonal-invariant-verification-5.json").read_text(encoding="utf-8"))
original=json.loads((supp/"diagonal-invariant-verification-5.json").read_text(encoding="utf-8"))
assert {k:v for k,v in fresh.items() if k!="created_at"}=={k:v for k,v in original.items() if k!="created_at"}
# The table formula/script/record are identical; reuse the 100-digit author rerun and independent 130-digit computation.
table=json.loads((supp/"table-verification-3.json").read_text(encoding="utf-8"))["analytic_table"]
tex=(out/"reviewed-inputs"/"main.tex").read_text(encoding="utf-8")
pdf=(out/"main-extracted.txt").read_text(encoding="utf-8")
rows=[]
for row in table:
 vals=row["upward_6"]
 assert "&".join(vals) in tex
 assert all(v in pdf for v in vals)
 rows.append(dict(N=row["N"],rounded_up_6=vals,present_in_tex_and_pdf=True))
oldcheck=json.loads((old/"supplement-verification.json").read_text(encoding="utf-8"))
assert [x["rounded_up_6"] for x in oldcheck["table_rows"]]==[x["upward_6"] for x in table]
result=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 manifest_valid=True,only_scripts_records_readme=True,reused_identical_files=reused,
 new_reproductions=[dict(script="verify_diagonal_invariant_5.py",cases=264,
 equal_except_created_at=True,summary=fresh["summary"])],
 table=dict(author_precision=100,independent_precision=130,reused_unchanged_evidence=True,entries=24,rows=rows),
 limitations="Finite algebra only, not proofs of coding/security/rates/priority. Identical successful earlier evidence reused rather than rerun.",
 passed=True)
(out/"supplement-verification.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(dict(passed=True,reused_files=len(reused),new_reproduction=fresh["summary"],table_entries=24),indent=2))

