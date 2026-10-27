"""Build 3 scalar (P, Q) at FIXED numeric k (fast path: k substituted before solving).
Chain: simultaneous (Phi,B) elimination -> E1 algebraic in psi -> H -> chain rule ->
E2 -> (c2, P, Q). Elastic prediction: P = 3/t, Q = (3k^2+4)/t^2."""
import sympy as sp
exec(open("scalar_adm3.py").read())
dd = lambda f: sp.Derivative(f, t)
def EL(L, X):
    return sp.expand(sp.diff(L, X) - sp.diff(sp.diff(L, dd(X)), t))
for kv in [3]:
    L3 = L2b.subs({k: sp.Integer(kv), sp.Derivative(a, t): 1 / sp.sqrt(3), a: t / sp.sqrt(3)})
    L3 = sp.expand(L3.subs({C: 1, kap: 1}))
    sol = sp.solve([EL(L3, Phi), EL(L3, B)], (Phi, B), dict=True)[0]
    Lred = sp.expand(L3.subs(sol))
    E1, E2 = EL(Lred, psi), EL(Lred, pi)
    cpsi = sp.expand(E1).coeff(psi)
    H = sp.expand(-(E1 - cpsi * psi) / cpsi)
    pdd = sp.Derivative(pi, (t, 2))
    Hd = sp.expand(sp.diff(H, t) + sp.diff(H, pi) * dd(pi) + sp.diff(H, dd(pi)) * pdd)
    E2r = sp.expand(E2.subs({psi: H, dd(psi): Hd}))
    c2 = sp.simplify(E2r.coeff(pdd)); rem = sp.expand(E2r - c2 * pdd)
    c1 = sp.simplify(rem.coeff(dd(pi))); c0 = sp.simplify(sp.expand(rem - c1 * dd(pi)) / pi)
    P = sp.simplify(c1 / c2); Q = sp.simplify(c0 / c2)
    print(f"k^2={kv}: P = {P} | Q = {Q} | elastic Q = {(3*kv+4)}/t^2 | match = {sp.simplify(Q - (3*kv+4)/t**2) == 0}")
    print(f"   A_kin sign (A = -c2/2 at t=1): {sp.sign((-c2/2).subs(t, 1))}")
