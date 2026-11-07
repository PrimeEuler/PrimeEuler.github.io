"""
Phase-angle integration as a law source? (2026-11-06,
sandbox; Jeremy: "dont we get a position space law from
the lamour phase angle integration?")

"Phase angle integration" is the project's name for the
(Et - px)/hbar accumulation along trajectories -- the
cone's first proven dynamics (winding = quantization at
the hbar pin, v14.620; Jeremy 2026-10-22: the phase point
can ride any eccentricity on the cone). Question: does
integrating the phase over orbits OUTPUT a law?

The closed-orbit phase integral IS the action variable
J = (closed) int p dx. Its energy relation J(E) is a
FINGERPRINT of the trajectory family fed in:
  constant force (the cone's own parabolas / bouncer):
    J(E) = (4 sqrt2 / (3 a sqrt m)) E^{3/2}   (v15.469)
    -> E ~ J^{2/3}: the Airy comb (n - 1/4)^{2/3}.
  Kepler (the imported 1/r law):
    J_r + 2 pi L ~ (-E)^{-1/2}  ->  E ~ -(J)^{-2}.
TEST: compute both fingerprints numerically with the
SAME phase-integration machine. If the machine returns
whichever law's fingerprint it was fed, the direction of
flow is demonstrated: phase integration is law-CONSUMING
(it quantizes and keeps the books for a trajectory
family) -- it has never output the family. The cone's
native family is the parabolas, whose fingerprint is the
constant-force one (the 2/3 family of v15.469); Kepler's
fingerprint appears only when Kepler orbits -- the
imported law's trajectories -- are fed in. (The 2026-10
Larmor-orbit tests sit in the same posture: phase-
weighted orbit integration reproduced the lobes/
harmonics exactly -- position-space STRUCTURE from a
given orbit, recorded as an identity/consistency check,
not a law.)
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 30

print("=" * 76)
print("the phase integral J(E) for the cone's own family (constant force)")
print("=" * 76)
m_, a_ = mp.mpf(1), mp.mpf(1)
def J_bouncer(E):
    # int_0^{E/a} sqrt(2m(E - a x)) dx, closed orbit = 2x (up+down)
    return 2 * mp.quad(lambda x: mp.sqrt(2 * m_ * (E - a_ * x)),
                       [0, E / a_])
Es = [mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(4), mp.mpf(8)]
Js = [J_bouncer(E) for E in Es]
slope = np.polyfit([float(mp.log(E)) for E in Es],
                   [float(mp.log(J)) for J in Js], 1)[0]
print(f"  J(E) at E = 0.5..8: {[mp.nstr(J, 5) for J in Js]}")
print(f"  log-log slope d log J / d log E = {slope:.4f} "
      f"(constant-force fingerprint: 3/2 -> E ~ J^(2/3), the")
print("  Airy comb of v15.469: the law this family carries is the")
print("  uniform field -- the parabola's own.)")

print()
print("=" * 76)
print("the same machine fed Kepler orbits (the imported law's trajectories)")
print("=" * 76)
k_, L_ = mp.mpf(1), mp.mpf(1)
def J_radial_kepler(E):
    # turning points in closed form: r = (L^2/k)/(1 +- e),
    # e = sqrt(1 + 2 E L^2 / k^2); integrand clamped at the ends
    e = mp.sqrt(1 + 2 * E * L_**2 / k_**2)
    lo = (L_**2 / k_) / (1 + e)
    hi = (L_**2 / k_) / (1 - e)
    def f(r):
        arg = 2 * (E + k_ / r) - L_**2 / r**2
        return mp.sqrt(arg) if arg > 0 else mp.mpf(0)
    return 2 * mp.quad(f, [lo, hi])
EsK = [mp.mpf('-0.40'), mp.mpf('-0.25'), mp.mpf('-0.15'), mp.mpf('-0.08')]
tots = [J_radial_kepler(E) + 2 * mp.pi * L_ for E in EsK]
slopeK = np.polyfit([float(mp.log(-E)) for E in EsK],
                    [float(mp.log(t)) for t in tots], 1)[0]
print(f"  J_r + 2 pi L at E = -0.40..-0.08: {[mp.nstr(t, 5) for t in tots]}")
print(f"  log-log slope d log(J_tot) / d log(-E) = {slopeK:.4f} "
      f"(Kepler fingerprint: -1/2 -> E ~ -J^(-2).)")
print("  Kepler's fingerprint appears ONLY because Kepler orbits")
print("  were fed in. The machine returned the input law's")
print("  signature in both cases.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("No position-space law comes out of the phase-angle")
print("integration, and the two fingerprints show the exact")
print("reason: the closed-orbit phase integral is a READOUT")
print("of the trajectory family, not a source of it. Fed the")
print("cone's parabolas, it returns the constant-force")
print("fingerprint (E ~ J^{2/3}, the Airy/2-3 family -- real")
print("dynamics, and exactly the law the parabolas ARE the")
print("trajectories of). Fed Kepler ellipses, it returns")
print("Kepler's. The integration quantizes, keeps energy")
print("books (radiation reaction collecting the Larmor loss,")
print("v15.275), and manufactures position-space structure")
print("from given orbits (the Larmor lobes, 2026-10) -- all")
print("law-consuming operations. A law would have to select")
print("the family; the phase integral presupposes it. This")
print("is the same input/output direction as the Kepler")
print("audit (v15.277) and the force-law scan (v15.487), now")
print("exhibited at the level of the cone's first dynamical")
print("mechanism itself.")
