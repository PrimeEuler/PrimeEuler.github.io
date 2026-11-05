"""
Door anatomy III (2026-11-05, sandbox): the coupling door,
measured. v15.391 sec.2 compressed the dynamics door to
g1, g2, g3 + Higgs/Yukawa, with every vertex matrix element
frame-fixed. This build asks the anatomy question: exactly
which coupling-related quantities DOES the frame determine,
and what species is the residue?

Frame-determined (all computed here from the closed label
table, exact Fractions):
 (a) the trace indices S_i = sum over one LH generation of the
     Dynkin index per gauge factor -- equal for SU(3) and SU(2),
     and for U(1) iff the generator is the equal-index
     normalization yhat = sqrt(3/5) * (Y/2): the 5/3 is a
     property of the frame's table;
 (b) sin^2 theta_W = 3/8 at a hypothetical equal-coupling
     point (a rational frame point, conditional on the
     EXTERNAL assumption of unification);
 (c) the one-loop beta coefficients b_i -- the frame knows how
     the couplings MOVE (slopes are label arithmetic, and they
     depend on door II's integer N_g).
Not frame-determined:
 (d) the values: running the b_i up from the measured
     (imported) mZ values, the three pairwise crossing scales
     are three different scales -- the table itself, given
     measured inputs, falsifies exact one-loop unification.
     The frame's dimensionless outputs are all rational;
     nature's coupling values are three real numbers it
     cannot name. Plus the Higgs/Yukawa reals, filed at the
     shared border with door II.
"""
from fractions import Fraction as F
import numpy as np

# LH Weyl fields of one generation: (name, color dim, weak dim,
# Y/2 as Fraction). Conjugates used for R singlets (Y flips sign;
# indices use |.|, squares -- signs tracked where linear).
LH = [("L_L", 1, 2, F(-1, 2)), ("Q_L", 3, 2, F(1, 6)),
      ("u^c", 3, 1, F(-2, 3)), ("d^c", 3, 1, F(1, 3)),
      ("e^c", 1, 1, F(1))]
T3 = {"3": F(1, 2), "3bar": F(1, 2)}   # Dynkin index of (anti)fundamental

print("=" * 76)
print("(a) trace indices over one LH generation (exact)")
print("=" * 76)
S_su3 = sum(F(2 if n == "Q_L" else 1) * T3["3"] for n, cd, wd, y in LH if cd == 3)
S_su2 = sum(F(cd) * F(1, 2) for n, cd, wd, y in LH if wd == 2)
S_y = sum(F(cd * wd) * y * y for n, cd, wd, y in LH)
print(f"  S_SU(3) = {S_su3},  S_SU(2) = {S_su2},  S_(Y/2) = {S_y}")
print(f"  ratio S_(Y/2)/S_SU(2) = {S_y / S_su2}  -> equal-index generator")
print(f"  yhat = sqrt(3/5)*(Y/2) makes S_yhat = {S_y * F(3, 5)} = S_SU(2): "
      f"the 5/3 is frame-table arithmetic.")

print()
print("=" * 76)
print("(b) the rational point: sin^2 theta_W at equal couplings")
print("=" * 76)
s2 = F(3, 5) / (1 + F(3, 5))
print(f"  g'^2 = (3/5) g1^2 and g1 = g2  =>  sin^2 = (3/5)/(1+3/5) = {s2} "
      f"= {float(s2):.4f}   (measured, imported: 0.23122)")

print()
print("=" * 76)
print("(c) one-loop beta coefficients from the table (exact)")
print("=" * 76)
def betas(Ng):
    # per-generation fermion index sums (LH Weyl), all components
    f3 = sum(F(2 if n == "Q_L" else 1) * T3["3"] for n, cd, wd, y in LH if cd == 3)
    f2 = sum(F(cd) * F(1, 2) for n, cd, wd, y in LH if wd == 2)
    f1 = sum(F(cd * wd) * y * y for n, cd, wd, y in LH) * F(3, 5)  # yhat^2
    b3 = F(-11) + F(2, 3) * Ng * f3
    b2 = F(-22, 3) + F(2, 3) * Ng * f2 + F(1, 3) * F(1, 2)      # + Higgs doublet
    b1 = F(2, 3) * Ng * f1 + F(1, 3) * (2 * F(3, 5) * F(1, 2) ** 2)  # Higgs: 2 comps
    return b1, b2, b3
b1, b2, b3 = betas(3)
print(f"  N_g = 3: (b1, b2, b3) = ({b1}, {b2}, {b3})  "
      f"= ({float(b1):.4f}, {float(b2):.4f}, {float(b3):.4f})  [standard SM values]")
print(f"  the slopes are functions of door II's integer: "
      f"b3(N_g) = -11 + (4/3) N_g -> N_g=2: {betas(2)[2]}, N_g=4: {betas(4)[2]}")

print()
print("=" * 76)
print("(d) values are not frame data: pairwise crossings from mZ inputs")
print("=" * 76)
MZ = 91.1876
ainv = 127.951; s2w = 0.23122; als = 0.1179     # imported measured values
a1i = (3 / 5) * ainv * (1 - s2w)                # GUT-normalized alpha_1^-1
a2i = ainv * s2w
a3i = 1 / als
print(f"  alpha_i^-1(mZ) = ({a1i:.2f}, {a2i:.2f}, {a3i:.2f})  [imported]")
b = [float(b1), float(b2), float(b3)]
ai = [a1i, a2i, a3i]
for (i, j) in ((0, 1), (0, 2), (1, 2)):
    t = 2 * np.pi * (ai[i] - ai[j]) / (b[i] - b[j])
    print(f"  alpha_{i+1} = alpha_{j+1} at mu = {MZ * np.exp(t):.2e} GeV")
print("  three different scales: no common meeting point. Given the")
print("  measured values, the frame's own table falsifies exact")
print("  one-loop unification -- 3/8 is a conditional rational")
print("  point, not a frame theorem.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("Frame-determined: all vertex matrix elements; all charge")
print("ratios; the equal-index ratio 5/3; the conditional point")
print("sin^2 = 3/8; the full one-loop beta vector (given N_g).")
print("Every dimensionless number the frame produces is rational.")
print("Residue species: THREE REAL NUMBERS (g1, g2, g3 at a scale)")
print("-- continuous empirical data, a third species beside door")
print("I's bit and door II's integer -- plus the Higgs/Yukawa")
print("reals at the shared border with door II. The frame knows")
print("how the couplings move; where they are is nature's data.")
print("Full SM tally (massless neutrinos): 18 continuous inputs")
print("(3 gauge + 2 Higgs + 9 masses + 4 CKM) + theta_QCD; the")
print("frame determines none of the values and all of the")
print("discrete structure they hang on.")
