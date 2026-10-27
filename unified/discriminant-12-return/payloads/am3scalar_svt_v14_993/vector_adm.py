"""Quadratic ADM action, VECTOR sector: transverse shift V (along x, mode along z),
transverse label pi_T: phi^1 = x + e (pT/k) sin kz. Spatial vector gauge W=0.
N = 1 (no scalar lapse), h = a^2 delta (background only), N_x = e a V(t) cos kz."""
import sympy as sp

t, z, k, e, C, kap = sp.symbols('t z k e C kappa', positive=True)
a = sp.Function('a')(t)
V = sp.Function('V')(t); pT = sp.Function('pT')(t)
ck, sk = sp.cos(k * z), sp.sin(k * z)
N = sp.Integer(1)
Nx = e * a * V * sk                     # shift covector (sin phase: pairs with dt phi ~ sin)
hf = a**2
def avg(expr):
    return sp.simplify(sp.integrate(expr, (z, 0, 2 * sp.pi / k)) * k / (2 * sp.pi))
# h = a^2 delta: R3 = 0. K_ij: only K_xz = -(D_x N_z + D_z N_x)/(2N) + hdot terms bg.
# D_z N_x = d_z N_x (Christoffel of flat scaled metric vanish for mixed comps up to a'/a terms:
# Gamma^x_{zx} = 0 (diagonal, z-indep scale) -> D_z N_x = d_z N_x ; D_x N_z = 0 (N_z=0, Gamma^z_{xx}=0)
DzNx = sp.diff(Nx, z)
Kxz = -DzNx / 2                          # /(2N), N=1 ; K_xx etc are background (a adot delta)
adot = sp.diff(a, t)
Kbg = a * adot                           # K_ij^bg = a adot delta_ij  (K_ij = hdot_ij/2)
Ktr_bg = 3 * adot / a
# K_ij K^ij - K^2 at O(e^2): bg part subtract via expansion; perturbation: only K_xz nonzero at O(e)
Ksq_pert = 2 * (Kxz**2) / hf**2          # x,z and z,x
L_EH = N * hf**sp.Rational(3, 2) * (Ksq_pert) / (2 * kap)   # R3=0, Ktr has no O(e) part (K_xz traceless)
# BUT cross term: K^2 and Ksq contain bg x pert cross at O(e) only (Ktr_pert=0, Ksq cross needs pert in diag) -> 0. Good.
# matter: phi^1 = x + e pT/k sin kz ; g^tt=-1, g^tx = N^x/N^2 = hf^-1 Nx, g^xx = 1/hf
phi1 = sp.Symbol('x') + e * pT / k * sk
dtp = sp.diff(pT, t) * e / k * sk
dzp = e * pT * ck                          # d_z phi^1 - (bg handled: d_x phi^1 = 1)
# (dphi^1)^2 = g^tt dtp^2 + 2 g^tx dtp*dxp + g^xx dxp^2 + g^zz dzp^2 ; dxp = 1 (bg, x-dir)
gtx = Nx / hf
kin1 = -dtp**2 + 2 * gtx * dtp * 1 + 1 / hf + dzp**2 / hf
kin_other = 2 / hf                          # phi^2, phi^3 background spatial
L_M = hf**sp.Rational(3, 2) * (-C / 3) * (kin1 + kin_other)
def quad(expr):
    return sp.expand(sp.series(sp.expand(expr), e, 0, 3).removeO()).coeff(e, 2)
L2 = sp.simplify(avg(quad(L_EH)) + avg(quad(L_M)))
