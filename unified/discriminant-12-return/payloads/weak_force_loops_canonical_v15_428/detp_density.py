"""
Loop program, step 6 (2026-11-05, sandbox): higher renormalization
for the canonical pair. Step 5 found B R_D(z) is not
Hilbert-Schmidt on the infinite operator (section HS^2 grows
~linearly in S remotely), so det_2 does not exist for the pair.
Question: does some finite-order det_p exist? That needs
X = B R_D(z) in the Schatten class S_p, i.e. sum_j s_j(X)^p < inf.

Method (finite sections of the canonical kernel, float stack and
sectors imported from canonical_krein.py; same probe-grade [N]
standing): for S = 200/400/800, per sector and regime,
  - Schatten sums sum_j s_j^p for p = 2, 3, 4 and their per-mode
    ratios: if a ratio stabilizes at a positive constant, the
    infinite sum diverges linearly and NO det_p exists at that
    order either;
  - singular-value quantiles at S=400 vs 800: a stable empirical
    distribution = the mechanism (a local band operator has ~S
    singular values of typical size, at every p);
  - the det_p densities (1/S) log det_p(1+X_S), p = 2, 3, 4,
    with log det_p = log det - sum_{k<p} (-1)^{k-1} Tr(X^k)/k
    (Tr X = 0 identically here, B hollow): whether the DENSITY
    stabilizes, and whether higher p improves it.
z as in step 5 (head: per-sector census z; remote: z = 7).
"""
import contextlib
import io

import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import canonical_krein as ck   # re-runs step 5 quietly (repro check)

print("=" * 76)
print("SCHATTEN DIAGNOSTICS for X = B R_D(z), canonical sections")
print("=" * 76)
sv_store = {}
for name, sec in ck.SECTORS.items():
    for regime, z in (("head", None), ("remote", 7.0)):
        zz = ck.ZHEAD[name] if z is None else z
        for S in (200, 400, 800):
            modes, a, K, B = ck.section(sec, regime, S)
            X = B * (1.0 / (a - zz))[None, :]
            s = np.linalg.svd(X, compute_uv=False)
            sv_store[(name, regime, S)] = s
            sch = {p: float(np.sum(s ** p)) for p in (2, 3, 4)}
            trX2 = float(np.trace(X @ X))
            trX3 = float(np.trace(X @ X @ X))
            M = (K - zz * np.eye(S)) / (a - zz)[None, :]
            _, logdet = np.linalg.slogdet(M)
            ld2 = logdet                       # Tr X = 0
            ld3 = logdet + trX2 / 2.0
            ld4 = logdet + trX2 / 2.0 - trX3 / 3.0
            print(f"  [{name}/{regime}] S={S:>4}: "
                  f"||X||_2^2={sch[2]:8.2f} (per mode {sch[2]/S:.4f}), "
                  f"||X||_3^3={sch[3]:8.3f} ({sch[3]/S:.4f}), "
                  f"||X||_4^4={sch[4]:7.3f} ({sch[4]/S:.4f})")
            print(f"      densities (1/S) log det_p: p=2 {ld2/S:+.5f}, "
                  f"p=3 {ld3/S:+.5f}, p=4 {ld4/S:+.5f};  "
                  f"Tr X^2/S={trX2/S:+.4f}, Tr X^3/S={trX3/S:+.4f}", flush=True)

print()
print("=" * 76)
print("SINGULAR-VALUE DISTRIBUTION stability (quantiles of s_j)")
print("=" * 76)
for name, regime in (("odd", "remote"), ("even", "remote"),
                     ("odd", "head"), ("even", "head")):
    q = {}
    for S in (400, 800):
        s = sv_store[(name, regime, S)]
        q[S] = np.quantile(s, [0.1, 0.25, 0.5, 0.75, 0.9, 0.99])
    print(f"  [{name}/{regime}] S=400: {np.array2string(q[400], precision=3)}")
    print(f"  [{name}/{regime}] S=800: {np.array2string(q[800], precision=3)}")

print()
print("READING: if every per-mode Schatten ratio stabilizes at a")
print("positive constant and the s_j quantiles are S-independent,")
print("then sum_j s_j^p ~ const * S for EVERY finite p: no det_p")
print("exists for the canonical pair at any order; the density is")
print("the only determinant-level object, at every order.")
