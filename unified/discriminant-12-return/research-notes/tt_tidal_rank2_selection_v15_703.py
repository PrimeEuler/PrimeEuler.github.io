#!/usr/bin/env python3
"""v15.703: ordinary GR TT tidal tensor / orbital quadrupole controls.

E_ij=R_0i0j in Fermi-normal frame for a plane vacuum GW along z.
The orbital Gaunt coefficients are conventional rank-2 angular momentum,
not physical Cone quarter-spin operators. No measured G is inserted.
"""
import sympy as s
from sympy.physics.wigner import wigner_3j

A,B=s.symbols("A B",real=True)
E=s.Matrix([[A,B,0],[B,-A,0],[0,0,0]])
lam=s.symbols("lam")
assert E.trace()==0
assert s.simplify(E.det())==0
assert s.simplify(E.charpoly(lam).as_expr()-lam*(lam**2-A*A-B*B))==0
assert s.simplify(s.trace(E*E)-2*(A*A+B*B))==0
assert s.simplify(s.trace(E*E*E))==0

def gaunt(l,m,lp,mp,q):
    return s.simplify(
        (-1)**mp*s.sqrt(s.Rational((2*l+1)*5*(2*lp+1),4)/s.pi)
        *wigner_3j(lp,2,l,0,0,0)*wigner_3j(lp,2,l,-mp,q,m)
    )
assert gaunt(0,0,0,0,0)==0
assert s.simplify(gaunt(1,-1,1,1,2)+s.sqrt(30)/(10*s.sqrt(s.pi)))==0
assert s.simplify(gaunt(0,0,2,2,2)-1/(2*s.sqrt(s.pi)))==0

# A TT wave along +z has helicity/azimuthal components q=+2 and q=-2.
# Within orbital harmonics, other delta-m and odd-parity transitions
# therefore vanish at first order in the long-wavelength quadrupole term.
for l in range(5):
    for lp in range(5):
        for m in range(-l,l+1):
            for mp in range(-lp,lp+1):
                if mp-m not in (-2,2) or (l+lp)%2:
                    for q in (-2,2):
                        assert gaunt(l,m,lp,mp,q)==0

print("PASS: TT tidal eigenvalues 0,+sqrt(A²+B²),-sqrt(A²+B²)")
print("PASS: standard orbital q=±2 selection; no Cone-specific residue")
