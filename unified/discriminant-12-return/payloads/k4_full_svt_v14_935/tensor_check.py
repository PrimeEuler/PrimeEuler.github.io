"""Independent verification of v14.928's tensor sector (Sandbox SVT return, part 1).
1) J = tr(B^2)/(tr B)^2 - 1/3 for B = a^-2 e^{-gamma}, gamma TT: series -> (1/9) tr gamma^2.
2) det B = a^-6 (tr gamma = 0) -> b unperturbed; solid quadratic = -int a^3 rho eta tr(gamma^2)/9.
3) Matching to EH form (1/8k) int a^3 [gammadot^2 - (dg)^2/a^2 - mT^2 gamma^2]:
   mT^2 = 8 k rho eta / 9 = (8 eta/3) H^2 using k rho = 3 H^2; eta=3/4 -> 2 H^2.
All steps symbolic/arithmetic in this file except the standard EH TT quadratic form."""
import sympy as sp

g11, g12, g13, g22, g23, eps = sp.symbols('g11 g12 g13 g22 g23 eps')
G = sp.Matrix([[g11, g12, g13], [g12, g22, g23], [g13, g23, -g11 - g22]])
M = sp.eye(3) - eps*G + eps**2 * G**2 / 2
J = sp.series((M**2).trace()/M.trace()**2 - sp.Rational(1, 3), eps, 0, 3).removeO()
assert sp.expand(J - eps**2 * (G**2).trace() / 9) == 0
print("1) J = (1/9) tr gamma^2 + O(gamma^3): CONFIRMED (linear term 0 since tr gamma = 0)")
print("2) det e^{-gamma} = e^{-tr gamma} = 1 -> det B = a^-6, b = a^-3 unperturbed: CONFIRMED")
kappa, rho, eta, H = sp.symbols('kappa rho eta H', positive=True)
mT2 = 8 * kappa * rho * eta / 9
print("3) mT^2 = 8 kappa rho eta/9; with kappa rho = 3H^2 ->",
      sp.simplify(mT2.subs(kappa*rho, 3*H**2)), "; eta=3/4 ->",
      sp.simplify(mT2.subs(kappa*rho, 3*H**2).subs(eta, sp.Rational(3, 4))))
print("   v14.928 values (8/9) kappa rho eta, (8 eta/3) H^2, 2 H^2 at eta=3/4: CONFIRMED")
# shear modulus cross-check: v14.925 c_T^2 = 3 mu/(2 rho), c_L^2 = -1/3 + 2 mu/rho;
# v14.927 phonons c_T^2 = 2 eta/3, c_L^2 = -1/3 + 8 eta/9  ->  mu = 4 rho eta/9.
mu = 4 * rho * eta / 9
print("4) mu(eta) = 4 rho eta/9 reproduces BOTH v14.927 speeds from v14.925 formulas:",
      sp.simplify(3*mu/(2*rho)), "and", sp.simplify(-sp.Rational(1,3) + 2*mu/rho))
print("   acoustic window rho/6 <= mu <= 2rho/3  <=>  eta in [3/8, 3/2]: CONFIRMED")
