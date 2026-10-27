"""Scalar sector: DEFINITIVE reduction via {E1, E1', E2} linear solve (function-object
substitutions only), exact peeling, residuals vs the ORIGINAL L2 equations."""
import sympy as sp
exec(open("scalar_adm.py").read())
L2 = L2.subs(sp.Derivative(a, t), 1 / sp.sqrt(3)).subs(a, t / sp.sqrt(3))
L2 = sp.expand(L2.subs({C: 1, kap: 1}))
dd = lambda f: sp.Derivative(f, t)
def EL(L, X):
    return sp.expand(sp.diff(L, X) - sp.diff(sp.diff(L, dd(X)), t))
EB0, EP0 = EL(L2, B), EL(L2, Phi)
solPhi = sp.solve(EB0, Phi)[0]
solB = sp.solve(sp.expand(EP0.subs(Phi, solPhi)), B)[0]
PhiS = sp.expand(solPhi.subs(B, solB))
Lred = sp.expand(L2.subs({Phi: PhiS, B: solB}))
E1 = EL(Lred, psi); E2 = EL(Lred, pi)
E1p = sp.expand(sp.diff(E1, t))
solpsi = sp.solve(E1, psi)[0]
solpsid = sp.expand(sp.solve(E1p, dd(psi))[0].subs(psi, solpsi))
E2f = sp.expand(E2.subs({psi: solpsi, dd(psi): solpsid}))
pdd = sp.Derivative(pi, (t, 2)); pd_ = dd(pi)
c2 = E2f.coeff(pdd); rem = sp.expand(E2f - c2 * pdd)
c1 = rem.coeff(pd_); rem2 = sp.expand(rem - c1 * pd_)
c0 = sp.simplify(rem2 / pi); assert sp.simplify(rem2 - c0 * pi) == 0, "peel failed"
c2, c1 = sp.simplify(c2), sp.simplify(c1)
P = sp.simplify(c1 / c2); Q = sp.simplify(c0 / c2)
Om2 = sp.simplify(Q - P**2 / 4 - sp.diff(P, t) / 2)
print("c2 =", c2, "  [= -2A_kin]")
print("P =", P); print("Q =", Q)
print("Omega^2 =", sp.factor(sp.together(Om2)))
print("high-k Om2/(k^2/a^2):", sp.limit(Om2 / (3 * k**2 / t**2), k, sp.oo))
print("k->0: Om2*t^2:", sp.limit(Om2 * t**2, k, 0), " P*t:", sp.limit(P * t, k, 0))
# residuals: original EL_Phi, EL_B on the reconstruction (pi_ddot replaced via reduced eq)
pdd_sol = -P * pd_ - Q * pi
recon = {Phi: PhiS.subs({psi: solpsi, dd(psi): solpsid, dd(pi): pd_}).subs(pdd, pdd_sol),
         B: solB.subs(dd(pi), pd_)}
# PhiS/B contain psi, psi_dot, pi, pi_dot (checked by census); substitute psi, psi_dot, then pi_ddot
def full_sub(expr):
    e = expr.subs({psi: solpsi, dd(psi): solpsid})
    e = sp.expand(e).subs(pdd, pdd_sol)
    return sp.simplify(e)
print("residual EL_B(orig) on recon:", full_sub(EB0.subs({Phi: PhiS.subs({psi: solpsi, dd(psi): solpsid}), B: solB})))
print("residual EL_Phi(orig) on recon:", full_sub(EP0.subs({Phi: PhiS.subs({psi: solpsi, dd(psi): solpsid}), B: solB})))
print("residual E1:", sp.simplify(E1.subs(psi, solpsi)), "| E2f is the reduced eq by construction")
fv = sp.lambdify(k, sp.together(Om2).subs(t, 1), 'numpy')
fp = sp.lambdify(k, (P * t).subs(t, 1), 'numpy')
for kv in [0.05, 0.2, 0.4, 0.5, 0.5774, 0.7, 1.0, 1.1547, 1.3, 1.5, 3.0]:
    print(f"  k={kv:6.4f}  Om2*t^2={fv(kv):+10.4f}   P*t={fp(kv):+8.4f}")
with open('scalar_final.txt', 'w') as f:
    f.write(f"c2 = {c2}\nP = {P}\nQ = {Q}\nOm2 = {Om2}\npsi_sol = {solpsi}\npsid_sol = {solpsid}\n")
