#!/usr/bin/env python3
"""Quantify the smoothness cancellation in <w_o, (D_o-D_e) w_e>.

Compares the naive bound ||D_o-D_e||*||w_o||*||w_e|| against the actual
quadratic form, to measure how much the oscillatory operator difference
cancels against smooth vectors. This motivates the Riccati approach.
"""
from __future__ import annotations
import numpy as np
from infinite_tail_producer import paired_modes, z_parity, kernel, diag_kernel
from infinite_tail_probe import build_D

def main():
    N = 16000
    J = 400
    ns, ms = paired_modes(N, J)
    zcache = {}
    for n in ns: zcache[(n, "even")] = z_parity(n, "even")
    for m in ms: zcache[(m, "odd")] = z_parity(m, "odd")
    De = build_D(ns, "even", zcache); De = 0.5*(De+De.T)
    Do = build_D(ms, "odd", zcache);  Do = 0.5*(Do+Do.T)

    ue = 1.0/np.array(ns,float); uo = 1.0/np.array(ms,float)
    we = np.linalg.solve(De, ue); wo = np.linalg.solve(Do, uo)
    Delta = Do - De

    naive = np.linalg.norm(Delta,2)*np.linalg.norm(wo)*np.linalg.norm(we)
    actual = wo @ (Delta @ we)
    print(f"naive  ||Delta||*||wo||*||we|| = {naive:.6e}")
    print(f"actual |<wo,Delta we>|           = {abs(actual):.6e}")
    print(f"cancellation factor = {naive/abs(actual):.3e}")
    print()
    # K_o - K_e via Riccati vs direct
    Ke = ue @ we; Ko = uo @ wo
    print(f"K_e={Ke:.6e} K_o={Ko:.6e} diff={Ko-Ke:.6e}")
    print(f"Riccati -<wo,Delta we> = {-actual:.6e}  (should equal K_o-K_e)")
    # decompose Delta into diagonal and off-diagonal contributions
    dd = np.diag(np.diag(Delta)); off = Delta - dd
    print(f"<wo, diag(Delta) we> = {wo@(dd@we):.6e}")
    print(f"<wo, offdiag(Delta) we> = {wo@(off@we):.6e}")
    # rank-1 C/(nm) fit: least squares for C in Delta_jk ~ C/(n_j m_k)
    nj = np.array(ns,float); mj = np.array(ms,float)
    A = np.outer(1/mj, 1/nj)  # C/(m_j n_k)? careful with index order
    # Delta_jk ~ C/(n_j*m_k)? use outer(1/nj, 1/mk)
    B = np.outer(1/nj, 1/mj)
    Cfit = np.sum(Delta*B)/np.sum(B*B)
    print(f"rank-1 fit C in Delta~C/(n_j m_k): C={Cfit:.4f}")
    resid = Delta - Cfit*B
    print(f"||resid||_2={np.linalg.norm(resid,2):.4e} ||resid||_F={np.linalg.norm(resid,'fro'):.4e}")
    print(f"<wo, resid we> = {wo@(resid@we):.6e}")

if __name__ == "__main__":
    main()
