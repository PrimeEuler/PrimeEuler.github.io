"""Pantheon+ FULL-COVARIANCE k4-vs-LCDM comparison (v14.923 handoff to Sandbox).
Step 1 reproduces the v14.923 diagonal diagnostic exactly (validation gate).
Step 2 verifies the official 1701x1701 STAT+SYS covariance ordering against
the .dat rows (diag(C) vs m_b_corr_err_DIAG^2), subselects the same 1580 rows.
Step 3 computes profiled full-covariance chi2 (common additive magnitude
offset marginalized analytically per model), dual-solver cross-checks.
NO sigma/exclusion is computed (handoff instruction)."""
import json
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.linalg import cho_factor, cho_solve, eigh

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261026-pantheon-fullcov"
df = pd.read_csv(f"{RUN}/data/Pantheon+SH0ES.dat", sep=r"\s+")
assert len(df) == 1701, len(df)
sel = (df.zHD > 0.01) & (df.IS_CALIBRATOR == 0) & (df.zHEL > 0) & (df.m_b_corr_err_DIAG > 0)
idx = np.where(sel.to_numpy())[0]
a = df[sel]
print(f"selected {len(a)} rows (expect 1580)")
assert len(a) == 1580

def mu_model(z, zh, kind):
    if kind == "cone":
        I = np.log1p(z)
    else:
        I = quad(lambda u: 1 / np.sqrt(0.315 * (1 + u) ** 3 + 0.685), 0, z)[0]
    return 5 * np.log10((1 + zh) * I)

models = {}
for kind in ["cone", "lcdm"]:
    models[kind] = np.array([mu_model(z, zh, kind) for z, zh in zip(a.zHD, a.zHEL)])
mb = a.m_b_corr.to_numpy()
sig = a.m_b_corr_err_DIAG.to_numpy()

# ---- Step 1: diagonal reproduction (validation gate) ----
diag_out = {}
w = 1 / sig ** 2
for kind in ["cone", "lcdm"]:
    y = mb - models[kind]
    off = np.sum(w * y) / np.sum(w)
    chi2 = float(np.sum(w * (y - off) ** 2))
    diag_out[kind] = {"offset": float(off), "chi2": chi2}
    print(f"DIAG {kind}: offset={off:.8f} chi2={chi2:.7f}")
targets = {"cone": (23.88812561765, 786.1217145063), "lcdm": (23.80256473998, 697.6175999269)}
for kind, (toff, tchi2) in targets.items():
    assert abs(diag_out[kind]["offset"] - toff) < 2e-4, (kind, diag_out[kind])
    assert abs(diag_out[kind]["chi2"] - tchi2) < 5e-3, (kind, diag_out[kind])
print("DIAGONAL REPRODUCTION: PASS (offsets <2e-4, chi2 <5e-3 vs v14.923)")

# ---- Step 2: covariance load + checks ----
raw = np.loadtxt(f"{RUN}/data/Pantheon+SH0ES_STAT+SYS.cov", skiprows=1)
assert raw.size == 1701 ** 2, raw.size
C = raw.reshape(1701, 1701)
sym = float(np.max(np.abs(C - C.T)))
C = 0.5 * (C + C.T)  # file print precision: max asymmetry 3e-8, symmetrize
diag_all = np.diag(C).copy()
v_extra = df.m_b_corr_err_DIAG.to_numpy() ** 2 - diag_all
print(f"covariance: max|C-C^T| before symmetrization={sym:.3e}")
print(f"DIAG^2 - C_ii (=v): min={v_extra.min():.3e}, median={np.median(v_extra):.4f}, "
      f"negative rows={(v_extra < 0).sum()} -> the .dat DIAG errors are NOT sqrt(diag(.cov)); "
      f"they carry an extra nonnegative diagonal term. Two constructions reported (see NOTE).")
