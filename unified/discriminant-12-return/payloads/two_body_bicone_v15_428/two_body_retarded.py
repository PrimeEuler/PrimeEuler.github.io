"""
Retarded EM two-charge simulation (2026-11-02): fields carry the interaction.

Units: Gaussian (E of a point charge = q/R^2), c = 1, m = 1.
Charges q1 = +1, q2 = -1 (attracting pair), initial separation 10 (each body
on a radius-5 circle about the COM), tangential speed 0.221 (p = 0.2267).

Dynamics: relativistic shell-sliding as in two_body_bicone_rel.py
(dp/dt = q(E + v x B), E_particle = sqrt(p^2 + m^2), dr/dt = p/E_particle),
but the fields at each body are the LIENARD-WIECHERT fields of the OTHER
charge, evaluated at the retarded time t_r = t - |r - r_src(t_r)|/c:

  E = q_src [ (n-beta)(1-beta^2)/(kappa^3 R^2)
              + n x ((n-beta) x beta_dot) / (c kappa^3 R) ],   B = n x E,
  kappa = 1 - n.beta, all source quantities at t_r.

Runs:
  A  instantaneous Coulomb control (solve_ivp, potential -1/r): conservative.
  B  retarded VELOCITY fields only (accel term dropped): delay/aberration,
     but no radiation fields -- a diagnostic, not a consistent theory.
  C  full Lienard-Wiechert: radiation fields on. Expect secular inspiral:
     the field carries energy/momentum away; particle totals stop conserving.

Integration of B/C: fixed-step RK4 for the delay system. Retarded times are
~10 time units behind the present (dt = 0.02), so the source state at t_r is
always in stored history: cubic-Hermite interpolation of (r, v), linear for a.
History for t < 0 is prescribed uniform circular motion (analytic a), so
position/velocity/acceleration are continuous at t = 0.

Energy audit for C: bookkeeping orbital energy
  E_book = sum (gamma-1) m c^2  - 1/r   (instantaneous-Coulomb bookkeeping)
should DECLINE, and its decline is compared against the time-integrated
relativistic Larmor power sum_i (2 q_i^2/3c^3) gamma^6 [a^2 - |v x a|^2/c^2].
Agreement is expected only at the tens-of-percent level (field energy also
sloshes in the near zone); a wildly different number would indict the code.
"""
import sys, math, time
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C_LIGHT = 1.0
M = 1.0
Q = [1.0, -1.0]
RAD = 5.0            # each body's orbital radius; separation = 10
V0 = 0.221           # tangential speed (gamma ~ 1.0257, p ~ 0.2267)
OMEGA = V0 / RAD
DT = 0.02
HIST = 13.0          # prescribed-history depth (max light-travel ~ separation + margin)
TMAX = float(sys.argv[1]) if len(sys.argv) > 1 else 320.0
RSTOP = 3.2

GAM0 = 1.0 / math.sqrt(1 - V0**2)
P0 = GAM0 * M * V0

