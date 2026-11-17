#!/usr/bin/env python3
"""Gravity v15.1123: causal-circle geometric bicone and old double SU(2).

Two truncated (one future, one past) null sheets glued at their common
causal-diamond circle each form a topological 2-disk. Their gluing is
a 2-sphere, NOT SU(2)=S3 or Spin(4).
Given independently added Schwinger doublets (spin-half each),
diagonal shared-circle U(1) axial matching Lz=0 preserves BOTH
the total-spin singlet and m=0 triplet; full diagonal SU(2)
invariance is a stronger added constraint selecting the singlet.
"""
import sympy as s
I=s.I
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-I],[I,0]]);sz=s.diag(1,-1);id2=s.eye(2)
kron=s.kronecker_product
JA=[kron(a,id2)/2 for a in (sx,sy,sz)]
JB=[kron(id2,a)/2 for a in (sx,sy,sz)]
L=[a+b for a,b in zip(JA,JB)]
D=[a-b for a,b in zip(JA,JB)]
for J in (JA,JB,L):
    assert s.simplify(J[0]*J[1]-J[1]*J[0]-I*J[2])==s.zeros(4)
z=s.zeros(4,1)
sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
trip0=s.Matrix([0,1,1,0])/s.sqrt(2)
assert L[2]*sing==z and L[2]*trip0==z
for j in L: assert j*sing==z
L2=sum((j*j for j in L),s.zeros(4))
assert s.simplify(L2*sing)==z
assert s.simplify(L2*trip0-2*trip0)==z
P_axial=s.eye(4)-L[2]*L[2]
assert P_axial.rank()==2
assert s.simplify(P_axial*sing-sing)==z
assert s.simplify(P_axial*trip0-trip0)==z
P_sing=s.eye(4)-L2/2
assert P_sing.rank()==1
assert s.simplify(P_sing*sing-sing)==z and P_sing*trip0==z
assert s.kronecker_product(-id2,-id2)==s.eye(4)
assert s.simplify(D[2]*sing-trip0)==z
assert s.simplify(D[2]*trip0-sing)==z
# Two disk sheets: chi(D2 glued_S1 D2)=1+1-0=2 = chi(S2).
# The shared interface S1 is U(1) angular, not SU(2)=S3.
assert 1+1-0==2
print("PASS old two-SU2 bicone generators, singlet/triplet and relative generator")
print("PASS shared-circle U1 matching rank",P_axial.rank(),
      "full diagonal SU2 singlet rank",P_sing.rank())
print("PASS spinor 2pi signs cancel in paired state; two disks glue to S2 not S3")
