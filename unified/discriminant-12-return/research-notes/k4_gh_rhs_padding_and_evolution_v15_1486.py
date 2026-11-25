#!/usr/bin/env python3
"""Gravity v15.1486: true 2x padded nonlinear GH Einstein-H2 RHS
vs independent 3x reference; actual short RK4 with unchanged
constrained initial state. NEGATIVE: padding RHS alone does not
improve all Einstein/GH constraints. Uses repaired v15.1485 solver.
"""
import numpy as np
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial,rk4
def resize(a,M):
 for axis in (-3,-2,-1):
  a=resample(a,M,axis=axis)
 return np.asarray(a.real)
def padded_rhs(y,M):
 N=y[0].shape[-1]
 up=tuple(resize(c,M) for c in y)
 hi=GHGrid(M).rhs(up)
 return tuple(resize(c,N) for c in hi)
def check_rhs(N):
 g=GHGrid(N);state=initial(N)
 native=g.rhs(state);twice=padded_rhs(state,2*N);thrice=padded_rhs(state,3*N)
 for idx,name in [(1,"metric acceleration"),(3,"sigma acceleration")]:
  err_native=float(np.max(abs(native[idx]-thrice[idx])))
  err_padded=float(np.max(abs(twice[idx]-thrice[idx])))
  print("RHS",N,name,"native_vs_3x",err_native,"2x_vs_3x",err_padded,flush=True)
  assert err_padded<err_native
def finite_time(N,T=.008,dt=.004):
 g=GHGrid(N);base=initial(N)
 for label,rhs in [("native",g.rhs),("2x_padded",lambda y:padded_rhs(y,2*N))]:
  y=tuple(c.copy() for c in base)
  for _ in range(round(T/dt)):y=rk4(y,dt,rhs)
  gh,gtt=g.rhs(y,True);ham,mom=g.adm(y)
  print("EVOL",N,label,"T",T,"GH",gh,"Hamiltonian",ham,
       "Momentum",mom,"inverse_gtt",gtt,flush=True)
  assert np.isfinite(gh+ham+mom) and gtt<0
if __name__=="__main__":
 for n in (12,16):
  check_rhs(n)
  finite_time(n)
 print("PASS 2x padded acceleration closer to 3x reference")
 print("NEGATIVE 2x padded short-time full GH Einstein-H2 evolution")
 print("         does not uniformly improve ADM H/M and GH residuals")
 print("OPEN consistent high-resolution constraint monitor and initial elliptic correction")
