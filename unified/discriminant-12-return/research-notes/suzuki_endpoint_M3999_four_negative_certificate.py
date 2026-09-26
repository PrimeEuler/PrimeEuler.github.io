#!/usr/bin/env python3
"""Outward certificate for the four frozen negative endpoint directions.

Endpoint:
    F^-_0.10 = A - 0.10 B_sm.

The four core bases are exact-dyadic verifier inputs frozen independently from
the six positive directions.  For each parity, this script certifies negativity
of the exact finite-buffer Schur restriction

    Bneg = Qneg^T (F_CC - F_CF F_FF^{-1} F_FC) Qneg.

Since the corresponding graph vectors have remote coordinate identically zero,
their quadratic form in the full infinite endpoint operator equals this finite
core-buffer quadratic form.  No remote-tail estimate is needed for the lower
index bound.

The arithmetic/error model matches the repaired finite six-plane certificate:
binary64 nominal source data, longdouble residual checks, gamma_n envelopes,
validated source-operator uncertainty 2e-13, plus 1e-14 endpoint reserve.
"""
from __future__ import annotations

from fractions import Fraction
import math
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
    structured_ldl,
    ldl_solve,
)
from suzuki_endpoint_M3999_frozen_four_negative_inputs import (
    EVEN_QNEG_HEX,
    EVEN_LNEG_HEX,
    ODD_QNEG_HEX,
    ODD_LNEG_HEX,
    EVEN_PAYLOAD_SHA256,
    ODD_PAYLOAD_SHA256,
    payload_hash,
    exact_first4_det,
    floats,
)


U64 = 2.0**-53
ULD = float(np.finfo(np.longdouble).eps / 2)
EPS_F = 2.1e-13

KQ_CAP = {
    "even-v": 0.680,
    "odd-v": 0.255,
}
SOLVE_RESIDUAL_CAP = {
    "even-v": 9.00e-16,
    "odd-v": 2.60e-16,
}
REFERENCE_DEFECT_CAP = {
    "even-v": 3.20e-16,
    "odd-v": 1.60e-16,
}


def gamma_n(n: int, u: float) -> float:
    nu = n * u
    if nu >= 1:
        raise RuntimeError("gamma_n invalid")
    return nu / (1.0 - nu)


def fraction_matrix(hex_rows):
    return [
        [Fraction.from_float(float.fromhex(x)) for x in row]
        for row in hex_rows
    ]


def exact_gram_gershgorin(qhex, lhex):
    Q = fraction_matrix(qhex)
    L = fraction_matrix(lhex)
    m = 4

    Gq = [
        [
            sum(Q[k][i] * Q[k][j] for k in range(10))
            for j in range(m)
        ]
        for i in range(m)
    ]
    q_upper = max(
        Gq[i][i]
        + sum(abs(Gq[i][j]) for j in range(m) if j != i)
        for i in range(m)
    )

    Gl = [
        [
            sum(L[i][k] * L[j][k] for k in range(m))
            for j in range(m)
        ]
        for i in range(m)
    ]
    l_lower = min(
        Gl[i][i]
        - sum(abs(Gl[i][j]) for j in range(m) if j != i)
        for i in range(m)
    )

    return (
        np.nextafter(float(q_upper), math.inf),
        np.nextafter(float(l_lower), -math.inf),
    )


def dense_polefree(modes, z, diag):
    A = offdiag(modes, modes, z, z)
    np.fill_diagonal(A, diag)
    return A


def factor_residual_outward(A, L, D):
    n = len(D)
    C = (L * D) @ L.T
    R = A - C
    r_fro = np.linalg.norm(R, "fro")

    M = np.abs(L * D) @ np.abs(L).T
    prod = gamma_n(n + 2, U64) * np.linalg.norm(M, "fro")

    sub = (
        U64 / (1 - U64)
        * (np.linalg.norm(A, "fro") + np.linalg.norm(C, "fro"))
    )

    return np.nextafter(float(r_fro + prod + sub), math.inf)


