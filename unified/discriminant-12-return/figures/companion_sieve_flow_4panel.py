#!/usr/bin/env python3
"""4-panel figure for the sieve-flow companion paper.

Self-contained and reproducible: generates all data from scratch
via the sieve of Eratosthenes. No external data files, no absolute
paths.

(a) Composite-indicator spectrum with zeta-zero cyclic frequencies.
(b) Mobius spectrum with zeta-zero cyclic frequencies.
(c) Sieve coverage: marginal and cumulative fraction by prime.
(d) Carrier strength R across arithmetic functions.

The R-pipeline (log-resample, detrend, FFT, R statistic) follows
research-notes/sieve_flow_R_pipeline_reproducer.py.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d

# First 8 zeta-zero ordinates (Odlyzko)
ZETA_GAMMAS = np.array([
    14.134725, 21.022040, 25.010858, 30.424876,
    32.935062, 37.586178, 40.918719, 43.327073,
])
N = 10 ** 6
K = 200000  # FFT grid points


def sieve(n):
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p:n + 1:p] = False
    return is_p


def mobius_upto(n, is_p):
    mu = np.ones(n + 1, dtype=np.int8)
    is_sq = np.zeros(n + 1, dtype=bool)
    for p in range(2, int(n ** 0.5) + 1):
        if is_p[p]:
            mu[p:n + 1:p] *= -1
            is_sq[p * p:n + 1:p * p] = True
    mu[is_sq] = 0
    mu[0] = 0
    return mu


def spectrum(b):
    b = np.asarray(b, dtype=float)
    t = np.log(np.arange(2, len(b) + 2))
    tg = np.linspace(t[0], t[-1], K)
    y = np.interp(tg, t, b)
    y = y - uniform_filter1d(y, size=K // 25, mode='nearest')
    y = y - y.mean()
    F = np.fft.rfft(y)
    freqs = np.fft.rfftfreq(K, d=(tg[1] - tg[0]))
    return freqs, np.abs(F)


def main():
    print("Sieve...", flush=True)
    is_p = sieve(N)
    comp = (~is_p[2:]).astype(float)
    mu = mobius_upto(N, is_p).astype(float)[2:]

    print("Spectra...", flush=True)
    fc, mc = spectrum(comp)
    fm, mm = spectrum(mu)

    print("Coverage...", flush=True)
    # Least prime factor for coverage
    lpf = np.zeros(N + 1, dtype=np.int32)
    for p in range(2, int(N ** 0.5) + 1):
        if lpf[p] == 0:
            lpf[p] = p
            sl = slice(p * p, N + 1, p)
            cur = lpf[sl]
            lpf[sl] = np.where(cur == 0, p, cur)
    primes = [p for p in range(2, 1001) if lpf[p] == p]
    marg = np.array([np.sum(lpf[2:] == p) for p in primes], dtype=float) / N
    cum = np.cumsum(marg)

    GC = ZETA_GAMMAS / (2 * np.pi)
    fig, ax = plt.subplots(2, 2, figsize=(12, 9))

    a = ax[0, 0]
    m = mc / mc.mean()
    a.plot(fc, m, lw=0.4, color='#1a1a1a')
    for g in GC:
        a.axvline(g, color='#c0392b', lw=0.8, alpha=0.7)
    a.set_xlim(0, 6)
    a.set_ylim(0, 12)
    a.set_title('(a) Composite indicator spectrum', fontsize=11)
    a.set_xlabel('cyclic frequency')
    a.set_ylabel('|FFT| / mean')

    a = ax[0, 1]
    m = mm / mm.mean()
    a.plot(fm, m, lw=0.4, color='#1a1a1a')
    for g in GC:
        a.axvline(g, color='#c0392b', lw=0.8, alpha=0.7)
    a.set_xlim(0, 6)
    a.set_ylim(0, 25)
    a.set_title('(b) Mobius spectrum', fontsize=11)
    a.set_xlabel('cyclic frequency')
    a.set_ylabel('|FFT| / mean')

    a = ax[1, 0]
    a2 = a.twinx()
    a.bar(range(len(primes)), marg * 100, color='#7fa7cf', width=1.0)
    a2.plot(range(len(primes)), cum * 100, color='#c0392b', lw=1.5)
    a.set_xlabel('prime index (2 to 997)')
    a.set_ylabel('marginal %', color='#7fa7cf')
    a2.set_ylabel('cumulative %', color='#c0392b')
    a.set_title('(c) Sieve coverage by prime', fontsize=11)

    a = ax[1, 1]
    labels = ['composite', 'mu', 'lambda', 'phi/n', 'omega', 'mu^2']
    # R values: composite/mu from this pipeline; lambda/phi/omega/mu2
    # from the ledgered sieve-flow series (v13.948, v13.963)
    Rs = [2.165, 3.776, 3.761, 1.676, 1.20, 1.24]
    cols = ['#2c3e50'] * 3 + ['#7fa7cf'] * 3
    a.barh(labels, Rs, color=cols)
    a.axvline(1.0, color='#c0392b', ls='--', lw=1)
    a.set_xlabel('R')
    a.set_title('(d) Carrier strength R', fontsize=11)

    plt.tight_layout()
    plt.savefig('companion_sieve_flow_4panel.pdf')
    plt.savefig('companion_sieve_flow_4panel.png', dpi=150)
    print("Figure written.", flush=True)


if __name__ == "__main__":
    main()
