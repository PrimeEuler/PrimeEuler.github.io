#!/usr/bin/env python3
"""Terminal certificate for the rho=0.10 PLUS tail endpoint.

This certifies positivity of the entire ten-dimensional M=3999/4000 effective
core in both parity sectors after the infinite remote tail is eliminated.

Unlike the minus endpoint, no eigenspace is frozen: the core basis is the
standard coordinate basis I_10.  Only the midpoint Cholesky preconditioner L0
is frozen as an exact binary64 dyadic payload and hash-checked.

The verifier is deliberately fail-closed:
  * fresh endpoint reconstruction with sign=+1;
  * structured LDL residual and inverse-factor conditioning checks;
  * corrected odd negative-pole Sherman-Morrison check;
  * ten-RHS residual and frozen-reference checks;
  * fixed exact-vs-nominal endpoint budget eps_F=2.1e-13;
  * outward interval tail-floor calculation at n=4001/4002;
  * direct+inverse-power remote Gram replay through 2,000,000;
  * analytic |Z_endpoint|<8 far-generator proof including rho*pi/2 shift;
  * wide residual-operator perturbation cap EPS_Y=1e-6.

No basis regeneration occurs.
"""
from __future__ import annotations

from decimal import Decimal, getcontext
import math

import mpmath as mp
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    RHO,
    endpoint_data,
    offdiag,
    pole_vector,
    structured_ldl,
    ldl_solve,
    z_source_faithful,
)
from suzuki_endpoint_M3999_plus_frozen_L0 import (
    EVEN_L0_HEX,
    ODD_L0_HEX,
    EVEN_SHA256,
    ODD_SHA256,
    payload_hash,
    floats,
)


getcontext().prec = 60

PI = math.pi
U64 = 2.0**-53
ULD = float(np.finfo(np.longdouble).eps / 2)
EPS_F = 2.1e-13
KEXP = 8
EXPLICIT_STOP = 2_000_000
Z_FAR_BOUND = 8.0

KQ_CAP = {"even-v": 1.10, "odd-v": 0.82}
SOLVE_RESIDUAL_CAP = {"even-v": 1.70e-15, "odd-v": 1.30e-15}
REFERENCE_DEFECT_CAP = {"even-v": 8.0e-16, "odd-v": 6.0e-16}
L0_INV_CAP = {"even-v": 10.0, "odd-v": 6.0}
WNORM_CAP = {"even-v": 10.0, "odd-v": 6.0}

C_LOWER = {
    "even-v": Decimal("0.9999999279"),
    "odd-v": Decimal("0.9999999760"),
}
GAMMA_LOWER = {
    "even-v": Decimal("3.82049621074657"),
    "odd-v": Decimal("3.82066116500621"),
}
H_EXPLICIT_CAP = {
    "even-v": Decimal("0.036395"),
    "odd-v": Decimal("0.019089"),
}
H_FAR_CAP = {
    "even-v": Decimal("0.00009"),
    "odd-v": Decimal("0.00005"),
}
Y_POINT_NORM_CAP = {
    "even-v": Decimal("0.192"),
    "odd-v": Decimal("0.139"),
}
EPS_Y = Decimal("1e-6")
REMOTE_CROSS_CAP = Decimal("20")
REPLAY_ARITH_CAP = Decimal("1e-8")


def gamma_n(n: int, u: float) -> float:
    nu = n * u
    if nu >= 1:
        raise RuntimeError("gamma_n invalid")
    return nu / (1.0 - nu)


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


def reference_defect_outward(C, R, Y, L0):
    C = np.asarray(C, dtype=np.longdouble)
    R = np.asarray(R, dtype=np.longdouble)
    Y = np.asarray(Y, dtype=np.longdouble)
    L0 = np.asarray(L0, dtype=np.longdouble)

    BQ = R.T
    tail = BQ.T @ Y
    Bhat = C - tail
    Bref = L0 @ L0.T
    D = Bhat - Bref
    dp = np.sqrt(np.sum(D * D, dtype=np.longdouble))

    EBQ = np.longdouble(gamma_n(10, ULD)) * np.abs(R).T
    Etail = (
        np.longdouble(gamma_n(Y.shape[0], ULD))
        * (np.abs(BQ).T @ np.abs(Y))
        + EBQ.T @ np.abs(Y)
    )
    Eref = np.longdouble(gamma_n(10, ULD)) * (
        np.abs(L0) @ np.abs(L0).T
    )
    Esub = (
        np.longdouble(ULD) / (1 - np.longdouble(ULD))
        * (np.abs(C) + np.abs(tail) + np.abs(Bref))
    )
    E = Etail + Eref + Esub
    ee = np.sqrt(np.sum(E * E, dtype=np.longdouble))
    return float(np.nextafter(dp + ee, np.longdouble(np.inf)))


