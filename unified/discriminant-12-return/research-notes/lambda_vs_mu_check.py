"""External audit (Round 144) independent check of v13.948's theoretical
backbone claims:
  1. Sigma lambda(n) n^-s = zeta(2s)/zeta(s) (classical identity, checked
     by hand in the write-up; this script checks the numerical consequences).
  2. The theoretical |zeta(1+2i*gamma_k)| modulation values for the first
     8 nontrivial zeta zeros, compared against the entry's claimed values.
  3. mean(lambda(n)) for n=2..10^6 -- includes the corrected linear sieve
     (lambda is COMPLETELY multiplicative, unlike mu, so the sieve's
     "stop early at p|i" shortcut used for mu's mu(p^2)=0 case must NOT be
     applied to lambda; this script's first (buggy) attempt confused the
     two and is documented in the audit write-up as a caught-and-fixed
     error).
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 30


def theoretical_modulation(k_max=8):
    vals = []
    for k in range(1, k_max + 1):
        gamma_k = mp.im(mp.zetazero(k))
        z = mp.zeta(1 + 2j * gamma_k)
        vals.append(float(abs(z)))
    return vals


def lambda_sieve(N):
    """Correct linear sieve for the (completely multiplicative) Liouville
    function: ALWAYS multiply by lambda(p)=-1, regardless of whether p
    already divides the running index (unlike mu, where that case forces
    mu(p^2)=0 and an early stop)."""
    primes_list = []
    is_comp = np.zeros(N + 1, dtype=bool)
    lam = np.zeros(N + 1, dtype=np.int64)
    lam[1] = 1
    for i in range(2, N + 1):
        if not is_comp[i]:
            primes_list.append(i)
            lam[i] = -1
        for p in primes_list:
            if i * p > N:
                break
            is_comp[i * p] = True
            lam[i * p] = -lam[i]
            if i % p == 0:
                break
    return lam


def omega_direct(n):
    cnt = 0
    d = 2
    m = n
    while d * d <= m:
        while m % d == 0:
            cnt += 1
            m //= d
        d += 1
    if m > 1:
        cnt += 1
    return cnt


if __name__ == '__main__':
    claimed = [1.949, 0.831, 0.534, 0.515, 0.813, 0.938, 1.922, 0.978]
    mine = theoretical_modulation()
    print("Theoretical |zeta(1+2i*gamma_k)|:")
    for k, (c, m_) in enumerate(zip(claimed, mine), 1):
        print(f"  k={k}  claimed={c}  mine={m_:.4f}")

    print("\nSanity check: lambda sieve matches direct factorization for n<=2000?")
    lam_small = lambda_sieve(2000)
    mismatches = sum(1 for n in range(2, 2001) if lam_small[n] != (-1)**omega_direct(n))
    print(f"  mismatches: {mismatches} (should be 0)")

    N = 10**6
    lam = lambda_sieve(N)
    mean_lambda = lam[2:N + 1].mean()
    print(f"\nmean(lambda(n)) for n=2..{N} = {mean_lambda:.6f}  (claimed: -0.0005)")
