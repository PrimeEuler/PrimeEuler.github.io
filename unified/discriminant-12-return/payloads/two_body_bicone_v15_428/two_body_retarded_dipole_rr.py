"""
Retarded bicone dipoles (2026-11-02): Reports 1-2 meet Report 3.

Each body = centre charge (Qc = +1 / -1, as in the retarded monopole run)
PLUS a rigid dipole: charges +/-QD at +/- (S/2) n(theta) along the bicone
axis. Dipole moment p = QD * S * n. All forces are Lienard-Wiechert fields
of point charges, cross-body only (intra-body interactions are carried by
the rigid constraint and excluded -- stated seam; no self-fields anywhere).

  - Net force on a body = sum of Lorentz forces on its 3 constituents
    (each constituent moves with V_centre + rotational velocity of its
    attachment point); dp_centre/dt = F_net, centre slides on uv = m^2.
  - Torque about the centre = sum (offset x F_constituent)_z;
    I theta'' = tau. The field producing the torque is RETARDED: it was
    emitted roughly one light-crossing time (~10 time units) before it acts.
  - Watch item: the dipole-alignment libration period (~2 pi sqrt(I/pE)
    ~ 22 time units at these parameters) is only ~2x the delay. Retarded
    feedback on a pendulum can damp or PUMP it. Which one happens is the
    question of the run, not an assumption.

Parameters: QD = 3, S = 1 (p = 3), I = 0.5, separation 10, V0 = 0.221,
theta0 = (0.6, 2.2), omega0 = 0, c = m = 1, Gaussian units, dt = 0.02.
Baseline for comparison: retarded_runs.npz run C (monopole LW, same orbit).
"""
import sys, math, time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C_LIGHT = 1.0; M = 1.0
RAD = 5.0; V0 = 0.221; OMEGA_ORB = V0 / RAD
GAM0 = 1.0 / math.sqrt(1 - V0**2); P0 = GAM0 * V0
DT = 0.02; HIST = 13.0
QD = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
I_ROT = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
S = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
RR = int(sys.argv[5]) if len(sys.argv) > 5 else 1   # Dirac antisymmetric reaction torque on/off
INTRA = 0  # full-retarded intra stays OFF in this build: replaced by the (ret+-adv)/2 split
RR_CAP = 0.2
rr_stats = {"max": 0.0, "cap_hits": 0}
LAST_ALC = [0.0, 0.0]  # cross-torque alphas from the most recent deriv call
TH0 = (0.6, 2.2)
QC = (1.0, -1.0)
TMAX = float(sys.argv[1]) if len(sys.argv) > 1 else 200.0
RSTOP = 3.2

def charges(b):
    return [(0.0, QC[b]), (1.0, QD), (-1.0, -QD)]

