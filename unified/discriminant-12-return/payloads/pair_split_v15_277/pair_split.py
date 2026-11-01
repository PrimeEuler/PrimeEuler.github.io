#!/usr/bin/env python3
"""
Testing the emerging pair-split generalization:
observables of an opposed pair split under the EXCHANGE (u <-> v)
into even (kinematics: invariants, shell, energy) and odd (dynamics:
momentum, rapidity, reaction); rest = the fixed locus u = v.
Instances: (a) pair observables under swap (exact); (b) the Unruh
pair -- Minkowski vacuum as an exchange-symmetric two-wedge state
whose one-sided reduction is exactly thermal.
"""
import numpy as np
from fractions import Fraction as Fr

print("(a) exchange parity of the pair observables (exact):")
n, k = Fr(6), Fr(4)   # a generic crossing
def obs(nn, kk):
    return {"uv = m^2": nn * kk, "AM = E": (nn + kk) / 2,
            "offset = p": (nn - kk) / 2,
            "curv net (1/k - 1/n)": Fr(1, 1) / kk - Fr(1, 1) / nn}
a, b = obs(n, k), obs(k, n)
for key in a:
    par = "EVEN" if a[key] == b[key] else ("ODD " if a[key] == -b[key] else "????")
    print(f"    {key:22s} {str(a[key]):>6s} -> swap -> {str(b[key]):>6s}   {par}")
print("    rapidity psi = (1/2) ln(n/k): "
      f"{0.5*np.log(6/4):+.4f} -> {0.5*np.log(4/6):+.4f}   ODD")
print("    phase doublet (e^{+i phi}, e^{-i phi}): exchanged as a pair")
print("  -> invariants even; momentum, rapidity, net curvature odd;")
print("     the fixed locus n = k (p = psi = net curvature = 0) is rest.")

print("\n(b) Unruh pair: |0_M> = sqrt(1-t^2) sum_n t^n |n_L, n_R>, t = tanh r")
for t in (0.3, 0.6, 0.9):
    nn = np.arange(0, 400)
    p_n = (1 - t**2) * t**(2 * nn)
    ratio = p_n[1:13] / p_n[:12]
    print(f"    t={t}: reduced one-wedge spectrum geometric: "
          f"ratios constant = {np.allclose(ratio, t**2)} (ratio {ratio[0]:.3f}); "
          f"full state L<->R symmetric by construction of the pair sum;")
    Ebar = t**2 / (1 - t**2)
    print(f"          mean occupation {np.sum(nn*p_n):.4f} = "
          f"t^2/(1-t^2) = {Ebar:.4f} -- a thermal (Bose) spectrum: balance")
print("          in the pair (pure, symmetric vacuum); heat in the part")
print("          (tracing one wedge). T = a/(2 pi) in natural units.")
