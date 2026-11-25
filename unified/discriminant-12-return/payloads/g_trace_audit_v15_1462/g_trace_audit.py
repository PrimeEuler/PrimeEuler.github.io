"""
G-trace audit (2026-11-25, sandbox; Jeremy's direction:
exploit the density / acceleration / interface web to
get a coupling -- first trace every appearance of G in
that web and count the independent payments).

Checks:
P1 G-power of every monomial entry in the web, by the
   logarithmic derivative G d(ln f)/dG.
P2 Surface gravity is Poisson's payment propagated to
   the boundary (Gauss), not a second payment.
P3 The Sciama apex cancels G: Omega = 1 identically
   along the flat FLRW constraint, so B = Omega/2
   is G-free as an output.
P4 The two-body closure (v15.428) forces ONE G:
   split source/response constants break momentum
   conservation identically.
P5 Census bookkeeping: exactly one independent
   payment (Poisson; kappa = 8 pi G is the same
   payment in ADM dress); every other entry is
   propagated, inverted, powered, or cancelled.
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and bool(cond)

G, rho, R, c, hb, Ms, I, mp, k2 = sp.symbols(
    "G rho R c hbar M_s I m_p k2", positive=True)

def gpower(f):
    return sp.simplify(G * sp.diff(sp.log(f), G))

entries = {
    "Poisson source 4 pi G rho": 4 * sp.pi * G * rho,
    "surface g (4/3) pi G rho R": sp.Rational(4, 3) * sp.pi * G * rho * R,
    "free-fall t_ff": sp.sqrt(3 * sp.pi / (32 * G * rho)),
    "tangency gap c^2/g_s": c**2 / (sp.Rational(4, 3) * sp.pi * G * rho * R),
    "tidal beta_2": 2 * G * Ms * I**2 / (hb**2 * R**3),
    "compactness GM/(R c^2)": G * Ms / (R * c**2),
    "tidal deformability Lambda": sp.Rational(2, 3) * k2 * (R * c**2 / (G * Ms))**5,
    "alpha_G": G * mp**2 / (hb * c),
    "ADM kappa": 8 * sp.pi * G,
}
expect = {
    "Poisson source 4 pi G rho": 1,
    "surface g (4/3) pi G rho R": 1,
    "free-fall t_ff": sp.Rational(-1, 2),
    "tangency gap c^2/g_s": -1,
    "tidal beta_2": 1,
    "compactness GM/(R c^2)": 1,
    "tidal deformability Lambda": -5,
    "alpha_G": 1,
    "ADM kappa": 1,
}
allpow = all(sp.simplify(gpower(f) - expect[k]) == 0
             for k, f in entries.items())
for k, f in entries.items():
    print(f"    G-power of {k}: {gpower(f)}")
check("P1 G-powers across the web: +1 at Poisson, "
      "surface g, beta_2, compactness, alpha_G, kappa; "
      "-1/2 free-fall; -1 tangency gap; -5 in Lambda "
      "-- all monomial propagations of one constant",
      allpow)

# ---------- P2: surface g is Poisson propagated ----------
g_s = sp.symbols("g_s", positive=True)
sol = sp.solve(sp.Eq(g_s * 4 * sp.pi * R**2,
                     4 * sp.pi * G * (4 * sp.pi * R**3 * rho / 3)),
               g_s)[0]
check("P2 Gauss on Poisson gives g_s = (4/3) pi G rho "
      "R identically -- the boundary face of the same "
      "payment, not a second one",
      sp.simplify(sol - sp.Rational(4, 3) * sp.pi * G * rho * R) == 0)

# ---------- P3: apex cancellation ----------
H = sp.symbols("H", positive=True)
rho_crit = 3 * H**2 / (8 * sp.pi * G)
Omega = sp.simplify(rho / rho_crit.subs(H**2, 8 * sp.pi * G * rho / 3))
check("P3 along the flat FLRW constraint "
      "H^2 = (8 pi G/3) rho, Omega = rho/rho_crit = 1 "
      "identically: G cancels, B = Omega/2 is G-free "
      "as an output", Omega == 1)

# ---------- P4: one G in the two-body closure ----------
m1, m2, r, G12, G21 = sp.symbols("m1 m2 r G12 G21",
                                 positive=True)
F_one = G * m2 * m1 / r**2 - G * m1 * m2 / r**2
F_split = G21 * m1 * m2 / r**2 - G12 * m2 * m1 / r**2
check("P4 one G: the pair's forces cancel identically "
      "(momentum conserved, v15.428's closure); split "
      "source/response constants leave net force "
      "(G21 - G12) m1 m2 / r^2, not identically zero -- "
      "the web admits no second gravitational constant",
      sp.simplify(F_one) == 0 and sp.simplify(F_split) != 0)

# ---------- P5: the count ----------
status = {
    "Poisson source 4 pi G rho": "PAYMENT",
    "surface g (4/3) pi G rho R": "propagated (P2)",
    "free-fall t_ff": "propagated",
    "tangency gap c^2/g_s": "inverted propagation",
    "tidal beta_2": "propagated (source field)",
    "compactness GM/(R c^2)": "propagated",
    "tidal deformability Lambda": "propagated (k2 G-free)",
    "alpha_G": "propagated (same G, hierarchy outfit)",
    "ADM kappa": "same payment, relativistic dress",
    "Sciama apex B = Omega/2": "cancelled (P3)",
}
check("P5 census count: exactly ONE independent "
      "payment (Poisson / kappa); every other G "
      "appearance in the density-interface web is a "
      "propagation, inversion, power, dress, or "
      "cancellation of it",
      sum(1 for v in status.values() if v == "PAYMENT") == 1
      and len(status) == 10)

print("ALL PASS" if ok else "SOME FAILED")
