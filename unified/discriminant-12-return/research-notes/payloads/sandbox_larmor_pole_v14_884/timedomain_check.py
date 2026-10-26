#!/usr/bin/env python3
"""Independent time-domain (v14.881 sinc route) evaluation of Dhat.

Sector angular factors from tensor derivatives of I(Dc) = 4 pi sinc(k|Dc|),
computed by finite differences of I in 3D (Dc_x = 0 on shell, derivatives
taken in 3D). Propagator: int_0^inf e^{iz tau} sin(k tau)/k dtau = 1/(k^2-z^2)
(Im z>0), which fixes the overall factor 6 pi^{3/2} exactly (alpha=0 anchor
reproduces z^2 F(z) analytically). Brute-force (mu,phi,t) quadrature spots
verify the sector assembly; t-independence of sectors is checked numerically.
"""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sweep import load_kernel
import mpmath as mp

def I3(D, k):
    """4 pi sinc(k|D|) for D array (...,3); k scalar or array broadcast."""
    d = np.sqrt(np.sum(D**2, axis=-1))
    u = k*d
    s = np.where(np.abs(u) < 1e-8, 1 - u**2/6, np.sin(u)/np.where(np.abs(u) < 1e-8, 1, u))
    return 4*np.pi*s

def hessian_I(D0, k, h=1.5e-3):
    """Hessian of I at points D0 (...,3) via 5-point FD per direction pair."""
    D0 = np.asarray(D0, dtype=float)
    shp = D0.shape[:-1]
    H = np.zeros(shp + (3, 3))
    for i in range(3):
        ei = np.eye(3)[i]
        fp2 = I3(D0 + 2*h*ei, k); fp1 = I3(D0 + h*ei, k)
        f0 = I3(D0, k)
        fm1 = I3(D0 - h*ei, k); fm2 = I3(D0 - 2*h*ei, k)
        H[..., i, i] = (-fp2 + 16*fp1 - 30*f0 + 16*fm1 - fm2)/(12*h*h)
        for j in range(i+1, 3):
            ej = np.eye(3)[j]
            fpp = I3(D0 + h*ei + h*ej, k); fpm = I3(D0 + h*ei - h*ej, k)
            fmp = I3(D0 - h*ei + h*ej, k); fmm = I3(D0 - h*ei - h*ej, k)
            H[..., i, j] = H[..., j, i] = (fpp - fpm - fmp + fmm)/(4*h*h)
    return H

def d3_I(D0, k, h=2e-3):
    """T3[i,j,l] = d_i d_j d_l I at D0: differentiate Hessian field in l."""
    shp = np.asarray(D0).shape[:-1]
    T = np.zeros(shp + (3, 3, 3))
    for l in range(3):
        el = np.eye(3)[l]
        Hp = hessian_I(D0 + h*el, k); Hm = hessian_I(D0 - h*el, k)
        T[..., :, :, l] = (Hp - Hm)/(2*h)
    return T

def d4_I(D0, k, h=2.5e-3):
    """T4[i,j,l,m]: second x-derivative of Hessian_jl field."""
    shp = np.asarray(D0).shape[:-1]
    ex = np.eye(3)[0]
    Hp = hessian_I(D0 + h*ex, k); H0 = hessian_I(D0, k); Hm = hessian_I(D0 - h*ex, k)
    d2x_H = (Hp - 2*H0 + Hm)/(h*h)   # [.., j, l] = d_x d_x d_j d_l I
    return d2x_H

def sectors(k, tau, z, alpha, beta, t=0.7):
    """S_aa, S_ab(+ba), S_bb at scalar k, tau (arrays broadcast)."""
    k = np.asarray(k, float); tau = np.asarray(tau, float)
    kk, tt = np.broadcast_arrays(k, tau)
    zz = np.zeros_like(tt)
    ct = np.stack([zz, beta*np.cos(alpha*t) + zz, beta*np.sin(alpha*t) + zz], -1)
    cp = np.stack([zz, beta*np.cos(alpha*(t-tt)), beta*np.sin(alpha*(t-tt))], -1)
    Dc = ct - cp
    vt = np.stack([zz, -alpha*beta*np.sin(alpha*t) + zz, alpha*beta*np.cos(alpha*t) + zz], -1)
    vp = np.stack([np.zeros_like(tt), -alpha*beta*np.sin(alpha*(t-tt)), alpha*beta*np.cos(alpha*(t-tt))], -1)
    I0 = I3(Dc, kk)
    H = hessian_I(Dc, kk)
    T3 = d3_I(Dc, kk)
    d2xH = d4_I(Dc, kk)
    Saa = z*z*(I0 + H[..., 0, 0]/kk**2)
    vsum = vt + vp
    Sab = (1j*z/kk**2) * np.sum(vsum * T3[..., 0, 0, :], axis=-1)
    vvp = np.sum(vt*vp, axis=-1)
    term2 = np.einsum('...j,...l,...jl->...', vt, vp, d2xH)/kk**2
    Sbb = -(H[..., 0, 0]*vvp) - term2 + 0*kk  # k^2 * [ -(1/k^2) Hxx (v.v') - (1/k^2) T4term ]... see note
    # NOTE: S_bb = k^2 * (v.v') * (-(1/k^2) Hxx) - k^2 * v_j v'_l (1/k^4) T4_xxjl
    #            = -(v.v') Hxx - (1/k^2) v_j v'_l d2xH_jl
    return Saa, Sab, Sbb

