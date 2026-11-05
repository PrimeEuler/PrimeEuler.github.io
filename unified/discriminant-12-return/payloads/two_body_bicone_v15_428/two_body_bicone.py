"""
Two-body bicone-dipole sandbox simulation (2026-11-02).

Model (dimensionless, planar, HONEST scope):
  - Two equal masses, each carrying a rigid dipole along its bicone axis n_i.
  - Interaction energy depends ONLY on the relative position r = r2 - r1
    and the two axis angles theta_i:
        U = -K / r  +  Cdd / r^3 * [ n1.n2 - 3 (n1.e)(n2.e) ],   e = r/r
    First term: central monopole attraction (keeps the pair bound; baseline).
    Second term: textbook dipole-dipole interaction (the new ingredient:
    each body's force/torque is SOURCED by the other body -- this is the
    'interaction' step past the single-particle v15.270-v15.282 chain).
  - Translation:  m r_i'' = F_i,  F1 = -F2 (U depends only on r).
  - Rotation:     I theta_i'' = tau_i = -dU/dtheta_i  (rigid bicone axis).
  - NOT claimed: this is classical dipole physics imported into the pair
    language, not a force law derived from the cone. The question under test
    is narrower: once a is sourced by the other body, how does each body's
    instantaneous acceleration parabola (v t + 1/2 a t^2) reorient over time,
    and does the dipole term measurably bend a AWAY from the line of centres?

Runs:
  A) monopole only (Cdd = 0): control. Acceleration must point exactly along
     the line of centres at all times (deviation = 0 to integrator accuracy).
  B) monopole + dipole: deviation angle delta(t), axis precession, separation.

Checks printed: total energy drift, total linear momentum drift,
total angular momentum (orbital + spin) drift.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------- parameters ----------
M = 1.0          # each mass
I_ROT = 0.2      # moment of inertia of each bicone axis
K = 1.0          # monopole strength
SEED_R = 2.0     # initial separation

def make_rhs(Cdd):
    def rhs(t, y):
        r1 = y[0:2]; r2 = y[2:4]; v1 = y[4:6]; v2 = y[6:8]
        th1, th2, om1, om2 = y[8], y[9], y[10], y[11]
        rv = r2 - r1
        r = np.linalg.norm(rv); e = rv / r
        n1 = np.array([np.cos(th1), np.sin(th1)])
        n2 = np.array([np.cos(th2), np.sin(th2)])
        n1p = np.array([-np.sin(th1), np.cos(th1)])  # dn1/dth1
        n2p = np.array([-np.sin(th2), np.cos(th2)])
        a_ = n1 @ e; b_ = n2 @ e
        f = (n1 @ n2) - 3.0 * a_ * b_
        # grad of U wrt rv (= dU/dr2)
        grad = K * e / r**2
        if Cdd != 0.0:
            bracket = b_ * n1 + a_ * n2 - 2.0 * a_ * b_ * e
            grad = grad + Cdd * r**-4 * (-3.0 * f * e - 3.0 * bracket)
        F2 = -grad; F1 = grad
        # torques (z-components via -dU/dtheta)
        tau1 = tau2 = 0.0
        if Cdd != 0.0:
            dU_dth1 = Cdd * r**-3 * ((n1p @ n2) - 3.0 * (n1p @ e) * b_)
            dU_dth2 = Cdd * r**-3 * ((n1 @ n2p) - 3.0 * a_ * (n2p @ e))
            tau1 = -dU_dth1; tau2 = -dU_dth2
        return np.array([v1[0], v1[1], v2[0], v2[1],
                         F1[0]/M, F1[1]/M, F2[0]/M, F2[1]/M,
                         om1, om2, tau1/I_ROT, tau2/I_ROT])
    return rhs

def energy_and_momenta(y, Cdd):
    r1 = y[0:2]; r2 = y[2:4]; v1 = y[4:6]; v2 = y[6:8]
    th1, th2, om1, om2 = y[8], y[9], y[10], y[11]
    rv = r2 - r1; r = np.linalg.norm(rv); e = rv / r
    n1 = np.array([np.cos(th1), np.sin(th1)])
    n2 = np.array([np.cos(th2), np.sin(th2)])
    U = -K / r
    if Cdd != 0.0:
        U += Cdd / r**3 * ((n1 @ n2) - 3.0 * (n1 @ e) * (n2 @ e))
    KE = 0.5*M*(v1@v1 + v2@v2) + 0.5*I_ROT*(om1**2 + om2**2)
    P = M*(v1 + v2)
    L_orb = M*(r1[0]*v1[1]-r1[1]*v1[0] + r2[0]*v2[1]-r2[1]*v2[0])
    L = L_orb + I_ROT*(om1 + om2)
    return KE + U, P, L

def accel1(y, Cdd):
    """Acceleration of body 1 at state y (fresh evaluation, for diagnostics)."""
    dydt = make_rhs(Cdd)(0.0, y)
    return dydt[4:6]

def run(Cdd, tmax=40.0):
    # COM at origin, circular-orbit speed for the monopole baseline, split evenly
    # each body orbits the COM at radius SEED_R/2 under accel K/SEED_R^2:
    # v^2 / (SEED_R/2) = K/SEED_R^2  ->  v = sqrt(K / (2*SEED_R))
    vhalf = np.sqrt(K / (2.0 * SEED_R))
    y0 = np.array([-SEED_R/2, 0.0,  SEED_R/2, 0.0,   # r1, r2 on x-axis
                   0.0, -vhalf,  0.0, vhalf,        # opposite tangential velocities
                   0.6, 2.2, 0.0, 0.0])             # bicone axes th1, th2; spins 0
    sol = solve_ivp(make_rhs(Cdd), [0, tmax], y0, rtol=1e-10, atol=1e-12,
                    dense_output=True, max_step=0.05)
    ts = np.linspace(0, tmax, 2001)
    Y = sol.sol(ts)
    E0, P0, L0 = energy_and_momenta(Y[:, 0], Cdd)
    E1, P1, L1 = energy_and_momenta(Y[:, -1], Cdd)
    Emin = min(energy_and_momenta(Y[:, i], Cdd)[0] for i in range(0, 2001, 100))
    Emax = max(energy_and_momenta(Y[:, i], Cdd)[0] for i in range(0, 2001, 100))
    print(f"Cdd={Cdd}: success={sol.success}  E0={E0:.8f} E_end={E1:.8f} "
          f"E_spread(sampled)={Emax-Emin:.2e}  |dP|={np.linalg.norm(P1-P0):.2e}  dL={L1-L0:.2e}")
    return ts, Y

def diagnostics(ts, Y, Cdd):
    rv = Y[2:4] - Y[0:2]
    r = np.linalg.norm(rv, axis=0); e = rv / r
    phi = np.arctan2(e[1], e[0])                     # line-of-centres angle
    a1 = np.array([accel1(Y[:, i], Cdd) for i in range(0, len(ts), 10)]).T
    phi_s = phi[::10]
    delta = (np.arctan2(a1[1], a1[0]) - phi_s + np.pi) % (2*np.pi) - np.pi
    th1, th2 = Y[8], Y[9]
    S = np.cos(th1-th2) - 3*np.cos(th1-phi)*np.cos(th2-phi)  # dipole alignment factor f
    return dict(r=r, phi=phi, delta_full=(ts[::10], delta), th1=th1, th2=th2, f=S)

# ---------- run both cases ----------
tsA, YA = run(0.0)
tsB, YB = run(0.6)
dA = diagnostics(tsA, YA, 0.0)
dB = diagnostics(tsB, YB, 0.6)
print(f"CONTROL  (Cdd=0):   max |deviation of a1 from line of centres| = "
      f"{np.degrees(np.max(np.abs(dA['delta_full'][1]))):.4f} deg  (expect ~0)")
print(f"DIPOLE   (Cdd=0.6): max |deviation| = {np.degrees(np.max(np.abs(dB['delta_full'][1]))):.2f} deg, "
      f"rms = {np.degrees(np.sqrt(np.mean(dB['delta_full'][1]**2))):.2f} deg")
print(f"DIPOLE run: separation range [{dB['r'].min():.3f}, {dB['r'].max():.3f}], "
      f"axis th1 swept {np.degrees(YB[8].max()-YB[8].min()):.1f} deg (unwrapped range), "
      f"dipole factor f range [{dB['f'].min():.3f}, {dB['f'].max():.3f}]")

# ---------- figure 1: trajectories + osculating acceleration parabolas ----------
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
for ax, (Y, Cdd, ttl) in zip(axes, [(YA, 0.0, "A: monopole only (control)"),
                                    (YB, 0.6, "B: monopole + bicone dipole-dipole")]):
    ax.plot(Y[0], Y[1], color="#7fa7cf", lw=1.2, label="body 1")
    ax.plot(Y[2], Y[3], color="#b08fcf", lw=1.2, label="body 2")
    # snapshot acceleration arrows for body 1 (direction + magnitude of a1):
    # the osculating parabola at a snapshot lies almost on top of the trajectory
    # itself (it osculates it), so its ORIENTATION is read cleanly off the arrow:
    # parabola axis = a1 direction, curvature = |a1|.
    for frac in np.linspace(0.03, 0.97, 8):
        idx = int(frac * (Y.shape[1]-1)); y = Y[:, idx]
        a1 = accel1(y, Cdd); p = y[0:2]
        ax.annotate("", xy=p + 0.45*a1, xytext=p,
                    arrowprops=dict(arrowstyle="->", color="#d1495b", lw=1.8))
        ax.plot(p[0], p[1], "o", color="#d1495b", ms=4)
    ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
    ax.set_title(ttl + "\nred arrows = body 1 acceleration (parabola axis)", fontsize=10)
fig.tight_layout(); fig.savefig("fig_trajectories_parabolas.png", dpi=160)

# ---------- figure 1b: osculating parabolas in body-1 velocity frame ----------
# Local coordinates at a snapshot: e_par along v1, e_perp rotated +90 deg.
# Parabola coords: (v s + 1/2 a_par s^2,  1/2 a_perp s^2). Its tilt in this
# frame is set by a_perp/a_par -- i.e. by how far a has rotated off v.
fig, axes = plt.subplots(1, 4, figsize=(13, 3.4))
for ax, frac in zip(axes, [0.05, 0.30, 0.55, 0.85]):
    for (Y, Cdd, col, lab) in [(YA, 0.0, "#888888", "monopole"), (YB, 0.6, "#d1495b", "dipole")]:
        idx = int(frac * (Y.shape[1]-1)); y = Y[:, idx]
        a1 = accel1(y, Cdd); v1 = y[4:6]; sp = np.linalg.norm(v1)
        epar = v1/sp; eperp = np.array([-epar[1], epar[0]])
        apar, aperp = a1 @ epar, a1 @ eperp
        s = np.linspace(0, 1.1, 80)
        ax.plot(sp*s + 0.5*apar*s**2, 0.5*aperp*s**2, color=col, lw=1.6, label=lab)
    ax.axhline(0, color="k", lw=0.6); ax.grid(alpha=0.3); ax.legend(fontsize=7)
    ax.set_title(f"t = {frac*40:.0f}", fontsize=10)
    ax.set_xlabel("along v1"); ax.set_ylabel("perp to v1")
fig.suptitle("Body 1 osculating parabola in its own velocity frame (grey = control, red = dipole run)")
fig.tight_layout(); fig.savefig("fig_local_parabolas.png", dpi=160)

# ---------- figure 2: orientation diagnostics ----------
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
t_d, delta = dB["delta_full"]
axes[0].plot(t_d, np.degrees(delta), color="#d1495b", lw=1.2)
axes[0].axhline(0, color="k", lw=0.7); axes[0].set_ylabel("deviation of a1\nfrom line of centres [deg]")
axes[0].set_title("Dipole run: how far the acceleration parabola's axis bends off the line of centres")
wrapdeg = lambda x: np.degrees((x + np.pi) % (2*np.pi) - np.pi)
axes[1].plot(tsB, wrapdeg(dB["th1"] - dB["phi"]), color="#7fa7cf", label="axis1 - line of centres")
axes[1].plot(tsB, wrapdeg(dB["th2"] - dB["phi"]), color="#b08fcf", label="axis2 - line of centres")
axes[1].set_ylabel("bicone axis angle\nrelative to line of centres [deg]"); axes[1].legend(fontsize=8)
axes[2].plot(tsB, dB["r"], color="#30638e", label="separation r")
axes[2].plot(tsB, dB["f"], color="#edae49", label="dipole factor f")
axes[2].set_ylabel("r  /  f"); axes[2].set_xlabel("time"); axes[2].legend(fontsize=8)
for ax in axes: ax.grid(alpha=0.3)
fig.tight_layout(); fig.savefig("fig_orientation_diagnostics.png", dpi=160)
print("figures written: fig_trajectories_parabolas.png, fig_local_parabolas.png, fig_orientation_diagnostics.png")
