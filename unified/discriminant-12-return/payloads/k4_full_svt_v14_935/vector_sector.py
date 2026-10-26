"""SVT return part 4b: VECTOR sector. Gauge F_i = 0 (no vector in g_ij).
Fields: metric shift Bv (g_0y = -a Bv), solid transverse displacement f = pi^y
(k along z; the x-polarization is identical). EH part from the validated ADM
machinery: L_EH2 = a/(4 kappa) Bv_z^2 + 3 a adot^2/(2 kappa) Bv^2 (derived in
NOTE; R3 = 0 since h = a^2 delta exactly). Matter from B^IJ directly."""
import sympy as sp
import pickle

eps, a, adot, kappa, C, eta, k = sp.symbols('eps a adot kappa C eta k', positive=True)
Bv, ft, fz = sp.symbols('Bv ft fz')

def ser(expr, n=3):
    return sp.expand(sp.series(expr, eps, 0, n).removeO())

B_, F_, Z_ = eps*Bv, eps*ft, eps*fz
# inverse metric {0,y} block: g00=1, g0y=-a B, gyy=-a^2 ; det = -a^2 (1+B^2)
detb = -a**2 * (1 + B_**2)
gi00 = ser(-a**2 / detb)
gi0y = ser(-B_ / (a * (1 + B_**2)))   # -g0y/det,  g0y = -a B
giyy = ser(1 / detb)
gixx = -1/a**2; gizz = -1/a**2
# d phi^y: (tau: ft, y: 1 [background], z: fz) -- background derivative included
Byy = ser(-(gi00*F_**2 + 2*gi0y*F_*(1 + Z_) + giyy*1 + gizz*Z_**2))
Byz = ser(-(gizz*Z_))
Bzz = -gizz; Bxx = -gixx
detB = ser(Bxx*(Byy*Bzz - Byz**2))
b_s = ser(sp.sqrt(detB))
trB = ser(2*Bxx + Byy); trB2 = ser(2*Bxx**2 + Byy**2 + 2*Byz**2)
J_s = ser(trB2/trB**2 - sp.Rational(1, 3))
sqrtg = ser(a**3 * sp.sqrt(1 + B_**2))
Lm = ser(-sqrtg * C * b_s**sp.Rational(2, 3) * (1 + eta*J_s))
Lm2 = sp.expand(Lm).coeff(eps, 2)
print("matter vector L2 ="); sp.pprint(sp.factor(Lm2))
# EH vector (Fourier: Bv_z -> -k Bv)
Le2 = a/(4*kappa) * k**2 * Bv**2 + 3*a*adot**2/(2*kappa) * Bv**2
Ltot = sp.expand(Lm2.subs({fz: -k*sp.Symbol('f'), ft: sp.Symbol('ft')})) + Le2
f = sp.Symbol('f')
Ltot = sp.expand(Lm2.subs({fz: -k*f, ft: sp.Symbol('f_t')}) ) + Le2
f_t = sp.Symbol('f_t')
dB = sp.diff(Ltot, Bv)
sol = sp.solve(dB, Bv, dict=True)[0]
print("Bv* =", sp.simplify(sol[Bv]))
Lred = sp.expand(Ltot.subs(sol))
print("reduced vector L2 ="); sp.pprint(sp.factor(Lred))
pickle.dump({'Lred_vector': str(Lred), 'Bv_star': str(sol[Bv])}, open('vector_reduced.pkl', 'wb'))
# coefficients
Kf = sp.diff(Lred, f_t, 2); Gf = -sp.diff(Lred, f, 2)
print("kinetic coeff (d2L/dft2):", sp.factor(Kf))
print("potential coeff (-d2L/df2):", sp.factor(Gf))
