#!/usr/bin/env python3
"""Represented Near Jacobi correction and actual new complete finite RHS; no contraction claim."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_near_trial_lift_rhs import transpose_rows,floor,writebuffer
from suzuki_certified_remote_diagonal import log_normalized
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
from suzuki_certified_remote_z import enclosure,midpoint

def buf(root,spec):
 raw=(root/spec['file']).read_bytes();assert len(raw)==spec['bytes'] and hashlib.sha256(raw).hexdigest()==spec['sha256'];return [int.from_bytes(raw[i:i+spec['width']],'little',signed=True) for i in range(0,len(raw),spec['width'])]
def run(root,resroot,sector,out):
 nr=root/'near_trial_rhs_witness_v14_238';ir=root/'infinite_seed_rhs_witness_v14_268';rr=(resroot/f'region1-residual-{sector}.json').read_bytes();assert hashlib.sha256(rr).hexdigest()=={'even-v':'de7a7a62d3cc161345376b8f25dd2d9ad2859d9896d00cb0bae656b2a31048ee','odd-v':'e6e8cc403dcafd5b7c12f5c0f71f6d4fe311ea4d09ed3874c5794b691c312735'}[sector];rc=json.loads(rr);nearraw=(nr/f'new-near-trial-rhs-{sector}.json').read_bytes();assert hashlib.sha256(nearraw).hexdigest()=={'even-v':'7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45','odd-v':'3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480'}[sector]
 near=json.loads(nearraw);gr=(ir/f'infinite-seed-finite-rhs-{sector}.json').read_bytes();assert hashlib.sha256(gr).hexdigest()=={'even-v':'1dcd60af05c3ad589c8d04d84bd3d5372ce4b4079b12d7626472067dea0d0933','odd-v':'3b05491693a6769fbfdf30b6ed8785384242364223498be73b3fb8f5c00133d4'}[sector];oldrhs=json.loads(gr);r=buf(resroot,rc['point_buffer']);y=buf(nr,near['buffers']['trial-near']);z=buf(nr,near['buffers']['action-z-near']);g=buf(ir,oldrhs['buffers']['lift-rhs']);N=128000;assert len(r)==len(y)==len(z)==len(g)==N
 start=1 if sector=='even-v' else 2;delta=[]
 for i,v in enumerate(r):
  n=256000+start+2*i;ll,lh=log_normalized(n,128);delta.append(floor(F(v,1<<256)/((ll+lh)/2),160))
 newy=[a+b for a,b in zip(y,delta)];dn=sqrt_upper(F(sum(v*v for v in delta),1<<320),256);assert dn<F('2e-5')
 # This is a chosen exact dyadic trial; no physical inverse or contraction is asserted.
 u,v=transpose_rows(delta,[a*b for a,b in zip(delta,z)],start)
 # Original front points are loaded from the immutable snapshot by the same reader as prior gates.
 from suzuki_exact_outward_certificate import read_snapshot
 from suzuki_full_stationary_source_transport import PINS
 sp=root/'actual256'/f'joint-256000-{sector}.trace-256000.full.zip';assert hashlib.sha256(sp.read_bytes()).hexdigest()==PINS[sector][0];_,s,_,_=read_snapshot(sp)
 pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))));li=enclosure(*times(times(constant(4),enclose(hyperbolic(start==2))),recip(pi)),256);ti=enclosure(*times(recip(pi),recip(pi)),256);L=midpoint(li,256);t=midpoint(ti,256)
 P=sum((F(floor(L*n/(n*n+t),256)*dy,1<<416) for n,dy in ((256000+start+2*i,dy) for i,dy in enumerate(delta))),F(0));c=F(s['c']['values'][0],1<<s['c']['bits']);dg=[]
 for j,(up,vp) in enumerate(zip(u,v)):
  zf=F(s['z']['values'][j],1<<s['z']['bits']);pf=F(s['pole']['values'][j],1<<s['pole']['bits']);q=c*(F(up,1<<576)-zf*F(vp,1<<416))/2+s['alpha']*pf*P;dg.append(floor(q,256))
 l1=F(sum(abs(v) for v in delta),1<<160);eps=F(1,1<<256);row=(F('21e-38')+19*eps)*l1+2*F('1e-38')*abs(P)+16*eps*l1+eps;de=sqrt_upper(F(N),256)*row;error=F(oldrhs['rational']['physical_lift_rhs_error_upper'])+de
 # Original infinite seed norm <0.000146, safe both-sector upper bound from v14.250.
 trial=F('0.000146')+dn;assert trial<F('0.002') and error<F('4e-30')
 out.mkdir(parents=True,exist_ok=True);buffers={'near-correction':writebuffer(out,sector,'near-correction',delta,160),'refined-near-trial':writebuffer(out,sector,'refined-near-trial',newy,160),'lift-rhs':writebuffer(out,sector,'refined-lift-rhs',[a+b for a,b in zip(g,dg)],256)}
 return {'schema':'cone.actual-residual-near-seed-refinement.v1','sector':sector,'residual_point_sha256':rc['point_buffer']['sha256'],'original_complete_RHS_point_sha256':oldrhs['buffers']['lift-rhs']['sha256'],'buffers':buffers,'definition':'new y_Near=old y_Near+floor160(r_point/midpoint(log(n/4))); infinite Far seed unchanged','rational':{'represented_correction_norm_upper':str(dn),'new_whole_trial_norm_upper':str(trial),'RHS_correction_error_upper':str(de),'physical_lift_rhs_error_upper':str(error)},'display_approximate':{'correction_norm':float(dn),'trial_norm_upper':float(trial),'complete_RHS_error':float(error)},'trial_domain_preserved_by_finite_correction':True,'all_finite_RHS_rows_evaluated':True,'new_finite_lift_certified':False,'refined_residual_evaluated':False,'contraction_certified':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--payload-root',type=Path,required=True);p.add_argument('--residual-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--sector',choices=('even-v','odd-v'),required=True);a=p.parse_args();d=run(a.payload_root,a.residual_root,a.sector,a.output_root);(a.output_root/f'near-seed-refinement-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d['display_approximate']),flush=True)
