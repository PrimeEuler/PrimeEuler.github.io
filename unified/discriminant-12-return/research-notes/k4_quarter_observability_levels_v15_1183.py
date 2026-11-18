#!/usr/bin/env python3
"""Gravity v15.1183: generalized step-h observable levels and q=2 boundary."""
import sympy as s
j,m,h=s.symbols('j m h',real=True)
Ap=(j-m)*(j+m+h); Am=(j+m)*(j-m+h)
y2=s.factor((Ap+Am)/2)
assert s.simplify(y2-(j*(j+h)-m*m))==0
assert s.simplify((j+h/2)**2-m*m-y2-h*h/4)==0
for L in range(1,16):
    jj=s.Rational(L,4); n=L+1
    ms=[-jj+s.Rational(i,2) for i in range(n)]
    J=s.zeros(n)
    for i,mm in enumerate(ms):
        if i+2<n: J[i+2,i]=s.sqrt((jj-mm)*(jj+mm+1))
    Y2=s.simplify((J*J.T+J.T*J)/2)
    defect=[s.simplify(jj*(jj+1)-mm*mm-Y2[i,i]) for i,mm in enumerate(ms)]
    assert all(x>=0 for x in defect)
    for i,mm in enumerate(ms):
        assert s.simplify((jj+s.Rational(1,2))**2-mm*mm-Y2[i,i]-s.Rational(1,4)-defect[i])==0
    B=s.zeros(n)
    for i,mm in enumerate(ms):
        if i+1<n: B[i+1,i]=s.sqrt((jj-mm)*(jj+mm+s.Rational(1,2)))
    Yclosed=s.simplify((B*B.T+B.T*B)/2)
    for i,mm in enumerate(ms):
        assert s.simplify((jj+s.Rational(1,4))**2-mm*mm-Yclosed[i,i]-s.Rational(1,16))==0
    if L in (1,3,5,8):
        print('L=',L,'original-step levels=',[s.Rational(1,4)+x for x in defect], 'closed-step=1/16')
print('PASS q2 L=1..15, generalized h²/4, original-step boundary defects')
print('Formal geometric C is not automatically a physical Casimir.')
