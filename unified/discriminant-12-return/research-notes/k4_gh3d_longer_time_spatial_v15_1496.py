#!/usr/bin/env python3
"""Gravity v15.1496: unrestricted 3D Einstein-H2 generalized harmonic
time evolution at 24^3/32^3 to T=.04, with independent ADM and GH
native-grid constraints. Reproduces completed local N32 run.
Use OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 to avoid BLAS oversubscription.
N32 2x offgrid and dt=.002 were attempted but NOT completed.
"""
import os,time,numpy as np
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial,rk4
def run(N,dt=.004,T=.04):
    start=time.monotonic()
    grid=GHGrid(N)
    y=initial(N)
    initial_H,initial_M=grid.adm(y)
    initial_GH,_=grid.rhs(y,True)
    for _ in range(round(T/dt)):
        y=rk4(y,dt,grid.rhs)
    gh,gtt=grid.rhs(y,True)
    ham,mom=grid.adm(y)
    result=dict(N=N,dt=dt,T=T,initial_GH=initial_GH,
       initial_H=initial_H,initial_M=initial_M,
       final_GH=gh,final_H=ham,final_M=mom,
       max_inverse_gtt=gtt,elapsed_s=time.monotonic()-start)
    print(result,flush=True)
    assert np.isfinite(gh+ham+mom) and gtt<0
    return result
if __name__=="__main__":
    a=run(24);b=run(32)
    print("native-grid resolution ratios",{
     k:a[k]/b[k] for k in ("final_GH","final_H","final_M")},flush=True)
    assert all(a[k]/b[k]>30 for k in ("final_GH","final_H","final_M"))
    print("PASS 24^3 and 32^3 unrestricted Einstein-H2 GH evolution to T=.04")
    print("OPEN 32^3 offgrid check, dt refinement, independent Audit and long-time stability")
