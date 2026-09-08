#!/usr/bin/env python3
"""Exact recurrence for integrating the certified polynomial h_N.

For odd n let b=n*pi/2 and define

  I_p(b)=int_0^2 t^p cos(bt) dt,
  J_p(b)=int_0^2 t^p sin(bt) dt.

Because sin(2b)=0 and cos(2b)=-1,

  I_0=0,
  J_0=2/b,
  I_p=-(p/b) J_{p-1},                    p>=1,
  J_p=2^p/b + (p/b) I_{p-1},            p>=1.

If h_N(t)=sum_p a_p t^p, then

  H_n^N = sum_p a_p J_p,

and the diagonal arch entry is

  D_n^N = -sum_p a_p [2 I_p-I_{p+1}+J_p/b].

The off-diagonal entries are reconstructed from H_n^N via

  K_mn=-(4/pi)(n H_m-m H_n)/(n^2-m^2).

Thus after the explicit Taylor truncation of h, every finite archimedean entry
is a finite expression in rational Taylor coefficients and powers of b=n*pi/2.
No numerical quadrature or special-function evaluation is required.

The only analytic error is the uniform Taylor tail from
suzuki_arch_polynomial_certificate.py; outward rounding of pi and arithmetic
must be added in a proof-grade implementation.
"""
from __future__ import annotations


def IJ_table(b,degree):
    I=[0]*(degree+2)
    J=[0]*(degree+2)
    I[0]=0
    J[0]=2/b
    for p in range(1,degree+2):
        I[p]=-(p/b)*J[p-1]
        J[p]=(2**p)/b+(p/b)*I[p-1]
    return I,J


def HD_from_coeffs(coeffs,b):
    I,J=IJ_table(b,len(coeffs))
    H=sum(a*J[p] for p,a in enumerate(coeffs))
    D=-sum(a*(2*I[p]-I[p+1]+J[p]/b) for p,a in enumerate(coeffs))
    return H,D
