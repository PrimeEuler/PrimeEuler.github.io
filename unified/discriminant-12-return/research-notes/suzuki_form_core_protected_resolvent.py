#!/usr/bin/env python3
"""Protected-subspace/Feshbach evaluation of Suzuki form-core source resolvents.

Lane A continuation after ledger v13.797.  This script deliberately reuses the
source-faithful Dirichlet form matrix from
suzuki_componentwise_high_precision_audit.py and the analytic source overlap
from suzuki_form_core_schur_parameter_diagnostic.py.

For each parity block B of A_a at a=1, lambda=0 it evaluates

    E = f^T B^{-1} f

in two independent finite-dimensional ways:

  1. high-precision spectral resolution of the full parity block;
  2. a protected-subspace Feshbach reduction.  The protected basis is frozen
     from a smaller anchor cutoff and embedded into the larger target block.

No endpoint condition is imposed on a deficiency vector, no raw Fredholm
operator is inverted, and no S_a/ordinary-derivative identification is used.
The lambda=0 outputs are finite-a diagnostics for the xi-target branch only;
they do not prove positivity of A_a, RH, or finite-to-infinite convergence.
"""
from __future__ import annotations

import hashlib
import mpmath as mp

from suzuki_componentwise_high_precision_audit import (
    component_matrices_mp,
    parity_indices_v,
)
from suzuki_form_core_schur_parameter_diagnostic import source_overlap


def _submatrix(A: mp.matrix, idx: list[int]) -> mp.matrix:
    return mp.matrix([[A[i, j] for j in idx] for i in idx])


def _subvector(v: mp.matrix, idx: list[int]) -> mp.matrix:
    return mp.matrix([v[i] for i in idx])


def _solve_columns(A: mp.matrix, B: mp.matrix) -> mp.matrix:
    X = mp.matrix(A.rows, B.cols)
    for j in range(B.cols):
        rhs = mp.matrix([B[i, j] for i in range(B.rows)])
        x = mp.lu_solve(A, rhs)
        for i in range(A.rows):
            X[i, j] = x[i]
    return X


def _frob(A: mp.matrix) -> mp.mpf:
    return mp.sqrt(sum(abs(A[i, j]) ** 2 for i in range(A.rows) for j in range(A.cols)))


def _orthogonal_complement(P: mp.matrix, tol: mp.mpf | None = None) -> mp.matrix:
    """Complete orthonormal columns P to an orthonormal basis by Gram-Schmidt."""
    n, r = P.rows, P.cols
    if tol is None:
        tol = mp.sqrt(mp.eps)
    protected = [P[:, j] for j in range(r)]
    complement: list[mp.matrix] = []
    for i in range(n):
        v = mp.matrix(n, 1)
        v[i] = 1
        for q in protected + complement:
            v -= q * (q.T * v)[0]
        nv = mp.sqrt((v.T * v)[0])
        if nv > tol:
            complement.append(v / nv)
        if len(complement) == n - r:
            break
    if len(complement) != n - r:
        raise RuntimeError("failed to construct orthogonal complement")
    Q = mp.matrix(n, n - r)
    for j, q in enumerate(complement):
        for i in range(n):
            Q[i, j] = q[i]
    return Q


def canonical_hash_matrix(A: mp.matrix, digits: int = 60) -> str:
    payload = "\n".join(
        mp.nstr(A[i, j], digits, strip_zeros=False)
        for i in range(A.rows)
        for j in range(A.cols)
    ) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


def canonical_hash_vector(v: mp.matrix, digits: int = 60) -> str:
    payload = "\n".join(
        mp.nstr(v[i], digits, strip_zeros=False) for i in range(v.rows)
    ) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


def spectral_quadratic_form(B: mp.matrix, f: mp.matrix) -> dict:
    vals, Q = mp.eigsy(B)
    y = Q.T * f
    terms = [y[j] ** 2 / vals[j] for j in range(len(vals))]
    coeff = mp.matrix([y[j] / vals[j] for j in range(len(vals))])
    c = Q * coeff
    residual = B * c - f
    residual_inf = max(abs(residual[j]) for j in range(residual.rows))
    E = sum(terms)
    return {
        "eigenvalues": vals,
        "eigenvectors": Q,
        "source_coordinates": y,
        "terms": terms,
        "energy": E,
        "residual_inf": residual_inf,
        "lowest_fraction": terms[0] / E,
        "condition_number": abs(vals[-1] / vals[0]),
    }


def feshbach_quadratic_form(B: mp.matrix, f: mp.matrix, P: mp.matrix) -> dict:
    """Exact finite-dimensional protected/Feshbach reduction.

    With Q spanning the orthogonal complement,

        S = P^T B P - P^T B Q (Q^T B Q)^-1 Q^T B P,
        g = P^T f - P^T B Q (Q^T B Q)^-1 Q^T f,

    one has

        f^T B^-1 f = f_Q^T (Q^T B Q)^-1 f_Q + g^T S^-1 g.
    """
    Q = _orthogonal_complement(P)
    App = P.T * B * P
    Apc = P.T * B * Q
    Acc = Q.T * B * Q
    fp = P.T * f
    fc = Q.T * f

    zc = mp.lu_solve(Acc, fc)
    Y = _solve_columns(Acc, Apc.T)
    S = App - Apc * Y
    g = fp - Apc * zc
    zp = mp.lu_solve(S, g)
    E = (fc.T * zc)[0] + (g.T * zp)[0]

    vals_c, _ = mp.eigsy(Acc)
    vals_s, _ = mp.eigsy(S)
    return {
        "energy": E,
        "complement_gap": vals_c[0],
        "protected_eigenvalues": vals_s,
        "cross_frobenius": _frob(Apc),
    }


