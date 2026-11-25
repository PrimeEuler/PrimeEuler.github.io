#!/usr/bin/env python3
"""v15.1410: controlled fifth-order nonlinear crossed H2 sigma correction.
A=t-x,B=t-y. EOM corrected order seven. The normalized spacetime
area is nonzero with corrections first order four (metric), order six
(dynamic). Separate prescribed physical Weyl packet / full EFT open.
"""
import sympy as s
import numpy as np
A,B,a,b=s.symbols("A B a b",real=True)
u=a*s.sin(A);v=b*s.sin(B)
du=-a**3*b**2*s.sin(A)**3*s.sin(B)**2/s.Integer(6)
dv=-a**2*b**3*s.sin(A)**2*s.sin(B)**3/s.Integer(6)
box=lambda f:-2*s.diff(f,A,B)
assert s.simplify(box(du)-2*a**3*b**2*s.sin(A)**2*s.sin(B)*s.cos(A)*s.cos(B))==0
assert s.simplify(box(dv)-2*a**2*b**3*s.sin(A)*s.sin(B)**2*s.cos(A)*s.cos(B))==0
def residual(U,V):
 D=1+U*U+V*V
 G=s.eye(2)-s.Matrix([U,V])*s.Matrix([[U,V]])/D
 dot=lambda p,q:-(s.diff(p,A)*s.diff(q,B)+s.diff(p,B)*s.diff(q,A))
 kin=sum(G[i,j]*dot(F[i],F[j]) for i in range(2) for j in range(2) for F in [[U,V]])
 return [s.factor(box(F)-F*kin) for F in (U,V)]
orig=residual(u,v);corr=residual(u+du,v+dv)
for i in range(2):
 leading=s.factor(orig[i]*(1+u*u+v*v))
 expect=(-2*a**3*b**2*s.sin(A)**2*s.sin(B)*s.cos(A)*s.cos(B) if i==0 else
         -2*a**2*b**3*s.sin(A)*s.sin(B)**2*s.cos(A)*s.cos(B))
 assert s.simplify(leading-expect)==0
for f in corr:
 for n in range(7):
  for p in range(n+1):
   assert s.simplify(s.diff(f,a,p,b,n-p).subs({a:0,b:0}))==0
raw=s.factor(s.diff(u+du,A)*s.diff(v+dv,B)-s.diff(u+du,B)*s.diff(v+dv,A))
raw0=s.diff(u,A)*s.diff(v,B)
assert s.simplify(s.expand(raw-raw0).coeff(a,3).coeff(b,3)+s.sin(A)**2*s.sin(B)**2*s.cos(A)*s.cos(B))==0
# Physical normalized target area: real pullback C(A,B) dA^dB
area=raw/s.sqrt(1+(u+du)**2+(v+dv)**2)
lead=raw0
assert s.simplify(s.diff(area,a,b).subs({a:0,b:0})-s.cos(A)*s.cos(B))==0
functions=[s.lambdify((A,B,a,b),f,'numpy',cse=True) for f in orig+corr+[area,lead]]
last=None
for amp in (.25,.125,.0625):
 vals=[float(fn(.53,.76,amp,amp)) for fn in functions]
 origmax=max(abs(i) for i in vals[:2]);corrmax=max(abs(i) for i in vals[2:4])
 print(dict(amplitude=amp,uncorrected_residual=origmax,corrected_residual=corrmax,
       ratio=corrmax/origmax,normalized_area=vals[4],leading_area=vals[5],
       area_relative_deviation=(vals[4]-vals[5])/vals[5]),flush=True)
 if last:assert abs((corrmax/origmax)/last-.25)<.02
 last=corrmax/origmax
print("PASS corrected nonlinear sigma EOM residual begins order seven")
print("PASS area source nonzero; normalized area first corrected at order four, dynamic corrections order six")
print("OPEN homogeneous Cauchy data choice, tensor contracted Weyl J and full coupled gravity")
