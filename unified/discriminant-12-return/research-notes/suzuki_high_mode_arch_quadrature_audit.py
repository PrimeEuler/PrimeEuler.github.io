#!/usr/bin/env python3
"""Audit high-mode archimedean scalar evaluation used by the source matrix.

The older high-precision finite-section producer evaluates

    A_n = int_0^2 h_arch(t) sin(k_n t) dt

and the archimedean diagonal with one mp.quad call over [0,2].
At high frequency this can lose the cancellation that controls the tiny
source-capacity scalar.

This audit compares three independent evaluations:
  1. exact convergent Taylor series + endpoint moment recurrences;
  2. direct high-precision quadrature split into n oscillation cells;
  3. the legacy one-shot mp.quad evaluation.

It also compares the exact displacement generator

    z_n = Si(n*pi) + 2*prime_sine_n + 2*A_n

against the digamma/exponential-correction formula used by the M3999
source-faithful architecture and the DD engine.

No theorem is promoted; this is a scalar provenance/accuracy audit.
"""
from __future__ import annotations

import argparse
import mpmath as mp

from suzuki_doubledouble_source_operator import arch_coefficients, arch_diag_series

QS=(2,3,4,5,7)


def weights():
    return (
        mp.log(2)/mp.sqrt(2),
        mp.log(3)/mp.sqrt(3),
        mp.log(2)/2,
        mp.log(5)/mp.sqrt(5),
        mp.log(7)/mp.sqrt(7),
    )


def h_arch(t,coeffs=None):
    t=mp.mpf(t)
    if t==0:
        return mp.mpf(1)/4
    # Tanh-sinh quadrature evaluates exponentially close to t=0.  The closed
    # form subtracts two ~1/(2t) quantities there and can lose all working
    # digits even in arbitrary precision.  Use the convergent Taylor series
    # near the removable singularity.
    if coeffs is not None and abs(t)<mp.mpf("0.25"):
        out=mp.mpf(0)
        for a in reversed(coeffs):
            out=out*t+a
        return out
    return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)


def prime_sine(n):
    return mp.fsum(
        w*mp.sin(mp.mpf(n)*mp.pi*mp.log(q)/2)
        for q,w in zip(QS,weights())
    )


def arch_sine_series(n, coeffs):
    k=mp.mpf(n)*mp.pi/2
    rmax=len(coeffs)-1
    eps=mp.mpf(-1 if n%2 else 1)
    C=[mp.mpf(0)]*(rmax+1)
    S=[mp.mpf(0)]*(rmax+1)
    C[0]=0
    S[0]=(1-eps)/k
    for r in range(1,rmax+1):
        C[r]=-mp.mpf(r)*S[r-1]/k
        S[r]=-(mp.mpf(2)**r)*eps/k+mp.mpf(r)*C[r-1]/k
    return mp.fsum(coeffs[r]*S[r] for r in range(rmax+1))


def segmented_quad(fun,n):
    # n half-period cells of length 2/n; endpoints include every sin zero.
    pts=[mp.mpf(2)*j/n for j in range(n+1)]
    return mp.fsum(mp.quad(fun,[pts[j],pts[j+1]]) for j in range(n))


def arch_diag_segmented(n,coeffs):
    k=mp.mpf(n)*mp.pi/2
    return segmented_quad(
        lambda t: -h_arch(t,coeffs)*((2-t)*mp.cos(k*t)+mp.sin(k*t)/k),
        n,
    )


def arch_sine_segmented(n,coeffs):
    k=mp.mpf(n)*mp.pi/2
    return segmented_quad(lambda t:h_arch(t,coeffs)*mp.sin(k*t),n)


def z_digamma(n, correction_terms=80):
    nn=mp.mpf(n)
    k=nn*mp.pi/2
    parity=mp.mpf(1 if n%2==0 else -1)
    corr=mp.fsum(
        mp.e**(-2*(2*j+mp.mpf("0.5")))/
        ((2*j+mp.mpf("0.5"))**2+k*k)
        for j in range(correction_terms)
    )
    return (
        2*prime_sine(n)
        + mp.im(mp.digamma(mp.mpf("0.25")+1j*nn*mp.pi/4))
        - parity*nn*mp.pi*corr
    )


def one(n,coeffs):
    k=mp.mpf(n)*mp.pi/2
    asi_series=arch_sine_series(n,coeffs)
    asi_seg=arch_sine_segmented(n,coeffs)
    asi_legacy=mp.quad(lambda t:h_arch(t)*mp.sin(k*t),[0,2])

    ad_series=arch_diag_series(n,coeffs)
    ad_seg=arch_diag_segmented(n,coeffs)
    ad_legacy=mp.quad(
        lambda t:-h_arch(t)*((2-t)*mp.cos(k*t)+mp.sin(k*t)/k),
        [0,2],
    )

    z_series=mp.si(n*mp.pi)+2*prime_sine(n)+2*asi_series
    z_seg=mp.si(n*mp.pi)+2*prime_sine(n)+2*asi_seg
    zd=z_digamma(n)

    print("\nmode",n)
    print("arch_sine series =",mp.nstr(asi_series,50))
    print("arch_sine segmented =",mp.nstr(asi_seg,50))
    print("arch_sine legacy =",mp.nstr(asi_legacy,50))
    print("  |series-seg| =",mp.nstr(abs(asi_series-asi_seg),20))
    print("  |legacy-seg| =",mp.nstr(abs(asi_legacy-asi_seg),20))
    print("arch_diag series =",mp.nstr(ad_series,50))
    print("arch_diag segmented =",mp.nstr(ad_seg,50))
    print("arch_diag legacy =",mp.nstr(ad_legacy,50))
    print("  |series-seg| =",mp.nstr(abs(ad_series-ad_seg),20))
    print("  |legacy-seg| =",mp.nstr(abs(ad_legacy-ad_seg),20))
    print("z series =",mp.nstr(z_series,50))
    print("z segmented =",mp.nstr(z_seg,50))
    print("z digamma =",mp.nstr(zd,50))
    print("  |series-digamma| =",mp.nstr(abs(z_series-zd),20))
    print("  |seg-digamma| =",mp.nstr(abs(z_seg-zd),20))

    return max(
        abs(asi_series-asi_seg),
        abs(ad_series-ad_seg),
        abs(z_series-zd),
    ), max(
        abs(asi_legacy-asi_seg),
        abs(ad_legacy-ad_seg),
    )


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--dps",type=int,default=100)
    args=p.parse_args()
    modes=(31,32,63,64,95,96,127,128,191,192)
    with mp.workdps(args.dps):
        coeffs=arch_coefficients(160)
        good=mp.mpf(0)
        legacy=mp.mpf(0)
        for n in modes:
            g,l=one(n,coeffs)
            good=max(good,g)
            legacy=max(legacy,l)
        print("\nmax series/segmented/digamma consistency =",mp.nstr(good,30))
        print("max legacy one-shot discrepancy =",mp.nstr(legacy,30))
        if good >= mp.mpf("1e-70"):
            raise RuntimeError(("independent high-mode formulas disagree",good))
        print("PASS: segmented quadrature confirms series/digamma high-mode scalars.")
        print("Legacy discrepancy is reported diagnostically above.")


if __name__=="__main__":
    main()
