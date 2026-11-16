# Run after the native attempt, including a failed attempt, to preserve surviving evidence.
# Actual rendered base64 only: no browser-download or runtime-closure claim.
need((UI/'outer-launch354D.observation.json').is_file(),'No actual native-attempt observation')
receipt_zip=UI/'notebook-receipts354D.zip'
need(not receipt_zip.exists() and not receipt_zip.is_symlink(),'Preserve previous receipt export; do not rebuild it')
members={}
for path in sorted(UI.iterdir()):
    if path==receipt_zip:continue
    need(path.is_file() and not path.is_symlink(),'Unexpected notebook evidence directory/symlink')
    name='notebook/'+safe(path.name);need(name not in members,'Duplicate receipt name');members[name]=path
for path in sorted((P/'gates').rglob('*')):
    need(not path.is_symlink(),'Gate symlink in export')
    if not path.is_file():continue
    need(path.resolve().is_relative_to((P/'gates').resolve()),'Gate export boundary')
    name='gates/'+safe(path.relative_to(P/'gates').as_posix())
    need(name not in members,'Duplicate gate receipt');members[name]=path
need(len(members)<=40,'Bounded notebook receipt universe')
receipt_rows=[];total=0
with zipfile.ZipFile(receipt_zip,'x',zipfile.ZIP_DEFLATED) as z:
    for name,path in members.items():
        raw=path.read_bytes();total+=len(raw);need(total<=64*1024*1024,'Notebook evidence byte bound')
        z.writestr(name,raw);receipt_rows.append({'path':name,'bytes':len(raw),'sha256':sha(raw)})
    z.writestr('NOTEBOOK-RECEIPT-MANIFEST.json',json.dumps(receipt_rows,indent=2)+'\n')
result=Path('/content/tep354D-return.zip')
exports=[]
for path in (result,receipt_zip):
    if not path.exists():continue
    need(path.is_file() and not path.is_symlink(),'Unsafe actual export path')
    raw=path.read_bytes();need(len(raw)<=512*1024*1024,'Bounded rendered transport required')
    exports.append({'name':path.name,'bytes':len(raw),'sha256':sha(raw),
                    'base64':base64.b64encode(raw).decode('ascii')})
print(json.dumps({'source':SOURCE,'transport':'actual rendered notebook base64 output',
 'producer_return_exists':result.is_file(),'browser_download_completion_observed':False,
 'runtime_closure_observed':False,'return_validation_performed':False,'files':exports}))
# After exact bytes are saved and independently checked, close ONLY this own runtime
# and observe its absence. If output is truncated, retain ZIPs and re-render their
# existing bytes through a separately observed read-only transport; never invent a receipt.