#!/usr/bin/env python3
"""Gravity v15.1487: independent 2x-grid evaluation of nonlinear
Einstein H/M and all four GH constraints on the SAME initial and
short-time evolved 3D GH-H2 state. Strong NEGATIVE: native collocation
constraint cancellations do not survive oversampled evaluation.
Uses repaired v15.1485 solver. Do not confuse with filtering fields.
"""
import numpy as np
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial,rk4
def upsample(state,M):
 result=[]
 for a in state:
  for axis in (-3,-2,-1):a=resample(a,M,axis=axis)
  result.append(a.real)
 return tuple(result)
def monitor(N,T=.008):
 lo=GHGrid(N);hi=GHGrid(2*N)
 y=initial(N)
 def check(label,y):
  gh,gtt=lo.rhs(y,True);ham,mom=lo.adm(y)
  interpolated=upsample(y,2*N)
  gh2,gtt2=hi.rhs(interpolated,True);ham2,mom2=hi.adm(interpolated)
  print(dict(N=N,stage=label,native_GH=gh,padded_GH=gh2,
    native_H=ham,padded_H=ham2,native_M=mom,padded_M=mom2,
    native_inverse_gtt=gtt,padded_inverse_gtt=gtt2),flush=True)
  assert gtt<0 and gtt2<0
  return gh,gh2,ham,ham2,mom,mom2
 start=check("initial",y)
 for _ in range(round(T/.004)):y=rk4(y,.004,lo.rhs)
 end=check("t=.008",y)
 assert start[1]>start[0]*5
 assert start[3]>start[2]
 return start,end
if __name__=="__main__":
 for n in (16,24):monitor(n)
 print("PASS NEGATIVE native-grid constraints do not certify same state on oversampled grid")
 print("NEXT nonlinear elliptic Cauchy constraints must be solved/certified with oversampled products")
