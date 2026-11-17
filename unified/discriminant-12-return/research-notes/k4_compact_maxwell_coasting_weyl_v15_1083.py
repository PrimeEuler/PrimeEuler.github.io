#!/usr/bin/env python3
"""Canonical Gravity v15.1083 reproducer; v15.1082 provisional script superseded
because Sandbox landed its v15.1082 entry earlier. Do not alter Sandbox work.
Derives the tensor electric Weyl jet with physical Maxwell stress a^-4.
"""
import sympy as s
t=s.symbols("t",real=True)
H,q,M,K,a0,P0,P2=s.symbols("H q M K a0 P0 P2",real=True)
J=2*K/a0**2*s.exp(-2*H*t)*(P0+P2*t*t/2)
coeff=s.symbols("c0:6")
h=sum(coeff[n]*t**n for n in range(6))
eq=s.diff(h,t,2)+2*H*s.diff(h,t)+(q*q+M)*h-J
sol={coeff[0]:s.S.Zero,coeff[1]:s.S.Zero}
for n in range(4):
    expression=s.series(eq.subs(sol),t,0,n+1).removeO().expand().coeff(t,n)
    sol[coeff[n+2]]=s.factor(s.solve(expression,coeff[n+2])[0])
h=s.expand(h.subs(sol))
weyl=s.exp(-2*H*t)*(s.diff(h,t,2)-q*q*h)/(4*a0*a0)
w=[s.factor(s.series(weyl,t,0,3).removeO().expand().coeff(t,i)) for i in range(3)]
assert s.simplify(w[0]-K*P0/(2*a0**4))==0
assert s.simplify(w[1]+3*H*K*P0/a0**4)==0
assert s.simplify(w[2]-K*(32*H**2*P0-M*P0-2*q*q*P0+P2)/(4*a0**4))==0
psi=a0*s.exp(H*t)*h
assert all(s.simplify(s.series(
 s.diff(psi,t,2)+(q*q+M-H**2)*psi-a0*s.exp(H*t)*J,
 t,0,4).removeO().expand().coeff(t,n))==0 for n in range(4))
zeta=s.symbols("zeta",real=True)
assert s.simplify((M-H**2).subs({M:8*zeta/9,H:1/s.sqrt(3)})-(8*zeta-3)/9)==0
print("PASS canonical v15.1083 coasting Maxwell source and tensor electric Weyl")
print("Weyl series =",w)
