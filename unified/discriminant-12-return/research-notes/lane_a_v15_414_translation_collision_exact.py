#!/usr/bin/env python3
"""Exact arithmetic for cross-pair translation collisions."""
from fractions import Fraction as F
from itertools import combinations,product
Q=(2,3,4,5,7)
by_label={}
for q,r in combinations(Q,2):
    for s,t in product((-1,1),repeat=2):
        v=F(q if s==1 else 1,q if s==-1 else 1)*F(r if t==1 else 1,r if t==-1 else 1)
        by_label.setdefault(v,[]).append((q,r,s,t))
assert sum(map(len,by_label.values()))==40
collisions={v:rows for v,rows in by_label.items() if len(rows)>1}
assert not collisions,collisions
assert len(by_label)==40
# log(v) = log(w) mod 2 iff v/w=e^(2k). For rational v/w,
# Lindemann-Weierstrass rules out nonzero integer k; k=0 => v=w.
print("CERTIFIED: 40/40 distinct rational translation labels")
print("All 40 log-labels distinct modulo period 2")
print("No cross-pair common-shift coefficient combination available")
