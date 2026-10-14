#!/usr/bin/env python3
"""Station Gram scaling run: N = 48, 64, 96, 128 (plus N=32 cross-check).

Persists the archimedean-term cache to arch_cache.json so restarts resume.
Writes scaling_results.json after each N. Same pipeline as station_gram.py
(Suzuki eq. (1.3) pieces, dps=50), so eigenvalues are directly comparable.
"""
import json, math, os
import numpy as np
from multiprocessing import Pool
from suzuki_riemann_screw_calibration import pole_term, prime_ramp, archimedean_term

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(HERE, 'arch_cache.json')
OUT_PATH = os.path.join(HERE, 'scaling_results.json')

def key(t):
    # quantize to 1e-9: log(n)-log(k) and log(n/k) differ in the last ulp and
    # split across round(...,12) boundaries (KeyError crash, 2026-10-14 run).
    return round(abs(t), 9)

def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH) as fh:
            return {key(float(k)): v for k, v in json.load(fh).items()}
    return {}

def eval_arch(t):
    return (t, archimedean_term(t, dps=50))

def needed_ts(N):
    ts = set()
    for n in range(1, N + 1):
        ts.add(key(math.log(n)))
        for k in range(1, N + 1):
            ts.add(key(math.log(n / k)))
    return ts

def main():
    cache = load_cache()
    results = {}
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH) as fh:
            results = json.load(fh)
    for N in (32, 48, 64, 96, 128):
        need = needed_ts(N)
        missing = sorted(t for t in need if t not in cache)
        print(f'N={N}: {len(need)} distinct |t| values, {len(missing)} arch evals needed', flush=True)
        if missing:
            with Pool(2) as pool:
                for t, v in pool.imap_unordered(eval_arch, missing, chunksize=16):
                    cache[t] = v
            with open(CACHE_PATH, 'w') as fh:
                json.dump({repr(k): v for k, v in cache.items()}, fh)
        def g(t):
            return pole_term(t) + prime_ramp(t) + cache[key(t)]
        u = [math.log(n) for n in range(1, N + 1)]
        G = np.zeros((N, N))
        for i in range(N):
            gi = g(u[i])
            for j in range(N):
                G[i, j] = g(u[i] - u[j]) - gi - g(u[j])
        w = np.linalg.eigvalsh((G + G.T) / 2)
        results[str(N)] = {
            'lambda_min': float(w[0]),
            'lambda_2_smallest_positive': float(w[1]),
            'lambda_3': float(w[2]),
            'lambda_max': float(w[-1]),
            'n_negative_beyond_1e-9': int(np.sum(w < -1e-9)),
            'n_negative_beyond_1e-7': int(np.sum(w < -1e-7)),
        }
        with open(OUT_PATH, 'w') as fh:
            json.dump(results, fh, indent=1)
        print(f'N={N}: done -> {results[str(N)]}', flush=True)
    print('SCALING COMPLETE')

if __name__ == '__main__':
    main()
