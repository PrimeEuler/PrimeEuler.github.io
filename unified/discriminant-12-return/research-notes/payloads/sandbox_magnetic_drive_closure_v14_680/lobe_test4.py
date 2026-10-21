"""Test 4 (Jeremy's correction, 2026-10-21): integrate over the PHASE
ANGLE. Larmor vector = complex null vector in the shell coords (X,Y,W),
w(chi) = (1, i cos chi, i sin chi), precessing about X with phase chi.
Lobe amplitude = phase-weighted orbit integral (Schlaefli/Laplace-Heine):
  I_jm(theta) = (1/2pi) int_0^2pi e^{-i m chi} (cos t + i sin t cos chi)^j dchi
Test: I_jm(theta) / P_j^m(cos theta) constant in theta for all (j,m),
and |I_jm|^2 theta-marginal == |Y_jm|^2 theta-marginal."""
import numpy as np
from scipy.special import lpmv, sph_harm

NCHI = 4096
chi = np.linspace(0, 2*np.pi, NCHI, endpoint=False)
dchi = 2*np.pi/NCHI
th = np.linspace(0.02, np.pi-0.02, 200)
cth, sth = np.cos(th), np.sin(th)

def I_jm(j, m):
    # integrand: e^{-im chi} (cth + i sth cos chi)^j   [theta x chi grid]
    base = cth[:, None] + 1j*sth[:, None]*np.cos(chi)[None, :]
    integ = np.exp(-1j*m*chi)[None, :] * base**j
    return integ.sum(axis=1)*dchi/(2*np.pi)

def lobe_marginal_from_amp(amp):
    p = np.abs(amp)**2 * 2*np.pi*np.sin(th)
    return p/np.trapz(p, th)

def lobe_marginal_Y(j, m):
    Y = sph_harm(m, j, np.zeros_like(th), th)
    p = np.abs(Y)**2 * 2*np.pi*np.sin(th)
    return p/np.trapz(p, th)

print(f'{"(j,m)":>7} {"ratio |I/P|":>12} {"rel.dev.":>10} {"L1 |I|^2 vs |Y|^2":>18}')
worst = 0.0
for j in range(0, 4):
    for m in range(-j, j+1):
        I = I_jm(j, m)
        P = lpmv(abs(m), j, cth)          # P_j^|m|
        mask = np.abs(P) > 0.05*np.max(np.abs(P))
        ratio = np.abs(I[mask]/P[mask])
        rel = ratio.std()/ratio.mean()
        l1 = np.trapz(np.abs(lobe_marginal_from_amp(I) - lobe_marginal_Y(j, m)), th)
        worst = max(worst, rel, l1)
        print(f'({j},{m:+d}) {ratio.mean():12.6f} {rel:10.2e} {l1:18.2e}')
print(f'\nworst relative deviation / L1 across all (j,m): {worst:.2e}')
