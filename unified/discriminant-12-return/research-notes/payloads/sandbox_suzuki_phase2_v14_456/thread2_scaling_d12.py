#!/usr/bin/env python3
"""Thread 2: chi_12 and Dedekind-K station-Gram scaling to N=96/128.
Reuses d12_station_gram.py machinery (importing it re-runs its N=32/64
computations as a consistency check). Fresh values only for 96/128;
32/64 read from d12_gram_results.json for the decay fit.
Saves Gram matrices for Thread 1 (eigenvector analysis).
Finite statements only [N]."""
import json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)

import d12_station_gram as d12  # noqa: E402  (runs its own 32/64 block on import)

out = {"thread": 2, "screws": {}}
stored = json.load(open("d12_gram_results.json"))

for name, gfun in (("chi", d12.g_chi), ("K", d12.g_K)):
    rows = {}
    for N in (96, 128):
        G = d12.gram(gfun, N)
        rep = d12.eig_report(G)
        rep["lambda2_times_N"] = rep["lambda_2"] * N
        rep["lambda2_over_max"] = rep["lambda_2"] / rep["lambda_max"]
        rows[str(N)] = rep
        np.savez_compressed(f"gram_{name}_N{N}.npz", G=G)
        print(f"{name} N={N}: " + json.dumps(rep), flush=True)
    # decay fit over 32/64 (stored) + 96/128 (fresh): log lam2 vs log N
    Ns, l2 = [], []
    for N in (32, 64):
        key = f"{name}_N{N}"
        if key in stored:
            Ns.append(N); l2.append(stored[key]["lambda_2"])
    for N in (96, 128):
        Ns.append(N); l2.append(rows[str(N)]["lambda_2"])
    A = np.polyfit(np.log(Ns), np.log(l2), 1)
    out["screws"][name] = {"fresh": rows, "Ns_fit": Ns,
                          "lambda2_fit": l2,
                          "decay_exponent": float(-A[0]),
                          "prefactor": float(math.exp(A[1])),
                          "lambda2_times_N_all": [l * n for l, n in zip(l2, Ns)]}
    print(f"{name} fit: lambda2 ~ {math.exp(A[1]):.4f} / N^{{-A[0]:.3f}} -> exponent {-A[0]:.3f}", flush=True)

json.dump(out, open("thread2_results.json", "w"), indent=1)
print("THREAD2 DONE")
