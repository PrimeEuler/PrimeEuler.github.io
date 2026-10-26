"""SVT return part 3b: EH quadratic action, scalar sector, via validated ADM.
R3 = -2 A''/(AB) + A'B'/(AB^2) + A'^2/(2A^2 B) for h=diag(A,A,B)(z) [derived from
Christoffels; limits: conformal, warped, pure-gauge all exact]; density
N sqrt(h) [R3 + Kij K^ij - K^2] / (2 kappa); validated: background -3 a adot^2/kappa,
TT kinetic a^3 tr(gammadot^2)/(8 kappa), TT gradient in Fourier average."""
import sympy as sp
import pickle

eps, a, adot, kappa = sp.symbols('eps a adot kappa', positive=True)
Phi, Bz, Bzz, psi, Ezz = sp.symbols('Phi Bz Bzz psi Ezz')
psi_t, psi_z, psi_zz = sp.symbols('psi_t psi_z psi_zz')
E_zzt, E_zzz, E_zzzz = sp.symbols('E_zzt E_zzz E_zzzz')

def ser(expr, n=3):
    return sp.expand(sp.series(expr, eps, 0, n).removeO())

Ph, B, ps, Ez = eps*Phi, eps*Bz, eps*psi, eps*Ezz
Bzz_s = eps*Bzz
hA = a**2*(1 - 2*ps)
hB = a**2*(1 - 2*ps - 2*Ez)
hA_t = 2*a*adot*(1 - 2*ps) - 2*a**2*eps*psi_t
hB_t = 2*a*adot*(1 - 2*ps - 2*Ez) - 2*a**2*(eps*psi_t + eps*E_zzt)
hA_z = -2*a**2*eps*psi_z
hB_z = a**2*(-2*eps*psi_z - 2*eps*E_zzz)
hA_zz = -2*a**2*eps*psi_zz
hB_zz = a**2*(-2*eps*psi_zz - 2*eps*E_zzzz)
Nz_cov = a*B
Nz_z = a*Bzz_s
N = ser(sp.sqrt(1 + 2*Ph + a**2 * B**2 / hB))
sqrth = ser(sp.sqrt(hA*hA*hB))
R3 = ser(-2*hA_zz/(hA*hB) + hA_z*hB_z/(hA*hB**2) + hA_z**2/(2*hA**2*hB))
DxNx = (hA_z/(2*hB))*Nz_cov
DzNz = Nz_z - (hB_z/(2*hB))*Nz_cov
KA = ser((hA_t - 2*DxNx)/(2*N))
KB = ser((hB_t - 2*DzNz)/(2*N))
Ktr = ser(2*KA/hA + KB/hB)
KK = ser(2*(KA/hA)**2 + (KB/hB)**2)
dens = ser(N*sqrth*(R3 + KK - Ktr**2))
L2 = sp.expand(dens).coeff(eps, 2)/(2*kappa)
L1 = sp.expand(dens).coeff(eps, 1)/(2*kappa)
print("EH L1 (should be constraint combo, nonzero):"); sp.pprint(sp.factor(L1))
pickle.dump({'L2': str(L2)}, open('eh_scalar.pkl', 'wb'))
print("EH scalar L2 saved;", len(str(L2)), "chars")
# sanity: no Phi_t / B_t symbols exist by construction; check L2 has no E_zzt^2 (E is gauge)
print("E_zzt^2 coeff:", L2.coeff(E_zzt, 2), "| psi_t^2 coeff:", sp.simplify(L2.coeff(psi_t, 2)))
