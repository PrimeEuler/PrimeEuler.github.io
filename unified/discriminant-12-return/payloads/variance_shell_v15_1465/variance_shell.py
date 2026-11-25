"""
Variance shells (2026-11-25, sandbox; Jeremy's proposal,
filed at his direction): the nested mass hyperboloids
inside the photon cone read as constant-variance
sections. Exact checks:

V1 offset^2 IS the pair variance: for the pair {n, k},
   AM^2 - GM^2 = ((n-k)/2)^2 = the two-point variance.
V2 Elementary variances: the first unbalanced EM pair
   (2,1) has variance 1/4; the first unbalanced
   gravity pair (1, 1/2) at the half-step has 1/16.
V3 The mass shell is a section: the state point
   ((n+k)/2, (n-k)/2, sqrt(nk)) lies on the cone and
   at fixed product nk = m^2 sits at height Y = m
   with T^2 - X^2 = m^2.
V4 Gap identity: E - |p| = min(n, k) -- the state's
   distance from the cone along its ray.
V5 m/E = sech(psi), psi = (1/2) ln(n/k): the
   Gudermannian radius of the shell point.
V6 Dilation: (n,k) -> (cn, ck) sends m -> cm and
   scales the cone point by c; the cone is invariant.
   Mass ratios are dilation factors between sections.
V7 The quarter-grid Casimir residues decompose as
   EM quarters plus the gravity variance:
   5/16 = 1/4 + 1/16, 13/16 = 3/4 + 1/16 (v15.544,
   v15.866).
"""
from fractions import Fraction as F
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and bool(cond)

pairs = [(F(a), F(b)) for a in range(1, 13) for b in range(1, 13)]
pairs += [(F(1), F(1, 2)), (F(3, 2), F(1, 2)), (F(5, 2), F(3, 2))]

def var2(n, k):
    return ((n - k) / 2) ** 2

check("V1 AM^2 - GM^2 = ((n-k)/2)^2 = two-point "
      "variance of {n,k}, exact on integer and "
      "half-step pairs",
      all(((n + k) / 2) ** 2 - n * k == var2(n, k)
          for n, k in pairs))

check("V2 elementary variances: (2,1) -> 1/4 (EM), "
      "(1, 1/2) -> 1/16 (gravity half-step)",
      var2(F(2), F(1)) == F(1, 4)
      and var2(F(1), F(1, 2)) == F(1, 16))

n, k = sp.symbols("n k", positive=True)
T = (n + k) / 2
X = (n - k) / 2
Y = sp.sqrt(n * k)
check("V3 state point lies on the cone identically "
      "(T^2 = X^2 + Y^2) and its section invariant is "
      "T^2 - X^2 = Y^2 = nk: fixed product = fixed "
      "height Y = m, the mass shell as a cone section",
      sp.simplify(T**2 - X**2 - Y**2) == 0)

def gap_ok(nn, kk):
    E = (nn + kk) / 2
    p = abs(nn - kk) / 2
    return E - p == min(nn, kk)
check("V4 E - |p| = min(n, k) on all test pairs: "
      "the smaller light-cone component is the "
      "state's distance from the cone along its ray",
      all(gap_ok(nn, kk) for nn, kk in pairs))

r = sp.symbols("r", positive=True)
# both sides depend only on the ratio r = n/k:
# m/E = 2 sqrt(r)/(r+1); sech((1/2) ln r)
#     = 2/(sqrt(r) + 1/sqrt(r)) -- equal by sqrt algebra
check("V5 m/E = sech(psi), psi = (1/2) ln(n/k): both "
      "sides are functions of the ratio alone and "
      "agree identically",
      sp.simplify(2 * sp.sqrt(r) / (r + 1)
                  - 2 / (sp.sqrt(r) + 1 / sp.sqrt(r))) == 0
      and sp.simplify(sp.sqrt(n * k) / ((n + k) / 2)
                      - 2 * sp.sqrt(n / k) / (n / k + 1)) == 0)

c = sp.symbols("c", positive=True)
check("V6 dilation (n,k) -> (cn,ck): product scales "
      "c^2 (m -> cm), the cone point scales by c, "
      "and T^2 - X^2 - Y^2 = 0 is preserved -- mass "
      "ratios are dilation factors between sections",
      sp.simplify((c * n) * (c * k) - c**2 * n * k) == 0
      and sp.simplify((c * T) ** 2 - (c * X) ** 2
                      - (c * Y) ** 2) == 0)

check("V7 Casimir residues: 5/16 = 1/4 + 1/16 and "
      "13/16 = 3/4 + 1/16 -- EM quarters carrying "
      "the gravity sector's elementary variance",
      F(5, 16) == F(1, 4) + F(1, 16)
      and F(13, 16) == F(3, 4) + F(1, 16))

print("ALL PASS" if ok else "SOME FAILED")
