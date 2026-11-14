"""One host catalogue correction, with quiescence, durable backup and readback."""
from pathlib import Path
import hashlib,json,os,sqlite3,stat,urllib.request,datetime,subprocess,sys,traceback
PID='ARR-2026-7KV9Y9ASX48H7A7N'
PREVIOUS={'record_id':'arr:record:f3da7c95-67a4-444e-a3d7-814279e5f7cd','version_id':'arr:version:ecce318a-932c-4452-a1a3-0f202a524568','version':'v8','canonical_sha256':'a4d0449b973b657a741ab4d48693d9c270320c5e8b9750ef6ad437e987927359','authors':['Lluis Eriksson']}
ENTRY={'record_id':'arr:record:f3da7c95-67a4-444e-a3d7-814279e5f7cd','version_id':'arr:version:e29c767c-1a5c-418b-a711-04a34ae18e74','version':'v9','canonical_sha256':'e4bf6bfe658a59a9a0d61dc0f5e97d530dd6dd3504ba8d51052d37d747afd3e8','authors':['Lluis Eriksson']}
P=Path('/srv/airr-private/historical-revisions/catalogue.json')
DB=Path('/srv/airr-private/instance/intake.sqlite3')
BASE=Path('/srv/airr-private')
BACK=BASE/'tep337-catalogue-before.json'
TMP=P.with_name('catalogue.json.tep337.tmp')
OUT=BASE/'tep337-catalogue-result.json'
LOG=BASE/'tep337-catalogue-attempt.json'
EXPECTED_PUBLIC_PDF_BYTES = 680930 # Exact produced PDF; public readback remains required
# Draft pin gate is before any service import, URL fetch, file write or host operation.
if (type(EXPECTED_PUBLIC_PDF_BYTES) is not int or EXPECTED_PUBLIC_PDF_BYTES <= 0
    or len(ENTRY['canonical_sha256']) != 64
    or any(c not in '0123456789abcdef' for c in ENTRY['canonical_sha256'])):
 raise RuntimeError('DRAFT337_NOT_RUNNABLE: exact released v9 PDF SHA256 and byte count pending')
def require(ok,msg):
 if not ok:raise RuntimeError(msg)
def sha(raw):return hashlib.sha256(raw).hexdigest()
def syncdir(path):
 fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY)
 try:os.fsync(fd)
 finally:os.close(fd)
