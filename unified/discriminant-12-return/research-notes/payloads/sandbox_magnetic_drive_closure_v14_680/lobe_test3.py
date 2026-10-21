"""Test 3: composed shell motion (REPORT sec.7): lab Larmor about X
composed with the Rabi drive about Y, r(t) = Rx(wL t) Ry(wR t) r0,
time-averaged density on the shell vs |Y_1m|^2 theta-marginals.
theta measured from the X (quantization) axis."""
import numpy as np
from scipy.special import sph_harm

def lobe_marginal(j, m, ntheta=361):
    th = np.linspace(0, np.pi, ntheta)
    Y = sph_harm(m, j, np.zeros_like(th), th)
    p = np.abs(Y)**2 * 2*np.pi*np.sin(th)
    return th, p/np.trapz(p, th)

def trajectory_profile(x0, wL=1.0, wR=(np.sqrt(5)-1)/2, T=4000.0, dt=0.02):
    n = int(T/dt)
    t = np.arange(n)*dt
    # r0 on the meridian (X,Y plane, W=0) at cone latitude x0 = X/T
    y0 = np.sqrt(max(0.0, 1-x0*x0))
    # Ry(wR t) r0 then Rx(wL t): build r(t) vectorized in chunks
    cbins = np.linspace(-1, 1, 361)
    hist = np.zeros(360)
    chunk = 200000
    for s in range(0, n, chunk):
        tt = t[s:s+chunk]
        cR, sR = np.cos(wR*tt), np.sin(wR*tt)
        # Ry rotates (X,W) plane? Use axes: state coords (X, Y, W);
        # Rabi about Y: rotates X<->W. Larmor about X: rotates Y<->W.
        x1 = cR*x0 + sR*0.0          # r0 has W=0
        w1 = -sR*x0 + cR*0.0
        y1 = np.full_like(tt, y0)
        cL, sL = np.cos(wL*tt), np.sin(wL*tt)
        y2 = cL*y1 - sL*w1
        # x stays x1 under Larmor about X
        hist += np.histogram(x1, bins=cbins)[0]
    c = 0.5*(cbins[:-1]+cbins[1:]); du = cbins[1]-cbins[0]
    h = hist/(hist.sum()*du)
    th = np.arccos(c); p = h*np.sin(th)
    o = np.argsort(th)
    return th[o], p[o]/np.trapz(p[o], th[o])

targets = {1: 'm=+1', 1/3: 'm=0', -1/3: 'm=-1'}
for x0, lab in targets.items():
    th, p = trajectory_profile(x0)
    pk = np.degrees(th[np.argmax(p)])
    line = f'start X/T={x0:+.3f} ({lab} cone point): profile peak theta={pk:5.1f}'
    for m in (1, 0, -1):
        tq, q = lobe_marginal(1, m)
        l1 = np.trapz(np.abs(p - np.interp(th, tq, q)), th)
        line += f' | L1 vs |Y_1{m}|^2 = {l1:.3f}'
    print(line)
# reference: what does a pure Rabi (no Larmor) meridian dwell give? (wL=0)
th, p = trajectory_profile(1.0, wL=0.0)
tq, q = lobe_marginal(1, 0)
print('pole start, Rabi only: peak theta=%.1f  L1 vs |Y_10|^2 = %.3f'
      % (np.degrees(th[np.argmax(p)]),
         np.trapz(np.abs(p - np.interp(th, tq, q)), th)))
