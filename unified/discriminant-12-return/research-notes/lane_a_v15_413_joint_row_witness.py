#!/usr/bin/env python3
"""Exact rational enclosure of a joint five-frequency absolute-Schur row.
Independent replay: python3 lane_a_v15_413_joint_row_witness.py
Only proves a limitation of the absolute-row certificate, NOT an
operator-norm lower bound or a whole-tail obstruction.
"""
from fractions import Fraction as F
from math import isqrt
from itertools import combinations, product
P = 10**35
N = 140
QS = (2, 3, 4, 5, 7)
def log_bounds(q):
    x = F(q-1,q+1)
    s = sum((2*x**(2*k+1)/F(2*k+1) for k in range(N)), F(0))
    e = 2*x**(2*N+1)/((2*N+1)*(1-x*x))
    return s, s+e
def sqrt_bounds(q):
    t = isqrt(q*P*P)
    return F(t,P), F(t+1,P)
def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def neg(a):return -a[1],-a[0]
def scale(a,s):return mul(a,(F(s),F(s)))
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def mod2(a):
    assert a[0]//2 == a[1]//2, "ambiguous sawtooth wrap"
    t=a[0]//2
    return sub(a,(F(2*t),F(2*t)))
def saw(a):return sub((F(1),F(1)),mod2(a))
def shift_diff(x,sign,ell):return sub(saw(sub(x,scale(ell,sign))),saw(x))
def abs_interval(a):
    if a[0]>=0:return a
    if a[1]<=0:return neg(a)
    return F(0),max(-a[0],a[1])
Ls={q:log_bounds(q) for q in QS}
alpha={q:div(Ls[q],scale(sqrt_bounds(q),2)) for q in QS}
x=(F(3,1250),)*2
joint=(F(0),F(0))
for q,r in combinations(QS,2):
    A,B=Ls[q],Ls[r]
    raw=(F(0),F(0))
    for s,t in product((-1,1),repeat=2):
        u=add(x,scale(A,s))
        v=sub(x,scale(B,t))
        g=add(mul(shift_diff(u,s,A),shift_diff(u,t,B)),
              mul(shift_diff(v,-t,B),shift_diff(v,-s,A)))
        raw=add(raw,abs_interval(g))
    pair=mul(mul(alpha[q],alpha[r]),raw)
    joint=add(joint,pair)
    print(f'{q},{r}: {float(pair[0]):.12f} <= row contribution <= {float(pair[1]):.12f}')
assert joint[0]>F(11,2) # strict, certified >5.5
assert joint[0]>F(425,100) # strict, certified >4.25 >4.249030...
assert joint[1]<F(56,10)
print('CERTIFIED 5.5 < joint absolute row at x=3/1250 < 5.6')
print('joint enclosure midpoint',float((joint[0]+joint[1])/2))
print('all sawtooth wrap intervals unambiguous')
