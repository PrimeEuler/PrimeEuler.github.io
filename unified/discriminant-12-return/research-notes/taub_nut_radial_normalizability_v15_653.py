#!/usr/bin/env python3
"""Exact Jante–Schroers JHEP01(2014)114 eqs (3.38)-(3.45), v15.653."""
import sympy as s
rho,j,p=s.symbols('rho j p', positive=True)
d=p-2*j-1
R=rho**j/s.sqrt(rho+1)*s.exp(-d*rho/2)
ODE=s.diff(R,rho)+((p-1)/2-j+(s.Rational(1,2)-j)/rho-s.Rational(1,2)/(rho*(rho+1)))*R
assert s.simplify(ODE/R)==0
weight=rho*(rho+1)
assert s.simplify(weight*R**2-rho**(2*j+1)*s.exp(-d*rho))==0
# For n=2j+1 the radial norm integral is Gamma(n+1)/(p-n)**(n+1), when p>n.
for n in range(1,11):
    jj=s.Rational(n-1,2)
    assert s.simplify(d.subs(j,jj)-(p-n))==0
    for aux in (s.Rational(n+1,2),s.Integer(n),s.Rational(2*n+1,2),s.Integer(n+2)):
        if aux>n:
            assert s.factorial(n)/(aux-n)**(n+1)>0
        else:assert aux-n<=0
# Paper uses strict integer cut-off: at p an integer the top n=p mode is NOT allowed.
for aux,top in [(s.Rational(1,2),0),(s.Integer(1),0),(s.Rational(3,2),1),(s.Integer(2),1),(s.Rational(5,2),2),(s.Integer(3),2),(s.Rational(7,2),3)]:
    ns=[n for n in range(1,20) if n<aux]
    assert sum(ns)==top*(top+1)//2
for k in range(10):
    assert s.simplify(d.subs(j,s.Rational(k,2))-(p-k-1))==0
    assert s.simplify(d.subs(j,s.Rational(k+1,2))-(p-k-2))==0
# Radial shape overlaps, not 4D transition matrix elements (angular factors orthogonal).
P=s.symbols('P',positive=True)
d1=P-1; d2=P-2
overlap=s.gamma(s.Rational(5,2))*s.sqrt(d1**2*d2**3/s.Integer(2))/((d1+d2)/2)**s.Rational(5,2)
assert s.simplify(overlap.subs(P,3)-2*s.sqrt(3*s.pi)/9)==0
assert s.simplify(overlap.subs(P,4)-18*s.sqrt(10*s.pi)/125)==0
print("PASS: TN radial ODE, weighted norm, strict normalizability, n-sector census, p-dependent radial overlap")
