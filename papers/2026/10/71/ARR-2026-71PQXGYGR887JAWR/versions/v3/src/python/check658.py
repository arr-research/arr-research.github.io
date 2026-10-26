import pathlib,json,math,random
import mpmath as mp
import sympy as sp
mp.mp.dps=65
rng=random.Random(658)
def g(x):
    x=mp.mpf(x)
    return ((x+1)*mp.log(x+1)-x*mp.log(x))/mp.log(2) if x else mp.mpf(0)
slack_low=mp.inf;slack_high=mp.inf;slack_choi=mp.inf;slack_loss=mp.inf
for i in range(360):
    k=mp.mpf(10)**rng.uniform(-1.4,1.4);E=mp.mpf(10)**rng.uniform(-.5,9)
    t=max(mp.mpf(0),k-1)+mp.mpf(10)**rng.uniform(-3,8)
    G=g(k*E+t)-g(t)
    slack_low=min(slack_low,G-mp.log(1+k*E/(t+1),2))
    slack_high=min(slack_high,mp.log(1+k*E/t,2)-G)
    c=1/(t+max(mp.mpf(0),1-k))
    if k<1:const=mp.log(mp.e,2)-mp.log(1-k,2)
    elif k>1:const=mp.log(mp.e,2)+mp.log(1+1/(k-1),2)
    slack_choi=min(slack_choi,const-g(t)-mp.log(c,2))
    eta=k/(t+1)
    upper=g(eta*E)-mp.log(1-eta,2)
    pureloss=g(E)+g(eta*E)-g((1-eta)*E)
    slack_loss=min(slack_loss,upper-pureloss)
assert min(slack_low,slack_high,slack_choi,slack_loss)>-mp.mpf('1e-50')
k,t=sp.symbols('k t',positive=True)
eta=k/(t+1);gain=t+1
# Attenuate then amplify: symmetric characteristic exponents add.
res=sp.simplify(gain*(1-eta)/2+(gain-1)/2-(t+(1-k)/2))
assert res==0
out={'cases':360,'gaussian_gain_range':'10^-1.4 to10^1.4','symbolic_loss_then_amplifier_noise_residue':str(res),'minimum_G_lower_slack':str(slack_low),'minimum_G_upper_slack':str(slack_high),'minimum_Choi_entropy_constant_slack':str(slack_choi),'minimum_pure_loss_information_upper_slack':str(slack_loss),'scope':'Gaussian parameter, inequality and noise-convention diagnostics; not proof of block converse/coding/novelty','pass':True}
p=pathlib.Path(__file__).parent;(p/'checks658.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
