#!/usr/bin/env python3
"""Fail-closed acceptance budget for the N=4000 -> M=8000 near-shell interval.

Midpoint arch-200 shell increments:
  eta_e = C_Ne/C_Me - 1
  eta_o = C_No/C_Mo - 1.

The final outward width is split into:
  (1) represented finite-solve/source-energy uncertainty at N and M;
  (2) exact-source representation uncertainty of the common-mode ratio.

For (1), impose the deliberately loose public target
  |log C_exact,rep - log C_mid| <= -log(1-RCAP),
with RCAP=1e-7 at each cutoff/parity.  The observed correlated residual-energy
fractions are <=3.71e-10, so this target has >250x headroom at the worst gate.

For (2), consume the common-mode arch-200 source sensitivity diagnostic:
  even  total log-ratio bound 5.671705860025666e-10
  odd   total log-ratio bound 5.965770715658009e-15.
Those gradients use refined trial source solutions.  Charge trial-vs-exact
gradient transport using the same public energy-defect RCAP and the certified
relative operator radii theta:
  correction <= theta*(2 sqrt(r)+3r) at each cutoff.
Sum N and M.

Convert log-ratio radius L to eta absolute radius:
  |delta eta| <= (1+eta)*(exp(L)-1).

The parity-difference near-shell half-width is the sum of the two sector
absolute radii.  Sandbox v14.047 asks for <5e-7 for the demanding cumulative
sign certification.
"""
from decimal import Decimal,getcontext
getcontext().prec=80
D=Decimal

CN={
 "even-v":D("7.577300593508684046987061407977088062924610221588719868051183884612194e-30"),
 "odd-v":D("2.18452398382894726279272688336674430821848968233438745876200387493459e-25"),
}
CM={
 "even-v":D("7.527204146090199002420215905103784264066292950197906558714717192133483e-30"),
 "odd-v":D("2.170029381845773125826862298995949154842867652129568694828364419654003e-25"),
}
SOURCE_LOG={
 "even-v":D("5.671705860025666e-10"),
 "odd-v":D("5.965770715658009e-15"),
}
THETA={
 "even-v":D("3.899270146651301e-6"),
 "odd-v":D("9.692586810135521e-11"),
}
RCAP=D("1e-7")
SANDBOX_NEAR_HALF=D("5e-7")

def expD(x):
    # Decimal exp is available at current context.
    return x.exp()

def ln1m(r):
    return -(D(1)-r).ln()

def one(sector):
    eta=CN[sector]/CM[sector]-D(1)
    # Two cutoffs, each with public relative source-energy/capacity defect RCAP.
    solve_log=D(2)*ln1m(RCAP)
    # Trial-gradient transport at N and M.
    root=RCAP.sqrt()
    grad_transport=D(2)*THETA[sector]*(D(2)*root+D(3)*RCAP)
    total_log=solve_log+SOURCE_LOG[sector]+grad_transport
    eta_rad=(D(1)+eta)*(expD(total_log)-D(1))
    return {
      "sector":sector,
      "eta_mid":str(eta),
      "solve_log_radius":str(solve_log),
      "source_log_radius":str(SOURCE_LOG[sector]),
      "trial_gradient_transport_log_radius":str(grad_transport),
      "total_log_radius":str(total_log),
      "eta_absolute_radius":str(eta_rad),
      "observed_worst_residual_energy_fraction":{
        "even-v":"3.7006573350354208e-10",
        "odd-v":"6.490947404149507e-11",
      }[sector],
      "public_RCAP":str(RCAP),
    }

def main():
    rows=[one("even-v"),one("odd-v")]
    near_mid=D(rows[1]["eta_mid"])-D(rows[0]["eta_mid"])
    half=D(rows[0]["eta_absolute_radius"])+D(rows[1]["eta_absolute_radius"])
    print("near parity-difference midpoint =",near_mid)
    for r in rows:
        print("\n",r["sector"])
        for k,v in r.items():
            if k!="sector": print(k,"=",v)
    print("\nnear parity-difference half-width target =",half)
    print("Sandbox demanding allowance =",SANDBOX_NEAR_HALF)
    if not half < SANDBOX_NEAR_HALF:
        raise RuntimeError(("near-shell width target failed",half))
    print("PASS: public RCAP=1e-7 is sufficient for v14.047 near-shell width.")
    print("GUARDRAIL: theorem promotion requires outward certification of RCAP at all four finite solves.")

if __name__=="__main__":
    main()
