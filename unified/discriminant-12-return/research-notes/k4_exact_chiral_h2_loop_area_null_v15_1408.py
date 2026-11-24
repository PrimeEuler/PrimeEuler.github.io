#!/usr/bin/env python3
"""Gravity v15.1408: exact nonlinear chiral H2 loop sigma solution.
Nonzero target holonomy does NOT imply nonzero spacetime area pullback:
rank-one map gives B=dphi1 wedge dphi2=0, so Weyl-F-B interaction off.
"""
import sympy as s
t,x,k,a,f,r=s.symbols('t x k a f r',real=True,positive=True)
w=k*(t-x)
u=a*s.cos(w);v=a*s.sin(w);phi=s.Matrix([u,v])
G=s.eye(2)-phi*phi.T/(1+u*u+v*v)
box=lambda z:-s.diff(z,t,2)+s.diff(z,x,2)
dot=lambda z,q:-s.diff(z,t)*s.diff(q,t)+s.diff(z,x)*s.diff(q,x)
E=[s.trigsimp(s.simplify(box(phi[j])-phi[j]*sum(G[p,q]*dot(phi[p],phi[q]) for p in range(2) for q in range(2)))) for j in range(2)]
assert E==[0,0]
Btx=s.simplify(s.diff(u,t)*s.diff(v,x)-s.diff(u,x)*s.diff(v,t))
assert Btx==0
L=-f*f*r*r*sum(G[p,q]*dot(phi[p],phi[q]) for p in range(2) for q in range(2))/2
assert s.simplify(L)==0
rho=s.trigsimp(s.simplify(f*f*r*r*sum(G[p,q]*s.diff(phi[p],t)*s.diff(phi[q],t) for p in range(2) for q in range(2))))
flux=s.trigsimp(s.simplify(f*f*r*r*sum(G[p,q]*s.diff(phi[p],t)*s.diff(phi[q],x) for p in range(2) for q in range(2))))
assert s.simplify(rho-f*f*r*r*a*a*k*k)==0
assert s.simplify(flux+rho)==0
angle=2*s.pi*(s.sqrt(1+a*a)-1)
assert s.simplify(angle.subs(a,s.Rational(3,4))-s.pi/2)==0
assert s.simplify(s.sinh(s.log(2))*s.cosh(s.log(2))-s.Rational(15,16))==0
print('PASS exact nonlinear H2 sigma null traveling loop for arbitrary a,k')
print('PASS a=3/4 yields intrinsic pi/2 target holonomy and positive null stress',rho)
print('NEGATIVE rank-one spacetime pullback B=0: no Weyl–Maxwell area coupling')
print('NEGATIVE amplitude freely chosen; full Einstein backreaction open')