def inverse_factor_bounds_outward(L):
    n = L.shape[0]
    A = np.abs(L).astype(np.longdouble)

    y = np.ones(n, dtype=np.longdouble)
    for i in range(1, n):
        s = np.dot(A[i, :i], y[:i])
        g = np.longdouble(gamma_n(i, ULD))
        val = (
            np.longdouble(1) + s / (1 - g)
        ) / (1 - np.longdouble(ULD))
        y[i] = np.nextafter(val, np.longdouble(np.inf))

    z = np.ones(n, dtype=np.longdouble)
    for j in range(n - 2, -1, -1):
        m = n - j - 1
        s = np.dot(A[j + 1:, j], z[j + 1:])
        g = np.longdouble(gamma_n(m, ULD))
        val = (
            np.longdouble(1) + s / (1 - g)
        ) / (1 - np.longdouble(ULD))
        z[j] = np.nextafter(val, np.longdouble(np.inf))

    linf = float(np.nextafter(np.max(y), np.longdouble(np.inf)))
    lone = float(np.nextafter(np.max(z), np.longdouble(np.inf)))
    l2 = float(
        np.nextafter(
            np.sqrt(np.longdouble(linf) * np.longdouble(lone)),
            np.longdouble(np.inf),
        )
    )
    return linf, lone, l2


def vector_residual_outward(A, y, b):
    A = np.asarray(A, dtype=np.longdouble)
    y = np.asarray(y, dtype=np.longdouble)
    b = np.asarray(b, dtype=np.longdouble)

    Ay = A @ y
    r = b - Ay
    rp = np.sqrt(np.sum(r * r, dtype=np.longdouble))

    E = (
        np.longdouble(gamma_n(A.shape[1], ULD))
        * (np.abs(A) @ np.abs(y))
        + np.longdouble(ULD) / (1 - np.longdouble(ULD))
        * (np.abs(b) + np.abs(Ay))
    )
    ee = np.sqrt(np.sum(E * E, dtype=np.longdouble))
    return float(np.nextafter(rp + ee, np.longdouble(np.inf)))


def rhs_residual_outward(A, B, Y):
    A = np.asarray(A, dtype=np.longdouble)
    B = np.asarray(B, dtype=np.longdouble)
    Y = np.asarray(Y, dtype=np.longdouble)

    AY = A @ Y
    R = B - AY
    rp = np.sqrt(np.sum(R * R, dtype=np.longdouble))

    E = (
        np.longdouble(gamma_n(A.shape[1], ULD))
        * (np.abs(A) @ np.abs(Y))
        + np.longdouble(ULD) / (1 - np.longdouble(ULD))
        * (np.abs(B) + np.abs(AY))
    )
    ee = np.sqrt(np.sum(E * E, dtype=np.longdouble))
    return float(np.nextafter(rp + ee, np.longdouble(np.inf)))


def negative_reference_defect(C, R, Q, Y, Lneg):
    C = np.asarray(C, dtype=np.longdouble)
    R = np.asarray(R, dtype=np.longdouble)
    Q = np.asarray(Q, dtype=np.longdouble)
    Y = np.asarray(Y, dtype=np.longdouble)
    Lneg = np.asarray(Lneg, dtype=np.longdouble)

    BQ = R.T @ Q
    CQ = C @ Q
    core = Q.T @ CQ
    tail = BQ.T @ Y

    Nhat = -(core - tail)
    Nref = Lneg @ Lneg.T
    D = Nhat - Nref
    dp = np.sqrt(np.sum(D * D, dtype=np.longdouble))

    EBQ = np.longdouble(gamma_n(10, ULD)) * (
        np.abs(R).T @ np.abs(Q)
    )
    ECQ = np.longdouble(gamma_n(10, ULD)) * (
        np.abs(C) @ np.abs(Q)
    )
    Ecore = (
        np.longdouble(gamma_n(10, ULD))
        * (np.abs(Q).T @ np.abs(CQ))
        + np.abs(Q).T @ ECQ
    )
    Etail = (
        np.longdouble(gamma_n(Y.shape[0], ULD))
        * (np.abs(BQ).T @ np.abs(Y))
        + EBQ.T @ np.abs(Y)
    )
    Eref = np.longdouble(gamma_n(4, ULD)) * (
        np.abs(Lneg) @ np.abs(Lneg).T
    )
    Esub = (
        np.longdouble(ULD) / (1 - np.longdouble(ULD))
        * (np.abs(core) + np.abs(tail) + np.abs(Nref))
    )
    E = Ecore + Etail + Eref + Esub
    ee = np.sqrt(np.sum(E * E, dtype=np.longdouble))
    return float(np.nextafter(dp + ee, np.longdouble(np.inf)))


