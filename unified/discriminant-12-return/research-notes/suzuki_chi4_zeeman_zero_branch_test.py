#!/usr/bin/env python3
"""First falsifiable chi_-4 zero-branch test for the Zeeman Suzuki prototype.

Independently computes critical-line zeros of beta(s)=L(s,chi_-4), then locates
real zeros of the finite theta=pi characteristic from
suzuki_chi4_zeeman_finite_characteristic.py.

The experiment deliberately reports ALL finite characteristic roots in a fixed
window and repeats across A.  It does not nearest-neighbour rematch roots to
beta zeros at each resolution.  This exposes box/interval roots whose density
is controlled by A.

Status: numerical diagnostic, not a zero-convergence theorem.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    "fc",HERE/"suzuki_chi4_zeeman_finite_characteristic.py")
fc=importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)


def beta_completed(t, dps=50):
    with mp.workdps(dps):
        s=mp.mpf("0.5")+1j*mp.mpf(t)
        L=mp.dirichlet(s,[0,1,0,-1])
        return (4/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)*L


def beta_zeros(n=8,zmax=30,step=0.05):
    out=[]; a=mp.mpf("0"); fa=mp.re(beta_completed(a))
    k=1
    while float(a)<zmax and len(out)<n:
        b=mp.mpf(k)*step; fb=mp.re(beta_completed(b))
        if fa*fb<0:
            r=mp.findroot(lambda x: mp.re(beta_completed(x)),(a,b))
            if not out or abs(r-out[-1])>mp.mpf("1e-30"): out.append(r)
        a,fa=b,fb; k+=1
    return out


def wreal(data,z):
    # Reflection at theta=pi makes W purely imaginary on real z in this gauge.
    return float(np.imag(fc.characteristic(data,float(z),theta=np.pi)))


def characteristic_roots(data,zmax=30,step=0.02):
    zs=np.arange(1e-6,zmax+step,step)
    fs=np.array([wreal(data,z) for z in zs])
    roots=[]
    for a,b,fa,fb in zip(zs[:-1],zs[1:],fs[:-1],fs[1:]):
        if fa==0 or fa*fb<0:
            r=brentq(lambda z:wreal(data,z),a,b,xtol=1e-12,rtol=1e-12)
            if not roots or abs(r-roots[-1])>1e-7: roots.append(r)
    return roots


def run():
    bz=beta_zeros()
    print("beta critical-line zeros:")
    print(" ".join(f"{float(z):.12f}" for z in bz))
    print()
    for A in (1.5,2.0,2.5):
        print("A =",A)
        for two_j in (12,20,30,40):
            d=fc.deficiency_data(two_j,A)
            rr=characteristic_roots(d,zmax=30)
            print("j=%4.1f first12="% (two_j/2),
                  " ".join(f"{z:.6f}" for z in rr[:12]))
        print()


if __name__=="__main__":
    run()
