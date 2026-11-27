#!/usr/bin/env python3
"""Chandrasekaran (4.21) vs Gravity-lane H^2: symbolic comparison.
Run: python3 compare_h2.py  (SymPy 1.12, NumPy 1.26.4 box)
"""
import sympy as sp

def gauss_curvature(metric, coords):
    """K = R_scalar/2 for a 2D metric matrix."""
    n = 2
    inv = metric.inv()
    # Christoffel Gamma^k_ij
    G = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                expr = 0
                for l in range(n):
                    expr += inv[k, l]*(sp.diff(metric[l, j], coords[i])
                                       + sp.diff(metric[l, i], coords[j])
                                       - sp.diff(metric[i, j], coords[l]))
                G[k][i][j] = sp.simplify(expr/2)
    # Ricci R_ij = d_k Gamma^k_ij - d_j Gamma^k_ik + Gamma Gamma - Gamma Gamma
    Ric = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            expr = 0
            for k in range(n):
                expr += sp.diff(G[k][i][j], coords[k]) - sp.diff(G[k][i][k], coords[j])
                for m in range(n):
                    expr += G[k][k][m]*G[m][i][j] - G[k][j][m]*G[m][i][k]
            Ric[i, j] = sp.simplify(expr)
    R = sp.simplify(sum(inv[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
    return sp.simplify(R/2), G

print("="*70)
print("(a) Chandrasekaran (4.21a) -> (4.21c), and curvature")
z1, z2 = sp.symbols('z1 z2', real=True)
E = sp.exp(z1)
qbar = sp.Matrix([[E, E*z2],
                  [E*z2, sp.exp(-z1) + E*z2**2]])
print("det qbar            =", sp.simplify(qbar.det()), " (expect 1)")
# positive definite: leading minors
print("qbar[0,0]           =", qbar[0, 0], "> 0 for real z1; det = 1 > 0 -> pos.def.")
qinv = qbar.inv()
coords_z = [z1, z2]
dq = [qbar.diff(c) for c in coords_z]
g = sp.zeros(2)
for a in range(2):
    for b in range(2):
        # (4.21b): (1/2) qbar^AC qbar^BD dq_AB dq'_CD = (1/2) Tr(q^-1 dq_a q^-1 dq_b)
        g[a, b] = sp.simplify(sp.Rational(1, 2)*(qinv*dq[a]*qinv*dq[b]).trace())
print("DeWitt metric (4.21b) pulled back =\n", g, " (expect diag(1, exp(2 z1)))")
K_ch, _ = gauss_curvature(g, coords_z)
print("Gaussian curvature of (4.21c) metric =", K_ch, " (expect -1)")

print("="*70)
print("Lane metric (v15.1386/1451/1453/1454): G_AB = delta_AB - phi_A phi_B/(1+phi^2)")
u, v = sp.symbols('u v', real=True)
D = 1 + u**2 + v**2
Glane = sp.Matrix([[1 - u**2/D, -u*v/D],
                   [-u*v/D,     1 - v**2/D]])
print("det G_lane          =", sp.simplify(Glane.det()), " (entry: 1/(1+u^2+v^2))")
print("G_lane^-1           =\n", sp.simplify(Glane.inv()), " (entry: delta^AB + phi^A phi^B)")
K_lane, Gam = gauss_curvature(Glane, [u, v])
print("Gaussian curvature of lane metric =", K_lane, " (expect -1: unit H^2, no rescaling)")
# entry's Christoffel claim: Gamma^A_BC = -phi^A G_BC
phi = [u, v]
ok = True
for A in range(2):
    for B in range(2):
        for C in range(2):
            if sp.simplify(Gam[A][B][C] - (-phi[A]*Glane[B, C])) != 0:
                ok = False
print("Christoffel Gamma^A_BC = -phi^A G_BC holds:", ok)

print("="*70)
print("(b) Chart change: lane (u,v) = embedding (X,Y);  Q = [[T+Y, X],[X, T-Y]] = qbar")
# Forward: z -> (u,v)
u_of_z = E*z2
v_of_z = sp.sinh(z1) - E*z2**2/2
T_of_z = sp.cosh(z1) + E*z2**2/2
print("T^2 - u^2 - v^2     =", sp.simplify((T_of_z**2 - u_of_z**2 - v_of_z**2).rewrite(sp.exp)), " (expect 1)")
# Pullback of lane metric under the chart change
J = sp.Matrix([[sp.diff(u_of_z, z1), sp.diff(u_of_z, z2)],
               [sp.diff(v_of_z, z1), sp.diff(v_of_z, z2)]])
Gpull = sp.simplify(J.T * Glane.subs({u: u_of_z, v: v_of_z}) * J)
# rewrite in exp(z1) to help simplification
Gpull = sp.simplify(Gpull.rewrite(sp.exp))
print("Pullback of lane G under chart change =\n", Gpull, " (expect diag(1, exp(2 z1)))")
# Inverse: z1 = log(T + v), z2 = u/(T + v),  T = sqrt(1+u^2+v^2)
Tuv = sp.sqrt(1 + u**2 + v**2)
z1_back = sp.log(Tuv + v)
z2_back = u/(Tuv + v)
print("exp(z1_back) - (T+v) =", sp.simplify(sp.exp(z1_back) - (Tuv + v)), " (identity by construction)")
# numeric spot-check of the full round trip + metric pullback
import random
random.seed(27112026)
maxerr = 0.0
for _ in range(5):
    a, b = random.uniform(-1.5, 1.5), random.uniform(-2, 2)
    uu = float(u_of_z.subs({z1: a, z2: b})); vv = float(v_of_z.subs({z1: a, z2: b}))
    TT = float(Tuv.subs({u: uu, v: vv}))
    z1n = float(z1_back.subs({u: uu, v: vv})); z2n = float(z2_back.subs({u: uu, v: vv}))
    maxerr = max(maxerr, abs(z1n - a), abs(z2n - b))
    Gnum = Gpull.subs({z1: a, z2: b})
    target = sp.diag(1, sp.exp(2*a))
    maxerr = max(maxerr, max(abs(float(x)) for x in (Gnum - target)))
print("numeric round-trip + pullback max error over 5 random points:", maxerr)

print("="*70)
print("(d) integrand identity: (d qbar)(d qbar)^raised = 2 * H^2 speed^2 along a curve")
s = sp.symbols('s', real=True)
z1s = sp.Function('z1')(s); z2s = sp.Function('z2')(s)
qs = qbar.subs({z1: z1s, z2: z2s})
qps = qs.diff(s)
contr = sp.simplify((qs.inv()*qps*qs.inv()*qps).trace())
speed2 = sp.diff(z1s, s)**2 + sp.exp(2*z1s)*sp.diff(z2s, s)**2
print("Tr(q^-1 q' q^-1 q') - 2[(z1')^2 + e^{2z1}(z2')^2] =", sp.simplify(contr - 2*speed2))
print("=> (1/8)(ds qbar)_AB (ds qbar)^AB = (1/4)[(z1')^2 + e^{2z1}(z2')^2]  (classical (3.26c) integrand)")
print("   quantum (4.22) is the same density with coefficient 1/4, Weyl-ordered, s-weighted per (3.26c).")
