#!/usr/bin/env python3
"""v15.1421: Weyl zero in 3D and representative higher-derivative
metric variation in curvature-F-B EFT. A derivative-order warning,
NOT a ghost theorem or full covariant tensor principal symbol.
"""
import sympy as s
r00,r11,r22,r01,r02,r12=s.symbols("r00 r11 r22 r01 r02 r12",real=True)
g=s.eye(3)
Ric=s.Matrix([[r00,r01,r02],[r01,r11,r12],[r02,r12,r22]])
scalar=s.trace(Ric)
P=Ric-scalar*g/4
R=lambda a,b,c,d:g[a,c]*P[b,d]-g[a,d]*P[b,c]-g[b,c]*P[a,d]+g[b,d]*P[a,c]
assert s.Matrix([[s.simplify(sum(R(k,i,k,j) for k in range(3))) for j in range(3)] for i in range(3)])==Ric
W=lambda a,b,c,d:s.simplify(R(a,b,c,d)-(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])+scalar*(g[a,c]*g[b,d]-g[a,d]*g[b,c])/2)
assert all(W(a,b,c,d)==0 for a in range(3) for b in range(3) for c in range(3) for d in range(3))
t=s.symbols("t",real=True)
h=s.Function("h")(t);A=s.Function("A")(t);B=s.Function("B")(t)
lam=s.symbols("lambda",real=True)
L=lam*s.diff(h,t,2)*s.diff(A,t)*B
Eh=s.simplify(s.diff(s.diff(L,s.diff(h,t,2)),t,2))
EA=s.simplify(-s.diff(s.diff(L,s.diff(A,t)),t))
assert s.simplify(Eh-lam*s.diff(B*s.diff(A,t),t,2))==0
assert s.simplify(EA+lam*s.diff(B*s.diff(h,t,2),t))==0
assert Eh.has(s.diff(A,t,3))
assert EA.has(s.diff(h,t,3))
print("PASS D=3 Weyl identically zero, hence full Weyl area interaction zero in 2+1")
print("PASS representative linearized curvature-F-B term yields third derivatives by variation")
print("NEGATIVE cannot infer full EFT ghost or causal front without all tensor and constraints")
