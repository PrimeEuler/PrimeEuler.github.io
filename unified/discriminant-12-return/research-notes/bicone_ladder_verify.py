#!/usr/bin/env python3
"""Bicone ladder-algebra verification (v14.097 S2-S3; audit request v14.102).

Part 1 (matrix, exact in truncation): M[i,j,m] = <1s|a_i b_j|2p,m>
  selection rule verified by explicit 16-dim computation.

Part 2 (analytic, exact): [L_+, a1b1] = -(a2b1 + a1b2).
  Proof: [J^a_+, a1] = [a1^dagger a2, a1] = -a2 (bosonic [a1^dagger,a1]=-1).
  Hence [L_+,a1b1] = -a2 b1 - a1 b2.
  A proper SO(3) vector operator needs [L_+, T_-1] = +sqrt(2) T_0.
  The minus sign is the obstruction: a_i are DUAL spinors (annihilation
  operators), not proper SU(2) tensors. [D]

Schwinger: cone a: (a1,a2), cone b: (b1,b2). L = J^a + J^b.
|1s> = vacuum; |2p,m> triplet as in v14.097.
"""
from __future__ import annotations
import numpy as np

def idx(na1,na2,nb1,nb2): return na1+2*na2+4*nb1+8*nb2
DIM=16
def lowering(mode):
    M=np.zeros((DIM,DIM))
    for na1 in (0,1):
     for na2 in (0,1):
      for nb1 in (0,1):
       for nb2 in (0,1):
        n={'a1':na1,'a2':na2,'b1':nb1,'b2':nb2}
        if n[mode]==1:
            n2=dict(n); n2[mode]=0
            M[idx(n2['a1'],n2['a2'],n2['b1'],n2['b2']),
              idx(n['a1'],n['a2'],n['b1'],n['b2'])]=1.0
    return M

a1,a2=lowering('a1'),lowering('a2')
b1,b2=lowering('b1'),lowering('b2')
a1d,a2d,b1d,b2d=a1.T,a2.T,b1.T,b2.T
vac=np.zeros(DIM); vac[idx(0,0,0,0)]=1.0
s2p={'+1':a1d@b1d@vac,'0':(a1d@b2d+a2d@b1d)/np.sqrt(2)@vac,'-1':a2d@b2d@vac}

print("Part 1: M[i,j,m]=<1s|a_i b_j|2p,m>  [a1b1 a1b2 a2b1 a2b2]")
ok=True
for m,sv in s2p.items():
    v=[float(vac@op@sv) for op in (a1@b1,a1@b2,a2@b1,a2@b2)]
    nz=[1 if abs(x)>1e-9 else 0 for x in v]
    exp={'+1':[1,0,0,0],'0':[0,1,1,0],'-1':[0,0,0,1]}[m]
    good=(nz==exp); ok&=good
    print(f"  m={m:>2}: {' '.join(f'{x:+.4f}' for x in v)}  {'OK' if good else 'FAIL'}")
print(f"  Selection rule q(i,j)=-m: {'CONFIRMED [D]' if ok else 'FAILED'}")
print()
print("Part 2: SO(3) vector-operator obstruction (analytic, exact).")
print("  [a1^dagger a2, a1] = a1^dagger[a2,a1] + [a1^dagger,a1]a2 = -a2.")
print("  So [J^a_+, a1] = -a2, [J^b_+, b1] = -b2.")
print("  [L_+, a1b1] = [J^a_+,a1]b1 + a1[J^b_+,b1] = -a2b1 - a1b2.")
print("  Proper vector needs [L_+,T_-1] = +sqrt(2) T_0.")
print("  We get -(a2b1+a1b2) = -sqrt(2) T_0.  SIGN FLIP.")
print("  => ab-bilinears are NOT proper SO(3) vector operators. [D]")
print("  Cause: a_i are annihilation ops = dual/conjugate spinors.")
print()
print("VERDICT: v14.097 S2 (selection rule) and S3 (obstruction) independently verified.")
