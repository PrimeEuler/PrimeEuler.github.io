#!/usr/bin/env python3
"""Parity-correct exact recurrence for polynomial archimedean integrals on even modes.

For even n let b=n*pi/2.  Since sin(2b)=0 and cos(2b)=+1,

  I_p(b)=int_0^2 t^p cos(bt) dt,
  J_p(b)=int_0^2 t^p sin(bt) dt

obey

  I_0=0,
  J_0=0,
  I_p=-(p/b) J_{p-1},                         p>=1,
  J_p=-(2^p)/b + (p/b) I_{p-1},             p>=1.

If h_N(t)=sum_p a_p t^p, then

  H_n^N = sum_p a_p J_p,

and the source-faithful diagonal archimedean term is

  D_n^N = -sum_p a_p [2 I_p-I_{p+1}+J_p/b].

The off-diagonal archimedean contribution is reconstructed from H_n^N by the
same source-faithful displacement formula used in the finite-high matrix.

This helper only supplies the exact algebraic recurrence.  A proof-grade
outward replay must combine it with the certified h_N truncation bound and
outward enclosures for pi and finite arithmetic.
"""
from __future__ import annotations


def IJ_table_even(b,degree):
    I=[0]*(degree+2)
    J=[0]*(degree+2)
    I[0]=0
    J[0]=0
    for p in range(1,degree+2):
        I[p]=-(p/b)*J[p-1]
        J[p]=-(2**p)/b+(p/b)*I[p-1]
    return I,J


def HD_from_coeffs_even(coeffs,b):
    I,J=IJ_table_even(b,len(coeffs))
    H=sum(a*J[p] for p,a in enumerate(coeffs))
    D=-sum(a*(2*I[p]-I[p+1]+J[p]/b) for p,a in enumerate(coeffs))
    return H,D