def schur_source_perturbation(eps, K, mu):
    return (
        eps
        + 2 * K * eps / (mu - eps)
        + eps * eps / (mu - eps)
        + K * K * eps / (mu * (mu - eps))
    )


def sector_layout(sector):
    if sector == "even-v":
        return (
            np.arange(5, 24, 2, dtype=int),
            np.arange(25, 4000, 2, dtype=int),
            EVEN_L0_HEX,
            EVEN_SHA256,
        )
    if sector == "odd-v":
        return (
            np.arange(6, 25, 2, dtype=int),
            np.arange(26, 4001, 2, dtype=int),
            ODD_L0_HEX,
            ODD_SHA256,
        )
    raise ValueError(sector)


def finite_payload(sector):
    core, buffer_, lhex, expected_hash = sector_layout(sector)
    if payload_hash(lhex) != expected_hash:
        raise RuntimeError("plus-endpoint L0 hash mismatch")

    L0 = floats(lhex)
    if not all(L0[i, i] > 0 for i in range(10)):
        raise RuntimeError("plus-endpoint L0 diagonal failed")

    modes = np.concatenate([core, buffer_])
    z, diag = endpoint_data(modes, sign=+1)
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
        raise RuntimeError("plus pole-free buffer floor failed")

    if sector == "even-v":
        mu_nom = mu0
        pole_den_lower = 1.0
    else:
        yp0 = ldl_solve(L, D, pf)
        rp = rhs_residual_outward(A0, pf[:, None], yp0[:, None])
        inv0 = 1.0 / mu0
        yerr = inv0 * rp
        pnorm = np.linalg.norm(pf)
        yhat = np.linalg.norm(yp0)

        qhat = (
            np.longdouble(pf.astype(np.longdouble))
            @ np.longdouble(yp0.astype(np.longdouble))
        )
        qround = gamma_n(len(pf), ULD) * float(
            np.sum(
                np.abs(
                    pf.astype(np.longdouble)
                    * yp0.astype(np.longdouble)
                ),
                dtype=np.longdouble,
            )
        )
        qupper = float(qhat) + qround + pnorm * yerr
        pole_den_lower = 1.0 - 2.0 * qupper
        if pole_den_lower <= 0:
            raise RuntimeError("plus odd pole denominator failed")

        invfull = inv0 + 2.0 * (yhat + yerr)**2 / pole_den_lower
        mu_nom = 1.0 / invfull

    mu_exact = mu_nom - EPS_F
    if mu_exact <= 0:
        raise RuntimeError("plus exact buffer floor failed")

    BQ = R.T
    X0 = ldl_solve(L, D, BQ)
    yp = ldl_solve(L, D, pf)
    q = float(pf @ yp)
    den = 1.0 + alpha * q
    Y = X0 - alpha * np.outer(yp, pf @ X0) / den

    Afull = A0 + alpha * np.outer(pf, pf)
    solve_resid = rhs_residual_outward(Afull, BQ, Y)

    Kactual = float(
        np.sqrt(
            np.sum(
                BQ.astype(np.longdouble)**2,
                dtype=np.longdouble,
            )
        )
    )
    if Kactual >= KQ_CAP[sector]:
        raise RuntimeError(("plus coupling cap failed", Kactual))
    if solve_resid >= SOLVE_RESIDUAL_CAP[sector]:
        raise RuntimeError(("plus solve residual cap failed", solve_resid))

    ref_defect = reference_defect_outward(C, R, Y, L0)
    if ref_defect >= REFERENCE_DEFECT_CAP[sector]:
        raise RuntimeError(("plus reference defect cap failed", ref_defect))

    invL0 = float(np.linalg.norm(np.linalg.inv(L0), 2))
    if invL0 >= L0_INV_CAP[sector]:
        raise RuntimeError(("plus L0 inverse cap failed", invL0))

    eps_source = schur_source_perturbation(
        EPS_F,
        KQ_CAP[sector],
        mu_nom,
    )
    eps_solve = (
        KQ_CAP[sector]
        / mu_nom
        * SOLVE_RESIDUAL_CAP[sector]
    )
    eps_total = (
        REFERENCE_DEFECT_CAP[sector]
        + eps_source
        + eps_solve
    )

    c_lower_computed = 1.0 - L0_INV_CAP[sector]**2 * eps_total
    if Decimal(str(c_lower_computed)) <= C_LOWER[sector]:
        raise RuntimeError(("plus finite C lower failed", c_lower_computed))

    W = np.vstack([np.eye(10), -Y])
    T = np.linalg.inv(L0.T)
    Wnorm = float(np.linalg.norm(W @ T, 2))
    if Wnorm >= WNORM_CAP[sector]:
        raise RuntimeError(("plus normalized W cap failed", Wnorm))

    pW = p @ W

    return {
        "sector": sector,
        "modes": modes.astype(float),
        "z": z.astype(float),
        "p": p.astype(float),
        "alpha": alpha,
        "W": W,
        "pW": pW,
        "L0": L0,
        "mu_nom": mu_nom,
        "mu_exact": mu_exact,
        "pole_den_lower": pole_den_lower,
        "factor_residual": factor_resid,
        "linv": (linf, lone, l2),
        "Kactual": Kactual,
        "solve_residual": solve_resid,
        "reference_defect": ref_defect,
        "invL0": invL0,
        "Wnorm": Wnorm,
        "eps_source": eps_source,
        "eps_solve": eps_solve,
        "eps_total": eps_total,
        "C_lower_computed": c_lower_computed,
    }


