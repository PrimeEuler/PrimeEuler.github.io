#!/usr/bin/env python3
"""Convergence sweep: chi_-4 Zeeman carrier vs breakpoint Fredholm control.

Extends v13.614/Round-65 from one baseline point to a two-axis refinement:
  (i) Zeeman spin j at fixed breakpoint discretization;
 (ii) breakpoint interpolation degree and panel quadrature order at fixed j.

All comparisons use the same A and the same lambda supplied by each Zeeman
finite pair.  The observable is the projective characteristic W(z)/W(z_ref).
No beta-zero matching is performed here.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("pb",HERE/"suzuki_chi4_phase_and_breakpoint_comparison.py")
pb=importlib.util.module_from_spec(s); s.loader.exec_module(pb)
fc=pb.fc

ZGRID=(1.0,3.0,6.0,10.0)
ZREF=0.5


def projective_zeeman(d,theta,z):
    return fc.characteristic(d,z,theta)/fc.characteristic(d,ZREF,theta)


def projective_bp(b,theta,z):
    return pb.bp_char(b,z,theta)/pb.bp_char(b,ZREF,theta)


def one(A,two_j,degree,qorder):
    d=fc.deficiency_data(two_j,A)
    theta,alpha,rres=pb.derived_theta(d)
    b=pb.solve_breakpoint(A,d["lam"],degree,qorder)
    diffs=[]
    for z in ZGRID:
        diffs.append(abs(projective_zeeman(d,theta,z)-projective_bp(b,theta,z)))
    return dict(A=A,j=two_j/2,degree=degree,qorder=qorder,lam=d["lam"],
                alpha=alpha,reflection_res=rres,cond_e=b["cond_e"],cond_o=b["cond_o"],
                res_e=b["res_e"],res_o=b["res_o"],diffs=diffs,maxdiff=max(diffs))


def main():
    for A in (1.5,2.0,2.5):
        print("\n=== A",A,"spin refinement; BP degree=10 qorder=8 ===")
        for two_j in (12,20,30,40):
            r=one(A,two_j,10,8)
            print("j=%4.1f lam=% .6g maxdiff=% .6e diffs="% (r["j"],r["lam"],r["maxdiff"]),
                  " ".join("%.6e"%x for x in r["diffs"]))
        print("\n=== A",A,"BP refinement at j=10 ===")
        for degree,qorder in ((6,6),(8,8),(10,8),(12,10),(14,12)):
            r=one(A,20,degree,qorder)
            print("deg=%2d q=%2d cond=(%.3e,%.3e) res=(%.2e,%.2e) maxdiff=%.6e diffs="%(
                degree,qorder,r["cond_e"],r["cond_o"],r["res_e"],r["res_o"],r["maxdiff"]),
                " ".join("%.6e"%x for x in r["diffs"]))


if __name__=="__main__":
    main()
