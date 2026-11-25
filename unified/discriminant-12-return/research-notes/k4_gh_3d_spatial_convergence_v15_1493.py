#!/usr/bin/env python3
"""Gravity v15.1493: spatial resolution convergence of genuine unrestricted
3+1 generalized-harmonic Einstein-H2 evolution on independently solved
nonlinear ADM+GH initial data. Replays corrected v15.1485 solver.
Do not confuse convergent native-grid constraints with off-grid
certification (see v15.1487 and v15.1491).
"""
import time
import numpy as np
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid, initial, rk4
def run(N,dt=.004,T=.008):
    g=GHGrid(N); t0=time.time(); y=initial(N)
    h0,m0=g.adm(y);c0=g.rhs(y,True)[0]
    for _ in range(round(T/dt)):
        y=rk4(y,dt,g.rhs)
    c,gtt=g.rhs(y,True);h,m=g.adm(y)
    row=dict(N=N,dt=dt,T=T,initial_H=h0,initial_M=m0,
             initial_GH=c0,evolved_H=h,evolved_M=m,evolved_GH=c,
             inverse_gtt=gtt,seconds=time.time()-t0)
    print(row,flush=True)
    assert gtt<0 and np.isfinite(c+h+m)
    return row
if __name__=="__main__":
    rows=[run(n) for n in (24,32,40)]
    for field in ("evolved_H","evolved_M","evolved_GH"):
        ratios=[rows[i][field]/rows[i+1][field] for i in (0,1)]
        print("resolution reduction",field,ratios,flush=True)
        assert all(x>15 for x in ratios)
    print("PASS short-time spatial convergence on native grids")
    print("OPEN independent Audit, dealiased/offgrid constraint and long-time certification")
