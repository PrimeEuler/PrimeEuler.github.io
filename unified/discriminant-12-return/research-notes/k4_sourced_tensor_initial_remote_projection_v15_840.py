#!/usr/bin/env python3
"""Gravity v15.840: exact initial TT-sector remote-source acceleration trap.

v15.838's 3D C7 compact canonical scalar stress S_ij=grad_i chi grad_j chi
is locally zero at receiver but its spatial TT projection is nonzero.
At tau=1, physical anisotropic stress Pi_TT=3*S_TT (a^-2=3).
Original K4 sourced tensor equation in each TT Cartesian component:
 gamma_ddot + 3 gamma_dot/tau + (3k^2+8eta/3)gamma/tau^2 = -2 Pi_TT.
For initial propagating gamma=gamma_dot=0, the *isolated sector* tensor
electric Riemann component -(gamma_ddot+2 gamma_dot/tau)/2 = Pi_TT.
This nonzero value at a remote receiver is a constraint/projector
initialization artifact in an incomplete SVT calculation, NOT evidence
of physical superluminal curvature propagation. The full constrained
Einstein+solid initial data are not solved by this script.
"""
import sympy as s
import numpy as np
from k4_compact_tt_projector_remote_v15_838 import compute

tau,beta,P=s.symbols('tau beta Pi',positive=True,real=True)
gamma,gdot=s.symbols('gamma gamma_dot')
gdd=-3*gdot/tau-beta*gamma/tau**2-2*P
R=s.simplify(-(gdd+2*gdot/tau)/2)
assert s.simplify(R.subs({gamma:0,gdot:0})-P)==0
# The continuum physical canonical stress in an orthonormal spatial
# basis is a^-2 grad chi grad chi, with a(1)=1/sqrt(3).
vals=[]
for n in (96,112,128):
    raw_norm,raw_TT=compute(n)
    Pi_TT=3*raw_TT
    tensor_R_at_initial=Pi_TT # conditional zero dynamical tensor IC
    assert np.max(abs(np.trace(Pi_TT)))<1e-10
    assert abs(np.linalg.norm(tensor_R_at_initial)-3*raw_norm)<1e-13
    assert np.linalg.norm(tensor_R_at_initial)>0.004
    vals.append(np.linalg.norm(tensor_R_at_initial))
    print('N',n,'local raw stress zero, isolated sourced TT electric'
          ' Riemann norm at remote receiver',vals[-1])
assert max(vals)-min(vals)<1.5e-6
print('PASS: exact sourced tensor equation and conditional remote projection')
print('NEGATIVE: isolated TT branch is NOT full constraint-completed local Riemann')
print('OPEN: solve full Einstein-solid constraints with matched exterior data')
