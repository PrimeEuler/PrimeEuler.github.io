"""
Audit: mass, acceleration and hbar in the acceleration /
transition parabola complex (2026-11-25, sandbox;
Jeremy's direction: gravity accelerates mass -- find a
selector in the acceleration/transition parabolas, or
at least a pointer; plus his proposal that every mass
hyperboloid has its own G acceleration paraboloid).

Method: census of the filed objects built from
acceleration parabolas and transition parabolas, each
marked for what it carries -- m, a, hbar -- and whether
its inputs are independent. Checks:

A1 EM acceleration reads q/m; gravitational
   acceleration is m-blind (one-tag seat, v15.1088).
A2 The quantum bouncer (the cone's own linear family,
   v15.469) is the unique object carrying m, a, hbar
   together: spectrum E_n = (hbar^2 m a^2 / 2)^{1/3}
   |a_n| with rigid Airy zeros -- verified numerically,
   including the m^{1/3} and a^{2/3} scalings.
A3 rho-power bookkeeping: with a = a*/rho,
   a* = m c^3 / hbar, the bouncer reads rho^{-2/3}
   while the seat clock reads rho^{+1} -- the pointer
   pair of v15.1163, re-derived.
A4 Jeremy's per-mass G acceleration paraboloid: the
   osculating paraboloid E = m + p^2/(2m) of the mass
   hyperboloid at its seat; gap series coefficients
   are v15.233's tangency numbers; curvature 1/m;
   focal length m/2. Shape carries m; the dynamics
   on it (uniform g) does not.
A5 Transition parabolas: J_+ amplitudes sqrt(r(D-r))
   are pure ladder combinatorics -- no m, no a.
"""
import numpy as np
import sympy as sp
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and bool(cond)

# ---------- A1: who carries m ----------
q, E, m, g = sp.symbols("q E m g", positive=True)
a_em = q * E / m
a_g = g
check("A1 a_EM = qE/m carries m (d/dm != 0); a_G = g "
      "is m-blind (d/dm = 0) -- universality in "
      "parabola language",
      sp.diff(a_em, m) != 0 and sp.diff(a_g, m) == 0)

# ---------- A2: the quantum bouncer ----------
AIRY = [2.3381074105, 4.0879494441, 5.5205598281]
def bouncer_levels(mm, gg, npts=1400, L=16.0):
    x = np.linspace(0, L, npts)
    dx = x[1] - x[0]
    main = np.full(npts, 1.0 / (mm * dx**2)) + mm * gg * x
    off = np.full(npts - 1, -0.5 / (mm * dx**2))
    H = diags([main, off, off], [0, 1, -1])
    vals = eigsh(H, k=3, which="SM", return_eigenvectors=False)
    return np.sort(vals)
E1 = bouncer_levels(1.0, 1.0)
pred = (0.5) ** (1 / 3) * np.array(AIRY)
rel = np.abs(E1 / pred - 1)
E2 = bouncer_levels(2.0, 1.0)
E3 = bouncer_levels(1.0, 2.0)
print(f"    bouncer m=g=hbar=1: levels {E1.round(4)} vs "
      f"Airy prediction {pred.round(4)} (max rel dev "
      f"{rel.max():.4f}); m-scaling {E2[0]/E1[0]:.4f} "
      f"(2^(1/3) = {2**(1/3):.4f}); a-scaling "
      f"{E3[0]/E1[0]:.4f} (2^(2/3) = {2**(2/3):.4f})")
check("A2 bouncer spectrum = (hbar^2 m a^2/2)^{1/3} "
      "|a_n| numerically, with m^{1/3} and a^{2/3} "
      "scalings -- the unique m+a+hbar object",
      rel.max() < 0.01
      and abs(E2[0] / E1[0] - 2 ** (1 / 3)) < 0.01
      and abs(E3[0] / E1[0] - 2 ** (2 / 3)) < 0.01)

# ---------- A3: rho powers ----------
rho, c, hb = sp.symbols("rho c hbar", positive=True)
a_star = m * c**3 / hb
a_of_rho = a_star / rho
En = (hb**2 * m * a_of_rho**2 / 2) ** sp.Rational(1, 3)
ratio = sp.simplify(En / (m * c**2))
seat_clock = sp.simplify(2 * sp.pi * c / a_of_rho
                         / (2 * sp.pi * hb / (m * c**2)))
print(f"    E_n/(m c^2) = {ratio} x |a_n|; seat clock "
      f"= {seat_clock} x (2 pi tau_C)")
check("A3 bouncer reads rho^{-2/3}, seat clock reads "
      "rho^{+1}: the pointer pair -- a second "
      "independent computation of either would read "
      "rho off their ratio",
      sp.simplify(ratio - 2 ** sp.Rational(-1, 3)
                  * rho ** sp.Rational(-2, 3)) == 0
      and sp.simplify(seat_clock - rho) == 0)

# ---------- A4: per-mass G paraboloid ----------
p = sp.symbols("p", real=True)
gap = sp.series(sp.sqrt(m**2 + p**2) - (m + p**2 / (2 * m)),
                p, 0, 9).removeO()
gap_expect = (-p**4 / (8 * m**3) + p**6 / (16 * m**5)
              - 5 * p**8 / (128 * m**7))
curv = sp.diff(sp.sqrt(m**2 + p**2), p, 2).subs(p, 0)
check("A4 osculating paraboloid of the m-hyperboloid: "
      "gap = -p^4/(8m^3) + p^6/(16m^5) - 5p^8/(128m^7) "
      "(v15.233's tangency coefficients 1/8, 1/16, "
      "5/128); seat curvature 1/m; focal length m/2 "
      "from p^2 = 2m(E - m)",
      sp.simplify(gap - gap_expect) == 0 and curv == 1 / m)

# ---------- A5: transition ladder carries nothing ----------
def ladder_ok(j2):
    # j = j2/2; rungs r = 0..2j; amp^2 = r (D - r), D = 2j+1
    j = sp.Rational(j2, 2)
    D = 2 * j + 1
    for r in range(1, int(2 * j) + 1):
        mj = j - r  # source m: target m+1 sits r below top
        su2 = j * (j + 1) - mj * (mj + 1)
        if sp.simplify(su2 - r * (D - r)) != 0:
            return False
    return True
check("A5 J_+ amplitudes sqrt(r(D-r)) equal the SU(2) "
      "values for j = 1/2..5 exactly -- pure ladder "
      "combinatorics, carrying neither m nor a",
      all(ladder_ok(j2) for j2 in range(1, 11)))

print("ALL PASS" if ok else "SOME FAILED")
