#!/usr/bin/env python3
"""Gravity v15.1265: combine archived nonzero-mode K4 local tidal field
(v15.1262) with homogeneous periodic Bianchi-I Maxwell-K4 response
(v15.1264), at precisely matched grid, source, time and normalization.

This is a COMPOSITION regression, not a new metric field equation.
The parent source files are loaded unchanged; no archive rewrite.
The k=0 periodic background is a chosen finite-box model, not the
unique gravitational response of an isolated Maxwell packet.
"""
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
NONZERO="k4_compact_maxwell_full_grid_mean_subtracted_riemann_v15_1262.py"
HOMOGENEOUS="k4_homogeneous_maxwell_bianchi_shear_v15_1264.py"

def load_nonzero():
    path=HERE/NONZERO
    raw=path.read_text(encoding="utf-8")
    needle="    return result\n"
    assert raw.count(needle)==1, "archived return structure changed; refuse silent patch"
    # Add arrays to returned result *in memory only*, after the archived
    # printed summary; this does NOT modify or overwrite the archived file.
    revised=raw.replace(needle,
        "    result['_Efield']=Er\n"
        "    result['_rho_field']=rho\n"
        "    return result\n")
    ns={"__name__":"_gravity_1262_in_memory","__file__":str(path)}
    exec(compile(revised,str(path),"exec"),ns)
    return ns["run"]

def load_homogeneous():
    path=HERE/HOMOGENEOUS
    ns={"__name__":"_gravity_1264_in_memory","__file__":str(path)}
    exec(compile(path.read_text(encoding="utf-8"),str(path),"exec"),ns)
    return ns["run"]

def run_pair(N,tf=1.08):
    nonzero=load_nonzero()(N=N,nt=9,tf=tf)
    zero=load_homogeneous()(N=N,nt=17,end=tf)
    E=nonzero["_Efield"]
    rho=nonzero["_rho_field"]
    background=np.diag(zero["homogeneous_tide"])
    total=E+background[:,:,None,None,None]
    energy_mean=float(np.mean(rho))
    mean_delta=energy_mean-zero["mean_conformal_energy"]
    assert abs(mean_delta)<2e-12, ("Maxwell means differ",mean_delta)
    a=9*rho/tf**4
    trace=np.trace(total,axis1=0,axis2=1)
    resid=np.max(np.abs(trace-a))
    expected_mean=9*energy_mean/tf**4
    assert abs(np.trace(background)-expected_mean)<2e-12
    assert resid<3e-12
    assert np.max(np.abs(total-total.swapaxes(0,1)))<3e-12
    center=total[:,:,N//2,N//2,N//2]
    full_mean=np.mean(total,axis=(2,3,4))
    assert np.max(np.abs(full_mean-background))<5e-12
    output={
        "N":N,"tau":tf,
        "Maxwell_mean":energy_mean,
        "homogeneous_tidal_diagonal":np.diag(background).tolist(),
        "center_total_tidal_diagonal":np.diag(center).tolist(),
        "center_total_tidal_matrix":center.tolist(),
        "center_Maxwell_energy":float(rho[N//2,N//2,N//2]),
        "full_trace_max_abs_error":float(resid),
        "mean_max_abs_error":float(np.max(np.abs(full_mean-background))),
        "homogeneous_mean_match_error":float(abs(mean_delta)),
    }
    print(output,flush=True)
    return output

if __name__=="__main__":
    runs=[run_pair(N) for N in (32,40,48)]
    assert all(r["full_trace_max_abs_error"]<3e-12 for r in runs)
    print("PASS matched 3D periodic-cell full electric-Riemann trace and homogeneous k0 completion")
    print("NOT certified: continuum convergence, full metric constraints, causal photon/mirror/clock, isolated source boundary")
