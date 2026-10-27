from pathlib import Path
from fractions import Fraction as F
import json,hashlib,traceback
P=Path(__file__).parent;arith=P/'replay/interval1077/integer_arithmetic1077.py';ns={'__file__':str(arith)};exec(arith.read_text(encoding='utf-8'),ns)
iv,plane,saved,S=ns['iv'],ns['plane'],ns['saved'],ns['S'];rows=[]
cases=[(3,F(1,100),-F(1,8),'gap','.06388352285582','.06388352285583'),(3,F(1,1000),-F(1,8),'gap','.07668420592533','.07668420592535'),(4,F(1,100),-F(1,15),'gap','.06782712362496','.06782712362498'),(4,F(1,1000),-F(1,15),'gap','.08088908969722','.08088908969723'),(3,F(1,10**30),F(1,2),'ratio','.41495890226843','.41495890226844'),(4,F(1,10**30),F(1,2),'ratio','.44684466269731','.44684466269733')]
try:
 for d,e,lam,kind,lo,hi in cases:
  theta=F(99,100);ein,*_=plane(d,theta,e);eout,*_=plane(d,lam*theta,e)
  ratio=iv(lam*lam)*eout/ein;bench=iv(lam*lam/(lam+2*(1-lam)/(d*d)));gap=ratio-bench;target=gap if kind=='gap' else ratio
  assert gap.l>0 and F(lo)<F(target.l,S)<=F(target.h,S)<F(hi)
  rows.append({'d':d,'e':str(e),'lambda':str(lam),'theta':str(theta),'ratio':saved(ratio),'gap':saved(gap),'printed_quantity':kind,'printed_open_interval':[lo,hi],'strict_containment':True})
 out={'all_six_passed':True,'method':'Reused explicitly identified integer interval primitives from1077/1068/1054;1024bits and600term atanh tail. New1084 evaluation of all6 printed finite-phase claims, not a second independent library.','arithmetic_sha256':hashlib.sha256(arith.read_bytes()).hexdigest(),'cases':rows}
 (P/'FINITE-CERTIFICATES1084.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('All6finite-phase printed intervals strictly contain computed integer enclosures; allgaps positive.')
except Exception as ex:
 (P/'FINITE-FAILURE1084.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise
