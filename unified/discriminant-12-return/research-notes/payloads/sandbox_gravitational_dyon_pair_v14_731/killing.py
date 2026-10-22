"""
Taub-NUT: find the SU(2) Killing vectors, verify the Killing equation exactly.

Metric (geometric units), coords (t, r, th, ph):
  ds^2 = -f(r) (dt + 2 l cos(th) dph)^2 + dr^2/f(r) + (r^2+l^2)(dth^2 + sin^2 th dph^2)
f left as an unspecified function of r: the isometry algebra does not depend on it.
"""
import sympy as sp

t, r, th, ph = sp.symbols('t r th ph')
l = sp.symbols('l', positive=True)
f = sp.Function('f')(r)
Sig = r**2 + l**2
coords = [t, r, th, ph]

g = sp.zeros(4, 4)
g[0, 0] = -f
g[0, 3] = g[3, 0] = -2 * l * f * sp.cos(th)
g[3, 3] = -4 * l**2 * f * sp.cos(th)**2 + Sig * sp.sin(th)**2
g[1, 1] = 1 / f
g[2, 2] = Sig

def lie(xi):
    """(L_xi g)_{mu nu} for contravariant components xi (list of 4)."""
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            expr = sum(xi[lam] * sp.diff(g[mu, nu], coords[lam]) for lam in range(4))
            expr += sum(g[lam, nu] * sp.diff(xi[lam], coords[mu]) for lam in range(4))
            expr += sum(g[mu, lam] * sp.diff(xi[lam], coords[nu]) for lam in range(4))
            out[mu, nu] = sp.simplify(expr)
    return out

def report(name, xi):
    L = lie(xi)
    nonzero = [(mu, nu, L[mu, nu]) for mu in range(4) for nu in range(4) if L[mu, nu] != 0]
    print(f"{name}: Killing = {len(nonzero) == 0}")
    for mu, nu, e in nonzero:
        print("   ", (mu, nu), sp.simplify(e))
    return len(nonzero) == 0

zero, one = sp.Integer(0), sp.Integer(1)
# trivial Killings
report("d_t", [one, zero, zero, zero])
report("d_ph", [zero, zero, zero, one])

# Rotation generators on S^2 (standard):
# R_x = -sin(ph) d_th - cos(ph) cot(th) d_ph
# R_y =  cos(ph) d_th - sin(ph) cot(th) d_ph
# Add unknown t-shift c(th, ph): solve from the (t, th) and (t, ph) Lie components.
c = sp.Function('c')(th, ph)

xi_x = [c, zero, -sp.sin(ph), -sp.cos(ph) * sp.cos(th) / sp.sin(th)]
Lx = lie(xi_x)
eqs = set()
for mu in range(4):
    for nu in range(4):
        if Lx[mu, nu] != 0:
            eqs.add(sp.simplify(Lx[mu, nu]))
print("\nx-rotation: nonzero Lie components (in terms of c):")
for e in eqs:
    print("   ", e)
sol = sp.dsolve  # inspect manually below
# From the equations, try candidate c_x:
cand_x = 2 * l * sp.cos(ph) / sp.sin(th)
xi_x2 = [cand_x, zero, -sp.sin(ph), -sp.cos(ph) * sp.cos(th) / sp.sin(th)]
report("R_x with c = +2l cos(ph)/sin(th)", xi_x2)
cand_xm = -2 * l * sp.cos(ph) / sp.sin(th)
report("R_x with c = -2l cos(ph)/sin(th)", [cand_xm, zero, -sp.sin(ph), -sp.cos(ph) * sp.cos(th) / sp.sin(th)])

cand_y = 2 * l * sp.sin(ph) / sp.sin(th)
xi_y2 = [cand_y, zero, sp.cos(ph), -sp.sin(ph) * sp.cos(th) / sp.sin(th)]
report("R_y with c = +2l sin(ph)/sin(th)", xi_y2)
cand_ym = -2 * l * sp.sin(ph) / sp.sin(th)
report("R_y with c = -2l sin(ph)/sin(th)", [cand_ym, zero, sp.cos(ph), -sp.sin(ph) * sp.cos(th) / sp.sin(th)])
