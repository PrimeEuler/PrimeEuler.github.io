"""List AM-GM clarification: point/volume pictures, Lorentzian n+1 form,
trace-determinant form, multipole ladder. All identities exact, checked numerically."""
import sympy as sp
import numpy as np
from scipy.special import gamma
rng = np.random.default_rng(7)

for n in [2, 3, 5, 8]:
    x = rng.uniform(0.5, 9, size=n)
    A = x.mean(); G = np.exp(np.log(x).mean()); Q = np.sqrt((x**2).mean())
    cosang = (x @ np.ones(n)) / (np.linalg.norm(x) * np.sqrt(n))
    assert abs(cosang - A / Q) < 1e-12                                  # cos(angle to diagonal) = A/Q
    assert abs(np.linalg.norm(x - A) - np.sqrt(n * (Q**2 - A**2))) < 1e-9   # distance to diagonal = sqrt(n) * std
    Vn1 = np.pi**(n / 2) / gamma(n / 2 + 1)
    assert abs((Vn1 * np.prod(x)) / (Vn1 * A**n) - (G / A)**n) < 1e-12  # ellipsoid/ball = (G/A)^n
    assert abs(np.linalg.norm(x) - np.sqrt(n) * Q) < 1e-12              # sphere through point: radius sqrt(n) Q
    t = np.sqrt(n) * A
    assert abs(t**2 - x @ x + (x - A).var() * n) < 1e-9                 # Lorentz: t^2 - |x|^2 = -sum (x_i - A)^2
    assert (x.sum() / n)**n >= np.prod(x)                               # (tr/n)^n >= det
print("list pictures + Lorentzian form + (tr/n)^n >= det: OK for n = 2,3,5,8")

T, X, mu = sp.symbols('T X mu', real=True)
u, v = T + X, T - X
assert sp.expand(u * v) == T**2 - X**2                                  # G^2 = Lorentzian interval
shift = sp.simplify(sp.Rational(1, 2) * sp.log(sp.exp(mu) * u / (sp.exp(-mu) * v)) - sp.Rational(1, 2) * sp.log(u / v))
assert shift == mu                                                      # s is the boost rapidity
uu, vv = sp.symbols('u v', positive=True)
M = sp.Matrix([[uu, sp.sqrt(uu * vv)], [sp.sqrt(uu * vv), vv]])
assert M.trace() == uu + vv and sp.simplify(M.det()) == 0               # crossing matrix: trace = sum, det = 0 (null)
print("pair Lorentzian: G^2 = T^2 - X^2, s = boost rapidity, crossing matrix null with trace = the sum: OK")

a, b, c = sp.symbols('a b c')
pair = [(uu, 1), (vv, -1)]
p = [sum(q * xx**k for q, xx in pair) for k in range(3)]
trip = [(a, 1), (b, 0), (c, -1)]
p3 = [sum(q * xx**k for q, xx in trip) for k in range(3)]
assert p[0] == uu + vv and p[1] == uu - vv and p[2] == p[0]             # pair: monopole + dipole only
assert len({p3[0], p3[1], p3[2]}) == 3                                  # triple: quadrupole independent
print("multipole ladder: p0 = sum (monopole); pair has exactly (2T, 2X); triple gains a quadrupole: OK")
