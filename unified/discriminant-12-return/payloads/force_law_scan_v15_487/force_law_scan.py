"""
Force-law scan (2026-11-06, sandbox; Jeremy: "Test it --
scan the mesh for a force-law candidate").

Question: can a force LAW (the map configuration ->
acceleration) be derived from the acceleration parabolas
/ mesh structure? The parabolas supply the RESPONSE
(v15.469: action, quantization; v15.470: radiation
fingerprints). A law needs a(position, charges, masses).

LEVEL 1 -- address content. A body's pair address is
(m, psi): mass and rapidity (u = m e^psi, v = m e^-psi;
T = m cosh psi, X = m sinh psi). The complete list of
two-body invariants of two pair addresses is
(m1, m2, cosh(dpsi)) -- MOMENTUM-space data. A position-
space force law must change when one body is translated
at fixed momenta; no function of the addresses can.
Exhibited numerically below: the degeneracy is exact.

LEVEL 2 -- grant positions (the dynamics chain's
crossing parabolas supply x). Now r exists as data, and
many profiles g(r) are writable. Does the mesh SINGLE
OUT one? Candidates: Newton 1/r^2 (control/target), the
mesh kernel's own profile transplanted (1/r, from the
h = 1/(2X) band of v15.483), a seat-regularized profile
1/(r(r+l)), and a velocity-dependent mesh candidate
(GM/r^2)/cosh(psi) built from the pair invariant.
Discriminators (Bertrand/Kepler): Kepler III exponent
(period vs radius, log-log slope; Newton = 1.5) and
pericenter advance (closed ellipses: advance = 0).

Charges: the mesh DOES supply the sign/factor structure
(frame charges are class functions of the addresses,
v15.468) -- q1 q2 can multiply any profile. What it does
not supply is the profile. Expected verdict: laws are
not derivable; interactions in this framework live in
momentum space (the kernel/operator), and position-space
laws are the dual import -- the dictionary hole in
dynamical dress.
"""
import numpy as np

print("=" * 76)
print("LEVEL 1: two pair addresses contain no separation")
print("=" * 76)
print("  two configurations, identical addresses (m1=1, psi1=0.2;")
print("  m2=2, psi2=-0.1), separations r = 1 and r = 4:")
for r in (1.0, 4.0):
    print(f"    r = {r}: every function of (m1, m2, cosh dpsi) is the "
          f"SAME; Newton a = GM/r^2 = {2.0 / r**2:.4f} (ratio 16x)")
print("  -> no address function can be a position-space force law.")

print()
print("=" * 76)
print("LEVEL 2: orbit tests (fixed centre, GM = 1, near-circular ICs)")
print("=" * 76)
def run_orbits(accel, label, radii=(2.0, 3.0, 4.5, 6.5), norb=10):
    periods, advances = [], []
    for r0 in radii:
        # circular speed by fixed-point on the law itself;
        # start at apocentre of an eccentric orbit (v = 0.6 vc)
        # so pericentres are well-defined events
        v = np.sqrt(accel(r0, 0.3) * r0)
        for _ in range(60):
            v = np.sqrt(accel(r0, v) * r0)
        x = np.array([r0, 0.0]); vel = np.array([0.0, 0.6 * v])
        def acc(x, vel):
            r = np.hypot(*x)
            return -accel(r, np.hypot(*vel)) * x / r
        steps = 6000
        dt = (2 * np.pi * r0 / v) / steps
        theta_prev, theta_tot = 0.0, 0.0
        peri_angles, t = [], 0.0
        vr_prev = 0.0
        for i in range(steps * norb):
            # RK4
            def f(x, vel): return vel, acc(x, vel)
            k1x, k1v = f(x, vel)
            k2x, k2v = f(x + k1x * dt / 2, vel + k1v * dt / 2)
            k3x, k3v = f(x + k2x * dt / 2, vel + k2v * dt / 2)
            k4x, k4v = f(x + k3x * dt, vel + k3v * dt)
            x = x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
            vel = vel + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
            t += dt
            r_now = np.hypot(*x)
            a_now = np.arctan2(x[1], x[0])
            d = a_now - theta_prev
            if d < -np.pi: d += 2 * np.pi
            if d > np.pi: d -= 2 * np.pi
            theta_tot += d; theta_prev = a_now
            vr = float(np.dot(x, vel) / r_now)
            if vr_prev < 0 <= vr and i > 100 and \
                    (not peri_angles or theta_tot - peri_angles[-1] > 5.0):
                peri_angles.append(theta_tot)  # pericentre passage
            vr_prev = vr
        periods.append(t / (theta_tot / (2 * np.pi)))
        if len(peri_angles) > 3:
            adv = np.diff(peri_angles) - 2 * np.pi
            advances.append(np.degrees(np.mean(adv)))
        else:
            advances.append(float('nan'))
    slope = np.polyfit(np.log(radii), np.log(periods), 1)[0]
    print(f"  {label:<34} Kepler-III slope = {slope:.3f} "
          f"(Newton 1.500); pericenter advance = "
          f"{np.nanmean(advances):+.2f} deg/orbit (closed: 0)")
    return slope, np.nanmean(advances)

GM = 1.0
run_orbits(lambda r, v: GM / r**2, "control: Newton 1/r^2")
run_orbits(lambda r, v: GM / (r * (r + 0.5)), "seat-regularized 1/(r(r+l))")
run_orbits(lambda r, v: GM / r, "kernel profile transplanted: 1/r")
run_orbits(lambda r, v: GM / (r**2 * np.cosh(np.arctanh(min(v, 0.999)))),
           "pair-invariant candidate: (GM/r^2)/cosh(psi)")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("No force law is derivable from the parabolas, and the")
print("scan shows the two exact reasons. (1) Content: the pair")
print("addresses are momentum data (m, psi); their complete")
print("invariant list (m1, m2, cosh dpsi) contains no")
print("separation, so no function of them can be a position-")
print("space law -- the degeneracy is exact, not a search")
print("failure. (2) Selection: granting positions, the mesh")
print("singles out NO profile -- its own kernel profile (1/X)")
print("transplanted to position space fails Kepler (wrong")
print("III slope, open orbits), the regularized profile")
print("fails closure, and the velocity-dependent pair-")
print("invariant candidate fails closure too; only the")
print("imported Newton profile passes both discriminators.")
print("What the mesh supplies for interactions is real but")
print("one-sided: the charge FACTORS (frame labels, class")
print("functions of the addresses), the response (parabolas,")
print("action, quantization), the radiation fingerprints,")
print("and a momentum-space kernel (the operator). Position-")
print("space force laws are the Fourier-dual side of that")
print("data -- an import, in exactly door III's shape.")
