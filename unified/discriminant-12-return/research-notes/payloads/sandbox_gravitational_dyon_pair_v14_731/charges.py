"""
Taub-NUT conserved charges from the verified SU(2) Killing triad.
Extract the radial (Poincare) term of the total angular momentum.
"""
import sympy as sp

t, r, th, ph = sp.symbols('t r th ph')
l, m = sp.symbols('l m', positive=True)
f = sp.Function('f')(r)
Sig = r**2 + l**2
coords = [t, r, th, ph]

g = sp.zeros(4, 4)
g[0, 0] = -f
g[0, 3] = g[3, 0] = -2 * l * f * sp.cos(th)
g[3, 3] = -4 * l**2 * f * sp.cos(th)**2 + Sig * sp.sin(th)**2
g[1, 1] = 1 / f
g[2, 2] = Sig

# verified Killing vectors (contravariant), triad + fiber
xi = {
    'x': [2 * l * sp.cos(ph) / sp.sin(th), 0, -sp.sin(ph), -sp.cos(ph) * sp.cos(th) / sp.sin(th)],
    'y': [2 * l * sp.sin(ph) / sp.sin(th), 0,  sp.cos(ph), -sp.sin(ph) * sp.cos(th) / sp.sin(th)],
    'z': [0, 0, 0, 1],           # d_ph
    't': [1, 0, 0, 0],           # d_t
    'z2': [2 * l, 0, 0, 1],      # d_ph + 2l d_t (alternative z candidate)
}

def bracket(a, b):
    return [sp.simplify(sum(a[j] * sp.diff(b[i], coords[j]) - b[j] * sp.diff(a[i], coords[j])
                            for j in range(4))) for i in range(4)]

print("commutators (target: SU(2) [xi, xj] = -eps_ijk xk  or +eps):")
for (i, j, k) in [('x', 'y', 'z'), ('y', 'z', 'x'), ('z', 'x', 'y')]:
    br = bracket(xi[i], xi[j])
    diff = [sp.simplify(br[q] - xi[k][q]) for q in range(4)]
    diffm = [sp.simplify(br[q] + xi[k][q]) for q in range(4)]
    print(f"  [{i},{j}] = +{k}: {all(d == 0 for d in diff)} ; = -{k}: {all(d == 0 for d in diffm)}")
for (i, j, k) in [('x', 'y', 'z2'), ('y', 'z2', 'x'), ('z2', 'x', 'y')]:
    br = bracket(xi[i], xi[j])
    diff = [sp.simplify(br[q] - xi[k][q]) for q in range(4)]
    diffm = [sp.simplify(br[q] + xi[k][q]) for q in range(4)]
    print(f"  [{i},{j}] = +{k}: {all(d == 0 for d in diff)} ; = -{k}: {all(d == 0 for d in diffm)}")

# ---- conserved charges for a unit-mass geodesic: Q = xi^mu p_mu ----
td, rd, thd, phd = sp.symbols('td rd thd phd')
u = [td, rd, thd, phd]
p = [sum(g[mu, nu] * u[nu] for nu in range(4)) for mu in range(4)]
p_t, p_r, p_th, p_ph = p
eps = -p_t  # specific energy (per unit mass), >0 outside horizon

Q = {k: sp.simplify(sum(xi[k][mu] * p[mu] for mu in range(4))) for k in ['x', 'y', 'z', 'z2']}

n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
S = sp.simplify(n[0] * Q['x'] + n[1] * Q['y'] + n[2] * Q['z'])
print("\nradial projection  n.Q  (triage with xi_z = d_ph):", sp.simplify(S))
print("   in units of eps*l:", sp.simplify(S / (eps * l)))
S2 = sp.simplify(n[0] * Q['x'] + n[1] * Q['y'] + n[2] * Q['z2'])
print("radial projection with xi_z = d_ph + 2l d_t      :", sp.simplify(S2))

J2 = sp.simplify(Q['x']**2 + Q['y']**2 + Q['z']**2)
# EM-monopole-style candidate decomposition: orbital part + (Poincare)^2
cand = Sig**2 * thd**2 + (p_ph + 2 * l * eps * sp.cos(th))**2 / sp.sin(th)**2 + (2 * l * eps)**2
print("\nJ^2 - [ Sig^2 thd^2 + (p_ph + 2 l eps cos th)^2/sin^2 th + (2 l eps)^2 ] =",
      sp.simplify(sp.together(J2 - cand)))
cand2 = Sig**2 * thd**2 + (p_ph - 2 * l * eps * sp.cos(th))**2 / sp.sin(th)**2 + (2 * l * eps)**2
print("J^2 - [ same with (p_ph - 2 l eps cos th) ] =",
      sp.simplify(sp.together(J2 - cand2)))
print("\nJ^2 =", sp.simplify(J2))
print("p_ph =", sp.simplify(p_ph))
print("eps  =", sp.simplify(eps))
