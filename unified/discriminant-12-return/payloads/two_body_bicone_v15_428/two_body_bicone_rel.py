"""
Relativistic version of the two-body bicone-dipole sandbox (2026-11-02).

WHAT CHANGED vs two_body_bicone.py (Newtonian):
  - State is (r_i, p_i): relativistic momentum is the dynamical variable.
  - Force still slides momentum: dp_i/dt = F_i  (the v15.270 statement,
    now exact rather than a gamma->1 shadow).
  - Position follows from the SHELL: E_i = sqrt(|p_i|^2 c^2 + m^2 c^4),
    dr_i/dt = p_i c^2 / E_i.  Each body therefore lives on its mass shell
    u_i v_i = (m c^2)^2 with u_i = E_i + |p_i| c, v_i = E_i - |p_i| c,
    at rapidity psi_i = atanh(|p_i| c / E_i) -- the crossing slides along
    its uv = m^2 hyperbola instead of leaving it, by construction.
  - Coordinate acceleration a_i = dv_i/dt is NO LONGER parallel to F_i:
    a_parallel = F_parallel/(gamma^3 m), a_perp = F_perp/(gamma m).
    So the spatial (worldline) parabola can bend off the line of centres
    even in the monopole control -- a purely relativistic effect that we
    separate from the dipole's bending of F itself.

WHAT DID *NOT* CHANGE / HONEST SEAMS:
  - The interaction is still the same instantaneous potential
    U(r, th1, th2) in the LAB frame. A truly covariant interacting 2-body
    relativistic dynamics needs fields/retardation (no-interaction theorem);
    this is relativistic KINEMATICS + lab-frame potential, the standard
    sandbox compromise, stated plainly.
  - Bicone axis rotation is still a lab-frame rigid rotor (I th'' = tau);
    no Thomas precession / covariant spin transport.
  - Force law still imported classical dipole physics, not cone-derived.

FOUR RUNS, SAME initial (r, p, theta) state:
  N-control, N-dipole (Newtonian, as before), R-control, R-dipole.
  c = 1, m = 1: initial |v| = 0.5 Newtonian, gamma ~ 1.12 -- mild but visible.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C = 1.0
M = 1.0
I_ROT = 0.2
K = 1.0

def force_torque(rv, th1, th2, Cdd):
    """Return F1, tau1, tau2 for relative vector rv = r2 - r1 (U as before)."""
    r = np.linalg.norm(rv); e = rv / r
    n1 = np.array([np.cos(th1), np.sin(th1)]); n2 = np.array([np.cos(th2), np.sin(th2)])
    n1p = np.array([-np.sin(th1), np.cos(th1)]); n2p = np.array([-np.sin(th2), np.cos(th2)])
    a_ = n1 @ e; b_ = n2 @ e
    f = (n1 @ n2) - 3.0 * a_ * b_
    grad = K * e / r**2                      # dU/drv (monopole part)
    tau1 = tau2 = 0.0
    if Cdd != 0.0:
        bracket = b_*n1 + a_*n2 - 2.0*a_*b_*e
        grad = grad + Cdd * r**-4 * (-3.0*f*e - 3.0*bracket)
        tau1 = -Cdd * r**-3 * ((n1p @ n2) - 3.0*(n1p @ e)*b_)
        tau2 = -Cdd * r**-3 * ((n1 @ n2p) - 3.0*a_*(n2p @ e))
    return grad, tau1, tau2   # F1 = grad, F2 = -grad

def potential(rv, th1, th2, Cdd):
    r = np.linalg.norm(rv); e = rv / r
    n1 = np.array([np.cos(th1), np.sin(th1)]); n2 = np.array([np.cos(th2), np.sin(th2)])
    U = -K / r
    if Cdd != 0.0:
        U += Cdd / r**3 * ((n1 @ n2) - 3.0*(n1 @ e)*(n2 @ e))
    return U

def rhs_rel(t, y, Cdd):
    r1, r2, p1, p2 = y[0:2], y[2:4], y[4:6], y[6:8]
    th1, th2, om1, om2 = y[8], y[9], y[10], y[11]
    F1, tau1, tau2 = force_torque(r2 - r1, th1, th2, Cdd)
    E1 = np.sqrt((p1@p1)*C**2 + M**2*C**4); E2 = np.sqrt((p2@p2)*C**2 + M**2*C**4)
    v1 = p1 * C**2 / E1; v2 = p2 * C**2 / E2
    return np.array([v1[0], v1[1], v2[0], v2[1], F1[0], F1[1], -F1[0], -F1[1],
                     om1, om2, tau1/I_ROT, tau2/I_ROT])

def rhs_newt(t, y, Cdd):
    # y here uses velocities in the p slots (m = 1, so p_slot = v)
    r1, r2, v1, v2 = y[0:2], y[2:4], y[4:6], y[6:8]
    th1, th2, om1, om2 = y[8], y[9], y[10], y[11]
    F1, tau1, tau2 = force_torque(r2 - r1, th1, th2, Cdd)
    return np.array([v1[0], v1[1], v2[0], v2[1], F1[0]/M, F1[1]/M, -F1[0]/M, -F1[1]/M,
                     om1, om2, tau1/I_ROT, tau2/I_ROT])

Y0 = np.array([-1.0, 0.0,  1.0, 0.0,     # r1, r2 (separation 2)
               0.0, -0.5,  0.0, 0.5,     # p1, p2 (Newtonian reading: v = p/m)
               0.6, 2.2, 0.0, 0.0])      # th1, th2, om1, om2

def run(rhs, Cdd, tmax=40.0):
    sol = solve_ivp(rhs, [0, tmax], Y0, args=(Cdd,), rtol=1e-10, atol=1e-12,
                    dense_output=True, max_step=0.05)
    assert sol.success
    ts = np.linspace(0, tmax, 2001)
    return ts, sol.sol(ts)

def rel_energy_momenta(Y, Cdd):
    E = np.zeros(Y.shape[1]); L = np.zeros(Y.shape[1]); P = np.zeros((2, Y.shape[1]))
    for i in range(Y.shape[1]):
        y = Y[:, i]
        E1 = np.sqrt((y[4:6]@y[4:6])*C**2 + M**2*C**4)
        E2 = np.sqrt((y[6:8]@y[6:8])*C**2 + M**2*C**4)
        U = potential(y[2:4]-y[0:2], y[8], y[9], Cdd)
        E[i] = E1 + E2 + U + 0.5*I_ROT*(y[10]**2 + y[11]**2)
        P[:, i] = y[4:6] + y[6:8]
        L[i] = (y[0]*y[5]-y[1]*y[4] + y[2]*y[7]-y[3]*y[6]) + I_ROT*(y[10]+y[11])
    return E, P, L

def shell_data(Y):
    """u, v, psi, gamma, |v| for body 1."""
    p = Y[4:6]; pm = np.linalg.norm(p, axis=0)
    E = np.sqrt(pm**2 * C**2 + M**2 * C**4)
    u = E + pm*C; v = E - pm*C
    psi = 0.5*np.log(u/v)
    gamma = E/(M*C**2)
    vel = pm * C**2 / E          # |v| of body 1 (= |p| c^2 / E, along p)
    return u, v, psi, gamma, vel, E

def coord_accel(y, Cdd):
    """a = dv/dt of body 1 at state y: a_par = F_par/(gamma^3 m), a_perp = F_perp/(gamma m)."""
    F1, _, _ = force_torque(y[2:4]-y[0:2], y[8], y[9], Cdd)
    p = y[4:6]; E = np.sqrt((p@p)*C**2 + M**2*C**4)
    vel = p * C**2 / E; gamma = E/(M*C**2); sp = np.linalg.norm(vel)
    if sp < 1e-14: return F1/(M)
    epar = vel/sp; eperp = np.array([-epar[1], epar[0]])
    return (F1@epar)/(gamma**3 * M) * epar + (F1@eperp)/(gamma * M) * eperp

def angle_dev(a_vec, e_to_other):
    return np.degrees(np.arctan2(a_vec[1], a_vec[0]) - np.arctan2(e_to_other[1], e_to_other[0]))

wrap = lambda d: (d + 180.0) % 360.0 - 180.0

# ---------------- runs ----------------
runs = {}
for name, rhs, Cdd in [("N-control", rhs_newt, 0.0), ("N-dipole", rhs_newt, 0.6),
                       ("R-control", rhs_rel, 0.0), ("R-dipole", rhs_rel, 0.6)]:
    ts, Y = run(rhs, Cdd); runs[name] = (ts, Y)
    print(f"{name}: done")

# ---------------- checks: relativistic ----------------
for name in ["R-control", "R-dipole"]:
    ts, Y = runs[name]; Cdd = 0.0 if "control" in name else 0.6
    u, v, psi, gamma, vel, E1 = shell_data(Y)
    print(f"{name}: shell check max |u*v - (mc^2)^2| = {np.max(np.abs(u*v - (M*C**2)**2)):.2e} "
          f"(body1), gamma range [{gamma.min():.3f}, {gamma.max():.3f}], "
          f"psi range [{psi.min():.3f}, {psi.max():.3f}], max |v|/c = {vel.max()/C:.3f}")
    Etot, P, L = rel_energy_momenta(Y[::, ::20], Cdd)
    print(f"          total E drift {Etot.max()-Etot.min():.2e}, |P| drift "
          f"{np.max(np.abs(P - P[:, [0]])):.2e}, L drift {L.max()-L.min():.2e}")
tsN, YN = runs["N-dipole"]
print(f"N-dipole: max |v1| = {np.linalg.norm(YN[4:6], axis=0).max():.3f} (units of c=1 in the R runs)")

# deviations: force vs coordinate acceleration, body 1
dev = {}
for name, rhs in [("R-control", rhs_rel), ("R-dipole", rhs_rel), ("N-dipole", rhs_newt)]:
    ts, Y = runs[name]; Cdd = 0.0 if "control" in name else 0.6
    dF, dA = [], []
    for i in range(0, len(ts), 10):
        y = Y[:, i]; rv = y[2:4]-y[0:2]; e = rv/np.linalg.norm(rv)
        F1, _, _ = force_torque(rv, y[8], y[9], Cdd)
        dF.append(wrap(angle_dev(F1, e)))
        if rhs is rhs_rel:
            dA.append(wrap(angle_dev(coord_accel(y, Cdd), e)))
        else:
            dA.append(wrap(angle_dev(F1/M, e)))   # Newtonian: a parallel F
    dev[name] = (ts[::10], np.array(dF), np.array(dA))
    print(f"{name}: force deviation rms {np.sqrt(np.mean(np.array(dF)**2)):.2f} deg, "
          f"max {np.max(np.abs(dF)):.2f};  accel deviation rms {np.sqrt(np.mean(np.array(dA)**2)):.2f} deg, "
          f"max {np.max(np.abs(dA)):.2f}")

# ---------------- figure 1: trajectories ----------------
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
for ax, (ctrl, dip, ttl) in zip(axes, [("N-control", "N-dipole", "Newtonian (as before)"),
                                       ("R-control", "R-dipole", "Relativistic: state slides on uv = m\u00b2 shells")]):
    for nm, col, ls, lab in [(ctrl, "#999999", "--", "control (monopole)"), (dip, "#7fa7cf", "-", "dipole: body 1")]:
        _, Y = runs[nm]; ax.plot(Y[0], Y[1], color=col, ls=ls, lw=1.2, label=lab)
    _, Y = runs[dip]; ax.plot(Y[2], Y[3], color="#b08fcf", lw=1.0, label="dipole: body 2")
    ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.legend(fontsize=8); ax.set_title(ttl)
fig.tight_layout(); fig.savefig("fig_rel_trajectories.png", dpi=160)

# ---------------- figure 2: shell tracks ----------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
ax = axes[0]
uu = np.linspace(1.25, 2.05, 200); ax.plot(uu, 1.0/uu, color="k", lw=1.0, label="shell uv = (mc\u00b2)\u00b2 = 1")
for nm, col in [("R-control", "#999999"), ("R-dipole", "#d1495b")]:
    _, Y = runs[nm]; u, v, *_ = shell_data(Y)
    ax.plot(u, v, ".", color=col, ms=2.5, label=f"body 1 track ({nm})")
ax.set_xlim(1.25, 2.05); ax.set_ylim(0.42, 0.82)
ax.annotate("seat (1,1), psi = 0: off-frame up-left\n(bodies never rest in the lab frame)",
            xy=(1.32, 0.78), fontsize=8)
ax.set_xlabel("u = E + |p| c"); ax.set_ylabel("v = E \u2212 |p| c"); ax.set_title("Body 1 crossing sliding on its shell (zoom on the visited arc)")
ax.grid(alpha=0.3); ax.legend(fontsize=8)
ax = axes[1]
for nm, col, ls in [("R-dipole", "#d1495b", "-"), ("R-control", "#999999", "--")]:
    ts_, Y = runs[nm]; _, _, psi, gamma, vel, _ = shell_data(Y)
    ax.plot(ts_, psi, color=col, ls=ls, label=f"psi ({nm})")
ax.set_xlabel("time"); ax.set_ylabel("rapidity psi of body 1"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
ax.set_title("Rapidity along the shell vs time")
fig.tight_layout(); fig.savefig("fig_rel_shell.png", dpi=160)

# ---------------- figure 3: deviations, rel vs newt ----------------
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
t_, dF, dA = dev["R-dipole"]
axes[0].plot(t_, dF, color="#30638e", lw=1.2, label="R-dipole: FORCE deviation (dipole bending)")
axes[0].plot(*[dev["N-dipole"][0], dev["N-dipole"][1]], color="#edae49", lw=1.0, label="N-dipole: force (= accel) deviation")
t_, dFc, dAc = dev["R-control"]
axes[0].plot(t_, dFc, color="#999999", ls="--", lw=1.0, label="R-control: force deviation (must be 0)")
axes[0].axhline(0, color="k", lw=0.6); axes[0].set_ylabel("force deviation [deg]"); axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3)
axes[1].plot(dev["R-dipole"][0], dev["R-dipole"][2], color="#d1495b", lw=1.2, label="R-dipole: coordinate-acceleration (worldline parabola) deviation")
axes[1].plot(dev["R-control"][0], dev["R-control"][2], color="#999999", ls="--", lw=1.0, label="R-control: accel deviation (pure gamma anisotropy, no dipole)")
axes[1].axhline(0, color="k", lw=0.6); axes[1].set_ylabel("accel deviation [deg]"); axes[1].set_xlabel("time")
axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)
axes[0].set_title("Two different bendings: the dipole bends F; relativity additionally bends a away from F")
fig.tight_layout(); fig.savefig("fig_rel_deviations.png", dpi=160)

# ---------------- figure 4: local peel-off at a snapshot ----------------
# Take R-dipole snapshot with largest gamma; freeze F; continue three ways:
# exact relativistic (integrate dp/dt=F), force parabola (1/2 F/m tau^2),
# worldline parabola (1/2 a0 tau^2). Plot gap vs tau (log-log).
_, Y = runs["R-dipole"]; u, v, psi, gamma, vel, _ = shell_data(Y)
i0 = int(np.argmax(gamma)); y0 = Y[:, i0]
F1, _, _ = force_torque(y0[2:4]-y0[0:2], y0[8], y0[9], 0.6)
a0 = coord_accel(y0, 0.6)
p0 = y0[4:6]; E0 = np.sqrt((p0@p0)*C**2 + M**2*C**4); v0 = p0*C**2/E0
def rhs_frozen(t, z):  # z = [x, y, px, py], body-1 only, constant F1
    E = np.sqrt((z[2:]@z[2:])*C**2 + M**2*C**4)
    vv = z[2:]*C**2/E
    return np.array([vv[0], vv[1], F1[0], F1[1]])
taus = np.linspace(0, 1.6, 200)
sol = solve_ivp(rhs_frozen, [0, 1.6], np.concatenate([y0[0:2], p0]), rtol=1e-11, atol=1e-13, dense_output=True)
exact = sol.sol(taus)[0:2]
parF = y0[0:2][:, None] + v0[:, None]*taus + 0.5*(F1/M)[:, None]*taus**2
parA = y0[0:2][:, None] + v0[:, None]*taus + 0.5*a0[:, None]*taus**2
gapF = np.linalg.norm(exact - parF, axis=0); gapA = np.linalg.norm(exact - parA, axis=0)
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.loglog(taus[1:], gapF[1:], color="#30638e", label="|exact hyperbola \u2212 Newtonian force parabola (F/m)|")
ax.loglog(taus[1:], gapA[1:], color="#d1495b", label="|exact hyperbola \u2212 worldline parabola (a\u2080 = dv/dt)|")
ax.set_xlabel("tau (time since snapshot)"); ax.set_ylabel("gap")
ax.set_title(f"Peel-off at the highest-gamma snapshot (t={i0/len(u)*40:.1f}, gamma={gamma[i0]:.3f})\n"
             "worldline parabola hugs the hyperbola far longer: it carries the local gamma")
ax.grid(alpha=0.3, which="both"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig("fig_rel_peeloff.png", dpi=160)
small = (taus > 0.05) & (taus < 0.4)
slopeF = np.polyfit(np.log(taus[small]), np.log(gapF[small]), 1)[0]
slopeA = np.polyfit(np.log(taus[small]), np.log(gapA[small]), 1)[0]
print(f"peel-off snapshot gamma={gamma[i0]:.3f}; small-tau log-log slopes: force-parabola gap ~ tau^{slopeF:.2f}, "
      f"worldline-parabola gap ~ tau^{slopeA:.2f}; gaps at tau=1.6: {gapF[-1]:.3f} vs {gapA[-1]:.3f}")
print("figures written")
