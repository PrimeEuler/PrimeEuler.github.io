#!/usr/bin/env python3
"""Gravity v15.1380: symmetry-respecting quarter-H2 area-form/Maxwell
interaction. Exact algebra, explicit current, current conservation,
field redefinition and free-coefficient negative selectors.
A candidate EFT, NOT a derived physical quarter-grid force.
"""
import sympy as S
u,v,r,g,a,b,k,q,x,y=S.symbols("u v r g a b k q x y",positive=True,real=True)
T=r*S.sqrt(1+u*u+v*v)
X=r*u;Y=r*v
jac=S.Matrix([[-S.diff(T,u),S.diff(X,u),S.diff(Y,u)],
              [-S.diff(T,v),S.diff(X,v),S.diff(Y,v)]])
eta=S.diag(-1,1,1)
G=S.simplify(jac*eta*jac.T)
area=S.simplify(S.sqrt(S.factor(G.det())))
assert S.simplify(area-r*r/S.sqrt(1+u*u+v*v))==0
factor=1/S.sqrt(1+u*u+v*v)
Cu=-v/(1+S.sqrt(1+u*u+v*v))
Cv=u/(1+S.sqrt(1+u*u+v*v))
assert S.simplify(S.diff(Cv,u)-S.diff(Cu,v)-factor)==0
# Dynamic internal-map test: any independent spacetime u,v gives B=du^dv /sqrt(...).
U=a*S.sin(k*x);V=b*S.sin(q*y)
Bxy=S.simplify(factor.subs({u:U,v:V})*S.diff(U,x)*S.diff(V,y))
Jx=g*S.diff(Bxy,y);Jy=-g*S.diff(Bxy,x)
assert S.simplify(S.diff(Jx,x)+S.diff(Jy,y))==0
Jx2=-g*a*b*k*q*q*S.cos(k*x)*S.sin(q*y)
Jy2=g*a*b*k*k*q*S.sin(k*x)*S.cos(q*y)
assert S.simplify(S.diff(Jx,a).diff(b).subs({a:0,b:0})-Jx2/(a*b))==0
assert S.simplify(S.diff(Jy,a).diff(b).subs({a:0,b:0})-Jy2/(a*b))==0
# F'=F+gB; Maxwell mixing completes square, leaving g² B²/4.
FF,FB,BB=S.symbols("FF FB BB",real=True)
assert S.expand(-(FF+2*g*FB+g*g*BB)/4+g*g*BB/4-(-FF/4-g*FB/2))==0
# Target radius r cancels from the normalized target-area form.
assert not factor.has(r)
# Fixed quarter-shell factor product Q=1/16, not a dynamical mass scale.
i,L=S.symbols("i L",integer=True,nonnegative=True)
A=(2*i+1)/4;C=(2*L-2*i+1)/4
assert S.simplify(A*C-(((L+1)**2-(2*i-L)**2)/16))==0
print("PASS induced H2 area / radius² =",S.simplify(area/r**2))
print("PASS primitive dC=B; H2 has no area-flux quantization from a nontrivial 2-cycle")
print("PASS nonzero induced current, conserved divergence, 2-internal-field selection")
print("PASS free-Maxwell field redefinition; target-radius cancellation")
print("leading current Jx =",Jx2," Jy =",Jy2)
print("NEGATIVE coupling g free; not predicted by 1/4; generic EFT")
print("OPEN physical H2 carrier, state preparation, gauge-charged detector, matched-EFT null")
