"""Per-rung means on the circle + the means-as-conics identities in both walks."""
import sympy as sp
for n in range(1, 7):
    k = 12 - n
    A = sp.Rational(n + k, 2); H = sp.Rational(2 * n * k, n + k)
    Q2 = sp.Rational(n**2 + k**2, 2); X = sp.Rational(n - k, 2)
    assert sp.simplify(A * H - n * k) == 0            # AH = G^2
    assert sp.simplify(Q2 - (A**2 + X**2)) == 0      # Q^2 = A^2 + X^2
print("per-rung: AH = G^2 and Q^2 = A^2 + X^2 at every rung: OK")
T, u, X, A = sp.symbols('T u X A', positive=True)
n, k = u, 2 * T - u
print("row walk (pair (u, 2T-u)): A =", sp.simplify((n + k) / 2),
      "| G^2 =", sp.expand(n * k),
      "| H =", sp.simplify(2 * n * k / (n + k)),
      "| Q^2 =", sp.expand((n**2 + k**2) / 2))
n2, k2 = A + X, A - X
print("offset walk (pair (A+X, A-X)): G^2 =", sp.expand(n2 * k2),
      "| H =", sp.simplify(2 * n2 * k2 / (n2 + k2)),
      "| Q^2 =", sp.expand((n2**2 + k2**2) / 2))
