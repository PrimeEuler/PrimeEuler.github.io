#!/usr/bin/env python3
"""Directed convergent geometric-difference consumer for oscillatory log tails."""
from fractions import Fraction as F
from math import comb,factorial,isqrt
import json,argparse
from suzuki_certified_remote_z import constants,midpoint,radius,sin_integer,interval_add as add,interval_mul as mul,interval_scale as scale,interval_recip as recip,enclosure
from suzuki_certified_remote_diagonal import log_normalized
B=512
rawadd,rawmul,rawscale,rawrecip=add,mul,scale,recip
def add(a,b):return enclosure(*rawadd(a,b),B)
def mul(a,b):return enclosure(*rawmul(a,b),B)
def scale(a,q):return enclosure(*rawscale(a,q),B)
def recip(a):return enclosure(*rawrecip(a),B)
ZERO=(F(0),F(0));ONE=(F(1),F(1))
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def cmul(a,b):return sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))
def cadd(a,b):return add(a[0],b[0]),add(a[1],b[1])
def cscale(a,q):return scale(a[0],q),scale(a[1],q)
def cinv(a):
 # denominator enclosure by exact interval products; imaginary sign is reversed.
 den=add(mul(a[0],a[0]),mul(a[1],a[1]));assert den[0]>0
 return mul(a[0],recip(den)),mul(neg(a[1]),recip(den))
def sine(arg,pi):
 pp=midpoint(pi,B);ap=midpoint(arg,B);turns=(ap+pp)//(2*pp);reduced=ap-2*turns*pp
 err=radius(arg,ap)+2*abs(turns)*radius(pi,pp)
 value,rounding=sin_integer(int(reduced*(1<<B)),B,56)
 error=err+rounding+F(1,1<<B);v=F(value,1<<B)
 return v-error,v+error
def expi(arg,pi):return sine(add(arg,scale(pi,F(1,2))),pi),sine(arg,pi)
def run(a,p,freq,J=32):
 assert a>=512001 and p>=2 and J>=1
 pi,_,_,phases,_,_=constants(B);theta=ZERO
 for q,v in zip((2,3,5,7),freq):theta=add(theta,scale(phases[(2,3,4,5,7).index(q)][1],v))
 q=expi(scale(theta,2),pi);front=expi(scale(theta,a),pi)
 denom=(sub(ONE,q[0]),neg(q[1]));inv=cinv(denom)
 # Chord lower bound is taken from real/imag component intervals independently.
 def distance0(i):return min(abs(i[0]),abs(i[1])) if i[0]*i[1]>0 else F(0)
 d2=distance0(denom[0])**2+distance0(denom[1])**2
 dl=F(isqrt((d2.numerator<<(2*B))//d2.denominator),1<<B);assert dl>0
 vals=[]
 for k in range(J):
  n=a+2*k;li=log_normalized(n,B);assert li[0]>11
  vals.append(scale(recip(li),F(a,n)**p))
 total=(ZERO,ZERO);factor=inv
 for j in range(J):
  total=cadd(total,(mul(factor[0],vals[0]),mul(factor[1],vals[0])))
  vals=[sub(vals[k+1],vals[k]) for k in range(len(vals)-1)]
  factor=cmul(cmul(factor,q),inv)
 # Complete monotonicity: f(x)=(a/x)^p/log(x/4)=a^p integral_0^infty 4^t x^(-p-t)dt.
 # |Delta^J f(a)| <= (2/a)^J sum binom(J,k)(p+J)^(J-k)k!/11^(k+1).
 difference=F(2,a)**J*sum((F(comb(J,k)*(p+J)**(J-k)*factorial(k),11**(k+1)) for k in range(J+1)),F(0))
 # For unit q and 0<=r<=1, |1-q*r|>=|1-q|/2.
 rem=2*difference/dl**(J+1);rem=enclosure(rem,rem,B)[1]
 total=cmul(front,total);out=[enclosure(v[0]-rem,v[1]+rem,160) for v in total]
 widths=[(hi-lo)/2 for lo,hi in out]
 return {'a':a,'power':p,'frequency_prime_exponents':list(freq),'difference_terms':J,
  'definition':'sum_{k>=0} exp(i*theta*(a+2k))*(a/(a+2k))^p/log((a+2k)/4); theta=(pi/2)*sum exponent*log(prime)',
  'real_interval':[str(x) for x in out[0]],'imag_interval':[str(x) for x in out[1]],
  'chord_lower':str(dl),'difference_remainder_upper':str(rem),
  'maximum_component_radius':str(max(widths)),'radius_below_1e_minus40':max(widths)<F('1e-40'),
  'whole_inverse_moment_evaluated':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 rows=[]
 base=((1,0,0,0),(0,1,0,0),(2,0,0,0),(0,0,1,0),(0,0,0,1))
 frequencies=set(base)
 for x in base:
  for y in base:
   for sign in (-1,1):
    v=tuple(a+sign*b for a,b in zip(x,y))
    if not any(v):continue
    if next(a for a in v if a)!=abs(next(a for a in v if a)):v=tuple(-a for a in v)
    frequencies.add(v)
 for freq in sorted(frequencies):
  for start in (512001,512002):
   for power in (2,128):rows.append(run(start,power,freq))
 assert all(r['radius_below_1e_minus40'] for r in rows)
 # Independent closed-form geometric sequences verify the finite identity's signs and powers.
 checks=0
 for qr,qi in ((F(3,5),F(4,5)),(F(-1),F(0)),(F(0),F(1))):
  q=((qr,qr),(qi,qi));iv=cinv((sub(ONE,q[0]),neg(q[1])))
  for r in (F(1,4),F(3,4)):
   target=cinv((sub(ONE,scale(q[0],r)),neg(scale(q[1],r))))
   for J in (1,2,5,32):
    total=(ZERO,ZERO);factor=iv
    for j in range(J):
     total=cadd(total,cscale(factor,(r-1)**j));factor=cmul(cmul(factor,q),iv)
    rem=target
    for j in range(J):rem=cmul(cmul(rem,q),iv)
    combined=cadd(total,cscale(rem,(r-1)**J))
    assert all(max(a[0],b[0])<=min(a[1],b[1]) for a,b in zip(combined,target));checks+=1
 from pathlib import Path
 Path(a.output).write_text(json.dumps({'schema':'cone.oscillatory-log-tail.v1','nonzero_frequency_count':len(frequencies),'closed_geometric_identity_checks':checks,'cases':rows},indent=2,sort_keys=True)+'\n')
 print(json.dumps({'frequency_count':len(frequencies),'case_count':len(rows),'identity_checks':checks,'maximum_radius':float(max(F(r['maximum_component_radius']) for r in rows))}))
