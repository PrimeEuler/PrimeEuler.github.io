#!/usr/bin/env python3
"""Validate an FFT Toeplitz/Hankel matvec for the high remote raw operator.

On one parity lattice n_i=a+2i,

  (2/pi)(z_i n_j-n_i z_j)/(n_i^2-n_j^2)
   = (1/pi)[(z_i-z_j)/(n_i-n_j) - (z_i+z_j)/(n_i+n_j)].

The 1/(n_i-n_j) part is Toeplitz and the 1/(n_i+n_j) part is Hankel, so the
off-diagonal source-faithful Cauchy action can be evaluated by FFT
convolutions.  The parity pole is a rank-one update.

For high modes the arch diagonal is evaluated by a vectorized version of the
same Bernoulli recurrence used by arch_diag_series.  This script validates:
  * vectorized arch recurrence vs the quadrature endpoint producer;
  * full FFT matvec vs a dense exact-source block;
  * symmetry through random bilinear forms;
and benchmarks a larger matvec.

Diagnostic only: no outward rounding or infinite-tail theorem is promoted.
"""
from __future__ import annotations
import json,time
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.signal import fftconvolve

from suzuki_doubledouble_source_operator import arch_coefficients
from suzuki_endpoint_M3999_midpoint_effective_core import (
    cusp_diag,prime_diag,z_source_faithful,pole_vector,endpoint_data,offdiag,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"remote_fft_matvec_validation_result.json"
ARCH_TERMS=80

def arch_diag_vector(ns,terms=ARCH_TERMS):
    ns=np.asarray(ns,dtype=float)
    coeff=np.array([float(x) for x in arch_coefficients(terms)],dtype=float)
    k=ns*np.pi/2.0
    eps=np.where(ns.astype(int)%2==0,1.0,-1.0)
    C=np.zeros_like(ns)
    S=(1.0-eps)/k
    total=np.zeros_like(ns)
    for q in range(terms+1):
        Cnext=-(q+1)*S/k
        total += coeff[q]*(2*C-Cnext+S/k)
        Snext=-(2.0**(q+1))*eps/k+(q+1)*C/k
        C,S=Cnext,Snext
    return -total

def fft_offdiag(n,z,x):
    n=np.asarray(n,dtype=float);z=np.asarray(z,dtype=float);x=np.asarray(x,dtype=float)
    N=len(n);a=float(n[0])

    shifts=np.arange(-(N-1),N,dtype=float)
    kt=np.zeros(2*N-1,dtype=float)
    mask=shifts!=0
    kt[mask]=1.0/(2.0*shifts[mask])
    hm_x=fftconvolve(x,kt,mode="full")[N-1:N-1+N]
    hm_zx=fftconvolve(z*x,kt,mode="full")[N-1:N-1+N]

    s=np.arange(2*N-1,dtype=float)
    kh=1.0/(2.0*(a+s))
    hp_x=fftconvolve(x[::-1],kh,mode="full")[N-1:N-1+N]
    hp_zx=fftconvolve((z*x)[::-1],kh,mode="full")[N-1:N-1+N]
    hp_x-=x/(2*n)
    hp_zx-=z*x/(2*n)

    return (z*hm_x-hm_zx-z*hp_x-hp_zx)/np.pi

def fast_raw_matvec(modes,sector,x):
    modes=np.asarray(modes,dtype=int)
    z=z_source_faithful(modes)
    diag=cusp_diag(modes)+prime_diag(modes)+arch_diag_vector(modes)
    p,alpha=pole_vector(modes,sector)
    return fft_offdiag(modes,z,x)+diag*x+alpha*p*float(p@x)

def dense_raw_matrix(modes,sector):
    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    A=offdiag(modes,modes,z,z)
    np.fill_diagonal(A,diag)
    p,alpha=pole_vector(modes,sector)
    A+=alpha*np.outer(p,p)
    return (A+A.T)/2

def one_sector(sector):
    start=16001 if sector=="even-v" else 16002
    modes=np.arange(start,start+402,2,dtype=int)
    rng=np.random.default_rng(2401 if sector=="even-v" else 2402)
    x=rng.standard_normal(len(modes))
    y=rng.standard_normal(len(modes))

    aq=np.array([endpoint_data(np.array([n]),sign=-1,rho=0.0)[1][0]
                 -cusp_diag(np.array([n]))[0]-prime_diag(np.array([n]))[0]
                 for n in modes],dtype=float)
    av=arch_diag_vector(modes)
    arch_abs=float(np.max(np.abs(aq-av)))
    arch_rel=float(np.max(np.abs(aq-av)/np.maximum(np.abs(aq),1e-300)))

    A=dense_raw_matrix(modes,sector)
    yd=A@x
    yf=fast_raw_matvec(modes,sector,x)
    abs_err=float(np.max(np.abs(yd-yf)))
    rel_err=float(np.linalg.norm(yd-yf)/np.linalg.norm(yd))

    sym_dense=float(x@(A@y)-y@(A@x))
    fx=fast_raw_matvec(modes,sector,x)
    fy=fast_raw_matvec(modes,sector,y)
    sym_fft=float(x@fy-y@fx)

    return {
      "sector":sector,"start":int(modes[0]),"stop":int(modes[-1]),
      "dimension":len(modes),
      "arch_max_abs_error":arch_abs,
      "arch_max_relative_error":arch_rel,
      "matvec_max_abs_error":abs_err,
      "matvec_relative_l2_error":rel_err,
      "dense_symmetry_defect":sym_dense,
      "fft_symmetry_defect":sym_fft,
    }

def benchmark(sector,N=32768):
    start=16001 if sector=="even-v" else 16002
    modes=start+2*np.arange(N,dtype=int)
    rng=np.random.default_rng(99)
    x=rng.standard_normal(N)
    t=time.perf_counter()
    y=fast_raw_matvec(modes,sector,x)
    dt=time.perf_counter()-t
    return {
      "sector":sector,"dimension":N,"seconds":dt,
      "output_l2":float(np.linalg.norm(y)),
      "finite":bool(np.all(np.isfinite(y))),
    }

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    bench=[benchmark("even-v"),benchmark("odd-v")]
    for r in rows: print(json.dumps(r,indent=2))
    print("BENCH")
    for r in bench: print(json.dumps(r,indent=2))
    if max(r["matvec_relative_l2_error"] for r in rows)>2e-10:
        raise RuntimeError(("FFT matvec validation failed",rows))
    OUT.write_text(json.dumps({"rows":rows,"benchmark":bench},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
