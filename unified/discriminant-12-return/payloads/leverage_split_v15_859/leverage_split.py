"""
The leverage split (2026-11-13, sandbox; Jeremy: "look at
the accel/decel parabolas as different leverage for our
force" -- filed at his direction).

A state is the crossing of two opposite-sign parabolas,
the pair (u, v) = (E + p, E - p) on the shell uv = m^2,
u = m e^{psi}, v = m e^{-psi}. A longitudinal force
(dp/dt = F, dE/dt = F beta, beta = p/E) slides the state
along its shell (v15.270). Its action divides between
the two parabolas as

  du = F (1 + beta) dt,   dv = -F (1 - beta) dt:

the accel parabola grows at the (1 + beta) rate while
the decel parabola shrinks at the (1 - beta) rate --
magnitudes in the ratio (1 + beta)/(1 - beta) = e^{2 psi}
= u/v, on the integer mesh the pair ratio n/k itself.
(Sign note: an earlier chat sketch wrote dv without the
minus; the psi-slide check below caught it -- v falls as
psi rises, dv = -v d psi, and the filed form is the
corrected one. Deceleration, F < 0, flips both signs:
u collapses at (1 + beta), v climbs at (1 - beta).)
The arms are u and v; the fulcrum is the invariant
product uv = m^2; the response shares |du| : |dv|
normalized are u/(u+v) and v/(u+v), i.e. arm over twice
the AM. At the seat (psi = 0) the leverage is 1, an even
reciprocal split; the lever redistributes at fixed
product and amplifies nothing.

Checks: (1) all identities symbolic on the shell;
(2) the force as a psi-slide, d psi = F dt / E (the
shell's energy is the inertia per unit rapidity), with
du = u d psi, dv = -v d psi -- the boost's reciprocal
action read channel-wise; (3) a transverse force has no
first-order action on (u, v) at all -- the lever is
purely longitudinal; (4) numeric spot checks including
the record's electron (E = 1 MeV, psi = 1.2917) and the
mesh pair ratio; (5) the same e^{2 psi} is the head-on
vs tail-on Doppler ratio. Scope: a response coefficient
(how a given force lands on the pair), the corridor's
transport species -- it supplies the drive x reaction
split (v15.275) with its psi-dependent channel weights,
and selects no force.
"""
import numpy as np
import sympy as sp

m, psi, F = sp.symbols("m psi F", positive=True)
E = m * sp.cosh(psi)
p = m * sp.sinh(psi)
u, v = E + p, E - p
beta = sp.simplify(p / E)
print(f"u = {sp.simplify(u)}, v = {sp.simplify(v)}, uv = {sp.simplify(u * v)}, beta = {beta}")
du = sp.simplify(F * (1 + beta)); dv = sp.simplify(F * (beta - 1))
print(f"du/dt = {du}, dv/dt = {dv}  (u grows, v shrinks, for F > 0)")
ratio = sp.simplify(du / (-dv))
ratio_exp = sp.simplify(ratio.rewrite(sp.exp))
print(f"magnitude ratio du/|dv| = {ratio_exp}; u/v = {sp.simplify(u / v)}; "
      f"equal to e^(2 psi): {sp.simplify(ratio_exp - sp.exp(2 * psi)) == 0}")
share_u = sp.simplify(du / (du - dv)); share_v = sp.simplify(-dv / (du - dv))
print(f"response shares: |du|/(|du|+|dv|) = {share_u} = u/(u+v) = {sp.simplify(u / (u + v))} "
      f"(equal: {sp.simplify(share_u - u / (u + v)) == 0}); "
      f"|dv| share = {share_v} = v/(u+v) (equal: {sp.simplify(share_v - v / (u + v)) == 0})")

# the force as a psi-slide: dp = E d psi on the shell
dpsi = F / E
print(f"\npsi-slide: d psi/dt = F/E (dp = E d psi on shell); "
      f"du = u d psi: {sp.simplify(u * dpsi)} vs du/dt above: "
      f"{sp.simplify(u * dpsi - du) == 0}; dv = -v d psi: "
      f"{sp.simplify(-v * dpsi - dv) == 0}")

# transverse force: no first-order action on (u, v)
eps = sp.symbols("eps")
p_par = p * sp.cos(eps); E_t = E  # rotation of p by eps at fixed |p|, E
u_t = sp.series(E_t + p_par, eps, 0, 2).removeO()
v_t = sp.series(E_t - p_par, eps, 0, 2).removeO()
print(f"\ntransverse (rotate p by eps, E fixed): u(eps) = {u_t}, v(eps) = {v_t} "
      f"to first order -- no linear term: the lever is longitudinal only")

print("\nspot checks (psi, beta, split ratio = e^{2 psi} = u/v):")
for ps in (0.0, 0.5, 1.0, 1.2917, 2.0, 3.0):
    b = np.tanh(ps)
    print(f"  psi = {ps:6.4f}: beta = {b:.4f}, (1+b)/(1-b) = {(1 + b) / (1 - b):10.4f}, "
          f"e^(2 psi) = {np.exp(2 * ps):10.4f}")
print("  record's electron at E = 1 MeV (psi = 1.2917): a longitudinal force's")
print("  impulse divides 13.24 : 1 between the accel and decel parabolas.")
print("  mesh pair (n, k): leverage = n/k directly (pair (36, 1): 36 : 1).")
print("  Doppler: head-on vs tail-on frequency ratio = e^{2 psi}, same number.")
