"""Tensor sector: TT mode gamma (h_xx = a^2(1+e g ck), h_yy = a^2(1-e g ck), h_zz = a^2),
N=1, no shift. ADM quadratic action -> oscillator; verify v14.991 m_T^2 = 4H^2."""
import sympy as sp
t, z, k, e, C, kap = sp.symbols('t z k e C kappa', positive=True)
a = sp.Function('a')(t)
g_ = sp.Function('g')(t)
ck, sk = sp.cos(k * z), sp.sin(k * z)
h = [a**2 * (1 + e * g_ * ck), a**2 * (1 - e * g_ * ck), a**2]
def avg(expr):
    return sp.simplify(sp.integrate(expr, (z, 0, 2 * sp.pi / k)) * k / (2 * sp.pi))
# R3 for diag h_i(z): machine Christoffel/Ricci of the 3-metric (coords x,y,z; only z varies)
hmat = sp.diag(h[0], h[1], h[2]); hinv = hmat.inv()
cs = [sp.Symbol('x'), sp.Symbol('y'), z]
dh = [[[sp.diff(hmat[m, s], cs[r]) for s in range(3)] for m in range(3)] for r in range(3)]
G3 = [[[sum(hinv[u, s] * (dh[mu][s][nu] + dh[nu][s][mu] - dh[s][mu][nu]) / 2 for s in range(3))
        for nu in range(3)] for mu in range(3)] for u in range(3)]
R3 = 0
for i in range(3):
    rij = 0
    for l in range(3):
        rij += sp.diff(G3[l][i][i], cs[l]) - sp.diff(G3[l][i][l], cs[i])
        for m in range(3):
            rij += G3[l][l][m] * G3[m][i][i] - G3[l][i][m] * G3[m][i][l]
    R3 += rij / h[i]
K = [sp.diff(h[i], t) / 2 for i in range(3)]          # K_ij (N=1, no shift), components diag
Ktr = sum(K[i] / h[i] for i in range(3))
Ksq = sum((K[i] / h[i])**2 for i in range(3))
sqrth = sp.sqrt(h[0] * h[1] * h[2])
L_EH = sqrth * (R3 + Ksq - Ktr**2) / (2 * kap)
# matter: (dphi^I)^2 summed = sum_i 1/h_i (background labels); sqrt(-g) = sqrth
L_M = sqrth * (-C / 3) * sum(1 / h[i] for i in range(3))
def quad(expr):
    return sp.expand(sp.series(sp.expand(expr), e, 0, 3).removeO()).coeff(e, 2)
L2 = sp.simplify(avg(quad(L_EH)) + avg(quad(L_M)))
L2 = L2.subs(sp.Derivative(a, t), 1 / sp.sqrt(3)).subs(a, t / sp.sqrt(3))
L2 = sp.expand(L2.subs({C: 1, kap: 1}))
dd = lambda f: sp.Derivative(f, t)
A = sp.simplify(L2.coeff(dd(g_)**2))
ELg = sp.expand(sp.diff(L2, g_) - sp.diff(sp.diff(L2, dd(g_)), t))
pdd = sp.Derivative(g_, (t, 2))
c2 = ELg.coeff(pdd); rem = sp.expand(ELg - c2 * pdd)
c1 = rem.coeff(dd(g_)); c0 = sp.simplify(sp.expand(rem - c1 * dd(g_)) / g_)
P = sp.simplify(c1 / c2); Q = sp.simplify(c0 / c2)
print("A_tensor =", A, "| check A == -c2/2:", sp.simplify(A + c2 / 2) == 0)
print("P =", P, "| Q =", Q)
print("Q - k^2/a^2 =", sp.simplify(Q - 3 * k**2 / t**2), " (expect 4/t^2 = 4H^2)")
with open('tensor_final.txt', 'w') as f:
    f.write(f"A = {A}\nP = {P}\nQ = {Q}\n")
