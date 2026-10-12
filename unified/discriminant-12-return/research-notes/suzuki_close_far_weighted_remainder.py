#!/usr/bin/env python3
"""Directed weighted Region-1 split bounds; no D*y coordinate evaluation."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_infinite_tail_bounds import run as envelopes
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_certified_remote_diagonal import log_normalized

def run(source):
 out=[]
 for d in envelopes(source)['cases']:
  b=d['first_tail_mode'];a=2*b+b%2;C=F(d['rational']['Phi_pointwise_C_upper']);J=42
  # n<=b-2, m>=a>=2b: numerator<=16.5m, denominator>=3m²/4.
  # Kernel remainder<=22*4^-J/m. |y(m)|<=C/(11m).
  # Spacing-two decreasing sum: sum m^-2<=a^-2+(1/2)integral_a^infty x^-2 dx.
  weighted=F(1,a*a)+F(1,2*a);row=22*C*F(1,4**J)*weighted/11
  # Remote Region-1 has n=R+start,...,b-2: exactly R/2 rows.
  count=128000;l2=sqrt_upper(F(count),256)*row
  # Direct close kernel (offdiagonal only), minimum gap two, spacing two:
  # sum_{k=1}^K 1/(2k)<= (1+log K)/2. No dropped first endpoint term.
  K=(a-b)//2;assert K>0
  # log_normalized(4K)=log K with directed interval.
  loghi=log_normalized(4*K,256)[1]
  close=8*C*(1+loghi)/(22*b)
  # Exact algebra checks of the geometric remainder at representative separated indices.
  checks=[]
  for n in (1,b//2,b-2):
   for m in (a,a+2,4*a):
    q=F(n*n,m*m);exact=F(1,m*m-n*n)-sum(F(n**(2*j),m**(2*j+2)) for j in range(J));assert exact==q**J/F(m*m-n*n)
    rem=11*(m+n)*exact;assert rem<=22*F(1,4**J*m);checks.append({'n':n,'m':m,'geometric_identity_and_kernel_bound':True})
  assert l2<F('1e-27')
  out.append({'sector':d['sector'],'first_tail_mode':b,'first_far_input_mode':a,'J':J,'remote_region1_output_count':count,'rational':{'Phi_C_upper':str(C),'weighted_far_sum_upper':str(weighted),'far_offdiagonal_remainder_per_row_upper':str(row),'far_offdiagonal_remainder_l2_upper':str(l2),'close_offdiagonal_absolute_row_envelope_upper':str(close)},'display_approximate':{'far_remainder_l2':float(l2),'close_absolute_row_envelope':float(close)},'exact_geometric_checks':checks,'kernel_remainder_decay':'22*4^-J/m','unweighted_l1_used':False,'pole_truncation_included':False,'close_rows_evaluated':False,'far_moment_values_evaluated':False,'whole_action_evaluated':False})
 return {'schema':'cone.corrected-weighted-region1-remainder.v1','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'cases':out,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();d=run(a.source);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps([x['display_approximate'] for x in d['cases']]))
