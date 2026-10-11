#!/usr/bin/env python3
"""Directed nonprime inverse-power and exact-parameter pole tail coefficients."""
from fractions import Fraction as F
from math import comb
import json,argparse
from pathlib import Path
from suzuki_oscillatory_log_tail import B,ONE,ZERO,add,mul,scale,recip
from suzuki_certified_remote_z import constants,precise_nonprime,enclosure
from suzuki_bulk_action_z import moments
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add as oldadd,times,neg,constant,recip as oldrecip,enclose

def power(x,k):
 out=ONE
 for _ in range(k):out=mul(out,x)
 return out

def coefficient_checks():
 result=[]
 for k in (1,3,5,7):
  value=F((-1)**((k+1)//2),k)+2*(-1)**((k-1)//2)
  for j,b in enumerate((F(1,6),F(-1,30),F(1,42),F(-1,30)),1):
   if k>=2*j:value+=b/F(2*j)*((-1)**((k+1)//2))*4**(2*j)*comb(k-1,2*j-1)
  result.append(value)
 assert result==[F(1),F(1),F(5),F(61)]
 # Negative binomial tails after complex degree 8 have ratio<=8x<1/2.
 rational_tail=F(1,9)+4+sum(2*F(abs(b),2*j)*4**(2*j)*comb(8,2*j-1) for j,b in enumerate((F(1,6),F(-1,30),F(1,42),F(-1,30)),1))
 assert rational_tail<7000
 return result,rational_tail

def run(source):
 import hashlib
 raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()=="6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6"
 whole=json.loads(raw)
 pi,_,_,_,_,_=constants(B);ip=recip(pi);ss=moments(B);numbers,tailconstant=coefficient_checks();cases=[];checks=[]
 for sector,start in (('even-v',1),('odd-v',2)):
  parity=(-1)**start;b=512000+start
  coefficients=[]
  for r,e in enumerate(numbers):
   k=2*r+1
   bracket=add((e,e),scale(ss[r],-parity*(-1)**r*2**(2*r+2)))
   coeff=mul(bracket,power(ip,k));coefficients.append({'power':k,'interval':[str(x) for x in coeff]})
  rational=F(7000,(3*b)**9)
  em=13*F(4,3*b)**8;arch=F(1024*10**7,3**9*b**9);physical=rational+em+arch
  assert physical<F('1e-40')
  pole_pi=enclose(oldadd(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
  L=enclosure(*times(times(constant(4),enclose(hyperbolic(start==2))),oldrecip(pole_pi)),B)
  t=enclosure(*times(oldrecip(pole_pi),oldrecip(pole_pi)),B)
  assert 0<L[0]<L[1]<2 and 0<t[0]<t[1]<1
  polecoeff=[{'power':2*j+1,'interval':[str(x) for x in scale(mul(L,power(t,j)),(-1)**j)]} for j in range(8)]
  poleerror=L[1]*t[1]**8/F(b**17);odd=F(2,b**17) if sector=='odd-v' else F(0)
  row=next(x for x in whole['cases'] if x['sector']==sector)
  ca=sum(abs(F(x['A_coefficient_rational']))/b**(2*x['j']+1) for x in row['far_channels'])
  cw=sum(abs(F(x['W_coefficient_rational']))/b**(2*x['j']) for x in row['far_channels'])
  cphi=cw+8*ca+(F(2,b) if sector=='odd-v' else F(0))
  delta=ca*physical+(F(2,b**16) if sector=='odd-v' else F(0))
  uerror=(physical*cphi+9*delta)/11*(F(1,b)+F(1,4))
  verror=delta/11*(F(1,b)+F(1,2))
  perror=2*delta/11*(F(1,b*b)+F(1,2*b))+L[1]*t[1]**8*(cphi+delta)/11*(F(1,b**18)+F(1,34*b**17))
  assert max(uerror,verror,perror)<F('1e-40')
  cases.append({'sector':sector,'first_tail_mode':b,
   'nonprime_constant_interval':[str(x) for x in scale(pi,F(1,2))],'nonprime_coefficients':coefficients,
   'physical_nonprime_remainder_upper':str(enclosure(physical,physical,B)[1]),
   'nonprime_rational_model_remainder_upper':str(enclosure(rational,rational,B)[1]),
   'pole_parameters':{'L_interval':[str(x) for x in L],'t_interval':[str(x) for x in t]},
   'pole_coefficients':polecoeff,'pole_series_remainder_upper':str(enclosure(poleerror,poleerror,B)[1]),
   'odd_source_powers':list(range(2,17)) if sector=='odd-v' else [],
   'odd_source_series_remainder_upper':str(enclosure(odd,odd,B)[1]),
   'display_approximate':{'physical_nonprime_remainder_upper':float(physical),'pole_series_remainder_upper':float(poleerror),'maximum_inverse_moment_model_error_upper':float(max(uerror,verror,perror))},
   'normalized_U_model_error_upper':str(enclosure(uerror,uerror,B)[1]),'normalized_V_model_error_upper':str(enclosure(verror,verror,B)[1]),'pole_moment_model_error_upper':str(enclosure(perror,perror,B)[1]),'complete_inverse_moments_evaluated':False,'infinite_capacity_tail_closed':False})
  for multiplier in (1,2,4,16,256):
   n=512000*multiplier+start;ref=precise_nonprime(n,pi,B)
   model=scale(pi,F(1,2))
   for row in coefficients:model=add(model,scale(tuple(F(x) for x in row['interval']),F(1,n**row['power'])))
   err=F(7000,(3*n)**9)
   assert model[0]-err<=ref[0] and ref[1]<=model[1]+err
   checks.append({'sector':sector,'n':n,'original_exact_rational_nonprime_interval_contained':True})
 return {'schema':'cone.physical-infinite-tail-coefficients.v1','digamma_odd_integer_coefficients':[str(x) for x in numbers],
 'rational_negative_binomial_tail_constant':str(tailconstant),'cases':cases,'exact_reference_checks':checks,
 'complete_RHS_evaluated':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--source',type=Path,required=True);a=p.parse_args();d=run(a.source);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps([x['display_approximate'] for x in d['cases']]))