def tail_z_plus(ns):
    return z_source_faithful(ns) + RHO * PI / 2.0


def direct_rows(payload, ns):
    ns = np.asarray(ns, dtype=float)
    zn = tail_z_plus(ns)
    modes = payload["modes"]
    z = payload["z"]
    W = payload["W"]

    den = ns[:, None]**2 - modes[None, :]**2
    A0 = (
        (2.0 / PI)
        * (
            zn[:, None] * modes[None, :]
            - ns[:, None] * z[None, :]
        )
        / den
    )

    pn, _ = pole_vector(ns, payload["sector"])
    return (
        A0 @ W
        + payload["alpha"]
        * pn[:, None]
        * payload["pW"][None, :]
    )


def inverse_power_moments(payload):
    j = payload["modes"].astype(np.longdouble)
    W = payload["W"].astype(np.longdouble)
    z = payload["z"].astype(np.longdouble)

    aa = []
    bb = []
    for k in range(KEXP):
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


def expanded_rows(payload, ns, aa, bb):
    nn = np.asarray(ns, dtype=np.longdouble)
    zn = tail_z_plus(np.asarray(ns, dtype=float)).astype(np.longdouble)
    R = np.zeros((len(nn), 10), dtype=np.longdouble)
    pild = np.longdouble(PI)

    for k in range(KEXP):
        R += (
            np.longdouble(2) / pild
        ) * (
            zn[:, None]
            * aa[k][None, :]
            / nn[:, None]**(2*k + 2)
            - bb[k][None, :]
            / nn[:, None]**(2*k + 1)
        )

    pn, _ = pole_vector(
        np.asarray(ns, dtype=float),
        payload["sector"],
    )
    R += (
        np.longdouble(payload["alpha"])
        * pn.astype(np.longdouble)[:, None]
        * payload["pW"].astype(np.longdouble)[None, :]
    )
    return np.asarray(R, dtype=float)


def normalized_gram(payload):
    sector = payload["sector"]
    start = 4001 if sector == "even-v" else 4002
    direct_stop = 16001 if sector == "even-v" else 16000

    G = np.zeros((10, 10), dtype=float)

    for st in range(start, direct_stop + 1, 2000):
        en = min(st + 1998, direct_stop)
        ns = np.arange(st, en + 1, 2, dtype=float)
        R = direct_rows(payload, ns)
        G += R.T @ R

    aa, bb = inverse_power_moments(payload)
    st = direct_stop + 2
    while st <= EXPLICIT_STOP:
        en = min(st + 199998, EXPLICIT_STOP)
        if (en - st) % 2:
            en -= 1
        ns = np.arange(st, en + 1, 2, dtype=float)
        R = expanded_rows(payload, ns, aa, bb)
        G += R.T @ R
        st = en + 2

    L0 = payload["L0"]
    H = np.linalg.solve(L0, G) @ np.linalg.inv(L0.T)
    H = (H + H.T) / 2
    return H