# ---------------------------------------------------------------- history ---
# History stored on a uniform grid from t = -HIST. Per body: lists of
# (x, y) position, (vx, vy) velocity, (ax, ay) coordinate acceleration.
class History:
    def __init__(self):
        self.t0 = -HIST
        self.R = [[], []]
        self.V = [[], []]
        self.A = [[], []]
        nh = int(round(HIST / DT)) + 1
        for k in range(nh):
            t = -HIST + k * DT
            for b in range(2):
                phi = (math.pi if b == 0 else 0.0) + OMEGA * t
                x, y = RAD * math.cos(phi), RAD * math.sin(phi)
                # phi = pi (body 1) gives v = (0,-V0) at t=0; phi = 0 (body 2) gives (0,+V0).
                vx, vy = -RAD * OMEGA * math.sin(phi), RAD * OMEGA * math.cos(phi)
                ax, ay = -OMEGA**2 * x, -OMEGA**2 * y
                self.R[b].append((x, y)); self.V[b].append((vx, vy)); self.A[b].append((ax, ay))
        # fix body-1 velocity sign properly: at phi=pi, (-sin, cos) = (0,-1) -> (0,-V0) correct as-is.
    def _idx(self, t):
        f = (t - self.t0) / DT
        k = int(math.floor(f))
        k = max(0, min(k, len(self.R[0]) - 2))
        return k, f - k
    def pos_vel(self, b, t):
        k, s = self._idx(t)
        (x0, y0), (x1, y1) = self.R[b][k], self.R[b][k+1]
        (u0, w0), (u1, w1) = self.V[b][k], self.V[b][k+1]
        s2, s3 = s*s, s*s*s
        h00 = 2*s3 - 3*s2 + 1; h10 = s3 - 2*s2 + s; h01 = -2*s3 + 3*s2; h11 = s3 - s2
        x = h00*x0 + h10*DT*u0 + h01*x1 + h11*DT*u1
        y = h00*y0 + h10*DT*w0 + h01*y1 + h11*DT*w1
        # velocity: Hermite on (V, A)
        (a0x, a0y), (a1x, a1y) = self.A[b][k], self.A[b][k+1]
        vx = h00*u0 + h10*DT*a0x + h01*u1 + h11*DT*a1x
        vy = h00*w0 + h10*DT*a0y + h01*w1 + h11*DT*a1y
        return (x, y), (vx, vy)
    def acc(self, b, t):
        k, s = self._idx(t)
        (a0x, a0y), (a1x, a1y) = self.A[b][k], self.A[b][k+1]
        return (a0x + s*(a1x-a0x), a0y + s*(a1y-a0y))
    def append(self, b, r, v, a):
        self.R[b].append(r); self.V[b].append(v); self.A[b].append(a)

# ------------------------------------------------------------- LW field -----
def lw_field(hist, src, q_src, fx, fy, t, include_accel):
    """E (2-vector) and Bz at field point (fx, fy), time t, from source body."""
    # fixed-point iteration for retarded time
    (sx, sy), _ = hist.pos_vel(src, min(t, -1e-9) if t - 10 < -HIST else t - 10.0)
    tr = t - math.hypot(fx - sx, fy - sy) / C_LIGHT
    for _ in range(10):
        (sx, sy), _ = hist.pos_vel(src, tr)
        tr_new = t - math.hypot(fx - sx, fy - sy) / C_LIGHT
        if abs(tr_new - tr) < 1e-12: tr = tr_new; break
        tr = tr_new
    (sx, sy), (svx, svy) = hist.pos_vel(src, tr)
    Rx, Ry = fx - sx, fy - sy
    R = math.hypot(Rx, Ry); nx, ny = Rx / R, Ry / R
    bx, by = svx / C_LIGHT, svy / C_LIGHT
    b2 = bx*bx + by*by
    kap = 1.0 - (nx*bx + ny*by)
    # velocity field
    coef = q_src * (1.0 - b2) / (kap**3 * R**2)
    Ex = coef * (nx - bx); Ey = coef * (ny - by)
    if include_accel:
        (sax, say) = hist.acc(src, tr)
        bdx, bdy = sax / C_LIGHT, say / C_LIGHT
        wz = (nx - bx) * bdy - (ny - by) * bdx      # z of (n-beta) x beta_dot
        coef2 = q_src * wz / (C_LIGHT * kap**3 * R)
        Ex += coef2 * ny; Ey += -coef2 * nx        # n x (wz z-hat) = wz*(ny, -nx)
    Bz = nx * Ey - ny * Ex
    return Ex, Ey, Bz

