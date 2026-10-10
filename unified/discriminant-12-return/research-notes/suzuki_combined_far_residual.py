#!/usr/bin/env python3
"""Corrected combined-support Far residual bounds, including rejection tests."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from suzuki_exact_integer_source_action import sqrt_upper
PINS={'even-v':'d2feb4f36030fe528fec66771cb891054fa0e50192a3fa3f8033939370ec2505','odd-v':'690962a2dc1dd4b099d75c73f9e6a4eb77f4d42812aecb5e2dc6e78ee104d1aa'}
LIFTS={'even-v':'f9507a0c98d460698c6c6a112e80c66c8127f1dbb4be326500b18d6fd92f2d1c','odd-v':'20e784ae8a23afcb000479cd19d6fe07412b3699f16487c5a5bb8c7a021379cb'}
SOURCES={'even-v':'40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80','odd-v':'41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f'}
def load(path,pin):
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==pin;return json.loads(raw)
def tail(a,p):
 assert p>1
 return F(1,2*(p-1)*a**(p-1)),F(1,a**p)+F(1,2*(p-1)*a**(p-1))
def rootlow(q,b=256):
 hi=sqrt_upper(q,b);lo=max(F(0),hi-F(1,1<<b));assert lo*lo<=q;return lo
def run(root,liftroot,sourceroot,sector):
 d=load(root/f'combined-far-action-{sector}.json',PINS[sector]);a=d['far_first_mode'];p=d['point_parameters']
 lc=load(liftroot/f'new-finite-lift-{sector}.json',LIFTS[sector]);sc=load(sourceroot/f'full-stationary-source-{sector}.json',SOURCES[sector])
 c=F(p['c']);t=F(p['t']);L=F(p['L']);P=F(p['pole_moment']);LP=p['alpha']*L*P
 assert 0<t<1 and 0<L<2 and abs(c)<1
 # g_n is EXACTLY 1/n (even-v), 1/(n-1) (odd-v), not rho's affine expansion.
 C={1:F(1)};D={}
 if sector=='odd-v':
  for k in range(2,44):C[k]=F(1)
 for j,m in enumerate(d['moments']):
  assert m['j']==j
  C[2*j+1]=C.get(2*j+1,F(0))+c*F(m['Z_even_rational'])-LP*(-t)**j
  D[2*j+2]=-c*F(m['M_odd_rational'])
 def charge(k,v):return sqrt_upper(v*v*tail(a,2*k)[1],256)
 cfirstlow=rootlow(C[1]*C[1]*tail(a,2)[0]);cfirstup=charge(1,C[1])
 crest=sum((charge(k,v) for k,v in C.items() if k!=1),F(0))
 dnorm=sum((charge(k,v) for k,v in D.items()),F(0))
 # Exact pole remainder after 42 powers: |LP|*t^42/n^85/(1+t/n²).
 pole=sqrt_upper(LP*LP*t**84*tail(a,170)[1],256)
 # 1/(n-1)=sum_{k=1}^{43} n^-k + 1/[n^43(n-1)].
 shift=sqrt_upper(4*tail(a,88)[1],256) if sector=='odd-v' else F(0)
 geo=F(d['rational']['geometric_action_remainder_upper'])
 xn=F(d['rational']['combined_support_norm_upper']);l1=sqrt_upper(F(256000),256)*xn
 # Conservatively derived physical scalar/pole error: <=1e-36*l1/n, see ledger.
 scalar=F('1e-36')*l1*sqrt_upper(tail(a,2)[1],256)
 pointrest=pole+shift+geo
 pointlo=max(F(0),cfirstlow-crest-8*dnorm-pointrest)
 pointup=cfirstup+crest+8*dnorm+pointrest
 physical_lo=max(F(0),pointlo-scalar);physical_up=pointup+scalar
 source=F(sc['rational']['whole_remote_source_transport_upper'])
 lift=F(lc['rational']['finite_lift_remote_action_charge_upper'])
 true_lo=max(F(0),physical_lo-source-lift);true_up=physical_up+source+lift
 assert true_lo>F('3e-5')
 vals={'leading_C_coefficient':C[1],'leading_C_norm_lower':cfirstlow,'other_C_norm_upper':crest,
 'D_norm_upper':dnorm,'pole_series_remainder_upper':pole,'odd_source_series_remainder_upper':shift,
 'geometric_action_remainder_upper':geo,'physical_scalar_error_upper':scalar,
 'represented_point_Far_residual_lower':pointlo,'represented_point_Far_residual_upper':pointup,
 'physical_combined_Far_residual_lower':physical_lo,'physical_combined_Far_residual_upper':physical_up,
 'source_transport_upper':source,'finite_lift_transport_upper':lift,
 'true_Schur_Far_residual_lower':true_lo,'true_Schur_Far_residual_upper':true_up}
 return {'schema':'cone.corrected-combined-far-residual.v1','sector':sector,'far_first_mode':a,
 'combined_action_payload_sha256':PINS[sector],'actual_CI_lift_certificate_sha256':LIFTS[sector],
 'full_source_certificate_sha256':SOURCES[sector],
 'formula':'r=g-Dx; g=1/n even-v, 1/(n-1) odd-v; no extra source or lift moment term',
 'coefficient_recipe':'C_1 starts at 1; odd source adds 1 at powers 2..43; add c*Z_j-alpha*L*P*(-t)^j at powers 2j+1; D_(2j+2)=-c*M_j',
 'rational':{k:str(v) for k,v in vals.items()},
 'display_approximate':{k:float(vals[k]) for k in ('physical_scalar_error_upper','true_Schur_Far_residual_lower','true_Schur_Far_residual_upper')},
 'z_bound_applied_after_combining':8,'Far_residual_above_unchanged_target':True,
 'current_compact_Near_trial_rejected':True,'whole_residual_norm_evaluated':False,
 'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for arg in ('root','lift-root','source-root','output'):p.add_argument('--'+arg,type=Path,required=True)
 p.add_argument('--sector',choices=list(PINS),required=True);a=p.parse_args()
 out=run(a.root,a.lift_root,a.source_root,a.sector);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out['display_approximate']),flush=True)
