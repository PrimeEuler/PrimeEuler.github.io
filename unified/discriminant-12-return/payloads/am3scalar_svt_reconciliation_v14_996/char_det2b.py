"""Characteristic determinant, done carefully: per EL equation, coefficients of
(qdd, qd, q) are monomials t^(s+2), t^(s+1), t^s. Build M(m) with entries
a m(m-1) + b m + c at fixed numeric k; roots = mode exponents of the UNREDUCED
system. Muse v14.993 scalar prediction k^2=1: m = -1 +- sqrt(14) ~ {2.74, -4.74};
elastic eta=3/2: m = -1 +- i sqrt(6)."""
import sympy as sp
exec(open("scalar_adm2.py").read())
L2s = L2b.subs(sp.Derivative(a, t), 1 / sp.sqrt(3)).subs(a, t / sp.sqrt(3))
L2s = sp.expand(L2s.subs({C: 1, kap: 1}))
dd = lambda f: sp.Derivative(f, t)
def EL(L, X):
    return sp.expand(sp.diff(L, X) - sp.diff(sp.diff(L, dd(X)), t))
fields = [Phi, B, psi, pi]
eqs = [EL(L2s, X) for X in fields]
m = sp.symbols('m')
def tpow(expr):
    expr = sp.expand(expr)
    if expr == 0: return None
    pows = set()
    for term in expr.as_ordered_terms():
        p = sp.Poly(term, t)
        pows.add(p.degree() if p else 0)
    assert len(pows) == 1, f"non-monomial coefficient: {expr}"
    return pows.pop()
for kv in [1, 2]:
    M = sp.zeros(4, 4)
    for i, e in enumerate(eqs):
        e = e.subs(k, sp.Integer(kv))
        coefs = []
        for src, shift in [(2, 2), (1, 1), (0, 0)]:
            row = []
            for f in fields:
                obj = sp.Derivative(f, (t, 2)) if src == 2 else (dd(f) if src == 1 else f)
                row.append(sp.expand(e).coeff(obj))
            coefs.append(row)
        s = None
        for j in range(4):
            p = tpow(coefs[2][j])
            if p is not None: s = p; break
        for j in range(4):
            a_ = sp.simplify(coefs[0][j] / t**(s + 2)) if coefs[0][j] != 0 else sp.Integer(0)
            b_ = sp.simplify(coefs[1][j] / t**(s + 1)) if coefs[1][j] != 0 else sp.Integer(0)
            c_ = sp.simplify(coefs[2][j] / t**s) if coefs[2][j] != 0 else sp.Integer(0)
            assert not a_.has(t) and not b_.has(t) and not c_.has(t), (i, j, a_, b_, c_)
            M[i, j] = a_ * m * (m - 1) + b_ * m + c_
    det = sp.factor(M.det())
    print(f"k^2={kv}: det(m) proportional to {det}")
    print("   roots:", [complex(r) for r in sp.nroots(sp.Poly(det, m))])
