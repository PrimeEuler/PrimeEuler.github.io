#!/usr/bin/env python3
"""Outward-Decimal interval certificate for the five-frequency X^4 Schur gate."""
from decimal import Decimal as D, getcontext
from itertools import combinations, product
from bisect import bisect_right
getcontext().prec=90
Q=(2,3,4,5,7); PR=(2,3,5,7); Z=(0,0,0,0)

def down(x):return x.next_minus()
def up(x):return x.next_plus()
def I(x):x=D(x);return x,x
def add(a,b):return down(a[0]+b[0]),up(a[1]+b[1])
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[a[i]*b[j] for i in (0,1) for j in (0,1)]
 return down(min(z)),up(max(z))
def scl(a,z):z=D(z);return (down(a[0]*z),up(a[1]*z)) if z>=0 else (down(a[1]*z),up(a[0]*z))
def absi(a):
 if a[0]>=0:return a
 if a[1]<=0:return -a[1],-a[0]
 return D(0),max(-a[0],a[1])
LOG={p:(down(D(p).ln()),up(D(p).ln())) for p in PR}
SQ={q:(down(D(q).sqrt()),up(D(q).sqrt())) for q in {a*b for a,b in combinations(Q,2)}}

def qv(q):return (2,0,0,0) if q==4 else tuple(int(p==q) for p in PR)
def va(a,b):return tuple(x+y for x,y in zip(a,b))
def vs(a,n):return tuple(n*x for x in a)
def ex(c,v):
 o=I(c)
 for n,p in zip(v,PR):
  if n:o=add(o,scl(LOG[p],n))
 return o
def canon(c,v):
 lo,hi=ex(c,v);n=int((lo/D(2)).to_integral_value(rounding='ROUND_FLOOR'))
 assert D(2)*n<=lo and hi<D(2)*(n+1)
 return int(D(c)-D(2)*n),v
def reduce_expr(c,v):
 lo,hi=ex(c,v);n=int((lo/D(2)).to_integral_value(rounding='ROUND_FLOOR'))
 assert D(2)*n<=lo and hi<D(2)*(n+1)
 return D(c)-D(2)*n,v
def pa(a,b):return canon(a[0]+b[0],va(a[1],b[1]))
P0=(0,Z)
def pv(p):return ex(*p)
def pf(p):a=pv(p);return float((a[0]+a[1])/2)
def order(s):
 z=sorted(set(s),key=pf)
 for a,b in zip(z,z[1:]):assert pv(a)[1]<pv(b)[0]
 assert z[0]==P0
 return z
def mid(z):
 return [(pv(p)[1]+(pv(z[i+1])[0] if i+1<len(z) else D(2)))/2 for i,p in enumerate(z)]
def es(x,v,n=1):return x[0],va(x[1],vs(v,n))
def saw(x):
 lo,hi=ex(*x);k=int((lo/D(2)).to_integral_value(rounding='ROUND_FLOOR'))
 assert D(2)*k<lo and hi<D(2)*(k+1)
 return sub(I(1+2*k),(lo,hi))
def dd(s,x,L):return sub(saw(es(x,L,-s)),saw(x))

T=[]
for q,r in combinations(Q,2):
 A=qv(q);B=qv(r)
 for s,t in product((-1,1),repeat=2):
  sh=canon(0,va(vs(B,t),vs(A,-s)));bp={P0,canon(0,vs(A,-s)),canon(0,vs(B,t)),sh}
  T.append((q,r,s,t,A,B,sh,bp))
def cf(a,x):
 q,r,s,t,A,B,sh,bp=a;u=es(x,A,s);v=es(x,B,-t)
 g=add(mul(dd(s,u,A),dd(t,u,B)),mul(dd(-t,v,B),dd(-s,v,A)))
 la=ex(0,A);lb=ex(0,B);sq=SQ[q*r];w=mul(mul(la,lb),(down(D(1)/(D(4)*sq[1])),up(D(1)/(D(4)*sq[0]))))
 return scl(mul(w,g),s*t)

L2=order({pa(a[6],b[6]) for a in T for b in T});GI={p:i for i,p in enumerate(L2)};pairs=[[] for _ in L2]
for i,a in enumerate(T):
 for j,b in enumerate(T):pairs[GI[pa(a[6],b[6])]].append((i,j))
B2=set()
for a in T:
 B2.update(a[7])
 for b in T:B2.update(pa(z,a[6]) for z in b[7])
B2=order(B2); H=[];R=[]
for x in mid(B2):
 xe=(x,Z);base=[cf(a,xe) for a in T];row=[]
 shifted=[[cf(T[j],es(xe,T[i][6][1],-1)) for j in range(40)] for i in range(40)]
 for ij in pairs:
  h=I(0)
  for i,j in ij:h=add(h,mul(base[i],shifted[i][j]))
  row.append(h)
 H.append(row);R.append(sum((absi(h)[1] for h in row),D(0)))
BF=set(B2)
for g in L2:BF.update(pa(b,g) for b in B2)
BF=order(BF);bf=[pf(p) for p in B2]
def loc(x):
 c=reduce_expr(*x);ci=pv(c);k=bisect_right(bf,pf(c))-1;ri=pv(B2[k+1]) if k+1<len(B2) else I(2)
 assert pv(B2[k])[1]<ci[0] and ci[1]<ri[0],(k,pv(B2[k]),ci,ri,c)
 return k
mx=D(0)
for x in mid(BF):
 ix=loc((x,Z));tot=D(0)
 for g,h in zip(L2,H[ix]):tot=up(tot+up(absi(h)[1]*R[loc((x-g[0],vs(g[1],-1)))]))
 mx=max(mx,tot)
target=D('2.535946');diag=I(0)
for q in Q:
 l=ex(0,qv(q));rq=D(1)/D(q);diag=add(diag,mul(mul(l,l),(down(rq),up(rq))))
budget=down(target*target-diag[1]);b4=down(budget**4)
assert mx<b4
print('x2_labels',len(L2));print('x2_cells',len(B2));print('x4_row_cells',len(BF))
print('x4_row_upper',mx);print('fourth_root_upper',mx.sqrt().sqrt())
print('budget_lower',budget);print('budget_fourth_power_lower',b4);print('fourth_power_margin',b4-mx)
print('certified','||X|| < 2.535946^2-D');print('scope','five-frequency commutator only')
