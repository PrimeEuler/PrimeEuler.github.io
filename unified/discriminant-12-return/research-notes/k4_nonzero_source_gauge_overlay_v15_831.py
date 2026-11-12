#!/usr/bin/env python3
"""v15.831: audited five-helicity nonzero source, overlaid with 3D gauge.

Inputs are the independently audited v15.818 five differential complex
Fourier coefficients. The 3D pure-gauge optical variation is separately
computed by the new v15.830 numerical photon/mirror/clock/event code.
First-order optical linearity => a pure diffeomorphism leaves the real
physical signal unchanged. Omitting spatial shear produces a false
differential much bigger than source grid/refinement error.
This is NOT a complete nonlinear/on-shell cosmological gauge theorem.
"""
import numpy as np
from k4_3d_diffeo_optical_v15_830 import arm,arms,pairs
physical=np.array([
 .00249919655+.000125688324j,
 .000417265262-.00000000002694j,
 .000470444542+.000027185473j,
 -.000477720493-.000027605448j,
 -.00103158740-.00000000001130j
])
pure=np.array([arm(u,d=.075,te=.08) for u in arms])
differential=lambda r:np.array([r[i]-r[j] for i,j in pairs])
delta=differential(pure)
shifted=physical+delta
assert np.max(abs(delta))<2e-10
assert np.max(abs(shifted-physical))<2e-10
noshear=np.array([arm(u,d=.075,te=.08,ignore_shear=True) for u in arms])
false_delta=differential(noshear)
assert np.max(abs(false_delta))>1e-4
print("AUDITED v15.818 physical five-channel Fourier coefficients:",physical)
print("PASS 3D gauge overlay: max physically anchored change:",
      np.max(abs(shifted-physical)))
print("FAIL if missing 3D shear: max spurious differential:",
      np.max(abs(false_delta)))
print("False-to-largest-physical ratio:",
      np.max(abs(false_delta))/np.max(abs(physical)))
print("SCOPE: fixed-gauge physical source at linear optical response; no generic all-order gauge proof")
