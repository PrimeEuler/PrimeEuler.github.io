#!/usr/bin/env python3
"""Lane A Suzuki: exact nonbipartite 3-cycle in signed B_R(x).
Certifies no diagonal sign grading anticommutes with this finite field.
Original frozen physical q/r transported G as v15.420; rational
atanh logarithm interval enclosures, no floating assertions.
"""
from fractions import Fraction as F
N = 100
def logi(q):
    z = F(q - 1, q + 1)
    low = sum((2 * z**(2*k+1) / F(2*k+1) for k in range(N)), F(0))
    return low, low + 2 * z**(2*N+1) / ((2*N+1)*(1-z*z))
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    v=[s*t for s in a for t in b]
    return min(v),max(v)
def sc(a,k): return mul(a,(F(k),F(k)))
def saw(a):
    assert a[0]//2 == a[1]//2, "unresolved wrap"
    j = a[0]//2
    return sub((F(1+2*j),F(1+2*j)), a)
def D(x,e,L): return sub(saw(sub(x,sc(L,e))),saw(x))
def G(x,e,f,A,B):
    u=add(x,sc(A,e));v=sub(x,sc(B,f))
    return add(mul(D(u,e,A),D(u,f,B)),
               mul(D(v,-f,B),D(v,-e,A)))
Ls={q:logi(q) for q in (2,3,5)}
x=(F(2469,20000),)*2
# Vertices in the integer Z4 regular-representation cube: v0=0,
# v1=(-1,1,0,0)=e3-e2, v2=(-1,0,1,0)=e5-e2.
# Their differences are v1-v0=g23, v2-v1=g35, v2-v0=g25,
# each physical shift belonging to (sigma,tau)=(-1,+1).
three=(
    (2,3,sub(Ls[3],Ls[2])),
    (3,5,sub(Ls[5],Ls[2])),
    (2,5,sub(Ls[5],Ls[2])),
)
for q,r,hlog in three:
    value=G(add(x,hlog),-1,+1,Ls[q],Ls[r])
    assert value[0]>0, f"zero/ambiguous physical coefficient for {q,r}"
    print(f"edge({q},{r}): strict_positive; rational interval midpoint≈{float((value[0]+value[1])/2):.12f}")
print("PASS_EXACT_NONBIPARTITE_3_CYCLE")
print("No diagonal sign grading can anticommute with B_R(x=2469/20000), R>=1.")
print("Does not rule out non-diagonal symmetries or certify spectral norm.")
