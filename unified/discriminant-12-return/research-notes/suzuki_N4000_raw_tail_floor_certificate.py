#!/usr/bin/env python3
"""Outward source-faithful raw-tail Euclidean floors at the N=4000 split.

This is the v13.391 coercivity formula evaluated at the present remote split.

even-v remote modes start at n=4001.
odd-v remote modes start at n=4002.

Pole-free:
  alpha_N =
    log(N/4) - pi/2 - 2.05
    - beta_cusp(N) - beta_arch(N).

The even rank-one pole is positive and costs nothing.
The odd rank-one pole is negative and is bounded by
  32 sinh(1/2)^2/pi^2 * s2(N).

All arithmetic is mpmath interval arithmetic.
"""
from __future__ import annotations

import mpmath as mp

iv=mp.iv
iv.dps=80


def zeta3_interval(M=20000):
    s=iv.mpf(0)
    for k in range(1,M+1):
        x=iv.mpf(k)
        s += 1/x**3
    lo=1/(2*iv.mpf(M+1)**2)
    hi=1/(2*iv.mpf(M)**2)
    return iv.mpf([s.a+lo.a,s.b+hi.b])


def one(N:int,odd:bool):
    n=iv.mpf(N)
    pi=iv.pi

    s2=n**-2+1/(2*n)
    c=2/pi**3+6/pi**4
    aa=2*c/pi
    cd=2/pi**2+2/pi**3+2/pi**4+6/pi**5

    cusp=(
        2/pi**2*s2
        +2*aa*iv.sqrt(pi**2/12*(n**-6+1/(10*n**5)))
        +cd*iv.sqrt(n**-4+1/(6*n**3))
    )

    q=2/pi
    z3=zeta3_interval()
    r4=z3*q**3/(4*(1-q)**3)
    cr=iv.mpf(19)/12+4*r4
    arch=4*cr/pi**2*s2

    floor=iv.log(n/4)-pi/2-iv.mpf("2.05")-cusp-arch
    pole=iv.mpf(0)
    if odd:
        sh=(iv.exp(iv.mpf(".5"))-iv.exp(-iv.mpf(".5")))/2
        pole=32*sh**2/pi**2*s2
        floor-=pole

    return floor,cusp,arch,pole


for sector,N,odd,target in [
    ("even-v",4001,False,"3.2867"),
    ("odd-v",4002,True,"3.2868"),
]:
    floor,cusp,arch,pole=one(N,odd)
    print("\n",sector)
    print("start =",N)
    print("cusp =",cusp)
    print("arch =",arch)
    print("odd pole loss =",pole)
    print("raw floor =",floor)
    if not (floor > iv.mpf(target)):
        raise RuntimeError((sector,"raw tail floor failed",floor,target))

print("\nPASS: source-faithful raw remote floors exceed 3.2867 even and 3.2868 odd.")
