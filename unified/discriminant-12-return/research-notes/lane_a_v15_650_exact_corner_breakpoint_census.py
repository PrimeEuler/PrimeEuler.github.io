#!/usr/bin/env python3
"""Suzuki finite matrix-field active sawtooth corner census.
Exact integer enumeration for R=1..6 and symbolic full-R formula.
This script is NOT a norm upper certificate.
"""
from itertools import combinations,product
from collections import Counter
V={2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),5:(0,0,1,0),7:(0,0,0,1)}
def add(u,v):return tuple(a+b for a,b in zip(u,v))
def sc(u,k):return tuple(k*x for x in u)
def inside(h,R):return all(-R<=x<=R for x in h)
def census(R):
    corners=set()
    usage=Counter()
    entries=0
    for h in product(range(-R,R+1),repeat=4):
        for q,r in combinations(V,2):
            for sigma,tau in product((-1,1),repeat=2):
                corner_a=add(h,sc(V[q],sigma))
                corner_d=add(h,sc(V[r],-tau))
                target=add(corner_a,sc(V[r],-tau))
                if not inside(target,R):continue
                entries+=1
                for k in {h,corner_a,corner_d,target}:
                    corners.add(k)
                    usage[k]+=1
    expected={(k0,k1,k2,k3)
      for k0 in range(-R-1,R+2)
      for k1,k2,k3 in product(range(-R,R+1),repeat=3)}
    assert corners==expected, f"active corner set mismatch R={R}"
    assert len(corners)==(2*R+3)*(2*R+1)**3
    assert max(usage.values())<=160
    return (R,(2*R+1)**4,entries,len(corners),max(usage.values()))
if __name__=='__main__':
    for R in (1,2,3,4,5,6):
        print('radius,sites,nonzeros,active_corners,max_entries_per_breakpoint=',census(R))
    R=16
    print('R16_exact_active_breakpoint_count=',(2*R+3)*(2*R+1)**3)
    print('PASS_INTEGER_CORNER_CENSUS_R1_TO_R6')
    print('Full-R formula requires accompanying combinatorial proof in ledger v15.650.')
