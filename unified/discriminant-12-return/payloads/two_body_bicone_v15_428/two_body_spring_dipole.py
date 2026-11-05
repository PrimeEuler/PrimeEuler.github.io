"""
Spring-arm retarded bicone dipoles (2026-11-02): the symmetric channel wakes up.

Extension of two_body_retarded_dipole_rr.py. The dipole arm length S(t) is
now a dynamical coordinate per body (the rotation stays rigid; translation
stays shell-sliding). Stretch equation (generalized mass MU_S = MD/2):

  MU_S * S'' = -KS (S - S0)          spring (the symmetric channel, awake)
               - QD^2 / S^2          intra-pair Coulomb attraction (symmetric)
               + MD * S * om^2 / 2   centrifugal
               + Q_S^cross           tidal pull of the partner's retarded field:
                                     Q_S = sum_c (off/2) (F_c . n)
               + Q_S^rr              antisymmetric stretch reaction:
                                     (QD^2/3) * S_jerk, jerk from grid history
                                     (reduction of order, as for the torque)

Rotation: I(S) = I0 + MD S^2/2,  d/dt(I om) = tau_cross + tau_rr with the
variable-moment reaction torque tau_rr = (2/3)(p x p_triple_dot)_z,
p = QD*S(t) n. Constituent source states for the LW fields now include
stretch velocity/acceleration. Intra-pair Coulomb enters ONLY through the
stretch equation's symmetric potential term (instantaneous = leading
symmetric channel); the full retarded intra field remains excluded
(Report RETDIP negative result stands).

Equilibrium: KS(S-S0) + QD^2/S^2 = 0 has a root S_EQ < S0 (spring vs Coulomb)
-- with KS=10, QD=1: S_EQ ~ 0.868. The run starts there, at rest in S.
Watch items: adiabatic S modulation at orbital/libration frequencies,
back-action via p = QD*S and I(S), plunge chirp sweeping the drive
frequency up toward the stretch resonance om_s = sqrt(KS/MU_S) ~ 6.3.

Parameters: QD=1, MD=0.5, MU_S=0.25, KS=10, S0=1, I0=1.75 (I(S=1)=2.0 as
before), separation 10, V0=0.221, c=m=1, Gaussian units, dt=0.02.
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
QD = 1.0; QC = (1.0, -1.0); TH0 = (0.6, 2.2)
MD = 0.5; MU_S = MD / 2.0; KS = 10.0; S0 = 1.0; I0 = 1.75
TMAX = float(sys.argv[1]) if len(sys.argv) > 1 else 200.0
RSTOP = 3.2
RR_CAP = 0.2; QSRR_CAP = 0.5
rr_stats = {"max": 0.0, "cap_hits": 0, "qsrr_max": 0.0}
LAST_ALC = [0.0, 0.0]

def solve_seq():
    lo, hi = 0.3, 0.999
    f = lambda S: KS * (S - S0) + QD**2 / S**2
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0: hi = mid
        else: lo = mid
    return 0.5 * (lo + hi)
S_EQ = solve_seq()
print(f"S_EQ = {S_EQ:.4f} (spring KS={KS} vs Coulomb QD^2/S^2; rigid runs used S=1)")

def charges(b):
    return [(0.0, QC[b]), (1.0, QD), (-1.0, -QD)]

# ---------------------------------------------------------------- history ---
class History:
    def __init__(self):
        self.t0 = -HIST
        for name in ["R", "V", "A", "TH", "OM", "AL", "ALC", "SS", "SD", "SD2"]:
            setattr(self, name, [[], []])
        nh = int(round(HIST / DT)) + 1
        for k in range(nh):
            t = -HIST + k * DT
            for b in range(2):
                phi = (math.pi if b == 0 else 0.0) + OMEGA_ORB * t
                x, y = RAD * math.cos(phi), RAD * math.sin(phi)
                vx, vy = -RAD * OMEGA_ORB * math.sin(phi), RAD * OMEGA_ORB * math.cos(phi)
                self.R[b].append((x, y)); self.V[b].append((vx, vy))
                self.A[b].append((-OMEGA_ORB**2 * x, -OMEGA_ORB**2 * y))
                self.TH[b].append(TH0[b]); self.OM[b].append(0.0)
                self.AL[b].append(0.0); self.ALC[b].append(0.0)
                self.SS[b].append(S_EQ); self.SD[b].append(0.0); self.SD2[b].append(0.0)
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
        return ((self._herm(s, R0[0], V0_[0], R1[0], V1_[0]), self._herm(s, R0[1], V0_[1], R1[1], V1_[1])),
                (self._herm(s, V0_[0], A0[0], V1_[0], A1[0]), self._herm(s, V0_[1], A0[1], V1_[1], A1[1])),
                (A0[0] + s*(A1[0]-A0[0]), A0[1] + s*(A1[1]-A0[1])))
    def axis(self, b, t):
        k, s = self._idx(t)
        th = self._herm(s, self.TH[b][k], self.OM[b][k], self.TH[b][k+1], self.OM[b][k+1])
        om = self._herm(s, self.OM[b][k], self.AL[b][k], self.OM[b][k+1], self.AL[b][k+1])
        al = self.AL[b][k] + s*(self.AL[b][k+1]-self.AL[b][k])
        return th, om, al
    def stretch(self, b, t):
        k, s = self._idx(t)
        Sv = self._herm(s, self.SS[b][k], self.SD[b][k], self.SS[b][k+1], self.SD[b][k+1])
        Sdv = self._herm(s, self.SD[b][k], self.SD2[b][k], self.SD[b][k+1], self.SD2[b][k+1])
        SD2v = self.SD2[b][k] + s*(self.SD2[b][k+1]-self.SD2[b][k])
        return Sv, Sdv, SD2v
    def append(self, b, r, v, a, th, om, al, alc, Sv, Sdv, SD2v):
        self.R[b].append(r); self.V[b].append(v); self.A[b].append(a)
        self.TH[b].append(th); self.OM[b].append(om); self.AL[b].append(al); self.ALC[b].append(alc)
        self.SS[b].append(Sv); self.SD[b].append(Sdv); self.SD2[b].append(SD2v)

def src_state(hist, b, off, t):
    (cx, cy), (cvx, cvy), (cax, cay) = hist.centre(b, t)
    th, om, al = hist.axis(b, t)
    Sv, Sdv, SD2v = hist.stretch(b, t)
    d = off * Sv / 2.0
    nx, ny = math.cos(th), math.sin(th); px_, py_ = -ny, nx
    return ((cx + d*nx, cy + d*ny),
            (cvx + off*((Sdv/2)*nx + (Sv*om/2)*px_), cvy + off*((Sdv/2)*ny + (Sv*om/2)*py_)),
            (cax + off*((SD2v/2 - Sv*om*om/2)*nx + (Sdv*om + Sv*al/2)*px_),
             cay + off*((SD2v/2 - Sv*om*om/2)*ny + (Sdv*om + Sv*al/2)*py_)))

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
    st = np.array([-RAD, 0.0, 0.0, -P0, TH0[0], 0.0, S_EQ, 0.0,
                   RAD, 0.0, 0.0, P0, TH0[1], 0.0, S_EQ, 0.0])
    def vel(px, py):
        E = math.sqrt(px*px + py*py + M*M); return px / E, py / E
    def body_forces(t, s, b):
        base = 8 * b
        cx, cy, px, py, th, om, Sv, Sdv = s[base:base+8]
        Vx, Vy = vel(px, py)
        nx, ny = math.cos(th), math.sin(th); px_, py_ = -ny, nx
        Fx = Fy = tau = QS = 0.0
        for off, qc in charges(b):
            d = off * Sv / 2.0
            fx, fy = cx + d*nx, cy + d*ny
            vcx = Vx + off*((Sdv/2)*nx + (Sv*om/2)*px_)
            vcy = Vy + off*((Sdv/2)*ny + (Sv*om/2)*py_)
            Ex = Ey = Bz = 0.0
            for soff, sq in charges(1 - b):
                e_x, e_y, b_z = lw_field(hist, 1 - b, soff, sq, fx, fy, t)
                Ex += e_x; Ey += e_y; Bz += b_z
            Fcx = qc * (Ex + vcy * Bz); Fcy = qc * (Ey - vcx * Bz)
            Fx += Fcx; Fy += Fcy
            tau += d * (nx * Fcy - ny * Fcx)
            QS += (off / 2.0) * (Fcx * nx + Fcy * ny)
        return Fx, Fy, tau, QS, (Vx, Vy)
    def deriv(t, s):
        out = np.zeros(16)
        for b in range(2):
            base = 8 * b
            Fx, Fy, tau, QS, V = body_forces(t, s, b)
            th, om, Sv, Sdv = s[base+4], s[base+5], s[base+6], s[base+7]
            I_b = I0 + MD * Sv * Sv / 2.0
            al_cross = tau / I_b
            LAST_ALC[b] = al_cross
            # stretch reaction (antisymmetric): (QD^2/3) * S_jerk from grid history
            SD2h = hist.SD2[b]
            Sjerk = (SD2h[-1] - SD2h[-2]) / DT if (t >= 1.0 and len(SD2h) >= 2) else 0.0
            QSrr = (QD**2 / 3.0) * Sjerk
            if abs(QSrr) > QSRR_CAP: QSrr = math.copysign(QSRR_CAP, QSrr)
            rr_stats["qsrr_max"] = max(rr_stats["qsrr_max"], abs(QSrr))
            Sdd = (-KS * (Sv - S0) - QD**2 / Sv**2 + MD * Sv * om * om / 2.0 + QS + QSrr) / MU_S
            # rotation reaction (antisymmetric), variable moment p = QD*S(t)
            ALC = hist.ALC[b]
            al_dot = (ALC[-1] - ALC[-2]) / DT if (t >= 1.0 and len(ALC) >= 2) else 0.0
            Pd = QD * Sv; Pdd = QD * Sdd; Pdot = QD * Sdv
            trr = (2.0/3.0) * Pd * (Pd * al_dot + 3 * Pdd * om + 3 * Pdot * al_cross - Pd * om**3)
            if abs(trr) > RR_CAP:
                rr_stats["cap_hits"] += 1; trr = math.copysign(RR_CAP, trr)
            rr_stats["max"] = max(rr_stats["max"], abs(trr))
            Idot = MD * Sv * Sdv
            om_dot = (tau + trr - Idot * om) / I_b
            out[base:base+8] = [V[0], V[1], Fx, Fy, om, om_dot, Sdv, Sdd]
        return out
    nsteps = int(TMAX / DT)
    diag = {k: [] for k in ["t", "sep", "S1", "S2", "om1", "om2", "rel1", "rel2", "fdev"]}
    t_stop = TMAX; stop_reason = "tmax"
    for n in range(nsteps):
        t = n * DT
        d0 = deriv(t, st)
        alc_now = (LAST_ALC[0], LAST_ALC[1])
        V1 = vel(st[2], st[3]); V2 = vel(st[10], st[11])
        a1 = coord_accel(d0[2], d0[3], *V1); a2 = coord_accel(d0[10], d0[11], *V2)
        hist.A[0][-1] = a1; hist.A[1][-1] = a2
        hist.AL[0][-1] = d0[5]; hist.AL[1][-1] = d0[13]
        hist.ALC[0][-1] = alc_now[0]; hist.ALC[1][-1] = alc_now[1]
        hist.SD2[0][-1] = d0[7]; hist.SD2[1][-1] = d0[15]
        k1 = d0
        k2 = deriv(t + DT/2, st + DT/2*k1); k3 = deriv(t + DT/2, st + DT/2*k2)
        k4 = deriv(t + DT, st + DT*k3)
        st_new = st + DT/6 * (k1 + 2*k2 + 2*k3 + k4)
        nV1 = vel(st_new[2], st_new[3]); nV2 = vel(st_new[10], st_new[11])
        hist.append(0, (st_new[0], st_new[1]), nV1, a1, st_new[4], st_new[5], d0[5], alc_now[0],
                    st_new[6], st_new[7], d0[7])
        hist.append(1, (st_new[8], st_new[9]), nV2, a2, st_new[12], st_new[13], d0[13], alc_now[1],
                    st_new[14], st_new[15], d0[15])
        st = st_new
        if n % 25 == 0:
            sep = math.hypot(st[8]-st[0], st[9]-st[1])
            phi = math.atan2(st[9]-st[1], st[8]-st[0])
            wrap = lambda a: (a + math.pi) % (2*math.pi) - math.pi
            fdev = math.degrees(wrap(math.atan2(d0[3], d0[2]) - phi))
            diag["t"].append(t); diag["sep"].append(sep)
            diag["S1"].append(st[6]); diag["S2"].append(st[14])
            diag["om1"].append(st[5]); diag["om2"].append(st[13])
            diag["rel1"].append(math.degrees(wrap(st[4]-phi))); diag["rel2"].append(math.degrees(wrap(st[12]-phi)))
            diag["fdev"].append(fdev)
            if n % 250 == 0:
                print(f"  t={t:6.1f} sep={sep:6.3f} S1={st[6]:.4f} S2={st[14]:.4f} om2={st[13]:+.3f}")
            if sep < RSTOP: t_stop, stop_reason = t, "plunge (sep<RSTOP)"; break
            if not (0.3 < st[6] < 2.5 and 0.3 < st[14] < 2.5):
                t_stop, stop_reason = t, "stretch out of range"; break
    print(f"spring dipole: stopped t={t_stop:.1f} ({stop_reason}), sep -> {diag['sep'][-1]:.3f}, "
          f"S1 range [{min(diag['S1']):.4f}, {max(diag['S1']):.4f}], S2 range [{min(diag['S2']):.4f}, {max(diag['S2']):.4f}]")
    return hist, {k: np.array(v) for k, v in diag.items()}

t0 = time.time()
hist, dg = run()
print(f"elapsed {time.time()-t0:.1f}s; reaction: max|tau_rr|={rr_stats['max']:.4f} cap_hits={rr_stats['cap_hits']}, "
      f"max|Q_S^rr|={rr_stats['qsrr_max']:.4f}")
np.savez("spring_dipole_runs.npz", **dg)
rigid = np.load("retarded_dipole_rr_runs_qd1_I2_S1_rr1.npz")
cross = np.load("retarded_dipole_runs_qd1_I2_intra0_S1.npz")

# ---------------------------------------------------------------- figures ---
fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
axes[0].plot(cross["t"], cross["sep"], color="#999999", lw=1.0, label="rigid S=1, cross-only (R0)")
axes[0].plot(rigid["t"], rigid["sep"], color="#7fa7cf", lw=1.0, label="rigid S=1 + reaction torque (R1)")
axes[0].plot(dg["t"], dg["sep"], color="#d1495b", lw=1.5, label="spring arm (S dynamic, starts at S_EQ)")
axes[0].set_ylabel("separation"); axes[0].legend(fontsize=8); axes[0].grid(alpha=0.3)
axes[0].set_title("Spring-arm dipoles: inspiral vs rigid runs")
axes[1].plot(dg["t"], dg["S1"], color="#7fa7cf", label="S1 (arm length, body 1)")
axes[1].plot(dg["t"], dg["S2"], color="#b08fcf", label="S2 (arm length, body 2)")
axes[1].axhline(S_EQ, color="k", lw=0.7, ls="--", label="S_EQ")
axes[1].axhline(S0, color="#999999", lw=0.7, ls=":", label="spring rest length S0 = 1")
axes[1].set_ylabel("arm length S"); axes[1].legend(fontsize=8); axes[1].grid(alpha=0.3)
axes[2].plot(dg["t"], dg["om1"], color="#7fa7cf", label="omega1")
axes[2].plot(dg["t"], dg["om2"], color="#b08fcf", label="omega2")
axes[2].plot(rigid["t"], rigid["om2"], color="#999999", lw=0.9, label="omega2 rigid (R1)")
axes[2].axhline(0, color="k", lw=0.6); axes[2].set_ylabel("axis spin rate"); axes[2].set_xlabel("time")
axes[2].legend(fontsize=8); axes[2].grid(alpha=0.3)
fig.tight_layout(); fig.savefig("fig_spring_main.png", dpi=160)

# zoom on S modulation (first 40 time units, detrended by eye via tight ylim)
fig, ax = plt.subplots(figsize=(10, 4.5))
m = dg["t"] <= 40
ax.plot(dg["t"][m], dg["S1"][m], color="#7fa7cf", label="S1")
ax.plot(dg["t"][m], dg["S2"][m], color="#b08fcf", label="S2")
ax.axhline(S_EQ, color="k", lw=0.7, ls="--")
ax.set_ylabel("arm length S"); ax.set_xlabel("time"); ax.legend(fontsize=8); ax.grid(alpha=0.3)
ax.set_title("Arm-length modulation, first 40 time units (stretch period ~1.0 would show as fast ripple)")
fig.tight_layout(); fig.savefig("fig_spring_zoom.png", dpi=160)
print("figures written")
