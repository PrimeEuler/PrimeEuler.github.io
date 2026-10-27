"""Quadratic ADM action, SCALAR sector: Einstein + 3 canonical label scalars.
Signature -+++; S_m = -(C/3) sum_I (dphi^I)^2  [= handoff's +(C/3)(dphi)^2 in +---].
Background a=t/sqrt3, phi^I = x^I, kappa*C = 1 (kept symbolic C, kappa for checks;
A = a(t) symbolic with Adot = a/t, Addot = 0 substituted at the end).
Ansatz (single real mode, E=0 gauge):
  N = 1 + e Phi(t) cos kz ; N_z = -e a k B(t) sin kz
  h_ij = a^2 (1 - 2 e psi(t) cos kz) delta_ij
  phi^3 = z + e (pi(t)/k) sin kz ; phi^1 = x, phi^2 = y.
L2 = z-average of ADM EH density + matter density at O(e^2)."""
import sympy as sp

t, z, k, e, C, kap = sp.symbols('t z k e C kappa', positive=True)
a = sp.Function('a')(t)
Phi = sp.Function('Phi')(t); B = sp.Function('B')(t)
psi = sp.Function('psi')(t); pi = sp.Function('pi')(t)
ck, sk = sp.cos(k * z), sp.sin(k * z)

N = 1 + e * Phi * ck
Nz = -e * a * k * B * sk                      # shift covector (only z comp)
hf = a**2 * (1 - 2 * e * psi * ck)            # h_ij = hf * delta_ij
phi3 = z + e * pi / k * sk

def avg(expr):
    return sp.simplify(sp.integrate(expr, (z, 0, 2 * sp.pi / k)) * k / (2 * sp.pi))

# --- spatial metric geometry (3-metric hf * delta) ---
lnO = sp.log(sp.sqrt(hf))                     # h = Omega^2 delta, Omega = sqrt(hf)
dlnO = sp.diff(lnO, z)
# R3 for conformal 3-metric: R = Omega^-2 [ -4 lap(lnO) - 2 |grad lnO|^2 ]
lap = sp.diff(dlnO, z)                        # (flat delta Laplacian of lnO, only z varies)
R3 = hf**-1 * (-4 * lap - 2 * dlnO**2)
# --- extrinsic curvature ---
hdot = sp.diff(hf, t)
# D_z N_z = d_z N_z - Gamma^z_zz N_z ; Gamma^z_zz = dlnO (conformal, only comp)
DzNz = sp.diff(Nz, z) - dlnO * Nz
Kzz = (hdot - 2 * DzNz) / (2 * N)
Kxx = hdot / (2 * N)
Ktr = (2 * Kxx + Kzz) / hf                    # K = h^ij K_ij
Ksq = (2 * Kxx**2 + Kzz**2) / hf**2           # K_ij K^ij
sqrth = hf**sp.Rational(3, 2)
L_EH = N * sqrth * (R3 + Ksq - Ktr**2) / (2 * kap)
# --- matter ---
# g^tt = -1/N^2 ; g^tz = h^zz Nz / N^2 ; g^ij = delta/hf ; sqrt(-g) = N sqrth
gtz = Nz / (hf * N**2)
gtt = -1 / N**2
dtp = sp.diff(phi3, t); dzp = sp.diff(phi3, z)
kin3 = gtt * dtp**2 + 2 * gtz * dtp * dzp + dzp**2 / hf
kin1 = 1 / hf                                  # phi^1 = x: (dphi)^2 = g^xx
L_M = N * sqrth * (-C / 3) * (2 * kin1 + kin3)

def quad(expr):
    s = sp.series(sp.expand(expr), e, 0, 3).removeO()
    return sp.expand(s).coeff(e, 2)

L2 = sp.simplify(avg(quad(L_EH)) + avg(quad(L_M)))
sp.save_pickles = False
print("L2(scalar) built. Terms:", len(L2.args) if hasattr(L2, 'args') else 1)
