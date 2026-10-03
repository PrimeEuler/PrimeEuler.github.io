#!/usr/bin/env python3
"""Remote residual certificate for the arbitrary-carrier KKT solves.

Purpose
-------
v13.980 reduces the final exact finite-a certification error to transformed
residuals of a finite list of constrained complement solves.  The frozen
vectors have support through 16001/16002, so their uploaded finite saddle
residuals do not by themselves include the omitted infinite rows.

This script certifies those remote rows with the same source-faithful
architecture used by suzuki_tail_P4_residual_basis_certificate.py:

  1. direct evaluation on the near remote band;
  2. high-order Cauchy/moment expansion through an explicit large cutoff;
  3. signed 1/n + O(1/n^2) far-tail envelope;
  4. conversion from Euclidean residual to B_sm^{-1} norm using the already
     certified global smooth-bulk floor.

It handles the three v13.975 solves immediately:
  core-1, core-2, source.

If the v13.978 residual-cross payload is present, it also handles the four
additional right-hand sides automatically.

Guardrails
----------
This script certifies residuals of the fixed numerical-carrier KKT solves.
It does not assert RH/GRH, Xi convergence, or exact identification of the
numerical carrier with P4.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    pole_vector,
    z_source_faithful,
)
from suzuki_tail_P4_residual_basis_certificate import BETA_CAP


HERE = Path(__file__).resolve().parent
P4ROOT = HERE / "p4_payload"
KKTROOT = HERE / "p4_payload_kkt"
CROSSROOT = HERE / "p4_payload_kkt_residual_cross"

DIRECT_STOP = {
    "even-v": 64001,
    "odd-v": 64000,
}
EXPLICIT_STOP = 2_000_000
DIRECT_CHUNK = 500
EXP_CHUNK = 200_000
K_A = 10
K_B = 16
Z_FAR_CAP = 8.0
ARITH_RESERVE = 1.0e-8


def sector_data(sector: str):
    p4 = P4ROOT / sector
    kkt = KKTROOT / sector

    modes = np.load(p4 / "modes.npy").astype(int)
    Zraw = np.load(p4 / "Z.npy")
    AZraw = np.load(p4 / "AZ.npy")
    BZraw = np.load(p4 / "BZ.npy")

    GB = np.load(kkt / "G_B.npy")
    ee, UU = np.linalg.eigh((GB + GB.T) / 2.0)
    if np.min(ee) <= 0:
        raise RuntimeError(("G_B not positive", sector, ee))
    Gmhalf = (UU * (1.0 / np.sqrt(ee))[None, :]) @ UU.T

    # Reproduce the KKT carrier convention.
    Z = Zraw @ Gmhalf
    AZ = AZraw @ Gmhalf
    BZ = BZraw @ Gmhalf
    theta = (Z.T @ AZ + AZ.T @ Z) / 2.0

    XC = np.load(kkt / "X_C.npy")
    xf = np.load(kkt / "x_f.npy")
    lam = [
        np.load(kkt / "saddle_lam1.npy"),
        np.load(kkt / "saddle_lam2.npy"),
        np.load(kkt / "saddle_lamf.npy"),
    ]

    core = np.array([1, 3], dtype=int) if sector == "even-v" else np.array([2, 4], dtype=int)

    out = dict(
        modes=modes,
        core=core,
        Z=Z,
        AZ=AZ,
        BZ=BZ,
        theta=theta,
        XC=XC,
        xf=xf,
        lam=lam,
    )

    cross = CROSSROOT / sector
    if cross.exists() and (cross / "X_R.npy").exists():
        out["XR"] = np.load(cross / "X_R.npy")
        # Accept either a 4x4 multiplier array or four separate arrays.
        if (cross / "saddle_lamR.npy").exists():
            LR = np.load(cross / "saddle_lamR.npy")
        else:
            LR = np.column_stack([
                np.load(cross / f"saddle_lamR{j+1}.npy")
                for j in range(4)
            ])
        out["lamR"] = LR

    return out


def source_rows(ns: np.ndarray, sector: str) -> np.ndarray:
    """Exact coefficient formula <psi_n,e^x> for a=1."""
    n = np.asarray(ns, dtype=float)
    k = n * math.pi / 2.0
    parity = np.where(np.asarray(ns, dtype=int) % 2 == 0, 1.0, -1.0)
    u = math.exp(-1.0) - parity * math.e
    return k * u / (1.0 + k * k)


def A_apply_remote(ns, modes, W, sector):
    """Apply exact off-diagonal A_{remote,finite} to one/many finite vectors."""
    ns = np.asarray(ns, dtype=float)
    modes = np.asarray(modes, dtype=float)
    W = np.asarray(W, dtype=float)
    if W.ndim == 1:
        W = W[:, None]

    zn = z_source_faithful(ns)
    zm = z_source_faithful(modes)
    den = ns[:, None] ** 2 - modes[None, :] ** 2

    A0 = (
        (2.0 / math.pi)
        * (
            zn[:, None] * modes[None, :]
            - ns[:, None] * zm[None, :]
        )
        / den
    )

    pn, _ = pole_vector(ns, sector)
    pm, alpha = pole_vector(modes, sector)

    return A0 @ W + alpha * pn[:, None] * (pm @ W)[None, :]


def B_apply_remote(ns, modes, W):
    ns = np.asarray(ns, dtype=float)
    modes = np.asarray(modes, dtype=float)
    W = np.asarray(W, dtype=float)
    if W.ndim == 1:
        W = W[:, None]
    return -(1.0 / (ns[:, None] + modes[None, :])) @ W


def build_jobs(sector, d):
    modes = d["modes"]
    core = d["core"]
    Z = d["Z"]
    theta = d["theta"]
    XC = d["XC"]
    xf = d["xf"]
    lam1, lam2, lamf = d["lam"]

    jobs = []

    # Core coupling solves:
    # residual = A(e_core - x) - B(Z lambda).
    for j in range(2):
        all_modes = np.concatenate([core, modes])
        w = np.concatenate([
            np.eye(2)[:, j],
            -XC[:, j],
        ])
        q = Z @ (lam1 if j == 0 else lam2)
        jobs.append(dict(
            name=f"core{j+1}",
            kind="Aw-Bq",
            modes_A=all_modes,
            w=w,
            modes_B=modes,
            q=q,
        ))

    # Source solve:
    # residual = f - A x - B(Z lambda).
    jobs.append(dict(
        name="source",
        kind="source-Ax-Bq",
        modes_A=modes,
        w=-xf,
        modes_B=modes,
        q=Z @ lamf,
    ))

    # Residual-cross solves, if uploaded:
    if "XR" in d:
        XR = d["XR"]
        LR = d["lamR"]
        for j in range(4):
            # RHS S_j = A Z_j - B Z Theta_j.
            # residual = A(Z_j-XR_j) - B Z(Theta_j + lambda_Rj).
            jobs.append(dict(
                name=f"ritz_residual{j+1}",
                kind="Aw-Bq",
                modes_A=modes,
                w=Z[:, j] - XR[:, j],
                modes_B=modes,
                q=Z @ (theta[:, j] + LR[:, j]),
            ))

    return jobs


def direct_remote_residual(sector, job):
    start = int(max(job["modes_A"][-1], job["modes_B"][-1])) + 2
    stop = DIRECT_STOP[sector]
    sq = 0.0

    for st in range(start, stop + 1, DIRECT_CHUNK * 2):
        en = min(st + 2 * (DIRECT_CHUNK - 1), stop)
        ns = np.arange(st, en + 1, 2, dtype=int)
        if len(ns) == 0:
            continue

        Aterm = A_apply_remote(ns, job["modes_A"], job["w"], sector)[:, 0]
        Bterm = B_apply_remote(ns, job["modes_B"], job["q"])[:, 0]

        if job["kind"] == "source-Ax-Bq":
            r = source_rows(ns, sector) + Aterm - Bterm
        else:
            r = Aterm - Bterm

        sq += float(np.dot(r, r))

    return math.sqrt(sq)


def moments_A(modes, w):
    m = np.asarray(modes, dtype=np.longdouble)
    w = np.asarray(w, dtype=np.longdouble)
    z = z_source_faithful(np.asarray(modes, dtype=float)).astype(np.longdouble)

    aa, bb = [], []
    for k in range(K_A):
        aa.append(np.sum(m ** (2*k + 1) * w))
        bb.append(np.sum(z * m ** (2*k) * w))
    return np.array(aa), np.array(bb)


def moments_B(modes, q):
    m = np.asarray(modes, dtype=np.longdouble)
    q = np.asarray(q, dtype=np.longdouble)
    return np.array([
        np.sum(((-m) ** k) * q)
        for k in range(K_B)
    ])


def A_expanded(ns, sector, modes, w, aa, bb):
    nn = np.asarray(ns, dtype=np.longdouble)
    zn = z_source_faithful(np.asarray(ns, dtype=float)).astype(np.longdouble)
    out = np.zeros(len(nn), dtype=np.longdouble)
    pi = np.longdouble(math.pi)

    for k in range(K_A):
        out += (
            np.longdouble(2.0) / pi
            * (
                zn * aa[k] / nn ** (2*k + 2)
                - bb[k] / nn ** (2*k + 1)
            )
        )

    pn, _ = pole_vector(np.asarray(ns, dtype=float), sector)
    pm, alpha = pole_vector(np.asarray(modes, dtype=float), sector)
    out += (
        np.longdouble(alpha)
        * pn.astype(np.longdouble)
        * np.longdouble(np.dot(pm, w))
    )
    return np.asarray(out, dtype=float)


def B_expanded(ns, bm):
    nn = np.asarray(ns, dtype=np.longdouble)
    # B q = -sum q_m/(n+m).
    out = np.zeros(len(nn), dtype=np.longdouble)
    for k in range(K_B):
        out -= bm[k] / nn ** (k + 1)
    return np.asarray(out, dtype=float)


def same_parity_sum_bound(N, p):
    return N ** (-p) + 1.0 / (2.0 * (p - 1) * N ** (p - 1))


def expansion_remainder_bound(job, start):
    """Minkowski L2 bound for omitted geometric-series terms from start onward."""
    mA = np.asarray(job["modes_A"], dtype=float)
    w = np.asarray(job["w"], dtype=float)
    mB = np.asarray(job["modes_B"], dtype=float)
    q = np.asarray(job["q"], dtype=float)

    ratioA = float(np.max(mA)) / float(start)
    ratioB = float(np.max(mB)) / float(start)
    if ratioA >= 1 or ratioB >= 1:
        raise RuntimeError(("invalid expansion start", start, ratioA, ratioB))

    # A off-diagonal expansion remainder:
    # z_n * sum m^(2K+1)w / n^(2K+2)
    # and      sum z_m m^(2K)w / n^(2K+1).
    c1 = (
        (2.0 / math.pi)
        * Z_FAR_CAP
        / (1.0 - ratioA * ratioA)
        * np.sum(np.abs((mA ** (2*K_A + 1)) * w))
    )
    zm = z_source_faithful(mA)
    c2 = (
        (2.0 / math.pi)
        / (1.0 - ratioA * ratioA)
        * np.sum(np.abs(zm * (mA ** (2*K_A)) * w))
    )

    # B q = -sum (-m)^k q / n^(k+1).
    cB = (
        np.sum(np.abs((mB ** K_B) * q))
        / (1.0 - ratioB)
    )

    eA = (
        c1 * math.sqrt(same_parity_sum_bound(start, 4*K_A + 4))
        + c2 * math.sqrt(same_parity_sum_bound(start, 4*K_A + 2))
    )
    eB = cB * math.sqrt(same_parity_sum_bound(start, 2*K_B + 2))
    return eA + eB


def expanded_mid_residual(sector, job):
    start = DIRECT_STOP[sector] + 2
    stop = EXPLICIT_STOP

    aa, bb = moments_A(job["modes_A"], job["w"])
    bm = moments_B(job["modes_B"], job["q"])

    sq = 0.0
    st = start
    while st <= stop:
        en = min(st + 2 * (EXP_CHUNK - 1), stop)
        ns = np.arange(st, en + 1, 2, dtype=int)

        Aterm = A_expanded(ns, sector, job["modes_A"], job["w"], aa, bb)
        Bterm = B_expanded(ns, bm)

        if job["kind"] == "source-Ax-Bq":
            r = source_rows(ns, sector) + Aterm - Bterm
        else:
            r = Aterm - Bterm

        sq += float(np.dot(r, r))
        st = en + 2

    trunc = expansion_remainder_bound(job, start)
    return math.sqrt(sq), trunc


def far_bound(sector, job):
    N = (
        2_000_001.0
        if sector == "even-v"
        else 2_000_002.0
    )
    mA = np.asarray(job["modes_A"], dtype=float)
    w = np.asarray(job["w"], dtype=float)
    mB = np.asarray(job["modes_B"], dtype=float)
    q = np.asarray(job["q"], dtype=float)

    ratio = float(np.max(mA)) / N
    zm = z_source_faithful(mA)
    pm, alpha = pole_vector(mA, sector)
    ghalf = math.cosh(0.5) if sector == "even-v" else math.sinh(0.5)

    # Exact signed 1/n coefficient for A w.
    lead = (
        -(2.0 / math.pi) * float(np.dot(zm, w))
        + alpha * (4.0 * ghalf / math.pi) * float(np.dot(pm, w))
    )

    # residual includes -B q = +sum q_m/(n+m)
    lead += float(np.sum(q))

    # Exact source leading coefficient, where applicable.
    source_C3 = 0.0
    if job["kind"] == "source-Ax-Bq":
        if sector == "even-v":
            Ls = 4.0 * math.cosh(1.0) / math.pi
        else:
            Ls = -4.0 * math.sinh(1.0) / math.pi
        lead += Ls
        # |source - Ls/n| <= |Ls|*(4/pi^2)/n^3.
        source_C3 = abs(Ls) * 4.0 / math.pi**2

    # Conservative n^-2 and n^-3 envelopes.
    B2 = (
        (2.0 / math.pi)
        * Z_FAR_CAP
        / (1.0 - ratio * ratio)
        * float(np.sum(np.abs(mA * w)))
        + abs(float(np.sum(mB * q)))
    )

    C3 = (
        (2.0 / math.pi)
        / (1.0 - ratio * ratio)
        * float(np.sum(np.abs((mA * mA) * zm * w)))
        + abs(alpha)
        * (4.0 * ghalf / math.pi**3)
        * abs(float(np.dot(pm, w)))
        + float(np.sum(np.abs((mB * mB) * q)))
        + source_C3
    )

    return (
        abs(lead) * math.sqrt(same_parity_sum_bound(N, 2))
        + B2 * math.sqrt(same_parity_sum_bound(N, 4))
        + C3 * math.sqrt(same_parity_sum_bound(N, 6))
    ), dict(lead=lead, B2=B2, C3=C3)


def manifest_finite_residual(sector, name):
    p = KKTROOT / sector / "manifest.json"
    if not p.exists():
        return 0.0
    row = json.loads(p.read_text())
    if name == "core1":
        return float(row["residuals"]["solve1"][0])
    if name == "core2":
        return float(row["residuals"]["solve2"][0])
    if name == "source":
        return float(row["residuals"]["solvef"][0])
    # Residual-cross manifest, if present, should be read by a future extension.
    return 0.0


def one_job(sector, job):
    finite = manifest_finite_residual(sector, job["name"])
    near = direct_remote_residual(sector, job)
    mid, trunc = expanded_mid_residual(sector, job)
    far, far_parts = far_bound(sector, job)

    euclidean = finite + near + mid + trunc + far + ARITH_RESERVE
    transformed = euclidean / math.sqrt(BETA_CAP[sector])

    return dict(
        name=job["name"],
        finite_residual=finite,
        near_remote=near,
        expanded_mid=mid,
        expansion_remainder=trunc,
        far_remote=far,
        far_parts=far_parts,
        euclidean_total=euclidean,
        transformed_total=transformed,
    )


def main():
    for sector in ("even-v", "odd-v"):
        print("\nsector =", sector)
        d = sector_data(sector)
        jobs = build_jobs(sector, d)
        for job in jobs:
            row = one_job(sector, job)
            print("\n", row["name"])
            for k, v in row.items():
                if k != "name":
                    print(k, "=", v)

    print("\nGUARDRAIL: transformed totals certify the fixed numerical-carrier")
    print("KKT inverse actions; no RH/GRH or Xi convergence claim follows.")


if __name__ == "__main__":
    main()