def coord_accel(Fx, Fy, vx, vy):
    """dv/dt from force F and velocity v (relativistic, m=1)."""
    E = math.sqrt(1.0 + 0.0)  # placeholder, gamma computed below from v
    g = 1.0 / math.sqrt(max(1e-15, 1.0 - (vx*vx + vy*vy) / C_LIGHT**2))
    sp = math.hypot(vx, vy)
    if sp < 1e-14: return Fx / M, Fy / M
    ex, ey = vx / sp, vy / sp
    Fpar = Fx*ex + Fy*ey; Fperp_x = Fx - Fpar*ex; Fperp_y = Fy - Fpar*ey
    return (Fpar/(g**3*M))*ex + Fperp_x/(g*M), (Fpar/(g**3*M))*ey + Fperp_y/(g*M)

# ------------------------------------------------------------- DDE driver ---
def run_dde(include_accel, label):
    hist = History()
    # state: r1, p1, r2, p2 as floats
    st = np.array([-RAD, 0.0, 0.0, -P0, RAD, 0.0, 0.0, P0])
    def vel(px, py):
        E = math.sqrt(px*px + py*py + M*M)
        return px / E, py / E        # c = 1: v = p c^2 / E
    def deriv(t, s):
        x1, y1, px1, py1, x2, y2, px2, py2 = s
        v1x, v1y = vel(px1, py1); v2x, v2y = vel(px2, py2)
        E1x, E1y, B1z = lw_field(hist, 1, Q[1], x1, y1, t, include_accel)
        F1x = Q[0] * (E1x + v1y * B1z); F1y = Q[0] * (E1y - v1x * B1z)
        E2x, E2y, B2z = lw_field(hist, 0, Q[0], x2, y2, t, include_accel)
        F2x = Q[1] * (E2x + v2y * B2z); F2y = Q[1] * (E2y - v2x * B2z)
        return np.array([v1x, v1y, F1x, F1y, v2x, v2y, F2x, F2y])
    nsteps = int(TMAX / DT)
    out_t, out_sep, out_E, out_L, out_P, out_Fdev, out_rad = [], [], [], [], [], [], []
    rad_cum = 0.0
    prev_P_larmor = None
    t_stop = TMAX
    for n in range(nsteps):
        t = n * DT
        # grid-point forces/accels for history + diagnostics
        d0 = deriv(t, st)
        v1x, v1y = vel(st[2], st[3]); v2x, v2y = vel(st[6], st[7])
        a1 = coord_accel(d0[2], d0[3], v1x, v1y); a2 = coord_accel(d0[6], d0[7], v2x, v2y)
        # correct the placeholder accel stored for THIS grid point last iteration
        hist.A[0][-1] = a1; hist.A[1][-1] = a2
        # RK4 step
        k1 = d0
        k2 = deriv(t + DT/2, st + DT/2 * k1)
        k3 = deriv(t + DT/2, st + DT/2 * k2)
        k4 = deriv(t + DT, st + DT * k3)
        st_new = st + DT/6 * (k1 + 2*k2 + 2*k3 + k4)
        # append NEXT grid point to history (its accel computed at start of next loop;
        # for interpolation during this step it was not needed: retarded times << t)
        nv1 = vel(st_new[2], st_new[3]); nv2 = vel(st_new[6], st_new[7])
        # placeholder accel, overwritten at next iteration's deriv before any use
        # (retarded lookups trail by >= ~3 time units), EXCEPT keep continuity:
        hist.append(0, (st_new[0], st_new[1]), nv1, a1)
        hist.append(1, (st_new[4], st_new[5]), nv2, a2)
        st = st_new
        # diagnostics every 25 steps
        if n % 25 == 0:
            sep = math.hypot(st[4]-st[0], st[5]-st[1])
            g1 = math.sqrt(1 + st[2]**2 + st[3]**2); g2 = math.sqrt(1 + st[6]**2 + st[7]**2)
            Ebook = (g1 - 1) + (g2 - 1) - 1.0/sep
            Lz = (st[0]*st[3] - st[1]*st[2]) + (st[4]*st[7] - st[5]*st[6])
            Pm = math.hypot(st[2]+st[6], st[3]+st[7])
            # force deviation for body 1 vs instantaneous line of centres
            ex, ey = (st[4]-st[0])/sep, (st[5]-st[1])/sep
            fdev = math.degrees(math.atan2(d0[3], d0[2]) - math.atan2(ey, ex))
            fdev = (fdev + 180) % 360 - 180
            # Larmor (relativistic), trapezoid accumulation at diagnostic cadence
            def larmor(vx, vy, a):
                g = 1.0/math.sqrt(max(1e-15, 1-(vx*vx+vy*vy)))
                vz_cross = vx*a[1] - vy*a[0]
                return (2.0/3.0) * g**6 * (a[0]**2 + a[1]**2 - vz_cross**2)
            Pl = larmor(v1x, v1y, a1) + larmor(v2x, v2y, a2)
            if prev_P_larmor is not None:
                rad_cum += 0.5 * (Pl + prev_P_larmor) * (25 * DT)
            prev_P_larmor = Pl
            out_t.append(t); out_sep.append(sep); out_E.append(Ebook)
            out_L.append(Lz); out_P.append(Pm); out_Fdev.append(fdev); out_rad.append(rad_cum)
            if sep < RSTOP:
                t_stop = t; break
    print(f"{label}: stopped at t={t_stop:.1f}, final sep={out_sep[-1]:.3f}, "
          f"E_book {out_E[0]:.4f} -> {out_E[-1]:.4f} (delta {out_E[-1]-out_E[0]:+.4f}), "
          f"integrated Larmor = {rad_cum:.4f}, L drift {out_L[-1]-out_L[0]:+.4f}, "
          f"|P_particles| max {max(out_P):.4f}")
    return hist, (np.array(out_t), np.array(out_sep), np.array(out_E),
                  np.array(out_L), np.array(out_P), np.array(out_Fdev),
                  np.array(out_rad)), rad_cum

