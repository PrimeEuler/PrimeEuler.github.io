#!/usr/bin/env python3
"""Repaired final six-root Rouché diagnostic using the whole high-tail inverse.

Keep core modes 1..23 / 2..24 and eliminate only the finite high-tail front
through 999/1000.  The finite graph residual is then charged against the
inverse of the entire exact high tail, whose contour coercivity is certified
separately.  This avoids the buffer-mediated self-energy omission in the
first 12001/12002 candidate.
"""
from __future__ import annotations
import math
import numpy as np
import suzuki_full_six_root_rouche_certificate as R

R.CUT={"even-v":999,"odd-v":1000}
R.REMOTE_START={"even-v":1001,"odd-v":1002}
R.EXPLICIT_STOP=20000

HIGH_TAIL_FLOOR={"even-v":0.28,"odd-v":0.32}
NSAMP=R.NSAMP

def one_sector(sector):
    outer=R.outer_analytic_caps(sector)
    theta=2.0*math.pi*np.arange(NSAMP)/NSAMP
    modes0=R.modes_for(sector,R.CUT[sector])
    nremote=len(np.arange(R.REMOTE_START[sector],R.EXPLICIT_STOP+1,2))

    Ssamples=np.empty((NSAMP,12,12),dtype=np.complex128)
    Ysamples=np.empty((NSAMP,nremote,12),dtype=np.complex128)
    Wsamples=np.empty((NSAMP,len(modes0),12),dtype=np.complex128)

    for j,th in enumerate(theta):
        zparam=R.RADIUS*np.exp(1j*th)
        modes,zfinite,pfinite,alpha,S,W=R.finite_graph(sector,zparam)
        Ssamples[j]=S
        Wsamples[j]=W
        Ysamples[j]=R.direct_remote_rows(
            sector,zparam,modes,zfinite,pfinite,alpha,W
        )

    Scoef=R.dft_coeff(Ssamples)
    Ycoef=R.dft_coeff(Ysamples)
    Wcoef=R.dft_coeff(Wsamples)

    salias=R.analytic_alias_cap(outer["Schur_outer"])+R.MODEL_RESERVE
    minpoly,deriv=R.fourier_matrix_dense(Scoef)
    finite_floor=minpoly-salias

    winding,phase_step,phase_speed,phase_interval=R.winding_from_coeff(
        Scoef,minpoly,deriv
    )

    yalias=R.analytic_alias_cap(outer["Y_outer"])+R.MODEL_RESERVE
    yexplicit=R.fourier_operator_sup(Ycoef,yalias)
    far=R.uniform_far_bound(
        sector,modes0,Wcoef,outer["graph_outer"]
    )+R.MODEL_RESERVE

    residual_sq=yexplicit*yexplicit+far*far
    correction=residual_sq/HIGH_TAIL_FLOOR[sector]+R.MODEL_RESERVE
    margin=finite_floor-correction

    # Diagnostic: direction-aware explicit-row Rouché factor at sample nodes.
    directional=[]
    for j in range(NSAMP):
        S=Ssamples[j]
        Y=Ysamples[j]
        yn=float(np.linalg.norm(Y,2))
        left=np.linalg.solve(S,Y.T)
        ln=float(np.linalg.norm(left,2))
        directional.append((ln*yn)/HIGH_TAIL_FLOOR[sector])
    directional_max=max(directional)

    print("\nsector =",sector)
    print("outer caps =",outer)
    print("finite contour floor =",finite_floor)
    print("finite winding =",winding)
    print("phase step =",phase_step)
    print("phase speed bound =",phase_speed)
    print("phase interval bound =",phase_interval)
    print("explicit residual norm =",yexplicit)
    print("far residual norm =",far)
    print("residual square cap =",residual_sq)
    print("high-tail floor =",HIGH_TAIL_FLOOR[sector])
    print("exact Schur correction =",correction)
    print("Rouche margin =",margin)
    print("sample directional explicit Rouche factor =",directional_max)

    if winding!=6: raise RuntimeError(("finite winding",sector,winding))
    if finite_floor<=0: raise RuntimeError(("finite floor",sector,finite_floor))
    # Scalar margin may fail; the directional factor is the next proof gate.
    if directional_max>=5.0:
        raise RuntimeError(("directional factor unexpectedly huge",sector,directional_max))

    return dict(
        finite_floor=finite_floor,winding=winding,
        yexplicit=yexplicit,far=far,residual_sq=residual_sq,
        correction=correction,margin=margin,
        directional_explicit=directional_max,
        phase_interval=phase_interval,outer=outer,
    )

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    print("\nPASS repaired whole-high-tail directional diagnostic")
    print("Scalar Rouché may fail; inspect the reported direction-aware factors.")

if __name__=="__main__":
    main()
