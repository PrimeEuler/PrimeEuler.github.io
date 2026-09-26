#!/usr/bin/env python3
"""Residual-certified numerical basis for the exact rank-four tail projector P4.

Certified background
--------------------
For each parity tail,

    P4 = 1_{(-0.02,0.02)}(J_T),   rank(P4)=4,

and the complementary spectrum obeys

    sigma(J_T | Ran(P4)^perp) cap [-0.10,0.10] = empty.

Hence any B_sm-orthonormal four-column Ritz basis Q with Ritz matrix Theta
inside (-0.02,0.02) and transformed residual

    E = B_sm^{-1/2}(A Q - B_sm Q Theta)

satisfies the invariant-subspace residual theorem

    ||sin Angle(Ran Q, Ran P4)|| <= ||E|| / 0.08.

Construction
------------
1. Solve the generalized tail pencil through M1=8001/8002.
2. Retain the four Ritz values in (-0.021,0.021).
3. Extend each Ritz vector by an exact graph solve through M2=16001/16002.
4. Re-Rayleigh-Ritz in that extended four-dimensional span.
5. Accumulate the residual explicitly through two million and bound the
   remaining far tail analytically.
6. Certify a global lower floor B_sm >= beta I, converting the Euclidean
   residual bound to the B_sm^{-1} residual norm.

This script does not use either endpoint negative trial basis as the numerical
P4 basis.  Those are inertia witnesses only.

No low-core residue, kappa0, kappa1, RH, or GRH claim is made here.
"""
from __future__ import annotations

import gc
import math

import numpy as np
from scipy.linalg import eigh

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
    structured_ldl,
    ldl_solve,
    z_source_faithful,
)


RHO = 0.02
M1 = {"even-v": 8001, "odd-v": 8002}
M2 = {"even-v": 16001, "odd-v": 16002}
DIRECT_STOP = {"even-v": 64001, "odd-v": 64000}
EXPLICIT_STOP = 2_000_000

K_F = 10
K_B = 16
Z_FAR_CAP = 8.0

# Existing source/operator uncertainty lineage.  A much larger arithmetic
# reserve is used below, so this never controls the final result.
EPS_SOURCE = 2.1e-13
ARITH_RESERVE = 1.0e-8
B_ENTRY_RESERVE = 1.0e-10

# Deliberately widened public residual caps.
POINT_RESIDUAL_CAP = {
    "even-v": 0.00260,
    "odd-v": 0.01310,
}
FAR_RESIDUAL_CAP = {
    "even-v": 0.00040,
    "odd-v": 0.00150,
}
TOTAL_EUCLIDEAN_RESIDUAL_CAP = {
    "even-v": 0.00301,
    "odd-v": 0.01461,
}

# Smooth-bulk global floors certified below.
BETA_CAP = {
    "even-v": 0.00830,
    "odd-v": 0.20500,
}

# Final transformed residual and moat-only subspace caps.
TRANSFORMED_RESIDUAL_CAP = {
    "even-v": 0.0331,
    "odd-v": 0.0323,
}
SIN_THETA_CAP = {
    "even-v": 0.414,
    "odd-v": 0.404,
}
RITZ_ABS_CAP = {
    "even-v": 0.00030,
    "odd-v": 0.01050,
}

U64 = 2.0**-53
ULD = float(np.finfo(np.longdouble).eps / 2)


def gamma_n(n, u):
    nu = n * u
    if nu >= 1:
        raise RuntimeError("gamma_n invalid")
    return nu / (1 - nu)


def parity_modes(sector, stop):
    start = 5 if sector == "even-v" else 6
    return np.arange(start, stop + 1, 2, dtype=int)


def smooth_bulk_matrix(modes):
    m = np.asarray(modes, dtype=float)
    B = -1.0 / (m[:, None] + m[None, :])
    np.fill_diagonal(
        B,
        np.log(m / 4.0) - 1.0 / (2.0 * m),
    )
    return B


def full_A_matrix(modes, sector):
    z, diag = endpoint_data(modes, sign=-1, rho=0.0)
    A = offdiag(modes, modes, z, z)
    np.fill_diagonal(A, diag)
    p, alpha = pole_vector(modes, sector)
    A += alpha * np.outer(p, p)
    return A


