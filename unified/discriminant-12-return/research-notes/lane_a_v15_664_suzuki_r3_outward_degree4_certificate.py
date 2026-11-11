#!/usr/bin/env python3
"""Suzuki R=3 outward all-arc B^4 certificate.

Uses exact-rational log/sqrt/cut/word-state enclosures and conservative
IEEE-754 sparse-product/row-sum error envelopes.  This certifies R=3 only;
it is not a radius-16 certificate.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import time
from fractions import Fraction as F
from math import isqrt
from itertools import combinations,product
from multiprocessing import Pool
from importlib.util import spec_from_file_location,module_from_spec
import numpy as np

PTH='unified/discriminant-12-return/research-notes/lane_a_v15_657_suzuki_positive_polynomial_small_radius_probe.py'
sp=spec_from_file_location('producer',PTH); producer=module_from_spec(sp);sp.loader.exec_module(producer)

# Exact rational intervals, following audited v15.645.
P=10**45; N=220; QS=(2,3,4,5,7); R=3
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def scale(a,s):return mul(a,(F(s),F(s)))
def div(a,b):assert b[0]>0;return mul(a,(1/b[1],1/b[0]))
def logbound(q):
 x=F(q-1,q+1);s=sum((2*x**(2*k+1)/F(2*k+1) for k in range(N)),F())
 e=2*x**(2*N+1)/((2*N+1)*(1-x*x));return s,s+e
def sqrtbound(q):
 k=isqrt(q*P*P);return F(k,P),F(k+1,P)
LS={q:logbound(q) for q in QS}
ALPHA={q:div(LS[q],scale(sqrtbound(q),2)) for q in QS}
def mod2(a):
 assert a[0]//2==a[1]//2,(float(a[0]),float(a[1]))
 return sub(a,scale((F(2),F(2)),a[0]//2))
def saw(a):return sub((F(1),F(1)),mod2(a))
def D(x,s,L):return sub(saw(sub(x,scale(L,s))),saw(x))
def G(x,s,t,A,B):
 y=add(x,scale(A,s));z=sub(x,scale(B,t))
 return add(mul(D(y,s,A),D(y,t,B)),mul(D(z,-t,B),D(z,-s,A)))

TOL=F(1,10**12)
INPUT_TOL=F(1,10**15)
STATE_TOL=F(1,10**15)
for q in QS:
 lf=F.from_float(float(producer.L[q]));assert LS[q][0]-INPUT_TOL<lf<LS[q][1]+INPUT_TOL
 sf=F.from_float(float(np.sqrt(q)));si=sqrtbound(q);assert si[0]-INPUT_TOL<sf<si[1]+INPUT_TOL

# Certify every finite word-state coefficient lies within 1e-12 of its float replay.
max_state_error=F()
for q,r in combinations(QS,2):
 for s,t in product((-1,1),repeat=2):
  A,B=LS[q],LS[r]
  cuts=[(F(),F()),(F(2),F(2)),mod2(scale(A,-s)),mod2(scale(B,t)),mod2(sub(scale(B,t),scale(A,s)))]
  cuts=sorted(cuts,key=lambda z:z[0])
  for left,right in zip(cuts,cuts[1:]):
   assert left[1]<right[0]
   x=(left[1]+right[0])/2; xi=(x,x)
   exact=mul((F(s*t),F(s*t)),mul(ALPHA[q],mul(ALPHA[r],G(xi,s,t,A,B))))
   xf=float(x)
   vf=s*t*producer.ALPHA[q]*producer.ALPHA[r]*producer.G(xf,s,t,producer.L[q],producer.L[r])
   v=F.from_float(float(vf))
   err=max(abs(v-exact[0]),abs(v-exact[1]));max_state_error=max(max_state_error,err)
   assert err<STATE_TOL,(q,r,s,t,float(err))

# Exact global cut ordering and certified agreement with binary64 cut labels.
def cut_interval(k):
 z=(F(),F())
 for ki,q in zip(k,(2,3,5,7)):z=add(z,scale(LS[q],-ki))
 return mod2(z)
EXACT=[]
for k0 in range(-R-1,R+2):
 for k1,k2,k3 in product(range(-R,R+1),repeat=3):
  EXACT.append(cut_interval((k0,k1,k2,k3)))
EXACT.sort(key=lambda z:z[0])
for a,b in zip(EXACT,EXACT[1:]):assert a[1]<b[0]
FCUTS=producer.cuts(R)
assert len(EXACT)==len(FCUTS)==3087
for I,c in zip(EXACT,FCUTS):
 cf=F.from_float(float(c));assert I[0]-TOL<cf<I[1]+TOL
MARGIN=F(1,10**6)
MID=[]
for i,c in enumerate(FCUTS):
 wrap=i+1==len(FCUTS); right=float(FCUTS[(i+1)%len(FCUTS)])+(2 if wrap else 0)
 xu=(float(c)+right)/2; xf=xu%2; xq=F.from_float(xu)
 li=EXACT[i];ri=EXACT[(i+1)%len(EXACT)];rlo=ri[0]+(2 if wrap else 0)
 assert xq>li[1]+MARGIN and xq<rlo-MARGIN
 MID.append(xf)

U=F(1,2**53)
def gamma(k):
 x=F(k)*U;assert x<1;return x/(1-x)
def rowstats(A):
 counts=np.diff(A.indptr);k=int(counts.max())
 obs=float(np.asarray(abs(A).sum(axis=1)).ravel().max())
 oq=F.from_float(obs);up=oq/(1-gamma(k))
 return up,k

# True coefficient matrix differs from stored CSR by <1e-9 in infinity norm.
# 40 source words per row; 1e-12 certified per term, with a >20x reserve for
# COO duplicate accumulation and elementary binary operations.
E=F(1,10**9)
TARGET=F(41,10)**4
def work(x):
 B=producer.assemble(R,x);B2=B@B;B4=B2@B2
 m,k1=rowstats(B);c2,k2=rowstats(B2);c4,k4=rowstats(B4)
 r2=gamma(2*k1)*m*m
 r4=r2*(m*m+c2)+gamma(2*k2)*c2*c2
 perturb=(m+E)**4-m**4
 total=c4+r4+perturb
 assert total<TARGET,(x,float(total**F(1,4)))
 return total,x,k1,k2,k4

if __name__=='__main__':
 print('max_exact_word_state_error',float(max_state_error),'cuts',len(MID),flush=True)
 start=time.time();best=(F(),None,None,None,None)
 with Pool(6) as pool:
  for j,z in enumerate(pool.imap_unordered(work,MID,chunksize=1),1):
   if z[0]>best[0]:best=z
   if j%250==0:print('progress',j,'root_bound',float(best[0])**.25,'seconds',time.time()-start,flush=True)
 print('CERTIFIED_R3_B4',len(MID),float(best[0]),float(best[0])**.25,best[1:],time.time()-start)
 print('TARGET4',float(TARGET),'PASS',best[0]<TARGET)
