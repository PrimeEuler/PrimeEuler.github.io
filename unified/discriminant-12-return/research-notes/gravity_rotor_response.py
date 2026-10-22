#!/usr/bin/env python3
"""
Gravity rotor response gate for the Cone project.

Keep rank-1 and rank-2 rotor channels in one consistent 3-D rigid-rotor
model, compare them with the older planar-pendulum model, and derive the
G-free coupling-ratio observable. No value of G is inserted or inferred.
"""
from fractions import Fraction
from math import sqrt
import numpy as np

def c_up_sq(j, m=0):
    return Fraction((j + 1)**2 - m*m, (2*j + 1)*(2*j + 3))

def c_dn_sq(j, m=0):
    if j == 0:
        return Fraction(0, 1)
    return Fraction(j*j - m*m, (2*j - 1)*(2*j + 1))

def rank2_diag(j, m=0):
    if j == 0:
        return Fraction(0, 1)
    return Fraction(j*(j + 1) - 3*m*m, (2*j - 1)*(2*j + 3))

def rank1_static_second_order(j, m=0):
    # delta epsilon = beta1^2 S_jm + O(beta1^4)
    if j == 0:
        return -c_up_sq(0, 0)/2
    return c_dn_sq(j, m)/(2*j) - c_up_sq(j, m)/(2*(j + 1))

def w(j):
    return (j + 1)/sqrt((2*j + 1)*(2*j + 3))

def v(j):
    # <j+2,0|P2|j,0>
    return 1.5*w(j)*w(j + 1)

def spherical_m0_levels(beta, jmax=240, nlevels=6):
    H = np.diag([j*(j + 1) for j in range(jmax + 1)]).astype(float)
    for j in range(jmax):
        H[j, j + 1] = H[j + 1, j] = -beta*w(j)
    return np.linalg.eigvalsh(H)[:nlevels]

def planar_levels(beta, nmax=120, nlevels=6):
    ns = np.arange(-nmax, nmax + 1)
    H = np.diag(ns.astype(float)**2)
    for k in range(len(ns) - 1):
        H[k, k + 1] = H[k + 1, k] = -beta/2.0
    return np.linalg.eigvalsh(H)[:nlevels]

def xi_power_law(p):
    # Phi=-A/R^p => Xi=[1-R Phi''/Phi']/3=(p+2)/3
    return Fraction(p + 2, 3)

print("=== A. 3-D rigid-rotor identities ===")
for j in range(1, 7):
    d = rank2_diag(j, 0)
    S = rank1_static_second_order(j, 0)
    assert d == 2*j*(j + 1)*S
    print(f"j={j}: d_j={d}  S_j={S}  residual={d-2*j*(j+1)*S}")

print("\nGeneral-m spot checks:")
for j, m in [(1,1),(2,1),(2,2),(3,1),(4,2)]:
    d = rank2_diag(j, m)
    S = rank1_static_second_order(j, m)
    assert d == 2*j*(j + 1)*S
    print(f"(j,m)=({j},{m}): d={d}, S={S}")

print("\nRank-2 direct transition factorization:")
for j in range(6):
    ratio = v(j)/(w(j)*w(j + 1))
    assert abs(ratio - 1.5) < 2e-15
    print(f"j={j}: v_j/(w_j w_j+1)={ratio:.15f}")

print("\n=== B. planar-vs-spherical separation ===")
print("beta=0 planar:   ", planar_levels(0.0))
print("beta=0 spherical:", spherical_m0_levels(0.0))
for beta in (1.0, 64.0, 256.0):
    ep = planar_levels(beta, nlevels=4)
    es = spherical_m0_levels(beta, nlevels=4)
    print(f"\nbeta={beta:g}")
    print("  planar   :", np.array2string(ep, precision=9))
    print("  spherical:", np.array2string(es, precision=9))
    if beta >= 64:
        print("  planar first spacing / sqrt(2 beta) =",
              (ep[1]-ep[0])/sqrt(2*beta))
        print("  spherical first spacing / [2 sqrt(2 beta)] =",
              (es[1]-es[0])/(2*sqrt(2*beta)))

print("\n=== C. G-free field-shape observable ===")
print("Xi=(M l R/q)(beta2/beta1)=[1-R Phi''/Phi']/3")
for p in (0,1,2,3):
    print(f"Phi ~ -A/R^{p}: Xi={xi_power_law(p)}")
assert xi_power_law(1) == 1
print("Newton 1/R: Xi=1 exactly; amplitude A cancels.")

print("\nVERDICT")
print("rank-1/rank-2 response identities are standard SO(3) rotor algebra;")
print("the old Mathieu spectrum is a separate planar model;")
print("Xi is dimensionless and G-free but is the standard field-slope/gradiometric ratio.")