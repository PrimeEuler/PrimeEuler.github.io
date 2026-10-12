#!/usr/bin/env python3
"""All finite RHS rows for the actual infinite diagonal seed, directed error budget."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_full_stationary_source_transport import PINS
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_near_trial_lift_rhs import writebuffer
from suzuki_infinite_tail_bounds import run as tail_bounds
BITS=256;S=1<<BITS
MOM={'even-v':'7ec00186bc123d15c761e9cd1389e6ad4ae26f8c9087f4485291480f097e17ec','odd-v':'f2487596f23d06fdc6234c8f0caa92bd364aa5f5194b89873cffe2c4938ef106'}
NEAR={'even-v':'7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45','odd-v':'3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480'}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def floor(q):return q.numerator*S//q.denominator
def point(row):
 lo,hi=map(F,row['interval']);q=F(floor((lo+hi)/2),S);return floor(q),max(q-lo,hi-q)
def readbuf(root,spec):
 raw=(root/spec['file']).read_bytes();assert sha(raw)==spec['sha256'] and len(raw)==spec['bytes']
 v=[int.from_bytes(raw[i:i+spec['width']],'little',signed=True) for i in range(0,len(raw),spec['width'])];assert len(v)==spec['count'];return v

def run(root,nearroot,momentroot,source,sector,out):
 snapshot=root/f'joint-256000-{sector}.trace-256000.full.zip';assert sha(snapshot.read_bytes())==PINS[sector][0]
 _,s,_,_=read_snapshot(snapshot);N=len(s['modes']);assert N==128000
 raw=(nearroot/f'new-near-trial-rhs-{sector}.json').read_bytes();assert sha(raw)==NEAR[sector];near=json.loads(raw);spec=near['buffers']['lift-rhs'];assert spec['bits']==BITS;old=readbuf(nearroot,spec)
 raw=(momentroot/f'infinite-rhs-moments-{sector}.json').read_bytes();assert sha(raw)==MOM[sector];mom=json.loads(raw);a=mom['first_tail_mode'];assert a==512000+s['modes'][0]
 U=[point(r) for r in mom['Ubar']];V=[point(r) for r in mom['Vbar']];P,prad=point(mom['P_tail']);assert len(U)==len(V)==42
 assert max(abs(v) for v,r in U+V)<S and abs(P)<S
 c=F(s['c']['values'][0],1<<s['c']['bits']);assert abs(c)<1
 cscaled=floor(c/a);z=[floor(F(v,1<<s['z']['bits'])) for v in s['z']['values']];pole=[floor(F(v,1<<s['pole']['bits'])) for v in s['pole']['values']];assert max(abs(v) for v in z)<11*S and max(abs(v) for v in pole)<2*S
 output=[];checks=[]
 for i,m in enumerate(s['modes']):
  u=m*S//a;t=u*u//S;assert 0<=u<=S//2
  hu=hv=0
  for (uq,_),(vq,_) in zip(reversed(U),reversed(V)):hu=uq+t*hu//S;hv=vq+t*hv//S
  off=cscaled*(u*hu//S-z[i]*hv//S)//S;pp=s['alpha']*pole[i]*P//S;value=old[i]+off+pp;output.append(value)
  if i in (0,N//2,N-1):
   x=F(m,a);exact=c/a*sum((x**(2*j+1)*F(U[j][0],S)-F(s['z']['values'][i],1<<s['z']['bits'])*x**(2*j)*F(V[j][0],S) for j in range(42)))+s['alpha']*F(s['pole']['values'][i],1<<s['pole']['bits'])*F(P,S)
   err=abs(F(off+pp,S)-exact);assert err<=F(100000,S);checks.append({'index':i,'mode':m,'exact_rational_polynomial_error':str(err),'below_rounding_charge':True})
  if (i+1)%32000==0:print(sector,'complete infinite-seed finite RHS rows',i+1,flush=True)
 # With |u|<=1/2, |t|<=1/4, |U|,|V|,|P|<1, Horner series and their derivatives are <2.
 # Input floors and each multiply floor cost <eps; 100000eps dominates all 84 Horner steps,
 # argument perturbation, front c/a,z,p floors and final arithmetic (|z|<11,|p|<2).
 eps=F(1,S);momentrow=(F(1,2)+11)*sum(max(U[j][1],V[j][1])*F(1,4**j) for j in range(42))/a+4*prad
 # Original front scalar caps: c 2e-41, z 1e-38, p 1e-39. These enter only the tail RHS.
 physicalrow=F('2e-41')*F(24,a)+F('1e-38')*F(2,a)+2*F('1e-39')*abs(F(P,S))
 roundingrow=100000*eps;norm=sqrt_upper(F(N),256)
 remainder=next(d for d in tail_bounds(source)['cases'] if d['sector']==sector)['rational']['inverse_moment_RHS_truncation_upper']
 charges={'unchanged_near_RHS':F(near['rational']['physical_lift_rhs_error_upper']),'inverse_moment_uncertainty':norm*momentrow,'front_physical_scalar_uncertainty':norm*physicalrow,'fixed_integer_row_arithmetic':norm*roundingrow,'geometric_infinite_input_remainder':F(remainder)}
 error=sum(charges.values());assert error<F('4e-30');assert 22*5*10**14*error<F('5e-14')
 out.mkdir(parents=True,exist_ok=True);buf=writebuffer(out,sector,'infinite-seed-lift-rhs',output,BITS)
 return {'schema':'cone.infinite-seed-complete-finite-rhs.v1','sector':sector,'snapshot_sha256':PINS[sector][0],'near_rhs_certificate_sha256':NEAR[sector],'inverse_moments_sha256':MOM[sector],'first_tail_mode':a,'buffers':{'lift-rhs':buf},'rational':{'physical_lift_rhs_error_upper':str(error),'future_remote_action_rhs_charge_upper':str(22*5*10**14*error)},'charges_l2':{k:str(v) for k,v in charges.items()},'complete_rows_evaluated':N,'exact_rational_row_checks':checks,'all_42_inverse_moment_pairs_used':True,'pole_retained':True,'finite_lift_certified':False,'whole_action_evaluated':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name in ('root','near-root','moment-root','source','output-root'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--sector',choices=list(MOM),required=True);a=p.parse_args();d=run(a.root,a.near_root,a.moment_root,a.source,a.sector,a.output_root);(a.output_root/f'infinite-seed-finite-rhs-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps({'sector':a.sector,'RHS_error':float(F(d['rational']['physical_lift_rhs_error_upper'])),'future_action_charge':float(F(d['rational']['future_remote_action_rhs_charge_upper'])),'buffer':d['buffers']['lift-rhs']}),flush=True)
