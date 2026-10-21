"""Figure: shell + Larmor/Rabi orbits (canonical mesh) and the
theta-profile comparison for j=1."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import sph_harm

T = 6.0  # display shell radius in cone units (T-frame for the mesh)
fig = plt.figure(figsize=(11, 4.6))

# --- panel 1: bicone/shell cross-section with canonical parabola mesh
ax = fig.add_subplot(1, 2, 1)
u = np.linspace(0, 2*T, 400)
for k in range(13):  # rows x=u (blue) / columns y=u (purple), T-frame clip
    uu = np.linspace(0, 2*T, 200)
    X = uu - T; Y = np.sqrt(np.clip(uu*(2*T-uu), 0, None))
    ax.plot(X, Y, color='#7fa7cf', lw=0.5, alpha=0.35)
    ax.plot(X, -Y, color='#7fa7cf', lw=0.5, alpha=0.35)
    Xc = T - uu
    ax.plot(Xc, Y, color='#b08fcf', lw=0.5, alpha=0.35)
    ax.plot(Xc, -Y, color='#b08fcf', lw=0.5, alpha=0.35)
th = np.linspace(0, 2*np.pi, 200)
ax.plot(T*np.cos(th), T*np.sin(th), color='k', lw=1.0)          # shell
ax.plot([-T, T], [0, 0], color='gray', lw=0.7)
for xm, lab in ((1/3, 'm=0'), (-1/3, 'm=-1')):                   # Larmor latitudes
    ax.axvline(xm*T, color='#c0392b', lw=0.9, ls='--')
    ax.annotate(lab, (xm*T, T*0.82), color='#c0392b', fontsize=8, ha='center')
ax.axvline(T, color='#c0392b', lw=0.9, ls='--')
ax.annotate('m=+1', (T*0.97, -T*0.95), color='#c0392b', fontsize=8, ha='center')
ax.set_aspect('equal'); ax.set_xlabel('X (quantization)'); ax.set_ylabel('Y / W')
ax.set_title('Shell $S^2_T$: Larmor latitudes $X=m+1/2$ (T=3/2 ring shown at T=6 scale)')

# --- panel 2: theta profiles, j=1
ax = fig.add_subplot(1, 2, 2)
thd = np.linspace(0, np.pi, 361)
for m, c in ((0, '#c0392b'), (1, '#2471a3')):
    Y = sph_harm(m, 1, np.zeros_like(thd), thd)
    p = np.abs(Y)**2*2*np.pi*np.sin(thd); p /= np.trapz(p, thd)
    ax.plot(np.degrees(thd), p, color=c, lw=1.6,
            label=f'$|Y_{{1{m}}}|^2$ marginal')
# Test 3 pole-start profile (arcsine X-dwell of the Rabi meridian motion)
uu = np.linspace(-0.999, 0.999, 720)
dwell = 1/np.sqrt(1-uu**2); dwell /= np.trapz(dwell, uu)
th_u = np.arccos(uu); prof = dwell*np.sin(th_u); prof /= np.trapz(prof, th_u)
o = np.argsort(th_u)
ax.plot(np.degrees(th_u[o]), prof[o], color='k', lw=1.2, ls='--',
        label='Test 3 pole start: Rabi X-dwell (arcsine)')
ax.set_xlabel(r'$\theta$ from X axis (deg)'); ax.set_ylabel(r'$p(\theta)$')
ax.set_title('j=1: lobes vs integrated-orbit profile'); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig('fig_lobes.png', dpi=150); fig.savefig('fig_lobes.pdf')
print('figure written')