def build_payload(max_modes: int = 16, a: int | float = 1, dps: int = 70):
    with mp.workdps(dps):
        P, R, H = component_matrices_mp(max_modes, a=a, dps=dps)
        A = P + R + H
        aa = mp.mpf(str(a))
        f = mp.matrix([source_overlap(n, aa, mp.mpf(1)) for n in range(1, max_modes + 1)])
        return A, f


def cutoff_report(A: mp.matrix, f: mp.matrix, cutoffs=(4, 6, 8, 10, 12, 14, 16)):
    rows = []
    for N in cutoffs:
        energies = {}
        parity_rows = {}
        for parity in ("even", "odd"):
            idx = parity_indices_v(N, parity)
            B = _submatrix(A, idx)
            fp = _subvector(f, idx)
            r = spectral_quadratic_form(B, fp)
            energies[parity] = r["energy"]
            parity_rows[parity] = r
        Ee, Eo = energies["even"], energies["odd"]
        rows.append({
            "N": N,
            "even": parity_rows["even"],
            "odd": parity_rows["odd"],
            "kappa0": (Ee - Eo) / (Ee + Eo),
        })
    return rows


def protected_report(
    A: mp.matrix,
    f: mp.matrix,
    anchor_modes: int = 12,
    target_modes: int = 16,
    protected_dim: int = 4,
):
    out = {}
    anchor_block_dim = len(parity_indices_v(anchor_modes, "even"))
    target_block_dim = len(parity_indices_v(target_modes, "even"))
    if protected_dim >= anchor_block_dim:
        raise ValueError("protected_dim must leave an anchor complement")

    for parity in ("even", "odd"):
        ia = parity_indices_v(anchor_modes, parity)
        it = parity_indices_v(target_modes, parity)
        Ba = _submatrix(A, ia)
        Bt = _submatrix(A, it)
        ft = _subvector(f, it)
        _, Qa = mp.eigsy(Ba)

        P = mp.matrix(target_block_dim, protected_dim)
        for i in range(anchor_block_dim):
            for j in range(protected_dim):
                P[i, j] = Qa[i, j]

        spec = spectral_quadratic_form(Bt, ft)
        fesh = feshbach_quadratic_form(Bt, ft, P)
        fesh["relative_energy_difference"] = (
            fesh["energy"] - spec["energy"]
        ) / spec["energy"]
        out[parity] = {"spectral": spec, "feshbach": fesh}
    return out


def print_report(max_modes: int = 16, dps: int = 70) -> None:
    with mp.workdps(dps):
        A, f = build_payload(max_modes=max_modes, a=1, dps=dps)
        print("Lane A protected form-core source-resolvent diagnostic")
        print("a=1 lambda=0 max_modes=", max_modes, "dps=", dps)
        print("A payload sha256 (60 digits) =", canonical_hash_matrix(A))
        print("f payload sha256 (60 digits) =", canonical_hash_vector(f))
        for parity in ("even", "odd"):
            idx = parity_indices_v(max_modes, parity)
            print(parity, "block sha256 =", canonical_hash_matrix(_submatrix(A, idx)))
            print(parity, "source sha256 =", canonical_hash_vector(_subvector(f, idx)))

        print("cutoff diagnostics")
        for row in cutoff_report(A, f):
            e = row["even"]
            o = row["odd"]
            print(
                "N=", row["N"],
                "kappa0=", mp.nstr(row["kappa0"], 20),
                "lam_e=", mp.nstr(e["eigenvalues"][0], 10),
                "lam_o=", mp.nstr(o["eigenvalues"][0], 10),
                "cond_e=", mp.nstr(e["condition_number"], 8),
                "cond_o=", mp.nstr(o["condition_number"], 8),
                "frac1_e=", mp.nstr(e["lowest_fraction"], 12),
                "frac1_o=", mp.nstr(o["lowest_fraction"], 12),
                "res=", mp.nstr(max(e["residual_inf"], o["residual_inf"]), 6),
            )

        print("protected dimension scan: anchor N=12 -> target N=16")
        for r in range(1, 6):
            p = protected_report(A, f, anchor_modes=12, target_modes=16, protected_dim=r)
            print("r=", r)
            for parity in ("even", "odd"):
                fz = p[parity]["feshbach"]
                print(
                    " ", parity,
                    "comp_gap=", mp.nstr(fz["complement_gap"], 12),
                    "S_min=", mp.nstr(fz["protected_eigenvalues"][0], 12),
                    "cross_F=", mp.nstr(fz["cross_frobenius"], 10),
                    "rel_E_diff=", mp.nstr(fz["relative_energy_difference"], 8),
                )


if __name__ == "__main__":
    print_report()