def prove_z_far_bound():
    iv = mp.iv
    iv.dps = 80

    qs = [iv.mpf(2), iv.mpf(3), iv.mpf(4), iv.mpf(5), iv.mpf(7)]
    lambdas = [
        iv.log(2),
        iv.log(3),
        iv.log(2),
        iv.log(5),
        iv.log(7),
    ]
    wsum = sum(l / iv.sqrt(q) for l, q in zip(lambdas, qs))

    n = iv.mpf(2_000_001)
    y = n * iv.pi / 4
    psi_upper = iv.pi / 2 + 1 / y
    corr_upper = (
        4 / (n * iv.pi)
        * iv.exp(-1)
        / (1 - iv.exp(-4))
    )

    z_endpoint_upper = (
        2 * wsum
        + psi_upper
        + corr_upper
        + iv.mpf("0.10") * iv.pi / 2
    )
    assert z_endpoint_upper < iv.mpf(8)
    return z_endpoint_upper


def far_envelope(payload):
    T = np.linalg.inv(payload["L0"].T)
    W = payload["W"] @ T
    pW = payload["p"] @ W
    modes = payload["modes"]
    z = payload["z"]
    alpha = payload["alpha"]

    if payload["sector"] == "even-v":
        N = 2_000_001.0
        g = math.cosh(0.5)
    else:
        N = 2_000_002.0
        g = math.sinh(0.5)

    rho = np.max(modes) / N

    leading = (
        -(2.0 / PI) * (z @ W)
        + alpha * (4.0 * g / PI) * pW
    )

    B = (
        (2.0 / PI)
        * Z_FAR_BOUND
        / (1 - rho * rho)
        * np.sum(np.abs(modes[:, None] * W), axis=0)
    )

    C = (
        (2.0 / PI)
        / (1 - rho * rho)
        * np.sum(
            np.abs(
                (modes * modes * z)[:, None] * W
            ),
            axis=0,
        )
        + abs(alpha)
        * (4.0 * g / PI**3)
        * np.abs(pW)
    )

    def S(power):
        return (
            N**(-power)
            + 1.0 / (2.0 * (power - 1) * N**(power - 1))
        )

    root = (
        np.linalg.norm(leading) * math.sqrt(S(2))
        + np.linalg.norm(B) * math.sqrt(S(4))
        + np.linalg.norm(C) * math.sqrt(S(6))
    )
    return root * root


def zeta3_interval(M=20000):
    iv = mp.iv
    s = iv.mpf(0)
    for k in range(1, M + 1):
        x = iv.mpf(k)
        s += 1 / x**3
    lo = 1 / (2 * iv.mpf(M + 1)**2)
    hi = 1 / (2 * iv.mpf(M)**2)
    return iv.mpf([s.a + lo.a, s.b + hi.b])


def endpoint_tail_floor_plus(sector):
    iv = mp.iv
    iv.dps = 80
    N = 4001 if sector == "even-v" else 4002
    n = iv.mpf(N)
    pi = iv.pi

    s2 = n**-2 + 1 / (2 * n)
    c = 2 / pi**3 + 6 / pi**4
    alpha = 2 * c / pi
    cdiag = (
        2 / pi**2
        + 2 / pi**3
        + 2 / pi**4
        + 6 / pi**5
    )

    cusp = (
        2 / pi**2 * s2
        + 2 * alpha
        * iv.sqrt(
            pi**2 / 12
            * (n**-6 + 1 / (10 * n**5))
        )
        + cdiag
        * iv.sqrt(n**-4 + 1 / (6 * n**3))
    )

    q = 2 / pi
    zeta3 = zeta3_interval()
    m4 = zeta3 * q**3 / (4 * (1 - q)**3)
    cr = iv.mpf(19) / 12 + 4 * m4
    arch = 4 * cr / pi**2 * s2

    out = (
        iv.mpf("1.10")
        * (iv.log(n / 4) - pi / 2)
        - iv.mpf("2.05")
        - cusp
        - arch
    )

    if sector == "odd-v":
        sh = (iv.exp(iv.mpf("0.5")) - iv.exp(-iv.mpf("0.5"))) / 2
        out -= 32 * sh**2 / pi**2 * s2

    return out


