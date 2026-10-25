from pathlib import Path
import runpy,json,time
r=Path(__file__).resolve().parent
e=runpy.run_path(str(r/'werner412-h-sector.py'));s=e['s'];simp=e['simp'];Ts=e['Ts'];Hb=e['Hb'];w=e['w'];product=e['product']
X=s.Matrix(3,3,lambda i,j:int(i==(j+1)%3));Z=s.diag(1,w,w**2)
ops={'Z':Z,'X':X,'XZ':X*Z,'XZ2':X*Z**2}
Ps={name:[((s.eye(3)+w**((-k)%3)*U+w**((-2*k)%3)*U**2)/3).applyfunc(simp) for k in range(3)] for name,U in ops.items()}
for projs in Ps.values():
 assert sum(projs,s.zeros(3))==s.eye(3)
 for k,P in enumerate(projs):
  assert s.trace(P)==1 and (P*P-P).applyfunc(simp)==s.zeros(3) and P.H==P
  for j,Q in enumerate(projs):assert (P*Q).applyfunc(simp)==(P if k==j else s.zeros(3))
for name,projs in Ps.items():
 for other,qs in Ps.items():
  if name!=other:
   for P in projs:
    for Q in qs:assert simp(s.trace(P*Q))==s.Rational(1,3)
swap=s.Matrix(9,9,lambda i,j:int(i//3==j%3 and i%3==j//3))
assert (sum((s.kronecker_product(P,P) for ps in Ps.values() for P in ps),s.zeros(9))-s.eye(9)-swap).applyfunc(simp)==s.zeros(9)
def eq(A,B):return (A-B).applyfunc(simp)==s.zeros(3)
records=[]
for sector,T in Ts.items():
 if sector==(0,0):continue
 Bs={key:(T.H*H*T/3).applyfunc(simp) for key,H in Hb.items()}
 Ds={key:(4*B-2*int(key[0]==key[1])*s.eye(3)).applyfunc(simp) for key,B in Bs.items()}
 axes=[name for name,U in ops.items() if all(eq(U*B,B*U) for B in Ds.values())]
 assert len(axes)==1
 axis=axes[0];outP=Ps[axis];effects=[];matches=[]
 for P in outP:
  F=s.Matrix(3,3,lambda j,i:simp(s.trace(P*Ds[i,j])))
  assert eq(F*F,F) and s.trace(F)==1 and eq(F.H,F)
  match=[(name,k) for name,projs in Ps.items() for k,Q in enumerate(projs) if eq(F,Q)]
  assert len(match)==1
  effects.append(F);matches.append(match[0])
 assert sum(effects,s.zeros(3)).applyfunc(simp)==s.eye(3)
 for key,B in Ds.items():assert eq(B,sum((effects[k][key[1],key[0]]*outP[k] for k in range(3)),s.zeros(3)))
 records.append({'sector':sector,'output_axis':axis,'input_axis_and_label_for_each_output_label':matches})
 print(records[-1],flush=True)
out={'status':'PASS_EXACT_ALL_COMPLEX_LOGICAL_MATRIX_UNITS','sector_maps':records,'code_sector':'H00(X)=Tr(X) I/2+X/8','noncode_sector':'Hs(X)=Tr(X) I/2+sum_k Tr(Fs,k X) Ps,k/4','inverse_unit_pure_code':'2I-(2/5)psi psi*','inverse_unit_noncode':'sum_k 4 Ps,k/(2+Tr(Fs,k psi psi*))','unit_anchor_global_bounds':'I/2 <= H <= 3I/4','all_four_MUBs_and_exact_2design_verified':True,'full_unit_anchor_spectrum':'1/2 multiplicity2; 5/8 multiplicity1; (2+p_b,k)/4 each multiplicity2, b in Z,X,XZ,XZ2; k in 0,1,2; coincidences add multiplicities','TrH2_unit_anchor':'585/64','scope':'Universal H and inverse reduction; NOT the missing signed co-Choi PSD comparison or a new importance score.'}
(r/'werner413-h-mub.json').write_text(json.dumps(out,indent=2)+'\n')
