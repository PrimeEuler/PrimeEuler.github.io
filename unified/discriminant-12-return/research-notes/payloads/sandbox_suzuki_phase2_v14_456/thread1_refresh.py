#!/usr/bin/env python3
"""Thread 1 refresh: lambda_2 eigenvector structure on Thread 2's saved
chi/K Grams at N=96/128 — does the edge localization follow the edge?"""
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)


def describe(v, N):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    if v[np.argmax(np.abs(v))] < 0:
        v = -v
    mass = v ** 2
    deciles = [float(mass[i * N // 10:(i + 1) * N // 10].sum()) for i in range(10)]
    signs = np.sign(v[np.abs(v) > 1e-12])
    top = np.argsort(-np.abs(v))[:5]
    return {
        "participation_ratio": float(1.0 / np.sum(mass ** 2)),
        "decile_mass": deciles,
        "n_sign_changes": int(np.sum(signs[1:] * signs[:-1] < 0)),
        "top5_stations": [(int(i + 1), float(v[i])) for i in top],
        "vector": [float(x) for x in v],
    }


out = {}
for name in ("chi", "K"):
    for N in (96, 128):
        G = np.load(f"gram_{name}_N{N}.npz")["G"]
        w, V = np.linalg.eigh((G + G.T) / 2)
        d = describe(V[:, 1], N)
        d["lambda_min"] = float(w[0]); d["lambda_2"] = float(w[1])
        out[f"{name}_N{N}"] = d
        print(f"{name}_N{N}: lam2={w[1]:.5g} PR={d['participation_ratio']:.1f} "
              f"signchg={d['n_sign_changes']} top5={[s for s, _ in d['top5_stations']]} "
              f"last_decile={d['decile_mass'][-1]:.2f}", flush=True)

json.dump(out, open("thread1_refresh_96128.json", "w"), indent=1)
print("REFRESH DONE")
