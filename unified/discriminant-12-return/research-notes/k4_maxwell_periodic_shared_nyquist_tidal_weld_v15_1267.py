#!/usr/bin/env python3
"""Gravity v15.1267: additive correction to v15.1266 Maxwell k0/nonzero
tidal composition. The original parent source files remain immutable.

The finite FFT initial electric spectrum is transverse-projected but that
projection is not automatically Hermitian on the self-conjugate Nyquist
planes. Remove those planes consistently BEFORE free Maxwell evolution
in both parent solvers. This preserves real fields and conserved Parseval
Maxwell energy, allowing strict homogeneous/nonzero energy matching.

Verified with equivalent independent local parents at N=32,40,48; original
committed-byte launcher remains an external Audit replay requirement.
"""
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
NONZERO=ROOT/"k4_compact_maxwell_full_grid_mean_subtracted_riemann_v15_1262.py"
HOM=ROOT/"k4_homogeneous_maxwell_bianchi_shear_v15_1264.py"

def load_nonzero():
    src=NONZERO.read_text(encoding="utf-8")
    anchor="    Eh-=n*np.einsum('i...,i...->...',n,Eh)"
    assert src.count(anchor)==1, "nonzero parent Gauss projection changed"
    src=src.replace(anchor,anchor+
        "\n    nyquist=np.any(np.abs(K)==N/2*2*pi/L,axis=0)"+
        "\n    Eh[:,nyquist]=0")
    marker="    return result\n"
    assert src.count(marker)==1
    src=src.replace(marker,
        "    result['_Efield']=Er\n"+
        "    result['_rho_field']=rho\n"+
        marker)
    space={"__name__":"_v1262_nyquist_in_memory","__file__":str(NONZERO)}
    exec(compile(src,str(NONZERO),"exec"),space)
    return space["run"]

def load_hom():
    src=HOM.read_text(encoding="utf-8")
    anchor="    h-=unit*np.einsum('i...,i...->...',unit,h)"
    assert src.count(anchor)==1, "homogeneous parent Gauss projection changed"
    src=src.replace(anchor,anchor+
        "\n    nyquist=np.any(np.abs(q)==N/2*2*pi/L,axis=0)"+
        "\n    h[:,nyquist]=0")
    space={"__name__":"_v1264_nyquist_in_memory","__file__":str(HOM)}
    exec(compile(src,str(HOM),"exec"),space)
    return space["run"]

def run_pair(N,tf=1.08):
    a=load_nonzero()(N=N,nt=9,tf=tf)
    b=load_hom()(N=N,nt=17,end=tf)
    field=a["_Efield"]; rho=a["_rho_field"]
    background=np.diag(b["homogeneous_tide"])
    total=field+background[:,:,None,None,None]
    delta=float(abs(np.mean(rho)-b["mean_conformal_energy"]))
    trace_err=float(np.max(abs(np.trace(total,axis1=0,axis2=1)-9*rho/tf**4)))
    mean_err=float(np.max(abs(np.mean(total,axis=(2,3,4))-background)))
    symmetry_err=float(np.max(abs(total-total.swapaxes(0,1))))
    assert delta<2e-12,(N,"mean Maxwell mismatch",delta)
    assert trace_err<3e-12,(N,"local Einstein trace",trace_err)
    assert mean_err<5e-12,(N,"mean tidal tensor",mean_err)
    assert symmetry_err<3e-12
    central=total[:,:,N//2,N//2,N//2]
    row={"N":N,"tau":tf,"rho_mean":float(rho.mean()),
         "rho_center":float(rho[N//2,N//2,N//2]),
         "central_tidal_diagonal":np.diag(central).tolist(),
         "mean_Maxwell_error":delta,"trace_error":trace_err,
         "mean_tidal_error":mean_err,"symmetry_error":symmetry_err}
    print(row,flush=True)
    return row

if __name__=="__main__":
    [run_pair(N) for N in (32,40,48)]
    print("PASS shared-Nyquist homogeneous/nonzero Maxwell-K4 tidal composition")
    print("OPEN full metric, independent constraints, continuum, causal optical probe")
