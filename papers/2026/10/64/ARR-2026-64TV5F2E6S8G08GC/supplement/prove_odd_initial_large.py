"""Attempt exact shifted-coefficient certificates; no inference on failure."""
from pathlib import Path
import json,sympy as sp
R=Path(__file__).parent;data=json.loads((R/'odd-initial-five-symbolic.json').read_text())
s,k,B,u,v,w=sp.symbols('s k B u v w');out=[]
for row in data['rows']:
    for dd in row['determinants']:
        r=dd['r']
        if r==2:continue
        want=1 if r==3 else -1
        num,den=sp.fraction(sp.sympify(dd['det']))
        assert sp.Poly(den,s,k,B).total_degree()==0 and den>0
        # Remove positive factors s, s-1, s-2 to keep certificates compact.
        pp=sp.factor(want*num)
        scalar,factors=sp.factor_list(pp);core=sp.Integer(scalar)
        for f,e in factors:
            if f in [s,s-1,s-2,k,B]:continue
            core*=f**e
        certified=False
        for power,shift in [(8,20),(10,30),(12,40)]:
            lower=s**power
            recurrence=sp.Poly(sp.expand(((4*s+2)*s**power-(s+1)**(power+1)).subs(s,u+shift)),u)
            recurrence_ok=bool(all(c>=0 for c in recurrence.all_coeffs()) and recurrence.eval(0)>0)
            base_margin=sp.binomial(2*shift,shift)-shift**power
            q=sp.Poly(sp.expand(core.subs(B,lower+w).subs(k,v+3).subs(s,u+shift)),w,v,u)
            negatives=[(mon,c) for mon,c in q.terms() if c<0]
            ok=not negatives and q.eval({w:0,v:0,u:0})>0 and recurrence_ok and base_margin>0
            rec=dict(mode=row['mode'],r=r,desired_sign=want,power=power,threshold=shift,positive=len([c for c in q.coeffs() if c>0]),negative=len(negatives),base_binomial_margin=str(base_margin),binomial_recurrence_positive=recurrence_ok,proved=bool(ok))
            if ok:rec['certificate_terms']=[[list(mon),str(c)] for mon,c in q.terms()]
            else:rec['first_negative_terms']=[[list(mon),str(c)] for mon,c in negatives[:3]]
            out.append(rec);print(json.dumps({key:val for key,val in rec.items() if key not in ['certificate_terms','first_negative_terms']}),flush=True)
            if ok:certified=True;break
(R/'odd-initial-five-large-certificates.json').write_text(json.dumps(dict(rows=out),indent=2)+'\n')