# ------------------------------------------------------------- control A ----
def run_instant():
    def rhs(t, s):
        x1, y1, px1, py1, x2, y2, px2, py2 = s
        rx, ry = x2-x1, y2-y1; r = math.hypot(rx, ry); ex, ey = rx/r, ry/r
        F = 1.0 / r**2
        E1 = math.sqrt(px1**2+py1**2+1); E2 = math.sqrt(px2**2+py2**2+1)
        return [px1/E1, py1/E1, F*ex, F*ey, px2/E2, py2/E2, -F*ex, -F*ey]
    s0 = np.array([-RAD, 0.0, 0.0, -P0, RAD, 0.0, 0.0, P0])
    sol = solve_ivp(rhs, [0, TMAX], s0, rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.1)
    ts = np.linspace(0, TMAX, 801); Y = sol.sol(ts)
    sep = np.hypot(Y[4]-Y[0], Y[5]-Y[1])
    Eb = (np.sqrt(1+Y[2]**2+Y[3]**2)-1) + (np.sqrt(1+Y[6]**2+Y[7]**2)-1) - 1/sep
    print(f"A instant: sep range [{sep.min():.3f}, {sep.max():.3f}], E_book drift {Eb.max()-Eb.min():.2e}")
    return ts, sep, Eb, Y

t_start = time.time()
tsA, sepA, EbA, YA = run_instant()
histB, dB, radB = run_dde(False, "B vel-only")
histC, dC, radC = run_dde(True, "C full-LW ")
print(f"elapsed {time.time()-t_start:.1f}s")
np.savez("retarded_runs.npz", tA=tsA, sepA=sepA,
         tB=dB[0], sepB=dB[1], EB=dB[2], tC=dC[0], sepC=dC[1], EC=dC[2],
         LC=dC[3], PC=dC[4], FdevC=dC[5], radC=radC, radC_series=dC[6])

