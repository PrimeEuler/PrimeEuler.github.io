"""Multi-split diameter: boundaries are cumulative pairs sharing one center.
Tests: (1) circle identity per boundary; (2) sum h_i^2 = separation-weighted
pair sum; (3) equal-section closed form; (4) product form m=3;
(5) local adjacent GM != chord height; (6) (prod s_i)^(1/m) not a monomial in (h_i, D)."""
import sympy as sp, itertools
import numpy as np

def heights(sections):
    D = sum(sections); S = 0; out = []
    for s in sections[:-1]:
        S += s
        out.append((S, D - S, sp.sqrt(S * (D - S)), S - D / 2))
    return D, out

a, b, c, d = sp.symbols('a b c d', positive=True)
D, H = heights([a, b, c])
for (L, R, h, X) in H:
    assert sp.simplify(X**2 + h**2 - (D / 2)**2) == 0
print("1. every boundary: X^2 + h^2 = (D/2)^2 with pair (S_i | D - S_i): OK")
for secs in ([a, b], [a, b, c], [a, b, c, d]):
    D, H = heights(secs)
    lhs = sum(h**2 for _, _, h, _ in H)
    rhs = sum((l - j) * secs[j] * secs[l] for j, l in itertools.combinations(range(len(secs)), 2))
    assert sp.simplify(lhs - rhs) == 0
print("2. sum h_i^2 = sum_{j<l} (l-j) s_j s_l  (m=2,3,4 symbolic): OK")
s = sp.symbols('s', positive=True)
for mv in range(2, 8):
    D, H = heights([s] * mv)
    assert sp.simplify(sum(h**2 for _, _, h, _ in H) - s**2 * (mv - 1) * mv * (mv + 1) / 6) == 0
print("3. equal sections: sum h_i^2 = s^2 (m-1)m(m+1)/6: OK")
D, H = heights([a, b, c])
assert sp.factor(H[0][2]**2 * H[1][2]**2) == a * c * (a + b) * (b + c)
print("4. m=3: h1^2 h2^2 = a c (a+b)(b+c): OK")
D, H = heights([1, 2, 3])
print(f"5. (1,2,3): chord height at 2nd boundary = {H[1][2]}, local GM sqrt(b c) = sqrt(6) -> NOT equal (ratio {sp.nsimplify(H[1][2]/sp.sqrt(6))})")
def vals(aa, bb, cc):
    DD, HH = heights([aa, bb, cc])
    return np.array([np.log(float(HH[0][2])), np.log(float(HH[1][2])), np.log(float(DD)), np.log(float((aa * bb * cc) ** (1 / 3)))])
M = np.array([vals(1, 2, 3)[:3], vals(2, 5, 1)[:3], vals(3, 1, 4)[:3]]).T
y = np.array([vals(1, 2, 3)[3], vals(2, 5, 1)[3], vals(3, 1, 4)[3]])
sol = np.linalg.solve(M, y)
pred = float(np.exp(vals(5, 2, 2)[:3] @ sol)); actual = float(20 ** (1 / 3))
print(f"6. (abc)^(1/3) as monomial in (h1,h2,D): fitted exponents {np.round(sol,3)}, prediction {pred:.4f} vs actual {actual:.4f} -> NO identity")