# ---------------------------------------------------------------- history ---
class History:
    """Per body: centre R,V,A and axis TH,OM,AL on a uniform grid from -HIST."""
    def __init__(self):
        self.t0 = -HIST
        self.R = [[], []]; self.V = [[], []]; self.A = [[], []]
        self.TH = [[], []]; self.OM = [[], []]; self.AL = [[], []]; self.ALC = [[], []]
        nh = int(round(HIST / DT)) + 1
        for k in range(nh):
            t = -HIST + k * DT
            for b in range(2):
                phi = (math.pi if b == 0 else 0.0) + OMEGA_ORB * t
                x, y = RAD * math.cos(phi), RAD * math.sin(phi)
                vx, vy = -RAD * OMEGA_ORB * math.sin(phi), RAD * OMEGA_ORB * math.cos(phi)
                self.R[b].append((x, y)); self.V[b].append((vx, vy))
                self.A[b].append((-OMEGA_ORB**2 * x, -OMEGA_ORB**2 * y))
                self.TH[b].append(TH0[b]); self.OM[b].append(0.0); self.AL[b].append(0.0); self.ALC[b].append(0.0)
    def _idx(self, t):
        f = (t - self.t0) / DT
        k = int(math.floor(f)); k = max(0, min(k, len(self.R[0]) - 2))
        return k, f - k
    @staticmethod
    def _herm(s, y0, d0, y1, d1):
        s2, s3 = s*s, s*s*s
        return ((2*s3-3*s2+1)*y0 + (s3-2*s2+s)*DT*d0 + (-2*s3+3*s2)*y1 + (s3-s2)*DT*d1)
    def centre(self, b, t):
        k, s = self._idx(t)
        R0, R1 = self.R[b][k], self.R[b][k+1]; V0_, V1_ = self.V[b][k], self.V[b][k+1]
        A0, A1 = self.A[b][k], self.A[b][k+1]
        px = self._herm(s, R0[0], V0_[0], R1[0], V1_[0]); py = self._herm(s, R0[1], V0_[1], R1[1], V1_[1])
        vx = self._herm(s, V0_[0], A0[0], V1_[0], A1[0]); vy = self._herm(s, V0_[1], A0[1], V1_[1], A1[1])
        ax = A0[0] + s*(A1[0]-A0[0]); ay = A0[1] + s*(A1[1]-A0[1])
        return (px, py), (vx, vy), (ax, ay)
    def axis(self, b, t):
        k, s = self._idx(t)
        th = self._herm(s, self.TH[b][k], self.OM[b][k], self.TH[b][k+1], self.OM[b][k+1])
        om = self._herm(s, self.OM[b][k], self.AL[b][k], self.OM[b][k+1], self.AL[b][k+1])
        al = self.AL[b][k] + s*(self.AL[b][k+1]-self.AL[b][k])
        return th, om, al
    def append(self, b, r, v, a, th, om, al, alc=0.0):
        self.R[b].append(r); self.V[b].append(v); self.A[b].append(a)
        self.TH[b].append(th); self.OM[b].append(om); self.AL[b].append(al); self.ALC[b].append(alc)

def src_state(hist, b, off, t):
    """Position/velocity/acceleration of body b's constituent at offset off*(S/2)."""
    (cx, cy), (cvx, cvy), (cax, cay) = hist.centre(b, t)
    th, om, al = hist.axis(b, t)
    d = off * S / 2.0
    nx, ny = math.cos(th), math.sin(th); px_, py_ = -ny, nx
    return ((cx + d*nx, cy + d*ny),
            (cvx + d*om*px_, cvy + d*om*py_),
            (cax + d*(al*px_ - om*om*nx), cay + d*(al*py_ - om*om*ny)))

# ------------------------------------------------------------- LW field -----
def lw_field(hist, src_b, src_off, q_src, fx, fy, t):
    tr = t - 10.0
    for _ in range(9):
        (sx, sy), _, _ = src_state(hist, src_b, src_off, tr)
        tr_new = t - math.hypot(fx - sx, fy - sy) / C_LIGHT
        if abs(tr_new - tr) < 1e-12: tr = tr_new; break
        tr = tr_new
    (sx, sy), (svx, svy), (sax, say) = src_state(hist, src_b, src_off, tr)
    Rx, Ry = fx - sx, fy - sy
    R = math.hypot(Rx, Ry); nx, ny = Rx / R, Ry / R
    bx, by = svx / C_LIGHT, svy / C_LIGHT
    b2 = bx*bx + by*by; kap = 1.0 - (nx*bx + ny*by)
    coef = q_src * (1.0 - b2) / (kap**3 * R**2)
    Ex = coef * (nx - bx); Ey = coef * (ny - by)
    bdx, bdy = sax / C_LIGHT, say / C_LIGHT
    wz = (nx - bx) * bdy - (ny - by) * bdx
    coef2 = q_src * wz / (C_LIGHT * kap**3 * R)
    Ex += coef2 * ny; Ey += -coef2 * nx
    return Ex, Ey, nx * Ey - ny * Ex

