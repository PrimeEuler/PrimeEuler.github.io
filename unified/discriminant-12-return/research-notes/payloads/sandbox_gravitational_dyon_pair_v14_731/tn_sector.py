"""
Taub-NUT HJ vs MIC-Kepler HJ: exact sector identity.

TN HJ (unit mass), from the inverse metric (see charges.py):
    Sig f p_r^2 + p_th^2 + (k + 2 l eps cos th)^2 / sin^2 th = Sig (eps^2/f - mu^2),
    Sig = r^2 + l^2,  f = (r^2 - 2 m r - l^2)/Sig,  eps = specific energy, k = p_phi.

MIC HJ (flat, Poincare strength s), multiplied by r^2:
    r^2 p_r^2 + p_th^2 + (k + s cos th)^2 / sin^2 th + s^2 = r^2 (2E + 2 kap/r).

Claim: with s := 2 l eps the angular+pair sectors are IDENTICAL, and the full
left sides differ only radially:
    TN_LHS - MIC_LHS = (Sig f - r^2) p_r^2 - (2 l eps)^2 = -(2 m r + l^2) p_r^2 - (2 l eps)^2.
So the parabolic separation constants of TN are MIC's with s = 2 l eps:
charges (k/2 -/+ eps l) per parabola -- centre k/2, offset eps*l.
"""
import sympy as sp

r, th = sp.symbols('r th', positive=True)
l, m, eps, k = sp.symbols('l m eps k')
pr, pth = sp.symbols('pr pth')
Sig = r**2 + l**2
f = (r**2 - 2 * m * r - l**2) / Sig
s = 2 * l * eps

TN = Sig * f * pr**2 + pth**2 + (k + 2 * l * eps * sp.cos(th))**2 / sp.sin(th)**2
MIC = r**2 * pr**2 + pth**2 + (k + s * sp.cos(th))**2 / sp.sin(th)**2 + s**2
diff = sp.simplify(TN - MIC)
print("TN_LHS - MIC_LHS =", diff)
print("expected         =", sp.expand(-(2 * m * r + l**2) * pr**2 - (2 * l * eps)**2))
print("match:", sp.simplify(diff - (-(2 * m * r + l**2) * pr**2 - (2 * l * eps)**2)) == 0)
print("Sig*f - r^2 =", sp.simplify(Sig * f - r**2))
