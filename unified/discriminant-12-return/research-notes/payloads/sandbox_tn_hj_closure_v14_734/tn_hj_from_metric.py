"""
Close Audit R338's one loose end (v14.732): derive the raw Taub-NUT
Hamilton-Jacobi equation quoted at the top of tn_sector.py DIRECTLY from
the inverse metric, symbolically, with f(r) arbitrary.

HJ: g^mn p_m p_n = -1 (unit mass), p = (-eps, pr, pth, k).
Claim (tn_sector.py): multiplied by Sig = r^2 + l^2,

  Sig f pr^2 + pth^2 + (k + 2 l eps cos th)^2 / sin^2 th = Sig (eps^2/f - 1).

The step a first pass typically misses: the (t, ph) block determinant is
-f*Sig*sin^2(th), so g^tt contributes -Sig/f * eps^2 through its
-Sig sin^2(th) part, while its 4 l^2 f cos^2(th) part completes the square
(k + 2 l eps cos th)^2 with the cross term.
"""
import sympy as sp

r, th = sp.symbols('r th', positive=True)
l, eps, k, pr, pth = sp.symbols('l eps k pr pth')
f = sp.Function('f')(r)
Sig = r**2 + l**2

g = sp.zeros(4, 4)
g[0, 0] = -f
g[0, 3] = g[3, 0] = -2 * l * f * sp.cos(th)
g[3, 3] = -4 * l**2 * f * sp.cos(th)**2 + Sig * sp.sin(th)**2
g[1, 1] = 1 / f
g[2, 2] = Sig

ginv = g.inv()
p = sp.Matrix([-eps, pr, pth, k])
HJ = sp.expand((p.T * ginv * p)[0])
lhs = sp.simplify(Sig * (HJ + 1))
claim = Sig * f * pr**2 + pth**2 + (k + 2 * l * eps * sp.cos(th))**2 / sp.sin(th)**2 \
        - Sig * (eps**2 / f - 1)
print("Sig*(HJ+1) - [claimed HJ lhs - Sig(eps^2/f - 1)] =", sp.simplify(sp.together(lhs - claim)))
print("det of (t,ph) block =", sp.factor(g[0, 0] * g[3, 3] - g[0, 3]**2))
