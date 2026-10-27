"""The (n+k)/(n-k) step ladder on diameter m (unit sections): rung table for m=12
and the exact ladder aggregates, checked at m=10,12."""
import sympy as sp
D = 12
V = sp.Integer(1)
print("step split off GM ratio dim cumvol")
for n in range(1, D):
    k = D - n; V *= sp.sqrt(n * k)
    ratio = "inf" if n == k else str(sp.Rational(D, abs(n - k)))
    print(n, f"{n}|{k}", n - 6, sp.sqrt(n * k), ratio, n + 1, sp.nsimplify(V))
for m in [10, 12]:
    rungs = [(n, m - n) for n in range(1, m)]
    A = sp.Rational(m, 2)
    sG2 = sum(n * k for n, k in rungs)
    sQ2 = sum(sp.Rational(n**2 + k**2, 2) for n, k in rungs)
    sH = sum(sp.Rational(2 * n * k, m) for n, k in rungs)
    pG = sp.prod(sp.sqrt(n * k) for n, k in rungs)
    pH = sp.prod(sp.Rational(2 * n * k, m) for n, k in rungs)
    pQ2 = sp.prod(sp.Rational(n**2 + k**2, 2) for n, k in rungs)
    assert sG2 == (m - 1) * m * (m + 1) // 6 and sQ2 == (m - 1) * m * (2 * m - 1) // 6
    assert sH == sp.Rational(m**2 - 1, 3) and sp.simplify(pG - sp.factorial(m - 1)) == 0
    assert sp.simplify(pH - sp.factorial(m - 1)**2 / A**(m - 1)) == 0
    print(f"m={m}: sumG2={sG2} sumQ2={sQ2} sumH={sH} prodG={sp.factorial(m-1)} prodH={pH} prodQ2={pQ2} (no collapse)")
print("ladder aggregates: ALL EXACT")
