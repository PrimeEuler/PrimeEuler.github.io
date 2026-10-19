#!/usr/bin/env python3
"""Thread 5 (Phase 2 follow-up): is the chi/K lambda_2 edge mode a truncation
artifact or large-rapidity behavior? All restricted Grams are principal
submatrices of the full station Grams (entries are pair-determined:
G[i,j] = g(u_i-u_j) - g(u_i) - g(u_j)), so no kernel re-evaluation is
needed for chi/K (saved npz). The zeta N=128 Gram is assembled once here
and saved. Descriptive finite statements only [N]."""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)


def mode_stats(v, stations):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    if v[np.argmax(np.abs(v))] < 0:
        v = -v
    mass = v ** 2
    signs = np.sign(v[np.abs(v) > 1e-12])
    top = np.argsort(-np.abs(v))[:5]
    return {
        "participation_ratio": float(1.0 / np.sum(mass ** 2)),
        "n_sign_changes": int(np.sum(signs[1:] * signs[:-1] < 0)),
        "top5_stations": [int(stations[i]) for i in top],
        "mass_last_1": float(mass[-1]), "mass_last_2": float(mass[-2:].sum()),
        "mass_last_4": float(mass[-4:].sum()), "mass_last_8": float(mass[-8:].sum()),
        "mass_last_16": float(mass[-16:].sum()),
        "mass_first_8": float(mass[:8].sum()),
        "mass_first_decile": float(mass[:len(mass) // 10].sum()),
        "mass_last_decile": float(mass[-(len(mass) // 10):].sum()),
    }


def eig_modes(G, stations, kmax=4):
    w, V = np.linalg.eigh((G + G.T) / 2)
    out = {"lambda_min": float(w[0]), "modes": {}}
    for k in range(1, kmax + 1):
        d = mode_stats(V[:, k], stations)
        d["lambda"] = float(w[k])
        out["modes"][f"lambda_{k + 1}"] = d
    return out


results = {}

# ---- assemble + save zeta Gram at 128 (once)
if os.path.exists("gram_zeta_N128.npz"):
    Gz = np.load("gram_zeta_N128.npz")["G"]
else:
    import station_gram as sg
    Gz = sg.gram(sg.g_full, 128)
    np.savez_compressed("gram_zeta_N128.npz", G=Gz)
grams = {"zeta": Gz,
         "chi": np.load("gram_chi_N128.npz")["G"],
         "K": np.load("gram_K_N128.npz")["G"]}
stations_full = np.arange(1, 129)

# ---- E4: full-Gram modes lambda_2..lambda_5 at N=128
results["full128"] = {name: eig_modes(G, stations_full) for name, G in grams.items()}

# ---- E2: drop the near edge: stations 33..128 (principal submatrix)
idx = np.arange(32, 128)
results["drop_near_33_128"] = {
    name: eig_modes(G[np.ix_(idx, idx)], stations_full[idx], kmax=2)
    for name, G in grams.items()}

# ---- E2b: drop BOTH edges: stations 33..96
idx2 = np.arange(32, 96)
results["middle_33_96"] = {
    name: eig_modes(G[np.ix_(idx2, idx2)], stations_full[idx2], kmax=2)
    for name, G in grams.items()}

# ---- E3: sliding windows of width 64: [k..k+63], k = 1,17,33,49,65
results["windows64"] = {}
for k0 in (1, 17, 33, 49, 65):
    widx = np.arange(k0 - 1, k0 + 63)
    results["windows64"][f"start_{k0}"] = {
        name: eig_modes(G[np.ix_(widx, widx)], stations_full[widx], kmax=2)
        for name, G in grams.items()}

json.dump(results, open("thread5_edgetest_results.json", "w"), indent=1)

def brief(tag, d):
    m = d["modes"]["lambda_2"]
    return (f"{tag}: lam2={m['lambda']:.5g} PR={m['participation_ratio']:.1f} "
            f"top5={m['top5_stations']} last8={m['mass_last_8']:.2f} "
            f"first8={m['mass_first_8']:.2f} signchg={m['n_sign_changes']}")

for name in grams:
    print(brief(f"{name} full128", results["full128"][name]))
    print(brief(f"{name} 33..128", results["drop_near_33_128"][name]))
    print(brief(f"{name} 33..96 ", results["middle_33_96"][name]))
    for k0 in (1, 17, 33, 49, 65):
        print(brief(f"{name} win@{k0:3d}", results["windows64"][f"start_{k0}"][name]))
    for kk in ("lambda_3", "lambda_4", "lambda_5"):
        m = results["full128"][name]["modes"][kk]
        print(f"{name} full128 {kk}: lam={m['lambda']:.5g} PR={m['participation_ratio']:.1f} "
              f"top5={m['top5_stations']} last8={m['mass_last_8']:.2f} first8={m['mass_first_8']:.2f}")
print("EDGETEST DONE")
