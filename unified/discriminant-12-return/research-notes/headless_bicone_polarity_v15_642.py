#!/usr/bin/env python3
"""v15.642 exact headless-polarity Z2 quotient and physical rotor equivalence."""
import sympy as s
from itertools import product
t1,t2,alpha=s.symbols("t1 t2 alpha",real=True)
u=lambda x,y:s.cos(x-y)-3*s.cos(x-alpha)*s.cos(y-alpha)
for p1,p2 in product((-1,1),repeat=2):
    sh=lambda p:s.pi*(1-p)/2
    assert s.trigsimp(u(t1+sh(p1),t2+sh(p2))-p1*p2*u(t1,t2))==0
    assert s.trigsimp(-p1*p2*u(t1+s.pi,t2)-p1*p2*u(t1,t2))==0
    assert s.trigsimp(-p1*p2*u(t1,t2+s.pi)-p1*p2*u(t1,t2))==0

# Finite cover of theta (integer Fourier m), polarity p and deck T.
modes=list(range(-3,4)); cover=[(m,p) for m in modes for p in (1,-1)]
index={mp:i for i,mp in enumerate(cover)}
T=s.zeros(len(cover)); O=s.zeros(len(cover)); bare=s.zeros(len(cover)); N=s.zeros(len(cover))
for col,(m,p) in enumerate(cover):
    T[index[(m,-p)],col]=s.Integer(-1)**m
    N[col,col]=m
    for dm in (-1,1):
        dest=(m+dm,p)
        if dest in index:
            O[index[dest],col]+=s.Rational(p,2)
            bare[index[dest],col]+=s.Rational(1,2)
assert T*T==s.eye(len(cover))
assert T*O==O*T and T*N==N*T
assert T*bare!=bare*T

# Isometry from the physical directed-rotor Hilbert space onto T=+1.
V=s.zeros(len(cover),len(modes)); cosbeta=s.zeros(len(modes))
for col,m in enumerate(modes):
    V[index[(m,1)],col]=s.sqrt(2)/2
    V[index[(m,-1)],col]=s.sqrt(2)*s.Integer(-1)**m/2
    for dm in (-1,1):
        if m+dm in modes:cosbeta[modes.index(m+dm),col]+=s.Rational(1,2)
assert V.T*V==s.eye(len(modes)) and T*V==V
assert V.T*O*V==cosbeta
Pi=s.diag(*[s.Integer(-1)**m for m in modes])
assert Pi*cosbeta==-cosbeta*Pi
assert s.kronecker_product(Pi,Pi)*s.kronecker_product(cosbeta,cosbeta)==s.kronecker_product(cosbeta,cosbeta)*s.kronecker_product(Pi,Pi)
print("PASS: local polarity redundancy, physical rotor quotient, Fourier projection and two-body reversal symmetry.")
