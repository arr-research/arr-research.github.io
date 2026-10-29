from pathlib import Path
import sympy as s,json
C=Path(__file__).parent
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
P=[s.diag(1,0),s.diag(0,1)]
ops=[P,[H*p for p in P],[(I+X)/2,(I-X)/2]]
def vec(a):return s.Matrix([a[i,j] for j in range(2) for i in range(2)])
def rnk(seq):
 w=[I]
 for ks in seq:w=[b*a for b in ks for a in w]
 return int(s.Matrix.hstack(*(vec(a) for a in w)).rank())
rows=[]
for phase in range(3):
 for n in range(1,7):
  reverse=[[a.H for a in ops[(phase-j-1)%3]] for j in range(n)]
  shifted=[ops[(phase-n+j)%3] for j in range(n)]
  a=rnk(reverse);b=rnk(shifted);assert a==b
  rows.append({'phase':phase,'n':n,'reverse_rank':a,'shifted_original_rank':b})
for n in range(1,7):
 original=[rnk([ops[(phase+j)%3] for j in range(n)]) for phase in range(3)]
 reverse=[next(r['reverse_rank'] for r in rows if r['phase']==phase and r['n']==n) for phase in range(3)]
 assert sorted(original)==sorted(reverse)
onsets=[next(r['n'] for r in rows if r['phase']==phase and r['reverse_rank']==4) for phase in range(3)]
assert onsets==[4,2,3]
(C/'REVERSE1223.json').write_text(json.dumps({'scope':'Own exact supporting control for an unreviewed corrected-statement draft, not new score or formal proof','proper_reverse':'Inverse base T^-1 and local adjoint tuple at T^-1 omega','original_onsets':[4,3,2],'proper_reverse_onsets':onsets,'same_distribution':True,'pointwise_equal':False,'rank_identity_controls':rows,'all_assertions_pass':True},indent=2)+'\n',encoding='utf-8',newline='\n')
(C/'STATEMENT1223.txt').write_text('''Draft corrected quantifiers, not a reviewed theorem or manuscript.

Let T be invertible and probability preserving, and S(omega) a measurable finite Kraus tuple on M_d. Write Pi_n(omega;sigma)=A_sigma_n(T^(n-1)omega)...A_sigma_1(omega). Define the reversed system on base T^-1 by S_rev(omega)=S(T^-1 omega)^*. Then for every fixed n and label word sigma,
Pi_rev_n(omega;sigma)=Pi_n(T^-n omega;reverse(sigma))^*.
Thus the dimension of the complete reversed Kraus-word span at omega equals that of the original span at T^-n omega. For each fixed n their distributions coincide by preservation of probability. No ergodicity, trace preservation or unitality is required for this fixed-block assertion.

For the first and eventual full-span onsets, assume additionally that each local CP map and its Hilbert-Schmidt adjoint are faithful, on a T-invariant full-probability set. In finite dimensions dual faithfulness is equivalent to Phi(I)>0. If an unnormalized Choi matrix J_n is positive definite, J_n>=c I, then the next block has Choi matrix (id tensor Phi_next)(J_n)>=c I tensor Phi_next(I)>0. Hence full span is persistent in the forward process. The reverse maps are original adjoints, so persistence there uses faithfulness of original maps. Consequently first full-span onset equals eventual full-span onset in each process, and {ell0<=n} is exactly the fixed-block full-span event. The fixed-block probability identity yields equality in distribution of the two first onsets, and likewise of eventual onsets, including a possible atom at infinity. It does not assert pointwise equality at the same base point.

Check the conventions before using this draft: choose a fixed unnormalized Choi orientation, later maps multiply on the left, and replace the forward base by T^-1. The source's forward pointwise-adjoint process is different. In the three-phase bistochastic model D_Z,H after D_Z,D_X, original onsets are(4,3,2), proper reversed onsets(4,2,3), and forward pointwise-adjoint onsets(2,2,2). The first two laws agree but their same-point values need not; the last law differs.

Proof status: hand derivation and18 exact finite rank controls plus law comparisons; no Lean certificate or independent component verdict. This is an elementary correction candidate, not a claimed solution of gapped-EMPS classification or a priority claim. The one active review1220 has received no further supplement from this draft; preserve its stated scope.
''',encoding='utf-8',newline='\n')
print('18 exact shifted-block controls and6 law comparisons pass; proper-reverse onsets4,2,3')
