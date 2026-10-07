#!/usr/bin/env python3
"""Pair the corrected-anchor pre-Gram normalized 64k->128k diagnostics.

Consumes the pure-JSON artifacts emitted by
suzuki_reduced_feshbach_gram_outward_budget.py for even-v and odd-v.

For each parity:
    Phi = sigma + tau^* (I-G)^-1 tau.

Then evaluates the two exact common-mode-preserving paired bounds from
v14.136.  This is a midpoint diagnostic: no outward uncertainty is added here.
No clipping, pseudoinverse, numerical-rank threshold, or protected S-D
subtraction is used.
"""
from __future__ import annotations
import argparse, json
import mpmath as mp

DPS=120


def mm(rows):
    return mp.matrix([[mp.mpf(x) for x in row] for row in rows])


def vv(xs):
    return mp.matrix([[mp.mpf(x)] for x in xs])


def norm2(v):
    return mp.sqrt(mp.fsum(abs(v[i])**2 for i in range(v.rows)))


def spectral_norm_sym(A):
    vals,_=mp.eigsy((A+A.T)/2)
    return max(abs(vals[0]),abs(vals[vals.rows-1]))


def load(path):
    row=json.load(open(path))
    p=row["pregram_normalized"]
    if p is None:
        raise RuntimeError(("missing pregram payload",path))
    G=mm(p["G_pregram_matrix"])
    tau=vv(p["tau_vector"])
    sigma=mp.mpf(p["sigma"])
    vals,_=mp.eigsy((G+G.T)/2)
    if vals[vals.rows-1] >= 1:
        raise RuntimeError(("I-G not positive",path,mp.nstr(vals[vals.rows-1],50)))
    R=(mp.eye(6)-G)**-1
    Phi=sigma+(tau.T*R*tau)[0]
    return dict(row=row,G=G,tau=tau,sigma=sigma,R=R,Phi=Phi,vals=vals)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--even",required=True)
    ap.add_argument("--odd",required=True)
    a=ap.parse_args()

    with mp.workdps(DPS):
        e=load(a.even)
        o=load(a.odd)

        dG=o["G"]-e["G"]
        dt=o["tau"]-e["tau"]
        ds=o["sigma"]-e["sigma"]
        ng=spectral_norm_sym(dG)
        nt=norm2(dt)

        Re=e["R"]; Ro=o["R"]
        te=e["tau"]; to=o["tau"]

        # v14.136 even-reference bound.
        bound_e=(
            abs(ds)
            + ng*norm2(Ro*to)*norm2(Re*to)
            + nt*(norm2(Re*to)+norm2(Re*te))
        )
        # v14.136 odd-reference companion.
        bound_o=(
            abs(ds)
            + ng*norm2(Ro*te)*norm2(Re*te)
            + nt*(norm2(Ro*to)+norm2(Ro*te))
        )
        bound=min(bound_e,bound_o)
        actual=o["Phi"]-e["Phi"]

        out={
          "R":64000,"R2":128000,
          "even_increment":mp.nstr(e["Phi"],70),
          "odd_increment":mp.nstr(o["Phi"],70),
          "odd_minus_even_increment":mp.nstr(actual,70),
          "abs_paired_increment":mp.nstr(abs(actual),70),
          "delta_sigma":mp.nstr(ds,70),
          "delta_G_spectral_norm":mp.nstr(ng,70),
          "delta_tau_l2":mp.nstr(nt,70),
          "paired_bound_even_reference":mp.nstr(bound_e,70),
          "paired_bound_odd_reference":mp.nstr(bound_o,70),
          "paired_bound_min":mp.nstr(bound,70),
          "bound_minus_abs_actual":mp.nstr(bound-abs(actual),70),
          "bound_over_abs_actual":mp.nstr(bound/abs(actual),50),
          "even_G_min":mp.nstr(e["vals"][0],50),
          "even_G_max":mp.nstr(e["vals"][e["vals"].rows-1],50),
          "odd_G_min":mp.nstr(o["vals"][0],50),
          "odd_G_max":mp.nstr(o["vals"][o["vals"].rows-1],50),
          "guardrail":(
            "pre-Gram long-double midpoint pair only; exact algebra and "
            "common-mode bound, but theorem use still requires outward "
            "propagation through the normalized large-vector construction"
          ),
        }
        print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
