"""Vector sector with FULL g^ij in the matter action: g^xx = h^xx - (N^x)^2/N^2.
Rebuild L2_vec, eliminate V, compare Q_V with elastic (3k^2+4)/t^2."""
import sympy as sp
exec(open("vector_adm.py").read())   # t,z,k,e,C,kap,a,V,pT,L2 (truncated g)
# patch the matter kin1: g^xx coefficient for (dx phi^1)^2 = 1 gets -Nx^2/hf^2 correction
# rebuild matter part only: recompute L2 from vector_adm internals is messy; instead
# add the missing term directly: dL = sqrt(-g)*(C/3)*(N^x)^2 * (dx phi^1)^2 averaged at O(e^2)
Nx = e * a * V * sk
hfv = a**2
Nxup = Nx / hfv                       # N^x
dL = (hfv**sp.Rational(3, 2)) * (C / 3) * Nxup**2 * 1   # (dx phi^1)^2 = 1, sign: -(C/3)*(-(Nx)^2) = +
dL2 = sp.expand(sp.series(sp.expand(dL), e, 0, 3).removeO()).coeff(e, 2)
dL2 = sp.simplify(sp.integrate(dL2, (z, 0, 2 * sp.pi / k)) * k / (2 * sp.pi))
print("missing matter term dL2 =", dL2)
L2f = sp.expand(L2 + dL2)
L2f = L2f.subs(sp.Derivative(a, t), 1 / sp.sqrt(3)).subs(a, t / sp.sqrt(3))
L2f = sp.expand(L2f.subs({C: 1, kap: 1}))
dd = lambda f: sp.Derivative(f, t)
ELV = sp.expand(sp.diff(L2f, V))
solV = sp.solve(ELV, V)[0]
print("V sol:", solV, "| residual:", sp.simplify(ELV.subs(V, solV)))
Lred = sp.expand(L2f.subs(V, solV))
A = sp.simplify(Lred.coeff(dd(pT)**2))
ELp = sp.expand(sp.diff(Lred, pT) - sp.diff(sp.diff(Lred, dd(pT)), t))
pdd = sp.Derivative(pT, (t, 2))
c2 = ELp.coeff(pdd); rem = sp.expand(ELp - c2 * pdd)
c1 = rem.coeff(dd(pT)); c0 = sp.simplify(sp.expand(rem - c1 * dd(pT)) / pT)
P = sp.simplify(c1 / c2); Q = sp.simplify(c0 / c2)
print("A_vec(fixed) =", A, "| A == -c2/2:", sp.simplify(A + c2 / 2) == 0)
print("P =", P, "| Q =", Q)