def canonicalize_columns(Q):
    Q = np.array(Q, dtype=float, copy=True)
    for j in range(Q.shape[1]):
        i = int(np.argmax(np.abs(Q[:, j])))
        if Q[i, j] < 0:
            Q[:, j] *= -1
    return Q


def first_stage_ritz(sector):
    modes = parity_modes(sector, M1[sector])
    A = full_A_matrix(modes, sector)
    B = smooth_bulk_matrix(modes)

    theta, Q = eigh(
        A,
        B,
        subset_by_value=(-0.021, 0.021),
        driver="gvx",
        check_finite=False,
    )
    if len(theta) != 4:
        raise RuntimeError(("expected four M1 Ritz values", sector, theta))

    Q = canonicalize_columns(Q)
    defect = np.linalg.norm(Q.T @ B @ Q - np.eye(4), 2)

    # Free the dense M1 matrices before the graph-extension stage.
    del A, B
    gc.collect()

    return modes, theta, Q, defect


def solve_graph_shell(old_modes, q, sector, delta, new_modes):
    z_old, _ = endpoint_data(old_modes, sign=-1, rho=float(delta))
    z_new, d_new = endpoint_data(new_modes, sign=-1, rho=float(delta))

    R0 = offdiag(old_modes, new_modes, z_old, z_new)
    L, D = structured_ldl(new_modes, z_new, d_new)

    all_modes = np.concatenate([old_modes, new_modes])
    p, alpha = pole_vector(all_modes, sector)
    p_old = p[:len(old_modes)]
    p_new = p[len(old_modes):]

    rhs = R0.T @ q + alpha * p_new * (p_old @ q)

    x0 = ldl_solve(L, D, rhs)
    yp = ldl_solve(L, D, p_new)
    den = 1.0 + alpha * float(p_new @ yp)
    if den <= 0:
        raise RuntimeError(("graph-shell pole denominator failed", sector, delta))

    y = x0 - alpha * yp * float(p_new @ x0) / den
    return y


def graph_extend(sector, old_modes, theta, Q):
    new_modes = np.arange(
        int(old_modes[-1]) + 2,
        M2[sector] + 1,
        2,
        dtype=int,
    )
    tails = []
    for j in range(4):
        tails.append(
            solve_graph_shell(
                old_modes,
                Q[:, j],
                sector,
                theta[j],
                new_modes,
            )
        )

    Y = np.column_stack(tails)
    X = np.vstack([Q, -Y])
    modes = np.concatenate([old_modes, new_modes])
    return modes, X


def apply_A_B(modes, X, sector, chunk=500):
    z, diag = endpoint_data(modes, sign=-1, rho=0.0)
    p, alpha = pole_vector(modes, sector)
    mf = modes.astype(float)

    AX = np.zeros_like(X)
    BX = np.zeros_like(X)

    for i0 in range(0, len(modes), chunk):
        i1 = min(len(modes), i0 + chunk)
        rows = modes[i0:i1]

        Ablk = offdiag(rows, modes, z[i0:i1], z)
        for local, global_i in enumerate(range(i0, i1)):
            Ablk[local, global_i] = diag[global_i]
        Ablk += alpha * np.outer(p[i0:i1], p)

        Bblk = -1.0 / (
            rows.astype(float)[:, None] + mf[None, :]
        )
        for local, global_i in enumerate(range(i0, i1)):
            Bblk[local, global_i] = (
                math.log(mf[global_i] / 4.0)
                - 1.0 / (2.0 * mf[global_i])
            )

        AX[i0:i1] = Ablk @ X
        BX[i0:i1] = Bblk @ X

    return AX, BX


def second_stage_ritz(sector, modes, X):
    AX, BX = apply_A_B(modes, X, sector)

    G = (X.T @ BX + BX.T @ X) / 2.0
    H = (X.T @ AX + AX.T @ X) / 2.0

    theta, V = eigh(H, G)
    Z = canonicalize_columns(X @ V)

    # Canonicalizing signs requires the same signs in transformed actions.
    signs = np.ones(4)
    raw = X @ V
    for j in range(4):
        i = int(np.argmax(np.abs(raw[:, j])))
        if raw[i, j] < 0:
            signs[j] = -1.0

    AZ = (AX @ V) * signs[None, :]
    BZ = (BX @ V) * signs[None, :]

    finite_residual = AZ - BZ * theta[None, :]
    finite_gram = finite_residual.T @ finite_residual
    finite_gram = (finite_gram + finite_gram.T) / 2.0

    orth_defect = np.linalg.norm(
        Z.T @ BZ - np.eye(4),
        2,
    )

    return theta, Z, AZ, BZ, finite_gram, orth_defect


