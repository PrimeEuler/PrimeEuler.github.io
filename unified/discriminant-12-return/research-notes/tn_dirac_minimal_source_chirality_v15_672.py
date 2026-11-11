#!/usr/bin/env python3
"""Exact Taub-NUT zero-mode source-selection gate v15.672.
The bounded Fourier scalar comparator is a CHOSEN perturbation, not sourced gravity.
"""
import sympy as s
I=s.I
sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1); Z=s.zeros(2); unit=s.eye(2)
def block(A,B,C,D):return A.row_join(B).col_join(C.row_join(D))
gam=[block(Z,-I*t,I*t,Z) for t in (sx,sy,sz)]+[block(Z,unit,unit,Z)]
chir=s.diag(1,1,-1,-1); Pplus=(s.eye(4)+chir)/2
for a in gam:
    assert chir*a+a*chir==s.zeros(4)
    assert Pplus*a*Pplus==s.zeros(4) # minimal gauge perturbation
rho=s.symbols('rho',positive=True)
h=s.sqrt(rho)*s.exp(-rho/2)
assert s.simplify(s.diff(h,rho)/h-(1-rho)/(2*rho))==0
assert s.simplify(h.subs(rho,1)-s.exp(-s.Rational(1,2)))==0
p=s.Rational(7,2)
# Radial norm I_n = Gamma(n+1)/(p-n)^(n+1), angular normalized z1 raising=sqrt((a+1)/(n+1)).
basis=[(n,a) for n in (1,2,3) for a in range(n)]
idx={b:i for i,b in enumerate(basis)}
T=s.zeros(6); N=s.diag(*[n for n,a in basis])
for col,(n,a) in enumerate(basis):
    if n+1<p:
        delta=p-n
        In=s.factorial(n)/delta**(n+1)
        Inext=s.factorial(n+1)/(delta-1)**(n+2)
        # R_n R_(n+1) * h * rho(1+rho) = rho^(n+1)*exp[-(p-n)rho]
        radial=s.factorial(n+1)/delta**(n+2)/s.sqrt(In*Inext)
        angle=s.sqrt(s.Rational(a+1,n+1))
        coeff=s.sqrt(a+1)*(delta-1)**s.Rational(n+2,2)/delta**s.Rational(n+3,2)
        assert s.simplify(radial*angle-coeff)==0
        T[idx[n+1,a+1],col]=s.simplify(coeff)
assert T[idx[2,1],idx[1,0]]==3*s.sqrt(6)/25
assert N*T-T*N==T
assert (T+T.T).T==T+T.T
assert N*(T+T.T)-(T+T.T)*N!=s.zeros(6)
assert T!=s.zeros(6)
print("PASS v15.672: chiral gauge-vector selection zero; bounded Fourier comparator nonzero with p-dependent coefficients")
