"""Scalar quadratic ADM action, BUILD 2: machine Christoffels for the 3-metric
(no hand R3/K formulas). Same ansatz/gauge as build 1 (scalar_adm.py).
Returns L2b for exact comparison with build 1."""
import sympy as sp

t, z, k, e, C, kap = sp.symbols('t z k e C kappa', positive=True)
a = sp.Function('a')(t)
Phi = sp.Function('Phi')(t); B = sp.Function('B')(t)
psi = sp.Function('psi')(t); pi = sp.Function('pi')(t)
ck, sk = sp.cos(k * z), sp.sin(k * z)
N = 1 + e * Phi * ck
Nz = -e * a * k * B * sk
hf = a**2 * (1 - 2 * e * psi * ck)
phi3 = z + e * pi / k * sk
x, y = sp.symbols('x y')
cs = [x, y, z]
hmat = sp.diag(hf, hf, hf); hinv = hmat.inv()
dh = [[[sp.diff(hmat[mu, s], cs[r]) for s in range(3)] for mu in range(3)] for r in range(3)]
G3 = [[[sum(hinv[u, s] * (dh[mu][s][nu] + dh[nu][s][mu] - dh[s][mu][nu]) / 2 for s in range(3))
        for nu in range(3)] for mu in range(3)] for u in range(3)]
R3 = 0
for i in range(3):
    rij = 0
    for l in range(3):
        rij += sp.diff(G3[l][i][i], cs[l]) - sp.diff(G3[l][i][l], cs[i])
        for mm in range(3):
            rij += G3[l][l][mm] * G3[mm][i][i] - G3[l][i][mm] * G3[mm][i][l]
    R3 += hinv[i, i] * rij
# extrinsic curvature: K_ij = (dh_ij/dt - D_i N_j - D_j N_i)/(2N); N_i = (0,0,Nz)
Nv = [0, 0, Nz]
DN = [[sp.diff(Nv[j], cs[i]) - sum(G3[m][i][j] * Nv[m] for m in range(3)) for j in range(3)] for i in range(3)]
hd = sp.diff(hf, t)
K = [[( (hd if i == j else 0) - DN[i][j] - DN[j][i]) / (2 * N) for j in range(3)] for i in range(3)]
Ktr = sum(hinv[i, j] * K[i][j] for i in range(3) for j in range(3))
Ksq = sum(hinv[i, m] * hinv[j, n] * K[i][j] * K[m][n] for i in range(3) for j in range(3) for m in range(3) for n in range(3))
sqrth = hf**sp.Rational(3, 2)
L_EH = N * sqrth * (R3 + Ksq - Ktr**2) / (2 * kap)
gtz = Nz / (hf * N**2); gtt = -1 / N**2
dtp = sp.diff(phi3, t); dzp = sp.diff(phi3, z)
kin3 = gtt * dtp**2 + 2 * gtz * dtp * dzp + (1 / hf - (Nz / hf)**2 / N**2) * dzp**2
L_M = N * sqrth * (-C / 3) * (2 / hf + kin3)
def avg(expr):
    return sp.simplify(sp.integrate(expr, (z, 0, 2 * sp.pi / k)) * k / (2 * sp.pi))
def quad(expr):
    return sp.expand(sp.series(sp.expand(expr), e, 0, 3).removeO()).coeff(e, 2)
L2b = sp.simplify(avg(quad(L_EH)) + avg(quad(L_M)))
print("BUILD2 L2 built")
print("BUILD2 L2 ready")
