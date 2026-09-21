#!/usr/bin/env python3
"""chi_-4 Suzuki screw kernel compressed to a finite Zeeman SU(2) carrier.

This is a construction/audit prototype, not a GRH proof and not yet a
finite-characteristic zero computation.

Arithmetic input:
    chi_-4(n) = 0 (n even), +1 (n=1 mod 4), -1 (n=3 mod 4)
    L(s,chi_-4) = beta(s)
    completed gamma argument on the critical line: 3/4 + it/2
    conductor q=4

The screw function is the direct primitive-character analogue of Suzuki v2
Eq. (1.3): no zeta pole term, chi_-4 twists every prime-power ramp, and the
archimedean/conductor term uses a=3/4 and q=4.

The finite carrier is the spin-j Zeeman basis |j,m>.  J_z supplies the ordered
nodes and J_x supplies the exact SU(2) nearest-neighbour weights
sqrt((j-m)(j+m+1))/2.  G_j is the literal sampled/Galerkin compression of the
continuous screw kernel g(x-y) to those nodes.

Important: eigenvalues of G_j are NOT asserted to be beta-zero ordinates.
Suzuki zeros arise from the self-adjoint-extension characteristic; that is the
next layer to build on this compressed kernel.
"""
from __future__ import annotations

from functools import lru_cache
from math import exp, log, sqrt
import numpy as np
import mpmath as mp


def chi4(n: int) -> int:
    r = n % 4
    return 1 if r == 1 else (-1 if r == 3 else 0)


def von_mangoldt_prime_powers(limit: float):
    """Yield (n, Lambda(n), chi4(n)) for prime powers n <= limit."""
    N = int(limit)
    if N < 2:
        return
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(sqrt(N)) + 1):
        if sieve[p]:
            sieve[p*p:N+1:p] = False
    for p in np.flatnonzero(sieve):
        pk = int(p)
        lp = log(int(p))
        while pk <= N:
            c = chi4(pk)
            if c:
                yield pk, lp, c
            if pk > N // int(p):
                break
            pk *= int(p)


@lru_cache(None)
def _lerch1(a_str: str):
    a = mp.mpf(a_str)
    return mp.zeta(2, a)  # Phi(1,2,a)


def g_chi4(t: float, dps: int = 50) -> float:
    """Primitive chi_-4 screw function in Suzuki's v2 normalization."""
    T = abs(float(t))
    if T == 0.0:
        return 0.0

    # Prime-power ramps: chi4(n) Lambda(n)/sqrt(n) (T-log n)_+.
    prime = 0.0
    for n, lam, c in von_mangoldt_prime_powers(exp(T)):
        prime += c * lam / sqrt(n) * (T - log(n))

    # Primitive odd character: q=4, gamma parameter a=(1+1/2)/2=3/4.
    # This is the exact analogue of Suzuki's zeta a=1/4 Lerch term, with
    # the conductor included in the linear coefficient.
    with mp.workdps(dps):
        TT = mp.mpf(T)
        a = mp.mpf(3) / 4
        z = mp.e**(-2*TT)
        phi1 = mp.zeta(2, a)
        phiz = mp.lerchphi(z, 2, a)
        linear = -TT/2 * (mp.digamma(a) + mp.log(mp.mpf(4)/mp.pi))
        lerch = -mp.mpf(1)/4 * (phi1 - mp.e**(-2*a*TT)*phiz)
        arch = linear + lerch

    return float(prime + arch)


def zeeman_carrier(two_j: int):
    """Return m, Jz, Jx for j=two_j/2 in the standard Jz basis."""
    j = two_j / 2.0
    d = two_j + 1
    m = np.arange(d, dtype=float) - j
    Jz = np.diag(m)
    Jx = np.zeros((d, d), dtype=float)
    for r in range(d - 1):
        mm = m[r]
        y = sqrt((j-mm)*(j+mm+1.0))
        Jx[r, r+1] = Jx[r+1, r] = 0.5*y
    return m, Jz, Jx


def trapezoid_weights(x):
    w = np.empty_like(x)
    if len(x) == 1:
        w[0] = 1.0
        return w
    w[0] = (x[1]-x[0])/2
    w[-1] = (x[-1]-x[-2])/2
    if len(x) > 2:
        w[1:-1] = (x[2:]-x[:-2])/2
    return w


def compress_kernel(two_j: int, A: float = 2.0):
    """Compress g_chi4(x-y) on [-A,A] to the Zeeman Jz grid."""
    m, Jz, Jx = zeeman_carrier(two_j)
    j = two_j/2.0
    if j == 0:
        x = np.array([0.0])
    else:
        x = A*m/j
    w = trapezoid_weights(x)
    G = np.empty((len(x), len(x)), dtype=float)
    for r, xr in enumerate(x):
        for s in range(r, len(x)):
            v = sqrt(w[r]*w[s]) * g_chi4(float(xr-x[s]))
            G[r, s] = G[s, r] = v
    return x, w, Jz, Jx, G


def audit(two_j: int = 12, A: float = 2.0):
    x, w, Jz, Jx, G = compress_kernel(two_j, A)
    j = two_j/2
    # SU(2) commutator check using Jy reconstructed from J+/-.
    # Casimir check is enough here: Jx^2+Jy^2+Jz^2=j(j+1)I.
    Jy = np.zeros_like(Jx, dtype=complex)
    for r in range(len(x)-1):
        y = 2*Jx[r,r+1]
        Jy[r,r+1] = -0.5j*y
        Jy[r+1,r] = 0.5j*y
    cas = Jx@Jx + Jy@Jy + Jz@Jz
    cas_err = np.linalg.norm(cas-j*(j+1)*np.eye(len(x)), ord=np.inf)
    even_err = max(abs(g_chi4(float(t))-g_chi4(float(-t)))
                   for t in np.linspace(0, 2*A, 17))
    sym_err = np.linalg.norm(G-G.T, ord=np.inf)
    print(f"j={j:g}, dim={len(x)}, A={A:g}")
    print("chi4 prime signs: 3->", chi4(3), "5->", chi4(5),
          "7->", chi4(7), "13->", chi4(13))
    print("g(0) =", g_chi4(0.0))
    print("max sampled evenness error =", even_err)
    print("SU(2) Casimir inf-norm error =", cas_err)
    print("compressed-kernel symmetry error =", sym_err)
    print("Jx edge weights =", np.diag(Jx,1))
    print("G eigenvalue range =", (np.linalg.eigvalsh(G)[0],
                                   np.linalg.eigvalsh(G)[-1]))


if __name__ == "__main__":
    audit()