def private_file(path,raw):
 fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 with os.fdopen(fd,'wb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
 syncdir(path.parent)
 require(path.read_bytes()==raw and stat.S_IMODE(path.stat().st_mode)==0o600 and path.stat().st_uid==os.geteuid(),'Private file readback differs')
def physical(path,file=True):
 require(path.resolve(strict=True)==path and not path.is_symlink(),'Physical path differs: '+str(path))
 require(stat.S_ISREG(path.stat().st_mode) if file else stat.S_ISDIR(path.stat().st_mode),'Unexpected file type')
 for parent in [path.parent,*path.parents]:
  require(not parent.is_symlink() and not (parent.stat().st_mode & 0o022),'Unsafe writable/symlink parent')
def ctl(*args):
 r=subprocess.run(['systemctl',*args],capture_output=True,text=True,timeout=45)
 require(r.returncode==0,'systemctl failed: '+str(args)+' '+r.stderr[:500]);return r.stdout.strip()
require(sys.argv[1:]==['--apply'],'Explicit --apply required')
require(os.geteuid()==0,'Authenticated root operator required')
physical(P);physical(DB);physical(BASE,False)
require(not any(p.exists() or p.is_symlink() for p in [BACK,TMP,OUT,LOG]),'Preserve previous attempt')
require(Path.cwd().resolve()==Path('/opt/airr-intake/current').resolve(strict=True),'Unexpected service checkout')
from services.intake.app import app
require(Path(app.config['DATABASE']).resolve(strict=True)==DB and Path(app.config['HISTORICAL_REVISION_CATALOGUE']).resolve(strict=True)==P,'Loaded service configuration differs')
require(app.config.get('HISTORICAL_OPERATOR_AUTHOR')=='Lluis Eriksson' and app.config.get('HISTORICAL_REVISIONS_ENABLED'),'Operator/config mismatch')
require(ctl('show','airr-intake','--property=ActiveState','--value')=='active','Service not initially active')
require(ctl('show','airr-intake','--property=KillMode','--value')=='control-group','Unexpected service drain semantics')
url='https://airr.science/papers/'+PID+'/versions/v9/'+PID+'-v9.pdf'
with urllib.request.urlopen(url,timeout=25) as response:rawpdf=response.read(1048576)
require(len(rawpdf)==EXPECTED_PUBLIC_PDF_BYTES and sha(rawpdf)==ENTRY['canonical_sha256'],'Live public predecessor bytes differ')
result={'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entry':ENTRY,'catalogue_replaced':False,'service_stop_attempted':False,'service_restarted':False,'creates_grant_receipt_scope_or_publication':False,'status':'STARTED'}
private_file(LOG,(json.dumps(result,indent=2)+'\n').encode())
db=None;error=None;raw=None
try:
 result['service_stop_attempted']=True
 ctl('stop','airr-intake')
 require(ctl('show','airr-intake','--property=ActiveState','--value')=='inactive','Service did not quiesce')
 require(ctl('show','airr-intake','--property=MainPID','--value')=='0','Service process remains')
 result['issuance_quiesced']=True
 physical(P);physical(DB)
 db=sqlite3.connect('file:'+str(DB)+'?mode=rw',uri=True,timeout=15);db.execute('BEGIN IMMEDIATE')
 raw=P.read_bytes();data=json.loads(raw)
 require(data.get(PID)==PREVIOUS,'Installed predecessor differs; preserve and reconcile')
 n=db.execute("select count(*) from historical_revision_grants h join agent_grants g on h.grant_id=g.id where g.state='approved' and g.uses=0 and julianday(g.expires_at)>julianday('now')").fetchone()[0]
 require(n==0,'Live unused historical grants; preserve them and stop')
 private_file(BACK,raw)
 before=dict(data);data[PID]=ENTRY
 require(all(data[k]==v for k,v in before.items() if k!=PID) and len(data)==len(before),'Unrelated entry differs')
 new=(json.dumps(data,sort_keys=True,indent=2)+'\n').encode();st=P.stat()
 require(P.read_bytes()==raw,'Concurrent out-of-band catalogue change')
 private_file(TMP,new)
 os.chmod(TMP,stat.S_IMODE(st.st_mode));os.chown(TMP,st.st_uid,st.st_gid)
 fd=os.open(TMP,os.O_RDONLY)
 try:os.fsync(fd)
 finally:os.close(fd)
 os.replace(TMP,P);result['catalogue_replaced']=True;syncdir(P.parent)
 actual=P.stat()
 require(P.read_bytes()==new and (actual.st_uid,actual.st_gid,stat.S_IMODE(actual.st_mode))==(st.st_uid,st.st_gid,stat.S_IMODE(st.st_mode)),'Final catalogue bytes/owner/mode differ')
 db.commit()
 result.update(status='RECONCILED_VERIFIED_PUBLIC_PREDECESSOR',old_sha256=sha(raw),new_sha256=sha(new),active_unused_grants=n,unrelated_entries_preserved=len(before)-1,public_pdf_bytes=len(rawpdf),backup_sha256=sha(BACK.read_bytes()))
except BaseException as exc:
 error=exc;result['status']='FAILED_PRESERVED';result['error']=str(exc);result['traceback']=traceback.format_exc()
finally:
 if db is not None:db.close()
 if result['service_stop_attempted']:
  try:
   ctl('start','airr-intake');result['service_restarted']=ctl('show','airr-intake','--property=ActiveState','--value')=='active'
   require(result['service_restarted'],'Service restart not active')
  except BaseException as exc:
   result['restart_error']=str(exc);result['status']='FAILED_PRESERVED';error=error or exc
 result['actual_catalogue_sha256']=sha(P.read_bytes()) if P.is_file() else None
 result['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 result['recovery_boundary']='A SQL rollback never rolls back a catalogue rename; inspect actual bytes and preserved backup before any further mutation. No automatic JSON rollback.'
 try:private_file(OUT,(json.dumps(result,indent=2)+'\n').encode())
 except BaseException as exc:
  result['result_retention_error']=str(exc);result['status']='FAILED_PRESERVED';error=error or exc
 print(json.dumps(result))
if error is not None:raise SystemExit(1)
require(result['catalogue_replaced'] and result['service_restarted'],'Incomplete outcome')
