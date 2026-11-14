#!/usr/bin/env python3
"""Cone v15.970: shared-D EM/formal-quarter Casimir kinetic comparison.
Three mechanically plausible inertia radii give inequivalent energy
splittings. No new physical gravity Casimir or kinetic action is sourced.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
Ce=s.factor((D**2-1)/s.Integer(4))
L=2*D-1
Cq=s.factor(L*(L+4)/s.Integer(16))
assert s.simplify(Cq-Ce-(4*D+1)/s.Integer(16))==0
radii={
 'outer':(D**2/s.Integer(4),D**2/s.Integer(4)),
 'casimir':((D**2-1)/s.Integer(4),(D**2-s.Rational(1,4))/s.Integer(4)),
 'inner':(D-1,D/s.Integer(2)-s.Rational(1,4)),
}
expected={
 'outer':(4*D+1)/(4*D**2),
 'casimir':2/(2*D+1),
 'inner':(D+2)/4,
}
for key,(re,rg) in radii.items():
    gap=s.factor(Cq/rg-Ce/re)
    assert s.simplify(gap-expected[key])==0
    print(key,gap)
    for d in range(2,1001):
        assert gap.subs(D,d)>0
M,ell,hbar,Me,Mg=s.symbols('M ell hbar M_e M_g',positive=True)
r2=radii['outer'][0]
Ee=hbar**2*Ce/(2*Me*ell**2*r2)
Eg=hbar**2*Cq/(2*Mg*ell**2*r2)
Mc=s.factor(s.solve(s.Eq(Eg,Ee),Mg)[0])
assert s.simplify(Mc/Me-Cq/Ce)==0
assert s.simplify((Eg-Ee).subs(Mg,Mc))==0
lamb=s.symbols('lambda',positive=True)
for re,rg in radii.values():
    gap=hbar**2*(Cq/rg-Ce/re)/(2*M*ell**2)
    assert s.simplify(gap.subs(ell,lamb*ell)-gap/lamb**2)==0
I=s.symbols('I',positive=True)
p=s.symbols('p',real=True)
assert s.simplify(p*(p/I)-I*(p/I)**2/2-p**2/(2*I))==0
print('Canceling positive inertia/mass ratio',Mc/Me)
print('PASS: D=2..1000; three exact kinetic profiles; adjustable mass; action scale no-go')
