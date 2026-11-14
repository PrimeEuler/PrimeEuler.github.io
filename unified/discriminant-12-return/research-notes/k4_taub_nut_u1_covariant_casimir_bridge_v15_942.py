#!/usr/bin/env python3
"""Gravity v15.942: Taub-NUT fiber/U(1) monopole angular spectrum
vs the geometric quarter Casimir; exact physical SU2/refined-step
match and no affine full-spectrum identification. No field coupling
or new spacetime connection is constructed here.
"""
import sympy as s

k, r = s.symbols("k r", integer=True, nonnegative=True)
a, b = s.symbols("a b")
charge = k / 2
j_phys = charge + r
L = k + 2*r
C_phys = s.factor(j_phys*(j_phys+1))
C_covlap = s.factor(C_phys-charge**2)
C_geom = s.factor(L*(L+4)/16)
C_refined = s.factor(L*(L+2)/4)
assert s.simplify(C_phys-C_refined) == 0
assert s.simplify(C_phys-C_geom-L*(3*L+4)/16) == 0
assert s.simplify(C_phys-4*C_geom+L/2) == 0
assert s.simplify(C_covlap-(charge*(2*r+1)+r*(r+1))) == 0
assert s.simplify((2*j_phys+1)-(L+1)) == 0

# A fixed affine Casimir recalibration cannot fit three or more levels.
fit = s.solve([C_phys.subs(r,rr)-a*C_geom.subs(r,rr)-b
               for rr in (0,1)], (a,b), dict=True)[0]
assert s.simplify(fit[a]-4*(k+2)/(k+3)) == 0
assert s.simplify(fit[b]+k*(k+2)/(4*(k+3))) == 0
residual = s.factor((C_phys-a*C_geom-b).subs(fit))
assert s.simplify(residual-r*(r-1)/(k+3)) == 0
assert s.simplify(residual.subs(r,2)-2/(k+3)) == 0
for kk in range(1,9):
    for rr in range(0,6):
        LL = kk+2*rr
        J = s.Rational(LL,2)
        assert s.simplify((C_phys-C_geom).subs({k:kk,r:rr})-
                          s.Rational(LL*(3*LL+4),16)) == 0
        assert 2*J+1 == LL+1
        if rr>=2:
            assert residual.subs({k:kk,r:rr}) > 0
    print("k",kk,"three-level affine residual",residual.subs({k:kk,r:2}))
# The physical angular generators are full ordinary SU2; the
# original unit-step projected quarter operators are defective.
for LL in (1,3,5,7):
    jq = s.Rational(LL,4)
    Mq = s.diag(*[-jq+s.Rational(i,2) for i in range(LL+1)])
    Jq = s.zeros(LL+1)
    for i in range(LL-1):
        Jq[i+2,i] = s.sqrt(s.Rational((LL-i)*(i+2),4))
    D = s.simplify(jq*(jq+1)*s.eye(LL+1)-
                  Mq**2-(Jq*Jq.T+Jq.T*Jq)/2)
    assert D.rank()==2
    assert Jq*Jq.T-Jq.T*Jq != 2*Mq
    Jp = s.zeros(LL+1)
    for i in range(LL):
        Jp[i+1,i]=s.sqrt((LL-i)*(i+1))
    Mphys=s.diag(*[-s.Rational(LL,2)+i for i in range(LL+1)])
    assert Jp*Jp.T-Jp.T*Jp == 2*Mphys
print("PASS: winding k=1..8, levels r=0..5; no affine bridge;")
print("full SU2 monopole multiplets vs defective quarter ladders")