def brute_sector(k, tau, z, alpha, beta, t=0.7, nmu=28, nphi=56, nt=40):
    """Direct (mu, phi, t) quadrature of the sector definitions at scalar k, tau."""
    from numpy.polynomial.legendre import leggauss
    xm, wm = leggauss(nmu)
    phi = np.linspace(0, 2*np.pi, nphi, endpoint=False); wphi = 2*np.pi/nphi
    ts = np.linspace(0, 2*np.pi/alpha, nt, endpoint=False); wt = (2*np.pi/alpha)/nt
    MU, PHI, TT = np.meshgrid(xm, phi, ts, indexing='ij')
    sq = np.sqrt(1-MU**2)
    khat = np.stack([MU, sq*np.cos(PHI), sq*np.sin(PHI)], -1)
    def cv(tt):
        return np.stack([np.zeros_like(tt), beta*np.cos(alpha*tt), beta*np.sin(alpha*tt)], -1)
    def vv(tt):
        return np.stack([np.zeros_like(tt), -alpha*beta*np.sin(alpha*tt), alpha*beta*np.cos(alpha*tt)], -1)
    c1, c2 = cv(TT), cv(TT-tau)
    v1, v2 = vv(TT), vv(TT-tau)
    ph1 = np.exp(-1j*k*np.sum(khat*c1, -1))   # e^{-ik.c(t)}
    ph2 = np.exp(1j*k*np.sum(khat*c2, -1))    # e^{+ik.c(t-tau)} (sharp partner)
    kx = k*MU
    PT = lambda U, W: np.sum(U*W, -1) - np.sum(khat*U, -1)*np.sum(khat*W, -1)  # bilinear: W is already the sharp partner
    xhat = np.zeros_like(khat); xhat[..., 0] = 1.0
    Aa = -1j*z*ph1[..., None]*xhat
    Ab = -1j*kx[..., None]*ph1[..., None]*v1
    Aa_s = 1j*z*ph2[..., None]*xhat
    Ab_s = 1j*kx[..., None]*ph2[..., None]*v2
    w3 = wm[:, None, None]*wphi*wt
    # int dOmega <f>_t = sum(w3 * f) / period   (sum w3 = 4 pi * period)
    period = 2*np.pi/alpha
    Saa = np.sum(w3*PT(Aa, Aa_s))/period
    Sab = np.sum(w3*(PT(Aa, Ab_s) + PT(Ab, Aa_s)))/period
    Sbb = np.sum(w3*PT(Ab, Ab_s))/period
    return Saa, Sab, Sbb

def Dhat_time(z, alpha, beta, nk=260, ntau=1600, taumax=80.0):
    ks = np.linspace(0.02, 8.0, nk)
    taus = np.linspace(0.0, taumax, ntau)
    dk = ks[1]-ks[0]; dtau = taus[1]-taus[0]
    K, T = np.meshgrid(ks, taus, indexing='ij')
    Saa, Sab, Sbb = sectors(K, T, z, alpha, beta)
    S = Saa + Sab + Sbb
    integ = np.exp(-K**2) * (np.sin(K*T)/K) * S * K**2/(2*np.pi)**3
    rad = np.trapz(integ, dx=dk, axis=0)
    return -0.25 + 6*np.pi**1.5 * np.trapz(rad*np.exp(1j*z*taus), dx=dtau)

def F(z):
    return 1+1j*np.sqrt(np.pi)*z*np.exp(-z*z)*complex(mp.erfc(-1j*z))

if __name__ == "__main__":
    print("== sector spot checks vs brute force ==")
    rng = np.random.default_rng(3)
    for (alpha, beta) in ((0.35, 1.0), (0.2, 2.0)):
        for _ in range(3):
            k = rng.uniform(0.4, 3.0); tau = rng.uniform(0.5, 9.0); z = 0.35+0.05j
            s1 = sectors(k, tau, z, alpha, beta)
            s2 = brute_sector(k, tau, z, alpha, beta)
            print(f"a={alpha} b={beta} k={k:.2f} tau={tau:.2f}: FD={[f'{x:.4f}' for x in s1]} brute={[f'{x:.4f}' for x in s2]}")
    print("== t-independence of FD sectors ==")
    for t in (0.0, 1.3, 2.9):
        print(t, sectors(1.7, 4.2, 0.35+0.05j, 0.35, 1.0, t=t))
    print("== alpha=0 anchor vs F ==")
    for z in (0.3+0.05j, 0.45+0.05j):
        got = Dhat_time(z, 0.0, 1.0); want = -0.25 + z*z*F(z)
        print(f"z={z}: time={got:.8f} closed={want:.8f} diff={abs(got-want):.2e}")
    print("== finite alpha vs kernel5 ==")
    for (beta, alpha) in ((1.0, 0.35), (2.0, 0.2)):
        K = load_kernel(beta)
        for z in (0.3+0.05j, 0.45+0.05j):
            gt = Dhat_time(z, alpha, beta); gk = K.Dhat(z, alpha)
            print(f"beta={beta} alpha={alpha} z={z}: time={gt:.8f} harm={gk:.8f} diff={abs(gt-gk):.2e}")
