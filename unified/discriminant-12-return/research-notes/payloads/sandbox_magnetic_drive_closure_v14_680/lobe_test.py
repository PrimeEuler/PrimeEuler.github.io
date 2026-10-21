"""Lobe test (sandbox, 2026-10-21). Jeremy: 'the cone projects the
Larmor vector orbits onto the sphere, and those vector orbits create
the orbital lobes through integration.'
Anchors: shell S^2_T, lab Larmor about X = latitude circles X=const
(hydrogen-radial REPORT sec.7); multiplet ring T=j+1/2, X_m = m+1/2
(2026-10-06 orbital map); |L| = GM = sqrt(j(j+1)) (v14.620).
Candidates:
 A) per-state Larmor ring on the shell, projected to unit sphere.
 B) vector model: r-hat sweeps the plane perp to L (circular orbit,
    uniform dwell) while L precesses about X on its cone; integrate
    over both phases -> theta-profile of the direction density.
    Cone angle: (a) cone anchors cos a = (m+1/2)/(j+1/2);
                (b) textbook    cos a = m/sqrt(j(j+1)).
Compare with |Y_jm|^2 theta-marginals (probability per unit theta)."""
import numpy as np
from scipy.special import sph_harm

def lobe_profile(j, m, ntheta=361):
    th = np.linspace(0, np.pi, ntheta)
    Y = sph_harm(m, j, np.zeros_like(th), th)     # phi=0 slice
    p = np.abs(Y)**2 * 2*np.pi*np.sin(th)          # theta-marginal
    return th, p/np.trapz(p, th)

def ring_alpha_cone(j, m):
    return np.degrees(np.arccos((m+0.5)/(j+0.5)))

def integrated_profile(j, m, convention, n1=1440, n2=1440, ntheta=361):
    if convention == 'cone':
        ca = (m+0.5)/(j+0.5)
    else:
        ca = m/np.sqrt(j*(j+1.0))
    a = np.arccos(np.clip(ca, -1, 1))
    # L precesses about X axis: L = (ca, sa cos p2, sa sin p2)
    # r-hat uniform on circle perp to L: r = cos p1 * e1 + sin p1 * e2
    p2 = np.linspace(0, 2*np.pi, n2, endpoint=False)
    sa = np.sin(a)
    L = np.stack([np.full_like(p2, ca), sa*np.cos(p2), sa*np.sin(p2)], 1)
    e1 = np.stack([-np.full_like(p2, sa), ca*np.cos(p2), ca*np.sin(p2)], 1)
    e2 = np.cross(L, e1)
    p1 = np.linspace(0, 2*np.pi, n1, endpoint=False)
    # accumulate cos(theta) of r over the (p1,p2) grid in blocks over p2
    cbins = np.linspace(-1, 1, ntheta)
    hist = np.zeros(ntheta-1)
    for k in range(n2):
        r = (np.cos(p1)[:, None]*e1[k] + np.sin(p1)[:, None]*e2[k])
        hist += np.histogram(r[:, 0], bins=cbins)[0]
    c = 0.5*(cbins[:-1] + cbins[1:])
    du = cbins[1] - cbins[0]
    h = hist/(hist.sum()*du)               # density per unit u=cos(theta)
    th = np.arccos(c)
    p = h*np.sin(th)                        # theta-marginal
    p = p/np.trapz(p[::-1], th[::-1])
    return th[::-1], p[::-1], np.degrees(a)

print('=== A) Larmor rings (cone anchors) vs |Y_jm|^2 maxima ===')
for j in (1, 2):
    for m in range(-j, j+1):
        th, p = lobe_profile(j, m)
        peak = np.degrees(th[np.argmax(p*np.sin(th)**0 + 0*p + (p>0))]) if False else None
        # lobe maxima of |Y|^2 itself (surface density, not marginal):
        Y2 = np.abs(sph_harm(m, j, np.zeros_like(th), th))**2
        mx = np.degrees(th[np.argmax(Y2)])
        print(f'j={j} m={m:+d}: ring alpha={ring_alpha_cone(j,m):7.2f} deg   '
              f'|Y|^2 max at theta={mx:6.1f} deg')

print()
print('=== B) integrated vector-model profiles ===')
for j in (1, 2):
    for m in range(-j, j+1):
        thq, pq = lobe_profile(j, m)
        for conv in ('cone', 'textbook'):
            th, p, adeg = integrated_profile(j, m, conv, n1=720, n2=720)
            pk = np.degrees(th[np.argmax(p)])
            l1 = np.trapz(np.abs(p - np.interp(th, thq, pq)), th)
            print(f'j={j} m={m:+d} [{conv:8s}] cone-angle={adeg:7.2f}  '
                  f'integrated peak theta={pk:6.1f}  L1 vs |Y_jm|^2 marginal={l1:.3f}')