def coord_accel(Fx, Fy, vx, vy):
    g = 1.0 / math.sqrt(max(1e-15, 1.0 - (vx*vx + vy*vy)))
    sp = math.hypot(vx, vy)
    if sp < 1e-14: return Fx / M, Fy / M
    ex, ey = vx / sp, vy / sp
    Fpar = Fx*ex + Fy*ey
    return ((Fpar/(g**3*M))*ex + (Fx - Fpar*ex)/(g*M),
            (Fpar/(g**3*M))*ey + (Fy - Fpar*ey)/(g*M))

# ---------------------------------------------------------------- driver ----
def run():
    hist = History()
    st = np.array([-RAD, 0.0, 0.0, -P0, TH0[0], 0.0,
                   RAD, 0.0, 0.0, P0, TH0[1], 0.0])
    def vel(px, py):
        E = math.sqrt(px*px + py*py + M*M); return px / E, py / E
    def body_forces(t, s, b):
        base = 0 if b == 0 else 6
        cx, cy, px, py, th, om = s[base:base+6]
        Vx, Vy = vel(px, py)
        nx, ny = math.cos(th), math.sin(th); px_, py_ = -ny, nx
        Fx = Fy = tau = 0.0
        for off, qc in charges(b):
            d = off * S / 2.0
            fx, fy = cx + d*nx, cy + d*ny
            vcx, vcy = Vx + d*om*px_, Vy + d*om*py_
            Ex = Ey = Bz = 0.0
            for soff, sq in charges(1 - b):
                e_x, e_y, b_z = lw_field(hist, 1 - b, soff, sq, fx, fy, t)
                Ex += e_x; Ey += e_y; Bz += b_z
            if INTRA and off != 0.0:
                # the dipole's own partner charge (retarded across the arm):
                # this is where a dipole's radiation-reaction torque lives.
                e_x, e_y, b_z = lw_field(hist, b, -off, -qc, fx, fy, t)
                Ex += e_x; Ey += e_y; Bz += b_z
            Fcx = qc * (Ex + vcy * Bz); Fcy = qc * (Ey - vcx * Bz)
            Fx += Fcx; Fy += Fcy; tau += d * (nx * Fcy - ny * Fcx)
        return Fx, Fy, tau, (Vx, Vy)
    def reaction_torque(b, om, al_cross, t):
        """Dirac antisymmetric channel for the dipole's OWN radiation:
        tau_rr = (2/3c^3) (p x p_triple_dot)_z = (2/3) P^2 (alpha_dot - om^3),  c = 1,
        for a rigidly rotating dipole of moment P = QD*S. alpha_dot is a causal
        finite difference against the stored alpha history. The symmetric
        (ret+adv)/2 intra channel is NOT added: for a rigid pair its net force
        and torque vanish identically (verified numerically at t = 0 in run())."""
        if not RR: return 0.0
        Pd = QD * S
        # Reduction of order (Landau-Lifshitz style): alpha_dot comes ONLY from
        # the stored CROSS-alpha grid history (smooth, orbital timescale), never
        # from stage values -- a stage finite difference is the ALD runaway in
        # miniature (first version of this build blew up exactly that way).
        ALC = hist.ALC[b]
        al_dot = (ALC[-1] - ALC[-2]) / DT if len(ALC) >= 2 else 0.0
        if t < 1.0: al_dot = 0.0  # prescribed-history turn-on window: cross torque switches on at t=0
        trr = (2.0/3.0) * Pd * Pd * (al_dot - om**3)
        if abs(trr) > RR_CAP:
            rr_stats["cap_hits"] += 1
            trr = math.copysign(RR_CAP, trr)
        rr_stats["max"] = max(rr_stats["max"], abs(trr))
        return trr
    def deriv(t, s):
        F1x, F1y, tau1, V1 = body_forces(t, s, 0)
        F2x, F2y, tau2, V2 = body_forces(t, s, 1)
        al1 = tau1/I_ROT; al2 = tau2/I_ROT
        LAST_ALC[0] = al1; LAST_ALC[1] = al2
        trr1 = reaction_torque(0, s[5], al1, t)
        trr2 = reaction_torque(1, s[11], al2, t)
        return np.array([V1[0], V1[1], F1x, F1y, s[5], al1 + trr1/I_ROT,
                         V2[0], V2[1], F2x, F2y, s[11], al2 + trr2/I_ROT])
    # Symmetric-channel silence check (t = 0, instantaneous Coulomb intra pair):
    # net intra force and torque on a rigid dipole must vanish identically.
    for b in range(2):
        th = TH0[b]; nx, ny = math.cos(th), math.sin(th); d = S/2.0
        # partner (-QD at -d n) field at +constituent (+QD at +d n), and vice versa
        Rx, Ry = 2*d*nx, 2*d*ny; R3 = (2*d)**3
        Fp = (QD * (-QD) * Rx/R3, QD * (-QD) * Ry/R3)     # force on + charge
        Fm = ((-QD) * QD * (-Rx)/R3, (-QD) * QD * (-Ry)/R3)  # force on - charge
        net = (Fp[0]+Fm[0], Fp[1]+Fm[1])
        tq = d*(nx*Fp[1]-ny*Fp[0]) + (-d)*(nx*Fm[1]-ny*Fm[0])
        print(f"symmetric intra check body{b}: |net F| = {math.hypot(*net):.2e}, torque = {tq:.2e} (expect ~0)")
    nsteps = int(TMAX / DT)
    diag = {k: [] for k in ["t", "sep", "th1", "th2", "rel1", "rel2", "om1", "om2",
                            "fdev", "Ltot", "rad"]}
    rad_cum = 0.0; prev_Pl = None; t_stop = TMAX
    for n in range(nsteps):
        t = n * DT
        d0 = deriv(t, st)
        alc_now = (LAST_ALC[0], LAST_ALC[1])  # cross alphas at THIS grid point (captured before stages overwrite)
        # grid-point accelerations / angular accelerations (correct placeholders)
        V1 = vel(st[2], st[3]); V2 = vel(st[8], st[9])
        a1 = coord_accel(d0[2], d0[3], *V1); a2 = coord_accel(d0[8], d0[9], *V2)
        hist.A[0][-1] = a1; hist.A[1][-1] = a2
        hist.AL[0][-1] = d0[5]; hist.AL[1][-1] = d0[11]
        hist.ALC[0][-1] = alc_now[0]; hist.ALC[1][-1] = alc_now[1]
        k1 = d0
        k2 = deriv(t + DT/2, st + DT/2*k1); k3 = deriv(t + DT/2, st + DT/2*k2)
        k4 = deriv(t + DT, st + DT*k3)
        st_new = st + DT/6 * (k1 + 2*k2 + 2*k3 + k4)
        nV1 = vel(st_new[2], st_new[3]); nV2 = vel(st_new[8], st_new[9])
        hist.append(0, (st_new[0], st_new[1]), nV1, a1, st_new[4], st_new[5], d0[5], alc_now[0])
        hist.append(1, (st_new[6], st_new[7]), nV2, a2, st_new[10], st_new[11], d0[11], alc_now[1])
        st = st_new
        if n % 25 == 0:
            sep = math.hypot(st[6]-st[0], st[7]-st[1])
            phi = math.atan2(st[7]-st[1], st[6]-st[0])
            wrap = lambda a: (a + math.pi) % (2*math.pi) - math.pi
            # Larmor sum over the 6 constituents (audit-grade estimate)
            Pl = 0.0
            for b in range(2):
                base = 0 if b == 0 else 6
                Vb = vel(st[base+2], st[base+3]); ab = a1 if b == 0 else a2
                alb = d0[5] if b == 0 else d0[11]
                th, om = st[base+4], st[base+5]
                nx, ny = math.cos(th), math.sin(th); px_, py_ = -ny, nx
                for off, qc in charges(b):
                    d = off * S / 2.0
                    vx = Vb[0] + d*om*px_; vy = Vb[1] + d*om*py_
                    ax = ab[0] + d*(alb*px_ - om*om*nx); ay = ab[1] + d*(alb*py_ - om*om*ny)
                    g = 1.0/math.sqrt(max(1e-15, 1-(vx*vx+vy*vy)))
                    vz = vx*ay - vy*ax
                    Pl += qc*qc * (2.0/3.0) * g**6 * (ax*ax + ay*ay - vz*vz)
            if prev_Pl is not None: rad_cum += 0.5*(Pl + prev_Pl)*(25*DT)
            prev_Pl = Pl
            Lorb = (st[0]*st[3]-st[1]*st[2]) + (st[6]*st[9]-st[7]*st[8])
            fdev = math.degrees(wrap(math.atan2(d0[3], d0[2]) - phi))
            diag["t"].append(t); diag["sep"].append(sep)
            diag["th1"].append(st[4]); diag["th2"].append(st[10])
            diag["rel1"].append(math.degrees(wrap(st[4]-phi))); diag["rel2"].append(math.degrees(wrap(st[10]-phi)))
            diag["om1"].append(st[5]); diag["om2"].append(st[11])
            diag["fdev"].append(fdev); diag["Ltot"].append(Lorb + I_ROT*(st[5]+st[11]))
            diag["rad"].append(rad_cum)
            if sep < RSTOP: t_stop = t; break
    print(f"retarded dipole: stopped t={t_stop:.1f}, sep {diag['sep'][0]:.2f} -> {diag['sep'][-1]:.3f}, "
          f"rad estimate {rad_cum:.4f}, Ltot {diag['Ltot'][0]:.3f} -> {diag['Ltot'][-1]:.3f}")
    return hist, {k: np.array(v) for k, v in diag.items()}

