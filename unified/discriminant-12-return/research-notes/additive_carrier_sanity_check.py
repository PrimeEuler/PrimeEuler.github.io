"""External audit (Round 147) independent sanity check of v13.963 Track 1's
basic arithmetic claims: omega(n) (distinct prime factors) and Omega(n)
(prime factors with multiplicity), computed by a linear-sieve-style smallest-
prime-factor array, cross-checked against direct trial-division factorization,
and checked against the classical Hardy-Ramanujan mean ~ log log n.

This does not attempt to reproduce the sandbox's R-statistic/log-FFT pipeline
(not posted, per the standing firewall) -- only the underlying arithmetic
sequences it operates on.

Fresh implementation, not reusing anything from the ledger entry.
"""
import math
import numpy as np


def sieve_omega_Omega(n_max):
    spf = np.zeros(n_max + 1, dtype=np.int64)  # smallest prime factor
    omega = np.zeros(n_max + 1, dtype=np.int32)
    Omega = np.zeros(n_max + 1, dtype=np.int32)
    for i in range(2, n_max + 1):
        if spf[i] == 0:  # i is prime
            for j in range(i, n_max + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    for n in range(2, n_max + 1):
        m = n
        distinct = 0
        total = 0
        while m > 1:
            p = spf[m]
            cnt = 0
            while m % p == 0:
                m //= p
                cnt += 1
            distinct += 1
            total += cnt
        omega[n] = distinct
        Omega[n] = total
    return omega, Omega


def direct_factor_omega_Omega(n):
    m = n
    distinct = 0
    total = 0
    p = 2
    while p * p <= m:
        if m % p == 0:
            cnt = 0
            while m % p == 0:
                m //= p
                cnt += 1
            distinct += 1
            total += cnt
        p += 1
    if m > 1:
        distinct += 1
        total += 1
    return distinct, total


if __name__ == '__main__':
    N = 200_000
    omega, Omega = sieve_omega_Omega(N)

    # cross-check against direct factorization on a sample
    mismatches = 0
    for n in [2, 3, 4, 12, 16, 60, 97, 1024, 999, 123456, 199999]:
        d_o, d_O = direct_factor_omega_Omega(n)
        if d_o != omega[n] or d_O != Omega[n]:
            mismatches += 1
            print(f"MISMATCH at n={n}: sieve=({omega[n]},{Omega[n]}) direct=({d_o},{d_O})")
    print(f"Cross-check vs direct factorization: {mismatches} mismatches out of 11 sampled n.")

    for n_max in [10_000, 100_000, 200_000]:
        mean_omega = omega[2:n_max + 1].mean()
        mean_Omega = Omega[2:n_max + 1].mean()
        loglog = math.log(math.log(n_max))
        print(f"N={n_max}: mean omega={mean_omega:.4f}  mean Omega={mean_Omega:.4f}  "
              f"log(log(N))={loglog:.4f}")
