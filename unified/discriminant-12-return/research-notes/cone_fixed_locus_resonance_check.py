#!/usr/bin/env python3
"""
Reproducer for v13.917:
  1) fixed-locus theta/Casimir cosine-transform zeros for zeta;
  2) chi_12 fixed-locus theta cosine-transform zeros.

Requires: mpmath
"""

import mpmath as mp

mp.mp.dps = 50


def phi_xi(r):
    r = abs(mp.mpf(r))
    total = mp.mpf("0")
    n = 1
    while True:
        term = (
            4 * mp.pi**2 * n**4 * mp.e**(mp.mpf("4.5") * r)
            - 6 * mp.pi * n**2 * mp.e**(mp.mpf("2.5") * r)
        ) * mp.e**(-mp.pi * n**2 * mp.e**(2 * r))
        total += term
        if n > 3 and abs(term) < mp.mpf("1e-60"):
            break
        n += 1
        if n > 300:
            raise RuntimeError("phi_xi series failed to converge")
    return total


def Xi_from_fixed_locus(gamma):
    f = lambda r: 2 * phi_xi(r) * mp.cos(gamma * r)
    return mp.quad(f, [0, .25, .5, .75, 1, 1.25, 1.5, 2, 3])


def chi12(n):
    a = int(n) % 12
    if a in (1, 11):
        return 1
    if a in (5, 7):
        return -1
    return 0


def theta_chi12(x):
    x = mp.mpf(x)
    total = mp.mpf("0")
    n = 1
    while True:
        env = mp.e**(-mp.pi * n * n * x / 12)
        total += 2 * chi12(n) * env
        if n > 20 and env < mp.mpf("1e-60"):
            break
        n += 1
        if n > 2000:
            raise RuntimeError("theta_chi12 series failed to converge")
    return total


def K_chi12(r):
    r = abs(mp.mpf(r))
    return mp.e**(r / 2) * theta_chi12(mp.e**(2 * r))


def L_chi12(s):
    return 12**(-s) * (
        mp.zeta(s, mp.mpf(1) / 12)
        - mp.zeta(s, mp.mpf(5) / 12)
        - mp.zeta(s, mp.mpf(7) / 12)
        + mp.zeta(s, mp.mpf(11) / 12)
    )


def Lambda_chi12(s):
    return (12 / mp.pi)**(s / 2) * mp.gamma(s / 2) * L_chi12(s)


def Lambda_chi12_from_fixed_locus(gamma):
    f = lambda r: 2 * K_chi12(r) * mp.cos(gamma * r)
    return mp.quad(f, [0, .25, .5, .75, 1, 1.5, 2, 3])


def Z_chi12(t):
    return mp.re(Lambda_chi12(mp.mpf("0.5") + 1j * t))


print("zeta fixed-locus/Casimir resonance check")
for k in range(1, 6):
    g = mp.im(mp.zetazero(k))
    residual = abs(Xi_from_fixed_locus(g))
    print(k, mp.nstr(g, 25), mp.nstr(residual, 8))

print("\nchi12 fixed-locus resonance check")
seeds = [
    mp.mpf("3.804628"),
    mp.mpf("6.692223"),
    mp.mpf("8.890593"),
    mp.mpf("11.188393"),
    mp.mpf("12.966179"),
    mp.mpf("15.181481"),
]
for k, seed in enumerate(seeds, 1):
    g = mp.findroot(Z_chi12, (seed - mp.mpf(".01"), seed + mp.mpf(".01")))
    residual = abs(Lambda_chi12_from_fixed_locus(g))
    print(k, mp.nstr(g, 25), mp.nstr(residual, 8))
