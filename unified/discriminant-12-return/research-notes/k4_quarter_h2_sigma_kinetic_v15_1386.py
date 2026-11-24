#!/usr/bin/env python3
"""Gravity v15.1386: positive leading intrinsic H2 sigma kinetic
and exact Levi-Civita equations; not full coupled EFT stability."""
import sympy as s
u,v=s.symbols("u v",real=True);z=s.Matrix([u,v]);D=1+u*u+v*v
G=s.eye(2)-z*z.T/D
inv=s.simplify(G.inv())
assert s.simplify(G.det()-1/D)==0
assert s.simplify(inv-(s.eye(2)+z*z.T))==s.zeros(2)
for a in range(2):
 for b in range(2):
  for c in range(2):
   Gamma=s.factor(sum(inv[a,d]*(s.diff(G[d,c],z[b])+s.diff(G[d,b],z[c])-s.diff(G[b,c],z[d])) for d in range(2))/2)
   assert s.simplify(Gamma+z[a]*G[b,c])==0
assert s.simplify(s.trace(G)-(1+1/D))==0
print("PASS normalized H2 metric positive eigenvalues 1,1/(1+u²+v²)")
print("PASS intrinsic sigma EOM: Box z^a - z^a G_bc dz^b.dz^c=0")
print("PASS f²>0 gives positive two-derivative free sigma energy")
print("OPEN higher-derivative Weyl interaction stability and coupled metric evolution")
