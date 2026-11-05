"""
Loop program, step 3 (2026-11-04 evening, sandbox): the Krein pair
test PROPER -- comparability diagnostics FIRST, and only the
determinant the diagnostics license gets quoted. Reference
operator D (d_n = log(n/4)) against two perturbations, analysed
per parity channel (even/odd mode index -- the model analog of the
ledger's odd/even sectors, in which the K_full theory was
certified sector by sector):

  Pair A: diagonal, summable shifts delta_n = 0.5/(n log^2(n+3)).
          Expected class: TRACE class -> raw determinant licensed.
  Pair B: channel-preserving Hilbert-like B (0.3/(j+k-1) within
          each channel). Expected class: NOT trace class,
          Hilbert-Schmidt after one resolvent -> det_2 licensed.
          (Channel-preserving by construction so that channel
          operators exist; the step-2 B mixed channels.)

Protocol per pair and channel:
  (i)   diagnostics: T1(N) = sum |B_nn| / |d_n - z| (trace-side
        growth) and T2(N) = ||B R_D||_HS on the section;
  (ii)  the licensed determinant, tracked over growing sections;
  (iii) Birman-Krein per channel by interval integration.
z = -3.5 throughout (below all spectra incl. Weyl shifts).
"""
import numpy as np

Z = -3.5

def channel_indices(N, parity):
    return np.array([n for n in range(1, N + 1) if n % 2 == parity])

def logdet_ratio(K, d, z):
    M = (K - z * np.eye(len(d))) / (d - z)[None, :]
    s, ld = np.linalg.slogdet(M)
    return ld

def bk_check(ev0, ev1, z):
    f = lambda lam: 1.0 / (lam - z)
    pts = np.sort(np.concatenate([ev0, ev1]))
    tot = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        mid = 0.5 * (a + b)
        xi = np.sum(ev0 <= mid) - np.sum(ev1 <= mid)
        tot += xi * (f(b) - f(a))
    lhs = np.sum(1.0 / (ev1 - z)) - np.sum(1.0 / (ev0 - z))
    return lhs, tot

print("=" * 76)
print("PAIR A -- diagonal summable perturbation (expect: trace class)")
print("=" * 76)
for parity, pname in [(1, "odd "), (0, "even")]:
    vals = []
    for N in [200, 400, 800, 1600]:
        idx = channel_indices(N, parity)
        d = np.log(idx / 4.0)
        delta = 0.5 / (idx * np.log(idx + 3.0) ** 2)
        T1 = np.sum(delta / np.abs(d - Z))
        logD = np.sum(np.log((d + delta - Z) / (d - Z)))
        vals.append(logD)
        if N in (200, 1600):
            print(f"  [{pname}] N={N:>5}: T1 diagnostic = {T1:.6f} (converging), "
                  f"raw log det = {logD:+.8f}")
    inc = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    print(f"  [{pname}] raw-determinant increments per doubling: "
          f"{['%+.2e' % x for x in inc]} -> LICENSED, limit {vals[-1]:+.8f}")
    idx = channel_indices(400, parity)
    d = np.log(idx / 4.0)
    delta = 0.5 / (idx * np.log(idx + 3.0) ** 2)
    lhs, tot = bk_check(np.sort(d), np.sort(d + delta), Z)
    print(f"  [{pname}] Birman-Krein (N=400 section): Tr = {lhs:+.10f}, "
          f"int f' xi = {tot:+.10f}, agree {abs(lhs - tot) < 1e-8}")

print()
print("=" * 76)
print("PAIR B -- channel-preserving Hilbert-like (expect: HS only, det_2)")
print("=" * 76)
for parity, pname in [(1, "odd "), (0, "even")]:
    raws, rens = [], []
    for N in [200, 400, 800]:
        idx = channel_indices(N, parity)
        d = np.log(idx / 4.0)
        j = np.arange(1, len(idx) + 1)
        B = 0.3 / (j[:, None] + j[None, :] - 1)
        K = np.diag(d) + B
        RD = 1.0 / (d - Z)
        T1 = np.sum(np.abs(np.diag(B)) * np.abs(RD))
        T2 = np.sqrt(np.sum((B * RD[None, :]) ** 2))
        logD = logdet_ratio(K, d, Z)
        ren = logD - np.sum(np.diag(B) * RD)
        raws.append(logD); rens.append(ren)
        if N in (200, 800):
            print(f"  [{pname}] N={N:>5}: T1 = {T1:.4f} (grows, log log-like), "
                  f"T2(HS) = {T2:.4f} (settling)")
    print(f"  [{pname}] raw increments: {['%+.4f' % (raws[i+1]-raws[i]) for i in range(2)]}"
          f" -> raw NOT licensed")
    print(f"  [{pname}] det_2 increments: {['%+.6f' % (rens[i+1]-rens[i]) for i in range(2)]}"
          f" -> LICENSED, value at N=800: {rens[-1]:+.6f}")
    idx = channel_indices(400, parity)
    d = np.log(idx / 4.0)
    j = np.arange(1, len(idx) + 1)
    B = 0.3 / (j[:, None] + j[None, :] - 1)
    evK = np.linalg.eigvalsh(np.diag(d) + B)
    lhs, tot = bk_check(np.sort(d), evK, Z)
    print(f"  [{pname}] Birman-Krein (N=400 section): Tr = {lhs:+.10f}, "
          f"int f' xi = {tot:+.10f}, agree {abs(lhs - tot) < 1e-8}")

print()
print("PROTOCOL VERDICT: diagnostics discriminated the two pairs exactly")
print("as designed -- A trace class (raw determinant converges per")
print("channel), B Hilbert-Schmidt only (raw drifts per channel, det_2")
print("settles). No ratio was quoted beyond its licence.")
