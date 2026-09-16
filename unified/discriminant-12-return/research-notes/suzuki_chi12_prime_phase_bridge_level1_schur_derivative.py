#!/usr/bin/env python3
"""Level-1 analytic prime-channel Schur derivative for the canonical M=3999 Suzuki split.

Companion to suzuki_chi12_prime_phase_bridge_level0.py and the canonical
suzuki_M3999_unresolved_fourplane_residual_gram_replay.py.

For each existing source channel q in {2,3,4,5,7}, scale that channel by
(1+alpha) and differentiate the *full finite Schur complement* analytically at
alpha=0.  This is the first non-tautological propagation observable in the
chi_12 phase-bridge program.

Important: the Schur complement is nonlinear.  dS_q is a Frechet derivative;
we do NOT assert S=sum_q S_q.  The frozen unresolved four-plane is N=ker(Q^T),
with Q exactly the v13.399 dyadic basis used by the M3999 replay.

Status: numerical diagnostic only. No bridge/RH/GRH claim.
"""
from __future__ import annotations
import importlib.util, math, pathlib
import numpy as np

HERE=pathlib.Path(__file__).resolve().parent
BASE_PATH=HERE/'suzuki_M3999_unresolved_fourplane_residual_gram_replay.py'
spec=importlib.util.spec_from_file_location('base3999',BASE_PATH)
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
PI=math.pi


def qbasis():
    Q=np.array([[float.fromhex(x) for x in row] for row in base.Q_HEX])
    # deterministic SVD null basis; only the four-plane is intrinsic.
    U,s,Vh=np.linalg.svd(Q.T,full_matrices=True)
    N=Vh[6:].T
    assert np.linalg.norm(Q.T@N,2)<2e-15
    return Q,N


def channel_arrays(q:int,vm:int,modes:np.ndarray):
    ell=math.log(q); w=math.log(vm)/math.sqrt(q); k=modes*PI/2
    dP=w*np.sin(k*ell)
    dPd=-w*((2-ell)*np.cos(k*ell)+np.sin(k*ell)/k)
    # Z=2P+..., diag0=cusp+Pd+D
    return 2*dP,dPd


def source_with_components():
    modes,Z,diag0,c=base.source_data()
    return modes,Z,diag0,c


def build_blocks(modes,Z,diag0,c):
    low=modes[:10]; high=modes[10:]
    ZC,ZF=Z[:10],Z[10:]; cC,cF=c[:10],c[10:]
    A0CC=base.off_block(low,ZC,low,ZC); np.fill_diagonal(A0CC,diag0[:10])
    A0FC=base.off_block(high,ZF,low,ZC)
    ACC=A0CC+2*np.outer(cC,cC); AFC=A0FC+2*np.outer(cF,cC)
    return low,high,ACC,AFC,ZC,ZF,cC,cF


def derivative_blocks(modes,Z,dZ,ddiag):
    low=modes[:10].astype(float); high=modes[10:].astype(float)
    ZC,ZF=Z[:10],Z[10:]; dZC,dZF=dZ[:10],dZ[10:]
    # Off-diagonal Frechet derivative of
    # -(2/pi)*(n Z_m - m Z_n)/(n^2-m^2).
    def doff(ms,Zs,dZs,ns,Zn,dZn):
        ms=ms[:,None]; ns=ns[None,:]
        dZs=dZs[:,None]; dZn=dZn[None,:]
        return -(2/PI)*(ns*dZs-ms*dZn)/(ns**2-ms**2)
    dCC=doff(low,ZC,dZC,low,ZC,dZC)
    np.fill_diagonal(dCC,ddiag[:10])
    dFC=doff(high,ZF,dZF,low,ZC,dZC)
    dFF=doff(high,ZF,dZF,high,ZF,dZF)
    np.fill_diagonal(dFF,ddiag[10:])
    return dCC,dFC,dFF


def dense_ff(modes,Z,diag0,c):
    high=modes[10:]; ZF=Z[10:]; cF=c[10:]
    AFF=base.off_block(high,ZF,high,ZF); np.fill_diagonal(AFF,diag0[10:])
    AFF+=2*np.outer(cF,cF)
    return AFF


def analytic_dS(q:int,vm:int):
    modes,Z,diag0,c=source_with_components()
    low,high,ACC,AFC,ZC,ZF,cC,cF=build_blocks(modes,Z,diag0,c)
    dZ,ddiag=channel_arrays(q,vm,modes.astype(float))
    dCC,dFC,dFF=derivative_blocks(modes,Z,dZ,ddiag)
    AFF=dense_ff(modes,Z,diag0,c)
    # X=A_FF^{-1} A_FC; Y=A_FF^{-1} dA_FC.
    # Dense solve is intentional here: this derivative checker is an independent
    # algebraic implementation, not a reuse of the structured derivative itself.
    X=np.linalg.solve(AFF,AFC)
    Y=np.linalg.solve(AFF,dFC)
    dS=dCC-dFC.T@X-AFC.T@Y+X.T@dFF@X
    return (dS+dS.T)/2


def finite_difference(q:int,vm:int,h:float):
    modes,Z,diag0,c=source_with_components(); dZ,ddiag=channel_arrays(q,vm,modes.astype(float))
    def S(alpha):
        Za=Z+alpha*dZ; da=diag0+alpha*ddiag
        low,high,ACC,AFC,*_=build_blocks(modes,Za,da,c)
        AFF=dense_ff(modes,Za,da,c)
        X=np.linalg.solve(AFF,AFC)
        out=ACC-AFC.T@X
        return (out+out.T)/2
    return (S(h)-S(-h))/(2*h)


def main():
    Q,N=qbasis(); support=((2,2),(3,3),(4,2),(5,5),(7,7))
    print('Level-1 M3999 analytic Schur derivative')
    print('||Q^T N||_2 =',np.linalg.norm(Q.T@N,2))
    for q,vm in support:
        dS=analytic_dS(q,vm); B=N.T@dS@N; B=(B+B.T)/2
        # One finite-difference regression point. This is expensive but independent.
        h=2.0**-12; dSfd=finite_difference(q,vm,h)
        rel=np.linalg.norm(dS-dSfd,'fro')/max(np.linalg.norm(dS,'fro'),1e-300)
        eig=np.linalg.eigvalsh(B)
        print(f'q={q:2d} ||dS||F={np.linalg.norm(dS,"fro"):.17g} '
              f'||B||F={np.linalg.norm(B,"fro"):.17g} fd_rel={rel:.3e} '
              f'eig(B)={eig}')
        assert rel<2e-6, (q,rel)
    print('PASS Level 1 algebraic propagation regression.')
    print('AUDIT: dS_q is a derivative of the nonlinear Schur map, not an additive channel decomposition.')
    print('AUDIT: no bridge, terminal-direction, RH, or GRH claim.')

if __name__=='__main__': main()
