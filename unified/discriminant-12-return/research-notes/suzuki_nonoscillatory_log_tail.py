#!/usr/bin/env python3
"""Directed zero-frequency log-tail consumer using panel integrals and EM."""
from fractions import Fraction as F
from math import factorial
import json,argparse
from pathlib import Path
from functools import lru_cache
from suzuki_oscillatory_log_tail import B,ZERO,ONE,add,sub,mul,scale,recip,neg
from suzuki_certified_remote_z import enclosure,exp_minus_one
from suzuki_certified_remote_diagonal import log_normalized
@lru_cache(None)
def expneg(k):
 assert k>=0
 x=enclosure(*exp_minus_one(B),B);out=ONE
 while k:
  if k&1:out=mul(out,x)
  x=mul(x,x);k//=2
 return out

def power(x,k):
 out=ONE
 for _ in range(k):out=mul(out,x)
 return out

def bernoulli(n):
 A=[F(0)]*(n+1);out=[]
 for m in range(n+1):
  A[m]=F(1,m+1)
  for j in range(m,0,-1):A[j-1]=j*(A[j-1]-A[j])
  out.append(A[0])
 assert out[2]==F(1,6) and out[4]==F(-1,30)
 return out

def derivative(a,p,d,lam):
 # Positive magnitude of d-th derivative at a for f=(a/x)^p/log(x/4).
 coeff=[1]
 for i in range(d):
  nxt=[0]*(len(coeff)+1)
  for k,v in enumerate(coeff):nxt[k]+=(p+i)*v;nxt[k+1]+=v
  coeff=nxt
 inv=recip(lam);ip=inv;total=ZERO
 for k,c in enumerate(coeff):total=add(total,scale(ip,c*factorial(k)));ip=mul(ip,inv)
 return scale(total,F(1,a**d))

def integral(a,p,lam,K=64,T=128):
 # normalized integral=a*integral_0^inf exp(-(p-1)u)/(lam+u)du.
 h=p-1;total=ZERO;error=F(0)
 for l in range(0,T,4):
  r=l+4;v=l+2;el=expneg(h*l);er=expneg(h*r)
  I=scale(sub(el,er),F(1,h));den=add(lam,(F(v),F(v)));ip=recip(den);inv=ip
  panel=ZERO
  for k in range(K):
   if k:
    boundary=sub(scale(el,F((-2)**k,h)),scale(er,F(2**k,h)))
    I=add(boundary,scale(I,F(k,h)))
   panel=add(panel,scale(mul(I,ip),(-1)**k));ip=mul(ip,inv)
  total=add(total,panel)
  ratio=F(2,1)/den[0];assert ratio<1
  error+=ratio**K/(den[0]*(1-ratio))*4*el[1]
 tail=expneg(h*T)[1]/(h*(lam[0]+T))
 total=scale(total,a);error=a*(error+tail)
 return total,error

def run(a,p,M=16):
 assert a>=512001 and p>=2
 lam=log_normalized(a,B);assert lam[0]>11
 T=4*((32+p-2)//(p-1));integ,ie=integral(a,p,lam,T=T);value=add(scale(integ,F(1,2)),scale(recip(lam),F(1,2)))
 bern=bernoulli(2*M)
 for j in range(1,M+1):
  # odd f derivative is negative; EM's minus sign makes this coefficient positive.
  value=add(value,scale(derivative(a,p,2*j-1,lam),bern[2*j]*F(2**(2*j-1),factorial(2*j))))
 em=F(2**(2*M+1),6**(2*M))*derivative(a,p,2*M-1,lam)[1]
 error=ie/2+em
 lo,hi=enclosure(value[0]-error,value[1]+error,160);rad=(hi-lo)/2
 assert rad<F('1e-40')
 return {'a':a,'power':p,'definition':'sum_{k>=0}(a/(a+2k))^p/log((a+2k)/4)',
 'interval':[str(lo),str(hi)],'integral_remainder_upper':str(enclosure(ie/2,ie/2,B)[1]),
 'EM_remainder_upper':str(enclosure(em,em,B)[1]),'radius':str(rad),
 'radius_below_1e_minus40':True,'integral_panel_width':4,'integral_T':T,'panel_terms':64,'EM_order':M,
 'complete_RHS_evaluated':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 rows=[run(start,power) for start in (512001,512002) for power in range(2,129)]
 a.output.write_text(json.dumps({'schema':'cone.nonoscillatory-log-tail.v1','cases':rows},indent=2,sort_keys=True)+'\n')
 print(json.dumps({'case_count':len(rows),'maximum_radius':float(max(F(r['radius']) for r in rows))}))
