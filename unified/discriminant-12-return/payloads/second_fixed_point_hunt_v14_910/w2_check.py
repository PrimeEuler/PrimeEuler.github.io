"""W2(N) = sum_{ab<=N} j(j+1), j=(a+b-2)/2  (v14.858's open gate).
Exact integer arithmetic via per-a closed forms.
Predictions: W2(N) = C3 N^3 + (1/4) N^2 ln N + O(N^2),
C3 = zeta(3)/6 [shell/Dirichlet route: sum_m sigma_2(m) ~ zeta(3) N^3/3];
W2(4n)/W2(n) -> 64 (degree-3 homogeneity);
Delta_64(n) = W2(4n) - 64 W2(n) ~ -12 n^2 ln n."""
from fractions import Fraction as F
import mpmath as mp

def F2M(fr):
    return mp.mpf(fr.numerator) / fr.denominator

def W2(N):
    tot = F(0)
    for a in range(1, N + 1):
        M = N // a
        s1 = M * a + M * (M + 1) // 2                      # sum (a+b)
        s2 = M * a * a + a * M * (M + 1) + M * (M + 1) * (2 * M + 1) // 6  # sum (a+b)^2
        tot += F(s2 - 2 * s1, 4)
    return tot

# v14.858's 113 is the SHELL weight (ab = 12 exactly), not the cumulative.
def shell(n):
    tot = F(0)
    for a in range(1, n + 1):
        if n % a == 0:
            b = n // a
            j = F(a + b - 2, 2)
            tot += j * (j + 1)
    return tot
assert shell(12) == 113, shell(12)
# brute-force cross-check of the cumulative closed form at N=12
brute = sum(F(a + b - 2, 2) * (F(a + b - 2, 2) + 1)
            for a in range(1, 13) for b in range(1, 13) if a * b <= 12)
assert brute == W2(12), (brute, W2(12))
print("shell(12) = 113 exact: OK; cumulative closed form = brute force at N=12: OK")
C3 = mp.zeta(3) / 6
print(f"C3 predicted = {mp.nstr(C3, 10)}")
prev = None
for n in [1000, 4000, 16000, 64000]:
    w_n, w_4n = W2(n), W2(4 * n)
    ratio = F2M(w_4n) / F2M(w_n)
    c3fit = F2M(w_n) / n ** 3
    d64 = F2M(w_4n - 64 * w_n) / (n ** 2 * mp.log(n))
    print(f"n={n:6d}  W2(4n)/W2(n)={mp.nstr(ratio, 8)} (->64)  "
          f"W2(n)/n^3={mp.nstr(c3fit, 8)}  Delta64/(n^2 ln n)={mp.nstr(d64, 6)} (->-12)")
print("DONE")