t0 = time.time()
hist, dg = run()
print(f"elapsed {time.time()-t0:.1f}s  (QD={QD}, I={I_ROT}, S={S}, RR={RR})  "
      f"reaction torque: max |tau_rr| = {rr_stats['max']:.4f}, cap hits = {rr_stats['cap_hits']}")
base = np.load("retarded_runs.npz")
TAG = f"qd{QD:g}_I{I_ROT:g}_S{S:g}_rr{RR}"
np.savez(f"retarded_dipole_rr_runs_{TAG}.npz", **dg)

for key in ["rel1", "rel2"]:
    r = dg[key]
    print(f"{key}: range [{r.min():.1f}, {r.max():.1f}] deg, first-half range "
          f"[{r[:len(r)//2].min():.1f}, {r[:len(r)//2].max():.1f}], second-half "
          f"[{r[len(r)//2:].min():.1f}, {r[len(r)//2:].max():.1f}]")
print(f"omegas: om1 range [{dg['om1'].min():.3f}, {dg['om1'].max():.3f}], om2 [{dg['om2'].min():.3f}, {dg['om2'].max():.3f}]")
print(f"force deviation: rms {np.sqrt(np.mean(dg['fdev']**2)):.2f} deg, range [{dg['fdev'].min():.2f}, {dg['fdev'].max():.2f}]")
i140 = np.argmin(np.abs(base["tC"] - 140)) if base["tC"][-1] >= 140 else -1
print(f"baseline monopole C sep at t~{base['tC'][i140]:.0f}: {base['sepC'][i140]:.3f}; dipole run sep then: "
      f"{dg['sep'][np.argmin(np.abs(dg['t']-base['tC'][i140]))]:.3f}")

