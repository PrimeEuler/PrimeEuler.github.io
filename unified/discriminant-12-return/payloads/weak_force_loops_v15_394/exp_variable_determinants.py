"""
Loop program, step 1 (2026-11-04 evening, sandbox): determinants in
the exponentiated variable, on the cone's diagonal spectrum
d_n = log(n/4) (the seed/diagonal of K; the bounded perturbation B
is NOT included -- see the scope note at the end).

The literature scout's obstruction, made numerical: in the lambda
variable the spectral sums diverge; in the exponentiated variable
A = e^D (eigenvalues n/4) everything is classical:
  zeta_A(s) = 4^s zeta(s),   Tr e^{-beta D} = 4^beta zeta(beta).
"""
import mpmath as mp
import math
mp.mp.dps = 30

print("=" * 76)
print("1. The obstruction in the lambda variable, vs the exponentiated one")
print("=" * 76)
for N in [10**3, 10**4, 10**5, 10**6]:
    s_lam = sum(1.0 / (math.log(k / 4)) ** 2 for k in range(5, N + 1))
    print(f"  sum_{{n<= {N:>7}}} (log(n/4))^-2 = {s_lam:12.1f}   (still growing ~ N/log^2 N)")
s_exp = sum((k / 4) ** -2 for k in range(1, 200001))
print(f"  sum (n/4)^-2 (N=2e5, tail ~1e-4) = {s_exp:.6f}  vs 16 zeta(2) = {float(16 * mp.zeta(2)):.6f}")

print()
print("=" * 76)
print("2. Heat trace Tr e^{-beta D} = 4^beta zeta(beta), with certified tail")
print("   (tail bound: sum_{n>N} (n/4)^-beta <= 4^beta * N^{1-beta}/(beta-1), integral test)")
print("=" * 76)
for beta in [2, 3]:
    N = 100000
    partial = sum((k / 4) ** (-beta) for k in range(1, N + 1))
    tail = 4 ** beta * N ** (1 - beta) / (beta - 1)
    exact = float(4 ** beta * mp.zeta(beta))
    print(f"  beta={beta}: partial={partial:.8f}, tail <= {tail:.2e}, "
          f"exact 4^beta zeta(beta)={exact:.8f}, "
          f"inside certified interval: {partial <= exact <= partial + tail}")

print()
print("=" * 76)
print("3. zeta-determinant of A = e^D (eigenvalues n/4)")
print("=" * 76)
zp0 = mp.diff(lambda s: mp.zeta(s), 0)          # zeta'(0)
zA0 = mp.diff(lambda s: 4 ** s * mp.zeta(s), 0)  # zeta_A'(0)
logdetA = -zA0
print(f"  zeta'(0) = {float(zp0):.10f}  (exact: -1/2 log(2pi) = {float(-mp.log(2 * mp.pi) / 2):.10f})")
print(f"  zeta_A'(0) = {float(zA0):.10f}  (exact: -log 2 - 1/2 log(2pi) = {float(-mp.log(2) - mp.log(2 * mp.pi) / 2):.10f})")
print(f"  log det A = {float(logdetA):.10f};  det A = {float(mp.e ** logdetA):.8f}  "
      f"(exact sqrt(8pi) = {float(mp.sqrt(8 * mp.pi)):.8f})")
print("  (zeta prescription at mu=1 in A's units; the zeta(0) log mu^2 term is the scheme dial.)")

print()
print("=" * 76)
print("4. Determinant ratio: A_{1/2} (eigenvalues (n+1/2)/4) vs A -- and its subtlety")
print("=" * 76)
zH = lambda s: 4 ** s * mp.zeta(s, mp.mpf(3) / 2)   # Hurwitz: sum (n+1/2)^-s = zeta(s, 3/2)
zHp0 = mp.diff(zH, 0)
zH0_val = zH(0)
print(f"  zeta(0, 3/2) = {float(mp.zeta(0, mp.mpf(3)/2))} (exact 1/2 - a = -1) vs zeta(0) = -1/2: Delta zeta(0) = -1/2 != 0")
logdetH = -zHp0
ratio_zeta = mp.e ** (logdetH - logdetA)
print(f"  log det A_{{1/2}} = {float(logdetH):.8f}; zeta-prescription ratio = {float(ratio_zeta):.8f} "
      f"(exact 4/sqrt(pi) = {float(4 / mp.sqrt(mp.pi)):.8f})")
# partial products with the canonical cutoff-power subtraction
for N in [1000, 10000, 100000]:
    logp = sum(math.log((k + 0.5) / k) for k in range(1, N + 1))
    finite = math.exp(logp - 0.5 * math.log(N))
    print(f"  partial products N={N:>6}: [prod (n+1/2)/n] / sqrt(N) = {finite:.8f} "
          f"-> 1/Gamma(3/2) = 2/sqrt(pi) = {float(2 / mp.sqrt(mp.pi)):.8f}")
print("  The two finite parts differ by exactly log 2 = -Delta zeta(0) * log 4:")
print("  the pair's zeta(0)s differ, so the ratio is scale-sensitive -- the first")
print("  concrete instance of the Krein comparability gate, on our own spectrum.")
print()
print("SCOPE: diagonal seed spectrum only. The real K = D + B (bounded B,")
print("certified |d_n - log(n/4)| <= 1.7459 in the ledger work) has")
print("A_K = e^K not diagonal in this basis; determinants of the perturbed")
print("operator are the next refinement, not this toy.")
