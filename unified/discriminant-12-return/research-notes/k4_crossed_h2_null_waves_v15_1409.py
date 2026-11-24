#!/usr/bin/env python3
"""Gravity v15.1409: crossed 2-direction null internal H2 waves.
Pullback area nonzero at order ab, while exact nonlinear sigma EOM
residual starts at fifth order; this is perturbative not on-shell exact.
"""
import sympy as s
t,x,y,a,b=s.symbols('t x y a b',real=True)
u=a*s.sin(t-x);v=b*s.sin(t-y)
phi=[u,v];D=1+u*u+v*v
G=s.eye(2)-s.Matrix(phi)*s.Matrix(phi).T/D
coords=[t,x,y];sgn=[-1,1,1]
dot=lambda f,g:s.simplify(sum(sgn[i]*s.diff(f,coords[i])*s.diff(g,coords[i]) for i in range(3)))
box=lambda f:s.simplify(sum(sgn[i]*s.diff(f,coords[i],2) for i in range(3)))
E=[s.trigsimp(s.factor(box(phi[i])-phi[i]*sum(G[j,k]*dot(phi[j],phi[k]) for j in range(2) for k in range(2)))) for i in range(2)]
C=a*b*s.cos(t-x)*s.cos(t-y)
Btx=s.diff(u,t)*s.diff(v,x)-s.diff(u,x)*s.diff(v,t)
Bty=s.diff(u,t)*s.diff(v,y)-s.diff(u,y)*s.diff(v,t)
Bxy=s.diff(u,x)*s.diff(v,y)-s.diff(u,y)*s.diff(v,x)
assert s.simplify(Btx-C)==0 and s.simplify(Bty+C)==0 and s.simplify(Bxy-C)==0
assert s.simplify(E[0]+2*a**3*b**2*s.sin(t-x)**2*s.sin(t-y)*s.cos(t-x)*s.cos(t-y)/D)==0
assert s.simplify(E[1]+2*a**2*b**3*s.sin(t-x)*s.sin(t-y)**2*s.cos(t-x)*s.cos(t-y)/D)==0
for e in E:
 for total in range(5):
  for p in range(total+1):
   assert s.simplify(s.diff(e,a,p,b,total-p).subs({a:0,b:0}))==0
print('PASS rank-two spacetime pullback B=du wedge dv nonzero order ab')
print('PASS nonlinear H2 sigma EOM residual begins order a^3 b^2, a^2 b^3')
print('NEGATIVE not an exact full-amplitude sigma solution; action/coupling still chosen')
