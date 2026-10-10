#!/usr/bin/env python3
"""Exact combined-support Far coefficients; no residual acceptance claim."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_full_stationary_source_transport import PINS,combine
from suzuki_exact_integer_source_action import norm2,sqrt_upper
from suzuki_bulk_action_z import evaluate
from suzuki_near_trial_lift_rhs import floor
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
from suzuki_certified_remote_z import enclosure,midpoint

def sha(raw):return hashlib.sha256(raw).hexdigest()
def buffer(root,spec):
 raw=(root/spec['file']).read_bytes();assert sha(raw)==spec['sha256'] and len(raw)==spec['bytes']
 out=[int.from_bytes(raw[i:i+spec['width']],'little',signed=True) for i in range(0,len(raw),spec['width'])]
 assert len(out)==spec['count'];return {'bits':spec['bits'],'values':out}
def run(root,rhsroot,liftroot,sourceroot,sector):
 stem=f'joint-256000-{sector}.trace-256000.full';sp=root/(stem+'.zip')
 assert sha(sp.read_bytes())==PINS[sector][0]
 _,s,V,_=read_snapshot(sp);N=len(s['modes']);assert N==128000
 sr=(sourceroot/f'full-stationary-source-{sector}.json').read_bytes()
 assert sha(sr)=={'even-v':'40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80','odd-v':'41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f'}[sector]
 source=json.loads(sr);Z=combine(V,[F(a) for a in source['q_rational']])
 assert norm2(Z)==F(source['rational']['represented_full_stationary_vector_norm2'])
 lr=(liftroot/f'new-finite-lift-{sector}.json').read_bytes()
 assert sha(lr)=={'even-v':'f9507a0c98d460698c6c6a112e80c66c8127f1dbb4be326500b18d6fd92f2d1c','odd-v':'20e784ae8a23afcb000479cd19d6fe07412b3699f16487c5a5bb8c7a021379cb'}[sector]
 lc=json.loads(lr);lift=buffer(liftroot,lc['lift_buffer'])
 rc=json.loads((rhsroot/f'new-near-trial-rhs-{sector}.json').read_text())
 assert sha((rhsroot/f'new-near-trial-rhs-{sector}.json').read_bytes())==lc['new_trial_rhs_certificate_sha256']
 y=buffer(rhsroot,rc['buffers']['trial-near']);zn=buffer(rhsroot,rc['buffers']['action-z-near'])
 b=max(Z['bits'],lift['bits'],y['bits']);zb=max(s['z']['bits'],zn['bits'])
 x=[(a<<(b-Z['bits']))-(v<<(b-lift['bits'])) for a,v in zip(Z['values'],lift['values'])]+[a<<(b-y['bits']) for a in y['values']]
 z=[a<<(zb-s['z']['bits']) for a in s['z']['values']]+[a<<(zb-zn['bits']) for a in zn['values']]
 start=s['modes'][0];m=[2*i+start for i in range(2*N)];U=4*N
 pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
 li=enclosure(*times(times(constant(4),enclose(hyperbolic(start==2))),recip(pi)),256)
 ti=enclosure(*times(recip(pi),recip(pi)),256);L=midpoint(li,256);t=midpoint(ti,256)
 pp=s['pole']['values'];pb=s['pole']['bits'];P=F(sum(a*v for a,v in zip(pp,x[:N])),1<<(pb+b))
 P+=sum((F(floor(L*n/(n*n+t),256)*v,1<<(256+b)) for n,v in zip(m[N:],x[N:])),F(0))
 c=F(s['c']['values'][0],1<<s['c']['bits']);alpha=s['alpha']
 assert abs(c)<1 and max(abs(a) for a in z)<11*(1<<zb)
 power=[1]*len(m);mom=[]
 for j in range(42):
  odd=F(sum(n*v*w for n,v,w in zip(m,x,power)),1<<b)
  even=F(sum(a*v*w for a,v,w in zip(z,x,power)),1<<(zb+b))
  mom.append({'j':j,'M_odd_rational':str(odd),'Z_even_rational':str(even)})
  power=[w*n*n for w,n in zip(power,m)]
  if (j+1)%7==0:print(sector,'exact Far moments',j+1,'/42',flush=True)
 xn=sqrt_upper(F(sum(v*v for v in x),1<<(2*b)),192)
 hs2=50*F(1,1<<168)*(F(1,U)+F(1,169))
 remainder=sqrt_upper(hs2,192)*xn
 checks=[]
 for n in (2*U+start,3*U+start,8*U+start):
  row=evaluate(n);zp=(F(row['lower_rational'])+F(row['upper_rational']))/2;assert abs(zp)<8
  retained=c*zp*sum((F(q['M_odd_rational'])/n**(2*j+2) for j,q in enumerate(mom)),F(0))-c*sum((F(q['Z_even_rational'])/n**(2*j+1) for j,q in enumerate(mom)),F(0))
  pole=alpha*L*n/(n*n+t)*P
  direct=c*F(sum(floor(F(v,1<<b)*(zp*k-n*F(a,1<<zb))/(n*n-k*k),512) for k,v,a in zip(m,x,z)),1<<512)
  # Exact geometric identity controls each omitted channel, without float arithmetic.
  exact_tail=c*F(sum(floor(F(v,1<<b)*(zp*k-n*F(a,1<<zb))/(n*n-k*k)*F(k,n)**84,512) for k,v,a in zip(m,x,z)),1<<512)
  check_error=2*abs(c)*F(len(x),1<<512)
  assert abs(direct-retained-exact_tail)<=check_error
  rowbound=F(20,n)*F(U,n)**84*F(sum(abs(v) for v in x),1<<b)
  assert abs(exact_tail)<=rowbound+check_error
  checks.append({'n':n,'retained_action_including_exact_parameter_pole':str(retained+pole),'geometric_tail_rounded_down_rational':str(exact_tail),'absolute_geometric_row_bound':str(rowbound),'all_256000_terms_outward_identity':True,'direct_sum_rounding_error_upper':str(check_error)})
  print(sector,'complete direct Far row',n,'verified',flush=True)
 return {'schema':'cone.combined-support-far-action.v1','sector':sector,'snapshot_sha256':PINS[sector][0],
 'full_source_certificate_sha256':sha(sr),'actual_CI_lift_certificate_sha256':sha(lr),'actual_CI_lift_sha256':lc['lift_buffer']['sha256'],
 'definition':'x_front=Z_full-ztilde_actual_CI; x_Near=y; x_elsewhere=0',
 'far_first_mode':2*U+start,'support_last_mode':U-2+start,'K':42,
 'action_formula':'c*z_n*sum(M_j/n^(2j+2))-c*sum(Z_j/n^(2j+1))+alpha*p_n*P; retain physical z_n and pole',
 'moments':mom,'point_parameters':{'c':str(c),'alpha':alpha,'L':str(L),'t':str(t),'pole_moment':str(P)},
 'rational':{'combined_support_norm_upper':str(xn),'geometric_HS_squared_upper':str(hs2),'geometric_action_remainder_upper':str(remainder)},
 'display_approximate':{'combined_support_norm_upper':float(xn),'geometric_action_remainder_upper':float(remainder)},
 'complete_direct_Far_checks':checks,'retained_point_coefficients_evaluated':True,
 'physical_scalar_parameter_errors_included':False,'whole_remote_residual_norm_evaluated':False,
 'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for arg in ('root','rhs-root','lift-root','source-root','output'):p.add_argument('--'+arg,type=Path,required=True)
 p.add_argument('--sector',choices=list(PINS),required=True);a=p.parse_args()
 out=run(a.root,a.rhs_root,a.lift_root,a.source_root,a.sector)
 a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out['display_approximate']),flush=True)
