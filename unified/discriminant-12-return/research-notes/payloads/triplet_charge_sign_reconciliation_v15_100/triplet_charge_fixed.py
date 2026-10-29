"""Build the triplet-carrying configuration the Wald loophole requires, and test it.
Configuration: rotating labels phi^I(t, z) = R^I_J(omega t) z^J on the coasting background
(R = rotation about the 3-axis). The record's backgrounds all had time-independent labels,
so the action's B was never disambiguated: (R1) spatial strain B = a^-2 F F^T (elastic reading),
(R2) full contraction B = g^mn d_m phi d_n phi. The test forces the fork; compute both."""
import sympy as sp

t, w, a = sp.symbols('t omega a', positive=True)
z1, z2, z3 = sp.symbols('z1 z2 z3', real=True)
R = sp.Matrix([[sp.cos(w * t), -sp.sin(w * t), 0],
               [sp.sin(w * t), sp.cos(w * t), 0],
               [0, 0, 1]])
z = sp.Matrix([z1, z2, z3])
phi = R * z
F = R  # spatial Jacobian d phi^I / d z^i = R^I_i (orthogonal)
B1 = (F * F.T) / a**2
print("R1 (spatial B): B =", sp.simplify(B1), " -> A_B = tr B/3 =", sp.simplify(sp.trace(B1) / 3), ": rotation INVISIBLE to W (singular values of R are 1)")
print("   canonical momentum pi_I = dL/d(phidot^I) = 0 (W has no phidot) -> Noether charge density J^t = pi_I * delta phi^I = 0 EXACTLY:")
print("   the internal rotation is a flat direction carrying NO charge density (spatial current only).")

phidot = sp.diff(phi, t)
B2tr = sp.simplify(sum(phidot[i]**2 for i in range(3)) - sp.trace(F * F.T) / a**2)  # tr of full-contraction B, signature (+,-,-,-)
# A_B = -tr B / 3, NOT tr B / 3: matched to the static normalization (omega=0 must give A_B = 1/a^2, as in R1),
# and consistent with pi_I = (2C/3) phidot_I from L = -C A_B below. (Sign reconciliation of Audit R389 / v15.051.)
print("\nR2 (full B): tr B =", B2tr, " -> A_B = -tr B/3 =", sp.simplify(-B2tr / 3))
# Noether charge density for rotation about 3-axis under R2: pi_I = (2C/3) phidot_I (from L = -C A_B), q3 = sum_I pi_I (eps_{IJ3} phi^J)
C = sp.symbols('C', positive=True)
dphi = sp.Matrix([-phi[1], phi[0], 0])        # delta phi for alpha = z-hat: eps_{IJ3} phi^J
q3 = sp.simplify(sum((2 * C / 3) * phidot[i] * dphi[i] for i in range(3)))
print("   internal charge density q3 =", q3, " -> proportional to C * omega * (distance to axis)^2: a MOMENT density,")
print("   extensive over any ball (integral ~ C omega R^5), and omega, R are state data: quantization of a total")
print("   charge would pin C x (state), not C. On the homogeneous cosmology there is no finite total at all.")

print("\nDerrick check (finite lump, pure-gradient W): profile phi(z/lam): A_B -> A_B/lam^2, volume -> lam^3,")
print("   E(lam) = lam * E(1): monotone -- no finite-size soliton; and W has no potential term, so no Q-ball either.")
