"""External audit (Round 143) independent check of v13.942's exact,
well-defined numerical claims (pi(N), the nonzero-mu count, M(N), D(N) via
two independent methods, Delta(N), and the hyperbola-identity cross-check).

Does NOT attempt to reproduce the entry's FFT/windowing-based R-value,
dose-response, or kill-test experiments -- those depend on unposted
methodological choices (windowing, detrending) and are not re-derived here.
"""
import math
import numpy as np


def pi_and_mu(N):
    primes_list = []
    is_comp = np.zeros(N + 1, dtype=bool)
    mu = np.zeros(N + 1, dtype=np.int64)
    mu[1] = 1
    for i in range(2, N + 1):
        if not is_comp[i]:
            primes_list.append(i)
            mu[i] = -1
        for p in primes_list:
            if i * p > N:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]
    pi_N = len(primes_list)
    nonzero_mu = int(np.count_nonzero(mu[1:N + 1]))
    M_N = int(np.cumsum(mu[1:N + 1])[-1])
    return pi_N, nonzero_mu, M_N


def divisor_summatory_hyperbola(N):
    s = math.isqrt(N)
    return 2 * sum(N // k for k in range(1, s + 1)) - s * s


def divisor_summatory_direct(N):
    d = np.zeros(N + 1, dtype=np.int64)
    for k in range(1, N + 1):
        d[k::k] += 1
    return int(d[1:N + 1].sum())


def delta(N, D_N):
    gamma = 0.5772156649015329
    return D_N - (N * math.log(N) + (2 * gamma - 1) * N)


def hyperbola_rhs(N):
    s = math.isqrt(N)
    frac_sum = sum((N / k - N // k) for k in range(1, s + 1))
    return math.sqrt(N) - 2 * frac_sum


if __name__ == '__main__':
    N = 10**6
    pi_N, nonzero_mu, M_N = pi_and_mu(N)
    print(f"pi({N}) = {pi_N}  (claimed: 78498)")
    print(f"nonzero mu(n) count = {nonzero_mu}  (claimed: 607926)")
    print(f"M({N}) = {M_N}  (claimed: 212)")

    D_hyp = divisor_summatory_hyperbola(N)
    D_direct = divisor_summatory_direct(N)
    print(f"D({N}) via hyperbola method = {D_hyp}  (claimed: 13970034)")
    print(f"D({N}) via direct divisor-count sieve = {D_direct}  (independent cross-check)")

    Delta_N = delta(N, D_hyp)
    print(f"Delta({N}) = {Delta_N:.4f}  (claimed: 92.1)")

    rhs = hyperbola_rhs(N)
    print(f"sqrt(N) - 2*sum{{N/k}} = {rhs:.4f}  (claimed seed-scale prediction: 92.28)")
