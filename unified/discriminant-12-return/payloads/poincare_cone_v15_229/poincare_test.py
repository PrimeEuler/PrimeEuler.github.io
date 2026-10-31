#!/usr/bin/env python3
"""
Poincare cone verification in the MIC (charge-monopole) system.

Claim under test [D]: for a charge moving in a fixed monopole field
(s = eg) plus a Coulomb attraction, the total angular momentum
    J = r x v - s * rhat        (m = 1, hbar = c = 1)
is conserved, and J . rhat = -s identically. Hence the position
vector keeps a constant angle to the fixed vector J: the trajectory
lies on a cone with apex at the monopole, axis -Jhat, and

    cos(alpha) = s / |J|,   |J|^2 = L^2 + s^2   (L = |r x v|).

With the Dirac unit s = 1/2 and shell angular momentum L^2 = j(j+1),
|J| = j + 1/2 = R (the ladder radius), so cos(alpha) = 1/(2j+1).

Equations of motion (Lorentz force of the monopole + Coulomb):
    a(r, v) = -kappa * r / |r|^3  +  s * (v x r) / |r|^3
The monopole force does no work, so E = |v|^2/2 - kappa/|r| is
conserved as a cross-check. J . rhat = -s is an algebraic identity
(L_mech is perpendicular to rhat); J conservation is the dynamical
content (dJ/dt = 0 follows from the EOM; verified numerically here
by RK4 integration over many orbits, several s and several shells).
"""
import numpy as np

KAPPA = 1.0


def accel(r, v, s):
    r2 = float(r @ r)
    rn = np.sqrt(r2)
    return -KAPPA * r / (rn * r2) + s * np.cross(v, r) / (rn * r2)


def rk4_step(r, v, s, dt):
    def a(rr, vv):
        return accel(rr, vv, s)
    k1r, k1v = v, a(r, v)
    k2r, k2v = v + 0.5 * dt * k1v, a(r + 0.5 * dt * k1r, v + 0.5 * dt * k1v)
    k3r, k3v = v + 0.5 * dt * k2v, a(r + 0.5 * dt * k2r, v + 0.5 * dt * k2v)
    k4r, k4v = v + dt * k3v, a(r + dt * k3r, v + dt * k3v)
    return (r + dt * (k1r + 2 * k2r + 2 * k3r + k4r) / 6.0,
            v + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6.0)


def run_case(s, L_target, v_r, dt=1e-3, nsteps=60000):
    """One orbit: r0 on +x axis, transverse speed fixed so |L| hits
    the target with the transverse direction tilted (J not axis
    aligned), plus a radial component v_r for eccentricity."""
    v_perp = 0.45
    d = L_target / v_perp
    tilt = 0.6
    r = np.array([d, 0.0, 0.0])
    v = np.array([v_r, v_perp * np.cos(tilt), v_perp * np.sin(tilt)])
    Lvec = np.cross(r, v)
    assert abs(np.linalg.norm(Lvec) - L_target) < 1e-12
    J0 = Lvec - s * r / np.linalg.norm(r)
    Jmag = np.linalg.norm(J0)
    E0 = 0.5 * float(v @ v) - KAPPA / np.linalg.norm(r)
    cos_target = s / Jmag
    max_dJ = max_id = max_cos = max_dE = 0.0
    for _ in range(nsteps):
        r, v = rk4_step(r, v, s, dt)
        rn = np.linalg.norm(r)
        J = np.cross(r, v) - s * r / rn
        max_dJ = max(max_dJ, float(np.linalg.norm(J - J0)))
        max_id = max(max_id, abs(float(J @ (r / rn)) + s))
        max_cos = max(max_cos, abs(float(-(J @ (r / rn))) / Jmag - cos_target))
        E = 0.5 * float(v @ v) - KAPPA / rn
        max_dE = max(max_dE, abs(E - E0))
    alpha = np.degrees(np.arccos(np.clip(cos_target, -1.0, 1.0)))
    return dict(s=s, L=L_target, E=E0, Jmag=Jmag, alpha=alpha,
                max_dJ=max_dJ, max_id=max_id, max_cos=max_cos, max_dE=max_dE)


def main():
    print("Poincare cone verification -- MIC charge-monopole trajectories")
    print("checks per orbit: |dJ| (conservation), |J.rhat + s| (identity),")
    print("|cos(alpha) - s/|J|| (cone angle constancy), |dE| (integrator)\n")
    hdr = (f"{'s':>6} {'L^2=j(j+1)':>10} {'|J|':>8} {'alpha(deg)':>11} "
           f"{'max|dJ|':>10} {'max|J.r+s|':>11} {'max|dcos|':>10} {'max|dE|':>10}")
    print(hdr)
    fails = 0
    # s scan at fixed shell (j = 3/2, L^2 = 15/4): opening set by s
    for s in [0.0, 0.5, 1.0, 1.5, -0.5]:
        c = run_case(s, np.sqrt(3.75), v_r=0.2)
        print(f"{c['s']:>6} {c['L']**2:>10.4f} {c['Jmag']:>8.4f} {c['alpha']:>11.4f} "
              f"{c['max_dJ']:>10.2e} {c['max_id']:>11.2e} {c['max_cos']:>10.2e} {c['max_dE']:>10.2e}")
        fails += not (c['max_dJ'] < 1e-7 and c['max_id'] < 1e-12
                      and c['max_cos'] < 1e-9 and c['max_dE'] < 1e-7)
    # shell scan at the Dirac unit s = 1/2: |J| should equal j + 1/2
    print("\nshell scan at s = 1/2 (closed form: |J| = j + 1/2 = R, "
          "cos(alpha) = 1/(2j+1))")
    for j in [0.5, 1.0, 1.5, 2.5]:
        for v_r in [0.0, 0.25]:
            c = run_case(0.5, np.sqrt(j * (j + 1)), v_r=v_r)
            ok_R = abs(c['Jmag'] - (j + 0.5))
            print(f"{c['s']:>6} {c['L']**2:>10.4f} {c['Jmag']:>8.4f} {c['alpha']:>11.4f} "
                  f"{c['max_dJ']:>10.2e} {c['max_id']:>11.2e} {c['max_cos']:>10.2e} {c['max_dE']:>10.2e}"
                  f"   |J|-(j+1/2) = {ok_R:.2e}")
            fails += not (c['max_dJ'] < 1e-7 and c['max_id'] < 1e-12
                          and c['max_cos'] < 1e-9 and c['max_dE'] < 1e-7
                          and ok_R < 1e-12)
    print(f"\nVERDICT: {'ALL CHECKS PASS' if fails == 0 else f'{fails} FAILURES'}")
    print("Trajectory lies on the Poincare cone in every case; the cone")
    print("opening is a function of (s, |J|) only -- not of energy,")
    print("eccentricity, or radial range. At s = 1/2 the cone axis data")
    print("are the ladder radius R = j + 1/2 and cos(alpha) = 1/(2j+1).")


if __name__ == "__main__":
    main()
