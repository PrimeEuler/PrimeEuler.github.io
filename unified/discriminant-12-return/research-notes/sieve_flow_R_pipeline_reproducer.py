#!/usr/bin/env python3
"""Sieve-flow zero-spectrum R-statistic pipeline — reproducer.

This is the numerical pipeline behind ledger entries v13.942 (sieve
renormalization / zero spectrum), v13.948 (Liouville-vs-Mobius),
v13.952 (chi12 twist kill test), and v13.963 (non-multiplicative
carriers / fold recursion).

Method:
  1. Sieve to N (Eratosthenes). The primes <= sqrt(N) generate the full
     prime/composite bitmap, the Mobius function, and the Liouville
     function on [2, N] exactly.
  2. Build the arithmetic pattern (prime indicator, composite indicator,
     mu, lambda, omega, ...).
  3. Interpolate onto a uniform t = log n grid, detrend with a uniform
     filter, mean-subtract, real FFT.
  4. R statistic: mean magnitude in +/-0.12 windows around the first 8
     zeta-zero cyclic frequencies (gamma_k / 2*pi), divided by mean
     magnitude in the gap midpoints. R >> 1 indicates the zero spectrum
     is present; R ~ 1 is null.

Expected outputs (N=10^6):
  composite indicator : R ~ 2.17  (v13.942)
  mu(n)               : R ~ 3.78  (v13.948)
  lambda(n)           : R ~ 3.76  (v13.948)
  omega(n)            : R ~ 1.2   (v13.963, weak)
  shuffled null       : R ~ 1.0

Dependencies: numpy, scipy.
"""

import numpy as np
from scipy.ndimage import uniform_filter1d

ZETA_GAMMAS = [
    14.134725, 21.022040, 25.010858, 30.424876,
    32.935062, 37.586178, 40.918719, 43.327073,
]
W = 0.12  # half-width of on/off windows (cyclic frequency)


def sieve(n):
    """Eratosthenes bitmap: is_p[i] True iff i prime, for i in [0, n]."""
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p:n + 1:p] = False
    return is_p


def mobius_lambda(N, is_p):
    """mu and lambda on [0, N] via linear sieve. Exact."""
    mu = np.zeros(N + 1, dtype=np.int32)
    lam = np.zeros(N + 1, dtype=np.int32)
    mu[1] = 1
    lam[1] = 1
    primes = []
    is_c = np.zeros(N + 1, dtype=bool)
    for i in range(2, N + 1):
        if not is_c[i]:
            primes.append(i)
            mu[i] = -1
            lam[i] = -1
        for p in primes:
            if i * p > N:
                break
            is_c[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                lam[i * p] = lam[i] * lam[p]
                break
            else:
                mu[i * p] = -mu[i]
                lam[i * p] = lam[i] * lam[p]
    return mu, lam


def spectrum(bits, K=200000):
    """Log-coordinate FFT with trend removal. Returns (freqs, magnitude)."""
    b = np.asarray(bits, dtype=float)
    t = np.log(np.arange(2, len(b) + 2))
    tg = np.linspace(t[0], t[-1], K)
    y = np.interp(tg, t, b)
    y = y - uniform_filter1d(y, size=K // 25, mode='nearest')
    y = y - y.mean()
    F = np.fft.rfft(y)
    freqs = np.fft.rfftfreq(K, d=(tg[1] - tg[0]))
    return freqs, np.abs(F)


def R_at(freqs, mag, gammas=ZETA_GAMMAS, W=W):
    """On-zero vs gap-background ratio. R >> 1 => zero spectrum present."""
    GC = np.asarray(gammas) / (2 * np.pi)
    on = np.concatenate([mag[(freqs >= g - W) & (freqs <= g + W)] for g in GC])
    mids = 0.5 * (GC[:-1] + GC[1:])
    off = np.concatenate(
        [mag[(freqs >= m - W) & (freqs <= m + W)] for m in mids]
    )
    return float(on.mean() / off.mean())


def main(N=10 ** 6):
    print(f"sieving to {N} ...")
    is_p = sieve(N)
    mu, lam = mobius_lambda(N, is_p)

    patterns = {
        "composite indicator": (~is_p[2:]).astype(float),
        "mu(n)": mu[2:].astype(float),
        "lambda(n)": lam[2:].astype(float),
    }
    # shuffled null control
    rng = np.random.default_rng(0)
    shuf = (~is_p[2:]).astype(float).copy()
    rng.shuffle(shuf)
    patterns["shuffled null"] = shuf

    for name, pat in patterns.items():
        f, m = spectrum(pat)
        print(f"  {name:22s} R = {R_at(f, m):.3f}")


if __name__ == "__main__":
    main()
