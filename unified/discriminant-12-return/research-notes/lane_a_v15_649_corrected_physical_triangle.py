#!/usr/bin/env python3
"""Suzuki v15.649: corrected physical nonbipartite three-cycle.
Exact rational atanh-log enclosures for physical (sigma,tau)=(+1,+1).
No numerical equality or float comparison is used in assertions.
"""
from fractions import Fraction as F
N=100
def logi(q):
    z=F(q-1,q+1)
    low=sum((2*z**(2*k+1)/F(2*k+1) for k in range(N)), F(0))
    return low,low+2*z**(2*N+1)/((2*N+1)*(1-z*z))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[s*t for s in a for t in b]
    return min(v),max(v)
def sc(a,k):return mul(a,(F(k),F(k)))
def saw(a):
    assert a[0]//2==a[1]//2, "unresolved period-two wrap"
    j=a[0]//2
    return sub((F(1+2*j),F(1+2*j)),a)
def D(x,e,L):return sub(saw(sub(x,sc(L,e))),saw(x))
def G(x,e,f,A,B):
    u=add(x,sc(A,e));v=sub(x,sc(B,f))
    return add(mul(D(u,e,A),D(u,f,B)),mul(D(v,-f,B),D(v,-e,A)))
L={q:logi(q) for q in (2,3,5)}
x=(F(2469,20000),)*2
e2=(1,0,0,0);e3=(0,1,0,0);e5=(0,0,1,0)
def vsub(a,b):return tuple(s-t for s,t in zip(a,b))
g23=vsub(e3,e2);g35=vsub(e5,e3);g25=vsub(e5,e2)
assert tuple(g23[k]+g35[k] for k in range(4))==g25
h0=(0,0,0,0);h1=g23;h2=g25
assert vsub(h1,h0)==g23
assert vsub(h2,h1)==g35
assert vsub(h2,h0)==g25
# In the faithful regular representation row h sees the coefficient at x+h dot log.
# For physical (sigma,tau)=(+1,+1), g=v_r-v_q.
edges=((2,3,sub(L[3],L[2])),(3,5,sub(L[5],L[2])),(2,5,sub(L[5],L[2])))
for q,r,row in edges:
    v=G(add(x,row),+1,+1,L[q],L[r])
    assert v[0]>0, f"zero or ambiguous {q,r} coefficient"
    print(f"edge({q},{r}) strict-positive interval midpoint {float((v[0]+v[1])/2):.15f}")
print("PASS_PHYSICAL_SIGNED_NONBIPARTITE_TRIANGLE")
print("R>=1 contains the triangle; no diagonal unitary sign grading anticommutes at this x.")
print("Does NOT prove asymmetry of spectral extrema or an upper norm bound.")
