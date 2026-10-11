#!/usr/bin/env python3
"""Domain/norm certificate for an unevaluated infinite diagonal seed."""
import json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_integer_source_action import sqrt_upper
PIN='6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6'
NEAR={'even-v':'7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45','odd-v':'3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480'}
def run(source,rhsroot):
 raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()==PIN;whole=json.loads(raw);rows=[]
 for d in whole['cases']:
  sector=d['sector'];a=d['far_first_mode'];assert a>512000
  # 8/3<e<11/4 by the exponential series through 4 and its geometric tail.
  assert F(65,24)>F(8,3) and F(65,24)+F(1,100)<F(11,4)
  assert F(11,4)**11<128000 and F(8,3)**12>128000
  nr=(rhsroot/f'new-near-trial-rhs-{sector}.json').read_bytes();assert hashlib.sha256(nr).hexdigest()==NEAR[sector]
  near=json.loads(nr);yn=F(near['rational']['trial_norm_upper']);q=F(0)
  for row in d['far_channels']:
   j=row['j'];p=4*j+2;tail=F(1,a**p)+F(1,2*(p-1)*a**(p-1))
   q+=sqrt_upper(F(row['W_coefficient_rational'])**2*tail,256)
   p+=2;tail=F(1,a**p)+F(1,2*(p-1)*a**(p-1))
   q+=8*sqrt_upper(F(row['A_coefficient_rational'])**2*tail,256)
  if sector=='odd-v':q+=2*sqrt_upper(F(1,a**4)+F(1,6*a**3),256)
  far_y=q/11;total=sqrt_upper(yn*yn+far_y*far_y,256)
  lambda_norm=sqrt_upper((12*yn)**2+q*q,256)
  assert total<F('0.000146') and lambda_norm<F('0.0017')
  rows.append({'sector':sector,'near_trial_certificate_sha256':NEAR[sector],'first_infinite_mode':a,
   'tail_recipe':'Phi(n)=sum W_j/n^(2j+1)-z_physical(n)*sum A_j/n^(2j+2)+odd/(n*(n-1)); y(n)=Phi(n)/log(n/4)',
   'Near_recipe':'reuse frozen v14.238 compact Near trial exactly',
   'rational':{'Phi_tail_norm_upper':str(q),'Far_trial_norm_upper':str(far_y),'whole_trial_norm_upper':str(total),'whole_logarithmic_diagonal_norm_upper':str(lambda_norm)},
   'display_approximate':{'whole_trial_norm_upper':float(total),'logarithmic_diagonal_norm_upper':float(lambda_norm)},
   'admissible_in_logarithmic_diagonal_domain':True,'trial_tail_numerically_evaluated':False,'action_evaluated':False,'residual_acceptance_met':False})
 return {'schema':'cone.infinite-diagonal-seed-domain.v1','source_affine_payload_sha256':PIN,'cases':rows,
 'domain_basis':'Phi is ell2 by inverse-power parity tails and |z|<8; Lambda*y=Phi on Far. Near is finite. Domain(S)=Domain(Lambda) since ||S-Lambda||<575.',
 'requires_finite_42_positive_power_moments':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--rhs-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 d=run(a.source,a.rhs_root);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps([x['display_approximate'] for x in d['cases']]))