def eps_y_derived(payload):
    sector = payload["sector"]
    mu = Decimal(str(payload["mu_nom"]))
    k = Decimal(str(KQ_CAP[sector]))
    r = Decimal(str(SOLVE_RESIDUAL_CAP[sector]))
    t = Decimal(str(L0_INV_CAP[sector]))
    eps = Decimal(str(EPS_F))

    dx = (
        eps / (mu - eps)
        + eps * k / (mu * (mu - eps))
        + r / mu
    ) * t

    total = (
        REMOTE_CROSS_CAP * dx
        + eps * Decimal(str(WNORM_CAP[sector]))
        + REPLAY_ARITH_CAP
    )
    return dx, total


def terminal_one(sector):
    payload = finite_payload(sector)

    H = normalized_gram(payload)
    lam = float(np.linalg.eigvalsh(H)[-1])
    far = float(far_envelope(payload))

    if Decimal(str(lam)) >= H_EXPLICIT_CAP[sector]:
        raise RuntimeError(("plus explicit H cap failed", lam))
    if Decimal(str(far)) >= H_FAR_CAP[sector]:
        raise RuntimeError(("plus far H cap failed", far))

    gamma_iv = endpoint_tail_floor_plus(sector)
    if not gamma_iv > mp.iv.mpf(str(GAMMA_LOWER[sector])):
        raise RuntimeError(("plus gamma floor failed", gamma_iv))

    dx, epsy = eps_y_derived(payload)
    if epsy >= EPS_Y:
        raise RuntimeError(("plus EPS_Y failed", epsy))

    h_point = H_EXPLICIT_CAP[sector] + H_FAR_CAP[sector]
    h_perturb = (
        2 * Y_POINT_NORM_CAP[sector] * EPS_Y
        + EPS_Y * EPS_Y
    )
    h_upper = h_point + h_perturb

    terminal_lower = GAMMA_LOWER[sector] * C_LOWER[sector]
    margin = terminal_lower - h_upper
    normalized_lower = (
        C_LOWER[sector]
        - h_upper / GAMMA_LOWER[sector]
    )

    if margin <= Decimal("3.7"):
        raise RuntimeError(("plus terminal margin failed", margin))
    if normalized_lower <= Decimal("0.99"):
        raise RuntimeError(("plus normalized margin failed", normalized_lower))

    return {
        "sector": sector,
        "payload": payload,
        "point_lambda": lam,
        "far_envelope": far,
        "gamma_interval": gamma_iv,
        "dx": dx,
        "derived_eps_y": epsy,
        "h_upper": h_upper,
        "terminal_lower": terminal_lower,
        "margin": margin,
        "normalized_lower": normalized_lower,
    }


def main():
    zbound = prove_z_far_bound()
    print("plus endpoint far generator bound =", zbound)

    rows = [terminal_one("even-v"), terminal_one("odd-v")]
    for row in rows:
        p = row["payload"]
        print("\nsector =", row["sector"])
        for key in (
            "mu_nom",
            "mu_exact",
            "pole_den_lower",
            "factor_residual",
            "Kactual",
            "solve_residual",
            "reference_defect",
            "invL0",
            "Wnorm",
            "eps_source",
            "eps_solve",
            "eps_total",
            "C_lower_computed",
        ):
            print(key, "=", p[key])
        for key in (
            "point_lambda",
            "far_envelope",
            "gamma_interval",
            "dx",
            "derived_eps_y",
            "h_upper",
            "terminal_lower",
            "margin",
            "normalized_lower",
        ):
            print(key, "=", row[key])

    even, odd = rows

    assert even["margin"] > Decimal("3.7840")
    assert odd["margin"] > Decimal("3.8015")

    print("\nPASS: rho=0.10 plus tail endpoint is strictly positive")
    print("even normalized lower >", even["normalized_lower"])
    print("odd normalized lower  >", odd["normalized_lower"])


if __name__ == "__main__":
    main()
