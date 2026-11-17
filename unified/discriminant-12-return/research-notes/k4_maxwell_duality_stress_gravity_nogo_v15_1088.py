#!/usr/bin/env python3
"""Gravity v15.1088: vacuum EM duality swaps T/X invariant labels but preserves
the full stress-energy tensor, Maxwell evolution and identical K4 ADM sources.
No magnetic monopoles or external electric charges assumed.
"""
import sympy as s

ex,ey,ez,bx,by,bz=s.symbols('ex ey ez bx by bz',real=True)
C,S=s.symbols('C S',real=True)
E=s.Matrix([ex,ey,ez]); B=s.Matrix([bx,by,bz])
Enew=C*E+S*B
Bnew=C*B-S*E

def stress(E,B):
    rho=(E.dot(E)+B.dot(B))/2
    spatial=s.eye(3)*rho-E*E.T-B*B.T
    flux=E.cross(B)
    return rho,spatial,flux

rho,T,flux=stress(E,B)
rhon,Tn,fluxn=stress(Enew,Bnew)
assert s.simplify(rhon-rho-(C*C+S*S-1)*rho)==0
assert (Tn-T-(C*C+S*S-1)*T).applyfunc(s.simplify)==s.zeros(3)
assert (fluxn-flux-(C*C+S*S-1)*flux).applyfunc(s.simplify)==s.zeros(3,1)

for cos,sin in [(0,1),(s.sqrt(2)/2,s.sqrt(2)/2),(s.Rational(3,5),s.Rational(4,5))]:
    sub={C:cos,S:sin}
    assert s.simplify((rhon-rho).subs(sub))==0
    assert (Tn-T).subs(sub).applyfunc(s.simplify)==s.zeros(3)
    assert (fluxn-flux).subs(sub).applyfunc(s.simplify)==s.zeros(3,1)

I1=E.dot(E)-B.dot(B)
I2=E.dot(B)
I1new=s.expand(Enew.dot(Enew)-Bnew.dot(Bnew))
I2new=s.expand(Enew.dot(Bnew))
assert s.simplify(I1new-((C*C-S*S)*I1+4*C*S*I2))==0
assert s.simplify(I2new-((C*C-S*S)*I2-C*S*I1))==0

# For a nonzero electric field only, a 45 degree dual rotation gives
# I1=0 but I2 != 0, so the putative 'hinge' is NOT a null Maxwell field.
e=s.symbols('e',real=True,nonzero=True)
initial={ex:e,ey:0,ez:0,bx:0,by:0,bz:0}
assert I1.subs(initial)==e*e
assert I1new.subs(initial).subs({C:s.sqrt(2)/2,S:s.sqrt(2)/2})==0
assert s.simplify(I2new.subs(initial).subs({C:s.sqrt(2)/2,S:s.sqrt(2)/2})+e*e/2)==0
assert I1new.subs(initial).subs({C:0,S:1})==-e*e
assert s.simplify((Tn[0,0]-Tn[1,1]-(T[0,0]-T[1,1])).subs({C:0,S:1}))==0

print("PASS: EM duality preserves energy, momentum and all stresses under sample rotations")
print("PASS: invariant-sign T/X sectors exchange with identical gravitational Maxwell source")
print("PASS: I1=0 alone is not null radiation; need I1=0 AND I2=0")