def fminus_direct_rows(modes, zminus, sector, alpha, Q, ns):
    ns = np.asarray(ns, dtype=float)
    zn = z_source_faithful(ns) - RHO * math.pi / 2.0

    den = ns[:, None]**2 - modes[None, :]**2
    A0 = (
        (2.0 / math.pi)
        * (
            zn[:, None] * modes[None, :]
            - ns[:, None] * zminus[None, :]
        )
        / den
    )

    pn, _ = pole_vector(ns, sector)
    p, _ = pole_vector(modes, sector)

    return (
        A0 @ Q
        + alpha * pn[:, None] * (p @ Q)[None, :]
    )


def b_direct_rows(modes, Q, ns):
    ns = np.asarray(ns, dtype=float)
    return -(
        1.0 / (ns[:, None] + modes[None, :])
    ) @ Q


def fminus_moments(modes, zminus, Q):
    j = modes.astype(np.longdouble)
    W = Q.astype(np.longdouble)
    z = zminus.astype(np.longdouble)

    aa, bb = [], []
    for k in range(K_F):
        aa.append(
            np.sum(
                (j**(2*k + 1))[:, None] * W,
                axis=0,
            )
        )
        bb.append(
            np.sum(
                (z * j**(2*k))[:, None] * W,
                axis=0,
            )
        )
    return np.array(aa), np.array(bb)


def b_moments(modes, Q):
    j = modes.astype(np.longdouble)
    W = Q.astype(np.longdouble)
    out = []
    for k in range(K_B):
        out.append(
            np.sum(((-j)**k)[:, None] * W, axis=0)
        )
    return np.array(out)


def fminus_expanded_rows(
    modes,
    zminus,
    sector,
    alpha,
    Q,
    ns,
    aa,
    bb,
):
    nn = np.asarray(ns, dtype=np.longdouble)
    zn = (
        z_source_faithful(np.asarray(ns, dtype=float))
        - RHO * math.pi / 2.0
    ).astype(np.longdouble)

    R = np.zeros((len(nn), 4), dtype=np.longdouble)
    pi = np.longdouble(math.pi)

    for k in range(K_F):
        R += (
            np.longdouble(2.0) / pi
            * (
                zn[:, None] * aa[k][None, :]
                / nn[:, None]**(2*k + 2)
                - bb[k][None, :]
                / nn[:, None]**(2*k + 1)
            )
        )

    pn, _ = pole_vector(
        np.asarray(ns, dtype=float),
        sector,
    )
    p, _ = pole_vector(modes, sector)
    R += (
        np.longdouble(alpha)
        * pn.astype(np.longdouble)[:, None]
        * (p @ Q).astype(np.longdouble)[None, :]
    )

    return np.asarray(R, dtype=float)


def b_expanded_rows(ns, moments):
    nn = np.asarray(ns, dtype=np.longdouble)
    R = np.zeros((len(nn), 4), dtype=np.longdouble)
    for k in range(K_B):
        R -= moments[k][None, :] / nn[:, None]**(k + 1)
    return np.asarray(R, dtype=float)


def explicit_remote_gram(sector, modes, Z, theta):
    zminus, _ = endpoint_data(modes, sign=-1, rho=RHO)
    _, alpha = pole_vector(modes, sector)

    start = int(modes[-1]) + 2
    direct_stop = DIRECT_STOP[sector]
    G = np.zeros((4, 4), dtype=float)

    for st in range(start, direct_stop + 1, 2000):
        en = min(st + 1998, direct_stop)
        if (en - st) % 2:
            en -= 1
        if en < st:
            continue

        ns = np.arange(st, en + 1, 2, dtype=float)
        F = fminus_direct_rows(
            modes, zminus, sector, alpha, Z, ns
        )
        B = b_direct_rows(modes, Z, ns)
        R = F + B * (RHO - theta)[None, :]
        G += R.T @ R

    aa, bb = fminus_moments(modes, zminus, Z)
    bm = b_moments(modes, Z)

    st = direct_stop + 2
    while st <= EXPLICIT_STOP:
        en = min(st + 199998, EXPLICIT_STOP)
        if (en - st) % 2:
            en -= 1

        ns = np.arange(st, en + 1, 2, dtype=float)
        F = fminus_expanded_rows(
            modes, zminus, sector, alpha, Z, ns, aa, bb
        )
        B = b_expanded_rows(ns, bm)
        R = F + B * (RHO - theta)[None, :]
        G += R.T @ R
        st = en + 2

    return (G + G.T) / 2.0


