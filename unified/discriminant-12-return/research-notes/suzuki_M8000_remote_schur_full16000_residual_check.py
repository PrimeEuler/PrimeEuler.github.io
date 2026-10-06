#!/usr/bin/env python3
"""Calibrate the exact-near Schur operator against the known full M=16000 solution.

No outer remote solve is performed.  The promoted/full finite-section solution
is partitioned at M=8000; its remote component is inserted into the Schur
equation.  We test both:
  (1) exact dense remote raw block, and
  (2) FFT + arch-200 remote raw action.

This isolates transport/normalization errors from remote-CG convergence.
Diagnostic only.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

import suzuki_M8000_remote_schur_fft_diagnostic as b
import suzuki_M8000_remote_schur_exact_near_endpoint as ex
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import state

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_remote_schur_full16000_residual_check_result.json"

def one(sector):
    print("build M8000 front operator",sector,flush=True)
    st=ex.build_front_operator(sector)
    print("build full M16000 theorem state",sector,flush=True)
    full=state(sector,16000)

    nf=len(st["modes"])
    if not np.array_equal(full["modes"][:nf],st["modes"]):
        raise RuntimeError("front prefix mismatch")

    rm,BT,Bv,cmeta=ex.build_coupling(st,sector,16000)
    if not np.array_equal(full["modes"][nf:],rm):
        raise RuntimeError(("remote suffix mismatch",full["modes"][nf:nf+4],rm[:4]))

    sq=float(st["sqrtC"])
    f=b.source_rows(rm)
    r=sq*f-Bv(st["y"])

    # Known normalized remote component from the full M16000 source solution.
    z=sq*np.asarray(full["x"][nf:],dtype=float)
    eta_rz=float(r@z)

    counters={"calls":0,"max_res0":0.0,"max_res1":0.0}
    t=BT(z)
    y=ex.front_response(st,t,counters)
    schur_term=Bv(y)

    # FFT/arch-200 raw action.
    zr=b.z_source_faithful(rm)
    p,alpha=b.pole_vector(rm,sector)
    diag=b.cusp_diag(rm)+b.prime_diag(rm)+b.arch_diag_vector(rm,terms=200)
    raw_fft=b.fft_offdiag(rm,zr,z)+diag*z+alpha*p*float(p@z)
    res_fft=raw_fft-schur_term-r

    # Fully dense exact-source remote raw block at the same endpoint.
    Drr,fr_dense=b.full_source_matrix(rm,sector)
    source_diff=float(np.linalg.norm(fr_dense-f))
    raw_dense=Drr@z
    res_dense=raw_dense-schur_term-r

    C_front=sq*sq
    eta_caps=C_front/float(full["C"])-1.0
    target=ex.TARGET[sector]
    row={
      "sector":sector,
      "front_dimension":nf,
      "remote_dimension":len(rm),
      "eta_r_dot_full_remote":eta_rz,
      "eta_from_capacities":eta_caps,
      "eta_theorem_target":target,
      "eta_rz_minus_target":eta_rz-target,
      "eta_caps_minus_target":eta_caps-target,
      "remote_source_formula_l2_difference":source_diff,
      "schur_residual_dense_l2":float(np.linalg.norm(res_dense)),
      "schur_residual_dense_linf":float(np.max(np.abs(res_dense))),
      "schur_residual_fft_l2":float(np.linalg.norm(res_fft)),
      "schur_residual_fft_linf":float(np.max(np.abs(res_fft))),
      "fft_minus_dense_action_l2":float(np.linalg.norm(raw_fft-raw_dense)),
      "fft_minus_dense_action_linf":float(np.max(np.abs(raw_fft-raw_dense))),
      "front_response_calls":counters["calls"],
      "front_response_max_residual_before_refine":counters["max_res0"],
      "front_response_max_residual_after_refine":counters["max_res1"],
      **cmeta,
      "guardrail":"Known-full-solution Schur residual diagnostic only; no infinite-tail claim."
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
