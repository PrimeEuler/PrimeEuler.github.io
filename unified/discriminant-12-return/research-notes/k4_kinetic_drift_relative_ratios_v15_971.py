#!/usr/bin/env python3
"""Gravity v15.971: explain v15.970's apparent inner kinetic drift.
All quantities are conditional equal-M, equal-length thin-ring
comparisons of EM C and *formal* q2 Casimir labels, not physics.
"""
import sympy as s
D=s.symbols("D",positive=True)
Ce=(D**2-1)/4
Cq=(2*D-1)*(2*D+3)/16
radii={
 'outer':(D**2/4,D**2/4),
 'casimir':((D**2-1)/4,(D**2-s.Rational(1,4))/4),
 'inner':(D-1,D/2-s.Rational(1,4)),
}
expected={
 'outer':((D**2-1)/D**2,(2*D-1)*(2*D+3)/(4*D**2),
          (4*D+1)/(4*D**2),s.Integer(1)),
 'casimir':(s.Integer(1),(2*D+3)/(2*D+1),
            2/(2*D+1),s.Integer(1)),
 'inner':((D+1)/4,(2*D+3)/4,(D+2)/4,s.Integer(2))
}
for label,(re,rg) in radii.items():
    e=s.factor(Ce/re)
    g=s.factor(Cq/rg)
    ed,gd,gap,limit=expected[label]
    assert s.simplify(e-ed)==0
    assert s.simplify(g-gd)==0
    assert s.simplify(g-e-gap)==0
    assert s.limit(g/e,D,s.oo)==limit
    print(label, "EM",e,"quarter formal",g,
          "gap",s.factor(g-e),"ratio",s.factor(g/e),
          "asymptotic ratio",limit)
print("PASS: exact differences and normalized relative drift")
