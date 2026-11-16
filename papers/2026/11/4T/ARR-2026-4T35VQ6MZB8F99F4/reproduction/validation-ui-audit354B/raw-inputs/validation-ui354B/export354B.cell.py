# Export actual bytes, including failure receipts if present. Export is not an acceptance verdict.
core=BASE/'validation354A-receipts.zip'
if core.is_file() and not core.is_symlink():
    raw=core.read_bytes();need(len(raw)<64_000_000,'Bounded actual validation receipt ZIP')
    alias=UI/'validation354B-receipts.zip';publish_bytes(alias,raw,len(raw),digest(raw))
    print('VALIDATION354B_ZIP '+json.dumps(dict(name=alias.name,bytes=len(raw),sha256=digest(raw),
          base64=base64.b64encode(raw).decode(),native_internal_names_unchanged=True)))
else:
    print('No native validation ZIP exists. Exporting only actual UI observations; no success claimed.')
files={}
for path in sorted(UI.iterdir()):
    if path.is_file() and not path.is_symlink() and path.suffix in ('.json','.raw','.stdout','.stderr','.exit'):
        files[path.name]=path.read_bytes()
for name in ('transport-readback.json',):
    path=BASE/name
    if path.is_file() and not path.is_symlink():files[name]=path.read_bytes()
need(sum(len(b) for b in files.values())<32_000_000,'Bounded actual UI receipts')
manifest=dict(source=SOURCE,status='ACTUAL_TRANSPORT_OBSERVATIONS_NOT_A_REVIEW',
    download_event_claim=False,validation_runtime_closed=False,billed_units=None,
    files=[dict(path=n,bytes=len(b),sha256=digest(b)) for n,b in sorted(files.items())])
files['UI-RETURN-MANIFEST354B.json']=(json.dumps(manifest,indent=2)+'\n').encode()
stream=io.BytesIO()
with zipfile.ZipFile(stream,'w',zipfile.ZIP_DEFLATED) as z:
    for name,raw in sorted(files.items()):z.writestr(name,raw)
raw=stream.getvalue()
with zipfile.ZipFile(io.BytesIO(raw)) as z:
    need(set(z.namelist())==set(files) and len(z.namelist())==len(files),'UI ZIP exact members')
    for name,b in files.items():need(z.read(name)==b,'UI ZIP raw readback')
path=UI/'validation-ui354B-receipts.zip';publish_bytes(path,raw,len(raw),digest(raw))
print('UI354B_ZIP '+json.dumps(dict(name=path.name,bytes=len(raw),sha256=digest(raw),base64=base64.b64encode(raw).decode())))
print('Retain and verify both actual byte returns, then disconnect this own validation runtime and record actual closure separately.')
