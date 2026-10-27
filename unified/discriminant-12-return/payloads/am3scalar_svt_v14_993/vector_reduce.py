"""Vector reduction: eliminate V (algebraic) -> pT oscillator. Exact."""
import sympy as sp
exec(open('vector_adm.py').read())  # shares namespace: t,z,k,e,C,kap,a,V,pT,L2
L2 = L2.subs(sp.Derivative(a, t), 1 / sp.sqrt(3)).subs(a, t / sp.sqrt(3))
L2 = sp.expand(L2.subs({C: 1, kap: 1}))
dd = lambda f: sp.Derivative(f, t)
ELV = sp.expand(sp.diff(L2, V))
solV = sp.solve(ELV, V)[0]
print("V solution:", solV, "| residual:", sp.simplify(ELV.subs(V, solV)))
Lred = sp.expand(L2.subs(V, solV))
A = sp.simplify(Lred.coeff(dd(pT)**2))
print("kinetic coeff A_vec =", A)
ELp = sp.expand(sp.diff(Lred, pT) - sp.diff(sp.diff(Lred, dd(pT)), t))
pdd = sp.Derivative(pT, (t, 2))
c2 = ELp.coeff(pdd); rem = sp.expand(ELp - c2 * pdd)
c1 = rem.coeff(dd(pT)); c0 = sp.simplify(sp.expand(rem - c1 * dd(pT)) / pT)
P = sp.simplify(c1 / c2); Q = sp.simplify(c0 / c2)
Om2 = sp.simplify(Q - P**2 / 4 - sp.diff(P, t) / 2)
print("check A == -c2/2:", sp.simplify(A + c2 / 2) == 0)
print("P =", P, "| Q =", Q, "| Omega^2 =", Om2)
print("high-k Om2/(k^2/a^2):", sp.limit(Om2 / (3 * k**2 / t**2), k, sp.oo), "| k->0 Om2*t^2:", sp.limit(Om2 * t**2, k, 0))
with open('vector_final.txt', 'w') as f:
    f.write(f"A = {A}\nP = {P}\nQ = {Q}\nOm2 = {Om2}\nVsol = {solV}\n")