# ------------------------------------------------------------- figures ------
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(tsA, sepA, color="#999999", lw=1.2, label="A: instantaneous Coulomb (control)")
axes[0].plot(dB[0], dB[1], color="#edae49", lw=1.2, label="B: retarded velocity fields only")
axes[0].plot(dC[0], dC[1], color="#d1495b", lw=1.4, label="C: full Lienard-Wiechert")
axes[0].set_ylabel("separation r"); axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3)
axes[0].set_title("Field-carried interaction: separation vs time")
axes[1].plot(tsA, EbA, color="#999999", lw=1.2, label="A: E_book (must be flat)")
axes[1].plot(dC[0], dC[2], color="#d1495b", lw=1.4, label="C: E_book (particle bookkeeping)")
axes[1].plot(dC[0], dC[2][0] - dC[6], color="#30638e", ls="--", lw=1.2,
             label="C: E_book(0) - integrated Larmor power (audit prediction)")
axes[1].set_ylabel("E_book = sum(gamma-1) - 1/r"); axes[1].set_xlabel("time")
axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)
fig.tight_layout(); fig.savefig("fig_ret_separation_energy.png", dpi=160)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(dC[0], dC[5], color="#30638e", lw=1.0)
axes[0].axhline(0, color="k", lw=0.6); axes[0].set_ylabel("force deviation [deg]"); axes[0].grid(alpha=0.3)
axes[0].set_title("C: body-1 force direction vs instantaneous line of centres\n"
                  "(NOT ~omega*delay: the LW velocity field points at the extrapolated position)")
axes[1].plot(dC[0], dC[3] - dC[3][0], color="#7fa7cf", lw=1.2, label="particle angular momentum change")
axes[1].plot(dC[0], dC[4], color="#b08fcf", lw=1.2, label="|total particle momentum| (identically 0 by mirror symmetry -- uninformative here)")
axes[1].set_ylabel("delta Lz / |P|"); axes[1].set_xlabel("time"); axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)
fig.tight_layout(); fig.savefig("fig_ret_diagnostics.png", dpi=160)

# field snapshot from run C history at its final time
t_snap = dC[0][-1]
gx = np.linspace(-9, 9, 55); gy = np.linspace(-9, 9, 55)
EX = np.zeros((55, 55)); EY = np.zeros((55, 55))
for i, xx in enumerate(gx):
    for j, yy in enumerate(gy):
        ex_t = ey_t = 0.0
        for src in range(2):
            e_x, e_y, _ = lw_field(histC, src, Q[src], xx, yy, t_snap, True)
            ex_t += e_x; ey_t += e_y
        EX[j, i] = ex_t; EY[j, i] = ey_t
speed = np.hypot(EX, EY)
fig, ax = plt.subplots(figsize=(8.5, 8))
ax.streamplot(gx, gy, EX, EY, color=np.log10(speed + 1e-12), cmap="viridis", density=1.6, linewidth=0.7)
# current charge positions from history end (pos_vel at t_snap uses appended grid)
for src, col, lab in [(0, "#d1495b", "q = +1 now"), (1, "#30638e", "q = -1 now")]:
    (x, y), _ = histC.pos_vel(src, t_snap - 1e-6)
    ax.plot(x, y, "o", color=col, ms=9, label=lab)
    (xr, yr), _ = histC.pos_vel(src, t_snap - 10.0)
    ax.plot(xr, yr, "o", markerfacecolor="none", markeredgecolor=col, ms=11, label=f"{lab.split()[2]} 10 time units earlier")
ax.set_title(f"E-field of the pair at t = {t_snap:.0f} (full Lienard-Wiechert, from stored history)\n"
             "hollow circles: where each charge was one light-crossing time earlier")
ax.legend(fontsize=8, loc="upper right"); ax.set_xlabel("x"); ax.set_ylabel("y")
fig.tight_layout(); fig.savefig("fig_ret_field_snapshot.png", dpi=160)
print("figures written")
