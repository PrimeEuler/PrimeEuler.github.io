"""Spinor-source test: homogeneous pair spinor chi (v14.990 action
S = int sqrt(-g)[(1/2)|d chi|^2 - V(|chi|)], minimal coupling) on flat FLRW.
Coasting target: a = tau/sqrt(3), i.e. rho_chi = 1/(kappa a^2), w = -1/3.
Homogeneous: chi = r(tau) e^{i theta(tau)}; comoving charge a^3 r^2 theta' = Q;
K = (rdot^2 + r^2 thetadot^2)/2; rho = K + V, p = K - V; w = -1/3 iff V = 2K."""
import sympy as sp

tau, a, r, Q, kap, lam, c = sp.symbols('tau a r Q kappa lambda c', positive=True)

print("A. w = -1/3 condition: (K - V)/(K + V) = -1/3  <=>  V = 2K  [algebra: 3K-3V = -K-V -> 4K = 2V] OK")
print("   r = r0 const, Q != 0: K = Q^2/(2 a^6 r0^2) ~ a^-6, V const -> rho never ~ a^-2: NO COASTING")

print("\nB. Exact scaling r ~ a^-beta: (1/2) rdot^2 = (beta^2/2) H^2 r^2 ~ a^(-2-2beta) needs beta = 0;")
print("   charge term Q^2/(2 a^6 r^2) ~ a^(-6+2beta) needs beta = 2. Incompatible for Q != 0:")
print("   NO exact charged power-law coasting for any V(r). (Q = 0 escapes via r ~ ln tau, not a power.)")

print("\nC. Q = 0: theta frozen, spinor = one real canonical scalar. Tracker ansatz a = tau/sqrt(3),")
# conditions from exponent/coefficient matching (stated, then the claimed solution is VERIFIED):
# V ~ tau^-2 needs mu*A = 2; K = A^2/(2 tau^2) = 1/tau^2 needs A = sqrt(2) (kappa=1) -> mu = sqrt(2).
V0, B = sp.symbols('V0 B', positive=True)
rr = sp.sqrt(2) * sp.log(tau) + B
K = sp.Rational(1, 2) * sp.diff(rr, tau)**2
Vv = V0 * sp.exp(-sp.sqrt(2) * rr)
Vv = sp.simplify(Vv.subs(V0, 2 * sp.exp(sp.sqrt(2) * B)))   # amplitude condition V0 e^{-mu B} = 2
H = 1 / tau; aa = tau / sp.sqrt(3)
kg = sp.simplify(sp.diff(rr, tau, 2) + 3 * H * sp.diff(rr, tau) - sp.sqrt(2) * Vv)  # r'' + 3H r' + V'(r), V' = -sqrt(2) V
print("   verify A = sqrt(2), mu = sqrt(2): K =", sp.simplify(K), "| V =", sp.simplify(Vv), "| rho = K + V =", sp.simplify(K + Vv), "(need 3/tau^2)")
print("   Klein-Gordon residual on a = tau/sqrt(3):", kg, " -> exponential tracker is an exact solution; v14.959 recovered, charge = 0")

print("\nE. Charge-dominated asymptotic branch r = c/a^2: r thetadot^2 = Q^2/(a^6 r^3) =", sp.simplify(Q**2 / (a**6 * (c / a**2)**3)), "(const)")
print("   r-equation on the ansatz: a^3 rdot = -2c/sqrt(3) = const, so need V'(r) = Q^2/c^3 -> V linear, slope lam = Q^2/c^3 (state-tuned).")
print("   rho = K + V with (1/2) rdot^2 = 2c^2/(3 a^6): rho = 3Q^2/(2 c^2 a^2) + 2c^2/(3 a^6): Friedmann amplitude needs 3Q^2/(2c^2) = 1/kappa,")
Qstar = ((2 / (3 * kap))**sp.Rational(3, 4)) * lam**(-sp.Rational(1, 2))
print("   i.e. for FIXED theory (lam, kappa) the charge is forced to Q* =", Qstar, "-- codimension-1 in the state;")
print("   and exactness still fails at O(a^-6) in rho (the rdot^2 piece): asymptotic only.")

print("\nF. Angular (phase) perturbation mass^2 = V'(r)/r [|chi| = r + dpar + dperp^2/(2r)]:")
print("   exponential branch: V'/r = -mu V/r < 0 TACHYONIC, |m^2|/H^2 = 2 mu/(kappa r(tau)) -> 0 like 1/ln tau (mild, sub-power-law growth e^{2 sqrt(ln tau)}); radial V'' = mu^2 V > 0; kinetic canonical, c_s^2 = 1.")
print("   linear branch: V'/r = lam/r > 0, m^2/H^2 = 3 lam a^4/c -> grows: healthy sign, heavy.")
print("\nG. Charge density q_chi = Q/a^3 (exact conservation under minimal coupling, any V(r));")
print("   energy footprint of the charge ~ a^-6 vs source rho ~ a^-2: q_chi/rho ~ a^-1 -> 0. Decouples.")
