#!/usr/bin/env python3
"""Outward source-faithful raw near/tail Euclidean floors at the N~8000 split.

Same interval theorem as the audited N=4000 raw-tail certificate.

For the full raw remote principal block starting at the first parity mode:
  even-v: n>=8001 odd Fourier modes,
  odd-v : n>=8002 even Fourier modes,

pole-free
  alpha_N = log(N/4)-pi/2-2.05-beta_cusp(N)-beta_arch(N).

The even rank-one pole is positive. The odd rank-one pole is negative and
is charged by the same l2 tail formula as the N4000 theorem.

The returned RAW floor is before the mu=1 remote shift. Therefore
  D_nn - I >= raw_floor - 1
on any principal near subspace starting at the same mode.
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
    n=iv.mpf(N); pi=iv.pi
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

targets=[
 ("even-v",8001,False,iv.mpf("3.9800")),
 ("odd-v",8002,True, iv.mpf("3.9800")),
]
for sector,N,odd,target in targets:
    floor,cusp,arch,pole=one(N,odd)
    shifted=floor-1
    print("\n",sector)
    print("start =",N)
    print("cusp =",cusp)
    print("arch =",arch)
    print("odd pole loss =",pole)
    print("raw floor =",floor)
    print("mu=1 shifted floor =",shifted)
    if not (floor>target):
        raise RuntimeError((sector,"raw near floor failed",floor,target))
    if not (shifted>iv.mpf("2.98")):
        raise RuntimeError((sector,"shifted near floor failed",shifted))

print("\nPASS: raw source-faithful floors exceed 3.9800; mu=1 shifted near floors exceed 2.98 in both parities.")
