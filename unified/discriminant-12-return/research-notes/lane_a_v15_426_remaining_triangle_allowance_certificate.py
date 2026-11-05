#!/usr/bin/env python3
"""Outward-Decimal allowance after the audited v15.423 commutator bound.

This is a conditional triangle budget inside the same normalized tail
decomposition, not a bound on any uncomputed remainder and not FULL_K_TRANSFER.
"""
from decimal import Decimal as D, getcontext
getcontext().prec=100

def lo(x): return x.next_minus()
def hi(x): return x.next_plus()
def add(a,b): return lo(a[0]+b[0]),hi(a[1]+b[1])
def mul(a,b):
    z=[a[i]*b[j] for i in (0,1) for j in (0,1)]
    return lo(min(z)),hi(max(z))

Q=(2,3,4,5,7)
diag=(D(0),D(0))
for q in Q:
    l=D(q).ln(); L=(lo(l),hi(l)); rq=D(1)/D(q); R=(lo(rq),hi(rq))
    diag=add(diag,mul(mul(L,L),R))

# Frozen outward upper endpoint from v15.423 / audited Round 485.
x4_upper=D('323.936488148718861059877350839129801352317284106475204354056930156412541764177447515338418')
x_upper=hi(hi(x4_upper.sqrt()).sqrt())
comm_square_upper=hi(diag[1]+x_upper)
comm_upper=hi(comm_square_upper.sqrt())
target=D('2.535946')
allowance_lower=lo(target-comm_upper)

assert allowance_lower>D('0.0013')
assert comm_upper<target

print('diagonal_upper',diag[1])
print('joint_cross_upper',x_upper)
print('commutator_square_upper',comm_square_upper)
print('commutator_upper',comm_upper)
print('target',target)
print('remaining_triangle_allowance_lower',allowance_lower)
print('certified','if ||R|| < allowance_lower, then ||T+R|| < 2.535946')
print('scope','conditional same-normalization tail budget only; R not evaluated; no FULL_K_TRANSFER')
