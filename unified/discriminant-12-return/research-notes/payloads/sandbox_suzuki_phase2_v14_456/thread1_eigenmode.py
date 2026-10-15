#!/usr/bin/env python3
"""Thread 1: structure of the lambda_2 eigenvector (softest nonzero mode)
of the station Grams for zeta, chi_12, Dedekind-K.
Existing sizes: zeta N=32/64/96/128, chi/K N=32/64 (96/128 refresh runs
separately once Thread 2 saves those Grams). Descriptive statistics
only [N]; no claim beyond the finite matrices."""
import json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)

import station_gram as sg       # zeta: g_full, gram
import d12_station_gram as d12  # chi/K: g_chi, g_K, gram


def primes_upto(N):
    sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
    for p in range(2, int(math.sqrt(N)) + 1):
        if sieve[p]:
            sieve[p * p:N + 1:p] = False
    return set(np.flatnonzero(sieve).astype(int))


def describe(v, N):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    if v[np.argmax(np.abs(v))] < 0:
        v = -v
    mass = v ** 2
    stations = np.arange(1, N + 1)
    deciles = [float(mass[i * N // 10:(i + 1) * N // 10].sum()) for i in range(10)]
    pr = float(1.0 / np.sum(mass ** 2))
    signs = np.sign(v[np.abs(v) > 1e-12])
    n_sign_changes = int(np.sum(signs[1:] * signs[:-1] < 0))
    top = np.argsort(-np.abs(v))[:5]
    u = np.log(stations)
    shapes = {
        "const": np.ones(N),
        "linear_u_centered": u - u.mean(),
        "inv_sqrt_n": 1.0 / np.sqrt(stations),
        "sqrt_n_centered": np.sqrt(stations) - np.sqrt(stations).mean(),
    }
    overlaps = {}
    for k, s in shapes.items():
        s = s / np.linalg.norm(s)
        overlaps[k] = float(abs(v @ s))
    primes = primes_upto(N)
    pp = set()
    for p in primes:
        pk = p
        while pk <= N:
            pp.add(pk); pk *= p
    out = {
        "participation_ratio": pr,
        "participation_over_N": pr / N,
        "decile_mass": deciles,
        "first_station_mass": float(mass[0]),
        "n_sign_changes": n_sign_changes,
        "top5_stations": [(int(stations[i]), float(v[i])) for i in top],
        "overlaps": overlaps,
        "mass_prime_stations": float(sum(mass[n - 1] for n in primes)),
        "mass_primepower_stations": float(sum(mass[n - 1] for n in pp)),
        "share_prime_stations_uniform": len(primes) / N,
        "mass_ramified_2or3": float(sum(mass[n - 1] for n in stations if n % 2 == 0 or n % 3 == 0)),
        "share_ramified_uniform": float(np.mean([(n % 2 == 0 or n % 3 == 0) for n in stations])),
        "vector": [float(x) for x in v],
    }
    return out


results = {"thread": 1, "runs": {}}

jobs = []
for N in (32, 64, 96, 128):
    jobs.append((f"zeta_N{N}", sg.g_full, sg.gram, N))
for N in (32, 64):
    jobs.append((f"chi_N{N}", d12.g_chi, d12.gram, N))
    jobs.append((f"K_N{N}", d12.g_K, d12.gram, N))

for label, gfun, gramfun, N in jobs:
    G = gramfun(gfun, N)
    w, V = np.linalg.eigh((G + G.T) / 2)
    d = describe(V[:, 1], N)
    d["lambda_min"] = float(w[0]); d["lambda_2"] = float(w[1]); d["lambda_3"] = float(w[2])
    results["runs"][label] = d
    print(f"{label}: lam2={w[1]:.6g} PR={d['participation_ratio']:.1f}/{N} "
          f"signchg={d['n_sign_changes']} decile0={d['decile_mass'][0]:.3f} "
          f"ramified_mass={d['mass_ramified_2or3']:.3f} (unif {d['share_ramified_uniform']:.3f})", flush=True)

json.dump(results, open("thread1_results.json", "w"), indent=1)
print("THREAD1 DONE")