# ---------------------------------------------------------------- figures ---
fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
axes[0].plot(base["tC"], base["sepC"], color="#999999", lw=1.1, label="monopole LW baseline (run C)")
axes[0].plot(dg["t"], dg["sep"], color="#d1495b", lw=1.4, label="retarded bicone dipoles")
axes[0].set_ylabel("separation"); axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3)
axes[0].set_title("Retarded dipoles: inspiral vs monopole baseline")
axes[1].plot(dg["t"], dg["rel1"], color="#7fa7cf", label="axis 1 - line of centres")
axes[1].plot(dg["t"], dg["rel2"], color="#b08fcf", label="axis 2 - line of centres")
axes[1].axhline(0, color="k", lw=0.6); axes[1].set_ylabel("axis angle rel. line of centres [deg]")
axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)
axes[2].plot(dg["t"], dg["om1"], color="#7fa7cf", label="omega 1")
axes[2].plot(dg["t"], dg["om2"], color="#b08fcf", label="omega 2")
axes[2].axhline(0, color="k", lw=0.6); axes[2].set_ylabel("axis spin rate [rad / time]"); axes[2].set_xlabel("time")
axes[2].legend(fontsize=8); axes[2].grid(alpha=0.3)
fig.tight_layout(); fig.savefig("fig_rr_axes.png", dpi=160)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(dg["t"], dg["fdev"], color="#30638e", lw=1.1, label="retarded dipoles: net force deviation")
axes[0].plot(base["tC"], base["FdevC"], color="#999999", lw=0.9, label="monopole LW baseline")
axes[0].axhline(0, color="k", lw=0.6); axes[0].set_ylabel("force deviation [deg]")
axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3); axes[0].set_title("Force deviation: dipoles vs monopole-only")
axes[1].plot(dg["t"], dg["Ltot"] - dg["Ltot"][0], color="#7fa7cf", lw=1.2, label="dipole run: delta (orbital + spin) L, particles only")
axes[1].plot(base["tC"], base["LC"] - base["LC"][0], color="#999999", lw=1.0, label="monopole baseline: delta orbital L")
axes[1].set_ylabel("delta L"); axes[1].set_xlabel("time"); axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)
fig.tight_layout(); fig.savefig("fig_rr_deviation.png", dpi=160)

