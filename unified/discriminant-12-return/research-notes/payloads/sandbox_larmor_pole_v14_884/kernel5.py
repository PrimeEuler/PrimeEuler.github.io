#!/usr/bin/env python3
"""Finite-Larmor retarded Maxwell seat kernel, v5 (production).

Bilinear in z; real-axis composite-Gauss radial grid; per-channel residue
correction (+2 pi i Res) for channels with Im(z + n alpha) < 0 gives the
retarded analytic continuation (validated against v14.874's F(z) closed form).

  Dhat(z;a,b) = -1/4 + 6 pi^{3/2} [ sum_{n,i} W_i (z^2 H2 + z ab H1 + ab^2 H0)_{n,i}
                / (p_i^2 - (z+n a)^2)
                + sum_{n: Im nu_n<0} 2 pi i * nu_n e^{-nu_n^2} Hnum_n(nu_n) / (2 (2pi)^3) ]

H_j: angular contractions of numerator coefficients (DERIVATION.md).
"""
import numpy as np
from scipy.special import jv
from numpy.polynomial.legendre import leggauss

EDGES = [0, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 5, 6, 7.5, 9, 11.0]

def _panels(edges, nper):
    xs, ws = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        x, w = leggauss(nper)
        xs.append(0.5*(b-a)*x + 0.5*(a+b)); ws.append(0.5*(b-a)*w)
    return np.concatenate(xs), np.concatenate(ws)

def _coeffs(beta, n, rho, PHI):
    """C0, C1, C2 numerator coefficient fields on a (mu, phi) shaped grid."""
    def bb(nn, sharp=False):
        J = jv(nn, rho)
        return (np.exp(-1j*nn*PHI)*(1j)**nn*J) if sharp else (np.exp(1j*nn*PHI)*(-1j)**nn*J)
    bn, bns = bb(n), bb(n, True)
    bm, bp = bb(n-1), bb(n+1); bms, bps = bb(n-1, True), bb(n+1, True)
    ey, ez = 0.5*(-1j*bm + 1j*bp), 0.5*(bm + bp)
    eys, ezs = 0.5*(1j*bms - 1j*bps), 0.5*(bms + bps)
    return bn, bns, ey, ez, eys, ezs

def _Hnum(beta, n, p, z, ab, xm, wm, phi, wphi):
    MU, PHI = np.meshgrid(xm, phi, indexing='ij')
    sq = np.sqrt(np.maximum(0.0, 1-MU**2))
    bn, bns, ey, ez, eys, ezs = _coeffs(beta, n, beta*p*sq, PHI)
    de = sq*np.cos(PHI)*ey + sq*np.sin(PHI)*ez
    des = sq*np.cos(PHI)*eys + sq*np.sin(PHI)*ezs
    px = p*MU
    C2 = bn*bns*(1-MU**2)
    C1 = px*(-MU*(bn*des + bns*de))
    C0 = px**2*(ey*eys + ez*ezs - de*des)
    return np.sum(wm[:, None]*wphi*(z*z*C2 + z*ab*C1 + ab*ab*C0))

class Kernel5:
    def __init__(self, beta, N=None, nmu=40, nphi=72, nper=20, edges=EDGES):
        self.beta = beta
        self.N = N if N is not None else int(np.ceil(beta*4 + 14))
        self.p, self.wp = _panels(edges, nper)
        self.xm, self.wm = leggauss(nmu)
        self.phi = np.linspace(0, 2*np.pi, nphi, endpoint=False); self.wphi = 2*np.pi/nphi
        nrad = len(self.p); N = self.N
        MU, PHI = np.meshgrid(self.xm, self.phi, indexing='ij')
        sq = np.sqrt(np.maximum(0.0, 1-MU**2))
        w2 = self.wm[:, None]*self.wphi
        H0 = np.zeros((2*N+1, nrad), dtype=complex)
        H1 = np.zeros_like(H0); H2 = np.zeros_like(H0)
        for i, pi in enumerate(self.p):
            rho = beta*pi*sq
            px = pi*MU
            for n in range(-N, N+1):
                bn, bns, ey, ez, eys, ezs = _coeffs(beta, n, rho, PHI)
                de = sq*np.cos(PHI)*ey + sq*np.sin(PHI)*ez
                des = sq*np.cos(PHI)*eys + sq*np.sin(PHI)*ezs
                H2[n+N, i] = np.sum(w2*bn*bns*(1-MU**2))
                H1[n+N, i] = np.sum(w2*px*(-MU*(bn*des + bns*de)))
                H0[n+N, i] = np.sum(w2*px**2*(ey*eys + ez*ezs - de*des))
        self.H0, self.H1, self.H2 = H0, H1, H2
        self.ns = np.arange(-N, N+1)
        self.W = self.wp * self.p**2 * np.exp(-self.p**2) / (2*np.pi)**3

    def Dhat(self, z, alpha):
        ab = alpha*self.beta
        num = (z*z)*self.H2 + (z*ab)*self.H1 + (ab*ab)*self.H0
        den = self.p[None, :]**2 - (z + self.ns*alpha)[:, None]**2
        tot = np.sum(self.W[None, :] * num/den)
        for n in self.ns:
            nu = z + n*alpha
            if nu.imag < 0:
                Hn = _Hnum(self.beta, int(n), nu, z, ab, self.xm, self.wm, self.phi, self.wphi)
                tot += 2j*np.pi * (nu*np.exp(-nu*nu)*Hn/2) / (2*np.pi)**3
        return -0.25 + 6*np.pi**1.5 * tot