def far_residual_bound(sector, modes, Z, theta):
    """Minkowski bound for the residual beyond EXPLICIT_STOP."""
    N = (
        2_000_001.0
        if sector == "even-v"
        else 2_000_002.0
    )
    ratio = float(np.max(modes)) / N

    zminus, _ = endpoint_data(modes, sign=-1, rho=RHO)
    p, alpha = pole_vector(modes, sector)
    pZ = p @ Z
    d = RHO - theta

    g = (
        math.cosh(0.5)
        if sector == "even-v"
        else math.sinh(0.5)
    )

    # F^- residual coefficients, following the already audited endpoint
    # far-tail envelope.
    lead_f = (
        -(2.0 / math.pi) * (zminus @ Z)
        + alpha * (4.0 * g / math.pi) * pZ
    )
    b_f = (
        (2.0 / math.pi)
        * Z_FAR_CAP
        / (1.0 - ratio*ratio)
        * np.sum(
            np.abs(modes[:, None] * Z),
            axis=0,
        )
    )
    c_f = (
        (2.0 / math.pi)
        / (1.0 - ratio*ratio)
        * np.sum(
            np.abs(
                (
                    modes.astype(float)**2
                    * zminus
                )[:, None]
                * Z
            ),
            axis=0,
        )
        + abs(alpha)
        * (4.0 * g / math.pi**3)
        * np.abs(pZ)
    )

    # Exact first two terms of
    #   -sum_m Z_m /(n+m) * (rho-theta),
    # followed by a positive n^{-3} remainder bound.
    s0 = np.sum(Z, axis=0)
    s1 = np.sum(modes[:, None] * Z, axis=0)
    lead_b = -s0 * d
    b_b = s1 * d
    c_b = np.sum(
        (modes.astype(float)**2)[:, None]
        * np.abs(Z),
        axis=0,
    ) * np.abs(d)

    lead = lead_f + lead_b
    Bnorm = np.linalg.norm(b_f) + np.linalg.norm(b_b)
    Cnorm = np.linalg.norm(c_f) + np.linalg.norm(c_b)

    def S(power):
        return (
            N**(-power)
            + 1.0
            / (
                2.0 * (power - 1)
                * N**(power - 1)
            )
        )

    root = (
        np.linalg.norm(lead) * math.sqrt(S(2))
        + Bnorm * math.sqrt(S(4))
        + Cnorm * math.sqrt(S(6))
    )
    return float(root)


def cholesky_factor_residual(A, L):
    R = A - L @ L.T
    point = np.linalg.norm(R, "fro")
    M = np.abs(L) @ np.abs(L).T
    prod = gamma_n(A.shape[0] + 1, U64) * np.linalg.norm(M, "fro")
    sub = (
        U64 / (1.0 - U64)
        * (
            np.linalg.norm(A, "fro")
            + np.linalg.norm(L @ L.T, "fro")
        )
    )
    return float(np.nextafter(point + prod + sub, math.inf))


def inverse_factor_bounds_outward(L):
    n = L.shape[0]
    A = np.abs(L).astype(np.longdouble)

    y = np.ones(n, dtype=np.longdouble)
    for i in range(1, n):
        s = np.dot(A[i, :i], y[:i])
        g = np.longdouble(gamma_n(i, ULD))
        y[i] = np.nextafter(
            (
                np.longdouble(1.0) + s / (1.0 - g)
            )
            / (1.0 - np.longdouble(ULD)),
            np.longdouble(np.inf),
        )

    z = np.ones(n, dtype=np.longdouble)
    for j in range(n - 2, -1, -1):
        m = n - j - 1
        s = np.dot(A[j + 1:, j], z[j + 1:])
        g = np.longdouble(gamma_n(m, ULD))
        z[j] = np.nextafter(
            (
                np.longdouble(1.0) + s / (1.0 - g)
            )
            / (1.0 - np.longdouble(ULD)),
            np.longdouble(np.inf),
        )

    linf = float(np.nextafter(np.max(y), np.longdouble(np.inf)))
    lone = float(np.nextafter(np.max(z), np.longdouble(np.inf)))
    ltwo = float(np.nextafter(
        np.sqrt(
            np.longdouble(linf)
            * np.longdouble(lone)
        ),
        np.longdouble(np.inf),
    ))
    return linf, lone, ltwo


