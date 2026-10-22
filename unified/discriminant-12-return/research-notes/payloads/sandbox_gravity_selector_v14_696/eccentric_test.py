"""Eccentric phase integration — CORRECTED producer (2026-10-22, erratum
to v14.696; Audit R330 finding). The original deposit's version of
this file contained only a docstring; the computation had run inline
and was never saved. This is the real producer.

Construction: I_jm(th; rho) = (1/2pi) int e^{-im chi}
(cos th + i rho sin th cos chi)^j dchi, rho = sqrt((1-e)/(1+e)),
evaluated EXACTLY by the binomial/moment sum (moments
(1/2pi) int e^{-imx} cos^k x dx = 2^-k C(k,(k-m)/2) for k=m mod 2),
with quadrature spot-checks. Compared against P_j^m(cos th).

FINDINGS (e = 0.6, rho = 0.5), correcting the original claim:
- (j=1, m=0) is INVARIANT: I = cos th exactly at every rho — the
  k=1 term's moment vanishes. The originally quoted "0.64-0.99 for
  j=1,m=0" was measured against a squashed-ANGLE Legendre function
  and does NOT describe deformation of the integral. Retracted.
- m = j states rescale in AMPLITUDE only (factor rho^j).
- States with an even k>=2 moment at m=0, and mixed-parity states
  (3,1), deform in SHAPE: ratio to P_j^m(cos th) is theta-dependent.
So eccentricity genuinely deforms the family — through the k>=2
moments — but state by state, not uniformly."""
import numpy as np
from fractions import Fraction as Fr
from math import comb
from scipy.special import lpmv

def I_exact(j, m, th, rho):
    tot = 0j
    for k in range(m, j+1):
        if (k-m) % 2: continue
        M = Fr(comb(k, (k-m)//2), 2**k)
        tot += comb(j, k) * np.cos(th)**(j-k) * (1j*rho*np.sin(th))**k * float(M)
    return tot

def I_quad(j, m, th, rho, n=400001):
    chi = np.linspace(0, 2*np.pi, n)
    f = np.exp(-1j*m*chi)*(np.cos(th) + 1j*rho*np.sin(th)*np.cos(chi))**j
    return np.trapz(f, chi)/(2*np.pi)

rho = 0.5
ths = np.linspace(0.06, np.pi-0.06, 300)
print(f'e = 0.6 (rho = {rho}); ratio |I_jm(th;rho)| / |P_j^m(cos th)|, |P|>0.05 only')
for j in range(0, 4):
    for m in range(0, j+1):
        Iv = np.array([abs(I_exact(j, m, t, rho)) for t in ths])
        Pv = np.abs(lpmv(m, j, np.cos(ths)))
        mask = Pv > 0.05
        r = Iv[mask]/Pv[mask]
        spread = r.max()/r.min() if r.min() > 0 else np.inf
        from math import factorial
        c0 = factorial(j)/factorial(j+m)   # the rho=1 (e=0) constant of v14.680
        if spread >= 1.001:
            kind = 'SHAPE (theta-dependent ratio)'
        elif abs(r.mean() - c0) < 1e-6:
            kind = 'INVARIANT (ratio = e=0 constant)'
        else:
            kind = 'AMPLITUDE (constant ratio, rescaled)'
        print(f'  j={j} m={m}: ratio min {r.min():.4f} max {r.max():.4f}  -> {kind}')
print()
th = 0.7
print(f'quadrature spot-check (2,0) th={th}: exact {I_exact(2,0,th,rho):.12f}  quad {I_quad(2,0,th,rho):.12f}')
print(f'quadrature spot-check (3,1) th={th}: exact {I_exact(3,1,th,rho):.12f}  quad {I_quad(3,1,th,rho):.12f}')
ths2 = np.linspace(0.01, np.pi-0.01, 999)
err = max(abs(I_exact(1, 0, t, rho) - np.cos(t)) for t in ths2)
print(f'(1,0) invariance: max |I_10 - cos th| over 999 angles at rho=0.5: {err:.2e}')
