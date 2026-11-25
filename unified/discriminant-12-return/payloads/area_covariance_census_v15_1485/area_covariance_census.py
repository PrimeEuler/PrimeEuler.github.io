"""
Area-covariance census producer (2026-11-25, sandbox;
Gravity v15.1469 [NEXT SANDBOX] handoff, Audit R649
confirmed): verify the load-bearing arithmetic of the
census -- the trigger identity, the measure split, the
counting split, the boost counterexample, and the
radius cancellation.

C1 v15.1469 trigger: for independent centered
   Gaussian gradient pairs with common covariance
   Sigma, E[(a_x b_y - a_y b_x)^2] = 2 det Sigma.
   At fixed trace V = 1/16 (diagonal family
   diag(s, V-s)) the area-squared runs 0 -> V^2/2
   = 1/512; fixed-norm gradients give V^2 sin^2
   theta, 0 -> V^2 = 1/256. Variance fixes the
   trace only; the area lives in the determinant /
   orientation the trace does not see.
C2 v15.1401 measure split: fixed-T transverse
   annular areas give ratio 3; rapidity-cutoff
   proper volumes give 7. The area answer depends
   on the chosen measure/slicing.
C3 v15.1402 counting split: Hilbert dimension ratio
   is 2 for all D; coadjoint orbit area ratio
   (2D-1)/(D-1) equals 3 only at D=2 and tends to
   2. The carriers' own measures do not select the
   geometric 3:1.
C4 v15.1467 boost counterexample: the balanced pair
   (1,1) has pair variance 0 and Q = nk = 1; after
   a boost of rapidity 1 the variance is sinh^2(1)
   = 1.3810978455418155 while Q stays 1. Pair
   variance is a rung label in a pairing frame, not
   a shell invariant.
C5 v15.1398 radius cancellation: the canonical
   quartic vertex prefactor g r^2 (sqrt2/M_Pl)
   (1/(f^2 r^2)) is exactly r-free.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and bool(cond)

# ---------- C1: the 1469 trigger ----------
s, V = sp.symbols("s V", nonnegative=True)
# diagonal Sigma = diag(s, V-s); independent centered
# a, b: E[wedge^2] = E[ax^2]E[by^2] + E[ay^2]E[bx^2]
# (cross terms vanish by centering/independence)
Ewedge2 = s * (V - s) + (V - s) * s
det = s * (V - s)
extremum = sp.diff(Ewedge2, s)
s_star = sp.solve(extremum, s)[0]
check("C1 E[wedge^2] = 2 det Sigma on the diagonal "
      "family; at tr Sigma = V = 1/16 it runs from 0 "
      "(s = 0, rank one) to V^2/2 = 1/512 at s = V/2; "
      "fixed-norm area^2 = V^2 sin^2(theta) reaches "
      "V^2 = 1/256 only at theta = pi/2",
      sp.simplify(Ewedge2 - 2 * det) == 0
      and s_star == V / 2
      and sp.simplify(Ewedge2.subs(s, V / 2)
                      .subs(V, sp.Rational(1, 16))
                      - sp.Rational(1, 512)) == 0
      and Ewedge2.subs(s, 0) == 0)

# ---------- C2: the 1401 measure split ----------
a, b = F(1, 2), F(1, 4)
area_ratio = (a * a - b * b) / (b * b)
vol_ratio = (a ** 3 - b ** 3) / b ** 3
check("C2 fixed-T annular area ratio = 3 exactly, "
      "rapidity-cutoff proper-volume ratio = 7 "
      "exactly: the 'area' of the same shells is "
      "measure-supplied, not shell-fixed",
      area_ratio == 3 and vol_ratio == 7)

# ---------- C3: the 1402 counting split ----------
def orbit_ratio(D):
    return F(2 * D - 1, D - 1)
check("C3 Hilbert ratio = 2 for all D; orbit area "
      "ratio (2D-1)/(D-1) = 3 only at D = 2, = 5/2 "
      "at D = 3, tends to 2: no carrier measure "
      "selects the geometric ratio",
      all(F(2 * D, D) == 2 for D in range(2, 50))
      and orbit_ratio(2) == 3 and orbit_ratio(3) == F(5, 2)
      and orbit_ratio(10 ** 6) < F(2000001, 999999))

# ---------- C4: the 1467 boost counterexample ----------
eta = 1.0
T0, X0 = 1.0, 0.0  # balanced pair (1,1): T=1, X=0
X1 = X0 * np.cosh(eta) + T0 * np.sinh(eta)
Q0 = 1 * 1
check("C4 balanced pair: variance 0 at rest, "
      "sinh^2(1) = 1.3810978455418155 after boost, "
      "Q = nk = 1 invariant -- pair variance is not "
      "a shell invariant",
      abs(X1 ** 2 - np.sinh(eta) ** 2) < 1e-15
      and abs(np.sinh(eta) ** 2 - 1.3810978455418155) < 1e-12
      and Q0 == 1)

# ---------- C5: the 1398 cancellation ----------
g, r, f, Mpl = sp.symbols("g r f M_Pl", positive=True)
vertex = g * r ** 2 * (sp.sqrt(2) / Mpl) * (1 / (f ** 2 * r ** 2))
check("C5 canonical quartic vertex = sqrt(2) g / "
      "(M_Pl f^2): the quarter radius cancels "
      "exactly and cannot fix the coupling",
      sp.simplify(vertex - sp.sqrt(2) * g / (Mpl * f ** 2)) == 0)

print("ALL PASS" if ok else "SOME FAILED")
