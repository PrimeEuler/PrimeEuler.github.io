#!/usr/bin/env python3
"""Gravity v15.1176 — EM Jxy offset from quarter-midpoint geometry versus
formal q=2 geometric shell Casimir and closed refined-step SU2 Casimir.
This is a correction of interpretation, NOT a new physical spin operator.
Parents: v15.952, v15.955, v15.602, v15.626, v15.630, v15.1174-75.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
k=s.symbols('k',integer=True,nonnegative=True)
f=lambda x:x*(D-x)
Cem=(D**2-1)/4
L=2*D-1
Cq=s.factor(L*(L+4)/16)
Cclosed=s.factor(L*(L+2)/4)
assert s.simplify(f(k+s.Rational(1,2))-(f(k)+f(k+1))/2-s.Rational(1,4))==0
assert s.simplify(Cq-Cem-(D/s.Integer(4)+s.Rational(1,16)))==0
assert s.simplify(Cclosed-Cq-L*(3*L+4)/16)==0
for d in range(2,14):
    j=s.Rational(d-1,2)
    for ki in range(d):
        m=j-ki
        xy=s.simplify((f(ki)+f(ki+1))/2).subs(D,d)
        assert xy==j*(j+1)-m*m
        assert s.simplify(f(ki+s.Rational(1,2)).subs(D,d)-xy)==s.Rational(1,4)
    assert s.simplify((Cq-Cem).subs(D,d))>0
print('PASS D=2..13: EM state-center/Jxy diagonal and two distinct Casimir spectra')
print('C quarter - C EM:',s.factor(Cq-Cem))
print('C closed - C quarter:',s.factor(Cclosed-Cq))
for d in [2,3,5]:
    print('D=',d,'CEM=',Cem.subs(D,d),'Cquarter=',Cq.subs(D,d),
          'Cclosed=',Cclosed.subs(D,d))
