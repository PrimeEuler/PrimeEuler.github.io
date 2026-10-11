#!/usr/bin/env python3
"""Complete directed normalized inverse moments for the infinite diagonal seed."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse,json,hashlib
from suzuki_oscillatory_log_tail import run as oscillatory,constants,B,ZERO,ONE,add,scale,mul,cmul,cadd,cscale
SOURCE='6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6'
F0=(0,0,0,0);CZ=(ZERO,ZERO)
def cp(a):return (a,ZERO)
def conj(a):return a[0],(-a[1][1],-a[1][0])
def acc(poly,key,value):poly[key]=cadd(poly.get(key,CZ),value)
def product(a,b):
 out={}
 for (fa,pa),va in a.items():
  for (fb,pb),vb in b.items():acc(out,(tuple(x+y for x,y in zip(fa,fb)),pa+pb),cmul(va,vb))
 return out

def run(source,coeffpath,realpath,sector):
 raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCE;whole=json.loads(raw)
 assert hashlib.sha256(coeffpath.read_bytes()).hexdigest()=='f2d4da7447483fc4ec010158fee1ec8abcab354d718bcf205b910742c7158e55'
 co=json.loads(coeffpath.read_text());case=next(x for x in co['cases'] if x['sector']==sector)
 d=next(x for x in whole['cases'] if x['sector']==sector);a=case['first_tail_mode']
 # The real input is the already certified complete 2..128 power bank.
 assert hashlib.sha256(realpath.read_bytes()).hexdigest()=='ce70f8b407836f4904c965b793962608541aa415efcdabd05af2843b801695c2'
 real=json.loads(realpath.read_text());assert len(real['cases'])==254
 realmap={(r['a'],r['power']):tuple(F(x) for x in r['interval']) for r in real['cases']}
 _,_,weights,_,_,_=constants(B);z={};phi={};apoly={}
 acc(z,(F0,0),cp(tuple(F(x) for x in case['nonprime_constant_interval'])))
 for row in case['nonprime_coefficients']:acc(z,(F0,row['power']),cp(scale(tuple(F(x) for x in row['interval']),F(1,a**row['power']))))
 for index,freq in enumerate(((1,0,0,0),(0,1,0,0),(2,0,0,0),(0,0,1,0),(0,0,0,1))):
  wp,err=weights[index];w=(wp-err,wp+err)
  acc(z,(freq,0),(ZERO,scale(w,-1)));acc(z,(tuple(-x for x in freq),0),(ZERO,w))
 for row in d['far_channels']:
  j=row['j'];w=F(row['W_coefficient_rational'])/a**(2*j);v=F(row['A_coefficient_rational'])/a**(2*j+1)
  acc(phi,(F0,2*j),cp((w,w)));acc(apoly,(F0,2*j+1),cp((v,v)))
 for key,v in product(z,apoly).items():acc(phi,key,cscale(v,-1))
 for k in case['odd_source_powers']:
  q=F(1,a**(k-1));acc(phi,(F0,k-1),cp((q,q)))
 upoly=product(z,phi)
 count=[0]
 @lru_cache(None)
 def scalar(freq,p):
  assert 2<=p<=128
  if not any(freq):return cp(realmap[a,p])
  if next(x for x in freq if x)<0:return conj(scalar(tuple(-x for x in freq),p))
  r=oscillatory(a,p,freq);assert r['radius_below_1e_minus40'];count[0]+=1
  if count[0]%100==0:print(sector,'directed oscillatory primitives',count[0],flush=True)
  return tuple(tuple(F(x) for x in r[name]) for name in ('real_interval','imag_interval'))
 def sum_poly(poly,k):
  result=CZ
  for (freq,p),v in sorted(poly.items()):result=cadd(result,cmul(v,scalar(freq,p+k+1)))
  result=cscale(result,F(1,a));assert result[1][0]<=0<=result[1][1]
  return result[0]
 def enclose_model(point,err):
  from suzuki_certified_remote_z import enclosure
  lo,hi=enclosure(point[0]-err,point[1]+err,160);rad=(hi-lo)/2
  assert rad<F('1e-40');return {'interval':[str(lo),str(hi)],'radius':str(rad),'model_error_upper':str(err)}
 U=[];V=[]
 for j in range(42):
  U.append({'j':j,**enclose_model(sum_poly(upoly,2*j+2),F(case['normalized_U_model_error_upper']))})
  V.append({'j':j,**enclose_model(sum_poly(phi,2*j+1),F(case['normalized_V_model_error_upper']))})
  if (j+1)%7==0:print(sector,'complete inverse-moment pairs',j+1,'/42',flush=True)
 # Pole polynomial is sum coefficient*n^(-power), directly from directed physical L,t.
 polepoly={}
 for row in case['pole_coefficients']:acc(polepoly,(F0,row['power']),cp(scale(tuple(F(x) for x in row['interval']),F(1,a**row['power']))))
 pp=sum_poly(product(polepoly,phi),0);pole=enclose_model(pp,F(case['pole_moment_model_error_upper']))
 # Independent positive pointwise Phi envelopes check normalization and signs.
 cw=sum(abs(F(r['W_coefficient_rational']))/a**(2*r['j']) for r in d['far_channels'])
 ca=sum(abs(F(r['A_coefficient_rational']))/a**(2*r['j']+1) for r in d['far_channels'])
 w0=F(d['far_channels'][0]['W_coefficient_rational']);low=w0-(cw-abs(w0))-8*ca
 high=cw+8*ca+(F(2,a) if sector=='odd-v' else F(0));assert low>0
 for j,row in enumerate(V):
  base=realmap[a,2*j+2];bounds=(low*base[0]/a,high*base[1]/a)
  vl,vh=map(F,row['interval']);assert bounds[0]<=vl<=vh<=bounds[1]
 radii=[F(r['radius']) for r in U+V]+[F(pole['radius'])]
 return {'schema':'cone.complete-infinite-seed-rhs-moments.v1','sector':sector,'first_tail_mode':a,
 'source_affine_sha256':hashlib.sha256(raw).hexdigest(),'physical_coefficients_sha256':hashlib.sha256(coeffpath.read_bytes()).hexdigest(),
 'real_scalar_bank_sha256':hashlib.sha256(realpath.read_bytes()).hexdigest(),
 'Ubar':U,'Vbar':V,'P_tail':pole,'maximum_radius':str(max(radii)),
 'positive_V_envelope_checks':42,'oscillatory_scalar_values_evaluated':count[0],'all_85_infinite_inverse_moments_evaluated':True,
 'physical_nonprime_pole_odd_model_errors_included_once':True,'radius_below_1e_minus40_all':True,
 'finite_RHS_rows_evaluated':False,'finite_lift_certified':False,'whole_action_evaluated':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name in ('source','coefficients','real-scalars','output'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--sector',choices=('even-v','odd-v'),required=True);a=p.parse_args()
 d=run(a.source,a.coefficients,a.real_scalars,a.sector);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps({'sector':a.sector,'maximum_radius':float(F(d['maximum_radius'])),'scalar_count':d['oscillatory_scalar_values_evaluated']}),flush=True)
