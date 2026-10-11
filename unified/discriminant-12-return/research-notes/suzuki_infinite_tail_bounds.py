#!/usr/bin/env python3
"""Infinite-tail envelope and inverse-moment RHS remainder; no action evaluation."""
import json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_certified_remote_diagonal import log_normalized
SOURCE='6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6'
def run(path):
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCE;w=json.loads(raw);out=[]
 for d in w['cases']:
  b=d['far_first_mode'];R=256000;a=2*b
  C=sum((abs(F(r['W_coefficient_rational']))/b**(2*r['j'])+8*abs(F(r['A_coefficient_rational']))/b**(2*r['j']+1) for r in d['far_channels']),F(0))
  if d['sector']=='odd-v':C+=F(2,b)
  # |Phi_n|<=C/n and |y_n|<=C/[n log(n/4)].
  tail2=F(1,b*b)+F(1,2*b);yn=C*sqrt_upper(tail2,256)/11
  hs2=50*F(1,1<<168)*(F(1,R)+F(1,169));rhsrem=sqrt_upper(hs2,256)*yn
  # Corrected offdiagonal envelope for outputs n>=2b:
  # A<=16 C/(11n)*(1/b+log(n/b)/2), B<=16 C/n*(1+log n)/log(n/8),
  # C_region<=16 C/11*(1/(4n²)+1/(4n)).
  # Since log(n/8)>11 here, and log n=log(n/8)+log8<log(n/8)+3,
  # B<=16 C/n*(1+4/11)=240 C/(11n).
  constant=C*(F(16,11*b)+F(240,11)+F(4,11)+F(4,11*a))
  slope=F(8,11)*C # envelope=(constant+slope*log(n/b))/n.
  # First term plus spacing-two integral of envelope². It is decreasing at a.
  lo,hi=log_normalized(2*b,256);bl,bh=log_normalized(b,256);log2hi=hi-bl
  assert constant+slope*log2hi>slope
  point=(constant+slope*log2hi)**2/a**2
  integral=(constant**2+2*constant*slope*(log2hi+1)+slope**2*(log2hi**2+2*log2hi+2))/a
  envelope_norm=sqrt_upper(point+integral/2,256)
  out.append({'sector':d['sector'],'first_tail_mode':b,'output_lower_threshold':a,
   'RHS_formula':'c*sum_j(m^(2j+1)*U_j-z_m*m^(2j)*V_j)+alpha*p_m*P_tail',
   'U_j':'sum_tail z_n*y_n/n^(2j+2)','V_j':'sum_tail y_n/n^(2j+1)',
   'K':42,'rational':{'Phi_pointwise_C_upper':str(C),'tail_trial_norm_upper':str(yn),
    'inverse_moment_RHS_HS_squared_upper':str(hs2),'inverse_moment_RHS_truncation_upper':str(rhsrem),
    'offdiagonal_envelope_constant':str(constant),'offdiagonal_envelope_log_slope':str(slope),
    'offdiagonal_output_tail_norm_upper':str(envelope_norm)},
   'display_approximate':{'Phi_C':float(C),'RHS_truncation_upper':float(rhsrem),'offdiagonal_output_tail_norm_upper':float(envelope_norm)},
   'inverse_moment_values_numerically_evaluated':False,'whole_action_evaluated':False,
   'slow_one_over_log_decay_required':False,'residual_acceptance_met':False})
 return {'schema':'cone.infinite-tail-corrected-envelopes.v1','source_affine_payload_sha256':SOURCE,'cases':out,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 d=run(a.source);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps([x['display_approximate'] for x in d['cases']]))
