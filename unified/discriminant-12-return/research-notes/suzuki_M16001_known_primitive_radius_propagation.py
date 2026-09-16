#!/usr/bin/env python3
"""Propagate already-audited primitive entry radii into the 7991x10 residual.

This is deliberately conditional/fail-closed: it closes only the primitive
arithmetic pieces already derived by v13.521, the pole-FC transcript, and the
v13.526 Frobenius stage.  Diagonal/source/X payload conversion remain separate.
No empirical discrepancy or safety multiplier is used.
"""
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import finite_solve_stop
from suzuki_M16001_pole_FC_primitive_outward_transcript import scan as pole_scan
LD=np.longdouble; U=LD(2)**LD(-64)
def gamma(k):
    ku=LD(k)*U; return ku/(1-ku)
# Audited outward maxima from v13.521 / External Audit Round 42.
RHO_FF_DISP=LD('9.022982959826541e-16')
RHO_FC_DISP=LD('4.848047102922417e-19')

def main():
    _,_,_,X,_=finite_solve_stop(); X=np.asarray(X,dtype=LD)
    N,NRHS=X.shape
    ps=pole_scan()
    rho_pole=LD(ps['max_pole_rad'])
    rho_pole_add=LD(ps['max_add_rad'])
    rho_fc=RHO_FC_DISP+rho_pole+rho_pole_add
    col_l1=np.sum(np.abs(X),axis=0,dtype=LD)
    # Off-diagonal FF coefficient errors contribute rho*sum_{j != i}|X_jr|.
    # Using full column l1 is conservative and avoids a subtraction rounding step.
    E=np.empty((N,NRHS),dtype=LD)
    for r in range(NRHS):
        E[:,r]=RHO_FF_DISP*col_l1[r]+rho_fc
    # Charge the two scalar products/addition used to form this propagated bound.
    form=gamma(1)*(RHO_FF_DISP*col_l1[None,:]+rho_fc)
    E+=form
    sq=np.sum(E*E,dtype=LD)
    # Charge square products and the N*NRHS accumulation, then outward sqrt.
    sq_hi=sq+gamma(1)*sq+gamma(N*NRHS)*sq
    frob=np.sqrt(sq_hi)
    frob_hi=np.nextafter(frob,LD(np.inf),dtype=LD)
    print('N, NRHS =',N,NRHS)
    print('max column l1(X) =',np.max(col_l1))
    print('rho_FF_disp =',RHO_FF_DISP)
    print('rho_FC_disp =',RHO_FC_DISP)
    print('rho_pole =',rho_pole)
    print('rho_pole_add =',rho_pole_add)
    print('combined FC primitive arithmetic radius =',rho_fc)
    print('max residual-entry primitive increment =',np.max(E))
    print('OUTWARD known-primitive Frobenius increment <=',frob_hi)
    print('FAIL-CLOSED remainder: diag_payload_conversion, source_payload_conversion, X_payload_conversion')
if __name__=='__main__': main()
