from pathlib import Path
import runpy,json
P=Path(__file__).parent
try:runpy.run_path(str(P/'own1148_initial.py'))
except Exception as ex:
 t=ex.__traceback__
 while t.tb_next:t=t.tb_next
 q=t.tb_frame.f_locals;m=t.tb_frame.f_globals['mp']
 out={k:m.nstr(q[k],100) for k in ['Di','Do','Db','p','q']}
 out['Do_minus_Di']=m.nstr(q['Do']-q['Di'],30)
 out['diagnosis']='Chained tolerance expression adds same tolerance to both final terms, cancelling it. Disjoint-support channel is an exact equality case.'
 (P/'OWN-DIAGNOSIS1148.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(out))