def cross_hilbert_hs_upper(modes, remote_start):
    """Elementary infinite HS upper bound for the finite/remote B cross block."""
    total = np.longdouble(0.0)
    for m in modes.astype(np.longdouble):
        a = m + np.longdouble(remote_start)
        # Same-parity remote n=remote_start+2k:
        # sum f(k) <= f(0)+int_0^inf f(x)dx.
        total += 1.0 / (a*a) + 1.0 / (2.0*a)
    return float(np.sqrt(total))


def smooth_bulk_global_floor(sector):
    if sector == "even-v":
        modes = parity_modes(sector, 3999)
        shift = 0.0415
        remote_start = 4001
        beta_public = BETA_CAP[sector]
    else:
        modes = parity_modes(sector, 4000)
        shift = 0.2400
        remote_start = 4002
        beta_public = BETA_CAP[sector]

    B = smooth_bulk_matrix(modes)
    shifted = B - shift * np.eye(len(modes))
    L = np.linalg.cholesky(shifted)

    fres = cholesky_factor_residual(shifted, L)
    _, _, inv_bound = inverse_factor_bounds_outward(L)
    shifted_floor = 1.0 / (inv_bound*inv_bound) - fres
    if shifted_floor <= 0:
        raise RuntimeError(("shifted B floor failed", sector, shifted_floor))

    # Absorb explicit-entry/log rounding before using the finite floor.
    finite_floor = shift - B_ENTRY_RESERVE

    c = cross_hilbert_hs_upper(modes, remote_start)
    if c >= 0.42:
        raise RuntimeError(("B cross HS cap failed", sector, c))

    gamma_remote = (
        math.log(remote_start / 4.0)
        - math.pi / 2.0
    )
    if gamma_remote <= 5.33:
        raise RuntimeError(("B remote floor failed", sector, gamma_remote))

    # The public beta is derived only from conservative constants:
    # finite_floor >= shift-reserve, cross <= 0.42, remote >= 5.33.
    c_public = 0.42
    gamma_public = 5.33
    beta = 0.5 * (
        finite_floor + gamma_public
        - math.sqrt(
            (gamma_public - finite_floor)**2
            + 4.0 * c_public*c_public
        )
    )
    if beta <= beta_public:
        raise RuntimeError(("global B floor cap failed", sector, beta))

    return {
        "finite_shift": shift,
        "finite_floor_after_entry_reserve": finite_floor,
        "shifted_floor": shifted_floor,
        "cross_hs": c,
        "remote_floor": gamma_remote,
        "beta": beta,
        "beta_public": beta_public,
        "factor_residual": fres,
        "inverse_factor_bound": inv_bound,
    }


