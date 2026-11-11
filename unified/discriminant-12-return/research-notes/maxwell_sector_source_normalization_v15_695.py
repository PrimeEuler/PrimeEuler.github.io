#!/usr/bin/env python3
"""v15.695: independently reproduce minimal metric/EM source and grading obstruction."""
import sympy as s
z,t,B0,eps=s.symbols("z t B0 eps",real=True)
a=s.Function("a")(t,z)
b=s.Function("b")(t,z)
A=s.Function("A")(t,z)
Ay=B0*z+eps*a
L=s.exp(2*eps*b)/2*(s.diff(Ay,t)**2-s.diff(Ay,z)**2)
Lfull=s.exp(2*eps*b)/2*(s.diff(A,t)**2-s.diff(A,z)**2)
EL=s.diff(s.diff(Lfull,s.diff(A,t)),t)+s.diff(s.diff(Lfull,s.diff(A,z)),z)
wave=s.simplify(EL.subs(A,Ay))
lin=s.simplify(s.diff(wave,eps).subs(eps,0))
assert s.simplify(lin-(s.diff(a,t,2)-s.diff(a,z,2)-2*B0*s.diff(b,z)))==0
coeff2=s.expand(s.diff(L,eps,2).subs(eps,0)/2)
az=s.Symbol("az")
poly=s.expand(coeff2.subs(s.diff(a,z),az))
assert s.simplify(poly.coeff(B0,1).coeff(az,1)+2*b)==0
chi=s.diag(1,1,-1,-1)
P=(s.eye(4)+chi)/2
u,v,w,x=s.symbols("u v w x")
W=s.Matrix([[0,0,u,v],[0,0,w,x],[u,w,0,0],[v,x,0,0]])
assert chi*W+W*chi==s.zeros(4)
assert P*W*P==s.zeros(4)
g=s.symbols("g",nonzero=True)
assert chi*(g*W)*(g*W)-(g*W)*(g*W)*chi==s.zeros(4)
assert P*(g*W)*(g*W)*P-g*g*(P*W*W*P)==s.zeros(4)
print("PASS: metric/EM source is 2 B0 partial_z b")
print("PASS: odd rung has zero EM->EM matrix elements; even composite normalization free")