Csub = C[np.ix_(idx, idx)]
ev = eigh(Csub, eigvals_only=True)
cond = float(ev[-1] / ev[0])
print(f"submatrix A (released .cov) 1580x1580: min eig={ev[0]:.6e}, max eig={ev[-1]:.6e}, cond={cond:.6e}")
assert ev[0] > 0, "submatrix A not positive definite"
vsub = np.clip(v_extra[idx], 0, None)
CsubB = Csub + np.diag(vsub)
evB = eigh(CsubB, eigvals_only=True)
print(f"submatrix B (A + diag(v), diagonal restored to DIAG errors): min eig={evB[0]:.6e}, cond={float(evB[-1]/evB[0]):.6e}")
assert evB[0] > 0

# ---- Step 3: full-covariance profiled chi2, two constructions x two solvers ----
def profiled(r, Cmat, solver):
    if solver == "chol":
        cf = cho_factor(Cmat)
        Ci_r = cho_solve(cf, r); Ci_1 = cho_solve(cf, np.ones_like(r))
    else:
        w_e, V = eigh(Cmat)
        Ci_r = V @ ((V.T @ r) / w_e); Ci_1 = V @ ((V.T @ np.ones_like(r)) / w_e)
    s_r = float(np.sum(Ci_r)); s_1 = float(np.sum(Ci_1))
    return s_r / s_1, float(r @ Ci_r - s_r ** 2 / s_1)

full_out = {}
for label, Cmat in [("A_released_cov", Csub), ("B_diag_restored", CsubB)]:
    full_out[label] = {}
    for kind in ["cone", "lcdm"]:
        r = mb - models[kind]
        off_c, chi2_c = profiled(r, Cmat, "chol")
        off_e, chi2_e = profiled(r, Cmat, "eig")
        assert abs(chi2_c - chi2_e) < 1e-4 * chi2_c, (label, kind, chi2_c, chi2_e)
        full_out[label][kind] = {"offset": off_c, "chi2": chi2_c, "chi2_eig": chi2_e}
        print(f"FULL[{label}] {kind}: offset={off_c:.8f} chi2={chi2_c:.7f} (eig {chi2_e:.7f})")
    print(f"FULL[{label}] delta chi2 (cone-lcdm) = {full_out[label]['cone']['chi2'] - full_out[label]['lcdm']['chi2']:+.7f}")

# jitter sensitivity on construction A
jit = 1e-10 * float(np.mean(np.diag(Csub)))
jit_out = {}
for kind in ["cone", "lcdm"]:
    _, cj = profiled(mb - models[kind], Csub + jit * np.eye(len(idx)), "chol")
    jit_out[kind] = cj
    print(f"JITTER[A] {kind}: chi2={cj:.7f} (shift {cj - full_out['A_released_cov'][kind]['chi2']:+.2e})")

results = {
    "n_selected": int(len(a)), "dof_profiled": int(len(a) - 1),
    "diagonal_v14_923_reproduction": diag_out,
    "covariance_checks": {"max_sym_asym_before_symmetrization": sym,
                          "v_extra_min": float(v_extra.min()), "v_extra_median": float(np.median(v_extra)),
                          "v_extra_negative_rows": int((v_extra < 0).sum()),
                          "cond_A": cond, "min_eig_A": float(ev[0]), "max_eig_A": float(ev[-1]),
                          "cond_B": float(evB[-1] / evB[0]), "min_eig_B": float(evB[0])},
    "full_covariance": full_out,
    "delta_chi2_full_A": full_out["A_released_cov"]["cone"]["chi2"] - full_out["A_released_cov"]["lcdm"]["chi2"],
    "delta_chi2_full_B": full_out["B_diag_restored"]["cone"]["chi2"] - full_out["B_diag_restored"]["lcdm"]["chi2"],
    "delta_chi2_diag_cone_minus_lcdm": diag_out["cone"]["chi2"] - diag_out["lcdm"]["chi2"],
    "jitter_chi2_A": jit_out,
}
json.dump(results, open(f"{RUN}/results.json", "w"), indent=2)
print(json.dumps(results, indent=2))
print("DONE")