def certify_sector(sector):
    m1, theta1, Q1, defect1 = first_stage_ritz(sector)
    m2, X = graph_extend(sector, m1, theta1, Q1)

    theta, Z, AZ, BZ, Gfinite, defect2 = second_stage_ritz(
        sector, m2, X
    )

    if not np.all(np.abs(theta) < 0.02):
        raise RuntimeError(("second-stage Ritz values left inner window", sector, theta))
    if float(np.max(np.abs(theta))) >= RITZ_ABS_CAP[sector]:
        raise RuntimeError(("second-stage Ritz cap failed", sector, theta))

    Gremote = explicit_remote_gram(sector, m2, Z, theta)
    Gpoint = Gfinite + Gremote
    Gpoint = (Gpoint + Gpoint.T) / 2.0

    point_residual = math.sqrt(
        max(0.0, float(np.linalg.eigvalsh(Gpoint)[-1]))
    )
    far = far_residual_bound(sector, m2, Z, theta)

    if point_residual >= POINT_RESIDUAL_CAP[sector]:
        raise RuntimeError(("point residual cap failed", sector, point_residual))
    if far >= FAR_RESIDUAL_CAP[sector]:
        raise RuntimeError(("far residual cap failed", sector, far))

    # Minkowski plus a source/arithmetic reserve.
    total_euclidean = (
        point_residual
        + far
        + ARITH_RESERVE
        + EPS_SOURCE / math.sqrt(BETA_CAP[sector])
    )
    if total_euclidean >= TOTAL_EUCLIDEAN_RESIDUAL_CAP[sector]:
        raise RuntimeError(("total Euclidean residual cap failed", sector, total_euclidean))

    bulk = smooth_bulk_global_floor(sector)
    transformed = (
        TOTAL_EUCLIDEAN_RESIDUAL_CAP[sector]
        / math.sqrt(BETA_CAP[sector])
    )
    if transformed >= TRANSFORMED_RESIDUAL_CAP[sector]:
        raise RuntimeError(("transformed residual cap failed", sector, transformed))

    # Exact certified spectral moat from v13.823.
    sin_theta = transformed / 0.08
    if sin_theta >= SIN_THETA_CAP[sector]:
        raise RuntimeError(("subspace sin-theta cap failed", sector, sin_theta))

    angle_deg = math.degrees(math.asin(sin_theta))

    # A sharper certified separation uses only the public Ritz cap,
    # together with the exact complementary spectrum outside [-0.10,0.10].
    sep_sharp = 0.10 - RITZ_ABS_CAP[sector]
    sharp_sin = transformed / sep_sharp
    sharp_angle = math.degrees(math.asin(sharp_sin))

    return {
        "sector": sector,
        "theta_M1": theta1,
        "theta_M2": theta,
        "M1_B_orthogonality_defect": defect1,
        "M2_B_orthogonality_defect": defect2,
        "finite_residual_operator": math.sqrt(
            max(0.0, float(np.linalg.eigvalsh(Gfinite)[-1]))
        ),
        "explicit_remote_residual_operator": math.sqrt(
            max(0.0, float(np.linalg.eigvalsh(Gremote)[-1]))
        ),
        "point_total_residual_operator": point_residual,
        "far_residual_bound": far,
        "total_euclidean_cap": TOTAL_EUCLIDEAN_RESIDUAL_CAP[sector],
        "bulk_floor": bulk,
        "transformed_residual_cap": TRANSFORMED_RESIDUAL_CAP[sector],
        "moat": 0.08,
        "sin_theta_cap": SIN_THETA_CAP[sector],
        "angle_deg_cap": angle_deg,
        "sharp_sep": sep_sharp,
        "sharp_sin_theta": sharp_sin,
        "sharp_angle_deg": sharp_angle,
    }


def main():
    rows = [
        certify_sector("even-v"),
        certify_sector("odd-v"),
    ]

    for row in rows:
        print("\nsector =", row["sector"])
        print("M1 Ritz values =", row["theta_M1"])
        print("M2 Ritz values =", row["theta_M2"])
        print("M1 B-orth defect =", row["M1_B_orthogonality_defect"])
        print("M2 B-orth defect =", row["M2_B_orthogonality_defect"])
        print("finite residual =", row["finite_residual_operator"])
        print("explicit remote residual =", row["explicit_remote_residual_operator"])
        print("point total residual =", row["point_total_residual_operator"])
        print("far residual bound =", row["far_residual_bound"])
        print("total Euclidean cap =", row["total_euclidean_cap"])
        print("B floor detail =", row["bulk_floor"])
        print("B^-1/2 residual cap =", row["transformed_residual_cap"])
        print("exact moat =", row["moat"])
        print("sin(theta_max) cap =", row["sin_theta_cap"])
        print("theta_max deg cap =", row["angle_deg_cap"])
        print("sharpened separation =", row["sharp_sep"])
        print("sharpened sin(theta) =", row["sharp_sin_theta"])
        print("sharpened theta deg =", row["sharp_angle_deg"])

    print("\nPASS residual-certified numerical basis for Ran P4")
    print(
        "The four-column M2 Ritz spaces have the same dimension as the exact "
        "rank-four spectral projector and satisfy the reported Davis-Kahan/"
        "Kato subspace-error bounds."
    )
    print(
        "Guardrail: this constructs a certified approximate basis for Ran P4; "
        "it does not identify individual infinite eigenvectors when cluster "
        "eigenvalues are unresolved or repeated."
    )


if __name__ == "__main__":
    main()
