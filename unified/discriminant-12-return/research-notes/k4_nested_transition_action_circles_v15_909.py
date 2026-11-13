#!/usr/bin/env python3
"""Gravity v15.909: each fixed-D Schwinger ladder station has its own positive
product-shell rest circle and tangent parabola. Geometric, not physical acceleration.
"""
import sympy as s
n,k,u,D,X=s.symbols("n k u D X",positive=True)
D0=n+k
P=n*k
T=u*D0/2
x0=u*(n-k)/2
r=u*s.sqrt(P)
assert s.simplify(T*T-x0*x0-r*r)==0
# At a given product P, shell hyperbola and rest circle in auxiliary (X,T):
shell=s.sqrt(r*r+X*X)
rest=s.sqrt(r*r-X*X)
assert s.simplify(s.diff(shell-rest,X,2).subs(X,0)-2/r)==0
# Each row y=u*k has its own factor parabola Y^2=u²*k²+2*u*k*X.
assert s.simplify((u*u*k*k+2*u*k*x0)-r*r)==0
# Fixed-sum transition n->n+1,k->k-1 changes the local action radius.
deltaP=s.expand((n+1)*(k-1)-n*k)
assert s.simplify(deltaP-(k-n-1))==0
# For fixed D, product along stations and discrete curvature vary.
for di in range(2,10):
    vals=[]
    for ki in range(di-1,-1,-1):
        ni=di-ki
        ri2=ni*ki
        if ki>0:
            vals.append((ni,ki,ri2,str(s.sqrt(ri2)),str(1/s.sqrt(ri2))))
        else:
            vals.append((ni,ki,0,"degenerate","undefined"))
    print("D=",di,vals)
# The outer circle's curvature is constant 1/T; local circle is 1/sqrt(nk).
# Their ratio varies with k, thus one outer osculating curvature != each local curvature.
assert s.simplify((T/r)-D0/(2*s.sqrt(n*k)))==0
print("PASS fixed-D conserved outer boundary, varying nk rest circle and contact parabola")
