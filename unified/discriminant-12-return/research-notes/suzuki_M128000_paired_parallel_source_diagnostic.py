#!/usr/bin/env python3
"""Paired protected-range source diagnostic on the 128k->256k octave.

For each parity:
  D=F^T H^-1 F, c=F^T H^-1 r,
  v=D^+ c, a=S^-1 b,
  q_parallel=F(v-a).

Pairs even/odd octave coordinates by index and reports common/difference
norms. Binary64 diagnostic only; intended to reveal whether the source
difference collapses after exact Gram projection.
"""
from __future__ import annotations
import json
import numpy as np
import suzuki_M128000_M256000_reduced_feshbach_transport as red

R=128000

def one(sector):
    a=red.setup(sector,R)
    b2=red.setup(sector,2*R)
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
    v=np.linalg.pinv(D,rcond=1e-12)@c
    aa=np.linalg.lstsq(a["S"],a["b"],rcond=None)[0]
    w=v-aa
    qpar=F@w
    return {
      "qpar":qpar,
      "D":D,"c":c,"v":v,"a":aa,"w":w,
      "qpar_energy":float(qpar@qpar),
    }

def main():
    e=one("even-v"); o=one("odd-v")
    de=o["qpar"]-e["qpar"]
    sm=o["qpar"]+e["qpar"]
    ne=float(np.linalg.norm(e["qpar"]))
    no=float(np.linalg.norm(o["qpar"]))
    nd=float(np.linalg.norm(de))
    dot=float(e["qpar"]@o["qpar"])
    cos=dot/(ne*no)
    out={
      "qpar_even_norm":ne,
      "qpar_odd_norm":no,
      "qpar_even_energy":e["qpar_energy"],
      "qpar_odd_energy":o["qpar_energy"],
      "qpar_energy_difference_odd_minus_even":o["qpar_energy"]-e["qpar_energy"],
      "delta_qpar_norm":nd,
      "sum_qpar_norm":float(np.linalg.norm(sm)),
      "qpar_cosine":cos,
      "delta_qpar_max_abs":float(np.max(np.abs(de))),
      "delta_qpar_l1":float(np.sum(np.abs(de))),
      "delta_qpar_partial_sum_max":float(np.max(np.abs(np.cumsum(de)))),
      "guardrail":"binary64 protected-anchor diagnostic only"
    }
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
