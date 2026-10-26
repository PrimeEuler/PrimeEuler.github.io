"""SVT return part 2: EXACT quadratic expansion of the SOLID action (scalar sector).
S_m = -int sqrt(-g) C b^(2/3) (1 + eta J),  B^IJ = -g^mn d_m phi^I d_n phi^J,
J = tr(B^2)/(tr B)^2 - 1/3.  Metric (scalar, k along z, real space):
g00 = 1+2Phi, g0z = -a B_z, gzz = -a^2[(1-2psi) - 2 E_zz], gxx = gyy = -a^2(1-2psi).
Solid: phi^z = z + P_z (P = pi_L); V^z = P_zt; F_z^z = 1 + P_zz.
Perturbations are eps-scaled ONCE at construction; ser() only expands."""
import sympy as sp
import pickle

eps, a, C, eta = sp.symbols('eps a C eta', positive=True)
Phi, Bz, psi, Ezz, Pzz, Pzt = sp.symbols('Phi Bz psi Ezz Pzz Pzt')

def ser(expr, n=3):
    return sp.expand(sp.series(expr, eps, 0, n).removeO())

# scaled fields
Ph, B, ps, Ez, Pz, Pt = eps*Phi, eps*Bz, eps*psi, eps*Ezz, eps*Pzz, eps*Pzt
g00 = 1 + 2*Ph
g03 = -a*B
g33 = -a**2*((1 - 2*ps) - 2*Ez)
g11 = -a**2*(1 - 2*ps)
det_block = g00*g33 - g03**2
detg = det_block * g11**2
sqrtg = ser(sp.sqrt(-detg))
gi00 = ser(g33/det_block); gi03 = ser(-g03/det_block)
gi33 = ser(g00/det_block); gi11 = ser(1/g11)

V, F = Pt, 1 + Pz
Bzz = ser(-(gi00*V**2 + 2*gi03*V*F + gi33*F**2))
Bxx = ser(-gi11)
Bmat = sp.diag(Bxx, Bxx, Bzz)
b_s = ser(sp.sqrt(sp.expand(Bmat.det())))
trB = ser(Bmat.trace()); trB2 = ser((Bmat**2).trace())
J_s = ser(trB2/trB**2 - sp.Rational(1, 3))
print("J eps^0:", sp.expand(J_s).coeff(eps, 0), "| J eps^1:", sp.expand(J_s).coeff(eps, 1))

L = ser(-sqrtg * C * b_s**sp.Rational(2, 3) * (1 + eta*J_s))
L0 = sp.expand(L).coeff(eps, 0); L1 = sp.expand(L).coeff(eps, 1); L2 = sp.expand(L).coeff(eps, 2)
print("L0 =", L0)
assert sp.simplify(L0 + a*C) == 0
print("L1 =", sp.factor(L1))
# hand-check: L1 should be -a*C*(Phi - psi - Ezz/3 + (2/3) Pzz)
hand = -a*C*(Phi - psi - Ezz/3 + sp.Rational(2, 3)*Pzz)
assert sp.simplify(L1 - hand) == 0, sp.simplify(L1 - hand)
print("L1 matches hand derivation -aC(Phi - psi - Ezz/3 + 2Pzz/3): CONFIRMED")
pickle.dump({'L1': str(L1), 'L2': str(L2), 'J2': str(sp.expand(J_s).coeff(eps, 2))},
            open('matter_scalar.pkl', 'wb'))
print("L2 ="); sp.pprint(L2)
