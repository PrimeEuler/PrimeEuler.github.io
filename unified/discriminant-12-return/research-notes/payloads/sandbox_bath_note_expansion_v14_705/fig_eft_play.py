import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
ROW, COL = "#7fa7cf", "#b08fcf"
fig = plt.figure(figsize=(11, 4.6))
# Panel A: reduced hot-limit shape flow e(t) -> e0
axA = fig.add_subplot(1, 2, 1)
def flow(q0, C=0.35, tmax=30, dt=0.005):
    q, t, es, ts = q0, 0.0, [], []
    while t < tmax:
        ts.append(t); es.append(np.sqrt(1-q*q)); q += -C*(3*q*q-1)/q*dt; t += dt
    return ts, es
for q0 in [0.08, 0.3, 0.85, 0.99]:
    ts, es = flow(q0); axA.plot(ts, es, lw=1.6)
axA.axhline(np.sqrt(2/3), ls="--", color="#c0504d")
axA.text(20, 0.845, "$e_0=\\sqrt{2/3}$", color="#c0504d")
axA.set_xlabel("secular time (arb.)"); axA.set_ylabel("eccentricity $e$")
axA.set_title("Hot-bath shape flow: every start $\\to e_0$", fontsize=10)
# Panel B: the cone object with canonical mesh + attractor rays
axB = fig.add_subplot(1, 2, 2, projection="3d")
RMAX = 3.0
for u in range(1, 6):
    T = np.linspace(u/2.0, RMAX, 120); Y = np.sqrt(u*(2*T-u))
    for s in (1.0, -1.0):
        axB.plot(u-T, s*Y, T, color=ROW, lw=0.6, alpha=0.35)
        axB.plot(T-u, s*Y, T, color=COL, lw=0.6, alpha=0.35)
T = np.linspace(0, RMAX, 50)
for sgn in (1.0, -1.0):
    axB.plot(sgn*np.sqrt(3)/2*T, T/2, T, color="#c0504d", lw=2.6)
axB.text(0.2, 1.75, 3.05, "attractor rays\n$X:Y:T = sqrt(3) : 1 : 2$", color="#c0504d", fontsize=9)
axB.set_xlabel("X"); axB.set_ylabel("Y"); axB.set_zlabel("T")
axB.set_title("The attractor is a ray pair on the cone", fontsize=10)
axB.view_init(elev=18, azim=-58)
plt.tight_layout(); plt.savefig("fig_eft_play.png", dpi=160)
print("saved")
