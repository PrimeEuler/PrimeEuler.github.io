#!/usr/bin/env python3
"""Exact accelerated representation for the archimedean sine sequence H_n.

Let

  h(t)=exp(-t/2)/(1-exp(-2t))-1/(2t),
  H_n=int_0^2 h(t) sin(n*pi*t/2) dt,

for odd n and b=n*pi/2.  Expand

  exp(-t/2)/(1-exp(-2t)) = sum_{k>=0} exp(-(2k+1/2)t).

The sine-weight makes termwise integration absolutely summable, and because
sin(n*pi)=0, cos(n*pi)=-1,

  int_0^2 exp(-a t) sin(b t) dt
    = b(1+exp(-2a))/(a^2+b^2).

Therefore

  H_n = b sum_{k>=0} (1+exp(-2a_k))/(a_k^2+b^2)
        - 1/2 Si(n*pi),
  a_k=2k+1/2.

The non-exponential part has the digamma closed form

 sum_{k>=0} 1/(a_k^2+b^2)
 = 1/4 * [psi(q+i c)-psi(q-i c)]/(2 i c),
 q=1/4, c=b/2.

The remaining exponential correction decays like exp(-4k), so rigorous tail
enclosure is elementary.  Thus all off-diagonal arch entries can be generated
without direct quadrature of H_n.

This is an analytic representation; a proof-grade implementation still needs
outward-rounded Si/digamma/exponential evaluation or equivalent series bounds.
"""
from __future__ import annotations
import mpmath as mp


def H_accel(n:int,dps:int=50,terms:int=20):
    assert n%2==1 and n>0
    with mp.workdps(dps):
        b=mp.mpf(n)*mp.pi/2
        q=mp.mpf(1)/4
        c=b/2
        base=(mp.digamma(q+1j*c)-mp.digamma(q-1j*c))/(8j*c)
        corr=mp.fsum([
            mp.e**(-2*(2*k+mp.mpf('0.5')))/((2*k+mp.mpf('0.5'))**2+b*b)
            for k in range(terms)
        ])
        return mp.re(b*(base+corr)-mp.si(n*mp.pi)/2)


if __name__=='__main__':
    for n in (1,3,19,153):
        print(n,mp.nstr(H_accel(n),30))
