#!/usr/bin/env python3
"""High-precision protected-anchor transport through 64k->128k->256k.

Consumes a committed/exported 64k LDDD protected anchor:
    S, b, h, Sinv_b
and regenerates the stable reduced Gram data D,c,d for the 64k->128k and
128k->256k octaves using the validated reduced-Feshbach producer.

All 6x6 algebra is performed with mpmath at high precision.  This script is
a consumer/diagnostic until the anchor payload and Gram radii are promoted.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

import suzuki_M128000_M256000_reduced_feshbach_transport as red

DPS=120

def mp_mat(rows):
    return mp.matrix([[mp.mpf(str(x)) for x in row] for row in rows])

def mp_vec(xs):
    return mp.matrix([[mp.mpf(str(x))] for x in xs])

def reduced_payload(sector,R):
    R2=2*R
    a=red.setup(sector,R)
    b2=red.setup(sector,R2)
    n1=len(a["modes"])

    Wpad=np.zeros((len(b2["modes"]),6),dtype=float)
    Wpad[:n1,:]=a["W"]
    qpad=np.zeros(len(b2["modes"]),dtype=float)
    qpad[:n1]=a["q"]

    F=b2["raw"](Wpad)[n1:,:]
    r=b2["g"][n1:]-b2["raw"](qpad)[n1:]
    X=b2["Y"][n1:,:]
    y=b2["q"][n1:]

    D=F.T@X; D=(D+D.T)/2
    c=F.T@y
    d=float(r@y)
    return D,c,d

def scalar(x):
    return x[0] if hasattr(x,"__len__") else x

def step(S,b,h,D,c,d):
    a=mp.lu_solve(S,b)
    K=h+(b.T*a)[0]

    Dm=mp_mat(D.tolist())
    cm=mp_vec(c.tolist())
    dm=mp.mpf(str(d))

    sigma=dm-2*(a.T*cm)[0]+(a.T*Dm*a)[0]
    t=cm-Dm*a
    S2=S-Dm
    b2=b-cm
    h2=h+dm
    z=mp.lu_solve(S2,t)
    parallel=(t.T*z)[0]
    delta=sigma+parallel

    a2=mp.lu_solve(S2,b2)
    K2=h2+(b2.T*a2)[0]
    vals,_=mp.eigsy((S2+S2.T)/2)

    return {
      "S":S2,"b":b2,"h":h2,"a":a2,
      "K_old":K,"K_new":K2,"delta_formula":delta,
      "delta_direct":K2-K,
      "sigma":sigma,"parallel":parallel,"t":t,
      "S_min":vals[0],"S_max":vals[-1],
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--anchor",required=True)
    args=ap.parse_args()

    data=json.loads(Path(args.anchor).read_text())
    with mp.workdps(DPS):
        S=mp_mat(data["S"])
        b=mp_vec(data["b"])
        h=mp.mpf(data["h"])

        D1,c1,d1=reduced_payload(args.sector,64000)
        r1=step(S,b,h,D1,c1,d1)

        D2,c2,d2=reduced_payload(args.sector,128000)
        r2=step(r1["S"],r1["b"],r1["h"],D2,c2,d2)

        out={
          "sector":args.sector,
          "anchor_K":mp.nstr(r1["K_old"],70),
          "K_128k":mp.nstr(r1["K_new"],70),
          "delta_64_128":mp.nstr(r1["delta_direct"],70),
          "sigma_64_128":mp.nstr(r1["sigma"],70),
          "parallel_64_128":mp.nstr(r1["parallel"],70),
          "S128_min":mp.nstr(r1["S_min"],70),
          "K_256k":mp.nstr(r2["K_new"],70),
          "delta_128_256":mp.nstr(r2["delta_direct"],70),
          "sigma_128_256":mp.nstr(r2["sigma"],70),
          "parallel_128_256":mp.nstr(r2["parallel"],70),
          "S256_min":mp.nstr(r2["S_min"],70),
          "formula_check_64_128":mp.nstr(abs(r1["delta_formula"]-r1["delta_direct"]),30),
          "formula_check_128_256":mp.nstr(abs(r2["delta_formula"]-r2["delta_direct"]),30),
          "guardrail":"high-precision 6x6 consumer; Gram inputs still midpoint binary64 until outward radii are promoted"
        }
        print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