def schur_source_perturbation(eps, K, mu, qnorm2):
    q = math.sqrt(qnorm2)
    if mu <= eps:
        raise RuntimeError("buffer perturbation exceeds floor")
    return (
        qnorm2 * eps
        + 2 * K * q * eps / (mu - eps)
        + qnorm2 * eps * eps / (mu - eps)
        + K * K * eps / (mu * (mu - eps))
    )


def one_sector(sector):
    if sector == "even-v":
        core = np.arange(5, 24, 2, dtype=int)
        buffer_ = np.arange(25, 4000, 2, dtype=int)
        Q = floats(EVEN_QNEG_HEX)
        Lneg = floats(EVEN_LNEG_HEX)
        qhex, lhex = EVEN_QNEG_HEX, EVEN_LNEG_HEX
    elif sector == "odd-v":
        core = np.arange(6, 25, 2, dtype=int)
        buffer_ = np.arange(26, 4001, 2, dtype=int)
        Q = floats(ODD_QNEG_HEX)
        Lneg = floats(ODD_LNEG_HEX)
        qhex, lhex = ODD_QNEG_HEX, ODD_LNEG_HEX
    else:
        raise ValueError(sector)

    expected_hash = (
        EVEN_PAYLOAD_SHA256
        if sector == "even-v"
        else ODD_PAYLOAD_SHA256
    )
    if payload_hash(qhex, lhex) != expected_hash:
        raise RuntimeError("frozen negative payload hash mismatch")
    if exact_first4_det(qhex) == 0:
        raise RuntimeError("frozen negative payload rank test failed")

    modes = np.concatenate([core, buffer_])
    z, diag = endpoint_data(modes)
    zc, zf = z[:10], z[10:]
    dc, df = diag[:10], diag[10:]

    C0 = offdiag(core, core, zc, zc)
    np.fill_diagonal(C0, dc)
    R0 = offdiag(core, buffer_, zc, zf)

    p, alpha = pole_vector(modes, sector)
    pc, pf = p[:10], p[10:]

    C = C0 + alpha * np.outer(pc, pc)
    R = R0 + alpha * np.outer(pc, pf)

    A0 = dense_polefree(buffer_, zf, df)
    L, D = structured_ldl(buffer_, zf, df)

    factor_resid = factor_residual_outward(A0, L, D)
    linf, lone, l2 = inverse_factor_bounds_outward(L)
    dmin = np.nextafter(float(np.min(D)), -math.inf)
    mu0 = dmin / (l2 * l2) - factor_resid
    if mu0 <= 0:
        raise RuntimeError("pole-free buffer floor failed")

    if sector == "even-v":
        mu_nom = mu0
        pole_den_lower = 1.0
    else:
        y = ldl_solve(L, D, pf)
        ry = vector_residual_outward(A0, y, pf)
        inv0 = 1.0 / mu0
        yerr = inv0 * ry

        pnorm = np.linalg.norm(pf)
        yhat_norm = np.linalg.norm(y)
        qhat = (
            np.longdouble(pf.astype(np.longdouble))
            @ np.longdouble(y.astype(np.longdouble))
        )
        qround = gamma_n(len(pf), ULD) * float(
            np.sum(
                np.abs(
                    pf.astype(np.longdouble)
                    * y.astype(np.longdouble)
                ),
                dtype=np.longdouble,
            )
        )
        qupper = float(qhat) + qround + pnorm * yerr
        pole_den_lower = 1.0 - 2.0 * qupper
        if pole_den_lower <= 0:
            raise RuntimeError("negative-pole denominator failed")

        y_upper = yhat_norm + yerr
        invfull = (
            inv0
            + 2.0 * y_upper * y_upper / pole_den_lower
        )
        mu_nom = 1.0 / invfull

    mu_exact = mu_nom - EPS_F
    if mu_exact <= 0:
        raise RuntimeError("exact buffer floor failed")

    BQ = R.T @ Q

    X0 = ldl_solve(L, D, BQ)
    yp = ldl_solve(L, D, pf)
    q = float(pf @ yp)
    den = 1.0 + alpha * q
    Y = X0 - alpha * np.outer(yp, pf @ X0) / den

    Afull = A0 + alpha * np.outer(pf, pf)
    solve_resid = rhs_residual_outward(Afull, BQ, Y)

    KQ_fro = float(
        np.sqrt(
            np.sum(
                BQ.astype(np.longdouble) ** 2,
                dtype=np.longdouble,
            )
        )
    )
    K = KQ_CAP[sector]
    if not KQ_fro < K:
        raise RuntimeError(("negative coupling cap failed", KQ_fro))

    qnorm2, lmin = exact_gram_gershgorin(qhex, lhex)

    ref_defect = negative_reference_defect(
        C, R, Q, Y, Lneg
    )
    if solve_resid > SOLVE_RESIDUAL_CAP[sector]:
        raise RuntimeError(
            ("negative solve residual cap failed", solve_resid)
        )
    if ref_defect > REFERENCE_DEFECT_CAP[sector]:
        raise RuntimeError(
            ("negative reference defect cap failed", ref_defect)
        )

    # Independent algebra check: graph quadratic form and one-sided Schur
    # expression differ only by the solve residual.
    BQ64 = R.T @ Q
    schur_one_sided = Q.T @ C @ Q - BQ64.T @ Y
    graph_form = (
        Q.T @ C @ Q
        - BQ64.T @ Y
        - Y.T @ BQ64
        + Y.T @ Afull @ Y
    )
    graph_discrepancy = np.linalg.norm(
        graph_form - schur_one_sided,
        2,
    )
    graph_bound = (
        np.linalg.norm(Y, 2)
        * SOLVE_RESIDUAL_CAP[sector]
        + 5e-15
    )
    if graph_discrepancy > graph_bound:
        raise RuntimeError(
            ("graph/Schur consistency failed", graph_discrepancy)
        )

    eps_source = schur_source_perturbation(
        EPS_F, K, mu_nom, qnorm2
    )
    eps_solve = (
        K / mu_nom * SOLVE_RESIDUAL_CAP[sector]
    )
    eps_total = (
        REFERENCE_DEFECT_CAP[sector]
        + eps_solve
        + eps_source
    )

    eta = eps_total / lmin
    normalized_negative_lower = 1.0 - eta
    raw_negative_margin = lmin - eps_total

    return {
        "sector": sector,
        "factor_residual": factor_resid,
        "linv_inf": linf,
        "linv_one": lone,
        "linv_two": l2,
        "mu_nominal": mu_nom,
        "mu_exact": mu_exact,
        "pole_den_lower": pole_den_lower,
        "KQ_fro": KQ_fro,
        "KQ_cap": K,
        "solve_residual": solve_resid,
        "solve_residual_cap": SOLVE_RESIDUAL_CAP[sector],
        "reference_defect": ref_defect,
        "reference_defect_cap": REFERENCE_DEFECT_CAP[sector],
        "qnorm2_upper": qnorm2,
        "LnegLnegT_min_lower": lmin,
        "eps_source": eps_source,
        "eps_solve": eps_solve,
        "eps_total": eps_total,
        "graph_discrepancy": graph_discrepancy,
        "graph_bound": graph_bound,
        "normalized_negative_lower": normalized_negative_lower,
        "raw_negative_margin": raw_negative_margin,
    }


def report():
    rows = [one_sector("even-v"), one_sector("odd-v")]

    for row in rows:
        print("\nsector =", row["sector"])
        for k, v in row.items():
            if k != "sector":
                print(k, "=", v)

    even, odd = rows

    assert even["normalized_negative_lower"] > 0.99999935
    assert odd["normalized_negative_lower"] > 0.99999986

    assert even["raw_negative_margin"] > 0.0292493433
    assert odd["raw_negative_margin"] > 0.0300224607

    print("\nPASS: four exact frozen negative directions certified")
    print(
        "even: Q^T S_exact Q < -0.0292493433 I"
    )
    print(
        "odd:  Q^T S_exact Q < -0.0300224607 I"
    )
    print(
        "These four-dimensional graph subspaces have remote coordinate zero, "
        "so they are genuine negative trial spaces for the infinite endpoint "
        "operator. No remote-tail estimate enters this lower-index proof."
    )


if __name__ == "__main__":
    report()