# field snapshot at final time, with dipole axes drawn
t_snap = dg["t"][-1]
gx = np.linspace(-9, 9, 46); gy = np.linspace(-9, 9, 46)
EX = np.zeros((46, 46)); EY = np.zeros((46, 46))
for i, xx in enumerate(gx):
    for j, yy in enumerate(gy):
        ex_t = ey_t = 0.0
        for b in range(2):
            for off, qc in charges(b):
                e_x, e_y, _ = lw_field(hist, b, off, qc, xx, yy, t_snap)
                ex_t += e_x; ey_t += e_y
        EX[j, i] = ex_t; EY[j, i] = ey_t
speed = np.hypot(EX, EY)
fig, ax = plt.subplots(figsize=(8.5, 8))
ax.streamplot(gx, gy, EX, EY, color=np.log10(speed + 1e-12), cmap="viridis", density=1.5, linewidth=0.7)
for b, col in [(0, "#d1495b"), (1, "#30638e")]:
    (x, y), _, _ = hist.centre(b, t_snap - 1e-6)
    th, _, _ = hist.axis(b, t_snap - 1e-6)
    nx, ny = math.cos(th), math.sin(th)
    ax.plot([x - 0.9*nx, x + 0.9*nx], [y - 0.9*ny, y + 0.9*ny], color=col, lw=2.5)
    ax.plot(x, y, "o", color=col, ms=8)
    ax.plot(x + 0.9*nx, y + 0.9*ny, "s", color=col, ms=6)  # + end of dipole
ax.set_title(f"E-field at t = {t_snap:.0f}: two retarded bicone dipoles\n"
             "thick lines = bicone axes (square = + end of dipole)")
ax.set_xlabel("x"); ax.set_ylabel("y")
fig.tight_layout(); fig.savefig("fig_rr_field.png", dpi=160)
print("figures written")
