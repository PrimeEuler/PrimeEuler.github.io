#!/usr/bin/env python3
"""Gravity v15.1153: full Fermi-Riemann five-helicity bicone torque time series.

Reuses the EXACT archived compact canonical physical-source and five-mode
solver of v15.818, without changing its stress, background, normalization,
initial data or field equations. See v15.787 for full local Riemann.
This is a local initial-value Fourier mode benchmark, NOT calibrated SI
gravity, remote retarded detection or a new K4-minus-GR signal.
"""
import sys
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline
sys.path.insert(0,str(Path(__file__).resolve().parent))
from k4_compact_five_helicity_optical_v15_818 import source_and_modes

def fermi_curvature(hist, times):
    t=hist[:,0].real
    phi,psi,ve,vb,tp,tx=[CubicSpline(t,hist[:,i]) for i in range(1,7)]
    k=np.sqrt(5.)
    out=[]
    for T in times:
        a=T/np.sqrt(3.)
        # v15.787: scalar, 2 transverse vector components, 2 TT.
        S=-5*phi(T)/a**2
        Ve=-1j*k*(ve(T,1)+ve(T)/T)/(2*a)
        Vb=-1j*k*(vb(T,1)+vb(T)/T)/(2*a)
        Tp=-.5*(tp(T,2)+2*tp(T,1)/T)
        Tx=-.5*(tx(T,2)+2*tx(T,1)/T)
        out.append([S,Ve,Vb,Tp,Tx])
    return np.array(out)

M=np.array([[0,-1,0,0,0],
            [0,0,-1,0,0],
            [0,0,0,0,-1],
            [0,0,0,-1,0],
            [-.5,0,0,.5,0]])
def gate():
    times=np.array([1.12,1.20,1.28])
    assert np.isclose(np.linalg.det(M),.5)
    h48=source_and_modes(48,41)
    h64=source_and_modes(64,61)
    c48=fermi_curvature(h48,times)
    c64=fermi_curvature(h64,times)
    s48=c48@M.T
    s64=c64@M.T
    err=np.max(np.abs(s48-s64))
    assert err<1.5e-4,err
    assert np.min(np.abs(c64))>1e-3
    assert np.max(abs(M.T@np.linalg.inv(M.T)-np.eye(5)))<1e-12
    assert np.max(abs((s64@np.linalg.inv(M).T)-c64))<1e-11
    print("Times",times)
    print("Five sourced physical full-Riemann components S,Ve,Vb,T+,Tx")
    print(np.round(c64.real,7))
    print("Five calibrated-orientation torque coefficients (per DeltaQ)")
    print(np.round(s64.real,7))
    print("Max two-resolution absolute torque discrepancy",err)
    print("Max two-resolution relative torque discrepancy",err/np.max(abs(s64)))
    print("PASS source-first K4 five-helicity local full-Riemann bicone tomography")
    print("MATCHED-ACTION NULL: identical Einstein-Hilbert+same-solid apparatus")
    print("LIMIT: time-spline second derivatives; not five SI tidal sources")
if __name__=="__main__":
    gate()
