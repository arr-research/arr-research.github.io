"""Separate internal review checks; imports no constructing-agent verifier.

Run: python quantum_composite_review_checks.py --source-dir .
     python quantum_composite_review_checks.py --source-dir . --pdf quantum.pdf
All mathematical decisions use exact integer/algebraic arithmetic. PDF text
checks supplement the separately recorded visual review, not replace it.
"""
from pathlib import Path
from itertools import product
from math import gcd
import argparse
import hashlib
import json
import time
import sympy as S

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def group(d,u,v):
    return {((a*u[0]+b*v[0])%d,(a*u[1]+b*v[1])%d)
            for a,b in product(range(d),repeat=2)}

def det(u,v):return u[0]*v[1]-u[1]*v[0]

def arithmetic():
    rows=[]
    for d in [6,8,9,10,12,15,16,18,20,24,25,27,30,36]:
        pairs=set()
        for j in range(1,31):
            pairs.add(((j%d,(j*j+1)%d),((3*j+2)%d,(j*j+5*j+3)%d)))
        divisors=[a for a in range(1,d) if d%a==0]
        pairs.update(((a,0),(0,b)) for a,b in product(divisors,repeat=2))
        pairs.update(((a,0),((2*a)%d,0)) for a in divisors)
        checked=0; classes=set()
        for u,v in sorted(pairs):
            if u==v or u==(0,0) or v==(0,0):continue
            H=group(d,u,v)
            radical={r for r in H if det(r,u)%d==0 and det(r,v)%d==0}
            gg=gcd(d,det(u,v));q=d//gg
            qH={(q*x%d,q*y%d) for x,y in H}
            assert radical==qH
            h=len(radical)
            assert len(H)==q*q*h and d%(q*h)==0
            m=d//(q*h)
            assert m==gcd(gg,*u,*v,det(u,v)//gg)
            if gcd(d,*u,*v)==1:assert m==1
            if len(S.factorint(d))==1 and q>1:assert m==1
            # The label-group calculation is lift-free; test the optional formula
            # with several different lifts, including negative coordinates.
            for ku,kv in [((1,-1),(-1,2)),((-2,0),(1,-1))]:
                uu=tuple(u[i]+d*ku[i] for i in range(2))
                vv=tuple(v[i]+d*kv[i] for i in range(2))
                delta=det(uu,vv);gl=gcd(d,delta)
                assert gl==gg and gcd(gl,*uu,*vv,delta//gl)==m
            classes.add((q,h,m));checked+=1
        rows.append({'d':d,'label_pairs':checked,'classes_q_h_m':sorted(classes)})
    return rows

def weyl(d,a,b):
    # Build actual matrices from the definition, with exact root-of-unity entries.
    W=S.zeros(d)
    for j in range(d):
        phase=S.expand_complex(S.exp(2*S.pi*S.I*S.Rational((b*j)%d,d)))
        W[(j+a)%d,j]=phase
    return W

def matrix_cases():
    omega3=(-1+S.sqrt(3)*S.I)/2
    definitions=[
      ('published_even_sharp',36,(3,0),(-3,18),1,1,S.I,6),
      ('published_zero_constant_control',12,(1,0),(1,6),0,1,1,6),
      ('additional_odd_three_order_five_copies',15,(5,0),(0,5),-S.real_root(2,3),1,1,5),
      ('additional_odd_commuting_two_zeros',15,(0,5),(0,10),omega3,-(1+omega3),1,10),
      ('additional_odd_zero_constant_control',15,(1,0),(1,5),0,1,-1,5),
      ('even_commuting_two_zeros',12,(0,3),(0,6),S.I,-(1+S.I),1,6)]
    records=[]
    for name,d,u,v,c,a,b,expected in definitions:
        U,V=weyl(d,*u),weyl(d,*v)
        q=d//gcd(d,det(u,v));H=group(d,u,v)
        h=len({(q*x%d,q*y%d) for x,y in H});m=d//(q*h)
        D=c*S.eye(d)+a*U+b*V
        central=c**q*S.eye(d)-(-1)**q*(a**q*(U**q)+b**q*(V**q))
        central=central.applyfunc(S.simplify)
        Dm=D.to_DM(extension=True);nullity=d-Dm.rank()
        central_nullity=d-central.to_DM(extension=True).rank()
        assert nullity==expected and central_nullity==q*nullity
        if c!=0:assert nullity<=m*min(2,h)
        else:assert nullity>2*m
        records.append({'name':name,'d':d,'u':u,'v':v,'c':str(c),'a':str(a),'b':str(b),
                        'q':q,'h':h,'m':m,'exact_nullity':nullity,'exact_rank':d-nullity,
                        'central_exact_nullity':central_nullity,'exact_field':str(Dm.domain)})
    return records

def determinant_signs():
    # Independent polynomial resultant, including q=1 and even composite q.
    z,c,a=S.symbols('z c a');checks=[]
    for q in [1,2,3,4,6,9,10,12,18]:
        # Product via characteristic polynomial of all q-th roots, independent
        # of the constructing verifier's custom cyclotomic product routine.
        resultant=S.resultant(z**q-1,c+a*z,z)
        assert S.expand(resultant-c**q+(-a)**q)==0
        # Cycle permutation contribution has sign (-1)^(q-1).
        if q>1:
            weights=S.symbols('b0:'+str(q));cyclic=S.zeros(q)
            for j in range(q):cyclic[(j+1)%q,j]=weights[j]
            assert S.expand(cyclic.det()-(-1)**(q-1)*S.prod(weights))==0
        checks.append(q)
    return checks

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-dir',type=Path,required=True)
    parser.add_argument('--pdf',type=Path)
    args=parser.parse_args();start=time.monotonic()
    files=[args.source_dir/name for name in ['quantum_weyl_trinomials.md','quantum_weyl_verify.py',
                                           'composite_matrix_checks.py']]
    report={'status':'PASS','independence':'Separate reviewing agent; no import or execution of constructing verifiers. Same model family, not external refereeing.',
            'source_hashes':{p.name:sha(p) for p in files},'arithmetic':arithmetic(),
            'matrix_cases':matrix_cases(),'determinant_orders':determinant_signs()}
    if args.pdf:
        from pypdf import PdfReader
        pdf=PdfReader(args.pdf)
        text='\n'.join(p.extract_text() or '' for p in pdf.pages)
        required=['A universal central reduction','central sectors and their multiplicity',
                  'universal trinomial rank rule','Arithmetic evaluation','prime-power case',
                  'Composite multiplicities and a necessary coefficient hypothesis',
                  'zero-constant negative control','two-sector bound','Lluis Eriksson']
        flags={s:s.lower() in text.lower() for s in required}
        assert all(flags.values()),flags
        report['pdf']={'sha256':sha(args.pdf),'pages':len(pdf.pages),'text_markers':flags,
                       'limitation':'Mathematical display correspondence and layout require the recorded visual review.'}
    report['checker_sha256']=sha(Path(__file__))
    report['elapsed_seconds']=round(time.monotonic()-start,3)
    report['limits']=['Finite exact examples supplement the analytic delta review.',
                      'No proof-assistant kernel replay or external priority determination.',
                      'No constructing-agent verifier is imported or executed.']
    (HERE/'quantum_composite_review_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'label_pairs':sum(x['label_pairs'] for x in report['arithmetic']),
                      'direct_matrix_cases':len(report['matrix_cases']),'determinant_orders':len(report['determinant_orders']),
                      'elapsed_seconds':report['elapsed_seconds']}))

if __name__=='__main__':main()
