#!/usr/bin/env python3
"""Direct normalized seven-column producer with optional exact-point caps.

Freezes one corrected-anchor T,v, forms all seven normalized protected/source
RHSs before solving, refines their joint residuals in LDDD, and emits small
affine reductions. The optional exact kernel separately certifies all-source
assembly and projected residual caps from full represented-vector snapshots.
Represented-vector trace bounds have exact dyadic witnesses; their correction
cap transport, full-Q coercivity and overall certification remain explicit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time
import platform
import scipy

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg, LinearOperator

from suzuki_ldd_source_operator import (
    LD, add, sub, mul, dot_columns, matvec, norm2,
    hp_parity_data_ld, split_mpf_ld, column,
)
from suzuki_ldd_refined_capacity_bracket import (
    dd_project, dd_matrix_to_mp, mp_inverse_split, dd_small_matmul,
)

HERE = Path(__file__).resolve().parent
DPS = 180
SCHEMA = "cone.normalized-joint-reduction.midpoint.v1"
ANCHOR_HASHES = {
    "even-v": "b46e9862d804ad3ddc75edc8ec844ed7cc24b3b4e5d73989fdb7698e5a4e6032",
    "odd-v": "682a69f6668211b5f8a03686c7a6b6e56ee0609fefed29db12fd02b69145ec41",
}
MISSING = [
    "outward_source_operator_and_projector_arithmetic",
    "protected_trace_certificate_or_certified_defect_correction",
    "coercivity_certificate_for_exact_full_frozen_six_plane_complement",
    "outward_affine_assembly_error",
    "outward_normalized_joint_residual_norms_or_gram",
]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def split_matrix(a):
    h = np.empty((a.rows, a.cols), dtype=LD)
    l = np.empty_like(h)
    for i in range(a.rows):
        for j in range(a.cols):
            h[i, j], l[i, j] = split_mpf_ld(a[i, j])
    return h, l


def right_multiply(xh, xl, ch, cl):
    """Apply a small matrix BEFORE any Gram/solve collapse, retaining hi/lo."""
    if xh.ndim != 2 or ch.ndim != 2 or xh.shape[1] != ch.shape[0]:
        raise ValueError("right multiply shape mismatch")
    h = np.zeros((xh.shape[0], ch.shape[1]), dtype=LD)
    l = np.zeros_like(h)
    for j in range(xh.shape[1]):
        ph, pl = mul(xh[:, j:j+1], xl[:, j:j+1], ch[j:j+1], cl[j:j+1])
        h, l = add(h, l, ph, pl)
    return h, l


def source_action(data, xh, xl):
    """Same columnwise source action, skipping exactly zero input rows."""
    active = np.flatnonzero(np.any((xh != 0) | (xl != 0), axis=1))
    if len(active) == len(xh):
        return matvec(data, xh, xl)
    yh = np.zeros_like(xh); yl = np.zeros_like(xl)
    for j in active:
        ah, al = column(data, int(j))
        ph, pl = mul(ah[:, None], al[:, None], xh[j:j+1], xl[j:j+1])
        yh, yl = add(yh, yl, ph, pl)
    return yh, yl


def frozen_normalizer(sector, anchor_root, offset_scale):
    raw = (anchor_root / f"M64000_paired_schur_anchor_{sector}.json").read_bytes()
    if digest(raw) != ANCHOR_HASHES[sector]:
        raise RuntimeError("corrected anchor byte hash mismatch")
    a = json.loads(raw)
    if a["sector"] != sector:
        raise RuntimeError("anchor sector mismatch")
    with mp.workdps(DPS):
        s = mp.matrix([[mp.mpf(x) for x in row] for row in a["S"]])
        b = mp.matrix(a["b"])
        exported = mp.matrix(a["Sinv_b"])
        rec = mp.mpf(a["h"]) + (b.T * mp.lu_solve(s, b))[0]
        ev, _ = mp.eigsy(s)
        if abs(rec-mp.mpf(a["K_total"])) > mp.mpf("1e-60"):
            raise RuntimeError("anchor K self-check failed")
        if abs(ev[0]-mp.mpf(a["protected_S_min"])) > mp.mpf("1e-45"):
            raise RuntimeError("anchor floor self-check failed")
        factor = mp.cholesky(s)
        t = factor.T ** -1
        v = mp.mpf(offset_scale) * factor.T * exported
        obj = {
            "T": [[mp.nstr(t[i, j], 100) for j in range(6)] for i in range(6)],
            "v": [mp.nstr(v[i], 100) for i in range(6)],
            "anchor_sha256": digest(raw), "sector": sector,
            "offset_scale": str(offset_scale),
            "interpretation": "fixed decimal coordinate constants; not exact source Cholesky",
        }
    canonical = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    obj["normalizer_sha256"] = digest(canonical)
    return obj


def affine_assembly(vh, vl, avh, avl, gh, gl):
    ah, al = dot_columns(vh, vl, avh, avl)
    bh, bl = dot_columns(vh, vl, gh[:, None], gl[:, None])
    with mp.workdps(DPS):
        a = dd_matrix_to_mp(ah, al)
        b = dd_matrix_to_mp(bh, bl)
        for i in range(7):
            a[i, 6] -= b[i]
            a[6, i] -= b[i]
        return (a + a.T) / 2


def evaluate(p, gih, gil, apply_source, protected, zh, zl, gh, gl):
    vh, vl = add(protected[0], protected[1], zh, zl)
    avh, avl = apply_source(vh, vl)
    rh, rl = avh.copy(), avl.copy()
    rh[:, 6], rl[:, 6] = sub(rh[:, 6], rl[:, 6], gh, gl)
    rh, rl = dd_project(p, gih, gil, rh, rl)
    return vh, vl, avh, avl, rh, rl


def solve_joint(p, op, proj, apply_source, gh, gl, t, v, refinements, progress,
                exact_normalizer=None, trace_witness_path=None,
                exact_backend=None, outward_context=None):
    """All seven solves receive direct normalized affine RHSs."""
    th, tl = split_matrix(t)
    vhi, vlo = split_matrix(v)
    uh, ul = right_multiply(p.astype(LD), np.zeros_like(p, dtype=LD), th, tl)
    u7h, u7l = right_multiply(uh, ul, vhi, vlo)
    protected = (np.column_stack([uh, u7h]), np.column_stack([ul, u7l]))
    gp_h, gp_l = dot_columns(p, None, p, None)
    gih, gil, gi_mp = mp_inverse_split(gp_h, gp_l, DPS)

    ap_h, ap_l = apply_source(*protected)
    rhs_h, rhs_l = -ap_h, -ap_l
    rhs_h[:, 6], rhs_l[:, 6] = add(rhs_h[:, 6], rhs_l[:, 6], gh, gl)
    rhs_h, rhs_l = dd_project(p, gih, gil, rhs_h, rhs_l)
    zh = np.zeros_like(protected[0]); zl = np.zeros_like(zh)
    iterations = []
    initial_residuals = []
    for j in range(7):
        rhs = np.asarray(rhs_h[:, j] + rhs_l[:, j], dtype=float)
        count = [0]
        z, info = cg(op, rhs, rtol=2e-14, atol=0.0, maxiter=40000,
                     callback=lambda _: count.__setitem__(0, count[0]+1))
        if info != 0:
            raise RuntimeError(("normalized CG failed", j, info))
        z = proj(z)
        zh[:, j] = z.astype(LD)
        iterations.append(count[0])
        initial_residuals.append(float(np.linalg.norm(op @ z - rhs)))
    zh, zl = dd_project(p, gih, gil, zh, zl)
    history = []
    for step in range(refinements + 1):
        state = evaluate(p, gih, gil, apply_source, protected, zh, zl, gh, gl)
        vh, vl, avh, avl, rh, rl = state
        norms = [norm2(rh[:, j], rl[:, j]) for j in range(7)]
        history.append(norms)
        progress({"refinement": step, "joint_residual_max_midpoint": max(norms)})
        if step < refinements:
            for j in range(7):
                rhs = -np.asarray(rh[:, j] + rl[:, j], dtype=float)
                delta, info = cg(op, rhs, rtol=2e-14, atol=0.0, maxiter=40000)
                if info != 0:
                    raise RuntimeError(("normalized correction failed", j, info))
                delta = proj(delta).astype(LD)
                zh[:, j], zl[:, j] = add(zh[:, j], zl[:, j], delta, np.zeros_like(delta))
            zh, zl = dd_project(p, gih, gil, zh, zl)

    matrix = affine_assembly(vh, vl, avh, avl, gh, gl)
    rgh, rgl = dot_columns(rh, rl, rh, rl)
    traceh, tracel = dot_columns(p, None, vh, vl)
    with mp.workdps(DPS):
        rg = dd_matrix_to_mp(rgh, rgl); rg = (rg + rg.T) / 2
        if any(not mp.isfinite(matrix[i, j]) or not mp.isfinite(rg[i, j])
               for i in range(7) for j in range(7)):
            raise RuntimeError("nonfinite normalized matrix or residual Gram")
        if any(rg[j, j] < 0 for j in range(7)):
            raise RuntimeError("negative residual-square midpoint; no clipping allowed")
        trace = gi_mp * dd_matrix_to_mp(traceh, tracel)
        expected = mp.matrix(6, 7)
        for i in range(6):
            for j in range(6):
                expected[i, j] = t[i, j]
            expected[i, 6] = (t * v)[i]
        trace_defect = trace - expected
        f = mp.sqrt(mp.fsum(rg[j, j] for j in range(6)))
        s = mp.sqrt(rg[6, 6])
        result = {
            "M_trial_midpoint": [[mp.nstr(matrix[i, j], 100) for j in range(7)] for i in range(7)],
            "residual_gram_midpoint": [[mp.nstr(rg[i, j], 100) for j in range(7)] for i in range(7)],
            "graph_residual_fro_midpoint": mp.nstr(f, 70),
            "combined_source_residual_l2_midpoint": mp.nstr(s, 70),
            "protected_trace_coefficient_defect_midpoint": [[mp.nstr(trace_defect[i, j], 70) for j in range(7)] for i in range(6)],
            "protected_trace_coefficient_defect_fro_midpoint": mp.nstr(mp.norm(trace_defect), 70),
            "normalized_cg_iters": iterations,
            "initial_cg_residuals_midpoint": initial_residuals,
            "lddd_residual_history_midpoint": history,
        }
    if exact_normalizer is not None:
        if trace_witness_path is None:
            raise ValueError("exact trace capture requires a witness path")
        from suzuki_exact_represented_trace_certificate import capture
        result["represented_trial_trace_certificate"] = capture(
            p, vh, vl, exact_normalizer, trace_witness_path)
    if exact_backend is not None:
        from suzuki_exact_integer_source_action import family_from_pairs
        from suzuki_exact_outward_certificate import certificate, p_families, write_snapshot
        columns = [family_from_pairs(vh[:, j], vl[:, j]) for j in range(7)]
        if columns != exact_backend.last_inputs:
            raise RuntimeError("exact action cache does not match final represented trial")
        pf = p_families(p)
        cert = certificate(exact_backend.source, columns, pf, exact_normalizer,
                           outward_context["sector"], outward_context["remote_start"],
                           exact_backend.engine.kernel_bits, exact_backend.last_outputs)
        if cert["frozen_base_P_sha256"] != result["represented_trial_trace_certificate"]["frozen_base_P_sha256"]:
            raise RuntimeError("full-vector exact certificate differs from trace plane")
        if cert["relative_trace_fro_upper_rational"] != result["represented_trial_trace_certificate"]["relative_defect_fro_upper_rational"]:
            raise RuntimeError("full-vector trace bound differs from standalone dyadic trace")
        result["M_lddd_assembly_diagnostic"] = result["M_trial_midpoint"]
        result["M_trial_midpoint"] = cert["M_point_decimal"]
        result["outward_numerical_certificate"] = cert
        snapshot = outward_context["snapshot_path"]
        sha = write_snapshot(snapshot, exact_backend.source, columns, pf, exact_normalizer,
                             outward_context["sector"], outward_context["remote_start"],
                             exact_backend.engine.kernel_bits)
        result["outward_snapshot"] = {"file": snapshot.name, "sha256": sha}
        reference = snapshot.with_suffix(".certificate.json")
        reference.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n")
    return result


def numerical_reduction_summary(row):
    with mp.workdps(DPS):
        m = mp.matrix(row["M_trial_midpoint"])
        j = m[:6, :6]; beta = -m[:6, 6]; eta = -m[6, 6]
        eig, _ = mp.eigsy(j)
        kval = None
        if eig[0] > 0:
            kval = eta + (beta.T * mp.lu_solve(j, beta))[0]
        return {
            "J_min_eigenvalue_midpoint": mp.nstr(eig[0], 70),
            "beta_l2_midpoint": mp.nstr(mp.norm(beta), 70),
            "eta_midpoint": mp.nstr(eta, 100),
            "K_if_J_positive_midpoint": mp.nstr(kval, 100) if kval is not None else None,
        }


def one(sector, cutoff, remote_start, normalizer, refinements, kernel,
        trace_witness_path):
    from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P, modes_for
    from suzuki_full_fft_fixed_capacity_replay import fixed_operator
    started = time.monotonic()
    modes = modes_for(sector, cutoff)
    p = embedded_P(sector, modes)
    ph, pl = dot_columns(p, None, p, None)
    _, _, gi = mp_inverse_split(ph, pl, DPS)
    gif = np.array([[float(gi[i, j]) for j in range(6)] for i in range(6)])
    _, proj, op, _ = fixed_operator(modes, sector, p, gif)
    progress = lambda d: print(json.dumps({"sector": sector, "cutoff": cutoff, **d}), flush=True)
    progress({"stage": "build source-faithful scalar data"})
    data = hp_parity_data_ld(modes, sector, dps=DPS, arch_terms=200, correction_terms=50)
    gh = np.zeros(len(modes), dtype=LD); gl = np.zeros_like(gh)
    with mp.workdps(DPS):
        for i, n in enumerate(modes):
            if n > remote_start:
                denom = int(n) if sector == "even-v" else int(n)-1
                gh[i], gl[i] = split_mpf_ld(1/mp.mpf(denom))
        t = mp.matrix(normalizer["T"]); v = mp.matrix(normalizer["v"])
        progress({"stage": "direct normalized RHS solves and refinement"})
        backend = None
        if kernel == "exact":
            from suzuki_exact_integer_source_action import ExactBackend
            backend = ExactBackend(data)
            action = backend.action_arrays
        elif kernel == "native":
            from suzuki_ldd_native_matvec import native_matvec
            action = lambda h, l: native_matvec(data, h, l)
        else:
            action = lambda h, l: source_action(data, h, l)
        row = solve_joint(p, op, proj, action, gh, gl, t, v,
                          refinements, progress, normalizer, trace_witness_path,
                          backend, {"sector": sector, "remote_start": remote_start,
                          "snapshot_path": trace_witness_path.with_name(trace_witness_path.name.replace(".json.gz", ".full.zip"))})
    if row["represented_trial_trace_certificate"]["frozen_base_P_sha256"] != digest(np.asarray(p[:2000], dtype="<f8").tobytes()):
        raise RuntimeError("exact trace witness differs from the frozen represented P bytes")
    row.update({
        "schema": SCHEMA, "sector": sector, "cutoff": cutoff,
        "dimension": len(modes), "remote_start": remote_start,
        "normalizer_sha256": normalizer["normalizer_sha256"],
        "frozen_base_P_sha256": digest(np.asarray(p[:2000], dtype="<f8").tobytes()),
        "modes_sha256": digest(np.asarray(modes, dtype="<i8").tobytes()),
        "source_definition": "zero through remote_start; 1/n even-v, 1/(n-1) odd-v, formed before solves in high precision",
        "precision": {"mp_dps": DPS, "longdouble_nmant": np.finfo(LD).nmant,
                      "operator_arch_terms": 200, "operator_correction_terms": 50},
        "runtime": {"python": platform.python_version(), "numpy": np.__version__,
                    "scipy": scipy.__version__, "mpmath": mp.__version__, "kernel": kernel},
        "trace_contract": {"exact_target": "(I-Q)V=[P T,P T v]",
                           "certificate_status": "exact represented-vector defect bound; correction cap transport still required",
                           "outward_defect_cap": row["represented_trial_trace_certificate"]["coefficient_defect_fro_upper_rational"],
                           "relative_defect_fro_cap": row["represented_trial_trace_certificate"]["relative_defect_fro_upper_rational"],
                           "correction_assembly_cap": None},
        "coercivity_contract": {"required_operator": "C_R=(Q_R A_R Q_R)|Ran Q_R, full frozen-six-plane complement",
                                "operator_projector_cutoff_identification_certificate": None,
                                "gamma_certified": None,
                                "remote_S_gamma_1_is_not_this_operator": True},
        "certification": {"ready": False, "missing": MISSING, "assembly_alpha": None,
                          "graph_residual_fro_outward": None, "combined_source_residual_l2_outward": None,
                          "normalized_matrix_outward": None},
        "elapsed_seconds": time.monotonic()-started,
        "guardrail": "Direct normalized LDDD source/assembly/residual midpoint. Represented-vector trace bound is exact rational; overall certificate incomplete; no use of remote-Schur gamma=1 for full Q complement.",
    })
    row["summary_midpoint"] = numerical_reduction_summary(row)
    if backend is not None:
        cert = row["outward_numerical_certificate"]
        bounds = cert["bounds_rational"]
        row["certification"].update({
            "assembly_J_alpha_outward": bounds["assembly_J"],
            "assembly_beta_alpha_outward": bounds["assembly_beta"],
            "assembly_eta_alpha_outward": bounds["assembly_eta"],
            "graph_residual_fro_outward": bounds["graph_residual_fro"],
            "combined_source_residual_l2_outward": bounds["source_residual_l2"],
            "all_six_numerical_targets_met": cert["all_six_numerical_targets_met"],
            "missing": [k for k, passed in cert["checks_exact"].items() if not passed]
                       + ["independent_audit_of_new_exact_point_outward_arithmetic_bridge"],
        })
        if cert["fullQ_floor_rational"] is not None:
            row["coercivity_contract"].update({
                "operator_projector_cutoff_identification_certificate": "v14.155/v14.158/v14.161; audited frozen P byte hash matched",
                "gamma_certified": cert["fullQ_floor_rational"],
            })
        row["guardrail"] = "All-source point action, assembly and projection checked with exact integers/Fractions; physical-source charges explicit. New outward bridge awaits independent audit; no infinite-tail conclusion."
    progress({"stage": "complete", **row["summary_midpoint"]})
    return row


def transition(rows):
    out = []
    with mp.workdps(DPS):
        for a, b in zip(rows, rows[1:]):
            if a["normalizer_sha256"] != b["normalizer_sha256"] or a["frozen_base_P_sha256"] != b["frozen_base_P_sha256"]:
                raise RuntimeError("nested reductions do not share frozen coordinates")
            ma, mb = mp.matrix(a["M_trial_midpoint"]), mp.matrix(b["M_trial_midpoint"])
            diff = ma-mb
            ja, jb = ma[:6, :6], mb[:6, :6]
            beta, z = -ma[:6, 6], -mb[:6, 6]
            phi = None
            ea, _ = mp.eigsy(ja); eb, _ = mp.eigsy(jb)
            if ea[0] > 0 and eb[0] > 0:
                phi = diff[6, 6]+(z.T*mp.lu_solve(jb, z))[0]-(beta.T*mp.lu_solve(ja, beta))[0]
            out.append({"R": a["cutoff"], "R2": b["cutoff"],
                        "G_midpoint": [[mp.nstr(diff[i, j], 100) for j in range(6)] for i in range(6)],
                        "tau_midpoint": [mp.nstr(-diff[i, 6], 100) for i in range(6)],
                        "sigma_midpoint": mp.nstr(diff[6, 6], 100),
                        "increment_if_both_J_positive_midpoint": mp.nstr(phi, 100) if phi is not None else None,
                        "certificate_ready": False})
    return out


def self_test():
    """Independent exact-rational reference for the actual normalization path."""
    from fractions import Fraction as F
    from suzuki_fixed_normalizer_joint_residual_replay import (
        zeros, eye, mul as fm, tr, add as fa, inv, reduction,
    )
    import random
    rng = random.Random(194)
    n, k = 11, 6
    b = [[F(rng.randint(-3, 3), 7) for _ in range(n)] for _ in range(n)]
    a = fa(fm(tr(b), b), eye(n)); g = [[F(rng.randint(-3, 3), 23)] for _ in range(n)]
    c = zeros(k, k)
    for i in range(k):
        c[i][i] = F(10**(3*i))
        if i+1 < k: c[i][i+1] = c[i][i]/3
    transform = eye(n)
    for i, row in enumerate(inv(c)): transform[i][:k] = row
    a = fm(tr(transform), fm(a, transform)); g = fm(tr(transform), g)
    offset = [[F(i+1, 1000)] for i in range(k)]
    reference = reduction(a, g, c, offset, 194)
    def asmp(x): return mp.matrix([[mp.mpf(v.numerator)/v.denominator for v in row] for row in x])
    with mp.workdps(DPS):
        am, gm, tm, vm = asmp(a), asmp(g), asmp(c), asmp(offset)
        ah, al = split_matrix(am); gh, gl = split_matrix(gm)
        p = np.zeros((n, k)); p[:k] = np.eye(k)
        ap = np.asarray(am.tolist(), dtype=float)
        def proj(x):
            q = np.array(x, dtype=float, copy=True); q[:k] = 0; return q
        def mv(x):
            q = proj(x); y = proj(ap @ q); y[:k] += x[:k]; return y
        op = LinearOperator((n, n), matvec=mv, dtype=float)
        result = solve_joint(p, op, proj, lambda h, l: dd_small_matmul(ah, al, h, l),
                             gh[:, 0], gl[:, 0], tm, vm, 1, lambda _: None)
        actual = mp.matrix(result["M_trial_midpoint"])
        error = mp.norm(actual-asmp(reference["m"]))
        if error > mp.mpf("1e-25"):
            raise RuntimeError(("direct normalized synthetic identity failure", mp.nstr(error, 60)))
        trace = mp.mpf(result["protected_trace_coefficient_defect_fro_midpoint"])
        if trace > mp.mpf("1e-25"):
            raise RuntimeError("synthetic protected trace failed")
    from suzuki_ldd_native_matvec import native_matvec
    checked = 0
    rngn = np.random.default_rng(193)
    with mp.workdps(DPS):
        for sector, start in (("even-v", 1), ("odd-v", 2)):
            data = hp_parity_data_ld(np.arange(start, 65, 2), sector, dps=DPS, arch_terms=200)
            for sparse in (False, True):
                h = rngn.normal(size=(32, 7)).astype(LD)
                l = (rngn.normal(size=(32, 7))*1e-20).astype(LD)
                if sparse: h[4:] = 0; l[4:] = 0
                ah, al = matvec(data, h, l)
                bh, bl = native_matvec(data, h, l)
                if not (np.array_equal(ah, bh) and np.array_equal(al, bl)):
                    raise RuntimeError("native kernel differs from reference hi/lo components")
                checked += 1
    from suzuki_exact_represented_trace_certificate import self_test as trace_test
    return {"synthetic_passed": True, "affine_matrix_error": mp.nstr(error, 60),
            "normalizer_span": "1 to 1e15", "source_reference": "exact Fraction full-system elimination",
            "native_reference_component_identical_cases": checked,
            "exact_trace_certificate_test": trace_test(),
            "certificate_promoted": False}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--require-certificate", action="store_true")
    ap.add_argument("--sector", choices=["even-v", "odd-v"])
    ap.add_argument("--cutoffs", type=int, nargs="+", default=[64000, 128000])
    ap.add_argument("--remote-start", type=int, default=32000)
    ap.add_argument("--refinements", type=int, default=1)
    ap.add_argument("--kernel", choices=["native", "numpy", "exact"], default="native")
    ap.add_argument("--offset-scale", default="1")
    ap.add_argument("--anchor-root", type=Path, default=HERE/"payloads/M64000_corrected_run_37659896312")
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    if np.finfo(LD).nmant < 63:
        raise RuntimeError("LDDD requires a 64-bit longdouble significand")
    if a.self_test:
        print(json.dumps(self_test(), indent=2)); return
    if a.require_certificate:
        raise RuntimeError(("outward certificate unavailable", MISSING))
    if not a.sector or not a.output:
        ap.error("--sector and --output required for source replay")
    if a.cutoffs != sorted(set(a.cutoffs)) or min(a.cutoffs) < 4000 or max(a.cutoffs) > 128000:
        ap.error("unique increasing cutoffs between 4000 and 128000 required")
    if a.remote_start < 0 or a.refinements < 0:
        ap.error("nonnegative source frontier and refinement count required")
    normalizer = frozen_normalizer(a.sector, a.anchor_root, a.offset_scale)
    rows = [one(a.sector, r, a.remote_start, normalizer, a.refinements, a.kernel,
                a.output.with_name(a.output.stem + f".trace-{r}.json.gz"))
            for r in a.cutoffs]
    out = {"schema": SCHEMA, "normalizer": normalizer, "rows": rows, "transitions": transition(rows),
           "certification_ready": False,
           "missing_certificates": sorted({k for row in rows for k in row["certification"]["missing"]})}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    print("OUTPUT", a.output, flush=True)


if __name__ == "__main__":
    main()
