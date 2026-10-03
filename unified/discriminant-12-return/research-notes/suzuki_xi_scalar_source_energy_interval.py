#!/usr/bin/env python3
"""Instantiate the v13.980-v13.981 Xi scalar source-energy certificate.

This is the Lane-A consumer for the frozen arbitrary-carrier payloads.

Required payloads
-----------------
Existing:
    research-notes/p4_payload/{even-v,odd-v}/
    research-notes/p4_payload_kkt/{even-v,odd-v}/

Final residual-cross payload:
    research-notes/p4_payload_kkt_residual_cross/{even-v,odd-v}/
with at minimum
    X_R.npy                 shape (7999,4)
    saddle_lamR.npy         shape (4,4)
    manifest.json           finite block/constraint residuals

The script:
  1. reconstructs the exact arbitrary-carrier nominal 6x6 matrices of v13.980;
  2. runs the committed remote-residual certificate for all seven KKT jobs;
  3. converts residuals to exact-complement action errors using the certified
     numerical-complement inverse caps from v13.979;
  4. instantiates the v13.981 source-energy interval theorem;
  5. emits E_even, E_odd and the resulting kappa interval.

Guardrails
----------
This certifies the finite a=1, absolute-lambda=0 numerical-carrier reduction
only when every residual input used below is certified.  It makes no RH/GRH
or a->infinity convergence claim.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
)
from suzuki_form_core_schur_parameter_diagnostic import source_overlap
from suzuki_kkt_remote_residual_certificate import (
    sector_data,
    build_jobs,
    one_job,
    CROSSROOT,
)


HERE = Path(__file__).resolve().parent
P4ROOT = HERE / "p4_payload"
KKTROOT = HERE / "p4_payload_kkt"

# Certified arbitrary-carrier complement inverse caps, v13.979.
DINV_CAP = {
    "even-v": 10.152566,
    "odd-v": 10.302509,
}

# Certified transformed core/tail coupling caps inherited by v13.971/v13.981.
C_CAP = {
    "even-v": 0.160,
    "odd-v": 0.204,
}

# Certified arbitrary-carrier Ritz-residual cross-block caps from v13.979.
# These are the public constants used in its numerical-complement theorem.
RHO_CAP = {
    "even-v": 0.00580,
    "odd-v": 0.00880,
}

# Crude analytic transformed-source norm caps from v13.981.
GSTAR_CAP = {
    "even-v": 18.412,
    "odd-v": 1.993,
}

# Separate arithmetic reserve for assembled 6x6 data/source.  This is much
# larger than the frozen source-coordinate arithmetic radii (~1e-16).
ASSEMBLY_ARITH = 1.0e-11


def full_A_block(rows, cols, sector):
    rows = np.asarray(rows, dtype=int)
    cols = np.asarray(cols, dtype=int)
    zr, dr = endpoint_data(rows, sign=-1, rho=0.0)
    zc, dc = endpoint_data(cols, sign=-1, rho=0.0)

    M = offdiag(rows, cols, zr, zc)

    if np.array_equal(rows, cols):
        np.fill_diagonal(M, dr)

    all_modes = np.unique(np.concatenate([rows, cols]))
    p_all, alpha = pole_vector(all_modes, sector)
    pmap = {int(n): float(v) for n, v in zip(all_modes, p_all)}
    pr = np.array([pmap[int(n)] for n in rows])
    pc = np.array([pmap[int(n)] for n in cols])
    M = M + alpha * np.outer(pr, pc)
    return np.asarray(M, dtype=float)


def source_vector(modes):
    return np.array(
        [source_overlap(int(n), 1.0, 1.0) for n in modes],
        dtype=float,
    )


def load_cross_manifest(sector):
    path = CROSSROOT / sector / "manifest.json"
    if not path.exists():
        raise FileNotFoundError(
            f"missing residual-cross payload: {path}"
        )
    return json.loads(path.read_text())


def cross_finite_residuals(man):
    """Return four (block, constraint) finite residual pairs.

    Accept several natural manifest conventions so the sandbox payload can be
    consumed without a filename-format dependency.
    """
    r = man.get("residuals", man)

    out = []
    for j in range(1, 5):
        candidates = [
            f"solveR{j}",
            f"solve_r{j}",
            f"ritz_residual{j}",
            f"residual{j}",
            f"solve{j}",
        ]
        val = None
        for key in candidates:
            if key in r:
                val = r[key]
                break
        if val is None:
            raise KeyError(
                f"cannot find finite residual for residual-cross solve {j}; "
                f"available keys={list(r.keys())}"
            )
        if isinstance(val, dict):
            block = float(
                val.get("block", val.get("block_residual", val.get("residual")))
            )
            constraint = float(
                val.get(
                    "constraint",
                    val.get("constraint_residual", val.get("orthogonality", 0.0)),
                )
            )
        else:
            block = float(val[0])
            constraint = float(val[1]) if len(val) > 1 else 0.0
        out.append((block, constraint))
    return out


def all_finite_constraints(sector, cross_man):
    base = json.loads((KKTROOT / sector / "manifest.json").read_text())
    base_r = base["residuals"]

    pairs = {
        "core1": tuple(map(float, base_r["solve1"])),
        "core2": tuple(map(float, base_r["solve2"])),
        "source": tuple(map(float, base_r["solvef"])),
    }
    for j, pair in enumerate(cross_finite_residuals(cross_man), start=1):
        pairs[f"ritz_residual{j}"] = pair
    return pairs


def residual_rows_with_cross_finite(sector, d, cross_man):
    """Run the committed remote certificate and restore finite XR residuals.

    suzuki_kkt_remote_residual_certificate.py predates the residual-cross
    manifest and currently reports zero finite residual for those four jobs.
    We add those finite residuals here before converting to transformed norm.
    """
    jobs = build_jobs(sector, d)
    pairs = all_finite_constraints(sector, cross_man)
    rows = {}

    # beta is encoded inside one_job's transformed_total relation.  Recover
    # it robustly from the remote script's published BETA_CAP via import.
    from suzuki_tail_P4_residual_basis_certificate import BETA_CAP

    for job in jobs:
        row = one_job(sector, job)
        name = row["name"]
        finite_true = pairs[name][0]
        finite_used = float(row["finite_residual"])
        delta_euclid = max(0.0, finite_true - finite_used)
        row["finite_residual"] = finite_true
        row["euclidean_total"] += delta_euclid
        row["transformed_total"] += delta_euclid / math.sqrt(BETA_CAP[sector])
        row["constraint_residual"] = pairs[name][1]
        rows[name] = row

    required = {
        "core1", "core2", "source",
        "ritz_residual1", "ritz_residual2",
        "ritz_residual3", "ritz_residual4",
    }
    missing = required.difference(rows)
    if missing:
        raise RuntimeError(f"remote certificate missing jobs: {sorted(missing)}")
    return rows


def complement_action_error(sector, row):
    """v13.980 eq. (12), with rho*constraint term."""
    M = DINV_CAP[sector]
    rho = RHO_CAP[sector]
    e = float(row["transformed_total"])
    eta = float(row.get("constraint_residual", 0.0))
    return M * (e + rho * eta) + eta


def assemble_nominal(sector, d):
    cross = CROSSROOT / sector
    XR = np.load(cross / "X_R.npy")

    modes = np.asarray(d["modes"], dtype=int)
    core = np.asarray(d["core"], dtype=int)
    Z = np.asarray(d["Z"], dtype=float)
    AZ = np.asarray(d["AZ"], dtype=float)
    theta = np.asarray(d["theta"], dtype=float)
    XC = np.asarray(d["XC"], dtype=float)
    xf = np.asarray(d["xf"], dtype=float)

    R = full_A_block(modes, core, sector)
    ACC = full_A_block(core, core, sector)

    fT = source_vector(modes)
    fC = source_vector(core)

    S = AZ - d["BZ"] @ theta

    HChat = ACC - R.T @ XC
    Keff = Z.T @ R - XR.T @ R
    Jeff = theta - S.T @ XR

    f6 = np.concatenate([
        fC - R.T @ xf,
        Z.T @ fT - S.T @ xf,
    ])
    hreg = float(fT @ xf)

    M6 = np.block([
        [HChat, Keff.T],
        [Keff, Jeff],
    ])
    M6 = (M6 + M6.T) / 2.0

    return dict(
        M6=M6,
        f6=f6,
        hreg=hreg,
        R=R,
        S=S,
        XR=XR,
        XC=XC,
        xf=xf,
        theta=theta,
    )


def interval_one_sector(sector):
    d = sector_data(sector)
    if "XR" not in d:
        raise FileNotFoundError(
            f"{sector}: residual-cross X_R payload has not landed"
        )

    cross_man = load_cross_manifest(sector)
    rows = residual_rows_with_cross_finite(sector, d, cross_man)
    nom = assemble_nominal(sector, d)

    # Exact-complement action errors.
    dc = np.array([
        complement_action_error(sector, rows["core1"]),
        complement_action_error(sector, rows["core2"]),
    ])
    dr = np.array([
        complement_action_error(sector, rows[f"ritz_residual{j}"])
        for j in range(1, 5)
    ])
    df = complement_action_error(sector, rows["source"])

    Delta_C = float(np.linalg.norm(dc))
    Delta_R = float(np.linalg.norm(dr))

    c = C_CAP[sector]
    rho = RHO_CAP[sector]

    # v13.981 eqs. (10), (14), (16).
    epsM = c * Delta_C + (c + rho) * Delta_R + ASSEMBLY_ARITH
    epsf = math.sqrt(c*c + rho*rho) * df + ASSEMBLY_ARITH
    epsh = GSTAR_CAP[sector] * df + ASSEMBLY_ARITH

    M6 = nom["M6"]
    f6 = nom["f6"]
    hreg = nom["hreg"]

    svals = np.linalg.svd(M6, compute_uv=False)
    muhat = float(np.min(svals))
    what = np.linalg.solve(M6, f6)
    qhat = float(f6 @ what)
    Ehat = hreg + qhat

    result = dict(
        sector=sector,
        muhat=muhat,
        epsM=epsM,
        epsf=epsf,
        epsh=epsh,
        nominal_energy=Ehat,
        nominal_reduced=qhat,
        nominal_background=hreg,
        Delta_C=Delta_C,
        Delta_R=Delta_R,
        delta_f=df,
        complement_action_errors={
            k: complement_action_error(sector, rows[k])
            for k in rows
        },
        remote_rows=rows,
    )

    if epsM >= muhat:
        result["closed"] = False
        result["reason"] = (
            "v13.981 inverse-stability gate fails: epsM >= sigma_min(Mhat)"
        )
        return result

    wnorm = float(np.linalg.norm(what))
    fnorm = float(np.linalg.norm(f6))
    deltaw = (epsf + epsM * wnorm) / (muhat - epsM)
    epsq = epsf * wnorm + (fnorm + epsf) * deltaw
    epsE = epsh + epsq

    result.update(
        closed=True,
        wnorm=wnorm,
        fnorm=fnorm,
        deltaw=deltaw,
        epsq=epsq,
        epsE=epsE,
        energy_interval=[Ehat - epsE, Ehat + epsE],
    )
    return result


def kappa_interval(even, odd):
    if not (even.get("closed") and odd.get("closed")):
        return None
    Le, Ue = even["energy_interval"]
    Lo, Uo = odd["energy_interval"]
    if Le <= 0 or Lo <= 0:
        return dict(
            closed=False,
            reason="one parity energy interval is not strictly positive",
            even=[Le, Ue],
            odd=[Lo, Uo],
        )
    return dict(
        closed=True,
        interval=[
            (Le - Uo) / (Le + Uo),
            (Ue - Lo) / (Ue + Lo),
        ],
        even=[Le, Ue],
        odd=[Lo, Uo],
    )


def main():
    missing = [
        str(CROSSROOT / sector)
        for sector in ("even-v", "odd-v")
        if not (CROSSROOT / sector / "X_R.npy").exists()
    ]
    if missing:
        print("WAITING FOR RESIDUAL-CROSS PAYLOAD:")
        for p in missing:
            print(" ", p)
        raise SystemExit(2)

    out = {}
    for sector in ("even-v", "odd-v"):
        print("\nsector =", sector)
        row = interval_one_sector(sector)
        out[sector] = row
        print("nominal energy =", row["nominal_energy"])
        print("sigma_min(Mhat) =", row["muhat"])
        print("epsM =", row["epsM"])
        print("delta_f =", row["delta_f"])
        if row["closed"]:
            print("energy interval =", row["energy_interval"])
        else:
            print("NOT CLOSED:", row["reason"])

    kap = kappa_interval(out["even-v"], out["odd-v"])
    out["kappa"] = kap

    print("\nkappa result =", kap)

    outfile = HERE / "xi_scalar_source_energy_interval_result.json"
    outfile.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("wrote", outfile)

    print("\nGUARDRAIL: finite a=1, absolute lambda=0 scalar only.")
    print("No RH/GRH or a->infinity convergence claim follows.")


if __name__ == "__main__":
    main()
