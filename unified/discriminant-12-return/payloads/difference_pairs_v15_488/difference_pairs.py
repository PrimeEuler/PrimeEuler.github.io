"""
Difference of two point pairs on boost hyperbolas
(2026-11-06, sandbox; Jeremy: "what about the difference
between 2 parabolic point pairs on a boost hyperbola?").

A point pair: (u, v) = (m e^psi, m e^-psi) on uv = m^2
(T = m cosh psi, X = m sinh psi). For two pairs
(m1, psi1), (m2, psi2), dpsi = psi2 - psi1:

DIFFERENCE PAIR  D = (u2 - u1, v2 - v1). Its own pair
coordinates are (T_D, X_D) = (dT, dX): it IS the
displacement pair of the two points. Its product is
exact (verified numerically below, and in sympy up to
exp/cosh rewriting):
  (u2-u1)(v2-v1) = m1^2 + m2^2 - 2 m1 m2 cosh(dpsi)
                = the momentum-transfer invariant
                  (p1 - p2)^2 of the two states.
Same hyperbola (m1 = m2 = m): product = -4 m^2
sinh^2(dpsi/2) <= 0, and the components have OPPOSITE
signs (instance below: (+0.822, -0.451)) -- the
difference of two momentum pairs is a CROSSED pair, the
opposite-sign species: in the dynamics chain's own
construction, crossed pairs are the position-type pairs
(a state's position is the crossing of two opposite-sign
parabolas). Differencing changes species.

RATIO PAIR  R = (u2/u1, v2/v1) = ((m2/m1) e^dpsi,
(m2/m1) e^-dpsi): the mass-ratio shell's boost pair;
same shell it is the pure boost (e^dpsi, e^-dpsi) on
uv = 1 with T = cosh(dpsi).

SCOPE. The difference pair's invariant content is still
(m1, m2, dpsi): it contains no separation, so it does
NOT reopen the force-law scan's Level-1 no-go (v15.487)
-- a difference of addresses is a function of addresses.
What it does: it is the atom of the bilinear level
(v15.483): the kernel's band is a function of the
difference variable X = (N-M)/2, and momentum-space
interactions are universally functions of the transfer
-- whose pair form is exactly this difference pair, with
product t = (p1-p2)^2. Force in this framework, where it
legitimately lives, is a property of differences.
"""
import mpmath as mp

for (m1, p1, m2, p2) in [(1, 0.2, 2, -0.1), (0.5, 1.0, 3.0, 0.4),
                         (2.0, -0.7, 2.0, 0.9), (1.0, 0.0, 1.0, 0.6)]:
    u1, v1 = m1 * mp.e**p1, m1 * mp.e**(-p1)
    u2, v2 = m2 * mp.e**p2, m2 * mp.e**(-p2)
    lhs = (u2 - u1) * (v2 - v1)
    rhs = m1**2 + m2**2 - 2 * m1 * m2 * mp.cosh(p2 - p1)
    print(f"  m1={m1} m2={m2} dpsi={mp.nstr(p2-p1, 3)}: "
          f"diff pair = ({mp.nstr(u2-u1, 6)}, {mp.nstr(v2-v1, 6)}), "
          f"product = {mp.nstr(lhs, 8)}, transfer form = "
          f"{mp.nstr(rhs, 8)}, match = {abs(lhs - rhs) < 1e-12}")
print("  same-shell rows: components of opposite sign (crossed")
print("  pair), product = -4 m^2 sinh^2(dpsi/2) <= 0 (spacelike).")
print("  ratio pair (same shell): (e^dpsi, e^-dpsi), uv = 1,")
print("  T = cosh(dpsi) -- the pure relative boost.")
