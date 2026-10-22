"""
MIC-Kepler Hamilton-Jacobi in parabolic coordinates: exact separation.

HJ (unit mass, energy E, azimuthal constant k, Poincare/monopole strength s,
Coulomb coupling kap), spherical (r, th). The MIC system includes its
defining Zwanziger term +s^2/(2r^2) in H, i.e. +s^2/r^2 in the 2E form:
    p_r^2 + [ p_th^2 + (k + s cos th)^2 / sin^2 th ] / r^2 + s^2/r^2 - 2 kap / r = 2E

Parabolic: xi = r(1+cos th), eta = r(1-cos th);  W = U(xi) + V(eta).
Claim: after multiplying by (xi+eta)/4 the equation splits EXACTLY as
    [ xi U'^2 + ((k-s)/2)^2 / xi - E xi/2 ] + [ eta V'^2 + ((k+s)/2)^2 / eta - E eta/2 ]
        = kap
i.e. each parabola carries charge (k -/+ s)/2: centre k/2, offset s/2.
Hydrogen is s = 0: both parabolas carry (k/2)^2, the standard (n1, n2) seats.
"""
import sympy as sp

xi, eta = sp.symbols('xi eta', positive=True)
k, s, E, kap = sp.symbols('k s E kap')
Up, Vp = sp.symbols('Up Vp')   # U'(xi), V'(eta) as independent symbols

r = (xi + eta) / 2
cth = (xi - eta) / (xi + eta)
sth2 = xi * eta / r**2          # sin^2 th
# p_r = (1+cth) U' + (1-cth) V' ;  p_th = sqrt(xi eta) (V' - U')
pr = (1 + cth) * Up + (1 - cth) * Vp
pth = sp.sqrt(xi * eta) * (Vp - Up)

HJ = pr**2 + (pth**2 + (k + s * cth) ** 2 / sth2) / r**2 + s**2 / r**2 - 2 * kap / r - 2 * E
HJ = sp.simplify(sp.together(HJ))
print("HJ numerator (should factor as (xi+eta) * separated):")
num = sp.factor(sp.together(HJ).as_numer_denom()[0])
print("   ", num)

mult = sp.simplify(HJ * (xi + eta) / 4)
mult = sp.expand(mult)
print("\nHJ * (xi+eta)/4 expanded:")
print("   ", mult)

# Candidate split: A(xi) + B(eta) - kap == mult ?
A = xi * Up**2 + ((k - s) / 2) ** 2 / xi - E * xi / 2
B = eta * Vp**2 + ((k + s) / 2) ** 2 / eta - E * eta / 2
resid = sp.simplify(mult - (A + B - kap))
print("\nmult - [A(xi) + B(eta) - kap] =", resid)

# hydrogen limit s=0 must give both charges (k/2)^2:
print("s=0 charges:", sp.simplify(A.subs(s, 0)), "|", sp.simplify(B.subs(s, 0)))
